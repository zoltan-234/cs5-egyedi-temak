// Unics DOM-szkenner – DevTools konzolba illesztve futtatandó.
// Csak szelektorokat és színeket gyűjt, az oldal szövegét NEM.
// Az eredményt JSON-ként a vágólapra másolja.
(() => {
  const isTransparent = (c) => c === "rgba(0, 0, 0, 0)" || c === "transparent";
  // Generált (számokat tartalmazó) id-k/osztályok kiszűrése, mert oldalanként változnak.
  const stable = (s) => !/\d{3,}/.test(s);

  const sel = (el) => {
    if (!el) return "";
    let s = el.tagName.toLowerCase();
    if (el.id && stable(el.id)) s += "#" + el.id;
    const cls = [...el.classList].filter(stable).slice(0, 4);
    if (cls.length) s += "." + cls.join(".");
    return s;
  };

  const map = new Map();
  for (const el of document.querySelectorAll("body *")) {
    const r = el.getBoundingClientRect();
    if (r.width < 20 || r.height < 10) continue;
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") continue;

    const bg = cs.backgroundColor;
    const hasImg = cs.backgroundImage !== "none";
    const border = parseFloat(cs.borderTopWidth) > 0 || parseFloat(cs.borderBottomWidth) > 0
      ? cs.borderTopColor : null;
    const shadow = cs.boxShadow !== "none";
    if (isTransparent(bg) && !hasImg && !border && !shadow) continue;

    const key = sel(el);
    const e = map.get(key) ?? {
      selector: key,
      parent: sel(el.parentElement),
      count: 0,
      bg,
      color: cs.color,
      border,
      shadow,
      bgImage: hasImg ? cs.backgroundImage.slice(0, 80) : null,
      maxArea: 0,
    };
    e.count++;
    e.maxArea = Math.max(e.maxArea, Math.round(r.width * r.height));
    map.set(key, e);
  }

  const rows = [...map.values()].sort((a, b) => b.maxArea - a.maxArea).slice(0, 100);
  const out = {
    page: location.pathname,
    viewport: `${innerWidth}x${innerHeight}`,
    iframes: document.querySelectorAll("iframe").length,
    stylesheets: [...document.styleSheets].map((s) => s.href).filter(Boolean),
    rootVars: [...document.styleSheets].flatMap((s) => {
      try { return [...s.cssRules]; } catch { return []; }
    }).filter((r) => r.selectorText === ":root")
      .flatMap((r) => [...r.style].filter((p) => p.startsWith("--")).map((p) => `${p}: ${r.style.getPropertyValue(p).trim()}`))
      .slice(0, 80),
    rows,
  };

  console.table(rows.map(({ selector, count, bg, color, border }) => ({ selector, count, bg, color, border })));
  copy(JSON.stringify(out, null, 1));
  console.log(`✓ ${rows.length} elem a vágólapon (${out.page})`);
})();
