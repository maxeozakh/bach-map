You are improving the connections on a public website, a map of ideas about mind and consciousness through history, so that each one is backed by a source. Do not edit any file except the one output file named below.

Input: a JSON list. Each item has `key` ("from>to"), `from_title`, `to_title`, `kind`, `note` and `check_1` / `check_2`: two earlier source checks with a verdict, a URL and a note. Meaning of `kind`: "builds" = the `to` point builds on the `from` point; "against" = the `to` point argues against the `from` point; "related" = the two are related, no direction claimed. The `note` says in a few words what the link is. For links to "Joscha Bach" or "CIMC", his own talks, essays and papers are the best sources: look for him naming the other idea or thinker.

For EVERY item, do one of these, in order of preference:
1. "sourced": find and open a page that explicitly states this link as described (who drew on, extended, replied to or criticised whom, or that discusses the two together as the note says). Keep kind and note.
2. "changed": a page you opened supports a weaker or different link: change `kind` (often "builds" to "related") and/or rewrite `note` (a few words, lower case, like the others) so it says exactly what the page supports.
3. "dropped": the link is only a thematic parallel that no source draws; remove it.
4. "kept": you are unsure; keep it unchanged.

Rules: actually open each page and read the relevant part; never invent a URL. Be strict: a page about only one of the two points does not support a link.

Output: a JSON list, one object per input item, in input order: {"key": ..., "action": "sourced"|"changed"|"dropped"|"kept", "kind": <final kind>, "note": <final note>, "urls": [...], "why": <at most 25 words>}. Validate the JSON and the item count. Final message: counts per action.
