# Build the cumulative reading edition

The current reader includes the historical source editions through turn 8
and the new turn-9 proof. It is an editorial/typesetting derivative of the
supplied cumulative TeX; the mathematical bodies are retained.

With LuaLaTeX and the DejaVu fonts installed, run from this directory:

```sh
lualatex -interaction=nonstopmode -halt-on-error Cumulative_Research_Record.tex
lualatex -interaction=nonstopmode -halt-on-error Cumulative_Research_Record.tex
```

The source uses relative `\input{turn9.tex}`. The supplied original TeX,
the unchanged cumulative archive, and the explanation of the typesetting
repair are linked in the [edition record](../../../integration/20260917/README.md).
Its research and review status is unchanged by compilation.
