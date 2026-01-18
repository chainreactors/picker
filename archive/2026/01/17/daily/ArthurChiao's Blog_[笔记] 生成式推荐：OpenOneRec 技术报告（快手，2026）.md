---
title: [笔记] 生成式推荐：OpenOneRec 技术报告（快手，2026）
url: https://arthurchiao.art/blog/openonerec-tech-report-notes-zh/
source: ArthurChiao's Blog
date: 2026-01-17
fetch_date: 2026-01-18T03:38:08.882951
---

# [笔记] 生成式推荐：OpenOneRec 技术报告（快手，2026）

# [ArthurChiao's Blog](https://arthurchiao.art/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)
* [RSS](/feed.xml)

TOC

# [笔记] 生成式推荐：OpenOneRec 技术报告（快手，2026）

Published at 2026-01-17 | Last Update 2026-01-17

本文是阅读学习快手的 [OpenOneRec Tech Report](https://arxiv.org/html/2512.24762v1) 时整理的一些笔记，
很多训练相关的信息已经开源，见 [github.com/Kuaishou-OneRec/OpenOneRec](https://github.com/Kuaishou-OneRec/OpenOneRec)，
包括：

1. **测评框架** RecIF-Bench 和**训练数据**：16w 用户，96million 交互数据
2. **数据处理代码、训练代码**，确保可复现文中内容（非 pro 版本）
3. **训练好的模型**：1.7B、8B

整体框架：

![](/assets/img/openonerec/fig-2.png)

训练&评估任务：

![](/assets/img/openonerec/fig-4.png)

相关文章：

* [从 Tokenization 视角看生成式推荐（GR）近几年的发展（2025）](/blog/large-generative-recommendation-tokenization-perspective-notes-zh/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 引言](#1-引言)
  + [1.1 RecIF-Bench：推荐领域的指令遵循 benchmark](#11-recif-bench推荐领域的指令遵循-benchmark)
  + [1.2 缓解 SFT 带来的通用能力退化](#12-缓解-sft-带来的通用能力退化)
  + [1.3 开源模型：1.7B/8B](#13-开源模型17b8b)
* [2 基础](#2-基础)
  + [2.1. Items as Tokens: 商品的语义编码](#21-items-as-tokens-商品的语义编码)
  + [2.2. Recommendation as Auto-regressive Models：用自回归模型做推荐](#22-recommendation-as-auto-regressive-models用自回归模型做推荐)
* [3 RecIF-Bench: 推荐领域的指令遵循 Benchmark](#3-recif-bench-推荐领域的指令遵循-benchmark)
  + [3.1 数据集构建](#31-数据集构建)
    - [数据集切分策略：按用户维度 `80:20` 切分](#数据集切分策略按用户维度-8020-切分)
  + [3.2 评估任务：4 层，从对齐到推理](#32-评估任务4-层从对齐到推理)
    - [3.2.1. Layer 0: 语义对齐能力](#321-layer-0-语义对齐能力)
    - [3.2.2. Layer 1: 基础推荐能力](#322-layer-1-基础推荐能力)
    - [3.2.3. Layer 2: 指令遵循能力](#323-layer-2-指令遵循能力)
    - [3.2.4. Layer 3: 推理能力（推荐理由）](#324-layer-3-推理能力推荐理由)
  + [3.3. 评估指标](#33-评估指标)
    - [推荐指标：`Pass@K, Recall@K`](#推荐指标passk-recallk)
    - [文本生成指标：`LLM-as-Judge`](#文本生成指标llm-as-judge)
* [4 Pre-Training](#4-pre-training)
  + [4.1 Item Tokenization](#41-item-tokenization)
    - [4.1.1 Rec-domain 训练数据](#411-rec-domain-训练数据)
    - [4.1.2. General-domain 训练数据](#412-general-domain-训练数据)
  + [4.2. 训练配方](#42-训练配方)
    - [Stage 1: Itemic-Text Alignment（冻结大部分参数）](#stage-1-itemic-text-alignment冻结大部分参数)
    - [Stage 2: Full-Parameter Co-Pretraining（全参继续预训练）](#stage-2-full-parameter-co-pretraining全参继续预训练)
    - [Training Recipe](#training-recipe)
* [5 Post-Training](#5-post-training)
  + [5.1. 恢复通用 instruct-following & thinking 能力：多任务 SFT](#51-恢复通用-instruct-following--thinking-能力多任务-sft)
  + [5.2. 恢复通用 reasoning 能力：On-policy Distillation](#52-恢复通用-reasoning-能力on-policy-distillation)
    - [Off-Policy vs. On-Policy Distillation](#off-policy-vs-on-policy-distillation)
    - [实现](#实现)
    - [效果验证](#效果验证)
  + [5.3. 针对推荐任务的强化学习：GRPO](#53-针对推荐任务的强化学习grpo)
* [6 评估](#6-评估)
* [7 结论、局限性和未来方向](#7-结论局限性和未来方向)
  + [7.1 Tokenizer 的可迁移性](#71-tokenizer-的可迁移性)
  + [7.2 最优数据配比](#72-最优数据配比)
  + [7.3 思维链推理目前仅在有限场景中带来改进](#73-思维链推理目前仅在有限场景中带来改进)
* [附录 B](#附录-b)
  + [B.3. Pre-training 数据 sample（推荐领域）](#b3-pre-training-数据-sample推荐领域)
    - [B.3.1. 物品描述数据（Itemic Dense Caption Data）](#b31-物品描述数据itemic-dense-caption-data)
    - [B.3.2. 顺序用户行为数据（Sequential User Behavior Data）](#b32-顺序用户行为数据sequential-user-behavior-data)
    - [B.3.3. 用户综合事实数据（点赞、收藏、评论 … ）](#b33-用户综合事实数据点赞收藏评论--)
  + [B.4. Pre-training 数据配比和 Token Budgets](#b4-pre-training-数据配比和-token-budgets)
  + [B.5. SFT 数据配比和 Token Budgets](#b5-sft-数据配比和-token-budgets)

---

# 1 引言

## 1.1 RecIF-Bench：推荐领域的指令遵循 benchmark

本文提出了 RecIF-Bench：一个**推荐领域**的**指令遵循**测试基准 (benchmark)。

* 能评估 8 种任务类型，从基础推荐到复杂推理
* 场景包括：**短视频、电商、在线广告**（short-video, e-commerce, and online advertising）

## 1.2 缓解 SFT 带来的通用能力退化

为了缓解 SFT 带来的通用能力退化，本文引入了一个**两阶段对齐策略**，
能同时**恢复通用能力+提升具体任务的准确率**：

1. **`on-policy distillation`**
2. **`recommendation-oriented Reinforcement Learning`** (Rec-RL)

## 1.3 开源模型：1.7B/8B

每个尺寸的模型又分为两个版本，

1. Standard 版本：基于开源数据训练
2. Pro 版本：用快手的 a hundred-billion-token industrial corpus 增强

# 2 基础

## 2.1. Items as Tokens: 商品的语义编码

将 Item 作为一个独立的模态（a distinct modality），采用 Itemic Tokens 方案 (Luo et al., 2025; Zhou et al., 2025a)，见图 2，

![](/assets/img/openonerec/fig-2.png)

Figure 2 | OneRec 整体框架。
(1) Pre-Training: 通过 `Itemic-Text Alignment` 和**推荐领域+通用领域数据的联合预训练**，使模型能**理解推荐领域的业务语义**。
(2) Post-Training: 通过 **`SFT`** 解锁多种下游任务能力，
以及通过交替进行**通用蒸馏**和**强化学习**来平衡模型的**通用推理能力和推荐能力**。
(3) Evaluation: 基于 RecIF-Bench，以及这 Amazon 数据集上验证跨领域转移能力。

采用 **`RQ-Kmeans`** (Luo et al., 2025)，将 item metadata 的语义 embedding 离散化为 discrete codes。

* 将 item semantics 压缩为了**短的、固定长度的序列**，在保留 collaborative structure 的同时使得长上下文建模更加高效；
* 这些 tokens 自带的层级特性（hierarchical nature of these tokens）确保了**语义类似的商品，共享相同的 prefixes**，
  使得模型能基于 token 相似性转移知识，类似于自然语言 tokens 中的语义关系编码。

## 2.2. Recommendation as Auto-regressive Models：用自回归模型做推荐

* **扩展词表**：将 item tokens 添加到模型原有的 vocabulary： V = V𝑡𝑒𝑥𝑡 ∪ V𝑖𝑡𝑒𝑚. 这种方式使我们能将用户的交互历史作为 text+item 的一个长上下文序列，而不是作为一个特殊的数据结构，跟基座语言模型还是一致的。
* 训练目标：**`Next-Token Prediction`**
* 训练任务：ranging from prediction (e.g., retrieval) to reasoning (e.g., explanation)

# 3 RecIF-Bench: 推荐领域的指令遵循 Benchmark

## 3.1 数据集构建

### 数据集切分策略：按用户维度 `80:20` 切分

基于**用户**维度切分训练集和测试集。**`20w`** 用户，**随机拆分**，

* 80% 训练
* 20% 测试

## 3.2 评估任务：4 层，从对齐到推理

RecIF-Bench 将 8 类任务分为了 4 层。

Table 2 | RecIF-Bench 任务术语：8 类任务分为 4 层，描述了它们的 input/output 格式和评估重点。

![](/assets/img/openonerec/table-2.png)

训练数据样例：

![](/assets/img/openonerec/fig-4.png)

Figure 4 | RecIF-Bench **任务举例**。We organize 8 tasks across 4 capability layers, specifying the instruction, context, and target.

### 3.2.1. Layer 0: 语义对齐能力

评估模型是否已经**抹平 itemic tokens 和 natural language 之间的差异**，这是后续所有任务的基础。

* 训练任务：
  + **继续预训练**（CPT）：`Item 描述 -> Item Token`
* 评估任务
  + **`Item Understanding`**：`Item Token -> Item textual metadata` (e.g., title, caption)

### 3.2.2. Layer 1: 基础推荐能力

评估模型**捕捉用户偏好的能力**，预测**用户-货品交互行为**，

1. Short Video Recommendation.
2. Ad / Product Recommendation (Cross-Domain).
3. Label Prediction. Given the user’s history H 𝑣𝑖𝑑𝑒𝑜 and a candidate item 𝑖, the model predicts whether the user will engage (e.g., effective view) with a binary **`Yes/No`** response.

### 3.2.3. Layer 2: 指令遵循能力

这一层评估模型是否能**将预测能力适应到自然语言指令上**，也就是自然语言推荐任务的指令遵循能力，这是基于 LLM 的推荐系统与传统推荐系统的核心不同。

1. **交互式推荐**. Given the user portrait P and a natural language query 𝑞
   * 输入：
     + 用户画像 P
     + 自然语言 query 𝑞（例如，“放松的视频”）
   * 输出：
     + 用户可能会积极互动（点击、点赞、收藏等）的物品
2. **条件推荐**：更细粒度的行为建模
   * 输入：
     + 用户历史行为 H𝑣𝑖𝑑𝑒𝑜
     + 目标行为 label 𝑎（例如，点赞、分享等）
   * 输出：
     + 用户在给定目标行为下会积极互动（点击、点赞、收藏等）的物品

### 3.2.4. Layer 3: 推理能力（推荐理由）

输入：

* 用户画像 P
* 用户历史行为 H𝑣𝑖𝑑𝑒𝑜
* 推荐物品 𝑠

输出：**一段自然语言的推荐理由，解释为什么推荐这个商品**。

> Ground Truth for L3: Since reasoning tasks lack natural ground truth, we use Gemini-2.5-Pro with
> full metadata access to **`generate high-quality reference outputs`**.

## 3.3. 评估指标

### 推荐指标：`Pass@K, Recall@K`

对推荐任务 (Layer 1 & 2)，使用如下评估指标：

* Pass@1/Pass@32. Pass@K measures whether the ground truth item appears in the top-K generated candidates
* Recall@32. Recall@K measures the proportion of relevant items retrieved.

### 文本生成指标：`LLM-as-Judge`

对文本生成任务 (Layer 0 & 3), we employ LLM-as-Judge,
prompting an independent LLM to rate the generated text on dimensions such as accuracy and
coherence. 详见 Appendix B.1

# 4 Pre-Training

## 4.1 Item Tokenization

* 三层量化，每层的 codebook size of 8192
* Each item 𝑖 is thus mapped to a tuple of hierarchical codes 𝑆𝑖 = (𝑐1, 𝑐2, 𝑐3), which is then flattened into a token sequence wrapped by special tokens:

```
<|item_begin|><item_a_5028><item_b_6733><item_c_2559><|item_end|>
```

### 4.1.1 Rec-domain 训练数据

为了增强模型对 item 的推荐能力，对 item metadata 数据分为了三类：

1. **`Itemic Dense Caption Data`**：基础的物品语义数据
   1. 训练任务：给定 itemic tokens，让模型生成 corresponding natural-language caption
   2. 在商品的 SID 和文本描述之间建立语义映射。
2. **`Sequential User Behavior Data`**：基础推荐能力的核心训练语料

   1. 内容包括用户的观看、点赞、分享等行为。通过训练模型在长期序列中进行 next-item prediction，我们使其能够内化基础的协同过滤信号和 temporal patterns。
   2. 让模型具备根据 historical behavioral trajectory 预测用户 future interest 的能力.
3. **`Interleaved User Persona Grounding Data`**：构建量化空间的 deep semantic groundin...