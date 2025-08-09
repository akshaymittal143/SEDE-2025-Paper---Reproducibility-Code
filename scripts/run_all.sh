#!/usr/bin/env bash
set -euo pipefail

# Optional venv activation if present
if [[ -d .venv ]]; then
  source .venv/bin/activate
fi

python3 scripts/ablation_rag_alpha.py
python3 scripts/simulate_latency.py
python3 confusion_matrix.py
python3 scripts/hallucination_eval.py

latexmk -pdf -interaction=nonstopmode sn-article.tex

echo "Done. See sn-article.pdf and figures/."