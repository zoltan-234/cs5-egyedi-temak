#!/usr/bin/env python3
"""A weboldal (site/) élő előnézetéhez szükséges fájlok másolása és a demo oldal generálása.
Futtatás: python3 tools/build-site.py   (témák/stílusok módosítása után újra)"""
import json, re, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"; DEMO = SITE / "demo"

def main():
    if DEMO.exists(): shutil.rmtree(DEMO)
    for d in ("themes", "layouts", "fonts", "content"): (DEMO / d).mkdir(parents=True)
    for pat, d in (("themes/*.css", "themes"), ("themes/*.jpg", "themes"), ("layouts/*.css", "layouts"),
                   ("fonts/*.woff2", "fonts")):
        for f in ROOT.glob(pat): shutil.copy(f, DEMO / d / f.name)
    for n in ("jss-resolver.js", "surface-tagger.js"): shutil.copy(ROOT / "content" / n, DEMO / "content" / n)
    data = {n: json.load(open(ROOT / f"{n}.json", encoding="utf-8")) for n in ("themes", "layouts")}
    (SITE / "data.js").write_text("window.CS5=" + json.dumps(data, ensure_ascii=False) + ";", encoding="utf-8")
    (SITE / "fonts").mkdir(exist_ok=True)
    for f in ROOT.glob("fonts/inter-*.woff2"): shutil.copy(f, SITE / "fonts" / f.name)   # a Space Grotesk / JetBrains Mono már a site/fonts-ban van
    page = (ROOT / "tools" / "mock" / "page.html").read_text(encoding="utf-8")
    page = re.sub(r'<link rel="stylesheet" href="\.\./\.\./(themes/THEME|layouts/LAYOUT)\.css">\n?', "", page)
    page = page.replace("../../", "")
    page = page.replace('data-unics-theme="THEME" data-unics-layout="LAYOUT"', "")
    page = page.replace("<script>UnicsSurfaceTagger.start();</script>", DEMO_JS)
    page = page.replace("<!doctype html><html ", '<!doctype html><html lang="hu" ', 1)
    page = page.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><title>CS5 Témák – előnézeti minta</title>', 1)
    (DEMO / "index.html").write_text(page, encoding="utf-8")
    fill_theme_list(data["themes"])
    print("site/demo kész")

def fill_theme_list(themes):
    """A színtémák nevei sima szövegként is bekerülnek az index.html-be (<!--THEMES-->...<!--/THEMES-->)."""
    idx = SITE / "index.html"; t = idx.read_text(encoding="utf-8")
    names = ", ".join(x["name"] for x in themes if x["id"] != "original")
    t = re.sub(r"<!--THEMES-->.*?<!--/THEMES-->", f"<!--THEMES-->{names}<!--/THEMES-->", t, flags=re.S)
    idx.write_text(t, encoding="utf-8")

DEMO_JS = """<script>
// A szülő oldal (site/index.html) küldi: {theme: {...themes.json elem}, layout: {...layouts.json elem}}
const SLOT = {theme: "data-unics-theme", layout: "data-unics-layout"};
function put(kind, item){
  document.querySelectorAll("link["+SLOT[kind]+"-link]").forEach(l=>l.remove());
  const root=document.documentElement, key=SLOT[kind].replace("data-","").replace(/-(\\w)/g,(m,c)=>c.toUpperCase());
  if(!item||!item.css||!item.css.length){root.removeAttribute(SLOT[kind]);return;}
  root.setAttribute(SLOT[kind],item.id);
  item.css.forEach(p=>{const l=document.createElement("link");l.rel="stylesheet";l.href=p;l.setAttribute(SLOT[kind]+"-link","");document.head.appendChild(l);});
}
function setDark(t){const r=document.documentElement;if(t&&t.dark)r.setAttribute("data-unics-dark","");else r.removeAttribute("data-unics-dark");}
addEventListener("message",e=>{
  const d=e.data||{}; if(!d.cs5)return;
  if("theme" in d){put("theme",d.theme);setDark(d.theme);}
  if("layout" in d)put("layout",d.layout);
  document.querySelectorAll("link[data-unics-theme-link],link[data-unics-layout-link]").forEach(l=>document.head.appendChild(l));
  UnicsSurfaceTagger.stop();UnicsSurfaceTagger.start();
});
UnicsSurfaceTagger.start();
parent.postMessage({cs5:"ready"},"*");
</script>"""
main()
