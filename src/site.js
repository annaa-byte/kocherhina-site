(function () {
  // Scale the 1440px desktop stage to the window width (phones use the stacked layout from CSS).
  function fit() {
    var w = document.documentElement.clientWidth;
    var k = w >= 760 ? Math.min(1, w / 1440) : 1;
    document.documentElement.style.setProperty('--k', k);
  }
  fit();
  window.addEventListener('resize', fit);

  // ---- motion: reveal on scroll, hero lines, header shadow ----
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hdr = document.querySelector('.hdr');
  addEventListener('scroll', function () { if (hdr) hdr.classList.toggle('scrolled', scrollY > 10); }, { passive: true });
  var first = document.querySelector('main > section');
  if (first && !reduce) {
    first.querySelectorAll('.t.big').forEach(function (el, i) { el.classList.add('hero-line'); el.style.setProperty('--d', (0.15 + i * 0.18) + 's'); });
  }
  var heroImg = first && first.querySelector('img.keep');
  if (heroImg && !reduce) heroImg.classList.add('float');
  if ('IntersectionObserver' in window && !reduce) {
    var targets = [];
    document.querySelectorAll('main > section').forEach(function (sec, si) {
      var items = sec.querySelectorAll('.stage > .a:not(.hero-line):not(.shape):not(.line):not(.srow), .srow > .a, .tcol > .tcard, .sp .wrap > *, .sp-weeks > *, .sp-want > li, .sp-ts > *, .sp-band, .ed-facts dl > div, .ed-hook .wrap > *, .ed-text > p, .ed-art, .ed-promise p, .ed-for-art, .ed-h, .ed-list li, .ed-grid li, .ed-acc details, .ed-steps li, .ed-car, .ed-author, .ed-sign, .ed-close, .ed-card, .ab-tx > *, .ab-ph, .ab2 p, .hm-portrait, .hm-about-tx > *, .hm-mission, .hm-h, .hm-spheres li, .hm-cta-tx > *, .hm-fl');
      var n = 0;
      items.forEach(function (el) {
        if (el.classList.contains('float')) return;
        el.classList.add('rv');
        el.style.setProperty('--d', Math.min(n++ * 0.07, 0.5) + 's');
        targets.push(el);
      });
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (t) { io.observe(t); });
  }

  // Testimonial carousel on season pages
  document.querySelectorAll('[data-car]').forEach(function (car) {
    var sl = car.querySelectorAll('.ed-slide'), cnt = car.querySelector('.ed-cnt b'), i = 0, timer;
    function go(d) {
      sl[i].classList.remove('on'); i = (i + d + sl.length) % sl.length; sl[i].classList.add('on');
      cnt.textContent = (i < 9 ? '0' : '') + (i + 1);
    }
    function auto() { clearInterval(timer); if (!reduce) timer = setInterval(function () { go(1); }, 9000); }
    car.querySelector('[data-prev]').addEventListener('click', function () { go(-1); auto(); });
    car.querySelector('[data-next]').addEventListener('click', function () { go(1); auto(); });
    auto();
  });

  // Close the mobile menu after a tap on a link.
  document.querySelectorAll('.hdr nav a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
  });

  // ---- "Заявка на повтор" form ----
  // Where submissions go: set FORM_ENDPOINT to a Formspree / Google Apps Script URL.
  // While it is empty, the form opens Telegram of the manager with the application text copied.
  var FORM_ENDPOINT = '';
  var MANAGER_TG = 'https://t.me/pnm_a';

  var modal = document.getElementById('apply');
  var form = document.getElementById('apply-form');
  function open(season) {
    if (season) form.season.value = season;
    document.getElementById('apply-form-wrap').hidden = false;
    document.getElementById('apply-done').hidden = true;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    setTimeout(function () { form.name.focus(); }, 50);
  }
  function close() { modal.classList.remove('open'); modal.setAttribute('aria-hidden', 'true'); }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-apply]');
    if (t) { e.preventDefault(); open(t.getAttribute('data-apply')); return; }
    if (e.target === modal || e.target.closest('[data-close]')) close();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  if (location.hash === '#zayavka') open();

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var err = form.querySelector('.ferr');
    if (!form.name.value.trim() || !form.contact.value.trim() || !form.agree.checked) { err.hidden = false; return; }
    err.hidden = true;
    var seasonText = form.season.options[form.season.selectedIndex].text;
    var msg = 'Заявка на повтор сезону\nІм\'я: ' + form.name.value.trim() + '\nКонтакт: ' + form.contact.value.trim() +
      '\nСезон: ' + seasonText + (form.note.value.trim() ? '\nКоментар: ' + form.note.value.trim() : '');
    var done = document.getElementById('apply-done-t');
    function finish(text) {
      document.getElementById('apply-form-wrap').hidden = true;
      document.getElementById('apply-done').hidden = false;
      done.textContent = text;
      form.reset();
    }
    if (FORM_ENDPOINT) {
      fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
        .then(function () { finish('Заявку отримано. Менеджер напише вам, щойно відкриється набір.'); })
        .catch(function () { finish('Не вдалося надіслати. Напишіть, будь ласка, менеджеру в Telegram: @pnm_a'); });
    } else {
      if (navigator.clipboard) navigator.clipboard.writeText(msg).catch(function () {});
      window.open(MANAGER_TG, '_blank', 'noopener');
      finish('Текст заявки скопійовано. Надішліть його менеджеру в Telegram, що відкрився: @pnm_a');
    }
  });
})();
