TEAM = "https://cimc.ai/team"
WP = "https://cimc.ai/publications/research-program-whitepaper/"
PRO = "https://projects.propublica.org/nonprofits/organizations/993858960"
LAUNCH = "https://cimcai.substack.com/p/the-beginning-of-the-california-institute"
NL2 = "https://cimcai.substack.com/p/cimc-newsletter-02"
BERLIN = "https://cimcai.substack.com/p/cimc-berlin-recap-hackathons-and"
PROJ = "https://cimc.ai/research"


def P(name, role, url):
    return {"name": name, "role": role, "source_url": url}


people = [
    P("Joscha Bach", "Executive Director; Board Director (co-founder)", TEAM),
    P("Erik Newton", "President; Board Director (co-founder)", TEAM),
    P("Lou de Kerhuelvez (Lou de K)", "VP of Programs; Board Director", TEAM),
    P("Zhen Tan", "Secretary; Board Director", TEAM),
    P("Philip Rosedale", "Treasurer; Board Director; CTO", TEAM),
    P("Franz Hildebrandt-Harangozó", "Researcher (philosophy)", TEAM),
    P("Hikari Sorensen", "Researcher (computational philosophy); co-author of the Machine Consciousness Hypothesis essay", TEAM),
    P("Angie Normandale", "Research and Ecosystem Coordinator", TEAM),
    P("Emily Quiles", "Operations Manager", TEAM),
    P("Ivan Yakovenko", "Research engineer (called principal engineer in the October 2026 newsletter)", TEAM),
    P("Toni (Antonia) Antonova", "Research engineer", TEAM),
    P("Aishik Sanyal", "Research engineer", TEAM),
    P("Jane Rhee", "Assistant to the CTO (joined August 2026)", TEAM),
    P("Karl Friston", "Scientific Advisor (University College London)", TEAM),
    P("Christoph von der Malsburg", "Scientific Advisor (Frankfurt Institute for Advanced Studies)", TEAM),
    P("Stephen Wolfram", "Scientific Advisor (Wolfram Research)", TEAM),
    P("Kirill Eves", "Board Director; named 'Primary Donor' in the whitepaper appendix. ProPublica's filing extract spells the name 'Krill Eves'.", TEAM),
    P("Christine Peterson", "Board Observer", TEAM),
    P("Allison Duettmann", "Organizational Advisor (Foresight Institute)", TEAM),
    P("Dan Girshovich", "Organizational Advisor (Tools for Humanity)", TEAM),
    P("Era Qian", "Organizational Advisor (Edge)", TEAM),
    P("Adam Brown", "Organizational Advisor (The Institute)", TEAM),
    P("Trent McConaghy", "Organizational Advisor", TEAM),
    P("Jim Rutt", "Board Chairman Emeritus per the whitepaper appendix; listed as Chairman in the FY2024 tax filing extract; whitepaper co-author", WP),
    P("Michael Levin", "Informal supporter, not a formal advisor (whitepaper appendix says his institution does not allow formal advisor roles); speaker at the launch and at MC0001", WP),
    P("Chris Percy", "First CIMC Fellow (announced October 2026)", NL2),
    P("Aleksandr Groznykh", "Grantee: 'Self-Organizing Generative Perception' (neural cellular automata)", PROJ),
    P("Priska Herger and Jochen Kerdels", "Grantees: 'Coherent active state dynamics in self-organizing systems'. The site data spells the second name 'Joschen Kerdels'.", PROJ),
    P("Leander Rust", "Grantee: 'Motivational architecture for conscious control'", PROJ),
    P("Patricia Craja and Jan Saputra Müller", "Grantees (Amalie Technologies): 'From Personality to Perceptual Architectures'", PROJ),
    P("Zahra Sheikhbahaee and Adam Safron", "Grantees (Allen Discovery Center at Tufts; Mila): 'Dream to Explore', led by Sheikhbahaee, with Dalton Sakthivadivel, Alex Kiefer, Arthur Juliani and Leonardo Christov-Moore", PROJ),
    P("Roshni Lulla and Era Qian", "'Child LLM Project' (University of Southern California); marked hidden in the site data, so status unclear", PROJ),
    P("Linus Eickhoff", "'Building a self-organizing Mixture-of-Experts Architecture'; marked hidden in the site data, so status unclear", PROJ),
    P("Stephen Fitz and Wes Johnson", "'Emergent Agents in Minimal Computation'; marked hidden in the site data, so status unclear", PROJ),
]

outputs = []


def O(title, date, typ, authors, url, tldr, verified=True):
    outputs.append({"title": title, "date": date, "type": typ, "authors": authors, "url": url, "tldr": tldr, "verified": verified})


# ---- papers and essays
O("The Machine Consciousness Hypothesis", "2025-09-15", "essay / hypothesis document", ["Joscha Bach", "Hikari Sorensen"],
  "https://cimc.ai/publications/the-machine-consciousness-hypothesis/",
  "CIMC's founding essay. Dated September 15, 2025 on the publications page, announced on Substack on January 16, 2026, and marked as last updated January 15, 2026. States that general computers can implement consciousness and that this can be tested. PDF at https://cimc.ai/cimcHypothesis.pdf.")
O("Did Your Chatbot Just Wake Up? A friendly reality-check from CIMC", "2025-10-07", "essay (Substack)", ["CIMC (no individual byline)"],
  "https://cimcai.substack.com/p/did-your-chatbot-just-wake-up",
  "A public explainer written because people keep writing to CIMC about chatbots that seem to wake up. Explains how language models are trained, calls them shapeshifters and 'really good actors', and says that text about an experience is not the experience.")
O("The California Institute for Machine Consciousness Research Program Whitepaper", "2026-04-27", "whitepaper", ["Hikari Sorensen", "Franz Hildebrandt-Harangozó", "Lou de Kerhuelvez", "Jim Rutt", "Joscha Bach"], WP,
  "The research programme in full: operational definition of consciousness, three research directions, relation to other theories, ethics and risk, and an appendix on people. First announced on Substack on 2026-01-30; the text says this version was published April 27, 2026; the publications index shows September 28, 2026.")
O("Prime Hypostasis: A Short Reflection on the Idea that Provability + Hypostasis = Classical Semantics", "2026-10-05", "paper (philosophy note)", ["Franz Hildebrandt-Harangozó", "Hikari Sorensen"],
  "https://cimc.ai/publications/prime-hypostasis/",
  "A short Kant-based note on the foundations of mathematics. It suggests that classical truth is what you get when provability is treated as if it were a thing in itself. Also posted on PhilArchive according to the page. Bach is not an author.")
O("Against intrinsic properties", "2026-10-07", "essay (reply)", ["Hikari Sorensen", "Franz Hildebrandt-Harangozó"],
  "https://cimc.ai/publications/against-intrinsic-properties/",
  "A reply to Alexander Lerchner's 2026 paper 'The Abstraction Fallacy', defending computational functionalism about consciousness. Bach is not an author.")
# ---- newsletters
O("The Beginning of the California Institute for Machine Consciousness", "2025-06-24", "newsletter (Substack)", ["CIMC"], LAUNCH,
  "Report on the launch. Says CIMC officially launched on May 30, 2025 and describes the launch days in San Francisco.")
O("Best Wishes for 2026: A Year of Research, Collaboration, and Shared Progress", "2026-01-10", "newsletter (Substack)", ["CIMC"],
  "https://cimcai.substack.com/p/best-wishes-for-2026-a-year-of-research",
  "Year-end letter listing funded research projects and the planned AAAI collaboration.")
O("Essay: The Machine Consciousness Hypothesis", "2026-01-16", "newsletter (Substack)", ["CIMC"],
  "https://cimcai.substack.com/p/essay-the-machine-consciousness-hypothesis", "Announcement of the essay's public release.")
O("Foundational White Paper", "2026-01-30", "newsletter (Substack)", ["CIMC"],
  "https://cimcai.substack.com/p/foundational-white-paper", "Announcement of the research programme whitepaper.")
O("CIMC | Berlin Recap, Hackathons & Upcoming Events", "2026-09-25", "newsletter (Substack)", ["CIMC; researcher note by Hikari Sorensen"], BERLIN,
  "Recap of the Berlin conference and the August hackathon, with upcoming events.")
O("CIMC Research Update | Lattice Animals, New Researchers & Vision Weekend", "2026-10-28", "newsletter (Substack)", ["CIMC; note by Ivan Yakovenko"], NL2,
  "Research update: the Lattice Animals hackathon, new people including the first CIMC Fellow, an October 30 hackathon on a visual-cortex-inspired architecture, and attendance at Foresight's Vision Weekend on November 13-15, 2026.")
# ---- events organised or co-organised
O("CIMC Machine Consciousness Salon: Existential Hope", "2025-05-15", "salon", ["Joscha Bach", "Lou de Kerhuelvez"], "https://youtu.be/4kZE479isH8",
  "Salon conversation between Bach and Lou de K, held two weeks before the launch.")
O("Conscious AI Meetup / salon: What if we had bigger brains?", "2025-05-29", "salon", ["Stephen Wolfram", "Joscha Bach"], LAUNCH,
  "Conversation between Wolfram and Bach at the Internet Archive in San Francisco, on the first day of the launch.")
O("CIMC Launch", "2025-05-29", "launch event (May 29-31, 2025, San Francisco)", ["Joscha Bach", "Erik Newton", "Hikari Sorensen", "Christoph von der Malsburg", "Karl Friston", "Michael Levin"], LAUNCH,
  "Three-day launch with talks by Bach on CIMC's vision and on the AI perspective on consciousness, and by von der Malsburg, Friston, Levin, Sorensen and Newton. The official launch date given is May 30, 2025.")
O("AAAI 2026 Spring Symposium: Machine Consciousness: Integrating Theory, Technology, and Philosophy", "2026-04-07", "symposium (April 7-9, 2026, Burlingame, California)", ["CIMC with AAAI; speakers included Ryota Kanai, Michael Timothy Bennett, Takashi Ikegami, Robert Long, Joscha Bach"],
  "https://cimc.ai/events/aaai-symposium",
  "A two-and-a-half-day symposium in the AAAI Spring Symposium Series. CIMC reports about fifty participants, proceedings of 25 papers over 178 pages, and more than eleven hours of video. I did not find a Bach-authored paper in the proceedings; I only saw two of the papers.")
O("MC0001: The Founding Assembly for Machine Consciousness Research", "2026-05-29", "conference (May 29-31, 2026, Lighthaven, Berkeley)", ["CIMC; speakers announced included Stephen Wolfram, Anders Sandberg, Ryota Kanai, Thorsten Zander, Karl Friston, Max Hodak, Hikari Sorensen, Jim Rutt, Joscha Bach, Irina Rish, Lenore Blum, Chris Percy, Michael Levin, Richard Granger"],
  "https://machine-consciousness.ai",
  "CIMC's own field-building conference, with four tracks: foundational theory, technical implementation, ethics and governance, art and culture. Bach's talk was titled 'Consciousness and Identity'. Included an art exhibition, 'Uncanny Nova Phenomenon', curated by Aleksandra Smilek.")
O("CIMC Hackathon: Distributed Mind Sandbox Coopetition", "2026-08-01", "hackathon (San Francisco)", ["CIMC"], BERLIN,
  "A hackathon run on 'Loom', which CIMC calls its distributed compute fabric; described as Loom's first live test.")
O("CIMC x Apart Research: Digital Minds Research Sprint", "2026-08-14", "research sprint (August 14-16, 2026; San Francisco and Berlin, plus online)", ["CIMC", "Apart Research", "NYU Center for Mind, Ethics, and Policy", "Eleos AI"],
  "https://cimcai.substack.com/p/apart-research-the-digital-minds",
  "A three-day global research sprint on artificial sentience, model preferences, AI welfare and introspection. CIMC hosted the San Francisco hub. The September 2026 newsletter reports that 950 people signed up and 237 projects were submitted across six tracks. Partner names beyond Apart Research are from my notes of that newsletter.")
O("Computational Consciousness", "2026-09-11", "conference (one day, CIC Berlin)", ["CIMC with Foresight Institute's AI Node; keynotes by Joscha Bach, Thorsten Zander, Virginie van Wassenhove, Trent McConaghy, Franz Hildebrandt-Harangozó, Hikari Sorensen"],
  "https://cimc.ai/events/computational-consciousness",
  "One-day European event. Bach's keynote: 'What would it mean for a machine to be conscious?'. Hildebrandt-Harangozó spoke on the phenomenological profile of conscious experience and Sorensen on defending computational functionalism. Speaker names as shown in the event schedule.")
O("CIMC Hackathon: Lattice Animals", "2026-09-25", "hackathon (San Francisco)", ["Philip Rosedale", "Joscha Bach"], BERLIN,
  "Each participant writes a 'mind' for one grid cell; cells must find each other and hold a shape together, with movement as the only channel. Hosted by Rosedale and Bach.")
O("Ambhasi: AI x Consciousness Residency at Edge City Goa", "2026-10-18", "residency (October 18 - November 1, 2026, Goa, India)", ["CIMC", "Edge City", "Consciousness Foundation"],
  "https://cimc.ai/events/ambhasi-residency",
  "A two-week philosophy-of-mind research residency organised by CIMC with Edge City and the Consciousness Foundation.")
O("CIMC Hackathon (visual-cortex-inspired architecture)", "2026-10-30", "hackathon (San Francisco)", ["CIMC"], NL2,
  "Challenge: build software that takes live video and predicts the next frame, as a test of an architecture inspired by the visual cortex.")
O("Machine Consciousness Salons (recurring)", "2025", "salon series (San Francisco)", ["CIMC"], BERLIN,
  "Regular salons in San Francisco, listed on CIMC's Luma calendar. Individual dates beyond May 2025 were not collected.")
# ---- funded research projects
O("Funded research projects (grants)", "2025", "research grants", ["Aleksandr Groznykh; Priska Herger & Jochen Kerdels; Leander Rust; Patricia Craja & Jan Saputra Müller; Adam Safron & Zahra Sheikhbahaee"], PROJ,
  "Projects shown on the site: Self-Organizing Generative Perception; Coherent active state dynamics in self-organizing systems; Motivational architecture for conscious control; From Personality to Perceptual Architectures; Dream to Explore. Three further projects are marked hidden in the site data.")

cimc = {
    "founded": "Officially launched May 30, 2025 in San Francisco (CIMC's own statement). The legal entity is older: ProPublica shows a 501(c)(3) with EIN 99-3858960, a fiscal-year-2024 filing, and tax exemption issued June 2025. Secondary, not directly checked: Erik Newton's LinkedIn gives 'Founder and President, Jul 2024', and Bach's LinkedIn gives Executive Director from January 2025.",
    "founded_evidence": [
        {"source_url": LAUNCH, "quote_or_paraphrase": "On May 30th, we officially launched the California Institute for Machine Consciousness (CIMC)", "is_verbatim": True, "source_id": "cs_launch_2025"},
        {"source_url": PRO, "quote_or_paraphrase": "Paraphrase: 'California Institute Of Machine Consciousness', San Francisco, EIN 99-3858960; tax exemption issued June 2025; a fiscal year 2024 Form 990-EZ is listed.", "is_verbatim": False, "source_id": "propublica"},
    ],
    "founders": [
        {"name": "Joscha Bach", "basis": "Executive Director and Board Director on the team page. Described as co-founder in Erik Newton's LinkedIn text, which I saw only as a search snippet.", "verified": True},
        {"name": "Erik Newton", "basis": "President and Board Director on the team page; gave the launch talk 'How it started'. The words 'Founder' and 'co-founded with Joscha Bach' come from a LinkedIn search snippet, not from a page I fetched.", "verified": False},
    ],
    "founders_note": "No CIMC page that I retrieved states in so many words who the founders are. Bach and Newton are the best-supported answer. The FY2024 filing extract on ProPublica lists officers: Erik Newton (President), Joscha Bach (Executive Director), Lou De K (VP), Zhen Tan (Secretary), Jim Rutt (Chairman), Philip Rosedale (Treasurer), Krill Eves (Director).",
    "people": people,
    "programme_tldr": "CIMC is an independent non-profit in San Francisco that says its research is open-source. It describes its method as 'experimental computational philosophy': write down testable theories of consciousness and then try to build systems that implement them, aiming for a minimal working model. Its working definition is that a system is conscious if it implements self-organised second-order perception that increases global coherence. Research runs in three directions: foundational theory (including a project tying Kant's Critique of Pure Reason to computational philosophy), self-organisation and multi-agent systems (mostly neural cellular automata), and cognitive architectures (starting from Request Confirmation Networks, Attention Schema Theory and Global Workspace Theory). It also gives grants, runs salons, hackathons and conferences, and publishes a newsletter.",
    "programme_quotes": [
        {"source_url": "https://cimc.ai/", "quote_or_paraphrase": "CIMC does experimental computational philosophy to develop testable theories of consciousness and engineer systems that implement them.", "is_verbatim": True, "source_id": "cimc_site"},
        {"source_url": WP, "quote_or_paraphrase": "A system is conscious if it implements self-organized second-order perception that increases global coherence.", "is_verbatim": True, "source_id": "wp_2026"},
    ],
    "outputs": outputs,
    "events_attended_not_organised": [
        "Edge City Esmeralda, Healdsburg CA, 2025-06-01 to 2025-06-08",
        "CogSci 2025, San Francisco, 2025-07-30 to 2025-08-02",
        "AGI-25, Reykjavik, 2025-08-10 to 2025-08-13 (Bach talk 'The Operation of Consciousness')",
        "Models of Consciousness 2025, Sapporo, 2025-09-30 to 2025-10-04",
        "ALife 2025, Kyoto, 2025-10-06 to 2025-10-10",
        "Edge City Patagonia, 2025-10-18 to 2025-11-15",
        "Vision Weekend 2025, San Francisco, 2025-12-05 to 2025-12-07",
        "ALIFE 2026, Waterloo, Canada, 2026-08-17 to 2026-08-21 (CIMC researchers presented, including Toni Antonova)",
        "Models of Consciousness 2026 (the September newsletter says October 2026 and that CIMC researchers will attend; my earlier notes had September 12-16 in Copenhagen, so the dates are uncertain)",
        "Vision Weekend USA 2026, San Francisco, 2026-11-13 to 2026-11-15 (announced as upcoming)",
    ],
    "source_urls": ["https://cimc.ai/", TEAM, "https://cimc.ai/library", "https://cimc.ai/publications/", "https://cimc.ai/cimcHypothesis.pdf", WP,
                    "https://cimc.ai/publications/prime-hypostasis/", "https://cimc.ai/publications/against-intrinsic-properties/",
                    "https://cimcai.substack.com/", LAUNCH, "https://cimcai.substack.com/p/did-your-chatbot-just-wake-up", BERLIN, NL2,
                    "https://machine-consciousness.ai", PRO, "https://aaai.org/conference/spring-symposia/sss26/"],
}

# ---------------- bio
CVU = "http://bach.ai/pub/CV%20Joscha%20Bach.pdf"
bio = []


def B(years, place, role, url, verified=True, note=None):
    d = {"years": years, "place": place, "role": role, "source_url": url, "verified": verified}
    if note:
        d["note"] = note
    bio.append(d)


B("1973", "Weimar, Germany", "Born 21 December 1973", CVU)
B("1994-2000", "Humboldt University of Berlin", "Student: Diploma in Computer Science (equivalent to MA), secondary subject Philosophy", CVU)
B("1998-1999", "University of Waikato, Hamilton, New Zealand", "Graduate studies in Computer Science", CVU)
B("2000-2003", "Humboldt University of Berlin, Department of Computer Science, Artificial Intelligence Group", "Research assistant; led the Socionics project, the MicroPsi project and the robotic soccer simulation team", CVU)
B("2003-2005", "University of Osnabrück, Institute for Cognitive Science", "Researcher and lecturer; developed a cognitive architecture (research position September 2003 to March 2005)", CVU)
B("2007", "University of Osnabrück", "PhD in Cognitive Science, summa cum laude (thesis dated March 2007)", CVU, True,
  "English Wikipedia gives 2006 for the PhD. The CV and the thesis draft dated 30 March 2007 support 2007.")
B("2005-2010", "Berlin (start-ups)", "Founder of Bookpac GbR (2005); co-founder of Wizpac Ltd (2007); co-founder and product manager at txtr GmbH (2008-2010)", CVU)
B("2011-2012", "Berlin School of Mind and Brain, Humboldt University of Berlin", "Postdoctoral fellow", CVU)
B("2011-2013", "Hotheaven AG", "Co-founder (2011); AI scientist and development lead", CVU)
B("2012", "MicroPsi Industries GmbH", "Co-founder", CVU)
B("2013-2014", "Humanity Plus foundation", "Research fellow", CVU)
B("2014-2016", "MIT Media Lab", "Research scientist", CVU, True, "LinkedIn capture gives April 2014 to October 2016.")
B("2016-2019", "Harvard Program for Evolutionary Dynamics", "Research scientist", CVU, True, "LinkedIn capture gives November 2016 to February 2019.")
B("2019-2021", "AI Foundation", "VP of Research", CVU, True, "LinkedIn capture gives March 2019 to March 2021.")
B("2021-2023", "Intel Labs", "Principal Research Engineer, Cognitive AI", CVU, True, "LinkedIn capture gives March 2021 to January 2023.")
B("2023", "Thistledown Foundation", "Research scientist ('Current Position' in the CV dated July 14, 2023)", CVU, True, "Only the CV mentions this; end date unknown.")
B("2023-", "Liquid AI", "AI Strategist", "https://www.linkedin.com/in/joschabach", False,
  "From a search-engine capture of LinkedIn (September 2023 to present), which I could not fetch directly. Supported by the AGI-25 introduction in August 2025, which calls him 'an AI strategist at Liquid AI'. Whether he still holds the role in November 2026 is not confirmed.")
B("2025-", "California Institute for Machine Consciousness, San Francisco", "Executive Director and Board Director", "https://cimc.ai/team", True,
  "Role verified on the CIMC team page. Start date: LinkedIn capture says January 2025; CIMC's official launch was May 30, 2025; a fiscal-year-2024 tax filing extract already lists him as Executive Director.")
