---
title: A Gentle Tour of AI Fundamentals
url: https://www.hackingdream.net/2025/06/a-gentle-tour-of-ai-fundamentals.html
source: Hacking Dream
date: 2025-06-21
fetch_date: 2025-10-06T22:53:29.884629
---

# A Gentle Tour of AI Fundamentals

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### A Gentle Tour of AI Fundamentals

[June 21, 2025](https://www.hackingdream.net/2025/06/a-gentle-tour-of-ai-fundamentals.html "permanent link")

A Gentle Tour of AI Fundamentals

# A Gentle Tour of AI Fundamentals

> **Goal**—Provide a clear, progressive travel‑guide through the landscape of Artificial Intelligence (AI), Machine Learning (ML) and Deep Learning (DL). Each section builds on the previous one so that newcomers can read straight through without back‑tracking.

## 1 What Is Artificial Intelligence?

**Artificial Intelligence (AI)** is the broad scientific quest to create machines that perform tasks we regard as intelligent: reasoning, perception, language understanding, planning and learning from experience.

[![A Gentle Tour of AI Fundamentals](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXvSLHaFn1GQIlj2Oxu1hzBdS8GORUuGi48r73IUxIO_tFD1HR52TCH6UsNnypWKEcJUNLBys0Z4cV9TbPj77ivkzd21wWNuCbU6o6mxyEHKTs-DycoqakeVssX8ItB31vvXS-iFsr9jhcBMKw_8RvTltF23sCCB_iG-BAEFEcbwC_Ec7_YuhouWE1ex4N/w640-h426/A-Gentle-Tour-of-AI-Fundamentals.jpg "A Gentle Tour of AI Fundamentals")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXvSLHaFn1GQIlj2Oxu1hzBdS8GORUuGi48r73IUxIO_tFD1HR52TCH6UsNnypWKEcJUNLBys0Z4cV9TbPj77ivkzd21wWNuCbU6o6mxyEHKTs-DycoqakeVssX8ItB31vvXS-iFsr9jhcBMKw_8RvTltF23sCCB_iG-BAEFEcbwC_Ec7_YuhouWE1ex4N/s1024/A-Gentle-Tour-of-AI-Fundamentals.jpg)

**Classical branches**

* **Natural Language Processing (NLP)** – parse, interpret and generate human language.
* **Computer Vision** – extract meaning from images and video.
* **Robotics** – sense‑plan‑act loops for physical agents.
* **Expert Systems** – rule‑based decision engines drawing on specialist knowledge.

## 2 From AI ➜ ML ➜ DL — How They Relate

| Layer | Main Idea | Typical Output |
| --- | --- | --- |
| **AI** | Any approach that mimics human intellect | A chatbot, a chess engine, a self‑driving car |
| **ML** | Sub‑field of AI; algorithms that *learn patterns from data* instead of explicit rules | Email spam filter, loan‑default predictor |
| **DL** | Sub‑field of ML; *multi‑layer neural networks* that learn hierarchical features from raw data | Image captioning, large language models |

The pyramid is *nested*: DL ⟶ ML ⟶ AI.

## 3 Data Foundations (Before Any Model!)

* **Data Quality & Cleaning** – handle missing values, fix outliers, deduplicate.
* **Feature Engineering & Encoding** – scaling, normalisation, one‑hot encoding, domain‑specific transforms.
* **Data Augmentation** – synthesise new examples (e.g., image flips, noise injection) to improve generalisation.
* **Dataset Splits** – maintain *train / validation / test* partitions to measure generalisation honestly.

> *Rule of thumb*: Better data beats cleverer algorithms.

## 4 Core Learning Paradigms

### 4.1 Supervised Learning

Learns from **labelled** examples (feature ➜ known output).

#### Workflow

1. Collect & clean data
2. Split → train/val/test
3. Train model on *train*
4. Tune hyper‑parameters on *val*
5. Report metrics on *test*
6. Deploy & monitor

#### Key Concepts

| Term | One‑Line Explanation |
| --- | --- |
| **Features** | Measurable attributes (pixels, words, sensor values) |
| **Labels** | Ground‑truth answers (cat/dog, price) |
| **Overfitting** | Memorising training noise; poor generalisation |
| **Regularisation** | Penalty that discourages overly complex models |
| **Cross‑Validation** | Rotate train/val splits for robustness |

#### Classification vs Regression

* *Classification* → discrete categories (spam / not‑spam)
* *Regression* → continuous values (house price)

#### Popular Algorithms

Linear & Logistic Regression • Decision Trees / Random Forest • Gradient Boosting (XGBoost, LightGBM, CatBoost) • Support Vector Machines • k‑Nearest Neighbours • Neural Networks

#### Evaluation Cheatsheet

| Problem | Top Metrics |
| --- | --- |
| Classification | accuracy, precision, recall, F1, ROC‑AUC |
| Regression | MAE, MSE, RMSE, R² |

### 4.2 Unsupervised Learning

Finds structure in **unlabelled** data.

| Task | Goal | Example |
| --- | --- | --- |
| **Clustering** | group similar items | customer segmentation |
| **Dimensionality Reduction** | compress data while preserving structure | visualise high‑D bio‑markers |
| **Anomaly Detection** | flag out‑of‑pattern cases | credit‑card fraud alert |

**Popular Algorithms**
k‑Means • DBSCAN • Hierarchical Clustering • Gaussian Mixtures • PCA • t‑SNE • UMAP • Isolation Forest • One‑Class SVM • Autoencoders

> **FYI** – Anomalies come in *point*, *contextual* and *collective* flavours.

### 4.3 Reinforcement Learning

An **agent** learns via trial‑and‑error in an **environment** to maximise cumulative **reward**.

| Component | Role |
| --- | --- |
| Agent | Learner / decision maker |
| Environment | The world it acts in (maze, game, traffic) |
| State | Environment snapshot |
| Action | Choice the agent can make |
| Reward | Scalar feedback after action |
| Policy | Mapping state → action |

Core ideas: *exploration vs exploitation*, *discount factor*, *value functions*.

**Algorithms:** Q‑Learning • SARSA • Deep Q‑Network (DQN) • Proximal Policy Optimisation (PPO) • Actor–Critic • AlphaZero self‑play.

### 4.4 Emerging Paradigms (2025 & Beyond)

| Paradigm | Essence | Real‑World Spark |
| --- | --- | --- |
| **Semi‑Supervised** | small labelled + large unlabelled pool | medical imaging (few radiologist labels) |
| **Self‑Supervised** | generate labels from data itself | large language models predicting next‑word |
| **Transfer Learning** | reuse pre‑trained weights on new task | fine‑tuning BERT for legal texts |

## 5 Deep Learning in Focus

**Deep Learning (DL)** uses stacked layers of artificial neurons (a *deep* neural network) to discover increasingly abstract features directly from raw signals—pixels, waveforms, tokens, tabular rows—without heavy hand‑crafted engineering.

### 5.1 Key Architectures & Their Superpowers

| Family | Core Idea | Signature Strengths | Everyday Examples |
| --- | --- | --- | --- |
| **Convolutional Neural Networks (CNNs)** | Learn local spatial filters shared across the image | Image, video & audio recognition; robustness to translation | Face unlock, medical X‑ray triage, self‑driving lane detection |
| **Recurrent Nets (LSTM / GRU)** | Maintain a hidden state that rolls through time | Sequential & time‑series data; can remember long‑range context | Speech‑to...