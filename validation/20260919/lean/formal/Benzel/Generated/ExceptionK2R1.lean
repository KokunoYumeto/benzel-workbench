import Benzel.IndexedTables

namespace Benzel.Generated
open Benzel.Tables

-- Literal source: turn10/edits-k2-r1.json
-- SHA-256: 8037a803875f466accdf3194e92b14a92ba00321ad8ec3a62e4381140d420dc5
def exceptionK2R1 : List EditGroup :=
[
  { name := "channel-low", count := ⟨1, 0, (-8)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 8⟩, ⟨(-1), 0, 1, 0⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 8⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "channel-high", count := ⟨1, 0, (-9)⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 8⟩, ⟨(-1), 0, 1, 3⟩⟩
],
    newTiles := [

],
    owners := [
      .common 1 ⟨0, 0, 1, 8⟩ ⟨0, 0, 0, 1⟩ "tail"
] },
  { name := "channel-new", count := ⟨1, 0, (-9)⟩,
    oldTiles := [

],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 7⟩, ⟨(-1), 0, 1, 3⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 7⟩, ⟨(-1), 0, 1, 4⟩⟩
],
    owners := [

] },
  { name := "p0D", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 1, 3⟩, ⟨(-1), 0, 1, (-4)⟩⟩,
      ⟨.vertical, ⟨0, 0, 1, 4⟩, ⟨(-1), 0, 1, (-6)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 1, 2⟩, ⟨(-1), 0, 1, (-4)⟩⟩,
      ⟨.diagonal, ⟨0, 0, 1, 2⟩, ⟨(-1), 0, 1, (-3)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 1, 3⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 1 ⟨0, 0, 1, 4⟩ ⟨0, 0, 0, 3⟩ "prefix"
] },
  { name := "p0U", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 3⟩, ⟨(-1), 0, 3, (-1)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 3, (-3)⟩⟩
],
    newTiles := [
      ⟨.vertical, ⟨0, 0, 0, 3⟩, ⟨(-1), 0, 3, (-3)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 3, (-4)⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 3⟩ ⟨0, 0, (-1), 1⟩ "prefix",
      .common 1 ⟨0, 0, 0, 4⟩ ⟨0, 0, (-1), 2⟩ "prefix"
] },
  { name := "p0T", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.vertical, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨0, 0, 0, 7⟩, ⟨(-1), 0, 0, 0⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨0, 0, 0, 3⟩, ⟨(-1), 0, 0, 0⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 3⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.diagonal, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, 3⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 4⟩, ⟨(-1), 0, 0, 2⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 5⟩, ⟨(-1), 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨0, 0, 0, 6⟩, ⟨(-1), 0, 0, 0⟩⟩
],
    owners := [
      .common 1 ⟨0, 0, 0, 4⟩ ⟨0, 0, 0, 1⟩ "prefix",
      .common 1 ⟨0, 0, 0, 5⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 1 ⟨0, 0, 0, 6⟩ ⟨0, 0, 0, 2⟩ "prefix",
      .common 1 ⟨0, 0, 0, 7⟩ ⟨0, 0, 0, 2⟩ "prefix"
] },
  { name := "p2D", count := ⟨0, 0, 2⟩,
    oldTiles := [
      ⟨.vertical, ⟨1, 0, 1, (-1)⟩, ⟨0, 0, 1, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 1, 0⟩, ⟨0, 0, 1, (-8)⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 1, (-2)⟩, ⟨0, 0, 1, (-6)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 1, (-2)⟩, ⟨0, 0, 1, (-5)⟩⟩
],
    owners := [
      .common 1 ⟨1, 0, 1, (-1)⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 1, 0⟩ ⟨0, 0, 0, 2⟩ "tail"
] },
  { name := "p2R", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-4)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-5)⟩, ⟨0, 0, 0, 0⟩⟩
],
    newTiles := [
      ⟨.horizontal, ⟨1, 0, 3, (-6)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 3, (-6)⟩, ⟨0, 0, 0, 0⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, (-1), 1⟩,
      .parent "corner" 7 2 ⟨0, 0, (-1), 0⟩ ⟨0, 0, 0, 0⟩
] },
  { name := "small-terminal", count := ⟨0, 0, 1⟩,
    oldTiles := [
      ⟨.horizontal, ⟨1, 0, 0, (-1)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, (-2)⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-6)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-5)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-2)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 1⟩⟩
],
    newTiles := [
      ⟨.diagonal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 0⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.diagonal, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, (-3)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-3)⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-3)⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-2)⟩, ⟨0, 0, 0, 1⟩⟩,
      ⟨.horizontal, ⟨1, 0, 0, (-2)⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 1⟩, ⟨0, 0, 0, 0⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 2⟩, ⟨0, 0, 0, 2⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-4)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, (-1)⟩⟩,
      ⟨.vertical, ⟨1, 0, 0, 3⟩, ⟨0, 0, 0, 2⟩⟩
],
    owners := [
      .parent "corner" 6 2 ⟨0, 0, 0, 1⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 9 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 10 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 11 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .parent "corner" 3 2 ⟨0, 0, 0, 0⟩ ⟨0, 0, 0, 0⟩,
      .common 1 ⟨1, 0, 0, 1⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 2⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 2⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 1⟩ "tail",
      .common 1 ⟨1, 0, 0, 3⟩ ⟨0, 0, 0, 0⟩ "tail"
] }
]

end Benzel.Generated
