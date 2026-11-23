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
    (2, "Стосунки у парі", "Іде зараз · з 19 жовтня", "1/69cf91c623efa9cc44611d23_optimized.webp", "season-2.html"),
    (3, "Гроші та реалізація", "Старт у грудні 2026", "1/69cf92ec378263656007dff2_optimized.webp", "season-3.html"),
    (4, "Тіло та здоров'я", "Старт у березні 2027", "1/69cf927ceecd0ca27089a758_optimized.webp", "season-4.html"),
    (5, "Імідж та краса", "Старт у червні 2027", "1/69cf93237ed93e76919e3406_optimized.webp", "season-5.html"),
]

def build():
    secs = []
    P = dict(weight=500)  # body text: Cormorant 500 reads much better than the original hairline 400
    # Hero: same composition, plus who she is and one clear action
    secs.append(SEC(600, [
        I(318, 45, 220, 304, "2/6945c466f079e06014374273_optimized_969.webp", cls="keep mob-hide"),
        T(482, 182, 481, "ВІТАЮ ВАС", "C", 90, 90, "#000", "right", cls="big", tag="h1", extra="margin:0;"),
        T(517, 246, 446, "У СВОЄМУ", "C", 90, 90, "#000", "right", cls="big"),
        T(515, 310, 448, "ПРОСТОРІ", "C", 90, 90, "#000", "right", cls="big"),
        T(463, 422, 500, "психотерапевт · психодинамічний коуч", "F", 20, 24, "#757575", "right", cls="p"),
        BTN(750, 470, 213, 50, "Подати заявку", TG_N, "fill", "#000", "#fff", 19, "C", 25, 'target="_blank" rel="noopener"', arrow=True),
    ], bg="#fff"))
    # About (lifted 80px: the original had a dead gap under the hero)
    secs.append(SEC(640, [
        T(368, 122, 300, "Наталя Кочергіна", "C", 40, 52, "#000", "left", cls="h2"),
        T(340, 172, 346, "Я психотерапевт та психодинамічний<br>коуч із практикою понад 10 років", "C", 20, 24, "#757575", "center", 600, cls="p"),
        LINE(434, 246, 158, "#000"),
        T(262, 282, 501, "Мій метод — це тонка робота з особистістю, де поєднуються психоаналіз, коучинг і системне бачення. Я спираюся на повагу до індивідуальності і впевнена, що в кожній людині є прихований потенціал для змін.", "C", 21, 30, "#000", "center", cls="p", **P),
        BTN(434, 462, 158, 40, "ПРО МЕНЕ", "about.html", "line", "#000", "#000", 15),
        I(937, 0, 383, 575, "2/694e7e27080a9d0140ffdb16_optimized_930.webp", cls="keep", alt="Наталя Кочергіна"),
    ], bg="#fff"))
    # Spheres
    rows = [("01", "тіло та здоровʼя"), ("02", "гроші, реалізація та особистий потенціал"),
            ("03", "лідерство та управління командою"), ("04", "сімʼя. стосунки між батьками та дітьми"),
            ("05", "любов та стосунки у парі")]
    ch = [T(441, 29, 559, "Я ПРАЦЮЮ ІЗ ЗАПИТАМИ<br>НА ЗМІНИ У ТАКИХ СФЕРАХ:", "F", 48, 48, "#000", "center", cls="h2", tag="h2", extra="margin:0;")]
    for i, (n, t) in enumerate(rows):
        ch.append(G(630, 166 + i * 42, 570, 42, [
            T(1, 7, 60, n, "F", 25, 28, "#000", cls="p", extra="position:absolute"),
            T(102, 7, 460, t, "F", 25, 28, "#000", cls="p"),
        ], cls="row", extra="border-bottom:1px solid #000;"))
    secs.append(SEC(420, ch, bg="#fff", id="sfery"))
    # Mission grid
    secs.append(SEC(830, [
        I(188, 40, 221, 224, "2/694e7f3bc2c73c4433f45bca_optimized.webp"),
        I(536, 40, 221, 224, "2/694e7f3edc0acba3c58c1825_optimized.webp"),
        I(883, 297, 221, 224, "2/694e7fc8080a9d0140ffdf80_optimized.webp", cls="keep"),
        T(281, 355, 440, "Моє завдання — допомогти вам звільнитися від внутрішніх обмежень і побудувати якісне життя у відповідності до вашого справжнього Я!", "C", 24, 32, "#000", "left", cls="p", **P),
        I(188, 552, 221, 224, "2/694e7fe8dc4fd58c318ee1e6_optimized_572_c572x1024-0x0.webp"),
        I(536, 552, 221, 224, "2/694e7fe9c2c73c4433f45e1d_optimized_572_c572x1024-0x0.webp"),
    ], bgimg="2/6945cfbf364911d845d9da3b_optimized_2560.webp"))
    # Services: white titles now sit on a soft shade, so they read on any photo
    cards = [(120, "6947ff97364911d845de49e9_optimized_921.webp", "індивідуальна<br>терапія", 609),
             (520, "694e852edc4fd58c318ef385_optimized.webp", "психодинамічний<br>коучінг", 609),
             (920, "6948002c364911d845de4b73_optimized_921.webp", "групи", 641)]
    ch = [T(120, 88, 1200, "ІНДИВІДУАЛЬНА РОБОТА ЗІ МНОЮ:", "F", 48, 48, "#000", "center", cls="h2", tag="h2", extra="margin:0;")]
    for x, f, t, ty in cards:
        ch.append(G(x, 151, 400, 609, [
            I(0, 0, 400, 609, "2/" + f, cls="keep"),
            S(0, 330, 400, 279, "linear-gradient(to bottom, rgba(0,0,0,0), rgba(0,0,0,.55))"),
            T(32, ty - 151, 340, t, "F", 32, 32, "#fff", cls="h2"),
            LINE(30, 534, 339, "#fff"),
            f'<a class="a t" href="{TG_N}" target="_blank" rel="noopener" style="left:30px;top:562px;font-family:var(--forum);font-size:20px;line-height:30px;color:#fff;text-decoration:none">записатися →</a>',
        ], cls="svc"))
    secs.append(SEC(840, ch, bg=CREAM, id="poslugy"))
    # Products: one olive block in the salon's colours. Title in the centre, horse in an arch on the right,
    # the five seasons as beige cards underneath.
    C2 = "#fffaf1"; BEIGE = "#fff5e7"
    ch = [
        I(70, 110, 375, 540, "1/69cf74dc7ed93e76919db552_optimized.webp", extra="opacity:.9"),
        S(972, 128, 366, 516, "", f"1px solid rgba(255,250,241,.55)", extra="border-radius:183px 183px 0 0;"),
        I(990, 146, 330, 480, "1/69dd1850e56bc464c74e3faa_optimized_978_c978x1326-0x0.webp", cls="keep",
          extra="border-radius:165px 165px 0 0;object-position:40% 50%;"),
        T(420, 150, 600, "ПРОДУКТИ · психологічний салон", "F", 20, 24, C2, "center", cls="p", extra="opacity:.75;letter-spacing:.04em"),
        T(420, 196, 600, '<a href="svoboda-buty-zhinkoyu.html" style="text-decoration:none">СВОБОДА</a>', "C", 86, 86, C2, "center", cls="big", tag="h2", extra="margin:0;"),
        T(420, 276, 600, '<a href="svoboda-buty-zhinkoyu.html" style="text-decoration:none">БУТИ ЖІНКОЮ</a>', "C", 86, 86, C2, "center", italic=True, cls="big"),
        T(450, 400, 540, "Це трансформаційний жіночий онлайн-простір, де ми повертаємося до своєї  цілісності, звільняємось від очікувань інших  та навʼязаних ролей, знаходимо ресурс та підтримку одна в одній, і будуємо життя за власним сценарієм.", "C", 21, 30, C2, "center", cls="p", **P),
        T(420, 556, 600, "5 сезонів · 8 тижнів кожен · лекції, вправи та живі групи", "F", 18, 22, C2, "center", cls="p", extra="opacity:.75"),
        BTN(614, 600, 212, 50, "ПРО ПРОЄКТ", "svoboda-buty-zhinkoyu.html", "fill", C2, "#595f45", 17, "C", 25),
        T(120, 726, 600, "ТЕМИ СЕЗОНІВ", "F", 28, 32, C2, "left", cls="h2"),
        T(820, 732, 500, '<a href="svoboda-buty-zhinkoyu.html#temy" style="color:#fffaf1">усі сезони →</a>', "F", 20, 24, C2, "right", cls="p mob-hide"),
    ]
    for i, (n, t, st_, im, href) in enumerate(SEASON_CARDS):
        ch.append(G(120 + i * 244, 780, 224, 300, [
            I(37, 20, 150, 140, im, cls="keep", extra="object-fit:contain;"),
            T(20, 172, 184, f"Сезон {n}", "F", 16, 18, "#595f45", "left", extra="opacity:.65"),
            T(20, 194, 184, t, "F", 22, 25, "#595f45", "left", 700),
            T(20, 252, 184, st_, "F", 16, 18, "#595f45", "left", extra="opacity:.85"),
            f'<a class="a" href="{href}" style="inset:0" aria-label="Сезон {n}. {t}"></a>',
        ], bg=BEIGE, cls="scard"))
    secs.append(SEC(1170, ch, bg=OLIVE, id="produkty"))
    # Testimonials
    secs.append(SEC(1480, testimonials("#f8f8f8", dy=20), bg="#fff", id="vidguky"))
    # CTA
    secs.append(SEC(500, [
        I(120, -50, 470, 410, "2/694841a4c2caec12d4b177bd_optimized_1220.webp"),
        S(415, 79, 610, 362, "#fff"),
        T(501, 148, 439, "ВИ ВЖЕ В ПОТРІБНОМУ МІСЦІ І В ПОТРІБНИЙ ЧАС.", "C", 28, 36.4, "#000", "center", cls="p"),
        T(561, 257, 318, "ЗРОБІТЬ КРОК ДО ЗМІН!", "C", 28, 36.4, "#000", "center", cls="p"),
        BTN(613, 348, 213, 50, "Подати заявку", TG_N, "fill", "#000", "#fff", 19, "C", 25, 'target="_blank" rel="noopener"', arrow=True),
        I(891, 155, 452, 394, "2/694841a4c2caec12d4b177bd_optimized_1220_flop.webp"),
        LINE(120, 488, 1200, "#000"),
    ], bg="#fff"))
    body = "".join(secs)
    return page("Наталя Кочергіна — психотерапевт і психодинамічний коуч",
                "Психоаналітичний психотерапевт і психодинамічний коуч Наталя Кочергіна: індивідуальна терапія, коучинг, групи та жіночий проєкт «Свобода бути жінкою».",
                body, "index.html")
