---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
author_profile: false
---

{% include base_path %}

<!-- Download button -->
<div class="cv-download" data-reveal>
  <a href="{{ base_path }}/files/cv.pdf" class="btn-cv" target="_blank">
    <i class="fa-solid fa-file-pdf"></i>
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_download_label }}</span>
    {% endfor %}
  </a>
</div>

<!-- Education -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_education_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      {% for item in site.data.languages[lang].about_education_items %}
      <div class="cv-entry">
        <div class="cv-entry__period">{{ item.period }}</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">{{ item.degree }}</div>
          <div class="cv-entry__org">{{ item.institution }}</div>
          <div class="cv-entry__detail">{{ item.detail }}</div>
        </div>
      </div>
      {% endfor %}
    </div>
    {% endfor %}
  </div>
</section>

<!-- Research Experience -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_research_experience_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    <div class="lang-zh">
      <div class="cv-entry">
        <div class="cv-entry__period">2026.03 – 2026.07</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">科研与党务助理</div>
          <div class="cv-entry__org">复旦大学国际关系与公共事务学院</div>
          <div class="cv-entry__detail">协助科研服务工作，负责项目管理、文案写作、会议记录整理；协助学院第四次党代会会务支持；协助国家社科基金项目申报和审核。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2025.06 – 至今</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">视频部记者/策划</div>
          <div class="cv-entry__org">复旦大学党委宣传部融媒体中心</div>
          <div class="cv-entry__detail">策划复旦学生官方博客"旦问研究所"，已制作3-5期；参与广播台与融媒体中心共创项目"旦夕之声"。</div>
        </div>
      </div>
    </div>
    <div class="lang-en">
      <div class="cv-entry">
        <div class="cv-entry__period">2026.03 – 2026.07</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Research & Party Affairs Assistant</div>
          <div class="cv-entry__org">SIRPA, Fudan University</div>
          <div class="cv-entry__detail">Assisted with research services, project management, copywriting, and meeting minutes. Supported the 4th Party Congress of SIRPA. Assisted with National Social Science Fund applications.</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2025.06 – Present</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Video Journalist / Producer</div>
          <div class="cv-entry__org">Converged Media Center, Fudan University</div>
          <div class="cv-entry__detail">Planned and produced the "Danwen Institute" student blog series. Participated in the "Danxi Voice" collaborative project.</div>
        </div>
      </div>
    </div>
    <div class="lang-ja">
      <div class="cv-entry">
        <div class="cv-entry__period">2026年3月 – 2026年7月</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">研究・党務アシスタント</div>
          <div class="cv-entry__org">復旦大学国際関係・公共事務学院</div>
          <div class="cv-entry__detail">研究サービス、プロジェクト管理、文書作成、議事録整理を補助。学院第4回党代表大会の運営支援。国家社会科学基金プロジェクト申請・審査の補助。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2025年6月 – 現在</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">映像部門記者/プロデューサー</div>
          <div class="cv-entry__org">復旦大学コンバージドメディアセンター</div>
          <div class="cv-entry__detail">学生公式ブログ「旦問研究所」の企画・制作（3～5エピソード）。放送局との共同プロジェクト「旦夕之声」に参加。</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Work & Internship Experience (streamlined) -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_work_experience_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    <div class="lang-zh">
      <div class="cv-entry">
        <div class="cv-entry__period">2025.02 – 2025.06</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">人力资源实习生</div>
          <div class="cv-entry__org">哔哩哔哩 (Bilibili)</div>
          <div class="cv-entry__detail">负责2026届暑期实习生项目6个岗位共20个HC招聘，转正率100%；共计约面550+。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024.07 – 2024.10</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">组织效能实习生</div>
          <div class="cv-entry__org">华住集团</div>
          <div class="cv-entry__detail">新员工全局融入项目，覆盖全国14个品牌近万家门店。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024.11</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">商贸对接</div>
          <div class="cv-entry__org">香港贸易发展局 (进博会)</div>
          <div class="cv-entry__detail">累计对接40+人次，服务时长60小时。</div>
        </div>
      </div>
    </div>
    <div class="lang-en">
      <div class="cv-entry">
        <div class="cv-entry__period">2025.02 – 2025.06</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">HR Intern</div>
          <div class="cv-entry__org">Bilibili</div>
          <div class="cv-entry__detail">2026 Summer Intern Program: 6 roles, 20 HC, 100% conversion rate. 550+ interviews scheduled.</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024.07 – 2024.10</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Organizational Effectiveness Intern</div>
          <div class="cv-entry__org">Huazhu Group</div>
          <div class="cv-entry__detail">New employee onboarding program across 14 brands and nearly 10,000 stores.</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024.11</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Business Liaison</div>
          <div class="cv-entry__org">HKTDC (CIIE)</div>
          <div class="cv-entry__detail">Assisted 40+ clients, 60 service hours at the 8th CIIE Hong Kong Pavilion.</div>
        </div>
      </div>
    </div>
    <div class="lang-ja">
      <div class="cv-entry">
        <div class="cv-entry__period">2025年2月 – 2025年6月</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">人事インターン</div>
          <div class="cv-entry__org">Bilibili</div>
          <div class="cv-entry__detail">2026年度サマーインターン：6職種・20名採用、内定承諾率100%。累計550件以上の面接調整。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024年7月 – 2024年10月</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">組織効率化インターン</div>
          <div class="cv-entry__org">華住グループ</div>
          <div class="cv-entry__detail">新入社員グローバル統合プログラム、全国14ブランド・約10,000店舗をカバー。</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2024年11月</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">商務連絡担当</div>
          <div class="cv-entry__org">香港貿易発展局（進博会）</div>
          <div class="cv-entry__detail">第8回進博会香港パビリオンにて延べ40名以上の接客、60時間のサービス提供。</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Publications -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_publications_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
    {% for post in sorted_pubs %}
    <div class="cv-entry cv-entry--pub">
      <div class="cv-entry__period">{{ post.date | date: "%Y.%m" }}</div>
      <div class="cv-entry__body">
        <div class="cv-entry__title">{{ post.title | markdownify | remove: "<p>" | remove: "</p>" | strip }}</div>
        <div class="cv-entry__org">{{ post.venue | markdownify | remove: "<p>" | remove: "</p>" | strip }}</div>
      </div>
    </div>
    {% endfor %}
  </div>
</section>

<!-- Awards -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_awards_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    <div class="lang-zh">
      <div class="cv-entry">
        <div class="cv-entry__period">2026</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">第二届京津冀日本学研究硕博论坛 三等奖</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2021–2025</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">复旦大学优秀学生二等奖学金×1、三等奖学金×2</div>
          <div class="cv-entry__detail">复旦大学优秀学生、优秀毕业生</div>
        </div>
      </div>
    </div>
    <div class="lang-en">
      <div class="cv-entry">
        <div class="cv-entry__period">2026</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Third Prize, 2nd Beijing-Tianjin-Hebei Graduate Forum on Japanese Studies</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2021–2025</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">Second-Class Scholarship x1, Third-Class Scholarship x2</div>
          <div class="cv-entry__detail">Outstanding Student and Outstanding Graduate of Fudan University</div>
        </div>
      </div>
    </div>
    <div class="lang-ja">
      <div class="cv-entry">
        <div class="cv-entry__period">2026</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">第2回京津冀日本学研究大学院生フォーラム 三等賞</div>
        </div>
      </div>
      <div class="cv-entry">
        <div class="cv-entry__period">2021–2025</div>
        <div class="cv-entry__body">
          <div class="cv-entry__title">優秀学生二等奨学金×1、三等奨学金×2</div>
          <div class="cv-entry__detail">復旦大学優秀学生、優秀卒業生</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Campus Activities -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_campus_activities_label }}</span>
    {% endfor %}
  </h2>
  <div class="cv-entries">
    <div class="lang-zh">
      <div class="cv-entry"><div class="cv-entry__period">2026.01 – 至今</div><div class="cv-entry__body"><div class="cv-entry__title">复旦大学声音剧场 — 宣传负责人兼前台导演</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2023.09 – 2024.08</div><div class="cv-entry__body"><div class="cv-entry__title">复旦大学广播台 — 副台长兼团书记</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2022.09 – 2022.12</div><div class="cv-entry__body"><div class="cv-entry__title">复旦大学演讲与口才协会 — 副理事长</div></div></div>
    </div>
    <div class="lang-en">
      <div class="cv-entry"><div class="cv-entry__period">2026.01 – Present</div><div class="cv-entry__body"><div class="cv-entry__title">Fudan Sound Theater — PR Lead & Front-of-House Director</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2023.09 – 2024.08</div><div class="cv-entry__body"><div class="cv-entry__title">Fudan Broadcasting Station — Deputy Director & Youth League Secretary</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2022.09 – 2022.12</div><div class="cv-entry__body"><div class="cv-entry__title">Fudan Speech & Eloquence Association — Vice President</div></div></div>
    </div>
    <div class="lang-ja">
      <div class="cv-entry"><div class="cv-entry__period">2026年1月 – 現在</div><div class="cv-entry__body"><div class="cv-entry__title">復旦大学サウンドシアター — 広報責任者兼フロントディレクター</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2023年9月 – 2024年8月</div><div class="cv-entry__body"><div class="cv-entry__title">復旦大学放送局 — 副局長兼団書記</div></div></div>
      <div class="cv-entry"><div class="cv-entry__period">2022年9月 – 2022年12月</div><div class="cv-entry__body"><div class="cv-entry__title">復旦大学スピーチ・ディベート協会 — 副理事長</div></div></div>
    </div>
  </div>
</section>

<!-- Skills -->
<section class="cv-section" data-reveal>
  <h2 class="cv-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].cv_skills_label }}</span>
    {% endfor %}
  </h2>
  <ul class="skills-list">
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      {% for skill in site.data.languages[lang].about_skills_items %}
      <li>{{ skill }}</li>
      {% endfor %}
    </div>
    {% endfor %}
  </ul>
</section>
