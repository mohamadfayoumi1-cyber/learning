import json,sys,os,pypdf
B=sys.argv[1]
w=pypdf.PdfWriter(); n={}
for f in ['cover.pdf','toc.pdf','body.pdf']:
    r=pypdf.PdfReader(B+'/'+f); n[f]=len(r.pages)
    for p in r.pages: w.add_page(p)
off=n['cover.pdf']+n['toc.pdf']
w.add_outline_item('Cover',0); w.add_outline_item('Contents',n['cover.pdf'])
parent=None
for o in json.load(open(B+'/toc.json')):
    idx=off+o['page']-1
    if o['kind']=='part': parent=w.add_outline_item(o['title'],idx)
    else: w.add_outline_item(f"{o['num']}  {o['title']}",idx,parent=parent)
w.add_metadata({
 '/Title':'Collaborative Training Cone System — Functional Specification, System Architecture & Project Plan',
 '/Author':'Mohamad Fayoumi',
 '/Subject':'Senior Learning Project 2026-2027 — design specification for a swarm of self-driving driver-training cones',
 '/Keywords':'SLP, capstone, swarm robotics, UWB localisation, ORCA, ESP-NOW, driver training, mechatronics',
 '/Creator':'Chromium + Playwright','/Producer':'pypdf'})
w.page_layout='/SinglePage'; w.page_mode='/UseOutlines'
out=B+'/SLP_Cone_System_Design_Specification.pdf'
w.write(out)
print('MERGED:',n,'-> total',sum(n.values()),'pages |',round(os.path.getsize(out)/1024,1),'KB')
