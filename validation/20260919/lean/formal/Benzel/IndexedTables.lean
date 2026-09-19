import Benzel.Tiles

namespace Benzel.Tables

/-- Coefficients in the exact order m,k,i,constant. -/
structure Affine4 where
  m : ℤ
  k : ℤ
  i : ℤ
  c : ℤ
  deriving DecidableEq, Repr

def Affine4.eval (a : Affine4) (m k i : ℤ) : ℤ :=
  a.m*m+a.k*k+a.i*i+a.c

/-- Coefficients in the exact order m,k,i,j,constant. -/
structure Affine5 where
  m : ℤ
  k : ℤ
  i : ℤ
  j : ℤ
  c : ℤ
  deriving DecidableEq, Repr

def Affine5.eval (a : Affine5) (m k i j : ℤ) : ℤ :=
  a.m*m+a.k*k+a.i*i+a.j*j+a.c

structure IndexedTile where
  kind : Kind
  x : Affine4
  y : Affine4
  deriving DecidableEq, Repr

def IndexedTile.eval (t : IndexedTile) (m k i : ℤ) : Tile :=
  tile t.kind (t.x.eval m k i) (t.y.eval m k i)

structure Count3 where
  m : ℤ
  k : ℤ
  c : ℤ
  deriving DecidableEq, Repr

def Count3.eval (n : Count3) (m k : ℤ) : ℤ := n.m*m+n.k*k+n.c

/-- Labels retain original ownership data; they are not quotient classes. -/
inductive Owner where
  | common (sector : ℕ) (row depth : Affine4) (branch : String)
  | corner (family sector : ℕ) (i j : Affine4)
  | parent (part : String) (family sector : ℕ) (i j : Affine4)
  deriving DecidableEq, Repr

structure EditGroup where
  name : String
  count : Count3
  oldTiles : List IndexedTile
  newTiles : List IndexedTile
  owners : List Owner
  deriving DecidableEq, Repr

/-- Use integer index sets. A separate domain proof must establish count >= 0;
Nat truncation is not allowed to conceal a bad range. -/
def indices (g : EditGroup) (m k : ℤ) : Finset ℤ :=
  Finset.Ico 0 (g.count.eval m k)

structure DoubleFamily where
  kind : Kind
  x : Affine5
  y : Affine5
  outerCount : Count3
  /-- The inner coefficients are m,k,i,constant; none denotes one inner index. -/
  innerCount : Option Affine4
  deriving DecidableEq, Repr

end Benzel.Tables
