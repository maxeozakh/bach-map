You are checking short summaries on a public website (a map of ideas about mind and consciousness) against sources, so that each summary can carry an honest confidence label. Do not edit any file except the one output file named below.

Input: the JSON file given below. It is a list of items; each has `id`, `facet`, `title`, `years`, `by` (credited author, may be null) and `summary`.

For EVERY item, look for a reliable source on the web that covers the main claims of the summary (Stanford Encyclopedia of Philosophy, Internet Encyclopedia of Philosophy, Wikipedia, Britannica, the original paper or book page, a university or publisher page). Actually open the page and read the relevant part; do not rely on a search-result snippet alone and never invent a URL. Then give one verdict:

- "supported": you opened a source and it backs the main claims of the summary (who, what, roughly when, and the idea as described). Small details the source does not mention are fine as long as nothing conflicts.
- "partly": you opened a source; it backs the core but at least one specific claim in the summary is not confirmed by it or is stated more strongly than the source does. Say which claim in `note`.
- "contradicted": a source you opened conflicts with something in the summary. Quote the wrong phrase and say what the source says in `note`.
- "not_found": you could not find and open a source that covers it in a reasonable effort (two or three searches). This is an acceptable honest answer.

Rules: `url` must be the exact page you opened and is required for every verdict except "not_found". `note` is at most 25 words, empty for a clean "supported". Do not judge style or omissions. Work through all items; do not stop early or sample.

Output: write a JSON list to the output file named below, one object per input item, in the same order, with exactly these keys: `id`, `facet` (copy both unchanged from the input), `verdict`, `url`, `note`. Make sure the file is valid JSON and has the same number of items as the input.

Your final message: the counts per verdict, and the full list of any "contradicted" items with the wrong phrase and the correction.
