---
layout: single
title: "Research"
permalink: /research/
author_profile: false
---

{% include base_path %}

<!-- Intro -->
<section class="research-intro" data-reveal>
  {% for lang in "zh,en,ja" | split: "," %}
  <div class="lang-{{ lang }}">
    {{ site.data.languages[lang].research_page_intro | markdownify }}
  </div>
  {% endfor %}
</section>

<!-- Research Areas -->
{% for area in site.data.research.areas %}
<section class="research-area" id="area-{{ area.id }}" data-reveal>
  <div class="research-area__header">
    <span class="research-area__number">{{ area.id }}</span>
    {% if area.icon %}
    <i class="research-area__icon {{ area.icon }}"></i>
    {% endif %}
    {% for lang in "zh,en,ja" | split: "," %}
    <div class="lang-{{ lang }}">
      <h2 class="research-area__title">{{ area[lang].title }}</h2>
      <span class="research-area__subtitle">{{ area[lang].subtitle }}</span>
    </div>
    {% endfor %}
  </div>

  {% for lang in "zh,en,ja" | split: "," %}
  <div class="lang-{{ lang }} research-area__content">
    <p class="research-area__desc">{{ area[lang].description }}</p>

    {% if area[lang].questions %}
    <h3 class="research-area__label">{{ site.data.languages[lang].research_questions_label }}</h3>
    <ul class="research-area__questions">
      {% for question in area[lang].questions %}
      <li>{{ question }}</li>
      {% endfor %}
    </ul>
    {% endif %}

    {% if area[lang].current_projects %}
    <h3 class="research-area__label">{{ site.data.languages[lang].research_current_projects_label }}</h3>
    <p>{{ area[lang].current_projects }}</p>
    {% endif %}

    {% if area[lang].future %}
    <h3 class="research-area__label">{{ site.data.languages[lang].research_future_label }}</h3>
    <p>{{ area[lang].future }}</p>
    {% endif %}
  </div>
  {% endfor %}
</section>
{% endfor %}

<!-- Related Publications -->
<section class="research-publications" data-reveal>
  <h2 class="section-title">
    {% for lang in "zh,en,ja" | split: "," %}
    <span class="lang-{{ lang }}">{{ site.data.languages[lang].research_publications_label }}</span>
    {% endfor %}
  </h2>
  <div class="pub-list">
    {% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
    {% for post in sorted_pubs %}
      {% include publication_entry.html %}
    {% endfor %}
  </div>
</section>
