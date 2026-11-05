# CooSpace felület – elemek és szelektorok

Referencia témák és stílusok tervezéséhez. Minden itt felsorolt szelektor a valódi CooSpace oldal szkenneléséből származik (2026. október, CooSpace 1.4.0).

**Technológia:** React + Material-UI v4 (`Mui*` osztályok), naptár: react-big-calendar (`rbc-*`).

---

## 0. Alapszabályok

| Szabály | Miért |
|---|---|
| Minden szabály elé: `html[data-unics-theme]` (szín) vagy `html[data-unics-layout="modern"]` (forma) | Csak akkor hasson, ha a bővítmény aktív |
| `!important` kell | A MUI futásidőben, a mi CSS-ünk *után* szúrja be a stílusait |
| `background-color`, **ne** `background` | A rövidítés letörli a háttérképeket (ikonok, kurzusképek, fejléc-banner) |
| **Ne** építs `jss123` osztályra | Buildenként változik a szám |
| Stabil: `Mui*`, `rbc-*`, `#id`, saját CooSpace nevek (`.ToolContainer`, `.forumItem`…) | Ezek nem változnak |

---

## 1. Téma-változók

Egy színtéma **csak ezeket** adja meg (`themes/*.css`):

```css
html[data-unics-theme="sajat"] {
  color-scheme: dark;          /* vagy light */
  --ut-bg: #16181d;            /* oldal háttér */
  --ut-surface: #1d2027;       /* kártyák, panelek */
  --ut-surface-2: #23262e;     /* menü, fejlécsávok, hover */
  --ut-row-alt: #1a1d23;       /* páros sorok, fórum-elemek */
  --ut-input-bg: #121419;      /* natív input mezők */
  --ut-border: #343846;        /* keretek, elválasztók */
  --ut-fg: #d6d9e0;            /* szöveg */
  --ut-muted: #9aa0ad;         /* másodlagos szöveg, címkék */
  --ut-heading: #f1f3f7;       /* h1–h6 */
  --ut-accent: #7aa2f7;        /* CooSpace kék helyett (#0b84ae) */
  --ut-accent-fg: #0f1117;     /* szöveg az accent-en */
  --ut-accent-2: #f07a5a;      /* CooSpace narancs helyett (#f55431) */
  --ut-accent-2-fg: #16181d;
  --ut-icon-filter: invert(0.85);          /* sötét témán az ikonok */
  --ut-logo-filter: brightness(0) invert(0.88);
  --ut-shadow-k: 3;            /* árnyék-erősség szorzó (világos: 1) */
  --ut-sidebar: #10141a;       /* bal menü háttere */
  --ut-sidebar-fg: #d8dce5;    /* bal menü szövege (eltérhet a tartalomtól) */
  --ut-sidebar-muted: #9aa1b0; /* bal menü halvány szövege */
  --ut-header-bg: #10141a;     /* lapos fejléc (Modern stílus) */
  --ut-header-fg: #f3f5f9;     /* lapos fejléc szövege */
  --ut-header-grad: none;      /* pl. linear-gradient(110deg, #4338ca, #be185d) */
  --ut-glow: transparent;      /* kártya ráviteli fénye (Modern) */
  --ut-c1 … --ut-c5;           /* 5 színű paletta – lásd lent */
  --ut-star: #f5c76b;          /* kedvenc csillag */
  --ut-success: #5fd39a;       /* online jelző, siker */
}
```

A témákat a `tools/build-themes.py` generálja (kontraszt-ellenőrzéssel) – kézzel ne szerkeszd a `themes/<id>.css` fájlokat.

### Modern stílus belső változói (`layouts/modern.css`)

| Változó | Érték | Mire |
|---|---|---|
| `--m-ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | minden animáció görbéje |
| `--m-fast` / `--m-med` / `--m-slow` | 180 / 320 / 520 ms | hover / átmenet / betöltés |
| `--m-r-sm` / `--m-r-md` / `--m-r-lg` | 10 / 14 / 18 px | gomb / lista-elem / kártya |
| `--m-shadow-1` / `-2` / `-3` | nyugalmi / hover / felugró | árnyékok |

---

### Paletta (`--ut-c1…c5`) – hol jelenik meg

| Elem | Szín |
|---|---|
| Menüikonok | menüpontonként c1→c5 sorban |
| Félév-gombok pöttye | gombonként c1→c5 |
| Kezdőlap dobozainak fejléce | FavScenes c1, Messages c2, ToDos c4, PersonalStats c5 (színátmenettel) |
| Kurzus szakaszainak felső sávja | szakaszonként c1→c5 |
| Naptár | Test c1, Survey c2, SimpleTask c3, Attendance c4; fejléc c1→c2 |
| Fül-jelölő | c1→c2 színátmenet |

## 2. Az CooSpace eredeti színei

| Szín | Hol | Változó |
|---|---|---|
| `#0b84ae` kék | aktív menüpont, linkek, primary gomb | `--ut-accent` |
| `#f55431` narancs | lebegő gomb (FAB), naptár fejléc | `--ut-accent-2` |
| `#ffffff` | kártyák, menü, panelek | `--ut-surface` |
| `#f0f0f0` / `#ededed` | eszköztárak, dobozok háttere | `--ut-surface-2` |
| `rgba(0,0,0,.87)` | alap szöveg | `--ut-fg` |
| `#757575`, `rgba(0,0,0,.54)` | másodlagos szöveg, ikonok | `--ut-muted` |
| `#ccc`, `#ddd`, `#f8f8f8` | keretek | `--ut-border` |

---

## 3. Oldalváz

```
body
└─ div#app
   └─ div.DLCLayout
      ├─ div#leftmenu                 bal menü (250px)
      │  ├─ aside#left
      │  │  ├─ ul > li > a.icon-*     menüpontok
      │  │  ├─ a.LayoutUserMenu       felhasználó-blokk
      │  │  └─ div.collapseMenuButton összecsukó gomb
      │  └─ div.dlclogo               logó (háttérkép!)
      ├─ div#header                   fejléc (bannerkép háttérrel)
      │  ├─ div.scrollOutRow          felső sor: intézmény, keresés, értesítés
      │  └─ h1                        oldalcím + gyorsgombok
      └─ div#content                  tartalom
```

---

## 4. Bal menü

| Elem | Szelektor | Eredeti |
|---|---|---|
| Menü konténer | `#leftmenu` | fehér |
| Menüpont | `aside#left > ul > li` | 250×50 px, hover: kék háttér |
| Menüpont link | `aside#left > ul > li > a` | 14px, `line-height: 50px` |
| Aktív menüpont | `aside#left > ul > li.current` | kék háttér, fehér szöveg |
| Menü ikonok | `a.icon-dashboard`, `.icon-szinterek`, `.icon-dokumentumok`, `.icon-naptar`, `.icon-uzenetek`, `.icon-kedvencek`, `.icon-kilepes` | ikonfont `::before`-ben |
| Kedvencek almenü | `aside#left li.showfavs ul li` | `span.icon-Scene` + név |
| Felhasználó | `.LayoutUserMenu`, benne `.avatarblock`, `.loggedUserName` | |
| Összecsukó gomb | `.collapseMenuButton` | fehér kör |
| Logó | `.dlclogo` | háttérkép, összecsukva kis ikon |
| Összecsukott állapot | `.DLCLayout.collapsedMenu` | |

```css
html[data-unics-layout="modern"] aside#left > ul > li {
  height: 44px !important;
  margin: 4px 10px !important;
  border-radius: var(--m-r-md) !important;
}
```

---

## 5. Fejléc

| Elem | Szelektor | Megjegyzés |
|---|---|---|
| Fejléc | `#header` | bannerkép: `fejlec_graf.png` – a témák ezt `background-image: var(--ut-banner)` színátmenettel váltják le (`--ut-banner`, `--ut-banner-fg`) |
| Felső sor | `#header .scrollOutRow` | |
| Oldalcím | `#header h1` | 60px magas, flex |
| Ikongombok | `#header .MuiIconButton-root` | fehér ikonok |
| Gyorsmenü | `.FastMenu` | |

---

## 6. Kártyák és panelek

| Elem | Szelektor | Hol |
|---|---|---|
| **Minden kártya/panel** | `.MuiPaper-root` | mindenhol |
| Kártya | `.MuiCard-root` | kurzuskártya, eszköz-konténer, profil |
| Kártya fejléc | `.MuiCardHeader-root`, `.MuiCardHeader-title`, `.MuiCardHeader-subheader` | |
| Kártya kép | `.MuiCardMedia-root` | profil oldalon |
| Kezdőlap dobozai | `section.FavScenes`, `section.Messages`, `section.ToDos`, `section.PersonalStats` | Áttekintés |
| Doboz fejléc | `section > div.head`, benne `h2` | |
| Félév-fejléc („Állandó”) | `h2.defaultBackgroundColor.defaultColor` | Színterek, 48px, `::before` = nyíl |
| Félév-gombok | `[data-ut~="term-btn"]` | jss-resolver, lásd 12b |
| Félév-gombok sávja | `[data-ut~="term-bar"]` | |
| Nézetváltó eszköztár | `[data-ut~="view-bar"]` | |
| Kurzuskártya-rács | `[data-ut~="scene-grid"]` | eredetileg flex, Modernben grid |
| Kurzuskártya | `#content .MuiCard-root` (Színterek) | 300px széles, felül kép |
| Kurzuskártya képe | ⚠ **még nincs megerősítve** – osztály nélküli `div`, háttérképpel | `dump-structure.js` kell |

```css
html[data-unics-layout="modern"] .MuiCard-root {
  border-radius: var(--m-r-lg) !important;
  box-shadow: var(--m-shadow-1) !important;
  transition: transform var(--m-med) var(--m-ease), box-shadow var(--m-med) var(--m-ease) !important;
}
html[data-unics-layout="modern"] #content .MuiCard-root:hover {
  transform: translateY(-4px);
  box-shadow: var(--m-shadow-3) !important;
}
```

---

## 7. Kurzuson belül

| Elem | Szelektor | Megjegyzés |
|---|---|---|
| Eszköz-csoport („Információk”, „Tananyag”) | `.MuiCard-root.ToolContainer` | |
| Eszközlista | `.ToolContainer ul`, `.ToolContainer li` | `#f8f8f8` keret |
| Doboz-elrendezés | `ul.boxLayout` | `#ededed` háttér |
| Eszköz-doboz | `li[class*="boxbg-"]` → `.boxbg-Test`, `.boxbg-Attendance`, `.boxbg-Forum`… | |
| Doboz belső | `li[class*="boxbg-"] > div` → `.Test`, `.Attendance` | `#ccc` keret |
| Eszköz ikonok | `span.svg-Forum`, `.svg-Folder`, `.svg-Test`, `.svg-SimpleTask`, `.svg-Attendance`, `.svg-Text_0`, `.svg-ss_todo`, `.svg-Survey` | háttérkép-ikonok |
| Szöveges bejegyzés | osztály nélküli `div`-ek | automatikus jelölés kezeli |
| Flex sor (cím + dátum) | `.horizontal` | ⚠ **általános segédosztály**, ne színezd |

---

## 8. Fórum, beszélgetések, profil

| Elem | Szelektor |
|---|---|
| Fórum szál | `.forumItem` (`rgba(0,0,0,.05)` háttér) |
| Fórum hozzászólás | `.DialogItem` |
| Beszélgetések – bal lista | `.leftpanel` |
| Beszélgetés-elem | `.MuiCard-root.item` |
| Jobb panel (üres) | `.rightpanel.noSelectedMessage` |
| Profil oldal | `.profile` |
| Profil mező | `.editfieldcontainer` → `.editfieldleft`, `.editfieldcontent` (`.editfieldvalue`, `.editfieldlabel`), `.editfieldright` |
| Dokumentum ikonok | `span.icon.svg-file_pdf`, `.svg-file_zip`, `.svg-file_folder` |

---

## 9. Naptár (react-big-calendar)

| Elem | Szelektor | Eredeti |
|---|---|---|
| Havi nézet | `.rbc-month-view` | fehér, `#ddd` keret |
| Saját eszköztár | `.rbc-customToolbar` | |
| Napnevek sora | `.rbc-month-header` | narancs |
| Napnév | `.rbc-header` | |
| Hét sor | `.rbc-month-row` | |
| Nap háttér | `.rbc-day-bg` | |
| Más hónap napja | `.rbc-off-range-bg` | `#f8f8f8` |
| Mai nap | `.rbc-today`, dátum: `.rbc-date-cell.rbc-now` | dátum: `#464646` |
| Esemény | `.rbc-event` | `#f0f0f0` |
| Esemény típusa | `.ctcolor-Test`, `.ctcolor-Survey`, `.ctcolor-SimpleTask`, `.ctcolor-Attendance` | típusonként színezhető |
| Többnapos | `.rbc-event-continues-prior`, `.rbc-event-continues-after` | |

---

## 10. MUI komponensek (mindenhol)

| Komponens | Szelektor | Állapotok |
|---|---|---|
| Fülek | `.MuiTabs-root`, `.MuiTab-root`, `.MuiTabs-indicator` | `.Mui-selected` |
| Gomb | `.MuiButton-root` | `.MuiButton-contained`, `-text`, `-outlined`, `-containedPrimary`, `-containedSecondary`, `-containedSizeSmall` |
| Lebegő gomb | `.MuiFab-root` | `.MuiFab-primary` (kék), `.MuiFab-secondary` (narancs), `.MuiFab-extended` |
| Ikongomb | `.MuiIconButton-root` | `.MuiIconButton-sizeSmall` |
| Kapcsológomb | `.MuiToggleButton-root`, `.MuiToggleButtonGroup-root` | `.Mui-selected` |
| Szövegmező | `.MuiInputBase-root`, `.MuiInputBase-input`, `.MuiOutlinedInput-notchedOutline`, `.MuiInput-underline` | `.Mui-focused` |
| Címke | `.MuiFormLabel-root`, `.MuiInputLabel-root` | |
| Jelölő | `.MuiCheckbox-root`, `.MuiRadio-root` | |
| Felugró ablak | `.MuiDialog-paper`, `.MuiBackdrop-root` | |
| Legördülő menü | `.MuiPopover-paper`, `.MuiMenu-paper`, `.MuiMenuItem-root` | |
| Tooltip | `.MuiTooltip-tooltip` | |
| Badge | `.MuiBadge-badge` | `.MuiBadge-colorError` |
| Másodlagos szöveg | `.MuiTypography-colorTextSecondary`, `.MuiListItemText-secondary` | |
| Elválasztó | `.MuiDivider-root` | |
| Táblázat cella | `.MuiTableCell-root`, `.MuiTableCell-head` | |
| Ripple effekt | `.MuiTouchRipple-root` | |
| Tiltott | `.Mui-disabled` | |

---

## 11. Avatarok és ikonok

| Elem | Szelektor | Megjegyzés |
|---|---|---|
| Avatar | `.avatar` (+ `jss*` színosztály) | monogramos színes kör – **ne színezd át** |
| Material ikon | `span.material-icons`, `span.FontIcon2` | font-ikon, `color` hat rá |
| Eszköz ikon | `span[class*="svg-"]` | háttérkép → csak `filter` hat rá |

---

## 12. Automatikus felület-jelölés (sötét témákhoz)

A `content/surface-tagger.js` a **kiszámolt** stílus alapján jelöli meg azokat az elemeket, amelyekre nincs stabil szelektor (osztály nélküli div, `jss*`, Wordből bemásolt inline stílus). Minden színtémánál fut (az Eredeti kivételével).

| Attribútum | Mikor kapja | CSS-ben |
|---|---|---|
| `[data-ut-bg="surface"]` | fehér háttér | `--ut-surface` |
| `[data-ut-bg="surface-2"]` | világosszürke háttér | `--ut-surface-2` |
| `[data-ut-fg]` | sötét szöveg | `--ut-fg` |
| `[data-ut-border="line"]` | vékony világos keret (< 4px) | `--ut-border` |
| `[data-ut-border="gap"]` | vastag fehér keret (≥ 4px) | `--ut-bg` |
| `[data-ut-before]` / `[data-ut-after]` | világos `::before`/`::after` | `--ut-surface(-2)` |

Kihagyja: képek, SVG, avatarok, `#header`, háttérképes elemek.

```css
/* Saját sötét témában ezek automatikusan működnek, nem kell semmit írni.
   Felülírni csak konkrétabb szelektorral lehet (ezek a base.css elején vannak). */
html[data-unics-dark] [data-ut-bg="surface"] { background-color: var(--ut-surface) !important; }
```

---

## 12b. Generált JSS osztályok → `data-ut`

A `content/jss-resolver.js` a `<style data-meta="…">` lapokból tulajdonság alapján megkeresi az aktuális `jss123` osztályt, és stabil attribútumot tesz az elemekre. Új elem felvétele: a `RULES` listába egy `{ name, meta, test }` sor.

| `data-ut` | `data-meta` lap | Felismerés |
|---|---|---|
| `term-btn` | SceneList | `width: 180px; height: 60px` |
| `term-bar` | SceneList | `margin-top: -20px; padding-bottom: 20px` |
| `scene-grid` | SceneList | `flex-wrap: wrap; margin-left: 51px` |
| `view-bar` | SceneList | `height: 58px; align-items: center` |
| `page-title` | PageTitle | `height: 60px; font-size: 20px` |

```css
html[data-unics-layout="modern"] [data-ut~="term-btn"]:hover { transform: translateY(-2px); }
```

## 13. Nyitott kérdések

- **Kurzuskártya képe:** pontos szelektor kell → `tools/dump-structure.js` a Színterek oldalon.
- **Még nem szkennelt oldalak:** teszt kitöltése, nyitott legördülő menü, felugró ablak, bejelentkező oldal.

## Eszközök

| Szkript | Mire |
|---|---|
| `tools/scan-unics.js` | színes/keretes elemek listája oldalanként |
| `tools/dump-structure.js` | teljes elrendezés-fa (szülő-gyerek, flex/grid, méretek) |

Mindkettő a DevTools konzolba illesztve fut, szöveget nem gyűjt, az eredményt a vágólapra másolja.
