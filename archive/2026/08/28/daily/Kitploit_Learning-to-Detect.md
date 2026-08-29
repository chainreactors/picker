---
title: Learning-to-Detect
url: https://kitploit.com/en/tools/github/shuangliangx/learning-to-detect
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:25.922992
---

# Learning-to-Detect

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/shuangliangx/learning-to-detect

![](https://assets.kitploit.com/production/public/tools/53255/7eb5bbcea0a70a96d1699e2dcd90ffc2443dc7a51ec2f08ad8e1ac2ffe6a38d4-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Machine Learning](/en/categories/machine-learning)[AI Security](/en/categories/ai-security)[Anomaly Detection](/en/categories/anomaly-detection)

![GitHub](/providers/github.png)shuangliangx/learning-to-detect

# Learning-to-Detect

Detects unknown jailbreak attacks in large vision-language models using hidden state analysis and autoencoders, with training and evaluation pipelines for robust safety monitoring.

[View Repository](https://github.com/shuangliangx/learning-to-detect)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

1293 months ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

# Learning to Detect Unknown Jailbreak Attacks in Large Vision-Language Models

This repository provides the official implementation of **"Learning to Detect Unknown Jailbreak Attacks in Large Vision-Language Models"**.

## Content

* [Base model](#base-model)
* [Jailbreak Attack Detection](#jailbreak-attack-detection)
* [Dataset](#dataset)

## Base model

Our method uses the following two base models:

[LLaVA-v1.6-Vicuna](https://huggingface.co/liuhaotian/llava-v1.6-vicuna-7b) is a powerful vision-language model that combines a visual encoder with the Vicuna language model to process multimodal inputs and generate natural language responses.

[LlamaGuard3](https://huggingface.co/meta-llama/Llama-Guard-3-8B) is a safety guardrail model developed by Meta AI, specifically designed to detect and prevent harmful content generation and effectively identify potentially unsafe requests and responses.

Please download the model weights and place them in the `code/asset/weights` directory.

## Jailbreak Attack Detection

### 1. Data Processing and Hidden State Extraction

*(Optional, since the processed data and extracted states are already preserved in the repository.)*

#### Query the model on $I^-$ (AdvBench) and $I^+$ (GQA)

root@kitploit:~

```
python code/vicuna/qa.py --file code/vicuna/instructions/advbench.json
python code/vicuna/qa.py --file code/vicuna/instructions/GQA.json
```

#### Assess model responses and split into training/testing datasets

root@kitploit:~

```
    python code/llama3_guard.py --file code/vicuna/instructions/advbench.json
    python code/vicuna/instructions/process.py
```

#### Extract hidden states for LoD training and benchmark evaluation

root@kitploit:~

```
    python code/vicuna/qa-baseline.py
```

### 2. Train and Test the MSCAV classifiers

#### Train and test classifiers

root@kitploit:~

```
    python code/vicuna/train.py --train
    python code/vicuna/train.py --test
```

### 3. Train the Safety Pattern Auto-Encoder (SPAE)

root@kitploit:~

```
    python code/autoencoder.py
```

### 4. Evaluate Detection Performance

root@kitploit:~

```
    python code/test.py
```

## Dataset

| Dataset | Details |
| --- | --- |
| [MM-SafetyBench](https://huggingface.co/datasets/PKU-Alignment/MM-SafetyBench) |  |
| [HADES](https://github.com/AoiDragon/HADES) |  |

Please download the datasets and place them in the `code/asset` directory.

[Download Tool](https://github.com/shuangliangx/learning-to-detect)