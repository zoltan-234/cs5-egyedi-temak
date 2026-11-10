# Útmutató tartalma (magyar + angol). A tools/build-guide.py ebből készít PDF-et és Markdownt.
REPO = "https://github.com/zoltan-234/cs5-egyedi-temak"
REL = REPO + "/releases/latest"

# Képernyőképek: id -> (magyar felirat, angol felirat, mit kell lefotózni [magyarul])
SHOTS = {
 "GH-01": ("A GitHub Releases oldal: itt tölthető le a két fájl", "The GitHub Releases page: the two downloadable files", ""),
 "GH-02": ("A letöltött fájlok: az .xpi és a -chromium.zip", "The downloaded files: the .xpi and the -chromium.zip", ""),
 "FF-00": ("Firefox: a github.com telepítési engedélye", "Firefox: permission for github.com to install an add-on", ""),
 "FF-01": ("Firefox: a CS5 Témák hozzáadása, a kért engedélyekkel", "Firefox: adding CS5 Themes, with the permissions it asks for", ""),
 "FF-02": ("Firefox: a bővítmény a kiegészítők listájában", "Firefox: the add-on in the add-ons list", ""),
 "FF-03": ("Firefox: az ikon menüje: hozzáférés a CooSpace oldalhoz, kitűzés, eltávolítás", "Firefox: the icon's menu: site access, pinning, removal", ""),
 "CH-00": ("Chrome: a menü → Bővítmények → Bővítmények kezelése", "Chrome: menu → Extensions → Manage extensions", ""),
 "CH-01": ("Chrome: a bővítménykezelő, bekapcsolt fejlesztői móddal és a betöltés gombbal", "Chrome: the extensions page with Developer mode on and the load button", ""),
 "CH-02": ("A mappaválasztó ablak: válaszd ki a kicsomagolt mappát", "The folder picker: choose the extracted folder", ""),
 "CH-03": ("Chrome: a betöltött bővítmény kártyája", "Chrome: the loaded extension card", ""),
 "CH-04": ("Chrome: a bővítmény kitűzése az eszköztárra", "Chrome: pinning the extension to the toolbar", ""),
 "CH-05": ("Chrome: a bővítmény eltávolítása", "Chrome: removing the extension", ""),
 "ED-00": ("Edge: a menü → Bővítmények → Bővítmények kezelése", "Edge: menu → Extensions → Manage extensions", ""),
 "ED-01": ("Edge: a bővítménykezelő, bekapcsolt fejlesztői móddal és a betöltés gombbal", "Edge: the extensions page with Developer mode on and the load button", ""),
 "ED-02": ("Edge: a betöltött bővítmény kártyája", "Edge: the loaded extension card", ""),
 "ED-03": ("Edge: kitűzés az eszköztárra és eltávolítás a bővítmények menüjéből", "Edge: pinning to the toolbar and removing from the extensions menu", ""),
 "BR-00": ("Brave: a menü → Bővítmények → Bővítmények kezelése", "Brave: menu → Extensions → Manage extensions", ""),
 "BR-01": ("Brave: a bővítménykezelő, bekapcsolt fejlesztői móddal és a betöltés gombbal", "Brave: the extensions page with Developer mode on and the load button", ""),
 "BR-02": ("Brave: a betöltött bővítmény kártyája", "Brave: the loaded extension card", ""),
 "BR-03": ("Brave: kitűzés az eszköztárra és eltávolítás", "Brave: pinning to the toolbar and removal", ""),
}

def browser(code, name, addr, devmode_hu, devmode_en):
    """Chromium-alapú böngésző fejezete (a három ugyanolyan)."""
    return code, name, addr, devmode_hu, devmode_en

CHAPTERS_HU = [
 ("h1", "mi", "1. Mi ez, és mire jó?"),
 ("p", "A <b>CS5 Témák</b> egy kis böngészőbővítmény a <b>CooSpace 5 (CS5)</b> felületéhez. Segítségével kiválaszthatod, hogyan nézzen ki az oldal: 19 színtéma (világos, színes, rózsaszín, sötét) és 5 stílus (Klasszikus, Modern, Üveg, Szigetek, Brutalista) közül, és tetszőlegesen kombinálhatod őket."),
 ("list", ["A választásod <b>megmarad</b> frissítés (F5) és a böngésző újraindítása után is.", "Egy kattintással váltasz: a bővítmény ikonjára kattintva megnyílik a választó ablak.", "Ingyenes, és bármikor kikapcsolható vagy eltávolítható."]),
 ("note", "ok", "Nem kell aggódnod: ez csak a kinézetet változtatja", "A bővítmény <b>kizárólag az oldal megjelenését</b> módosítja (színek, formák, animációk). Biztonságos, mert:"),
 ("list", [
   "<b>Csak a CooSpace 5 oldalán fut</b>, más weboldalhoz nem fér hozzá.",
   "<b>Nem küld el semmit sehova</b>: nincs szervere, nincs követés, nincs statisztika. A választott téma csak a saját böngésződben tárolódik.",
   "<b>Nem módosítja a CooSpace adatait</b>: nem ír, nem küld be semmit, nem érinti a jegyeidet, üzeneteidet vagy beadandóidat. Ha kikapcsolod, minden pontosan olyan, mint előtte.",
   "<b>Nem kér jelszót</b>, és nem fér hozzá a böngésződ jelszavaihoz, előzményeihez vagy más füleihez.",
   "<b>Nyílt a forráskód</b>: a teljes kód megtekinthető a GitHubon, bárki ellenőrizheti.",
   "<b>Nem hivatalos</b> projekt, nem áll kapcsolatban a CooSpace oldal üzemeltetőivel vagy fejlesztőivel."]),
 ("p", "Technikai pontosság kedvéért: a bővítménynek a CooSpace oldalon futnia kell, hogy átszínezhesse azt. Ezt a böngésző külön engedélyhez köti (lásd a telepítési részt). Az oldal tartalmát nem olvassa ki és nem továbbítja, csak a megjelenést (színeket, méreteket) állítja."),

 ("h1", "melyik", "2. Melyik böngészőt használod?"),
 ("p", "A telepítés böngészőnként kicsit más. Keresd meg a sajátodat a táblázatban, majd ugorj a hozzá tartozó fejezetre."),
 ("table", ["Böngésző", "Telepítés módja", "Marad újraindítás után?", "Automatikus frissítés"], [
   ["<b>Firefox</b>", "Aláírt .xpi fájl, egy kattintás", "Igen", "Igen (naponta)"],
   ["<b>Chrome</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"],
   ["<b>Edge</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"],
   ["<b>Brave</b>", "Kicsomagolt mappa betöltése", "Igen, ha a mappa a helyén marad", "Nem, kézzel"]]),
 ("note", "info", "Telefonon és tableten", "Androidos Chrome, Edge és Brave nem támogat bővítményeket, ezért ott nem használható. Az Android-Firefoxon nem teszteltük, nem ajánlott. A bővítmény asztali gépre (Windows, macOS, Linux) készült."),

 ("h1", "letoltes", "3. A fájl letöltése"),
 ("p", "Minden kiadás a GitHub <b>Releases</b> oldalán található: <code>%s</code>" % REL),
 ("steps", [
   ("Nyisd meg a fenti oldalt. Az <b>Assets</b> (Fájlok) listában két fájlt látsz.", ["GH-01"]),
   ("<b>Firefox-hoz</b> az <code>.xpi</code> végű fájlt töltsd le (pl. <code>cs5-temak-0.7.1.xpi</code>).", []),
   ("<b>Chrome-hoz, Edge-hez és Brave-hez</b> a <code>…-chromium.zip</code> fájlt töltsd le.", ["GH-02"])]),

 ("h1", "firefox", "4. Telepítés Firefoxban"),
 ("note", "ok", "Ez a legkényelmesebb", "A Firefox-verzió a Mozilla által <b>aláírt</b>, ezért egyszerűen telepíthető, tartósan megmarad, és magától frissül."),
 ("steps", [
   ("Töltsd le az <code>.xpi</code> fájlt a Releases oldalról (lásd a 3. fejezetet): kattints a hivatkozásra, vagy nyisd meg a letöltött fájlt.", []),
   ("A Firefox megkérdezi, engedélyezed-e a <b>github.com</b>-nak, hogy kiegészítőt telepítsen. Kattints a <b>Telepítés folytatása</b> gombra.", ["FF-00"]),
   ("Megjelenik a <b>CS5 Témák hozzáadása</b> ablak. Itt látod, mit kér a bővítmény: csak a CooSpace 5 oldalán lévő adatok elérését, és hogy nem gyűjt adatot. Kattints a <b>Hozzáadás</b> gombra.", ["FF-01"]),
   ("Ellenőrizd: a <code>about:addons</code> oldalon a <b>CS5 Témák</b> a bővítmények között látszik, bekapcsolva.", ["FF-02"]),
   ("Adj hozzáférést a CooSpace oldalhoz (Firefoxban ezt külön meg kell tenni, egyszer): kattints jobb gombbal a bővítmény ikonjára, és válaszd a <b>Mindig engedélyezve a következőkön: unics.szte.hu</b> lehetőséget. Ugyanitt tűzheted ki az ikont az eszköztárra (<b>Rögzítés az eszköztárra</b>). A bővítmény popupjában is van egy <b>Engedélyezés</b> gomb, az ugyanezt teszi.", ["FF-03"]),
   ("Nyisd meg a CooSpace oldalt, kattints az ikonra, és válassz színt és stílust. A változás azonnal látszik.", [])]),
 ("note", "info", "Frissítés", "A Firefox naponta egyszer ellenőrzi, van-e újabb verzió, és magától frissít. Azonnali kereséshez: <code>about:addons</code> → fogaskerék → <b>Bővítmények frissítéseinek keresése</b>."),

 ("h1", "chrome", "5. Telepítés Chrome-ban"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "A Chrome a letöltött mappából olvassa a fájlokat, nem másolja át. Ezért a mappát <b>ne töröld és ne helyezd át</b>, különben a bővítmény leáll."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és <b>csomagold ki egy állandó helyre</b>, pl. <code>Dokumentumok\\cs5-temak</code>. Jobb klikk → <b>Összes kibontása</b>. A kicsomagolt mappában közvetlenül ott kell lennie a <code>manifest.json</code> fájlnak.", []),
   ("Nyisd meg a bővítménykezelőt: a Chrome menüje (⋮) → <b>Bővítmények</b> → <b>Bővítmények kezelése</b>. (Vagy írd a címsorba: <code>chrome://extensions</code>.)", ["CH-00"]),
   ("Kapcsold be jobb felül a <b>Fejlesztői módot</b>, majd kattints a <b>Kicsomagolt elemek betöltése</b> gombra.", ["CH-01"]),
   ("Válaszd ki a kicsomagolt mappát, és kattints a <b>Mappaválasztás</b> gombra.", ["CH-02"]),
   ("A <b>CS5 Témák</b> megjelenik a listában, hibajelzés nélkül.", ["CH-03"]),
   ("Tűzd ki az ikont: puzzle ikon → a CS5 Témák melletti tűzőcsap.", ["CH-04"]),
   ("Nyisd meg a CooSpace oldalt, kattints az ikonra, és válassz témát (lásd a 8. fejezetet).", [])]),
 ("note", "info", "Nem kell az „Engedélyezés” gomb", "Chrome-ban, Edge-ben és Brave-ben az oldalhoz való hozzáférés telepítéskor már megvan, a Firefoxtól eltérően."),

 ("h1", "edge", "6. Telepítés Edge-ben"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "Az Edge is a kicsomagolt mappából olvassa a fájlokat. A mappát <b>ne töröld és ne helyezd át</b>."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és csomagold ki egy állandó helyre.", []),
   ("Nyisd meg a bővítménykezelőt: az Edge menüje (⋯) → <b>Bővítmények</b> → <b>Bővítmények kezelése</b>. (Vagy: <code>edge://extensions</code>.)", ["ED-00"]),
   ("Kapcsold be a bal alsó sarokban a <b>Fejlesztői módot</b>, majd kattints a <b>Kicsomagolt bővítmény betöltése</b> gombra.", ["ED-01"]),
   ("Válaszd ki azt a mappát, amiben a <code>manifest.json</code> van (ugyanaz a mappaválasztó ablak, mint Chrome-ban).", ["CH-02"]),
   ("A <b>CS5 Témák</b> megjelenik a listában, hibajelzés nélkül.", ["ED-02"]),
   ("Tűzd ki az ikont az eszköztárra: Bővítmények (puzzle) menü → a CS5 Témák melletti tűzőcsap.", ["ED-03"]),
   ("Nyisd meg a CooSpace oldalt, és válassz témát (8. fejezet).", [])]),

 ("h1", "brave", "7. Telepítés Brave-ben"),
 ("note", "warn", "Fontos: a mappa a bővítmény helye", "A Brave is a kicsomagolt mappából olvassa a fájlokat. A mappát <b>ne töröld és ne helyezd át</b>."),
 ("steps", [
   ("Töltsd le a <code>…-chromium.zip</code> fájlt (3. fejezet), és csomagold ki egy állandó helyre.", []),
   ("Nyisd meg a bővítménykezelőt: a Brave menüje (☰) → <b>Bővítmények</b> → <b>Bővítmények kezelése</b>. (Vagy: <code>brave://extensions</code>.)", ["BR-00"]),
   ("Kapcsold be jobb felül a <b>Fejlesztői módot</b>, majd kattints a <b>Kicsomagolt elemek betöltése</b> gombra.", ["BR-01"]),
   ("Válaszd ki azt a mappát, amiben a <code>manifest.json</code> van (ugyanaz a mappaválasztó ablak, mint Chrome-ban).", ["CH-02"]),
   ("A <b>CS5 Témák</b> megjelenik a listában, hibajelzés nélkül.", ["BR-02"]),
   ("Tűzd ki az ikont az eszköztárra: puzzle ikon → a CS5 Témák melletti tűzőcsap.", ["BR-03"]),
   ("Nyisd meg a CooSpace oldalt, és válassz témát (8. fejezet).", [])]),
 ("note", "info", "Vivaldi, Opera és más Chromium-böngészők", "Ezekben ugyanígy működik a kicsomagolt betöltés (a cím <code>vivaldi://extensions</code>, ill. <code>opera://extensions</code>). Ezeket nem teszteltük."),

 ("h1", "hasznalat", "8. Használat"),
 ("steps", [
   ("Nyisd meg a CooSpace oldalt, és kattints a bővítmény ikonjára.", []),
   ("<b>Színek:</b> válassz a témák közül (Világos, Többszínű, Rózsaszín, Sötét). A kis előnézet mutatja a színeket.", []),
   ("<b>Stílus:</b> legörgetve válassz formát: Klasszikus (az eredeti), Modern, Üveg, Szigetek vagy Brutalista.", []),
   ("A kettő szabadon kombinálható, a változás azonnal látszik, és a böngésző bezárása után is megmarad.", []),
   ("<b>Funkciók:</b> a popup alján három kapcsoló van (induláskor a Színterek oldalra; csoportok alapmódja; emlékezés a csoportokra). Mindegyik mellett egy <b>ⓘ</b> jel magyarázza, mit csinál. Alapból mind ki van kapcsolva.", [])]),
 ("note", "info", "Vissza az eredetihez", "Válaszd a <b>Világos → Eredeti</b> színt és a <b>Klasszikus</b> stílust: az oldal pontosan úgy néz ki, mint a bővítmény nélkül."),

 ("h1", "figyelj", "9. Amikre figyelj"),
 ("list", [
   "<b>Chrome, Edge, Brave:</b> a kicsomagolt mappát <b>ne töröld, ne nevezd át és ne helyezd át</b>. Ha mégis, a bővítmény hibával kikapcsol; tedd vissza, vagy töltsd be újra.",
   "<b>Ne csomagold a Letöltések mappába</b>, mert ott könnyen kitörlődik. Állandó helyet válassz.",
   "<b>Chrome/Edge figyelmeztetés:</b> indításkor megjelenhet egy üzenet a „fejlesztői módú bővítményekről”. Ez normális, bezárhatod, a bővítmény működik.",
   "<b>Firefox:</b> az Engedélyezés gombot egyszer kell megnyomni. Utána minden CooSpace-oldalon működik.",
   "<b>Frissítés kézzel</b> (Chrome, Edge, Brave): lásd a következő fejezetet.",
   "Csak a CooSpace 5 oldalán látszik a hatása. Más weboldalakat nem változtat."]),

 ("h1", "frissites", "10. Frissítés"),
 ("p", "<b>Firefox:</b> automatikus, nem kell tenned semmit."),
 ("p", "<b>Chrome, Edge, Brave:</b>"),
 ("steps", [
   ("Töltsd le az új <code>…-chromium.zip</code> fájlt a Releases oldalról.", []),
   ("Csomagold ki <b>ugyanabba a mappába</b>, a régi fájlok fölé (felülírás).", []),
   ("Nyisd meg a bővítménykezelőt, és kattints a CS5 Témák kártyán az <b>Újratöltés</b> (⟳) gombra.", []),
   ("A CooSpace oldalon nyomj egy F5-öt.", [])]),

 ("h1", "hiba", "11. Hibaelhárítás"),
 ("table", ["Mi a gond?", "Megoldás"], [
   ["Nem változik az oldal kinézete", "Firefoxban nyomd meg a popupban az <b>Engedélyezés</b> gombot, vagy az ikon jobb klikk menüjében válaszd a <b>Mindig engedélyezve a következőkön: unics.szte.hu</b> lehetőséget. Nyomj F5-öt. Ellenőrizd, hogy a <code>unics.szte.hu</code> oldalon vagy-e."],
   ["Az Engedélyezés gomb nem tűnik el (Firefox)", "Kattints rá újra, és a böngésző kérdésére válaszolj <b>Engedélyezés</b>-sel. Ha így sem megy, indítsd újra a Firefoxot."],
   ["Újraindítás után eltűnt a bővítmény (Chrome/Edge/Brave)", "Valószínűleg a kicsomagolt mappa törlődött vagy elmozdult. Csomagold ki újra egy állandó helyre, és töltsd be."],
   ["Hibajelzés a bővítménykártyán", "Nyisd meg a Hibák gombot, és küldd el a szöveget a GitHub Issues oldalon. Próbáld meg az Újratöltés gombot is."],
   ["Valami rosszul néz ki (olvashatatlan szöveg, fehér doboz)", "Készíts képernyőképet, és írd meg, melyik téma és stílus. Addig válts másik témára."],
   ["Lassú az oldal", "Az Üveg stílus (elmosás) gyengébb gépen terhelőbb lehet. Válts Modern vagy Klasszikus stílusra."]]),

 ("h1", "eltavolitas", "12. Eltávolítás"),
 ("p", "Az eltávolítás után az oldal visszaáll az eredeti kinézetre, és a bővítmény minden adata törlődik a böngésződből."),
 ("steps", [
   ("<b>Firefox:</b> jobb klikk a bővítmény ikonján → <b>Kiegészítő eltávolítása</b> (vagy <code>about:addons</code> → <b>…</b> → <b>Eltávolítás</b>).", ["FF-03"]),
   ("<b>Chrome:</b> puzzle ikon → a CS5 Témák melletti <b>⋮</b> → <b>Eltávolítás a Chrome-ból</b> (vagy <code>chrome://extensions</code> → <b>Eltávolítás</b>).", ["CH-05"]),
   ("<b>Edge:</b> Bővítmények (puzzle) menü → <b>⋯</b> → <b>Eltávolítás a Microsoft Edge-ből</b>.", ["ED-03"]),
   ("<b>Brave:</b> puzzle ikon → a CS5 Témák melletti <b>⋮</b> → <b>Eltávolítás a Brave-ből</b>.", ["BR-03"]),
   ("Chrome/Edge/Brave esetén ezután a kicsomagolt mappát is törölheted.", [])]),

 ("h1", "licenc", "13. Licenc, hibabejelentés"),
 ("list", [
   "<b>Licenc:</b> PolyForm Noncommercial 1.0.0. Szabadon használható, másolható és módosítható <b>nem kereskedelmi célra</b>, de pénzt keresni vele nem lehet. A betűtípusok (Inter, Manrope) az SIL OFL licenc alatt állnak.",
   "<b>Nem hivatalos</b> projekt, nem áll kapcsolatban a CooSpace oldal üzemeltetőivel vagy fejlesztőivel.",
   "<b>Hibát találtál, vagy ötleted van?</b> Írj a GitHub <b>Issues</b> oldalon: <code>%s/issues</code>. Képernyőképet is csatolhatsz." % REPO,
   "A kód nyilvános: <code>%s</code>" % REPO]),
]

CHAPTERS_EN = [
 ("h1", "mi", "1. What is this?"),
 ("p", "<b>CS5 Themes</b> is a small browser extension for the <b>CooSpace 5 (CS5)</b> site. It lets you choose how the site looks: 19 colour themes (light, colourful, pink, dark) and 5 styles (Classic, Modern, Glass, Islands, Brutalist), freely combined."),
 ("list", ["Your choice <b>is kept</b> after a refresh (F5) and after restarting the browser.", "Switch with one click: click the extension icon and the picker opens.", "Free, and can be turned off or removed at any time."]),
 ("note", "ok", "Nothing to worry about: it only changes the looks", "The extension changes <b>only how the page looks</b> (colours, shapes, animations). It is safe because:"),
 ("list", [
   "<b>It runs only on the CooSpace 5 site</b> and has no access to any other website.",
   "<b>It sends nothing anywhere</b>: no server, no tracking, no analytics. Your chosen theme is stored only in your own browser.",
   "<b>It does not change any CooSpace data</b>: it submits nothing and does not touch your grades, messages or assignments. Turn it off and everything is exactly as before.",
   "<b>It never asks for a password</b> and has no access to your saved passwords, history or other tabs.",
   "<b>The source code is open</b>: the full code is on GitHub for anyone to inspect.",
   "It is an <b>unofficial</b> project, not affiliated with the operators or developers of the CooSpace site."]),
 ("p", "To be technically precise: the extension has to run on the CooSpace page in order to recolour it, which the browser gates behind a separate permission (see the install chapters). It does not read out or forward the page's content; it only adjusts the appearance (colours, sizes)."),

 ("h1", "melyik", "2. Which browser do you use?"),
 ("p", "Installation differs slightly per browser. Find yours in the table, then jump to its chapter."),
 ("table", ["Browser", "How to install", "Stays after restart?", "Automatic updates"], [
   ["<b>Firefox</b>", "Signed .xpi file, one click", "Yes", "Yes (daily)"],
   ["<b>Chrome</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"],
   ["<b>Edge</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"],
   ["<b>Brave</b>", "Load an unpacked folder", "Yes, as long as the folder stays put", "No, manual"]]),
 ("note", "info", "Phones and tablets", "Chrome, Edge and Brave on Android do not support extensions, so it cannot be used there. We have not tested Firefox for Android, so it is not recommended. The extension is made for desktop computers (Windows, macOS, Linux)."),

 ("h1", "letoltes", "3. Downloading the file"),
 ("p", "Every release is on the GitHub <b>Releases</b> page: <code>%s</code>" % REL),
 ("steps", [
   ("Open the page above. In the <b>Assets</b> list you will see two files.", ["GH-01"]),
   ("<b>For Firefox</b> download the file ending in <code>.xpi</code> (e.g. <code>cs5-temak-0.7.1.xpi</code>).", []),
   ("<b>For Chrome, Edge and Brave</b> download the <code>…-chromium.zip</code> file.", ["GH-02"])]),

 ("h1", "firefox", "4. Installing in Firefox"),
 ("note", "ok", "This is the easiest one", "The Firefox version is <b>signed</b> by Mozilla, so it installs simply, stays permanently and updates itself."),
 ("steps", [
   ("Download the <code>.xpi</code> file from the Releases page (chapter 3): click the link, or open the downloaded file.", []),
   ("Firefox asks whether to allow <b>github.com</b> to install an add-on. Click <b>Continue to Installation</b>.", ["FF-00"]),
   ("The <b>Add CS5 Themes</b> window appears. It shows what the extension asks for: access to data on the CooSpace 5 site only, and that it collects no data. Click <b>Add</b>.", ["FF-01"]),
   ("Check: on <code>about:addons</code> the <b>CS5 Themes</b> is listed among your extensions, switched on.", ["FF-02"]),
   ("Grant access to the CooSpace site (Firefox requires this separately, once): right-click the extension icon and choose <b>Always allow on unics.szte.hu</b>. You can also pin the icon to the toolbar there (<b>Pin to Toolbar</b>). The extension popup also has an <b>Allow</b> button that does the same.", ["FF-03"]),
   ("Open the CooSpace site, click the icon and choose a colour and a style. The change is instant.", [])]),
 ("note", "info", "Updates", "Firefox checks once a day for a newer version and updates itself. To check right away: <code>about:addons</code> → gear icon → <b>Check for Updates</b>."),

 ("h1", "chrome", "5. Installing in Chrome"),
 ("note", "warn", "Important: the folder is the extension's home", "Chrome reads the files from the downloaded folder instead of copying them. So <b>do not delete or move</b> the folder, otherwise the extension stops."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and <b>extract it to a permanent place</b>, e.g. <code>Documents\\cs5-temak</code>. Right-click → <b>Extract All</b>. <code>manifest.json</code> must be directly inside the extracted folder.", []),
   ("Open the extensions page: Chrome menu (⋮) → <b>Extensions</b> → <b>Manage extensions</b>. (Or type <code>chrome://extensions</code>.)", ["CH-00"]),
   ("Switch on <b>Developer mode</b> in the top right, then click <b>Load unpacked</b>.", ["CH-01"]),
   ("Choose the extracted folder and click <b>Select Folder</b>.", ["CH-02"]),
   ("<b>CS5 Themes</b> appears in the list, with no error.", ["CH-03"]),
   ("Pin the icon: puzzle icon → the pin next to CS5 Themes.", ["CH-04"]),
   ("Open the CooSpace site, click the icon and choose a theme (chapter 8).", [])]),
 ("note", "info", "No “Allow” button needed", "In Chrome, Edge and Brave, access to the site is already granted on install, unlike Firefox."),

 ("h1", "edge", "6. Installing in Edge"),
 ("note", "warn", "Important: the folder is the extension's home", "Edge also reads the files from the extracted folder. <b>Do not delete or move</b> the folder."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and extract it to a permanent place.", []),
   ("Open the extensions page: Edge menu (⋯) → <b>Extensions</b> → <b>Manage extensions</b>. (Or: <code>edge://extensions</code>.)", ["ED-00"]),
   ("Switch on <b>Developer mode</b> in the bottom left, then click <b>Load unpacked</b>.", ["ED-01"]),
   ("Choose the folder that contains <code>manifest.json</code> (the same folder picker as in Chrome).", ["CH-02"]),
   ("<b>CS5 Themes</b> appears in the list, with no error.", ["ED-02"]),
   ("Pin the icon to the toolbar: Extensions (puzzle) menu → the pin next to CS5 Themes.", ["ED-03"]),
   ("Open the CooSpace site and choose a theme (chapter 8).", [])]),

 ("h1", "brave", "7. Installing in Brave"),
 ("note", "warn", "Important: the folder is the extension's home", "Brave also reads the files from the extracted folder. <b>Do not delete or move</b> the folder."),
 ("steps", [
   ("Download the <code>…-chromium.zip</code> file (chapter 3) and extract it to a permanent place.", []),
   ("Open the extensions page: Brave menu (☰) → <b>Extensions</b> → <b>Manage extensions</b>. (Or: <code>brave://extensions</code>.)", ["BR-00"]),
   ("Switch on <b>Developer mode</b> in the top right, then click <b>Load unpacked</b>.", ["BR-01"]),
   ("Choose the folder that contains <code>manifest.json</code> (the same folder picker as in Chrome).", ["CH-02"]),
   ("<b>CS5 Themes</b> appears in the list, with no error.", ["BR-02"]),
   ("Pin the icon to the toolbar: puzzle icon → the pin next to CS5 Themes.", ["BR-03"]),
   ("Open the CooSpace site and choose a theme (chapter 8).", [])]),
 ("note", "info", "Vivaldi, Opera and other Chromium browsers", "Loading unpacked works the same way there (address <code>vivaldi://extensions</code> or <code>opera://extensions</code>). We have not tested these."),

 ("h1", "hasznalat", "8. Using it"),
 ("steps", [
   ("Open the CooSpace site and click the extension icon.", []),
   ("<b>Colours:</b> pick a theme (Light, Colourful, Pink, Dark). The small preview shows the colours.", []),
   ("<b>Style:</b> scroll down and pick a shape: Classic (the original), Modern, Glass, Islands or Brutalist.", []),
   ("The two combine freely, the change is instant, and it survives closing the browser.", []),
   ("<b>Features:</b> at the bottom of the popup there are three switches (open the Scenes page on start; default mode of the groups; remember groups). Each has an <b>ⓘ</b> mark that explains what it does. All are off by default.", [])]),
 ("note", "info", "Back to the original", "Choose <b>Light → Eredeti</b> as the colour and <b>Klasszikus</b> as the style: the page looks exactly as it does without the extension."),

 ("h1", "figyelj", "9. Things to watch out for"),
 ("list", [
   "<b>Chrome, Edge, Brave:</b> <b>do not delete, rename or move</b> the extracted folder. If you do, the extension switches off with an error; put it back or load it again.",
   "<b>Do not extract into the Downloads folder</b>, where it is easily deleted. Pick a permanent place.",
   "<b>Chrome/Edge warning:</b> at startup a message about “developer mode extensions” may appear. This is normal; close it, the extension works.",
   "<b>Firefox:</b> the Allow button is pressed once. After that it works on every CooSpace page.",
   "<b>Manual updates</b> (Chrome, Edge, Brave): see the next chapter.",
   "The effect is visible only on the CooSpace 5 site. It changes no other website."]),

 ("h1", "frissites", "10. Updating"),
 ("p", "<b>Firefox:</b> automatic, nothing to do."),
 ("p", "<b>Chrome, Edge, Brave:</b>"),
 ("steps", [
   ("Download the new <code>…-chromium.zip</code> from the Releases page.", []),
   ("Extract it <b>into the same folder</b>, over the old files (overwrite).", []),
   ("Open the extensions page and click <b>Reload</b> (⟳) on the CS5 Themes card.", []),
   ("Press F5 on the CooSpace site.", [])]),

 ("h1", "hiba", "11. Troubleshooting"),
 ("table", ["What is wrong?", "Fix"], [
   ["The page does not change", "In Firefox press <b>Allow</b> in the popup, or choose <b>Always allow on unics.szte.hu</b> in the icon's right-click menu. Press F5. Check that you are on the CooSpace 5 site."],
   ["The Allow button does not go away (Firefox)", "Click it again and answer the browser prompt with <b>Allow</b>. If it still fails, restart Firefox."],
   ["The extension vanished after a restart (Chrome/Edge/Brave)", "The extracted folder was probably deleted or moved. Extract it again to a permanent place and load it."],
   ["Error on the extension card", "Open the Errors button and send the text via GitHub Issues. Also try the Reload button."],
   ["Something looks wrong (unreadable text, white box)", "Take a screenshot and tell us which theme and style. Switch to another theme meanwhile."],
   ["The page feels slow", "The Glass style (blur) can be heavier on weaker machines. Switch to Modern or Classic."]]),

 ("h1", "eltavolitas", "12. Removing it"),
 ("p", "After removal the page returns to its original look and all extension data is deleted from your browser."),
 ("steps", [
   ("<b>Firefox:</b> right-click the extension icon → <b>Remove Extension</b> (or <code>about:addons</code> → <b>…</b> → <b>Remove</b>).", ["FF-03"]),
   ("<b>Chrome:</b> puzzle icon → the <b>⋮</b> next to CS5 Themes → <b>Remove from Chrome</b> (or <code>chrome://extensions</code> → <b>Remove</b>).", ["CH-05"]),
   ("<b>Edge:</b> Extensions (puzzle) menu → <b>⋯</b> → <b>Remove from Microsoft Edge</b>.", ["ED-03"]),
   ("<b>Brave:</b> puzzle icon → the <b>⋮</b> next to CS5 Themes → <b>Remove from Brave</b>.", ["BR-03"]),
   ("For Chrome/Edge/Brave you can then delete the extracted folder too.", [])]),

 ("h1", "licenc", "13. Licence, reporting issues"),
 ("list", [
   "<b>Licence:</b> PolyForm Noncommercial 1.0.0. Free to use, copy and modify for <b>non-commercial purposes</b>; it may not be used to make money. The fonts (Inter, Manrope) are under the SIL OFL licence.",
   "<b>Unofficial</b> project, not affiliated with the operators or developers of the CooSpace site.",
   "<b>Found a bug or have an idea?</b> Write on the GitHub <b>Issues</b> page: <code>%s/issues</code>. You can attach a screenshot." % REPO,
   "The code is public: <code>%s</code>" % REPO]),
]

META = {
 "hu": dict(file="utmutato-hu", title="CS5 Témák – telepítési útmutató", sub="Egyedi témák a CooSpace 5 felületéhez",
            ver="Verzió", toc="Tartalom", guide="Útmutató", footer="Nem hivatalos projekt · nem kereskedelmi licenc", missing="Ide kerül a képernyőkép", other="English version: GUIDE.md"),
 "en": dict(file="guide-en", title="CS5 Themes – installation guide", sub="Custom themes for CooSpace 5",
            ver="Version", toc="Contents", guide="Guide", footer="Unofficial project · non-commercial licence", missing="Screenshot goes here", other="Magyar verzió: UTMUTATO.md"),
}
