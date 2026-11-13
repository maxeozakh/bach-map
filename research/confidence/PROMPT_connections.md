You are checking connections on a public website (a map of ideas about mind and consciousness through history) against sources, so that each connection can carry an honest confidence label. Do not edit any file except the one output file named below.

Input: the JSON file given below. It is a list of connections; each has `from`, `to` (point ids), `from_title`, `to_title`, `kind` and `note`. Meaning of `kind`: "builds" = the `to` point builds on the `from` point; "against" = the `to` point argues against the `from` point; "related" = the two are related, no direction claimed. The `note` says in a few words what the link is.

For EVERY connection, try to find a reliable source on the web that states this specific link (Stanford Encyclopedia of Philosophy, Internet Encyclopedia of Philosophy, Wikipedia, Britannica, the original paper, a university or publisher page). Actually open the page and read the relevant part; do not rely on a search-result snippet alone and never invent a URL. Then give one verdict:

- "documented": a source you opened explicitly states the link: that the later thinker or work drew on, extended, replied to or criticised the earlier one (for builds/against), or explicitly discusses the two together in the way the note says (for related). The note's claim must also be consistent with the source.
- "standard": you did not find a page stating it in so many words, but the link is a commonplace of the field's textbooks and histories, and nothing you read conflicts with it.
- "interpretive": the link is a reasonable reading or thematic parallel, but you found no source making it, or the influence is indirect, or the kind (builds / against) is a judgement call.
- "wrong": a source you opened shows the kind, the direction or the note is false. Explain in `note_out`.

Be strict: "documented" needs an opened page that makes the link itself, not just a page about one of the two points. When in doubt between two verdicts, choose the weaker one.

Rules: `url` must be the exact page you opened and is required for "documented" and "wrong", empty otherwise. `note_out` is at most 25 words, may be empty. Work through all connections; do not stop early or sample.

Output: write a JSON list to the output file named below, one object per input connection, in the same order, with exactly these keys: `from`, `to` (copy both unchanged), `verdict`, `url`, `note_out`. Make sure the file is valid JSON and has the same number of items as the input.

Your final message: the counts per verdict, and the full list of any "wrong" connections with the reason.
