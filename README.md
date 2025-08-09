# RAG-Based Vulnerability Detection: Reproducibility Artifacts

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Conference](https://img.shields.io/badge/Conference-SEDE%202025-green)](https://sede-conference.org/)
[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/)

> 📖 **Paper**: "Enhancing Software Vulnerability Detection through Retrieval-Augmented Generation: A Comprehensive Evaluation"
> 
> 🏛️ **Venue**: 34th International Conference on Software Engineering and Data Engineering (SEDE 2025)
> 
> 👥 **Authors**: [Your Name] et al.

---

## 🎯 Abstract

This repository contains all experimental code, data, and reproducibility artifacts for our SEDE 2025 paper on RAG-enhanced vulnerability detection systems. Our work evaluates the effectiveness of Retrieval-Augmented Generation (RAG) approaches for identifying security vulnerabilities in software code, achieving **~82% F1-score** on binary classification tasks.

## 📁 Repository Structure

```
reproducibility/
├── 📋 README.md                 # This file
├── 📦 requirements.txt          # Python dependencies
├── 📂 scripts/                  # Experimental scripts
│   ├── 📄 README.md            # Detailed execution guide
│   ├── 🎯 confusion_matrix.py  # Performance visualization
│   ├── 🔬 ablation_rag_alpha.py # Parameter sensitivity study
│   ├── 🧠 hallucination_eval.py # RAG hallucination analysis
│   ├── ⏱️  simulate_latency.py   # Performance benchmarking
│   └── 🚀 run_all.sh           # Complete reproduction script
├── 💾 data/                     # Experimental results
│   ├── alpha_ablation.csv       # Ablation study results
│   ├── latency_summary.csv      # Performance benchmarks
│   └── hallucination_summary.*  # Hallucination metrics
└── 📊 figures/                  # Publication-ready visualizations
    ├── confusion_matrix.*       # Classification performance
    ├── alpha_ablation.*         # Parameter sensitivity plots
    └── latency.*               # Performance analysis
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+**
- **Git** (for cloning)
- **Virtual environment support** (recommended)

### Installation & Execution

```bash
# 1. Clone the repository
git clone https://github.com/akshaymittal143/SEDE-2025-Paper---Reproducibility-Code.git
cd SEDE-2025-Paper---Reproducibility-Code

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run complete reproduction
cd scripts
bash run_all.sh

# 5. Check generated outputs
ls -la ../figures/  # Visualizations
ls -la ../data/     # Raw results
```

### Individual Experiments

```bash
# Core performance evaluation
python scripts/confusion_matrix.py

# Parameter sensitivity analysis
python scripts/ablation_rag_alpha.py

# System performance benchmarking
python scripts/simulate_latency.py

# Hallucination detection evaluation
python scripts/hallucination_eval.py
```

## 🔬 Experimental Design

### Research Questions

1. **RQ1**: How effective are RAG systems for vulnerability detection compared to traditional methods?
2. **RQ2**: What is the impact of retrieval parameters (α) on detection performance?
3. **RQ3**: How do RAG systems perform in terms of computational efficiency and latency?
4. **RQ4**: What is the extent of hallucination in RAG-based vulnerability detection?

### Methodology

- **Dataset**: Synthetic vulnerability data with realistic distributions
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score
- **Baseline Comparisons**: Traditional ML approaches vs. RAG-enhanced systems
- **Statistical Analysis**: Bootstrap sampling with 95% confidence intervals

### Key Results

| Metric | Performance |
|--------|------------|
| **Accuracy** | 85.0% |
| **Precision** | 83.7% |
| **Recall** | 80.4% |
| **F1-Score** | 82.0% |
| **Latency** | <100ms |

## 📊 Generated Artifacts

### Figures
- **`confusion_matrix.{pdf,png}`**: Classification performance heatmap
- **`alpha_ablation.{pdf,png}`**: Parameter sensitivity analysis
- **`latency.{pdf,png}`**: Performance benchmarking results

### Data Files
- **`alpha_ablation.csv`**: Raw ablation study metrics
- **`latency_summary.csv`**: Performance timing data
- **`hallucination_summary.{json,csv}`**: RAG hallucination analysis

## 🛠️ Technical Details

### Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| `numpy` | Latest | Numerical computations |
| `matplotlib` | Latest | Visualization framework |
| `seaborn` | Latest | Statistical plotting |
| `scikit-learn` | Latest | ML metrics and utilities |

### System Requirements

- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: ~50MB for generated artifacts
- **Runtime**: ~5-10 minutes for complete reproduction

### Output Formats

- **Vector Graphics**: PDF format for publication
- **Raster Graphics**: High-DPI PNG (600 DPI) for presentations
- **Data**: CSV/JSON formats for further analysis

## 🔄 Reproducibility

### Deterministic Results

All experiments use **fixed random seeds** (`np.random.seed(42)`) to ensure reproducible results across different environments.

### Environment Consistency

```bash
# Check Python version compatibility
python --version  # Should be 3.7+

# Verify package versions
pip list

# Compare generated checksums (optional)
find figures/ -name "*.pdf" -exec shasum {} \;
```

### Expected Runtime

| Script | Estimated Time | Output Files |
|--------|----------------|-------------|
| `confusion_matrix.py` | ~30s | 2 files |
| `ablation_rag_alpha.py` | ~2min | 3 files |
| `simulate_latency.py` | ~1min | 3 files |
| `hallucination_eval.py` | ~1min | 2 files |
| **Total** | **~5min** | **10 files** |

## 📝 Citation

If you use this code or data in your research, please cite our paper:

```bibtex
@inproceedings{author2025rag,
  title={Enhancing Software Vulnerability Detection through Retrieval-Augmented Generation: A Comprehensive Evaluation},
  author={[Your Name] and [Co-authors]},
  booktitle={Proceedings of the 34th International Conference on Software Engineering and Data Engineering},
  series={SEDE '25},
  year={2025},
  publisher={ACM},
  doi={10.1145/XXXXXX.XXXXXX},
  url={https://github.com/akshaymittal143/SEDE-2025-Paper---Reproducibility-Code}
}
```

## 🤝 Contributing

We welcome contributions to improve reproducibility:

- **Issues**: Report bugs or inconsistencies
- **Pull Requests**: Enhance documentation or fix issues
- **Extensions**: Adapt experiments for new datasets

## 📧 Contact

- **Primary Author**: akshay.mittal@ieee.org
- **Issues**: Use GitHub Issues for technical problems
- **Paper Questions**: Contact authors via institutional email

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- SEDE 2025 Conference organizers
- Anonymous reviewers for valuable feedback
- Open-source community for tools and libraries

---

> 💡 **Tip**: For the best reproduction experience, use a fresh Python virtual environment and follow the exact steps in the Quick Start guide.
