# Tiny generator for the kocherhina.com copy.
# Desktop: absolute layout on a 1440px stage (coordinates captured from the original site).
# Narrow screens: stage is zoomed to fit; phones (<760px) switch to a stacked flow layout.
import html, os, time
VER = str(int(time.time()))

R1 = "https://res2.weblium.site/res/65ea13810e98e1000fe2502b/"
R2 = "https://res2.weblium.site/res/6945bd72725a016acbb5e84d/"
LOCAL = os.environ.get("LOCAL_IMG") == "1"

def img(name):
    """name like '1/69cf...webp' (R1) or '2/6945...webp' (R2)."""
    k, f = name.split("/", 1)
    if LOCAL:
        return "img/" + f
    return (R1 if k == "1" else R2) + f

OLIVE = "#595f45"; CREAM = "#fffaf1"; CREAM2 = "#fff5e7"

def st(x, y, w=None, h=None, extra=""):
    s = f"left:{x}px;top:{y}px;"
    if w is not None: s += f"width:{w}px;"
    if h is not None: s += f"height:{h}px;"
    return s + extra

def T(x, y, w, text, font="F", size=20, lh=None, color="#000", align="left",
      weight=400, italic=False, h=None, cls="", tag="div", extra=""):
    fam = "var(--forum)" if font == "F" else "var(--corm)"
    lh = lh if lh is not None else size
    style = st(x, y, w, h, f"font-family:{fam};font-size:{size}px;line-height:{lh}px;color:{color};text-align:{align};font-weight:{weight};" + ("font-style:italic;" if italic else "") + extra)
    return f'<{tag} class="a t {cls}" style="{style}">{text}</{tag}>'

def I(x, y, w, h, name, cls="deco", alt="", extra=""):
    return f'<img class="a {cls}" style="{st(x, y, w, h, extra)}" src="{img(name)}" alt="{html.escape(alt)}" loading="lazy">'

def S(x, y, w, h, bg="", border="", radius=0, cls="shape", extra=""):
    s = st(x, y, w, h)
    if bg: s += f"background:{bg};"
    if border: s += f"border:{border};"
    if radius: s += f"border-radius:{radius}px;"
    return f'<div class="a {cls}" style="{s}{extra}"></div>'

def LINE(x, y, w, color="#000", cls="deco"):
    # original dividers are 9px-high svgs with a 1px stroke in the middle
    return f'<div class="a line {cls}" style="{st(x, y + 4, w, 1)}background:{color}"></div>'

def BTN(x, y, w, h, label, href, kind="fill", color=OLIVE, text="#fff", size=15, font="F", radius=20, attrs="", arrow=False):
    fam = "var(--forum)" if font == "F" else "var(--corm)"
    if kind == "fill":
        s = f"background:{color};border:1px solid {color};color:{text};"
    else:
        s = f"background:transparent;border:1px solid {color};color:{text};"
    ar = f'<span class="arr" style="color:{color}">↗</span>' if arrow else ""
    return (f'<a class="a btn" href="{href}" {attrs} style="{st(x, y, w, h)}{s}border-radius:{radius}px;'
            f'font-family:{fam};font-size:{size}px;">{label}{ar}</a>')

def G(x, y, w, h, children, bg="", cls="", extra=""):
    s = st(x, y, w, h)
    if bg: s += f"background:{bg};"
    return f'<div class="a grp {cls}" style="{s}{extra}">' + "".join(children) + "</div>"

def SEC(h, children, bg="", bgimg=None, bgpos="50% 50%", id="", cls="", mbg=""):
    s = f"--h:{h}px;"
    if mbg: s += f"--mbg:{mbg};"; cls += " hasmbg"
    if bg: s += f"background-color:{bg};"
    if bgimg: s += f"background-image:url('{img(bgimg)}');background-size:cover;background-position:{bgpos};"
    i = f' id="{id}"' if id else ""
    return f'<section class="sec {cls}"{i} style="{s}"><div class="stage">' + "".join(children) + "</div></section>"

MENU = [("ПРО МЕНЕ", "about.html"), ("СФЕРИ", "index.html#sfery"), ("ПОСЛУГИ", "index.html#poslugy"),
        ("СВОБОДА БУТИ ЖІНКОЮ", "svoboda-buty-zhinkoyu.html"), ("ВІДГУКИ", "index.html#vidguky")]

def header(active=""):
    items = "".join(f'<a href="{h}"{" class=on" if h == active else ""}>{t}</a>' for t, h in MENU)
    return f'''<header class="hdr"><div class="hin">
<a class="logo" href="index.html">НАТАЛЯ КОЧЕРГІНА</a>
<button class="burger" aria-label="Меню" onclick="document.body.classList.toggle('menu-open')"><span></span><span></span></button>
<nav>{items}</nav></div></header>'''

def footer():
    return '''<footer class="ftr"><div class="fin">
<div class="fcol"><a class="logo" href="index.html">НАТАЛЯ КОЧЕРГІНА</a>
<p>Психоаналітичний психотерапевт, груповий терапевт, психодинамічний коуч</p></div>
<div class="fcol"><a href="about.html">Про мене</a><a href="svoboda-buty-zhinkoyu.html">Свобода бути жінкою</a><a href="index.html#poslugy">Послуги</a><a href="index.html#vidguky">Відгуки</a></div>
<div class="fcol"><a href="https://t.me/Kocher_Nataly" target="_blank" rel="noopener">Telegram: @Kocher_Nataly</a><a href="oferta.html">Публічна оферта</a><a href="privacy.html">Політика конфіденційності</a></div>
</div><div class="fbot">© 2026 Наталя Кочергіна</div></footer>'''

SEASON_OPTS = [("1", "Сезон 1. Стосунки з собою"), ("2", "Сезон 2. Стосунки у парі (Power Couple)"),
               ("3", "Сезон 3. Гроші та реалізація"), ("4", "Сезон 4. Тіло та здоров'я"),
               ("5", "Сезон 5. Імідж та краса")]

def modal():
    opts = "".join(f'<option value="{v}">{t}</option>' for v, t in SEASON_OPTS)
    return f'''<div class="modal" id="apply" aria-hidden="true" role="dialog" aria-labelledby="apply-t">
<div class="mbox"><button class="mx" aria-label="Закрити" data-close>×</button>
<div id="apply-form-wrap">
<h2 id="apply-t">ЗАЯВКА <i>НА ПОВТОР</i></h2>
<p class="msub">Залиште контакт, і менеджер напише вам, щойно відкриється набір на наступний потік.</p>
<form id="apply-form" novalidate>
<label>Ім'я<input name="name" autocomplete="given-name" required></label>
<label>Telegram або телефон<input name="contact" placeholder="@username" required></label>
<label>Сезон<select name="season">{opts}<option value="all">Ще не вирішила, розкажіть про всі</option></select></label>
<label>Коментар (необов'язково)<textarea name="note" rows="3"></textarea></label>
<label class="chk"><input type="checkbox" name="agree" required> Погоджуюся з <a href="privacy.html" target="_blank">політикою конфіденційності</a></label>
<p class="ferr" hidden>Заповніть ім'я, контакт і поставте галочку згоди.</p>
<button class="pill" type="submit">ЗАЛИШИТИ ЗАЯВКУ</button>
</form></div>
<div id="apply-done" hidden><h2>ДЯКУЄМО!</h2><p class="msub" id="apply-done-t"></p></div>
</div></div>'''

def page(title, desc, body, active="", path=""):
    return f'''<!doctype html>
<html lang="uk"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#595f45">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300;0,400;0,600;0,700;1,400;1,600&family=Forum&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={VER}">
</head><body>
{header(active)}
<main>{body}</main>
{footer()}
{modal()}
<script src="site.js?v={VER}"></script>
</body></html>'''
