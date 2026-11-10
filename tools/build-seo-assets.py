#!/usr/bin/env python3
"""favicon.ico, apple-touch-icon és a megosztási kép (og.png, 1200x630) generálása a site/ mappába."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
S = Path(__file__).resolve().parent.parent / "site"
def icon(n):
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, n - 1, n - 1), radius=round(n * .28), fill="#7c3aed")
    f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf" if Path("/usr/share/fonts/opentype/inter/Inter-Bold.otf").exists() else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", round(n * .42))
    d.text((n / 2, n / 2), "CS5", font=f, fill="white", anchor="mm"); return im
icon(256).save(S / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
icon(180).convert("RGB").save(S / "img" / "apple-touch-icon.png")
html = f"""<style>@font-face{{font-family:SG;font-weight:700;src:url(file://{S}/fonts/spacegrotesk-latin.woff2)}}
@font-face{{font-family:IN;font-weight:100 900;src:url(file://{S}/fonts/inter-latin-wght-normal.woff2)}}
body{{margin:0;width:1200px;height:630px;background:#f3f1ff;font-family:IN;display:flex;align-items:center;padding:0 70px;box-sizing:border-box;gap:50px;overflow:hidden}}
h1{{font:700 96px/1 SG;margin:0;letter-spacing:-.03em;color:#1a1d29}}h1 span{{color:#7c3aed}}
p{{font-size:32px;line-height:1.35;color:#3d4356;margin:22px 0 0}}.t{{flex:1}}
img{{width:520px;border-radius:18px;box-shadow:0 24px 60px rgba(26,29,41,.25);border:1px solid #e6e8f0}}</style>
<div class=t><h1>CS5 <span>Témák</span></h1><p>Új színek és sötét mód a CooSpace-hez.<br><b>19 színtéma · 5 stílus · ingyenes</b></p></div>
<img src="file://{S}/img/preview-floating.png">"""
with sync_playwright() as p:
    b = p.chromium.launch(args=["--allow-file-access-from-files"]); pg = b.new_page(viewport={"width": 1200, "height": 630})
    tmp = S.parent / "_og.html"; tmp.write_text(html, encoding="utf-8"); pg.goto(tmp.as_uri()); pg.wait_for_timeout(800); pg.screenshot(path=str(S / "img" / "og.png")); b.close(); tmp.unlink()
print("kész")
