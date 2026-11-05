#!/usr/bin/env python3
"""README-képek generálása az assets/ mappába (Playwright/Chromium kell):
   banner.png, themes.png (témagaléria), preview-<stílus>.png (szimulált CooSpace-oldal).
   A preview-*.png fájlokat később lecserélheted valódi képernyőképekre (ugyanaz a fájlnév).
   Futtatás: python3 tools/build-assets.py"""
import json, os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"; OUT.mkdir(exist_ok=True)
FONTS = (ROOT / "fonts").as_uri()
FONT_CSS = f"""
@font-face{{font-family:HD;src:url('{FONTS}/manrope-latin-wght-normal.woff2') format('woff2-variations');font-weight:200 800;unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+20AC,U+00B7}}
@font-face{{font-family:HD;src:url('{FONTS}/manrope-latin-ext-wght-normal.woff2') format('woff2-variations');font-weight:200 800;unicode-range:U+0100-02BA,U+1E00-1E9F}}
@font-face{{font-family:UI;src:url('{FONTS}/inter-latin-wght-normal.woff2') format('woff2-variations');font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+20AC}}
@font-face{{font-family:UI;src:url('{FONTS}/inter-latin-ext-wght-normal.woff2') format('woff2-variations');font-weight:100 900;unicode-range:U+0100-02BA,U+1E00-1E9F}}
"""

BANNER = FONT_CSS + """
*{box-sizing:border-box;margin:0}
body{width:1280px;height:360px;font-family:UI,sans-serif;overflow:hidden;position:relative;
 background:linear-gradient(120deg,#0b2f2c 0%,#0f766e 48%,#7c2d12 118%);color:#fff}
.o{position:absolute;border-radius:50%;background:rgba(255,255,255,.07)}
.o1{width:520px;height:520px;right:-120px;top:-210px}.o2{width:300px;height:300px;right:300px;bottom:-190px}
h1{font:800 76px/1 HD;letter-spacing:-.035em;position:absolute;left:70px;top:92px}
.s{position:absolute;left:72px;top:190px;font:500 25px/1.4 UI;opacity:.92}
.pills{position:absolute;left:72px;top:262px;display:flex;gap:12px}
.pills span{padding:9px 18px;border:1.5px solid rgba(255,255,255,.55);border-radius:99px;font:600 17px UI}
.card{position:absolute;border-radius:22px;box-shadow:0 24px 50px -16px rgba(0,0,0,.5)}
.c1{right:300px;top:46px;width:250px;height:150px;background:rgba(255,255,255,.16);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.35)}
.c2{right:70px;top:80px;width:260px;height:170px;background:#fff9}
.c3{right:200px;top:190px;width:300px;height:120px;background:#f4f1ea;border:3px solid #111;box-shadow:9px 9px 0 #111;border-radius:6px}
.bar{position:absolute;left:18px;top:18px;height:12px;border-radius:6px}
.dot{position:absolute;right:18px;top:16px;width:18px;height:18px;border-radius:50%}
"""
BANNER_HTML = f"""<style>{BANNER}</style>
<div class="o o1"></div><div class="o o2"></div>
<div class="card c1"><div class="bar" style="width:110px;background:#fff"></div><div class="dot" style="background:#ffb4a2"></div></div>
<div class="card c2"><div class="bar" style="width:130px;background:#c2255c"></div><div class="dot" style="background:#7048e8"></div></div>
<div class="card c3"><div class="bar" style="width:140px;background:#0f766e;border:2px solid #111;height:16px"></div><div class="dot" style="background:#ff6b35;border:2px solid #111"></div></div>
<h1>CS5 Témák</h1><div class="s">Egyedi témák és stílusok a CooSpace 5 felületéhez</div>
<div class="pills"><span>19 színtéma</span><span>6 stílus</span><span>Firefox · Chrome · Edge · Brave</span></div>"""

def gallery_html(themes):
    cards = ""
    for t in themes:
        bg, surface, c1, c2, side = t["preview"]
        head = t.get("previewHeader")
        headhtml = f'<i class="h" style="background:{head}"></i>' if head else ""
        cards += f"""<div class="t"><div class="m" style="background:{bg}">
<i class="sd" style="background:{side}"><b style="background:{c1}"></b><b style="background:{c2}"></b><b style="background:{c1}"></b><b style="background:{c2}"></b></i>{headhtml}
<i class="cd" style="background:{surface}"><u style="background:{c1}"></u><s style="background:{c2}"></s></i></div><span>{t['name']}</span></div>"""
    return f"""<style>{FONT_CSS}
*{{box-sizing:border-box;margin:0}}body{{width:1280px;padding:34px 40px 30px;background:#f6f8f7;font-family:UI}}
h2{{font:800 30px HD;letter-spacing:-.02em;color:#17201d;margin-bottom:22px}}
.g{{display:grid;grid-template-columns:repeat(6,1fr);gap:20px 18px}}
.t span{{display:block;margin-top:8px;font:600 14px UI;color:#26302c;text-align:center}}
.m{{position:relative;height:112px;border-radius:12px;border:1px solid rgba(0,0,0,.14);overflow:hidden;box-shadow:0 6px 16px -8px rgba(0,0,0,.35)}}
.sd{{position:absolute;inset:0 auto 0 0;width:30px;display:flex;flex-direction:column;align-items:center;gap:8px;padding-top:30px}}
.sd b{{width:9px;height:9px;border-radius:50%}}
.h{{position:absolute;top:0;left:30px;right:0;height:22px}}
.cd{{position:absolute;left:46px;right:14px;top:34px;bottom:0;border-radius:10px 10px 0 0;box-shadow:0 -1px 0 rgba(0,0,0,.06),0 3px 12px rgba(0,0,0,.2)}}
.cd u{{position:absolute;left:14px;top:16px;width:46%;height:10px;border-radius:5px}}
.cd s{{position:absolute;right:14px;top:14px;width:15px;height:15px;border-radius:50%}}
</style><h2>19 színtéma</h2><div class="g">{cards}</div>"""

def main():
    themes = json.load(open(ROOT / "themes.json", encoding="utf-8"))
    with sync_playwright() as p:
        b = p.chromium.launch()
        tmp = ROOT / "tools" / "mock" / "_tmp.html"   # file:// oldal kell, hogy a betűtípusok betöltsenek
        for name, htm, h in [("banner", BANNER_HTML, 360), ("themes", gallery_html(themes), 600)]:
            if name == "banner" and not os.environ.get("MAKE_BANNER"):
                continue   # a borítókép kézzel készült, csak MAKE_BANNER=1-gyel generáljuk újra
            tmp.write_text(htm, encoding="utf-8")
            pg = b.new_page(viewport={"width": 1280, "height": h}); pg.goto(tmp.as_uri()); pg.wait_for_timeout(600)
            pg.screenshot(path=str(OUT / f"{name}.png"), full_page=(name != "banner")); pg.close()
        tmp.unlink()
        page_tpl = (ROOT / "tools" / "mock" / "page.html").read_text(encoding="utf-8")
        for layout, theme in [("modern", "light"), ("glass", "aurora"), ("floating", "sakura"), ("brutal", "rosegarden"), ("topnav", "sakura-virag")]:
            f = ROOT / "tools" / "mock" / f"_{layout}.html"
            f.write_text(page_tpl.replace("THEME", theme).replace("LAYOUT", layout), encoding="utf-8")
            pg = b.new_page(viewport={"width": 1180, "height": 700}); pg.goto(f.as_uri()); pg.wait_for_timeout(1300)
            pg.screenshot(path=str(OUT / f"preview-{layout}.png")); pg.close(); f.unlink()
        b.close()
    print("kész:", ", ".join(sorted(x.name for x in OUT.glob("*.png"))))

if __name__ == "__main__":
    main()
