import re,sys
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
start=int(sys.argv[2]) if len(sys.argv)>2 else 0
i=start;n=len(s);out=[]
while i<n:
    c=s[i]
    if c in '"\'`':
        j=i+1
        while j<n and s[j]!=c:
            if s[j]=='\\': j+=1
            j+=1
        t=s[i+1:j]
        # preceding key
        k=re.search(r'([A-Za-z_]+):$',s[max(0,i-30):i])
        key=k.group(1) if k else ''
        keep = (len(t)>=3 and (' ' in t or t.startswith('http') or t.startswith('/') or key in('name','title','role','date','year','author','authors','label','type','location','venue','time','speaker','children'))) 
        if keep and not re.search(r'(rgb\(|var\(--|rem$|^\d+px|sc-[a-z0-9]+-\d|^M\d|^[\d. ]+$|--tw|&:|@media|^[\d.]+ [\d.]+ [\d.]+ [\d.]+$)',t) and 'displayName' not in key and key not in('d','viewBox','componentId','className','transition','fontFamily','boxShadow','border','gridTemplateColumns','stroke','fill','padding','margin'):
            out.append((key+': ' if key else '')+t.replace('\\n','\n'))
        i=j+1
    else: i+=1
open(sys.argv[3],'w').write('\n'.join(out))
print(len(out),sum(len(x) for x in out))
