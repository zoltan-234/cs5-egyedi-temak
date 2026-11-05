// Generált JSS osztályok (jss642…) → stabil data-ut="név" attribútum.
//
// Az Unics a komponensek stílusait <style data-meta="Komponens"> lapokba teszi.
// A számozott osztálynév buildenként változik, de a szabály tulajdonságai nem,
// így tulajdonság alapján megtaláljuk az aktuális osztályt, és az elemeket
// stabil attribútummal jelöljük. CSS-ben: [data-ut~="term-btn"].
(() => {
  const ATTR = "data-ut";

  // meta: a <style data-meta> értéke; test: a szabály deklarációira
  const RULES = [
    // Színterek: félév-gombok ("Állandó", "2026/27/1"…) – 180×60, 10px kerek
    { name: "term-btn", meta: "SceneList", test: (s) => s.width === "180px" && s.height === "60px" },
    // Színterek: a félév-gombok sávja (negatív margók, halvány háttér)
    { name: "term-bar", meta: "SceneList", test: (s) => s.marginTop === "-20px" && s.paddingBottom === "20px" },
    // Színterek: kurzuskártyák rácsa
    { name: "scene-grid", meta: "SceneList", test: (s) => s.flexWrap === "wrap" && s.marginLeft === "51px" },
    // Színterek: nézetváltó / szűrő eszköztár
    { name: "view-bar", meta: "SceneList", test: (s) => s.height === "58px" && s.alignItems === "center" },
    // Fejléc: oldalcím sor
    { name: "page-title", meta: "PageTitle", test: (s) => s.height === "60px" && s.fontSize === "20px" },
  ];

  const classToNames = new Map();
  let observer = null;

  function addMapping(cls, name) {
    const names = classToNames.get(cls) ?? new Set();
    names.add(name);
    classToNames.set(cls, names);
  }

  function resolve() {
    classToNames.clear();
    for (const styleEl of document.querySelectorAll("style[data-meta]")) {
      const rules = RULES.filter((r) => r.meta === styleEl.dataset.meta);
      if (!rules.length) continue;
      let cssRules;
      try { cssRules = styleEl.sheet?.cssRules; } catch { continue; }
      if (!cssRules) continue;
      for (const rule of cssRules) {
        const m = rule.selectorText?.match(/^\.(jss\d+)$/);
        if (!m) continue;
        for (const r of rules) if (r.test(rule.style)) addMapping(m[1], r.name);
      }
    }
  }

  function tagAll() {
    for (const [cls, names] of classToNames) {
      for (const el of document.getElementsByClassName(cls)) {
        const current = new Set((el.getAttribute(ATTR) ?? "").split(" ").filter(Boolean));
        let changed = false;
        for (const n of names) if (!current.has(n)) { current.add(n); changed = true; }
        if (changed) el.setAttribute(ATTR, [...current].join(" "));
      }
    }
  }

  function onMutations(mutations) {
    // Új JSS lap érkezett → újra feloldjuk az osztályneveket
    const newSheet = mutations.some((m) =>
      [...m.addedNodes].some((n) => n.nodeName === "STYLE"));
    if (newSheet) resolve();
    tagAll();
  }

  function start() {
    if (observer) return;
    observer = new MutationObserver(onMutations);
    observer.observe(document.documentElement, { childList: true, subtree: true });
    const run = () => { resolve(); tagAll(); };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run, { once: true });
    else run();
  }

  globalThis.UnicsJssResolver = { start };
  start();
})();
