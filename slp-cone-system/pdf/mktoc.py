import json,sys,html
B=sys.argv[1]
toc=json.load(open(B+'/toc.json'))
rows=[]
for o in toc:
    t=html.escape(o['title']); pg=o['page']
    if o['kind']=='part':
        rows.append(f'<div class="pt"><span class="t">{t}</span><span class="d"></span><span class="p">{pg}</span></div>')
    else:
        rows.append(f'<div class="sc"><span class="n">{html.escape(o["num"])}</span>'
                    f'<span class="t">{t}</span><span class="d"></span><span class="p">{pg}</span></div>')
body="\n".join(rows)
open(B+'/toc.html','w',encoding='utf-8').write(f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="style.css">
<style>
h1.c{{font-family:var(--sans);font-size:22pt;font-weight:700;letter-spacing:-.02em;color:var(--ink);margin:0 0 4px;border:0;padding:0}}
.sub{{font-family:var(--sans);font-size:8.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:0 0 4px}}
.bar{{height:2.5px;background:var(--accent);width:52mm;margin:10px 0 18px}}
.pt,.sc{{display:flex;align-items:baseline;font-family:var(--sans)}}
.pt{{font-size:10.4pt;font-weight:700;color:var(--accent);margin:15px 0 5px;padding-bottom:4px;border-bottom:1px solid var(--accent-edge)}}
.pt:first-of-type{{margin-top:0}}
.sc{{font-size:9.6pt;color:var(--body);margin:0 0 4px;padding-left:2px}}
.sc .n{{width:26px;flex:none;color:var(--accent-2);font-weight:700;font-size:8.6pt}}
.pt .t,.sc .t{{flex:none;max-width:118mm}}
.d{{flex:1;border-bottom:1px dotted #c3cbd2;margin:0 7px 0 8px;transform:translateY(-2.5px)}}
.pt .d{{border-bottom-color:transparent}}
.p{{flex:none;width:22px;text-align:right;font-variant-numeric:tabular-nums;font-weight:700;color:var(--ink);font-size:9pt}}
.pt .p{{color:var(--accent)}}
.foot{{margin-top:22px;padding-top:10px;border-top:1px solid var(--rule-soft);font-family:var(--sans);font-size:8pt;color:var(--muted);line-height:1.5}}
.foot b{{color:var(--accent)}}
</style></head><body>
<div class="sub">Collaborative Training Cone System</div>
<h1 class="c">Contents</h1>
<div class="bar"></div>
{body}
<div class="foot"><b>Reading order.</b> Part I is the specification and is authoritative.
Part II gives one defensible way of meeting it. Part III schedules the work in Part I's own
terms. If you read only two sections, read <b>&sect;7.2</b> — the four-minute demonstration the
whole project is built toward — and <b>&sect;10</b>, the five questions that must be put to the
advisor before anything is built.</div>
</body></html>''')
print('toc.html:',len(toc),'entries')
