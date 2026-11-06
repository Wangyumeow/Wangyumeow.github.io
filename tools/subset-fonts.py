#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subset-fonts.py — 按站点实际用字裁剪 Web 字体

背景：assets/fonts/ 下的 8 个 WOFF2 原为全字符集（约 17MB，其中游明朝单字重约 5MB），
首次访问需全部下载，国内访问 GitHub Pages 时极为缓慢。

本脚本收集站点全部可见字符（源码文本文件 + 线上渲染 HTML），
用 fonttools 将字体裁剪到该字符集，输出同名 WOFF2 覆盖回原目录。

依赖：
    pip install fonttools brotli zopfli

用法：
    python3 tools/subset-fonts.py            # 收集用字 + 裁剪 + 覆盖
    python3 tools/subset-fonts.py --collect  # 只更新 tools/charset.txt

新增内容后（如发博客）请重跑本脚本，否则新增汉字将回退到系统字体渲染。
"""
import glob
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARSET_PATH = os.path.join(REPO, 'tools', 'charset.txt')
FONTS = [
    'FZXiaoBiaoSong', 'FZXinBaoSong',
    'Garamond-Regular', 'Garamond-Bold', 'Garamond-Italic',
    'YuMincho-Regular', 'YuMincho-Demibold', 'YuMincho-Light',
]
LIVE_PAGES = [
    '/', '/about/', '/research/', '/publications/', '/cv/', '/blog/',
    '/publication/2026-03-01-japan-rightward-media-distrust',
    '/publication/2025-06-01-transnational-city-networks-climate',
    '/publication/2026-05-28-japan-defense-spending',
]
# 兜底字符：ASCII 可打印区 + 常用中西文标点（避免标点回退）
BASE_CHARS = (
    ''.join(chr(c) for c in range(0x20, 0x7F))
    + '，。：；、？！“”‘’（）《》—…·～￥「」『』【】〈〉〔〕％℃°′″'
    + '©®™§¶†‡•…–—‘’“”‹›«»×÷±≈≠≤≥∞µΩπαβγδ'
)


def collect_charset():
    chars = set(BASE_CHARS)
    n = 0
    for ext in ('md', 'yml', 'yaml', 'html', 'json', 'txt', 'csv', 'xml', 'svg'):
        for fp in glob.glob(os.path.join(REPO, '**', f'*.{ext}'), recursive=True):
            if os.sep + '.git' + os.sep in fp:
                continue
            try:
                with open(fp, encoding='utf-8', errors='ignore') as f:
                    chars.update(f.read())
                n += 1
            except OSError:
                pass
    for path in LIVE_PAGES:
        try:
            out = subprocess.run(
                ['curl', '-s', '-m', '30', 'https://wangyumeow.github.io' + path],
                capture_output=True, text=True, check=False)
            if out.returncode == 0:
                chars.update(out.stdout)
        except OSError:
            pass
    chars = {c for c in chars if ord(c) >= 0x20 or c in ' 　'}
    text = ''.join(sorted(chars))
    with open(CHARSET_PATH, 'w', encoding='utf-8') as f:
        f.write(text)
    cjk = sum(1 for c in chars if ord(c) >= 0x3000)
    print(f'charset: {len(chars)} unique chars ({cjk} CJK-range) from {n} files + {len(LIVE_PAGES)} live pages')
    return text


def subset_all():
    with open(CHARSET_PATH, encoding='utf-8') as f:
        text = f.read()
    total_before = total_after = 0
    for name in FONTS:
        src = os.path.join(REPO, 'assets', 'fonts', f'{name}.woff2')
        tmp = f'/tmp/subset_{name}.woff2'
        before = os.path.getsize(src)
        subprocess.run([
            'pyftsubset', src,
            '--text-file=' + CHARSET_PATH,
            '--flavor=woff2',
            '--output-file=' + tmp,
            '--layout-features=*',
            '--name-IDs=*', '--name-legacy',
            '--notdef-outline', '--no-hinting',
        ], check=True)
        after = os.path.getsize(tmp)
        # 校验字形覆盖
        from fontTools.ttLib import TTFont
        cmap = TTFont(tmp).getBestCmap()
        missing = [c for c in text if ord(c) not in cmap and ord(c) >= 0x20 and not c.isspace()]
        j_missing = [c for c in missing if 0x3040 <= ord(c) <= 0x30FF]
        if j_missing:
            print(f'  [warn] {name} 缺假名: {"".join(j_missing)}')
        os.replace(tmp, src)
        total_before += before
        total_after += after
        print(f'{name:22s} {before // 1024:>6}KB -> {after // 1024:>5}KB')
    print(f'TOTAL {total_before // 1024 // 1024}MB -> {total_after // 1024}KB')


if __name__ == '__main__':
    if '--collect' in sys.argv:
        collect_charset()
    else:
        if not os.path.exists(CHARSET_PATH):
            collect_charset()
        subset_all()
