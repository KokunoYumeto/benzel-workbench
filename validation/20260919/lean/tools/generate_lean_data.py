#!/usr/bin/env python3
"""Export literal audited data; no certificate status is exported as a theorem.
Re-run with --check to require byte-identical generated Lean source.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'reference/audit_snapshot/frozen/benzel-p7-cumulative-through-turn10/current'
DEST=ROOT/'formal/Benzel/Generated'
K={'R':'right','H':'horizontal','V':'vertical','D':'diagonal'}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def integer(n):
    if type(n) is not int: raise TypeError('An original integer coefficient was changed')
    return f'({n})' if n<0 else str(n)
def vec(a,n):
    if len(a)!=n: raise ValueError('Wrong original coefficient-vector length')
    return '⟨'+', '.join(integer(x)for x in a)+'⟩'
def text(s): return json.dumps(s,ensure_ascii=False)
def tile(row):
    k,x,y=row
    return f'tile .{K[k]} {integer(x)} {integer(y)}'
def indexed(row):
    k,x,y=row
    return f'⟨.{K[k]}, {vec(x,4)}, {vec(y,4)}⟩'
def owner(o):
    if o['type']=='common':
        return f'.common {o["p"]} {vec(o["row"],4)} {vec(o["depth"],4)} {text(o["branch"])}'
    if o['type']=='corner':
        return f'.corner {o["family"]} {o["p"]} {vec(o["i"],4)} {vec(o["j"],4)}'
    if o['type']=='parent':
        return f'.parent {text(o["part"])} {o["family"]} {o["p"]} {vec(o["i"],4)} {vec(o["j"],4)}'
    raise ValueError('Unrecognized original owner; do not discard it')
def lelist(items,indent='  '): return '[\n'+',\n'.join(indent+i for i in items)+'\n]'
def cell(p): return '('+', '.join(integer(x)for x in p)+')'
def write_or_check(path,txt,check):
    payload=(txt.strip()+'\n').encode()
    if check:
        if not path.exists() or path.read_bytes()!=payload: raise ValueError(f'Generated drift: {path.name}')
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    records=[];generated={};allparts=[]
    inputs=[('ResidueOne','turn9/edits.json'),('ResidueTwo','turn10/edits.json')]
    inputs += [(f'ExceptionK{k}R{r}',f'turn10/edits-k{k}-r{r}.json') for k in(2,3)for r in(1,2)]
    for name,relative in inputs:
        p=SRC/relative;ds=json.loads(p.read_text());parts=[]
        for g in ds:
            if len(g['old'])!=len(g['owners']):raise ValueError('Missing original owner')
            parts.append('  { name := '+text(g['name'])+', count := '+vec(g['count'],3)+',\n'+
               '    oldTiles := '+lelist([indexed(x)for x in g['old']],'      ')+',\n'+
               '    newTiles := '+lelist([indexed(x)for x in g['new']],'      ')+',\n'+
               '    owners := '+lelist([owner(x)for x in g['owners']],'      ')+' }')
        txt='import Benzel.IndexedTables\n\nnamespace Benzel.Generated\nopen Benzel.Tables\n\n'
        txt+=f'-- Literal source: {relative}\n-- SHA-256: {digest(p)}\n'
        txt+=f'def {name[0].lower()+name[1:]} : List EditGroup :=\n[\n'+',\n'.join(parts)+'\n]\n\nend Benzel.Generated\n'
        generated[name]=write_or_check(DEST/f'{name}.lean',txt,args.check)
        records.append({'path':relative,'sha256':digest(p),'groups':len(ds),
          'old_rows':sum(len(g['old'])for g in ds),'new_rows':sum(len(g['new'])for g in ds),
          'lean':f'formal/Benzel/Generated/{name}.lean'})
    p=SRC/'turn8/families.json';d=json.loads(p.read_text());txt='import Benzel.IndexedTables\n\nnamespace Benzel.Generated\nopen Benzel.Tables\n'
    for key in ('source','corner','long','deleted'):
        fs=[]
        for f in d[key]:
            # I: m,k,const. J: m,k,const,i. Reorder explicitly to m,k,i,const.
            inner='none' if f['J'] is None else 'some '+vec([f['J'][0],f['J'][1],f['J'][3],f['J'][2]],4)
            fs.append('⟨.'+K[f['kind']]+', '+vec(f['x'],5)+', '+vec(f['y'],5)+', '+vec(f['I'],3)+', '+inner+'⟩')
        txt+=f'\n-- Original {key} families; J coefficient permutation has an inverse.\ndef threefold{key.title()} : List DoubleFamily :=\n'+lelist(fs)+'\n'
    txt+='\nend Benzel.Generated\n';generated['Threefold']=write_or_check(DEST/'Threefold.lean',txt,args.check)
    records.append({'path':'turn8/families.json','sha256':digest(p),'groups':sum(len(d[k])for k in('source','corner','long','deleted')),'lean':'formal/Benzel/Generated/Threefold.lean'})
    # Exact finite partition producers. Old/new all ordered occurrences retained.
    alpha=lambda x,y:[[x,y],[x,y+1],[x+1,y-1]]
    beta=lambda x,y:[[x,y],[x+1,y],[x+1,y+1]]
    patches=[{'name':'bridgeSix','old':[['H',0,4],['H',0,5],['H',0,6],['H',1,2],['H',1,3],['H',1,7],['V',0,1],['V',3,4]],
      'new':[['V',0,0],['V',0,3],['V',1,0],['V',1,3],['V',2,2],['V',2,5],['V',3,2],['V',3,5]],'oldholes':beta(0,0),'newholes':beta(0,6),
      'source':'turn10/PROOF.md: eight-bone bridge'}]
    for k in(2,3):
        a=json.loads((SRC/f'turn10/small-q1-{k}.json').read_text())
        patches.append({'name':f'terminalQ{k}','old':a['old'],'new':a['new'],'oldholes':a['holes'],'newholes':[], 'source':f'turn10/small-q1-{k}.json'})
        b=json.loads((SRC/f'turn10/small-direct-{k}.json').read_text())
        patches.append({'name':f'directQ{k}',**{v:b[v]for v in('old','new','oldholes','newholes')},'source':f'turn10/small-direct-{k}.json'})
    txt='import Benzel.Tiles\n\nnamespace Benzel.Generated\n'
    targetnames=[]
    for p in patches:
        n=p['name'];txt+='\n-- Source: '+p['source']+'\n'
        for k,label in [('old','Old'),('new','New')]:
            txt+=f'def {n}{label} : List Tile :=\n'+lelist([tile(x)for x in p[k]])+'\n'
        for k,label in [('oldholes','Before'),('newholes','After')]:
            txt+=f'def {n}{label} : List Cell := '+ '['+', '.join(cell(x)for x in p[k])+']\n'
        txt+=f'''\ntheorem {n}_partition :
    (patchCells {n}Old {n}Before).Perm (patchCells {n}New {n}After) := by
  decide

theorem {n}_old_nodup : (patchCells {n}Old {n}Before).Nodup := by
  decide

theorem {n}_new_nodup : (patchCells {n}New {n}After).Nodup := by
  decide

/-- Same occurrence permutation at every integer translation, no sampling. -/
theorem {n}_translated (s : Cell) :
    ((patchCells {n}Old {n}Before).map (shiftCell s)).Perm
    ((patchCells {n}New {n}After).map (shiftCell s)) := by
  exact {n}_partition.map (shiftCell s)
'''
        targetnames += [f'Benzel.Generated.{n}_{q}' for q in('partition','old_nodup','new_nodup','translated')]
    txt+='\nend Benzel.Generated\n';generated['LocalPatches']=write_or_check(DEST/'LocalPatches.lean',txt,args.check)
    pp=ROOT/'evidence/local-patches.json';jp=json.dumps(patches,indent=2)+'\n'
    write_or_check(pp,jp,args.check)
    out={'schema':1,'status':'DATA_EXPORTED_NOT_LEAN_CHECKED','source_records':records,'generated_sha256':generated,'local_patch_targets':targetnames,'local_patch_count':len(patches)}
    write_or_check(ROOT/'evidence/generated-data.json',json.dumps(out,indent=2),args.check)
    print(json.dumps({'status':'PASS','mode':'comparison'if args.check else'write','edit_groups':sum(x.get('groups',0)for x in records),'patches':len(patches),'lean_files':len(generated)},indent=2))
if __name__=='__main__':main()
