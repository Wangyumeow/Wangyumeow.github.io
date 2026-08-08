---
layout: single
title: "About"
permalink: /about/
author_profile: false
---

{% include base_path %}

<!-- Biography -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_bio_label }}</span>
    {% endfor %}
  </h2>
  {% for lang in "zh,en,ja" | split: "," %}
  <div class="lang-{{ lang }} about-section__bio">
    {{ site.data.languages[lang].about_bio | markdownify }}
  </div>
  {% endfor %}
</section>

<!-- Education -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_education_label }}</span>
    {% endfor %}
  </h2>
  <div class="education-list">
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      {% for item in site.data.languages[lang].about_education_items %}
      <div class="education-item">
        <span class="education-item__period">{{ item.period }}</span>
        <div class="education-item__body">
          <span class="education-item__degree">{{ item.degree }}</span>
          <span class="education-item__institution">{{ item.institution }}</span>
          <p class="education-item__detail">{{ item.detail }}</p>
        </div>
      </div>
      {% endfor %}
    </div>
    {% endfor %}
  </div>
</section>

<!-- Research Interests -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_research_interests_label }}</span>
    {% endfor %}
  </h2>
  <ul class="interest-list">
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      {% for item in site.data.languages[lang].about_interest_items %}
      <li class="interest-item">
        <strong>{{ item.name }}</strong> — {{ item.desc }}
      </li>
      {% endfor %}
    </div>
    {% endfor %}
  </ul>
</section>

<!-- Interdisciplinary Experience -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_interdisciplinary_label }}</span>
    {% endfor %}
  </h2>
  {% for lang in "zh,en,ja" | split: "," %}
  <div class="lang-{{ lang }} about-section__bio">
    {{ site.data.languages[lang].about_interdisciplinary | markdownify }}
  </div>
  {% endfor %}
</section>

<!-- Languages -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_languages_label }}</span>
    {% endfor %}
  </h2>
  <div class="skills-grid">
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      {% for item in site.data.languages[lang].about_languages_items %}
      <div class="skill-chip">
        <span class="skill-chip__name">{{ item.name }}</span>
        <span class="skill-chip__level">{{ item.level }}</span>
      </div>
      {% endfor %}
    </div>
    {% endfor %}
  </div>
</section>

<!-- Technical Skills -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].about_skills_label }}</span>
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

<!-- Contact -->
<section class="about-section" data-reveal>
  <h2 class="about-section__title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].contact_title }}</span>
    {% endfor %}
  </h2>
  <div class="contact-info">
    <p>
      <strong>
        {% for lang in "zh,en,ja" | split: "," %}
        <span class="lang-{{ lang }}">{{ site.data.languages[lang].contact_email_label }}</span>
        {% endfor %}:
      </strong>
      <a href="mailto:Jasonwong_011003@163.com">Jasonwong_011003@163.com</a>
    </p>
    <p>
      <strong>
        {% for lang in "zh,en,ja" | split: "," %}
        <span class="lang-{{ lang }}">{{ site.data.languages[lang].contact_location_label }}</span>
        {% endfor %}:
      </strong>
      {% for lang in "zh,en,ja" | split: "," %}
      <span class="lang-{{ lang }}">{{ site.data.languages[lang].contact_location_value }}</span>
      {% endfor %}
    </p>
  </div>
</section>
