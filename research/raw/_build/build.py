import json, re, sys, os, glob, importlib
sys.path.insert(0, os.path.dirname(__file__))
RAW = "/Users/maksim.zakharov/mm/notes/bach-map/research/raw/"
OUT = "/Users/maksim.zakharov/mm/notes/bach-map/research/ccc.json"

S = [
 ("ccc30", "How to Build a Mind: Artificial Intelligence Reloaded (30C3)", "2013-12-29", "https://media.ccc.de/v/30C3_-_5526_-_en_-_saal_2_-_201312291600_-_how_to_build_a_mind_-_joscha", "ccc_30c3_how_to_build_a_mind.en.txt"),
 ("ccc31", "From Computation to Consciousness (31C3)", "2014-12-28", "https://media.ccc.de/v/31c3_-_6573_-_en_-_saal_2_-_201412281130_-_from_computation_to_consciousness_-_joscha", "ccc_31c3_from_computation_to_consciousness.en_DRAFT.txt"),
 ("ccc32", "Computational Meta-Psychology (32C3)", "2015-12-29", "https://media.ccc.de/v/32c3-7483-computational_meta-psychology", "ccc_32c3_computational_meta_psychology.en.txt"),
 ("ccc33", "Machine Dreams (33C3)", "2016-12-29", "https://media.ccc.de/v/33c3-8369-machine_dreams", "ccc_33c3_machine_dreams.en_DRAFT.txt"),
 ("ccc35", "The Ghost in the Machine (35C3)", "2018-12-28", "https://media.ccc.de/v/35c3-10030-the_ghost_in_the_machine", "ccc_35c3_ghost_in_the_machine.en.txt"),
 ("ccc37", "Synthetic Sentience (37C3)", "2023-12-28", "https://media.ccc.de/v/37c3-12167-synthetic_sentience", "ccc_37c3_synthetic_sentience.en_DRAFT.txt"),
 ("ccc38", "Self Models of Loving Grace (38C3)", "2024-12-28", "https://media.ccc.de/v/38c3-self-models-of-loving-grace", "ccc_38c3_self_models_of_loving_grace.biocomm_transcript.txt"),
 ("ds2017", "Machine Dreams (German-language lecture, Dresden / Datenspuren 2017)", "2017", "https://c3d2.de/media/20170930-TSD-When_Machines_Are_Dreaming-Joscha_Bach.transcript.html", "lecture_2017_datenspuren_machine_dreams.c3d2_transcript.txt"),
 ("cyber", "Cyber Animism (talk hosted by Michael Levin's center, Tufts)", "2024", "https://www.youtube.com/watch?v=YZl4zom3q2g", "lecture_2024_cyber_animism_levin_center.youtube_transcript.txt"),
 ("agi24", "AGI-24 keynote on cyber animism (Seattle; Machine Learning Street Talk recording)", "2024", "https://www.youtube.com/watch?v=34VOI_oo-qM", "lecture_2024_agi24_keynote_cyberanimism.youtube_transcript.txt"),
 ("agi25", "The Operation of Consciousness (AGI-25, Reykjavik)", "2025", "https://www.youtube.com/watch?v=oR-BQTSpL5U", "lecture_2025_agi25_operation_of_consciousness.youtube_transcript.txt"),
 ("tedx", "From Artificial Intelligence to Artificial Consciousness (TEDxBeaconStreet)", None, "https://www.youtube.com/watch?v=Jr7gY3JyzP8", None),
 ("ted2025", "If a machine became conscious, how would we know? (TED, TEDAI Vienna)", "2025", "https://www.ted.com/talks/joscha_bach_if_a_machine_became_conscious_how_would_we_know", None),
]
sources = [{"id": i, "title": t, "date": d, "url": u, "transcript_obtained": f is not None,
            "raw_file": (RAW + f) if f else None} for i, t, d, u, f in S]

def norm(s):
    s = s.lower().replace("’", "'").replace("“", '"').replace("”", '"').replace("…", "...")
    return re.sub(r"\s+", " ", s).strip()

texts = {i: norm(open(RAW + f).read()) for i, t, d, u, f in S if f}

refs = []
for p in sorted(glob.glob(os.path.dirname(__file__) + "/p*.py")):
    refs += importlib.import_module(os.path.basename(p)[:-3]).REFS

bad = 0
names = set()
for r in refs:
    if r["name"] in names: print("DUP", r["name"]); bad += 1
    names.add(r["name"])
    for m in r["mentions"]:
        if m["source_id"] not in texts: print("NOSRC", r["name"], m["source_id"]); bad += 1; continue
        if m["is_verbatim"] and norm(m["quote_or_paraphrase"]) not in texts[m["source_id"]]:
            print("MISS", r["name"], "|", m["source_id"], "|", m["quote_or_paraphrase"]); bad += 1
        if m["is_verbatim"] and len(m["quote_or_paraphrase"].split()) >= 30:
            print("LONG", r["name"], len(m["quote_or_paraphrase"].split()))

unresolved = importlib.import_module("unres").UNRESOLVED if os.path.exists(os.path.dirname(__file__) + "/unres.py") else []
json.dump({"sources": sources, "references": refs, "unresolved": unresolved}, open(OUT, "w"), ensure_ascii=False, indent=1)
v = sum(r["verified"] for r in refs)
print("refs", len(refs), "verified", v, "unverified", len(refs) - v, "problems", bad)
