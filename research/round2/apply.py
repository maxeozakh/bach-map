"""Turn round-two rewrites and checks into the files build.py and merge_cross_model.py read."""
import json
from pathlib import Path

H = Path(__file__).parent
load = lambda n: json.load(open(H / n))
late = load("late_fixes.json")
sfix, efix, ver = {}, {}, {"summaries": {}, "connections": {}}

for b in ("s1", "s2"):
    for o in load(f"out_{b}.json"):
        if o["action"] == "rewritten": sfix[o["key"]] = o["summary"]
    for v in load(f"ver_out_{b}.json"):
        ver["summaries"][v["id"] + "|" + v["facet"]] = {"verdict": v["verdict"], "url": v["url"], "note": v["note"]}
for b in ("c1", "c2"):
    for o in load(f"out_{b}.json"):
        if o["action"] == "dropped": efix[o["key"]] = None
        elif o["action"] == "changed": efix[o["key"]] = {"kind": o["kind"], "note": o["note"]}
    for v in load(f"ver_out_{b}.json"):
        ver["connections"][v["from"] + ">" + v["to"]] = {"verdict": v["verdict"], "url": v["url"], "note": v["note_out"]}

sfix.update(late["summaries"])
efix.update(late["connections"])
if (H / "ver_out_late.json").exists():
    for v in load("ver_out_late.json"):
        k = v.get("key") or (v["id"] + "|" + v["facet"] if "id" in v else v["from"] + ">" + v["to"])
        kind = "connections" if ">" in k else "summaries"
        ver[kind][k] = {"verdict": v["verdict"], "url": v["url"], "note": v.get("note", v.get("note_out", ""))}

json.dump(sfix, open(H / "summary_fix.json", "w"), ensure_ascii=False, indent=1)
json.dump(efix, open(H / "edge_fix.json", "w"), ensure_ascii=False, indent=1)
json.dump(ver, open(H / "verdicts.json", "w"), ensure_ascii=False, indent=1)
print(len(sfix), "summaries rewritten,", sum(v is None for v in efix.values()), "connections dropped,",
      sum(v is not None for v in efix.values()), "changed")
