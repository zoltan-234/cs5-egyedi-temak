# Forrás és építés (Mozilla-ellenőrzőknek)

A bővítmény JavaScript-kódja és a `base.css`, `modern.css` kézzel írt, nincs tömörítve vagy csomagolva.
Két CSS-készletet Python-szkriptek generálnak:

- `themes/<id>.css` és `themes.json` ← `tools/build-themes.py` (a színpalettákból)
- `layouts/glass.css`, `floating.css`, `brutal.css` ← `tools/build-layouts.py` (`layouts/modern.css` + `layouts/src/<id>.css`)

## Építés (Python 3, Linux/macOS, `zip` parancs)

```
python3 tools/build-themes.py
python3 tools/build-layouts.py
bash tools/build.sh
```

Eredmény: `dist/cs5-temak-<verzió>-firefox.zip` – ez azonos a beküldött csomaggal.
Külső függőség nincs (se npm, se pip).
