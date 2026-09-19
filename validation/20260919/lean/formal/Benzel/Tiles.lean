import Benzel.Geometry

namespace Benzel

inductive Kind where
  | right | horizontal | vertical | diagonal
  deriving DecidableEq, Repr

structure Tile where
  kind : Kind
  anchor : Cell
  deriving DecidableEq, Repr

def offsets : Kind → List Cell
  | .right => [(0,0),(1,0),(0,1)]
  | .horizontal => [(0,0),(1,0),(2,0)]
  | .vertical => [(0,0),(0,1),(0,2)]
  | .diagonal => [(0,0),(1,-1),(2,-2)]

def Tile.cells (t : Tile) : List Cell :=
  (offsets t.kind).map (fun c => t.anchor+c)

def tile (k : Kind) (x y : ℤ) : Tile := ⟨k,(x,y)⟩

def shiftTile (s : Cell) (t : Tile) : Tile := ⟨t.kind,s+t.anchor⟩

/-- Tile anchors have coordinate sum zero, unlike cell centers. -/
def rotateTile (t : Tile) : Tile :=
  let x := t.anchor.1
  let y := t.anchor.2
  match t.kind with
  | .right => tile .right y (-x-y)
  | .horizontal => tile .vertical y (-1-x-y)
  | .vertical => tile .diagonal y (1-x-y)
  | .diagonal => tile .horizontal (y-2) (1-x-y)

def reflectTile (t : Tile) : Tile :=
  let x := t.anchor.1
  let y := t.anchor.2
  match t.kind with
  | .right => tile .right x (-x-y)
  | .horizontal => tile .diagonal x (1-x-y)
  | .vertical => tile .vertical x (-1-x-y)
  | .diagonal => tile .horizontal x (1-x-y)

def rotateTileN (n : ℕ) (t : Tile) : Tile := (rotateTile^[n]) t

@[simp] theorem offsets_length (k : Kind) : (offsets k).length = 3 := by
  cases k <;> rfl

@[simp] theorem tile_cells_length (t : Tile) : t.cells.length = 3 := by
  simp [Tile.cells]

@[simp] theorem shiftTile_cells (s : Cell) (t : Tile) :
    (shiftTile s t).cells = t.cells.map (shiftCell s) := by
  simp [Tile.cells,shiftTile,shiftCell,List.map_map,Function.comp_def,add_assoc]

@[simp] theorem shiftTile_inverse (s : Cell) (t : Tile) :
    shiftTile (-s) (shiftTile s t) = t := by
  cases t
  simp [shiftTile]

/-- Keep all occurrences: this operation cannot hide an overlapping tile. -/
def occurrences (ts : List Tile) : List Cell := ts.flatMap Tile.cells

def patchCells (ts : List Tile) (holes : List Cell) : List Cell :=
  occurrences ts ++ holes

/-- Three numbered occurrences, explicitly related to the list carrier. -/
def Tile.cell (t : Tile) (i : Fin 3) : Cell :=
  let os : Fin 3 → Cell := match t.kind with
    | .right => ![(0,0),(1,0),(0,1)]
    | .horizontal => ![(0,0),(1,0),(2,0)]
    | .vertical => ![(0,0),(0,1),(0,2)]
    | .diagonal => ![(0,0),(1,-1),(2,-2)]
  t.anchor+os i

theorem Tile.cells_eq_ofFn (t : Tile) : t.cells = List.ofFn t.cell := by
  rcases t with ⟨k,a⟩
  cases k <;> rfl

end Benzel
