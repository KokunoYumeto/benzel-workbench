#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
pandoc AUDIT_REPORT.md --standalone \
  --from markdown+tex_math_dollars+tex_math_single_backslash --to latex \
  -V documentclass=article -V fontsize=11pt -V geometry:margin=0.82in \
  -V colorlinks=true -V linkcolor=linkink -V urlcolor=linkink \
  --include-in-header=header.tex -o AUDIT_REPORT.tex
pdflatex -interaction=nonstopmode -halt-on-error AUDIT_REPORT.tex > build.log
pdflatex -interaction=nonstopmode -halt-on-error AUDIT_REPORT.tex >> build.log
