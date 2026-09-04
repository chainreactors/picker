---
title: Final-project-SQL-injection-pipeline
url: https://kitploit.com/en/tools/github/mlily2024/final-project-sql-injection-pipeline
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:36.149063
---

# Final-project-SQL-injection-pipeline

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

Final-project-SQL-injection-pipeline — Hybrid machine-learning pipelines for detecting SQL injection in web traffic, combining DistilBERT and BERT-GNN models with adversarial training and robustness analysis. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/mlily2024/final-project-sql-injection-pipeline

![](https://assets.kitploit.com/production/public/tools/53818/4359bb4a0b133b35850af3fc62dde4c1ca0924945dee9a505256fc9a23a71f59-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Web Security](/en/categories/web-security)[Machine Learning](/en/categories/machine-learning)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)[Anomaly Detection](/en/categories/anomaly-detection)

![GitHub](/providers/github.png)mlily2024/final-project-sql-injection-pipeline

# Final-project-SQL-injection-pipeline

Hybrid machine-learning pipelines for detecting SQL injection in web traffic, combining DistilBERT and BERT-GNN models with adversarial training and robustness analysis.

[View Repository](https://github.com/mlily2024/final-project-sql-injection-pipeline)

231 month ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# SQL Injection Detection — Hybrid ML Pipelines

**Source code for the MSc dissertation:** *Enhancing Web Application Firewall with Machine Learning for SQL Injection Detection*

|  |  |
| --- | --- |

|  |  |
| --- | --- |
| **Author** | Lilliane Linnet Musoke |
| **Institution** | University of Reading, Department of Computer Science |
| **Programme** | MSc Data Science and Advanced Computing |
| **Supervisor** | Professor Atta Badii |
| **Submitted** | 17 September 2024 |

---

## What this repository contains

Two novel Hybrid Machine-Learning pipelines, each implemented as a self-contained Jupyter notebook, for detecting SQL Injection (SQLi) attacks in web application traffic:

1. **`DistilBERT_Stacked_Ensemble_pipeline.ipynb`** — a DistilBERT-Stacked Ensemble (Meta-Learner) pipeline. Uses DistilBERT contextual embeddings as input to a stack of conventional ML and ensemble classifiers (Logistic Regression, XGBoost, SVM), combined under a neural-network meta-learner. Adversarial training is performed with the Fast Gradient Sign Method (FGSM); hyperparameters are tuned with Optuna.
2. **`BERT_GNN_pipeline_FINAL.ipynb`** — a BERT–Graph-Neural-Network hybrid pipeline. BERT generates contextual embeddings of SQL queries; a GNN models the graph-structured query representation to capture structural patterns. Hyperparameters tuned with Optuna.

Plus the dataset used to train and evaluate both pipelines:

3. **`SQL_Injection_Dataset.csv`** — labelled SQL queries (benign vs malicious).

## Headline results (from the dissertation)

| Pipeline | Accuracy | Adversarial accuracy (FGSM) | Notes |
| --- | --- | --- | --- |
| **DistilBERT-Stacked Ensemble** | **99.81%** | **99.77%** | Selected recommended approach; fast execution time |
| **BERT-GNN** | **99.48%** (99.67% held-out) | — | Superior structural understanding; longer execution time (23.13 s); held-out-validation retrain reaches 99.67%, see [`RESULTS.md`](https://github.com/mlily2024/final-project-sql-injection-pipeline/blob/main/RESULTS.md) |
| Best conventional baseline (Random Forest) | 94.47% | — | Benchmarked in the same study |

All four performance metrics (accuracy, precision, recall, F1-score) hit the same headline figure for both Hybrid pipelines. Full per-model tables, confusion matrices, ROC curves, learning curves and sensitivity analyses are in the notebooks and in the dissertation.

The DistilBERT-Stacked Ensemble adversarial accuracy of **99.77%** exceeds the comparable adversarial-testing result reported by Guan et al. (2023, *Future Internet* 15(4):133, DOI 10.3390/fi15040133) by **2.38%** — see the dissertation §4.4 for the full comparison.

## How to view the work

* **Notebooks** — the two `.ipynb` files in the repo root contain the full pipeline code (data loading, preprocessing, embedding, training, evaluation, adversarial robustness, sensitivity analysis). Outputs are stripped so the notebooks render fast and small on GitHub; running either notebook top-to-bottom regenerates every figure.
* **Results gallery** — [`RESULTS.md`](https://github.com/mlily2024/final-project-sql-injection-pipeline/blob/main/RESULTS.md) shows all the figures (confusion matrices, ROC curves, learning curves, sensitivity-analysis plots, per-model comparison) as a viewable gallery without needing to run anything.
* **All figures** — individual PNG exports of every result figure are in the `results/` folder, named by pipeline and section.

## How to run the notebooks locally

Tested under Python 3.10+ with a Jupyter environment. To install all dependencies:

root@kitploit:~

```
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\activate             # Windows
pip install -r requirements.txt
```

Then open either notebook in JupyterLab or VS Code and run cells top-to-bottom. Each pipeline is end-to-end self-contained: data loading and preprocessing → embedding extraction → model training → evaluation → adversarial-robustness check → sensitivity analysis. A GPU is recommended for the BERT-GNN training step but not required for inference or for the DistilBERT-Stacked Ensemble.

**Resource requirement.** The DistilBERT (and BERT) embedding-extraction step holds the language model and its full-dataset embeddings in memory simultaneously. End-to-end execution needs approximately **6–8 GB of free RAM** for the DistilBERT-Stacked Ensemble pipeline and **8–12 GB** for BERT-GNN. The notebooks were originally developed on Google Colab (which provides 12–16 GB and a free GPU). If running locally on a machine with 8 GB total RAM, close other applications first or run in Colab via the badge links at the top of each notebook.

## Reproducing the revision results

The scripts in the repository root regenerate the extended analysis reported in the revised BERT-GNN paper (ablation, corrected held-out evaluation, structure-aware graph, obfuscation robustness, the seven-test robustness suite, full metrics, and cross-model execution time). They read the committed `SQL_Injection_Dataset.csv`, write their outputs to `results/`, and cache intermediate artifacts (BERT embeddings, graphs, trained models) under `.structure_work/` and `.corrected_work/`. Those cache directories are intentionally not tracked; each script rebuilds them from the dataset and is resumable, so a run interrupted on a CPU-only machine can simply be started again and will continue.

The scripts form a producer→consumer chain through those caches, so run them in this order (each step only needs the dataset plus the caches written by earlier steps):

root@kitploit:~

```
pip install -r requirements.txt

python structure_graph_gnn.py        # structure graphs + best.json (Optuna) + structure-GNN result
python corrected_bertgnn_retrain.py  # held-out-validation retrain (chain graph) ...