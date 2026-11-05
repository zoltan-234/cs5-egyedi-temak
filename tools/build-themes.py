#!/usr/bin/env python3
"""Témák generálása: themes/<id>.css + themes.json, kontraszt-ellenőrzéssel.
Futtatás a repó gyökeréből:  python3 tools/build-themes.py

Kötelező kulcsok: bg sidebar surface surface2 rowalt input border fg muted heading
                  accent accentfg accent2 accent2fg star success
Opcionális:       sidebarfg sidebarmuted  – ha a menü színe eltér a tartalomtól
                  headerbg headerfg headergrad – lapos fejléc (Modern stílus)
                  pal – 5 színű paletta (menüikonok, naptár, szakaszok…)
                  glow – ráviteli fény a kártyák körül (Modern stílus)
"""
import json
import re

DARK = {"icon-filter": "invert(0.85)", "logo-filter": "brightness(0) invert(0.9)", "shadow-k": "3"}
LIGHT = {"icon-filter": "none", "logo-filter": "none", "shadow-k": "1"}

# id, név, sötét?, csoport, paletta
THEMES = [
  # ---------- Világos, egyszínű alap ----------
  ("cs5-fresh", "CS5 friss", False, "Világos", dict(
    bg="#f4f6f8", sidebar="#ffffff", surface="#ffffff", surface2="#eef2f5", rowalt="#f7f9fb", input="#ffffff",
    border="#dde3e8", fg="#1d2733", muted="#5b6876", heading="#0f1720",
    accent="#0a77a0", accentfg="#ffffff", accent2="#cc3e20", accent2fg="#ffffff", star="#b7791f", success="#1f8a4c",
    pal=["#0a77a0", "#cc3e20", "#7b4fd6", "#1f8a4c", "#c27a00"])),
  ("light", "Világos modern", False, "Világos", dict(
    bg="#f7f7f5", sidebar="#ffffff", surface="#ffffff", surface2="#eef1ef", rowalt="#f9faf9", input="#ffffff",
    border="#d9dedb", fg="#26302c", muted="#5f6a65", heading="#111816",
    accent="#0f766e", accentfg="#ffffff", accent2="#c2410c", accent2fg="#ffffff", star="#a86410", success="#15803d",
    pal=["#0f766e", "#c2410c", "#6d28d9", "#b45309", "#2563eb"])),
  ("dawn", "Rosé Pine Dawn", False, "Világos", dict(
    bg="#faf4ed", sidebar="#fffaf3", surface="#fffaf3", surface2="#f2e9e1", rowalt="#f8f1e9", input="#fffaf3",
    border="#dfdad9", fg="#575279", muted="#65617c", heading="#464261",
    accent="#286983", accentfg="#fffaf3", accent2="#a2566c", accent2fg="#fffaf3", star="#a8670f", success="#3e7a62",
    pal=["#286983", "#b4637a", "#907aa9", "#c2780f", "#56949f"])),

  # ---------- Többszínű ----------
  ("pastel", "Pasztell", False, "Többszínű", dict(
    bg="#f7f5ff", sidebar="#2e2a5c", sidebarfg="#f1efff", sidebarmuted="#c3bfeb",
    surface="#ffffff", surface2="#efecff", rowalt="#faf9ff", input="#ffffff",
    border="#e0dcf5", fg="#2b2850", muted="#5f5a8a", heading="#1c1940",
    accent="#6d5bd0", accentfg="#ffffff", accent2="#c93a70", accent2fg="#ffffff", star="#a86410", success="#2f855a",
    headerbg="#c7d2fe", headerfg="#1c1940", headergrad="linear-gradient(110deg, #a5b4fc 0%, #f9a8d4 60%, #fde68a 100%)",
    pal=["#6d5bd0", "#d6457a", "#0e9f8e", "#d97706", "#2563eb"])),
  ("sunset", "Naplemente", False, "Többszínű", dict(
    bg="#fff8f1", sidebar="#10454f", sidebarfg="#e8fbf8", sidebarmuted="#a7d5cf",
    surface="#ffffff", surface2="#ffeede", rowalt="#fffbf6", input="#ffffff",
    border="#f1dcc8", fg="#3a2a22", muted="#6e5546", heading="#2a1a12",
    accent="#0f7a72", accentfg="#ffffff", accent2="#c2410c", accent2fg="#ffffff", star="#a86410", success="#2f855a",
    headerbg="#ff9a6b", headerfg="#2a1a12", headergrad="linear-gradient(110deg, #ff7e5f 0%, #feb47b 100%)",
    pal=["#0f7a72", "#d9480f", "#c2185b", "#b7791f", "#3b5bdb"])),
  ("aurora", "Aurora", True, "Többszínű", dict(
    bg="#0e1022", sidebar="#14163a", sidebarfg="#e7e8ff", sidebarmuted="#a9acd6",
    surface="#171a33", surface2="#20244a", rowalt="#13152c", input="#0f1126",
    border="#2c3163", fg="#dfe2ff", muted="#a2a7d4", heading="#ffffff",
    accent="#8b9cff", accentfg="#0e1022", accent2="#ff7ab6", accent2fg="#0e1022", star="#ffd166", success="#4ade80",
    headerbg="#5b21b6", headerfg="#ffffff", headergrad="linear-gradient(110deg, #4338ca 0%, #7e22ce 45%, #be185d 100%)",
    pal=["#60a5fa", "#a78bfa", "#f472b6", "#fbbf24", "#34d399"], glow="rgba(167, 139, 250, 0.28)")),
  ("neon", "Neon", True, "Többszínű", dict(
    bg="#07070d", sidebar="#0c0c18", sidebarfg="#e9e9ff", sidebarmuted="#9a9ac8",
    surface="#10101e", surface2="#181830", rowalt="#0c0c17", input="#0b0b16",
    border="#26264a", fg="#e6e6ff", muted="#a0a0cc", heading="#ffffff",
    accent="#22d3ee", accentfg="#07070d", accent2="#ff4fd8", accent2fg="#07070d", star="#facc15", success="#a3e635",
    headerbg="#0c0c18", headerfg="#ffffff", headergrad="linear-gradient(110deg, #0c0c18 0%, #2a0b3e 50%, #06303a 100%)",
    pal=["#22d3ee", "#ff4fd8", "#a3e635", "#facc15", "#818cf8"], glow="rgba(34, 211, 238, 0.30)")),

  # ---------- Rózsaszín ----------
  ("sakura", "Sakura", False, "Rózsaszín", dict(
    bg="#fff4f7", sidebar="#ffe3ec", sidebarfg="#5a1f36", sidebarmuted="#844460",
    surface="#ffffff", surface2="#ffe9f0", rowalt="#fff8fa", input="#ffffff",
    border="#f6d3df", fg="#4a2233", muted="#7f4a63", heading="#3a1426",
    accent="#c2255c", accentfg="#ffffff", accent2="#6741d9", accent2fg="#ffffff", star="#a86410", success="#2b8a3e",
    headerbg="#ffd1dc", headerfg="#3a1426", headergrad="linear-gradient(110deg, #ffc2d4 0%, #ffdde1 50%, #e5dbff 100%)",
    pal=["#c2255c", "#7048e8", "#e8590c", "#0c8599", "#d6336c"])),
  ("sakura-virag", "Sakura (virág)", False, "Rózsaszín", dict(
    bg="#fff4f7", sidebar="#ffe3ec", sidebarfg="#5a1f36", sidebarmuted="#844460",
    surface="#ffffff", surface2="#ffe9f0", rowalt="#fff8fa", input="#ffffff",
    border="#f6d3df", fg="#4a2233", muted="#7f4a63", heading="#3a1426",
    accent="#c2255c", accentfg="#ffffff", accent2="#6741d9", accent2fg="#ffffff", star="#a86410", success="#2b8a3e",
    headerbg="#ffe3ec", headerfg="#3a1426",
    # A fejléc háttere a virágmintás kép, fehéres fátyollal (hogy a sötét felirat olvasható maradjon).
    headergrad="linear-gradient(rgba(255, 244, 247, 0.58), rgba(255, 244, 247, 0.58))",
    previewheader="linear-gradient(110deg, #ffc2d4 0%, #ffe3ec 100%)",
    headerimg=True,
    pal=["#c2255c", "#7048e8", "#e8590c", "#0c8599", "#d6336c"])),
  ("rosegarden", "Rózsakert", False, "Rózsaszín", dict(
    bg="#fbf6f1", sidebar="#5b1a43", sidebarfg="#ffe9f4", sidebarmuted="#e0aecb",
    surface="#ffffff", surface2="#f8ecef", rowalt="#fdf9f7", input="#ffffff",
    border="#ecdcd9", fg="#3b2430", muted="#6f5260", heading="#2a1420",
    accent="#b0216b", accentfg="#ffffff", accent2="#2f7d5a", accent2fg="#ffffff", star="#a86410", success="#2f7d5a",
    headerbg="#b0216b", headerfg="#ffffff", headergrad="linear-gradient(110deg, #9d1b5f 0%, #c8406a 55%, #c4542a 100%)",
    pal=["#b0216b", "#2f7d5a", "#e0607e", "#c27a00", "#6a4c93"])),
  ("bubblegum", "Bubblegum", True, "Rózsaszín", dict(
    bg="#1a0d17", sidebar="#220f1e", sidebarfg="#ffe4f2", sidebarmuted="#d9a3c2",
    surface="#26131f", surface2="#33182a", rowalt="#1f0f1b", input="#1a0d17",
    border="#4a2340", fg="#f7d9ea", muted="#cf9dbb", heading="#fff0f8",
    accent="#ff6fb5", accentfg="#1a0d17", accent2="#7ee0ff", accent2fg="#1a0d17", star="#ffd166", success="#7ee8a2",
    headerbg="#7a1d5c", headerfg="#fff0f8", headergrad="linear-gradient(110deg, #3b0f2f 0%, #7a1d5c 55%, #b8336a 100%)",
    pal=["#ff6fb5", "#7ee0ff", "#c4a7ff", "#ffd166", "#7ee8a2"], glow="rgba(255, 111, 181, 0.30)")),

  # ---------- Sötét, egyszínű alap ----------
  ("dark", "Midnight", True, "Sötét", dict(
    bg="#0d1016", sidebar="#10141a", surface="#151920", surface2="#1a1f29", rowalt="#12161d", input="#12161d",
    border="#232835", fg="#d8dce5", muted="#9aa1b0", heading="#f3f5f9",
    accent="#7aa2f7", accentfg="#0d1016", accent2="#f07a5a", accent2fg="#0d1016", star="#f5c76b", success="#5fd39a",
    pal=["#7aa2f7", "#f07a5a", "#c4a7e7", "#5fd39a", "#f5c76b"])),
  ("nord", "Nord", True, "Sötét", dict(
    bg="#2e3440", sidebar="#2a2f3a", surface="#3b4252", surface2="#434c5e", rowalt="#353c4a", input="#2e3440",
    border="#4c566a", fg="#e5e9f0", muted="#b8c1cf", heading="#eceff4",
    accent="#88c0d0", accentfg="#2e3440", accent2="#d08770", accent2fg="#1f232b", star="#ebcb8b", success="#a3be8c",
    pal=["#88c0d0", "#d08770", "#b48ead", "#a3be8c", "#ebcb8b"])),
  ("mocha", "Catppuccin Mocha", True, "Sötét", dict(
    bg="#1e1e2e", sidebar="#181825", surface="#262637", surface2="#313244", rowalt="#222232", input="#181825",
    border="#45475a", fg="#cdd6f4", muted="#a6adc8", heading="#e6ebff",
    accent="#cba6f7", accentfg="#1e1e2e", accent2="#fab387", accent2fg="#1e1e2e", star="#f9e2af", success="#a6e3a1",
    pal=["#89b4fa", "#fab387", "#cba6f7", "#a6e3a1", "#f9e2af"])),
  ("dracula", "Dracula", True, "Sötét", dict(
    bg="#282a36", sidebar="#21222c", surface="#2f3142", surface2="#3a3d50", rowalt="#2b2d3a", input="#21222c",
    border="#4d5066", fg="#f8f8f2", muted="#b0b6cf", heading="#ffffff",
    accent="#bd93f9", accentfg="#21222c", accent2="#ff79c6", accent2fg="#21222c", star="#f1fa8c", success="#50fa7b",
    pal=["#8be9fd", "#ff79c6", "#bd93f9", "#50fa7b", "#ffb86c"])),
  ("gruvbox", "Gruvbox", True, "Sötét", dict(
    bg="#282828", sidebar="#1d2021", surface="#32302f", surface2="#3c3836", rowalt="#2d2b2a", input="#1d2021",
    border="#504945", fg="#ebdbb2", muted="#bdae93", heading="#fbf1c7",
    accent="#fabd2f", accentfg="#282828", accent2="#fe8019", accent2fg="#282828", star="#d79921", success="#b8bb26",
    pal=["#83a598", "#fe8019", "#d3869b", "#b8bb26", "#fabd2f"])),
  ("rosepine", "Rosé Pine", True, "Sötét", dict(
    bg="#191724", sidebar="#16141f", surface="#1f1d2e", surface2="#26233a", rowalt="#1c1a29", input="#16141f",
    border="#403d52", fg="#e0def4", muted="#a29fbd", heading="#f4f2ff",
    accent="#c4a7e7", accentfg="#191724", accent2="#ebbcba", accent2fg="#191724", star="#f6c177", success="#9ccfd8",
    pal=["#9ccfd8", "#ebbcba", "#c4a7e7", "#f6c177", "#eb6f92"])),
  ("amoled", "AMOLED fekete", True, "Sötét", dict(
    bg="#000000", sidebar="#000000", surface="#0b0b0d", surface2="#151518", rowalt="#070708", input="#0b0b0d",
    border="#26262b", fg="#e6e6e9", muted="#9d9da6", heading="#ffffff",
    accent="#a78bfa", accentfg="#0b0b0d", accent2="#fb7185", accent2fg="#000000", star="#fcd34d", success="#34d399",
    pal=["#60a5fa", "#fb7185", "#a78bfa", "#34d399", "#fcd34d"])),
]

def lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def mix(a, b, t):
    """a és b színek keveréke (t = b aránya)"""
    a, b = a.lstrip("#"), b.lstrip("#")
    ch = [round(int(a[i:i+2], 16) * (1 - t) + int(b[i:i+2], 16) * t) for i in (0, 2, 4)]
    return "#%02x%02x%02x" % tuple(ch)

def with_defaults(p):
    p = dict(p)
    p.setdefault("sidebarfg", p["fg"])
    p.setdefault("sidebarmuted", p["muted"])
    p.setdefault("headerbg", p["sidebar"])
    p.setdefault("headerfg", p["heading"])
    p.setdefault("headergrad", "none")
    p.setdefault("glow", "transparent")
    # Klasszikus nézet: az Unics bannerképét ez a színátmenet váltja le.
    if p["headergrad"] != "none":
        p["banner"], p["bannerfg"] = p["headergrad"], p["headerfg"]
    elif lum(p["headerbg"]) > 0.6:          # világos téma: a kiemelő színből
        p["banner"] = f"linear-gradient(110deg, {p['accent']} 0%, {mix(p['accent'], '#000000', 0.28)} 100%)"
        p["bannerfg"] = p["accentfg"]
    else:                                   # sötét téma: a fejléc színéből, kis kiemelő-árnyalattal
        p["banner"] = f"linear-gradient(110deg, {p['headerbg']} 0%, {mix(p['headerbg'], p['accent'], 0.30)} 100%)"
        p["bannerfg"] = p["headerfg"]
    return p

# (szín, háttér, minimum)
CHECKS = [("fg", "surface", 4.5), ("muted", "surface", 4.5), ("muted", "surface2", 4.5), ("fg", "bg", 4.5),
          ("accentfg", "accent", 4.5), ("accent2fg", "accent2", 4.5), ("heading", "surface", 4.5),
          ("sidebarfg", "sidebar", 4.5), ("sidebarmuted", "sidebar", 4.5)]

VARS = dict(bg="bg", sidebar="sidebar", sidebarfg="sidebar-fg", sidebarmuted="sidebar-muted",
            surface="surface", surface2="surface-2", rowalt="row-alt", input="input-bg", border="border",
            fg="fg", muted="muted", heading="heading", accent="accent", accentfg="accent-fg",
            accent2="accent-2", accent2fg="accent-2-fg", star="star", success="success",
            headerbg="header-bg", headerfg="header-fg", headergrad="header-grad", glow="glow",
            banner="banner", bannerfg="banner-fg")

entries = [{"id": "original", "name": "Eredeti", "group": "Világos", "css": [],
            "preview": ["#ffffff", "#f0f0f0", "#0b84ae", "#f55431", "#ffffff"]}]
ok = True
for tid, name, dark, group, raw in THEMES:
    p = with_defaults(raw)
    for a, b, need in CHECKS:
        c = contrast(p[a], p[b])
        if c < need:
            ok = False
            print(f"  ✗ {tid}: {a} on {b} = {c:.2f} (kell {need})")
    # Fejléc szöveg minden színátmenet-ponton: nagy, félkövér cím → 3:1
    for stop in re.findall(r"#[0-9a-fA-F]{6}", p["headergrad"]) or [p["headerbg"]]:
        c = contrast(p["headerfg"], stop)
        if c < 3:
            ok = False
            print(f"  ✗ {tid}: headerfg on {stop} = {c:.2f} (kell 3)")
    for stop in re.findall(r"#[0-9a-fA-F]{6}", p["banner"]):
        c = contrast(p["bannerfg"], stop)
        if c < 4.5:
            ok = False
            print(f"  ✗ {tid}: bannerfg on {stop} = {c:.2f} (kell 4.5)")

    extra = DARK if dark else LIGHT
    css = f'html[data-unics-theme="{tid}"] {{\n  color-scheme: {"dark" if dark else "light"};\n'
    for k, v in VARS.items():
        css += f"  --ut-{v}: {p[k]};\n"
    for i, col in enumerate(p["pal"], 1):
        css += f"  --ut-c{i}: {col};\n"
    for k, v in extra.items():
        css += f"  --ut-{k}: {v};\n"
    css += "}\n"
    if p.get("headerimg"):
        # A kép url()-je ebben a fájlban áll (nem változóban), mert a változó url()-ját
        # a felhasználó stíluslapjához képest oldaná fel a böngésző, és a layouts/ mappából nem találná.
        sel = f'html[data-unics-theme="{tid}"][data-unics-theme="{tid}"][data-unics-theme="{tid}"] #header'
        css += (f'{sel} {{\n'
                f'  background-image: {p["headergrad"]}, url("{tid}.jpg") !important;\n'
                f'  background-size: auto, 720px auto !important;\n'
                f'  background-position: 0 0, center top !important;\n'
                f'  background-repeat: no-repeat, repeat !important;\n}}\n')
    open(f"themes/{tid}.css", "w").write(f"/* {name} – generálva: tools/build-themes.py */\n" + css)

    e = {"id": tid, "name": name, "group": group, "css": ["themes/base.css", f"themes/{tid}.css", "themes/login.css"],
         "preview": [p["bg"], p["surface"], p["pal"][0], p["pal"][1], p["sidebar"]]}
    if p["headergrad"] != "none":
        e["previewHeader"] = p.get("previewheader", p["headergrad"])
    if dark:
        e["dark"] = True
    entries.append(e)

with open("themes.json", "w") as f:
    f.write("[\n" + ",\n".join("  " + json.dumps(e, ensure_ascii=False) for e in entries) + "\n]\n")
print("OK – minden kontraszt rendben" if ok else "Kontraszt-hibák fent")
