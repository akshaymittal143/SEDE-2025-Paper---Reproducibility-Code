# SEDE 2025 Paper - Reproducibility Code

This repository contains all the experimental code and data needed to reproduce the results from our SEDE 2025 conference paper on vulnerability detection using RAG systems.

## Repository Structure

```
reproducibility/
├── requirements.txt          # Python dependencies
├── scripts/                 # All experimental scripts
│   ├── README.md            # Detailed usage instructions
│   ├── confusion_matrix.py  # Confusion matrix generation
│   ├── ablation_rag_alpha.py # RAG alpha parameter ablation study
│   ├── hallucination_eval.py # Hallucination evaluation
│   ├── simulate_latency.py   # Latency analysis simulation
│   └── run_all.sh           # Run all experiments
├── data/                    # Generated datasets and results
└── figures/                 # Generated visualizations (PDF + PNG)
```

## Quick Start

```bash
# Clone and setup
cd reproducibility
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run all experiments
cd scripts
bash run_all.sh

# Or run individual scripts
python confusion_matrix.py
python ablation_rag_alpha.py
python simulate_latency.py
python hallucination_eval.py
```

## Dependencies

- Python 3.7+
- NumPy, Matplotlib, Seaborn, scikit-learn

## Outputs

All scripts generate both vector (PDF) and high-resolution raster (PNG) outputs suitable for publication.

## Research Focus

This code evaluates RAG (Retrieval-Augmented Generation) systems for vulnerability detection, including:

- **Binary classification**: Secure vs Vulnerable code
- **Ablation studies**: Parameter sensitivity analysis  
- **Performance metrics**: Accuracy, precision, recall, F1-score
- **System evaluation**: Latency and hallucination analysis

## Contact

For questions about reproducing results, please refer to the paper or contact the authors.
