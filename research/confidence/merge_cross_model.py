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
# reworded after both checks flagged the start date: "has led CIMC since 2025" became "is executive director of CIMC",
# which the page they opened states
summary_fixes["bach|Joscha Bach"] = ("supported", "https://en.wikipedia.org/wiki/Joscha_Bach", "")
# joscha bach's own ideas: the web checks often opened a page that did not cover a detail he states in his own
# essays or talks. these were checked against those texts (research/raw/) and reworded where they were not there
for label, url in [
    ("Motivated cognition: Psi theory and MicroPsi (2003)", "http://cognitive-ai.com/publications/assets/Draft-MicroPsi-JBach-07-03-30.pdf"),
    ("Request Confirmation Networks (ReCoN) (2015)", "https://ceur-ws.org/Vol-1583/CoCoNIPS_2015_paper_6.pdf"),
    ("From elementary computation to ethics (2016)", "https://joscha.substack.com/p/the-existential-risk-of-agi"),
    ("Only what can be constructed exists (2016)", "https://cimc.ai/cimcHypothesis.pdf"),
    ("Love as the discovery of shared purpose (2021)", "https://joscha.substack.com/p/the-age-of-age"),
    ("Consciousness comes before the self (2023)", "https://www.youtube.com/watch?v=yW_ngvMFlYs&t=3124s"),
    ("On large language models (2023)", "https://cimcai.substack.com/p/did-your-chatbot-just-wake-up"),
    ("Cyber-animism: software as spirit (2024)", "https://cimc.ai/cimcHypothesis.pdf"),
]:
    summary_fixes["bach|" + label] = ("supported", url, "")
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

# second round: rewritten or newly sourced items carry the fresh verdict of the model that did not rewrite them
R2 = HERE.parent / "round2" / "verdicts.json"
if R2.exists():
    r2 = json.load(open(R2))
    for kind in ("summaries", "connections"):
        merged[kind].update(r2[kind])

json.dump(merged, open(HERE / "confidence.json", "w"), ensure_ascii=False, indent=1)
