import Benzel.IndexedTables

namespace Benzel.Generated
open Benzel.Tables

-- Literal source: turn10/edits-k3-r1.json
-- SHA-256: b03d038a5aacefdd46f7a6502f2be4bb70b49d07bb5172fd04867e21e5d09be2
def exceptionK3R1 : List EditGroup :=
[
  { name := "channel-low", count := ⟨1, 0, (-11)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 11⟩, ⟨(-1), 0, 1, 0⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 11⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "channel-high", count := ⟨1, 0, (-12)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 11⟩, ⟨(-1), 0, 1, 3⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 11⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "channel-new", count := ⟨1, 0, (-12)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 10⟩, ⟨(-1), 0, 1, 3⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 10⟩, ⟨(-1), 0, 1, 4⟩⟩
],
    owners := [

] },
  { name := "p0D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 5⟩, ⟨(-1), 0, 1, (-8)⟩⟩,
      ⟨.vertical, ⟨0, 0, 1, 6⟩, ⟨(-1), 0, 1, (-10)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 4⟩, ⟨(-1), 0, 1, (-8)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 4⟩, ⟨(-1), 0, 1, (-7)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 1, 5⟩ ⟨0, 0, 0, 4⟩ "prefix",
      .common 1 ⟨0, 0, 1, 6⟩ ⟨0, 0, 0, 5⟩ "prefix"
] },
  { name := "p0U", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 3, (-4)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 3, (-6)⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 3, (-6)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 3, (-7)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 6⟩ ⟨0, 0, (-1), 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 7⟩ ⟨0, 0, (-1), 4⟩ "prefix"
] },
  { name := "p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 9⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 10⟩, ⟨(-1), 0, 0, 0⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 9⟩, ⟨(-1), 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 8⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 9⟩, ⟨(-1), 0, 0, 0⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 7⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 1 ⟨0, 0, 0, 8⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 9⟩ ⟨0, 0, 0, 3⟩ "prefix",
      .common 1 ⟨0, 0, 0, 10⟩ ⟨0, 0, 0, 3⟩ "prefix"
] },
  { name := "p2D", count := ⟨0, 0, 4⟩,
    oldTiles := [
      ⟨.vertical, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-9)⟩⟩,
      ⟨.vertical, ⟨1, 0, 1, 0⟩, ⟨0, 0, 1, (-11)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 1, (-2)⟩, ⟨0, 0, 1, (-9)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 1, (-2)⟩, ⟨0, 0, 1, (-8)⟩⟩
],
    owners := [
      .common 1 ⟨1, 0, 1, (-1)⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 3⟩ "tail"
] },
  { name := "p2R", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-5)⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-6)⟩, ⟨0, 0, 0, (-1)⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-7)⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-7)⟩, ⟨0, 0, 0, (-1)⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 2⟩ ⟨0, 0, (-1), 2⟩,
      .parent "corner" 7 2 ⟨0, 0, (-1), 1⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "small-terminal", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-7)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, 3⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 4⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 5⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 4⟩, ⟨0, 0, 0, 6⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 5⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 6⟩, ⟨0, 0, 0, 2⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 2⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 3 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 1 ⟨1, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 4⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 5⟩ ⟨0, 0, 0, 0⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 3⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 6⟩ ⟨0, 0, 0, 0⟩ "tail"
] }
]

end Benzel.Generated
