// Beszúrja a mentett színtémát és stílust (layout) az Unics oldalba.
// document_start-kor fut, hogy ne villanjon fel az eredeti design.
(() => {
  const api = globalThis.browser ?? globalThis.chrome;

  // Két független réteg: storage-kulcs → html data-attribútum
  const SLOTS = {
    unicsTheme:  { attr: "unicsTheme",  linkAttr: "data-unics-theme-link" },
    unicsLayout: { attr: "unicsLayout", linkAttr: "data-unics-layout-link" },
  };

  function apply(key, state) {
    const slot = SLOTS[key];
    const root = document.documentElement;
    document.querySelectorAll(`link[${slot.linkAttr}]`).forEach((l) => l.remove());

    if (key === "unicsTheme") syncDark(state);

    if (!state || !Array.isArray(state.css) || state.css.length === 0) {
      delete root.dataset[slot.attr];
      return;
    }
    root.dataset[slot.attr] = state.id;
    for (const path of state.css) {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = api.runtime.getURL(path);
      link.setAttribute(slot.linkAttr, "");
      (document.head || root).appendChild(link);
    }
  }

  // Sötét témánál a fehér/világos elemek felderítése (surface-tagger.js).
  // Régi mentett állapotban még nincs "dark" mező, ezért id alapján is felismerjük.
  function syncDark(state) {
    const root = document.documentElement;
    const dark = state?.dark ?? ["dark", "nord"].includes(state?.id);
    if (dark) root.dataset.unicsDark = "";
    else delete root.dataset.unicsDark;

    // A felület-jelölő minden színtémánál fut (az "Eredeti" kivételével),
    // mert a világos témák felülete sem tiszta fehér.
    const tagger = globalThis.UnicsSurfaceTagger;
    if (state?.css?.length) tagger?.start();
    else tagger?.stop();
  }

  // Az oldal saját stíluslapjai után kell lennünk, különben azok felülírnak.
  function moveLinksToEnd() {
    const target = document.head || document.documentElement;
    for (const slot of Object.values(SLOTS)) {
      document.querySelectorAll(`link[${slot.linkAttr}]`).forEach((l) => target.appendChild(l));
    }
  }

  // Firefox (browser.*) és Chromium MV3 (chrome.*) is Promise-t ad vissza.
  api.storage.local.get(Object.keys(SLOTS)).then((res) => {
    for (const key of Object.keys(SLOTS)) apply(key, res[key]);
  });

  document.addEventListener("DOMContentLoaded", moveLinksToEnd);

  // Popupban váltott beállítás azonnal érvényesül minden nyitott fülön.
  api.storage.onChanged.addListener((changes, area) => {
    if (area !== "local") return;
    for (const key of Object.keys(SLOTS)) {
      if (changes[key]) apply(key, changes[key].newValue);
    }
    if (document.readyState !== "loading") moveLinksToEnd();
  });
})();
