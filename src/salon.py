import re
from lib import *
LIGHT = "\x00light\x00"
from home import testimonials, TESTI

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

def blk(h):
    """Light blocks: text in black, like the home page."""
    h = re.sub(r"(?<![-\w])color:#595f45;", "color:#000;", h)
    return h.replace("border:1px solid #595f45;color:#000;", "border:1px solid #000;color:#000;")

def build():
    secs = []
    # B2 hero: one calm composition — words on the left, Natalia in the salon's arch on the right, no frames or plaques
    W = "#fdfbf7"
    secs.append(LIGHT + SEC(660, [
        S(812, 40, 420, 580, "", "1px solid rgba(89,95,69,.45)", extra="border-radius:210px 210px 0 0;", cls="shape arch-line"),
        I(830, 58, 384, 562, "1/69cf722d3782636560075676_optimized.webp", cls="keep sbz-arch", extra="object-fit:cover;object-position:50% 20%;border-radius:192px 192px 0 0;"),
        T(120, 146, 600, "психологічний салон", "F", 18, 22, OLIVE, "left", cls="p", extra="letter-spacing:.2em;text-transform:uppercase;opacity:.8"),
        T(112, 190, 720, "СВОБОДА", "C", 100, 100, "#000", "left", cls="big", tag="h1", extra="margin:0;"),
        T(112, 290, 720, "БУТИ ЖІНКОЮ", "C", 100, 100, "#000", "left", italic=True, cls="big"),
        T(120, 414, 600, "by Natalia Kocherhina", "C", 24, 28, "#000", "left", 500, italic=True, cls="p", extra="opacity:.7"),
        BTN(120, 478, 190, 52, "ПРОГРАМА", "#temy", "line", "#000", "#000", 17, "C", 26),
        BTN(330, 478, 210, 52, "ВЗЯТИ УЧАСТЬ", "#vartist", "fill", OLIVE, W, 17, "C", 26),
    ], bg=W, cls="m-sbzh"))
    # B3 mothers: set like a page of a book (as on the season pages), the turn of the thought pulled out
    secs.append(f'''<section class="ed-story ink sbz-book"><div class="wrap ed-story-in"><div class="ed-text">
<p>Наші мами передали нам свої жіночі стратегії: бути «зручними», терплячими, чимось поступатись або «тягнути все на собі».</p>
<p class="ed-pull">Але світ змінився, тепер ми маємо вибір і хочемо жити по іншому.</p></div>
<figure class="ed-art"><img src="{img("1/69cf76daeecd0ca270892e11_optimized.webp")}" alt="" loading="lazy"></figure></div></section>''')
    # B4 we want it all: the four wishes as a quiet 2x2 list on hairlines, no stickers or brackets
    wants = ["свої бажання та реалізацію без вигорання",
             "отримувати турботу від чоловіка і відчувати цінність в стосунках",
             "жити в розслабленому, здоровому тілі",
             "бути мамами, але мати час для себе без провини"]
    ch = [I(120, 93, 435, 594, "1/69d1520aee8819f70862b88b_optimized.webp", cls="keep mob-hide"),
          T(680, 96, 540, "МИ ХОЧЕМО МАТИ<br><i>ВСЕ Й ОДРАЗУ:</i>", "F", 44, 50, "#000", "left", cls="h2", tag="h2", extra="margin:0;")]
    for i, t in enumerate(wants):
        x = 680 + (i % 2) * 290; y = 260 + (i // 2) * 140
        ch.append(G(x, y, 250, 110, [T(0, 22, 250, t, "C", 23, 30, "#000", "left", 500, cls="p")], cls="want",
                    extra="border-top:1px solid rgba(89,95,69,.35);"))
    ch.append(T(680, 570, 540, "Це стає можливим, коли ми злагоджені із собою і своїм внутрішнім центром.", "C", 28, 36, OLIVE, "left", 500, italic=True, cls="p"))
    secs.append(LIGHT + SEC(780, ch, bg=CREAM))
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
    secs.append(LIGHT + SEC(1653, seasons_block(), bg=CREAM, id="temy"))
    # B9 guests (the philosophy plaque is gone)
    secs.append(LIGHT + SEC(300, [
        T(333, 1, 774, "До проекту будуть запрошені гості-експерти під запити учасниць.", "F", 28, 33.6, OLIVE, "center", cls="p"),
        I(437, 73, 550, 176, "1/69cf959e02d98a0e80c344b2_optimized.webp"),
    ], bg=CREAM))
    # B10 price
    feats = ["8 тижнів занурення в тему", "Доступ до записів лекцій та вправ", "Підтримуюча група в Телеграм каналі", "Живі групи з автором"]
    fch = []
    for i, f in enumerate(feats):
        fch.append(S(60, 126 + i * 37, 20, 20, OLIVE, cls="star"))
        fch.append(T(90, 125 + i * 37, 340, f, "F", 20, 22, OLIVE, "left", cls="p"))
    secs.append(LIGHT + SEC(700, [
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
    secs.append(LIGHT + SEC(800, [
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
    keys = "bdacef"
    slides = "".join(f'<blockquote class="ed-slide{" on" if i == 0 else ""}">{TESTI[k]}</blockquote>' for i, k in enumerate(keys))
    secs.append(f'''<section class="ed-rev ink" id="vidguky"><div class="wrap"><p class="ed-k">Відгуки</p>
<div class="ed-car" data-car><div class="ed-slides">{slides}</div>
<div class="ed-ctl"><button type="button" data-prev aria-label="Попередній відгук">←</button><span class="ed-cnt"><b>01</b> / {len(keys):02d}</span><button type="button" data-next aria-label="Наступний відгук">→</button></div></div></div></section>''')
    # B16 final CTA
    secs.append(LIGHT + SEC(700, [
        I(-37, 32, 622, 466, "1/69cfa4e7eecd0ca27089f7c3_optimized_1304_flop.webp"),
        I(911, 181, 491, 391, "1/69cfa2feeecd0ca27089eec7_optimized_833_flop.webp"),
        G(415, 169, 610, 362, [
            T(0, 48, 610, "НЕ ТРЕБА<br><i>ВІДМОВЛЯТИСЬ</i>", "F", 48, 48, OLIVE, "center", cls="h2"),
            T(0, 159, 610, "Якщо в цьому світі щось є -<br>ви можете це мати.", "F", 28, 28, OLIVE, "center", cls="p"),
            BTN(173, 262, 264, 50, "НАПИСАТИ МЕНЕДЖЕРУ", TG_M, "fill", OLIVE, "#fff", 15, "C", 25, 'target="_blank" rel="noopener"', arrow=True),
        ], bg=CREAM),
    ], bgimg="1/69cfa4c47ed93e76919e7f1b_optimized_1920.webp", bgpos="53.44% 45.28%"))
    secs = [blk(x[len(LIGHT):]) if x.startswith(LIGHT) else x for x in secs]
    # Small Forum body text -> Cormorant 500 like the home page (not in the season cards or the author card, which are sized for Forum)
    swap = lambda h: re.sub(r"font-family:var\(--forum\);font-size:20px;line-height:2[02]px;(color:[^;]*;text-align:[^;]*;)font-weight:400;",
                            r"font-family:var(--corm);font-size:22px;line-height:25px;\1font-weight:500;", h)
    body = "".join(x if ('id="temy"' in x or "Наталя Кочергіна" in x) else swap(x) for x in secs)
    # Warm white instead of the yellow cream
    body = body.replace("#fffaf1", "#fdfbf7")
    return page("Свобода бути жінкою — жіночий онлайн-простір Наталі Кочергіної",
                "Трансформаційний жіночий онлайн-простір: 5 сезонів по 8 тижнів, лекції, вправи та живі групи з психотерапевткою Наталею Кочергіною.",
                body, "svoboda-buty-zhinkoyu.html")

SEASONS = [
    # y, card h, title, small, desc lines, status, status kind, image, img rect (x,y,w,h), page, pay
    dict(n=1, y=207, h=205, title="Стосунки з собою", small="",
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
    for k, s in enumerate(SEASONS):
        sh = 14 * k  # each card grew by 14px for its "Сезон N" label
        x0, y0, hh = 302, s["y"] + sh, s["h"] + 14
        ix, iy, iw, ih = s["ir"]; iy += sh + 7
        t = f'{s["title"]} <span style="font-size:24px">{s["small"]}</span>' if s["small"] else s["title"]
        kids = [
            T(60, 24, 560, f"СЕЗОН {s['n']}", "F", 13, 16, C, "left", cls="p skick", extra="letter-spacing:.22em;opacity:.6"),
            T(60, 45, 560, f'<a href="{s["page"]}" style="text-decoration:none">{t}</a>', "F", 28, 33.6, C, "left", 700, cls="h2", tag="h3", extra="margin:0;"),
            T(60, 85, 560, s["desc"], "F", 20, 20, C, "left", cls="p"),
            T(60, hh - 106, 560, s["status"], "F", 20, 22, "rgba(255,250,241,.75)", "left", cls="p"),
            BTN(60, hh - 65, 142, 35, "ДЕТАЛЬНІШЕ", s["page"], "line", C, C, 15),
        ]
        if s["kind"] == "repeat":
            kids.append(BTN(222, hh - 65, 220, 35, "ЗАЯВКА НА ПОВТОР", "#zayavka", "fill", C, OLIVE, 15, attrs=f'data-apply="{s["n"]}"'))
        else:
            kids.append(BTN(222, hh - 65, 156, 35, "ПРИЄДНАТИСЯ", s["pay"], "line", C, C, 15, attrs='target="_blank" rel="noopener"'))
        kids.append(I(ix - x0, iy - y0, iw, ih, s["img"], cls="keep mob-hide", extra="object-fit:contain;"))
        ch.append(G(x0, y0, 836, hh, kids, bg=OLIVE, cls="scard"))
    ch.append(I(545, 1478, 350, 38, "1/69cf9218eecd0ca27089a59b_optimized_1045_flip.webp"))
    ch.append(T(302, 1550, 836, "Кожен сезон — окрема сторінка з програмою, форматом і відгуками. Натисніть «Детальніше».", "F", 20, 22, OLIVE, "center", cls="p", extra="opacity:.7"))
    return ch
