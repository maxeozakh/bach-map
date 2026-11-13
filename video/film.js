// The film of the map. Injected into index.html by render.mjs.
// Every frame is a pure function of film time: frame(t) sets the whole state of the page (camera, selection,
// panel, controls, cursor) from t alone, so frames can be rendered in any order and on any number of workers.
(() => {
  const W = innerWidth, H = innerHeight;
  // the shots were laid out for a 1280x720 page; X, Y and Z scale them to the real viewport, K to the film's length
  const X = W / 1280, Y = H / 720, Z = X, K = 19.9 / 36;
  const clamp = u => u < 0 ? 0 : u > 1 ? 1 : u;
  const seg = (t, a, b) => clamp((t - a) / (b - a));
  const ease = u => { u = clamp(u); return u < .5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2; };   // in and out
  const easeOut = u => 1 - Math.pow(1 - clamp(u), 3);
  const sine = u => .5 - Math.cos(Math.PI * clamp(u)) / 2;
  const lerp = (a, b, u) => a + (b - a) * u;

  // ---- film-only dressing: a cursor, a click ring, and fades for things the page itself switches in one frame
  const css = document.createElement('style');
  css.textContent = `
    #world.focus .node { opacity: var(--dim, .22); }
    #world.focus #edges path { opacity: var(--dime, .07); }
    #world.focus .node.hi { opacity: 1; }
    #world.focus #edges path.hi { opacity: 1; stroke: color-mix(in srgb, var(--text) calc(var(--hi, 1) * 100%), var(--edge)); stroke-width: calc(1.2px + .8px * var(--hi, 1)); }
    #fcur { position: fixed; left: 0; top: 0; z-index: 100; width: 22px; height: 22px; pointer-events: none; transform-origin: 3px 2px; }
    #fring { position: fixed; left: 0; top: 0; z-index: 99; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--text); pointer-events: none; }
    #psize { display: none !important; }
    .slab { opacity: var(--sch, 0) !important; transition: none !important; }
    .eralab, .lanelab, .rule, .vrule { opacity: calc(1 - var(--sch, 0)) !important; transition: none !important; }
    * { scrollbar-width: none; }
  `;
  document.head.appendChild(css);
  document.body.insertAdjacentHTML('beforeend',
    `<div id="fring"></div><svg id="fcur" viewBox="0 0 22 22"><path d="M3 2 L3 18.2 L7.3 14.3 L10.1 20.6 L12.9 19.4 L10.1 13.2 L15.8 13.2 Z" fill="#0b0c0f" stroke="#fff" stroke-width="1.3" stroke-linejoin="round"/></svg>`);
  const cur = el('fcur'), ring = el('fring'), panel = el('panel'), hud = el('hud'), root = document.documentElement;

  // ---- camera: the world point (cx, cy) sits at the screen point (ax, ay), at scale s
  const fromView = (ax, ay) => ({ cx: (ax - tx) / sc, cy: (ay - ty) / sc, s: sc, ax, ay });
  const center = (id, s, ax, ay) => ({ cx: pos[id].x + CW / 2, cy: pos[id].y + CH / 2, s, ax, ay });
  // smooth zoom-and-pan between two cameras (van Wijk and Nuij): pulls back, travels, pushes in, as one move
  function fly(a, b, u) {
    const w0 = W / a.s, w1 = W / b.s, dx = b.cx - a.cx, dy = b.cy - a.cy, d2 = dx * dx + dy * dy, rho = 1.25, r2 = rho * rho, r4 = r2 * r2;
    let k, w;
    if (d2 < 1e-6) { k = 0; w = w0 * Math.exp(u * Math.log(w1 / w0)); }
    else {
      const d1 = Math.sqrt(d2), b0 = (w1 * w1 - w0 * w0 + r4 * d2) / (2 * w0 * r2 * d1), b1 = (w1 * w1 - w0 * w0 - r4 * d2) / (2 * w1 * r2 * d1);
      const r0 = Math.log(Math.sqrt(b0 * b0 + 1) - b0), r1 = Math.log(Math.sqrt(b1 * b1 + 1) - b1), S = (r1 - r0) / rho, sv = u * S * rho;
      const cosh = x => (Math.exp(x) + Math.exp(-x)) / 2, sinh = x => (Math.exp(x) - Math.exp(-x)) / 2, tanh = x => sinh(x) / cosh(x);
      k = (w0 / (r2 * d1)) * (cosh(r0) * tanh(sv + r0) - sinh(r0));
      w = w0 * cosh(r0) / cosh(sv + r0);
    }
    return { cx: a.cx + k * dx, cy: a.cy + k * dy, s: W / w, ax: lerp(a.ax, b.ax, u), ay: lerp(a.ay, b.ay, u) };
  }

  // ---- measure the real interface once: where the buttons are that the cursor will press
  const PW0 = 460;                      // the detail panel's width
  hud.classList.remove('closed'); el('hudtoggle').textContent = 'hide';
  root.style.setProperty('--pw', PW0 + 'px');
  fit();
  const FIT = fromView(W / 2, H / 2);
  const mid = r => ({ x: r.left + r.width / 2, y: r.top + r.height / 2 });
  const gHide = mid(el('hudtoggle').getBoundingClientRect());
  const sb = el('schools').getBoundingClientRect(), gSch = { x: sb.left + sb.width / 2, y: sb.top + sb.height / 2 };
  const htop = el('hud').offsetHeight + 24;
  hud.classList.add('closed'); el('hudtoggle').textContent = 'show controls';
  const gShow = mid(el('hudtoggle').getBoundingClientRect());
  select('turing');
  const bb = panel.querySelector('[data-go="bach"]').getBoundingClientRect();
  const scrollB = Math.max(0, Math.min(bb.top + bb.height / 2 - 430 * Y, panel.scrollHeight - panel.clientHeight));
  const gBach = { x: bb.left + Math.min(bb.width / 2, 56), y: bb.top + bb.height / 2 - scrollB };
  select('bach');
  const gClose = mid(el('close').getBoundingClientRect());
  select(null);

  // ---- the shots
  const AX = (W - PW0) / 2;             // centre of the board when the panel is open
  const C0 = { ...FIT, s: FIT.s * .955 }, C1 = FIT;
  const ANT = { cx: 600, cy: 336, s: Z, ax: W / 2, ay: H / 2 };                       // antiquity: myth and philosophy
  const TUR = center('turing', Z, AX, H / 2);
  const BACH = center('bach', .82 * Z, AX, H / 2);
  // pull back until the lines into the selected card fan out across the centuries, the card kept at the right
  const PS = .3 * Z, PULL = { cx: pos.bach.x + CW / 2, cy: WH / 2 - 40, s: PS, ax: W - PW0 - 150 * X, ay: H / 2 };
  // the same cards regrouped by school of thought, framed the way fit() frames the board under the open controls
  const SW = SBLOCK.W, SH = SBLOCK.H, ss = Math.min(W / SW, (H - htop) / SH) * .97;
  const SFIT = { cx: SW / 2, cy: SH / 2, s: ss, ax: W / 2, ay: htop + SH * ss / 2 };
  const k = v => Array.isArray(v) ? v.map(k) : v * K;
  const T = Object.fromEntries(Object.entries({
    hide: 3.0, toAnt: [3.4, 6.6], glide: [8.2, 12.9], clickTur: 13.8, scroll: [15.6, 16.3], clickBach: 17.1, toBach: [17.2, 20.2],
    pull: [21.6, 24.7], close: 26.3, show: 27.5, sch: 28.45, toSch: [28.45, 30.35], unsch: 32.9, back: [32.9, 34.8], end: 36,
  }).map(([n, v]) => [n, k(v)]));
  function camera(t) {
    if (t < T.toAnt[0]) return { ...C0, s: lerp(C0.s, C1.s, sine(t / T.toAnt[0])) };
    if (t < T.glide[0]) return fly(C1, ANT, ease(seg(t, ...T.toAnt)));
    if (t < T.toBach[0]) {                                   // glide along the timeline to 1936, dipping out a little on the way
      const u = ease(seg(t, ...T.glide));
      return { cx: lerp(ANT.cx, TUR.cx, u), cy: lerp(ANT.cy, TUR.cy, u), s: Z * (1 - .3 * Math.sin(Math.PI * u)), ax: lerp(ANT.ax, TUR.ax, u), ay: H / 2 };
    }
    if (t < T.pull[0]) return fly(TUR, BACH, ease(seg(t, ...T.toBach)));
    if (t < T.toSch[0]) return fly(BACH, PULL, ease(seg(t, ...T.pull)));
    if (t < T.back[0]) return fly(PULL, SFIT, ease(seg(t, ...T.toSch)));
    return fly(SFIT, C0, ease(seg(t, ...T.back)));
  }
  // card positions between the timeline (0) and the schools layout (1)
  function schools(t) { return t < T.back[0] ? ease(seg(t, ...T.toSch)) : 1 - ease(seg(t, ...T.back)); }
  const WMAX = Math.max(WW, SW), HMAX = Math.max(WH, SH);
  world.style.width = WMAX + 'px'; world.style.height = HMAX + 'px'; svg.setAttribute('width', WMAX); svg.setAttribute('height', HMAX);
  let shownU = 0;

  // ---- the cursor: rests, then moves to each target in one eased, slightly curved stroke
  const REST = { x: 742 * X, y: 452 * Y }, SIDE = { x: 664 * X, y: 556 * Y };
  const tur = { x: AX + 34, y: H / 2 + 10 };
  const moves = [   // [start, end, to]
    [1.9, 2.85, gHide], [3.5, 4.5, SIDE], [12.95, 13.65, tur], [16.05, 16.9, gBach], [17.5, 18.4, { x: 560 * X, y: 540 * Y }],
    [24.9, 25.95, gClose], [26.6, 27.35, gShow], [27.7, 28.3, gSch], [35.0, 35.9, REST],
  ].map(([a, b, to]) => [a * K, b * K, to]);
  const clicks = [T.hide, T.clickTur, T.clickBach, T.close, T.show, T.sch, T.unsch];
  function cursor(t) {
    let p = REST;
    for (const [a, b, to] of moves) {
      if (t >= b) { p = to; continue; }
      if (t > a) {
        const u = ease(seg(t, a, b)), dx = to.x - p.x, dy = to.y - p.y, bow = Math.sin(Math.PI * u) * .07;
        p = { x: p.x + dx * u - dy * bow, y: p.y + dy * u + dx * bow };
      }
      break;
    }
    return p;
  }

  let shownPanel, shownSel;
  function frame(t) {
    t = Math.max(0, Math.min(t, T.end));
    const c = camera(t);
    sc = c.s; tx = c.ax - c.cx * c.s; ty = c.ay - c.cy * c.s; apply();

    // schools of thought: the box is ticked on the first click and unticked on the second
    el('schools').checked = t >= T.sch && t < T.unsch;
    const u = schools(t);
    if (u !== shownU) {
      D.nodes.forEach(n => { const a = home[n.id], b = SBLOCK.spos[n.id]; pos[n.id] = { x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u) }; place(n.id); });
      EDGES.forEach(e => e.el.setAttribute('d', pathFor(e)));
      shownU = u;
    }
    const lab = t < T.unsch ? ease(seg(t, T.sch, T.sch + .3)) : 1 - ease(seg(t, T.unsch, T.unsch + .3));
    root.style.setProperty('--sch', lab);

    // controls panel
    const closed = t >= T.hide && t < T.show;
    hud.classList.toggle('closed', closed); el('hudtoggle').textContent = closed ? 'show controls' : 'hide';

    // selection and the detail panel. the panel lingers a moment after the close click so it can slide away
    const sel = t < T.clickTur ? null : t < T.clickBach ? 'turing' : t < T.close + .35 ? 'bach' : null;
    const pan = t < T.clickTur ? null : t < T.clickBach ? 'turing' : t < T.close + .4 ? 'bach' : null;
    if (pan !== shownPanel || sel !== shownSel) {
      select(pan);
      if (pan && sel !== pan) { select(null); panel.classList.add('open'); }
      shownPanel = pan; shownSel = sel;
    }
    const cp = cursor(t);
    root.style.setProperty('--pw', PW0 + 'px');
    const slide = t < T.close ? 1 - easeOut(seg(t, T.clickTur, T.clickTur + .45)) : ease(seg(t, T.close, T.close + .4));
    panel.style.transform = slide ? `translateX(${(slide * 100).toFixed(3)}%)` : '';
    panel.scrollTop = pan === 'turing' ? scrollB * ease(seg(t, ...T.scroll)) : 0;

    // focus fades in on the first click and out on close
    const f = t < T.close ? ease(seg(t, T.clickTur, T.clickTur + .4)) : 1 - ease(seg(t, T.close, T.close + .35));
    root.style.setProperty('--dim', lerp(1, .22, f)); root.style.setProperty('--dime', lerp(1, .07, f)); root.style.setProperty('--hi', f);

    // cursor and click ring
    let press = 0, rg = null;
    for (const k of clicks) { if (t >= k - .07 && t < k + .11) press = 1; if (t >= k && t < k + .45) rg = (t - k) / .45; }
    cur.style.transform = `translate(${(cp.x - 3).toFixed(2)}px,${(cp.y - 2).toFixed(2)}px) scale(${press ? .86 : 1})`;
    if (rg === null) ring.style.display = 'none';
    else { const r = 5 + 19 * easeOut(rg); ring.style.display = 'block'; ring.style.width = ring.style.height = 2 * r + 'px';
      ring.style.transform = `translate(${cp.x - r}px,${cp.y - r}px)`; ring.style.opacity = .55 * (1 - rg); }
  }
  window.__film = { dur: T.end, frame, T };
})();
