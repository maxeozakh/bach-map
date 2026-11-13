#!/usr/bin/env python3
"""Download one portrait or cover per node from Wikipedia into img/. Safe to re-run: skips files that exist."""
import json, os, time, urllib.parse, urllib.request, urllib.error
from nodes import N

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
UA = {"User-Agent": "bach-map-personal-notes/1.0 (local research page; batch pageimages)"}


def have(nid):
    return any(os.path.exists(os.path.join(IMG, f"{nid}.{e}")) for e in ("jpg", "png", "webp"))


def get(url, tries=6):
    delay = 5
    for _ in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 90)
    raise RuntimeError("still rate limited: " + url)


todo = [(i, w) for i, w in [(n[0], n[5]) for n in N] + [("joscha_bach", "Joscha Bach")] if w and not have(i)]
print("to fetch:", len(todo))
thumb = {}
for i in range(0, len(todo), 40):
    batch = todo[i:i + 40]
    q = urllib.parse.urlencode(dict(action="query", format="json", prop="pageimages", piprop="thumbnail",
                                    pithumbsize=400, pilicense="any", redirects=1, titles="|".join(w for _, w in batch)))
    d = json.loads(get("https://en.wikipedia.org/w/api.php?" + q))["query"]
    alias = {}
    for k in ("normalized", "redirects"):
        for r in d.get(k, []):
            alias[r["from"]] = r["to"]
    by_title = {p["title"]: p.get("thumbnail", {}).get("source") for p in d["pages"].values()}
    for nid, w in batch:
        t = w
        for _ in range(3):
            t = alias.get(t, t)
        thumb[nid] = by_title.get(t)
    time.sleep(1)

ok = 0
for nid, w in todo:
    src = thumb.get(nid)
    if not src:
        print("no image:", nid, w)
        continue
    ext = src.rsplit(".", 1)[-1].lower()
    ext = "jpg" if ext in ("jpg", "jpeg") else "png" if ext in ("png", "svg", "gif") else "webp" if ext == "webp" else "jpg"
    try:
        open(os.path.join(IMG, f"{nid}.{ext}"), "wb").write(get(src))
        ok += 1
    except Exception as e:
        print("failed:", nid, w, e)
    time.sleep(1.2)
print("downloaded", ok)
