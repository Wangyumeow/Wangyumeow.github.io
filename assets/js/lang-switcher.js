/* ==========================================================================
   Language Switcher — 中/英/日 三语切换
   Critical init is inlined in <head>; this file handles buttons + sync.
   ========================================================================== */

(function () {
  'use strict';

  const STORAGE_KEY = 'site-lang';
  const SUPPORTED = ['zh', 'en', 'ja'];

  function setLang(lang) {
    if (!SUPPORTED.includes(lang)) return;
    document.documentElement.setAttribute('data-lang', lang);
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {}
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
  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      setLang(this.getAttribute('data-lang'));
    });
  });

  // Sync button state on load (in case inline script already set data-lang)
  var current = document.documentElement.getAttribute('data-lang') || 'zh';
  setLang(current);
})();
