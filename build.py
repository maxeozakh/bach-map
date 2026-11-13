#!/usr/bin/env python3
"""Merge the four research slices into data.json and write the two pages:
index.html (the board). With --timeline also timeline.html (era-by-field grid, shelved).

  python3 build.py           merge and report unmatched references
  python3 build.py --images  also download portraits and covers from Wikipedia into img/
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from collections import defaultdict
from nodes import N, MAIN, DROP, TLDR_FIX, AUTHOR_FIX, AUTHOR_BY_FACET
from edges import E
import start_here

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "research")
FILES = ["podcasts", "ccc", "debates", "writing_cimc"]

raw = {f: json.load(open(os.path.join(R, f + ".json"))) for f in FILES}
sources = {f: {s["id"]: s for s in raw[f]["sources"]} for f in FILES}

rules = []  # (node_id, facet_label, compiled regex)
meta = {}
for nid, title, year, label, theme, wiki, facets in N:
    meta[nid] = dict(id=nid, title=title, year=year, label=label, theme=theme, wiki=wiki)
    for flabel, rx in facets:
        rules.append((nid, flabel, re.compile(rx)))


def clean(q):
    return re.sub(r"^\s*paraphrase:\s*", "", q or "", flags=re.I).strip()


def mention(f, m):
    s = sources[f].get(m.get("source_id"), {})
    return dict(
        src=s.get("title") or m.get("source_id") or "",
        url=s.get("url") or "",
        date=str(s.get("date") or ""),
        q=clean(m.get("quote_or_paraphrase")),
        v=bool(m.get("is_verbatim")),
    )


buckets = defaultdict(lambda: defaultdict(list))  # node -> facet -> entries
unmatched = []
for f in FILES:
    for r in raw[f]["references"]:
        name = r["name"].strip().lower()
        for nid, flabel, rx in rules:
            if rx.search(name):
                buckets[nid][flabel].append((f, r))
                break
        else:
            unmatched.append((f, r["name"]))


def merge_facet(label, entries):
    tldr = max((r["tldr"] for _, r in entries), key=len)
    take = max(entries, key=lambda e: (len(e[1]["mentions"]), len(e[1].get("bach_take") or "")))[1].get("bach_take") or ""
    ms, seen = [], set()
    for f, r in entries:
        for m in r["mentions"]:
            mm = mention(f, m)
            key = (mm["src"], mm["q"][:60])
            if mm["q"] and key not in seen:
                seen.add(key)
                ms.append(mm)
    ms.sort(key=lambda m: (not m["v"], m["date"]))
    authors = [r.get("author") for _, r in entries if r.get("author")]
    return dict(
        label=label, tldr=tldr, take=take, mentions=ms,
        author=min(authors, key=len) if authors else None,
        verified=any(r["verified"] for _, r in entries),
        kind=entries[0][1]["kind"],
    )


nodes = []
for nid, title, year, label, theme, wiki, facets in N:
    if theme in ("bachidea", "cimc"):
        continue
    if nid not in buckets:
        print("EMPTY NODE", nid)
        continue
    order = [fl for fl, _ in facets]
    fs = [merge_facet(fl, buckets[nid][fl]) for fl in order if fl in buckets[nid]]
    # lead with the facet that names the node itself (or an explicit override)
    lead = MAIN.get(nid)
    fs.sort(key=lambda f: 0 if f["label"] and (f["label"] == lead or (not lead and f["label"].lower() in title.lower())) else 1)
    n = dict(meta[nid])
    n["facets"] = fs
    n["nsrc"] = len({m["src"] for f in fs for m in f["mentions"]})
    n["verified"] = any(f["verified"] for f in fs)
    nodes.append(n)

# ---- Bach's own ideas (from the writing/CIMC slice), with matching raw references as extra evidence
W = raw["writing_cimc"]
IDEA_IDS = {
    "The Machine Consciousness Hypothesis": "b_mch",
    "Consciousness is a simulated property; the self is a character in a story": "b_sim",
    "Consciousness as a coherence-inducing operator (the 'conductor')": "b_conductor",
    "Consciousness comes before the self (the 'Genesis' idea)": "b_genesis",
    "Cyber-animism: software as spirit": "b_animism",
    "Computational functionalism, and weak versus strong computationalism": "b_comp",
    "Only what can be constructed (computed) exists; Gödel as the end of classical mathematics": "b_construct",
    "Levels of Lucidity": "b_lucidity",
    "Love as the discovery of shared purpose; alignment through shared purpose": "b_love",
    "Position on large language models": "b_llm",
    "No 'Turing Test' for consciousness": "b_noturing",
    "Motivated cognition: the Psi theory and MicroPsi": "b_psi",
    "Seven principles of synthetic intelligence": "b_seven",
    "Request Confirmation Networks (ReCoN)": "b_recon",
    "Attention-based learning: consciousness as a record of attention": "b_attention",
    "From elementary computation to ethics": "b_ethics",
}
IDEA_TITLES = {
    "b_sim": "Consciousness is a simulated property; the self is a story",
    "b_conductor": "Consciousness as conductor and coherence operator",
    "b_genesis": "Consciousness comes before the self",
    "b_comp": "Functionalism, weak and strong computationalism",
    "b_construct": "Only what can be constructed exists",
    "b_love": "Love as the discovery of shared purpose",
    "b_llm": "On large language models",
    "b_noturing": "No Turing test for consciousness",
    "b_psi": "Motivated cognition: Psi theory and MicroPsi",
    "b_attention": "Attention-based learning",
}
for i in W["bach_ideas"]:
    nid = IDEA_IDS[i["name"]]
    year = int(re.search(r"\d{4}", i["year_first_stated"]).group())
    ms = [dict(src=s["title"], url=s.get("url") or "", date="", q=clean(s.get("quote_or_paraphrase")), v=bool(s.get("is_verbatim")))
          for s in i["sources"]]
    seen = {(m["src"], m["q"][:60]) for m in ms}
    for fl, entries in buckets.get(nid, {}).items():
        for f, r in entries:
            for m in r["mentions"]:
                mm = mention(f, m)
                if mm["q"] and (mm["src"], mm["q"][:60]) not in seen:
                    seen.add((mm["src"], mm["q"][:60]))
                    ms.append(mm)
    tldr = re.sub(r"\s*NOTE: the task brief.*$", "", i["tldr"])
    nodes.append(dict(
        id=nid, title=IDEA_TITLES.get(nid, i["name"]), year=year, label=str(year), theme="bach", wiki=None,
        facets=[dict(label=None, tldr=tldr, take="", mentions=ms, author="Joscha Bach", verified=i["verified"], kind="theory")],
        nsrc=len({m["src"] for m in ms}), verified=i["verified"],
    ))

nodes.sort(key=lambda n: (n["year"], n["theme"] == "bach", n["title"]))
for nid, old, new in TLDR_FIX:
    hit = False
    for n in nodes:
        if n["id"] == nid:
            for f in n["facets"]:
                if old in f["tldr"]:
                    f["tldr"] = f["tldr"].replace(old, new); hit = True
    if not hit:
        print("TLDR_FIX did not match:", nid, old[:40])
byid_ = {n["id"]: n for n in nodes}
for nid, old, new in AUTHOR_FIX:
    hits = [f for f in byid_[nid]["facets"] if f["author"] == old]
    for f in hits: f["author"] = new
    if not hits: print("AUTHOR_FIX did not match:", nid, old)
for nid, label, new in AUTHOR_BY_FACET:
    hits = [f for f in byid_[nid]["facets"] if f["label"] == label]
    for f in hits: f["author"] = new
    if not hits: print("AUTHOR_BY_FACET did not match:", nid, label)

# ---- CIMC, works, bio, source list
cimc = W["cimc"]
all_sources = []
for f in FILES:
    for s in raw[f]["sources"]:
        ok = s.get("transcript_obtained", s.get("retrieved"))
        all_sources.append(dict(title=s["title"], url=s.get("url") or "", date=str(s.get("date") or ""), ok=bool(ok), slice=f))

# ---- images
IMG = os.path.join(HERE, "img")
UA = {"User-Agent": "bach-map-personal-notes/1.0 (local research page)"}


def fetch_image(nid, wiki):
    for ext in ("jpg", "png", "webp"):
        if os.path.exists(os.path.join(IMG, f"{nid}.{ext}")):
            return f"img/{nid}.{ext}"
    if "--images" not in sys.argv:
        return None
    api = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(wiki.replace(" ", "_"), safe="")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(api, headers=UA), timeout=20))
        src = (d.get("thumbnail") or {}).get("source")
        if not src:
            print("  no image:", nid, wiki)
            return None
        ext = src.rsplit(".", 1)[-1].lower()
        ext = {"jpeg": "jpg", "svg": "png"}.get(ext, ext) if ext in ("jpg", "jpeg", "png", "webp", "svg") else "jpg"
        data = urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=30).read()
        open(os.path.join(IMG, f"{nid}.{ext}"), "wb").write(data)
        time.sleep(0.15)
        return f"img/{nid}.{ext}"
    except Exception as e:
        print("  image failed:", nid, wiki, e)
        return None


credits = []
for n in nodes:
    n["img"] = fetch_image(n["id"], n["wiki"]) if n.get("wiki") else None
    if n["img"]:
        credits.append(dict(title=n["title"], page="https://en.wikipedia.org/wiki/" + urllib.parse.quote(n["wiki"].replace(" ", "_"))))
    n.pop("wiki", None)

out = dict(
    generated="2026-11-13",
    bachimg=next((f"img/joscha_bach.{e}" for e in ("jpg", "png", "webp") if os.path.exists(os.path.join(IMG, f"joscha_bach.{e}"))), None),
    nodes=nodes,
    cimc=dict(
        founded=cimc["founded"], programme=cimc["programme_tldr"],
        people=[dict(name=p["name"], role=p["role"]) for p in cimc["people"]],
        outputs=sorted(cimc["outputs"], key=lambda o: o["date"]),
    ),
    works=sorted(W["bach_works"], key=lambda w: str(w["year"])),
    bio=W["bio"],
    sources=sorted(all_sources, key=lambda s: s["date"]),
    credits=credits,
)
ids = {n["id"] for n in nodes}
bad = [e for e in E if e[0] not in ids or e[1] not in ids or e[2] not in ("builds", "against", "related")]
for e in bad:
    print("BAD EDGE", e)
dupes = len(E) - len({(e[0], e[1]) for e in E})
out["edges"] = [list(e) for e in E if e not in bad]
print(f"edges {len(out['edges'])}  bad {len(bad)}  duplicate pairs {dupes}")
json.dump(out, open(os.path.join(HERE, "data.json"), "w"), ensure_ascii=False, indent=1)

# ---- what the pages get: off-topic points removed; for everything except Bach's own ideas, his commentary
# and the transcript quotes are left out (they stay in data.json)
def slim(n):
    own = n.get("own", False)
    return dict(n, facets=[dict(label=f["label"], tldr=f["tldr"], author=f["author"], mentions=f["mentions"] if own else [])
                           for f in n["facets"]])
unknown = DROP - ids
if unknown:
    print("DROP has unknown ids:", sorted(unknown))
kept = [n for n in nodes if n["id"] not in DROP]

# On the pages Bach is one thinker among the others: his ideas fold into a single "Joscha Bach" point
# (one section per idea), and the institute's hypothesis is its own point. No separate lane.
CIMC_IDS = ["b_mch", "b_noturing"]
own = [n for n in kept if n["theme"] == "bach"]
def as_facet(n, author=None):
    f = n["facets"][0]
    return dict(label=n["title"] + " (" + n["label"] + ")", tldr=f["tldr"], author=author, mentions=f["mentions"])
bach_node = dict(
    id="bach", title="Joscha Bach", year=2017, label="2003–2026", theme="cons", img=out["bachimg"], own=True, verified=True, nsrc=0,
    facets=[dict(label="Joscha Bach", author=None, mentions=[], tldr=(
        "German cognitive scientist and AI researcher, born 1973. He treats the mind as software: the brain builds a "
        "simulated world with a simulated self in it, and consciousness is a property of that simulation, a process "
        "that makes the mind's many models cohere. He began with cognitive architectures (MicroPsi) and is executive director of the "
        "California Institute for Machine Consciousness."))]
          + [as_facet(n) for n in own if n["id"] not in CIMC_IDS])
cimc_node = dict(
    id="cimc", title="CIMC: the Machine Consciousness Hypothesis", year=2025, label="2025", theme="cons", img=None, own=True,
    verified=True, nsrc=0,
    facets=[as_facet(n, "Joscha Bach and Hikari Sorensen, California Institute for Machine Consciousness")
            for i in CIMC_IDS for n in own if n["id"] == i])
kept = sorted([n for n in kept if n["theme"] != "bach"] + [bach_node, cimc_node], key=lambda n: (n["year"], n["title"]))

fold = {n["id"]: ("cimc" if n["id"] in CIMC_IDS else "bach") for n in own}
merged = {}
for a, b_, kind, note in out["edges"]:
    a, b_ = fold.get(a, a), fold.get(b_, b_)
    if a == b_:
        continue
    if (a, b_) in merged:
        if note and note not in merged[(a, b_)][3]:
            merged[(a, b_)][3] += "; " + note
    else:
        merged[(a, b_)] = [a, b_, kind, note]
merged[("bach", "cimc")][3] = "the institute's hypothesis rests on his conductor model, his functionalism and the idea that consciousness comes first"

keep = [slim(n) for n in kept]

# second round (research/round2/): items below "highly likely" were sourced or rewritten by one model and
# re-checked by the other. summaries are replaced whole by key "id|part"; connections by key "from>to", null drops one
R2 = os.path.join(R, "round2")
SFIX = json.load(open(os.path.join(R2, "summary_fix.json"))) if os.path.exists(os.path.join(R2, "summary_fix.json")) else {}
EFIX = json.load(open(os.path.join(R2, "edge_fix.json"))) if os.path.exists(os.path.join(R2, "edge_fix.json")) else {}
for n in keep:
    for f in n["facets"]:
        k = n["id"] + "|" + (f["label"] or "")
        if k in SFIX: f["tldr"] = SFIX.pop(k)
for k in SFIX: print("summary_fix did not match:", k)
for k, v in EFIX.items():
    a, b_ = k.split(">")
    if (a, b_) not in merged: print("edge_fix did not match:", k); continue
    if v is None: del merged[(a, b_)]
    else: merged[(a, b_)][2], merged[(a, b_)][3] = v["kind"], v["note"]
for n, k in zip(kept, keep):
    h = None if n.get("own") else start_here.hear(n["id"], n["facets"])
    if h and h["at"] is not None: h["at"] = start_here.clock(h["at"])
    k["start"] = dict(read=start_here.read(n["id"], n["facets"][0]["label"]), hear=h)

# ---- confidence: each level follows from what the source check found (research/confidence/), not from a rating
CONF = json.load(open(os.path.join(HERE, "research", "confidence", "confidence.json")))
S_LEVEL = {"supported": "highly likely", "partly": "likely", "not_found": "possible", "contradicted": "possible"}
C_LEVEL = {"documented": "highly likely", "standard": "likely", "interpretive": "possible", "wrong": "possible"}
conf_count = {"s": {}, "c": {}}
for n in keep:
    for f in n["facets"]:
        c = CONF["summaries"].get(n["id"] + "|" + (f["label"] or ""))
        if not c: print("no confidence for summary:", n["id"], f["label"]); continue
        lvl = S_LEVEL[c["verdict"]]
        f["conf"] = [lvl, c["url"], c["note"] if lvl != "highly likely" else ""]
        conf_count["s"][lvl] = conf_count["s"].get(lvl, 0) + 1
def edge_conf(e):
    c = CONF["connections"].get(e[0] + ">" + e[1])
    if not c: print("no confidence for connection:", e[0], e[1]); return e
    lvl = C_LEVEL[c["verdict"]]
    if lvl == "highly likely" and c.get("caveat"): lvl = "likely"   # a source makes the link but qualifies the kind or the note
    conf_count["c"][lvl] = conf_count["c"].get(lvl, 0) + 1
    return e + [[lvl, c["url"], c["note"] if lvl != "highly likely" else ""]]
# schools of thought: two models sorted every card independently; research/schools/final.json holds the result
SCHOOLS = json.load(open(os.path.join(R, "schools", "schools.json")))
SFINAL = json.load(open(os.path.join(R, "schools", "final.json")))
for n in keep:
    s = SFINAL.get(n["id"])
    if not s: print("no school for", n["id"]); continue
    n["school"] = dict(id=s["school"], alt=s.get("alt"))
keep_ids = {n["id"] for n in keep}
titles = {n["title"] for n in keep}
pageout = dict(out, nodes=keep, edges=[edge_conf(e) for e in merged.values() if e[0] in keep_ids and e[1] in keep_ids],
               credits=[c for c in credits if c["title"] in titles],
               schools=[dict(id=s["id"], name=s["name"]) for s in SCHOOLS])
print(f"pages: {len(keep)} points ({len(nodes) - len(keep)} left off), {len(pageout['edges'])} connections")
if "--timeline" in sys.argv:  # shelved for now; the template is kept
    page = open(os.path.join(HERE, "timeline_template.html")).read().replace(
        "__DATA__", json.dumps(pageout, ensure_ascii=False).replace("</", "<\\/"))
    open(os.path.join(HERE, "timeline.html"), "w").write(page)
gpage = open(os.path.join(HERE, "board_template.html")).read().replace(
    "__DATA__", json.dumps(pageout, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(HERE, "index.html"), "w").write(gpage)
# about.html: how the map was made, the transcripts it started from, image credits
aboutdata = dict(points=len(keep), connections=len(pageout["edges"]), credits=pageout["credits"], conf=conf_count,
                 sources=[dict(title=s["title"], url=s.get("url"), date=s.get("date"), ok=s.get("ok")) for s in pageout["sources"]])
apage = open(os.path.join(HERE, "about_template.html")).read().replace(
    "__DATA__", json.dumps(aboutdata, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(HERE, "about.html"), "w").write(apage)

# map.md: the whole map as one markdown file, for reading or handing to a language model
SITE = "https://maxeozakh.github.io/bach-map/"
LANES = {"rel": "myth and religion", "phil": "philosophy", "math": "mathematics and logic", "sci": "physics and life",
         "mind": "psychology and mind", "cons": "consciousness", "ai": "computing and AI", "fic": "fiction",
         "soc": "society", "eth": "ethics and AI risk"}
VERB = {"builds": ("builds on", "leads to"), "against": ("argues against", "challenged by"), "related": ("related to", "related to")}
md_title = {n["id"]: n["title"] for n in keep}
md_year = {n["id"]: n["year"] for n in keep}
md_adj = defaultdict(list)
for e in pageout["edges"]:
    md_adj[e[0]].append((e, e[1], 1)); md_adj[e[1]].append((e, e[0], 0))
def md_conf(c):
    if not c: return ""
    lvl, url, why = c
    return f"confidence: {lvl}" + (f", [source]({url})" if url else "") + (f". {why}" if why else "")
md = [
    "# a map of consciousness",
    "",
    f"ideas about mind and consciousness that joscha bach has mentioned in public, from the earliest myths to november 2026. "
    f"a simplified, AI-drawn picture of the ideas, not the ideas themselves. unofficial: joscha bach didn't make or approve it. made with claude fable 5.2 and independently checked by gpt 5.6 sol "
    f"as of 13 november 2026; not checked by a person. interactive version: {SITE}. "
    f"how to read it and where it comes from: {SITE}about.html",
    "",
    f"{len(keep)} points, {len(pageout['edges'])} connections, in chronological order. each summary and connection carries a "
    "confidence word (highly likely, likely, possible) that follows from source checks by two models; the lower verdict is shown. "
    "summaries are general background, not joscha bach's words, except quotes marked as his.",
    "",
]
for n in keep:
    sname = {s["id"]: s["name"] for s in SCHOOLS}
    school = f" school of thought: {sname[n['school']['id']]}." if n.get("school") else ""
    md += [f"## {n['title']}", "", f"{n['label']}, {LANES.get(n['theme'], n['theme'])}.{school} id: `{n['id']}`", ""]
    for i, f in enumerate(n["facets"]):
        if i or (f["label"] and f["label"] != n["title"] and len(n["facets"]) > 1):
            md += [f"### {f['label']}", ""]
        if f.get("author"): md += [f"by {f['author']}", ""]
        md += [f["tldr"], ""]
        if f.get("conf"): md += [md_conf(f["conf"]), ""]
        if f["mentions"]:
            md += ["sources:", ""]
            for m in f["mentions"]:
                src = f"[{m['src']}]({m['url']})" if m["url"] else m["src"]
                md.append(f"- {'verbatim' if m['v'] else 'paraphrase'}, {src}{', ' + m['date'] if m['date'] else ''}: {m['q']}")
            md.append("")
        if i == 0 and n.get("start"):
            s = n["start"]
            if s["read"]: md += [f"start here, read: [{s['read']['name']}]({s['read']['url']})", ""]
            if s["hear"]:
                r = s["hear"]
                link = f"[{r['src']}]({r['url']})" + (f", from {r['at']}" if r["at"] else "")
                md += [f"start here, mentioned by joscha bach in: {link}" if r["weak"] else
                       f"start here, joscha bach on it: {link} ({'verbatim' if r['v'] else 'paraphrase'}): {r['q']}", ""]
        if i == 0 and md_adj[n["id"]]:
            md += ["connections:", ""]
            for e, other, outgoing in sorted(md_adj[n["id"]], key=lambda x: md_year[x[1]]):
                c = md_conf(e[4]) if len(e) > 4 else ""
                md.append(f"- {VERB[e[2]][outgoing]} {md_title[other]} (`{other}`)" + (f": {e[3]}" if e[3] else "") + (f". {c}" if c else ""))
            md.append("")
open(os.path.join(HERE, "map.md"), "w").write("\n".join(md).rstrip() + "\n")
open(os.path.join(HERE, "llms.txt"), "w").write(
    "# a map of consciousness\n\n"
    "> unofficial map of ideas about mind and consciousness that joscha bach has mentioned in public. AI-made and model-checked, "
    "not checked by a person; joscha bach didn't make or approve it.\n\n"
    f"- [the whole map as markdown]({SITE}map.md): every point, summary, confidence level, connection and source\n"
    f"- [how to read it and where it comes from]({SITE}about.html)\n"
    f"- [interactive map]({SITE})\n")

nf = sum(len(n["facets"]) for n in nodes)
nm = sum(len(f["mentions"]) for n in nodes for f in n["facets"])
print(f"nodes {len(nodes)}  facets {nf}  mentions {nm}  images {sum(1 for n in nodes if n['img'])}")
print(f"sources {len(all_sources)} ({sum(s['ok'] for s in all_sources)} retrieved)")
print("UNMATCHED", len(unmatched))
for u in unmatched:
    print("  ", u)
if "--assign" in sys.argv:
    for nid in buckets:
        for fl, es in buckets[nid].items():
            print(f"{nid:16} | {str(fl)[:40]:40} | " + " ;; ".join(r["name"] for _, r in es))
