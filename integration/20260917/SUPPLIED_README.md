# Cumulative benzel / Split-Zero source handback through turn 9

17 September 2026. This extends the preserved through-turn-8 handback without replacing any original mathematical edition. The nine original ZIP handbacks and all recovered source variants remain under their earlier paths. The new continuation is under `continuations/benzel-p7-turn9/`.

New replay status: **PASS**. Read its exact scope and receipts at `continuations/benzel-p7-turn9/turn9/recorded-checks.json`. The full original Propp Problem 7 is not declared solved. Independent review and novelty determination are still pending.

The new written construction addresses q=3k+1 with k>=4, m>=3k+3, d>=m. Its argument retains the original source indices, zero-length channel endpoint, positive vacancy partitions, exact Laurent identities, and G(Z) supported cochain maps. It does not assert the remaining unbounded q=3k+2 result.

`latex/Cumulative_Research_Record.tex` with `latex/turn9.tex` is the editable cumulative LaTeX source. `pdf/Cumulative_Research_Record.pdf` is the compiled reading edition. The older source-only regeneration tool is preserved under `tools/rebuild_through_turn8_reader.py`; use `latex/build.sh` to rebuild the current editable LaTeX edition.

This is a source handback, not a complete Git clone. The original README below retains the exact remote-only recovery gaps. No remote branch or PR has been changed by this packaging step. The additive patch targets the recorded PR26 commit and must be reviewed against any subsequent local or remote edits.

---

# Cumulative Benzel P7 / Split-Zero handback

**Through focused turn 8; assembled 17 September 2026.**

Start with `pdf/Cumulative_Research_Record.pdf` (90 pages). Its complete editable LaTeX is `latex/Cumulative_Research_Record.tex`; rebuild it with `bash latex/build.sh`. `tools/rebuild_reader.py` regenerates the LaTeX from the indexed source Markdown using Pandoc. Literal algebra asterisks are escaped in the derived typesetting to avoid accidental Markdown emphasis; all original source bytes remain untouched.

`archives/` contains all NINE available original ZIP handbacks, unchanged. `catalog/archives.json` lists all archive and member hashes. `sources/` extracts them into separate source-edition directories. `supplements/` preserves independently mounted variants, original turn-7 code, earlier patches and source addenda. Alternative turn-2 editions are kept separately rather than overwriting one another. The initial and reviewed non-zeta portfolios and their job/source/status records are included.

The reader includes an editorial mathematical guide and TWELVE complete recovered proof-edition bodies. Turn 7 had no completed standalone manuscript in its delivery; its code is included, and the guide labels its report reconstruction rather than inventing a recovered proof file. Repeated proofs are source editions, not additional discoveries. Historical next-step statements and original checking boundaries remain visible.

This is a cumulative conversation-delivery archive, not a complete Git clone. The remote-only `TURN2.md` and 9-by-27 integer matrix extension at commit `038ed02bb524e60e9c2bd20c3a0aa02365f4001d` were not fully materialized. Their locator is https://github.com/KokunoYumeto/mathematics-commons-pilot/blob/038ed02bb524e60e9c2bd20c3a0aa02365f4001d/workbenches/splitzero-nonzeta/sprints/benzel-p7/TURN2.md . No fictitious local file or byte identity is supplied for them. The complete delivered third-collar integral quotient proofs and later full kernel calculations ARE included.

The last previously read remote mathematical pin is the draft PR26 contribution `20cb022dcfda7f37b3adec13b5619be8f13be3e8`, based on `6fe012fd1facd564e07e1fa052ad219debdd8278`. No current branch readback, new PR, merge, or remote modification is implied by this packaging step. Earlier patches can overlap: inspect them before local integration.

## Mathematical state

The full original P7 remains unresolved by this work. The turn-8 proof supplies q=3k for k>=1,m>=3k+2,d>=m, with Delta=binom(m,2)-3k and h=binom(d,2)-binom(m,2)+3k. The other deletion residues retain incomplete positive endpoint calculations. All finite observations and written all-parameter constructions keep their own domains. No independent mathematical acceptance, novelty certification, or new Lean certificate is added by this archive.

## Verification

`python tools/verify_manifest.py` checks the current self-excluding file manifest. Original archive manifests remain unchanged. The new root `evidence/` receipts record the exact replay performed during this assembly; they do not claim all historical experiments were rerun. For the turn-8 source, run its checker from its own directory:

```
cd sources/benzel-p7-turn8/benzel-p7-turn8/turn8
python bivariate_certificate.py
python verify.py --max-k 15 --output evidence/local-replay.json
```

The fresh replay in this package used k=1..4. The complete all-parameter Laurent identity is included in that checker. Historical outputs and model-produced written arguments remain subject to independent mathematical review. Manifest PASS, finite checker PASS, and LaTeX compilation are separate scopes.

No fonts, credentials, private transcripts, or third-party book/PDF corpus are included. Original component attribution and rights notes remain attached. Some exploratory scripts retain historical local-path conventions; the documented checkers are self-contained at their preserved source paths.
