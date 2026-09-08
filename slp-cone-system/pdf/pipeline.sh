set -e
B="$1"
cd "$B"
node build.mjs "$B" >/dev/null 2>&1
python3 - "$B" <<'PY'
import re,sys,html,json,pypdf
B=sys.argv[1]
src=open(B+'/body.html',encoding='utf-8').read()
items=[]
for m in re.finditer(r'<h1 class="part"><span class="tocmk">(QQ\d{3}QQ)</span>(.*?)<span class="pt">.*?</h1>'
                     r'|<h2(?: class="newpage")?><span class="tocmk">(QQ\d{3}QQ)</span>\s*<span class="n">(.*?)</span>(.*?)</h2>', src, re.S):
    if m.group(1):
        items.append(('part',m.group(1),'',html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()))
    else:
        items.append(('sec',m.group(3),html.unescape(re.sub(r'<[^>]+>','',m.group(4))).strip(),
                      html.unescape(re.sub(r'<[^>]+>','',m.group(5))).strip()))
pages=[re.sub(r'\s+','',(p.extract_text() or '')) for p in pypdf.PdfReader(B+'/body.pdf').pages]
out=[{'kind':k,'num':n,'title':t,'page':next((i+1 for i,p in enumerate(pages) if tok in p),None)}
     for k,tok,n,t in items]
assert all(o['page'] for o in out), [o for o in out if not o['page']]
json.dump(out,open(B+'/toc.json','w'),indent=1)
print('toc mapped:',len(out),'entries over',len(pages),'body pages')
PY
python3 "$B/mktoc.py" "$B"
node build.mjs "$B" toc >/dev/null 2>&1
python3 "$B/merge.py" "$B"
