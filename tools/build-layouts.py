#!/usr/bin/env python3
"""Stílusok generálása: layouts/modern.css + layouts/src/<id>.css -> layouts/<id>.css

A Modern a közös alap (szerkezet, tipográfia, animációk). A többi stílus ennek
másolata, ahol a data-unics-layout="modern" szelektor az adott azonosítóra
cserélődik, majd a layouts/src/<id>.css felülírásai következnek.
Futtatás a repó gyökeréből: python3 tools/build-layouts.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = (ROOT / "layouts" / "modern.css").read_text(encoding="utf-8")
VARIANTS = ["glass", "floating", "brutal"]

for vid in VARIANTS:
    over = (ROOT / "layouts" / "src" / f"{vid}.css").read_text(encoding="utf-8")
    body = BASE.replace('data-unics-layout="modern"', f'data-unics-layout="{vid}"')
    out = (f"/* GENERÁLVA: tools/build-layouts.py – ne szerkeszd közvetlenül.\n"
           f"   Alap: layouts/modern.css, felülírások: layouts/src/{vid}.css */\n\n"
           f"{body}\n\n/* ======== {vid}: felülírások ======== */\n\n{over}\n")
    (ROOT / "layouts" / f"{vid}.css").write_text(out, encoding="utf-8")
    print("ok", vid)
