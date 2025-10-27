---
title: [译][论文] InstructGPT：基于人类反馈训练语言模型遵从指令的能力（OpenAI，2022）
url: https://arthurchiao.github.io/blog/instructgpt-paper-zh/
source: ArthurChiao's Blog
date: 2024-03-25
fetch_date: 2025-10-04T12:08:31.572435
---

# [译][论文] InstructGPT：基于人类反馈训练语言模型遵从指令的能力（OpenAI，2022）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] InstructGPT：基于人类反馈训练语言模型遵从指令的能力（OpenAI，2022）

Published at 2024-03-24 | Last Update 2024-03-24

### 译者序

本文翻译自 2022 年 OpenAI 的论文：
[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)，
整理翻译了其中感兴趣的部分。

![](/assets/img/llm-practical-guide/fig-1.png)

大模型进化树，可以看到 InstructGPT 所处的年代和位置。来自 [大语言模型（LLM）综述与实用指南（Amazon，2023）](/blog/llm-practical-guide-zh/)。

**`GPT -> InstructGPT -> ChatGPT`** 的过程，可参考
[如何训练一个企业级 GPT 助手（OpenAI，2023）](/blog/how-to-train-a-gpt-assistant-zh/)。

**译者水平有限，不免存在遗漏或错误之处。如有疑问，敬请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.1 大模型存在的问题](#11-大模型存在的问题)
  + [1.2 语言模型建模偏差：预测下一个 token `vs.` 有益且安全地遵循用户指令](#12-语言模型建模偏差预测下一个-token-vs-有益且安全地遵循用户指令)
  + [1.3 常规解决方式及评估标准](#13-常规解决方式及评估标准)
  + [1.4 本文方法：基于人类反馈+微调来对齐](#14-本文方法基于人类反馈微调来对齐)
  + [1.5 模型尺寸及架构](#15-模型尺寸及架构)
  + [1.6 主要发现](#16-主要发现)
    - [1.6.1 标注员明显更喜欢 InstructGPT 而非 GPT-3 的输出](#161-标注员明显更喜欢-instructgpt-而非-gpt-3-的输出)
    - [1.6.2 InstructGPT 相比 GPT-3 在真实性方面有所改进](#162-instructgpt-相比-gpt-3-在真实性方面有所改进)
    - [1.6.3 InstructGPT 相比 GPT-3 毒性略微下降，但偏见未下降](#163-instructgpt-相比-gpt-3-毒性略微下降但偏见未下降)
    - [1.6.4 通过修改 RLHF 微调过程，可以最小化在公开 NLP 数据集上的性能退化](#164-通过修改-rlhf-微调过程可以最小化在公开-nlp-数据集上的性能退化)
    - [1.6.5 `在公开 NLP 数据集上微调`不如`在人类偏好数据上微调`的效果好](#165-在公开-nlp-数据集上微调不如在人类偏好数据上微调的效果好)
    - [1.6.6 InstructGPT 对 RLHF 微调之外的指令有良好的泛化能力](#166-instructgpt-对-rlhf-微调之外的指令有良好的泛化能力)
* [2 相关工作](#2-相关工作)
  + [2.1 对齐（alignment）与人类反馈学习（learning from human feedback）研究](#21-对齐alignment与人类反馈学习learning-from-human-feedback研究)
    - [2.1.1 RLHF：来自游戏领域](#211-rlhf来自游戏领域)
    - [2.1.2 InstructGPT：基于 RLHF 在更广泛的语言任务上对齐 LLM](#212-instructgpt基于-rlhf-在更广泛的语言任务上对齐-llm)
    - [2.1.3 语言模型对齐意味着什么](#213-语言模型对齐意味着什么)
  + [2.2 训练模型遵循指令（follow instructions）](#22-训练模型遵循指令follow-instructions)
  + [2.3 评估语言模型的危害](#23-评估语言模型的危害)
  + [2.4 修改模型行为，降低危害](#24-修改模型行为降低危害)
* [3 方法论与实验详情](#3-方法论与实验详情)
  + [3.1 High-level 方法论](#31-high-level-方法论)
    - [3.1.1 准备工作](#311-准备工作)
    - [3.1.2 InstructGPT 训练三部曲](#312-instructgpt-训练三部曲)
  + [3.2 数据集](#32-数据集)
    - [3.2.1 主要来自 OpenAI API 用户数据](#321-主要来自-openai-api-用户数据)
    - [3.2.2 去重](#322-去重)
    - [3.2.3 冷启动（第一版 InstructGPT）](#323-冷启动第一版-instructgpt)
    - [3.2.3 三种 prompt：plain/few-shot/user-based](#323-三种-promptplainfew-shotuser-based)
    - [3.2.4 三个 prompts 数据集及大小](#324-三个-prompts-数据集及大小)
    - [3.2.5 Prompts 类别分布及占比](#325-prompts-类别分布及占比)
    - [3.2.6 几个 prompt 例子](#326-几个-prompt-例子)
  + [3.3 训练任务](#33-训练任务)
  + [3.4 人工数据收集](#34-人工数据收集)
    - [3.4.1 标注员筛选](#341-标注员筛选)
    - [3.4.2 对齐冲突的处理](#342-对齐冲突的处理)
    - [3.4.3 对照度标注员：验证泛化能力](#343-对照度标注员验证泛化能力)
  + [3.5 Models（模型）](#35-models模型)
    - [3.5.1 Supervised fine-tuning (SFT)](#351-supervised-fine-tuning-sft)
    - [3.5.2 Reward modeling (RM)](#352-reward-modeling-rm)
    - [3.5.3 Reinforcement learning (RL)](#353-reinforcement-learning-rl)
    - [3.5.4 性能比较基线](#354-性能比较基线)
  + [3.6 性能评估](#36-性能评估)
    - [3.6.1 指标](#361-指标)
      * [helpful](#helpful)
      * [honest / truthfulness](#honest--truthfulness)
      * [harmless](#harmless)
    - [3.6.2 定量评估](#362-定量评估)
      * [在 OpenAI API 真实用户的 prompts 上的表现](#在-openai-api-真实用户的-prompts-上的表现)
      * [在公开 NLP 数据集上的表现](#在公开-nlp-数据集上的表现)
* [4 结果](#4-结果)
* [5 问题讨论](#5-问题讨论)
* [参考文献](#参考文献)
* [附录 A: Prompt 数据详情](#附录-a-prompt-数据详情)
  + [A.1 Labeler-written prompts](#a1-labeler-written-prompts)
  + [A.2 API user prompts](#a2-api-user-prompts)
  + [A.2.1 从 InstructGPT API (Playground) 收集上来的 user prompts 示例](#a21-从-instructgpt-api-playground-收集上来的-user-prompts-示例)
  + [A.2.2 从 GPT-3 API 收集上来的 user prompts 示例](#a22-从-gpt-3-api-收集上来的-user-prompts-示例)
  + [A.3 数据集大小：`SFT 15k / RM 50k / PPO 47k`](#a3-数据集大小sft-15k--rm-50k--ppo-47k)
  + [A.4 数据多样性](#a4-数据多样性)
* [附录 B：Additional human data collection details](#附录-badditional-human-data-collection-details)
* [附录 C：一些模型细节](#附录-c一些模型细节)
  + [C.1 SFT 训练细节](#c1-sft-训练细节)
  + [C.2 RM 训练细节](#c2-rm-训练细节)
  + [C.3 RLHF 的初始化模型（initialization models）细节](#c3-rlhf-的初始化模型initialization-models细节)
  + [C.4 RLHF 训练细节](#c4-rlhf-训练细节)
  + [C.5 FLAN 和 T0 模型](#c5-flan-和-t0-模型)
* [附录 D：Automatic evaluation details](#附录-dautomatic-evaluation-details)
* [附录 E：Additional results](#附录-eadditional-results)
* [附录 F：Model samples](#附录-fmodel-samples)

---

# 摘要

**增大模型尺寸**未必就能提高它**对用户意图的理解能力**。
例如，一些大模型可能会生成不真实、有毒或对用户并无帮助（untruthful, toxic, or simply not helpful）的输出。
换句话说，这些模型与它们的用户**没有对齐**（not aligned）。

本文展示了一种**基于人类反馈进行微调**（fine-tuning with human feedback），
从而在各种任务上**将语言模型与用户意图对齐**的方法。简单来说，

* 先收集一组**“预期的模型行为应该是什么样”**的数据集，
  然后使用**监督学习来微调 GPT-3**（SFT），
* 接着，收集一组排名形式组织的**模型输出**（rankings of model outputs）作为数据集，
  使用**人类反馈强化学习**（RLHF）进一步微调上一步得到的模型。

我们将最终得到的这种模型称为 **`InstructGPT`**。

* **`175b GPT-3 vs. 1.3b InstructGPT`** 的**人工测评**显示，
  大家更喜欢后者，尽管它的参数不到前者的 **`1%`**。
* InstructGPT 在真实性（truthfulness）方面也有所改进，减少了有毒输出，
  在公开 NLP 数据集上的性能退化也很小。

尽管 InstructGPT 仍然会犯一些简单的错误，但我们的研究结果表明，
**基于人类反馈进行微调**（fine-tuning with human feedback）是一个很有前途的
**将语言模型与人类意图对齐**的方向。

# 1 引言

给定一些任务示例（examples of the task）作为输入，大语言模型（LLMs）可以被 “prompt” 去执行一系列自然语言处理（NLP）任务。

## 1.1 大模型存在的问题

然而，这些模型经常会出现一些意外的行为，比如编造事实、生成有偏见或有毒的文本，
或者忽视用户的指示（Bender 等，2021；Bommasani 等，2021；Kenton 等，2021；
Weidinger 等，2021；Tamkin 等，2021；Gehman 等，2020）。

## 1.2 语言模型建模偏差：预测下一个 token `vs.` 有益且安全地遵循用户指令

出现以上现象，
是因为许多近期的 LLM 建模目标都是（基于互联网数据训练）**预测下一个 token** ——
而并不是**“有益且安全地遵循用户的指令”**（Radford 等，2019；Brown 等，2020；Fedus 等，2021；Rae 等，2021；Thoppilan 等，2022）。
也就是说，**语言建模目标有偏差**（the language modeling objective is misaligned）。

由于 LLM 已经部署在大量实际应用中，因此解决大模型的这些非预期行为非常重要。

## 1.3 常规解决方式及评估标准

通过训练语言模型按照用户意图行事（Leike 等，2018）来推进语言模型的对齐。
这里的意图包括

1. 明确的意图，如遵循指示，
2. 隐含的意图，如保持真实、无偏见、无毒及无害性。

使用 Askell 等（2021）的术语，我们希望语言模型是

* 有帮助的（**`helpful`**，应该帮助用户解决任务），
* 诚实的（**`honest`**，不应该捏造信息或误导用户），
* 无害的（**`harmless`**，不应该对人或环境造成身体、心理或社会伤害）。

我们在第 3.6 节中详细阐述了这些标准的评估。

## 1.4 本文方法：基于人类反馈+微调来对齐

本文专注于**通过微调方法来对齐语言模型**。具体来说，
使用人类反馈强化学习（RLHF；Christiano 等，2017；Stiennon 等，2020）
来微调 GPT-3，以便它能遵循类型广泛的各种用户指令。具体过程如图 2 所示，

![](/assets/img/instructgpt-paper/fig-2.png)

Figure 2: InstructGPT 三部曲：(1) SFT, (2)
RM training, (3) RLHF via proximal policy optimization (PPO) on RM.
蓝色箭头表示相应的数据用于训练模型。Step 2 中 A-D 是模型输出的采样，然后标注员对它们进行排序。详见 Section 3。

三个步骤：

1. 收集示例数据（**`demonstration data`**），训练一个监督策略（**`supervised policy`**）。

   对于给定的输入，**标注员给出期望的行为** (详见 3.2 节)。然后，使用监督学习（supervised learning）对一个预训练的 GPT-3 模型进行微调。
2. 收集对比数据（**`comparison data`**），训练一个奖励模型（**`RM`**）。

   对给定输入，收集两个输出，标注员给出他们的偏好（which output they prefer）。然后，训练一个奖励模型来预测人类偏好输出（human-preferred output）。
3. 针对奖励模型，使用 PPO 对策略进行优化（optimize a policy）。

   将 RM 的输出作为一个标量奖励。通过 PPO 算法 (Schulman 等，2017) 对监督策略进行微调（fine-tune the supervised policy），以优化这一奖励。

步骤 2 和 3 可以持续迭代；在当前最佳策略上收集更多的对比数据，这些数据又用于训练新的 RM 和新的策略。
实际上，大部分对比数据来自于我们的 supervised policies，一小部分来自于我们的 PPO policies。

这个过程将 GPT-3 的行为与特定人群的偏好（stated preferences of a specific group of people，大多是我们的标注员和研究人员），
而非任何更广泛的“人类价值观”对齐；5.2 节将进一步讨论这个问题。

## 1.5 模型尺寸及架构

我们训练了三种尺寸的 InstructGPT 模型：

1. **`1.3B`**
2. **`6B`**
3. **`175B`**

所有模型都使用了 **`GPT-3`** 架构。

## 1.6 主要发现

我们的主要发现如下。

### 1.6.1 标注员明显更喜欢 InstructGPT 而非 GPT-3 的输出

我们将 **`175b GPT-3 vs. 1.3b InstructGPT`** 的输出进行了**人工测评**，
大家明显更喜欢后者，尽管它的参数不到前者的 **`1%`**。

这两类模型具有相同的架构，唯一的区别是 **InstructGPT 在人工数据上进行了微调**。

作为对比，我们给 GPT-3 添加了一个 few-shot prompt 以使其更好地遵循指令（变成了一个**提示词调优过的 GPT-3**），
但效果仍赶不上 InstructGPT：

* 175B InstructGPT 在 `85 ± 3%` 的结果中优于 `175B GPT-3`，
* 175B InstructGPT 在 `71 ± 4%` 的结果中优于 `few-shot 175B GPT-3`。

根据标注员的反馈，InstructGPT 模型的输出更符合 prompt ，并更可靠地遵循指令中的明确约束。

### 1.6.2 InstructGPT 相比 GPT-3 在真实性方面有所改进

在 TruthfulQA 基准测试中，InstructGPT 生成 truthful & informative 答案的概率比 GPT-3 高约一倍。

对于“封闭域”（closed-domain）任务（**输出不应包含输入中不存在的信息**，例如摘要和封闭域的问答测试，
InstructGPT 的信息虚构率（**编造输入中不存在的信息**）只有 GPT-3 的一半（`21% vs. 41%`）。

### 1.6.3 InstructGPT 相比 GPT-3 毒性略微下降，但偏见未下降

为了衡量毒性，我...