"""Rebuild the literal affine edit table; only Python integer arithmetic."""
from pathlib import Path
import json
import core
class A(tuple):
 def __new__(cls,x=0):return tuple.__new__(cls,(0,0,0,x)if type(x)is int else tuple(x))
 def __add__(self,b):b=A(b);return A(tuple(x+y for x,y in zip(self,b)))
 __radd__=__add__
 def __neg__(self):return A(tuple(-x for x in self))
 def __sub__(self,b):return self+-A(b)
 def __rsub__(self,b):return A(b)+-self
 def __mul__(self,b):
  if type(b)is not int:raise TypeError('Only integer scalar action')
  return A(tuple(x*b for x in self))
 __rmul__=__mul__
m=A((1,0,0,0));k=A((0,1,0,0));i=A((0,0,1,0))
def C(y,ell,part='tail'):return {'type':'common','p':1,'row':list(A(y)),'depth':list(A(ell)),'branch':part}
def B(f,a=0,b=0):return {'type':'corner','p':2,'family':f,'i':list(A(a)),'j':list(A(b))}
rows=[]
def add(name,count,old,new,owners):
 count=A(count);assert count[2]==0
 rows.append({'name':name,'count':[count[0],count[1],count[3]],'old':[[c,list(A(x)),list(A(y))]for c,x,y in old],'new':[[c,list(A(x)),list(A(y))]for c,x,y in new],'owners':owners})
L=m-3*k-3
# Split channel old/new counts into three literal groups, allowing L=0.
add('channel-low',L+1,[('V',3*k+2+i,i-m)],[],[C(3*k+2+i,k)])
add('channel-high',L,[('V',3*k+2+i,i+3-m)],[],[C(3*k+2+i,k-1)])
add('channel-new',L,[],[('D',3*k+1+i,3-m+i),('D',3*k+1+i,4-m+i)],[])
old,new=core.move('D',2*k-2+i,4-4*k-m+i);add('p0D',k-1,old,new,[C(2*k-1+i,2*k-2,'prefix'),C(2*k+i,2*k-1,'prefix')])
old,new=core.move('U',3*k-3,3-3*k-m+3*i);add('p0U',k-1,old,new,[C(3*k-3,2*k-3-i,'prefix'),C(3*k-2,2*k-2-i,'prefix')])
add('p0T',1,core.trans(core.P0_OLD,3*k-3,-m),core.trans(core.P0_NEW,3*k-3,-m),[C(3*k-2,k-1,'prefix'),C(3*k-1,k,'prefix'),C(3*k,k,'prefix'),C(3*k+1,k,'prefix')])
old,new=core.move('D',m-2+i,-3*k+i);add('p2D',2*k-2,old,new,[C(m-1+i,k-1),C(m+i,k)])
old,new=core.move('R',m-k-4+3*i,1-k);add('p2R',k-1,old,new,[B(6,k-1,k-1-i),B(7,k-2-i,0)])
co=[B(6,k-1,0),B(9,2,0),B(3,0,0),C(m+2*k-5,k-3),C(m+2*k-5,k-4),C(m+2*k-4,k-3),C(m+2*k-4,k-4),C(m+2*k-3,k-1),C(m+2*k-3,k-3),C(m+2*k-2,k),C(m+2*k-2,k-1),C(m+2*k-1,k),C(m+2*k,k),C(m+2*k,k-1)]
add('lower',1,core.trans(core.LOW_OLD,m+2*k-4,1-k),core.trans(core.LOW_NEW,m+2*k-4,1-k),co)
old,new=core.move('B',m+2*k-5,7-k+3*i);add('beta',k-4,old,new,[C(m+2*k-5,k-5-i),C(m+2*k-4,k-5-i)])
add('upper',1,core.trans(core.UP_OLD,m+2*k-4,2*k-5),core.trans(core.UP_NEW,m+2*k-4,2*k-5),[B(10,k-2,0),B(11,k-2,0),C(m+2*k-1,0)])
if __name__=='__main__':
 out=Path(__file__).with_name('edits.json');out.write_text(json.dumps(rows,indent=2)+'\n');print(len(rows),'edit groups')
