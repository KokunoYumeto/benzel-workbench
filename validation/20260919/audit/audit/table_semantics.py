"""Tie literal symbolic source tables to the original constructor indices.

The formal comparisons here remain in the full six-variable Laurent ring.
Separate exact Fraction evaluations test the generic finite-sum compiler against
literal nested sums. They are compiler controls, not proofs by sampling.
"""
from independent_symbolic import *
from fractions import Fraction

def formal_source8():
    # Original (ell,y) intervals from the written source-label definition.
    intervals=[((0,0),(1,-2),(0,0,1,1),(1,2,0,-4),'cross'),
               ((0,0),(1,-2),(1,2,1,-2),(1,2,1,-1),'tail'),
               ((1,-1),(1,-1),(0,1,0,0),(1,3,0,-2),'cross'),
               ((1,0),(2,-2),(0,0,1,1),(0,2,0,0),'prefix')]
    out=Sum()
    for lo,hi,yl,yh,branch in intervals:
        if branch=='cross':
            out+=reflect(source_part(0,lo,hi,yl,(0,3,0,0),'prefix'))
            out+=reflect(source_part(0,lo,hi,(0,3,0,1),yh,'tail'))
        else:out+=reflect(source_part(0,lo,hi,yl,yh,branch))
    return out

def evaluate(expr,m,k):
    def power(x,y):return Fraction(2)**x*Fraction(3)**y
    value=Fraction(0)
    for num,den in expr.terms:
        numerator=sum((Fraction(int(c))*power(v[0]+m*v[2]+k*v[4],v[1]+m*v[3]+k*v[5]) for v,c in num.items()),Fraction(0))
        denominator=Fraction(1)
        for x,y in den:denominator*=1-power(x,y)
        if not denominator:raise ValueError('invalid test specialization')
        value+=numerator/denominator
    return value

def literal_family(f,m,k):
    total=Fraction(0);ni=f['I'][0]*m+f['I'][1]*k+f['I'][2]
    if ni<0:raise ValueError('invalid parameter domain')
    for i in range(ni):
        nj=1 if f['J'] is None else f['J'][0]*m+f['J'][1]*k+f['J'][2]+f['J'][3]*i
        if nj<0:raise ValueError('invalid inner range')
        for j in range(nj):
            x=sum(a*b for a,b in zip(f['x'],(m,k,i,j,1)));y=sum(a*b for a,b in zip(f['y'],(m,k,i,j,1)))
            for u,v in OFF[f['kind']]:total+=Fraction(2)**(x+u)*Fraction(3)**(y+v)
    return total

def main():
    records=[]
    records.append((formal_source8()-group('source')).verify('source8 original (ell,y) indices equal JSON source families'))
    directlong=fam('H',(0,1,2,1,1),(-1,1,-1,1,1),(0,1,0),(1,-3,0,1))
    records.append((directlong-group('long')).verify('source8 original long-strip indices equal JSON long families'))
    directdel=fam('R',(1,0,-1,0,-2),(0,0,-1,0,0),(0,1,0))
    records.append((directdel-group('deleted')).verify('source8 original corner deletion indices equal JSON deleted families'))
    controls=0
    for part in ('source','corner','long','deleted'):
        for f in SPECS[part]:
            expr=fam(f['kind'],f['x'],f['y'],f['I'],f['J'])
            for m,k in ((8,2),(11,3),(20,5),(35,9)):
                if evaluate(expr,m,k)!=literal_family(f,m,k):raise ValueError('finite-sum compiler mismatch in '+part)
                controls+=1
    out={'status':'PASS','formal_generator_map_comparisons':records,'exact_fraction_finite_sum_controls':controls,'producer_symbolic_code_imported':False}
    (ROOT/'evidence/table-semantics.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact generic finite-sum controls:',controls)
if __name__=='__main__':main()
