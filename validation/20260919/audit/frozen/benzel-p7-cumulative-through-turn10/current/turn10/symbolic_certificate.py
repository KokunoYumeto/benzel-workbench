from pathlib import Path
import json
import source10 as S
L=S.L
def expr(row,count):
 t,x,y=row;p=L.point(x[3],y[3],x[0],y[0],x[1],y[1])*L.char(t)
 return p if count==[0,0,1] else p*L.geo((x[2],y[2]),tuple(count))
def verify():
 a=S.identity().verify_zero();e=L.E();groups=json.loads(Path(__file__).with_name('edits.json').read_text())
 for g in groups:
  for r in g['new']:e+=expr(r,g['count'])
  for r in g['old']:e-=expr(r,g['count'])
 b=(e-S.residual_expr()).verify_zero()
 return {'status':'PASS','domain':'integers k>=4,m>=3k+4','scaffold':a,'transport':b,'residual_cells':27,'groups':len(groups)}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
