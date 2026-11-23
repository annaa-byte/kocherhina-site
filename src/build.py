import os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import home, salon, about, seasons, legal
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
pages = {"index.html": home.build(), "svoboda-buty-zhinkoyu.html": salon.build(), "about.html": about.build(),
         "privacy.html": legal.privacy(), "oferta.html": legal.oferta()}
for n in range(1, 6):
    pages[f"season-{n}.html"] = seasons.build_one(n)
for k, v in pages.items():
    open(os.path.join(OUT, k), "w").write(v)
for f in ("style.css", "site.js"):
    shutil.copy(os.path.join(os.path.dirname(__file__), f), OUT)
print("built", len(pages), "pages ->", OUT)
