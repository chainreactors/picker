---
title: AI Agent（智能体）技术白皮书（Google，2024）
url: https://arthurchiao.github.io/blog/ai-agent-white-paper-zh/
source: ArthurChiao's Blog
date: 2025-01-08
fetch_date: 2025-10-06T20:08:48.307358
---

# AI Agent（智能体）技术白皮书（Google，2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译] AI Agent（智能体）技术白皮书（Google，2024）

Published at 2025-01-07 | Last Update 2025-01-07

### 译者序

本文翻译自 2024 年 Google 团队的一份 [Agents 白皮书](https://drive.google.com/file/d/1oEjiRCTbd54aSdB_eEe3UShxLBWK9xkt/view?pli=1)，
作者 Julia Wiesinger, Patrick Marlow, Vladimir Vuskovic。

Agent 可以理解为是一个**扩展了大模型出厂能力**的应用程序。

**工具的使用，是人类区别于动物的标志 —— 也是 Agent 区别于大模型的标志**。

水平及维护精力所限，译文不免存在错误或过时之处，如有疑问，请查阅原文。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

以下是译文。

---

* [译者序](#译者序)
* [1 引言](#1-引言)
  + [1.1 人类的先验知识与工具的使用](#11-人类的先验知识与工具的使用)
  + [1.2 人类的模仿者](#12-人类的模仿者)
* [2 什么是 Agent？](#2-什么是-agent)
  + [2.1 概念：应用程序](#21-概念应用程序)
  + [2.2 架构：cognitive architecture](#22-架构cognitive-architecture)
  + [2.3 组件](#23-组件)
    - [2.3.1 模型（model）](#231-模型model)
    - [2.3.2 工具（tool）](#232-工具tool)
    - [2.3.3 编排层（orchestration）](#233-编排层orchestration)
  + [2.4 Agent 与 model 的区别](#24-agent-与-model-的区别)
* [3 认知架构：Agent 是如何工作的](#3-认知架构agent-是如何工作的)
  + [3.1 类比：厨师做菜](#31-类比厨师做菜)
  + [3.2 Agent 推理框架](#32-agent-推理框架)
    - [3.2.1 ReAct](#321-react)
    - [3.2.2 Chain-of-Thought (CoT)](#322-chain-of-thought-cot)
    - [3.2.3 Tree-of-Thoughts (ToT)](#323-tree-of-thoughts-tot)
  + [3.3 ReAct 例子](#33-react-例子)
* [4 工具：模型通往现实世界的关键](#4-工具模型通往现实世界的关键)
  + [4.1 工具类型一：extensions](#41-工具类型一extensions)
    - [4.1.1 需求：预定航班的 Agent](#411-需求预定航班的-agent)
    - [4.1.2 实现方式一：传统方式，写代码解析参数](#412-实现方式一传统方式写代码解析参数)
    - [4.1.3 实现方式二：使用 Extension](#413-实现方式二使用-extension)
    - [4.1.4 Extension 示例](#414-extension-示例)
  + [4.2 工具类型二：functions](#42-工具类型二functions)
    - [4.2.1 Function vs. Extension](#421-function-vs-extension)
    - [4.2.2 例子：教模型结构化输出信息](#422-例子教模型结构化输出信息)
    - [4.2.3 示例代码](#423-示例代码)
  + [4.3 工具类型三：data storage](#43-工具类型三data-storage)
    - [4.3.1 实现与应用](#431-实现与应用)
    - [4.3.2 例子](#432-例子)
  + [4.4 工具小结](#44-工具小结)
* [5 通过针对性学习提升模型性能](#5-通过针对性学习提升模型性能)
  + [5.1 In-context learning, e.g. `ReAct`](#51-in-context-learning-eg-react)
  + [5.2 Retrieval-based in-context learning, e.g. `RAG`](#52-retrieval-based-in-context-learning-eg-rag)
  + [5.3 Fine-tuning based learning](#53--fine-tuning-based-learning)
  + [5.4 再次与“厨师做饭”做类比](#54-再次与厨师做饭做类比)
* [6 基于 LangChain 快速创建 Agent](#6-基于-langchain-快速创建-agent)
  + [6.1 代码](#61-代码)
  + [6.2 运行效果](#62-运行效果)
  + [6.3 使用 Google Vertex AI Agent 创建生产应用](#63-使用-google-vertex-ai-agent-创建生产应用)
* [7 总结](#7-总结)
* [参考资料](#参考资料)

---

# 1 引言

## 1.1 人类的先验知识与工具的使用

人类能很好地处理**复杂和微妙的模式识别任务**。
能做到这一点是因为，我们会通过书籍、搜索或计算器之类的**工具**来补充我们头脑中的先验知识，
然后才会给出一个结论（例如，“图片中描述的是 XX”）。

## 1.2 人类的模仿者

与以上类似，我们可以对生成式 AI 模型进行训练，
让它们能**使用工具**来在现实世界中**获取实时信息或给出行动建议**。
例如，

* 利用数据库查询工具获取客户的购物历史，然后给出购物建议。
* 根据用户的查询，调用相应 API，替用户回复电子邮件或完成金融交易。

为此，模型不仅需要**访问外部工具**，还要能够**自主规划和执行任务**。
这种具备了**推理、逻辑和访问外部信息**的生成式 AI 模型，就是 Agent 的概念；
换句话说，Agent 是一个**扩展了生成式 AI 模型出厂能力**的程序。

# 2 什么是 Agent？

## 2.1 概念：应用程序

宽泛地来说，生成式 AI Agent 可以被定义为一个**应用程序**，
通过**观察周围世界并使用可用的工具来实现其目标**。

* Agent 是有自主能力的（autonomous），只要提供了合适的目标，它们就能独立行动，无需人类干预；
* 即使是模糊的人类指令，Agent 也可以推理出它接下来应该做什么，并采取行动，最终实现其目标。

在 AI 领域，Agent 是一个非常通用的概念。本文接下来要讨论的 Agent 会更具体，
指的是本文写作时，**基于生成式 AI 模型能够实现的 Agents**。

## 2.2 架构：cognitive architecture

为了理解 Agent 的内部工作原理，我们需要看看驱动 Agent 行为、行动和决策（behavior, actions, and decision making）的基础组件。

这些组件的组合实现了一种所谓的**认知架构**（cognitive architecture），
通过这些组件可以实现许多这样的架构。我们后面还会就这一点展开讨论。

## 2.3 组件

Agent 架构中有三个核心组件，如图所示，

![](/assets/img/ai-agent-white-paper/1-agent-arch.png)

Figure 1. 典型 Agent 架构与组件。

### 2.3.1 模型（model）

这里指的是用作 Agent 中用来做核心决策的语言模型（LM）。

* 可以是一个或多个任何大小的模型，能够遵循基于指令的推理和逻辑框架，如 **`ReAct、Chain-of-Thought、Tree-of-Thoughts`**。
* 可以是通用的、多模态的，或根据特定 Agent 架构的需求微调得到的模型。
* 可以通过“能展示 Agent 能力的例子或数据集”来进一步微调模型，例如 Agent 在什么上下文中使用什么工具，或者执行什么推理步骤。

### 2.3.2 工具（tool）

基础模型在文本和图像生成方面非常强大，但无法与外部世界联动极大限制了它们的能力。
工具的出现解决了这一问题。有了工具，Agent 便能够与外部数据和服务互动，大大扩展了它们的行动范围。

工具可以有多种形式，常见是 **`Web API`** 方式，即 GET、POST、PATCH 和 DELETE 方法。
例如，结合用户信息和获取天气数据的 tool，Agent 可以为用户提供旅行建议。

有了工具，Agent 可以访问和处理现实世界的信息，这使它们能够支撑更专业的系统，如检索增强生成（RAG），显著扩展了 Agent 的能力。

### 2.3.3 编排层（orchestration）

编排层描述了一个**循环**过程：Agent 如何接收信息，如何进行内部推理，如何使用推理来结果来指导其下一步行动或决策。

* 一般来说，这个循环会持续进行，直到 Agent 达到其目标或触发停止条件。
* 编排层的复杂性跟 Agent 及其执行的任务直接相关，可能差异很大。
  例如，一些编排就是简单的计算和决策规则，而其他的可能包含链式逻辑、额外的机器学习算法或其他概率推理技术。

我们将在认知架构部分更详细地讨论 Agent 编排层的详细实现。

## 2.4 Agent 与 model 的区别

为了更清楚地理解 Agent 和模型之间的区别，这里整理个表格，

|  | 模型 | Agent |
| --- | --- | --- |
| 知识范围 | 知识仅限于其**训练数据**。 | 通过工具连接外部系统，能够在模型自带的知识之外，实时、动态**扩展知识**。 |
| 状态与记忆 | **无状态**，每次推理都跟上一次没关系，除非在外部给模型加上会话历史或上下文管理能力。 | **有状态**，自动管理会话历史，根据编排自主决策进行多轮推理。 |
| 原生工具 | 无。 | 有，自带工具和对工具的支持能力。 |
| 原生逻辑层 | 无。需要借助提示词工程或使用推理框架（CoT、ReAct 等）来形成复杂提示，指导模型进行预测。 | 有，原生认知架构，内置 CoT、ReAct 等推理框架或 LangChain 等编排框架。 |

# 3 认知架构：Agent 是如何工作的

## 3.1 类比：厨师做菜

想象厨房中一群忙碌的厨师。他们的职责是根据顾客的菜单，为顾客烹制相应的菜品。
这就涉及到我们前面提到的**“规划 —— 执行 —— 调整”**循环。具体来说，
厨师们需要执行以下步骤，

1. 收集信息（输入）：顾客点的菜，后厨现有的食材等等；
2. 推理（思考）：根据收集到的信息，判断可以做哪些菜；
3. 做菜（行动）：包括切菜、加调料、烹炒等等。

在以上每个阶段，厨师都根据需要进行调整 —— 例如某些食材不够用了，或者顾客反馈好吃或难吃了 —— 进而不断完善他们的计划。
这个**信息接收、规划、执行和调整**（information intake, planning,
executing, and adjusting）的循环描述的就是一个**厨师用来实现其目标的特定认知架构**。

## 3.2 Agent 推理框架

跟以上厨师类似，Agent 也可以使用认知架构处理信息、做出决策，并根据前一轮的输出调整下一个行动，如此循环迭代来实现其最终目标。

* 在 Agent 中，**认知架构的核心是编排层，负责维护记忆、状态、推理和规划**（memory, state, reasoning and planning）。
* 它使用快速发展的**提示词工程及相关框架**（prompt engineering and associated frameworks）来**指导推理和规划**，使 Agent 能够更有效地与环境互动并完成任务。

在写作本文时，有下面几种流行的推理框架和推理技术。

### 3.2.1 ReAct

为语言模型提供了一个思考过程策略。

已经证明 ReAct 优于几个 SOTA 基线，提高了 LLM 的人机交互性和可信度。

### 3.2.2 Chain-of-Thought (CoT)

通过中间步骤实现推理能力。CoT 有各种子技术，包括自我一致性、主动提示和多模态 CoT，适合不同的场景。

### 3.2.3 Tree-of-Thoughts (ToT)

非常适合探索或战略前瞻任务。概括了链式思考提示，并允许模型探索各种思考链，作为使用语言模型解决问题的中间步骤。

## 3.3 ReAct 例子

Agent 可以使用以上一种或多种推理技术，给特定的用户请求确定下一个最佳行动。
例如，使用 ReAct 的例子，

1. 用户向 Agent 发送查询。
2. Agent 开始 ReAct sequence。
3. Agent 提示模型，要求其生成下一个 ReAct 步骤及其相应的输出：
   1. 问题：提示词 + 用户输入的问题
   2. 思考：模型的想法：下一步应该做什么
   3. 行动：模型的决策：下一步要采取什么行动。这里就是可以引入工具的地方，
      例如，行动可以是 **`[Flights, Search, Code, None]`** 中的一个，前三个代表模型可以选择的已知工具，最后一个代表“无工具选择”。
   4. 行动的输入：模型决定是否要向工具提供输入，如果要提供，还要确定提供哪些输入
   5. 观察：行动/行动输入序列的结果。根据需要，这个思考/行动/行动输入/观察（**`thought / action / action input / observation`**）可能会重复 N 次。
   6. 最终答案：模型返回对原始用户查询的最终答案。
4. ReAct 循环结束，并将最终答案返回给用户。

![](/assets/img/ai-agent-white-paper/2-agent-with-ReAct.png)

Figure 2. Example Agent with ReAct reasoning in the orchestration layer

如图 2 所示，模型、工具和 Agent 配置共同工作，根据用户的输入返回了一个有根据的、简洁的响应。
虽然模型第一轮根据其先前知识猜了一个答案（幻觉），但它接下来使用了一个工具（航班）来搜索实时外部信息，
从而能根据真实数据做出更明智的决策，并将这些信息总结回给用户。

总结起来，Agent 的响应质量与**模型的推理能力和执行任务的能力**直接相关，
包括选择正确工具的能力，以及工具自身的定义的好坏（how well that tools has been defined）。
就像厨师精选食材、精心做菜，并关注顾客的反馈一样，Agent 依赖于**合理的推理和可靠的信息**来提供最佳结果。

在下一节中，我们将深入探讨 Agent 与“新鲜”数据的各种连接方式。

# 4 工具：模型通往现实世界的关键

语言模型很擅长处理信息，但它们缺乏**直接感知和影响现实世界**的能力。
在需要与外部系统或数据联动的情况下，这些模型的实用性就很低了。某种意义上说，
**语言模型的能力**受限于它们的**训练数据中覆盖到的信息**。

那么，如何赋予模型**与外部系统进行实时、上下文感知的互动能力**呢？
目前有几种方式：

* Functions
* Extensions
* Data Stores
* Plugins

虽然名称各异，但它们都统称为**工具**（tools）。
**工具是将基础模型与外部世界连接起来的桥梁**。

能够连接到外部系统和数据之后，Agent 便能够执行更广泛的任务，并且结果更加准确和可靠。
例如，工具使 Agent 能够调整智能家居设置、更新日程、从数据库中获取用户信息或根据特定指令发送电子邮件。

写作本文时，Google 模型能够与三种主要工具类型互动：Functions、Extensions、Data Stores。

配备了工具之后，Agent 不仅解锁了**理解真实世界和在真实世界中做出行动**的超能力，
而且打开了各种新应用场景和可能性的大门。

## 4.1 工具类型一：extensions

在最简单的概念上：
extension 是一种**以标准化方式连接 API 与 Agent 的组件**，
使 Agent 能够**调用外部 API，而不用管这些 API 背后是怎么实现的**。

### 4.1.1 需求：预定航班的 Agent

假设你想创建一个帮用户预订航班的 Agent，并使用 Google Flights API 来搜索航班信息，
但不确定如何让你的 Agent 调用这个 API。

![](/assets/img/ai-agent-white-paper/3.png)

Figure 3. How do Agents interact with External APIs?

### 4.1.2 实现方式一：传统方式，写代码解析参数

传统解决方式是写代码，从用户输入中解析城市等相关信息，然后调用 API。
例如，

* 用户输入 “I want to book a flight from Austin to Zurich”（“我想从奥斯汀飞往苏黎世”）；
  我们的代码需要从中提取“Austin”和“Zurich”作为相关信息，然后才能进行 API 调用。
* 但如果用户输入“I want to book a flight to Zurich”，我们就无法获得出发城市信息，进而无法成功调用 API，所以需要写很多代码来处理边界 case。

显然，这种方法维护性和扩展性都很差。有没有更好的解决方式呢？
这就轮到 exntension 出场了。

### 4.1.3 实现方式二：使用 Extension
...