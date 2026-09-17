// English Outside the Box — small, dependency-free behaviours
(function () {
  // mobile nav
  var t = document.querySelector('.nav-toggle'), nav = document.getElementById('nav');
  if (t && nav) {
    t.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', String(!open));
      t.setAttribute('aria-expanded', String(!open));
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { nav.setAttribute('data-open', 'false'); t.setAttribute('aria-expanded', 'false'); } });
  }

  // one reveal grammar: fade-up on entry
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }
  setTimeout(function () { els.forEach(function (el) { var r = el.getBoundingClientRect(); if (r.top < innerHeight) el.classList.add('in'); }); }, 300);

  // blog category filter
  var chips = document.getElementById('cat-filter');
  if (chips) {
    var cards = document.querySelectorAll('.post-card'), blocks = document.querySelectorAll('.year-block'), empty = document.getElementById('filter-empty');
    function apply(cat) {
      var shown = 0;
      cards.forEach(function (c) {
        var ok = cat === 'all' || (' ' + c.getAttribute('data-cats') + ' ').indexOf(' ' + cat + ' ') > -1;
        c.hidden = !ok; if (ok) shown++;
      });
      blocks.forEach(function (b) { b.hidden = !b.querySelector('.post-card:not([hidden])'); });
      if (empty) empty.hidden = shown > 0;
      chips.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-cat') === cat)); });
    }
    chips.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var cat = b.getAttribute('data-cat'); apply(cat);
      if (history.replaceState) history.replaceState(null, '', cat === 'all' ? '/blog/' : '/blog/#' + cat);
    });
    var h = location.hash.replace('#', '');
    if (h && chips.querySelector('[data-cat="' + h + '"]')) apply(h);
  }

  // contact form → mailto with a readable body
  var f = document.querySelector('.contact-form');
  if (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var g = function (n) { return (f.querySelector('[name=' + n + ']') || {}).value || ''; };
      var subject = 'Website message: ' + g('help') + ' — ' + g('name');
      var body = 'Name: ' + g('name') + '\nEmail: ' + g('email') + '\nHow can I help: ' + g('help') + '\n\n' + g('message');
      location.href = 'mailto:' + f.getAttribute('data-mail') + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
