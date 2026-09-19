import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'turn8'))
import geometry as G, bivariate_certificate as L
# p, ell-lo=(k,c), ell-hi=(k,c), ylo=(m,k,ell,c), yhi, branch
ROWS=[
(0,(0,0),(0,0),(0,0,0,1),(1,2,0,-1),'cross'),
(0,(0,1),(1,-1),(0,0,1,1),(1,2,0,-3),'cross'),
(0,(0,1),(1,-1),(1,2,1,-2),(1,2,1,-1),'tail'),
(0,(1,0),(1,0),(0,1,0,1),(1,3,0,-1),'cross'),
(0,(1,1),(2,-1),(0,0,1,1),(0,2,0,1),'prefix'),
(1,(0,0),(1,-3),(0,0,1,1),(1,2,0,-6),'cross'),
(1,(0,0),(1,-3),(1,2,1,-3),(1,2,1,-2),'tail'),
(1,(1,-2),(1,-2),(0,1,0,-1),(1,3,0,-4),'cross'),
(1,(1,-1),(1,-1),(0,1,0,0),(0,2,0,-2),'prefix'),
(1,(1,-1),(1,-1),(0,3,0,-1),(0,3,0,1),'prefix'),
(1,(1,0),(2,-3),(0,0,1,1),(0,2,0,-2),'prefix'),
(2,(0,0),(1,-2),(0,0,1,1),(1,2,0,-3),'cross'),
(2,(0,0),(1,-2),(1,2,1,-1),(1,2,1,0),'tail'),
(2,(1,-1),(1,-1),(0,1,0,0),(1,3,0,-1),'cross'),
(2,(1,0),(2,-2),(0,0,1,1),(0,2,0,1),'prefix'),
(2,(2,-1),(2,-1),(0,2,0,0),(0,2,0,0),'prefix')]

def value(a,m,k,ell):return a[0]*m+a[1]*k+a[2]*ell+a[3]
def labels(m,k):
 for p,elo,ehi,lo,hi,branch in ROWS:
  for ell in range(elo[0]*k+elo[1],ehi[0]*k+ehi[1]+1):
   for y in range(value(lo,m,k,ell),value(hi,m,k,ell)+1):
    rr=m-1 if y<=3*k+1 else m
    yield p,y,ell,G.reflect_tile(G.rotate_tile(G.tile('H',y-rr-2-3*ell,y),p))
def orient(e,p):
 for _ in range(p):e=L.rotate(e)
 return L.reflect(e)
def strip_expr(p,elo,ehi,lo,hi,branch):
 # ell=ak*k+c+i; y = lo(m,k,ell)+j
 ak,c=elo;I=(0,ehi[0]-ak,ehi[1]-c+1)
 ym,yk,yi,yc=lo;yk+=yi*ak;yc+=yi*c
 jm,jk,ji,jc=tuple(hi[a]-lo[a]for a in range(4));jk+=ji*ak;jc+=ji*c+1
 off=1 if branch=='prefix'else 2
 if I==(0,0,1):
  e=L.point(yc-off-3*c,yc,ym-1,ym,yk-3*ak,yk)*L.geo((1,1),(jm,jk,jc))*L.char('H')
 else:
  e=L.family('H',(ym-1,yk-3*ak,yi-3,1,yc-off-3*c),(ym,yk,yi,1,yc),I,(jm,jk,jc,ji))
 return orient(e,p)
def expression():
 out=L.E()
 for p,elo,ehi,lo,hi,branch in ROWS:
  if branch=='cross':
   out+=strip_expr(p,elo,ehi,lo,(0,3,0,1),'prefix')
   out+=strip_expr(p,elo,ehi,(0,3,0,2),hi,'tail')
  else:out+=strip_expr(p,elo,ehi,lo,hi,branch)
 return out

def point_poly(rows):
 ans=L.E()
 for x0,y0,xm,ym,xk,yk in rows:ans+=L.point(x0,y0,xm,ym,xk,yk)
 return ans

def residual(m,k):
 return {(2*k-2,4-4*k-m),(2*k-2,5-4*k-m),(2*k-1,3-4*k-m),
 (3*k-1,1-m),(3*k-1,2-m),(3*k,2-m),(3*k,3-m),(3*k+1,3-m),(3*k+1,4-m),
 (m-k-4,1-k),(m-k-4,2-k),(m-k-3,1-k),
 (m+2*k-5,2*k-4),(m+2*k-5,2*k-3),(m+2*k-5,2*k-2),
 (m+2*k-2,2*k-1),(m+2*k-2,2*k),(m+2*k-1,2*k)}

RESIDUAL_COEFFICIENTS=[(-2, 4, 0, -1, 2, -4), (-2, 5, 0, -1, 2, -4), (-1, 3, 0, -1, 2, -4), (-1, 1, 0, -1, 3, 0), (-1, 2, 0, -1, 3, 0), (0, 2, 0, -1, 3, 0), (0, 3, 0, -1, 3, 0), (1, 3, 0, -1, 3, 0), (1, 4, 0, -1, 3, 0), (-4, 1, 1, 0, -1, -1), (-4, 2, 1, 0, -1, -1), (-3, 1, 1, 0, -1, -1), (-5, -4, 1, 0, 2, 2), (-5, -3, 1, 0, 2, 2), (-5, -2, 1, 0, 2, 2), (-2, -1, 1, 0, 2, 2), (-2, 0, 1, 0, 2, 2), (-1, 0, 1, 0, 2, 2)]

def residual_expr():
 return point_poly(RESIDUAL_COEFFICIENTS),RESIDUAL_COEFFICIENTS

def identity():
 base=L.family('R',(1,0,-2,-1,-2),(0,0,1,-1,0),(1,0,-1),(1,0,-1,-1))
 deleted=L.orbit(L.group('deleted'))+L.point(-2,0,1,0,-1,-1)*L.char('R')
 B=L.orbit(L.group('long')+L.point(ym=-1)*L.corner())
 shift=L.point(-2,1)
 M=L.orbit(L.point(1,2,0,-1,3,3)*L.geo((-1,-1),(0,3,1)))
 res,rows=residual_expr()
 expr=shift*(B+base-deleted)+res-base+M-expression()
 return expr,rows
if __name__=='__main__':
 e,rows=identity();print(e.verify_zero());print(rows)
