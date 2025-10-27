---
title: [译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）
url: https://arthurchiao.github.io/blog/llama2-paper-zh/
source: ArthurChiao's Blog
date: 2023-08-07
fetch_date: 2025-10-04T11:59:21.130038
---

# [译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）

Published at 2023-08-06 | Last Update 2025-02-15

### 译者序

本文来自 2023 年 Meta（facebook）的大模型论文：
[Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)。
翻译了其中感兴趣的部分。

LLaMA2 用了两个 GPU 集群进行训练：

1. RSC 集群：**`200Gbps InfiniBand + 400W A100 GPU`**；
2. 生产集群：**`200Gbps RoCE + 350W A100 GPU`**；

**`RoCE + 350W GPU`** 的集群，经过优化的代码能达到
**`IB + 400W GPU`** 集群性能的 **`90%`**。
总共耗费 **`3.3M GPU-hour`**。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 现状：没有能与 ChatGPT 匹敌的开源大模型](#11-现状没有能与-chatgpt-匹敌的开源大模型)
  + [1.2 开源 LLaMA2/LLaMA2-Chat，填补空白](#12-开源-llama2llama2-chat填补空白)
  + [1.3 LLaMA2 是如何炼成的：训练+微调鸟瞰](#13-llama2-是如何炼成的训练微调鸟瞰)
  + [1.4 本文组织](#14-本文组织)
* [2 预训练（Pretraining）](#2-预训练pretraining)
  + [2.1 预训练数据（Pretraining Data）](#21-预训练数据pretraining-data)
  + [2.2 训练细节（Training Details）](#22-训练细节training-details)
    - [2.2.1 超参数（Hyperparameters）](#221-超参数hyperparameters)
    - [2.2.2 分词器（Tokenizer）](#222-分词器tokenizer)
    - [2.2.3 训练硬件和碳足迹](#223-训练硬件和碳足迹)
      * [训练硬件（Training Hardware）](#训练硬件training-hardware)
      * [预训练碳足迹（Carbon Footprint of Pretraining）](#预训练碳足迹carbon-footprint-of-pretraining)
  + [2.3 LLaMA 2 预训练模型性能评估（Pretrained Model Evaluation）](#23-llama-2-预训练模型性能评估pretrained-model-evaluation)
    - [2.3.1 与开源基座大模型对比](#231-与开源基座大模型对比)
    - [2.3.2 与闭源大模型对比](#232-与闭源大模型对比)
* [3 微调（Fine-tuning）](#3-微调fine-tuning)
  + [3.1 监督式微调（SFT）](#31-监督式微调sft)
    - [3.1.1 使用公开的指令微调数据](#311-使用公开的指令微调数据)
    - [3.1.2 标注质量为王（Quality Is All You Need）](#312-标注质量为王quality-is-all-you-need)
    - [3.1.3 一些微调细节（Fine-Tuning Details）](#313-一些微调细节fine-tuning-details)
  + [3.2 基于人类反馈的强化学习（RLHF）](#32-基于人类反馈的强化学习rlhf)
    - [3.2.1 人类偏好数据收集](#321-人类偏好数据收集)
    - [3.2.2 奖励建模（Reward Modeling）](#322-奖励建模reward-modeling)
      * [训练目标](#训练目标)
      * [Data Composition](#data-composition)
      * [训练细节（Training Details）](#训练细节training-details)
      * [奖励模型的结果（Reward Model Results）](#奖励模型的结果reward-model-results)
      * [Scaling Trends](#scaling-trends)
    - [3.2.3 迭代式微调（Iterative Fine-Tuning）](#323-迭代式微调iterative-fine-tuning)
      * [Rejection Sampling（拒绝采样）](#rejection-sampling拒绝采样)
      * [PPO](#ppo)
  + [3.3 System Message for Multi-Turn Consistency](#33-system-message-for-multi-turn-consistency)
  + [3.4 RLHF Results](#34-rlhf-results)
    - [3.4.1 Model-Based Evaluation](#341-model-based-evaluation)
    - [3.4.2 Human Evaluation](#342-human-evaluation)
* [4 Safety（略）](#4-safety略)
* [5 讨论](#5-讨论)
  + [5.1 新发现与点评](#51-新发现与点评)
    - [超越人类监督：从 SFT 到 RLHF](#超越人类监督从-sft-到-rlhf)
    - [In-Context Temperature Rescaling](#in-context-temperature-rescaling)
    - [LLaMA2-Chat 时间感知能力（Temporal Perception）](#llama2-chat-时间感知能力temporal-perception)
    - [工具的使用](#工具的使用)
  + [5.2 限制和伦理考虑](#52-限制和伦理考虑)
  + [5.3 负责任的发布策略（Responsible Release Strategy）](#53-负责任的发布策略responsible-release-strategy)
    - [5.3.1 发布细节](#531-发布细节)
    - [5.3.2 负责任的发布](#532-负责任的发布)
* [6 相关工作](#6-相关工作)
  + [6.1 Large Language Models](#61-large-language-models)
  + [6.2 Instruction Tuning](#62-instruction-tuning)
  + [6.3 Known LLM Safety Challenges](#63-known-llm-safety-challenges)
* [7 总结](#7-总结)
* [参考文献（略）](#参考文献略)
* [附录（略）](#附录略)

---

# 摘要

本文介绍 LLaMA 2，我们开发的一组**预训练和微调**大语言模型集，

* LLaMA2 参数规模 **`7b~70b`**；
* 微调模型称为 **`LLaMA2-Chat`**，针对对话场景进行了优化。

与**其他开源聊天模型**进行比较，

* 大多数基准测试中，LLaMA2 性能更好；
* 有用性和安全性方面，人工评估（human evaluations）的结果也证明 LLaMA2 更优。

因此，LLaMA2 可以作为一个不错的**闭源模型替代方案**。
本文将详细描述我们是如何对 LLaMA2-Chat 进行微调和安全性改进的。
社区可以在我们的工作基础上进一步开发迭代，为 LLM 的负责任发展做出贡献。

# 1 引言

大语言模型（LLM）作为功能强大的人工智能助手，在涉及跨领域、需要专业知识
（例如**编程和创意写作**）的**复杂推理任务**中表现出了巨大的潜力。
LLM 通过聊天窗口与人类进行交互，简单方便，因此一经推出就迅速打开大众市场。

如果考虑到背后的**训练方法论**本质上非常**简单直观**，

* 首先，在大量自监督数据上对 **`auto-regressive transforer`** 进行**预训练**，
* 然后，通过基于人类反馈的强化学习（**`RLHF`**）等技术**与人类偏好对齐**。

就更会震惊于 LLM 的能力是多么出众。

## 1.1 现状：没有能与 ChatGPT 匹敌的开源大模型

大模型的训练方法很简单，但是，极高的**算力要求**限制了它的发展，
结果是只有少数几家公司有财力进行研究和训练。
虽然之前已经开源了一些预训练的大模型，包括

1. BLOOM（Scao 等，2022）
2. LLaMA-1（Touvron 等，2023）
3. Falcon（Penedo 等，2023）

这些模型的**性能已经与 GPT-3**（Brown 等，2020）和 Chinchilla（Hoffmann 等，2022）
等闭源预训练模型**相当**，但它们还无法成为 ChatGPT、BARD 和 Claude
等**性能更强大的闭源、生产级大模型**的替代品，

* 后者做了**大量微调**以与人类偏好对齐，
  极大增强了它们的可用性和安全性；
* 这一过程需要大量的**算力和人工标注成本**，并且通常不透明，也难以轻松照搬，
  因此限制了社区在 advance AI alignment research 方面的进展。

## 1.2 开源 LLaMA2/LLaMA2-Chat，填补空白

本文介绍我们开源的 LLaMA2，这是一组预训练和微调的 LLM，包括 LLaMA2 和 LLaMA2-Chat。
与其他开源 chat models 进行比较，

* 大多数基准测试中，LLaMA2 性能更好；
* 有用性和安全性方面，人工评估（human evaluations）的结果也证明 LLaMA2 更优。

因此，LLaMA2 可以作为一个不错的**闭源模型替代方案**。
本文将详细描述我们是如何对 LLaMA2-Chat 进行微调和安全性改进的，
这样社区就能够在我们的工作基础上进一步开发迭代，为 LLM 的负责任发展做出贡献。
具体来说，我们向公众（the general public）开源以下模型，供**研究和商业使用**（research and commercial use）：

1. LLaMA2：这是 LLaMA 1 的升级版

   * 新组合了公开可用数据（a new mix）进行训练，数据集大小 **`+40%`**（1.4T tokens -> 2T tokens），
   * 模型的**上下文长度翻倍**，
   * 采用了 grouped-query attention（Ainslie 等，2023）。

   本次发布 7B/13B/70B 参数的 LLaMA2 模型。
   **34B 的模型本文会给出性能参数，但发布要晚一些**（还在做安全测试）。
2. LLaMA2-Chat：LLaMA2 的微调版本，针对**对话场景**进行了优化。

   * 同样发布 7B/13B/70B 参数的版本。

我们相信，在安全的前提下，LLM 的开放将对社会产生积极影响。但注意，和所有 LLM 一样，LLaMA2 是一项新技术，
在使用中存在潜在风险（Bender 等，2021b；Weidinger 等，2021；Solaiman 等，2023），

* 目前的测试**仅涵盖了英语**。
  在部署任何 LLaMA2-Chat 应用之前，开发者应针对其特定场景进行安全测试和调优；
* 我们提供了一份负责任使用指南和代码示例，以促进 LLaMA2 和 LLaMA2-Chat 的安全部署。更多信息见 5.3 节。

一些资料链接：

1. [ai.meta.com/resources/models-and-libraries/llama/](https://ai.meta.com/resources/models-and-libraries/llama/)
2. [ai.meta.com/llama](https://ai.meta.com/llama)
3. [github.com/facebookresearch/llama](https://github.com/facebookresearch/llama)

## 1.3 LLaMA2 是如何炼成的：训练+微调鸟瞰

![](/assets/img/llama2-paper/fig-4.png)

图 4：LLaMA2-Chat 训练和调优过程。

炼丹四步：

1. 使用公开数据**预训练**（自监督学习），得到 **`LLaMA2`**；
2. 对 LLaMA2 进行**监督微调**（SFT），得到一个初始版本的 **`LLaMA2-Chat`**；
3. **人**对 LLaMA2-Chat 回答进行**反馈和标注**，得到两个**奖励模型**（分别针对有用性和安全性）；
4. 通过 **基于人类反馈的强化学习**（RLHF）/ rejection sampling / PPO，对 LLaMA2-Chat 进行（多次）迭代。

## 1.4 本文组织

本文其余部分组织如下：

* 第 2 节：预训练方法
* 第 3 节：微调方法
* 第 4 节：模型安全方法
* 第 5 节：核心观察和见解
* 第 6 节：相关工作
* 第 7 节：总结

# 2 预训练（Pretraining）

为了打造 LLaMA2 这个新系列模型，我们采用了 Touvron 等（2023）的预训练方法，
使用了一个**优化的自回归 transformer**，并进行了一些**改进**以提高性能，
包括，

* 更健壮的**数据清洗**；
* 更新的**训练数据比例**；
* 更多的**训练 tokens**；
* 更长的**上下文**；
* 使用 **grouped-query attention**（GQA），通过组查询来提高**推理性能**。

  > **GQA 优化推理的基本原理**：[大模型推理的极限：理论分析、数学建模与 CPU/GPU 实测（2024）](/blog/llm-inference-speed-zh/)。译注。

表 1 比较了 LLaMA 2 与 LLaMA 1 的一些属性：

|  | LLaMA | LLaMA 2 |
| --- | --- | --- |
| 训练数据 | 见 [LLaMA 论文](/blog/llama-paper-zh/) | 基于公开可用数据新组合的数据集 |
| 参数数量 | 7b / 13b / **`33b / 65b`** | 7b / 13b / **`34b / 70b`** |
| 上下文长度 | **`2k / 2k / 2k / 2k`** | **`4k / 4k / 4k / 4k`** |
| GQA | NO/NO/NO/NO | NO/NO/**`YES/YES`** |
| 训练 tokens 数量 | **`1T / 1T / 1.4T / 1.4T`** | **`2T / 2T / 2T / 2T`** |
| Learning Rate | `3.0*10-4 / 3.0*10-4 / 1.5*10-4 / 1.5*10-4` | `3.0*10-4 / 3.0*10-4 / 3.0*10-4 / 3.0*10-4` |

表 1：LLaMA 1 和 2 模型对比。Token 数量只计算了预训练数据。所有模型都是用
global batch-size of 4M tokens 训练的。

## 2.1 预训练数据（Pretraining Data）

* 组合了一些公开可用的数据源，其中不包含来 Meta 产品或服务的数据。
* 某些网站包含了很多个人信息，我们努力删掉了其中的此类信息。
* 训练了 2T（2 万亿）个 token，这在性能和成本之间提供了不错的折中（performance–cost trade-off），
* 对大部分事实类数据源进行 up-sampling，以增加知识减少幻觉（ increase knowledge and dampen hallucinations）。

我们进行了大量预训练数据研究，这样用户可以更好地了解 LLaMA2 的潜在能力和限制；详细结果见 4.1 节。

## 2.2 训练细节（Training Details）

我们**采用了 Llama 1 的大部分预训练设置和模型架构**。

* 使用标准的 transformer 架构（Vaswani 等，2017），
* 使用 RMSNorm 进行预归一化（Zhang 和 Sennrich，2019），
* 使用 SwiGLU 激活函数（Shazeer，2020），以及旋转位置嵌入（rotary positional embeddings，RoPE，Su 等，2022）。

与 Llama 1 相比，**主要的架构差异**包括

1. **上下文长度**（翻倍，`2k -> 4k`）
2. **组查询注意力**（GQA, grouped-query attention）

附录 A.2.1 中详细介绍了这些差异，并进行了 ablation experiments 以证明它们的重要性。

### 2.2.1 超参数（Hyperparameters）

* 使用 AdamW 优化器进行训练（Loshchilov 和 Hutter，2017），其中 β1 = 0.9，β2 = 0.95，eps = 10-5。
* 使用余弦学习率调度（a cosine learning rate schedule），...