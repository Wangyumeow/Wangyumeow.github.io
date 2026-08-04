/* ==========================================================================
   Language Switcher — 中/英/日 三语切换
   ========================================================================== */

(function () {
  'use strict';

  const STORAGE_KEY = 'site-lang';
  const SUPPORTED = ['zh', 'en', 'ja'];
  const DEFAULT = 'zh';

  function detectBrowserLang() {
    const nav = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (nav.startsWith('zh')) return 'zh';
    if (nav.startsWith('ja')) return 'ja';
    return 'en';
  }

  function getLang() {
    // 1. URL parameter (?lang=xx) has highest priority
    const params = new URLSearchParams(window.location.search);
    const urlLang = params.get('lang');
    if (urlLang && SUPPORTED.includes(urlLang)) {
      localStorage.setItem(STORAGE_KEY, urlLang);
      return urlLang;
    }
    // 2. localStorage persisted choice
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored && SUPPORTED.includes(stored)) return stored;
    // 3. Browser language detection
    return detectBrowserLang();
  }

  function setLang(lang) {
    if (!SUPPORTED.includes(lang)) return;
    document.documentElement.setAttribute('data-lang', lang);
    localStorage.setItem(STORAGE_KEY, lang);
    // Update button active states
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });
    // Update URL without reload
    try {
      var url = new URL(window.location);
      url.searchParams.set('lang', lang);
      window.history.replaceState({}, '', url.toString());
    } catch (_) {}
  }

  // Bind click handlers
  function bindButtons() {
    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        setLang(this.getAttribute('data-lang'));
      });
    });
  }

  // Initialize on DOM ready
  function init() {
    var lang = getLang();
    setLang(lang);
    bindButtons();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
