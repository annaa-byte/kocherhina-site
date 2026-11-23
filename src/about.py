from lib import *

RED = "#780201"

EDU = [
 ("b", "Міжнародний інститут глибинної психології"),
 ("p", "Психоаналітична освіта (спеціальність: практична психологія, спеціалізація: психоаналіз)"),
 ("p", "Обсяг: 1904 години"),
 ("gap", ""),
 ("b", "Sigmund Freud University (Відень / Київ)"),
 ("p", "• Postgraduate Seminar in Psychotherapy – Modern Psychoanalysis | 28 червня – 2 липня 2021 | 25 годин"),
 ("p", "• Postgraduate Seminar – Depression, Bipolar Disorder, Schizophrenia and other Pre-Oedipal Disorders | 17–21 червня 2019 | 20 годин"),
 ("p", "• Postgraduate Seminar (тема не вказана) | 22 червня 2018 | 15 годин"),
 ("p", "• Winter School – Diagnoses and treatment of ICD10 spectrum disorders | 16–20 грудня 2019 | участь"),
 ("p", "• Congress – Psychoanalytic views on death and dying | 6–8 вересня 2018 | участь"),
 ("p", "• Winter School – Love and Abuse in Clinical Context | 6–10 грудня 2021 | участь | Викладачі: Макс Притц, Нік Джайні"),
 ("p", "• Summer School – Cognitive Analytic Therapy | 6–10 червня 2022 | участь | Викладачі: Макс Притц, Нік Джайні"),
 ("p", "• Winter School – Crisis Intervention &amp; Suicide Prevention | 18–22 грудня 2023 | участь"),
 ("gap", ""),
 ("b", "Київський Інститут Сучасної Психології та Психотерапії"),
 ("p", "• Основи тренерської майстерності | вересень – грудень 2017 | 64 години | Напрям: Тренер, розробник тренінгових програм"),
 ("p", "• Психосоматика | 2–4 червня 2017 | 20 годин | Лектори: Anne D. Rosche (IPA), Horst Kächele"),
 ("gap", ""),
 ("b", "Psychology Global Forum (Одеса)"),
 ("p", "• Участь як спікер | 22–23 вересня 2018 | Подяка за внесок у розвиток психології в Україні | Організатор: Південна асоціація арт-терапії (Віра Попова)"),
 ("gap", ""),
 ("b", "International Society for the Psychoanalytic Study of Organizations (ISPSO)"),
 ("p", "• “Polarities of Money, Power and Feelings” – доповідь | ISPSO 36th Annual Meeting – “Perspectives on Polarities: Thinking Below the Surface” | Нью-Йорк, 24–30 червня 2019"),
 ("gap", ""),
 ("b", "Групова психотерапевтична підготовка"),
 ("p", "• International University Global Coaching (Лондон): Team Coaching – Accredited Coach Specific Program (CCE), 3 грудня 2017, 24 години. Модулі I–II, акредитовані ICF (CCE)"),
 ("gap", ""),
 ("b", "Групова психотерапевтична підготовка"),
 ("p", "Теоретичні модулі (13 модулів) – Українська школа групового аналізу (УШГА) – 288 годин"),
 ("p", "Навчальна терапевтична група – УШГА – 480 годин"),
 ("p", "Psychology of the Group and Group Process Analysis – Institute for Psychodynamic Coaching (IPDC) – 144 години"),
 ("p", "Конференція “Exploring Leadership” – IPDC / University of Chicago / AKRI – 29 годин"),
 ("p", "The Essence of Modern Group – The Center for Group Studies (USA) – 18 годин"),
 ("p", "Стажування «Основи сучасної групової психотерапії» – European Confederation for Psychoanalytic Psychotherapy (ECPP) – 24 години"),
 ("p", "Загалом:"),
 ("p", "Теоретичні години: 432"),
 ("p", "Практичні години: 551"),
 ("p", "Загальна кількість: 983 годин"),
]

def build():
    items = []
    for k, t in EDU:
        if k == "gap": items.append('<div style="height:24px"></div>')
        elif k == "b": items.append(f'<p class="ab-b">{t}</p>')
        else: items.append(f'<p class="ab-p">{t}</p>')
    body = f'''
<section class="ab1"><div class="ab-in">
  <div class="ab-ph"><img src="{img("2/69484f85c2caec12d4b1a4ff_optimized_896.webp")}" alt="Наталя Кочергіна" width="457" height="616"></div>
  <div class="ab-tx">
    <h1>НАТАЛЯ КОЧЕРГIНА</h1>
    <p class="ab-sub">Психоаналітичний психотерапевт, груповий терапевт, психодинамічний коуч та консультант організацій, тренер, розробник тренінгових програм, автор групових трансформаційних програм.</p>
    <p class="ab-r">Членкиня  Української  психотерапевтичної ліги, членкиня ISPSO (International Society for the Psychoanalytic Study of Organizations).</p>
    <p class="ab-r">10 років практики. Більше 4000 годин теоретичної та практичної підготовки.</p>
    <p class="ab-r">У своїй роботі поєдную сучасний психоаналіз, коучінг, техніки кататимно-імігінативної терапії, аналітичну психологію К.Юнга, сімейно-системний підхід, IFS.</p>
    <div style="height:19px"></div>
    {"".join(items)}
    <a class="ab-btn" href="https://t.me/Kocher_Nataly" target="_blank" rel="noopener">ЗАПИСАТИСЯ НА КОНСУЛЬТАЦІЮ</a>
  </div>
</div></section>
<section class="ab2"><p>Чим більше буде щасливих людей, тим в кращому світі будуть жити наші діти</p></section>
<section class="ab3" style="background-image:url('{img("2/694e854f080a9d0140fff0dd_optimized_2560.webp")}')"></section>
<style>
.ab1{{background:#fedfdd;padding:105px 24px 80px}}
.ab-in{{max-width:1200px;margin:0 auto;display:flex;gap:120px;align-items:flex-start}}
.ab-ph{{flex:0 0 457px;position:sticky;top:96px}}
.ab-ph img{{width:457px;height:616px;object-fit:cover}}
.ab-tx{{flex:1;max-width:623px}}
.ab-tx h1{{font-family:var(--forum);font-weight:400;font-size:48px;line-height:48px;color:{RED};margin:0 0 26px}}
.ab-sub{{font-family:var(--corm);font-weight:300;font-size:18px;line-height:18px;color:{RED};margin:0 0 27px}}
.ab-r,.ab-p,.ab-b{{font-family:var(--corm);font-size:24px;line-height:24px;margin:0 0 0}}
.ab-r{{font-weight:300;color:{RED};margin-bottom:19px}}
.ab-p{{font-weight:300;color:#000}}
.ab-b{{font-weight:700;color:#000}}
.ab-btn{{display:inline-block;margin-top:40px;background:{RED};color:#fff;text-decoration:none;font-family:var(--forum);font-size:15px;padding:15px 30px;border-radius:20px}}
.ab2{{background:#fffff6;height:500px;display:flex;align-items:center;justify-content:center;padding:0 24px}}
.ab2 p{{font-family:var(--forum);font-size:48px;line-height:48px;color:{RED};text-align:center;max-width:1008px;margin:0}}
.ab3{{height:550px;background-size:cover;background-position:50% 50%}}
@media (max-width:900px){{
 .ab1{{padding:40px 20px}} .ab-in{{flex-direction:column;gap:32px}} .ab-ph{{position:static;flex:none;width:100%}} .ab-ph img{{width:100%;height:auto}}
 .ab-tx h1{{font-size:36px;line-height:1.1}} .ab-r,.ab-p,.ab-b{{font-size:20px;line-height:1.25}}
 .ab2{{height:auto;padding:70px 20px}} .ab2 p{{font-size:32px;line-height:1.15}} .ab3{{height:300px}}
}}
</style>'''
    return page("Про мене — Наталя Кочергіна", "Освіта, досвід і підходи психоаналітичної психотерапевтки та психодинамічного коуча Наталі Кочергіної.", body, "about.html")
