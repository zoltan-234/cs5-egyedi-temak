<div align="center">

![CS5 Themes](assets/banner.png)

**Choose how CooSpace 5 (CS5) looks!**
19 colour themes · 5 styles · one click

[![Licence: PolyForm Noncommercial](https://img.shields.io/badge/licence-PolyForm%20Noncommercial-orange)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/zoltan-234/cs5-egyedi-temak?label=release)](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)
![Browsers](https://img.shields.io/badge/browsers-Firefox%20%C2%B7%20Chrome%20%C2%B7%20Edge%20%C2%B7%20Brave-0f766e)

**[⬇️ Download](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)** · **[📖 Installation guide (PDF)](docs/guide-en.pdf)** · **[🇭🇺 Magyar](README.md)** · **[🐞 Report an issue](https://github.com/zoltan-234/cs5-egyedi-temak/issues/new/choose)**

</div>

---

## What is it?

A small browser extension that lets you restyle **CooSpace 5 (CS5)**: colours, shapes, animations. Whether you want dark mode, pink, or glass-like panels, click the extension icon, pick from the popup, and the change shows **instantly**. Your choice survives a refresh and a browser restart.

> 🛡️ **Nothing to worry about:** it only changes **how the page looks**, runs only on the CooSpace 5 site, **sends nothing anywhere**, and writes nothing to CooSpace. Details: [Privacy](PRIVACY.md).

## Styles

A shape layer independent of the colour theme; combine it with any colour.

| | |
|:--:|:--:|
| ![Modern](assets/preview-modern.png) **Modern**<br>Clean, rounded, soft shadows | ![Glass](assets/preview-glass.png) **Glass**<br>Translucent, blurred panels |
| ![Islands](assets/preview-floating.png) **Islands**<br>Floating, pill-shaped elements, springy motion | ![Brutalist](assets/preview-brutal.png) **Brutalist**<br>Thick borders, hard shadows |

**Classic** keeps CooSpace's original shapes and only changes the colours.

## Colour themes

![19 colour themes](assets/themes.png)

**Light:** Eredeti (original) · CS5 friss · Világos modern · Rosé Pine Dawn
**Colourful:** Pasztell · Naplemente · Aurora · Neon
**Pink:** Sakura · Sakura (virág, flower-pattern header) · Rózsakert · Bubblegum
**Dark:** Midnight · Nord · Catppuccin Mocha · Dracula · Gruvbox · Rosé Pine · AMOLED black

Every theme gets a 5-colour palette, which colours the menu icons, the term-button dots, the home-page box headers and the calendar events. Text contrast is checked by the generator (WCAG 4.5:1).

## Features

Besides themes and styles, the extension popup has a few small convenience settings (**Funkciók** section; each has an ⓘ mark that explains what it does). All are off by default, so the page stays unchanged until you switch one on.

| Feature | What it does |
|---|---|
| **Open the Scenes page on start** | After login it takes you straight to the Scenes (Színterek) page, whatever page you land on. It jumps only once per browser tab, after that you can go anywhere. |
| **Groups on the Scenes page** | Choose whether the “Állandó” and the term groups load **all closed**, **all open** or **only the current term open**. |
| **Remember groups** | What you open or close yourself (e.g. you close only “Állandó”) is remembered by name and loaded that way next time. It beats the default mode. The remembered groups can be cleared with one button. |

Colour themes also recolour the grey arrow box of the Scenes group headers, and the icons show properly in the collapsed sidebar in every style.

## Installation

Download the latest release: **[Releases](https://github.com/zoltan-234/cs5-egyedi-temak/releases/latest)**

| Browser | File | How |
|---|---|---|
| **Firefox** | `.xpi` | Open the file in Firefox → **Add**. Permanent and self-updating. Press **Allow** once in the popup. |
| **Chrome** | `…-chromium.zip` | Extract to a **permanent** folder → `chrome://extensions` → **Developer mode** → **Load unpacked** |
| **Edge** | `…-chromium.zip` | Same: `edge://extensions` |
| **Brave** | `…-chromium.zip` | Same: `brave://extensions` |
| **Other Chromium-based browsers** (Vivaldi, Opera, Opera GX, Chromium) | `…-chromium.zip` | Same: `vivaldi://extensions`, `opera://extensions`, `chrome://extensions` |

> ⚠️ On Chrome, Edge and Brave **do not delete or move** the extracted folder, or the extension stops.

> Other Chromium-based browsers (Vivaldi, Opera, etc.) should work the same way, but I have not tested them. If one has a problem, please open an [Issue](../../issues).

📖 Step-by-step illustrated guide: **[guide-en.pdf](docs/guide-en.pdf)** ([Markdown](docs/GUIDE.md)) · **[utmutato-hu.pdf](docs/utmutato-hu.pdf)** (Hungarian)

Safari and mobile browsers are not supported for now.

## FAQ

<details><summary><b>Is it safe?</b></summary>

Yes. It only adjusts the appearance (CSS), runs only on the CooSpace 5 site, has no server, sends no data and has no access to other sites. The full source is public for anyone to inspect. Its only permissions are `storage` (to remember your chosen theme) and access to the CooSpace 5 site.
</details>

<details><summary><b>How do I go back to the original?</b></summary>

Choose **Light → Eredeti** and the **Klasszikus** style, or just turn the extension off; the page reverts instantly.
</details>

<details><summary><b>Why does Firefox need the “Allow” button?</b></summary>

Firefox does not grant extensions access to a site by default; it must be confirmed once. In Chrome, Edge and Brave this is granted on install.
</details>

<details><summary><b>Something looks wrong</b></summary>

Send a screenshot on the [issue page](https://github.com/zoltan-234/cs5-egyedi-temak/issues/new/choose) and say which theme and style. Switch to another theme meanwhile.
</details>

<details><summary><b>Is it official?</b></summary>

No. It is an independent, unofficial project, not affiliated with the operators or developers of the CooSpace site.
</details>

## For developers

```bash
python3 tools/build-themes.py     # generate themes (with contrast checks)
python3 tools/build-layouts.py    # generate styles
bash tools/build.sh               # packages into dist/ (Firefox + Chromium)
python3 tools/build-guide.py      # guide PDFs
python3 tools/build-assets.py     # README images
```

CooSpace element selectors: [`docs/ELEMEK.md`](docs/ELEMEK.md) (Hungarian). See also [CONTRIBUTING.md](CONTRIBUTING.md), [BUILD.md](BUILD.md), [CHANGELOG.md](CHANGELOG.md).

## Licence

[PolyForm Noncommercial 1.0.0](LICENSE): free to use, copy and modify for **non-commercial purposes**; it may not be used to make money. The fonts (Inter, Manrope) are under the SIL OFL licence.

<sub>Unofficial project. The name CooSpace belongs to its owner.</sub>
