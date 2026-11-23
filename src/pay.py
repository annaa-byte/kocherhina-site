"""Thank-you and failed-payment pages, one pair per season (set as returnUrl / failure page on each WayForPay button)."""
from lib import *
from salon import SEASONS, TG_M

START = {3: "у березні 2027", 4: "у червні 2027", 5: "у вересні 2027"}

def _wrap(title, inner):
    body = f'<section class="pay-res"><div class="wrap">{inner}</div></section>'
    return page(title, title, body).replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)

def ok(s):
    n, t = s["n"], s["title"].rstrip(":")
    when = f"Старт {START[n]}. " if n in START else ""
    inner = (f'<p class="ed-k">Сезон {n} · {t}</p><h1>Оплату отримано.<br><i>Ласкаво просимо!</i> 🤍</h1>'
             f'<p>Дякуємо, що обрали цей сезон. {when}Протягом доби менеджерка напише вам у Telegram і надішле всі деталі та доступи.</p>'
             f'<p>Якщо маєте питання вже зараз, напишіть нам.</p>'
             f'<div class="pay-btns"><a class="hm-btn" href="{TG_M}" target="_blank" rel="noopener">Написати менеджеру</a>'
             f'<a class="hm-btn ln" href="{s["page"]}">Про сезон</a></div>')
    return _wrap(f"Оплату отримано — Сезон {n}. {t}", inner)

def fail(s):
    n, t = s["n"], s["title"].rstrip(":")
    retry = s.get("pay") or s["page"]
    inner = (f'<p class="ed-k">Сезон {n} · {t}</p><h1>Оплата <i>не пройшла</i></h1>'
             f'<p>Схоже, платіж не завершився. Таке трапляється: банк міг відхилити операцію або зʼєднання перервалося.</p>'
             f'<p>Спробуйте ще раз або напишіть менеджерці, і ми допоможемо.</p>'
             f'<div class="pay-btns"><a class="hm-btn" href="{retry}"{" target=\"_blank\" rel=\"noopener\"" if s.get("pay") else ""}>Спробувати ще раз</a>'
             f'<a class="hm-btn ln" href="{TG_M}" target="_blank" rel="noopener">Написати менеджеру</a></div>')
    return _wrap(f"Оплата не пройшла — Сезон {n}. {t}", inner)

def pages():
    out = {}
    for s in SEASONS:
        out[f"oplata-sezon-{s['n']}-uspih.html"] = ok(s)
        out[f"oplata-sezon-{s['n']}-pomylka.html"] = fail(s)
    return out
