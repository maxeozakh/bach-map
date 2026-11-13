"""Build the check inputs for round two from the rewriters' outputs: python3 mkverify.py c1 (or s1, s2, c2)."""
import json, sys
from pathlib import Path

H = Path(__file__).parent
b = sys.argv[1]
src = {x["key"]: x for x in json.load(open(H / f"in_{b}.json"))}
out = json.load(open(H / f"out_{b}.json"))
items = []
for o in out:
    i = src[o["key"]]
    if b[0] == "c":
        if o["action"] == "dropped": continue
        a, z = o["key"].split(">")
        items.append(dict(**{"from": a, "to": z}, from_title=i["from_title"], to_title=i["to_title"],
                          kind=o["kind"], note=o["note"], suggested_urls=o["urls"]))
    else:
        nid, facet = o["key"].split("|", 1)
        items.append(dict(id=nid, facet=facet, **{k: i[k] for k in i if k in ("title", "years", "by")},
                          summary=o["summary"], suggested_urls=o["urls"]))
json.dump(items, open(H / f"ver_in_{b}.json", "w"), ensure_ascii=False, indent=1)
print(b, len(items))
