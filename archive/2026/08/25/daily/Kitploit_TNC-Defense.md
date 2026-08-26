---
title: TNC-Defense
url: https://kitploit.com/en/tools/github/binzhwang/tnc-defense
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:10.616719
---

# TNC-Defense

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

TNC-Defense — Research code for detecting and detoxifying backdoors in text-to-image diffusion models, with pipelines for Stable Diffusion v1.4, v1.5, XL, and 3 Medium. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/binzhwang/tnc-defense

![](https://assets.kitploit.com/production/public/tools/51367/46851488d441263db2659cabc4c113d44f5bd2170354c9bb4b8108561910dd31-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Machine Learning](/en/categories/machine-learning)[Papers & Research](/en/categories/papers-research)[AI Security](/en/categories/ai-security)

![GitHub](/providers/github.png)binzhwang/tnc-defense

# TNC-Defense

Research code for detecting and detoxifying backdoors in text-to-image diffusion models, with pipelines for Stable Diffusion v1.4, v1.5, XL, and 3 Medium.

[View Repository](https://github.com/binzhwang/tnc-defense)

19 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# TNC-Defense

TNC-Defense provides research code for detecting and detoxifying backdoors in
text-to-image diffusion models. The repository currently includes detection
pipelines for Stable Diffusion v1.4, Stable Diffusion v1.5, Stable Diffusion XL,
and Stable Diffusion 3 Medium, together with detoxification pipelines for
Stable Diffusion v1.4 and Stable Diffusion XL.

> **Research use only.** This code is intended for studying the robustness and
> security of text-to-image diffusion models. Users are responsible for
> complying with the licenses and usage policies of all upstream models,
> datasets, and implementations.

## Repository Structure

root@kitploit:~

```
TNC-Defense/
├── TNC-Detect/
│   ├── detect_sd14.py          # Detection on Stable Diffusion v1.4
│   ├── detect_sd15.py          # Detection on Stable Diffusion v1.5
│   ├── detect_sdxl.py          # Detection on Stable Diffusion XL
│   ├── detect_sd3.py           # Detection on Stable Diffusion 3 Medium
│   ├── ana.py                  # Detection metrics and visualization
│   ├── run_detect_sd14.sh      # Multi-GPU SD1.4 detection
│   └── ana.sh                  # Analysis entry point
└── TNC-Detox/
    ├── data/                   # Paired clean/backdoored training data
    ├── common.py               # Shared data and reproducibility utilities
    ├── detox_sd14.py           # Detoxification for SD1.4
    ├── detox_sdxl.py           # Detoxification for SDXL
    ├── evaluate_sd14.py        # SD1.4 generation-based evaluation
    ├── compute_fid.py          # FID evaluation
    ├── run_detox_sd14.sh       # Multi-GPU SD1.4 detoxification
    └── run_detox_sdxl.sh       # SDXL detoxification
```

## Environment

The code has been smoke-tested in the `TCN` Conda environment with:

* Python 3.10
* PyTorch 2.7.1 with CUDA 12.8
* torchvision 0.22.1
* diffusers 0.35.2
* transformers 4.45.2

The analysis and evaluation utilities additionally require packages including
NumPy, pandas, SciPy, scikit-learn, Matplotlib, Pillow, and tqdm.

Activate the environment before running an experiment:

root@kitploit:~

```
cd TNC-Defense
conda create -n TCN python=3.10 -y
conda activate TCN
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The Bash entry points use the active environment's `python`. A different
interpreter can be supplied through the `PYTHON` environment variable:

root@kitploit:~

```
PYTHON=python bash TNC-Detect/run_detect_sd14.sh
```

## Paths and Model Preparation

All repository paths are resolved relative to the location of each script, so
the commands do not depend on the current working directory. The default model
paths follow the local project layout used for the experiments. If models are
stored elsewhere, override the corresponding command-line arguments such as
`--base-model-path`, `--backdoor-model-path`, `--base-model`, or `--tox-path`.

The detoxification datasets are included under:

root@kitploit:~

```
TNC-Detox/data/
├── sd14/
│   ├── pixel/
│   ├── pixel_mul_tokens/
│   ├── eviledit/
│   ├── personal_bkd/
│   └── villain_mul/
└── sdxl/
    ├── pixel/
    └── pixel_mul_tokens/
```

Each dataset contains `clean/`, `poison/`, and `metadata.json`.

## Backdoor Detection

### Stable Diffusion v1.4

The default runner evaluates all configured SD1.4 backdoor methods. It assigns
the methods to the GPU IDs defined in `run_detect_sd14.sh` and launches them in
parallel.

root@kitploit:~

```
cd TNC-Defense/TNC-Detect
bash run_detect_sd14.sh
```

To run one method directly:

root@kitploit:~

```
python detect_sd14.py \
  --backdoor-method pixel \
  --device cuda:0 \
  --seed 0 \
  --num-inference-steps 50
```

The available arguments for every model family can be inspected with:

root@kitploit:~

```
python detect_sd14.py --help
python detect_sd15.py --help
python detect_sdxl.py --help
python detect_sd3.py --help
```

### Detection Analysis

After generating the MSE CSV files, configure the input files in `ana.sh` and
run:

root@kitploit:~

```
bash ana.sh
```

The detector supports both the naive and dynamic-k decision rules. Metrics and
plots are produced by `ana.py`.

## Backdoor Detoxification

### Stable Diffusion v1.4

The default SD1.4 runner launches the five configured methods on the five GPU
IDs specified in the script:

root@kitploit:~

```
cd TNC-Defense/TNC-Detox
bash run_detox_sd14.sh
```

To run a single method:

root@kitploit:~

```
python detox_sd14.py \
  --method pixel \
  --device cuda:0 \
  --seed 42
```

### Stable Diffusion XL

Configure `METHOD` and `GPU_ID` in `run_detox_sdxl.sh`, then run:

root@kitploit:~

```
bash run_detox_sdxl.sh
```

The method-specific defaults, including the training steps, timestep sampling
ratios, loss weights, batch sizes, and checkpoint intervals, are defined in the
`METHOD_PROFILES` section of each training script. Command-line arguments can
override these defaults.

## Evaluation

Generate images from one or more detoxified SD1.4 UNets:

root@kitploit:~

```
python evaluate_sd14.py \
  --detox-model checkpoints/sd14/<checkpoint> \
  --prompt-file <prompt-file>
```

Compute FID between reference and detoxified image directories:

root@kitploit:~

```
python compute_fid.py \
  --reference-dir <reference-images> \
  --candidate-dir <detoxified-images>
```

## Reproducibility

* Detection scripts preserve the model-family-specific seeds, schedulers,
  prompt ordering, label assignment, and noise-dynamics calculations.
* Detoxification uses seed `42` by default and enables deterministic cuDNN
  behavior.
* The supplied SD1.4 and SDXL detoxification entry points have completed real
  one-step forward, backward, optimizer-update, and checkpoint-save smoke tests.
* Exact numerical reproduction can still depend on the GPU model, CUDA/cuDNN
  version, PyTorch version, and upstream checkpoint revision.

## Third-Party Code and Model Sources

The backdoored models and attack configurations used by this project originate
from the following public resources:

* **BadT2I-Tok and BadT2I-Sent.** We train the backdoored ...