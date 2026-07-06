---
title: [译] 大模型训练的中场叙事：从 Reasoning Thinking 转向 Agentic Thinking (2026)
url: https://arthurchiao.art/blog/from-reasoning-thinking-to-agentic-thinking-zh/
source: ArthurChiao's Blog
date: 2026-07-05
fetch_date: 2026-07-06T06:17:55.423561
---

# [译] 大模型训练的中场叙事：从 Reasoning Thinking 转向 Agentic Thinking (2026)

# [ArthurChiao's Blog](https://arthurchiao.art/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)
* [RSS](/feed.xml)

TOC

# [译] 大模型训练的中场叙事：从 Reasoning Thinking 转向 Agentic Thinking (2026)

Published at 2026-07-05 | Last Update 2026-07-05

### 译者序

本文翻译自 2026 年 Junyang Lin 在 X 上的一篇文章
[From “Reasoning” Thinking to “Agentic” Thinking](https://x.com/JustinLin610/status/2037116325210829168)。

过去两年，有两件事情被重塑了：
我们**如何评估模型**（how we evaluate models），
以及**我们期望从模型得到什么**（what we expect from them）。

从 reasoning thinking 转向 agentic thinking 带来的深层次转变：

* 训练理念：为了想得更久而 thinking -> 为了**行动**而 thinking；
* 训练对象：模型本身 -> **模型+环境**（**`Agent+Harness`**）；
* 关注的多样性：数据多样性 -> **环境多样性**。

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [1 Reasoning thinking（推理式思考）](#1-reasoning-thinking推理式思考)
  + [1.1 OpenAI o1：thinking 作为新的一等能力，直接暴露给用户](#11-openai-o1thinking-作为新的一等能力直接暴露给用户)
  + [1.2 DeepSeek-R1：对 `thinking` 能力的复现和扩展](#12-deepseek-r1对-thinking-能力的复现和扩展)
  + [1.3 2025 年上半年：行业关注的仍然是推理式思考](#13-2025-年上半年行业关注的仍然是推理式思考)
* [2 Agentic thinking（智能体式思考）](#2-agentic-thinking智能体式思考)
  + [2.1 强化学习 scaling 的前提：确定、稳定且可扩展的反馈信号](#21-强化学习-scaling-的前提确定稳定且可扩展的反馈信号)
  + [2.2 强化学习不再是一个可选步骤，而是一个系统工程](#22-强化学习不再是一个可选步骤而是一个系统工程)
  + [2.3 重大转变：从大规模 pre-train 转向大规模 post-train (for reasoning)](#23-重大转变从大规模-pre-train-转向大规模-post-train-for-reasoning)
* [3 混合 thinking 的尝试](#3-混合-thinking-的尝试)
  + [3.1 Qwen 的尝试](#31-qwen-的尝试)
    - [3.1.1 困难：thinking 和 non-thinking 模式的数据分布和行为目标很不一样](#311-困难thinking-和-non-thinking-模式的数据分布和行为目标很不一样)
    - [3.1.2 用户行为画像的冲突](#312-用户行为画像的冲突)
    - [3.1.3 回到独立的 Instruct 和 Thinking 模型](#313-回到独立的-instruct-和-thinking-模型)
  + [3.2 其他厂商的融合模型](#32-其他厂商的融合模型)
    - [3.2.1 Claude / GLM / DeepSeek](#321-claude--glm--deepseek)
  + [3.3 背后的关键问题：强硬拼凑还是自然生长出来的](#33-背后的关键问题强硬拼凑还是自然生长出来的)
    - [3.3.1 生成更长的推理轨迹，并不会自动让模型更聪明](#331-生成更长的推理轨迹并不会自动让模型更聪明)
    - [3.3.2 thinking 应该由目标 workload 来决定](#332-thinking-应该由目标-workload-来决定)
* [4 从“训练模型”的时代，迈向“训练 Agent”的时代](#4-从训练模型的时代迈向训练-agent的时代)
  + [4.1 Agent 核心：与世界形成闭环交互](#41-agent-核心与世界形成闭环交互)
  + [4.2 Agentic thinking 与 Reasoning thinking 的区别](#42-agentic-thinking-与-reasoning-thinking-的区别)
* [5 为什么 Agentic RL 基础设施更难](#5-为什么-agentic-rl-基础设施更难)
  + [5.1 通过行动来推理（reasoning through action）的模型能力](#51-通过行动来推理reasoning-through-action的模型能力)
  + [5.2 目标转向：打榜 -> 解决交互式任务](#52-目标转向打榜---解决交互式任务)
  + [5.3 新的系统要求：训练与推理必须更加彻底地解耦](#53-新的系统要求训练与推理必须更加彻底地解耦)
  + [5.4 环境本身也开始成为一等研究对象](#54-环境本身也开始成为一等研究对象)
* [6 下一个行业前沿：更有用的思考](#6-下一个行业前沿更有用的思考)
  + [6.1 Agentic thinking 会成为未来主流的 thinking 形式](#61-agentic-thinking-会成为未来主流的-thinking-形式)
  + [6.2 Agentic Thinking 训练面临的新挑战](#62-agentic-thinking-训练面临的新挑战)
  + [6.3 Harness Engineering 变得极其重要](#63-harness-engineering-变得极其重要)
* [7 总结](#7-总结)
  + [7.1 推理的第一阶段：反馈信号 + 基础设施 + 语言模型 + 强化学习 -> 认知能力的质变](#71-推理的第一阶段反馈信号--基础设施--语言模型--强化学习---认知能力的质变)
  + [7.2 推理的第二阶段：训练模型 -> 训练”模型+环境”（Agent+Harness）](#72-推理的第二阶段训练模型---训练模型环境agentharness)
    - [7.2.1 改变一：哪些研究对象最重要](#721-改变一哪些研究对象最重要)
    - [7.2.2 改变二：Good thinking 的定义](#722-改变二good-thinking-的定义)
    - [7.2.3 改变三：竞争力的来源](#723-改变三竞争力的来源)

---

# 1 Reasoning thinking（推理式思考）

## 1.1 OpenAI o1：thinking 作为新的一等能力，直接暴露给用户

OpenAI 将 o1 描述为一种**通过强化学习训练出来、能够“先思考再回答”**的模型。

`o1` 证明了 **“thinking” 可以是一种一等能力**，一种可以**专门训练、并直接暴露给用户**的能力。

## 1.2 DeepSeek-R1：对 `thinking` 能力的复现和扩展

DeepSeek 把 R1 定位为一个可以与 o1 竞争的开源推理模型。

它也证明了 **reasoning-style 的后训练**可以被**复现和进一步强化**。

## 1.3 2025 年上半年：行业关注的仍然是推理式思考

以上阶段很重要。
事实上直到 2025 年上半年，行业关注的重点基本仍然是 **“reasoning thinking”**：

1. 如何让模型在 **inference 阶段使用更多算力**，
2. 如何用**更强的奖励**来训练它们，以及
3. 如何把这种额外的 **reasoning 能力暴露出来或加以控制**。

接下来会朝着什么方向演进？

# 2 Agentic thinking（智能体式思考）

我相信答案是“**agentic thinking**”：

1. 为了**执行行动**而思考
2. 在**与环境交互的过程中**思考，并且
3. **根据来自真实世界的反馈不断更新 plan**。

## 2.1 强化学习 scaling 的前提：确定、稳定且可扩展的反馈信号

第一波推理模型让我们明白，

* 如果想把**强化学习**在语言模型上 scale，
  就必须有 **确定、稳定且可扩展的反馈信号**。
* 数学、代码、逻辑以及其他**可验证的领域**之所以变得核心，正是因为这些场景下的奖励信号**远强于宽泛的偏好监督** (generic preference supervision)。
* 这些场景让强化学习优化的是**“正确性”** (correctness)，而不是“看起来像对的” (plausibility)。

## 2.2 强化学习不再是一个可选步骤，而是一个系统工程

一旦我们开始以“**能沿着更长的轨迹进行推理**”去训练一个模型，
强化学习就不再只是**监督微调之上的一个轻量附加组件**，
而会 **变成一个系统工程问题**。
你需要大规模 rollout、高吞吐验证、稳定的策略更新，以及高效采样。

## 2.3 重大转变：从大规模 pre-train 转向大规模 post-train (for reasoning)

推理模型的兴起，既是一个**关于建模的叙事**，也是一个**关于基础设施的叙事**。

* OpenAI 把 o1 描述为一条通过**强化学习训练出来**的**推理线** (reasoning line)，
* DeepSeek R1 后来进一步强化了这个方向，揭示了这种 **reasoning-based RL** 到底需要多少专门的算法与基础设施投入。

第一个重大转变，也由此发生：从扩展预训练 (scaling pretraining)，转向扩展面向推理的后训练 (scaling post-training for reasoning)。

# 3 混合 thinking 的尝试

## 3.1 Qwen 的尝试

在 2025 年初，Qwen 团队雄心勃勃地认为理想的模型应该 **统一 thinking 和 instruct 两种模式**。

* **可指定推理预算**，例如 low / medium / high 这样的推理档位；
* 最好还能从提示词和上下文中自动推断出合适的推理预算，让模型自己判断什么时候应该立刻回答，什么时候需要多想一会儿，什么时候又应该在真正困难的问题上投入更多计算。

从理念上说，这个方向是对的。Qwen3 就是当时最清晰的公开尝试之一：它引入了“混合思维模式”，
在同一模型家族中同时支持 thinking 和 non-thinking 两种行为，强调可控的思考预算，
并描述了一条四阶段后训练流程，其中在长 CoT 冷启动和推理强化学习之后，还显式加入了“thinking mode fusion（思维模式融合）”。

### 3.1.1 困难：thinking 和 non-thinking 模式的数据分布和行为目标很不一样

“融合”这件事，做起来远比说起来难。
真正困难的部分在于数据。

当考虑把 thinking 和 instruct 合并时，大家往往首先想到的是模型侧兼容性：

* 一个 checkpoint 能不能同时支持两种模式，
* 一个 chat template 能不能在两者之间切换，
* 一套服务栈能不能暴露出正确的控制开关。

但这里的一个深层的问题是，**这两种模式对应的数据分布和行为目标本来就有显著差异**。

在尝试平衡模型融合与提升后训练数据质量、多样性的过程中，我们做的并不好。

### 3.1.2 用户行为画像的冲突

在这个阶段，我们也非常关注用户究竟是如何实际使用 thinking 和 instruct 模式的。

* instruct 模型：优点是直接、简洁、格式合规，因此在改写、标注、模板化客服、结构化抽取、运营问答这类高频、批量的企业场景任务上很受客户欢迎；
* thinking 模型：优点是适合长程和复杂任务，有连贯的中间结构、多条备选路径，保留了足够多的内部计算来提升最终正确率，因此也需要花更多 token。

这两种行为画像**天然是彼此拉扯的**。
如果融合数据没有经过足够精细的策划与筛选，结果通常是在两个方向上都做得很平庸：

* “thinking” 会变得噪声更大、更臃肿、也更缺乏决断力；
* “instruct” 则会变得不够干净利落、不够稳定，成本也高于企业用户真正想要的水平。

### 3.1.3 回到独立的 Instruct 和 Thinking 模型

在实践中，还是 thinking 和 non-thinking 模式更有吸引力。因此，
Qwen3 2507 版本发布了独立的 Instruct 和 Thinking 更新，其中包括 30B 和 235B 版本。

在商业部署中，仍然有大量客户更需要那种高吞吐、低成本、高可控的 instruct 行为来处理批量任务。
在这些场景里，融合并没有显而易见的收益。

将两条线分开，反而让团队能够更干净地聚焦解决各自的数据和训练问题。

## 3.2 其他厂商的融合模型

### 3.2.1 Claude / GLM / DeepSeek

* Anthropic 公开主张一种一体化模型哲学
  + Claude 3.7 Sonnet 为混合推理模型，用户既可以选择普通响应，也可以选择 extended thinking，而 API 用户还能设置 thinking budget。
  + Anthropic 明确表示，他们相信**推理** (reasoning) 应该是一种**集成到模型内的能力**，
    **而不是一个独立模型**。
* GLM-4.5 也公开将自己定位为同时具有 thinking 和 non-thinking 模式的混合推理模型，把推理、编码和 agent 能力统一在一起；
* DeepSeek 后来也通过 V3.1 的 “Think & Non-Think” 混合推理走向了类似方向。

## 3.3 背后的关键问题：强硬拼凑还是自然生长出来的

这里有个关键问题是：**这种融合是不是“自然生长”出来的**。

* 如果 thinking 和 instruct 只是被强行塞进同一个 checkpoint 里，却依然像两个生硬拼接起来的人格那样行事，那么产品体验仍然会很别扭。
* 真正成功的融合，需要一条平滑的 reasoning effort 光谱。
  + 模型应当能够表达多个不同层级的 effort 程度，并且理想情况下还能自适应地做出选择。
  + GPT 风格的 effort control 指向的正是这一点：**控制的是一套关于推理预算的策略**，而不是一个非黑即白的二元开关。

Anthropic 对 Claude 3.7 和 Claude 4 的公开表述相对克制。

* 他们强调一体化推理、用户可控的思考预算、真实世界任务、代码质量，以及后来在 extended thinking 过程中使用工具的能力。
* Claude 3.7 呈现为一个具有可控预算的混合推理模型；Claude 4 则进一步扩展到允许**推理与工具使用交替进行**。
* 与此同时，Anthropic 也把**编码、长时间运行任务以及 agent 工作流**明确作为**主要目标**。

### 3.3.1 生成更长的推理轨迹，并不会自动让模型更聪明

* 很多时候，过度外显的推理恰恰意味着计算资源分配不佳。
* 如果模型试图用同一种冗长方式去思考所有事情，那它可能并没有做好优先级排序，没有做好压缩，也没有做好行动。

### 3.3.2 thinking 应该由目标 workload 来决定

Anthropic 的路径暗示了一种更克制、更有纪律性的观点：**thinking 应该由目标 workload 来决定**。

* 如果目标是编码，那么 thinking 就应该帮助代码库导航、规划、任务分解、错误恢复以及工具编排；
* 如果目标是 agent 工作流，那么 thinking 的作用就应该是在长时程里提升执行质量，而不是产出一段看起来很厉害的中间输出物。

# 4 从“训练模型”的时代，迈向“训练 Agent”的时代

这种对“目标导向”的强调，指向了一个更大的变化：**我们正在从“训练模型”的时代，迈向“训练 Agent”的时代**。

我们在 Qwen3 博客中也明确写到，“我们正从一个聚焦训练模型的时代，转向一个以训练智能体为中心的时代”，并把未来强化学习的进步与面向长时程推理的环境反馈联系起来。

## 4.1 Agent 核心：与世界形成闭环交互

所谓 Agent，是一种能够制定计划（plan）、决定何时行动（act）、何时使用工具（tools）、感知环境反馈、修正策略（reflection），
并在长时间范围内持续前进的系统。

**Agent 的核心，是与世界形成闭环交互**。

## 4.2 Agentic thinking 与 Reasoning thinking 的区别

二者对应的优化目标完全不同：

* reasoning thinking 通常是根据最终答案之前**那段内部思考的质量**来判断的：模型能不能解出定理、写出证明、生成正确代码，或者通过某项 benchmark；
* agentic thinking 关心的则是：**模型在与环境交互的过程中，能不能持续前进**。

核心问题由**“模型能不能思考得足够长？”**转变为
**“模型能不能以一种能够支撑有效行动的方式来思考？”**

Agentic thinking 必须处理几类纯推理模型大多不会遇到的问题：

* 决定什么时候停止思考并开始采取行动
* 选择调用哪个工具，以及按什么顺序调用
* 将来自环境的噪声观察或不完整观察纳入决策
* 在失败之后修正计划
* 在多轮交互和多次工具调用中维持...