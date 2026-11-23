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
    """The original collage block. dy shifts everything (home: 94px lower than on the salon page)."""
    Q = "2/694819b3364911d845de9420_optimized.webp"
    def card(cx, cy, qx, qy, tx, ty, tw, th, lx, ly, text, bg=True):
        out = []
        if bg: out.append(S(cx, cy + dy, 270, 412, card_bg, cls="shape"))
        out.append(I(qx, qy + dy, 25, 19, Q))
        out.append(T(tx, ty + dy, tw, text, "C", 20, 20, "#000", "center", 600, h=None, cls="p quote-t"))
        out.append(LINE(lx, ly + dy, 217, "#000"))
        return "".join(out)
    ch = [T(396, 104 + dy, 260, "ВІДГУКИ:", "F", 48, 48, head_color, "left", cls="h2")]
    ch.append(S(811, 160 + dy, 270, 412, card_bg))
    ch.append(I(461, 280 + dy, 519, 807, "2/6948180b5a2b8aea0311d229_optimized_914.webp"))
    ch.append(card(0, 0, 824, 242, 824, 270, 243, 204, 836, 481, TESTI["a"], bg=False))
    ch.append(S(276, 511 + dy, 270, 412, card_bg))
    ch.append(card(0, 0, 290, 523, 292, 550, 239, 364, 303, 909, TESTI["b"], bg=False))
    ch.append(S(922, 774 + dy, 270, 412, card_bg))
    ch.append(card(0, 0, 933, 836, 936, 854, 241, 264, 948, 1124, TESTI["c"], bg=False))
    ch.append(card(0, 0, 406, 216, 412, 244, 230, 244, 419, 492, TESTI["d"], bg=False))
    ch.append(card(0, 0, 959, 630, 964, 658, 234, 64, 972, 729, TESTI["e"], bg=False))
    ch.append(card(0, 0, 424, 980, 426, 1008, 239, 64, 437, 1079, TESTI["f"], bg=False))
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
    # B2 hero
    secs.append(SEC(600, [
        I(318, 45, 220, 304, "2/6945c466f079e06014374273_optimized_969.webp", cls="keep mob-hide"),
        T(482, 182, 481, "ВІТАЮ ВАС", "C", 90, 90, "#000", "right", cls="big", tag="h1", extra="margin:0;"),
        T(517, 246, 446, "У СВОЄМУ", "C", 90, 90, "#000", "right", cls="big"),
        T(515, 310, 448, "ПРОСТОРІ", "C", 90, 90, "#000", "right", cls="big"),
    ], bg="#fff"))
    # B3 about
    secs.append(SEC(700, [
        T(368, 202, 300, "Наталя Кочергіна", "C", 40, 52, "#000", "left", cls="h2"),
        T(340, 250, 346, "Я психотерапевт та психодинамічний<br>коуч із практикою понад 10 років", "C", 20, 20, "#757575", "center", 600, cls="p"),
        LINE(434, 322, 158, "#000"),
        T(272, 359, 481, "Мій метод — це тонка робота з особистістю, де поєднуються психоаналіз, коучинг і системне бачення. Я спираюся на повагу до індивідуальності і впевнена, що в кожній людині є прихований потенціал для змін.", "C", 21, 21, "#000", "center", cls="p"),
        BTN(434, 470, 158, 40, "ПРО МЕНЕ", "about.html", "line", "#000", "#000", 15),
        I(937, 62, 383, 575, "2/694e7e27080a9d0140ffdb16_optimized_930.webp", cls="keep", alt="Наталя Кочергіна"),
    ], bg="#fff"))
    # B4 spheres
    rows = [("01", "тіло та здоровʼя", 170), ("02", "гроші, реалізація та особистий потенціал", 207),
            ("03", "лідерство та управління командою", 244), ("04", "сімʼя. стосунки між батьками та дітьми", 285),
            ("05", "любов та стосунки у парі", 322)]
    ch = [T(441, 29, 559, "Я ПРАЦЮЮ ІЗ ЗАПИТАМИ<br>НА ЗМІНИ У ТАКИХ СФЕРАХ:", "F", 48, 48, "#000", "center", cls="h2", tag="h2", extra="margin:0;")]
    for n, t, y in rows:
        ch.append(G(630, y, 570, 33, [
            T(1, 0, 60, n, "F", 25, 28, "#000", cls="p", extra="position:absolute"),
            T(102, 0, 460, t, "F", 25, 28, "#000", cls="p"),
        ], cls="row", extra="border-bottom:1px solid #000;"))
    secs.append(SEC(400, ch, bg="#fff", id="sfery"))
    # B5 grid
    secs.append(SEC(830, [
        I(188, 40, 221, 224, "2/694e7f3bc2c73c4433f45bca_optimized.webp"),
        I(536, 40, 221, 224, "2/694e7f3edc0acba3c58c1825_optimized.webp"),
        I(883, 297, 221, 224, "2/694e7fc8080a9d0140ffdf80_optimized.webp", cls="keep"),
        T(281, 370, 422, "Моє завдання — допомогти вам звільнитися від внутрішніх обмежень і побудувати якісне життя у відповідності до вашого справжнього Я!", "C", 21, 27.3, "#000", "left", cls="p"),
        I(188, 552, 221, 224, "2/694e7fe8dc4fd58c318ee1e6_optimized_572_c572x1024-0x0.webp"),
        I(536, 552, 221, 224, "2/694e7fe9c2c73c4433f45e1d_optimized_572_c572x1024-0x0.webp"),
    ], bgimg="2/6945cfbf364911d845d9da3b_optimized_2560.webp"))
    # B6 services
    cards = [(120, "6947ff97364911d845de49e9_optimized_921.webp", "індивідуальна<br>терапія", 609),
             (520, "694e852edc4fd58c318ef385_optimized.webp", "психодинамічний<br>коучінг", 609),
             (920, "6948002c364911d845de4b73_optimized_921.webp", "групи", 641)]
    ch = [T(120, 88, 1200, "ІНДИВІДУАЛЬНА РОБОТА ЗІ МНОЮ:", "F", 48, 48, "#000", "center", cls="h2", tag="h2", extra="margin:0;")]
    for x, f, t, ty in cards:
        ch.append(G(x, 151, 400, 609, [
            I(0, 0, 400, 609, "2/" + f, cls="keep"),
            T(32, ty - 151, 340, t, "F", 32, 32, "#fff", cls="h2"),
            LINE(30, 534, 339, "#fff"),
            f'<a class="a t" href="{TG_N}" target="_blank" rel="noopener" style="left:30px;top:568px;font-family:var(--forum);font-size:20px;line-height:30px;color:#fff;text-decoration:none">записатися →</a>',
        ], cls="svc"))
    secs.append(SEC(760, ch, bg=CREAM, id="poslugy"))
    # B8 products + seasons (fix: the main project gets room and links to each season)
    ch = [T(604, 84, 231, "ПРОДУКТИ:", "F", 48, 48, "#000", "center", cls="h2", tag="h2", extra="margin:0;"),
          I(120, 222, 490, 350, "1/69dd1850e56bc464c74e3faa_optimized_978_c978x1326-0x0.webp", cls="keep"),
          G(610, 222, 710, 350, [
              T(50, 23, 620, '<a href="svoboda-buty-zhinkoyu.html" style="text-decoration:none">СВОБОДА БУТИ ЖІНКОЮ</a>', "F", 48, 48, "#000", "left", cls="h2"),
              f'<a class="a mob-hide" href="svoboda-buty-zhinkoyu.html" style="left:50px;top:175px"><img src="{img("2/69480f9228ee2c4d3bdc4bad_optimized.webp")}" width="29" height="28" alt=""></a>',
              T(50, 218, 608, "Це трансформаційний жіночий онлайн-простір, де ми повертаємося до своєї  цілісності, звільняємось від очікувань інших  та навʼязаних ролей, знаходимо ресурс та підтримку одна в одній, і будуємо життя за власним сценарієм.", "C", 21, 27.3, "#000", "left", cls="p"),
          ], bg="#fdfff2"),
          T(120, 640, 1200, "ТЕМИ СЕЗОНІВ", "F", 32, 36, "#000", "center", cls="h2")]
    for i, (n, t, s, im, href) in enumerate(SEASON_CARDS):
        x = 120 + i * 244
        ch.append(G(x, 700, 224, 330, [
            I(32, 24, 160, 150, im, cls="keep", extra="object-fit:contain;"),
            T(20, 190, 184, f"Сезон {n}", "F", 16, 18, "#fffaf1", "left", extra="opacity:.6"),
            T(20, 212, 184, t, "F", 22, 24, "#fffaf1", "left", 700),
            T(20, 262, 184, s, "F", 16, 18, "#fffaf1", "left", extra="opacity:.8"),
            f'<a class="a" href="{href}" style="inset:0" aria-label="{t}"></a>',
        ], bg=OLIVE, cls="scard"))
    ch.append(BTN(613, 1070, 213, 50, "ПРО ПРОЄКТ", "svoboda-buty-zhinkoyu.html", "fill", "#000", "#fff", 17, "C", 25))
    secs.append(SEC(1170, ch, bg="#fff", id="produkty"))
    # B9 testimonials
    secs.append(SEC(1333, testimonials("#f8f8f8", dy=94), bg="#fff", id="vidguky"))
    # B11 CTA
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
