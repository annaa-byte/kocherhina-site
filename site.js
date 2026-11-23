(function () {
  // Scale the 1440px desktop stage to the window width (phones use the stacked layout from CSS).
  function fit() {
    var w = document.documentElement.clientWidth;
    var k = w >= 760 ? Math.min(1, w / 1440) : 1;
    document.documentElement.style.setProperty('--k', k);
  }
  fit();
  window.addEventListener('resize', fit);

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
