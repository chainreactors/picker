---
title: [译][论文] BERT：预训练深度双向 Transformers 做语言理解（Google，2019）
url: https://arthurchiao.github.io/blog/bert-paper-zh/
source: ArthurChiao's Blog
date: 2024-03-11
fetch_date: 2025-10-04T12:07:58.499149
---

# [译][论文] BERT：预训练深度双向 Transformers 做语言理解（Google，2019）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] BERT：预训练深度双向 Transformers 做语言理解（Google，2019）

Published at 2024-03-10 | Last Update 2024-03-24

### 译者序

本文翻译自 2019 年 Google 的论文：
[BETT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)。

```
@article{devlin2018bert,
  title={BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}
```

与 GPT 一样，BERT **也基于 transformer 架构**，
从诞生时间来说，它位于 GPT-1 和 GPT-2 之间，是有代表性的现代 transformer 之一，
现在仍然在很多场景中使用，

![](/assets/img/llm-practical-guide/fig-1.png)

大模型进化树，可以看到 BERT 所处的年代和位置。来自 [大语言模型（LLM）综述与实用指南（Amazon，2023）](/blog/llm-practical-guide-zh/)。

根据 [Transformer 是如何工作的：600 行 Python 代码实现 self-attention 和两类 Transformer（2019）](/blog/transformers-from-scratch-zh/)，
BERT 是首批 **在各种自然语言任务上达到人类水平**的 transformer 模型之一。
预训练和 fine-tuning **代码**：[github.com/google-research/bert](https://github.com/google-research/bert)。

BERT 模型只有 **`0.1b ~ 0.3b`** 大小，因此在 CPU 上也能较流畅地跑起来。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 Pre-trained model 适配具体下游任务的两种方式](#11-pre-trained-model-适配具体下游任务的两种方式)
  + [1.2 以 OpenAI GPT 为代表的单向架构存在的问题](#12-以-openai-gpt-为代表的单向架构存在的问题)
  + [1.3 BERT 创新之处](#13-bert-创新之处)
  + [1.4 本文贡献](#14-本文贡献)
* [2 相关工作](#2-相关工作)
  + [2.1 无监督基于特征（Unsupervised Feature-based）的方法](#21-无监督基于特征unsupervised-feature-based的方法)
  + [2.2 无监督基于微调（Unsupervised Fine-tuning）的方法](#22-无监督基于微调unsupervised-fine-tuning的方法)
  + [2.3 基于监督数据的转移学习（Transfer Learning from Supervised Data）](#23-基于监督数据的转移学习transfer-learning-from-supervised-data)
* [3 BERT](#3-bert)
  + [3.0 BERT 架构](#30-bert-架构)
    - [3.0.1 BERT 模型架构和参数](#301-bert-模型架构和参数)
    - [3.0.2 输入/输出表示](#302-输入输出表示)
  + [3.1 预训练 BERT](#31-预训练-bert)
    - [3.1.1 任务 `＃1`：掩码语言模型（Masked LM）](#311-任务-1掩码语言模型masked-lm)
    - [3.1.2 任务 `＃2`：下一句预测（Next Sentence Prediction, NSP）](#312-任务-2下一句预测next-sentence-prediction-nsp)
    - [3.1.3 预训练数据集](#313-预训练数据集)
  + [3.2 微调 BERT](#32-微调-bert)
  + [3.3 各种场景](#33-各种场景)
* [4 实验](#4-实验)
  + [4.1 GLUE (General Language Understanding Evaluation)](#41-glue-general-language-understanding-evaluation)
    - [4.1.1 Fine-tune 工作](#411-fine-tune-工作)
    - [4.1.2 参数设置](#412-参数设置)
    - [4.1.3 结果](#413-结果)
  + [4.2 SQuAD (Stanford Question Answering Dataset) v1.1](#42-squad-stanford-question-answering-dataset-v11)
  + [4.3 SQuAD v2.0](#43-squad-v20)
  + [4.4 SWAG (Situations With Adversarial Generations)](#44-swag-situations-with-adversarial-generations)
* [5 对照研究](#5-对照研究)
  + [5.1 预训练任务（MLM/NSP）的影响](#51-预训练任务mlmnsp的影响)
    - [5.1.1 训练组](#511-训练组)
    - [5.1.2 结果对比](#512-结果对比)
    - [5.1.3 与 ELMo 的区别](#513-与-elmo-的区别)
  + [5.2 模型大小的影响](#52-模型大小的影响)
  + [5.3 BERT 基于特征的方式](#53-bert-基于特征的方式)
    - [5.3.1 基于特征的方式适用的场景](#531-基于特征的方式适用的场景)
    - [5.3.2 实验](#532-实验)
    - [5.3.3 结果](#533-结果)
* [6 总结](#6-总结)
* [附录](#附录)
  + [A. Additional Details for BERT](#a-additional-details-for-bert)
    - [A.1 Illustration of the Pre-training Tasks](#a1-illustration-of-the-pre-training-tasks)
    - [A.2 Pre-training Procedure](#a2-pre-training-procedure)
    - [A.3 Fine-tuning Procedure](#a3-fine-tuning-procedure)
    - [A.4 Comparison of BERT, ELMo ,and OpenAI GPT](#a4-comparison-of-bert-elmo-and-openai-gpt)
    - [A.5 Illustrations of Fine-tuning on Different Tasks](#a5-illustrations-of-fine-tuning-on-different-tasks)
  + [B. Detailed Experimental Setup](#b-detailed-experimental-setup)
  + [C. Additional Ablation Studies](#c-additional-ablation-studies)
* [参考文献](#参考文献)

---

# 摘要

本文提出 **`BERT`**（Bidirectional Encoder Representations from Transformers，
**基于 Transformers 的双向 Encoder 表示**） —— 一种新的语言表示模型
（language representation model）。

* 与最近的语言表示模型（Peters 等，2018a; Radford 等，2018）不同，
  BERT 利用了**所有层中的左右上下文**（both left and right context in all layers），
  在**无标签文本**（unlabeled text）上
  **预训练深度双向表示**（pretrain deep bidirectional representations）。
* **只需添加一个额外的输出层**，而无需任何 task-specific 架构改动，就可以对预训练的 BERT 模型进行微调，
  创建出用于各种下游任务（例如问答和语言推理）的高效模型。

BERT 在概念上很简单，实际效果却很强大，在 11 个自然语言处理任务中刷新了目前业界最好的成绩，包括，

* GLUE score to 80.5% (7.7% point absolute improvement)
* MultiNLI accuracy to 86.7% (4.6% absolute improvement)
* SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement)
* SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement)

# 1 引言

业界已证明，**语言模型预训练**（Language model pre-training）
能**显著提高许多自然语言处理（NLP）任务的效果**（Dai 和 Le，2015; Peters 等，2018a; Radford 等，2018; Howard 和 Ruder，2018）。
这些任务包括：

* **`sentence-level tasks`**：例如自然语言**推理**（Bowman 等，2015; Williams 等，2018）；
* **`paraphrasing`**（Dolan 和 Brockett，2005）：整体分析句子来预测它们之间的关系；
* **`token-level tasks`**：例如 named entity recognition 和**问答**，其模型需要完成 token 级别的细粒度输出（Tjong Kim Sang 和 De Meulder，2003; Rajpurkar 等，2016）。

## 1.1 Pre-trained model 适配具体下游任务的两种方式

将预训练之后的语言表示（pre-trained language representations）应用到下游任务，目前有两种策略：

1. **基于特征的方式**（feature-based approach）：例如 **`ELMo`**（Peters 等，2018a），**使用任务相关的架构，将预训练表示作为附加特征**。
2. **微调**（fine-tuning）：例如 **`Generative Pre-trained Transformer`** (OpenAI **`GPT`**)（Radford 等，2018），
   引入最少的 task-specific 参数，通过**微调所有预训练参数**来训练下游任务。

这两种方法都是使用**单向语言模型**来学习**通用语言表示**。

## 1.2 以 OpenAI GPT 为代表的单向架构存在的问题

我们认为，以上两种方式（尤其是微调）**限制了 pre-trained language representation 的能力**。
主要是因为其**语言模型是单向的**，这**限制了预训练期间的架构选择范围**。

例如，OpenAI GPT 使用从左到右的架构（Left-to-Right Model, LRM），因此
Transformer self-attention 层中的 token 只能关注它前面的 tokens（只能用到前面的上下文）：

* 对于**句子级别的任务**，这将导致**次优**结果；
* 对 **token 级别的任务**（例如问答）使用 fine-tuning 方式效果可能非常差，
  因为这种场景**非常依赖双向上下文**（context from both directions）。

## 1.3 BERT 创新之处

本文提出 BERT 来**改进基于微调的方式**。

受 Cloze（完形填空）任务（Taylor，1953）启发，BERT 通过一个**“掩码语言模型”**（masked language model, MLM）做预训练，
避免前面提到的**单向性带来的问题**，

* MLM **随机掩盖输入中的一些 token** ，仅基于上下文来**预测被掩盖的单词**（单词用 ID 表示）。
* 与从左到右语言模型的预训练不同，MLM 能够**同时利用左侧和右侧的上下文**，
  从而预训练出一个深度**双向** Transformer。

除了掩码语言模型外，我们还使用**“下一句预测”**（next sentence prediction, **`NSP`**）
任务来联合预训练 text-pair representation。

## 1.4 本文贡献

1. 证明了双向预训练对于语言表示的重要性。
   与 Radford 等（2018）使用单向模型预训练不同，BERT 使用掩码模型来实现预训练的深度双向表示。
   这也与 Peters 等（2018a）不同，后者使用独立训练的从左到右和从右到左的浅连接。
2. 展示了 pre-trained representations 可以**减少**对许多 task-specific 架构的**重度工程优化**。
   BERT 是第一个在大量 sentence-level 和 token-level 任务上达到了 state-of-the-art 性能的
   **基于微调的表示模型**，超过了许多 task-specific 架构。
3. BERT 刷新了 11 个自然语言处理任务的最好性能。

代码和预训练模型见 [github.com/google-research/bert](https://github.com/google-research/bert)。

# 2 相关工作

（这节不是重点，不翻译了）。

There is a long history of pre-training general language representations, and we briefly review the
most widely-used approaches in this section.

## 2.1 无监督基于特征（Unsupervised Feature-based）的方法

Learning widely applicable representations of
words has been an active area of research for
decades, including non-neural (Brown et al., 1992;
Ando and Zhang, 2005; Blitzer et al., 2006) and
neural (Mikolov et al., 2013; Pennington et al.,
2014) methods. **`Pre-trained word embeddings`**
are an integral part of modern NLP systems, offering significant improvements over embeddings
learned from scratch (Turian et al., 2010). To pretrain word embedding vectors,
**`left-to-right language modeling`** objectives have been used (Mnih
and Hinton, 2009), as well as objectives to discriminate correct from incorrect words in left and
right context (Mikolov et al., 2013).

These approaches have been generalized to coarser granularities, such as

* **`sentence embeddings`** (Kiros et al., 2015; Logeswaran and Lee, 2018)
* **`paragraph embeddings`** (Le and Mikolov, 2014).

To train sentence representations, prior
work has used objectives to rank candidate next
sentences (Jernite et al., 2017; Logeswaran and
Lee, 2018), left-to-right generation of next sentence words given a...