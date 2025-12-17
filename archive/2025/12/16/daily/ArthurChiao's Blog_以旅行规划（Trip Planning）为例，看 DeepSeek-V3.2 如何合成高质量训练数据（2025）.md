---
title: 以旅行规划（Trip Planning）为例，看 DeepSeek-V3.2 如何合成高质量训练数据（2025）
url: https://arthurchiao.github.io/blog/deepseek-agentic-dataset-synthesizing-zh/
source: ArthurChiao's Blog
date: 2025-12-16
fetch_date: 2025-12-17T03:18:39.319986
---

# 以旅行规划（Trip Planning）为例，看 DeepSeek-V3.2 如何合成高质量训练数据（2025）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# 以旅行规划（Trip Planning）为例，看 DeepSeek-V3.2 如何合成高质量训练数据（2025）

Published at 2025-12-16 | Last Update 2025-12-16

如何基于 Agent/LLM 强大的**规划能力+生成能力+代码执行能力+反思能力**，
自动化合成大批量高质量数据：

![](/assets/img/deepseek-agentic-dataset-synthesizing/hypothetical-workflow.png)

Hypothetical workflow

![](/assets/img/deepseek-agentic-dataset-synthesizing/agentic-dataset-synthesizing.png)

DeepSeek-V3.2: workflow for synthesizing high-quality agentic datasets for RL training (in agentic fashion, without human intervention)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 场景：增强模型的 Trip Planning 能力](#1-场景增强模型的-trip-planning-能力)
  + [1.1 方案拆解](#11-方案拆解)
  + [1.2 子任务：准备高质量的 Trip Planning 数据](#12-子任务准备高质量的-trip-planning-数据)
* [2 方案：自动合成高质量 Trip Planning 数据](#2-方案自动合成高质量-trip-planning-数据)
  + [2.1 思考：人（专家）怎么完成这个任务](#21-思考人专家怎么完成这个任务)
  + [2.2 自动化：人工方案的 workflow 化](#22-自动化人工方案的-workflow-化)
  + [2.3 这个 workflow 的独特之处](#23-这个-workflow-的独特之处)
  + [2.4 小结](#24-小结)
* [3 图解：DeepSeek-V3.2 是怎么做的（”Large-Scale Agentic Tasks”）](#3-图解deepseek-v32-是怎么做的large-scale-agentic-tasks)
  + [3.1 方案描述](#31-方案描述)
  + [3.2 方案图解](#32-方案图解)
    - [Step 0: Agent 输入](#step-0-agent-输入)
    - [Step 1: Agent 构建旅行数据库](#step-1-agent-构建旅行数据库)
    - [Step 2: Agent 合成 tools（代码生成）](#step-2-agent-合成-tools代码生成)
    - [Step 3: 合成一个具体旅行规划任务](#step-3-合成一个具体旅行规划任务)
    - [Step 4：执行 solution function，（基于 tool calling）生成一个线路规划](#step-4执行-solution-function基于-tool-calling生成一个线路规划)
    - [Step 5：执行 verification function，对上一步生成的线路规划进行验证](#step-5执行-verification-function对上一步生成的线路规划进行验证)
    - [Step 6: 如果验证成功，将这条数据输出](#step-6-如果验证成功将这条数据输出)
    - [Step 7: 返回到 step 3，继续合成下一个更难的任务](#step-7-返回到-step-3继续合成下一个更难的任务)
    - [Step 8: 如果 step 5 验证失败，也返回到 step 3](#step-8-如果-step-5-验证失败也返回到-step-3)
    - [Step 9: 将错误返回给 Agent，让 Agent 尝试扩充 toolset](#step-9-将错误返回给-agent让-agent-尝试扩充-toolset)
  + [3.3 官方 Trip Planning sample](#33-官方-trip-planning-sample)
* [4 Kimi 老师补充的一些细节，帮助理解](#4-kimi-老师补充的一些细节帮助理解)
  + [4.1 生成的 Task 示例](#41-生成的-task-示例)
  + [4.2 输出样本要求](#42-输出样本要求)
    - [关键点](#关键点)
    - [样本筛选标准](#样本筛选标准)
    - [样本保存格式](#样本保存格式)
    - [输出样本示例（Trip Planning 任务）](#输出样本示例trip-planning-任务)
* [5 DeepSeek papers](#5-deepseek-papers)

---

# 1 场景：增强模型的 Trip Planning 能力

假设你在训练一个**通用模型**或垂域的**旅游行业模型**，
那你可能会遇到下面这样的用户诉求：

> 我计划今年十一从杭州出发玩三天，请帮我制定一份行程规划。几个要求：整个行程我
> 不想重复任何一个城市、酒店、景点或餐厅。另外，请务必确保推荐的每家酒店、餐厅和
> 景点都确实位于我当日所在的城市。关于第二天还需要注意：如果当晚入住的豪华酒店
> 价格在800元人民币及以上，则需严格控制其他开销——当日两家餐厅（午餐与晚餐）总消
> 费需低于350元，且两家餐厅评分均不低于4星，下午游览的景点门票需低于120元。若第
> 二天酒店属于中高档（500-800元），则预算可稍放宽：只需确保至少一家餐厅评分达
> 4.0星以上，且景点门票低于180元。若选择经济型酒店（200-500元），则只需保证至少
> 一家餐厅评分在3.2星以上。

要回答好这类问题，就需要对模型的**行程规划**（Itinerary）或称
**旅游规划**（Trip Planning）能力进行专门训练。

具体该怎么做呢？我们来尝试设计一个方案。

## 1.1 方案拆解

从非常高的 level 来说，要完成以上训练任务只需要做两件事情：

1. **数据集准备**：准备一批高质量的 Trip Planning 数据
2. **后训练**：基于高质量训练数据，对模型进行微调（SFT）或强化学习（RL）

本文接下来只关注第一个任务，**高质量数据集的准备**。

## 1.2 子任务：准备高质量的 Trip Planning 数据

再次从 high level 来说，这样的高质量数据集有两种来源：

1. **人工标注**：例如，找专业的旅行定制师或资深的旅行家，人工编写高质量的语料；
2. **自动合成**：通过某种不依赖人工的方式自动合成。

考虑到这个数据集不仅要求质量高，样本数量也要比较多，靠专业的人工标注成本是很高的，
而且人工标注方式的可扩展很差，因此我们接下来考虑**自动合成的方式**。

# 2 方案：自动合成高质量 Trip Planning 数据

## 2.1 思考：人（专家）怎么完成这个任务

先来设想一下，如果上面的旅行规划任务给到的是专业的旅游定制师或资深的旅行家，
他们是如何来完成这个任务的（也就是数据标注过程）。可能的工作流程：

1. 定制师或旅行家基于自己丰富的业务知识（城市、交通、景点、酒店、预算、偏好等等），
   初步判断下杭州出发三天能玩的目的地范围，得到一些**备选目的地**；
2. 针对这些备选目的地，以杭州为出发地，通过手动搜索或数据库查询，
   进一步充实交通、住宿、餐饮、景点、预算等需求，
   得到一些**备选线路**；
3. 针对这些备选线路，再进一步**验证**里面的每个具体步骤是否满足用户的要求，
   以及整体方案是否满足用户的要求；如果**满足就留下**这个线路；
   如果**不满足**（例如某一天的预算超了）就**进行相应的调整**直到满足，
   或者多次失败之后直接弃用这个备选路线；
4. 如果用户觉得上一步验证通过的线路还是**不够有吸引力**，
   则回到 step 1 or step 2 并顺序执行到 step 3，针对用户需求**重新设计**一些更有吸引力的线路。

经过以上步骤，最终得到的就是一些符合用户要求的高质量线路规划。

## 2.2 自动化：人工方案的 workflow 化

把以上的人工生产线路过程变成一个 workflow，就得到了一个基于 Agent 的自动化方案：

* 首先，我们得从某些地方获取一些 Trip Planning 相关的**基础旅游数据**，
  例如城市、交通、酒店、景点、价格等等信息，把它们存储起来备用；
* 接下来，得有一些**工具**来从这些数据中**筛选出我们想要的信息**，
  例如查询两个城市之间的交通方案、查询给定城市内的餐厅和景点等；
* 有了前两步的基础，剩下的就是**生成一个具体的旅行规划任务**，
  例如，“规划从上海到北京的三日游”，让 Agent 基于上一步提供的各种工具，帮我们将这个旅行规划方案设计出来。
  这个过程可以**进一步拆解为两个子任务**：
  1. 生成：**生成具体的旅行规划**；
  2. 验证：**验证生成的旅行规划是否符合用户的要求**。

基于以上流程，无需人工参与，就能自动完成一个行程规划任务，

* 如果**验证 OK，就将这个结果输出**；然后继续生成下一个（更难的）旅行规划任务；
* 如果失败，就要看问题是出在哪里，例如可能是工具不够、生成的方案不对、方案对但验证过程有问题等，尝试调整这几个环节，直到方案成功。

## 2.3 这个 workflow 的独特之处

这个 workflow 画成图大概长下面这样，跟普通 workflow 的重要区别是：
Agent 不仅生成任务本身（**`task`**），还生成完成这个任务的代码
（**`solution function`**）、工具代码（**`tool functions`**）
和验证结果的代码（**`verification function`**），
并通过动态执行这些代码筛选出符合用户要求的高质量结果。

![](/assets/img/deepseek-agentic-dataset-synthesizing/hypothetical-workflow.png)

Hypothetical workflow

* 图的上半部分可以叫“**生成环境**”，这是常规 LLM 擅长做的；
* 图的下半部分是“**执行环境**”，把上一步生成的代码真正拿来运行，再根据运行结果给 Agent 一个反馈，进入 Agent 的反思和下一次迭代流程。
* 整个方案的输入只有一段**提示词**（如果不算执行环境），其他都是 Agent+Workflow 创建和管理的。

## 2.4 小结

实际上，思考以上问题是因为在看 DeepSeek-V3.2 tech report 时刚好看到它有这样一个 case，觉得玩得很高级。
接下来我们看看 DeepSeek 在这种**合成高质量数据场景**的具体方案设计。

# 3 图解：DeepSeek-V3.2 是怎么做的（”Large-Scale Agentic Tasks”）

DeepSeek-V3.2 tech report 的 **`3.2.3 Large-Scale Agentic Tasks`**
介绍了他们是如何强化大规模 Agentic 任务的，其中就涉及到了数据集的合成，我们前面介绍的 “Trip Planning” 例子其实就是来自这里。

## 3.1 方案描述

原文：

> General Agent To scale up agent environments and tasks in RL, we employ an automatic
> environment-synthesis agent that synthesizes 1,827 task-oriented environments. These tasks are
> hard to solve but easy to verify. The synthesis workflow primarily consists of environment and
> toolset construction, task synthesis, and solution generation. Specifically, the workflow proceeds
> as follows.
>
> 1. Given a task category (e.g., planning a travel itinerary) and a sandbox equipped with a
>    bash and a search tool, the agent first uses these tools to generate or retrieve relevant data
>    from the Internet and store them in the sandbox database.
> 2. The agent then synthesizes a set of task-specific tools, each implemented as a function.
> 3. To create tasks that are both challenging and automatically verifiable, the agent initially
>    proposes a simple task based on the current database, along with its
>    solution and verification functions implemented in Python. The solution
>    function is restricted to invoking tool functions or performing logical
>    computations, and cannot call other functions or directly access the
>    database, ensuring the task can only be solved through the tool interface.
>    Additionally, the results produced by the solution function must be
>    validated by the verification function. If the solution is not validated,
>    the agent will modify the solution or verification
>    functions until the solution’s output passes the verification. The agent then iteratively
>    increases the difficulty of the task and updates the corresponding solution and verification
>    functions. During this iterative process, if the current toolset is not sufficient to solve the
>    task, the agent will augment the toolset.

为了扩展 RL 中的 agent 环境和任务，我们采用了一个自动的 environment-synthesis
agent，该 agent 合成了 1,827 个 task-oriented environments。
这些任务的特点是**解决起来很难，但验证很容易**。
该 synthesis workflow 主要包括 environment & toolset 构建、task
synthesis 以及 solution generation。

**`Trip Planning`** 是其中的任务类型之一。

## 3.2 方案图解

具体过程如下图所示（根据个人理解画的，仅供参考，因为很多细节原文没提）：

![](/assets/img/deepseek-agentic-dataset-synthesizing/agentic-dataset-synthesizing.png)

核心是一个 Agent，接下来按序号介绍下各步骤。

### Step 0: Agent 输入

给 Agent 输入**任务类型**（e.g. “Trip Planning”）和可用的 sandbox 信息；

* 任务类型有很多种，旅行规划只是其中之一；
* sandbox 可以理解成一个 linux container，例如 **`Ubuntu`**，配置了 bash 和 search tool；

### Step 1: Agent 构建旅行数据库

Agent 开始干活，首先进入 sandbox，然后用 internet search tool
**从互联网搜索相关数据，并保存到 local database**；

* **输入**：任务类别（如 “trip planning”）+ 配备 `bash` 和 `search` 工具的 sandbox 环境
* **过程**：Agent 使用搜索工具从互联网爬取或生成结构化数据，包括交通、酒店、景点、门票、餐厅等等，存储到 sandbox 的数据库中
* **输出**：结构化数据表
* local database 可以想象成一个 **`SQLite`** 数据库

效果示意：

```
输入...