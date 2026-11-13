import re,sys,collections
files=sys.argv[1:]
c=collections.Counter(); where=collections.defaultdict(set)
stop=set("I The And But So It This That If You We They He She There What When Because Yeah Yes No Right Well Okay In Or For Is Not Of To A An As At On My Your Our Now Then Also Maybe Jim Joscha Lex Bach Fridman Friedman Steve Hsu Tim Rutt Yosha Josh Joshua OK Oh Mm Sure Exactly How Why Which Do Does Can Is Are Was Were Let Some Most Many Every Each All With From By Just Like Even Where Who Its These Those Here One Two Three Have Has Had Would Could Should Will Thank Thanks".split())
for f in files:
    s=open(f,errors='ignore').read()
    for m in re.finditer(r"(?<![.?!:]\s)(?<!\n)\b([A-Z][a-zA-Zöüäé'’\-]+(?:\s+(?:of|von|de|the)?\s*[A-Z][a-zA-Zöüäé'’\-]+){0,3})",s):
        t=m.group(1)
        if t.split()[0] in stop and len(t.split())==1: continue
        c[t]+=1; where[t].add(f.split('_')[0][:8])
for t,n in sorted(c.items(), key=lambda x:(-x[1],x[0])):
    print(n,t,','.join(sorted(where[t])),sep='|')
