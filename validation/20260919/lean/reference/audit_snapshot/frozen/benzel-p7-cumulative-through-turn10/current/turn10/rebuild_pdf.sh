#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build PROOF.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build PROOF.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build PROOF.tex
cp build/PROOF.pdf PROOF.pdf
