def R(name, kind, author, year, tldr, take, mentions, verified=True, note=None):
    d = {
        "name": name,
        "kind": kind,
        "author": author,
        "year": year,
        "tldr": tldr,
        "bach_take": take,
        "mentions": [
            {"source_id": s, "quote_or_paraphrase": q, "is_verbatim": v} for (s, q, v) in mentions
        ],
        "verified": verified,
    }
    if note:
        d["notes"] = note
    return d
