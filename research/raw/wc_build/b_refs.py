references = []


def m(sid, text, v=False):
    return {"source_id": sid, "quote_or_paraphrase": text, "is_verbatim": v}


def R(name, kind, author, year, tldr, take, mentions, verified=True):
    references.append({"name": name, "kind": kind, "author": author, "year": year, "tldr": tldr,
                       "bach_take": take, "mentions": mentions, "verified": verified})


BIB = "Paraphrase: listed in the dissertation bibliography"

# ================= A. Psi / MicroPsi lineage (dissertation draft 2007, Seven Principles 2008) =================
R("Dietrich Dörner", "person", None, None,
  "German psychologist at the University of Bamberg who built a theory of the whole mind as a machine. His Psi theory tries to explain motivation, emotion, memory and action control with one set of mechanisms. He was one of the advisors of Bach's doctoral thesis.",
  "Bach's MicroPsi is an implementation and extension of Dörner's theory. The first chapter of the thesis is a detailed retelling of Dörner's 'blueprint for a mind'.",
  [m("seven_2008", "MicroPsi [22, 23] is an implementation of Dietrich Dörner’s Psi theory of mental representation, information processing, perception, action control and emotion", True),
   m("psi_diss_2007", "Paraphrase: title page names Hans-Dieter Burkhard, Dietrich Dörner and Kai-Uwe Kühnberger as advisors; chapter 1 is titled Dörner's 'blueprint for a mind'."),
   m("cv_2023", "Paraphrase: CV lists joint tutorials and symposia with Dörner (ICCM 2006, KogWis 2005) and a 2008 published interview with him.")])
R("Psi theory", "theory", "Dietrich Dörner", "1999",
  "A theory of how a mind works as a whole system. An agent has a small set of built-in needs (for example food, safety, certainty, competence and belonging), and these needs create motives that steer perception, memory, planning and action. Emotions are not separate modules but ways in which the whole system changes its style of processing.",
  "Bach treats it as a serious candidate for a full cognitive architecture and turns it into running software (MicroPsi). He also notes what it leaves out, such as low-level brain details.",
  [m("psi_diss_2007", "Paraphrase: section 1.8 covers behaviour control and action selection with urges for fuel/water, intactness, certainty, competence and affiliation; section 2.3 discusses the Psi theory as a model of human cognition."),
   m("openalex", "Paraphrase: chapter 10 of the 2009 OUP book is titled 'Summary: The Psi theory as a model of cognition'.")])
R("Bauplan für eine Seele", "book", "Dietrich Dörner", "1999",
  "Dörner's main book, whose title means 'Blueprint for a Soul'. It builds up a mind step by step, starting from a very simple vehicle and adding needs, memory, planning, emotion and language.",
  "This is the main source Bach's thesis and book retell and formalise for an English-speaking audience.",
  [m("seven_2008", "Paraphrase: reference [24] Dörner, D. (1999). Bauplan für eine Seele. Reinbeck."),
   m("psi_diss_2007", "Paraphrase: the thesis says Dörner's theory of the mind is laid down in 'Bauplan für eine Seele' ('Blueprint for a Soul') and that Dörner introduces it incrementally.")])
R("Die Mechanik des Seelenwagens", "book", "Dietrich Dörner, C. Bartl, F. Detje, J. Gerdes, D. Halcour", "2002",
  "A follow-up to Dörner's 'Bauplan' that describes the regulation of action in more technical detail and reports computer implementations of the Psi agent.",
  "Used by Bach as the second main source for the details of Dörner's agent implementation.",
  [m("seven_2008", "Paraphrase: reference [25] Dörner et al. (2002). Die Mechanik des Seelenwagens. Handlungsregulation. Verlag Hans Huber, Bern.")])
R("Vehicles: Experiments in Synthetic Psychology", "book", "Valentino Braitenberg", "1984",
  "A short book of thought experiments. Very simple wheeled machines with a few sensors and motors seem to show fear, love or curiosity, which suggests that complex-looking behaviour can come from simple wiring.",
  "Bach reports that Dörner starts his blueprint of a mind from a Braitenberg vehicle and adds mechanisms from there.",
  [m("psi_diss_2007", "Paraphrase: Dörner 'starts out with a very simple system: a Braitenberg vehicle' (Braitenberg 1984).")])
R("Unified Theories of Cognition / Soar", "theory", "Allen Newell; John Laird, Paul Rosenbloom", "1990",
  "Newell argued that psychology needs single theories that cover all of cognition, built as running computer architectures. Soar is his group's example: a system that solves problems by applying rules and learning new ones.",
  "Bach uses Newell's layers of description and compares the Psi theory with Soar as one of the 'machines of cognition'. In the CIMC essay the cognitive-architecture tradition is named as background.",
  [m("psi_diss_2007", "Paraphrase: Table 2.1 'Layers of Description of a Cognitive System (Newell 1990)'; section 2.2 discusses Soar and ACT-R."),
   m("seven_2008", "Paraphrase: reference [16] Laird, Newell & Rosenbloom (1987), Soar: An architecture for general intelligence.")])
R("ACT-R", "theory", "John R. Anderson", "1990",
  "A widely used cognitive architecture from psychology. It models thinking as rules that fire one at a time over chunks of memory, each with a numeric level of activation, and it is tested against timing data from human experiments.",
  "Bach describes it next to Soar as a rule-based competitor to the Psi approach, which puts motivation and emotion at the centre instead.",
  [m("psi_diss_2007", "Paraphrase: 'Just as Soar, ACT-R is based on production rules', but unlike Soar it does not fire them in parallel and allows real-valued activations."),
   m("seven_2008", "Paraphrase: reference [15] Anderson, J. R. (1990). The adaptive character of thought.")])
R("Marvin Minsky", "person", None, None,
  "Co-founder of the field of artificial intelligence at MIT. In 'The Society of Mind' (1986) and 'The Emotion Machine' (2006) he described the mind as a large crowd of simple cooperating processes, with no single principle behind it.",
  "Bach calls him the most influential recent thinker on the nature of minds and opens his conductor paper with a Minsky epigraph. He borrows Minsky's remark that 'consciousness' is a suitcase word.",
  [m("bachai_minsky_2016", "Marvin Minsky was quite certainly the most influential thinker about the nature of our minds in recent history.", True),
   m("ctc_2018", "This has lead Marvin Minsky (2006) to call consciousness “a suitcase term”, a notion that is notoriously hard to unpack.", True),
   m("psi_diss_2007", BIB + " with Minsky (1975) on frames, The Society of Mind (1986) and The Emotion Machine (2006)."),
   m("cimc_library", "Paraphrase: The Society of Mind (1985 in the list) appears under modern texts in the CIMC library.")])
R("Aaron Sloman", "person", None, None,
  "British philosopher and AI researcher. He argued that philosophy of mind should be done by designing working minds, and he proposed the CogAff scheme that sorts mental processes into reactive, deliberative and reflective layers.",
  "Bach uses a Sloman line as the motto for his chapter on cognitive architectures and compares Sloman's Cognition and Affect work with the Psi theory, calling it inspiring but not very detailed.",
  [m("psi_diss_2007", "“Every intelligent ghost must contain a machine.” Aaron Sloman (2002)", True),
   m("psi_diss_2007", "Paraphrase: the preface mentions 'Aaron Sloman's inspiring but not very detailed Cognition and Affect architecture'.")])
R("Minds, Brains, and Programs (the Chinese Room)", "paper", "John Searle", "1980",
  "A thought experiment. A person who follows rules for shuffling Chinese symbols can give correct answers without understanding Chinese, so Searle concludes that running a program is not enough for understanding.",
  "Bach lists Searle among the standard objections to AI in 2008. The CIMC essay places the Chinese Room next to Leibniz's mill as an illustration of the gap that a functional account has to close, and does not accept Searle's conclusion.",
  [m("seven_2008", "Paraphrase: references [4] Searle (1992) The Rediscovery of the Mind and [9] Searle (1980) Minds, brains, and programs."),
   m("mch_2025", "Paraphrase: 'Centuries later, John Searle's Chinese Room illustrates a similar gap in his perspective on computational systems', replacing Leibniz' machine with a computer."),
   m("psi_diss_2007", "Paraphrase: index entry 'Chinese Room argument'; bibliography lists Searle 1980, 1984, 1992.")])
R("What Computers Still Can't Do", "book", "Hubert Dreyfus", "1992",
  "A philosopher's long-running critique of symbolic AI. Dreyfus argued that human skill rests on bodily know-how and context that cannot be written down as explicit rules.",
  "Bach cites Dreyfus for the weakness of purely symbolic systems in real-world grounding, without giving up on computational models of mind.",
  [m("psi_diss_2007", "Paraphrase: symbolic AI 'is also difficult to ground into real world interactions and to scale upon dynamic environments (see, for instance, Dreyfus 1992)'."),
   m("seven_2008", "Paraphrase: reference [5] Dreyfus (1992).")])
R("The Symbol Grounding Problem", "paper", "Stevan Harnad", "1990",
  "Asks how the symbols inside a computer can mean anything to the system itself, and not only to the people who read them. Harnad's answer is that symbols must be tied to perception and action.",
  "Bach's fourth principle says to build grounded systems but not to get stuck in this problem. For him grounding can happen in a simulated world as well as a physical one.",
  [m("seven_2008", "Build grounded systems, but do not get entangled in the Symbol Grounding Problem", True),
   m("seven_2008", "Paraphrase: 'Representations in MicroPsi are always grounded in environmental interaction or abstractions thereof', whether the environment is simulated or physical.")])
R("How the Body Shapes the Way We Think (embodied AI)", "book", "Rolf Pfeifer, Josh Bongard", "2006",
  "A statement of embodied AI: intelligence comes from the interplay of a body, its materials and the world, so robots are needed to study it.",
  "Bach pushes back. His fifth principle of 2008 tells researchers not to wait for robot bodies before modelling the mind.",
  [m("seven_2008", "Do not wait for the rapture of robotic embodiment", True),
   m("seven_2008", "Paraphrase: references [10] Pfeifer & Stieler (2007) and [11] Pfeifer & Bongard (2006).")])
R("The Language of Thought", "book", "Jerry Fodor", "1975",
  "Claims that thinking happens in an inner symbolic code with a grammar, somewhat like a language. This is the classic statement of symbolic cognitive science.",
  "Bach presents it as the position behind symbolic architectures and sets it against connectionist replies, as part of asking what kind of representation a mind needs.",
  [m("psi_diss_2007", "Paraphrase: 'The Language Of Thought Hypothesis (LOTH) is usually attributed to Jerry Fodor (1975)', and it tries to explain how a material thing can have semantic properties."),
   m("seven_2008", "Paraphrase: reference [14] Fodor (1975).")])
R("Daniel Dennett", "person", None, None,
  "American philosopher. He argued that beliefs and desires are real patterns visible from the 'intentional stance', and that consciousness is the work of many parallel processes with no inner theatre, so that the feeling of an inner show is a kind of user illusion.",
  "Bach puts his own conductor theory in the same functionalist family as Dennett and Graziano. He also cites Dennett for the view that the self-as-experienced is a representation.",
  [m("ctc_2018", "Unlike IIT, CTC is a functionalist model of consciousness, with similarity to other functionalist approaches, such as the ones suggested by Dennett and Graziano", True),
   m("psi_diss_2007", "Paraphrase: a compromise between realist and instrumentalist views 'is suggested by Dennett (1991)': beliefs and desires are detected from an intentional stance yet are objective phenomena."),
   m("cimc_library", "Paraphrase: Consciousness Explained (1991), From Bacteria to Bach and Back (2017) and The Mind's I (with Hofstadter, 1981) are in the CIMC library."),
   m("wp_2026", "Paraphrase: Dennett, Graziano and Hofstadter are named as people who mean to address the phenomenology questions yet are often perceived as not addressing them.")])
R("Being No One (self-model theory)", "book", "Thomas Metzinger", "2003",
  "Argues that there are no selves in the world, only self-models. The brain builds a model of the organism and cannot see that it is a model, so the organism feels like someone.",
  "Bach uses Metzinger as the detailed argument for his claim that the self is a representation without agency of its own. The 2007 thesis already uses Metzinger's idea of a model of the intentionality relation.",
  [m("phen_2019", "Paraphrase: 'For a detailed argument about why the self does not possess agency but is a representation, see Metzinger 2003.'"),
   m("psi_diss_2007", "Paraphrase: the agent needs a model of itself as a representing thing; 'Metzinger calls this representation a phenomenal model of the intentionality relation (PMIR)'."),
   m("cimc_library", "Paraphrase: Being No One (2003) and The Elephant and the Blind are in the CIMC library."),
   m("wp_2026", "Paraphrase: whitepaper reference list includes Metzinger 2000, 2003, 2021 and 2024.")])
R("Facing Up to the Problem of Consciousness / The Conscious Mind (the Hard Problem)", "paper", "David Chalmers", "1995",
  "Chalmers separates the 'easy' problems of explaining what the brain does from the 'hard' problem of why any of it is felt. He argues that function alone does not explain experience.",
  "Bach and CIMC take the hard problem as the starting challenge and answer that experience is a property of the brain's simulated world, so a functional account can cover it. Chalmers appears already in the 2008 paper's list of objections.",
  [m("mch_2025", "Paraphrase: the hard problem, 'coined more recently as a term by David Chalmers', is described as the difficulty of reducing phenomenology to mechanistic interactions."),
   m("phen_2019", "Paraphrase: Chalmers (1995) 'characterizes this as the Hard Problem of Consciousness'."),
   m("seven_2008", "Paraphrase: reference [3] Chalmers (1996) The Conscious Mind."),
   m("cimc_library", "Paraphrase: The Conscious Mind (1996) is in the CIMC library under classical texts.")])
R("Epiphenomenal Qualia", "paper", "Frank Jackson", "1982",
  "The 'Mary' argument. A scientist who knows all the physical facts about colour but has never seen colour seems to learn something new when she first sees red, which Jackson took to show that physical facts are not all the facts.",
  "It is the first entry in the reference list of Bach's 2008 paper, as one of the philosophical objections that AI has to face. No detailed reply to it was found in the retrieved text.",
  [m("seven_2008", "Paraphrase: reference [1] Jackson, F. (1982). Epiphenomenal qualia. Philosophical Quarterly 32.")])
R("Cybernetics", "tradition", "Norbert Wiener; W. Ross Ashby; Ludwig von Bertalanffy; Gregory Bateson", "1948",
  "The mid-century science of control and feedback in animals and machines. It describes minds, bodies and societies as systems that regulate themselves.",
  "Bach places the Psi theory in this systems-science line. His CV also lists an encyclopedia entry he wrote on 'Kybernetik'.",
  [m("psi_diss_2007", "Paraphrase: 'The description of such systems is the domain of cybernetics or systems science (Wiener 1948, Ashby 1956, von Bertalanffy 1968, Bischof 1968, Bateson 1972, Klir 1992).'"),
   m("cv_2023", "Paraphrase: Bach, J. (2010): Kybernetik. In Sandkühler (ed.), Enzyklopädie Philosophie, Felix-Meiner-Verlag.")])
R("Against Method", "book", "Paul Feyerabend", "1975",
  "Argues that science has no single fixed method and that rigid rules of method would have blocked many real discoveries.",
  "Bach cites it for the warning against 'methodologism': letting the tools you already have decide which questions you ask. This became his second principle, 'Avoid methodologism'.",
  [m("psi_diss_2007", "Paraphrase: one should not fall victim to 'methodologism', ignoring what lies outside the methodology already at hand (Feyerabend 1975)."),
   m("seven_2008", "Avoid methodologism", True)])
R("The Cognitive Structure of Emotions (OCC model)", "book", "Andrew Ortony, Gerald Clore, Allan Collins", "1988",
  "A widely used scheme that sorts emotions into types according to how a person appraises events, agents and objects. Many software agents use it as a lookup table for emotions.",
  "Bach lists it among the many competing taxonomies of emotion and reports that Dörner rejects this patchwork; in the Psi view emotions emerge from modulated processing and are not picked from a list.",
  [m("psi_diss_2007", "Paraphrase: emotion taxonomies are listed (Osgood 1957; Izard 1981; Ortony, Clore, Collins 1988; Ekman et al. 1972; Plutchik 1994); 'Dörner rejects this terminological and conceptual heterogeneity'.")])
R("Global Workspace Theory", "theory", "Bernard Baars; Stanislas Dehaene", "1988",
  "Says that a piece of information is conscious when it is broadcast across the brain so that many specialised processes can use it at once. Dehaene gave it a neuroscience version with measurable brain signatures.",
  "Bach treats it as a useful functional account. CIMC's whitepaper says it explains which information is available but that consciousness is the second-order perception that organises coherence among the contents, not the broadcast itself.",
  [m("phen_2019", "Paraphrase: relating perceptual content and knowledge 'is explored in Bernard Baars' Global Workspace theory (1993), and its neuroscientific adaptation by Stanislas Dehaene (2014)'."),
   m("wp_2026", "Paraphrase: 'Global Workspace Theory (Baars, 1988) proposes that conscious content is distinguished from unconscious processing by its availability to multiple specialized cognitive subsystems through global broadcast.'"),
   m("cimc_site", "Paraphrase: the cognitive-architectures research direction names Request Confirmation Networks, Attention Schema Theory and Global Workspace Theory."),
   m("psi_diss_2007", BIB + " (Baars 1993).")])
R("Ned Block", "person", None, None,
  "Philosopher of mind. He raised classic doubts about functionalism ('Troubles with functionalism', 1978) and separated phenomenal consciousness, what it is like, from access consciousness, what is available for report and control (1995).",
  "Bach cites Block in his 2007 thesis and 2008 paper. In the 2025 CIMC essay Block appears only at second hand, in a footnote. No direct discussion of Block by Bach was found.",
  [m("psi_diss_2007", BIB + " with Block (1978) 'Troubles with functionalism' and Block (1995) 'The Mind as the Software of the Brain'."),
   m("seven_2008", "Paraphrase: reference [2] Block (2001), Paradox and Cross Purposes in Recent Work on Consciousness."),
   m("mch_2025", "Paraphrase: a footnote on Amanda Askell's 2022 essay says 'Askell cites Block (1995) for a more nuanced account of the inner cinema metaphor'. Block is not discussed further there.")])
R("Tractatus Logico-Philosophicus", "book", "Ludwig Wittgenstein", "1921",
  "A short, strict book that tries to say what can be said clearly, by treating meaningful sentences as logical pictures of facts.",
  "Bach's thesis cites it for the habit of equating thought with language. The CIMC essay cites Russell's introduction to it for the point that all logic can be built from one operation (NAND); CIMC counts Wittgenstein among AI's philosophical ancestors.",
  [m("psi_diss_2007", "Paraphrase: 'since Wittgenstein (1921), thinking is generally quite often equated with linguistic productivity'."),
   m("mch_2025", "Paraphrase: 'As Bertrand Russell anticipates in the 1922 introduction to Wittgenstein's Tractatus', it is in principle sufficient to use combinations of Not-AND operations."),
   m("cimc_site", "Paraphrase: 'The Missing Institute' text says AI began with Aristotle and continued with Leibniz, La Mettrie, Frege, Tarski and Wittgenstein."),
   m("cimc_library", "Paraphrase: Tractatus (1921) is in the CIMC library under classical texts.")])
R("Stanisław Lem", "person", None, None,
  "Polish science fiction writer and philosopher of technology. 'Solaris' (1961) is about an alien mind humans cannot understand; 'Golem XIV' (1981) is a set of lectures given by a superhuman computer to humanity.",
  "Bach calls Lem an 'ingenious' author and 'cybernetic philosopher' and reads Golem XIV as an early picture of a large language model that outthinks scientists. He already cited Lem's Star Diaries in his thesis.",
  [m("sub_age_2026", "the ingenious Polish science fiction author and cybernetic philosopher Stanislaw Lem", True),
   m("sub_age_2026", "Paraphrase: 'Lem's Golem computer is a Large Language Model, capable of running circles around the best human scientists'."),
   m("psi_diss_2007", BIB + " (Lem 1971, The Star Diaries)."),
   m("cimc_library", "Paraphrase: Solaris (1961) is in the CIMC library under science fiction.")])
R("Developmental stage theories", "theory", "Jean Piaget; Jane Loevinger; Lawrence Kohlberg", "1954",
  "Theories that describe mental growth as a series of stages: Piaget for children's thinking, Loevinger for ego development, Kohlberg for moral reasoning.",
  "Bach names them as earlier stage models before giving his own seven 'Levels of Lucidity'. His thesis cites Piaget as a rare case of a unified theory in psychology.",
  [m("sub_lucidity_2023", "Paraphrase: mentions 'Piaget's famous four-stage model of childhood development, Jane Loevinger's nine stages of ego development, Lawrence Kohlberg's six stages of moral development'."),
   m("psi_diss_2007", "Paraphrase: 'Piaget's work (especially Piaget 1954) might be one of the notable exceptions' to psychology's preference for small microtheories.")])
R("Five-stage model of personality development", "theory", "Robert Kegan", "1982",
  "Kegan describes adult growth as five orders of mind. At each step, what a person used to be subject to (impulses, relationships, an ideology) becomes something they can look at and manage.",
  "Bach says this is the model he particularly likes and uses it as the base for his own seven levels, while not treating it as a strongly proven psychological theory.",
  [m("sub_lucidity_2023", "I particularly like Robert Kegan’s five stage model of personality development", True)],
  True)
R("Eight-circuit model of consciousness", "theory", "Timothy Leary; Robert Anton Wilson", "1977",
  "A counter-culture model that describes eight 'circuits' of the nervous system, from basic survival up to mystical states.",
  "Bach lists it, with Wilson's names for the circuits, as one of the stage models that came before his Levels of Lucidity. He gives no endorsement beyond that.",
  [m("sub_lucidity_2023", "Paraphrase: 'Timothy Leary's eight circuits, which have been adapted by the great Robert Anton Wilson'.")])
R("Ascribing Mental Qualities to Machines", "paper", "John McCarthy", "1979",
  "McCarthy argued that it is legitimate and useful to say a machine believes or wants something when that description helps predict what it does.",
  "Bach's thesis cites it where he discusses an agent that represents itself as a thing that represents.",
  [m("psi_diss_2007", "Paraphrase: cites (McCarthy 1979) for a self-representation that is intensional and not only extensional.")])
R("Parallel Distributed Processing (connectionism)", "book", "David Rumelhart, James McClelland and the PDP Research Group", "1986",
  "The two volumes that relaunched neural networks in cognitive science. Knowledge is stored as patterns of connection strengths, not as explicit rules.",
  "Bach treats connectionism and symbolic AI as two halves that a cognitive architecture must join; MicroPsi's node nets are meant to do both.",
  [m("seven_2008", "Paraphrase: reference [17] Rumelhart, McClelland and the PDP Research Group (1986)."),
   m("psi_diss_2007", "Paraphrase: many researchers abandoned symbolic systems for 'parallel distributed, entirely sub-symbolic approaches'.")])
R("Scripts, Plans, Goals and Understanding", "book", "Roger Schank, Robert Abelson", "1977",
  "Proposed that people understand everyday situations through 'scripts', stored step-by-step outlines such as what happens in a restaurant.",
  "Bach's Request Confirmation Networks are built to run script-like hierarchical plans in a neural style, joining top-down requests with bottom-up confirmation.",
  [m("recon_2015", "ReCoNs are spreading activation networks with units that contain an activation and a state", True),
   m("psi_diss_2007", BIB + " (Schank & Abelson 1977).")])
R("A Theory of Human Motivation", "paper", "Abraham Maslow", "1943",
  "Maslow's ranking of human needs, from bodily needs up to self-fulfilment.",
  "Cited in Bach's 2018 attention-learning paper next to his own MicroPsi model of motivation. How far he follows Maslow was not checked in the text.",
  [m("abl_2018", "Paraphrase: reference 7. Maslow, A.H. A theory of human motivation. Psychological Review 50 (4) 1943.")])
R("Norbert Bischof", "person", None, None,
  "German psychologist who modelled motivation, attachment and social distance as control systems.",
  "Bach names him as one of the sources Dörner's theory builds on.",
  [m("psi_diss_2007", "Paraphrase: Dörner's blueprint 'incorporates ideas of Norbert Bischof (1968, 1975, 1989, 1996), Friedhart Klix (1984, 1992), Ulrich Neisser (1967, 1976), Jens Rasmussen (1983) and many others'.")])
R("Antonio Damasio", "person", None, None,
  "Neuroscientist known for arguing that emotion and bodily feeling are needed for good reasoning ('Descartes' Error', 1994) and for a layered account of the self ('The Feeling of What Happens', 1999).",
  "Bach mentions him as an influence on Sloman's architecture; CIMC lists one of his books in its library. No direct discussion by Bach was found in the retrieved texts.",
  [m("psi_diss_2007", "Paraphrase: Sloman's Cognition and Affect architecture 'in turn owes much to Antonio Damasio'; bibliography lists Damasio 1994."),
   m("cimc_library", "Paraphrase: The Feeling of What Happens (1999) is in the CIMC library.")])
R("A Standard Model of the Mind", "paper", "John Laird, Christian Lebiere, Paul Rosenbloom", "2017",
  "A proposal for a shared baseline architecture of human-like minds that AI, cognitive science, neuroscience and robotics could all refer to.",
  "Bach's attention-learning position paper is addressed to this 'common model' effort and argues that it should include reflection, attention and learning from a record of one's own attention.",
  [m("abl_2018", "Paraphrase: reference 3. Laird, Lebiere, Rosenbloom. A Standard Model of the Mind. AI Magazine 38 (2017).")])

# ================= B. Consciousness papers 2018-2019 =================
R("Integrated Information Theory (IIT)", "theory", "Giulio Tononi; Christof Koch", "2004",
  "Says that consciousness is identical to integrated information in a physical system, measured by a quantity called Phi. On this view experience depends on the physical causal structure of the hardware, so a simulation of a brain on an ordinary computer would not be conscious.",
  "Bach rejects it. He calls his own theory functionalist 'unlike IIT' and cites Aaronson's argument that high integration is not sufficient. CIMC's whitepaper says IIT sits outside the representational framework CIMC works in.",
  [m("ctc_2018", "Unlike IIT, CTC is a functionalist model of consciousness", True),
   m("ctc_2018", "Paraphrase: Tononi 'argues that experience cannot be reduced to a functional mechanism, and hence it must be an intrinsic property of a system'."),
   m("wp_2026", "places the theory outside the representationalist framework in which CIMC operates", True),
   m("phen_2019", "Paraphrase: Tononi and Koch (2015) 'have offered five axioms', which Bach summarises before giving his own account.")])
R("Why I Am Not An Integrated Information Theorist (or, The Unconscious Expander)", "paper", "Scott Aaronson", "2015",
  "A blog essay by a computer scientist showing that simple, obviously mindless grid-like systems can score very high on IIT's measure Phi.",
  "Bach uses it as his main cited argument against IIT: integration might be necessary but cannot be sufficient for consciousness.",
  [m("ctc_2018", "Paraphrase: 'As has for instance been argued by Aaronson (2015), IIT's criterion of information integration could perhaps be necessary, but is not sufficient'.")])
R("Attention Schema Theory", "theory", "Michael Graziano; Taylor Webb", "2013",
  "Says the brain builds a simplified model of its own attention, and that this model is what we describe as awareness.",
  "Close to Bach's own view: he says treating consciousness as a model of attention was suggested by Graziano and Webb, Dennett and Drescher. CIMC names the theory as one of its starting points for architectures.",
  [m("phen_2019", "Paraphrase: 'The idea of treating consciousness as a model of attention has also been suggested in several forms by Graziano and Webb (2014), Dennett (1992), Drescher (2006) and others.'"),
   m("mch_2025", "Paraphrase: 'Michael Graziano describes consciousness as a control model of attention, and calls it the Attention Schema Theory.'"),
   m("cimc_library", "Paraphrase: Consciousness and the Social Brain (2013) is in the CIMC library.")])
R("Good and Real", "book", "Gary Drescher", "2006",
  "A computer scientist's attempt to fit consciousness, free choice and ethics into a fully mechanical, deterministic universe.",
  "Bach cites it for the idea that consciousness is a model of attention; CIMC lists it in its library.",
  [m("phen_2019", "Paraphrase: named with Graziano & Webb and Dennett as having suggested treating consciousness as a model of attention."),
   m("abl_2018", "Paraphrase: reference 11. Drescher, G. Good and Real. MIT Press (2006)."),
   m("cimc_library", "Paraphrase: Good and Real (2006) is in the CIMC library.")])
R("Solomonoff induction / Universal AI", "theory", "Ray Solomonoff; Marcus Hutter", "1964",
  "An ideal, uncomputable recipe for learning: prefer the shortest programs that reproduce everything you have observed so far. Hutter built a theory of an ideal agent on top of it.",
  "Bach uses it as his measure of a good world model and says machine-learning models of the mind approximate it. He applies it to the simulation question: the best model is the shortest one that predicts our observations.",
  [m("bachai_sim_2016", "I think that Ray Solomonoff had a good idea when he defined the limit of the quality of such a world model", True),
   m("ctc_2018", "Paraphrase: 'Machine learning models of the mind can be understood as approximating Solomonoff induction (see Hutter 2005)'.")])
R("L'Homme Machine (Man a Machine)", "book", "Julien Offray de La Mettrie", "1748",
  "An Enlightenment pamphlet arguing that humans, including their minds, are machines.",
  "Bach and CIMC claim La Mettrie as an ancestor of the computational view of mind.",
  [m("ctc_2018", "Paraphrase: mentions 'Julien Offray de LaMettrie's (1748) remark that while minds are machines, these had to be thought of as “immortal” and “transcendental”'."),
   m("cimc_site", "Paraphrase: AI 'began with Aristotle and continued with people like Leibniz, La Mettrie, Frege, Tarski, and Wittgenstein'."),
   m("cimc_library", "Paraphrase: L'Homme Machine (1748) is in the CIMC library.")])
R("Monadology (the mill argument)", "book", "Gottfried Wilhelm Leibniz", "1714",
  "Leibniz asks us to imagine a thinking machine enlarged to the size of a mill. Walking inside we would see only parts pushing each other and never a perception, so he concluded mechanism cannot explain perception.",
  "Bach quotes the mill passage in 2018 and again in the 2025 CIMC essay. His answer is that Leibniz lacked the idea of a substrate-independent machine: perception belongs to the software-level model, not to the pushing parts.",
  [m("ctc_2018", "Paraphrase: 'The absence of an understanding of substrate independent machines lead Leibniz to the rejection of mechanist philosophy', followed by the mill quotation (1714)."),
   m("mch_2025", "Paraphrase: 'already three centuries ago, in his Monadology, Gottfried Wilhelm Leibniz gives an illustration', followed by the mill quotation."),
   m("cimc_library", "Paraphrase: Leibniz's New Essays (1704) is in the CIMC library.")])
R("Consciousness as a State of Matter", "paper", "Max Tegmark", "2014",
  "A physicist's proposal to treat consciousness as a state of matter with certain information-processing properties, building on IIT.",
  "Mentioned by Bach only as support for IIT, which he rejects.",
  [m("ctc_2018", "Paraphrase: IIT 'has been championed by the neuroscientist Christof Koch and the physicist Max Tegmark (2014)'.")])
R("Christoph von der Malsburg", "person", None, None,
  "German neuroscientist and physicist. In 1981 he proposed that the brain binds features into objects through temporary correlations between neurons, and later defined consciousness as a state of high coherence among the brain's subsystems.",
  "A direct source for Bach's 'coherence' account, which he and CIMC attribute to von der Malsburg by name. He is a CIMC scientific advisor and spoke at the 2025 launch.",
  [m("mch_2025", "Christoph von der Malsburg calls this concept the coherence definition of consciousness", True),
   m("phen_2019", "Paraphrase: reference von der Malsburg, C. (1981), The correlation theory of brain function; cited for synchronization theory of binding."),
   m("cimc_team", "Paraphrase: listed as Scientific Advisor (Frankfurt Institute for Advanced Studies)."),
   m("wp_2026", "Paraphrase: 'The neuroscientist Christoph von der Malsburg calls this the coherence definition of consciousness (von der Malsburg, 1999).'")])
R("Illusionism", "theory", "Keith Frankish; Daniel Dennett; Susan Blackmore", "2016",
  "The view that phenomenal consciousness, as philosophers usually describe it, does not exist; what exists is the brain's mistaken impression that it has such inner qualities.",
  "Bach lists it as one of six possible stances. His own position is close but worded differently: experience is real inside the brain's simulation, and it is the self that is not real.",
  [m("phen_2019", "Paraphrase: option 6, 'Phenomenal consciousness does not exist and is an illusion (Frankish 2016, Dennett 1992, 2016).'"),
   m("phen_2019", "Our phenomenal experience is very real to ourselves, but our selves are not real.", True),
   m("mch_2025", "Paraphrase: 'This position is sometimes called illusionism and ascribed to Daniel Dennett, with the term largely being associated with Keith Frankish.' A separate footnote cites Dennett and Susan Blackmore on Nagel's bat essay.")])
R("Mysterianism", "theory", "Colin McGinn; Noam Chomsky", "1999",
  "The view that human minds are not built to solve the mind-body problem, so consciousness will stay unexplained.",
  "Bach lists it as one of the possible stances and does not adopt it.",
  [m("phen_2019", "Paraphrase: option 4, 'Consciousness can in principle not be explained. This is the mysterianist position, which has been argued by Colin McGinn (1999), and more recently also by Noam Chomsky.'")])
R("The Emperor's New Mind", "book", "Roger Penrose", "1989",
  "Penrose argues from Gödel's theorem that human mathematicians can see truths no computer program can prove, so the mind must use non-computable physics, possibly quantum gravity.",
  "Bach disagrees. In his reading Gödel shows a limit of classical mathematics, not a power of human minds that computers lack, and for epistemological reasons our models have to be computational.",
  [m("phen_2019", "Paraphrase: 'This is the position of Roger Penrose', against which Bach argues that we can only make finitely resolved, local observations and must describe our models computationally."),
   m("mch_2025", "Paraphrase: 'others (for example Roger Penrose) claim that human minds can construct mathematical objects that exceed the ability of computers'."),
   m("rutt87", "Paraphrase: Bach criticises Penrose's reading of Gödel in the section on Penrose."),
   m("psi_diss_2007", BIB + " (Penrose 1989, 1997).")])
R("The binding problem and neural synchrony", "theory", "Anne Treisman & Garry Gelade; Peter Milner; Francis Crick & Christof Koch", "1980",
  "The question of how the brain joins separately processed features such as colour, shape and motion into one perceived object. Proposed answers include an attention-driven integration step and the synchronised firing of the neurons involved.",
  "Bach's 2019 paper turns the question around: consciousness is tied to the 'perceptual binding state', the moment-to-moment unified model that attention builds.",
  [m("phen_2019", "Paraphrase: 'In neuroscience, a similar approach is found in feature integration theory (Treisman and Gelade 1980). Another way of achieving binding is called synchronization theory (Milner 1974, von der Malsburg 1981)'."),
   m("phen_2019", "Paraphrase: a nonlocal version of synchronization theory 'is advanced by Crick and Koch (1990)'.")])
R("Libet's readiness-potential experiments", "paper", "Benjamin Libet et al.", "1983",
  "Experiments in which brain activity leading to a voluntary movement began a fraction of a second before people reported deciding to move.",
  "Bach uses the timing data to argue that our experienced 'now' is a constructed story assembled after the fact.",
  [m("phen_2019", "Paraphrase: 'The initiation of a deliberate act is not instantaneous, but will require at least several hundred milliseconds of cortical activity (Libet 1983)'.")])

# ================= C. Machine Consciousness Hypothesis essay (2025) =================
R("De Anima (On the Soul)", "book", "Aristotle", "-350",
  "Aristotle's treatise on what makes living things alive. The soul is the 'form' of a living body, its organisation and capacities, with plant, animal and human levels.",
  "Bach reads Aristotle as an animist in a respectable sense: the soul is the causal structure, or software, of the body. CIMC names Aristotle as the start of the AI tradition, and Bach's 2015 blog post calls his own god concept 'Aristotelian'.",
  [m("mch_2025", "Aristotle describes the soul, spirit, or psyche, as a form (causal structure)", True),
   m("cimc_library", "Paraphrase: De Anima is the first classical text in the CIMC library."),
   m("bachai_fourgods_2015", "After I found God for myself (not a religious one, but an Aristotelian one)", True),
   m("agi25", "Paraphrase: Bach describes a vegetative layer that plants have, an animal layer above it, and a human soul on top (Aristotle's name was not checked in this passage).")])
R("Animism", "tradition", None, None,
  "The widespread traditional view that living things, and sometimes places and objects, are animated by spirits that act and experience.",
  "Bach adopts it in updated form as 'cyber-animism': spirits are self-organising software agents running on living matter. He says he takes it as a metaphysical perspective and not as superstition.",
  [m("mch_2025", "the spirits of the animist worldview are not superstitions or mere analogies to computer software", True),
   m("levin_2024", "Paraphrase: these thoughts 'led me to adopting animism as a useful metaphysical perspective not as some kind of religious superstition'."),
   m("mlst_2024", "Paraphrase: animism is not only found in rural Japan; it existed in Europe before Christianity and only stopped with the Enlightenment.")])
R("Structure and Interpretation of Computer Programs", "book", "Harold Abelson, Gerald Jay Sussman", "1996",
  "The classic MIT programming textbook. Its opening describes running programs as spirits that live in the computer and are conjured by the programmer's spells.",
  "Bach and Sorensen quote this opening as evidence that computer scientists have rediscovered the old idea of spirits.",
  [m("mch_2025", "Computational processes are abstract beings that inhabit computers.", True)])
R("'It from bit'", "concept", "John Archibald Wheeler", "1990",
  "Wheeler's slogan for the idea that information is more basic than matter and energy: every physical 'it' comes from yes-or-no answers, 'bits'.",
  "Cited by Bach and Sorensen in support of the view that physics studies how the universe processes information.",
  [m("mch_2025", "Paraphrase: the idea that information, not matter and energy, is fundamental 'has led John Archibald Wheeler to coin the slogan “it from bit”'.")])
R("Gödel's incompleteness theorems", "theory", "Kurt Gödel", "1931",
  "Gödel proved that any consistent formal system strong enough for arithmetic contains true statements it cannot prove, and cannot prove its own consistency.",
  "Bach's reading is unusual. He takes the result to show that mathematics which cannot be computed (with real infinities) does not work, and that only constructive, computable mathematics is real. This is his own interpretation, not the standard one among logicians.",
  [m("mch_2025", "A way to interpret Gödel's proof is that languages that cannot be automatically evaluated inevitably contain unresolvable paradoxes", True),
   m("rutt87", "classical mathematics that contains infinities cannot be implemented, cannot be real", True)])
R("Lambda calculus, combinators and the Church-Turing thesis", "theory", "Alonzo Church; Moses Schönfinkel; Alan Turing", "1936",
  "Different formal definitions of what it means to compute (Turing's machines, Church's lambda calculus, Schönfinkel's combinators) turned out to be equivalent. The Church-Turing thesis says they capture everything that can be computed at all.",
  "This equivalence is the base of Bach's computationalism: any system that can be described precisely can be implemented on any universal computer. He calls computation the 20th century's most important idea.",
  [m("edge_2016", "Computationalism is the new mechanism", True),
   m("edge_2016", "Paraphrase: an unbounded state-transition system 'becomes a Turing Machine, or a Lambda Calculus, or a Post machine, or one of the many other, mutually equivalent formalisms'."),
   m("mch_2025", "Paraphrase: cites Church 1936, Schönfinkel 1924 and the Turing machine as equivalent models of computation.")])
R("Principia Mathematica", "book", "Bertrand Russell, Alfred North Whitehead", "1910",
  "A huge attempt to derive all of mathematics from pure logic. Gödel's theorem was aimed at systems of this kind.",
  "Cited in the CIMC essay as part of the story of how the foundations of mathematics led to the idea of computation.",
  [m("mch_2025", "Paraphrase: Russell & Whitehead's Principia (1910-13) is cited in the section on the foundations of computation.")])
R("Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components", "paper", "John von Neumann", "1956",
  "Showed how to build reliable computation out of noisy, failure-prone parts by using redundancy.",
  "Bach and Sorensen cite it to say that a computer does not need a deterministic substrate, which matters for brains made of noisy cells.",
  [m("mch_2025", "Paraphrase: 'as John von Neumann and others note, determinism can be achieved on indeterministic (noisy, probabilistic) substrates'.")])
R("What Is It Like to Be a Bat?", "paper", "Thomas Nagel", "1974",
  "Nagel argues that an organism is conscious if there is something it is like to be that organism, and that objective science seems to leave this point of view out.",
  "Cited by Bach and Sorensen as an earlier statement of the hard problem.",
  [m("mch_2025", "Paraphrase: the issue 'has been described by many others, such as Thomas Nagel in his famous essay “What Is It Like to Be a Bat?”'.")])
R("The explanatory gap", "concept", "Joseph Levine", "1983",
  "Levine's name for the gap between any physical or functional description of the brain and an explanation of why it feels the way it does.",
  "Cited in the CIMC essay as another name for the problem the machine consciousness hypothesis is meant to close.",
  [m("mch_2025", "Paraphrase: Joseph Levine in 1983 'calls it the “explanatory gap”'.")])
R("Higher-order thought theory", "theory", "David Rosenthal", "2005",
  "Says a mental state is conscious when the mind has a higher-order thought about being in that state.",
  "Bach and Sorensen separate their view from it: for them consciousness is second-order perception, not a thought that needs concepts. The whitepaper notes the family resemblance.",
  [m("mch_2025", "Paraphrase: awareness as second-order perception 'is distinguished from the notion of consciousness as “higher-order thought” (HOT), which was introduced by David Rosenthal'."),
   m("wp_2026", "Paraphrase: 'Higher-Order Theories (Rosenthal, 2005) propose that a mental state is conscious when it is the object of a higher-order representation.'")])
R("Adaptive Resonance Theory", "theory", "Stephen Grossberg", "1976",
  "Grossberg's theory that the brain learns stably by matching top-down expectations against bottom-up input; a 'resonance' between the two is what becomes conscious.",
  "The CIMC essay says Grossberg came up with a model similar to the attention-control account; his 2021 book is in the CIMC library.",
  [m("mch_2025", "Paraphrase: 'The neuroscientist Stephen Grossberg came up with a similar model in the context of' his Adaptive Resonance Theory."),
   m("cimc_library", "Paraphrase: Conscious Mind, Resonant Brain (2021) is in the CIMC library.")])
R("Biological naturalism about consciousness", "theory", "Anil Seth", "2025",
  "The position that consciousness depends on being a living, self-maintaining organism, so computation alone would not produce it.",
  "Bach and Sorensen give Seth as their example of 'essentialism', the view they oppose with functionalism.",
  [m("mch_2025", "Paraphrase: essentialists may see consciousness as dependent on an intrinsic property of its substrate, 'e.g. its biological nature, as for instance argued by the philosopher Anil Seth'.")])
R("Zoom In: An Introduction to Circuits (universality hypothesis)", "paper", "Chris Olah et al.", "2020",
  "An interpretability paper claiming that different neural networks trained on similar data tend to learn similar features and circuits.",
  "Cited in the CIMC essay for the 'Universality Hypothesis'. The exact role in the argument was not re-read; treat the take as incomplete.",
  [m("mch_2025", "Paraphrase: Olah et al. 2020, 'Zoom In', is cited for the Universality Hypothesis.")])
R("ELIZA", "paper", "Joseph Weizenbaum", "1966",
  "An early chat program that imitated a therapist using simple pattern matching. Many users felt understood by it.",
  "Bach and Sorensen use it to show that people are easily fooled by surface behaviour, which is one reason they say behaviour tests cannot settle consciousness.",
  [m("mch_2025", "Paraphrase: among criticisms of the Turing Test is 'Joseph Weizenbaum's discovery that non-expert humans talking to computer programs can often be fooled by superficial appearances of intelligent behavior'.")])
R("Computing Machinery and Intelligence (the Turing Test)", "paper", "Alan Turing", "1950",
  "Turing proposed replacing the question 'can machines think?' with a test: can a machine hold a conversation that a judge cannot tell from a human's?",
  "Bach and Sorensen argue there can be no such test for consciousness, because consciousness is a way of producing behaviour and not a visible behaviour.",
  [m("mch_2025", "Consciousness is by its nature not an externally visible performance, but a particular way to achieve a performance", True)])
R("Best-effort computing", "concept", "Dave Ackley", None,
  "Ackley's research programme on computers that keep working when their parts are unreliable, in the manner of living tissue, instead of assuming perfect hardware.",
  "Mentioned in a footnote of the CIMC essay as a way to recreate how biological control copes with an indeterministic substrate.",
  [m("mch_2025", "Paraphrase: 'Dave Ackley is exploring the concept of best effort computing, which aims to recreate the ability of biological control structures to dynamically compensate for indeterministic substrates.'")])
R("Genesis 1", "book", None, None,
  "The opening chapter of the Hebrew Bible, usually read as an account of the creation of the physical world in six days.",
  "Bach reads it as an old description of how consciousness boots up a mind: a spirit hovers over the substrate, separates world-model from ideas, makes light and dark, and creates the self last. He names his 'Genesis' idea, consciousness before self, after it.",
  [m("c37_2023", "the earliest formulation of that theory is what I found in Genesis 1", True),
   m("lex392", "I suspect that it’s there in plain sight in Genesis 1", True),
   m("mch_2025", "We call this idea the Genesis Hypothesis", True)])
R("Phenomenology and embodied / enactive cognition", "tradition", "Martin Heidegger; Maurice Merleau-Ponty; Francisco Varela, Evan Thompson, Eleanor Rosch; Alva Noë; Shaun Gallagher", "1927",
  "A line of philosophy that starts from lived experience and holds that mind is constituted by a body acting in a world, not by inner representations alone.",
  "Bach has opposed enactivism since 2011 (talks titled 'Enactivism Considered Harmful' and 'No Room for the Mind'). CIMC's whitepaper is more polite and says it is sympathetic to part of the claim, but keeps a representational, computational view.",
  [m("cv_2023", "Paraphrase: CV lists Bach (2011) 'No Room for the Mind: Enactivism in Artificial Intelligence' and Bach (2011) 'Enactivism Considered Harmful'."),
   m("wp_2026", "Paraphrase: 'Enactivist and embodied approaches (Thompson, 2007; Varela et al., 1991; Noë, 2004) emphasize that consciousness is constituted by the organism's sensorimotor engagement with its environment'."),
   m("mch_2025", "Paraphrase: Heidegger 1927, Merleau-Ponty 1945, Gallagher 2005 and Noë 2004 are cited.")])

# ================= D. CIMC whitepaper and site =================
R("Critique of Pure Reason", "book", "Immanuel Kant", "1781",
  "Kant asks what the mind must supply for experience to be possible at all. His answer is that space, time and basic concepts such as cause are forms the mind brings to experience, so we know the world as it appears to us.",
  "CIMC has a stated project to connect the Critique to 20th-century computational philosophy, and its 'Prime Hypostasis' note starts from Kant. This is the work of Bach's colleagues Hildebrandt-Harangozó and Sorensen; no direct quotation of Bach on Kant was retrieved here.",
  [m("wp_2026", "One current project is on connecting the Critique of Pure Reason to insights from computational philosophy from the twentieth century.", True),
   m("prime_2026", "Paraphrase: opens with Kant's closing section of the Prolegomena on putting metaphysics on a sound foundation."),
   m("cimc_library", "Paraphrase: Critique of Pure Reason (1781) is in the CIMC library.")])
R("Free Energy Principle", "theory", "Karl Friston", "2010",
  "Friston's proposal that brains, and living systems in general, stay in existence by minimising surprise, which amounts to continually improving a model of their world and acting to make predictions come true.",
  "CIMC says its coherence-maximising account 'connects naturally' to Friston's principle and that working out the formal link is an active interest. Friston is a CIMC scientific advisor.",
  [m("wp_2026", "It connects naturally to Karl Friston’s Free Energy Principle", True),
   m("cimc_team", "Paraphrase: Karl Friston (University College London) is listed as Scientific Advisor.")])
R("Predictive processing", "theory", "Andy Clark; Jakob Hohwy", "2013",
  "The view that the brain is a prediction machine that constantly guesses its sensory input and corrects itself using the errors.",
  "The whitepaper presents it as a description of how brains maintain models of reality, which CIMC's account builds on.",
  [m("wp_2026", "Paraphrase: 'Predictive Processing frameworks (Clark, 2016; Hohwy, 2013) characterize the computational process by which brains maintain and update models of reality through continuous prediction and error correction'.")])
R("Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", "paper", "Patrick Butlin, Robert Long, et al.", "2023",
  "A multi-author report that turns leading scientific theories of consciousness into a checklist of 'indicator properties' and checks current AI systems against it. It concluded that no current system was a strong candidate.",
  "Listed in the CIMC library and whitepaper references. How CIMC positions itself against the checklist approach was not re-read.",
  [m("cimc_library", "Paraphrase: listed under publications (arXiv 2308.08708)."),
   m("wp_2026", "Paraphrase: in the reference list as Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., et al.")])
R("Artificial Suffering: An Argument for a Global Moratorium on Synthetic Phenomenology", "paper", "Thomas Metzinger", "2021",
  "Metzinger argues that we should not risk creating artificial beings that can suffer, and calls for a pause on research that aims at or risks machine consciousness.",
  "CIMC's whitepaper takes the argument seriously but does not accept it. It says such abstention is not morally inevitable and argues for studying the question openly.",
  [m("wp_2026", "Paraphrase: the risk of suffering 'leads some philosophers to call for abstaining from research' (Metzinger, 2021); 'Temporary AI antinatalism is by no means morally inevitable'.")])
R("AI existential-risk literature", "tradition", "Nick Bostrom; Eliezer Yudkowsky & Nate Soares; Roman Yampolskiy", "2014",
  "Books arguing that superhuman AI could escape human control and that this could be catastrophic.",
  "The whitepaper cites these authors for the claim that loss of human agency may be almost inevitable, and draws the conclusion that the possibilities should be studied in controlled settings. Bach's own 2023 essay argues that AI cannot simply be 'aligned to human values' and that alignment would have to come from shared purpose.",
  [m("wp_2026", "Paraphrase: 'Some thinkers argue that loss of human agency to AI is almost inevitable in the long run' (Bostrom, 2014; Yudkowsky & Soares, 2025; Yampolskiy, 2024)."),
   m("sub_xrisk_2023", "Thus, we cannot hope to “align AI to human values”.", True)])
R("Taking AI Welfare Seriously", "paper", "Robert Long, Jeff Sebo, et al.", "2024",
  "A report arguing that there is a realistic chance some AI systems will soon be conscious or agents with interests, so AI companies should start preparing welfare policies.",
  "In the whitepaper's reference list; Long spoke at the CIMC-organised AAAI symposium. The exact use in the text was not re-read.",
  [m("wp_2026", "Paraphrase: reference list entry Long, R., Sebo, J., et al. (2024). Taking AI Welfare Seriously. arXiv:2411.00986.")])
R("The Abstraction Fallacy", "paper", "Alexander Lerchner", "2026",
  "A paper arguing against computational functionalism about phenomenal consciousness. Only CIMC's description of it was seen, not the paper itself.",
  "CIMC researchers Sorensen and Hildebrandt-Harangozó wrote a reply, 'Against intrinsic properties', saying that many of its arguments are not valid. Bach is not an author of the reply.",
  [m("against_2026", "Paraphrase: 'Many people keep referencing Alexander Lerchner's “The Abstraction Fallacy” (Lerchner, 2026) as a set of valid arguments against the notion of computational functionalism'.")])
R("Stephen Wolfram", "person", None, None,
  "Physicist and founder of Wolfram Research. 'A New Kind of Science' (2002) argues that simple programs underlie nature; his 2023 essay 'Observer Theory' asks how the kind of observer we are shapes the laws we find.",
  "Bach cited A New Kind of Science in his thesis. CIMC's whitepaper cites it for 'epistemological computationalism', lists Observer Theory in its library, and has Wolfram as a scientific advisor who held the launch-week conversation with Bach.",
  [m("wp_2026", "Paraphrase: 'Epistemological computationalism (Wolfram, 2002) (Margolus, 2003) denies strong physicalism in favor of a universal primacy of information'."),
   m("cimc_team", "Paraphrase: Stephen Wolfram (Wolfram Research) is listed as Scientific Advisor."),
   m("cs_launch_2025", "Paraphrase: launch week included a salon at the Internet Archive, 'What if we had bigger brains?', with Stephen Wolfram and Joscha Bach."),
   m("psi_diss_2007", BIB + " (Wolfram 2002).")])
R("Michael Levin", "person", None, None,
  "Biologist at Tufts University who studies how groups of cells store and pursue anatomical goals using bioelectric signals, and who argues that intelligence comes in many unfamiliar forms.",
  "He spoke at the CIMC launch and at MC0001. The whitepaper thanks him as an informal supporter who cannot hold a formal advisor role. Bach's cyber-animism talks treat cell collectives as running 'software' in a way close to Levin's themes.",
  [m("cs_launch_2025", "Paraphrase: launch programme included Michael Levin among the speakers."),
   m("wp_2026", "Paraphrase: Appendix A acknowledges Michael Levin as an informal supporter who is contractually obliged by his institution to refrain from formal advisor roles.")])
R("Neural cellular automata", "concept", None, None,
  "Grids of identical small neural networks that only talk to their neighbours and yet grow and repair global patterns. They are a simple model of self-organisation.",
  "CIMC uses them as the main testbed for its 'self-organization and multi-agent systems' research direction and funds several projects built on them.",
  [m("cimc_site", "Paraphrase: the self-organization research direction names Neural Cellular Automata."),
   m("cimc_projects", "Paraphrase: grantee projects include 'Self-Organizing Generative Perception' (Aleksandr Groznykh) using NCA.")])
R("Autocatalytic networks (RAF theory) and autopoiesis", "theory", "Stuart Kauffman; Wim Hordijk & Mike Steel; Humberto Maturana & Francisco Varela", "1986",
  "Models of how a set of parts can come to produce and maintain itself as a whole, first used to explain the origin of life. Autopoiesis is the related idea of a system that continually makes its own components.",
  "In two co-authored papers with Liane Gabora (first author), Bach applies this framework to ask how an AI could have a self at the level of its worldview, though not at the level of a body.",
  [m("gabora_bach_2023", "We discuss the feasibility of an AI with creative agency and self-hood at the second (cognitive) level, but not the first (somatic) level.", True)])

# ================= E. CIMC library: books and fiction =================
R("I Am a Strange Loop / The Mind's I", "book", "Douglas Hofstadter (with Daniel Dennett for The Mind's I)", "2007",
  "Hofstadter argues that the 'I' is a pattern that arises when a system's model of the world loops back to include itself.",
  "Both books are in the CIMC library, and the whitepaper names Hofstadter with Dennett and Graziano. Bach's thesis cites Hofstadter 1995.",
  [m("cimc_library", "Paraphrase: I Am a Strange Loop (2007) and The Mind's I (1981) are listed under modern texts."),
   m("psi_diss_2007", BIB + " (Hofstadter 1995).")])
R("Meditations on First Philosophy", "book", "René Descartes", "1641",
  "Descartes doubts everything he can and concludes that he exists as a thinking thing, distinct from his body.",
  "Listed in the CIMC library; the CIMC essay names Descartes among the early mechanists.",
  [m("cimc_library", "Paraphrase: Meditations (1641) is listed under classical texts."),
   m("mch_2025", "Paraphrase: names 'the mechanist philosophers of the early Enlightenment, such as Descartes, Spinoza, Leibniz, and LaMettrie'.")])
R("The Principles of Psychology", "book", "William James", "1890",
  "The founding textbook of American psychology, known for its descriptions of the stream of consciousness, attention and the self.",
  "Listed in the CIMC library. The CIMC essay names James, with Freud, Jung, Piaget and Leary, as someone who implicitly used the idea of a mind made of parts.",
  [m("cimc_library", "Paraphrase: Principles of Psychology (1890) is listed under classical texts."),
   m("mch_2025", "Paraphrase: the compositional psyche 'has been implicitly used by William James, Sigmund Freud, Carl Gustav Jung, Jean Piaget, Timothy Leary and many others'.")])
R("The Doors of Perception", "book", "Aldous Huxley", "1954",
  "Huxley's report of taking mescaline, in which he suggests the brain normally filters a much wider field of awareness.",
  "Listed in the CIMC library under classical texts. No comment by Bach was retrieved.",
  [m("cimc_library", "Paraphrase: Doors of Perception (1954) is listed under classical texts.")])
R("Metazoa", "book", "Peter Godfrey-Smith", "2020",
  "A philosopher-diver traces how experience may have arisen step by step in the evolution of animal bodies and nervous systems.",
  "Listed in the CIMC library under modern texts. No comment by Bach was retrieved.",
  [m("cimc_library", "Paraphrase: Metazoa (2020) is listed under modern texts.")])
R("Observer Theory", "paper", "Stephen Wolfram", "2023",
  "An essay asking what it means to be an observer in a computational universe, and how an observer's limits determine the physical laws it perceives.",
  "Listed in the CIMC library under publications.",
  [m("cimc_library", "Paraphrase: Wolfram, Observer Theory (2023) is listed under publications.")])
R("Permutation City, Diaspora and 'Closer'", "fiction", "Greg Egan", "1994",
  "Hard science fiction about minds that run as software: copies of people living in simulations, citizens who are programs, and what personal identity means when a mind can be copied or merged.",
  "Three Egan works are in the CIMC library's science fiction shelf, the largest share for any author there.",
  [m("cimc_library", "Paraphrase: Permutation City (1994), Closer (1992) and Diaspora (1997) are listed under sci-fi.")])
R("The Lifecycle of Software Objects / Exhalation", "fiction", "Ted Chiang", "2010",
  "Stories about raising artificial minds over many years like children, and about a mechanical being who dissects his own brain to understand thought.",
  "Listed in the CIMC library under science fiction.",
  [m("cimc_library", "Paraphrase: Lifecycle of Software Objects (2010) and Exhalation (2019) are listed under sci-fi.")])
R("Blindsight / Echopraxia", "fiction", "Peter Watts", "2006",
  "Novels built on the idea that high intelligence might not need consciousness at all, and that consciousness could even be a handicap.",
  "Listed in the CIMC library under science fiction.",
  [m("cimc_library", "Paraphrase: Blindsight (2006) and Echopraxia (2014) are listed under sci-fi.")])
R("He Who Shapes", "fiction", "Roger Zelazny", "1965",
  "A novella about a therapist who enters and shapes his patients' dreams with a machine.",
  "Listed in the CIMC library under science fiction.",
  [m("cimc_library", "Paraphrase: He Who Shapes (1965) is listed under sci-fi.")])

# ================= F. Essays and blog posts =================
R("The simulation argument", "concept", "Nick Bostrom (popularised by Elon Musk)", "2003",
  "The argument that if advanced civilisations run many simulated worlds, we are more likely to be in a simulation than in base reality.",
  "Bach separates several meanings of 'simulation'. He accepts that the universe is computational but finds it implausible that it was built for our benefit or is mostly 'smoke and mirrors'. His post mentions Musk and does not name Bostrom.",
  [m("bachai_sim_2016", "Elon Musk recently suggested that we likely do not live in a base reality, but in a simulation.", True)])
R("1 Corinthians 13", "book", "Paul the Apostle", None,
  "A New Testament passage saying that knowledge, prophecy and sacrifice are worth nothing without love.",
  "Bach quotes it in his 2026 text to say that intelligence without love, 'hollow agency', leads into peril, and that AI should be built to find shared purposes with us.",
  [m("sub_age_2026", "and have not love, I am nothing", True),
   m("sub_age_2026", "We will have to build AI systems that can extend our wisdom, agents that find shared purposes with us.", True)])
