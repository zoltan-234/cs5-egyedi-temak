<div align="center">

![CS5 Témák](assets/banner.png)

**Válaszd ki, hogyan nézzen ki a CooSpace 5 (CS5)!**
19 színtéma · 6 stílus · egy kattintás

[![Licenc: PolyForm Noncommercial](https://img.shields.io/badge/licenc-PolyForm%20Noncommercial-orange)](LICENSE)
[![Legújabb kiadás](https://img.shields.io/github/v/release/zoltan-234/cs5-egyedi-temak?label=kiad%C3%A1s)](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)
![Böngészők](https://img.shields.io/badge/b%C3%B6ng%C3%A9sz%C5%91k-Firefox%20%C2%B7%20Chrome%20%C2%B7%20Edge%20%C2%B7%20Brave-0f766e)

**[⬇️ Letöltés](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)** · **[📖 Telepítési útmutató (PDF)](docs/utmutato-hu.pdf)** · **[🇬🇧 English](README.en.md)** · **[🐞 Hibabejelentés](https://github.com/zoltan-234/cs5-egyedi-temak/issues/new/choose)**

</div>

---

## Mi ez?

Egy kis böngészőbővítmény, amivel átszabhatod a **CooSpace 5 (CS5)** kinézetét: színeket, formákat, animációkat. Akár sötét módot, akár rózsaszínt, akár üveg-hatású felületet szeretnél, a bővítmény ikonjára kattintva egy popupban választasz, és a változás **azonnal** látszik. A választásod megmarad F5 és újraindítás után is.

> 🛡️ **Nem kell aggódni:** a bővítmény **csak a megjelenést** módosítja, csak a CooSpace 5 oldalán fut, **semmit nem küld el sehova**, és nem ír a CooSpace-be. Részletek: [Adatvédelem](PRIVACY.md).

## Stílusok

A színtémától független forma-réteg. Bármelyik színnel kombinálható.

| | |
|:--:|:--:|
| ![Modern](assets/preview-modern.png) **Modern**<br>Tiszta, lekerekített, finom árnyékok | ![Üveg](assets/preview-glass.png) **Üveg**<br>Áttetsző, elmosott panelek |
| ![Szigetek](assets/preview-floating.png) **Szigetek**<br>Lebegő, pirula-alakú elemek, rugalmas mozgás | ![Brutalista](assets/preview-brutal.png) **Brutalista**<br>Vastag keret, kemény árnyék |
| ![Felső menü](assets/preview-topnav.png) **Felső menü**<br>A menü fent, a profil jobbra, a fülek oldalt | |

A **Felső menü** stílus átrendezi a felületet: a menü vízszintes sávként felkerül az oldal tetejére, a profil jobbra kerül, a Színterek fülei pedig bal oldali sávot kapnak.

A **Klasszikus** stílus a CooSpace eredeti formáit tartja meg, csak a színeket cseréli.

## Színtémák

![19 színtéma](assets/themes.png)

**Világos:** Eredeti · CS5 friss · Világos modern · Rosé Pine Dawn
**Többszínű:** Pasztell · Naplemente · Aurora · Neon
**Rózsaszín:** Sakura · Sakura (virág) · Rózsakert · Bubblegum
**Sötét:** Midnight · Nord · Catppuccin Mocha · Dracula · Gruvbox · Rosé Pine · AMOLED fekete

Minden téma 5 színű palettát kap: ettől színesek a menüikonok, a félév-gombok pöttyei, a kezdőlap dobozainak fejlécei és a naptáresemények. A szövegek kontrasztját a generátor ellenőrzi (WCAG 4.5:1).

## Funkciók

A témákon és stílusokon túl néhány apró kényelmi beállítás is van a bővítmény popupjában (**Funkciók** rész, mindegyik mellett egy ⓘ jel magyarázza, mit csinál). Alapból mind ki van kapcsolva, ilyenkor az oldal nem változik.

| Funkció | Mit csinál |
|---|---|
| **Induláskor a Színterek oldalra** | Bejelentkezés után rögtön a Színterek oldalra visz, bármelyik oldalon is landolnál. Csak egyszer ugrik böngészőfülenként, utána bárhová el lehet menni. |
| **Csoportok a Színtereken** | Beállítható, hogy az „Állandó” és a félév-csoportok betöltéskor **mind csukva**, **mind nyitva** vagy **csak az aktuális félév nyitva** legyenek. |
| **Emlékezz a csoportokra** | Amit te kinyitsz vagy becsukol (pl. csak az „Állandó”-t csukod be), azt név szerint megjegyzi, és legközelebb így tölti be. Ez erősebb az alapmódnál. A megjegyzett csoportok egy gombbal törölhetők. |

A színtémák a Színterek csoportfejlécének szürke nyíl-dobozát is átszínezik, az oldalsáv összecsukott állapotában pedig minden stílusban rendesen látszanak az ikonok.

## Telepítés

Töltsd le a legújabb kiadást: **[Releases](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)**

| Böngésző | Fájl | Hogyan |
|---|---|---|
| **Firefox** | `.xpi` | Nyisd meg a fájlt a Firefoxban → **Hozzáadás**. Tartós, magától frissül. A popupban nyomd meg egyszer az **Engedélyezés** gombot. |
| **Chrome** | `…-chromium.zip` | Csomagold ki egy **állandó** mappába → `chrome://extensions` → **Fejlesztői mód** → **Kicsomagolt bővítmény betöltése** |
| **Edge** | `…-chromium.zip` | Ugyanígy: `edge://extensions` |
| **Brave** | `…-chromium.zip` | Ugyanígy: `brave://extensions` |
| **Más Chromium-alapú böngészők** (Vivaldi, Opera, Opera GX, Chromium) | `…-chromium.zip` | Ugyanígy: `vivaldi://extensions`, `opera://extensions`, `chrome://extensions` |

> ⚠️ Chrome, Edge és Brave esetén a kicsomagolt mappát **ne töröld és ne helyezd át**, különben a bővítmény leáll.

> A Chromium-alapú böngészők (Vivaldi, Opera stb.) elvileg ugyanígy működnek, de ezeket nem teszteltem. Ha valamelyiknél gond van, jelezd egy [Issue](../../issues)-ban.

📖 Képes, lépésről lépésre útmutató: **[utmutato-hu.pdf](docs/utmutato-hu.pdf)** ([Markdown](docs/UTMUTATO.md)) · **[guide-en.pdf](docs/guide-en.pdf)** ([Markdown](docs/GUIDE.md))

A Safarit és a telefonos böngészőket egyelőre nem támogatja.

## Gyakori kérdések

<details><summary><b>Biztonságos?</b></summary>

Igen. A bővítmény csak a megjelenést állítja (CSS), csak a CooSpace 5 oldalán fut, nincs szervere, nem küld el adatot, és nem fér hozzá más oldalakhoz. A teljes forráskód nyilvános, bárki ellenőrizheti. Egyetlen engedélye a `storage` (a választott téma mentése) és az Unics oldalhoz való hozzáférés.
</details>

<details><summary><b>Hogyan állítom vissza az eredetit?</b></summary>

Válaszd a **Világos → Eredeti** színt és a **Klasszikus** stílust. Vagy kapcsold ki a bővítményt, az oldal azonnal visszaáll.
</details>

<details><summary><b>Miért kell Firefoxban az „Engedélyezés” gomb?</b></summary>

A Firefox alapból nem adja meg a bővítményeknek az oldalhoz való hozzáférést, azt egyszer meg kell erősíteni. Chrome-ban, Edge-ben és Brave-ben ez telepítéskor megvan.
</details>

<details><summary><b>Valami rosszul néz ki</b></summary>

Küldj egy képernyőképet a [hibabejelentő](https://github.com/zoltan-234/cs5-egyedi-temak/issues/new/choose) oldalon, és írd meg, melyik téma és stílus. Addig válts másik témára.
</details>

<details><summary><b>Hivatalos?</b></summary>

Nem. Független, nem hivatalos projekt, nem áll kapcsolatban a CooSpace oldal üzemeltetőivel vagy fejlesztőivel.
</details>

## Fejlesztőknek

```
manifest.json              MV3, közös Firefox + Chromium
content/                   téma betöltése, jss-feloldó, felület-jelölő, funkciók (features.js)
popup/                     témaválasztó és funkció-beállító felület
themes/ , themes.json      színtémák (a build-themes.py generálja)
layouts/ , layouts.json    stílusok (a modern.css az alap, a többi src/-ből generálódik)
fonts/                     Inter és Manrope (OFL licenc)
docs/                      útmutató (PDF + Markdown), CooSpace elemek (ELEMEK.md)
tools/                     generátorok, build, szkennelő szkriptek
.github/workflows/         automatikus kiadás
```

```bash
python3 tools/build-themes.py     # témák generálása (kontraszt-ellenőrzéssel)
python3 tools/build-layouts.py    # stílusok generálása
bash tools/build.sh               # csomagok a dist/ mappába (Firefox + Chromium)
python3 tools/build-guide.py      # útmutató PDF-ek
python3 tools/build-assets.py     # README-képek
```

- **Új téma:** vedd fel a `tools/build-themes.py` `THEMES` listájába, futtasd, töltsd újra a bővítményt.
- **Új stílus:** `layouts/src/<id>.css` + a `tools/build-layouts.py` listája + `layouts.json`.
- **A CooSpace elemei és szelektorai:** [`docs/ELEMEK.md`](docs/ELEMEK.md). A CooSpace generált `jss…` osztályait ne használd, a `jss-resolver.js` stabil `data-ut` jelölést ad helyettük.
- Részletek: [CONTRIBUTING.md](CONTRIBUTING.md) · Forrás és építés: [BUILD.md](BUILD.md) · Változások: [CHANGELOG.md](CHANGELOG.md)

## Licenc

[PolyForm Noncommercial 1.0.0](LICENSE): szabadon használható, másolható és módosítható **nem kereskedelmi célra**, de pénzt keresni vele nem lehet. A betűtípusok (Inter, Manrope) az SIL OFL licenc alatt állnak. Magyar összefoglaló: [NOTICE.md](NOTICE.md).

<sub>Nem hivatalos projekt. A CooSpace név a tulajdonosáé.</sub>
