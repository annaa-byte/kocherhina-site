"""Download every image the pages hotlink from Weblium into img/ and point the pages at the local copies.
Runs in GitHub Actions before publishing, so the site keeps working without the Weblium account."""
import glob, os, re, urllib.request
os.makedirs("img", exist_ok=True)
pat = re.compile(r"https://res2\.weblium\.site/res/[0-9a-f]+/([A-Za-z0-9_.\-]+\.(?:webp|png|jpe?g|svg))")
for path in glob.glob("*.html") + glob.glob("*.css"):
    text = open(path, encoding="utf-8").read()
    for url, name in set((m.group(0), m.group(1)) for m in pat.finditer(text)):
        dst = os.path.join("img", name)
        if not os.path.exists(dst):
            urllib.request.urlretrieve(url, dst)
            print("downloaded", name)
    open(path, "w", encoding="utf-8").write(pat.sub(lambda m: "img/" + m.group(1), text))
