RAW = "/Users/maksim.zakharov/mm/notes/bach-map/research/raw/"
sources = []


def S(id, title, date, url, retrieved=True, raw=None, note=None):
    d = {"id": id, "title": title, "date": date, "url": url, "retrieved": retrieved,
         "raw_file": (RAW + raw) if raw else None}
    if note:
        d["note"] = note
    sources.append(d)


SUB = "wc_substack_cimcai_"
# ---- Bach's own writing
S("psi_diss_2007", "Principles of Synthetic Intelligence: Building Blocks for an Architecture of Motivated Cognition (PhD dissertation draft, Universität Osnabrück)", "2007-03-30",
  "http://cognitive-ai.com/publications/assets/Draft-MicroPsi-JBach-07-03-30.pdf", True, "wc_bach_psi_draft_2007.flat.txt",
  "Public draft of the dissertation that became the OUP 2009 book. Its 592-entry bibliography (parsed into wc_bach_psi_draft_2007_reference_entries.txt) is used as a stand-in for the book's bibliography, which was not retrieved.")
S("psi_book_2009", "Principles of Synthetic Intelligence. PSI: An Architecture of Motivated Cognition (Oxford University Press)", "2009",
  "https://doi.org/10.1093/acprof:oso/9780195370676.001.0001", False, "wc_openalex_bach_works.json",
  "Book text NOT retrieved. Only metadata (book DOI and ten chapter DOIs/titles) seen through the OpenAlex API.")
S("seven_2008", "Seven Principles of Synthetic Intelligence (Proc. 1st Conference on Artificial General Intelligence, Memphis, pp. 63-74)", "2008",
  "http://icontology.com/publications/assets/AGI%20Bach.pdf", True, "wc_bach_seven_principles_2008.flat.txt")
S("recon_2015", "Request confirmation networks for neuro-symbolic script execution (Bach & Herger, CoCo workshop at NIPS 2015)", "2015",
  "https://ceur-ws.org/Vol-1583/CoCoNIPS_2015_paper_6.pdf", True, "wc_bach_recon_2015.flat.txt")
S("ctc_2018", "The Cortical Conductor Theory: Towards Addressing Consciousness in AI Models (BICA 2018)", "2018",
  "http://bach.ai/pub/Bach%20-%20Cortical%20Conductor%20Theory%20(BICA%202018).pdf", True, "wc_bach_cortical_conductor_2018.flat.txt")
S("abl_2018", "Attention Based Learning as a Foundation for Conscious Agents (position paper, Harvard PED affiliation)", "2018",
  None, True, "wc_bach_attention_based_learning.txt",
  "PDF text was retrieved and read, but the exact URL it was downloaded from was not recorded, so url is null. The year/venue (BICA 2018 post-proceedings, Procedia Computer Science) is taken from Bach's 2023 CV, not from the PDF itself.")
S("phen_2019", "Phenomenal Experience and the Perceptual Binding State (AAAI Spring Symposium workshop TOCAIS 2019, CEUR Vol-2287)", "2019",
  "https://ceur-ws.org/Vol-2287/paper29.pdf", True, "wc_bach_phenomenal_experience_2019.flat.txt")
S("edge_2015", "The Age Of The New Machines, Or Every Society Will Get The Artificial Intelligence It Deserves (Edge Question 2015)", "2015",
  "https://www.edge.org/response-detail/26205", True, "wc_edge_2015_age_of_new_machines.txt")
S("edge_2016", "Everything Is Computation (Edge Question 2016)", "2016",
  "https://www.edge.org/response-detail/26733", True, "wc_edge_2016_everything_is_computation.txt")
S("bachai_ethics_2016", "From elementary computation to ethics? (bach.ai blog)", "2016-09-23",
  "http://bach.ai/from-computation-to-ethics/", True, "wc_bach_ai_feed_posts.txt")
S("bachai_sim_2016", "Do we live in a simulation or in the base reality? (bach.ai blog)", "2016-06-05",
  "http://bach.ai/Do-we-live-in-a-simulation/", True, "wc_bach_ai_feed_posts.txt")
S("bachai_minsky_2016", "On Marvin Minsky (bach.ai blog)", "2016-01-26",
  "http://bach.ai/on-marvin-minsky/", True, "wc_bach_ai_feed_posts.txt")
S("bachai_fourgods_2015", "Four Gods (bach.ai blog)", "2015-12-11",
  "http://bach.ai/four-gods/", True, "wc_bach_ai_feed_posts.txt")
S("bachai_pubs", "bach.ai publications page (list 2002-2012)", "2012",
  "http://bach.ai/publications/", True, "wc_bach_ai_publications.txt", "Date is the year of the latest entry on the page, not a page date.")
S("sub_lucidity_2023", "Levels of Lucidity (Joscha Bach, Substack)", "2023-05-21",
  "https://joscha.substack.com/p/levels-of-lucidity", True, "wc_substack_joscha_levels-of-lucidity.txt")
S("sub_xrisk_2023", "The Existential Risk of AGI: Reflections after the MLST Podcast with Connor Leahy (Joscha Bach, Substack)", "2023-06-22",
  "https://joscha.substack.com/p/the-existential-risk-of-agi", True, "wc_substack_joscha_the-existential-risk-of-agi.txt")
S("sub_age_2026", "The age of AGE: Artificial General Experience (Joscha Bach, Substack; text written for Rana Gujral's book 'The AI Instinct')", "2026-03-27",
  "https://joscha.substack.com/p/the-age-of-age", True, "wc_substack_joscha_the-age-of-age.txt")
S("cv_2023", "Joscha Bach, Curriculum Vitae, July 14, 2023", "2023-07-14",
  "http://bach.ai/pub/CV%20Joscha%20Bach.pdf", True, "wc_bach_cv_2023.txt")
S("openalex", "OpenAlex works list for author Joscha Bach (A5042931763)", "2026-11-13",
  "https://api.openalex.org/works?filter=author.id:A5042931763", True, "wc_openalex_bach_works.json", "Date is the retrieval date. Aggregator metadata; contains some mis-attributed items.")
S("arxiv", "arXiv API author query for Joscha Bach (3 items)", "2026-11-13",
  "https://export.arxiv.org/api/query?search_query=au:%22Joscha+Bach%22", True, "wc_arxiv_bach.xml",
  "Date is the retrieval date. The query URL here is a reconstruction of the author query; the saved XML is the evidence.")
S("gabora_bach_2023", "A Path to Generative Artificial Selves (Gabora & Bach, EPIA 2023, LNCS; OSF/PsyArXiv preprint text)", "2023",
  "https://doi.org/10.31234/osf.io/y3tzs", True, "wc_gabora_bach_2023_osf_websearch.txt", "Text obtained through the WebSearch tool's page capture.")
# ---- CIMC
S("cimc_site", "cimc.ai website (mission, research, grants text extracted from the JS bundle)", "2026-11-13",
  "https://cimc.ai/", True, "wc_cimc_main_strings.txt", "Date is the retrieval date. The site is a single-page app; text was extracted from its JavaScript bundle.")
S("cimc_team", "cimc.ai team page", "2026-11-13", "https://cimc.ai/team", True, "wc_cimc_main_strings.txt", "Date is the retrieval date.")
S("cimc_library", "cimc.ai library (reading list)", "2026-11-13", "https://cimc.ai/library", True, "wc_cimc_db_links.json", "Date is the retrieval date. Read from the site's public data backend.")
S("cimc_events", "cimc.ai events and news listings", "2026-11-13", "https://cimc.ai/events", True, "wc_cimc_db_events.json", "Date is the retrieval date. Read from the site's public data backend (events, news, projects tables).")
S("cimc_projects", "cimc.ai research projects / grantees listing", "2026-11-13", "https://cimc.ai/research", True, "wc_cimc_db_projects.json", "Date is the retrieval date. Page path is my best match for where the projects table is shown.")
S("cimc_pubs", "cimc.ai publications index", "2026-11-13", "https://cimc.ai/publications/", True, "wc_cimc_publications.txt", "Date is the retrieval date.")
S("mch_2025", "The Machine Consciousness Hypothesis (Joscha Bach & Hikari Sorensen, CIMC essay)", "2025-09-15",
  "https://cimc.ai/cimcHypothesis.pdf", True, "wc_cimc_hypothesis_pdf.txt",
  "Dated September 15, 2025 on the CIMC publications page; announced publicly on Substack 2026-01-16; page says last updated January 15, 2026.")
S("wp_2026", "The California Institute for Machine Consciousness Research Program Whitepaper (Sorensen, Hildebrandt-Harangozó, de Kerhuelvez, Rutt, Bach)", "2026-04-27",
  "https://cimc.ai/publications/research-program-whitepaper/", True, "wc_cimc_whitepaper.txt",
  "Three dates seen: first announced 2026-01-30 (Substack); text says this version was published April 27, 2026; publications index shows September 28, 2026.")
S("prime_2026", "Prime Hypostasis: A Short Reflection on the Idea that Provability + Hypostasis = Classical Semantics (Hildebrandt-Harangozó & Sorensen)", "2026-10-05",
  "https://cimc.ai/publications/prime-hypostasis/", True, "wc_cimc_pub_prime_hypostasis.txt")
S("against_2026", "Against intrinsic properties (Sorensen & Hildebrandt-Harangozó)", "2026-10-07",
  "https://cimc.ai/publications/against-intrinsic-properties/", True, "wc_cimc_pub_against_intrinsic.txt")
S("cs_launch_2025", "The Beginning of the California Institute for Machine Consciousness (CIMC Substack)", "2025-06-24",
  "https://cimcai.substack.com/p/the-beginning-of-the-california-institute", True, SUB + "the-beginning-of-the-california-institute.txt")
S("cs_chatbot_2025", "Did Your Chatbot Just Wake Up? A friendly reality-check from CIMC (CIMC Substack)", "2025-10-07",
  "https://cimcai.substack.com/p/did-your-chatbot-just-wake-up", True, SUB + "did-your-chatbot-just-wake-up.txt")
S("cs_2026_wishes", "Best Wishes for 2026: A Year of Research, Collaboration, and Shared Progress (CIMC Substack)", "2026-01-10",
  "https://cimcai.substack.com/p/best-wishes-for-2026-a-year-of-research", True, SUB + "best-wishes-for-2026-a-year-of-research.txt")
S("cs_mch_2026", "Essay: The Machine Consciousness Hypothesis (CIMC Substack announcement)", "2026-01-16",
  "https://cimcai.substack.com/p/essay-the-machine-consciousness-hypothesis", True, SUB + "essay-the-machine-consciousness-hypothesis.txt")
S("cs_wp_2026", "Foundational White Paper (CIMC Substack announcement)", "2026-01-30",
  "https://cimcai.substack.com/p/foundational-white-paper", True, SUB + "foundational-white-paper.txt")
S("cs_mc0001_2026", "MC0001: The Founding Assembly for Machine Consciousness Research (CIMC Substack)", "2026-02-24",
  "https://cimcai.substack.com/p/mc0001-the-founding-assembly-for", True, SUB + "mc0001-the-founding-assembly-for.txt")
S("cs_aaai_2026", "AAAI 2026 Spring Symposium - Machine Consciousness: Integrating Theory, Technology, and Philosophy (CIMC Substack)", "2026-03-16",
  "https://cimcai.substack.com/p/aaai-2026-spring-symposium-machine", True, SUB + "aaai-2026-spring-symposium-machine.txt")
S("cs_mc0001_talks_2026", "Discover the full talks and experiences program at MC0001 (CIMC Substack)", "2026-05-22",
  "https://cimcai.substack.com/p/discover-the-full-talks-and-experiences", True, SUB + "discover-the-full-talks-and-experiences.txt")
S("cs_apart_2026", "Apart Research: The Digital Minds Research Sprint (CIMC Substack)", "2026-07-28",
  "https://cimcai.substack.com/p/apart-research-the-digital-minds", True, SUB + "apart-research-the-digital-minds.txt")
S("cs_aaai_video_2026", "AAAI 2026 Machine Consciousness Symposium: Watch the Video Recordings (CIMC Substack)", "2026-08-19",
  "https://cimcai.substack.com/p/aaai-2026-machine-consciousness-symposium", True, SUB + "aaai-2026-machine-consciousness-symposium.txt")
S("cs_residency_2026", "Apply Now: AI x Consciousness Research Residency in India (CIMC Substack)", "2026-09-15",
  "https://cimcai.substack.com/p/apply-now-ai-x-consciousness-research", True, SUB + "apply-now-ai-x-consciousness-research.txt")
S("cs_berlin_2026", "CIMC | Berlin Recap, Hackathons & Upcoming Events (CIMC Substack)", "2026-09-25",
  "https://cimcai.substack.com/p/cimc-berlin-recap-hackathons-and", True, SUB + "cimc-berlin-recap-hackathons-and.txt")
S("cs_nl02_2026", "CIMC Research Update | Lattice Animals, New Researchers & Vision Weekend (CIMC Substack)", "2026-10-28",
  "https://cimcai.substack.com/p/cimc-newsletter-02", True, SUB + "cimc-newsletter-02.txt")
S("mc0001_site", "MC0001 conference website: The Founding Assembly for Machine Consciousness Research", "2026",
  "https://machine-consciousness.ai", True, "wc_mc0001_home.txt")
S("propublica", "ProPublica Nonprofit Explorer: California Institute Of Machine Consciousness (EIN 99-3858960)", "2026-11-13",
  "https://projects.propublica.org/nonprofits/organizations/993858960", True, "wc_propublica_cimc.txt", "Date is the retrieval date.")
S("aaai_sss26", "AAAI 2026 Spring Symposium Series page", "2026",
  "https://aaai.org/conference/spring-symposia/sss26/", True, "wc_aaai_sss26_page_websearch.txt", "Text obtained through the WebSearch tool's page capture.")
S("linkedin_snip", "Joscha Bach LinkedIn profile (search-engine capture, not fetched directly)", "2026-11-13",
  "https://www.linkedin.com/in/joschabach", False, "wc_linkedin_joschabach_websearch.txt",
  "LinkedIn itself was not fetched; this is a WebSearch capture of the profile. Treated as secondary. The profile URL is the standard one and was not opened by me.")
S("wikipedia", "Joscha Bach (English Wikipedia)", "2026-11-13", "https://en.wikipedia.org/wiki/Joscha_Bach", True, "wc_wikipedia_bach.txt", "Date is the retrieval date. Tertiary source.")
# ---- transcripts collected by the other researchers, used here only for quotes
S("lex101", "Lex Fridman Podcast #101: Joscha Bach, Artificial Consciousness and the Nature of Reality (transcript)", "2020",
  "https://podscripts.co/podcasts/lex-fridman-podcast/101-joscha-bach-artificial-consciousness-and-the-nature-of-reality", True, "lex101_podscripts.txt", "Machine transcript.")
S("lex212", "Lex Fridman Podcast #212: Joscha Bach, Nature of Reality, Dreams, and Consciousness (transcript)", "2021",
  "https://podscripts.co/podcasts/lex-fridman-podcast/212-joscha-bach-nature-of-reality-dreams-and-consciousness", True, "lex212_podscripts.txt", "Machine transcript with errors.")
S("lex392", "Lex Fridman Podcast #392: Joscha Bach, Life, Intelligence, Consciousness, AI & the Future of Humans (transcript)", "2023",
  "https://lexfridman.com/joscha-bach-3-transcript/", True, "lex392.txt")
S("rutt87", "The Jim Rutt Show EP87: Joscha Bach on Theories of Consciousness (transcript)", "2020-10-26",
  "https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-episode-87-joscha-bach-on-theories-of-consciousness/", True, "rutt_ep87.txt",
  "Rough transcript; the show asks to check before quoting.")
S("c37_2023", "37C3 talk 'Synthetic Sentience' (machine subtitles)", "2023",
  "https://c3subtitles.de/talk/2838", True, "ccc_37c3_synthetic_sentience.en_DRAFT.txt", "Machine-generated subtitles; URL is the subtitle page named inside the file. Talk was given at 37C3, December 2023.")
S("mlst_2024", "Machine Learning Street Talk interview with Joscha Bach at AGI-24 (YouTube transcript)", "2024",
  "https://www.youtube.com/watch?v=3MkJEGE9GRY", True, "debates_mlst_2024_thoughts_3MkJEGE9GRY.txt", "Machine transcript.")
S("levin_2024", "Joscha Bach lecture on cyber animism (YouTube transcript, video id YZl4zom3q2g)", "2024",
  "https://www.youtube.com/watch?v=YZl4zom3q2g", True, "lecture_2024_cyber_animism_levin_center.youtube_transcript.txt",
  "Machine transcript collected by another researcher; the URL is built from the video id in the file; the 2024 date comes from the file name and was not checked by me.")
S("agi25", "AGI-25 talk 'The Operation of Consciousness' (YouTube transcript)", "2025",
  "https://youtu.be/xDzAclUq3U4", True, "lecture_2025_agi25_operation_of_consciousness.youtube_transcript.txt", "Machine transcript; URL as listed in CIMC's events data.")
