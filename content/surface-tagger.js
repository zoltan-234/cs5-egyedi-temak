// Sötét témához: megjelöli azokat az elemeket, amelyek kiszámolt stílusa
// fehér/világosszürke háttér, világos keret, világos ::before/::after álelem
// vagy sötét szöveg – akkor is, ha nincs rájuk stabil szelektor
// (osztály nélküli div, generált jss osztály, inline style).
// A tényleges átszínezést a base.css [data-ut-*] szabályai végzik.
(() => {
  const ATTR_BG = "data-ut-bg";
  const ATTR_FG = "data-ut-fg";
  const ATTR_BORDER = "data-ut-border";
  const ATTR_BEFORE = "data-ut-before";
  const ATTR_AFTER = "data-ut-after";
  const ALL_ATTRS = [ATTR_BG, ATTR_FG, ATTR_BORDER, ATTR_BEFORE, ATTR_AFTER];

  const SKIP_TAGS = new Set(["IMG", "SVG", "CANVAS", "VIDEO", "IFRAME", "SCRIPT", "STYLE", "LINK", "META", "HEAD", "HTML", "BR"]);
  const SKIP_INSIDE = ".avatar, .MuiAvatar-root, #header";
  const SIDES = ["Top", "Right", "Bottom", "Left"];

  let observer = null;

  function parseColor(str) {
    const m = str.match(/[\d.]+/g);
    if (!m || m.length < 3) return null;
    const [r, g, b, a = 1] = m.map(Number);
    return { r, g, b, a };
  }

  // Világos, semleges szín? → "white" (≥250) / "light" (≥lightMin) / null
  function lightness(color, minAlpha = 0.95, lightMin = 222) {
    const c = parseColor(color);
    if (!c || c.a < minAlpha) return null;
    const min = Math.min(c.r, c.g, c.b);
    const max = Math.max(c.r, c.g, c.b);
    if (max - min > 14) return null;
    if (min >= 250) return "white";
    if (min >= lightMin) return "light";
    return null;
  }

  // Fehér → "surface", világosszürke → "surface-2"
  function classifyBg(cs) {
    if (cs.backgroundImage !== "none") return null;
    const l = lightness(cs.backgroundColor);
    return l === "white" ? "surface" : l === "light" ? "surface-2" : null;
  }

  // Vastag világos keret → "gap" (háttérszín, résnek látszik), vékony → "line"
  function classifyBorder(cs) {
    let maxWidth = 0;
    for (const s of SIDES) {
      const w = parseFloat(cs[`border${s}Width`]);
      // Kereteknél a #ccc-szerű elválasztók is számítanak (≥190)
      if (w > 0 && cs[`border${s}Style`] !== "none" && lightness(cs[`border${s}Color`], 0.5, 190)) {
        maxWidth = Math.max(maxWidth, w);
      }
    }
    if (maxWidth === 0) return null;
    return maxWidth >= 4 ? "gap" : "line";
  }

  // ::before / ::after álelem világos háttérrel (pl. elválasztó sáv)
  function classifyPseudo(el, which) {
    const ps = getComputedStyle(el, which);
    if (ps.content === "none" || ps.content === "normal") return null;
    return classifyBg(ps);
  }

  function isDarkText(cs) {
    const c = parseColor(cs.color);
    if (!c || c.a < 0.3) return false;
    const lum = (0.2126 * c.r + 0.7152 * c.g + 0.0722 * c.b) / 255;
    return lum < 0.5;
  }

  function isTagged(el) {
    return ALL_ATTRS.some((a) => el.hasAttribute(a));
  }

  function candidates(root) {
    if (root.nodeType !== 1) return [];
    const list = [root, ...root.querySelectorAll("*")];
    return list.filter((el) =>
      !SKIP_TAGS.has(el.tagName.toUpperCase()) &&
      !isTagged(el) &&
      !el.closest(SKIP_INSIDE));
  }

  // Előbb minden olvasás, utána minden írás – így nincs layout thrashing.
  function process(roots) {
    const els = roots.flatMap(candidates);
    const marks = els.map((el) => {
      const cs = getComputedStyle(el);
      return {
        el,
        [ATTR_BG]: classifyBg(cs),
        [ATTR_FG]: isDarkText(cs) ? "" : null,
        [ATTR_BORDER]: classifyBorder(cs),
        [ATTR_BEFORE]: classifyPseudo(el, "::before"),
        [ATTR_AFTER]: classifyPseudo(el, "::after"),
      };
    });
    for (const m of marks) {
      for (const attr of ALL_ATTRS) {
        if (m[attr] !== null) m.el.setAttribute(attr, m[attr]);
      }
    }
  }

  function clear(el) {
    for (const attr of ALL_ATTRS) el.removeAttribute(attr);
  }

  function onMutations(mutations) {
    const roots = [];
    for (const m of mutations) {
      if (m.type === "childList") {
        m.addedNodes.forEach((n) => n.nodeType === 1 && roots.push(n));
      } else if (m.target.nodeType === 1) {
        // Osztály/inline stílus változott (pl. lenyitott elem): újraértékelés
        clear(m.target);
        roots.push(m.target);
      }
    }
    if (roots.length) process(roots);
  }

  function start() {
    if (observer) return;
    observer = new MutationObserver(onMutations);
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ["class", "style"],
    });
    if (document.body) process([document.body]);
    else document.addEventListener("DOMContentLoaded", () => process([document.body]), { once: true });
  }

  function stop() {
    observer?.disconnect();
    observer = null;
    document.querySelectorAll(ALL_ATTRS.map((a) => `[${a}]`).join(",")).forEach(clear);
  }

  globalThis.UnicsSurfaceTagger = { start, stop };
})();
