#!/usr/bin/env python3
"""Merge independent Claude and GPT source checks, keeping the weaker verdict."""
import json
from pathlib import Path

HERE = Path(__file__).parent
claude = json.load(open(HERE / "claude_confidence.json"))
gpt = json.load(open(HERE / "gpt_confidence.json"))

summary_rank = {"supported": 3, "partly": 2, "not_found": 1, "contradicted": 0}
connection_rank = {"documented": 3, "standard": 2, "interpretive": 1, "wrong": 0}


def weaker(a, b, rank):
    chosen = a if rank[a["verdict"]] <= rank[b["verdict"]] else b
    return dict(chosen)


merged = {
    "checked": "2026-11-13",
    "by": "claude fable 5.2 and gpt 5.6 sol",
    "method": "independent source checks; weaker verdict wins",
    "summaries": {
        key: weaker(claude["summaries"][key], gpt["summaries"][key], summary_rank)
        for key in claude["summaries"]
    },
    "connections": {
        key: weaker(claude["connections"][key], gpt["connections"][key], connection_rank)
        for key in claude["connections"]
    },
}

# The second check found these claims wrong. The underlying text or relationship
# was corrected after review; these verdicts describe the corrected versions.
summary_fixes = {
    "functionalism|Computationalism, weak and strong": ("supported", "https://doi.org/10.17721/2523-4064.2023/8-1/8", ""),
    "groupsel|": ("supported", "https://en.wikipedia.org/wiki/Group_selection", ""),
    "penrose|The Road to Reality": ("supported", "https://en.wikipedia.org/wiki/The_Road_to_Reality", ""),
    "iit|Integrated Information Theory": ("supported", "https://royalsocietypublishing.org/doi/full/10.1098/rstb.2014.0167", ""),
    "deeplearning|GANs as a model of dreaming": ("partly", "https://arxiv.org/abs/1406.2661", "The original paper supports the method and date; the later photorealistic-image claim is not covered there."),
}
for key, (verdict, url, note) in summary_fixes.items():
    merged["summaries"][key] = {"verdict": verdict, "url": url, "note": note}

connection_fixes = {
    "pythagoras>plato": ("interpretive", "https://plato.stanford.edu/entries/pythagoreanism/", "Pythagorean influence on Plato is disputed."),
    "wundt>skinner": ("standard", "", "The broad behaviorist turn fits, but Skinner retained private events and self-observation."),
    "goedel>turing": ("documented", "https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/tp2-ie.pdf", ""),
    "vonneumann>singularity": ("documented", "https://doi.org/10.1090/s0002-9904-1958-10189-5", ""),
    "friston>fields": ("documented", "https://arxiv.org/abs/2112.15242", ""),
    "hot>bach": ("documented", "https://cimc.ai/cimcHypothesis.pdf", ""),
    "piaget>bach": ("documented", "https://joscha.substack.com/p/levels-of-lucidity", ""),
}
for key, (verdict, url, note) in connection_fixes.items():
    merged["connections"][key] = {"verdict": verdict, "url": url, "note": note}

json.dump(merged, open(HERE / "confidence.json", "w"), ensure_ascii=False, indent=1)
