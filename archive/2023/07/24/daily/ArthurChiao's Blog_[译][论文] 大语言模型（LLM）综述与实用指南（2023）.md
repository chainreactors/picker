---
title: [译][论文] 大语言模型（LLM）综述与实用指南（2023）
url: https://arthurchiao.github.io/blog/llm-practical-guide-zh/
source: ArthurChiao's Blog
date: 2023-07-24
fetch_date: 2025-10-04T11:51:48.437154
---

# [译][论文] 大语言模型（LLM）综述与实用指南（2023）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] 大语言模型（LLM）综述与实用指南（Amazon，2023）

Published at 2023-07-23 | Last Update 2024-03-10

### 译者序

本文来自 2023 年一篇大模型论文：
[Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond](https://arxiv.org/abs/2304.13712)，
翻译了其中感兴趣的部分。

论文信息：

```
@article{yang2023harnessing,
	title={Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond},
	author={Jingfeng Yang and Hongye Jin and Ruixiang Tang and Xiaotian Han and Qizhang Feng and Haoming Jiang and Bing Yin and Xia Hu},
	year={2023},
	eprint={2304.13712},
	archivePrefix={arXiv},
	primaryClass={cs.CL}
}
```

![](/assets/img/llm-practical-guide/fig-1.png)

一些工程信息：

1. 训练

   1. 训练费用：**`GPT-3 175B`** 单次训练 **460 万美元** [3]。
   2. 能耗：训练 PaLM 两个月左右耗费约了 3.4 Gwh [6]。
   3. 数据集大小：**`GPT-3 175B`** 训练了 **4990 亿个 token** [16]。
   4. OpenAI 训练集群：285k CPU, 10k high-end GPU。
2. 推理

   1. 推理时间

      * 最大 token 分别为 2、8 和 32 时，GPT-J 6B 模型的推理时间分别为 0.077s、0.203s 和 0.707s。
      * 最大 token 固定为 32 时，InstructGPT 模型（davinci v2）的推理时间为 **`1.969s`**。
   2. API 延迟：OpenAI API 的平均延迟时间从几百毫秒到几秒不等。
   3. InstructGPT davinci v2（175B）的理想**去噪推理时间**
      **`0.21s/request`**。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 本文目的](#11-本文目的)
  + [1.2 通用大模型和微调模型的定义](#12-通用大模型和微调模型的定义)
  + [1.3 本文组织](#13-本文组织)
* [2 模型：实用指南](#2-模型实用指南)
  + [2.1 BERT 风格语言模型：encoder-decoder 或 encoder-only](#21-bert-风格语言模型encoder-decoder-或-encoder-only)
    - [2.1.1 BERT paper](#211-bert-paper)
    - [2.1.2 典型模型](#212-典型模型)
  + [2.2 GPT 风格语言模型：decoder-only](#22-gpt-风格语言模型decoder-only)
* [3 数据：实用指南](#3-数据实用指南)
  + [3.1 预训练数据（Pretraining data）](#31-预训练数据pretraining-data)
  + [3.2 微调数据（Finetuning data）](#32-微调数据finetuning-data)
    - [3.2.1 无标注数据：通用大模型 + zero-shot 配置](#321-无标注数据通用大模型--zero-shot-配置)
    - [3.2.2 少量标注数据：通用大模型 + few-shot in-context learning](#322-少量标注数据通用大模型--few-shot-in-context-learning)
    - [3.2.3 丰富的标注数据：通用大模型/微调模型](#323-丰富的标注数据通用大模型微调模型)
    - [3.2.4 小结：通用模型 vs. 微调模型的选型](#324-小结通用模型-vs-微调模型的选型)
  + [3.3 测试数据/用户数据（Test data / user data）](#33-测试数据用户数据test-data--user-data)
* [4 NLP 任务：实用指南](#4-nlp-任务实用指南)
  + [4.1 传统 NLU 任务](#41-传统-nlu-任务)
    - [4.1.1 No use case.](#411-no-use-case)
    - [4.1.2 Use case. However, there are still some NLU tasks suitable for LLMs.](#412-use-case-however-there-are-still-some-nlu-tasks-suitable-for-llms)
  + [4.2 生成任务（Generation tasks）](#42-生成任务generation-tasks)
    - [4.2.1 Use case.](#421-use-case)
    - [4.2.2 No use case.](#422-no-use-case)
  + [4.3 Knowledge-intensive tasks](#43-knowledge-intensive-tasks)
    - [4.3.1 Use case.](#431-use-case)
    - [4.3.2 No use case.](#432-no-use-case)
  + [4.4 Abilities Regarding Scaling](#44-abilities-regarding-scaling)
    - [4.4.1 Use Case with Reasoning.](#441-use-case-with-reasoning)
    - [4.4.2 Use Cases with Emergent Abilities.](#442-use-cases-with-emergent-abilities)
    - [4.4.3 No-Use Cases and Understanding.](#443-no-use-cases-and-understanding)
  + [4.5 Miscellaneous tasks](#45-miscellaneous-tasks)
    - [4.5.1 No use case](#451-no-use-case)
    - [4.5.2 Use case.](#452-use-case)
  + [4.6 Real world “tasks”](#46-real-world-tasks)
* [5 其他方面](#5-其他方面)
  + [5.1 效率](#51-效率)
    - [5.1.1 成本](#511-成本)
    - [5.1.2 延迟](#512-延迟)
    - [5.1.3 部分参数调优（Parameter-Efficient Tuning）：降低计算和存储成本](#513-部分参数调优parameter-efficient-tuning降低计算和存储成本)
  + [5.2 Trustworthiness](#52-trustworthiness)
  + [5.3 Safety challenges](#53-safety-challenges)
* [6 总结及未来挑战](#6-总结及未来挑战)
* [参考文献](#参考文献)

---

# 摘要

本文是一份**大语言模型（LLMs）实用指南**，
目的是帮助从业者和用户更好地完成他们的下游**自然语言处理（NLP）**任务 ——
NLP 是 LLM 的典型下游使用场景。本文将从模型、数据和下游任务的角度讨论和分析 LLM 的选型和使用，

* 首先简要介绍 **GPT 风格和 BERT 风格**的大语言模型；
* 然后讨论**预训练**数据、**训练**数据和**测试**数据对模型选型的影响；
* 然后详细讨论大语言模型**适合和不适合**哪些自然语言处理任务（use and non-use cases）。

此外，我们还探讨了大模型的 spurious biases，以及工程角度的**效率、成本和延迟**等重要因素，
以便从业者对实际部署大模型有一个全面了解。

本文旨在为研究人员和从业者提供一些最新的技术见解和最佳实践，让大模型能更成功地应用于各种 NLP 任务中。
我们维护了一个资源列表页并定期更新，见 [**`github.com/Mooler0410/LLMsPracticalGuide`**](https://github.com/Mooler0410/LLMsPracticalGuide)。

# 1 引言

近年来，大语言模型的快速发展对自然语言处理领域产生了革命性的影响 [12, 128, 131]。
这些强大的模型在各种 NLP 任务 —— 从**自然语言理解**（NLU）到**生成式任务**（generation tasks）——
中都展现出了巨大的潜力，甚至为**通用人工智能**（AGI）铺平了道路。
但另一方面，**如何有效和高效地利用这些模型**，就需要了解它们的实际能力和局限性，
还需要考虑具体 NLP 任务及其涉及的数据。

## 1.1 本文目的

作为一份给大模型从业者和用户的指南，本文主要关注**下游 NLP 任务中如何使用 LLM**。例如，

* 为什么选择或不选择某些 LLM；
* 如何根据模型大小、计算要求和特定领域预训练模型的可用性等等因素，选择最合适的 LLM。

本文总结了以下 LLM 实用指南：

* **自然语言理解**：在数据分布不均或训练数据极少场景下，LLM 卓越的泛化能力（generalization ability）；
* **自然语言生成**：利用 LLM 的能力，为各种应用程序创建连贯、上下文相关的高质量文本；
* **知识密集型任务**：利用 LLM 中存储的大量知识，解决一些需要特定领域专业知识或世界常识（general world knowledge）的任务；
* **推理能力**：了解和利用 LLM 的推理能力，提升基于上下文的决策能力和解决问题能力。

## 1.2 通用大模型和微调模型的定义

为了评估**（通用）大语言模型**的能力，我们将把它们**与微调模型（fine-tuned models）进行比较**。
目前，LLM 和微调模型都还没有一个普遍认可的定义。考虑到实际效用，本文将使用如下定义：

* 大语言模型（LLM）：在大量数据集上预训练的大型语言模型，没有针对特定任务的数据进行调优；
* 微调模型（fine-tuned models）：通常较小，也是预训练，然后在较小的、特定任务的数据集上进一步调优，以优化其在该场景下的性能。

> From a practical standpoint, we consider models with less than 20B parameters
> to be fine-tuned models. While it’s possible to fine-tune even larger models
> like PlaM (540B), in reality, it can be quite challenging, particularly for
> academic research labs and small teams. Fine-tuning a model with 3B
> parameters can still be a daunting task for many individuals or
> organizations.

## 1.3 本文组织

本文接下来的内容组织如下：

* **讨论当前最重要的两种模型**（GPT 风格和 BERT 风格），让读者对 LLM 有一个简要理解；
* 深入研究**影响模型性能的关键因素**，包括预训练数据、训练/调优数据和测试数据；
* 深入探讨**各种具体的 NLP 任务**，包括知识密集型任务、传统 NLU 任务和生成任务；分析这些实际场景中的挑战等。

# 2 模型：实用指南

本节简要介绍当前业界最先进的 LLM。
这些模型在训练策略、模型架构和使用场景上有所不同。为了更清晰地理解 LLM 的发展，
本文将它们分为两种类型：

1. **encoder-decoder or encoder-only**
2. **decoder-only**

图 1 展示了语言模型的演进历程，

![](/assets/img/llm-practical-guide/fig-1.png)

图 1：Fig. 1. The evolutionary tree of modern LLMs traces the development of language models in recent years and highlights some of the
most well-known models. Models on the same branch have closer relationships. Transformer-based models are shown in non-grey
colors: decoder-only models in the blue branch, encoder-only models in the pink branch, and encoder-decoder models in the green
branch. The vertical position of the models on the timeline represents their release dates. Open-source models are represented by
solid squares, while closed-source models are represented by hollow ones. The stacked bar plot in the bottom right corner shows the
number of models from various companies and institutions.

几点说明：

1. **decoder-only 模型逐渐成为 LLM 的主要发展趋势**。

   * LLM 早期阶段，encoder-only 和 encoder-decoder 模型更受欢迎；
   * 随着 2021 年 GPT-3 的横空出世，decoder-only 模型完成了一次漂亮的翻身仗；
   * 在 BERT 带来的最初爆炸性增长之后，encoder-only 模型逐渐开始失宠；
2. **OpenAI 在 LLM 领域始终保持领先地位**。其他公司和机构正在努力追赶。
   这种领导地位可能归因于 OpenAI 对其技术路线的坚守，即使最初大家并不看好这条路线；
3. **Meta 对开源 LLM 做出了重大贡献**，并促进了 LLM 的研究。
   在考虑对开源社区尤其是 LLM 相关的贡献时，Meta 是最慷慨的商业公司之一，Meta 开发的所有 LLM 都是开源的；
4. **LLM 表现出闭源的趋势**。

   * LLM 早期阶段（2020 年之前），大多数模型都是开源的；
   * 随着 GPT-3 的推出，公司越来越倾向于闭源他们的模型，如 PaLM、LaMDA 和 GPT-4:
   * 因此，学术研究人员进行 LLM 训练实验变得更加困难，基于 API 的研究可能成为学术界的主要方法；
5. **encoder-decoder 模型仍然还有前途**。

   * 业界仍然在这个方向积极探索，且大部分都是开源的；
   * Google 对开源 encoder-decoder 架构做出了重大贡献，虽然 decoder-only
     模型的灵活性和多功能性使得 Google 对这个方向的坚持似乎前途有些暗淡。

表 1 中简要总结了每种类型的特点和代表性 LLM。

表 1：当前各种大语言模型（LLM）总结

|  | Encoder-Decoder or Encoder-only (**`BERT-style`**) | Decoder-only (**`GPT-style`**) |
| --- | --- | --- |
| 训练 | **Masked** Language Models（遮盖某些单词） | **Autoregressive** Language Models（自回归） |
| 模型类型 | **判别式**（Discriminative） | **生成式**（Generative） |
| 预训练任务 | 预测**遮掩掉的**单词（完形填空） | 预测**下一个**单词 |
| 大语言模型 | ELMo [80], **BERT** [28], RoBERTa [65], DistilBERT [90], BioBERT [57], XLM [54], Xlnet [119], ALBERT [55], ELECTRA [24], **T5** [84], **GLM** [123], XLM-E [20], ST-MoE [133], AlexaTM [95] | **`GPT 3/4`** [16,76], OPT [126]. PaLM [22], BLOOM [92], MT-NLG [93], GLaM [32],Gopher [83], chinchil...