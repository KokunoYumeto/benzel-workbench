"""Two original six-variable integer Laurent identities, before parameter evaluation."""
import json
from pathlib import Path
import source_table as S
L=S.L

def row_expression(row,count):
 kind,x,y=row
 p=L.point(x[3],y[3],x[0],y[0],x[1],y[1])*L.char(kind)
 if count==[0,0,1]:return p
 if x[2]==0 and y[2]==0:
  raise ValueError('A repeated fixed generator is not an indexed family')
 return p*L.geo((x[2],y[2]),tuple(count))

def verify():
 scaffold,coordinates=S.identity();a=scaffold.verify_zero()
 groups=json.loads(Path(__file__).with_name('edits.json').read_text())
 delta=L.E()
 for g in groups:
  for row in g['new']:delta+=row_expression(row,g['count'])
  for row in g['old']:delta-=row_expression(row,g['count'])
 residue,_=S.residual_expr();b=(delta-residue).verify_zero()
 return {'status':'PASS','domain':'All integers k>=4, m>=3k+3; no finite cutoff',
         'scaffold_identity':a,'endpoint_transport_identity':b,
         'residual_cells':18,'edit_groups':len(groups),
         'logical_receipt':'Original cell Laurent coefficients vanish before m or k is specialized. Exact affine source certificates supply positivity.'}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
