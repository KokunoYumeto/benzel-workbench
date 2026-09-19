from pathlib import Path
import json,sys,copy
from build_edits import A,transform_row
ROOT=Path(__file__).resolve().parent
parent=json.loads((ROOT.parent/'turn9/edits.json').read_text())
pre=parent[:next(i for i,g in enumerate(parent)if g['name']=='lower')]
M=A((1,0,0,0));K=A((0,1,0,0))
def special(name,file,anchor,p=0,s=(0,0)):
 data=json.loads((ROOT/file).read_text());x,y=anchor
 return {'name':name,'count':[0,0,1],**{key:[transform_row([t,list(x+a),list(y+b)],p,s)for t,a,b in data[key]]for key in('old','new')}}
def build(k,r):
 if r==1:
  return [{key:g[key]for key in('name','count','old','new')}for g in pre]+[special('small-terminal',f'small-q1-{k}.json',(M+2*K-4,A(1)-K))]
 groups=[]
 for g in pre:groups.append({'name':'first/'+g['name'],'count':g['count'],**{key:[transform_row(row,0,(1,-2))for row in g[key]]for key in('old','new')}})
 groups.append(special('direct-bridge',f'small-direct-{k}.json',(M+2*K-3,-K-1)))
 for g in pre:groups.append({'name':'second/'+g['name'],'count':g['count'],**{key:[transform_row(row,2,(-2,1))for row in g[key]]for key in('old','new')}})
 groups.append(special('small-terminal',f'small-q1-{k}.json',(M+2*K-4,A(1)-K),2,(-2,1)))
 return groups
if __name__=='__main__':
 for k in(2,3):
  for r in(1,2):
   groups=copy.deepcopy(build(k,r))
   for g in groups:
    g['count'][2]+=k*g['count'][1];g['count'][1]=0
    for key in ('old','new'):
     for row in g[key]:
      for v in row[1:]:v[3]+=k*v[1];v[1]=0
   (ROOT/f'edits-k{k}-r{r}.json').write_text(json.dumps(groups,indent=2)+'\n')
