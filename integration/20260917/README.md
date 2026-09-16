# Cumulative Benzel edition through turn 9

This edition adds the asymmetric $q=3k+1$ construction to the existing
Benzel workbench, while preserving the earlier $q=3k$ construction and
its September 16 review. The new stated domain is
$k\ge4$, $m\ge3k+3$, $d\ge m$, with
$\Delta=\binom m2-(3k+1)$ and $h=\binom d2-\Delta$.
The target tiling of $V(d+3h,2d+3h)$ uses $\Delta$ right stones and
$3h(h+d)$ bones. Independent mathematical review of turn 9 remains pending.

## Reading and reproducing

- [Current cumulative PDF](../../readers/20260917/Cumulative_Research_Record.pdf): 100 pages, including the new proof.
- [Editable reading-edition LaTeX](../../readers/20260917/latex/).
- [Turn-9 proof and original-coordinate code](../../workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/).
- [Previous 90-page through-turn-8 PDF](../../readers/20260917/Historical_Through_Turn8_Reader.pdf), preserved unchanged.
- [Unchanged cumulative source ZIP](../../archives/20260917/benzel-p7-cumulative-through-turn9.zip).
- [Source archive catalogue](catalog/archives.json), [proof-edition catalogue](catalog/proof-editions.json), and [supplied file manifest](SUPPLIED_MANIFEST.sha256).

The cumulative ZIP preserves all nine original ZIP handbacks, their extracted
source editions, independent recovered variants, earlier patches, and the
new continuation. Its [original README](SUPPLIED_README.md) retains the
remote-only recovery gaps and historical source pins. The ZIP is not presented
as a complete repository clone. Its embedded project instructions and patches
are historical source artifacts, not commands automatically applied here.

## What this integration checked

All 1,047 files declared in the supplied manifest match their SHA256 values.
A forward-slash relative-path comparison finds no missing or extra files.
The supplied manifest script has a Windows-only path-separator issue that can
report false extras; it is preserved unchanged inside the original archive.

The 14 supplied turn-8 root dependency files and its stable-packing proof were
compared with the canonical workbench before adding the sibling turn-9 directory.
They match exactly. No old source file was replaced, and no historical patch
was blindly applied. The new constructor therefore retains its actual source
dependency at the existing path.

The new manuscript, source tables and supplied receipts were read to describe
their precise scope. This publication step was not a new mathematical audit
or full replay. Its status is not promoted by byte-integrity checks or PDF
compilation.

## Supplied evidence and mathematical scope

The normal and optimized Python receipts record PASS for $k=4,\ldots,10$:
21 positive cores, 2,016 old-generator receivers, 777 expanded edit groups,
84 full/reflected tilings and 716,016 placements. Both retain 12 local homotopy
identities and four parameter-rejection tests. A separate final small replay
records $k=4$ only. The exact [recorded checks](../../workbenches/splitzero-nonzeta/sprints/benzel-p7/turn9/recorded-checks.json)
and their evidence files remain unchanged.

The unbounded written construction uses two integer Laurent identities and
exact rational source-index certificates. Its formal identities retain both
parameters before specialization; the source certificates address the
availability and distinctness of the released original generators. The
positive construction has the stated narrower domain, irrespective of a
formal identity's wider algebraic domain.

The full Problem 7 is not resolved by this work. The unbounded $q=3k+2$
positive endpoint, independent specialist review, and novelty determination
are not claimed complete. No Lean certificate is added.

## Reading-edition repair

The supplied README advertises a current cumulative PDF, but that file is
absent from the supplied ZIP. The included turn-9 build receipt records a
failed compilation; only the older PDF was supplied. The editable cumulative
TeX was present.

A separate reading derivative now compiles with installed LuaLaTeX. It
changes the appended obsolete `\rm` subscripts to `\mathrm`, updates the
subtitle to turn 9, gives the appended proof its own chapter hierarchy, adds
a note distinguishing historical chapters from the current continuation,
and adjusts table-of-contents spacing. No mathematical
formula or proof argument is changed. The [original supplied TeX](supplied-latex/)
and the unchanged ZIP are retained alongside the derivative.

The current reader has 100 pages. Its build and layout check are typesetting
checks, not proof certification. The [edition manifest](EDITION_MANIFEST.json)
records the published files and their hashes.
