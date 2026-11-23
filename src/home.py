from lib import *

TG_N = "https://t.me/Kocher_Nataly"

TESTI = {
 "a": "Дуже вдячна Наталії за можливість апгрейдити пакет участі у проєкті та відвідувати терапевтичну групу! Я в захваті від нашої групи! така ресурсна! я прямо вбираю все як губка, стільки інсайтів зʼявляється на групі, на багато ситуацій почала дивитися по іншому.",
 "b": "Наталія  домогла мені підсвітила мої різні сторони, як позитивні так і негативні. Після курсу  я навчилася  сприймати себе як  цілістну особистість, більш вільну, впевненішу . Прислуховуватися до своїх потреб та бажань. Щиро дякую за неймовірну можливість занурення в себе, за початок знайомства з психоаналізом! Це підштовхнуло мене до вибору направлення моєї професійної діяльності. Сердечно дякую за цю пригоду !!",
 "c": "Дякую Наталія за Вашу роботу💚 І дуже добре, що проводите таку психологічну роботу онлайн. Тепер люди з різних куточків світу завдяки Вам зможуть стати щасливіші і жити своє наповнене життя🫂Це була моя перша робота в групі і я задоволена тим, що це саме групова терапія. Цінні розповіді колег, історії, як ми бачимо одне одного, чуємо...",
 "d": "Я неймовірно щаслива що мала нагоду проходити курс у Пані Наталії. Щиро хочу подякувати  за неймовірну підтримку та супровід. Я відкрила для себе чудовий метод групової терапії, де є підтримка і від групи і від психотерапевта. Це допомагає сміливіше ділитися своїми емоціями, враженнями .",
 "e": "Велика подяка пані Наталії і всій команді за дуже професійну роботу!",
 "f": "Я щиро вдячна за цей проєкт Всім хто прикладав до неї свої зусилля.",
}

def testimonials(card_bg, dy=0, page_bg="#fff", head_color="#000"):
    """Collage block from the original, with readable cards: text flows inside each card,
    so longer quotes never spill out (original had line-height 1.0 and fixed boxes)."""
    Q = img("2/694819b3364911d845de9420_optimized.webp")
    def card(key):
        return (f'<figure class="tcard" style="background:{card_bg}">'
                f'<img src="{Q}" alt="" width="25" height="19"><blockquote>{TESTI[key]}</blockquote></figure>')
    ch = [T(396, 104 + dy, 260, "ВІДГУКИ:", "F", 48, 48, head_color, "left", cls="h2", tag="h2", extra="margin:0;"),
          I(461, 280 + dy, 519, 807, "2/6948180b5a2b8aea0311d229_optimized_914.webp")]
    ch.append(f'<div class="a tcol" style="left:290px;top:{190 + dy}px;width:280px">' + card("d") + card("b") + card("f") + '</div>')
    ch.append(f'<div class="a tcol" style="left:870px;top:{150 + dy}px;width:280px">' + card("a") + card("e") + card("c") + '</div>')
    return ch

SEASON_CARDS = [
    # n, title, status line, image, page
    (1, "Стосунки з собою", "Повтор сезону завершено", "1/69cf907e02d98a0e80c32e0c_optimized.webp", "season-1.html"),
    (2, "Стосунки у парі", "Іде зараз · з 19 жовтня", "L/power-couple.webp", "season-2.html"),
    (3, "Гроші та реалізація", "Старт у березні 2027", "1/69cf92ec378263656007dff2_optimized.webp", "season-3.html"),
    (4, "Тіло та здоров'я", "Старт у червні 2027", "1/69cf927ceecd0ca27089a758_optimized.webp", "season-4.html"),
    (5, "Імідж та краса", "Старт у вересні 2027", "1/69cf93237ed93e76919e3406_optimized.webp", "season-5.html"),
]

def build():
    secs = []
    P = dict(weight=500)  # body text: Cormorant 500 reads much better than the original hairline 400
    # Hero: same composition, plus who she is and one clear action
    secs.append(SEC(600, [
        I(318, 45, 220, 304, "2/6945c466f079e06014374273_optimized_969.webp", cls="keep"),
        T(482, 182, 481, "ВІТАЮ ВАС", "C", 90, 90, "#000", "right", cls="big", tag="h1", extra="margin:0;"),
        T(517, 246, 446, "У СВОЄМУ", "C", 90, 90, "#000", "right", cls="big"),
        T(515, 310, 448, "ПРОСТОРІ", "C", 90, 90, "#000", "right", cls="big"),
    ], bg="#fff", cls="m-hero").replace("--h:600px", "--h:480px"))
    # About: portrait in the salon's arch, words beside it — one person, one promise, one link
    secs.append(f'''<section class="hm-about"><div class="wrap hm-about-in">
<figure class="hm-portrait"><img src="{img("2/694e7e27080a9d0140ffdb16_optimized_930.webp")}" alt="Наталя Кочергіна" loading="lazy"></figure>
<div class="hm-about-tx"><p class="ed-k">Про мене</p><h2>Наталя Кочергіна</h2>
<p class="hm-role">Я психотерапевт та психодинамічний коуч із практикою понад 10 років</p>
<p class="hm-body">Мій метод — це тонка робота з особистістю, де поєднуються психоаналіз, коучинг і системне бачення. Я спираюся на повагу до індивідуальності і впевнена, що в кожній людині є прихований потенціал для змін.</p>
<a class="hm-link" href="about.html">Детальніше про мене <span>→</span></a></div></div></section>''')
    # Spheres
    rows = [("01", "тіло та здоровʼя"), ("02", "гроші, реалізація та особистий потенціал"),
            ("03", "лідерство та управління командою"), ("04", "сімʼя. стосунки між батьками та дітьми"),
            ("05", "любов та стосунки у парі")]
    ch = [T(441, 109, 559, "Я ПРАЦЮЮ ІЗ ЗАПИТАМИ<br>НА ЗМІНИ У ТАКИХ СФЕРАХ:", "F", 44, 50, OLIVE, "center", cls="h2", tag="h2", extra="margin:0;")]
    for i, (n, t) in enumerate(rows):
        ch.append(G(630, 246 + i * 52, 570, 52, [
            T(1, 15, 60, n, "F", 17, 24, "rgba(89,95,69,.6)", cls="p", extra="letter-spacing:.1em"),
            T(102, 11, 460, t, "C", 24, 30, "#2c2f22", cls="p", weight=500),
        ], cls="row", extra="border-bottom:1px solid rgba(89,95,69,.3);"))
    secs.append(SEC(600, ch, bg="#fff", id="sfery"))
    # Mission grid
    secs.append(SEC(830, [
        I(188, 40, 221, 224, "2/694e7f3bc2c73c4433f45bca_optimized.webp"),
        I(536, 40, 221, 224, "2/694e7f3edc0acba3c58c1825_optimized.webp"),
        I(883, 297, 221, 224, "2/694e7fc8080a9d0140ffdf80_optimized.webp", cls="keep"),
        T(281, 355, 440, "Моє завдання — допомогти вам звільнитися від внутрішніх обмежень і побудувати якісне життя у відповідності до вашого <i style=\"font-size:1.3em;color:#595f45;font-weight:600\">справжнього Я!</i>", "C", 24, 34, "#2c2f22", "left", cls="p", **P),
        I(188, 552, 221, 224, "2/694e7fe8dc4fd58c318ee1e6_optimized_572_c572x1024-0x0.webp"),
        I(536, 552, 221, 224, "2/694e7fe9c2c73c4433f45e1d_optimized_572_c572x1024-0x0.webp"),
    ], bgimg="2/6945cfbf364911d845d9da3b_optimized_2560.webp", cls="m-grid"))
    # Services: three arch-topped cards with air between them; details open in a popup that ends with an action
    svc = [
        ("terapiya", "6947ff97364911d845de49e9_optimized_921.webp", "індивідуальна терапія", "Індивідуальна терапія",
         "Вартість сесії 150€", "Розклад сформований. Запис можливий на січень 2027.",
         [("Як це відбувається?", "Робота з несвідомим для трансформації структур вашої особистості.<br>Я не вирішую вашу проблему, я допомагаю вам стати людиною, здатною вирішувати свої проблеми самостійно."),
          ("Для кого?", "Для тих, хто відчуває, що застряг у проблемі або ходить по колу. Хто не знає, як вийти на новий рівень життя, стосунків, самовідчуття. Хто прагне комплексної зміни життя, а не лише вирішення конкретної проблеми."),
          ("Результат", "Ви станете впевненішими у своїх силах, зможете глибше зрозуміти себе та свої життєві сценарії. Навички самостійного вирішення проблем дозволять вам бути більш адаптивними та гнучкими перед життєвими викликами.")]),
        ("kouching", "694e852edc4fd58c318ef385_optimized.webp", "психодинамічний коучінг", "Психодинамічний коучінг", "", "", []),
        ("grupy", "6948002c364911d845de4b73_optimized_921.webp", "групи", "Групи", "", "", []),
    ]
    cards = ""; pops = ""
    for key, f, label, title, price, note, acc in svc:
        cards += (f'''<button type="button" class="hm-svc" data-svc="{key}"><span class="hm-svc-img"><img src="{img("2/" + f)}" alt="" loading="lazy"></span>
<span class="hm-svc-t">{label}</span><span class="hm-svc-more">детальніше <i>→</i></span></button>''')
        items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}<span class="pl" aria-hidden="true"></span></summary><p>{a_}</p></details>' for i, (q, a_) in enumerate(acc))
        pops += (f'''<div class="modal svc-pop" id="svc-{key}" aria-hidden="true" role="dialog"><div class="svc-box"><button class="mx" aria-label="Закрити" data-close>×</button>
<img class="svc-img" src="{img("2/" + f)}" alt="" loading="lazy"><div class="svc-tx"><h2>{title}</h2>
{f'<p class="svc-price">{price}</p>' if price else ''}{f'<p class="svc-note">{note}</p>' if note else ''}
<div class="svc-acc">{items}</div><a class="hm-btn" href="{TG_N}" target="_blank" rel="noopener">Записатися</a></div></div></div>''')
    secs.append(f'''<section class="hm-svcs" id="poslugy"><div class="wrap"><h2 class="hm-h2">Індивідуальна робота зі мною:</h2>
<div class="hm-svc-row">{cards}</div></div>{pops}</section>''')
    # Products: one olive block in the salon's colours. Title in the centre, horse in an arch on the right,
    # the five seasons as beige cards underneath.
    C2 = "#fffaf1"; BEIGE = "#fff5e7"
    ch = [
        I(-30, 110, 375, 540, "1/69cf74dc7ed93e76919db552_optimized.webp", extra="opacity:.9"),
        S(972, 128, 366, 516, "", f"1px solid rgba(255,250,241,.55)", extra="border-radius:183px 183px 0 0;"),
        I(990, 146, 330, 480, "1/69dd1850e56bc464c74e3faa_optimized_978_c978x1326-0x0.webp", cls="keep",
          extra="border-radius:165px 165px 0 0;object-position:40% 50%;"),
        T(330, 150, 600, "ПРОДУКТИ · психологічний салон", "F", 20, 24, C2, "center", cls="p", extra="opacity:.75;letter-spacing:.04em"),
        T(330, 196, 600, '<a href="svoboda-buty-zhinkoyu.html" style="text-decoration:none">СВОБОДА</a>', "C", 86, 86, C2, "center", cls="big", tag="h2", extra="margin:0;"),
        T(330, 276, 600, '<a href="svoboda-buty-zhinkoyu.html" style="text-decoration:none">БУТИ ЖІНКОЮ</a>', "C", 86, 86, C2, "center", italic=True, cls="big"),
        T(360, 400, 540, "Це трансформаційний жіночий онлайн-простір, де ми повертаємося до своєї  цілісності, звільняємось від очікувань інших  та навʼязаних ролей, знаходимо ресурс та підтримку одна в одній, і будуємо життя за власним сценарієм.", "C", 21, 30, C2, "center", cls="p", **P),
        T(330, 556, 600, "5 сезонів · 8 тижнів кожен · лекції, вправи та живі групи", "F", 18, 22, C2, "center", cls="p", extra="opacity:.75"),
        BTN(524, 600, 212, 50, "ПРО ПРОЄКТ", "svoboda-buty-zhinkoyu.html", "fill", C2, "#595f45", 17, "C", 25),
        T(120, 726, 600, "ТЕМИ СЕЗОНІВ", "F", 28, 32, C2, "left", cls="h2"),
        T(820, 732, 500, '<a href="svoboda-buty-zhinkoyu.html#temy" style="color:#fffaf1">усі сезони →</a>', "F", 20, 24, C2, "right", cls="p mob-hide"),
    ]
    row = []
    for i, (n, t, st_, im, href) in enumerate(SEASON_CARDS):
        row.append(G(120 + i * 244, 780, 224, 300, [
            I(37, 20, 150, 140, im, cls="keep", extra="object-fit:contain;"),
            T(20, 172, 184, f"Сезон {n}", "F", 16, 18, "#595f45", "left", extra="opacity:.65"),
            T(20, 194, 184, t, "F", 22, 25, "#595f45", "left", 700),
            T(20, 252, 184, st_, "F", 16, 18, "#595f45", "left", extra="opacity:.85"),
            f'<a class="a" href="{href}" style="inset:0" aria-label="Сезон {n}. {t}"></a>',
        ], bg=BEIGE, cls="scard"))
    ch.append('<div class="a srow" style="left:0;top:0;width:1440px;height:0">' + "".join(row) + '</div>')
    secs.append(SEC(1170, ch, bg=OLIVE, id="produkty", cls="m-prod"))
    # Testimonials: one voice at a time (same pattern as the season pages)
    keys = "bdacef"
    slides = "".join(f'<blockquote class="ed-slide{" on" if i == 0 else ""}">{TESTI[k]}</blockquote>' for i, k in enumerate(keys))
    secs.append(f'''<section class="ed-rev" id="vidguky"><div class="wrap"><p class="ed-k">Відгуки</p>
<div class="ed-car" data-car><div class="ed-slides">{slides}</div>
<div class="ed-ctl"><button type="button" data-prev aria-label="Попередній відгук">←</button><span class="ed-cnt"><b>01</b> / {len(keys):02d}</span><button type="button" data-next aria-label="Наступний відгук">→</button></div></div></div></section>''')
    # Closing call: the two flowers frame one sentence and one button
    secs.append(f'''<section class="hm-cta"><div class="wrap hm-cta-in">
<img class="hm-fl" src="{img("2/694841a4c2caec12d4b177bd_optimized_1220.webp")}" alt="" loading="lazy">
<div class="hm-cta-tx"><p>Ви вже в потрібному місці і в потрібний час.</p><p class="it">Зробіть крок до змін!</p>
<a class="hm-btn" href="{TG_N}" target="_blank" rel="noopener">Подати заявку</a></div>
<img class="hm-fl r" src="{img("2/694841a4c2caec12d4b177bd_optimized_1220_flop.webp")}" alt="" loading="lazy"></div></section>''')
    body = "".join(secs)
    return page("Наталя Кочергіна — психотерапевт і психодинамічний коуч",
                "Психоаналітичний психотерапевт і психодинамічний коуч Наталя Кочергіна: індивідуальна терапія, коучинг, групи та жіночий проєкт «Свобода бути жінкою».",
                body, "index.html")
