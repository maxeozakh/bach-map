You are sorting the cards of a public map of ideas about mind and consciousness into schools of thought, so readers can see families of ideas side by side. Do not edit any file except the one output file named below.

Inputs: research/schools/schools.json is the fixed list of schools (id, name, covers). research/schools/in.json is the list of cards (id, title, years, by, summary, parts). Paths are relative to /Users/maksim.zakharov/mm/bach-map/.

For EVERY card choose the ONE school it belongs to best, as a reader of the history of ideas would expect: by what the card is mainly about, not by a passing theme. A thinker goes where their main contribution sits. Use only ids from schools.json. Use "bach" only for the cards with ids bach and cimc. If two schools fit almost equally, give the better one in `school` and the other in `alt`; otherwise `alt` is null. Work alone: do not look at other output files in research/schools/.

Output: a JSON list, one object per card in input order: {"id": ..., "school": ..., "alt": ... or null}. Validate it is valid JSON with the same number of items as the input and only known school ids. Final message: counts per school.
