#!/usr/bin/env python3
from pathlib import Path
import csv
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent.parent
data_dir = root / "data"
fig_dir = root / "figures"
data_dir.mkdir(exist_ok=True)
fig_dir.mkdir(exist_ok=True)

# Values reflected in the paper text and figure
rows = [
    {"system": "Baseline", "metric": "Median", "seconds": 12},
    {"system": "Baseline", "metric": "p90", "seconds": 25},
    {"system": "GenSecAI-Ops", "metric": "Median", "seconds": 18},
    {"system": "GenSecAI-Ops", "metric": "p90", "seconds": 30},
]

csv_path = data_dir / "latency_summary.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["system", "metric", "seconds"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

# Plot compact bar chart
plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42, "font.size": 11})
fig, ax = plt.subplots(figsize=(4.4, 2.6))
labels = ["Median", "p90"]
baseline = [12, 25]
ours = [18, 30]
width = 0.35
x = range(len(labels))
ax.bar([i - width/2 for i in x], baseline, width=width, label="Baseline", color="gray")
ax.bar([i + width/2 for i in x], ours, width=width, label="GenSecAI-Ops", color="black")
ax.set_ylabel("Seconds")
ax.set_xticks(list(x))
ax.set_xticklabels(labels)
ax.set_ylim(0, 35)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(fig_dir / "latency.pdf", bbox_inches="tight")
fig.savefig(fig_dir / "latency.png", dpi=400, bbox_inches="tight")
plt.close(fig)

print(f"Wrote {csv_path}")
print("Saved figures/latency.(pdf|png)")