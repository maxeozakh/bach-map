from b_sources import sources

SRC = {s["id"]: s for s in sources}
bach_ideas = []


def q(sid, text, v=False):
    s = SRC[sid]
    return {"title": s["title"], "url": s["url"], "quote_or_paraphrase": text, "is_verbatim": v, "source_id": sid}


def I(name, year, tldr, srcs, verified=True, note=None):
    d = {"name": name, "year_first_stated": year, "tldr": tldr, "sources": srcs, "verified": verified}
    if note:
        d["note"] = note
    bach_ideas.append(d)


I("The Machine Consciousness Hypothesis",
  "2025 as a named hypothesis (essay dated 2025-09-15, made public January 2026). The underlying claim that a machine could be conscious is in his papers from 2017-2018; that earlier date is my estimate from his CV.",
  "The claim is that an ordinary general-purpose computer with enough memory and speed has everything needed to be conscious, and that we can find out whether a system is conscious by analysing or testing it. Consciousness is treated as a pattern of organisation, so what the system is made of does not matter. CIMC adds a working definition: a system is conscious if it organises itself to perceive its own perceiving in a way that makes its overall model of the world more coherent. An 'extended' version says we can search for the right learning algorithm by recreating the conditions under which brains found it. The essay is co-written with Hikari Sorensen.",
  [q("mch_2025", "possess the necessary and sufficient means to implement consciousness", True),
   q("mch_2025", "Paraphrase: 'We call this possibility the Machine Consciousness Hypothesis: that general computational machines with sufficient resources' can implement consciousness and that this 'can be established via analyzing or testing the system'."),
   q("wp_2026", "A system is conscious if it implements self-organized second-order perception that increases global coherence.", True),
   q("cv_2023", "Paraphrase: CV lists 'The Cortical Conductor Theory: Towards Addressing Consciousness in AI Models' (IJCAI workshop 2017).")])

I("Consciousness is a simulated property; the self is a character in a story",
  "2018-2019 in the papers retrieved (stated plainly in the 2019 AAAI workshop paper). He very likely said it in talks before that; that is not verified here.",
  "Bach says that matter cannot be conscious; only a simulation can. The brain builds a dream-like model of a world and puts a character in it, the self, and experience is what is true for that character inside the model. So experience is real for us, while the self that seems to have it is a piece of fiction, like the hero of a novel. This lets him accept that consciousness feels real while denying that it is an extra ingredient of physics. His 2023 CV calls a 2021 talk on this view 'Virtualism'.",
  [q("phen_2019", "a physical system cannot be conscious, only a simulation can", True),
   q("phen_2019", "just like the main character of a novel inhabits a fictional universe", True),
   q("phen_2019", "Paraphrase: 'The subject of experience, the self, is a virtual character inhabiting this virtual world' (the quote is split by a page break in the PDF text)."),
   q("phen_2019", "Our phenomenal experience is very real to ourselves, but our selves are not real.", True),
   q("lex101", "we don't exist in the physical world. We do exist inside of a story that the brain tells itself", True),
   q("cv_2023", "Paraphrase: CV lists Bach (2021), 'Virtualism as a perspective on consciousness', Philosophy and Computing Conference at IS4SI 2021.")])

I("Consciousness as a coherence-inducing operator (the 'conductor')",
  "2017 (CV lists two 2017 conference papers on the conductor model; the retrieved full text is the BICA 2018 version).",
  "The mind is like an orchestra of many specialised processes, each modelling part of reality. Consciousness is the conductor: an attention process that notices where the players disagree and brings them into harmony, and that keeps a record of what it attended to. The conductor is one more learned process among the others, not a little person inside the head. In the CIMC texts this becomes 'consciousness is a coherence-maximising pattern', credited to von der Malsburg's coherence definition. Bach contrasts the view with Integrated Information Theory.",
  [q("ctc_2018", "The conductor is not a “homunculus”, but like the other instruments, a set of dynamic function approximators.", True),
   q("ctc_2018", "Unlike IIT, CTC is a functionalist model of consciousness", True),
   q("mch_2025", "Consciousness may be understood as a coherence maximizing pattern.", True),
   q("mch_2025", "Paraphrase: 'Let us call the control of a “mental orchestra” by consciousness' directed attention the conductor theory of consciousness.'"),
   q("cv_2023", "Paraphrase: CV lists Bach (2017), 'Consciousness as a Memory of Coordinating Attention: The Conductor Model of Consciousness', Science of Consciousness Conference, San Diego.")])

I("Consciousness comes before the self (the 'Genesis' idea)",
  "2023 (best estimate: stated in the Lex Fridman interview of 2023 and the 37C3 talk of December 2023; named 'Genesis Hypothesis' in the 2025 essay).",
  "The usual picture is that brains first become complex and then consciousness appears at the top. Bach turns this around: consciousness is there at the start and is what trains the mind. Babies are conscious before they have a self, language or reasoning, and no human leaves the vegetative state without it. He reads the first chapter of the Bible as an old description of this boot-up: first a spirit over the substrate, then light and dark, world and ideas, and only at the end a person. From this CIMC derives its 'Human Consciousness Hypothesis', that consciousness is the simplest learning algorithm evolution could find for a self-organising brain.",
  [q("mch_2025", "it’s not the result of our mental architecture and cognitive ability, but its prerequisite", True),
   q("mch_2025", "Instead of being brought forth by the organized architecture of the mind, it creates it. We call this idea the Genesis Hypothesis", True),
   q("c37_2023", "the earliest formulation of that theory is what I found in Genesis 1", True),
   q("lex392", "I suspect that it’s there in plain sight in Genesis 1", True),
   q("mch_2025", "Paraphrase: 'Our Human Consciousness Hypothesis states that consciousness is produced by the simplest learning algorithm that can be discovered by an evolutionary search to train a self-organizing biological substrate to become intelligent.'")])

I("Cyber-animism: software as spirit",
  "2024 (AGI-24 keynote on cyber-animism, referred to in an interview at that conference; written definition in the 2025 essay).",
  "Old cultures spoke of spirits that animate living things. Bach says this was a reasonable description of something real: self-organising software. A spirit is a pattern of control that runs on cells in the way a program runs on a computer, and it can be described without reference to the particular matter. Life, minds and even cultures are such software agents competing for substrates. He presents this as a metaphysical stance and says it is not superstition; in the essay, selves that span many minds are called gods.",
  [q("mch_2025", "the spirits of the animist worldview are not superstitions or mere analogies to computer software", True),
   q("mch_2025", "Paraphrase: 'We call the idea that natural spirits ... are best understood as software cyberanimism.'"),
   q("mch_2025", "selves capable of possessing multiple minds are called gods", True),
   q("mlst_2024", "Paraphrase: the interviewer refers to 'your cyber animism talk', the keynote given the day before at the AGI-24 conference."),
   q("agi25", "Paraphrase: 'last year I talked about the cyber animist hypothesis. It basically says that spirits can be understood as self-organizing software agents in nature'."),
   q("levin_2024", "Paraphrase: spirit is 'the word that our ancestors use to describe self organizing software agents'.")])

I("Computational functionalism, and weak versus strong computationalism",
  "2016 for 'computationalism is the new mechanism' (Edge essay). The weak/strong wording is from the 2025 essay. His CV lists a 2014 paper 'Computationalism and Cognitive Science' that was not retrieved.",
  "Bach holds two linked positions. Functionalism: a mental state is defined by what it does, so the same mind could run on different material; he sets this against 'essentialism', which ties consciousness to a special substance such as living tissue. Computationalism: any precise theory has to be a computational one. The 2025 essay separates a weak form, which says all formal theories of reality must be computational, from a strong form, which says reality itself is computational. NOTE: the task brief framed this as 'computational functionalism versus strong computationalism'; in the sources I retrieved, the stated contrasts are weak versus strong computationalism and functionalism versus essentialism, so I have recorded those.",
  [q("mch_2025", "the former states that all formal theories of reality have to be computational, while the latter applies that principle to reality itself", True),
   q("edge_2016", "Computationalism is the new mechanism", True),
   q("edge_2016", "A growing number of physicists understand that the universe is not mathematical, but computational", True),
   q("ctc_2018", "Unlike IIT, CTC is a functionalist model of consciousness", True),
   q("mch_2025", "Paraphrase: essentialists make consciousness depend on an intrinsic property of the substrate (Anil Seth is the example), while functionalists characterise the substrate fully by its causal role.")],
  note="Label in the brief corrected to match the sources.")

I("Only what can be constructed (computed) exists; Gödel as the end of classical mathematics",
  "2016 in writing (Edge essay separates computation from mathematics); the Gödel reading is stated in the 2020 Jim Rutt interview. A 2015 blog post on quantum computers may be earlier; it was saved but not read.",
  "Bach says that something is only real, or true, if it can in principle be computed step by step. Mathematics that needs completed infinities or perfect continua cannot be carried out by any physical process, so in his view it describes nothing that exists. He reads Gödel's incompleteness result as showing this: classical mathematics breaks, constructive mathematics is what is left, and constructive mathematics is the same thing as computation. This is his own reading; most logicians take Gödel's theorems to show limits of formal proof, not that classical mathematics is wrong. He uses it against Penrose's argument that human minds do something computers cannot.",
  [q("rutt87", "classical mathematics that contains infinities cannot be implemented, cannot be real", True),
   q("rutt87", "You can only claim that something is true, if you can actually compute that truth.", True),
   q("mch_2025", "A way to interpret Gödel's proof is that languages that cannot be automatically evaluated inevitably contain unresolvable paradoxes", True),
   q("mch_2025", "constructive mathematics based on finite automata is the only part of mathematics that actually works", True),
   q("edge_2016", "Computation is different from mathematics.", True)])

I("Levels of Lucidity",
  "2023 (Substack essay of 2023-05-21).",
  "A seven-step ladder of how a mind can come to understand its own workings. The steps are: reactive survival, personal self, social self, rational agency, self-authoring, enlightened mind and transcendent mind. Each step comes from seeing through a part of oneself that used to be taken for granted. It is based on Robert Kegan's five stages, which Bach says he has drifted away from. He says it is not a ranking of people's worth and that most people do not need to climb it.",
  [q("sub_lucidity_2023", "Let us call the framework the “Levels of Lucidity”.", True),
   q("sub_lucidity_2023", "Paraphrase: the stages listed are 1 Reactive survival, 2 Personal self, 3 Social self, 4 Rational agency, 5 Self authoring, 6 Enlightened mind, 7 Transcendent mind."),
   q("sub_lucidity_2023", "I particularly like Robert Kegan’s five stage model of personality development", True)])

I("Love as the discovery of shared purpose; alignment through shared purpose",
  "2021 (Lex Fridman interview #212). The application to AI alignment is in the 2023 Substack essay.",
  "Bach defines love as finding that you and another serve the same purpose above yourselves, which lets you deal with each other without bargaining. He applies this to AI. Advanced agents, human or artificial, cannot be aligned from outside; they align themselves by trade, by force, or because they find shared purposes. So the hopeful path with AI is to build systems that can share purposes with us. In 2026 he calls intelligence without this 'hollow agency'.",
  [q("lex212", "It's the recognition of the sacred and the other. And this enables non-transactual interactions.", True),
   q("lex212", "Paraphrase: the machine transcript reads 'love is, there is a curry of shared purpose', almost certainly a mis-transcription of 'the discovery of shared purpose'."),
   q("sub_xrisk_2023", "Alignment happens either transactionally, coercively, or because we discover shared purposes above the individual self, thereby creating shared agency together.", True),
   q("sub_age_2026", "We will have to build AI systems that can extend our wisdom, agents that find shared purposes with us.", True)])

I("Position on large language models",
  "2023 (Lex Fridman interview #392); restated in CIMC texts 2025-2026.",
  "Bach does not say current language models are conscious, and does not rule it out either. His stated view in 2023 is that if such a model is conscious, it is not in the way humans are, because it imitates text written by conscious people. CIMC's public note says chatbots are 'really good actors' that can play a conscious character, and that producing text about an experience is not having it. The 2025 essay says LLM agents 'tend to dream', meaning they do not separate perception from imagination. In 2026 he calls today's systems 'artificial idiot savants'. He and Sorensen also argue that no behaviour test can decide the matter.",
  [q("lex392", "If it’s conscious, it’s probably not conscious in a way that is closed to the way in which human beings are conscious", True),
   q("cs_chatbot_2025", "Being able to produce text about an experience does not imply that the model is actually having the experience it describes.", True),
   q("cs_chatbot_2025", "LLMs are essentially really good actors", True),
   q("mch_2025", "Current LLM based agents tend to dream and may need to learn the distinction between perception and imagination explicitly.", True),
   q("sub_age_2026", "Our first generation AGIs are artificial idiot savants that know nearly everything that has ever been written, yet are still prone to making stunning logical mistakes.", True)],
  note="The CIMC chatbot note is published under the byline 'CIMC', with no individual author named; it is CIMC's position, not a signed Bach text.")

I("No 'Turing Test' for consciousness",
  "2025 (essay with Sorensen).",
  "Bach and Sorensen argue that you cannot tell whether a system is conscious by watching what it does. Consciousness is a particular way of producing behaviour, and the same behaviour could be produced another way, as chatbots show. So the test has to look at how the system is built and how it works inside.",
  [q("mch_2025", "Consciousness is by its nature not an externally visible performance, but a particular way to achieve a performance", True),
   q("mch_2025", "Paraphrase: section heading 'Why there can be no “Turing Test for consciousness”'.")])

I("Motivated cognition: the Psi theory and MicroPsi",
  "2003 (first MicroPsi papers); book 2009.",
  "Bach's early work says a mind cannot be understood as a problem-solver alone. It needs built-in needs, such as food, safety, certainty, competence and belonging, that create goals, and emotions arise as changes in how the whole system processes information. He took this from Dietrich Dörner's Psi theory and built it as software called MicroPsi. Later papers extend the model of needs and connect it to personality.",
  [q("seven_2008", "MicroPsi [22, 23] is an implementation of Dietrich Dörner’s Psi theory of mental representation, information processing, perception, action control and emotion", True),
   q("psi_diss_2007", "Paraphrase: thesis chapters cover Dörner's blueprint for a mind, the Psi theory as a model of cognition, and the MicroPsi architecture."),
   q("cv_2023", "Paraphrase: CV lists 'The MicroPsi Agent Architecture' (ICCM-5, 2003) and the 2009 OUP book.")])

I("Seven principles of synthetic intelligence",
  "2008 (AGI-08 paper).",
  "A short list of lessons from fifty years of AI. Build whole architectures defined by function. Do not let your methods choose your questions. Aim for the big picture, not single experiments. Ground the system in an environment, but do not get stuck on the symbol grounding problem. Do not wait for robot bodies. Build autonomous systems with their own motives. Do not expect intelligence to emerge by itself.",
  [q("seven_2008", "Build whole functionalist architectures.", True),
   q("seven_2008", "Do not wait for the rapture of robotic embodiment", True),
   q("seven_2008", "The emergence of intelligence is not going to happen all by itself", True)])

I("Request Confirmation Networks (ReCoN)",
  "2015 (NIPS workshop paper with Priska Herger).",
  "A design for a neural network that can run step-by-step plans. Higher units send requests down to lower units, and lower units confirm or fail, so the network can check a hypothesis such as 'this is a face' by checking its parts in order. It is meant to join symbolic, script-like control with neural learning. CIMC lists it as one of its starting points for cognitive architectures.",
  [q("recon_2015", "ReCoNs are spreading activation networks with units that contain an activation and a state", True),
   q("cimc_site", "Paraphrase: the cognitive-architectures research direction names Request Confirmation Networks, Attention Schema Theory and Global Workspace Theory.")])

I("Attention-based learning: consciousness as a record of attention",
  "2018 (position paper; year from CV).",
  "Bach proposes that a system could learn by keeping a log of what its attention did and what came of it, and then adjusting only the parts that were involved. He suggests that producing this single integrated log may be what gives consciousness both its function and its felt quality.",
  [q("abl_2018", "The generation of an integrated protocol of the contents of an agent’s attention may also be responsible for the functionality and phenomenology of consciousness.", True)])

I("From elementary computation to ethics",
  "2016 (blog post).",
  "A 16-step sketch that starts with the universe as a reversible computation and works up through entropy, life, agency and minds to rules for living together. The aim is to show that values can be derived from an understanding of how systems work and do not have to be taken as given. The same thought returns in his 2023 essay, where he says values must be rationally derived and are not axioms.",
  [q("bachai_ethics_2016", "16 step path from elementary computation to normative regulation", True),
   q("bachai_ethics_2016", "The universe is probably a reversible computational process", True),
   q("sub_xrisk_2023", "Paraphrase: values 'cannot be treated as axiomatic, but have to be rationally derived from a systemic understanding of how our actions influence the set of possible futures'.")])
