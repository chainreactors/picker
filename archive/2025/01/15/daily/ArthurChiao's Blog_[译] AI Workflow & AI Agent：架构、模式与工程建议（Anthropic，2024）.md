---
title: [译] AI Workflow & AI Agent：架构、模式与工程建议（Anthropic，2024）
url: https://arthurchiao.github.io/blog/build-effective-ai-agent-zh/
source: ArthurChiao's Blog
date: 2025-01-15
fetch_date: 2025-10-06T20:09:22.876238
---

# [译] AI Workflow & AI Agent：架构、模式与工程建议（Anthropic，2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译] AI Workflow & AI Agent：架构、模式与工程建议（Anthropic，2024）

Published at 2025-01-14 | Last Update 2025-01-14

### 译者序

本文翻译自 2024 年 Anthropic（开发 Claude 大模型的公司）的一篇文章 [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)。

> Agents 只是一些**“在一个循环中，基于环境反馈来选择合适的工具，最终完成其任务”**的大模型。

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [1 什么是 AI `Agent`/`Workflow`？](#1-什么是-ai-agentworkflow)
  + [1.1 Workflow vs. Agent](#11-workflow-vs-agent)
  + [1.2 何时使用/不使用 Agent & Workflow](#12-何时使用不使用-agent--workflow)
  + [1.3 何时以及如何使用框架](#13-何时以及如何使用框架)
  + [1.4 一些例子](#14-一些例子)
* [2 Workflow & Agent 的基础构建模块](#2-workflow--agent-的基础构建模块)
  + [2.1 增强型大模型（augmented LLM）](#21-增强型大模型augmented-llm)
  + [2.2 功能选型建议](#22-功能选型建议)
  + [2.3 小结](#23-小结)
* [3 Workflow](#3-workflow)
  + [3.1 提示链（Prompt chaining）](#31-提示链prompt-chaining)
    - [3.1.1 适用场景](#311-适用场景)
    - [3.1.2 场景举例](#312-场景举例)
      * [生成营销文案](#生成营销文案)
      * [按大纲编写文档](#按大纲编写文档)
  + [3.2 路由（Routing）](#32-路由routing)
    - [3.2.1 适用场景](#321-适用场景)
    - [3.2.2 场景举例](#322-场景举例)
      * [智能客服](#智能客服)
      * [大小模型路由](#大小模型路由)
  + [3.3 并行化（Parallelization）](#33-并行化parallelization)
    - [3.3.1 适用场景](#331-适用场景)
    - [3.3.2 场景举例](#332-场景举例)
      * [旁路安全检测](#旁路安全检测)
      * [大模型性能评估的自动化](#大模型性能评估的自动化)
      * [Code review](#code-review)
      * [生成的代码的质量评估](#生成的代码的质量评估)
  + [3.4 编排者-工作者（Orchestrator-workers）](#34-编排者-工作者orchestrator-workers)
    - [3.4.1 适用场景](#341-适用场景)
    - [3.4.2 场景举例](#342-场景举例)
      * [Code review](#code-review-1)
      * [智能搜索](#智能搜索)
  + [3.5 评估者-优化者（Evaluator-optimizer）](#35-评估者-优化者evaluator-optimizer)
    - [3.5.1 适用场景](#351-适用场景)
    - [3.5.2 场景举例](#352-场景举例)
      * [文学翻译](#文学翻译)
      * [复杂的搜索任务](#复杂的搜索任务)
  + [3.6 AI Workflow 小结](#36-ai-workflow-小结)
* [4 Agent](#4-agent)
  + [4.1 原理](#41-原理)
  + [4.2 抽象层次：Agent vs. LLM](#42-抽象层次agent-vs-llm)
  + [4.3 何时使用 Agent](#43-何时使用-agent)
  + [4.4 Agent 设计三原则](#44-agent-设计三原则)
  + [4.5 场景举例](#45-场景举例)
* [5 总结](#5-总结)
* [致谢](#致谢)
* [附录 1：真实 Agent 举例](#附录-1真实-agent-举例)
  + [A. AI 客服](#a-ai-客服)
  + [B. Coding Agent](#b-coding-agent)
* [附录 2：工具的提示词工程（Prompt engineering your tools）](#附录-2工具的提示词工程prompt-engineering-your-tools)
  + [输出格式的选择](#输出格式的选择)
  + [建议](#建议)

---

过去一年中，我们与几十个团队合作过，构建了很多不同行业的大模型 Agent。
我们从中得到的经验是：**成功的 Agent** 并不是依靠复杂的框架或库，
而是**基于简单、可组合的模式逐步构建**的。

本文总结我们在此过程中积累的一些 **Agent 方法论**，并给出一些**实用的工程建议**。

# 1 什么是 AI `Agent`/`Workflow`？

目前关于 AI Agent 并**没有一个统一的定义**：

* 有人将 Agent 定义为**完全自主的系统**，这些系统可以在较长时间内**独立运行，使用各种工具来完成复杂任务**。
* 有人则用这个术语来描述一种遵循预定义**工作流**的规范实现（prescriptive implementations that follow predefined workflows）。

在 Anthropic，我们将所有这些统一归类为 **`agentic systems`**。

## 1.1 Workflow vs. Agent

虽然统一称为“智能体系统”，但我们还是对 Workflow 和 Agent 做出了重要的**架构区分**，
因此二者属于两类不同的系统：

* Workflow：**通过预定义的代码路径**来**编排大模型和和工具**
  （systems where LLMs and tools are orchestrated through predefined code paths）；
* Agent：**大模型动态决定自己的流程及使用什么工具，自主控制如何完成任务**
  （systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks）。

## 1.2 何时使用/不使用 Agent & Workflow

在使用大模型构建应用程序时，我们建议**寻找尽可能简单的方案，只有在必要时才增加复杂性**。

* 这意味着**如无必要，不要试图构建 Agent/Workflow**。
* Agent/Workflow 虽然在处理任务时效果更好，但通常也会有更高的延迟和成本，因此需要权衡利弊。

如果确实是要解决复杂场景的问题，

* Workflow 为明确定义的任务提供了可预测性和一致性，
* Agent 则在需要**大规模灵活性和模型驱动的决策**时是一个更好的选择。

但是，对于很多应用程序来说，大模型本身加上 **RAG、in-context examples**
等技术通常就足以解决问题了。

## 1.3 何时以及如何使用框架

许多框架可以简化 Agent/Workflow 的实现，包括：

* [LangGraph](https://langchain-ai.github.io/langgraph/) from LangChain;
* Amazon Bedrock’s [AI Agent framework](https://aws.amazon.com/bedrock/agents/);
* [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
* [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

这些框架通过简化标准的底层任务（如调用 LLM、定义和解析工具以及链接调用）使用户更容易入门。
但是，它们通常会**创建额外的抽象层**，这可能会使**底层的提示和响应变得难以调试**，增加了不必要的复杂性。

我们建议开发者，

* **首选直接使用 LLM API**：本文接下来介绍的许多模式几行代码就能实现；
* 如果**确实要用框架，要确保理解这些框架的底层代码**。对底层代码的错误假设是常见的问题来源。

## 1.4 一些例子

见 [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)。

# 2 Workflow & Agent 的基础构建模块

## 2.1 增强型大模型（augmented LLM）

如下图所示，Agent/Workflow 的基本构建模块是一个**增强型大语言模型**，

![](/assets/img/build-effective-ai-agents/augmented-llm.webp)

这个模型具有**检索、工具和记忆**等增强功能。
模型可以主动使用这些功能，例如搜索查询、选择适当的工具、保存必要的信息到记忆模块中等等。

## 2.2 功能选型建议

关于以上提到的增强功能如何选择，我们有如下建议：

1. 不是所有功能都需要用上，而应该**根据你的实际需求，只保留最必要的部分**；
2. 尽量使用那些**文档完善的组件**，否则就是给自己挖坑。

最后，实现这些增强功能有很多方式，我们最近发布的
[Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) 也是其中一种。
开发者只需要实现简单的客户端 [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients)，
就能与不断增长的第三方工具生态系统进行集成。

## 2.3 小结

基于增强型大模型，我们就可以构建出各种 AI Workflow & Agent。

# 3 Workflow

本节来看一些常见的 AI Workflow 范式。

## 3.1 提示链（Prompt chaining）

![](/assets/img/build-effective-ai-agents/prompt-chaining.webp)

提示链将任务分解为**一系列顺序的子任务**，

* 每个 LLM call 处理前一个 LLM call 的输出；
* 可以在中间任何步骤添加检查点（图中的 “Gate”），以确保处理过程仍在正轨上。

### 3.1.1 适用场景

适用于能**干净地将任务分解为固定子任务**的场景。

背后的逻辑：相比于一整个大任务，**拆解后的每个 LLM call 都是一个准确率更高、延迟更低、更容易完成的任务**。

### 3.1.2 场景举例

#### 生成营销文案

生成营销文案，然后将其翻译成不同的语言。

#### 按大纲编写文档

首先编写文档大纲，确保大纲符合某些标准，然后根据大纲编写文档。

## 3.2 路由（Routing）

![](/assets/img/build-effective-ai-agents/routing-workflow.webp)

通过路由对输入进行分类，并将其转发到**专门的后续任务**（specialized followup task）。

* 将任务的关注点进行拆解，从而**针对每个具体任务设计和调整提示词**。
* 否则，（all-in-one）提示词不仅很长，而且针对任何一种任务的提示词优化都可能会导致其他任务的性能下降。

### 3.2.1 适用场景

* 适用于**存在不同类别的复杂任务**，而且这些类别分开处理时，都能得到更好的效果。
* 前提是**能够准确分类**，至于是使用大模型分类，还是使用传统模型/算法分类，关系不大。

### 3.2.2 场景举例

#### 智能客服

将不同类型的用户问题（一般问题、请求退款、技术支持）转发到不同的下游流程、提示和工具。

#### 大小模型路由

将简单/常见问题路由到较小的模型，如 Claude 3.5 Haiku，将困难/不寻常问题路由到更强大的模型，如 Claude 3.5 Sonnet，以优化成本和速度。

## 3.3 并行化（Parallelization）

![](/assets/img/build-effective-ai-agents/parallelization-workflow.webp)

多个任务同时进行，然后**对输出进行聚合处理**。考虑两个场景：

1. 分段（Sectioning）：类似 MapReduce，将任务分解为独立的子任务并行运行，最后对输出进行聚合。
2. 投票（Voting）：相同的任务并行执行多次，以获得多样化的输出。

### 3.3.1 适用场景

分为两类：

1. 并行化可以提高任务的最终完成速度，
2. 需要多种视角或尝试，对所有结果进行对比，取最好的结果。

背后的逻辑：如果一个复杂任务需要考虑很多方面，那针对每个方面单独调用 LLM 效果通常会更好，
因为每个 LLM 都可以更好地关注一个具体方面。

### 3.3.2 场景举例

#### 旁路安全检测

属于 Sectioning。

一个模型实例处理用户查询，另一个模型实例筛选是否包含不当的内容或请求。这通常比让同一个模型实例同时请求响应和安全防护效果更好。

#### 大模型性能评估的自动化

属于 Sectioning。

针对给到的提示词，每个 LLM 调用评估模型不同方面的性能。

#### Code review

属于 voting。

几个不同的提示审查并标记代码，寻找漏洞。

#### 生成的代码的质量评估

属于 voting。

评估输出的代码是否恰当：使用多个提示词，分别评估生成的代码的不同方面，
或通过不同的投票阈值，以平衡误报和漏报（false positives and negatives）。

## 3.4 编排者-工作者（Orchestrator-workers）

![](/assets/img/build-effective-ai-agents/orchestrator-workers-workflow.webp)

在这种 Workflow 中，一个中心式 LLM 动态地分解任务，将其委托给 worker LLM，并汇总它们的结果。

### 3.4.1 适用场景

适用于无法预测所需子任务的复杂任务。例如，在编程中，修改的文件数量。

虽然在拓扑上与 Parallelization Workflow 相似，但关键区别在于其灵活性 —— 子任务不是预先定义的，而是由协调者/编排者根据特定输入确定的。

### 3.4.2 场景举例

#### Code review

编程产品：每次对多个文件（数量不确定）进行修改。

#### 智能搜索

搜索任务：从多个来源收集和分析信息。

## 3.5 评估者-优化者（Evaluator-optimizer）

![](/assets/img/build-effective-ai-agents/evaluator-optimizer-workflow.webp)

在这种 Workflow 中，一个 LLM call 生成响应，而另一个提供评估和反馈，形成一个闭环。

### 3.5.1 适用场景

**有明确的评估标准，并且迭代式改进确实有效**（可衡量）。

两个适用于此模式的标志，

1. 当人类给出明确反馈时，LLM 响应可以明显改进；
2. LLM 也能提供此类反馈。

类似于作家写一篇文章并不断润色的过程。

### 3.5.2 场景举例

#### 文学翻译

承担翻译任务的 LLM 可能没有捕捉到细微差别，但承担评估任务的 LLM 可以提供有用的批评。

#### 复杂的搜索任务

需要多轮搜索和分析以收集全面信息，评估者决定是否需要进一步搜索。

## 3.6 AI Workflow 小结

Workflow 是基于增强型大模型的一种应用形式，可以帮助用户**将任务分解为更小的子任务，以便更好地处理**。
虽然 Workflow 也有一些动态的能力，例如路由和并行化，但这种程度的动态能力还是**预定义的**。
下面将出场的 AI Agent，则在动态上与此完全不同了。

# 4 Agent

随着 LLM 在关键能力上的不断成熟 —— 理解复杂输入、进行推理和规划、可靠地使用工具以及自动从错误中恢复 ——
人们开始将 Agent 应用到生产环境中。

## 4.1 原理

Agent 一般从下面场景收到任务并开始执行：

1. **收到明确的人类指令**；
2. **与人类交流到一定程度时，理解了自己接下来应该做什么**。

一旦任务明确，Agent 就会独立规划和执行，中间也可能会问人类一些问题，以获取更多信息或帮助它自己做出正确判断。

* 在 Agent 执行过程中，对它来说最重要的是每一步执...