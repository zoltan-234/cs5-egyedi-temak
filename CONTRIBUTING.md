# Közreműködés

Örülök minden hibajelentésnek és ötletnek.

## Hibát találtál?
Nyiss egy **Issue**-t a hibabejelentő sablonnal. Írd meg, melyik **téma és stílus**, melyik **oldal** a CooSpace-ben, és csatolj **képernyőképet** (a nevedet és személyes adatokat takard ki).

## Kódhoz
1. Forkold a repót, készíts ágat.
2. A témák és stílusok generáltak, ne a kész fájlokat szerkeszd:
   - színtémák: `tools/build-themes.py` → `python3 tools/build-themes.py`
   - stílusok: `layouts/modern.css` (alap) és `layouts/src/<id>.css` → `python3 tools/build-layouts.py`
3. A CooSpace generált `jss…` osztályait **ne** használd szelektorban (build-enként változnak). Használd a stabil osztályokat, vagy a `jss-resolver.js` `data-ut` jelöléseit. Lásd: `docs/ELEMEK.md`.
4. CSS-ben `background-color`-t használj `background` helyett (megtartja az ikonokat), és `overflow: clip`-et `hidden` helyett.
5. Ellenőrzés: `npx web-ext lint` és `bash tools/build.sh`.
6. Nyiss Pull Requestet.

## Licenc
A közreműködéseddel elfogadod, hogy a PolyForm Noncommercial 1.0.0 licenc alatt kerül be a projektbe.
