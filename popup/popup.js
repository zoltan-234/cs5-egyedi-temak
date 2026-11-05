const api = globalThis.browser ?? globalThis.chrome;
const ORIGINS = { origins: ["https://unics.szte.hu/*"] };

// Popup-csoportok: melyik lista, melyik json, melyik storage-kulcs
const GROUPS = [
  { listId: "themes",  source: "themes.json",  key: "unicsTheme",  fallback: "original" },
  { listId: "layouts", source: "layouts.json", key: "unicsLayout", fallback: "classic" },
];

async function loadJson(path) {
  const res = await fetch(api.runtime.getURL(path));
  return res.json();
}

// Mentés: a content script a storage.onChanged-en keresztül azonnal frissít.
async function select(group, item) {
  await api.storage.local.set({ [group.key]: { id: item.id, css: item.css, dark: !!item.dark } });
  markActive(group.listId, item.id);
}

function markActive(listId, id) {
  document.querySelectorAll(`#${listId} .option`).forEach((el) => {
    el.setAttribute("aria-checked", String(el.dataset.id === id));
  });
}

function buildVisual(item) {
  const wrap = document.createElement("span");
  if (item.preview) {
    wrap.append(buildMiniPreview(item.preview, item.previewHeader));
    wrap.className = "mini-wrap";
  } else {
    wrap.className = `layout-icon layout-${item.id}`;
    wrap.append(document.createElement("span"), document.createElement("span"));
  }
  return wrap;
}

// Mini előnézet: bal menü-csík, fejléc-sáv, háttér, rajta egy kártya
// kiemelő sávval és pöttyel
function buildMiniPreview([bg, surface, accent, accent2, sidebar], headerGrad) {
  const mini = document.createElement("span");
  mini.className = "mini";
  mini.style.background = bg;

  const side = document.createElement("span");
  side.className = "mini-side";
  side.style.background = sidebar ?? surface;
  const sideDots = [accent, accent2, accent];
  for (const c of sideDots) {
    const d = document.createElement("span");
    d.style.background = c;
    side.append(d);
  }
  mini.append(side);

  if (headerGrad) {
    const head = document.createElement("span");
    head.className = "mini-head";
    head.style.background = headerGrad;
    mini.append(head);
  }

  const card = document.createElement("span");
  card.className = "mini-card";
  card.style.background = surface;

  const bar = document.createElement("span");
  bar.className = "mini-bar";
  bar.style.background = accent;

  const dot = document.createElement("span");
  dot.className = "mini-dot";
  dot.style.background = accent2 ?? accent;

  card.append(bar, dot);
  mini.append(card);
  return mini;
}

// Csoportcím a témarácsban ("Világos", "Többszínű"…), két oszlopot átfogva
function buildSubheading(label) {
  const li = document.createElement("li");
  li.className = "subgroup";
  li.setAttribute("role", "presentation");
  li.textContent = label;
  return li;
}

function renderGroup(group, items, currentId) {
  const list = document.getElementById(group.listId);
  let lastGroup = null;
  for (const item of items) {
    if (item.group && item.group !== lastGroup) {
      list.appendChild(buildSubheading(item.group));
      lastGroup = item.group;
    }
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.className = "option";
    btn.type = "button";
    btn.role = "radio";
    btn.dataset.id = item.id;

    const text = document.createElement("span");
    text.className = "text";
    const name = document.createElement("span");
    name.className = "name";
    name.textContent = item.name;
    text.appendChild(name);
    if (item.desc) {
      const desc = document.createElement("span");
      desc.className = "desc";
      desc.textContent = item.desc;
      text.appendChild(desc);
    }

    const check = document.createElement("span");
    check.className = "check";
    check.textContent = "✓";

    btn.append(buildVisual(item), text, check);
    btn.addEventListener("click", () => select(group, item));
    li.appendChild(btn);
    list.appendChild(li);
  }
  markActive(group.listId, currentId);
}

// Firefox MV3-ban a host-engedély alapból nincs megadva, kérni kell.
async function setupPermission() {
  if (!api.permissions?.contains) return;
  const has = await api.permissions.contains(ORIGINS);
  const box = document.getElementById("perm");
  box.hidden = has;
  if (has) return;
  document.getElementById("perm-btn").addEventListener("click", async () => {
    const granted = await api.permissions.request(ORIGINS);
    box.hidden = granted;
  });
}

// ---------- Funkciók (content/features.js olvassa) ----------
async function setupFeatures() {
  const KEYS = ["unicsStartScenes", "unicsGroupMode", "unicsGroupRemember"];
  const s = await api.storage.local.get(KEYS);
  const start = document.getElementById("f-start");
  const mode = document.getElementById("f-mode");
  const remember = document.getElementById("f-remember");
  start.checked = !!s.unicsStartScenes;
  mode.value = s.unicsGroupMode || "original";
  remember.checked = !!s.unicsGroupRemember;

  start.addEventListener("change", () => api.storage.local.set({ unicsStartScenes: start.checked }));
  mode.addEventListener("change", () => api.storage.local.set({ unicsGroupMode: mode.value }));
  remember.addEventListener("change", () => api.storage.local.set({ unicsGroupRemember: remember.checked }));

  // ⓘ jelek: a kis i betűre kattintva megjelenik/eltűnik a magyarázat
  document.querySelectorAll(".info").forEach((btn) => {
    btn.setAttribute("aria-expanded", "false");
    btn.addEventListener("click", () => {
      const tip = document.getElementById(btn.dataset.tip);
      tip.hidden = !tip.hidden;
      btn.setAttribute("aria-expanded", String(!tip.hidden));
    });
  });

  const forget = document.getElementById("f-forget");
  forget.addEventListener("click", async () => {
    await api.storage.local.remove("unicsGroups");
    forget.textContent = "Törölve";
    forget.classList.add("done");
    setTimeout(() => { forget.textContent = "Megjegyzett csoportok törlése"; forget.classList.remove("done"); }, 1500);
  });
}

(async () => {
  await setupFeatures();
  const stored = await api.storage.local.get(GROUPS.map((g) => g.key));
  for (const group of GROUPS) {
    const items = await loadJson(group.source);
    renderGroup(group, items, stored[group.key]?.id ?? group.fallback);
  }
  await setupPermission();
})();
