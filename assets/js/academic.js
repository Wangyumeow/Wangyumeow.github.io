/* ==========================================================================
   academic.js
   Scroll reveal (IntersectionObserver), smooth scroll, mobile nav toggle.
   ========================================================================== */

(function () {
  'use strict';

  // ---- Scroll Reveal via IntersectionObserver ----
  function initScrollReveal() {
    var revealEls = document.querySelectorAll('[data-reveal]');
    if (!revealEls.length) return;

    // Fallback: if IntersectionObserver not available, reveal everything
    if (!('IntersectionObserver' in window)) {
      revealEls.forEach(function (el) {
        el.classList.add('is-revealed');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          // Stagger reveal if siblings have data-reveal too
          var siblings = entry.target.parentElement
            ? entry.target.parentElement.querySelectorAll('[data-reveal]')
            : [];
          var index = Array.prototype.indexOf.call(siblings, entry.target);
          var delay = index > 0 ? Math.min(index * 80, 400) : 0;

          setTimeout(function () {
            entry.target.classList.add('is-revealed');
          }, delay);

          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -60px 0px'
    });

    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  }

  // ---- Mobile Nav Toggle ----
  function initMobileNav() {
    var navButton = document.querySelector('.greedy-nav > button');
    var greedyNav = document.querySelector('.greedy-nav');
    if (!navButton || !greedyNav) return;

    navButton.addEventListener('click', function () {
      greedyNav.classList.toggle('active');
    });

    // Close menu when clicking a link
    var navLinks = greedyNav.querySelectorAll('.visible-links a');
    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        greedyNav.classList.remove('active');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function (e) {
      if (!greedyNav.contains(e.target) && greedyNav.classList.contains('active')) {
        greedyNav.classList.remove('active');
      }
    });
  }

  // ---- Smooth Anchor Scroll (for in-page links) ----
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var targetId = this.getAttribute('href');
        if (targetId === '#' || targetId.length < 2) return;
        var target = document.querySelector(targetId);
        if (!target) return;

        e.preventDefault();
        var headerHeight = 60;
        var targetPos = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
        window.scrollTo({
          top: targetPos,
          behavior: 'smooth'
        });
      });
    });
  }

  // ---- Init ----
  function init() {
    initScrollReveal();
    initMobileNav();
    initSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
