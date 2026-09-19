"""Original-cell verification of the matching-comparison integer coordinates.

No original cohomology implementation is imported. Bone overlaps are converted
to a grounded oriented multigraph, with one edge per ORIGINAL cell. Exact path
flows are evaluated directly on the original bone columns.
"""
from collections import defaultdict,deque,Counter
from pathlib import Path
import json,time
from original_cell_check import load_producer,ROOT,need

def audit(old,new):
    def owners(tiles):
        out={}
        for n,(_,cells) in enumerate(tiles):
            for c in cells:
                need(c not in out,'input bone family is not a matching');out[c]=n
        return out
    a=owners(old);b=owners(new);na,nb=len(old),len(new);ground=na+nb
    edges=[];adj=defaultdict(list)
    for cell in sorted(set(a)|set(b)):
        tail=a.get(cell,ground);head=na+b[cell] if cell in b else ground
        idx=len(edges);edges.append((tail,head,cell));adj[tail].append((head,idx,1));adj[head].append((tail,idx,-1))
    roots={};parent={};components=[]
    # Grounded part first; the other roots are genuine new-bone pivots.
    for root in [ground]+list(range(na,na+nb)):
        if root in roots:continue
        members=[];queue=deque([root]);roots[root]=root
        while queue:
            u=queue.popleft();members.append(u)
            for v,e,sgn in adj[u]:
                if v not in roots:roots[v]=root;parent[v]=(u,e,sgn);queue.append(v)
        components.append((root,members))
    need(len(roots)==na+nb+1,'a source bone was not connected to the grounded graph')
    closed=[(root,members) for root,members in components if root!=ground]
    pivots={root-na for root,_ in closed};basis=[j for j in range(nb) if j not in pivots]
    for root,members in closed:
        ac=Counter(c for v in members if v<na for c in old[v][1])
        bc=Counter(c for v in members if na<=v<na+nb for c in new[v-na][1])
        need(ac==bc,'closed-component original relation failed')
    coefficient=[(5*j+2)%13-6 for j in range(nb)]
    def coordinates(q):
        result={}
        for j in basis:
            root=roots[na+j];result[j]=q[j]-(q[root-na] if root!=ground else 0)
        return result
    coordinate=coordinates(coefficient);back=[0]*nb
    for j,v in coordinate.items():back[j]=v
    need(coordinates(back)==coordinate,'integral inverse coordinate map failed')
    dual_size=0
    for j in basis:
        u=na+j;root=roots[u];flow=Counter()
        while u!=root:
            v,e,sgn=parent[u];flow[edges[e][2]]+=sgn;u=v
        need(all(sum(flow[c] for c in cs)==0 for _,cs in old),'dual does not annihilate original old columns')
        for n,(_,cs) in enumerate(new):
            wanted=int(n==j)-(int(n==root-na) if root!=ground else 0)
            need(sum(flow[c] for c in cs)==wanted,'incorrect exact new-column evaluation')
        need(sum(coefficient[n]*sum(flow[c] for c in cs) for n,(_,cs) in enumerate(new))==coordinate[j], 'dual-coordinate square failed')
        dual_size+=len(flow)
    holes=set(b)-set(a)
    return {'old_bones':na,'new_bones':nb,'closed_components':len(closed),'kernel_rank':len(basis),'integer_duals':len(basis),'dual_cell_coefficients':dual_size,'vacancy_cells':len(holes),'status':'PASS'}

def main():
    start=time.monotonic();p=load_producer();records=[]
    for k,r,extra in [(2,1,0),(2,2,0),(3,1,0),(3,2,0),(4,1,0),(4,2,0),(5,1,4),(5,2,4),(9,1,0),(9,2,0)]:
        m=3*k+r+2+extra;data=p.core(m,k,r,check=False);record=audit(data[3],data[4]);record.update(k=k,r=r,m=m);records.append(record)
    h=lambda x,y:('H',((x,y),(x+1,y),(x+2,y)))
    v=lambda x,y:('V',((x,y),(x,y+1),(x,y+2)))
    controls=[audit([h(0,0)],[h(0,0)]),audit([h(0,y) for y in range(3)],[v(x,0) for x in range(3)])]
    need(controls[0]['kernel_rank']==0 and controls[0]['closed_components']==1,'identical matching control')
    need(controls[1]['kernel_rank']==2 and controls[1]['closed_components']==1,'3-by-3 closed component control')
    result={'status':'PASS','seconds':round(time.monotonic()-start,3),'records':records,'closed_component_controls':controls,
            'exact_original_cell_duals':sum(v['integer_duals'] for v in records+controls),'producer_cohomology_module_used':False}
    (ROOT/'evidence/independent-kernel.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
