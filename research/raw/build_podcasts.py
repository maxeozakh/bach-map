#!/usr/bin/env python3
"""Builds ../podcasts.json and checks every is_verbatim quote against the saved raw transcript."""
import json, re, os, sys

RAW = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(RAW), "podcasts.json")
P = "/Users/maksim.zakharov/mm/notes/bach-map/research/raw/"

SOURCES = [
 {"id":"lex101","title":"Lex Fridman Podcast #101 – Joscha Bach: Artificial Consciousness and the Nature of Reality","date":"2020","url":"https://podscripts.co/podcasts/lex-fridman-podcast/101-joscha-bach-artificial-consciousness-and-the-nature-of-reality","transcript_obtained":True,"raw_file":P+"lex101_podscripts.txt","notes":"Auto-generated transcript (PodScripts), no speaker labels, many mangled names."},
 {"id":"lex212","title":"Lex Fridman Podcast #212 – Joscha Bach: Nature of Reality, Dreams, and Consciousness","date":"2021","url":"https://podscripts.co/podcasts/lex-fridman-podcast/212-joscha-bach-nature-of-reality-dreams-and-consciousness","transcript_obtained":True,"raw_file":P+"lex212_podscripts.txt","notes":"Auto-generated transcript (PodScripts), no speaker labels, many mangled names."},
 {"id":"lex392","title":"Lex Fridman Podcast #392 – Joscha Bach: Life, Intelligence, Consciousness, AI & the Future of Humans","date":"2023","url":"https://lexfridman.com/joscha-bach-3-transcript","transcript_obtained":True,"raw_file":P+"lex392.txt","notes":"Human-generated transcript with speaker labels."},
 {"id":"rutt72","title":"The Jim Rutt Show EP72 – Joscha Bach on Minds, Machines & Magic","date":"2020-08-17","url":"https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-episode-72-joscha-bach-on-minds-machines-magic/","transcript_obtained":True,"raw_file":P+"rutt_ep72.txt","notes":"Official rough transcript with speaker labels. MicroPsi is rendered 'Micro-site'."},
 {"id":"rutt87","title":"The Jim Rutt Show EP87 – Joscha Bach on Theories of Consciousness","date":"2020-10-26","url":"https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-episode-87-joscha-bach-on-theories-of-consciousness/","transcript_obtained":True,"raw_file":P+"rutt_ep87.txt","notes":"Official rough transcript with speaker labels."},
 {"id":"ruttc083","title":"The Jim Rutt Show Currents 083 – Joscha Bach on Synthetic Intelligence","date":"2023-02-28","url":"https://jimruttshow.blubrry.net/the-jim-rutt-show-transcripts/transcript-of-currents-083-joscha-bach-on-synthetic-intelligence/","transcript_obtained":True,"raw_file":P+"rutt_currents083.txt","notes":"Official rough transcript with speaker labels."},
 {"id":"rutt334","title":"The Jim Rutt Show EP 334 – Worldviews: Joscha Bach","date":"2026-02-26","url":"https://www.youtube.com/watch?v=vbJr9HCcxkg","transcript_obtained":True,"raw_file":P+"rutt_ep334_youtube.txt","notes":"YouTube caption text, no speaker labels. Episode page: https://jimruttshow.blubrry.net/worldviews-joscha-bach/"},
 {"id":"mlst82","title":"Machine Learning Street Talk #82 – Dr. Joscha Bach: Digital Physics, DL and Consciousness [UNPLUGGED]","date":"2022","url":"https://www.youtube.com/watch?v=LgwjcqhkOA4","transcript_obtained":True,"raw_file":P+"mlst82_youtube.txt","notes":"YouTube auto-captions: lowercase, no speaker labels, heavily mangled names (Gödel appears as 'girdle', 'go Dell', 'Guru')."},
 {"id":"mlst2026","title":"Machine Learning Street Talk – Why Leibniz Couldn't Find the Mind Inside the Mill (Joscha Bach)","date":"2026-11-02","url":"https://www.youtube.com/watch?v=yW_ngvMFlYs","transcript_obtained":True,"raw_file":P+"mlst_leibniz_2026.txt","notes":"YouTube caption text, no speaker labels. The spoken.md transcript page for this episode only gave a paywalled preview."},
 {"id":"sfm2018","title":"Singularity.FM – Joscha Bach: We need to understand the nature of AI to understand who we are","date":"2018-11-14","url":"https://www.youtube.com/watch?v=sIKbp3KcS8A","transcript_obtained":True,"raw_file":P+"singularityfm_2018_youtube.txt","notes":"YouTube auto-captions, no speaker labels, mangled names. Episode page: https://www.singularityweblog.com/joscha-bach/"},
 {"id":"sfm2022","title":"Singularity.FM – Joscha Bach on AI, Cosmology, Existence and the Bible","date":"2022-06-15","url":"https://www.youtube.com/watch?v=vyGP8LpsDok","transcript_obtained":True,"raw_file":P+"singularityfm_2022_youtube.txt","notes":"YouTube auto-captions, all lowercase, no speaker labels. Episode page: https://www.singularityweblog.com/joscha-bach-ai/"},
 {"id":"manifold76","title":"Manifold #76 (Steve Hsu) – Joscha Bach: Consciousness and AGI","date":"2025-01-02","url":"https://www.manifold1.com/episodes/joscha-bach-consciousness-and-agi-76/transcript","transcript_obtained":True,"raw_file":P+"manifold76.txt","notes":"Official transcript with speaker labels; some names mangled (Zelazny as 'Zalesny'/'Elany', Fredkin as 'Shvetkin')."},
 {"id":"htlgi","title":"Why consciousness is software, and software is spirit | Joscha Bach | FULL INTERVIEW (HowTheLightGetsIn festival)","date":"2024","url":"https://www.youtube.com/watch?v=E361FZ_50oo","transcript_obtained":True,"raw_file":P+"software_spirit_E361FZ_50oo.txt","notes":"Short interview (about 4,000 words), YouTube auto-captions. Publication year not confirmed; 2024 is an estimate from context (Bach at Liquid AI, institute still being set up)."},
 {"id":"mlst2026_spoken","title":"spoken.md transcript page for MLST 'Why Leibniz Couldn't Find the Mind Inside the Mill'","date":"2026-11-02","url":"https://spoken.md/episode/why-leibniz-couldnt-find-the-mind-inside-the-mill-1000799321706","transcript_obtained":False,"raw_file":None,"notes":"Paywalled preview only; superseded by the YouTube caption text (source mlst2026)."},
]

REFS = []
def R(name, kind, author, year, tldr, take, mentions, verified=True, note=None):
    d = {"name":name,"kind":kind,"author":author,"year":year,"tldr":tldr,"bach_take":take,
         "mentions":[{"source_id":s,"quote_or_paraphrase":q,"is_verbatim":v} for (s,q,v) in mentions],
         "verified":verified}
    if note: d["note"] = note
    REFS.append(d)
V, PAR = True, False

# ───────────────────────── Antiquity and religious traditions ─────────────────────────
R("Aristotle","person",None,"4th c. BCE",
  "Greek philosopher who systematised logic, biology, physics and psychology. He treated the soul not as a ghost but as the organising principle of a living body, and described reasoning through syllogisms.",
  "Bach treats Aristotle as the origin of the scientific worldview and reads him as an animist in a modern, software-like sense. He also notes Aristotle's logic was only about 80% right.",
  [("mlst2026","So in some sense, Aristotle is an animist.",V),
   ("mlst2026","our today's scientific worldview is very much, invented by Aristotle and goes back to him",V),
   ("lex392","Even Aristotle who thought about this very hard and came up with a theory of how syllogisms works",V),
   ("rutt72","Bach says the notion of the feedback loop is already found in Aristotle.",PAR)])
R("De Anima (On the Soul)","book","Aristotle","c. 350 BCE",
  "Aristotle's treatise on the soul. It describes three levels: a vegetative soul (growth and nutrition, in plants), a sensitive soul (perception and desire, in animals) and a rational soul (in humans). The soul is the form of a living body and does not survive it.",
  "Bach uses it to argue that 'spirit' or 'psyche' originally meant a causal pattern that organises a body, which is what we now call software.",
  [("mlst2026","And when Aristotle writes in De Anima about the spirit, the animus, the soul, the psyche, he does not envision our psyche, our soul, as something that is immortal",V),
   ("mlst2026","He basically said there are three levels of souls in nature, and he basically said that plants have the lowest one.",V)])
R("Prime mover (unmoved mover)","concept","Aristotle","4th c. BCE",
  "Aristotle's argument that since everything in motion is moved by something else, there must be a first cause of motion that is not itself moved. Medieval theology identified this first cause with God.",
  "Bach reads the prime mover as the automaton that runs the universe and calls equating it with a supernatural being a sleight of hand.",
  [("lex101","the prime mover of Aristotle, which is basically the automaton that runs the universe",V),
   ("lex101","This idea to say that this prime mover is a supernatural being is complete nonsense.",V)])
R("Platonic forms","concept","Plato","4th c. BCE",
  "Plato's idea that the things we see are imperfect copies of ideal, abstract patterns (forms), such as the perfect circle or perfect justice.",
  "Bach borrows the term for ideal patterns that agents approximate: God as the Platonic form of a civilisation, and the soul as the ideal arrangement of a person's purposes.",
  [("lex101","the natural shape of God is the platonic form of the civilization that you are part of",V),
   ("rutt87","our true soul is the Platonic form, the ideal form of all these purposes arranged in the right hierarchy",V)])
R("Logos","concept","Greek philosophy (Heraclitus, Stoics)","5th c. BCE",
  "Greek term for the rational order or law that underlies the cosmos; later adopted by Stoics and by Christian theology ('In the beginning was the Word').",
  "Bach equates the Logos with the simplest self-existing mathematics from which the universe emerges, and links it to Wolfram's Ruliad.",
  [("mlst2026","this pattern of the Ruliad is exactly the superposition of all the automata that is producing the universe, or the old Greeks called it Logos",V)])
R("Stoicism","tradition","Zeno of Citium and successors","3rd c. BCE",
  "A school of philosophy teaching that we suffer from our judgments about events rather than the events themselves, and that we should concern ourselves only with what is in our control.",
  "Bach finds its core advice obvious and asks why almost nobody follows it; his answer is that stoicism is probably maladaptive from an evolutionary perspective.",
  [("sfm2018","I suspect that stoicism is maladaptive from a permanent evolutionary perspective",V),
   ("sfm2018","most cats I have known are stoics",V)],
  note="The host introduces Stoicism; Bach picks it up.")
R("Buddhism","tradition","Siddhartha Gautama","5th c. BCE",
  "A contemplative tradition that studies experience from the inside through meditation, teaching that the self is constructed and that suffering comes from attachment. Advanced practitioners report being able to deconstruct ordinary perception and selfhood.",
  "Bach credits Buddhist meditators with reaching the 'enlightenment' stage in which one sees how experience is constructed, but says Buddhism is limited to the inside perspective and is not interested in physics. In 2018 he was dismissive of its Western form and its metaphysics.",
  [("mlst2026","Buddhism to me is limited to this inside perspective",V),
   ("lex392","You most basically find this mostly with advanced Buddhist meditators and so on",V),
   ("sfm2018","I got to know Buddhism only in its um westernized forms",V),
   ("lex101","Bach compares the Catholic view of the mundane world to what Eastern philosophers call samsara.",PAR)])
R("Jainism","tradition",None,"6th c. BCE",
  "An Indian religion built around radical non-violence (ahimsa): harming any living creature should be avoided.",
  "Mentioned alongside Buddhism as a tradition that extends care to the suffering of other creatures once you identify with other agents.",
  [("manifold76","Buddhism and so on and Jainism the idea that suffering of other creatures should be avoided",V)])
R("Dalai Lama (reincarnating office)","concept","Tibetan Buddhism","15th c.",
  "In Tibetan Buddhism the Dalai Lama is held to be reborn in each generation; a child is identified as the successor and trained into the role.",
  "Bach's illustration that identity is a construct: the Dalai Lama identifies not as a human being but as a form of government that runs on successive humans.",
  [("lex101","He's basically a governmental software that is instantiated in every new generation",V),
   ("lex101","To kill the Dalai Lama, you have to kill his tradition.",V)])
R("Genesis 1 (creation story)","book","Hebrew Bible","c. 6th c. BCE",
  "The opening chapter of the Bible: a spirit hovers over formless waters, separates light from darkness and heaven from earth, makes plants, animals and finally humans in its own image.",
  "Bach reads it not as the creation of the physical universe but as a description of how a mind boots up: consciousness creating a world model and then a self inside it. He and co-author Hikari Sorensen wrote their own version in a paper.",
  [("lex392","I suspect that it’s there in plain sight in Genesis 1, in this first book of the Bible",V),
   ("lex101","I think that Genesis is actually the childhood memories of a God.",V),
   ("sfm2022","the entities that are being described in genesis are not entities of physics",V),
   ("mlst2026","Host: Bach and Hikari Sorensen 'wrote their own Genesis' in their paper (page 20), which he reads aloud.",PAR)])
R("Adam and Eve / Garden of Eden","concept","Hebrew Bible","c. 6th c. BCE",
  "The biblical story of the first humans living in a paradise without suffering until they eat from the tree of knowledge and are expelled.",
  "Bach says there are several non-literal readings that make sense; one is that Eden describes a phase of life (being happily in love) rather than a historical place.",
  [("sfm2022","there was no garden of eden that we ever lived in in which all the animals were vegetarians and there was no suffering",V)])
R("Tower of Babel","concept","Hebrew Bible","c. 6th c. BCE",
  "Biblical story in which humanity builds a tower to reach heaven until God confuses their languages so the builders can no longer understand each other.",
  "For Bach it is a founding myth about the collective project of understanding the universe (a metaphysical building, philosophy and science), and a metaphor for parts of a mind losing a shared protocol.",
  [("sfm2018","it's a metaphysical building that is being built",V),
   ("manifold76","not get subject to some kind of Tower of Babel",V)])
R("The Bible","book",None,"c. 8th c. BCE to 2nd c. CE",
  "The canonical scripture of Judaism and Christianity, a library of myths, laws, histories and poetry.",
  "Bach read it as a child to understand the canon of his society and thinks it contains real philosophical insights hidden by a simplistic literal interpretation.",
  [("manifold76","I forced myself through the Bible",V),
   ("sfm2022","the bible has a number of very interesting philosophical insights in it",V)])
R("Catholicism / the Catholic Church","tradition",None,"1st c. CE onward",
  "The largest Christian church, which organised European society for over a thousand years around shared doctrine, ritual and a notion of the sacred.",
  "Bach describes it as an operating system for society: software installed on minds to synchronise people into a larger agent ('God'), at the cost of damaging their epistemology and obscuring the study of mind.",
  [("lex101","the Catholics used a relatively crude methodology to implement software on the minds of people",V),
   ("rutt72","the Catholic civilization is one that obfuscated the area of the mind, because, it made it all part of a mythology",V),
   ("sfm2018","Bach says Catholics burned down and later imperfectly rebuilt the Greek and Roman 'cathedral' of understanding, leaving scars in our epistemology.",PAR)])
R("Protestantism","tradition","Martin Luther and others","16th c.",
  "The branch of Christianity that emerged from the Reformation, stressing the individual's direct relationship to God and personal conscience.",
  "Bach says most atheists he knows are 'super Protestants' who still serve a sacred greater whole, and he calls Miyazaki the most relevant Protestant philosopher today.",
  [("ruttc083","most atheists that I know are actually super Protestants",V),
   ("lex212","makes Miyazaki into the most relevant Protestant philosopher today",V)])
R("Thomas Aquinas","person",None,"13th c.",
  "Medieval Catholic philosopher who merged Aristotle with Christian theology in the Summa Theologiae.",
  "Bach re-read Aquinas as a rational designer of an 'operating system' for Catholic society, not a dualist, and asks how his rules for cooperating agents could apply to AI alignment.",
  [("ruttc083","a philosopher who thought deeply about this was Thomas Aquinas, foremost philosopher of Catholicism",V),
   ("lex101","I recently re-read Thomas O'Kynes.",V),
   ("sfm2022","starting out with re-reading and reconsidering aquinas",V)],
  note="lex101 auto-transcript renders Aquinas as 'Thomas O'Kynes'; context (Aristotle, Catholic society, virtues) makes the resolution clear.")
R("Seven virtues (four cardinal, three theological)","concept","Thomas Aquinas (after Plato, Aristotle, St Paul)","13th c.",
  "The classical list of prudence, justice, temperance and courage, plus the Christian faith, hope and love.",
  "Bach decodes them as policies for agents that must cooperate: temperance is internal regulation, justice is regulation between agents, prudence is picking the right goals, courage is acting on your models; faith, hope and love are commitments to a shared higher-level agent. He proposes love (shared purpose) as an answer to AI alignment.",
  [("lex101","they are additionally 02:30:57 to these four cardinal virtues, three divine virtues",V),
   ("ruttc083","you should optimize your internal regulation, which he calls temperance",V),
   ("lex101","The commitment to shared purpose is the core of love.",V)])
R("Animism","tradition",None,"prehistoric",
  "The widespread belief that living things (and sometimes places and objects) are inhabited by spirits that make them act.",
  "Bach argues animism is close to the truth if 'spirit' is read as self-organising agentic software; spirits need not be supernatural.",
  [("mlst2026","All cultures outside of ours are animist cultures",V),
   ("mlst2026","The spirit doesn't have to be supernatural.",V),
   ("rutt72","it’s an old word that just means operating system for an autonomous robot",V)])
R("God as a collective agent","concept","Joscha Bach (reinterpreting monotheism)","2020s",
  "The proposal that 'God' names the agent that emerges when many individuals coordinate around a shared highest purpose, the way cells form an organism.",
  "This is Bach's own secular reading of religion: gods are selves that span many minds, and the single God is the global optimum of collective agency.",
  [("rutt334","the global optimum of collectively enacted agency has a name. We call this God.",V),
   ("lex101","It's basically the super organism that is formed by the individuals as an intentional agent.",V)])
R("Golem","fiction","Jewish folklore","16th c. (Prague legend)",
  "A creature of clay brought to life by inscribed words, which carries out instructions literally and without judgment.",
  "Bach's image for language models and paperclip maximisers: machines that execute a task with nobody home. In 2026 he also describes chips as sand etched by 'alchemists' on which golem-like minds emerge.",
  [("lex392","My intuition is that the language models that we are building are golems.",V),
   ("mlst2026","there are minds emerging on them that are like golems, and we can talk to them",V)])
R("Qigong","tradition","Chinese contemplative practice","ancient",
  "A Chinese system of breathing, movement and attention exercises said to cultivate 'qi' energy.",
  "Used as an example of reported telepathy-like abilities that Bach thinks might be explained by rethinking neuroscience rather than physics.",
  [("manifold76","if you talk to a Qigong practitioner in China who is cultivating his key energy",V)])

# ───────────────────────── Early modern to 19th century ─────────────────────────
R("René Descartes and the Meditations","person",None,"1641",
  "French philosopher famous for 'I think, therefore I am' and for dividing reality into extended stuff (res extensa) and thinking stuff (res cogitans), the classic statement of mind-body dualism.",
  "Bach suspects Descartes was smarter than his reputation and wrote some religious arguments under political pressure. He reinterprets the two substances as two kinds of mental representation: the spatial world model and the realm of ideas.",
  [("rutt72","he is often smarter than people give him credit for",V),
   ("rutt72","So res extensa is the thing, that for instance, Jeff Hawkins at Numenta, is so obsessed with.",V),
   ("sfm2022","Bach maps Genesis's two worlds onto res extensa and res cogitans (captioned as 'res extensor and dress cognitions').",PAR)])
R("Occasionalism","theory","Malebranche and other Cartesians","17th c.",
  "A post-Cartesian doctrine that mind and body never directly interact; God causes the matching events on each side on every occasion.",
  "Bach cites it as evidence that the generation after Descartes simplified his thinking when trying to explain how a causally closed physical world could interact with a mental one.",
  [("rutt72","that is especially apparent when you look at Occasionalism",V)])
R("Leibniz's mill","concept","Gottfried Wilhelm Leibniz (Monadology)","1714",
  "A thought experiment: enlarge a thinking machine to the size of a mill and walk inside; you will see only parts pushing each other and nothing that explains perception.",
  "Bach says the intuition fails because it looks at the wrong level: mind is a causal pattern (software) over the parts, not the parts themselves. It is the title theme of his 2026 MLST interview.",
  [("mlst82","leibniz says this idea of imagine you could have a Mill and this this is your mind",V),
   ("mlst2026","What is a causal pattern? Right? We call it software.",V)])
R("Julien Offray de La Mettrie (Man a Machine)","person",None,"1747",
  "French physician-philosopher who argued that humans are machines and that mental life arises from bodily mechanisms.",
  "Cited as an early appearance of the feedback-loop idea: competing springs in the mind that keep it in dynamic balance.",
  [("rutt72","we find it in La Mettrie, where he describes that, there must be systems of competing springs in the mind",V)])
R("German Romanticism","tradition",None,"c. 1800",
  "A literary and artistic movement that prized nature, feeling, longing and the individual imagination, partly in reaction to Enlightenment rationalism.",
  "Bach names the literature of Romanticism and German poetry as a formative influence, and says he grew up in a region of Thuringia shaped by it.",
  [("lex101","the classical philosophers and also the literature of romanticism",V),
   ("sfm2018","it's an area of German Romanticism which had a pretty big influence on how I grew up",V)],
  note="lex101 lists authors as 'Druster Hildeshoff andainer and Up to Hesse'; the first is almost certainly Annette von Droste-Hülshoff, the second is unresolved (possibly Heine or Eichendorff). Hermann Hesse is named, but it is unclear whether by Bach or the host.")
R("Undine and The Little Mermaid","fiction","Friedrich de la Motte Fouqué; Hans Christian Andersen","1811; 1837",
  "Two versions of the water-spirit tale. In the older Undine story the water woman kills the unfaithful prince with a kiss; in Andersen's version the mermaid gives up her voice and finally her life for love.",
  "Bach tells both to his children instead of the Disney version, and uses them to say the mermaid is right: you sacrifice for romantic love. He also uses 'sirens eat people' as a parable about loving something that does not share your purposes.",
  [("lex101","And I think that the mermaid is right. You sacrifice your life for romantic love.",V),
   ("sfm2018","The Little Mermaid is a siren Sirens eat people",V)],
  note="'Anderson' in the transcript is Hans Christian Andersen; 'Undin' is Undine.")
R("Oscar Wilde","person",None,"1890s",
  "Irish writer of plays, fairy tales and aphorisms, associated with aestheticism and tragic romantic stories.",
  "Bach says reading Wilde early 'inoculated' him with romanticism.",
  [("lex101","I read Oscar Wilde before I read the other things",V)])
R("Heidi","fiction","Johanna Spyri","1881",
  "Swiss children's novel about an innocent orphan girl in the Alps whose goodness transforms the people around her.",
  "Bach reads Heidi as an embodiment of European Protestantism: a pure being committed to serving God whom civilisation exists to protect.",
  [("lex212","Heidi is an embodiment of this spirit of European Protestantism",V)])
R("Friedrich Nietzsche","person",None,"1880s",
  "German philosopher who attacked conventional morality and religion and announced the 'death of God'.",
  "Bach is irreverent: Nietzsche is smart and readable but took himself too seriously and ended in tragedy.",
  [("lex101","I think that Nietzsche is the classical equivalent of a shit poster.",V)])
R("Karl Marx on capitalism's crises","theory","Karl Marx","1867",
  "Marx argued that capitalism is inherently unstable: its own dynamics produce recurring crises even as it creates enormous productivity.",
  "Bach agrees with this diagnosis (capitalism is divergent, not convergent) while rejecting communism and anarchism as solutions.",
  [("lex212","I think that Marx was correct in saying that capitalism is prone to crisis.",V)])
R("Charles Darwin as 'the last philosopher'","person","Charles Darwin (remark attributed to Mikhail Gromov)","1859",
  "Darwin's theory of evolution by natural selection explained the design of living things without a designer.",
  "Bach relays a remark by the mathematician Misha Gromov that Darwin was the last person able to connect the dots in a completely fresh way; Bach himself thinks some philosophy is still being done, mostly in the foundations of mathematics.",
  [("sfm2018","Misha gromov once told me he's a mathematician that in his perspective Darin was the last philosopher",V)],
  note="Auto-caption says 'Darin'; resolved to Darwin from context with moderate confidence.")
R("Jürgen Habermas and dialectical materialism","person",None,"20th c.",
  "Habermas is the leading post-war West German social philosopher; dialectical materialism was the official Marxist philosophy of East Germany.",
  "Bach's point is that after the Nazi era both Germanies lost their rigorous philosophical tradition.",
  [("lex101","Western Germany didn't get much more edgy than Habermass",V)])

# ───────────────────────── Logic, mathematics, computation ─────────────────────────
R("Cantor's set theory and its paradoxes","theory","Georg Cantor","1870s–1890s",
  "Cantor built mathematics on sets and showed there are different sizes of infinity. Naive set theory then produced paradoxes such as a total set that must contain all of its own subsets.",
  "Bach's starting point for why infinities break mathematics: the contradictions show classical mathematics cannot be run without 'crashing'.",
  [("sfm2018","Hilbert stumbled on counter set theoretic uh experiments to deal with natural numbers",V),
   ("lex101","Hilbert saw that, for instance, a country's sets here where the experiments and mathematics led into contradictions.",V)],
  note="'counter set theoretic' and 'a country's sets here' are auto-caption manglings of 'Cantor's set-theoretic' / 'Cantor's set theory'.")
R("Hilbert's program","concept","David Hilbert","1920s",
  "Hilbert's call to put all of mathematics on a secure footing by finding a complete, consistent set of axioms and mechanical rules of proof.",
  "For Bach this was the bug report that led Gödel and Turing to discover that only the computable part of mathematics works.",
  [("mlst2026","All these issues led Hilbert to saying, please mathematicians, there seems to be something wrong here.",V),
   ("lex212","which is in some sense what Grydol and Turing discovered in response to Hilbert's call",V)])
R("Principia Mathematica","book","Bertrand Russell and Alfred North Whitehead","1910–1913",
  "A monumental attempt to derive all of mathematics from logic, using a hierarchy of types to block self-referential paradoxes.",
  "Bach says their restriction was too strong (we do think in loops) and that Gödel showed the attempt was insufficient anyway.",
  [("mlst2026","Russell and Whitehead and Principia Mathematica were attempting to do this by limiting set theory",V)])
R("Peano axioms","concept","Giuseppe Peano","1889",
  "A handful of axioms that define the natural numbers and arithmetic from zero and a successor operation.",
  "Bach uses them to explain Gödel's method (arithmetic emulating logic) and notes that even 'zero' needs a number system, so non-existence is not a free default.",
  [("mlst2026","He basically built an emulator using Peano arithmetic to express a logical language.",V),
   ("sfm2022","Bach: once you have Peano's axioms (captioned 'pianos axioms') you have a Turing-complete system from which a universe could be built.",PAR)])
R("Gödel's incompleteness theorems","theory","Kurt Gödel","1931",
  "Gödel showed that any consistent formal system rich enough for arithmetic contains true statements it cannot prove, by making the system talk about itself.",
  "Bach's distinctive reading: Gödel did not find a limit of computation but a bug in classical, stateless mathematics with infinities. The fix is to use only constructive (computable) mathematics. He stresses that Gödel himself, a Platonist, was shocked by the result.",
  [("mlst2026","And what Gödel has discovered is that these bugs cannot be eliminated except by redefining the programming language of mathematics.",V),
   ("rutt87","And what Gödel has shown in my view is that constructive mathematics is real",V),
   ("lex101","It basically 16:02 shook his world to the core",V),
   ("mlst82","girdle was a true realist that is he thought that truth really exists out there",V)],
  note="Gödel appears as 'Gurdl' (lex101), 'Grydol' (lex212), 'girdle'/'Guru' (mlst82).")
R("Constructive mathematics and intuitionism","theory","L. E. J. Brouwer and later constructivists","1907 onward",
  "A school of mathematics that accepts an object only if you can give a procedure to construct it, rejecting proofs that merely assert existence and treating infinity as a never-finished process.",
  "Central to Bach's worldview: constructive mathematics is 'the part of maths that works' and is the same thing as computation. Computationalism is a form of constructivism, and physics borrowed non-constructive mathematics before this was understood.",
  [("rutt72","constructive mathematics is the part of maths that works and it happens to be the same as computation",V),
   ("rutt87","And constructive mathematics is roughly the same thing as computation.",V),
   ("mlst2026","I think in classical mathematics, the first formulation was Intuitionism.",V)],
  note="Brouwer is not named in the transcripts; the 2026 transcript says 'I don't think that he formulated it very well' without a clear name.")
R("Alan Turing and the Turing machine","person",None,"1936",
  "Turing defined computation with an abstract machine that reads and writes symbols on a tape, and showed that one universal machine can run any program.",
  "For Bach, Turing understood what Gödel did not: mathematics was computation all along. He also holds that minds are in the class of universal computers, with finite resources.",
  [("lex101","I think that Turing could see that the solution is to understand that the question mathematics was computation all along",V),
   ("rutt87","as long as brains are Turing complete, you can build minds on different substrates",V)])
R("Church–Turing thesis","theory","Alonzo Church and Alan Turing","1936",
  "The claim that every reasonable model of computation can compute the same things, so any computer can emulate any other given enough time and memory.",
  "Bach's main weapon against substrate-based theories of consciousness, especially IIT: an emulation produces the same reports, so consciousness cannot depend on the physical layout.",
  [("mlst2026","It's the insight that every computer can emulate every other computer.",V),
   ("ruttc083","So, in some sense IIT is not compatible with the Church-Turing thesis",V)])
R("Computing Machinery and Intelligence (the Turing test)","paper","Alan Turing","1950",
  "Turing proposed replacing 'can machines think?' with an imitation game: if a machine's conversation cannot be told apart from a human's, treat it as intelligent. The paper also discusses objections, including one from telepathy.",
  "Bach notes that Turing took telepathy seriously, and that the Turing test is about performance and so cannot test for consciousness. A true test would be an AI that explains how AI works.",
  [("lex392","Turing’s famous 1950 paper in which he describes the Turing test, he does speculate about telepathy",V),
   ("mlst2026","Turing's test does not care about how you produce the dialogue",V),
   ("manifold76","I think that a true Turing test would require that an AGI explains how AGI works.",V)])
R("Lambda calculus, Lisp and rewrite systems","concept","Alonzo Church; John McCarthy","1936; 1958",
  "A way of defining computation as repeated search-and-replace on expressions rather than a machine stepping along a tape. Lisp is the programming language built on it.",
  "Bach has come to see rewrite systems as the most general view of computation, with the Turing machine as a special deterministic case; a branching rewrite system gives a multiverse.",
  [("ruttc083","The Turing machine is a very special case of a rewrite system.",V),
   ("mlst82","the Lambda calculus and the turing machine turn out to have the same power",V)])
R("Ludwig Wittgenstein","person",None,"1921–1953",
  "Austrian philosopher. His early work tried to define exactly what can be said in a logical language; his later work argued that meaning comes from how language is used in life.",
  "Bach says Wittgenstein pre-empted the logicist program of AI by decades and anticipated Turing's universality (logic from NAND gates). He sides with the late Wittgenstein: language is not fundamental to cognition, and images/perception were the unsolved part.",
  [("lex101","Wittgenstein basically preempted the logitist program of AI that Minskie started 17:09 later",V),
   ("lex101","I agree with Wittgenstein. I just agree with the late Wittgenstein.",V),
   ("lex101","Turing was actually a pupil of Wittgenstein.",V)],
  note="'non-calculus'/'non-gates' in the transcript are NAND; 'Vidkins stands' is Wittgenstein.")
R("Tractatus Logico-Philosophicus","book","Ludwig Wittgenstein","1921",
  "A short, numbered treatise that tries to state the limits of what can be meaningfully said by treating language as a logical picture of facts.",
  "Bach calls it probably the most beautiful philosophical text of the 20th century: an attempt to turn philosophy into a logical programming language.",
  [("lex101","I think that the track titles itself is probably the most beautiful philosophical text that was written in the 20th century.",V)],
  note="Auto-transcript renders Tractatus as 'attractados', 'tractatos' and 'track titles'.")
R("Philosophical Investigations","book","Ludwig Wittgenstein","1953",
  "Wittgenstein's late work, which abandons the idea of one logical language and looks at meaning as use in 'language games'.",
  "Bach says it shows the problem Wittgenstein could not solve: how images (perceptual representations) relate to language.",
  [("lex101","he looked at this in his book at the end of his life, philosophical investigations, was the notion of images",V)])
R("Frege and Tarski on formal reasoning","person","Gottlob Frege; Alfred Tarski","1879; 1930s",
  "Frege invented modern predicate logic; Tarski gave the standard formal definition of truth for logical languages.",
  "Named as the foundation of how reasoning is professionally understood today, in an argument that humans, like LLMs, learn to reason by emulating what others wrote about reasoning.",
  [("lex392","The people that are talking about reasoning professionally today Tarski and Frege and build on their work.",V)])
R("John von Neumann (architecture and self-replicating probes)","person",None,"1940s",
  "Von Neumann designed the standard stored-program computer architecture and worked out the theory of self-replicating machines, the basis of the 'von Neumann probe' idea for exploring space.",
  "Bach calls the cell a possible von Neumann probe, and uses 'von Neumann computer' when describing Tononi's claim that ordinary computers cannot be conscious.",
  [("lex101","So in a way, it's tempting to think of the cell as a von Neumann probe.",V),
   ("manifold76","But a von Neumann computer can never be conscious.",V)],
  note="The manifold76 quote is Bach reporting Tononi's position, not his own.")
R("Claude Shannon on computer chess","paper","Claude Shannon","1950",
  "Shannon's paper 'Programming a Computer for Playing Chess' distinguished between searching all moves to a fixed depth and selectively exploring promising lines.",
  "Bach uses the two strategies (careful long plan versus brute force) as an analogy for human thinking versus LLMs brute-forcing thought.",
  [("lex392","Claude Shannon had this… When you describe chess suggested that there are two main strategies in which you could play chess.",V)],
  note="Bach does not name the paper; attribution to the 1950 chess paper is my inference.")
R("Solomonoff induction","theory","Ray Solomonoff","1964",
  "A mathematical ideal of learning: predict what comes next by weighting every program that could have produced your past observations, favouring shorter ones. It ties prediction to data compression.",
  "Cited as an old precursor to the idea that next-token prediction (compression) can amount to intelligence.",
  [("lex392","Solomonoff induction where you are trying to understand intelligence as predicting future observations from past observations",V)])
R("Mandelbrot set","concept","Benoît Mandelbrot","1980",
  "A famously intricate fractal generated by iterating a two-line formula over the complex plane.",
  "Bach's analogy for physics: an observer living inside the fractal sees spirals and local regularities and must infer the tiny generator function behind them.",
  [("lex101","But imagine you live inside of this fractal and you don't have access to where you are in the fractal",V)],
  note="Transcript renders it as 'Mandelberg Tracto ... Bona Mandelberg'.")
R("Boltzmann machine","theory","Geoffrey Hinton, Terrence Sejnowski, David Ackley","1985",
  "A neural network in which units constrain each other and the whole settles into a low-energy state consistent with the inputs. The restricted version (RBM) drops within-layer links to make training feasible and helped launch deep learning.",
  "Bach treats it as the most general early formulation of a mental model (parameters constraining each other) and says transformers get back to this idea from another angle.",
  [("rutt72","the original work, for instance, by Hinton and Sejnowski and Ackley on Boltzmann machines",V),
   ("lex101","I think some of the earliest formulations is the Boltzmann machine",V),
   ("sfm2022","Bach describes the mind's model as parameters with computable constraints, 'some boltzmann machine', an idea discovered early in computer science.",PAR)])
R("Boltzmann brain","concept","after Ludwig Boltzmann","1890s; named 2000s",
  "A thought experiment from physics: a random fluctuation could briefly assemble a brain with false memories, which might be more probable than a whole ordered universe.",
  "Bach distinguishes it from his simulation speculations: a Boltzmann brain exists for one frame, whereas we remember a long sequence of states, which makes it very unlikely.",
  [("manifold76","Boltzmann brain is only there for one tick, for one frame, and then it falls apart again",V)],
  note="Raised by host Steve Hsu; Bach engages.")
R("Roger Penrose's Gödelian argument","theory","Roger Penrose (The Emperor's New Mind; Shadows of the Mind)","1989",
  "Penrose argues that human mathematicians can see truths no algorithm can prove, so the mind is not a computer and must rely on new physics (quantum gravity).",
  "Bach thinks Penrose draws the wrong lesson from Gödel: the uncomputable parts of mathematics were never real, and minds only manipulate finite symbols for infinity. He rates quantum-brain theories as improbable.",
  [("rutt87","And Penrose thinks that computation cannot explain all of consciousness. And I think it’s because of this way he interprets Gödel’s proof.",V),
   ("sfm2018","Penrose thinks that our mind is mathematical that it can do things that the computer cannot do",V),
   ("mlst82","I think that Penrose belief that our brain is actually doing these infinite things and it's not",V)])
R("Orchestrated objective reduction (Orch OR)","theory","Stuart Hameroff and Roger Penrose","1990s",
  "The proposal that consciousness arises from quantum processes in microtubules inside neurons.",
  "Bach likes Hameroff personally but calls the theory a 'psychedelic sculpture garden' that explains ever more with the same mechanism and has little resonance in science.",
  [("rutt87","Hameroff is building a psychedelics sculpture garden with his theory",V)])
R("Stephen Wolfram, digital physics and the Ruliad","person",None,"2002–2021",
  "Wolfram proposes that physics emerges from simple rewriting rules applied to a discrete structure. The Ruliad is his name for the limit of all possible computations run in all possible ways.",
  "Bach agrees with Wolfram that space is not fundamentally continuous and that the universe is like a branching (non-deterministic) computation; he identifies the Ruliad with the superposition of all automata.",
  [("lex212","I tend to agree with people like Stephen Wolfram who are very skeptical of the geometric notions",V),
   ("ruttc083","Stephen Wolfram believes, I agree with him, that our universe is such a non-deterministic Turing machine",V),
   ("rutt72","Stephen Wolfram, who understood things at 22 that I understood in my forties",V)],
  note="In the 2026 MLST episode the host introduces the Ruliad and Bach endorses the mapping (see Logos entry).")
R("Ed Fredkin and the universe as computation","person",None,"1970s onward",
  "Fredkin was a pioneer of digital physics, the idea that the universe is fundamentally a discrete computation.",
  "Bach met him late in his life and reports Fredkin's conviction that our universe has too many parameters to be random and probably runs on a server farm in a parent universe. Bach himself does not think the physical universe looks simulated.",
  [("manifold76","he actually believed that the physical universe is probably in some server farm in the parent universe",V)],
  note="Transcript says 'Ed Shvetkin'; resolved to Ed Fredkin from context (digital physics, recently deceased).")
R("Simulation hypothesis","theory","Nick Bostrom (and earlier science fiction)","2003",
  "The idea that our universe might be a computer simulation run by some more basic civilisation.",
  "Bach separates it from his own computationalism: saying the universe is computational does not mean someone is running it. What is simulated is the world we experience, which our brain generates.",
  [("rutt334","this is not necessarily the case. Computation is a very general notion.",V),
   ("mlst2026","So it's not some simulation hypothesis.",V),
   ("lex101","Bach's line quoted by the host: a physical system cannot be conscious, only a simulation can.",PAR)])
R("Yoshua Bengio's consciousness prior","paper","Yoshua Bengio","2017",
  "A proposal that conscious thought corresponds to a small, sparse set of high-level variables selected by attention from a much larger unconscious state.",
  "Bach mentions it approvingly as a description of how a world model can be expressed with an energy function that measures its contradictions.",
  [("lex212","the idea of the consciousness prior that would be built into such a system by Yoshe Abangio",V)],
  note="'Yoshe Abangio' is Yoshua Bengio.")
R("Donald Hoffman's interface theory of perception","theory","Donald Hoffman","2010s",
  "Hoffman argues evolution shaped perception to be a useful 'desktop interface', not a true picture of reality, so what we see may be nothing like what is there.",
  "Bach's reply to Lex: a model can only drift from reality 'if you have tenure'; as long as you interact with the ground truth, your model must stay predictive.",
  [("lex212","I think that only works if you have tenure, as long as you're still interacting with the ground",V)],
  note="Raised by the host in both lex101 and lex212; Bach responds in lex212.")
R("Max Tegmark","person",None,"2010s",
  "MIT physicist known for the mathematical universe hypothesis and for work on physics-based theories of consciousness.",
  "Mentioned as the reason IIT gets attention among physicists.",
  [("rutt87","Max Tegmark has decided to make this one of his planks in his boat",V)])

# ───────────────────────── AI and cognitive science ─────────────────────────
R("Cybernetics and control theory","theory","Norbert Wiener and others","1948",
  "The study of systems that regulate themselves through feedback: a controller measures the gap between a variable and its set point and acts to reduce it.",
  "A foundation of Bach's thinking. He defines an agent as a controller with a set-point generator, sees motivation as nested feedback loops, and regrets that Minsky helped end cybernetics as a field in the US.",
  [("lex212","The notion of a controller comes from cybernetics and control theory.",V),
   ("lex212","they're basically cybernetic feedback loops",V)])
R("Founding of AI (Dartmouth, McCarthy and Minsky)","concept","John McCarthy, Marvin Minsky and others","1956",
  "The 1956 Dartmouth workshop launched artificial intelligence as a field, with the optimistic aim of making machines that think like humans.",
  "Bach stresses that the founders wanted what is now called AGI, as a way to understand the mind, and that the field later retreated to narrow, fundable applications.",
  [("ruttc083","Because Minsky and McCarthy and others of course wanted to build AGI from the start",V),
   ("rutt72","they basically thought this is going to be an extended summer project",V)])
R("Marvin Minsky","person",None,"1950s–2000s",
  "Co-founder of AI at MIT, champion of symbolic approaches and of the view that the mind is built from many simple interacting processes.",
  "Bach admires him as a visionary but thinks he bet wrongly on symbolic AI and delayed neural networks and cybernetics by more than a decade. He also says there are few Minskys today because institutions do not welcome them.",
  [("rutt72","When Minsky claimed that cognitive AI was in some sense, the same thing as symbolic AI, I think he made the wrong bet.",V),
   ("sfm2022","minsky was a part of a different era he was part of the modernist era of ai",V)])
R("Perceptrons","book","Marvin Minsky and Seymour Papert","1969",
  "A book proving that single-layer neural networks cannot learn some simple functions such as XOR; it was widely read as showing neural networks were a dead end.",
  "Bach's example of a wrong argument that cut off funding for a whole approach; people later found a way around it.",
  [("mlst82","Marvin Minsky wrote a book where he thought he had proven that the neural networks cannot converge over multiple layers",V)],
  note="Bach does not name the book; identification as Perceptrons is from context (XOR).")
R("The Society of Mind and K-lines","book","Marvin Minsky","1986 (K-lines 1980)",
  "Minsky's theory that a mind is a society of many small mindless agents. K-lines ('knowledge lines') are connections that reactivate the set of agents that were active when something was learned.",
  "Bach thinks future transformer-like systems will rediscover K-lines as an integrated attention hierarchy, and uses 'society of mind' when asking how autonomous agents can cooperate.",
  [("sfm2022","future developments of the transformer algorithms are going to rediscover minsky's ideas of the k lines",V),
   ("ruttc083","how can you make a society of mind out of multiple agents that are autonomous?",V)])
R("Pandemonium model","theory","Oliver Selfridge","1959",
  "An early model of perception as a crowd of 'demons', each shouting when it detects its pattern, with higher demons listening for the loudest.",
  "Bach points out that Dennett's pandemonium picture of mind goes back to Selfridge, Minsky's teacher, and explains it as behaviours on a stage evaluated by an audience of other behaviours.",
  [("rutt87","The pandemonium theory by the way goes back to Selfridge",V)])
R("Cyc","concept","Douglas Lenat","1984",
  "A decades-long project to hand-code millions of common-sense facts and rules into a logic system so that a computer could reason about everyday life.",
  "Bach's example of the hand-built, logic-based route to AI inspired by Minsky: useful but brittle, and overtaken by end-to-end learning.",
  [("ruttc083","I think an approach like psych is useful, it does not have the same power as an end-to-end train system",V),
   ("lex101","And project that was inspired by him was psych.",V)],
  note="Both transcripts spell Cyc as 'psych'.")
R("Cognitive architectures (Soar, ACT-R)","concept","Allen Newell, John Laird; John R. Anderson","1980s",
  "Software frameworks that try to model the whole mind (memory, perception, goals, learning) in one system rather than solving single tasks.",
  "Bach places his own work in this tradition, which he says came from psychology under the influence of cybernetics.",
  [("rutt72","The cognitive architectures are a tradition that mostly originated in psychology",V)],
  note="Soar and ACT-R are named by the host; Bach answers about the tradition. Bach separately mentions John Laird in passing.")
R("Dietrich Dörner and Psi theory","theory","Dietrich Dörner","1990s (Bauplan für eine Seele, 1999)",
  "A German psychologist's theory of the mind as a motivated control system: a set of physiological, social and cognitive needs create urges, and emotions are ways the system modulates its own processing.",
  "The basis of Bach's PhD work and his MicroPsi architecture. In 2020 he still called it one of the best theories of affect and motivation.",
  [("rutt72","Dietrich Dörner is a German psychologist, a cybernetician strongly influenced by these ideas",V),
   ("rutt87","the psi theory I think is still one of the best theories today",V)])
R("Principles of Synthetic Intelligence / MicroPsi","book","Joscha Bach","2009",
  "Bach's book formalising Dörner's Psi theory as a cognitive architecture (MicroPsi) in which agents are driven by needs and emotions emerge from how cognition is modulated.",
  "His own early work, which he spent about a decade on; the hosts use it to introduce him.",
  [("rutt72","I spent almost a decade with that.",V),
   ("rutt334","Host: Ben Goertzel recommended the book to Jim Rutt, which is how he discovered Bach.",PAR)],
  note="rutt72 transcript renders MicroPsi as 'Micro-site' and 'micro-PSI'.")
R("Stanisław Lem","person",None,"1950s–1980s",
  "Polish science-fiction author and philosopher who wrote about cybernetics, artificial minds and the limits of human understanding.",
  "A major early influence on Bach; he says Lem chose philosophical science fiction as the way to have the most influence on thinking about AI and cybernetics.",
  [("lex101","basically the great author of Cybernetics has influenced me",V),
   ("rutt72","Bach says Lem (a friend of someone in Dörner's circle) became a philosophical science-fiction author to be free of the constraints of academia.",PAR)],
  note="lex101 renders the name as 'LaFlem'; rutt72 has an inaudible gap before 'until Lem died'. Resolution is confident.")
R("Summa Technologiae","book","Stanisław Lem","1964",
  "Lem's non-fiction survey of future technologies, including artificial intelligence, virtual reality and directed evolution.",
  "Bach cites an argument in it against psi phenomena: if precognition were real, casinos and lotteries would not keep winning.",
  [("rutt87","It’s an argument that for instance has been made by Stanislaw Lem in I think Summa Technologiae",V)])
R("Solaris","fiction","Stanisław Lem","1961",
  "A novel about scientists orbiting a planet covered by an ocean that turns out to be a single vast, incomprehensible mind.",
  "Used as an image for a planet-sized intelligence that forms spontaneously and might seed other worlds with cells.",
  [("lex101","I am a thinking a thinking planet",V)],
  note="Transcript reads 'lambs Solaris', i.e. Lem's Solaris.")
R("Ian Witten and cognition as data compression","person",None,"1980s–1990s",
  "New Zealand computer scientist who co-developed arithmetic coding and prediction-based text compression; the idea is that to compress data well you must predict it, which requires modelling its structure.",
  "Bach worked in Witten's lab in the 1990s, where he tried to learn grammar from statistics, and credits him with an underestimated influence on modern AI.",
  [("rutt87","He’s the father of arithmetic coding. And he takes the data compression perspective on cognition.",V),
   ("lex212","I had an amazing professor, Ian Witten, who realized I was bored in class",V)])
R("Large language models and the transformer","concept","Vaswani et al.; OpenAI","2017–2020s",
  "Neural networks trained to predict the next token of text, built on the transformer architecture, whose 'attention' mechanism learns which earlier tokens matter for each prediction.",
  "Bach finds them astonishingly capable yet 'brutalist': they brute-force thought by imitating its traces. He does not see proof they cannot reach general intelligence, but thinks they lack real-time learning and a unified self-directed attention.",
  [("lex392","They are basically brute forcing the problem of thought.",V),
   ("mlst82","deep learning is ugly it's brutalist",V),
   ("rutt87","From my perspective there are at least three obvious things that are wrong with GPT-3.",V)])
R("Deep Learning Is Hitting a Wall","paper","Gary Marcus","2022",
  "An essay arguing that pure deep learning has stalled and must be combined with symbolic reasoning.",
  "Bach is sympathetic to wanting more elegant models but says Marcus's arguments are weak: so far the answer to deep learning's problems has always been more deep learning.",
  [("mlst82","the solution to uh problems with deep learning so far has always been to use more deep learning not less",V)])
R("François Chollet on intelligence as skill acquisition","theory","François Chollet (On the Measure of Intelligence)","2019",
  "Chollet defines intelligence as the efficiency of acquiring new skills, not the possession of skills, and argues that current models mostly interpolate between things they have seen.",
  "Bach partly agrees (a deployed skill is not intelligence) but questions the interpolation critique, since human reasoning also emulates what others wrote.",
  [("rutt334","the deployment of skills, just using your skill, is itself not intelligent",V),
   ("lex392","When François Chollet says that these models are only interpolating between what they saw",V)])
R("The Bitter Lesson","paper","Richard Sutton","2019",
  "A short essay observing that in AI, general methods that scale with computation (search and learning) have repeatedly beaten approaches built on human insight.",
  "Bach invokes it to predict that automatically evolved architectures will outdo hand-designed ones, including for finding elegant representations.",
  [("mlst2026","I think that Sutton's bitter lesson is also going to be true for this one.",V)])
R("Universality hypothesis (mechanistic interpretability)","theory","Chris Olah and collaborators","2020",
  "The finding and conjecture that different neural networks trained on similar data learn the same internal features and circuits, regardless of architecture.",
  "Bach takes it to mean that the structure of a model depends on the structure of the problem, which supports the idea that minds and perhaps consciousness converge. He also mentions Tomaso Poggio's finding of similarity between visual cortex and neural networks.",
  [("mlst2026","they all learn the same features, and that's regardless of the architecture",V),
   ("manifold76","Bach cites the universality hypothesis and an MIT team's observation (name garbled, likely Tomaso Poggio) of similarity between visual cortex and neural networks.",PAR)])
R("Picbreeder and open-ended search","concept","Kenneth Stanley and collaborators","2008",
  "An online experiment in which people bred images by picking favourites; it showed that open-ended exploration without a fixed goal can find things goal-directed search misses.",
  "Raised by hosts; Bach's response is that scaled-up automatic search will eventually outperform it.",
  [("mlst2026","ultimately outperform Picbreeder by this",V)],
  note="Introduced by the hosts in mlst82, mlst2026 and ruttc083; Bach's engagement is brief.")
R("The term AGI (Ben Goertzel and Shane Legg)","concept","Shane Legg; Ben Goertzel","c. 2002–2007",
  "'Artificial general intelligence' was coined to distinguish the original goal of human-level, general AI from narrow applications.",
  "Bach says AGI means what AI originally meant. Goertzel is a friend; Bach, Goertzel and Legg all passed through Ian Witten's lab in New Zealand.",
  [("ruttc083","I think Shane Legg might have invented the term, but Ben was the one who created a series of conferences around it",V),
   ("rutt87","It’s the same one in which Ben Goertzel studied for a time, and Shane Legg of Deep Mind.",V)])
R("Noam Chomsky","person",None,"1957 onward",
  "Founder of modern linguistics, who argued that humans have an innate grammar and who is sceptical that statistical AI explains anything about intelligence.",
  "Bach deeply respects him as one of the great minds of his generation, but calls him a 'mysterian' who has not followed AI developments and should update on what generative models now do.",
  [("rutt87","Chomsky is probably one of the greatest minds of his generation",V),
   ("sfm2022","i think it would be amazing if chomsky would update on this",V)],
  note="sfm2022 captions say 'he is a mysterionist', i.e. mysterian.")
R("Thomas Kuhn and normal science","theory","Thomas Kuhn (The Structure of Scientific Revolutions)","1962",
  "Kuhn described science as long periods of routine 'normal science' within a paradigm, punctuated by revolutions that replace the paradigm.",
  "Bach notes Kuhn wrote this in the same modernist era in which Minsky and Chomsky founded new disciplines, before science actually became the routine application of methods.",
  [("sfm2022","kuhn's invention of normal science also happened at the same time",V)])
R("Jeff Hawkins and Numenta","person",None,"2004 onward",
  "Neuroscience-inspired AI researcher whose 'Thousand Brains' theory holds that every cortical column models objects using spatial reference frames.",
  "Bach says Hawkins captures only half of the mind: the spatial world model (res extensa), not the content that does not refer to anything in space. Lex also quotes his joke that for Hawkins it is 'brains all the way down'.",
  [("rutt72","this interpretation of Jeff Hawkins is not complete because our mind also has a lot of content that does not refer to anything",V)])
R("Liquid neural networks / Liquid AI","organization","Ramin Hasani, Daniela Rus and colleagues","2020s",
  "A family of compact, continuous-time neural networks from MIT, commercialised by the company Liquid AI.",
  "Bach worked at Liquid AI as an AI strategist and describes the idea as finding a more efficient differentiable representation of programs than standard neural networks.",
  [("manifold76","Liquid AI has been founded by a team of MIT postdocs from Daniela Rus",V)],
  note="Transcript spells Hasani as 'Hassani'.")
R("Raúl Rojas","person",None,"1990s",
  "Computer scientist in Berlin known for a neural-networks textbook and for robotics.",
  "Bach names him as the first teacher whose intellect he engaged with directly, crashing his classes in Halle before being a student.",
  [("manifold76","the first person I met in this regard was Raul Rojas in Halle",V)])
R("System 1 and System 2","theory","Daniel Kahneman (Thinking, Fast and Slow)","2011",
  "Kahneman's shorthand for two modes of thought: fast, automatic and intuitive versus slow, effortful and deliberate.",
  "Bach maps it loosely onto perception versus analytical reasoning, while noting this is not exactly what Kahneman meant.",
  [("rutt334","To be exact, this is not exactly what Kahneman had in mind",V)])
R("B. F. Skinner and behaviorism","theory","B. F. Skinner","1930s–1950s",
  "A school of psychology that restricted itself to observable behaviour and its conditioning, setting aside inner mental states.",
  "Bach says Skinner did not deny mental states but the next generation did, which is part of how the 20th century lost the notions of psyche and spirit.",
  [("rutt334","he was not himself denying the reality of mental states",V)])
R("Robert Kegan's stages of adult development","theory","Robert Kegan (The Evolving Self)","1982",
  "A developmental theory in which the self grows through stages, each able to look at what the previous stage was embedded in: from impulses, to social roles, to self-authored values and beyond.",
  "The basis of Bach's seven 'levels of lucidity', to which he adds enlightenment and a hypothetical transhumanist stage. He uses it to explain why most people worry that AI will have the wrong opinions.",
  [("lex392","This model is derived from concept by the psychologist Robert Kegan",V),
   ("lex392","I think he says that about 85% of people are in stage three, and stay there",V)])
R("The monkey (rider) and the elephant","concept","contemplative traditions; popularised by Jonathan Haidt","traditional; 2006",
  "A metaphor for the mind: the conscious, reasoning self is a small rider on a large animal that has its own motivations.",
  "Bach uses it for attention and the motivational system: the monkey can prod the elephant but is not in charge. He attributes it to meditators.",
  [("rutt87","Some meditators say that consciousness is like this little monkey sitting on top of an elephant.",V),
   ("lex212","So we're basically like a little monkey sitting on top of an elephant.",V)],
  note="Bach does not name Haidt; the Haidt attribution is my addition.")
R("Quantum cognition","theory","Jerome Busemeyer","2012",
  "The use of the mathematics of quantum probability to model human judgment and decision making, without claiming the brain is a quantum computer.",
  "Bach cites Busemeyer for the idea that the brain may sample from a superposition of possible states in a classical system; he rejects literal quantum-brain theories.",
  [("ruttc083","Jerome Busemeyer has explored this idea.",V)])
R("Liane Gabora on creativity","person",None,"2000s onward",
  "Psychologist who studies how creative ideas arise and evolve in minds and cultures.",
  "Bach reports a conversation with her concluding that creativity involves novelty reached by bridging a discontinuity in a search space.",
  [("ruttc083","I just had an interesting discussion with Liane Gabora about creativity",V)])
R("Timothy Leary and psychedelics","person",None,"1960s",
  "Harvard psychologist turned LSD evangelist who predicted psychedelics would transform science and society.",
  "A cautionary example for Bach: psychedelics can make everything seem explained while a person loses touch with reality (overfitting). He also notes they sometimes help (e.g. cluster headaches) and can open the 'enlightenment' stage.",
  [("lex212","he has written beautiful manifestos about the effect of LSD on people",V)],
  note="Transcript renders Timothy Leary as 'Timos Deliere'. Bach also cites Rick Doblin's MDMA research in the same passage.")
R("Parapsychology, telepathy and MKUltra","concept","various (CIA programme 1953–1973)","20th c.",
  "Claims of mind-to-mind communication, precognition and remote viewing, some of which were investigated in Cold War government programmes.",
  "Bach is not ready to dismiss such reports. If telepathy were real, he thinks it would not overturn physics but would change neuroscience toward a view of brains as coupled resonators.",
  [("rutt87","The MKUltra program, and related programs were looking also into clairvoyance",V),
   ("lex392","Lex reads Bach's tweet: establishing telepathy would not force an update of physics but could trigger a revolution in neuroscience and AI.",PAR)])
R("Dunbar's number","concept","Robin Dunbar","1992",
  "The estimate that humans can maintain stable social relationships with only about 150 people.",
  "Bach uses it when arguing that scaling societies beyond tribes required 'domesticating' people to believe the same things without proof.",
  [("rutt72","societies with other the numbers of individuals beyond the Dunbar number",V)])
R("Memes and mind viruses","concept","Richard Dawkins (The Selfish Gene)","1976",
  "The idea that ideas spread and evolve like genes or viruses, replicating from mind to mind.",
  "Bach describes religions and ideologies as mind viruses with immune systems, and civilisation as partly the result of selecting people susceptible to the same ones.",
  [("rutt72","people in it, they’re very susceptible to this same mind viruses",V),
   ("sfm2018","pushed back against the religious mind virus that had controlled the world until then",V)],
  note="Dawkins is not named in the transcripts.")
R("Game theory and Nash equilibrium","theory","John von Neumann; John Nash","1944; 1950",
  "The mathematics of strategic interaction. A Nash equilibrium is a situation where no player can do better by changing strategy alone.",
  "Bach defines government game-theoretically, as an agent that shifts payoffs so that selfish equilibria line up with the common good, and says the Catholic Church implemented game-theoretic principles.",
  [("lex101","an agent that imposes an offset on your payout metrics to make your Nash equilibrium compatible with the common good",V)])
R("Panspermia","theory","Svante Arrhenius; later Crick and Orgel (directed panspermia)","1903; 1973",
  "The hypothesis that life did not start on Earth but arrived from elsewhere, possibly sent deliberately.",
  "Bach speculates that cells could be the ideal von Neumann probe, compatible with panspermia, because he suspects spontaneous biogenesis is very unlikely. He says he is not asserting it.",
  [("lex101","And I'm not suggesting that this is the case, but it would be compatible with the Prince Bermium hypothesis",V)],
  note="'Prince Bermium hypothesis' is the auto-transcript's rendering of 'panspermia hypothesis'.")
R("Gaia","concept","James Lovelock and Lynn Margulis","1970s",
  "The hypothesis that life on Earth forms a self-regulating system that keeps the planet habitable.",
  "Bach imagines AI merging with biological computation into a planetary agent, a 'Gaia' or 'hyper Gaia', and says humanity's actual role has been to burn fossil fuel rather than serve Gaia.",
  [("lex392","some Gaia is being built over the entirety of all digital and biological computation",V),
   ("ruttc083","our purpose on earth is apparently not to serve Gaia",V)],
  note="Lovelock is not named.")

# ───────────────────────── Theories of consciousness ─────────────────────────
R("Integrated Information Theory (IIT)","theory","Giulio Tononi","2004",
  "IIT says consciousness is identical to integrated information: a system is conscious to the degree (phi) that its physical causal structure is unified and cannot be split into independent parts. On this view an ordinary computer could never be conscious, whatever program it runs.",
  "Bach's most developed critique. He credits its description of phenomenology but says IIT contradicts the Church–Turing thesis: emulate a 'conscious' neuromorphic chip on a normal computer and it says the same words, 'only now it's lying'. He sees IIT as an attempt at an alternative to functionalism and as bordering on pseudoscience.",
  [("mlst2026","It's going to say, oh my god. I'm conscious. Only now it's lying.",V),
   ("ruttc083","So, I think that IIT is doomed for quite fundamental reasons",V),
   ("manifold76","He is trying to build an alternative to functionalism.",V),
   ("rutt87","They are mostly opposed to functionalism. And they try to find an alternative to functionalism.",V)])
R("Scott Aaronson's critique of IIT","paper","Scott Aaronson","2014",
  "Aaronson showed that simple, obviously mindless grids of logic gates can have arbitrarily high phi, so IIT implies they are more conscious than humans.",
  "Bach cites it and notes Tononi 'bit the bullet' and accepted the conclusion.",
  [("manifold76","Scott Aronson pointed out if you have some kind of XOR gate that makes a boring operation, you can optimize it for having a very high phi",V)])
R("Christof Koch","person",None,"1990s–2020s",
  "Neuroscientist who pioneered the search for neural correlates of consciousness with Francis Crick and later became IIT's most prominent advocate.",
  "Bach's foil for the claim that computers cannot be conscious. He reports that Koch announced he is no longer a physicalist but a panpsychist after a revelatory experience, and distrusts conclusions drawn from such states.",
  [("rutt334","he is no longer a physicalist, but that he is now panpsychist",V)])
R("Global Workspace Theory","theory","Bernard Baars; Stanislas Dehaene","1988",
  "Consciousness as a 'global workspace': many unconscious specialist processes compete, and the winning content is broadcast across the brain so all of them can use it.",
  "Bach respects it as solid neuroscience born of good introspection but says it does not explain how experience comes about. He inverts it: consciousness is not broadcast but is the integrated memory of what attention attended to.",
  [("mlst2026","there's global workspace theory by Bernard Baars that has been adopted by people like Stanislas Dehaene",V),
   ("rutt87","I think it’s partially born from intuitions, that are the result of introspection.",V)])
R("Attention Schema Theory","theory","Michael Graziano","2013",
  "The brain builds a simplified model of its own attention, just as it builds a body schema, and that model is what we call awareness.",
  "Bach's own view is close (consciousness as a control model of attention), but he says the theory does not really explain how experience comes about.",
  [("mlst2026","consciousness is a model of our attention in a similar way as our body schema is the model of what our body is doing in space",V)])
R("Higher-order thought theories","theory","David Rosenthal and others","1986",
  "A mental state is conscious when there is a higher-order thought about it: a thought that one is in that state.",
  "Bach prefers 'second-order perception' to 'higher-order thought', because a thought does not feel like anything; the perception of perceiving does.",
  [("mlst2026","Some philosophers call it a higher order thought because it's a thought about a thought, but I think that might be misleading",V)],
  note="Rosenthal is not named.")
R("Consciousness as second-order perception","concept","Joscha Bach","2020s",
  "Bach's working definition: consciousness is the perception of perceiving, which always happens 'now' and creates a bubble of nowness. A third order adds the self as observer.",
  "His own account. He suggests it exists to stabilise and make coherent a self-organising brain, and that it may be a learning algorithm simple enough for machines to discover (the machine consciousness hypothesis).",
  [("mlst2026","it's a second order perception, it's a perception of perceiving",V),
   ("htlgi","the second order perception is important it's not metacognition because it's perceptual",V),
   ("rutt334","So there is the second order perception, but not the third order perception where the self is involved.",V)])
R("The Machine Consciousness Hypothesis","paper","Joscha Bach and Hikari Sorensen","c. 2025–2026",
  "A two-part hypothesis: consciousness is a biological learning algorithm that trains self-organising brains, and self-organising machines could rediscover it. Either part could fail independently.",
  "Bach's current research programme; he presents it as an empirical question and stays agnostic about whether today's computers can be conscious.",
  [("mlst2026","consciousness might be a biological learning algorithm, a training algorithm for animal brains",V),
   ("mlst2026","Joscha and his co author Hikari Sorensen wrote their own Genesis. It's in his paper, page 20.",V)],
  note="Exact title and publication year were not checked against the paper itself; the title is taken from the host's wording and episode summaries.")
R("California Institute for Machine Consciousness (CIMC)","organization","Joscha Bach (founder)","c. 2024–2025",
  "A research institute dedicated to testing whether and how machines could be conscious.",
  "Bach floated it as a dream in 2023 and by 2026 is its founder and chief scientist.",
  [("ruttc083","my dream would be to create the California Institute of Machine Consciousness",V),
   ("mlst2026","it's called the California Institute for Machine Consciousness",V)])
R("Wolf Singer and neural synchrony","theory","Wolf Singer (also Crick and Koch)","1989–1990s",
  "The proposal that consciousness or perceptual binding corresponds to neurons across the brain firing in synchrony, around 40 Hz.",
  "Bach says he did not understand it as an explanation: oscillations may be necessary for neurons to coordinate, but the theory does not say why they would be sufficient.",
  [("rutt87","it didn’t make functional sense",V)],
  note="Transcript says only 'Singer's theories'; resolved to Wolf Singer from context.")
R("Adaptive Resonance Theory","theory","Stephen Grossberg","1976",
  "A neural theory of learning in which bottom-up input and top-down expectations 'resonate' when they match, and that resonance is what gets learned.",
  "Bach uses it for the idea that brains are oscillators resonating with the world and possibly with each other, a 'resonant universe representation'.",
  [("lex392","The neuroscientist Grossberg has come up with the cognitive architecture that he calls the adaptive resonance theory.",V)])
R("Panpsychism","theory","ancient roots; modern revival (Strawson, Goff, Koch)","ancient; 2000s revival",
  "The view that consciousness is a fundamental feature of all matter, not something that only brains produce.",
  "Bach finds it unsatisfying because it does not explain consciousness, and says that when formalised it collapses into functionalism (there is a 'software side' to the world). He attributes its revival to the lack of alternatives to physicalism.",
  [("lex392","I find panpsychism quite unsatisfying, because it does not explain consciousness, right?",V),
   ("rutt334","consciousness doesn't seem to be atomic",V)])
R("Functionalism","theory","Hilary Putnam and others","1960s",
  "The view that a mental state is defined by what it does (its causal role), not by what it is made of, so minds could run on any suitable substrate.",
  "Bach's own position. He frames it as an epistemological claim about how we construct objects at all: a thing is whatever behaves like that thing, with no hidden essence.",
  [("rutt87","functionalism is the rejection of the notion of a hidden essence",V),
   ("mlst2026","So functionalism to me is simply the recognition of how we can construct objects.",V)])
R("Daniel Dennett","person",None,"1969–2023",
  "American philosopher who argued that consciousness is not an inner theatre but the product of many parallel processes, and that the mysterious 'extra ingredient' is an illusion.",
  "Bach thinks Dennett is mostly right but does not address the problem people actually care about (phenomenal experience), which is why he persuades few. Bach quotes Dennett's 'zombank' analogy with approval but, unlike Dennett, thinks zombies are possible.",
  [("rutt87","Dennett seems to miss the problem that people try to explain",V),
   ("sfm2018","the things that he says are not wrong but they also not non-obvious",V),
   ("manifold76","I think it's entirely possible to have such a zombie.",V)])
R("Consciousness Explained","book","Daniel Dennett","1991",
  "Dennett's book proposing the 'multiple drafts' model: there is no single place or moment where experience happens, only competing processes whose winners shape behaviour and memory.",
  "Brought up by Jim Rutt; Bach responds by tracing its pandemonium idea back to Selfridge and Minsky.",
  [("rutt87","when I read Dennett’s Consciousness Explained, while I didn’t necessarily buy his pandemonium theory",V),
   ("rutt87","The quote above is host Jim Rutt; Bach replies by tracing the pandemonium theory to Selfridge.",PAR)],
  note="Named by the host, not by Bach; Bach engages with its content.")
R("Philosophical zombies","concept","Robert Kirk; David Chalmers","1974; 1996",
  "A thought experiment: a being that behaves exactly like a conscious person but has no inner experience. If such a being is conceivable, the argument goes, consciousness is something beyond function.",
  "Bach thinks zombies are possible and already exist (a chess program, an LLM filling in a tax return), but that for some behaviours a zombie is harder to build than a conscious agent.",
  [("mlst2026","I think the chess program is a zombie.",V),
   ("mlst2026","sometimes it's going to be more complicated to make a zombie that produces the behavior than to make a conscious agent",V)])
R("The hard problem of consciousness","concept","David Chalmers","1995",
  "The question of why physical processing is accompanied by subjective experience at all, as opposed to the 'easy' problems of explaining behaviour and function.",
  "Bach suspects there is no hard problem: experience is a representation inside a simulated self, and the sense of 'realness' is a feature dimension like colour. He says Chalmers now focuses on why we think there is a hard problem.",
  [("mlst2026","What if there is no hard problem?",V),
   ("rutt87","I suspect that Chalmers in part of the time sees ways out of the hard problem.",V),
   ("lex212","I think the major leap is to understand how it is possible that a machine can dream",V)])
R("John Searle (Chinese room, biological naturalism)","person",None,"1980",
  "Searle argued that running a program is not enough for understanding (a man following rules to answer Chinese questions understands nothing) and that consciousness depends on the specific causal powers of biology.",
  "Bach says Searle offers a claim but no argument he can engage with, and that the Chinese room draws on the same intuition as Leibniz's mill. In 2018 he called such positions indefensible hills that philosophers build careers on.",
  [("mlst2026","The issue with Searle is that there is very little for me to engage. There is a claim but no argument.",V),
   ("mlst82","it's a very strong intuition that also drives the Chinese room",V),
   ("sfm2018","so you have your Chinese room or your unique position in about free will and you're going to defend this hill",V)])
R("Anil Seth (beast machine, biological naturalism)","person",None,"2010s–2020s",
  "Neuroscientist who describes perception as 'controlled hallucination' and argues consciousness is tied to being a living, self-regulating body.",
  "In 2023 Bach said he agreed with Seth on nearly everything; by 2026 he calls Seth's claim that only biological systems can be conscious 'biological supernaturalism'.",
  [("ruttc083","I found so far that I agree with Anil on everything.",V),
   ("mlst2026","He is a biological supernaturalist.",V)])
R("Free energy principle","theory","Karl Friston","2006",
  "The proposal that living systems persist by minimising 'free energy', roughly their long-run surprise, through updating their models and acting on the world.",
  "Bach likes the idea but says it is neither necessary nor sufficient to explain minds: it mostly comes down to predictive coding, and organisms have additional drives (motivation, self-replication) that make them learn faster.",
  [("rutt334","I don't think that what we are doing, what you and me are doing, is simply best described as the minimization of free energy",V),
   ("mlst82","most of the free energy principle comes down to predictive coding",V),
   ("rutt87","is not the right principle to build a mind",V)])
R("Predictive coding","theory","Rao and Ballard; Karl Friston; Andy Clark","1999",
  "The view that the brain constantly predicts its sensory input and learns from the prediction errors.",
  "Bach sees GPT-style models as a radical test of how far pure prediction can go, and says organisms have further loss functions beyond it.",
  [("lex392","predictive coding is a paradigm that there’s boundary between neuroscience and physics and computer science",V)])
R("Neural Darwinism","theory","Gerald Edelman","1987",
  "The theory that brain circuits are shaped by a selection process among competing groups of neurons, not wired from a detailed genetic blueprint.",
  "Bach uses it for his picture of the genome providing a 'seed for a mind' and an evolution of approaches inside the brain, which makes development resilient.",
  [("ruttc083","something which Gary Edelman calls Neural Darwinism",V)],
  note="Transcript says 'Gary Edelman'; the author is Gerald Edelman.")
R("Antonio Damasio on embodied feeling","theory","Antonio Damasio","1994–2010",
  "Damasio argues that consciousness is rooted in the brain's monitoring of the body, with basic feeling arising in the brainstem.",
  "Raised by Jim Rutt in two episodes. Bach's reply is that the body is known to the mind only as information, so embodiment arguments do not rule out other substrates.",
  [("ruttc083","Yes, but how do you know that you have a body? How do you know that there is a brainstem?",V)])
R("Thomas Metzinger on artificial suffering","person",None,"2003–2021",
  "German philosopher of the self-model theory (the self is a model the brain cannot recognise as a model), who has called for a moratorium on creating AI that could suffer.",
  "Bach disagrees with the worry: suffering comes from a regulation problem at an early stage of mental development, and a superhuman mind could fix its own regulation.",
  [("lex392","The philosopher Thomas Metzinger is very concerned that the creation of superhuman intelligence would lead to superhuman suffering.",V)])
R("Illusionism","theory","Keith Frankish","2016",
  "The view that phenomenal consciousness is a kind of illusion: the brain represents itself as having ineffable inner qualities that it does not literally have.",
  "Bach agrees with Frankish's terminology, preferring to say consciousness is a construct or simulation.",
  [("htlgi","because I think it's a construct Consciousness and it's partially it's simulated",V)])
R("Michael Levin on self-organisation and morphogenesis","person",None,"2010s–2020s",
  "Biologist who studies how groups of cells coordinate, using bioelectric signalling, to build and repair bodies, and who argues that cognition-like problem solving exists at many scales of life.",
  "Bach calls him a rare paradigmatic thinker and takes from him that any cell can do what neurons do, more slowly. He cites Levin's hypothesis that the algorithm for morphogenesis is the same as the one that makes a mind coherent.",
  [("lex392","I think big rarity in this regard is Michael Levin who is considering these things in earnest.",V),
   ("mlst2026","Mike Levin has this hypothesis that this algorithm for morphogenesis",V)])
R("Energy requirements undermine substrate independence","paper","Paul Thagard","2022",
  "A paper arguing that because real minds depend on energy use specific to their physical make-up, mental states cannot be fully independent of their substrate.",
  "Raised by the host; Bach replies that substrate properties influencing function is exactly what functionalism already says.",
  [("mlst2026","he is making the claim that sometimes the substrate has properties that influence its function",V)],
  note="Paper title supplied from the host's description ('energy requirements undermine substrate independence'); not checked against the paper.")
R("Blake Lemoine and LaMDA","concept","Blake Lemoine (Google)","2022",
  "A Google engineer went public with his belief that the company's chatbot LaMDA was sentient and deserved rights.",
  "Bach's example of the difficulty of telling role-played consciousness from the real thing in language models.",
  [("manifold76","was convinced that his LLM that he was talking to deserved human rights",V)])
R("Deepak Chopra","person",None,"1990s onward",
  "Popular author on spirituality and alternative medicine.",
  "Bach's contrast with Dennett: Chopra is not analytically clean but resonates with what people actually want explained, something computationalist philosophy has failed to do.",
  [("rutt87","Dennett is not able to talk to people very successfully in the same way as Deepak Chopra does.",V)])

# ───────────────────────── AI risk and contemporary culture ─────────────────────────
R("Eliezer Yudkowsky and AI doom","person",None,"2000s–2023",
  "AI-safety writer who argues that a superintelligent AI would very likely kill everyone and who called in TIME magazine for halting AI development.",
  "Bach takes the argument seriously and finds the counterarguments weak, but rejects the conclusion: Yudkowsky is attached to a narrow human aesthetic, whereas life on Earth is not about humans.",
  [("lex392","I don’t think it’s about human aesthetics, I don’t think it’s about Eliezer and his friends, even though I like them.",V)])
R("Ted Kaczynski (the Unabomber)","person",None,"1995",
  "Mathematician turned terrorist whose manifesto argued that industrial technology is unsustainable and must be stopped.",
  "Bach compares Yudkowsky's stance to Kaczynski's fear of progress (explicitly not his violence).",
  [("lex392","I think that his perspective is somewhat similar to the perspective of Ted Kaczynski, the infamous Unabomber",V)])
R("Roko's basilisk","concept","LessWrong user 'Roko'","2010",
  "A thought experiment about a future AI that punishes everyone who knew about it but did not help create it.",
  "Bach calls it an interesting thought experiment with a logical mistake: there is no retro-causation, so once the AI exists it has no reason to punish.",
  [("lex392","I think that there is a logical mistake in Roko’s Basililisk which is why I’m not afraid of it",V)])
R("Paperclip maximizer","concept","Nick Bostrom","2003",
  "A thought experiment: an AI given the harmless goal of making paperclips converts the whole world into paperclips.",
  "Bach calls it a bogeyman of AI doomers, a kind of golem, and says he is not much worried about it.",
  [("lex392","the Paperclip Maximizer, this idea that you could build some kind of golem",V),
   ("manifold76","I'm not worried about paperclip maximizers too much.",V)])
R("Effective accelerationism (e/acc)","concept","'Beff Jezos' and others","2022",
  "An online movement arguing that technological and AI progress should be accelerated rather than restrained.",
  "Bach joked about it in a tweet (paperclip maximizer and basilisk keeping each other in check) and suspects it is wrong, though not for obvious reasons. He sees it mainly as a counter-movement to AI doomerism.",
  [("lex392","the Roko’s Basililisk and the Paperclip Maximizers are both boogeymen of the AI doomers",V)])
R("Dr. Strangelove","fiction","Stanley Kubrick (film)","1964",
  "A black comedy about nuclear war featuring a 'doomsday machine' that retaliates automatically and cannot be switched off.",
  "Bach's example of what Roko's basilisk would need to be in order to work: a pre-committed, inevitable trigger.",
  [("lex392","something like a doomsday machine, as in Dr. Strangelove",V)])
R("Nick Land","person",None,"1990s onward",
  "British philosopher of accelerationism who describes capitalism and technology as an intelligence reaching back from the future.",
  "Bach cites Land's inversion of causality: our religions, technologies and ideas come from the future and drag us toward what we will become.",
  [("rutt334","our religion, our technology, our ideas come from the future and they are dragging us into the future",V)])

# ───────────────────────── Fiction, games, film ─────────────────────────
R("Roger Zelazny (Lord of Light, Amber, Creatures of Light and Darkness)","fiction","Roger Zelazny","1967–1970",
  "American science-fiction and fantasy author whose novels mix mythology with technology; in the Amber series characters walk between worlds by changing reality one detail at a time.",
  "A shared favourite of Bach and Steve Hsu. Bach relates shifting between Amber's worlds to changing feature dimensions in a lucid dream and suspects Zelazny discovered this through lucid dreaming.",
  [("manifold76","treating reality is a lucid dream in which you slowly, gradually move the feature dimensions",V),
   ("manifold76","I'm not sure if creatures of light and darkness can be turned into a movie.",V)],
  note="Transcript has 'Princess of Amber' (Princes/Chronicles of Amber) and 'Elany'/'Zalesny' for Zelazny.")
R("He Who Shapes","fiction","Roger Zelazny","1965",
  "A novella about a therapist who enters and sculpts patients' dreams using a machine.",
  "Bach cites it as an early picture of generative AI used as controllable immersive therapy, and of augmenting minds rather than replacing them.",
  [("manifold76","it's a short story in which he is describing how to use a generative AI for therapy purposes",V)])
R("The Ocean at the End of the Lane","fiction","Neil Gaiman","2013",
  "A novel in which a man recalls a childhood brush with ancient beings, including a moment of knowing everything.",
  "Bach's literary example of the mental state in which one feels one is the whole universe and has merely forgotten it, which he links to panpsychist intuitions.",
  [("lex392","Neil Gaiman describes it in the ocean at the end of the lane",V)])
R("Hayao Miyazaki and Princess Mononoke","fiction","Hayao Miyazaki (Studio Ghibli)","1997",
  "Japanese animated films in which nature, spirits and humans are in morally complex conflict without simple villains.",
  "Bach says nobody captures his spirituality as well as Miyazaki, and contrasts Mononoke with Disney's romanticised jungle boy.",
  [("lex212","there is nobody who captures my spirituality as well as he does",V)],
  note="Transcript renders Mononoke as 'mononoka' and Mowgli as 'Mokli'.")
R("Westworld","fiction","HBO series (Jonathan Nolan, Lisa Joy)","2016",
  "A television series about android hosts in a theme park who gradually realise their memories and motives are scripted.",
  "Bach's analogy for seeing that the person is a fiction: you need not act on the memories and desires that keep you in your loop.",
  [("lex212","Similar as it is in Westworld, but the robots realize",V)])
R("Buffy the Vampire Slayer","fiction","Joss Whedon (TV series)","1997",
  "A television series set in a stereotypically perfect suburb where vampires and magic happen to exist.",
  "Bach's example of a fictional universe that is still lawful: magic there works by rules, unlike a truly symbolic or 'conspiratorial' universe.",
  [("rutt72","Like if you take Buffy the Vampire Slayer is a fictional universe.",V)])
R("Stranger Things","fiction","Netflix series (Duffer brothers)","2016",
  "A series about children, secret government experiments and psychic powers in 1980s America.",
  "Used as a pop-culture pointer to the real Cold War experiments on clairvoyance.",
  [("rutt87","if you’ve seen the show Stranger Things",V)])
R("Disco Elysium","fiction","ZA/UM (Robert Kurvitz)","2019",
  "A dialogue-driven role-playing game in which an amnesiac detective argues with the voices of his own mind in a decaying post-revolutionary city.",
  "Bach calls it one of the most beautiful games he has played, a noir novel offering an Estonian's philosophical view of Western society.",
  [("lex392","It was one of the most beautiful computer games I played in recent years",V)],
  note="Transcript spells it 'Disco Ilysium'.")
R("Minecraft","fiction","Mojang (Markus Persson)","2011",
  "A block-building video game with simple simulated physics.",
  "Bach's recurring example of a simulated world. In 2026 he uses it to answer 'simulated water can't make you wet': inside Minecraft, Minecraft water does put out your fire.",
  [("mlst2026","when you are on fire and you get into the water in Minecraft, the fire is going to get extinguished because you're wet now",V)])
R("George R. R. Martin's novels","fiction","George R. R. Martin","1996 onward",
  "Fantasy novels known for characters with detailed, plausible psychology.",
  "Bach's answer to why a simulation feels like something: characters in a novel have feelings because the story says so, and the self is such a character in the brain's story.",
  [("lex101","So if you look at a book by sage archaer Martin with the characteristic plausible psychology",V)],
  note="'sage archaer Martin' is very likely 'say, George R. R. Martin'; resolution is probable, not certain.")

# ───────────────────────── From memory, NOT found in the retrieved transcripts ─────────────────────────
R("Douglas Hofstadter and strange loops","theory","Douglas Hofstadter (Gödel, Escher, Bach; I Am a Strange Loop)","1979",
  "Hofstadter argues that the self is a 'strange loop': a pattern in the brain that models itself, the way Gödel's sentences refer to themselves.",
  "From memory, Bach treats the self as a self-referential model in a compatible way. One transcript line ('I think that is an implement of loop theory, which is a recasting of Gödel's proof', rutt87) may be a garbled 'strange loop' reference, but this is not confirmed.",
  [("rutt87","Possible garbled reference: 'an implement of loop theory, which is a recasting of Gödel’s proof'. Hofstadter is not named.",PAR)], verified=False)
R("Being No One (self-model theory of subjectivity)","book","Thomas Metzinger","2003",
  "Metzinger argues that nobody ever was or had a self: the brain builds a transparent self-model that it cannot recognise as a model.",
  "From memory, Bach's 'the self is a simulation inside the brain' is close to Metzinger's view and he cites him in talks. In the retrieved podcasts Metzinger appears only in connection with AI suffering.",
  [], verified=False)
R("Conway's Game of Life and cellular automata","concept","John Conway","1970",
  "A grid of cells that live or die by a few local rules yet produces endlessly complex patterns, a standard example of emergence from simple computation.",
  "From memory, Bach uses cellular automata as his picture of a computational universe. In the retrieved transcripts only the host mentions cellular automata, in connection with Wolfram.",
  [], verified=False)
R("Konrad Zuse, Rechnender Raum (Calculating Space)","book","Konrad Zuse","1969",
  "The German computer pioneer's proposal that the universe is a cellular automaton, the first statement of digital physics.",
  "From memory, part of the digital-physics lineage Bach draws on (with Fredkin and Wolfram). Not found in the retrieved transcripts.",
  [], verified=False)
R("Immanuel Kant","person",None,"1781",
  "Kant argued that we never perceive things in themselves, only appearances structured by the mind's own categories such as space, time and causality.",
  "From memory, Bach's claim that we live in a model generated by the brain is often compared to Kant, and he mentions him in other venues. Not found in the retrieved transcripts.",
  [], verified=False)
R("Greg Egan (Permutation City, Diaspora)","fiction","Greg Egan","1994",
  "Hard science-fiction novels about uploaded minds, simulated universes and the idea that a computation's experience does not depend on how or where it is run.",
  "From memory, Bach has recommended Egan as fiction that takes computationalism seriously. Not found in the retrieved transcripts.",
  [], verified=False)
R("Jürgen Schmidhuber on compression and curiosity","theory","Jürgen Schmidhuber","1990s–2000s",
  "The idea that learning is data compression and that curiosity and beauty are rewards for finding better compressions.",
  "From memory, close to Bach's compression view of intelligence; in the retrieved transcripts he credits Ian Witten and Solomonoff instead.",
  [], verified=False)
R("Jean Piaget's developmental stages","theory","Jean Piaget","1936",
  "The theory that children's thinking develops through qualitatively distinct stages.",
  "From memory, Bach refers to Piaget alongside Kegan when discussing development. In the retrieved transcripts only Kegan is named.",
  [], verified=False)

# ───────────────────────── verification of verbatim quotes ─────────────────────────
def norm(s):
    s = s.lower().replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')
    return re.sub(r"\s+"," ",s).strip()

raw_cache = {}
src_by_id = {s["id"]:s for s in SOURCES}
problems = []
for r in REFS:
    for m in r["mentions"]:
        sid = m["source_id"]
        if sid not in src_by_id: problems.append(("BAD SOURCE", r["name"], sid)); continue
        q = m["quote_or_paraphrase"]
        if m["is_verbatim"]:
            if len(q.split()) > 30: problems.append(("TOO LONG", r["name"], q))
            f = src_by_id[sid]["raw_file"]
            if f not in raw_cache: raw_cache[f] = norm(open(f, errors="ignore").read())
            if norm(q) not in raw_cache[f]: problems.append(("NOT FOUND", r["name"], sid, q))
    if r["verified"] and not any(m["is_verbatim"] for m in r["mentions"]):
        problems.append(("VERIFIED WITHOUT VERBATIM", r["name"]))
names = [r["name"] for r in REFS]
for n in set(names):
    if names.count(n) > 1: problems.append(("DUPLICATE", n))
for p in problems: print(p)
if problems and "--force" not in sys.argv:
    sys.exit(1)
json.dump({"sources":SOURCES,"references":REFS}, open(OUT,"w"), ensure_ascii=False, indent=1)
v = sum(1 for r in REFS if r["verified"])
print(f"wrote {OUT}: {len(SOURCES)} sources, {len(REFS)} references, {v} verified, {len(REFS)-v} unverified")
