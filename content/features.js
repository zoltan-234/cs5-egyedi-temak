// Extra funkciók az Unics oldalon (nem téma): 
//  1. Belépés után a Színterek oldalra ugrik, bármelyik oldalon is landolt (egyszer böngészőfülenként).
//  2. A Színterek oldalon a csoportok (Állandó, 2026/27/1 …) nyitott/csukott állapota:
//     alapmód + emlékezés név szerint.
//  3. Segédjelzések a stílusokhoz: összecsukott oldalsáv (html[data-unics-collapsed]),
//     szürke nyíl a csoportfejlécen (h2[data-ut-arrow]).
// Minden beállítás alapból KI van kapcsolva, ilyenkor az oldal nem változik.
(() => {
  const api = globalThis.browser ?? globalThis.chrome;
  const FLAG = "unicsStartDone";
  const KEYS = ["unicsStartScenes", "unicsGroupMode", "unicsGroupRemember", "unicsGroups"];
  const SEMESTER = /^\d{4}\/\d{2}\/\d+$/;

  const cfg = { startScenes: false, mode: "original", remember: false, groups: {} };
  let applied = new WeakSet(); // melyik fejléc-elemre alkalmaztuk már a szabályt (új elem = újrarajzolt csoport → újra alkalmazzuk)
  let scheduled = false;
  let resizeObs = null;
  let observedMenu = null;

  function readCfg(res) {
    cfg.startScenes = !!res.unicsStartScenes;
    cfg.mode = res.unicsGroupMode || "original";
    cfg.remember = !!res.unicsGroupRemember;
    cfg.groups = res.unicsGroups && typeof res.unicsGroups === "object" ? res.unicsGroups : {};
  }

  function ssGet(k) { try { return sessionStorage.getItem(k); } catch { return null; } }
  function ssSet(k, v) { try { sessionStorage.setItem(k, v); } catch { /* nincs tár */ } }
  function ssDel(k) { try { sessionStorage.removeItem(k); } catch { /* nincs tár */ } }

  // ---------- 3a. Összecsukott oldalsáv jelzése ----------
  function updateCollapsed() {
    const menu = document.getElementById("leftmenu");
    if (!menu) return;
    if (menu !== observedMenu && "ResizeObserver" in window) {
      resizeObs?.disconnect();
      resizeObs = new ResizeObserver(updateCollapsedNow);
      resizeObs.observe(menu);
      observedMenu = menu;
    }
    updateCollapsedNow();
  }
  function updateCollapsedNow() {
    const menu = document.getElementById("leftmenu");
    if (!menu) return;
    const narrow = menu.getBoundingClientRect().width < 110;
    document.documentElement.toggleAttribute("data-unics-collapsed", narrow);
  }

  // ---------- 1. Induláskor a Színterek oldalra ----------
  function maybeStartAtScenes() {
    if (document.getElementById("loginbox")) { ssDel(FLAG); return; }   // kilépett: újra lehet ugrani
    if (!document.querySelector("aside#left")) return;                  // még nincs bejelentkezett felület
    if (ssGet(FLAG)) return;
    ssSet(FLAG, "1");                                                   // a következő oldalakon már nem ugrik
    if (!cfg.startScenes) return;
    const path = location.pathname.replace(/\/+$/, "").toLowerCase();
    if (path === "/scenes" || path.startsWith("/scenes/")) return;      // már ott vagyunk
    // A menüből a Színterek hivatkozást a címe alapján keressük (nem az ikon osztálya alapján).
    const link = document.querySelector('aside#left a[href$="/Scenes" i]');
    if (link) {
      link.click();
      // Ha a kattintás nem vitt el (pl. még nem él a menü), biztos úton megyünk.
      setTimeout(() => { if (!location.pathname.toLowerCase().startsWith("/scenes")) location.assign("/Scenes"); }, 1500);
    } else {
      location.assign("/Scenes");
    }
  }

  // ---------- 2. Csoportok ----------
  const heads = () => document.querySelectorAll('h2[id^="termid_"]');
  const nameOf = (h) => h.textContent.trim();

  function isOpen(h) {
    const hh = h.getBoundingClientRect().height;
    const wrap = h.parentElement?.getBoundingClientRect().height ?? 0;
    const next = h.nextElementSibling?.getBoundingClientRect().height ?? 0;
    return wrap > hh + 8 || next > 8;
  }

  function wanted(name, firstSemester) {
    if (cfg.remember && cfg.groups[name]) return cfg.groups[name];
    if (cfg.mode === "closed") return "closed";
    if (cfg.mode === "open") return "open";
    if (cfg.mode === "current") return name === firstSemester ? "open" : "closed";
    return null;
  }

  function applyGroups() {
    const list = [...heads()];
    if (!list.length) return;
    const first = list.map(nameOf).find((n) => SEMESTER.test(n));
    for (const h of list) {
      const name = nameOf(h);
      if (!name || applied.has(h)) continue;
      applied.add(h);
      const want = wanted(name, first);
      if (!want) continue;
      // Kis várakozás: a ReactCollapse animációja ne zavarja a mérést.
      setTimeout(() => {
        if (!h.isConnected) return;
        if (isOpen(h) !== (want === "open")) h.click();
      }, 300);
    }
  }

  // Felhasználói kattintás: megjegyezzük (a saját, programozott kattintás nem "trusted").
  document.addEventListener("click", (e) => {
    if (!e.isTrusted || !cfg.remember) return;
    const h = e.target instanceof Element ? e.target.closest('h2[id^="termid_"]') : null;
    if (!h) return;
    const name = nameOf(h);
    setTimeout(() => {
      if (!h.isConnected) return;
      cfg.groups = { ...cfg.groups, [name]: isOpen(h) ? "open" : "closed" };
      api.storage.local.set({ unicsGroups: cfg.groups });
    }, 500);
  }, true);

  // ---------- 3b. Szürke nyíl a csoportfejlécen (témához) ----------
  function tagArrows() {
    if (!document.documentElement.dataset.unicsTheme) return;
    for (const h of heads()) {
      if (h.dataset.utArrow) continue;
      for (const pe of ["::before", "::after"]) {
        const cs = getComputedStyle(h, pe);
        const m = cs.backgroundColor.match(/[\d.]+/g);
        if (!m || cs.content === "none") continue;
        const [r, g, b, a = 1] = m.map(Number);
        if (a > 0.5 && Math.max(r, g, b) - Math.min(r, g, b) < 12 && r < 235 && r > 60) {
          h.dataset.utArrow = pe === "::before" ? "before" : "after";
          break;
        }
      }
    }
  }

  // ---------- futtatás ----------
  function tick() {
    scheduled = false;
    updateCollapsed();
    maybeStartAtScenes();
    tagArrows();
    applyGroups();
  }
  function schedule() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(tick);
  }

  api.storage.local.get(KEYS).then((res) => {
    readCfg(res);
    new MutationObserver(schedule).observe(document.documentElement, { childList: true, subtree: true });
    schedule();
  });

  api.storage.onChanged.addListener((changes, area) => {
    if (area !== "local" || !KEYS.some((k) => changes[k])) return;
    api.storage.local.get(KEYS).then((res) => {
      const prevMode = cfg.mode;
      readCfg(res);
      // Alapmód változott: a csoportok újra az új szabály szerint álljanak be.
      if (changes.unicsGroupMode || (changes.unicsGroupRemember && !changes.unicsGroups)) applied = new WeakSet();
      if (changes.unicsGroupMode && prevMode !== cfg.mode) applied = new WeakSet();
      schedule();
    });
  });
})();
