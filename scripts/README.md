# Reproducibility Guide

This directory contains minimal scripts to regenerate key quantitative artifacts in the paper and assist readers in reproducing the figures and metrics.

## Quick start
```bash
# (optional) create a virtualenv
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Generate figures and data artifacts
python scripts/ablation_rag_alpha.py
python scripts/simulate_latency.py
python scripts/confusion_matrix.py
python scripts/hallucination_eval.py

# Build the LaTeX PDF (requires TeX Live and latexmk)
latexmk -pdf -interaction=nonstopmode sn-article.tex
```

Outputs:
- `../data/alpha_ablation.csv` + `../figures/alpha_ablation.(pdf|png)`
- `../data/latency_summary.csv` + `../figures/latency.(pdf|png)`
- `../figures/confusion_matrix.(pdf|png)`
- `../data/hallucination_summary.(json|csv)`

Figure 1 (Architecture) is implemented with TikZ in `sn-article.tex` and compiles deterministically via LaTeX.

## Notes
- Scripts write vector PDFs alongside high-DPI PNGs for inspection.
- Randomness is either fixed by reporting exact values or seeded (`confusion_matrix.py`).
- Exact table/figure values match those stated in the paper.