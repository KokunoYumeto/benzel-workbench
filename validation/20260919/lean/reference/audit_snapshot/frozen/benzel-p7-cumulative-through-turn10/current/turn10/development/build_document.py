from pathlib import Path
import json,sys
from itertools import zip_longest
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import source10,complete_theorem as T

def lin(v,vars):
    out=''
    for c,x in zip(v,vars):
        if not c:continue
        t=(str(abs(c))if abs(c)!=1 or not x else'')+x
        if not out:out=('-'if c<0 else'')+t
        else:out+=(' - 'if c<0 else' + ')+t
    return out or'0'
def bound(v):return lin(v,('k',''))
def yr(v):return lin(v,('m','k','\\ell',''))
rows=['| Sector | Inclusive depth interval | Inclusive row interval |','|:--|:--|:--|']
for p,lo,hi,a,b,_ in source10.ROWS:
    l=bound(lo);h=bound(hi);x=yr(a);y=yr(b)
    dep=f'\\({l}\\)'if l==h else f'\\({l}\\le\\ell\\le {h}\\)'
    row=f'\\(y={x}\\)'if x==y else f'\\({x}\\le y\\le {y}\\)'
    rows.append(f'| {p} | {dep} | {row} |')
small=[]
for k in(2,3):
    for tp in('q1','direct'):
        f=ROOT/f'small-{tp}-{k}.json';r=json.loads(f.read_text())
        title=f'Terminal Q_{k}'if tp=='q1'else f'Direct bridge D_{k}'
        small.extend([f'## {title}',f'Original releases: {len(r["old"])} bones. Original insertions: {len(r["new"])} bones.','', '| Old placed bone | New placed bone |','|:--|:--|'])
        def tile(v):return ''if v is None else '\\('+v[0]+'('+str(v[1])+','+str(v[2])+')\\)'
        for a,b in zip_longest(r['old'],r['new']):small.append('| '+tile(a)+' | '+tile(b)+' |')
        small.append('')
tiles=T.G.encode_anchors(T.complete_W(2,1));d2=[]
for i in range(0,len(tiles),3):d2.append(',\\quad '.join(f'{k}({x},{y})'for k,x,y in tiles[i:i+3]))
s=(ROOT/'PROOF.md').read_text().replace('@@SOURCE_TABLE@@','\n'.join(rows)).replace('@@SMALL_TABLES@@','\n'.join(small)).replace('@@D2_TILES@@','\\[\n\\begin{gathered}\n'+'\\\\\n'.join(d2)+'\n\\end{gathered}\n\\]')
(ROOT/'PROOF.md').write_text(s)
