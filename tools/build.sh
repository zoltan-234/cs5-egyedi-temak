#!/usr/bin/env bash
# Csomagok készítése a dist/ mappába:
#   cs5-temak-<verzió>-firefox.zip    -> Mozilla aláírásra (ebből lesz az .xpi)
#   cs5-temak-<verzió>-chromium.zip   -> Chrome / Edge / Brave (kicsomagolva betölthető)
# Futtatás a repó gyökeréből: bash tools/build.sh
set -euo pipefail
cd "$(dirname "$0")/.."

VER=$(python3 -c "import json;print(json.load(open('manifest.json'))['version'])")
FILES=(manifest.json content popup themes layouts fonts icons themes.json layouts.json)
rm -rf dist && mkdir -p dist/ff dist/cr

for d in ff cr; do
  cp -r "${FILES[@]}" "dist/$d/"
  rm -rf "dist/$d/layouts/src"        # forrásfájlok, a csomagban nem kellenek
done

# Chromiumhoz kivesszük a Firefox-specifikus update_url-t
python3 - <<PY
import json
p="dist/cr/manifest.json"
m=json.load(open(p,encoding="utf-8"))
m.get("browser_specific_settings",{}).get("gecko",{}).pop("update_url",None)
json.dump(m,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
PY

(cd dist/ff && zip -qr "../cs5-temak-$VER-firefox.zip" .)
(cd dist/cr && zip -qr "../cs5-temak-$VER-chromium.zip" .)
rm -rf dist/ff dist/cr
echo "Kész:"; ls -1 dist
