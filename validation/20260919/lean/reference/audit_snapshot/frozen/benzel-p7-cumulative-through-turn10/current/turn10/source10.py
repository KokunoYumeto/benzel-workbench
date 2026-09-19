"""Original q=3k+2 scaffold, with a parameter-preserving Laurent identity."""
from pathlib import Path
import sys,importlib.util
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G, bivariate_certificate as L
# sector, inclusive depth bounds (k,c), row bounds (m,k,ell,c), branch
ROWS=[
 (0,(0,0),(0,0),(0,0,0,1),(1,2,0,0),'cross'),
 (0,(0,1),(1,-1),(0,0,1,1),(1,2,0,-2),'cross'),
 (0,(0,1),(1,-1),(1,2,1,-1),(1,2,1,0),'tail'),
 (0,(1,0),(1,0),(0,1,0,1),(1,3,0,0),'cross'),
 (0,(1,1),(2,-1),(0,0,1,1),(0,2,0,2),'prefix'),
 (0,(2,0),(2,0),(0,2,0,1),(0,2,0,1),'prefix'),
 (1,(0,0),(1,-2),(0,0,1,1),(1,2,0,-5),'cross'),
 (1,(0,0),(1,-2),(1,2,1,-3),(1,2,1,-2),'tail'),
 (1,(1,-1),(1,-1),(0,1,0,0),(1,3,0,-3),'cross'),
 (1,(1,0),(1,0),(0,1,0,1),(0,2,0,-1),'prefix'),
 (1,(1,0),(1,0),(0,3,0,0),(0,3,0,2),'prefix'),
 (1,(1,1),(2,-2),(0,0,1,1),(0,2,0,-1),'prefix'),
 (2,(0,0),(1,-3),(0,0,1,1),(1,2,0,-5),'cross'),
 (2,(0,0),(1,-3),(1,2,1,-2),(1,2,1,-1),'tail'),
 (2,(1,-2),(1,-2),(0,1,0,-1),(1,3,0,-3),'cross'),
 (2,(1,-1),(1,-1),(0,1,0,0),(0,2,0,-1),'prefix'),
 (2,(1,-1),(1,-1),(0,3,0,0),(0,3,0,2),'prefix'),
 (2,(1,0),(2,-3),(0,0,1,1),(0,2,0,-1),'prefix')]
def value(a,m,k,ell):return a[0]*m+a[1]*k+a[2]*ell+a[3]
def labels(m,k):
 for p,elo,ehi,lo,hi,branch in ROWS:
  for ell in range(elo[0]*k+elo[1],ehi[0]*k+ehi[1]+1):
   for y in range(value(lo,m,k,ell),value(hi,m,k,ell)+1):
    rr=m-1 if y<=3*k+2 else m
    yield p,y,ell,G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p))
def orient(e,p):
 for _ in range(p):e=L.rotate(e)
 return L.reflect(e)
def strip_expr(p,elo,ehi,lo,hi,branch):
 ak,c=elo;I=(0,ehi[0]-ak,ehi[1]-c+1)
 ym,yk,yi,yc=lo;yk+=yi*ak;yc+=yi*c
 jm,jk,ji,jc=tuple(hi[a]-lo[a]for a in range(4));jk+=ji*ak;jc+=ji*c+1
 off=1 if branch=='prefix'else 2
 if I==(0,0,1):e=L.point(yc-off-3*c,yc,ym-1,ym,yk-3*ak,yk)*L.geo((1,1),(jm,jk,jc))*L.char('H')
 else:e=L.family('H',(ym-1,yk-3*ak,yi-3,1,yc-off-3*c),(ym,yk,yi,1,yc),I,(jm,jk,jc,ji))
 return orient(e,p)
def expression():
 out=L.E()
 for p,elo,ehi,lo,hi,branch in ROWS:
  if branch=='cross':
   out+=strip_expr(p,elo,ehi,lo,(0,3,0,2),'prefix')
   out+=strip_expr(p,elo,ehi,(0,3,0,3),hi,'tail')
  else:out+=strip_expr(p,elo,ehi,lo,hi,branch)
 return out
# Parent's actual 18-cell vacancy, in (x0,y0,xm,ym,xk,yk).
Z9=[(-2,4,0,-1,2,-4),(-2,5,0,-1,2,-4),(-1,3,0,-1,2,-4),(-1,1,0,-1,3,0),(-1,2,0,-1,3,0),(0,2,0,-1,3,0),(0,3,0,-1,3,0),(1,3,0,-1,3,0),(1,4,0,-1,3,0),(-4,1,1,0,-1,-1),(-4,2,1,0,-1,-1),(-3,1,1,0,-1,-1),(-5,-4,1,0,2,2),(-5,-3,1,0,2,2),(-5,-2,1,0,2,2),(-2,-1,1,0,2,2),(-2,0,1,0,2,2),(-1,0,1,0,2,2)]
def transform_cell(v,p,s):
 x0,y0,xm,ym,xk,yk=v
 for _ in range(p):x0,y0,xm,ym,xk,yk=y0,1-x0-y0,ym,-xm-ym,yk,-xk-yk
 return x0+s[0],y0+s[1],xm,ym,xk,yk
RESIDUAL=[transform_cell(v,0,(1,-2))for v in Z9[:12]]+[transform_cell(v,2,(-2,1))for v in Z9[3:]]
def residual(m,k):return {(x0+xm*m+xk*k,y0+ym*m+yk*k)for x0,y0,xm,ym,xk,yk in RESIDUAL}
def residual_expr():
 out=L.E()
 for v in RESIDUAL:out+=L.point(*v)
 return out
def identity():
 base=L.family('R',(1,0,-2,-1,-2),(0,0,1,-1,0),(1,0,-1),(1,0,-1,-1))
 extra=L.point(-2,0,1,0,-1,-1)*L.char('R')
 deleted=L.orbit(L.group('deleted'))+extra+L.rotate(L.rotate(extra))
 B=L.orbit(L.group('long')+L.point(ym=-1)*L.corner())
 M=L.orbit(L.point(2,3,0,-1,3,3)*L.geo((-1,-1),(0,3,2)))
 return L.point(-1,-1)*(B+base-deleted)+residual_expr()-base+M-expression()
if __name__=='__main__':print(identity().verify_zero())
