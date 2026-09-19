"""Literal q=3k+2 edit tables, constructed from original tile-coordinate maps."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[0]/'turn8'))
import geometry as G
class A(tuple):
 def __new__(cls,x=0):return tuple.__new__(cls,(0,0,0,x)if type(x)is int else tuple(x))
 def __add__(self,x):return A([a+b for a,b in zip(self,A(x))])
 __radd__=__add__
 def __neg__(self):return A([-a for a in self])
 def __sub__(self,x):return self+-A(x)
 def __rsub__(self,x):return A(x)+-self
 def __mul__(self,n):return A([a*n for a in self])
 __rmul__=__mul__
def transform_row(row,p=0,shift=(0,0)):
 kind,x,y=row;x,y=A(x),A(y)
 for _ in range(p%3):
  if kind=='R':kind,x,y='R',y,-x-y
  elif kind=='H':kind,x,y='V',y,-1-x-y
  elif kind=='V':kind,x,y='D',y,1-x-y
  else:kind,x,y='H',y-2,1-x-y
 return [kind,list(x+A(shift[0])),list(y+A(shift[1]))]
def build():
 parent=json.loads((ROOT.parent/'turn9/edits.json').read_text())
 out=[]
 for g in parent:
  if g['name']=='upper':continue
  out.append({'name':'first/'+g['name'],'count':g['count'],**{key:[transform_row(r,0,(1,-2))for r in g[key]]for key in('old','new')}})
 m=A((1,0,0,0));k=A((0,1,0,0));x,y=m+2*k-4,2*k-7
 olds=[('H',0,4),('H',0,5),('H',0,6),('H',1,2),('H',1,3),('H',1,7),('V',0,1),('V',3,4)]
 news=[('V',0,0),('V',0,3),('V',1,0),('V',1,3),('V',2,2),('V',2,5),('V',3,2),('V',3,5)]
 out.append({'name':'bridge6','count':[0,0,1],**{key:[[t,list(x+a),list(y+b)]for t,a,b in rows]for key,rows in[('old',olds),('new',news)]}})
 for g in parent:
  out.append({'name':'second/'+g['name'],'count':g['count'],**{key:[transform_row(r,2,(-2,1))for r in g[key]]for key in('old','new')}})
 return out
if __name__=='__main__':
 out=build();(ROOT/'edits.json').write_text(json.dumps(out,indent=2)+'\n');print(len(out),'groups')
