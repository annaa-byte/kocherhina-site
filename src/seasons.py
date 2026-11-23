import json, os, re
from lib import *
from salon import hero, SEASONS as CARDS
from home import TESTI

D = json.load(open(os.path.join(os.path.dirname(__file__), "seasons.json")))
SHIP = "1/69cf7a9deecd0ca2708941e6_optimized.webp"
QUOTE = "2/694819b3364911d845de9420_optimized.webp"
ELLIPSE = "1/69cf83efeecd0ca2708963b1_optimized.webp"
JAG = "1/69cf9218eecd0ca27089a59b_optimized.webp"
JAGF = "1/69cf9218eecd0ca27089a59b_optimized_1045_flip.webp"

TITLES = {1: ("СТОСУНКИ", "З СОБОЮ"), 2: ("POWER", "COUPLE"), 3: ("ГРОШІ ТА", "РЕАЛІЗАЦІЯ"),
          4: ("ТІЛО ТА", "ЗДОРОВ'Я"), 5: ("ІМІДЖ ТА", "КРАСА")}
SUBS = {1: "Сезон 1 · Стосунки з собою", 2: "Сезон 2 · Стосунки у парі", 3: "Сезон 3", 4: "Сезон 4", 5: "Сезон 5"}

def strip(t):  # the old data used <mark>; keep b/i only
    return re.sub(r"</?mark>", "", t or "")

def cta(card, big=False):
    n = card["n"]
    if card["kind"] == "repeat":
        return f'<a class="sp-btn fill" href="#zayavka" data-apply="{n}">ЗАЛИШИТИ ЗАЯВКУ НА ПОВТОР</a>'
    return (f'<a class="sp-btn fill" href="{card["pay"]}" target="_blank" rel="noopener">ПРИЄДНАТИСЯ</a>'
            f'<a class="sp-btn line" href="#zayavka" data-apply="{n}">ХОЧУ В ЛИСТ ОЧІКУВАННЯ</a>')

def build_one(n):
    card = next(c for c in CARDS if c["n"] == n)
    s = next(x for x in D if x["id"] == n)
    t1, t2 = TITLES[n]
    status = re.sub(r"\. Залиште.*$", "", card["status"])
    title = [T(250, 160, 560, t1, "C", 76, 80, OLIVE, "center", cls="big", tag="h1", extra="margin:0;"),
             T(250, 240, 560, t2, "C", 76, 80, OLIVE, "center", italic=True, cls="big")]
    prog_btn = "#programa" if s.get("program") else "#vartist"
    main_btn = (BTN(487, 441, 240, 45, "ЗАЯВКА НА ПОВТОР", "#zayavka", "fill", OLIVE, "#fff", 15, attrs=f'data-apply="{n}"')
                if card["kind"] == "repeat" else
                BTN(522, 441, 170, 45, "ПРИЄДНАТИСЯ", card["pay"], "fill", OLIVE, "#fff", 15, attrs='target="_blank" rel="noopener"'))
    bx = 322 if card["kind"] == "repeat" else 357
    buttons = [BTN(bx, 441, 135, 47, "ПРОГРАМА" if s.get("program") else "ВАРТІСТЬ", prog_btn, "line", OLIVE, OLIVE, 16.5), main_btn]
    out = [SEC(600, hero(title=title, buttons=buttons, sub=SUBS[n], byline=status, photo=card["img"], photo_fit="contain", photo_box=(790, 12, 450, 548)), bg=OLIVE, mbg=CREAM, cls="m-shero")]
    out.append(f'<nav class="sp-crumbs wrap"><a href="svoboda-buty-zhinkoyu.html">Свобода бути жінкою</a> / <span>Сезон {n}</span></nav>')

    out += editorial(s, card, n)

    nav = []
    if n > 1: nav.append(f'<a href="season-{n-1}.html">← Сезон {n-1}</a>')
    nav.append('<a href="svoboda-buty-zhinkoyu.html">Усі сезони</a>')
    if n < 5: nav.append(f'<a href="season-{n+1}.html">Сезон {n+1} →</a>')
    out.append(f'<nav class="sp-next wrap">{"".join(nav)}</nav>')

    name = {1: "Стосунки з собою", 2: "Power Couple. Стосунки у парі", 3: "Гроші та реалізація", 4: "Тіло та здоровʼя", 5: "Імідж та краса"}[n]
    return page(f"Сезон {n}. {name} — Свобода бути жінкою", f"{name}: 8 тижнів лекцій, вправ і живих груп з Наталею Кочергіною. {s['topic']}",
                "".join(out), "svoboda-buty-zhinkoyu.html")


COLLAGE = "1/69d1520aee8819f70862b88b_optimized.webp"
SHELL = "1/69cf95e77ed93e76919e4019_optimized.webp"
AUTHOR = "2/69484f85c2caec12d4b1a4ff_optimized_896.webp"
CLOSE_BG = "1/69cfa37123efa9cc4461697a_optimized_1920.webp"

def editorial(s, card, n):
    """Season page body, art-directed: one idea per screen, readable measure, progressive disclosure."""
    o = []
    start = re.sub(r"\. Залиште.*$", "", card["status"])
    # 1. Key facts strip — orientation in one glance
    facts = [("Старт", start.replace("Сезон іде зараз, з ", "з ").replace("Старт запланований на ", "").replace("Повтор сезону завершився", "повтор за заявкою")),
             ("Тривалість", "8 тижнів"), ("Формат", "лекції, вправи, живі групи"), ("Вартість", "200$ · можливе розтермінування")]
    facts_html = '<section class="ed-facts"><div class="wrap"><dl>' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in facts) + "</dl></div></section>"
    # 2. Hook: the quote, big and alone
    if s.get("quote"):
        o.append(f'''<section class="ed-hook"><div class="wrap"><blockquote>«{s["quote"]}»</blockquote>
<p>{strip(s.get("quoteNote"))}</p></div></section>''')
    # 3. Story: narrow reading column + one image for breathing room
    if s.get("intro"):
        hl = {2: 1}.get(n)  # paragraph set apart like a highlighted passage in a book
        paras = "".join(f'<p class="ed-pull">{p}</p>' if i == hl else f"<p>{p}</p>" for i, p in enumerate(s["intro"]))
        o.append(f'''<section class="ed-story"><div class="wrap ed-story-in"><div class="ed-text">{paras}</div>
<figure class="ed-art"><img src="{img(COLLAGE)}" alt="" loading="lazy"></figure></div></section>''')
    # 4. The promise — one sentence on olive
    o.append(f'''<section class="ed-promise"><div class="wrap"><figure class="ed-author"><img src="{img(AUTHOR)}" alt="Наталя Кочергіна" loading="lazy"></figure>
<p>{s.get("pinned") or s["topic"]}</p>
<div class="ed-sign"><b>Наталя Кочергіна</b><span>психоаналітичний психотерапевт, авторка проєкту «Свобода бути жінкою»</span></div></div></section>''')
    # 5. For whom — a calm numbered list, no repeated icons
    if s.get("forWhom"):
        ft = s.get("forWhomTitle") or "Цей сезон для вас, якщо ви:"
        items = "".join(f"<li><span>{i+1:02d}</span>{x[:1].upper() + x[1:]}</li>" for i, x in enumerate(s["forWhom"]))
        o.append(f'''<section class="ed-for"><div class="wrap ed-for-in"><figure class="ed-for-art"><img src="{img(card["img"])}" alt="" loading="lazy"></figure>
<div><h2 class="ed-h">{ft}</h2><ol class="ed-list">{items}</ol></div></div></section>''')
    # 6. Outcomes — 2x2 with large italic numerals
    if s.get("outcomes"):
        items = "".join(f"<li><span>{i+1}</span><p>{x}</p></li>" for i, x in enumerate(s["outcomes"]))
        o.append(f'''<section class="ed-out"><div class="wrap"><h2 class="ed-h light">Що ви отримаєте</h2><ul class="ed-grid">{items}</ul></div></section>''')
    # 7. Program — accordion: titles at a glance, details on demand
    if s.get("program"):
        weeks = "".join(f'''<details{" open" if i == 0 else ""}><summary><span class="wk">Тиждень {i+1}</span><span class="tt">{t}</span><span class="pl" aria-hidden="true"></span></summary><p>{d}</p></details>''' for i, (t, d) in enumerate(s["program"]))
        o.append(f'''<section class="ed-prog" id="programa"><div class="wrap"><h2 class="ed-h">Програма сезону</h2>
<p class="ed-sub">8 тижнів · натисніть на тиждень, щоб прочитати більше</p><div class="ed-acc">{weeks}</div></div></section>''')
    else:
        o.append(f'''<section class="ed-prog" id="programa"><div class="wrap"><h2 class="ed-h">Програма сезону</h2>
<p class="ed-sub big">{s["topic"]}</p><p class="ed-sub">Детальна програма зʼявиться ближче до старту. Залиште заявку, і ми надішлемо її першою.</p></div></section>''')
    # 8. Format — four clear steps, words taken from the season text
    ft = s.get("formatText") or ""
    if ft:
        day = re.search(r"(Що\w+) — групова", ft)
        steps = [("8 лекцій", "з переглядом терапевтичного кіно"),
                 (day.group(1) if day else "Щотижня", "групова зустріч у Zoom"),
                 ("Вправи", "до кожної лекції, для саморефлексії"),
                 ("1 рік", "доступу до матеріалів")]
    else:
        steps = [("8 тижнів", "занурення в тему"), ("Лекції", "у записі, з вправами та техніками"),
                 ("Живі групи", "для глибокої зміни мислення та взаємної підтримки"), ("Телеграм", "підтримуюча група учасниць")]
    cells = "".join(f'<li><span class="n">{i+1:02d}</span><b>{a}</b><p>{b}</p></li>' for i, (a, b) in enumerate(steps))
    guests = ""
    if s.get("guests"):
        guests = ('<div class="ed-guests"><h3>Гості-експерти</h3><p>У кожному потоці до групи долучаються запрошені експерти. '
                  'Склад гостей щоразу змінюється.</p></div>')
    o.append(f'''<section class="ed-fmt"><div class="wrap"><h2 class="ed-h light">Як проходить сезон</h2>
<ol class="ed-steps">{cells}</ol>{guests}</div></section>''')
    # 9. Social proof: one voice at a time, large, with a gentle carousel
    keys = "dabcef"
    slides = "".join(f'<blockquote class="ed-slide{" on" if i == 0 else ""}">{TESTI[k]}</blockquote>' for i, k in enumerate(keys))
    o.append(f'''<section class="ed-rev" id="vidguky"><div class="wrap"><p class="ed-k">Відгуки учасниць</p>
<div class="ed-car" data-car><div class="ed-slides">{slides}</div>
<div class="ed-ctl"><button type="button" data-prev aria-label="Попередній відгук">←</button><span class="ed-cnt"><b>01</b> / {len(keys):02d}</span><button type="button" data-next aria-label="Наступний відгук">→</button></div></div></div></section>''')
    o.append(facts_html)
    # 10. Decision: closing words + price + one action
    cl = "".join(f"<p>{p}</p>" for p in (s.get("closing") or []))
    o.append(f'''<section class="ed-buy" id="vartist" style="background-image:url('{img(CLOSE_BG)}')"><div class="wrap ed-buy-in">
<div class="ed-close">{cl or "<p>Запрошую вас у простір жіночої підтримки та натхнення, щоб створити свій авторський шедевр!</p>"}</div>
<div class="ed-card"><p class="ed-k">Ціна за сезон</p><p class="ed-price">200$</p><p class="ed-soft">Можливе розтермінування</p>
<ul><li>8 тижнів занурення в тему</li><li>Доступ до записів лекцій та вправ</li><li>Підтримуюча група в Телеграм каналі</li><li>Живі групи з автором</li></ul>
{cta(card)}<p class="ed-soft small">Кількість місць обмежена для збереження камерної атмосфери</p>
<a class="ed-mgr" href="https://t.me/pnm_a" target="_blank" rel="noopener">Є питання? Напишіть менеджеру</a></div></div></section>''')
    return o
