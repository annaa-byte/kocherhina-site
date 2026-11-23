# kocherhina.com — копія сайту з виправленнями

Статичний сайт: `index.html`, `svoboda-buty-zhinkoyu.html`, `about.html`, `season-1..5.html`, `oferta.html`, `privacy.html`.
Сторінки генеруються скриптом `src/build.py` (`python3 src/build.py .`). Тексти сезонів — у `src/seasons.json`.

- Картинки поки беруться з Weblium; при публікації GitHub Actions копіює їх у `img/` (`scripts/localize_images.py`).
- Форма «Заявка на повтор»: у `site.js` змінна `FORM_ENDPOINT`. Поки вона порожня, заявка копіюється і відкривається Telegram менеджера @pnm_a.
