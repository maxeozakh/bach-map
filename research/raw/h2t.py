import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
s=re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header)\b.*?</\1>','',s)
s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>|</li>','\n',s)
s=re.sub(r'<[^>]+>','',s)
s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
open(sys.argv[2],'w').write(s.strip())
print(sys.argv[2],len(s.split()),'words')
