---
title: [译] DeepSeek-R1：通过强化学习激励大模型的推理能力（DeepSeek，2024）
url: https://arthurchiao.github.io/blog/deepseek-r1-paper-zh/
source: ArthurChiao's Blog
date: 2025-02-16
fetch_date: 2025-10-06T20:32:41.820379
---

# [译] DeepSeek-R1：通过强化学习激励大模型的推理能力（DeepSeek，2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译][论文] DeepSeek-R1：通过强化学习激励大模型的推理能力（DeepSeek，2024）

Published at 2025-02-15 | Last Update 2025-03-09

### 译者序

本文翻译自 2024 年 DeepSeek AI 的 paper [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)。
介绍了 DeepSeek 第一代**推理模型（reasoning models）**
（所以缩写为 R1）的设计和训练过程：

![](/assets/img/deepseek-r1-paper/training-pipelines.png)

Fig. How `DeepSeek-R1`-series models were trained.

要理解 DeepSeek-R1 的创新之处，可以先阅读 [如何训练一个企业级 GPT 助手（OpenAI，2023）](/blog/how-to-train-a-gpt-assistant-zh/)，
里面介绍了典型的大模型训练 pipeline，其中包括**预训练、SFT、RM、RL**等步骤。

![](/assets/img/how-to-train-a-gpt-assistant/training-pipeline.png)

OpenAI：训练一个 GPT 助手的流程

* **`DeepSeek-R1-Zero`** 的创新之处在于完全**跳过了 SFT 步骤**，
  直接在基座模型上进行大规模 `RM+`**`RL`** 训练，性能达到了 **`OpenAI-o1-0912`** 的水平。
  + [LLaMA 2：开放基础和微调聊天模型（Meta/Facebook，2023）](/blog/llama2-paper-zh/)
    对基于人类反馈的强化学习（HFRL）有较详细的介绍，DeepSeek 这里用的 RL 没有 HF，离 AGI 更进了一步。
  + 更详细的 HFRL 可介绍可以参考 [InstructGPT：基于人类反馈训练语言模型遵从指令的能力（OpenAI，2022）](/blog/instructgpt-paper-zh/)，

  ![](/assets/img/instructgpt-paper/fig-2.png)

  InstructGPT 三部曲：(1) SFT, (2)
  RM training, (3) RLHF via proximal policy optimization (PPO) on RM.
  蓝色箭头表示相应的数据用于训练模型。Step 2 中 A-D 是模型输出的采样，然后标注员对它们进行排序。
* 为了解决 DeepSeek-R1-Zero 存在的一些问题（可读性差，语言混用），又引入了少量的 SFT 数据作为冷启动，
  再参考 R1-Zero 的过程，训练了 **`DeepSeek-R1`**，
  在推理任务上的表现与 **`OpenAI-o1-1217`** 不相上下。
* 将 DeepSeek-R1 的推理能力蒸馏到 Qwen/LLaMA 等小型 dense 模型上，性能也很好。

总结下和 OpenAI 的性能对标：

| DeepSeek Models | OpenAI Models |
| --- | --- |
| DeepSeek-R1-Zero | OpenAI-o1-0912 |
| DeepSeek-R1 | OpenAI-o1-1217 |
| DeepSeek-R1 Distilled Models | OpenAI-o1-mini |

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 引言](#1-引言)
  + [1.0 Post-Training：完整 training pipeline 的重要组成部分](#10-post-training完整-training-pipeline-的重要组成部分)
    - [1.0.1 作用](#101-作用)
    - [1.0.2 提高推理能力：与 OpenAI-o1 的思路区别](#102-提高推理能力与-openai-o1-的思路区别)
  + [1.1 贡献](#11-贡献)
    - [1.1.1 post-training：在基础模型上进行大规模强化学习](#111-post-training在基础模型上进行大规模强化学习)
    - [1.1.2 蒸馏：小型模型也可以很强大](#112-蒸馏小型模型也可以很强大)
  + [1.2 性能评估结果](#12-性能评估结果)
    - [1.2.1 推理任务](#121-推理任务)
    - [1.2.2 知识](#122-知识)
    - [1.2.3 其他](#123-其他)
* [2 方法](#2-方法)
  + [2.1 概述](#21-概述)
  + [2.2 DeepSeek-R1-Zero：在基础模型（base model）上进行强化学习](#22-deepseek-r1-zero在基础模型base-model上进行强化学习)
    - [2.2.1 强化学习算法：Group Relative Policy Optimization (**`GRPO`**)](#221-强化学习算法group-relative-policy-optimization-grpo)
    - [2.2.2 奖励建模（Reward Modeling）：**`rule-based reward system`**](#222-奖励建模reward-modelingrule-based-reward-system)
      * [类型一：准确性奖励（Accuracy rewards）](#类型一准确性奖励accuracy-rewards)
      * [类型二：格式奖励（Format rewards）](#类型二格式奖励format-rewards)
    - [2.2.3 训练模板（提示词模板）](#223-训练模板提示词模板)
    - [2.2.4 DeepSeek-R1-Zero 的性能、自我进化过程和顿悟时刻](#224-deepseek-r1-zero-的性能自我进化过程和顿悟时刻)
      * [性能](#性能)
      * [自我进化过程](#自我进化过程)
      * [顿悟时刻](#顿悟时刻)
      * [缺点和解决方式](#缺点和解决方式)
  + [2.3 DeepSeek-R1：带冷启动的强化学习](#23-deepseek-r1带冷启动的强化学习)
    - [2.3.1 阶段一：冷启动](#231-阶段一冷启动)
      * [数据源](#数据源)
      * [冷启动数据的好处](#冷启动数据的好处)
    - [2.3.2 阶段二：面向 reasoning 的强化学习](#232-阶段二面向-reasoning-的强化学习)
    - [2.3.3 阶段三：拒绝采样和监督微调](#233-阶段三拒绝采样和监督微调)
      * [推理数据（Reasoning data）：600k](#推理数据reasoning-data600k)
      * [非推理数据（Non-Reasoning data）：200k](#非推理数据non-reasoning-data200k)
    - [2.3.4 阶段四：所有场景的强化学习](#234-阶段四所有场景的强化学习)
  + [2.4 蒸馏：赋予小型模型推理能力](#24-蒸馏赋予小型模型推理能力)
* [3 实验（略）](#3-实验略)
  + [3.1 DeepSeek-R1 评估](#31-deepseek-r1-评估)
  + [3.2 蒸馏模型评估](#32-蒸馏模型评估)
* [4 讨论](#4-讨论)
  + [4.1 蒸馏与强化学习的性能对比](#41-蒸馏与强化学习的性能对比)
  + [4.2 失败的尝试](#42-失败的尝试)
    - [4.2.1 Process Reward Model (PRM)](#421-process-reward-model-prm)
    - [4.2.2 Monte Carlo Tree Search (MCTS)](#422-monte-carlo-tree-search-mcts)
* [5 结论、局限性和未来工作](#5-结论局限性和未来工作)
* [参考文献](#参考文献)

---

# 摘要

本文介绍我们的第一代推理模型，**`DeepSeek-R1-Zero`** 和 **`DeepSeek-R1`**。

* DeepSeek-R1-Zero

  + 这是一个**跳过监督微调**（SFT）步骤，
    直接通过大规模**强化学习**（RL）训练得到的模型，具备卓越的推理能力。

    > 译注：下图来自 [如何训练一个企业级 GPT 助手（OpenAI，2023）](/blog/how-to-train-a-gpt-assistant-zh/)，
    > 展示了 OpenAI 从预训练开始逐步训练出一个 GPT 助手的步骤，
    > **`pre-training -> SFT -> RM -> RL`** 也是典型的大模型训练过程。
    > R1-Zero 是在 DeepSeek-V3 基座大模型上直接进行 RM+RL，跳过中间的 SFT，
    >
    > ![](/assets/img/how-to-train-a-gpt-assistant/training-pipeline.png)
    >
    > OpenAI：训练一个 GPT 助手的流程
  + 通过大规模 RL，DeepSeek-R1-Zero 自然地涌现出许多强大且有趣的推理行为。不过，它也存在可读性差、混用语言等问题。
* DeepSeek-R1

  + 为了解决以上提到的 R1-Zero 存在的问题，并进一步提升推理性能，
    在 RL 阶段之前引入了多阶段训练和冷启动数据，训练得到的模型称为 DeepSeek-R1。
  + DeepSeek-R1 在推理任务上的表现与 **`OpenAI-o1-1217`** 不相上下。

    ![](/assets/img/deepseek-r1-paper/1.png)

    Figure 1 | Benchmark performance of DeepSeek-R1.

为了支持研究社区，我们此次开源了 [8 个推理模型](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d)：

1. DeepSeek-R1
2. DeepSeek-R1-Zero
3. DeepSeek-R1-**`Distill-Llama-70B`**
4. DeepSeek-R1-**`Distill-Qwen-32B`**
5. DeepSeek-R1-**`Distill-Qwen-14B`**
6. DeepSeek-R1-**`Distill-Llama-8B`**
7. DeepSeek-R1-**`Distill-Qwen-7B`**
8. DeepSeek-R1-**`Distill-Qwen-1.5B`**

其中，**后面 6 个是以 Qwen/Llama 作为基座模型**，利用 DeepSeek-R1
**蒸馏出来的 dense 模型**。

# 1 引言

近年来，大模型的迭代与演进速度非常快（OpenAI, 2024a；Anthropic, 2024；Google, 2024）。

## 1.0 Post-Training：完整 training pipeline 的重要组成部分

现在，**`post-training`** 已成为完整 training pipeline 的一个重要组成部分。

### 1.0.1 作用

Post-Training 的好处：

1. **提高推理任务的准确性**，
2. 与人类社会价值观对齐，
3. 能适应用户偏好，
4. 相对于预训练，所需的计算资源极少。

### 1.0.2 提高推理能力：与 OpenAI-o1 的思路区别

具体到提高推理能力方面，

* OpenAI 的 o1（OpenAI, 2024b）系列模型首次通过**增加推理过程中的思维链长度**（Chain-of-Thought, CoT）
  来引入 **`inference-time scaling`**。
  这种方法在数学、编码和科学推理等推理任务上取得了显著的效果。
* 但是，有效的 **`test-time scaling`** 仍然是社区的一个开放性问题。
  此前，业界已经探索了很多方法，包括
  process-based reward models (Uesato et al., 2022; Lightman et al., 2023; Wang
  et al., 2023), reinforcement learning (Kumar et al., 2024), and search
  algorithms such as Monte Carlo Tree Search and Beam Search (Feng et al., 2024;
  Xin et al., 2024; Trinh et al., 2024)，但这些方法**都没有达到与 OpenAI o1 相当的通用推理性能**。

本文迈出了**通过纯强化学习（pure RL）提高模型推理能力**的第一步。

* 我们的目标是探索**大模型在没有任何监督数据的情况下 —— 单纯通过 RL 过程自我进化 —— 发展出推理能力的潜力**。
* 具体来说，我们使用 **`DeepSeek-V3-Base`** 作为基础模型，采用 GRPO（Shao 等，2024）作为 RL 框架，来**提高模型在推理方面的表现**。
* 在训练过程中，DeepSeek-R1-Zero 自然地涌现出许多强大且有趣的推理行为。经过几千步的 RL 训练后，
  DeepSeek-R1-Zero 在推理基准测试中表现出色。例如，AIME 2024 的 pass@1 得分从 15.6% 提高到 71.0%，加上多数投票，得分进一步提高到 86.7%，与 OpenAI-o1-0912 表现相当。

然而，DeepSeek-R1-Zero 面临着诸如可读性差、语言混用等挑战。为了解决这些问题并进一步提升推理性能，
我们引入了少量的冷启动数据和一个 multi-stage training pipeline，训练得到 DeepSeek-R1，
其性能与 OpenAI-o1-1217 相当。

最后，我们还进一步探索了从 DeepSeek-R1 蒸馏较小的 dense models。
例如，使用 Qwen2.5-32B（Qwen, 2024b）作为基础模型，两种思路：

1. 直接在 Qwen-32B 上进行强化学习（RL），得到一个推理模型；
2. 从 DeepSeek-R1 进行蒸馏（把 DeepSeek-R1 的知识“传授”给 Qwen2.5-32B），得到一个推理模型；

我们发现后者（蒸馏）的性能优于前者（直接 RL）。
这表明**尺寸更大的基础模型发现的推理模式**对于提高推理能力至关重要。

我们开源了基于 Qwen/Llama（Dubey 等，2024）的蒸馏模型。
值得注意的是，我们蒸馏出的 14B 模型在 AIME 2024 上的表现大幅超过了现有的开源模型 QwQ-32B-Preview（Qwen, 2024a），
而蒸馏出的 32B 和 70B 模型在针对 dense models 的推理基准测试中创下了新纪录。

## 1.1 贡献

### 1.1.1 post-training：在基础模型上进行大规模强化学习

我们跳过监督微调（SFT）步骤，直接在基础模型（base model）上应用 RL。
这会使模型去**探索解决复杂问题时的思维链**（CoT），用这种方式训练得到的就是 DeepSeek-R1-Zero。

* DeepSeek-R1-Zero 展现出**自我验证、反思和生成长 CoT** 等能力，为社区研究树立了一个重要的里程碑。
* 值得注意的是，这是首个证实**大模型的推理能力可以通过纯 RL 激励实现（无需 SFT）**的公开研究，这一突破为该领域的未来发展铺平了道路。

此外，我们还介绍了开发 DeepSeek-R1 的 pipeline。

![](/assets/img/deepseek-r1-paper/training-pipelines.png)

Fig. How DeepSeek-R1-Zero and DeepSeek-R1 were trained (based on the same base model).

该 pipeline 包含，

1. **两个 RL stage**
   * 一个用于发现更强的推理模式（stage 2）
   * 一个用于与人类偏好对齐（stage 4）
2. **两个 SFT stage**：用于激发出模型的 reasoning and non-reasoning 能力。

### 1.1.2 蒸馏：小型模型也可以很强大

我们证明了**大型模型的推理模式可以被蒸馏到小型模型中**，

* 与在小型模型上进行 RL 发现的推理模式相比，蒸馏可以取得更好的性能。
* 开源的 DeepSeek-R1 及其 API 将有助于社区在未来蒸馏出更好的小模型。

**利用 DeepSeek-R1 生成的推理数据**，我们微调了几个在社区中广泛使用的小型 dense 模型。
结果显示，这些经过蒸馏的小型 dense model 在基准测试中表现非常好。

* D...