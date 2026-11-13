import json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from b_sources import sources, RAW
from b_refs import references
from b_ideas import bach_ideas
from b_works import bach_works
from b_cimc import cimc, bio

SRC = {s["id"]: s for s in sources}
_cache = {}


def norm(t):
    t = t.replace("ﬁ", "fi").replace("ﬂ", "fl")
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("\u00a0", " ")]:
        t = t.replace(a, b)
    t = re.sub(r"-\n", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def text_of(sid):
    if sid not in _cache:
        p = SRC[sid]["raw_file"]
        _cache[sid] = norm(open(p, errors="ignore").read()) if p and os.path.exists(p) else ""
    return _cache[sid]


fails = []


def check(sid, quote, where):
    if sid not in SRC:
        fails.append(("UNKNOWN SOURCE", sid, where)); return
    if len(quote.split()) >= 30:
        fails.append(("TOO LONG", sid, where, len(quote.split())))
    nq = norm(quote)
    if nq not in text_of(sid):
        # tolerate PDF-extraction stray spaces: compare with all spaces removed
        if nq.replace(" ", "") not in text_of(sid).replace(" ", ""):
            fails.append(("NOT FOUND", sid, where, quote))


for r in references:
    for m in r["mentions"]:
        if m["source_id"] not in SRC:
            fails.append(("UNKNOWN SOURCE", m["source_id"], r["name"]))
        elif m["is_verbatim"]:
            check(m["source_id"], m["quote_or_paraphrase"], r["name"])
        if not m["is_verbatim"] and len(m["quote_or_paraphrase"].split()) > 60:
            fails.append(("LONG PARAPHRASE", m["source_id"], r["name"]))
for i in bach_ideas:
    for s in i["sources"]:
        if s["is_verbatim"]:
            check(s["source_id"], s["quote_or_paraphrase"], i["name"])
for e in cimc["founded_evidence"] + cimc["programme_quotes"]:
    if e["is_verbatim"]:
        check(e["source_id"], e["quote_or_paraphrase"], "cimc")
for s in sources:
    if s["raw_file"] and not os.path.exists(s["raw_file"]):
        fails.append(("MISSING RAW", s["id"], s["raw_file"]))
    if not re.fullmatch(r"\d{4}(-\d\d-\d\d)?", s["date"]):
        fails.append(("BAD DATE", s["id"], s["date"]))

for f in fails:
    print("FAIL", f)

out = {
    "meta": {
        "generated": "2026-11-13",
        "scope": "Researcher slice: Joscha Bach's own written work and its cited sources (Part A); CIMC, Bach's named ideas, and bio (Part B).",
        "how_to_read_verified": "verified=true means the item (the citation, the statement, the role, the listing) was seen in a source that was actually retrieved and saved. It does not mean every sentence of a tldr was checked: tldr text describing what an outside book or theory says is general background written from memory. Each mention carries is_verbatim; verbatim quotes were machine-checked against the saved raw files.",
        "raw_dir": RAW,
    },
    "sources": sources,
    "references": references,
    "bach_ideas": bach_ideas,
    "bach_works": bach_works,
    "cimc": cimc,
    "bio": bio,
}
if "--write" in sys.argv:
    p = "/Users/maksim.zakharov/mm/notes/bach-map/research/writing_cimc.json"
    json.dump(out, open(p, "w"), ensure_ascii=False, indent=2)
    print("wrote", p)
print(len(sources), len(references), len(bach_ideas), len(bach_works), len(cimc["people"]), len(cimc["outputs"]), len(bio), "fails:", len(fails))
