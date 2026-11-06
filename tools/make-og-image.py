#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-og-image.py — 生成社交分享卡片 images/og-image.png (1200x630)

用站点自有子集字体绘制，保持与网页一致的视觉（藏青/纸色/金）。
供 og:image 与 twitter:image 使用。

依赖：
    pip install pillow fonttools brotli

用法：
    python3 tools/make-og-image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(REPO, 'assets', 'fonts')
OUT = os.path.join(REPO, 'images', 'og-image.png')

NAVY = (26, 58, 92)
PAPER = (250, 248, 245)
GOLD = (184, 134, 11)
MUTED = (90, 98, 110)

W, H = 1200, 630
M = 90  # 左边距


def main():
    img = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(img)

    f_name = ImageFont.truetype(os.path.join(FD, 'FZXiaoBiaoSong.woff2'), 96)
    f_en = ImageFont.truetype(os.path.join(FD, 'Garamond-Regular.woff2'), 44)
    f_uni = ImageFont.truetype(os.path.join(FD, 'Garamond-Regular.woff2'), 34)
    f_areas = ImageFont.truetype(os.path.join(FD, 'Garamond-Italic.woff2'), 30)
    f_url = ImageFont.truetype(os.path.join(FD, 'Garamond-Regular.woff2'), 26)

    d.rectangle([0, 0, W, 10], fill=GOLD)
    d.text((M, 118), "Yu'ao Wang 王宇傲", font=f_name, fill=NAVY)
    d.rectangle([M, 268, M + 150, 274], fill=GOLD)
    d.text((M, 310), "International Relations Researcher", font=f_en, fill=NAVY)
    d.text((M, 380), "M.A. in International Politics & International Communication",
           font=f_uni, fill=MUTED)
    d.text((M, 428), "Fudan University", font=f_uni, fill=MUTED)
    d.text((M, 520), "Japan Politics  ·  Global Governance  ·  Political Communication",
           font=f_areas, fill=GOLD)
    d.text((W - 330, H - 64), "wangyumeow.github.io", font=f_url, fill=MUTED)

    img.save(OUT, optimize=True)
    print(f'written: {OUT} ({os.path.getsize(OUT) // 1024}KB)')


if __name__ == '__main__':
    main()
