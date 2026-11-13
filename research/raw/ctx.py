import re,sys
terms=sys.argv[1]; files=sys.argv[2:]
rx=re.compile(terms,re.I)
for f in files:
    s=open(f,errors='ignore').read()
    s=re.sub(r'\s+',' ',s)
    spans=[]
    for m in rx.finditer(s):
        a,b=max(0,m.start()-200),min(len(s),m.end()+300)
        if spans and a<=spans[-1][1]: spans[-1][1]=b; spans[-1][2].add(m.group(0).lower())
        else: spans.append([a,b,{m.group(0).lower()}])
    print(f"\n######## {f} ({len(spans)} spans)")
    for a,b,t in spans:
        print(f"--[{'/'.join(sorted(t))}] …{s[a:b]}…")
