---
title: [译][论文] P5 paper | 用语言模型做推荐：一种统一的预训练、个性化提示和预测范式（2022）
url: https://arthurchiao.github.io/blog/p5-paper-zh/
source: ArthurChiao's Blog
date: 2025-12-20
fetch_date: 2025-12-21T03:26:40.088288
---

# [译][论文] P5 paper | 用语言模型做推荐：一种统一的预训练、个性化提示和预测范式（2022）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] P5 paper | 用语言模型做推荐：一种统一的预训练、个性化提示和预测范式（2022）

Published at 2025-12-20 | Last Update 2025-12-20

### 译者序

本文翻译自 2022 年 RecSys 大会的一篇论文
[Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5)](https://arxiv.org/abs/2203.13366)。

![](/assets/img/p5-paper/fig-1.png)

Figure 1: P5 pretrains on an encoder–decoder Transformer model that takes in textual inputs and produces target responses.

![](/assets/img/p5-paper/fig-3.png)

图 3：P5 架构示意图。

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 现阶段推荐系统的特点](#11-现阶段推荐系统的特点)
    - [特征表示和学习越来越复杂](#特征表示和学习越来越复杂)
    - [推荐任务的类型越来越多样](#推荐任务的类型越来越多样)
  + [1.2 现代推荐系统需要什么](#12-现代推荐系统需要什么)
  + [1.3 P5 的创新点](#13-p5-的创新点)
* [2 相关工作](#2-相关工作)
  + [2.1 统一框架的尝试](#21-统一框架的尝试)
    - [基于通用语言模型（T5 和 GPT3）](#基于通用语言模型t5-和-gpt3)
    - [基于自然语言的 seq-to-seq 架构](#基于自然语言的-seq-to-seq-架构)
    - [基于通用用户表示](#基于通用用户表示)
  + [2.2 通过提示的方式学习（Prompt Learning）](#22-通过提示的方式学习prompt-learning)
  + [2.3 推荐领域的 NLP](#23-推荐领域的-nlp)
  + [2.4 Zero-shot 和冷启动推荐](#24-zero-shot-和冷启动推荐)
* [3 个性化 prompts 集合](#3-个性化-prompts-集合)
  + [3.1 Prompts 设计](#31-prompts-设计)
    - [rating prediction 提示词设计](#rating-prediction-提示词设计)
    - [**`sequential recommendation`** 提示词设计](#sequential-recommendation-提示词设计)
    - [**`explanation`** 提示词设计](#explanation-提示词设计)
    - [review 相关提示词设计](#review-相关提示词设计)
    - [**`direct recommendation`** 提示词设计](#direct-recommendation-提示词设计)
  + [3.2 从原始数据构建训练数据集（prompts & answers）](#32-从原始数据构建训练数据集prompts--answers)
* [4 P5 范式与模型](#4-p5-范式与模型)
  + [4.1 P5 架构](#41-p5-架构)
    - [位置编码](#位置编码)
    - [Whole-word embedding，补偿 item token 表示被 tokenizer 拆分带来的语义损失](#whole-word-embedding补偿-item-token-表示被-tokenizer-拆分带来的语义损失)
    - [encoder & decoder](#encoder--decoder)
  + [4.2 用预训练的 P5 进行推荐任务（推理）](#42-用预训练的-p5-进行推荐任务推理)
* [5 实验](#5-实验)
  + [5.0 要回答的问题 (RQ 1~5)](#50-要回答的问题-rq-15)
    - [问题一：P5 与 task-specific 方法的性能比较](#问题一p5-与-task-specific-方法的性能比较)
    - [问题二：P5 的零样本泛化能力](#问题二p5-的零样本泛化能力)
    - [问题三：P5 的性能如何受模型大小、任务数量和提示数量影响？](#问题三p5-的性能如何受模型大小任务数量和提示数量影响)
    - [问题四：P5 中实现个性化推荐的最佳方式是什么？（**`unique token vs. sub-word units`**）](#问题四p5-中实现个性化推荐的最佳方式是什么unique-token-vs-sub-word-units)
    - [问题五：P5 的预训练时间？P5 的推理性能？](#问题五p5-的预训练时间p5-的推理性能)
  + [5.1 Experimental Setup](#51-experimental-setup)
    - [Datasets](#datasets)
    - [Task splits](#task-splits)
    - [Implementation Details](#implementation-details)
    - [评估指标（Metrics）](#评估指标metrics)
    - [Rating Prediction and Direct Recommendation](#rating-prediction-and-direct-recommendation)
    - [Sequential Recommendation](#sequential-recommendation)
    - [Explanation Generation](#explanation-generation)
    - [Review Related](#review-related)
  + [5.3 Performance Comparison on Different Task Families (RQ1)](#53-performance-comparison-on-different-task-families-rq1)
    - [5.3.1 Rating Prediction](#531-rating-prediction)
    - [5.3.2 Sequential Recommendation](#532-sequential-recommendation)
    - [5.3.3 Explanation Generation](#533-explanation-generation)
    - [5.3.4 Review Related](#534-review-related)
    - [5.3.5 Direct Recommendation](#535-direct-recommendation)
  + [5.4 Zero-shot Generalization to Unseen Prompts and Items in New Domain (RQ2)](#54-zero-shot-generalization-to-unseen-prompts-and-items-in-new-domain-rq2)
    - [5.4.1 Transfer to Unseen Personalized Prompts](#541-transfer-to-unseen-personalized-prompts)
    - [5.4.2 Transfer to Items in New Domain](#542-transfer-to-items-in-new-domain)
  + [5.5 Ablation on Model Size (RQ3)](#55-ablation-on-model-size-rq3)
  + [5.6 Ablation on Task Scaling (RQ3)](#56-ablation-on-task-scaling-rq3)
  + [5.7 Ablation on Prompt Scaling (RQ3)](#57-ablation-on-prompt-scaling-rq3)
  + [5.8 如何实现个性化（**`unique tokens vs. sub-word units`**） (RQ4)](#58-如何实现个性化unique-tokens-vs-sub-word-units-rq4)
    - [Kimi 老师的进一步解释（译注）](#kimi-老师的进一步解释译注)
      * [一、参数效率与协同学习机制的根本差异](#一参数效率与协同学习机制的根本差异)
      * [二、任务场景差异的具体分析](#二任务场景差异的具体分析)
        + [1. P5-I 表现”相似或略好”的场景：回归任务 & 文本生成任务](#1-p5-i-表现相似或略好的场景回归任务--文本生成任务)
        + [2. P5-I 表现”显著更差”的场景：纯推荐任务](#2-p5-i-表现显著更差的场景纯推荐任务)
      * [三、数据集规模的影响](#三数据集规模的影响)
      * [四、总结](#四总结)
* [6 CONCLUSIONS AND FUTURE WORK](#6-conclusions-and-future-work)

---

# 摘要

长期以来，不同的推荐任务通常需要**针对特定任务**设计
**架构与训练目标** (task-specific architectures and training objectives)。
这导致**难以将学习到的知识与表征从一个任务迁移到另一个任务**，
从而**限制了现有推荐方法的泛化能力**。
例如，一个序列推荐模型 (sequential recommendation) 很难被应用或迁移到评论生成 (review generation) 任务中。

考虑到**语言几乎可以描述任何事物**，
而且语言基础是一种表征各种问题或任务的强大媒介，本文提出一种灵活、统一的**文本到文本**范式来解决以上问题 ——
这种范式我们称为 “**`Pretrain, Personalized Prompt, and Predict Paradigm`**” (预训练、个性化提示与预测范式)，缩写为 P5。
它将各类推荐任务统一在一个共享框架中，

* 在 P5 中，**所有数据**
  （user-item interactions, user descriptions, item metadata, user reviews 等）**都被转换为统一的自然语言序列**。
* **自然语言**所蕴含的丰富信息有助于 P5 **捕获更深层的语义**，从而实现**个性化推荐**。

具体而言，P5 在预训练阶段通过**相同的语言建模目标**学习**不同任务**，
从而成为各类下游推荐任务的基础模型。

* P5 不仅能轻松与其他模态信息融合，还能基于提示实现指令驱动的推荐。
* P5 将推荐系统从浅层模型、深度模型推进至大模型阶段，并将以**通用推荐引擎**的形式彻底革新推荐系统的技术形态。
* 通过为不同用户自适应生成个性化提示，P5 能够以零样本或少样本方式进行预测，大幅减少了对大量微调的依赖。

我们在多个推荐基准测试上进行了实验，验证了 P5 的有效性，相关代码和模型也已经开源：

* [github.com/jeykigung/P5](https://github.com/jeykigung/P5) 开源了源代码、数据集、提示词及预训练的 P5 模型。
* [huggingface.co/makitanikaze/P5](https://huggingface.co/makitanikaze/P5) 模型。

# 1 引言

过去几十年，推荐系统取得了显著进步，并在人们的日常生活中发挥着重要作用。
而现在，推荐系统在朝着特征更多样性、应用场景更广泛的综合系统发展。

## 1.1 现阶段推荐系统的特点

### 特征表示和学习越来越复杂

推荐系统中的 feature engineering 和 learning 已经从简单发展到复杂。

* 早期，推荐系统通常采用 **`logistic regression`** 或 **`collaborative filtering`** [25, 35, 50, 52]，利用 **`user-item
  interaction`** 数据来建模用户的行为模式。
* 之后，通过更复杂的模型如 factorization machines [48] 和 GBDT [20]，将 **`contextual features`**（如 **`user profile`** 和 **`item
  metadata`**）进一步整合到系统中。
* 最近，**`deep neural network models`**
  [3, 5, 19, 74] 促进了更加多样和复杂的特征之间的交叉与组合。因此，与传统基于
  feature engineering 的方法相比，这些模型获得了更好的表示能力。

### 推荐任务的类型越来越多样

**推荐任务的类型**也越来越多。
除了经典的 rating prediction 和基于 direct user-item matching 的推荐任务之外，
最近的研究正在将范围扩展到新的任务和场景，如

1. sequential recommendation [21, 60, 63, 80]
2. conversational recommendation [8, 61, 76]
3. explainable recommendation [17, 31, 62, 70, 75, 77]

等等。虽然上述推荐任务的方法通常是单独提出的，但一个明显的趋势是
**利用多个推荐任务来联合学习** **`transferable representations`** [31, 56, 57, 72]。

## 1.2 现代推荐系统需要什么

尽管现有的推荐系统取得了巨大成功，但在解决实际问题上仍面临很多问题，我们认为需要
一个能支持多样特征和不同类型任务的综合推荐系统。

推荐任务通常**共享同一个 user–item pool**（用户-物品信息池）
并**具有重叠的 contextual features**，
因此，我们任务**将多个推荐任务合并到一个统一框架中**是非常有希望的，
这样多个任务可以**隐式地 transfer knowledge**，相互受益，
并**泛化**到其它没见过的任务。

## 1.3 P5 的创新点

受最近 multitask prompt-based training [1, 51, 67] 进展的启发，本文提出一个统一的范式 P5。
它有三个主要优势：

1. 将**推荐模型**（行为模型）深度融入到**语言环境**（语言模型）中。

   基于 personalized prompts，**所有推荐任务都被重新表述为 NLP 任务**。
   由于自然语言足够灵活和强大，能够**用文本表达各种类型的特征**，
   因此**无需设计 feature-specific encoders**。
   通过这种方式，P5 可以充分利用训练语料库中丰富的语义和知识；

   > 译注：[从 Tokenization 视角看生成式推荐（GR）近几年的发展（2025）](/blog/large-generative-recommendation-tokenization-perspective-notes-zh/)
   >
   > ![](/assets/img/large-generative-recommendation-tokenization-perspective/model-as-reflection-of-real-world.png)
2. 将多个推荐任务放到同一个 text-to-text
   encoder-decoder 中，并使用**相同的 language modeling loss 进行训练**，
   而不是设计 task-specific 架构和 objective functions。

   换句话说，
   P5 **将所有 personalized tasks 视为 conditional text generation 问题**；
3. 通过 instruction-based prompts 训练，P5 在推广到新的 personalized prompts 或其它
   领域中未见过的 items 时，获得了**良好的 zero-shot 性能**。

![](/assets/img/p5-paper/fig-1.png)

Figure 1: P5 pretrains on an encoder–decoder Transformer model that takes in textual inputs and produces target responses.
We trained P5 on a multitask collection of personalized prompts. After multitask prompt-based pretraining on recommendation datasets, P5 achieves the capability of zero-shot generalization to unseen person...