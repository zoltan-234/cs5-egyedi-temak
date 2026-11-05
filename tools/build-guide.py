#!/usr/bin/env python3
"""Útmutató építése: docs/utmutato-hu.pdf, docs/guide-en.pdf + docs/UTMUTATO.md, docs/GUIDE.md

Képek: docs/screenshots/<ID>.png (vagy .jpg/.webp). Ha egy kép hiányzik, szaggatott keretes
helyőrző kerül a helyére (a tervezet így is olvasható). --strict: hibával leáll, ha hiányzik kép.
Futtatás a repó gyökeréből: python3 tools/build-guide.py [--strict]
Függőség: playwright (Chromium) a PDF-hez.
"""
import json, re, sys, html
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from guide_content import CHAPTERS_HU, CHAPTERS_EN, SHOTS, META

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SHOT_DIR = DOCS / "screenshots"
STRICT = "--strict" in sys.argv
VERSION = json.load(open(ROOT / "manifest.json", encoding="utf-8"))["version"]
EXTS = (".png", ".jpg", ".jpeg", ".webp")
missing = []

def find_img(sid):
    for e in EXTS:
        p = SHOT_DIR / f"{sid}{e}"
        if p.exists():
            return p
    return None

def caption(sid, lang):
    return SHOTS[sid][0 if lang == "hu" else 1]

# ---------------------------------------------------------------- HTML (PDF)
CSS = """
@font-face{font-family:UI;src:url('%(f)s/fonts/inter-latin-wght-normal.woff2') format('woff2-variations');font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2190-21FF,U+2212}
@font-face{font-family:UI;src:url('%(f)s/fonts/inter-latin-ext-wght-normal.woff2') format('woff2-variations');font-weight:100 900;unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:HD;src:url('%(f)s/fonts/manrope-latin-wght-normal.woff2') format('woff2-variations');font-weight:200 800;unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+20AC}
@font-face{font-family:HD;src:url('%(f)s/fonts/manrope-latin-ext-wght-normal.woff2') format('woff2-variations');font-weight:200 800;unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F}
:root{--ac:#0f766e;--ac2:#c2410c;--ink:#1b2420;--mut:#5a6660;--line:#dfe5e2;--soft:#f3f6f5}
*{box-sizing:border-box}
@page{size:A4;margin:18mm 16mm 20mm}
body{font:10.4pt/1.55 UI,system-ui,sans-serif;color:var(--ink);margin:0}
h1,h2{font-family:HD,UI,sans-serif;letter-spacing:-.02em;margin:0}
.cover{height:257mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always;
  background:linear-gradient(135deg,#0f766e 0%%,#115e59 55%%,#c2410c 130%%);color:#fff;border-radius:18px;padding:22mm 18mm;position:relative;overflow:hidden}
.cover:before,.cover:after{content:"";position:absolute;border-radius:50%%;background:rgba(255,255,255,.08)}
.cover:before{width:120mm;height:120mm;right:-35mm;top:-30mm}.cover:after{width:80mm;height:80mm;right:20mm;bottom:-40mm}
.cover h1{font-size:34pt;line-height:1.1;font-weight:800;position:relative}
.cover .sub{font-size:14pt;opacity:.9;margin-top:6mm;position:relative}
.cover .meta{margin-top:14mm;font-size:10pt;opacity:.85;position:relative}
.cover .tag{display:inline-block;margin-top:6mm;padding:2mm 4mm;border:1px solid rgba(255,255,255,.5);border-radius:99px;font-size:9.5pt;position:relative}
.toc{page-break-after:always}.toc h1{font-size:20pt;margin-bottom:6mm;color:var(--ac)}
.toc ol{list-style:none;padding:0;margin:0}.toc li{padding:2.2mm 0;border-bottom:1px solid var(--line);font-size:11pt}
.toc a{color:var(--ink);text-decoration:none}
.ch{page-break-before:always}.ch:first-of-type{page-break-before:auto}
h1.c{font-size:20pt;color:var(--ac);padding-bottom:3mm;border-bottom:3px solid var(--ac);margin-bottom:5mm}
h2{font-size:13pt;margin:6mm 0 2mm;color:var(--ink)}
p{margin:2.2mm 0}
code{font:9.2pt ui-monospace,Menlo,Consolas,monospace;background:var(--soft);border:1px solid var(--line);border-radius:4px;padding:.4mm 1.4mm;word-break:break-all}
ul.l{padding-left:5mm;margin:2mm 0}ul.l li{margin:1.4mm 0}
.note{border-radius:10px;padding:3.2mm 4mm;margin:4mm 0;page-break-inside:avoid;border-left:4px solid}
.note b.t{display:block;font-family:HD,UI;font-size:11pt;margin-bottom:1mm}
.note.ok{background:#e9f7ee;border-color:#16a34a}.note.warn{background:#fff4e0;border-color:#d97706}.note.info{background:#e8f1fb;border-color:#2563eb}
table{border-collapse:collapse;width:100%%;margin:3mm 0;font-size:9.6pt;page-break-inside:avoid}
th{background:var(--ac);color:#fff;text-align:left;padding:2.2mm 3mm}td{padding:2.2mm 3mm;border-bottom:1px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:var(--soft)}
ol.s{list-style:none;counter-reset:n;padding:0;margin:3mm 0}
ol.s>li{counter-increment:n;position:relative;padding-left:10mm;margin:0 0 4mm;page-break-inside:avoid}
ol.s>li:before{content:counter(n);position:absolute;left:0;top:0;width:7mm;height:7mm;border-radius:50%%;background:var(--ac);color:#fff;font:700 9.5pt/7mm HD,UI;text-align:center}
figure{margin:2.5mm 0 1mm;page-break-inside:avoid}
figure img{display:block;max-width:100%%;max-height:92mm;border:1px solid var(--line);border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,.12)}
figcaption{font-size:8.6pt;color:var(--mut);margin-top:1.2mm}
.ph{border:2px dashed #b7c2bd;border-radius:8px;background:repeating-linear-gradient(45deg,#fafcfb,#fafcfb 8px,#f1f5f3 8px,#f1f5f3 16px);
  padding:5mm;color:var(--mut);font-size:9pt;min-height:30mm}
.ph b{display:block;color:var(--ac2);font-size:10pt;margin-bottom:1mm}
"""

def esc_inline(s):
    return s  # a tartalom saját, megbízható HTML-részleteket használ (<b>, <code>)

def render_shot(sid, lang):
    img = find_img(sid)
    cap = html.escape(caption(sid, lang))
    if img:
        return f'<figure><img src="{img.as_uri()}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
    missing.append(sid)
    hint = html.escape(SHOTS[sid][2])
    return (f'<figure><div class="ph"><b>[{sid}] {META[lang]["missing"]}</b>{cap}<br><i>{hint}</i></div>'
            f'<figcaption>{cap}</figcaption></figure>')

def render_block(b, lang):
    t = b[0]
    if t == "p":    return f"<p>{b[1]}</p>"
    if t == "h2":   return f"<h2>{b[1]}</h2>"
    if t == "list": return '<ul class="l">' + "".join(f"<li>{i}</li>" for i in b[1]) + "</ul>"
    if t == "note": return f'<div class="note {b[1]}"><b class="t">{b[2]}</b>{b[3]}</div>'
    if t == "shot": return render_shot(b[1], lang)
    if t == "table":
        head = "".join(f"<th>{h}</th>" for h in b[1])
        rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b[2])
        return f"<table><tr>{head}</tr>{rows}</table>"
    if t == "steps":
        out = '<ol class="s">'
        for text, shots in b[1]:
            out += f"<li>{text}" + "".join(render_shot(s, lang) for s in shots) + "</li>"
        return out + "</ol>"
    raise ValueError(t)

def build_html(lang, chapters):
    m = META[lang]
    toc = "".join(f'<li><a href="#{c[1]}">{c[2]}</a></li>' for c in chapters if c[0] == "h1")
    body, open_ch = "", False
    for b in chapters:
        if b[0] == "h1":
            if open_ch: body += "</section>"
            body += f'<section class="ch" id="{b[1]}"><h1 class="c">{b[2]}</h1>'
            open_ch = True
        else:
            body += render_block(b, lang)
    body += "</section>"
    css = CSS % {"f": ROOT.as_uri()}
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{m['title']}</title><style>{css}</style></head><body>
<div class="cover"><h1>{m['title']}</h1><div class="sub">{m['sub']}</div>
<div class="meta">{m['ver']} {VERSION} · Firefox · Chrome · Edge · Brave</div><div class="tag">{m['footer']}</div></div>
<div class="toc"><h1>{m['toc']}</h1><ol>{toc}</ol></div>{body}</body></html>"""

# ---------------------------------------------------------------- Markdown
def md_inline(s):
    s = re.sub(r"<b>(.*?)</b>", r"**\1**", s)
    s = re.sub(r"<code>(.*?)</code>", r"`\1`", s)
    s = re.sub(r"<i>(.*?)</i>", r"*\1*", s)
    return html.unescape(s)

def md_shot(sid, lang):
    cap = caption(sid, lang)
    if find_img(sid):
        ext = find_img(sid).suffix
        return f"\n![{cap}](screenshots/{sid}{ext})\n*{cap}*\n"
    return f"\n> 🖼️ *[{sid}] {cap}*\n"

def build_md(lang, chapters):
    m = META[lang]
    out = [f"# {m['title']}\n", f"{m['sub']}  \n{m['ver']} {VERSION} · {m['other']}\n", f"## {m['toc']}\n"]
    out += [f"{i}. [{c[2].split('. ',1)[1]}](#{re.sub(r'[^a-z0-9áéíóöőúüű -]','',c[2].lower()).replace(' ','-')})" for i, c in enumerate([c for c in chapters if c[0] == 'h1'], 1)]
    out.append("")
    for b in chapters:
        t = b[0]
        if t == "h1":    out.append(f"\n## {b[2]}\n")
        elif t == "h2":  out.append(f"\n### {md_inline(b[1])}\n")
        elif t == "p":   out.append(md_inline(b[1]) + "\n")
        elif t == "list": out += ["- " + md_inline(i) for i in b[1]] + [""]
        elif t == "note":
            icon = {"ok": "✅", "warn": "⚠️", "info": "ℹ️"}[b[1]]
            out.append(f"> {icon} **{md_inline(b[2])}**  \n> {md_inline(b[3])}\n")
        elif t == "shot": out.append(md_shot(b[1], lang))
        elif t == "table":
            out.append("| " + " | ".join(md_inline(h) for h in b[1]) + " |")
            out.append("|" + "---|" * len(b[1]))
            out += ["| " + " | ".join(md_inline(c) for c in r) + " |" for r in b[2]] + [""]
        elif t == "steps":
            for i, (text, shots) in enumerate(b[1], 1):
                out.append(f"{i}. {md_inline(text)}")
                for s in shots:
                    out.append(md_shot(s, lang).replace("\n", "\n   "))
            out.append("")
    return "\n".join(out) + "\n"

# ---------------------------------------------------------------- futtatás
def main():
    from playwright.sync_api import sync_playwright
    jobs = [("hu", CHAPTERS_HU, "UTMUTATO.md"), ("en", CHAPTERS_EN, "GUIDE.md")]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for lang, chapters, mdname in jobs:
            missing.clear()
            htm = build_html(lang, chapters)
            tmp = ROOT / "dist" / f"guide-{lang}.html"
            tmp.parent.mkdir(exist_ok=True)
            tmp.write_text(htm, encoding="utf-8")
            pg = browser.new_page()
            pg.goto(tmp.as_uri()); pg.wait_for_timeout(500)
            pdf = DOCS / f"{META[lang]['file']}.pdf"
            pg.pdf(path=str(pdf), format="A4", print_background=True, display_header_footer=True,
                   header_template="<span></span>",
                   footer_template=f'<div style="font:8px sans-serif;color:#777;width:100%;text-align:center">{META[lang]["footer"]} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
                   margin={"top": "18mm", "bottom": "20mm", "left": "16mm", "right": "16mm"})
            pg.close()
            (DOCS / mdname).write_text(build_md(lang, chapters), encoding="utf-8")
            miss = sorted(set(missing))
            print(f"{lang}: {pdf.name} + {mdname} | hiányzó képek: {len(miss)}")
            if STRICT and miss:
                sys.exit("Hiányzó képek: " + ", ".join(miss))
        browser.close()

if __name__ == "__main__":
    main()
