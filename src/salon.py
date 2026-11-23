from lib import *
from home import testimonials

TG_M = "https://t.me/pnm_a"
STAR = "star"

def hero(ch_extra=None, photo="1/69cf722d3782636560075676_optimized.webp", title=None, sub="психологічний салон",
         byline="by Natalia Kocherhina", buttons=None, photo_fit="cover", photo_box=(903, 120, 297, 360)):
    ch = [I(120, 30, 375, 540, "1/69cf74dc7ed93e76919db552_optimized.webp"),
          I(945, 30, 375, 540, "1/69cf74dc7ed93e76919db552_optimized_670_flop.webp"),
          S(200, 80, 1040, 440, CREAM, cls="shape")]
    ch.append(T(244, 120, 560, sub, "F", 28, 33.6, OLIVE, "center", cls="p"))
    ch += title
    ch.append(T(244, 383, 560, byline, "F", 28, 33.6, OLIVE, "center", cls="p"))
    ch += buttons
    ch.append(I(*photo_box, photo, cls="keep hero-art", extra=f"object-fit:{photo_fit};object-position:50% 100%;"))
    return ch

def build():
    secs = []
    # B2 hero
    title = [T(326, 151, 422, "СВОБОДА", "C", 90, 90, OLIVE, "right", cls="big", tag="h1", extra="margin:0;"),
             T(281, 215, 208, "БУТИ", "C", 90, 90, OLIVE, "left", italic=True, cls="big"),
             T(425, 279, 362, "ЖІНКОЮ", "C", 90, 90, OLIVE, "right", italic=True, cls="big")]
    buttons = [BTN(361, 441, 135, 47, "ПРОГРАМА", "#temy", "line", OLIVE, OLIVE, 16.5),
               BTN(535, 441, 152, 45, "ВЗЯТИ УЧАСТЬ", "#vartist", "fill", OLIVE, "#fff", 15)]
    secs.append(SEC(600, hero(title=title, buttons=buttons), bg=OLIVE, mbg=CREAM, cls="m-shero"))
    # B3 mothers
    secs.append(SEC(466, [
        T(207, 82, 560, "Наші мами передали нам свої жіночі стратегії:<br>бути «зручними», терплячими, чимось поступатись або «тягнути все на собі».", "F", 28, 33.6, OLIVE, "left", cls="p", extra="max-width:540px"),
        T(207, 216, 520, "Але світ змінився, тепер ми маємо вибір<br>і хочемо жити по іншому.", "F", 28, 33.6, OLIVE, "left", cls="p"),
        I(743, 37, 588, 395, "1/69cf76daeecd0ca270892e11_optimized.webp", cls="keep"),
    ], bg=CREAM))
    # B4 we want it all
    SHIP = "1/69cf7a9deecd0ca2708941e6_optimized.webp"
    wants = [(666, 240, 764, 193, "свої бажання та реалізацію без вигорання"),
             (1044, 241, 1142, 193, "отримувати турботу від чоловіка і відчувати цінність в стосунках"),
             (666, 418, 764, 370, "жити в розслабленому, здоровому тілі"),
             (1044, 418, 1142, 370, "бути мамами, але мати час для себе без провини")]
    ch = [I(120, 93, 435, 594, "1/69d1520aee8819f70862b88b_optimized.webp", cls="keep mob-hide"),
          T(760, 78, 466, "МИ ХОЧЕМО МАТИ<br><i>ВСЕ Й ОДРАЗУ:</i>", "F", 48, 48, OLIVE, "center", cls="h2", tag="h2", extra="margin:0;")]
    for cx, cy, sx, sy, t in wants:
        ch.append(G(cx, cy, 276, 108, [T(24, 0, 228, t, "C", 21, 21, "#000", "center", cls="p",
                                          extra="height:108px;display:flex;align-items:center;justify-content:center")], bg="#fff"))
        ch.append(I(sx, sy, 79, 63, SHIP))
    ch += [I(666, 587, 20, 100, "1/69cf7c0c3782636560077fa6_optimized.webp"),
           T(760, 586, 466, "Це стає можливим, коли<br>ми злагоджені із собою<br>і своїм внутрішнім центром.", "F", 28, 28, OLIVE, "center", cls="p"),
           I(1300, 587, 20, 100, "1/69cf7c0c3782636560077fa6_optimized_34_flop.webp")]
    secs.append(SEC(799, ch, bg=CREAM))
    # B6 about the project
    secs.append(SEC(800, [
        I(411, 20, 619, 761, "1/69cf7efa7ed93e76919ddebb_optimized_1028.webp"),
        S(-1, 114, 1442, 572, "#fff5e7"),
        T(520, 131, 400, "ПРО ПРОЄКТ", "F", 48, 48, OLIVE, "center", cls="h2", tag="h2", extra="margin:0;"),
        T(209, 209, 1022, "Це трансформаційний жіночий онлайн-простір, де ми повертаємося до своєї цілісності, звільняємось від очікувань інших та навʼязаних ролей, знаходимо ресурс та підтримку одна в одній, і будуємо життя за власним сценарієм.", "F", 28, 30.8, OLIVE, "center", cls="p"),
        I(537, 346, 367, 390, "1/69cf7fc623efa9cc4460cee1_optimized.webp", cls="keep"),
    ], bg=OLIVE, id="pro-proekt", mbg="#fff5e7"))
    # B7 why salon / format / structure
    C = "#fffaf1"
    secs.append(SEC(550, [
        T(120, 72, 520, "ЧОМУ САМЕ «САЛОН»?", "F", 48, 48, C, "left", cls="h2", tag="h2", extra="margin:0;"),
        T(120, 140, 413, "Бо салонну культуру колись створили саме жінки, як простір свободи від жорстких норм і правил.", "F", 20, 20, C, "left", cls="p"),
        I(821, -33, 398, 265, "1/69cf80ffeecd0ca2708958d0_optimized.webp"),
        I(120, 254, 300, 69, "1/69cf83efeecd0ca2708963b1_optimized.webp"),
        T(120, 262, 300, "ФОРМАТ", "F", 48, 48, C, "center", cls="h2"),
        T(120, 341, 406, "Лекції в записі, вправи, техніки та живі групові зустрічі для глибокої зміни мислення та взаємної підтримки.", "F", 20, 20, C, "left", cls="p"),
        T(120, 421, 406, "Робота на базі глибинної психології.", "F", 20, 20, C, "left", cls="p"),
        I(720, 254, 300, 69, "1/69cf83efeecd0ca2708963b1_optimized.webp"),
        T(720, 263, 300, "СТРУКТУРА", "F", 48, 48, C, "center", cls="h2"),
        G(720, 341, 600, 30, [T(2, 0, 90, "1 сезон", "F", 20, 22, C), T(103, 0, 480, "досліджуємо та змінюємо 1 сферу життя.", "F", 20, 22, C)], cls="row"),
        LINE(720, 369, 600, C),
        G(720, 395, 600, 50, [T(2, 0, 90, "8 тижнів", "F", 20, 22, C), T(103, 0, 480, "тривалість сезону", "F", 20, 22, C),
                              T(103, 24, 480, "1 лекція і 1 жива група на тиждень", "F", 20, 22, "rgba(255,250,241,.4)")], cls="row"),
        LINE(720, 442, 600, C),
    ], bg=OLIVE))
    # B8 seasons (fixed: real pages, current statuses, apply-for-repeat)
    secs.append(SEC(1583, seasons_block(), bg=CREAM, id="temy"))
    # B9 guests + philosophy
    secs.append(SEC(844, [
        T(333, 1, 774, "До проекту будуть запрошені гості-експерти під запити учасниць.", "F", 28, 33.6, OLIVE, "center", cls="p"),
        I(437, 73, 550, 176, "1/69cf959e02d98a0e80c344b2_optimized.webp"),
        S(302, 221, 836, 205, "#555b41"),
        I(302, 161, 836, 89, "1/69cf95467ed93e76919e3d14_optimized_3491.webp"),
        I(302, 397, 836, 89, "1/69cf95467ed93e76919e3d14_optimized_3491_flip.webp"),
        I(455, 263, 514, 65, "1/69cf94ceeecd0ca27089b1ab_optimized.webp"),
        T(455, 269, 514, "Філософія проекту:", "F", 48, 48, C, "center", cls="h2"),
        T(482, 351, 476, "підтримуюче коло жінок без конкуренції", "F", 28, 33.6, C, "center", cls="p"),
        I(487, 361, 450, 428, "1/69cf95e77ed93e76919e4019_optimized.webp"),
    ], bg=CREAM, cls="philo", mbg="#555b41"))
    # B10 price
    feats = ["8 тижнів занурення в тему", "Доступ до записів лекцій та вправ", "Підтримуюча група в Телеграм каналі", "Живі групи з автором"]
    fch = []
    for i, f in enumerate(feats):
        fch.append(S(60, 126 + i * 37, 20, 20, OLIVE, cls="star"))
        fch.append(T(90, 125 + i * 37, 340, f, "F", 20, 22, OLIVE, "left", cls="p"))
    secs.append(SEC(700, [
        T(420, 57, 600, "<i>ВАРТІСТЬ</i> ТА УЧАСТЬ", "F", 48, 48, C, "center", cls="h2", tag="h2", extra="margin:0;"),
        T(420, 116, 600, "Кожен сезон можна придбати окремо", "F", 20, 22, C, "center", cls="p"),
        G(301, 190, 838, 318, [T(60, 58, 400, "Єдиний тариф:", "F", 48, 53, OLIVE, "left", cls="h2")] + fch + [
            T(500, 58, 266, "Ціна за сезон<br>200$", "F", 48, 48, OLIVE, "center", cls="h2"),
            T(500, 165, 266, "Можливе розтермінування", "F", 20, 22, "rgba(89,95,69,.5)", "center", cls="p"),
            BTN(502, 218, 272, 45, "ВЗЯТИ УЧАСТЬ", "#temy", "fill", OLIVE, "#fff", 15),
        ], bg=CREAM),
        T(320, 560, 800, "КІЛЬКІСТЬ МІСЦЬ <i>ОБМЕЖЕНА</i>", "F", 48, 53, C, "center", cls="h2"),
        T(420, 619, 600, "для збереження камерної атмосфери", "F", 20, 22, C, "center", cls="p"),
    ], bg=OLIVE, id="vartist"))
    # B11 author
    secs.append(SEC(800, [
        I(597, 4, 846, 791, "1/69cfa064eecd0ca27089e355_optimized.webp", cls="keep", extra="object-fit:contain;object-position:bottom right"),
        G(120, 145, 838, 442, [
            T(54, 51, 500, "Наталя Кочергіна", "F", 48, 53, OLIVE, "left", italic=True, cls="h2"),
            T(55, 117, 599, "Психоаналітичний психотерапевт, груповий терапевт, психодинамічний коуч та консультант організацій, тренер, розробник тренінгових програм, автор групових трансформаційних програм.", "F", 20, 20, OLIVE, "left", cls="p"),
            LINE(54, 211, 606, OLIVE),
            I(41, 215, 87, 130, "1/69cf9ea637826365600812f4_optimized.webp"),
            G(158, 240, 160, 100, [T(0, 0, 160, "10", "F", 48, 53, OLIVE, "left", italic=True), T(0, 49, 90, "років практики", "F", 20, 20, OLIVE)], cls="row"),
            G(365, 240, 220, 100, [T(0, 0, 220, "4000+", "F", 48, 53, OLIVE, "left", italic=True), T(0, 49, 190, "годин теоретичної та практичної підготовки", "F", 20, 20, OLIVE)], cls="row"),
            LINE(54, 342, 606, OLIVE),
            f'<a class="a t" href="about.html" style="left:54px;top:385px;font-family:var(--forum);font-size:16.5px;color:#000;text-decoration:none">ДІЗНАТИСЬ БІЛЬШЕ</a>',
        ], bg=CREAM),
    ], bgimg="1/69cf9d22eecd0ca27089d4af_optimized_1920.webp"))
    # B13 invitation
    secs.append(SEC(844, [
        T(120, 97, 400, "<i>Ваше життя —</i>", "F", 48, 53, C, "left", cls="h2"),
        T(150, 157, 519, "не заздалегідь прописаний сценарій,<br>а ваш власний творчий проект.", "F", 28, 33.6, C, "right", cls="p"),
        I(126, 202, 485, 327, "1/69cfa3e0eecd0ca27089f36d_optimized.webp"),
        T(120, 503, 520, "Запрошую вас у простір<br>жіночої підтримки та натхнення,<br>щоб створити свій авторський шедевр!", "F", 28, 33.6, C, "left", cls="p"),
        BTN(120, 653, 232, 45, "ВЗЯТИ УЧАСТЬ", "#temy", "fill", C, "#000", 15),
    ], bgimg="1/69cfa37123efa9cc4461697a_optimized_1920.webp"))
    # B14 testimonials
    secs.append(SEC(1470, testimonials("#fff", 0), bg=CREAM, id="vidguky", cls="m-testi"))
    # B16 final CTA
    secs.append(SEC(700, [
        I(-37, 32, 622, 466, "1/69cfa4e7eecd0ca27089f7c3_optimized_1304_flop.webp"),
        I(911, 181, 491, 391, "1/69cfa2feeecd0ca27089eec7_optimized_833_flop.webp"),
        G(415, 169, 610, 362, [
            T(0, 48, 610, "НЕ ТРЕБА<br><i>ВІДМОВЛЯТИСЬ</i>", "F", 48, 48, OLIVE, "center", cls="h2"),
            T(0, 159, 610, "Якщо в цьому світі щось є -<br>ви можете це мати.", "F", 28, 28, OLIVE, "center", cls="p"),
            BTN(173, 262, 264, 50, "НАПИСАТИ МЕНЕДЖЕРУ", TG_M, "fill", OLIVE, "#fff", 15, "C", 25, 'target="_blank" rel="noopener"', arrow=True),
        ], bg=CREAM),
    ], bgimg="1/69cfa4c47ed93e76919e7f1b_optimized_1920.webp", bgpos="53.44% 45.28%"))
    body = "".join(secs)
    return page("Свобода бути жінкою — жіночий онлайн-простір Наталі Кочергіної",
                "Трансформаційний жіночий онлайн-простір: 5 сезонів по 8 тижнів, лекції, вправи та живі групи з психотерапевткою Наталею Кочергіною.",
                body, "svoboda-buty-zhinkoyu.html")

SEASONS = [
    # y, card h, title, small, desc lines, status, status kind, image, img rect (x,y,w,h), page, pay
    dict(n=1, y=207, h=205, title="Стосунки з собою", small="(повторення)",
         desc="Цінність, самооцінка, авторський сценарій життя.",
         status="Повтор сезону завершився. Залиште заявку на наступний потік", kind="repeat",
         img="1/69cf907e02d98a0e80c32e0c_optimized.webp", ir=(941, 213, 161, 192), page="season-1.html"),
    dict(n=2, y=433, h=231, title="Стосунки у парі:", small="Power Couple",
         desc="Як  побудувати союз із чоловіком<br>за принципом «Power Couple».",
         status="Сезон іде зараз, з 19 жовтня. Залиште заявку на повтор", kind="repeat",
         img="L/power-couple.webp", ir=(918, 445, 192, 206), page="season-2.html"),
    dict(n=3, y=685, h=231, title="Гроші та реалізація:", small="",
         desc="Жіночі стратегії успіху без вигорання.<br>Стосунки з грошима. Грошові архетипи.",
         status="Старт запланований на березень 2027 року", kind="pay", pay="https://secure.wayforpay.com/button/bc93fb11f23a3",
         img="1/69cf92ec378263656007dff2_optimized.webp", ir=(918, 712, 192, 176), page="season-3.html"),
    dict(n=4, y=936, h=230, title="Тіло та здоров'я:", small="",
         desc="Розслаблення в період турбулентності, сексуальність та індивідуальна система турботи. Психосоматика. Стосунки з їжею.",
         status="Старт запланований на червень 2027 року", kind="pay", pay="https://secure.wayforpay.com/button/be8b6db315e1a",
         img="1/69cf927ceecd0ca27089a758_optimized.webp", ir=(947, 958, 175, 184), page="season-4.html"),
    dict(n=5, y=1186, h=230, title="Імідж та краса:", small="",
         desc="Як внутрішній стан змінює сприйняття нас іншими людьми.<br>Імідж, як інструмент досягнення цілей в соціумі.",
         status="Старт запланований на вересень 2027 року", kind="pay", pay="https://secure.wayforpay.com/button/b45d80f803d42",
         img="1/69cf93237ed93e76919e3406_optimized.webp", ir=(962, 1194, 150, 205), page="season-5.html"),
]

def seasons_block():
    C = "#fffaf1"
    ch = [T(420, 71, 600, "ТЕМИ СЕЗОНІВ", "F", 48, 53, OLIVE, "center", cls="h2", tag="h2", extra="margin:0;"),
          I(545, 180, 350, 38, "1/69cf9218eecd0ca27089a59b_optimized.webp")]
    for s in SEASONS:
        x0, y0 = 302, s["y"]
        ix, iy, iw, ih = s["ir"]
        t = f'{s["title"]} <span style="font-size:24px">{s["small"]}</span>' if s["small"] else s["title"]
        kids = [
            T(60, 31, 560, f'<a href="{s["page"]}" style="text-decoration:none">{t}</a>', "F", 28, 33.6, C, "left", 700, cls="h2", tag="h3", extra="margin:0;"),
            T(60, 71, 560, s["desc"], "F", 20, 20, C, "left", cls="p"),
            T(60, s["h"] - 106, 560, s["status"], "F", 20, 22, "rgba(255,250,241,.75)", "left", cls="p"),
            BTN(60, s["h"] - 65, 142, 35, "ДЕТАЛЬНІШЕ", s["page"], "line", C, C, 15),
        ]
        if s["kind"] == "repeat":
            kids.append(BTN(222, s["h"] - 65, 220, 35, "ЗАЯВКА НА ПОВТОР", "#zayavka", "fill", C, OLIVE, 15, attrs=f'data-apply="{s["n"]}"'))
        else:
            kids.append(BTN(222, s["h"] - 65, 156, 35, "ПРИЄДНАТИСЯ", s["pay"], "line", C, C, 15, attrs='target="_blank" rel="noopener"'))
        kids.append(I(ix - x0, iy - y0, iw, ih, s["img"], cls="keep mob-hide", extra="object-fit:contain;"))
        ch.append(G(x0, y0, 836, s["h"], kids, bg=OLIVE, cls="scard"))
    ch.append(I(545, 1408, 350, 38, "1/69cf9218eecd0ca27089a59b_optimized_1045_flip.webp"))
    ch.append(T(302, 1480, 836, "Кожен сезон — окрема сторінка з програмою, форматом і відгуками. Натисніть «Детальніше».", "F", 20, 22, OLIVE, "center", cls="p", extra="opacity:.7"))
    return ch
