import re,sys
f=sys.argv[1]; w=int(sys.argv[2]); maxn=int(sys.argv[3])
t=open(f,errors='ignore').read()
t=re.sub(r'\[\d+:\d\d(:\d\d)?\]','',t); t=re.sub(r'\s+',' ',t)
for p in sys.argv[4:]:
    ms=list(re.finditer(p,t,re.I)); print(f'## {f} [{p}] n={len(ms)}'); last=-10**9
    k=0
    for m in ms:
        if m.start()-last<w*2: continue
        last=m.start(); k+=1
        print('  …'+t[max(0,m.start()-w):m.end()+w]+'…')
        if k>=maxn: break
