#!/usr/bin/env python3
"""Read the emitted Lean literals back into Python and compare original tables.
This is an export/transport test, not Lean elaboration or theorem verification.
"""
from __future__ import annotations
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'reference/audit_snapshot/frozen/benzel-p7-cumulative-through-turn10/current'
GEN=ROOT/'formal/Benzel/Generated'
TOK=re.compile(r'\s+|--[^\n]*|"(?:\\.|[^"\\])*"|:=|[-]?\d+|[A-Za-z_][A-Za-z_0-9]*|[.⟨⟩\[\]{},()]')
ARITY={'common':4,'corner':4,'parent':5}
KINDS={'right':'R','horizontal':'H','vertical':'V','diagonal':'D'}
class Parser:
 def __init__(self,s):
  self.t=[];pos=0
  for m in TOK.finditer(s):
   if m.start()!=pos:raise ValueError('Unrecognized emitted Lean literal: '+repr(s[pos:m.start()]))
   pos=m.end();v=m.group()
   if not(v.isspace()or v.startswith('--')):self.t.append(v)
  if pos!=len(s):raise ValueError('Trailing unparsed literal')
  self.i=0
 def pop(self,w=None):
  if self.i>=len(self.t):raise ValueError('Unexpected end')
  v=self.t[self.i];self.i+=1
  if w is not None and v!=w:raise ValueError((w,v))
  return v
 def peek(self):return self.t[self.i]if self.i<len(self.t)else None
 def value(self):
  t=self.pop()
  if t=='(':
   a=self.value()
   if self.peek()==',':self.pop(',');b=self.value();self.pop(')');return(a,b)
   self.pop(')');return a
  if t in('[','⟨'):
   end=']'if t=='['else'⟩';out=[]
   while self.peek()!=end:
    out.append(self.value())
    if self.peek()!=end:self.pop(',')
   self.pop(end);return out if t=='['else tuple(out)
  if t=='{':
   out={}
   while self.peek()!='}':
    k=self.pop();self.pop(':=');out[k]=self.value()
    if self.peek()!='}':self.pop(',')
   self.pop('}');return out
  if t=='.':
   k=self.pop()
   if k in ARITY:return(k,*[self.value()for _ in range(ARITY[k])])
   if k not in KINDS:raise ValueError('Unknown kind')
   return KINDS[k]
  if t=='some':return('some',self.value())
  if t=='none':return None
  if t=='tile':
   k=self.value();x=self.value();y=self.value();return[k,x,y]
  if t.startswith('"'):return json.loads(t)
  if re.fullmatch(r'-?\d+',t):return int(t)
  raise ValueError('Unexpected literal '+t)
 def all(self):
  v=self.value()
  if self.peek()is not None:raise ValueError('Unused tokens')
  return v

def literal(path,name):
 s=path.read_text();m=re.search(r'\bdef\s+'+re.escape(name)+r'\s*:[^\n]*?\s*:=\s*',s)
 if not m:raise ValueError('Missing generated declaration: '+name)
 # Scan to next top-level declaration/comment/end; generated definitions have no proofs.
 start=m.end();rest=s[start:]
 end=re.search(r'\n(?:def |theorem |/--|-- |end )',rest)
 return Parser(rest[:end.start()]if end else rest).all()

def back_owner(o):
 if o[0]=='common':return {'type':'common','p':o[1],'row':list(o[2]),'depth':list(o[3]),'branch':o[4]}
 if o[0]=='corner':return {'type':'corner','p':o[2],'family':o[1],'i':list(o[3]),'j':list(o[4])}
 if o[0]=='parent':return {'type':'parent','part':o[1],'family':o[2],'p':o[3],'i':list(o[4]),'j':list(o[5])}
 raise ValueError('Unrecognized owner')

def check():
 d=json.loads((ROOT/'evidence/generated-data.json').read_text());ng=no=0
 for rec in d['source_records']:
  path=ROOT/rec['lean'];orig=json.loads((SRC/rec['path']).read_text())
  if rec['path'].endswith('families.json'):
   for key in ('source','corner','long','deleted'):
    raw=literal(path,'threefold'+key.title());back=[]
    for kind,x,y,I,J in raw:
     # Inverse of the explicitly documented coefficient permutation.
     j=None if J is None else[J[1][0],J[1][1],J[1][3],J[1][2]]
     back.append({'kind':kind,'x':list(x),'y':list(y),'I':list(I),'J':j})
    if back!=orig[key]:raise ValueError('Threefold data changed')
    ng+=len(back)
  else:
   name=path.stem[0].lower()+path.stem[1:];raw=literal(path,name);back=[]
   for g in raw:
    back.append({'name':g['name'],'count':list(g['count']),
      'old':[[k,list(x),list(y)]for k,x,y in g['oldTiles']],
      'new':[[k,list(x),list(y)]for k,x,y in g['newTiles']],
      'owners':[back_owner(o)for o in g['owners']]})
    no+=len(g['owners'])
   if back!=orig:raise ValueError('Edit or owner data changed')
   ng+=len(back)
 patches=json.loads((ROOT/'evidence/local-patches.json').read_text());np=0
 for p in patches:
  for key,suffix in [('old','Old'),('new','New'),('oldholes','Before'),('newholes','After')]:
   got=literal(GEN/'LocalPatches.lean',p['name']+suffix)
   # Coordinates use pairs in Lean and arrays in JSON; convert representation explicitly.
   if key.endswith('holes'):got=[list(x)for x in got]
   if got!=p[key]:raise ValueError('Local patch literal changed')
  np+=1
 return {'status':'PASS','typed_family_records_roundtripped':ng,'owner_records_roundtripped':no,
         'local_patches_roundtripped':np,'lean_typechecking':'NOT_PERFORMED'}
if __name__=='__main__':print(json.dumps(check(),indent=2))
