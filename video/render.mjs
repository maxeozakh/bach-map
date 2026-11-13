// Renders the film of the map frame by frame in headless Chromium.
//   node render.mjs stills 0 1 3.2 ...        a few frames by time, into stills/
//   node render.mjs frames [fps] [workers]    every frame, into frames/, on parallel workers
// The page is laid out at 1280x720 and drawn at 1.5x, so the film is 1920x1080 with the interface a readable size.
import { chromium } from 'playwright-core';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';
import os from 'node:os';
import { execFileSync } from 'node:child_process';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const EXE = path.join(os.homedir(), 'Library/Caches/ms-playwright/chromium_headless_shell-1194/chrome-mac/headless_shell');
const PAGE = pathToFileURL(path.join(HERE, '..', 'index.html')).href;

// Two thumbnails are animated GIFs, which play on the wall clock and would make a frame depend on when it was drawn.
// The film shows their first frame instead.
const IMG = path.join(HERE, '..', 'img'), STILL = path.join(HERE, 'frames-gif');
const frozen = {};
fs.mkdirSync(STILL, { recursive: true });
for (const f of fs.readdirSync(IMG)) {
  const fd = fs.openSync(path.join(IMG, f), 'r'), head = Buffer.alloc(4); fs.readSync(fd, head, 0, 4, 0); fs.closeSync(fd);
  if (head.toString('latin1') !== 'GIF8') continue;
  const out = path.join(STILL, f.replace(/\.[^.]+$/, '') + '.png');
  if (!fs.existsSync(out)) execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', path.join(IMG, f), '-frames:v', '1', out]);
  frozen['img/' + f] = pathToFileURL(out).href;
}

async function open() {
  const browser = await chromium.launch({ executablePath: EXE });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1.5, colorScheme: 'dark' });
  await page.goto(PAGE);
  await page.evaluate(frozen => {
    D.nodes.forEach(n => { if (frozen[n.img]) n.img = frozen[n.img]; });
    document.querySelectorAll('.node img').forEach(i => { const k = i.getAttribute('src'); if (frozen[k]) i.src = frozen[k]; });
  }, frozen);
  // nothing may pop in mid-film: load every image and the font before the first frame
  await page.evaluate(async () => {
    const imgs = [...document.images];
    imgs.forEach(i => { i.loading = 'eager'; });
    await Promise.all(imgs.map(i => i.decode().catch(() => {})));
    await document.fonts.ready;
  });
  await page.addScriptTag({ path: path.join(HERE, 'film.js') });
  return { browser, page };
}
async function shot(page, t, file) {
  await page.evaluate(t => { window.__film.frame(t); return new Promise(r => requestAnimationFrame(() => r())); }, t);
  await page.screenshot({ path: file, type: 'png' });
}

const [mode, ...args] = process.argv.slice(2);
if (mode === 'stills') {
  const dir = path.join(HERE, 'stills'); fs.mkdirSync(dir, { recursive: true });
  const { browser, page } = await open();
  for (const a of args) await shot(page, +a, path.join(dir, `t${(+a).toFixed(2).padStart(5, '0')}.png`));
  console.log('dur', await page.evaluate(() => window.__film.dur));
  await browser.close();
} else if (mode === 'frames') {
  const fps = +(args[0] || 60), workers = +(args[1] || 6);
  const dir = path.join(HERE, 'frames'); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
  const probe = await open(); const dur = await probe.page.evaluate(() => window.__film.dur); await probe.browser.close();
  const n = Math.round(dur * fps), t0 = Date.now();
  await Promise.all(Array.from({ length: workers }, async (_, w) => {
    const { browser, page } = await open();
    for (let i = Math.floor(n * w / workers); i < Math.floor(n * (w + 1) / workers); i++)
      await shot(page, i / fps, path.join(dir, `f${String(i).padStart(5, '0')}.png`));
    await browser.close();
  }));
  console.log(`${n} frames at ${fps} fps in ${((Date.now() - t0) / 1000).toFixed(0)} s`);
}
