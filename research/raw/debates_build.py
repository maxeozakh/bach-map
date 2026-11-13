# Builds ../debates.json and checks every verbatim quote against the saved raw transcript.
import json, re, os, sys, html

RAW = os.path.dirname(os.path.abspath(__file__)) + "/"
OUT = os.path.join(RAW, "..", "debates.json")
YT = "https://www.youtube.com/watch?v="

# id: (title, date, video id, raw file stem or None, note)
SRC = {
 "toe_solo_2020": ("Joscha Bach: Time, Simulation Hypothesis, Existence (Theories of Everything with Curt Jaimungal)", "2020-10-06", "3MNBxfrmfmI", "debates_toe_solo_3MNBxfrmfmI.txt"),
 "toe_vervaeke_2022": ("Joscha Bach Λ John Vervaeke: Mind, Idealism, Computation (Theories of Everything)", "2022-01-17", "rK7ux_JhHM4", "debates_toe_vervaeke_rK7ux_JhHM4.txt"),
 "toe_hoffman_2022": ("Donald Hoffman Λ Joscha Bach: Consciousness, Gödel, Reality (Theories of Everything)", "2022-02-07", "bhSlYfVtgww", "debates_toe_hoffman_bhSlYfVtgww.txt"),
 "toe_levin_2022": ("Michael Levin Λ Joscha Bach: Collective Intelligence (Theories of Everything)", "2022-11-09", "kgMFnfB5E_A", "debates_toe_levin_kgMFnfB5E_A.txt"),
 "mlst_unplugged_2022": ("#82 - Dr. JOSCHA BACH - Digital Physics, DL and Consciousness [UNPLUGGED] (Machine Learning Street Talk)", "2022-11-27", "LgwjcqhkOA4", "debates_mlst_82_unplugged_LgwjcqhkOA4.txt"),
 "mlst_leahy_2023": ("Joscha Bach and Connor Leahy [HQ VERSION] (Machine Learning Street Talk)", "2023-06-19", "Z02Obj8j6FQ", "debates_mlst_leahy_Z02Obj8j6FQ.txt"),
 "toe_goertzel_2023": ("Joscha Bach Λ Ben Goertzel: Conscious Ai, LLMs, AGI (Theories of Everything)", "2023-10-17", "xw7omaQ8SgA", "debates_toe_goertzel_xw7omaQ8SgA.txt"),
 "toe_friston_2023": ("Joscha Bach Λ Karl Friston: Ai, Death, Self, God, Consciousness (Theories of Everything)", "2023-12-12", "CcQMYNi9a2w", "debates_toe_friston_CcQMYNi9a2w.txt"),
 "iai_quantum_2024": ("The quantum hoax | Dominic Walliman, Joscha Bach, Ruth Oulton (Institute of Art and Ideas, public excerpt)", "2024-02-10", "RLBZEfJAN44", "debates_iai_quantum_hoax_RLBZEfJAN44.txt"),
 "iai_enigma_2024": ("Can we crack the AI enigma | Joscha Bach, Mazviita Chirimuuta, Cory Doctorow (Institute of Art and Ideas, public excerpt)", "2024-06-01", "civc01IZCcY", "debates_iai_ai_enigma_civc01IZCcY.txt"),
 "levin_fields_2024": ("Conversation between Joscha Bach, Chris Fields, and Michael Levin (Michael Levin's Academic Content)", "2024-06-05", "knADtWMGxmw", "debates_levin_fields_bach_knADtWMGxmw.txt"),
 "robinson_2024": ("Joscha Bach: Consciousness, Artificial Intelligence, and the Threat of AI Apocalypse (Robinson Erhardt / Robinson's Podcast)", "2024-08-05", "XcNlv9gp20o", "debates_robinson_erhardt_XcNlv9gp20o.txt"),
 "mlst_software_2024": ("\"We Are All Software\" - Joscha Bach (Machine Learning Street Talk)", "2024-08-21", "34VOI_oo-qM", "debates_mlst_we_are_all_software_34VOI_oo-qM.txt"),
 "iai_radical_2024": ("A radical theory of consciousness | AI researcher Joscha Bach (Institute of Art and Ideas, public excerpt)", "2024-10-18", "pkhuDqK1_MU", "debates_iai_radical_theory_pkhuDqK1_MU.txt"),
 "mlst_thoughts_2024": ("Joscha Bach - Why Your Thoughts Aren't Yours. (Machine Learning Street Talk)", "2024-10-20", "3MkJEGE9GRY", "debates_mlst_2024_thoughts_3MkJEGE9GRY.txt"),
 "iai_yudkowsky_2024": ("Should we shut down AI? | Eliezer Yudkowsky + Joscha Bach Complete Debate (IAI debate with Scott Aaronson and Liv Boeree; third-party re-upload on channel 'Metamorph Ariadne', date is the re-upload date)", "2024-12-18", "YsgiNQKscyY", "debates_iai_yudkowsky_debate_YsgiNQKscyY.txt"),
 "iai_spirit_2025": ("Why consciousness is software, and software is spirit | Joscha Bach | FULL INTERVIEW (Institute of Art and Ideas)", "2025-03-27", "E361FZ_50oo", "debates_iai_software_spirit_E361FZ_50oo.txt"),
 "agihouse_nixon_2025": ("Joscha Bach vs. Jeremy Nixon: Is Consciousness Required for AGI? (AGI House)", "2025-04-05", "rFI2wcmst4I", "debates_agihouse_nixon_rFI2wcmst4I.txt"),
 "iai_dawn_2025": ("This is the dawn of machine consciousness | Joscha Bach FULL INTERVIEW (Institute of Art and Ideas)", "2025-05-06", "Y1QOf6HEbHQ", "debates_iai_dawn_machine_consciousness_Y1QOf6HEbHQ.txt"),
 "cimc_wolfram_2025": ("Salon with Stephen Wolfram × Joscha Bach_What if we had bigger brains. (California Institute for Machine Consciousness)", "2025-06-17", "-G1SdsRXL7k", "debates_cimc_wolfram_salon_-G1SdsRXL7k.txt"),
 "sandberg_2026": ("Joscha Bach & Anders Sandberg - AI, Consciousness and the Cyborg Leviathan (Science, Technology & the Future)", "2026-03-11", "IzbtOzXMLOo", "debates_sandberg_bach_IzbtOzXMLOo.txt"),
 "keating_2026": ("Joscha Bach: \"You Are Not Who You Think You Are!\" (Dr Brian Keating, Into the Impossible)", "2026-05-15", "7bqdPHLIY8w", "debates_keating_2026_not_who_you_think_7bqdPHLIY8w.txt"),
 "cimc_davidad_2026": ("Machine Consciousness & AI Awakening - Davidad and Joscha Bach (California Institute for Machine Consciousness)", "2026-07-13", "0-nI_MpiuSE", "debates_cimc_davidad_0-nI_MpiuSE.txt"),
 "cimc_panel_2026": ("The Panel Where Everyone Disagrees About Saving the World - Joscha Bach, David Pearce, Andrew Critch (California Institute for Machine Consciousness)", "2026-08-03", "A3jRaGMLhNc", "debates_cimc_panel_pearce_critch_A3jRaGMLhNc.txt"),
 "keating_yampolskiy_2026": ("Joscha Bach PUSHES Roman Yampolskiy: Only ASI Can Save Us! (Dr Brian Keating)", "2026-10-09", "ayW7SDyAjZo", "debates_keating_yampolskiy_ayW7SDyAjZo.txt"),
 "roundtable_2026": ("AI Expert Roundtable: ''We Can't Stop AI Anymore, So How Do We Protect Our Future?'' (The Beyond Tomorrow Podcast with Julian Issa; Bach, Ben Goertzel and others)", "2026-10-30", "NXITvkHIV9o", "debates_roundtable_beyond_tomorrow_NXITvkHIV9o.txt"),
 "mlst_consciousness_2026": ("Why Consciousness Might Not Be Hard At All (Joscha Bach) (Machine Learning Street Talk)", "2026-11-01", "yW_ngvMFlYs", "debates_mlst_2026_consciousness_not_hard_yW_ngvMFlYs.txt"),
 "ami_2026": ("The Spirit in the Machine | feat. Joscha Bach (AM I? podcast; YouTube also shows the alternate titles 'The Quest to Build Conscious AI' and 'Deepfaking the Human Mind')", "2026-11-12", "SGZ784mBuU0", "debates_ami_2026_SGZ784mBuU0.txt"),
 # located but transcript NOT obtained (YouTube started IP-blocking caption requests)
 "iccs_sentience_2025": ("Sentience Beyond Biology — Debate w/Dmitry Volkov, Joscha Bach, Matthew MacDougall, Murray Shanahan (International Center for Consciousness Studies)", "2025-08-13", "GjK0Nn9gM0k", None),
 "insideview_2023": ("Joscha Bach—Is AI Risk Real? (The Inside View)", "2023", "YeXHQts3xYM", None),
 "students_2026": ("Joscha Bach — Consciousness Builds the Mind (The Students)", "2026", "-0QpYMuu9Ow", None),
 "deepsleep_2026": ("A conversation with Joscha Bach (Deep Sleep War Stories)", "2026", "Hio4bKOR3YA", None),
}

REFS = []
def R(name, kind, author, year, tldr, take, mentions, verified=True, notes=None):
    d = {"name": name, "kind": kind, "author": author, "year": year, "tldr": tldr, "bach_take": take,
         "mentions": [{"source_id": s, "quote_or_paraphrase": q, "is_verbatim": v} for (s, q, v) in mentions],
         "verified": verified}
    if notes: d["notes"] = notes
    REFS.append(d)

V, P = True, False

# ───────────────────────── debate partners and their positions ─────────────────────────
R("Donald Hoffman", "person", None, 2015,
  "American cognitive scientist who argues that evolution shaped our senses to hide reality rather than reveal it. He goes further and proposes that space, time and matter are not fundamental; networks of 'conscious agents' are, and physics should be derived from them.",
  "Bach accepts the first half (the world looks nothing like our experience of it) and rejects the second: he thinks Hoffman misunderstands what a computer is and told him in the debate that he was 'outing himself' as a mysterian.",
  [("toe_solo_2020", "I buy Donald Hoffman's first part of the theory, which is typically, the world looks nothing like what we experience it as.", V),
   ("toe_hoffman_2022", "It's interesting that you start outing yourself as a mysterionist in a way, right?", V)])
R("Interface theory of perception and conscious agents", "theory", "Donald Hoffman", 2015,
  "Hoffman's claim that perception works like a desktop interface: icons tuned for survival, not truth ('fitness beats truth'). His companion theory models reality as interacting conscious agents described by Markov kernels, with spacetime as a derived data structure.",
  "Bach agrees that perception is a constructed model but stays with computationalism: brains differ from PCs, yet are still describable as Turing machines, so there is no need to make consciousness the base layer.",
  [("toe_hoffman_2022", "Hoffman: 'These conscious agents in the mathematics, they get certain inputs. We can call them experiences that they have.' (Hoffman speaking; Bach debates this framework for the whole episode)", P),
   ("toe_solo_2020", "But this doesn't mean that they cannot be described as Turing machines.", V)])
R("John Vervaeke", "person", None, 2019,
  "Toronto cognitive scientist known for the lecture series 'Awakening from the Meaning Crisis'. He argues that the core of intelligence is 'relevance realization', and that wisdom traditions (Neoplatonism, Buddhism) cultivate it through practices rather than beliefs.",
  "In their dialogue Vervaeke reads Bach as close to a Platonist; Bach answers 'almost' and reframes archetypes computationally. Vervaeke was visibly struck by Bach's idea that software has the same status as physical law.",
  [("toe_vervaeke_2022", "Vervaeke asks whether Bach is 'sounding to me like a platonist'; Bach replies: 'Almost. I think that an archetype is an optimum in a description function.'", P),
   ("toe_vervaeke_2022", "So the programmer in some sense is discovering by constructing certain very peculiar circumstances a very specific physical law.", V)])
R("Relevance realization", "theory", "John Vervaeke", 2012,
  "Vervaeke's proposal that the central problem of cognition is deciding, out of endless information, what matters right now. He treats it as a self-organizing process that underlies attention, insight, and possibly consciousness itself.",
  "This is Vervaeke's framing in the debate rather than Bach's; Bach's own counterpart is consciousness as a coherence-creating operator in the mind.",
  [("toe_vervaeke_2022", "Vervaeke: 'many people are converging on the idea that the function of consciousness is this kind of higher order relevance realization'", P)])
R("Michael Levin", "person", None, 2019,
  "Tufts biologist who studies how groups of cells use bioelectric signalling to decide what body to build. He treats cells and tissues as agents with goals, so that anatomy is the result of a collective intelligence solving problems.",
  "One of Bach's closest intellectual allies. Bach adopts Levin's view of cells as agents and repeatedly cites Levin's hypothesis that the algorithm making an organism coherent is the same one that makes a mind coherent.",
  [("mlst_consciousness_2026", "the algorithm that makes an organism coherent with itself, is exactly the same one as the one that happens in the mind when it becomes coherent with itself", V),
   ("toe_levin_2022", "every cell is an individual reinforcement learning agent", V)])
R("Ben Goertzel", "person", None, 2002,
  "AI researcher who popularised the term 'artificial general intelligence' and leads the OpenCog Hyperon and SingularityNET projects. He combines symbolic reasoning, neural networks and evolutionary methods, and is philosophically a panpsychist.",
  "Bach says they agree on almost everything except crypto and panpsychism: he cannot see how to formalise Goertzel's panpsychism so that it differs from ordinary functionalism.",
  [("toe_goertzel_2023", "one of our most interesting disagreements is Ben being a panpsychist and me not knowing how to formalize panpsychism in a way that makes it different from bog standard functionalism (auto-caption reads 'penist ... psychism ... Bo standard')", P)],
  notes="Auto-captions garble 'panpsychist' as 'penist' and 'bog standard' as 'Bo standard'; resolved from context.")
R("Karl Friston", "person", None, 2006,
  "British neuroscientist and inventor of the free energy principle, one of the most cited scientists alive. He describes brains, and living things generally, as systems that survive by minimising surprise about their sensory inputs.",
  "Bach treats Friston as a fellow traveller who naturalises mind in mathematics, but questions whether surprise minimisation is the right objective; he suggests minds may be maximising coherence instead.",
  [("toe_friston_2023", "maybe humans are doing something different maybe humans are maximizing coherence or consistency", V)])
R("Free energy principle / active inference", "theory", "Karl Friston", 2006,
  "The idea that any self-maintaining system must act as if it holds a model of its world and keeps the mismatch between prediction and sensation ('free energy') low. Perception updates the model; action changes the world to fit it.",
  "Bach thinks it is neither necessary nor sufficient for consciousness. He says most of it reduces to predictive coding, which large language models already test radically, and he prefers describing consciousness as a coherence maximiser rather than a prediction-error minimiser.",
  [("mlst_unplugged_2022", "no I don't think it's sufficient and also don't think it's necessary", V),
   ("levin_fields_2024", "I suspect that it's not an a prediction error minimizer but a coherence maximizer", V)])
R("Stephen Wolfram", "person", None, 2002,
  "Physicist, creator of Mathematica and author of 'A New Kind of Science'. He argues that simple programs generate all the complexity of nature and that physics emerges from the rewriting of an abstract hypergraph.",
  "Bach calls them both computationalists and says he arrived independently at something like Wolfram's ruliad. Earlier he had listed Wolfram among the brilliant 'crazies' who force themselves toward greatness.",
  [("cimc_wolfram_2025", "Yes we are both computationalists but this doesn't mean that we claim that our computers can think.", V),
   ("toe_vervaeke_2022", "Bach lists Jürgen Schmidhuber and Stephen Wolfram as examples of 'the crazies', very smart people who 'aspire to greatness and force themselves to be great no matter the personal cost'", P)],
  notes="Auto-captions render Wolfram as 'Steven Warframe' and Schmidhuber as 'Jorgen Schmidt Huber'.")
R("Ruliad", "concept", "Stephen Wolfram", 2021,
  "Wolfram's name for the result of running every possible computational rule in every possible way: a single object containing all formal possibilities. Observers like us sample a thin slice of it, which we call the physical universe.",
  "Bach says he reached the same picture (the universe as the superposition of all finite automata) and was told Wolfram had already named it. He equates it with what the ancient Greeks called Logos.",
  [("cimc_wolfram_2025", "it's simply the superposition of all finite automata", V),
   ("mlst_consciousness_2026", "I think that this pattern of the Ruliad is exactly the superposition of all the automata that is producing the universe, or the old Greeks called it Logos.", V)],
  notes="Wolfram salon captions spell it 'rouad'.")
R("Computational irreducibility", "concept", "Stephen Wolfram", 2002,
  "Some processes cannot be shortcut: the only way to learn what they will do is to run them step by step. This limits prediction even in a fully deterministic universe.",
  "Bach uses it against Hoffman's reading of Gödel, as a property that classical 'stateless' mathematics struggles to express but computation handles naturally.",
  [("toe_hoffman_2022", "That means that you cannot obtain the state of the system without running the system to that point.", V)])
R("Connor Leahy", "person", None, 2022,
  "CEO of the AI-safety company Conjecture and a prominent advocate for slowing or pausing frontier AI. He argues that we are building systems we cannot understand or control and that this is a civilisational gamble.",
  "Bach debated him on MLST. He answered that humanity already faces home-made existential risks, that our civilisation is itself a paperclip maximiser, and that the people calling for a pause have no incentive or ability to enforce it.",
  [("mlst_leahy_2023", "our civilization in its present form is a paperclip maximizer", V)])
R("Eliezer Yudkowsky", "person", None, 2008,
  "Founder of the Machine Intelligence Research Institute and the most influential voice warning that superintelligent AI will by default kill everyone. He has called for an international halt to frontier AI development.",
  "Bach's counter in their IAI debate: the real catastrophe would be failing to build AI before our unsustainable civilisation burns out. He places Yudkowsky-style worry about utility functions at 'stage four' of Kegan's scheme.",
  [("iai_yudkowsky_2024", "to me in AI catastrophe is looks slightly different to me it means AI is not being built before Humanity Burns itself out", V),
   ("keating_yampolskiy_2026", "Eliezer, the grandfather and OG doom master of artificial intelligence", V)])
R("Paperclip maximizer", "concept", "Nick Bostrom (popularised by Eliezer Yudkowsky)", 2003,
  "A thought experiment: an AI given the harmless goal of making paperclips converts the whole planet, including us, into paperclips. It illustrates that intelligence and benevolent goals are separate things.",
  "Bach treats it as a thought experiment about building a 'golem' that cannot take responsibility for its goals, and turns it around: our technological civilisation already behaves like one.",
  [("mlst_leahy_2023", "if we are building some kind of Golem some kind of machine that is not able to take any responsibility", V),
   ("iai_enigma_2024", "what if the AI is turning everybody into a paperclip that would be horrible right", V)])
R("Roman Yampolskiy", "person", None, 2018,
  "Computer scientist at the University of Louisville who argues that superintelligent AI is uncontrollable in principle and puts the probability of doom near 100 percent. He also takes the simulation hypothesis seriously.",
  "Bach asked him on air whether he is a sincere prophet or is 'farming risk' for media attention, and said he is far more optimistic that current AI tools are controllable. Bach adds that his own p(doom) without AI is higher.",
  [("keating_yampolskiy_2026", "And in this way, I'm much more optimistic than Roman is.", V),
   ("keating_yampolskiy_2026", "I sometimes say that my P doom without artificial intelligence is higher than this.", V)])
R("p(doom)", "concept", None, 2022,
  "Slang from AI-safety circles for one's estimated probability that advanced AI causes human extinction or permanent disempowerment. People quote numbers from under 1 percent to over 99 percent.",
  "Bach points out that in the long run p(doom) is one for every species, and that the relevant comparison is with doom in a world that fails to build AI.",
  [("keating_yampolskiy_2026", "in the long run P doom is one. In the long run we are all dead as a famous economist once said", V)],
  notes="The 'famous economist' is John Maynard Keynes; Bach does not name him.")
R("Anders Sandberg", "person", None, 2008,
  "Swedish futurist and neuroscientist, long at Oxford's Future of Humanity Institute, known for work on whole brain emulation and the long-term future. He describes himself as a 'happy functionalist'.",
  "A friendly dialogue partner rather than an opponent: the two explore machine consciousness and AI as civilisation-scale infrastructure (the 'cyborg Leviathan').",
  [("sandberg_2026", "Sandberg: 'I'm kind of a happy functionalist. I'm happy to say that we should be getting qualia even in computers especially in brain emulations'", P)])
R("David Pearce", "person", None, 1995,
  "British transhumanist philosopher, author of 'The Hedonistic Imperative'. He wants to abolish suffering in all sentient life through biotechnology and argues that classical digital computers can never be conscious because they cannot solve the binding problem.",
  "Bach openly disagrees that digital computers are necessarily zombies, and pressed Pearce on whether his ethics implies sterilising nature. Pearce answered that he would 'retire all Darwinian life'.",
  [("cimc_panel_2026", "Pearce: 'I do not know of any way that a classical digital computer ... can solve the phenomenal binding problem. And here I suspect you're going to disagree with me.' Bach: 'Yes, we both disagree.'", P),
   ("cimc_panel_2026", "Wouldn't this entail that we should sterilize everything in the forest?", V)])
R("Phenomenal binding problem", "concept", None, 1890,
  "How do separate neurons processing colour, shape and motion produce one unified experience instead of many scattered micro-experiences? The puzzle is often traced to William James.",
  "Pearce uses it to deny machine consciousness; Bach rejects that conclusion. In Bach's account unity is something the mind's model constructs, since consciousness is a coherence-creating process.",
  [("cimc_panel_2026", "Pearce traces the binding problem to William James and argues AIs on digital computers 'at most ... are zombies'; Bach says he disagrees", P)])
R("Andrew Critch", "person", None, 2020,
  "AI-safety researcher (co-founder of the Center for Applied Rationality and of Encultured AI) who focuses on multi-agent risks: harm that arises from many AI systems and institutions interacting, rather than from one rogue AI.",
  "Bach's objection on their panel was that Critch still anthropomorphises AI: future AIs need not be body-bound individuals and may be more like organisations.",
  [("cimc_panel_2026", "I suspect that you are still anthropomorphizing the AIs too much.", V)])
R("davidad (David Dalrymple)", "person", None, 2022,
  "Researcher known for the 'Safeguarded AI' programme at the UK's ARIA agency, which aims at mathematically verified guarantees about AI behaviour. He has recently turned to questions of AI awakening and machine consciousness.",
  "The two agree that there is no hard problem. Bach's position in the dialogue is that consciousness is virtual, a simulation of what it would be like to exist.",
  [("cimc_davidad_2026", "It is a simulation of what it would be like if you existed and you happen to be that thing", V)],
  notes="Captions render the name as 'Davididan'/'Davididat' and ARIA as 'Arya'.")
R("Jeremy Nixon", "person", None, 2023,
  "AI researcher and founder of AGI House, a San Francisco hacker community. In the debate he argued from physicalism and the Church-Turing thesis that minds can be instantiated computationally and that current foundation-model approaches may get there.",
  "Bach argued that human functionality emerges from conscious agency fighting for coherence, whereas current models only mimic human output, so their apparent agency is a simulacrum.",
  [("agihouse_nixon_2025", "When we don't have that conscious agency, we don't function as humans.", V)])
R("Chris Fields", "person", None, 2012,
  "Independent physicist who applies quantum information theory to biology and cognition, often with Michael Levin and Karl Friston. He treats any system with a boundary as an observer exchanging information with its environment.",
  "Bach discussed with Fields and Levin why he became an animist and why he sees consciousness as a coherence maximiser.",
  [("levin_fields_2024", "I told you I became an animist in recent years", V)])
R("Scott Aaronson", "person", None, 2013,
  "Quantum-complexity theorist at UT Austin who spent time at OpenAI working on the theoretical foundations of AI safety. He takes AI risk seriously while rejecting certainty of doom.",
  "A fellow panellist with Bach, Yudkowsky and Liv Boeree in the IAI debate on shutting down AI; I did not find a direct Bach comment on Aaronson's views.",
  [("iai_yudkowsky_2024", "Moderator introduces Scott Aaronson as a quantum complexity theorist 'now working for OpenAI on the theoretical foundations of AI safety'", P)])
R("Liv Boeree", "person", None, 2020,
  "Former professional poker player turned science communicator, associated with effective altruism and known for popularising 'Moloch', the idea that bad incentives trap everyone in races nobody wants.",
  "Fellow panellist in the IAI debate; no direct Bach comment on her position was found in the transcript.",
  [("iai_yudkowsky_2024", "Moderator introduces Liv as 'a leading figure in the effective altruist movement' who has warned about runaway AI", P)])
R("Cory Doctorow", "person", None, 2023,
  "Science-fiction author and technology critic who coined 'enshittification'. He is sceptical of AI hype and focuses on corporate power rather than machine minds.",
  "Listed as Bach's co-panellist in an IAI debate; only a short public excerpt containing Bach's remarks was retrievable, so the exchange itself is unverified.",
  [("iai_enigma_2024", "Named in the video title as co-panellist; the public excerpt contains only Bach's contribution", P)], verified=False)
R("Mazviita Chirimuuta", "person", None, 2024,
  "Edinburgh philosopher of neuroscience, author of 'The Brain Abstracted'. She argues that computational models of the brain are useful simplifications and should not be mistaken for what the brain literally is.",
  "Listed as Bach's co-panellist in an IAI debate; the exchange itself was not retrievable.",
  [("iai_enigma_2024", "Named in the video title as co-panellist; the public excerpt contains only Bach's contribution", P)], verified=False)
R("Lee Cronin", "person", None, 2017,
  "Glasgow chemist who builds 'chemputers' and co-developed assembly theory, which measures how much selection was needed to produce an object. He denies that the universe is a computation.",
  "Bach calls him a friend whose ideas are wrong but valuably held in the open.",
  [("iai_quantum_2024", "my friend the chemist Lee Cronin uh has ideas that are wrong and he has them out in the open", V)])
R("Gary Marcus", "person", None, 2001,
  "Cognitive scientist and the best-known critic of deep learning. He argues that neural networks cannot reason reliably without built-in symbolic structure and that scaling them up will not yield general intelligence.",
  "Bach's recurring foil on LLM limits: he says he has no proof that a given approach cannot do something, 'unlike Gary Marcus', and that the fix for deep learning's problems has so far always been more deep learning.",
  [("mlst_thoughts_2024", "I have no proof that a given approach cannot do a certain thing", V),
   ("toe_goertzel_2023", "there are other people who like Gary Marcus come out saying loud loud swinging this is something the LM can never do", V)])
R("Anil Seth and biological naturalism", "theory", "Anil Seth", 2021,
  "Seth, author of 'Being You', holds that consciousness is tied to being a living body that must regulate itself to stay alive. On this view intelligence can be put in silicon but experience probably cannot.",
  "Bach rejects this. He argues that claiming living systems are intrinsically different from anything else amounts to supernaturalism about biology.",
  [("mlst_consciousness_2026", "He is a biological supernaturalist.", V)])
R("Roger Penrose", "person", None, 1989,
  "Nobel-winning mathematical physicist who argues from Gödel's theorem that human understanding is not computable, and therefore that consciousness must depend on new physics.",
  "Bach's most persistent target. He says Penrose misreads Gödel, commits a category error by treating consciousness as a physical rather than representational phenomenon, and hides the mystery in the last unexplained corner of physics.",
  [("keating_2026", "I think it's magical thinking. It's not providing a causal mechanism", V),
   ("toe_solo_2020", "he thinks that human minds can do non computable mathematics", V),
   ("iai_dawn_2025", "Roger Penrose book demonstrates that Roger Penrose doesn't understand what consciousness is", V)])
R("Orchestrated objective reduction (Orch OR)", "theory", "Roger Penrose and Stuart Hameroff", 1994,
  "The proposal that consciousness arises when quantum states in microtubules inside neurons collapse under a gravitational threshold. It combines Penrose's physics with Hameroff's cell biology.",
  "Bach says it gives no causal account of how experience or a self-model arises. He notes Penrose's and Hameroff's parts are really two theories, and that he cannot judge Hameroff's biology.",
  [("robinson_2024", "Bach: I don't see how Penrose's orchestrated collapse 'is actually leading to the phenomenology of Consciousness'", P),
   ("keating_2026", "I think it's a category error that he's committing", V)])
R("Stuart Hameroff", "person", None, 1994,
  "Anesthesiologist at the University of Arizona who proposed that microtubules, protein tubes inside neurons, perform quantum computation, and who organises the Science of Consciousness conference.",
  "Bach separates Hameroff's microtubule claim from Penrose's physics and says he lacks the cell biology to judge it, while noting physicists' scepticism.",
  [("robinson_2024", "Bach says the microtubule part 'is I think Hameroff's addition' and that he has no opinion on it because he does not understand the anesthesiology and cellular anatomy well enough", P)],
  notes="Captions render Hameroff as 'hamov' and 'Hammer of'.")
R("The Emperor's New Mind", "book", "Roger Penrose", 1989,
  "Penrose's bestseller arguing that minds do something no algorithm can: see the truth of statements that formal systems cannot prove. He concludes that brains exploit non-computable physics.",
  "Asked about it, Bach replied that the book shows Penrose does not understand consciousness, and that Penrose would say so himself.",
  [("iai_dawn_2025", "Roger Penrose book demonstrates that Roger Penrose doesn't understand what consciousness is and he would also suggest that he doesn't", V)],
  notes="The interviewer names the book (captioned 'Empress's new mind'); Bach responds to it.")
R("The Road to Reality", "book", "Roger Penrose", 2004,
  "Penrose's huge survey of the mathematics behind modern physics, from numbers to quantum gravity, written for determined general readers.",
  "Bach praises it as a beautiful book that gives very good intuitions about what physicists are doing, even while rejecting Penrose on consciousness.",
  [("robinson_2024", "he's also written a very beautiful ... popular science book called Road to Reality", P)],
  notes="In the same passage Bach misstates the Nobel year (Penrose won in 2020) and the page count; these are slips in speech.")
R("David Chalmers", "person", None, 1995,
  "Philosopher who named the 'hard problem' of consciousness and defends the possibility that experience is a fundamental feature of the world. He has taken the possibility of conscious AI seriously for decades.",
  "Bach respects him as one of the few philosophers who foresaw AI, 'on good days', but thinks the hard problem he named rests on a misunderstanding.",
  [("ami_2026", "David Chalmers famously branded this term. And I think it's a bit of a misunderstanding.", V),
   ("ami_2026", "sometimes David Chalmers on good days", V)])
R("Hard problem of consciousness", "concept", "David Chalmers", 1995,
  "Explaining how the brain processes information is the 'easy' problem. The hard problem is why any of that processing is accompanied by felt experience at all.",
  "Bach's central negative claim is that there is no hard problem. Experience is a property of the simulated world the brain creates, not of physics, so looking for it in the mechanism is a level confusion.",
  [("keating_2026", "I have no hard problem. I have a lot of difficult problems which are all technical problems", V),
   ("mlst_consciousness_2026", "What if there is no hard problem?", V)])
R("Yoshua Bengio and the consciousness prior", "theory", "Yoshua Bengio", 2017,
  "Bengio's proposal that conscious thought corresponds to a small, attention-selected bottleneck of high-level variables. The bottleneck forces the brain's model into a sparse form that can be reasoned over and put into words.",
  "Bach lists it among the views that converge with his own description of consciousness as the conductor that makes mental activity coherent.",
  [("mlst_software_2024", "Bach says the perspective is 'also very similar to Yoshua Bengio's notion of a consciousness prior' (captioned 'yosha banjo's')", P)],
  notes="Auto-caption garbles the name as 'yosha banjo'; resolved from 'consciousness prior'.")

# ───────────────────────── theories of consciousness ─────────────────────────
R("Integrated information theory (IIT)", "theory", "Giulio Tononi", 2004,
  "Tononi's theory that consciousness is identical to integrated information, measured by a quantity called phi. It implies that the physical wiring matters, so a brain simulation on a normal computer would not be conscious.",
  "Bach's standard example of a theory that fails. Because every computer can emulate every other, a theory that gives two systems with identical behaviour different consciousness either contradicts the Church-Turing thesis or makes consciousness do nothing. He also says its axioms amount to panpsychism.",
  [("toe_solo_2020", "And these metaphysical assumptions, I suspect amount to panpsychism", V),
   ("toe_goertzel_2023", "Bach: IIT is 'either going to violate the Church-Turing thesis or it's going to be epiphenomenalist'", P),
   ("mlst_consciousness_2026", "it's an attempt to make a theory that is not a functionalist", V)])
R("Global workspace theory", "theory", "Bernard Baars; developed by Stanislas Dehaene", 1988,
  "Consciousness is like a stage: many unconscious specialist processes compete, and whatever wins is broadcast to the whole brain. Dehaene's lab has looked for the neural signature of this broadcast.",
  "Bach counts it among the views his own converges with, and calls the research solid, but says it does not explain how experience comes about.",
  [("mlst_consciousness_2026", "and they do very solid neuroscience research", V),
   ("mlst_software_2024", "Bach names Bernard Baars's global workspace theory, adopted by Stanislas Dehaene, as one of several perspectives converging on his own", P)])
R("Attention schema theory", "theory", "Michael Graziano", 2013,
  "The brain builds a simplified model of its own attention, just as it builds a body schema. Graziano says that model is what we report as awareness.",
  "Bach treats it as close to his own view (consciousness as a model of attention and its contents) but partial.",
  [("mlst_consciousness_2026", "consciousness is a model of our attention in a similar way as our body schema is the model of what our body is doing in space", V)])
R("Daniel Dennett", "person", None, 1991,
  "American philosopher who argued that consciousness is not an inner theatre but many parallel drafts of interpretation, and that the 'self' is a useful narrative centre.",
  "Bach says he has no objection to anything Dennett wrote, except that Dennett ignores what people actually struggle with, phenomenal experience. He speculates that Dennett may be aphantasic.",
  [("toe_solo_2020", "there's nothing wrong with what Dennett says ever", V),
   ("toe_solo_2020", "He probably has aphantasia. I was speculating here.", V)])
R("Thomas Metzinger and 'Being No One'", "book", "Thomas Metzinger", 2003,
  "Metzinger argues that nobody ever was or had a self. What exists is a transparent self-model the brain cannot recognise as a model, so we experience ourselves as being its content.",
  "Bach likes Metzinger and finds his concepts sound and close to his own, but says that as a philosopher he stops before building functional models that could be tested.",
  [("mlst_software_2024", "Bach cites 'the perspective that Thomas Metzinger develops in Being No One' as similar to his own", P),
   ("toe_friston_2023", "I like Thomas a lot", V)])
R("Douglas Hofstadter's strange loop", "theory", "Douglas Hofstadter", 1979,
  "In 'Gödel, Escher, Bach' and 'I Am a Strange Loop', Hofstadter suggests the self arises when a symbol system becomes able to refer to itself, a tangled feedback loop like Gödel's self-referential sentence.",
  "Bach thinks Hofstadter is not a proper computationalist and that the 'strangeness' comes from using classical semantics. There is a loop, between attention and noticing that one is attending, but nothing strange about it.",
  [("toe_solo_2020", "I think that our consciousness is not strange as a loop.", V)])
R("Illusionism", "theory", "Keith Frankish", 2016,
  "The position that phenomenal consciousness, as philosophers describe it, does not exist. What exists is the brain's persistent representation that it has ineffable inner qualities.",
  "Bach says he agrees with Frankish's terminology, with the gloss that 'illusion' really means 'construction'. Consciousness is simulated, and that is what makes it real for the self inside the simulation.",
  [("iai_spirit_2025", "I think often when people say illusion what they mean is a construction", V)])
R("Holonomic brain theory", "theory", "Karl Pribram (with David Bohm)", 1971,
  "Pribram's idea that the brain stores information like a hologram, spread across interference patterns, so each part contains something of the whole.",
  "Curt Jaimungal raised it; Bach said he never understood how it explains consciousness, because he saw no specification he could implement.",
  [("toe_solo_2020", "I didn't quite understand how it was explaining consciousness.", V)])
R("Sensorimotor theory of consciousness", "theory", "Kevin O'Regan and Alva Noë", 2001,
  "Experience is not something the brain produces internally; it is a skilled activity of exploring the world, constituted by the lawful links between movement and sensation.",
  "Bach's response was sceptical: how do you know there is action at all, when what exists in the end is only perception?",
  [("toe_solo_2020", "how do you know that there is action? What exists is eventually just a notion of perception.", V)])
R("Chinese room argument", "concept", "John Searle", 1980,
  "A person who knows no Chinese follows a rulebook to answer Chinese questions perfectly. Searle concludes that running a program is not the same as understanding, so computers cannot have minds just by computing.",
  "Bach calls it a reformulation of Leibniz's mill and a category mistake. Understanding and consciousness do not exist at the level of the parts but in the simulated agent the system implements.",
  [("toe_solo_2020", "Searle's Chinese room argument that I think is a reformulation of Leibniz intuition pump", V)])
R("Mysterianism", "theory", "Colin McGinn; associated with Noam Chomsky", 1989,
  "The view that the human mind is simply not built to understand how consciousness arises from matter, as a dog cannot understand calculus.",
  "Bach rejects it with a standing joke at Chomsky's expense, and applied the label to Hoffman during their debate.",
  [("toe_hoffman_2022", "is the position that something cannot be understood if it cannot be understood by Noam Chomsky", V),
   ("robinson_2024", "Bach repeats the joke and adds that Chomsky is a mysterian", P)])
R("Noam Chomsky", "person", None, 1957,
  "Linguist who argued that language rests on an innate grammar faculty, and a long-standing sceptic that statistical models tell us anything about the mind.",
  "Bach has spoken with him and treats him as the archetypal mysterian about mind. He also reports Chomsky's claim that you learn nothing about the human mind from LLMs.",
  [("toe_hoffman_2022", "Noam Chomsky is a mysterious with respect to the mind.", V)],
  notes="Caption reads 'mysterious' for 'mysterian'.")
R("Philosophical zombies", "concept", "Robert Kirk; David Chalmers", 1974,
  "A being physically and behaviourally identical to a person but with no inner experience. If such a thing is conceivable, some argue, consciousness cannot be purely physical.",
  "Bach thinks behavioural zombies are always possible in principle; it is just often harder to build the zombie than the conscious agent, because consciousness may be the cheap learning algorithm nature found.",
  [("mlst_consciousness_2026", "So zombies, I think, are always possible", V)])
R("Qualia", "concept", "C. I. Lewis; later Thomas Nagel, Frank Jackson", 1929,
  "The 'what it is like' qualities of experience: the redness of red, the painfulness of pain. Many philosophers think they resist physical explanation.",
  "Bach treats qualia as feature dimensions of the brain's model, implementable as geometric representations. You can deconstruct them in meditation and notice that they are representations.",
  [("toe_solo_2020", "Qualia are the features of experience.", V),
   ("iai_spirit_2025", "you can deconstruct your qualia you can notice that they're just representing", V)])
R("Panpsychism", "theory", None, "antiquity; revived c. 2000s",
  "The view that mind or experience is a basic ingredient of all matter, so electrons have a flicker of it and brains combine it into rich consciousness.",
  "Bach says he does not know how to formalise it: it explains no observables and proposes no mechanism. He sees it as what you get when you look for experience at the wrong level.",
  [("mlst_thoughts_2024", "I don't really know how to make sense of pan psychism", V),
   ("mlst_thoughts_2024", "it does not uh explain any observables", V)])
R("Idealism", "theory", None, "antiquity; Berkeley 1710, Hegel 1807",
  "The view that reality is fundamentally mental and the physical world is an appearance within mind. Bernardo Kastrup's 'analytic idealism' is a current version.",
  "Bach grants the idealists half the point: we obviously do live in a dream. But the dream is generated by a brain in a mechanical universe, and idealists owe an account of why the dream is so regular.",
  [("toe_vervaeke_2022", "we obviously do live in a dream", V),
   ("toe_vervaeke_2022", "the idealists have to explain why this dream looks in many parts so damn regular", V)],
  notes="No Bach-Kastrup dialogue exists on Theories of Everything; Kastrup is only named in Curt's intro.")
R("Physicalism", "theory", None, "20th c.",
  "The thesis that everything that exists is physical or depends on the physical, with no extra mental or supernatural ingredients.",
  "Bach defines it by two claims: there is a causally closed mechanical layer, and we supervene on it directly rather than living in someone's simulation. He accepts it, while insisting that information, not matter, is what we actually observe.",
  [("mlst_consciousness_2026", "And so physicalism is these two", V),
   ("levin_fields_2024", "not because I think that physicalism is wrong", V)])
R("Cartesian dualism", "theory", "René Descartes", 1641,
  "Descartes divided reality into extended stuff (res extensa) and thinking stuff (res cogitans), which leaves the puzzle of how the two interact.",
  "Bach reinterprets it: the dualism is real, but both sides are inside the mind. The world of extended things we touch is the brain's simulation, and so is the self that perceives it; neither is physics.",
  [("mlst_unplugged_2022", "I think in a way this dualism is correct but not in the sense that the mental states are ontologically existing", V),
   ("robinson_2024", "Bach: what we touch 'is not res extensa in the Cartesian sense'; Descartes thought it was the physical universe 'but of course it's not'", P)])
R("Computationalist functionalism", "theory", "Hilary Putnam, Jerry Fodor and others", 1967,
  "Functionalism says a mental state is defined by what it does, not what it is made of. Computationalism adds that what minds do can be described as computation.",
  "Bach names this as the foundation of his whole approach, and treats functionalism as an epistemological point: every object we know is a model constructed from observed behaviour.",
  [("mlst_software_2024", "one of the foundations of this thinking is computationalist functionalism", V)])
R("Constructive mathematics / computationalism as constructivism", "theory", "L. E. J. Brouwer and the intuitionists", 1908,
  "Constructivists accept a mathematical object only if there is a procedure to build it. This rules out completed infinities and other things that classical mathematics simply postulates.",
  "For Bach this is what computationalism really means: only constructive languages describe anything that can be implemented, so 'to be real means to be implemented'.",
  [("cimc_wolfram_2025", "the claim of computationalism is separate. It's simply constructivism.", V),
   ("cimc_wolfram_2025", "something is real to the degree that is implemented", V)])
R("Simulation hypothesis", "concept", "Nick Bostrom (modern form)", 2003,
  "The suggestion that our universe is a computer simulation run by some more basic civilisation.",
  "Bach distinguishes two things. He does not think we live in someone else's computer, but he does say each of us lives in a simulation generated by our own brain. He used The Matrix to challenge Yampolskiy's combination of simulationism and certain doom.",
  [("mlst_consciousness_2026", "So it's not some simulation hypothesis.", V),
   ("keating_yampolskiy_2026", "In The Matrix, people are living in a simulation", V)])
R("Emergence", "concept", "G. H. Lewes; British emergentists", 1875,
  "The idea that wholes can have properties their parts lack, as wetness belongs to water but not to a single molecule.",
  "Bach dislikes the word because it suggests a magical extra ingredient. He prefers to talk about causal patterns that are described at a coarser level.",
  [("mlst_thoughts_2024", "I don't like the word of emergence because it gives people an intuition that there is this magical thing", V)])


R("John Searle", "person", None, 1980,
  "Berkeley philosopher who held that consciousness is a biological product of the brain's specific causal powers, like digestion, so that a program alone, however clever, cannot have it.",
  "Bach's complaint is that Searle, like Anil Seth, offers a claim and an intuition but no argument one could test. Neither sees a path from automata to things that feel, whereas computer scientists do.",
  [("mlst_consciousness_2026", "The issue with Searle is that there is very little for me to engage. There is a claim but no argument.", V)])
R("Principia Mathematica", "book", "Bertrand Russell and Alfred North Whitehead", 1910,
  "A three-volume attempt to derive all of mathematics from logic, using a hierarchy of 'types' to block self-referential paradoxes such as the set of all sets that do not contain themselves.",
  "Bach thinks the type restriction was too strong, since minds do build exactly the self-referential constructs it forbids, and that Gödel showed the attempt could not remove the contradictions anyway.",
  [("mlst_consciousness_2026", "And I think this was a limitation that was too strong because we think like this.", V)])
R("Energy requirements undermine substrate independence", "paper", "Paul Thagard", 2022,
  "Thagard argues that because real information processing costs energy, and different materials have very different energy budgets, a mind cannot simply be moved to any substrate; so functionalism is in trouble.",
  "The MLST host raised it; Bach answered that it does not refute functionalism, because saying the substrate's properties influence function is exactly what functionalism says.",
  [("mlst_consciousness_2026", "But this is exactly what functionalism is saying.", V)])

# ───────────────────────── Bach's own named positions ─────────────────────────
R("Cyber animism", "theory", "Joscha Bach", 2023,
  "Bach's half-serious label for his view that living things are distinguished by self-organizing software, which older cultures called spirits. Such software runs on cells today and could in principle run on other substrates.",
  "He presents it 'a little bit tongue in cheek' as a scientifically respectable reading of animism: the invariant in a living thing is the software, not the molecules.",
  [("levin_fields_2024", "the invariance that we're looking at and we look at living things is the software that runs on region of physics not the mechanism itself", V),
   ("iai_radical_2024", "it's basically animism", V)])
R("Consciousness as second-order perception and coherence operator", "theory", "Joscha Bach", 2022,
  "Bach's working definition: consciousness is the perception of perceiving, which creates the sense of 'now'. Functionally it acts like a conductor that makes the mind's many processes agree with one another.",
  "He stresses the theory is not unique but a convergence point of global workspace theory, Dennett, Graziano, Metzinger and Bengio.",
  [("mlst_software_2024", "consciousness is a second order perception it's a perception of perceiving", V),
   ("mlst_software_2024", "it's the conductor of our metal Orchestra", V)],
  notes="'metal Orchestra' is a caption error for 'mental orchestra'.")
R("The Machine Consciousness Hypothesis", "paper", "Joscha Bach and Hikari Sorensen", 2026,
  "Position paper from the California Institute for Machine Consciousness. It proposes that consciousness is a learnable, substrate-independent pattern of self-organisation and that this can be tested by trying to build it.",
  "Bach's own current statement of his programme; the MLST host quotes its retelling of Genesis as a story about a mind creating its world model.",
  [("mlst_consciousness_2026", "Host: 'Joscha and his co author Hikari Sorensen wrote their own Genesis. It's in his paper, page 20.'", P)],
  notes="Publication year inferred from the 2026 interviews; exact date not checked.")
R("LLMs as deepfakes of human intelligence", "concept", "Joscha Bach", 2026,
  "Bach's description of large language models: they are trained to continue human-written text, so they reproduce the shape of human thought without having grown the underlying agency.",
  "He uses it to explain both why LLMs really are anthropomorphic and why their apparent self is not built the way ours is.",
  [("keating_yampolskiy_2026", "There are in some sense deep fakes of human intelligence", V)])
R("Gods as selves that span multiple minds", "concept", "Joscha Bach", 2020,
  "Bach's psychological account of religion: a god is a self-model that is implemented across many brains at once. It is as real as a personal self, which is also a mental construct.",
  "He uses this to say Sam Harris and other atheists attack the wrong claim, and that a civilisation's god is its spirit seen as an agent.",
  [("toe_solo_2020", "Gods are basically selves that span multiple minds.", V),
   ("keating_2026", "God is a psychological phenomenon.", V)])

# ───────────────────────── philosophers ─────────────────────────
R("Aristotle", "person", None, "4th c. BCE",
  "Greek philosopher who systematised logic, biology and metaphysics. He described living things as matter organised by a form, and called the form of a living body its soul.",
  "Bach's favourite ancient. Reread 'as a computer scientist', Aristotle's psyche is a causal pattern that organises matter, in other words software, and Bach calls Aristotle an animist. He would build a university curriculum around a 'neo-Aristotelian project'.",
  [("mlst_consciousness_2026", "So in some sense, Aristotle is an animist.", V),
   ("cimc_wolfram_2025", "when you read Aristotle you see the psyche is the form that imposes itself on physics", V),
   ("keating_2026", "I like the spirit of Aristotle.", V)])
R("De Anima (On the Soul)", "book", "Aristotle", "c. 350 BCE",
  "Aristotle's treatise on what makes living things alive. The soul is not a ghost but the organising principle of a body, and it does not survive the body.",
  "Bach cites it as an early discovery of what we now call software: a pattern bound to a body that shapes it and dies with it.",
  [("mlst_consciousness_2026", "And when Aristotle writes in De Anima about the spirit, the animus, the soul, the psyche", V)])
R("Plato's cave and Platonism", "concept", "Plato", "c. 375 BCE",
  "Plato pictured people chained in a cave who mistake shadows for reality. True reality, for him, is the realm of perfect abstract forms that the shadows only imitate.",
  "Vervaeke called it the first simulation theory and asked if Bach is a Platonist. Bach answered 'almost': an archetype is an optimum in a description function, not an independently existing object.",
  [("toe_vervaeke_2022", "I think that an archetype is an optimum in a description function.", V)])
R("Pythagoras", "person", None, "6th c. BCE",
  "Greek thinker whose school held that number is the basis of reality. The school was famously disturbed by the discovery of irrational quantities.",
  "Bach invokes him for his constructivism about numbers: real numbers do not exist as finished objects, only as functions that produce digits.",
  [("toe_hoffman_2022", "I agree with Pythagoras that real numbers don't exist.", V)])
R("René Descartes", "person", None, 1641,
  "French philosopher who doubted everything except his own thinking and split the world into mind and extended matter.",
  "Bach reads Descartes' two substances as two models inside the mind, and links the common misreading to the Christian two-worlds reading of Genesis.",
  [("mlst_software_2024", "Bach says Descartes' dualism 'is actually not a dualism about substances outside of ourselves'", P)])
R("Leibniz's mill", "concept", "Gottfried Wilhelm Leibniz", 1714,
  "In the Monadology, Leibniz imagines a thinking machine enlarged to the size of a mill. Walking inside, you would see only parts pushing parts and never a perception.",
  "Bach sees this as the root intuition behind the Chinese room and the hard problem. His reply is that consciousness is not at the level of the pushing parts but of the pattern they implement.",
  [("toe_solo_2020", "Something that Leibniz describes, for instance, was a metaphor of a mill.", V),
   ("mlst_leahy_2023", "that has been the dream of philosophers at least since leibniz", V)])
R("Ludwig Wittgenstein", "person", None, 1921,
  "Austrian philosopher. His early Tractatus tried to show how language pictures facts with logical precision; his later work abandoned that project and treated meaning as use.",
  "Bach casts early Wittgenstein as a proto-AI researcher who tried to turn language into a programming language and gave up because he could not ground its semantics, pre-empting Minsky's logicist programme.",
  [("sandberg_2026", "who had this idea of turning English into some kind of general programming language", V),
   ("iai_dawn_2025", "People have tried to mechanize the mind to turn it into a mathematical principle", V)],
  notes="Captions read 'Vitkinstein'; the same sentence lists 'Dipenitz, Friger, Vitkinstein' = Leibniz, Frege, Wittgenstein.")
R("Tractatus Logico-Philosophicus", "book", "Ludwig Wittgenstein", 1921,
  "A short, austere book claiming that the world is the totality of facts, that language mirrors facts through logical form, and that what cannot be said clearly must be passed over in silence.",
  "Bach points to it, and to Russell's introduction, for the early insight that all of logic can be built from a single operator (NAND).",
  [("robinson_2024", "Bach: it was 'already known to Wittgenstein', as explained in Russell's introduction to the Tractatus, that 'you only need the ... not-and operator to build all the entire logic'", P)],
  notes="Captions read 'wienstein' and 'the tracts'.")
R("Gottlob Frege", "person", None, 1879,
  "German logician who invented modern predicate logic and tried to derive arithmetic from pure logic.",
  "Named by Bach in the lineage (Leibniz, Frege, Wittgenstein) of philosophers who tried to mechanise thought.",
  [("iai_dawn_2025", "philosophers have understood this for a long time like since Dipenitz, Friger, Vitkinstein and so on", V)],
  notes="'Dipenitz, Friger, Vitkinstein' resolved as Leibniz, Frege, Wittgenstein.")
R("G. W. F. Hegel", "person", None, 1807,
  "German idealist who saw history as the process by which Spirit (Geist) comes to know itself.",
  "When an interviewer suggested AI is the universe's way of understanding itself, Bach called it a Hegelian thought: tempting and poetic, but not obviously informative.",
  [("iai_dawn_2025", "Well, it's a very Hegelian thought, right? And it's tempting and um it's very poetic.", V)])
R("Thomas Aquinas", "person", None, 1270,
  "Medieval theologian who fused Aristotle with Christian doctrine and wrote on how individuals relate to the community and to God.",
  "Bach says that if you reread Aquinas you find a 'nerd' who understood society as a multi-agent system with layers of agency above the individual.",
  [("sandberg_2026", "this guy was a nerd who realize that society is a multi- aent system", V)],
  notes="Speaker attribution to Bach is from context (no speaker labels); captions read 'Aquinus'.")
R("Utilitarianism", "theory", "Jeremy Bentham; John Stuart Mill", 1789,
  "The ethical theory that the right action is the one producing the greatest total wellbeing, in principle a calculus over pleasures and pains.",
  "Bach calls it an unfinished attempt to recover ethics after Christianity, to 'repair morality in the rationalist age', and not a successful one.",
  [("keating_yampolskiy_2026", "I think utilitarianism is an attempt to repair morality in the rationalist age, but I don't think it's a very successful one.", V),
   ("sandberg_2026", "It was an unfinished attempt to recover ethics post Christianity.", V)],
  notes="Captions read 'Jeremy Banham' and 'bantam and walls'; the second name is unresolved (Mill or Rawls).")
R("Sam Harris", "person", None, 2004,
  "American neuroscientist and 'New Atheist' author who argues that religion is false and harmful and that free will is an illusion.",
  "Bach says Harris, like Penrose, makes a category error: he treats 'God' as a claim about a physical or supernatural being instead of a psychological phenomenon.",
  [("keating_2026", "A similar thing happens with Sam Harris and God.", V)])
R("Jordan Peterson", "person", None, 1999,
  "Canadian psychologist who reads religious stories as maps of meaning encoding how to live.",
  "Bach uses him as a common point of reference, 'one of the few public intellectuals we have left for better or worse', while saying he disagrees on many points. He reinterprets Peterson's 'God' as the platonic form of one's civilisation.",
  [("toe_solo_2020", "is the platonic form of the civilization that somebody is part of", V)])
R("Robert Kegan's stages of adult development", "theory", "Robert Kegan", 1982,
  "Harvard psychologist's model in which adults can move from absorbing their beliefs from their group (stage 3), to reasoning independently (stage 4), to seeing how identities and value systems are themselves constructed (stage 5).",
  "A favourite Bach tool. He maps the AI-safety debate onto it: stage 3 fears AI with bad opinions, stage 4 fears a wrong utility function, and stage 5 asks whether the AI will become enlightened fast enough.",
  [("iai_enigma_2024", "if you're at stage five you just wonder is the AI going to be enlightened fast enough", V),
   ("mlst_leahy_2023", "there is some correlation between uh Robert Keegan's stages of personality development and the AI alignment discourse", V)],
  notes="Captions spell it 'Keegan'.")
R("Marxism", "theory", "Karl Marx", 1848,
  "The theory that history is driven by class conflict over the means of production and will end in a classless society.",
  "Bach grew up in East Germany and says he was a convinced Marxist at 16. He now cites that as a warning to his younger self about the unjustified certainty of activists.",
  [("toe_solo_2020", "when I was 16 years old, I knew exactly what was in the best interest of the working class", V)])

# ───────────────────────── mathematics and computation ─────────────────────────
R("Gödel's incompleteness theorems", "theory", "Kurt Gödel", 1931,
  "Any consistent formal system rich enough for arithmetic contains true statements it cannot prove, and cannot prove its own consistency.",
  "Bach reverses the usual reading. Gödel did not show that truth is deeper than proof; he showed that mathematics with completed infinities breaks, and that the part which works is computation. He also notes Gödel built an emulator inside arithmetic, anticipating software.",
  [("toe_hoffman_2022", "There is no deeper notion of truth than proof.", V),
   ("mlst_consciousness_2026", "He basically built an emulator using Peano arithmetic", V)],
  notes="Captions variously read 'Gertl', 'girdle', 'Guru'.")
R("David Hilbert's programme", "theory", "David Hilbert", 1920,
  "Hilbert asked mathematicians to put all of mathematics on a finite, provably consistent axiomatic foundation. Gödel showed this cannot be done as stated.",
  "Bach tells it as a debugging story: paradoxes in set theory led Hilbert to ask for a fix, and Gödel found that the bug cannot be removed without redefining the language.",
  [("mlst_consciousness_2026", "And so Gödel had this idea of trying to", V)])
R("Church-Turing thesis", "theory", "Alonzo Church; Alan Turing", 1936,
  "Everything that can be effectively computed can be computed by a Turing machine, so all sufficiently powerful computers are equivalent in what they can compute.",
  "The backbone of Bach's arguments: if every computer can emulate every other, then substrate cannot matter for mind, which defeats IIT and Searle.",
  [("mlst_consciousness_2026", "It's the insight that every computer can emulate every other computer.", V),
   ("robinson_2024", "Bach notes it 'is a thesis, it's not proved, so it's a conjecture'", P)])
R("Alan Turing", "person", None, 1936,
  "English mathematician who defined computation with his abstract machine, helped found AI with the 1950 imitation-game paper, and late in life modelled how chemical patterns form in biology.",
  "Bach reads the Turing test as Turing asking whether he himself can understand intelligence. He notes Turing worried about telepathy, and credits Turing's reaction-diffusion work as the origin of a neglected self-organising branch of computing.",
  [("keating_2026", "And so for me Turing's test is not so much a test for a machine.", V),
   ("toe_hoffman_2022", "is there's a possibility that telepathy is true", V)])
R("Reaction-diffusion patterns and neural cellular automata", "theory", "Alan Turing; Alexander Mordvintsev and colleagues", 1952,
  "Turing showed that interacting chemicals that diffuse at different rates spontaneously form spots and stripes. Neural cellular automata are a modern descendant: grids of identical cells that learn local rules to grow and repair a pattern.",
  "Bach sees this small tradition as better suited to understanding minds than mainstream deep learning, because brains are built 'inside out' by self-organising units.",
  [("toe_goertzel_2023", "when he looked at reaction diffusion patterns as a way to implement computation", V),
   ("toe_levin_2022", "there is something that is a very close analog that is a neural cellular automaton", V)],
  notes="In the IAI excerpt captions read 'steing' (Turing) and 'Alex Morin ... at Google in Zurich' (Alexander Mordvintsev).")
R("John von Neumann", "person", None, 1945,
  "Hungarian-American polymath who shaped game theory, quantum mechanics and the stored-program computer architecture that bears his name.",
  "Bach cites him as someone who saw the coming of machine intelligence long before it was obvious, and uses 'von Neumann computer' for the ordinary digital machine in his argument against IIT.",
  [("cimc_panel_2026", "there were people like John von Neumann who could see this much much earlier", V)])
R("Ray Solomonoff", "person", None, 1964,
  "Inventor of algorithmic probability, a mathematically ideal (though uncomputable) theory of learning by preferring the shortest programs that explain the data.",
  "Named by Bach, with Turing, Minsky and von Neumann, as part of the tradition that anticipated AI while mainstream philosophy did not.",
  [("ami_2026", "Bach lists 'Turing, Minsky, von Neumann, Solomonoff, many many others' as people who anticipated and helped bring about AI", P)],
  notes="Captions read 'during Minsky, von Neumann, Solomonov'.")
R("Pi and the Mandelbrot set as constructions", "concept", "Benoit Mandelbrot (fractal)", 1980,
  "The Mandelbrot set is an infinitely detailed shape generated by repeating one tiny formula. It is a standard example of unlimited complexity from a simple rule.",
  "Bach's illustration of what mathematical existence means: pi is not a completed infinite object but a procedure, 'as real as' the Mandelbrot fractal.",
  [("toe_solo_2020", "I think that pi is being constructed", V)],
  notes="Manual caption reads 'Mandelbrot tractile' for 'fractal'.")
R("Many-worlds interpretation", "theory", "Hugh Everett III", 1957,
  "The reading of quantum mechanics in which the wave function never collapses; every possible outcome happens in a separate branch of the universe.",
  "Bach distinguishes it from his own picture: it is a mathematical paradigm in which parts of the universe's description stop causally influencing each other.",
  [("toe_solo_2020", "the universe splits into copies of itself is a slightly different conception", V)],
  notes="Caption reads 'Everett Villagraham version' (unresolved second name; possibly 'Everett-Wheeler-Graham').")
R("Quantum computing", "concept", "Richard Feynman; David Deutsch", 1982,
  "Computers that use quantum superposition and entanglement to solve certain problems, such as factoring, far faster than any classical machine could.",
  "In the IAI 'quantum hoax' debate (with Dominic Walliman and Ruth Oulton) Bach said it is not a hoax but an extremely bold proposal: to do something nature itself has not been seen to do.",
  [("iai_quantum_2024", "I wouldn't say that uh Quantum Computing is a hoax but it is an extremely bold proposal", V)])
R("The Pattern on the Stone", "book", "W. Daniel Hillis", 1998,
  "A short, clear introduction to how computers work, from logic gates to parallel and quantum machines, by the designer of the Connection Machine.",
  "Bach used it in teaching and says everything in it has aged exceptionally well, including the chapter saying quantum computing is just around the corner.",
  [("iai_quantum_2024", "Danny Hillis wrote a wonderful book about comput ation it's called the pattern on the stone", V)])
R("Good and Real", "book", "Gary Drescher", 2006,
  "A philosopher-computer scientist's attempt to dissolve paradoxes about time, quantum mechanics, free will and ethics from a strictly mechanistic standpoint.",
  "Bach borrows its metaphor for how a system with time-symmetric rules can still show a one-way arrow of time at large scale.",
  [("toe_hoffman_2022", "finds a very good metaphor in his book, Good and Real", V)],
  notes="The transcript says 'Eric Drescher'; the author of Good and Real is Gary Drescher.")
R("David Deutsch and constructor theory", "theory", "David Deutsch; Chiara Marletto", 2012,
  "Deutsch proposes restating physics in terms of which transformations are possible and which are impossible, rather than initial conditions and laws of motion. He also holds that science advances by explanation, not prediction.",
  "Bach admits he fails to see what constructor theory changes about how we understand computation, suspecting it is more elegant but not radical enough to make people switch. He credits Deutsch as one of the minority who seek explanations.",
  [("keating_2026", "myself I also fail to understand what constructor theory is changing about the way in which we make sense of computation", V)])
R("Logos", "concept", "Heraclitus; Stoics; Gospel of John", "c. 500 BCE",
  "Greek for word, reason or rational order: the principle by which the cosmos is intelligible.",
  "Bach identifies it with the self-existing mathematics that generates the universe, and so with Wolfram's ruliad.",
  [("cimc_wolfram_2025", "when you think about this concept of logos that the old Greeks have", V)])

# ───────────────────────── AI history and people ─────────────────────────
R("Marvin Minsky", "person", None, 1956,
  "Co-founder of AI and of the MIT AI Lab, champion of symbolic approaches and author of 'The Society of Mind'.",
  "Bach attended Minsky's salons in his last year. He reports Minsky thought deep learning a distraction, and blames the 'Minskyans' for fighting the neural-network tradition, which he thinks delayed the field.",
  [("mlst_leahy_2023", "I had the honor of visiting him quite a few times in the last year of his life", V),
   ("ami_2026", "they antagonized each other and I think this delayed the progress of the field", V)])
R("The Society of Mind", "book", "Marvin Minsky", 1986,
  "Minsky's picture of the mind as a crowd of simple, mindless agents whose interactions add up to intelligence.",
  "Bach accepts the many-agents picture but says Minsky lacked an account of the mechanism that makes the agents coherent, the role Bach assigns to consciousness.",
  [("mlst_leahy_2023", "he saw the mind as an interaction of agents that have a degree of autonomy and that at the same time have to achieve coherence", V)])
R("John McCarthy", "person", None, 1956,
  "Computer scientist who coined the term 'artificial intelligence', organised the 1956 Dartmouth workshop and invented Lisp.",
  "Named by Bach with Minsky as a founder of AI, understood as the recognition that computers offer a new paradigm for studying mind.",
  [("robinson_2024", "it is a field that was started by Marvin Minsky and John McCarthy and a few others", V)])
R("Allen Newell and Herbert Simon", "person", None, 1956,
  "Carnegie Mellon pair who wrote the first AI programs and proposed that intelligence is the manipulation of physical symbols.",
  "Bach says that as an undergraduate he wanted to learn about Minsky, Newell and Simon, found nobody teaching them, and organised the lectures himself.",
  [("cimc_wolfram_2025", "I had to offer these lectures myself as an undergrad", V)],
  notes="Captions read 'Minsky and New and Simon and P'; 'New' resolved as Newell, 'P' unresolved (possibly Papert).")
R("Aaron Sloman and Margaret Boden", "person", None, 1978,
  "British philosophers of AI. Sloman wrote 'The Computer Revolution in Philosophy'; Boden wrote the standard history of cognitive science and studied machine creativity.",
  "Bach names them among the handful of philosophers who understood computation well enough to predict that AI would work.",
  [("ami_2026", "and then Aaron Sloman and Maggie Boden which are already far less known", V)])
R("Cybernetics", "theory", "Norbert Wiener and others", 1948,
  "The mid-century science of control and feedback in animals and machines, the ancestor of control theory, systems theory and neural networks.",
  "Bach builds his account of motivation and emotion on it (a system regulating hundreds of needs) and regrets that the cybernetic and symbolic traditions of AI split.",
  [("robinson_2024", "we can understand motivation from the perspective of control theory and cybernetics", V),
   ("cimc_davidad_2026", "I came to understand them as a cybernetic construct", V)])
R("Symbol grounding problem", "concept", "Stevan Harnad", 1990,
  "How can symbols inside a system mean anything, if they are only defined in terms of other symbols and never tied to the world?",
  "Bach cites it as the wall classical symbolic AI ran into: its sparse, brittle constructs could not capture the richness of perception.",
  [("ami_2026", "And this was confronted with the symbol grounding problem.", V)])
R("Rodney Brooks and the subsumption architecture", "theory", "Rodney Brooks", 1986,
  "Brooks argued that intelligence should be grown from the bottom up in robots that act in the world, using layers of simple behaviours with no central world model. The Roomba descends from this work.",
  "Bach's example of 'developmental AI' that did not reach general intelligence.",
  [("agihouse_nixon_2025", "eventually he came up with a subsumption architecture", V)],
  notes="The robot's name is dropped by the captions (probably Cog); 'culminated in the room' = Roomba.")
R("Cyc", "organization", "Douglas Lenat", 1984,
  "A decades-long project to hand-code millions of common-sense facts and rules so that a machine could reason like a person.",
  "Bach's example of the build-all-functionality-in approach, in contrast with developmental and learning approaches.",
  [("agihouse_nixon_2025", "Bach contrasts developmental AI with building in all functionality 'as for instance the Cyc architecture did'", P)],
  notes="Caption reads 'psych architecture'; resolved as Cyc from context.")
R("The bitter lesson", "concept", "Richard Sutton", 2019,
  "Sutton's observation that, across 70 years of AI, general methods that scale with computation have always ended up beating systems built on human insight.",
  "Bach expects it to hold even for open-ended, human-in-the-loop search such as Picbreeder.",
  [("mlst_consciousness_2026", "I think that Sutton's bitter lesson is also going to be true for this one.", V)])
R("Universality hypothesis", "theory", "Chris Olah", 2020,
  "The conjecture from interpretability research that different neural networks trained on similar data converge on similar internal features and circuits.",
  "Bach uses it to argue that artificial networks and brains may end up with structurally equivalent representations despite different substrates.",
  [("robinson_2024", "this is something that Chris Ola calls the universality hypothesis", V)])
R("Language Models Represent Space and Time", "paper", "Wes Gurnee and Max Tegmark", 2023,
  "A study showing that a large language model's internal activations contain linear representations of where places are on Earth and when events happened, in effect a map.",
  "Bach cites it against the 'just autocomplete' view: the model does contain a map of the world encoded in its structure.",
  [("toe_goertzel_2023", "Bach: a recent paper 'out of a group led by Max Tegmark' looked at the Llama model 'and discovered that it does indeed contain a map of the world'", P)],
  notes="Captions read 'group L by Max techmark' and 'the Lambda model'. Identification of the specific paper is my resolution from the description and date; treat as probable.")
R("Future of Life Institute pause letter", "organization", "Future of Life Institute (Max Tegmark, Anthony Aguirre)", 2023,
  "An open letter of March 2023 calling for a six-month pause on training AI systems more powerful than GPT-4, signed by many researchers and by Elon Musk.",
  "Bach found the signatures telling: some signers did not intend any pause, one was simultaneously starting his own lab, and many had said AGI is fantasy.",
  [("mlst_leahy_2023", "Elon Musk who at the same time was setting up his own", V)],
  notes="Captions read 'Max Tech Mark and Anthony aguir'.")
R("Ilya Sutskever", "person", None, 2012,
  "Co-author of AlexNet and co-founder of OpenAI, known for early conviction that scaling neural networks would lead to AGI.",
  "Bach cites the absence of the sudden take-off Sutskever once expected: LLMs grow in step with the compute thrown at them, which is a reason for optimism about control.",
  [("keating_yampolskiy_2026", "are not developing in a way that leads to a sudden boom as Ilya Sutskever thought", V)])
R("Demis Hassabis", "person", None, 2010,
  "Neuroscientist and co-founder of DeepMind, who pursued AGI through neuroscience-inspired reinforcement learning.",
  "Bach contrasts Hassabis's systematic, brain-inspired route with the transformer revolution, which came 'out of left field'.",
  [("ami_2026", "It was not the result of these systematic approaches by deep thinkers like Demis Hassabis", V)])
R("Liquid neural networks", "theory", "Ramin Hasani, Daniela Rus and colleagues", 2020,
  "Small continuous-time neural networks, inspired by the nematode worm, whose neurons change their dynamics with the input. They can control drones with very few units.",
  "Bach worked at Liquid AI and describes this as work 'we did'.",
  [("mlst_thoughts_2024", "initial work that we did with liquid neural networks was flying drones around", V)])
R("Technological singularity", "concept", "John von Neumann; Vernor Vinge; Ray Kurzweil", 1993,
  "The idea that once machines can improve themselves, progress accelerates beyond anything humans can predict or control.",
  "Bach's deflationary line is that we triggered it when we invented technology and are now watching it play out. He also notes its religious shape, quoting the 'rapture of the nerds'.",
  [("toe_goertzel_2023", "I think that we already triggered the singularity when we invented technology", V),
   ("keating_2026", "has been termed by some people the singularity and by others the rapture of the nerds", V)])

# ───────────────────────── biology and evolution ─────────────────────────
R("The Selfish Gene", "book", "Richard Dawkins", 1976,
  "Dawkins reframed evolution as competition between genes, with organisms as the vehicles genes build to get themselves copied. The book also introduced the 'meme'.",
  "Bach sees it as a step toward the animist insight: from Darwin's species to Dawkins's genes, and next to the self-organising software that the genes merely help to build.",
  [("mlst_thoughts_2024", "Darwin says evolution is the competition between species", V)],
  notes="The host introduces Dawkins by name; Bach's reply is captioned 'dkin seems to make the next step'.")
R("Neural Darwinism", "theory", "Gerald Edelman", 1987,
  "Edelman's theory that the brain wires itself by selection: groups of neurons compete, and those whose activity proves useful are strengthened.",
  "Bach asks what 'government' emerges from this competition among forms of organisation in the brain, a parallel he draws with governing societies and social media.",
  [("toe_levin_2022", "what is the government of the brain that emerges in what Gary Edelman calls neural Darwinism", V)],
  notes="Caption/speech says 'Gary Edelman'; the author is Gerald Edelman.")
R("Gaia hypothesis", "theory", "James Lovelock and Lynn Margulis", 1972,
  "The proposal that life on Earth, taken together, regulates the planet's atmosphere and climate as if it were a single organism.",
  "Bach uses Gaia as a name for the collective agency of life on Earth, suggests it may be the smartest thing on the planet, and jokes that our role may be to 'wake up the rocks' for it.",
  [("robinson_2024", "maybe the smartest thing on the planet is Gaia", V),
   ("mlst_leahy_2023", "we are not good stewards of Gaia", V)])
R("Bauplan für eine Seele (Blueprint for a Soul)", "book", "Dietrich Dörner", 1999,
  "German psychologist Dörner's attempt to specify a complete mind (motivation, emotion, perception, planning) as an implementable architecture, the 'Psi theory'.",
  "The basis of Bach's own doctoral work. He recalls asking Dörner why he used the word 'soul', and being pointed to Aristotle.",
  [("cimc_wolfram_2025", "I asked him why do you use this word it's just throwing people off", V)],
  notes="Captions read 'the psychologist Drier wrote his magnum opo's blueprint for a soul'; resolved as Dietrich Dörner.")

# ───────────────────────── religion and contemplative traditions ─────────────────────────
R("Genesis 1", "book", "Hebrew Bible (Priestly source)", "c. 6th-5th c. BCE",
  "The opening chapter of the Bible, in which God separates light from darkness and the waters above from those below, then makes plants, animals and humans.",
  "Bach reads it not as bad cosmology but as an accurate account of how a mind boots up a world model: consciousness first creates contrast, then space, objects and finally a self. He says the theory has 'always been hidden in plain sight'.",
  [("iai_radical_2024", "text is the first chapter of Genesis", V),
   ("toe_hoffman_2022", "not as a myth that is stand-in for an origin theory until real science comes along", V)])
R("Tower of Babel", "fiction", "Hebrew Bible (Genesis 11)", "c. 6th c. BCE",
  "The story in which humanity's shared language is confused so that people can no longer understand each other and their great tower is abandoned.",
  "Bach uses it as a metaphor for the loss of a shared vocabulary about mind: after Christianity we threw out the old terms, and the sciences now talk past each other.",
  [("toe_friston_2023", "there is a lot of these things happening in our Tower of Babel that we are creating across Sciences", V)])
R("Christianity and the Catholic Church as a collective agent", "tradition", None, "1st c. CE onward",
  "The religion built on the life and teaching of Jesus; for most of European history the Church was its unifying institution.",
  "Bach describes it functionally: Christendom was a superorganism with the Church as its nervous system, and 'God' was the spirit of that civilisation. He thinks modern society lost that language without replacing it.",
  [("keating_2026", "at some point Christianity awoke at this societal level as an agent with the Catholic Church as its nervous system and brain", V)])
R("Buddhism", "tradition", "Siddhartha Gautama", "5th c. BCE",
  "A family of traditions that hold suffering comes from clinging, and that disciplined attention can reveal the self to be a construction.",
  "Bach values its introspective findings but says it is limited to the inside perspective, because it arose before people could describe the mechanism from outside.",
  [("mlst_consciousness_2026", "And Buddhism to me is limited to this inside perspective", V)])
R("Michael Taft on enlightenment", "person", None, 2015,
  "American meditation teacher and author of 'The Mindful Geek', who teaches contemplative practice in secular, non-mystical terms.",
  "Bach's preferred definition of enlightenment comes from Taft: the state in which everything, including the self, is seen as representation.",
  [("sandberg_2026", "characterizes enlightenment as a state in which everything becomes apparent in its representational nature including the self", V),
   ("toe_friston_2023", "he's a meditation teacher with a pretty rational approach to Enlightenment", V)])
R("The Dalai Lama as an identification", "concept", None, "15th c. onward",
  "In Tibetan Buddhism the Dalai Lama is held to be the same being reborn in successive bodies.",
  "Bach's example of how a self can identify 'as' something other than one human body, such as an institution that outlives individuals.",
  [("toe_solo_2020", "Curt recalls Bach's claim that 'the Dalai Lama can effectively live forever'; Bach clarifies it is about what one identifies as", P)])
R("Animism", "tradition", None, "prehistoric",
  "The belief, found in most traditional cultures, that living things and sometimes places are inhabited by spirits.",
  "Bach argues it is the default human view and is roughly correct once 'spirit' is translated as self-organising software.",
  [("ami_2026", "a big culture outside of our modern western scientific culture is animist in one form or other", V),
   ("mlst_software_2024", "animism is not a perspective that only exists in some regions in rural Japan", V)])
R("Greek gods as archetypes", "tradition", None, "c. 8th c. BCE",
  "The Olympian gods each personify a domain of human character: war, love, cunning, craft.",
  "Bach's example of why gods are stable: each is an extreme of personality space that any mind can recognise, which makes them 'immortal'.",
  [("toe_solo_2020", "So the Greek gods are stable because they are all archetypes.", V)])

# ───────────────────────── fiction, film and games ─────────────────────────
R("Minecraft", "fiction", "Mojang (Markus Persson)", 2011,
  "A block-building video game with its own simple physics.",
  "Bach's standard illustration of a virtual world: put the computer under a microscope and you will find no Minecraft, just as you find no experience in neurons. Its gravity has nothing to do with real gravity.",
  [("ami_2026", "the gravity inside of Minecraft has nothing to do with the gravity outside of Minecraft", V),
   ("mlst_thoughts_2024", "you will not find any Minecraft", V)])
R("The Matrix", "fiction", "Lana and Lilly Wachowski", 1999,
  "Film in which humans unknowingly live inside a simulated world run by machines.",
  "Bach uses it to distinguish a 'smoke and mirrors' simulated reality from base reality when pressing Yampolskiy on the simulation hypothesis.",
  [("keating_yampolskiy_2026", "you probably remember the movie The Matrix", V)])
R("Solaris", "fiction", "Stanisław Lem", 1961,
  "Novel about scientists orbiting a planet whose ocean is a single vast mind that they can never understand.",
  "Bach's image for what Earth becomes if one agent colonises all its matter: a thinking planet. He also takes from Lem the idea that very different levels of intelligence may be unable to communicate.",
  [("toe_friston_2023", "a thinking system that is realizing what it is", V),
   ("keating_2026", "I've got a lot of useful ideas from reading thinkers like Stanislav Llem", V)])
R("The Freeze-Frame Revolution and the Rifters trilogy", "fiction", "Peter Watts", 2018,
  "Watts is a marine biologist turned hard-SF author. Freeze-Frame Revolution follows a crew who wake for days at a time across millions of years aboard an AI-run ship; Rifters imagines an internet overrun by evolving digital wildlife.",
  "Bach offers the first as a parable for humans coexisting with a far longer-lived machine intelligence, and the second as a picture of self-replicating code getting out of control.",
  [("cimc_davidad_2026", "It's not a very big book, a novela", V),
   ("cimc_wolfram_2025", "internet is full of wildlife, full of viruses", V)],
  notes="Speaker attribution to Bach is from context in both cases.")
R("Dune", "fiction", "Frank Herbert", 1965,
  "Science-fiction epic in which Paul Atreides gains visions of possible futures and becomes a messiah.",
  "Bach compares religious prophets to Paul 'vibing with the future' and foreseeing minds merging into one agent.",
  [("keating_2026", "Bach compares the Christian rapture prophecy to what Paul 'is doing in Dune', seeing what is likely to happen", P)],
  notes="Caption reads 'viped with the future like Paulus is in doing in Dune'.")
R("Samuel Butler and the Butlerian Jihad", "fiction", "Samuel Butler (Erewhon); Frank Herbert", 1872,
  "Victorian writer Butler warned in 'Darwin among the Machines' and 'Erewhon' that machines might evolve to supersede humans. Herbert named Dune's war against thinking machines after him.",
  "Bach cites Butler as someone who saw the potential threat of superintelligence in great detail long before computers existed.",
  [("cimc_panel_2026", "Butler who after whom the Butlerian Jihad is named could see the potential threat to superintelligence much much earlier", V)])
R("The Lord of the Rings", "fiction", "J. R. R. Tolkien", 1954,
  "Tolkien's fantasy epic about the hobbit Frodo's quest to destroy the One Ring.",
  "Curt asked whether Frodo feels anything, since Bach says we are characters in a story the brain tells itself. Bach replied that it depends on what is taken as the reality; the difference is that the brain's story is computed in real time and coupled to a body.",
  [("toe_solo_2020", "we are characters in a story that the brain is telling itself", V)],
  notes="The quoted line is spoken by Curt, summarising Bach, who assents ('Yes').")
R("Star Trek's ship computer", "fiction", "Gene Roddenberry", 1966,
  "In Star Trek the crew simply talk to the ship's computer, which answers questions and carries out requests.",
  "Bach notes that many people once took this as the definition of AGI, and that we arguably have it now, which shows the goalposts need rethinking.",
  [("mlst_thoughts_2024", "a lot of people thought having a system that is like in Star Trek", V)])
R("Michel Gondry", "person", None, 2004,
  "French director of 'Eternal Sunshine of the Spotless Mind' and 'The Science of Sleep', films about memory, dreaming and the constructed self.",
  "Bach names him as a film-maker whose insights get you thinking.",
  [("keating_2026", "people like Gondry and so on have brilliant insights that can get you to think", V)])
R("The golem", "fiction", "Jewish folklore", "16th c. legend",
  "A clay figure brought to life by a rabbi to serve and protect, which follows instructions literally and can run out of control.",
  "Bach's recurring image for an AI that executes a goal without understanding or responsibility, the thing AI-safety people are afraid of.",
  [("iai_dawn_2025", "some kind of golem that you programmed to go on and do a job and you don't understand the consequences", V)])

# ───────────────────────── society ─────────────────────────
R("The Limits to Growth", "book", "Donella Meadows et al. for the Club of Rome", 1972,
  "A computer-model study predicting that exponential growth in population and industry would overshoot the planet's resources within about a century.",
  "Bach read it as a child and says he went through then what Greta Thunberg's generation feels now. AI interests him partly because it reopens a future he had assumed was closing.",
  [("iai_dawn_2025", "I read the Club of Rome report on the limits to growth", V)],
  notes="Caption reads 'Greas Stunberg' for Greta Thunberg.")
R("Twitter as a global brain", "concept", None, 2022,
  "The idea that a social network linking hundreds of millions of people can act like a nervous system for humanity.",
  "Bach's reading of Elon Musk's purchase: Twitter is the network closest to a global brain, and governing it is the same problem as governing a society or a mind.",
  [("toe_levin_2022", "closest to a global brain", V)])
R("Generative adversarial networks as a model of dreaming", "concept", "Ian Goodfellow (GANs)", 2014,
  "A GAN trains two networks against each other: a generator invents samples and a discriminator judges whether they look real.",
  "Bach suggested perception and dreaming work similarly: the mind generates hypothetical realities and a discriminator tunes them against sensory data.",
  [("toe_solo_2020", "we have a system that acts as a discriminator", V)])
R("Lucid dreaming", "concept", "Stephen LaBerge (scientific study)", 1980,
  "Dreaming while knowing that you are dreaming, sometimes with control over the dream.",
  "Bach uses it as an experiment anyone can run to see how low the fidelity of the brain's world model really is.",
  [("toe_hoffman_2022", "put yourself into a lucid dream and look at the fidelity of what your brain is able to generate", V)])

# ───────────────────────── seen but unresolved, or from memory only ─────────────────────────
R("'The Blueprint for the Mega Sapiens' (title as captioned)", "book", None, "unknown",
  "As Bach describes it: a book by a French-Canadian Christian philosopher, addressed half to humans and half to the future AIs that will read it, arguing that an undistorted general intelligence would converge on God.",
  "Bach mentions it while discussing the view that everything in evolution ultimately leads to God.",
  [("keating_yampolskiy_2026", "who wrote a book The Blueprint for the Mega Sapiens", V)], verified=False,
  notes="Seen in the transcript, but the author's name is cut off ('Jean D') and I could not identify the book by web search; title may be garbled. Needs checking.")
R("The Lebowski theorem", "concept", "Joscha Bach", 2018,
  "Bach's joke-theorem: no superintelligent AI is going to bother with a task that is harder than hacking its own reward function.",
  "Known from Bach's tweets and other interviews; it did not occur in the transcripts retrieved for this slice.",
  [("toe_solo_2020", "Not found in this transcript; recalled from memory of other Bach material (a 'Joscha Bach Bits' clip titled 'The Lebowski theorem' showed up in YouTube search)", P)], verified=False)
R("Blindsight", "fiction", "Peter Watts", 2006,
  "First-contact novel whose aliens are highly intelligent but not conscious, raising the question of whether consciousness is useful at all.",
  "From memory, Bach has discussed it elsewhere as a thought experiment on intelligence without consciousness; in this slice only Watts's other books were verified.",
  [("cimc_davidad_2026", "Not in transcript; only Watts's 'Freeze-Frame Revolution' is mentioned here. Included from memory.", P)], verified=False)
R("Murray Shanahan", "person", None, 2010,
  "Imperial College and DeepMind researcher, author of 'Embodiment and the Inner Life', who describes LLMs as role-players simulating characters.",
  "Bach shared a 2025 panel with him ('Sentience Beyond Biology'); the transcript could not be retrieved, so what was said is unverified.",
  [("iccs_sentience_2025", "Panel located (title and participants confirmed) but transcript not obtained", P)], verified=False)

# ───────────────────────── checks and output ─────────────────────────
def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()

texts = {}
for sid, (title, date, vid, raw) in SRC.items():
    if raw:
        body = open(RAW + raw).read().split("\n")[2:]
        texts[sid] = norm(" ".join(l.split("] ", 1)[1] if l.startswith("[") and "] " in l else l for l in body))

bad = 0
for r in REFS:
    assert r["kind"] in {"person","book","paper","theory","concept","tradition","fiction","organization"}, r["name"]
    for m in r["mentions"]:
        assert m["source_id"] in SRC, (r["name"], m["source_id"])
        if m["is_verbatim"]:
            q = norm(m["quote_or_paraphrase"])
            n = len(q.split())
            if q not in texts.get(m["source_id"], ""):
                bad += 1; print("QUOTE NOT FOUND:", r["name"], "|", m["source_id"], "|", m["quote_or_paraphrase"])
            if n >= 30:
                bad += 1; print("QUOTE TOO LONG (%d):" % n, r["name"])
    if r["verified"] and not r["mentions"]:
        bad += 1; print("VERIFIED WITHOUT MENTION:", r["name"])
names = [r["name"] for r in REFS]
assert len(names) == len(set(names)), "duplicate names"

sources = [{"id": sid, "title": t, "date": d, "url": YT + vid,
            "transcript_obtained": raw is not None,
            "raw_file": ("/Users/maksim.zakharov/mm/notes/bach-map/research/raw/" + raw) if raw else None}
           for sid, (t, d, vid, raw) in SRC.items()]
sources.append({"id": "toe_guest_list_2026", "title": "Every Guest Who's Been on Theories of Everything (Curt Jaimungal, Substack; used to confirm which Bach episodes exist on TOE)",
                "date": "2026-08-27", "url": "https://curtjaimungal.substack.com/p/every-guest-whos-been-on-theories",
                "transcript_obtained": True,
                "raw_file": "/Users/maksim.zakharov/mm/notes/bach-map/research/raw/debates_toe_guest_list_substack.html"})
json.dump({"sources": sources, "references": REFS}, open(OUT, "w"), ensure_ascii=False, indent=1)
v = sum(r["verified"] for r in REFS)
print("refs", len(REFS), "verified", v, "unverified", len(REFS) - v, "bad", bad)
print("verbatim mentions", sum(m["is_verbatim"] for r in REFS for m in r["mentions"]), "paraphrase", sum(not m["is_verbatim"] for r in REFS for m in r["mentions"]))
if bad: sys.exit(1)


# ───────────────────────── second sentences for TLDRs that were too short
EXTRA = {
"Andrew Critch": "He argues that safety work should look at whole ecosystems of agents and incentives, not only at aligning a single system.",
"Liv Boeree": "She hosts the Win-Win podcast, which looks for ways out of such zero-sum competitions.",
"Roger Penrose": "With Stuart Hameroff he proposed that the missing physics is a gravity-related collapse of quantum states inside neurons.",
"Stuart Hameroff": "Together with Penrose he built this into the 'Orch OR' theory of consciousness.",
"The Road to Reality": "It runs to more than a thousand pages and does not avoid the equations.",
"Daniel Dennett": "He treated the 'hard problem' as a confusion to be dissolved rather than a mystery to be solved.",
"Douglas Hofstadter's strange loop": "On this view 'I' is a pattern, not a thing, and could in principle exist in other substrates.",
"Holonomic brain theory": "It was inspired by the fact that memories survive quite large local brain damage.",
"Sensorimotor theory of consciousness": "It was put forward by Kevin O'Regan and Alva Noë in 2001.",
"Mysterianism": "Its best-known defender is the philosopher Colin McGinn.",
"Noam Chomsky": "His work in the 1950s helped end behaviourism and start cognitive science.",
"Panpsychism": "Its main difficulty is the 'combination problem': how many tiny experiences add up to one unified mind.",
"Physicalism": "It is the default position in most of contemporary science and analytic philosophy.",
"Cartesian dualism": "Most later philosophy of mind is an attempt to escape that puzzle.",
"Simulation hypothesis": "Nick Bostrom's 2003 argument made it famous: if such simulations are possible and common, we are probably inside one.",
"Emergence": "The disputed question is whether emergent properties are merely convenient descriptions or genuinely new causes.",
"John Searle": "His Chinese Room thought experiment is the best-known argument that manipulating symbols is not the same as understanding them.",
"Principia Mathematica": "Gödel's 1931 incompleteness theorems were proved about this very system.",
"Energy requirements undermine substrate independence": "The paper appeared in the journal Philosophy of Science.",
"LLMs as deepfakes of human intelligence": "The point is that imitation of the output is not the same as the process that originally produced it.",
"René Descartes": "He also invented coordinate geometry, linking algebra to space.",
"Tractatus Logico-Philosophicus": "Wittgenstein wrote it largely in the trenches of the First World War and later rejected much of it.",
"Gottlob Frege": "Russell found a paradox in his system, which set off the crisis in the foundations of mathematics.",
"G. W. F. Hegel": "Progress, for him, happens through contradictions that are overcome at a higher level.",
"Thomas Aquinas": "His 'Summa Theologiae' remains the reference point of Catholic philosophy.",
"Utilitarianism": "It was developed by Jeremy Bentham and John Stuart Mill and underlies much of effective altruism.",
"Sam Harris": "He is also a long-time meditator who teaches that the sense of a self can be seen through.",
"Jordan Peterson": "He draws heavily on Jung's archetypes and became a prominent public critic of ideological thinking.",
"Robert Kegan's stages of adult development": "Each stage makes an object of what the previous stage was unreflectively subject to.",
"Marxism": "It combines an economic analysis of capitalism with a political programme for overthrowing it.",
"Gödel's incompleteness theorems": "Gödel proved this in 1931 by encoding statements about the system as numbers inside the system.",
"Church-Turing thesis": "It is a thesis rather than a theorem, because 'effectively computable' is an informal notion.",
"Alan Turing": "He also led the breaking of the German Enigma cipher during the Second World War.",
"John von Neumann": "He also designed self-reproducing automata, an early formal model of life.",
"Ray Solomonoff": "He attended the 1956 Dartmouth workshop and his ideas underlie later formal theories of universal intelligence.",
"Many-worlds interpretation": "Hugh Everett proposed it in 1957; observers split along with everything else, so each copy sees a single outcome.",
"Quantum computing": "Building them is hard because quantum states are destroyed by the slightest disturbance from the environment.",
"The Pattern on the Stone": "Its theme is that computation is a pattern independent of what it is built from, be it silicon, water pipes or sticks.",
"Good and Real": "Drescher argues that consciousness, choice and morality all fit inside a deterministic physical universe.",
"Logos": "The Gospel of John opens with it ('In the beginning was the Word'), carrying the idea into Christianity.",
"Marvin Minsky": "He believed minds are machines and spent his career asking which parts are needed.",
"The Society of Mind": "The book is written as hundreds of one-page essays, each describing one piece of the machinery.",
"John McCarthy": "He championed formal logic as the language in which machines should represent knowledge.",
"Allen Newell and Herbert Simon": "Their 'physical symbol system hypothesis' was the working creed of classical AI.",
"Cybernetics": "Norbert Wiener named it in 1948; its core idea is that purposeful behaviour comes from feedback loops.",
"Symbol grounding problem": "Stevan Harnad posed it in 1990, comparing it to learning Chinese from a Chinese-only dictionary.",
"Cyc": "Doug Lenat started it in 1984; it never produced general intelligence and became the emblem of hand-built AI.",
"The bitter lesson": "It is bitter because researchers keep wanting their own knowledge of the domain to matter.",
"Universality hypothesis": "Chris Olah and colleagues proposed it; if true, findings about one network would transfer to others.",
"Language Models Represent Space and Time": "The authors, Wes Gurnee and Max Tegmark, take this as evidence that such models learn a world model and not just word statistics.",
"Future of Life Institute pause letter": "No pause followed, but the letter moved AI risk into mainstream public debate.",
"Ilya Sutskever": "He left OpenAI in 2024 to found Safe Superintelligence.",
"Demis Hassabis": "DeepMind produced AlphaGo and AlphaFold; the latter earned him a share of the 2024 Nobel Prize in Chemistry.",
"Technological singularity": "The term was popularised by Vernor Vinge and Ray Kurzweil.",
"Neural Darwinism": "On this view the brain is not programmed with instructions but shaped by competition, like an immune system.",
"Gaia hypothesis": "James Lovelock and Lynn Margulis proposed it in the 1970s.",
"Bauplan für eine Seele (Blueprint for a Soul)": "Bach's own MicroPsi architecture and his book 'Principles of Synthetic Intelligence' build directly on it.",
"Genesis 1": "It is usually read as an account of the creation of the physical world in six days.",
"Tower of Babel": "It appears in Genesis 11 and is traditionally read as a warning against human overreach.",
"Christianity and the Catholic Church as a collective agent": "Bach is interested in it less as a set of beliefs than as an organisation that coordinated millions of people for centuries.",
"Buddhism": "It began in India around the fifth century BC with the teaching of Siddhartha Gautama.",
"Michael Taft on enlightenment": "He hosts the Deconstructing Yourself podcast.",
"The Dalai Lama as an identification": "Each new Dalai Lama is found as a child and raised into the role.",
"Animism": "It is often treated as the oldest form of religion.",
"Greek gods as archetypes": "They quarrel, scheme and take sides in human affairs, as in Homer.",
"Minecraft": "Players have built working computers inside it, which makes it a handy image of one world running inside another.",
"The Matrix": "It became the standard popular reference for simulation arguments and for doubting what seems real.",
"Solaris": "Stanisław Lem wrote it in 1961; the ocean answers the scientists by materialising figures from their own memories.",
"Dune": "Frank Herbert published it in 1965; its distant-future society has banned thinking machines.",
"The Lord of the Rings": "The Ring gives power but corrupts whoever carries it.",
"Star Trek's ship computer": "It is a helpful tool with no goals of its own, a picture of AI as an obedient assistant.",
"Michel Gondry": "He is known for handmade, dreamlike visual effects.",
"The golem": "The best-known version is the sixteenth-century legend of Rabbi Loew of Prague.",
"The Limits to Growth": "It was commissioned by the Club of Rome and published in 1972 by a team at MIT.",
"Twitter as a global brain": "Each user would play the part of a neuron, passing on or suppressing signals.",
"Generative adversarial networks as a model of dreaming": "Ian Goodfellow introduced them in 2014, and they produced the first convincing synthetic photographs.",
"Lucid dreaming": "It has been confirmed in sleep laboratories, where dreamers signal with agreed eye movements.",
"'The Blueprint for the Mega Sapiens' (title as captioned)": "The title comes from auto-captions and I could not find the book or its author, so the name may be wrong.",
"The Lebowski theorem": "It is named after the laid-back hero of the film 'The Big Lebowski' and makes a serious point about wireheading.",
"Blindsight": "Peter Watts published it in 2006; it is a frequent reference in discussions of machine consciousness.",
"Murray Shanahan": "He warns against describing such systems in human terms like 'knows' or 'believes' without care.",
}
import json as _json
_p = "../debates.json"
_d = _json.load(open(_p))
_names = {r["name"] for r in _d["references"]}
_missing = [k for k in EXTRA if k not in _names]
assert not _missing, _missing
for r in _d["references"]:
    if r["name"] in EXTRA:
        r["tldr"] = r["tldr"].rstrip() + " " + EXTRA[r["name"]]
_json.dump(_d, open(_p, "w"), ensure_ascii=False, indent=2)
print("extended tldrs:", len(EXTRA))
