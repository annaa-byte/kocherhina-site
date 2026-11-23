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
    out = [SEC(600, hero(title=title, buttons=buttons, sub=SUBS[n], byline=status, photo=card["img"], photo_fit="contain"), bg=OLIVE, mbg=CREAM)]
    out.append(f'<nav class="sp-crumbs wrap"><a href="svoboda-buty-zhinkoyu.html">Свобода бути жінкою</a> / <span>Сезон {n}</span></nav>')

    if s.get("intro"):
        paras = "".join(f"<p>{p}</p>" for p in s["intro"])
        q = f'''<figure class="sp-quote"><img src="{img(SHIP)}" alt="" width="79" height="63"><blockquote>{s["quote"]}</blockquote><p>{strip(s.get("quoteNote"))}</p></figure>''' if s.get("quote") else ""
        out.append(f'<section class="sp cream"><div class="wrap sp-intro"><div class="sp-col">{paras}</div>{q}</div></section>')
    if s.get("pinned"):
        out.append(f'<section class="sp olive"><div class="sp-band"><p>{s["pinned"]}</p></div></section>')
    else:
        out.append(f'<section class="sp olive"><div class="sp-band"><p>{s["topic"]}</p></div></section>')

    if s.get("forWhom"):
        ft = s.get("forWhomTitle") or "Цей сезон для вас, якщо ви:"
        cards = "".join(f'<li><img src="{img(SHIP)}" alt="" width="58" height="46"><span>{x}</span></li>' for x in s["forWhom"])
        out.append(f'<section class="sp cream"><div class="wrap"><h2 class="sp-h">{ft.upper()}</h2><ul class="sp-want">{cards}</ul></div></section>')
    if s.get("outcomes"):
        rows = "".join(f'<li><span class="sp-star star"></span>{x}</li>' for x in s["outcomes"])
        out.append(f'''<section class="sp olive"><div class="wrap sp-two"><div class="sp-ell"><img src="{img(ELLIPSE)}" alt=""><h2>ЩО ВИ ОТРИМАЄТЕ</h2></div><ul class="sp-rows">{rows}</ul></div></section>''')
    if s.get("program"):
        weeks = "".join(f'<article class="sp-week"><span>ТИЖДЕНЬ {i+1}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(s["program"]))
        out.append(f'''<section class="sp cream" id="programa"><div class="wrap"><h2 class="sp-h">ПРОГРАМА СЕЗОНУ</h2>
<img class="sp-jag" src="{img(JAG)}" alt=""><div class="sp-weeks">{weeks}</div><img class="sp-jag" src="{img(JAGF)}" alt=""></div></section>''')
    else:
        out.append(f'''<section class="sp cream" id="programa"><div class="wrap"><h2 class="sp-h">ПРОГРАМА СЕЗОНУ</h2>
<p class="sp-lead">{s["topic"]}</p><p class="sp-lead soft">Детальна програма зʼявиться ближче до старту. Залиште заявку, і ми надішлемо її першою.</p></div></section>''')

    fmt = strip(s.get("formatText")) or "Лекції в записі, вправи, техніки та живі групові зустрічі для глибокої зміни мислення та взаємної підтримки. Робота на базі глибинної психології."
    fmt = fmt.replace("<b>Формат:</b> ", "")
    guests = ""
    if s.get("guests"):
        guests = '<div class="sp-guests"><h3>ГОСТІ-ЕКСПЕРТИ</h3>' + "".join(f"<p><b>{a}</b> — {b}</p>" for a, b in s["guests"]) + "</div>"
    out.append(f'''<section class="sp olive"><div class="wrap sp-two"><div class="sp-ell"><img src="{img(ELLIPSE)}" alt=""><h2>ФОРМАТ</h2></div>
<div><p class="sp-fmt">{fmt}</p><ul class="sp-rows small"><li><b>8 тижнів</b> тривалість сезону</li><li><b>1 лекція і 1 жива група</b> на тиждень</li></ul>{guests}</div></div></section>''')

    feats = "".join(f'<li><span class="sp-star star"></span>{f}</li>' for f in ["8 тижнів занурення в тему", "Доступ до записів лекцій та вправ", "Підтримуюча група в Телеграм каналі", "Живі групи з автором"])
    out.append(f'''<section class="sp olive" id="vartist"><div class="wrap"><h2 class="sp-h light"><i>ВАРТІСТЬ</i> ТА УЧАСТЬ</h2>
<div class="sp-price"><div><h3>Єдиний тариф:</h3><ul>{feats}</ul></div>
<div class="sp-pr"><h3>Ціна за сезон<br>200$</h3><p>Можливе розтермінування</p>{cta(card)}</div></div>
<p class="sp-lim">КІЛЬКІСТЬ МІСЦЬ <i>ОБМЕЖЕНА</i><small>для збереження камерної атмосфери</small></p></div></section>''')

    if s.get("closing"):
        cl = "".join(f"<p>{p}</p>" for p in s["closing"])
        out.append(f'''<section class="sp-close" style="background-image:url('{img("1/69cfa37123efa9cc4461697a_optimized_1920.webp")}')"><div class="wrap"><div class="sp-close-in">{cl}</div></div></section>''')

    tcards = "".join(f'<figure class="sp-t"><img src="{img(QUOTE)}" alt="" width="25" height="19"><blockquote>{TESTI[k]}</blockquote></figure>' for k in "debacf")
    out.append(f'<section class="sp cream" id="vidguky"><div class="wrap"><h2 class="sp-h dark">ВІДГУКИ:</h2><div class="sp-ts">{tcards}</div></div></section>')

    out.append(SEC(700, [
        I(-37, 32, 622, 466, "1/69cfa4e7eecd0ca27089f7c3_optimized_1304_flop.webp"),
        I(911, 181, 491, 391, "1/69cfa2feeecd0ca27089eec7_optimized_833_flop.webp"),
        G(415, 169, 610, 362, [
            T(0, 48, 610, "НЕ ТРЕБА<br><i>ВІДМОВЛЯТИСЬ</i>", "F", 48, 48, OLIVE, "center", cls="h2"),
            T(0, 159, 610, "Якщо в цьому світі щось є -<br>ви можете це мати.", "F", 28, 28, OLIVE, "center", cls="p"),
            BTN(173, 262, 264, 50, "НАПИСАТИ МЕНЕДЖЕРУ", "https://t.me/pnm_a", "fill", OLIVE, "#fff", 15, "C", 25, 'target="_blank" rel="noopener"', arrow=True),
        ], bg=CREAM),
    ], bgimg="1/69cfa4c47ed93e76919e7f1b_optimized_1920.webp", bgpos="53.44% 45.28%"))

    nav = []
    if n > 1: nav.append(f'<a href="season-{n-1}.html">← Сезон {n-1}</a>')
    nav.append('<a href="svoboda-buty-zhinkoyu.html">Усі сезони</a>')
    if n < 5: nav.append(f'<a href="season-{n+1}.html">Сезон {n+1} →</a>')
    out.append(f'<nav class="sp-next wrap">{"".join(nav)}</nav>')

    name = {1: "Стосунки з собою", 2: "Power Couple. Стосунки у парі", 3: "Гроші та реалізація", 4: "Тіло та здоровʼя", 5: "Імідж та краса"}[n]
    return page(f"Сезон {n}. {name} — Свобода бути жінкою", f"{name}: 8 тижнів лекцій, вправ і живих груп з Наталею Кочергіною. {s['topic']}",
                "".join(out), "svoboda-buty-zhinkoyu.html")
