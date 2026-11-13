"""'start here' for each card: one page to read, and one moment where Joscha Bach talks about it.

read: the most introductory of the pages the two source checks opened for the card's summary
      (encyclopedias first, then everything else).
hear: one of the card's transcript mentions, picked by a model for saying the most about the idea
      (research/start_picks.json; it chooses among real quotes and cannot write one). Where the quote is found in a
      timed transcript, the link jumps to the moment it is said. "weak" marks cards whose mentions are all in passing.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "research", "raw")
CONF = os.path.join(HERE, "research", "confidence")

READ_RANK = [  # (domain fragment, label)
    ("plato.stanford.edu", "Stanford Encyclopedia of Philosophy"),
    ("iep.utm.edu", "Internet Encyclopedia of Philosophy"),
    ("en.wikipedia.org", "Wikipedia"),
    ("britannica.com", "Britannica"),
]

# pages that no longer open (checked 13 november 2026)
DEAD = ["jimruttshow.blubrry.net", "cimc.ai/library"]

words = lambda s: re.findall(r"[a-z0-9]+", s.lower().replace("’", "'").replace("'", ""))


def hms(s):
    p = [int(x) for x in re.split(r"[:,.]", s)[:3]]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def stream_lines(path, rx):
    """[(word, seconds)] from a transcript with one timestamp per line."""
    out = []
    for line in open(path, encoding="utf-8", errors="ignore"):
        m = rx.match(line)
        if m:
            t = hms(m.group(1))
            out += [(w, t) for w in words(m.group(2))]
    return out


def stream_srt(path):
    out, t = [], None
    for line in open(path, encoding="utf-8", errors="ignore"):
        m = re.match(r"(\d\d:\d\d:\d\d),\d+ -->", line)
        if m: t = hms(m.group(1)); t = None if t > 6 * 3600 else t; continue   # some files end with a 99:59:59 credit cue
        if t is not None and line.strip() and not line.strip().isdigit():
            out += [(w, t) for w in words(line)]
    return out


def timed_sources():
    """url -> (word stream, url builder)"""
    src = {}
    for f in os.listdir(RAW):
        p = os.path.join(RAW, f)
        if f.startswith("debates_") and f.endswith(".txt"):
            head = open(p, encoding="utf-8", errors="ignore").readline()
            m = re.search(r"watch\?v=([\w-]{11})", head)
            if m:
                s = stream_lines(p, re.compile(r"\[(\d+:\d\d:\d\d)\]\s*(.*)"))
                if s: src["yt:" + m.group(1)] = s
        if f.startswith("ccc_") and f.endswith(".srt"):
            src["ccc:" + re.match(r"ccc_(\d\dc3)", f).group(1)] = stream_srt(p)
    return src


def key_for(url):
    m = re.search(r"(?:watch\?v=|youtu\.be/)([\w-]{11})", url)
    if m: return "yt:" + m.group(1)
    m = re.search(r"media\.ccc\.de/v/(\d\dc3)", url, re.I)
    if m: return "ccc:" + m.group(1).lower()
    return None


def link_at(url, t):
    if "ccc.de" in url: return f"{url.split('#')[0]}#t={t}"
    vid = re.search(r"(?:watch\?v=|youtu\.be/)([\w-]{11})", url).group(1)
    return f"https://www.youtube.com/watch?v={vid}&t={t}s"


def find(stream, quote, n=8):
    """seconds where the quote starts, trying each n-word window of the quote in turn"""
    q = words(re.sub(r"^\s*paraphrase:\s*", "", quote, flags=re.I))
    if len(q) < n: return None
    seq = [w for w, _ in stream]
    index = {}
    for i in range(len(seq) - n + 1):
        index.setdefault(tuple(seq[i:i + n]), i)
    for j in range(0, len(q) - n + 1):
        i = index.get(tuple(q[j:j + n]))
        if i is not None: return stream[i][1]
    return None


_streams = None


_picks = None


def candidates(facets):
    """the card's usable mentions, in the order the picking model saw them"""
    global _streams
    if _streams is None: _streams = timed_sources()
    out = []
    for f in facets:
        for m in f["mentions"]:
            if not m["url"] or any(d in m["url"] for d in DEAD): continue
            k = key_for(m["url"])
            t = find(_streams[k], m["q"]) if k in _streams and m["v"] else None
            out.append(dict(src=m["src"], url=link_at(m["url"], max(0, t - 2)) if t is not None else m["url"],
                            at=t, q=m["q"], v=m["v"]))
    return out[:12]


def hear(nid, facets):
    global _picks
    if _picks is None: _picks = json.load(open(os.path.join(HERE, "research", "start_picks.json")))
    c, p = candidates(facets), _picks.get(nid)
    if not c or not p: return None
    return dict(c[p["i"]], weak=p["weak"])


_checks = None


def read(nid, label):
    global _checks
    if _checks is None:
        _checks = [json.load(open(os.path.join(CONF, f))) for f in ("claude_confidence.json", "gpt_confidence.json")]
    urls = []
    for c in _checks:
        e = c["summaries"].get(nid + "|" + (label or ""))
        if e and e.get("url") and e["url"] not in urls: urls.append(e["url"])
    if not urls: return None
    def rank(u):
        for i, (d, _) in enumerate(READ_RANK):
            if d in u: return i
        return len(READ_RANK)
    u = min(urls, key=rank)
    r = rank(u)
    name = READ_RANK[r][1] if r < len(READ_RANK) else re.sub(r"^www\.", "", u.split("/")[2])
    return dict(url=u, name=name)


def clock(t):
    h, m, s = t // 3600, t // 60 % 60, t % 60
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"
