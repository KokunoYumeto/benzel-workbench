"""Small source-copy replay, using the same independently written cell checker."""
from original_cell_check import *
def main():
    t=time.monotonic();p=load_producer();records=[]
    cases=[(2,0),(2,1),(9,7),(10,8),(12,10),(13,11),(14,12),(15,13),(16,14),(17,15),(20,190),(21,40)]
    for d,h in cases:
        out=p.complete_W(d,h,check=False);a,b=d+3*h,2*d+3*h
        stats=verify_tiles(out,a,b);verify_tiles(reflect_output(out),b,a)
        records.append({'d':d,'h':h,**stats})
    obj={'status':'PASS','original_parameter_pairs':len(records),'tiling_certificates_with_reflections':2*len(records),
         'placements':2*sum(r['tiles']for r in records),'records':records,'seconds':round(time.monotonic()-t,3)}
    (ROOT/'evidence/quick-output.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
if __name__=='__main__':main()
