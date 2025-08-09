#!/usr/bin/env python3
import os
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Fixed ablation results reported in the paper
rows = [
    {"alpha": 0.3, "precision_at_5": 71.2},
    {"alpha": 0.5, "precision_at_5": 79.0},
    {"alpha": 0.7, "precision_at_5": 85.6},
    {"alpha": 0.9, "precision_at_5": 82.1},
]

root = Path(__file__).resolve().parent.parent
data_dir = root / "data"
fig_dir = root / "figures"
data_dir.mkdir(exist_ok=True)
fig_dir.mkdir(exist_ok=True)

csv_path = data_dir / "alpha_ablation.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["alpha", "precision_at_5"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

# Optional: generate a compact vector plot (PDF)
alphas = [r["alpha"] for r in rows]
precisions = [r["precision_at_5"] for r in rows]
plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42, "font.size": 11})
fig, ax = plt.subplots(figsize=(4.2, 2.6))
ax.plot(alphas, precisions, marker="o", color="black")
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel("Precision@5 (%)")
ax.set_ylim(65, 90)
ax.grid(True, linestyle=":", linewidth=0.6)
fig.tight_layout()
fig.savefig(fig_dir / "alpha_ablation.pdf", bbox_inches="tight")
fig.savefig(fig_dir / "alpha_ablation.png", dpi=400, bbox_inches="tight")
plt.close(fig)

print(f"Wrote {csv_path}")
print("Saved figures/alpha_ablation.(pdf|png)")