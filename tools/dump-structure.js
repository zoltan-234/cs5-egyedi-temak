// Unics elrendezés-fa – DevTools konzolba illesztve futtatandó.
// Kiírja a DOM vázát (tag, id, stabil osztályok, méret, layout-tulajdonságok).
// Szöveget, neveket, linkeket NEM gyűjt. Az eredmény a vágólapra kerül.
(() => {
  const MAX_DEPTH = 18;
  const SKIP = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "LINK", "META", "TEMPLATE"]);
  const stable = (s) => !/\d{3,}/.test(s);

  // jss osztályok: a szám része változhat, de a pozíció jelzésnek jó, ezért rövidítve megtartjuk.
  const label = (el) => {
    let s = el.tagName.toLowerCase();
    if (el.id && stable(el.id)) s += "#" + el.id;
    const cls = [...el.classList].filter(stable).map((c) => (/^jss\d+$/.test(c) ? "jss*" : c));
    const uniq = [...new Set(cls)].slice(0, 5);
    if (uniq.length) s += "." + uniq.join(".");
    return s;
  };

  const layout = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const parts = [`${Math.round(r.width)}x${Math.round(r.height)}`];
    if (cs.display !== "block" && cs.display !== "inline") parts.push(cs.display);
    if (cs.display.includes("flex")) {
      parts.push(cs.flexDirection);
      if (cs.flexWrap !== "nowrap") parts.push(cs.flexWrap);
      if (cs.gap !== "normal") parts.push("gap " + cs.gap);
    }
    if (cs.display.includes("grid")) parts.push("cols " + cs.gridTemplateColumns.split(" ").length);
    if (cs.position !== "static") parts.push(cs.position);
    if (cs.borderRadius !== "0px") parts.push("r " + cs.borderRadius);
    if (cs.padding !== "0px") parts.push("p " + cs.padding);
    if (cs.boxShadow !== "none") parts.push("shadow");
    if (cs.backgroundImage !== "none") parts.push(cs.backgroundImage.startsWith("url") ? "bg-img" : "bg-gradient");
    return parts.join(" | ");
  };

  const visible = (el) => {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };

  const lines = [];

  function walk(el, depth) {
    if (depth > MAX_DEPTH) return;
    // SVG belsejét nem bontjuk ki
    const kids = el.tagName === "svg" ? [] :
      [...el.children].filter((c) => !SKIP.has(c.tagName) && visible(c));

    let i = 0;
    while (i < kids.length) {
      const sig = label(kids[i]);
      let j = i + 1;
      while (j < kids.length && label(kids[j]) === sig) j++;
      const n = j - i;
      lines.push(`${"  ".repeat(depth)}${sig}${n > 1 ? ` ×${n}` : ""}  [${layout(kids[i])}]`);
      walk(kids[i], depth + 1); // ismétlődőknél csak az elsőt bontjuk ki
      i = j;
    }
  }

  lines.push(`# ${location.pathname}  viewport ${innerWidth}x${innerHeight}`);
  walk(document.body, 0);

  const out = lines.join("\n");
  copy(out);
  console.log(out.slice(0, 3000) + (out.length > 3000 ? "\n…" : ""));
  console.log(`✓ ${lines.length} sor a vágólapon`);
})();
