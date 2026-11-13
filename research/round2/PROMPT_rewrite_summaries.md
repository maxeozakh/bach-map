You are improving short summaries on a public website, a map of ideas about mind and consciousness, so that each one is backed by a source. Do not edit any file except the one output file named below.

Input: a JSON list. Each item has `key`, `title`, `part` (the section of the card, may be null), `years`, `by`, `summary`, and `check_1` / `check_2`: two earlier source checks with a verdict, the URL they opened and a note saying which claim they could not confirm.

For EVERY item, do one of these, in order of preference:
1. "sourced": find and open a reliable page that states the unconfirmed claim (the original book or paper, an author's own page, a Joscha Bach essay or talk transcript, the Stanford or Internet Encyclopedia of Philosophy, Wikipedia, Britannica, a university or publisher page). Keep the summary unchanged.
2. "rewritten": change as little as possible so every claim is backed by a page you opened: drop or soften only the unconfirmed claim. Keep the summary specific and interesting; do not make it vague to make it safe. Keep the house style: plain English, short sentences, two or three sentences, no hype.
3. "kept": if neither is possible without gutting the summary, keep it unchanged.

Rules: actually open each page and read the relevant part; never invent a URL; `urls` lists the pages that together back the final summary. Do not judge style beyond the rules above.

Output: a JSON list, one object per input item, in input order: {"key": ..., "action": "sourced"|"rewritten"|"kept", "summary": <the final summary text>, "urls": [...], "why": <at most 25 words>}. Validate the JSON and the item count. Final message: counts per action.
