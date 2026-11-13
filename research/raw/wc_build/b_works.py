bach_works = []
CV = "http://bach.ai/pub/CV%20Joscha%20Bach.pdf"


def W(title, year, venue, coauthors, url, tldr, verified=True, basis=None):
    d = {"title": title, "year": year, "venue": venue, "coauthors": coauthors, "url": url, "tldr": tldr, "verified": verified}
    if basis:
        d["verification_basis"] = basis
    bach_works.append(d)


FULL = "Full text retrieved and read (at least in part)."
CVB = "Title, year and venue seen in Bach's CV of July 2023; text not retrieved, so the summary is limited to what the title and listing show."
OA = "Metadata seen in OpenAlex (and CV where applicable); text not retrieved."

# ---- books and theses
W("Principles of Synthetic Intelligence. PSI: An Architecture of Motivated Cognition", "2009", "Oxford University Press (book)", [],
  "https://doi.org/10.1093/acprof:oso/9780195370676.001.0001",
  "Bach's only book. It presents Dietrich Dörner's Psi theory of mind in English, compares it with other cognitive architectures, and describes Bach's own software version, MicroPsi. Chapters (titles from the publisher's metadata): 1 Machines to explain the mind; 2 Dörner's 'blueprint for a mind'; 3 Representation of and for mental processes; 4 Behavior control and action selection; 5 Language and future avenues; 6 Dörner's Psi agent implementation; 7 From Psi to MicroPsi: Representations in the Psi model; 8 The MicroPsi architecture; 9 The MicroPsi framework; 10 Summary: The Psi theory as a model of cognition.",
  True, "Book text NOT retrieved. Existence, DOI and the ten chapter titles seen in OpenAlex; listed in the CV. Content summary rests on the 2007 dissertation draft, which was retrieved.")
W("Principles of Synthetic Intelligence: Building Blocks for an Architecture of Motivated Cognition (PhD thesis)", "2007", "Universität Osnabrück, Institute of Cognitive Science", [],
  "http://cognitive-ai.com/publications/assets/Draft-MicroPsi-JBach-07-03-30.pdf",
  "The doctoral thesis behind the book. Three parts: Dörner's 'blueprint for a mind' retold in detail; the Psi theory judged as a model of cognition against Soar, ACT-R and theories of emotion; and the MicroPsi architecture and toolkit. Advisors named on the title page: Hans-Dieter Burkhard, Dietrich Dörner, Kai-Uwe Kühnberger. Bibliography of roughly 590 entries.",
  True, FULL + " Draft dated 30 March 2007.")
W("Vorhersagegestützte Texteingabe durch Modellierung der Entropie (Diplomarbeit)", "2000", "Institut für Informatik, Humboldt-Universität Berlin", [], CV,
  "Diploma thesis on predictive text entry using entropy models. Not about mind or consciousness.", True, CVB)

# ---- early work
W("Lexical Attraction for Text Compression", "1999", "Data Compression Conference 1999", ["Ian H. Witten"], CV,
  "Early paper from his time at the University of Waikato on compressing text using word relationships. Not about mind.", True, CVB)
W("The MicroPsi Agent Architecture", "2003", "Proceedings of ICCM-5, International Conference on Cognitive Modeling, Bamberg", [], CV,
  "First conference description of MicroPsi, the software agent architecture based on Dörner's Psi theory.", True, CVB + " Also cited as reference [22] in the retrieved 2008 paper.")
W("Designing Agents with MicroPsi Node Nets", "2003", "KI 2003, German Conference on AI (LNAI 2821, Springer)", ["Ronnie Vuine"], CV,
  "Describes the node-net formalism MicroPsi uses to represent knowledge and control in a neural-symbolic way.", True, CVB)
W("The AEP Toolkit for Agent Design and Simulation", "2003", "MATES 2003 (LNAI 2831, Springer)", ["Ronnie Vuine"], CV,
  "Describes the software toolkit for building and simulating MicroPsi agents.", True, CVB)
W("Representations for a Complex World: Combining Distributed and Localist Representations for Learning and Planning", "2005", "In Wermter & Palm (eds.), Biomimetic Neural Learning for Intelligent Robots, Springer", [], CV,
  "On combining neural (distributed) and symbol-like (localist) representations in one agent.", True, CVB)
W("MicroPsi: Contributions to a Broad Architecture of Cognition", "2006", "KI 2006, Bremen", ["Colin Bauer", "Ronnie Vuine"], CV,
  "Overview of MicroPsi as a broad cognitive architecture.", True, CVB)
W("True Feelings: Functionalist and Descriptionalist Modeling of Emotion", "2007", "Workshop on Artificial Emotion, KI 2007, Osnabrück", [], CV,
  "Workshop paper on two ways of modelling emotion; by title, it contrasts modelling what emotions do with describing how they look.", True, CVB)
W("Seven Principles of Synthetic Intelligence", "2008", "Proceedings of the 1st Conference on Artificial General Intelligence, Memphis, pp. 63-74", [],
  "http://icontology.com/publications/assets/AGI%20Bach.pdf",
  "Seven lessons from five decades of AI: build whole functionalist architectures; avoid methodologism; aim for the big picture; build grounded systems without getting tangled in the symbol grounding problem; do not wait for robotic embodiment; build autonomous systems; intelligence will not emerge by itself. Uses MicroPsi as the example.",
  True, FULL)
W("Kybernetik (encyclopedia entry)", "2010", "Sandkühler (ed.), Enzyklopädie Philosophie, Felix-Meiner-Verlag, Hamburg", [], CV,
  "Encyclopedia article on cybernetics.", True, CVB)
W("Artificial General Intelligence and Organizational Intelligence (On the Singularity of AI)", "2010", "ECAP 10, 8th European Conference on Computing and Philosophy, Munich", [], CV,
  "Conference paper; by title, it relates general AI to the intelligence of organisations.", True, CVB)
W("A Motivational System for Cognitive AI", "2011", "AGI 2011 (Springer), pp. 232-242", [], CV,
  "Presents the MicroPsi model of needs and motives as a general motivational system for AI agents.", True, CVB)
W("No Room for the Mind: Enactivism in Artificial Intelligence", "2011", "International Conference on the History and Philosophy of Computing, Ghent", [], CV,
  "A critique of enactivism, the view that mind is made by bodily interaction with the world and not by internal models. Also cited in the 2018 conductor paper.", True, CVB)
W("Enactivism Considered Harmful", "2011", "Philosophy & Theory of Artificial Intelligence (PT-AI), Thessaloniki", [], CV,
  "Second 2011 conference paper against enactivism in AI.", True, CVB)
W("Requirements for Cognitive Artificial Intelligence", "2011", "Philosophy & Theory of Artificial Intelligence (PT-AI), Thessaloniki", [], CV,
  "Conference paper on what a cognitive AI system would need.", True, CVB)
W("MicroPsi 2: The Next Generation of the MicroPsi Framework", "2012", "AGI 2012, Oxford, pp. 11-20", [], CV,
  "Describes the rewritten MicroPsi 2 software framework.", True, CVB)
W("A Framework for Emergent Emotions, Based on Motivation and Cognitive Modulators", "2012", "International Journal of Synthetic Emotions 3(1), 43-63", [], CV,
  "Journal paper: emotions are treated as arising from needs plus 'modulators' that change how the whole system processes information.", True, CVB)
W("Functional Modeling of Personality Properties Based on Motivational Traits", "2012", "ICCM-7, International Conference on Cognitive Modeling, Berlin, pp. 271-272", [], CV,
  "Short paper linking personality differences to different settings of the needs in the motivational model.", True, CVB)
W("Modeling Motivation and the Emergence of Affect in a Cognitive Agent", "2012", "In Wang (ed.), Theoretical Foundations of Artificial General Intelligence, Atlantis Press", [], CV,
  "Book chapter on motivation and the emergence of affect in the MicroPsi agent.", True, CVB)
W("What Kind of Machine is the Mind?", "2012", "Turing-100, Alan Turing Centenary Conference, Manchester (published in EPiC Series)", ["Mario Verdicchio"],
  "https://doi.org/10.29007/k6f4",
  "A philosophical paper asking in what sense the mind is a machine. Cited in the 2026 CIMC whitepaper as Bach & Verdicchio 2012.", True, OA)
W("Mapping the Landscape of Human-Level Artificial General Intelligence", "2012", "AI Magazine 33(1)", ["Sam S. Adams", "Itamar Arel", "Robert Coop", "Rod Furlan", "Ben Goertzel", "J. Storrs Hall", "Alexei Samsonovich", "Matthias Scheutz", "Matthew Schlesinger", "Stuart C. Shapiro", "John Sowa"], CV,
  "A multi-author survey of what human-level AI would require and how to measure progress towards it.", True, CVB + " CV gives the short title 'Mapping the AGI Landscape'; the full title is from OpenAlex.")
W("Computationalism and Cognitive Science", "2014", "BICA 2014, Cambridge MA", [], CV,
  "Conference paper on computationalism as a basis for cognitive science.", True, CVB)
W("Artificial General Intelligence as a Foundational Discipline in Cognitive Science", "2014", "AGI 2014, Quebec", [], CV,
  "Conference paper arguing that building general AI is a basic method of cognitive science.", True, CVB)
W("Modeling Motivation in MicroPsi 2", "2015", "AGI 2015, Berlin (Springer LNCS)", [],
  "https://doi.org/10.1007/978-3-319-21365-1_1",
  "Updated model of needs, including bodily, social and cognitive ones, in MicroPsi 2. The CV lists it as 'Modeling Motivation in the MicroPsi Architecture'.", True, OA)
W("Request confirmation networks for neuro-symbolic script execution", "2015", "CoCo workshop at NIPS 2015, Montreal (CEUR Vol-1583)", ["Priska Herger"],
  "https://ceur-ws.org/Vol-1583/CoCoNIPS_2015_paper_6.pdf",
  "Introduces ReCoNs: networks whose units pass requests down and confirmations up, so that a neural system can run ordered, hierarchical scripts such as checking the parts of an object one after another.", True, FULL)
W("The Age Of The New Machines, Or Every Society Will Get The Artificial Intelligence It Deserves", "2015", "Edge Annual Question 2015; also in Brockman (ed.), What to Think About Machines That Think", [],
  "https://www.edge.org/response-detail/26205",
  "Short essay. There is no basic barrier to human-like AI; such systems will scale beyond humans; their motives will at first be those of the organisations that build them, so the danger lies in those organisations' goals.", True, FULL)
W("Four Gods", "2015", "bach.ai blog (2015-12-11)", [], "http://bach.ai/four-gods/",
  "Separates four things people mean by 'God': the god of a religious narrative, the god of spiritual experience, a principle of meaning, and Aristotle's prime mover.", True, FULL)
W("Everything Is Computation", "2016", "Edge Annual Question 2016", [], "https://www.edge.org/response-detail/26733",
  "Argues that computation is the 20th century's most important idea. It replaces 'mechanism' in philosophy, differs from mathematics, and suggests the universe is computational and not mathematical.", True, FULL)
W("Do we live in a simulation or in the base reality?", "2016", "bach.ai blog (2016-06-05)", [], "http://bach.ai/Do-we-live-in-a-simulation/",
  "Sorts out six meanings of 'we live in a simulation' and judges each, using Solomonoff's idea of the best predictive model.", True, FULL)
W("From elementary computation to ethics?", "2016", "bach.ai blog (2016-09-23)", [], "http://bach.ai/from-computation-to-ethics/",
  "A 16-step path from a computational universe through entropy, life and agency to norms.", True, FULL)
W("On Marvin Minsky", "2016", "bach.ai blog (2016-01-26)", [], "http://bach.ai/on-marvin-minsky/",
  "Obituary note on Minsky's influence on the study of mind.", True, FULL)
W("The Cortical Conductor Theory: Towards Addressing Consciousness in AI Models", "2017", "Workshop on Architectures for Generality and Autonomy, IJCAI 2017, Melbourne; revised version in BICA 2018 (Springer)", [],
  "http://bach.ai/pub/Bach%20-%20Cortical%20Conductor%20Theory%20(BICA%202018).pdf",
  "Proposes that consciousness is the work of a 'conductor': brain processes that direct attention across the cortical 'orchestra' and keep a record of it. Presented as a functionalist alternative to Integrated Information Theory.",
  True, FULL + " The retrieved PDF is the BICA 2018 version (doi 10.1007/978-3-319-99316-4_3 per OpenAlex); the 2017 IJCAI workshop version is from the CV.")
W("Consciousness as a Memory of Coordinating Attention: The Conductor Model of Consciousness", "2017", "Science of Consciousness Conference, San Diego", [], CV,
  "Conference presentation of the conductor model.", True, CVB)
W("Generic Animats", "2017", "AGI 2017, Melbourne", ["Claes Strannegård", "Nils Svangård", "Bas Steunebrink"], CV,
  "Co-authored paper on simple artificial animals as a route to general AI.", True, CVB)
W("The Animat Path to Artificial General Intelligence", "2017", "Workshop on Architectures for Generality and Autonomy, IJCAI 2017", ["Claes Strannegård", "Nils Svangård", "D. Lindström", "Bas Steunebrink"], CV,
  "Co-authored workshop paper on the same animat approach.", True, CVB)
W("Attention Based Learning as a Foundation for Conscious Agents", "2018", "BICA 2018 post-proceedings, Procedia Computer Science (venue per CV; the paper itself looks like a submission to a Common Model of Cognition workshop, so the CV venue may be wrong)", [], None,
  "Position paper. Suggests replacing or adding to backpropagation with learning from a record of what attention did, and proposes that this integrated record may explain both the function and the feel of consciousness.",
  True, FULL + " Download URL not recorded; venue and year from CV.")
W("Request Confirmation Networks in MicroPsi 2", "2018", "AGI 2018 (Springer LNCS)", ["Katherine Gallagher"],
  "https://doi.org/10.1007/978-3-319-97676-1_2",
  "Implementation of request confirmation networks in the MicroPsi 2 framework.", True, OA + " Co-author's first name as given by OpenAlex; CV gives 'Gallagher, K.'.")
W("Consciousness in Humans and other Machines", "2018", "AAAI Fall Symposium workshop 'Towards common model of cognition' (as cited by Bach)", [], None,
  "Cited by Bach as 'Bach 2018b' in his 2019 paper. Not retrieved.", True, "Seen only as a citation in the retrieved 2019 paper; not in the CV list. Treat venue as reported by that citation.")
W("Phenomenal Experience and the Perceptual Binding State", "2019", "AAAI Spring Symposium workshop 'Towards Conscious AI Systems' (CEUR Vol-2287)", [],
  "https://ceur-ws.org/Vol-2287/paper29.pdf",
  "Argues that experience belongs to the brain's simulated world and not to physics: only a simulation can be conscious. The self is a virtual character in that world. Consciousness is tied to the unified 'binding state' built by attention.", True, FULL)
W("Extending MicroPsi's Model of Motivation and Emotion for Conversational Agents", "2019", "AGI 2019 (Springer LNCS)", ["Murilo Coutinho", "Liza Lichtinger"],
  "https://doi.org/10.1007/978-3-030-27005-6_4",
  "Extends the MicroPsi model of needs and emotion for use in conversational agents; from his time at AI Foundation.", True, OA)
W("Mean Shift Rejection: Training Deep Neural Networks Without Minibatch Statistics or Normalization", "2019", "arXiv:1911.13173", ["Brendan Ruff", "Taylor Beck"],
  "https://arxiv.org/abs/1911.13173",
  "A machine-learning engineering paper on training deep networks without batch normalisation. Not about mind.", True, "Seen in the arXiv API result and the CV.")
W("When Artificial Intelligence Becomes General Enough to Understand Itself", "2020", "Journal of Artificial General Intelligence, special issue 'On Defining Artificial Intelligence' (commentary)", [],
  "https://doi.org/10.2478/jagi-2020-0003",
  "Bach's commentary in a journal special issue on how to define AI.", True, "Title and DOI from the CV; Crossref confirms the DOI is the special issue of commentaries. Text not retrieved.")
W("Virtualism as a perspective on consciousness", "2021", "Philosophy and Computing Conference at IS4SI 2021", [], CV,
  "Conference talk; by title, it presents the view that consciousness is a virtual (simulated) property.", True, CVB)
W("Functionality and phenomenology of consciousness", "2022", "Models of Consciousness MoC3, Stanford", [], CV,
  "Conference talk on the function and the felt side of consciousness.", True, CVB)
W("Thrill-K Architecture: Towards a Solution to the Problem of Knowledge Based Understanding", "2022", "AGI 2022 (Springer LNCS, published 2023)", ["Gadi Singer", "Tetiana Grinberg", "Nagib Z. Hakim", "Phillip Howard", "Vasudev Lal", "Zev Rivlin"],
  "https://doi.org/10.1007/978-3-031-19907-3_39",
  "Intel Labs paper proposing an AI architecture with three tiers of knowledge: instant, standby and retrieved from outside.", True, OA + " CV lists authors as Singer, Bach, Grinberg.")
W("We can almost see the AGI from up here", "2022", "Joscha Bach Substack (2022-04-15)", [], "https://joscha.substack.com/p/coming-soon",
  "First post on his Substack. Listed in the archive; not read for this map.", True, "Title and date seen in the Substack archive API; body not read.")
W("Generative Image Model Benchmark for Reasoning and Representation (GIMBRR)", "2023", "Workshop EDGeS 2023, AAAI 2023 Spring Symposium", ["J. Achterberg", "R. Arel", "A. Chaibi", "N. Tzagkarakis"], CV,
  "Co-authored benchmark paper for image-generating models. Not about consciousness.", True, CVB)
W("Levels of Lucidity", "2023", "Joscha Bach Substack (2023-05-21)", [], "https://joscha.substack.com/p/levels-of-lucidity",
  "Essay setting out seven stages of a mind's insight into itself, built on Kegan's stage model.", True, FULL)
W("The Existential Risk of AGI", "2023", "Joscha Bach Substack (2023-06-22)", [], "https://joscha.substack.com/p/the-existential-risk-of-agi",
  "Written after a debate with Connor Leahy. Argues that AI cannot simply be aligned to 'human values', that values must be derived and not assumed, and that lasting alignment comes from discovering shared purposes.", True, FULL)
W("A Path to Generative Artificial Selves", "2023", "EPIA 2023, Progress in Artificial Intelligence (Springer LNCS), pp. 15-29", ["Liane Gabora (first author)"],
  "https://doi.org/10.1007/978-3-031-49011-8_2",
  "Uses autocatalytic network theory to ask how a machine could have a self. Concludes that an AI could plausibly have selfhood and creative agency at the level of its worldview, but not at the bodily level.", True, "Abstract and preprint text retrieved.")
W("Building Artificial Intelligence with Creative Agency and Self-hood", "2024", "arXiv:2407.10978; OSF preprint (invited lay summary for The Academic)", ["Liane Gabora (first author)"],
  "http://arxiv.org/abs/2407.10978",
  "A short summary for general readers of the 2023 Gabora and Bach paper on autocatalytic networks and artificial selves.", True, "Abstract seen in the arXiv API result.")
W("Wie bewusst ist das Bewusstsein?", "2024", "Kursbuch 220", ["Sibylle Anderl"],
  "https://doi.org/10.5771/0023-5652-2024-220-29",
  "German-language piece with the journalist Sibylle Anderl; the title means 'How conscious is consciousness?'. Not retrieved, so the format (interview or essay) is not confirmed.", True, OA)
W("The Machine Consciousness Hypothesis", "2025", "California Institute for Machine Consciousness (essay; dated 2025-09-15, public January 2026)", ["Hikari Sorensen"],
  "https://cimc.ai/cimcHypothesis.pdf",
  "The founding essay of CIMC. States the hypothesis that general computers can be conscious and that this can be tested; defines consciousness as second-order perception that increases coherence; introduces cyber-animism, the conductor theory, the Genesis Hypothesis and the Human Consciousness Hypothesis; and argues there can be no Turing Test for consciousness.", True, FULL)
W("If a machine became conscious, how would we know? (TED talk)", "2025", "TED", [],
  "https://www.ted.com/talks/joscha_bach_if_a_machine_became_conscious_how_would_we_know",
  "TED talk listed in CIMC's news feed. Not watched or transcribed for this map.", True, "Title and link seen in CIMC's news data (dated September 2025 there); talk content not retrieved.")
W("The Operation of Consciousness (AGI-25 talk)", "2025", "AGI-25 conference, Reykjavik", [], "https://youtu.be/xDzAclUq3U4",
  "Conference talk on the mechanisms of consciousness; refers back to his 2024 cyber-animism talk and describes consciousness as a learning algorithm that builds world, self and mind.", True, "Listed in CIMC events data; transcript collected by another researcher was sampled.")
W("On the Jeffrey Epstein Affair", "2025", "Joscha Bach Substack (2025-11-28)", [], "https://joscha.substack.com/p/on-the-jeffrey-epstein-affair",
  "A personal statement. Outside the scope of this map (mind, consciousness, computation); listed for completeness and not summarised.", True, "Title and date seen in the Substack archive API; not summarised.")
W("The California Institute for Machine Consciousness Research Program Whitepaper", "2026", "California Institute for Machine Consciousness", ["Hikari Sorensen", "Franz Hildebrandt-Harangozó", "Lou de Kerhuelvez", "Jim Rutt"],
  "https://cimc.ai/publications/research-program-whitepaper/",
  "CIMC's programme document; Bach is the last-listed author. Gives the operational definition of consciousness, places CIMC against other theories (global workspace, higher-order, IIT, enactivism, predictive processing), and discusses ethics and risk.", True, FULL)
W("\"I had a feeling that Epstein had a dark heart\" (interview with Sibylle Anderl, Die Zeit)", "2026", "Joscha Bach Substack (2026-02-12), reproducing a Die Zeit interview", ["Sibylle Anderl (interviewer)"],
  "https://joscha.substack.com/p/i-had-a-feeling-that-epstein-had",
  "Newspaper interview. Outside the scope of this map; listed for completeness and not summarised.", True, "Title, subtitle and date seen in the Substack archive API; not summarised.")
W("The age of AGE: Artificial General Experience", "2026", "Joscha Bach Substack (2026-03-27); text written for Rana Gujral's book 'The AI Instinct'", [],
  "https://joscha.substack.com/p/the-age-of-age",
  "A foreword-style text. Calls current AI systems 'artificial idiot savants', says AI will change human identity, and argues that we need AI that shares purposes with us and extends our consciousness instead of 'hollow agency'.", True, FULL)
W("AAAI 2026 Spring Symposium keynote", "2026", "AAAI Spring Symposium 'Machine Consciousness: Integrating Theory, Technology, and Philosophy', Burlingame CA", [],
  "https://youtu.be/tO3qsL66eqU",
  "Bach's keynote at the symposium CIMC helped organise. Not watched; no title recorded.", True, "Video link seen in CIMC data; content not retrieved.")
W("Consciousness and Identity (MC0001 talk)", "2026", "MC0001, Lighthaven, Berkeley", [], "https://youtu.be/4qccvFCGpM0",
  "Bach's talk at CIMC's founding assembly. Not watched.", True, "Title and link seen in CIMC data; content not retrieved.")
W("What would it mean for a machine to be conscious? (keynote)", "2026", "Computational Consciousness, CIC Berlin (2026-09-11)", [], "https://cimc.ai/events/computational-consciousness",
  "Bach's keynote at CIMC's Berlin event. Not watched.", True, "Title seen in the CIMC event schedule; content not retrieved.")
