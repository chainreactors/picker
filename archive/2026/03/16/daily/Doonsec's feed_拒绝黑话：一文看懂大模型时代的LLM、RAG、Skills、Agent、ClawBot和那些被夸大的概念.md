---
title: 拒绝黑话：一文看懂大模型时代的LLM、RAG、Skills、Agent、ClawBot和那些被夸大的概念
url: https://mp.weixin.qq.com/s/7sz3-IdSnXYBuhx6Rq0rgQ
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:29.613033
---

# 拒绝黑话：一文看懂大模型时代的LLM、RAG、Skills、Agent、ClawBot和那些被夸大的概念

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XkUCeyh2WibiaKm8QpumkUKyyEeQwdazsyAPw7tdcHBrHZMSsicwKJGVFIbI1UiciczgprpE8xbEfeszfsFXL2aLoou6TYksEU5r2EYyjKego4Qw/0?wx_fmt=jpeg)

# 拒绝黑话：一文看懂大模型时代的LLM、RAG、Skills、Agent、ClawBot和那些被夸大的概念

原创

Real返璞归真
Real返璞归真

Real返璞归真

![]()

在小说阅读器中沉浸阅读

## 公众号

欢迎关注公众号【Real返璞归真】，我们将不定期分享**CTF竞赛、二进制安全、JS/安卓逆向、AI安全**等领域的前沿知识与技术内容。

## 前言

最近两年，大模型领域出现了大量新名词：

```
LLM、Prompt、RAG、Function Calling、MCP、LangChain、Workflow、Agent、Skills、ClawBot……
```

如果只是看技术宣传，很容易产生一种感觉：AI世界每天都在发明新技术。

但实际上，大多数概念只是**对已有能力的不同封装方式**。很多时候只是**工程方法的变化，而不是技术革命**。

这篇文章尝试从更高的视角，把这些概念梳理清楚。杜绝**名词诈骗**，核心问题只有一个：**大模型到底是如何被“使用起来”的。**

## LLM：一切的核心

### 简介

![image-20260316102559261](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibjnHBIeSYwzE5rELw6y7TnNbeawvDfTFUB1HIc1fRg4MicbehAgicmIjkTwBNIcTIWBia2XSXicKMsYfqb2D9urVRj60Kb0eJ35EiaA/640?wx_fmt=png&from=appmsg)

所有东西的核心，其实只有一个：**LLM（Large Language Model）**。

本质上它就是：**成语接龙**。根据你给它的信息，猜下一个字该说什么。

从 GPT-1 到 GPT-4，模型变得越来越聪明，是因为它的**参数**规模（B，即 Billion，十亿级）发生了指数级飞跃。

LLM 的能力就像一个人，由两部分组成：

* **预训练知识：** 预训练阶段学到的海量知识。
* **上下文**：你现在跟它聊天的内容（Context）。

```
示例：
我是一名Java后端开发程序员（上下文）
请你帮我编写HelloWorld程序（提示词）
```

许多看似复杂的 AI 系统，拆解到底层其实都在做同一件事：**向上下文窗口中“塞入”更多有效信息。**

理解 AI 开发的捷径是看穿其本质——**任何“AI 框架”归根结底都是在进行精细化的上下文管理。**

理解LLM时，有三个最容易被混淆的概念：

* Prompt（提示词）
* Context（上下文）
* Memory（记忆）

### Prompt（提示词）

提示词就是：**你给模型的指令**。

例如：

```
你是一个Python专家，请你帮我编写计算器程序。
```

### Context（上下文）

上下文就是：**模型在当前推理时能看到的全部内容**。

包括：

* 提示词
* 用户输入
* 历史对话
* RAG检索内容
* 工具返回结果

这些都会被拼接进上下文。

### Memory（记忆）

很多AI产品宣传“长期记忆”。

其实绝大多数实现方式很简单：

1. 把历史记录存数据库
2. 需要时再放回context

所以所谓“记忆”其实只是：**可检索的历史上下文**。

## RAG：数据库

### 简介

![image-20260316102815640](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibgZ7zpYgrmv40mEPug6yAsYmyicicay97m1f8hfHGlnUyyuED4XIicnQfnlcxiaX16VkfIuiaxHEWOK65Ub3hrltAhXCE9mkCSFgeibU/640?wx_fmt=png&from=appmsg)

**RAG（Retrieval Augmented Generation）**，翻译过来为**检索增强生成**。

**RAG 就是给 LLM 准备的一场“开卷考试”，而数据库就是那本供它随时查阅的资料书。**

### 为什么需要RAG？

模型在预训练阶段（Pre-training）确实背下了海量知识，但它有两个致命弱点：

* **知识断层：** 它不知道训练截止日期之后发生的事（比如昨天的安全漏洞、刚发布的论文）。
* **幻觉风险：** 当它记不清细节时，会为了“预测下一个 token”而一本正经地胡说八道。

**RAG 的逻辑是：** 不要让模型死记硬背，而是当用户提问时，先去数据库里把相关的“知识碎片”找出来，塞进上下文（Context）里，让模型看着这些资料来回答。

### 核心组件：向量数据库

在 RAG 流程中，传统的关键词数据库（比如搜“苹果”只能找到“苹果”）不够聪明。

我们通常使用**向量数据库**，它的严谨定义是：**将非结构化数据转化为高维向量并进行相似度检索的系统。**

通俗来说，它做了两件事：

1. **特征提取（Embedding）：** 把每一段文字（比如一段代码、一个漏洞描述）变成一串数字（坐标）。意思相近的内容，在多维空间里的坐标就离得近。
2. **语义搜索：** 当你问“如何修复缓冲区溢出”时，即使数据库里的文档用的是“Memory safety context”，向量数据库也能感知到它们在语义上的关联，从而把它捞出来。

### 工作原理

RAG分为三个阶段：

* **Retrieve（检索）：** 根据用户的问题，去向量数据库里“捞”出最相关的 Top-K 条文档片段。
* **Augment（增强）：** 把捞出来的这些“干货”和用户原始的问题、提示词（Prompt）拼在一起。

  ```
  新上下文 = 提示词 + 检索到的背景知识 + 用户问题。
  ```
* **Generate（生成）：** 模型读完这段变长了的上下文，吐出最终答案。

回到我们之前的结论：**任何 AI 框架都是在管理上下文。**

RAG 框架（如 LangChain、LlamaIndex）本质上是一套**“自动化搬运工”**：它们根据用户的问题，动态地从海量数据库中筛选出最精准的信息，精确地投喂到 LLM 的上下文窗口里。

## Function Calling：让AI使用工具

### 简介

![image-20260316103055138](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibjsXH4m1EA7FmtjYXInNL22cFwNu3OpiazCLZpVaserSzmhj74Jm8wvw8qgbM9hqVBMvqGcneLQVvicFrmA20XIQWgPUZibNHiaf5E/640?wx_fmt=png&from=appmsg)

如果说 **RAG** 是给 AI 准备了一本可以随时翻阅的**“参考书”**，那么 **Function Calling（函数调用）** 就是给 AI 装上了可以操作世界的**“双手”**。

### 为什么需要Function Calling？

LLM 虽然博学，但它本质上是一个**封闭系统**，存在天然局限：

* **无法获取实时数据：** 它不知道现在的天气、最新的股价，或者你公司内网的数据库。
* **逻辑计算不精确：** 让它算复杂的数学或进行精确的逻辑推导，容易出错。
* **无法改变物理世界：** 它自己不能下单订票、发邮件或关闭一个服务器端口。

**Function Calling 的本质是：** 让 LLM 具备“调用外部 API”的能力，把复杂任务交给专业的程序去处理，自己只负责逻辑调度。

### 工作原理

LLM 并不运行任何函数，它只负责产生**意图**。

整个过程分为四步，依然是在管理上下文：

1. **定义工具（Schema）：** 你在 Prompt 里告诉模型：“我这儿有一个工具叫 `get_weather`，它需要一个参数 `city`。”这部分定义会作为**上下文**的一部分喂给模型。
2. **识别意图（Output JSON）：** 当用户问“北京天气怎么样？”时，模型意识到它需要用工具。它不会直接回答天气，而是输出一段**结构化文本（通常是 JSON）**，比如：`{ "function": "get_weather", "args": {"city": "Beijing"} }`。
3. **外部执行（The Action）：** 你的后端程序拦截到这段 JSON，去跑真正的 Python 代码或调用天气 API，拿到结果（如：“晴天，25度”）。
4. **结果反馈（Feedback Loop）：** 程序把这个结果重新塞回**上下文**，告诉模型：“工具返回的结果是：晴天，25度。”模型读到这段新信息，再组织成自然语言回复用户。

**最终上下文 = 用户问题 + 提示词 + 工具调用结果（Execution Result）**

AI 系统通过多轮对话（Multi-turn Chat），动态地将工具执行的反馈信息“塞进”上下文窗口。模型看到的结果越多，它的判断就越准确。

## MCP

### 简介

![image-20260316103228000](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibhlibf0ic7nnspnaPZ6DNf9myySSC9uXhNgiafmO93ib2VjCccEe64TwqVBXaq64B8HSzQIiaOvIkzWcibu6AYricLboVqJhBu2XOsyGs/640?wx_fmt=png&from=appmsg)

**MCP（模型上下文协议）** 是由 Anthropic 提出的一种开放标准。

它的核心逻辑是：**将“工具提供方”与“模型接入方”解耦。**

在 MCP 的架构中，存在三方角色：

* **MCP Server（工具端）：** 负责把你的本地文件、数据库、或 API 封装好，并按照 MCP 标准吐出接口。
* **MCP Host（宿主/客户端）：** 比如 Claude Desktop 或 IDE 中的 agent助手。
* **LLM（大脑）：** 它通过 Host 看到这些工具。

### 为什么需要MCP？

在理解了 **Function Calling** 是如何让 AI “动手干活”之后，你可能会发现一个痛点：如果我有 100 个工具（GitHub、Slack、Google Drive、CodeQL），难道我要为每一个模型、每一个项目都手动写一遍那复杂的 JSON Schema 吗？

这就是 **MCP (Model Context Protocol)** 诞生的背景。

MCP 的出现标志着 AI 应用从“手工作坊式”的 Prompt Engineering，向“工业标准化”的连接器架构演进。它让上下文的获取不再依赖于繁琐的胶水代码，而是通过协议实现自动化的语义发现与交互。

### 工作原理

1. 初始化与发现 (Discovery)

   当你启动支持 MCP 的 Host 时，它会连接到指定的 Server。

   **Host 问**：你都能干什么？

   **Server 答**：我有这 3 个\*\*资源 (Resources)**（比如本地文档）、5 个**工具 (Tools)**（比如搜索代码函数）和 2 个**提示词模板 (Prompts)\*\*。
2. 上下文注入 (Contextualization)

   Host 将这些“能力清单”转化为模型能理解的格式，塞进 **LLM 的上下文**里。

   **模型感知**：模型现在知道，它面前摆着一排可以按下的按钮。
3. 产生意图 (Tool Call)

   用户问：“分析一下这个项目的 CVE-2023-38545 漏洞。”

   **模型决策**：模型发现自己没看过这个项目代码，于是发出一个指令：“我要调用 `read_local_repo` 工具，参数是 `path/to/project`。”
4. 安全执行与反馈 (Execution Loop)

   **Host 转发**：Host 收到模型的 JSON 指令，转发给 MCP Server。

   **Server 执行**：Server 在本地执行读取动作，把代码内容返回给 Host。

   **闭环**：Host 把代码塞回上下文，模型读到代码，开始分析并给出最终答案。

### 与Function Calling的区别

Function Calling是让LLM输出调用意图，然后由后端代码手动调用并将返回结果扔给LLM。

MCP引入了MCP Server，让LLM自动发现并调用工具返回结果。

## Agent

### 简介

![image-20260316103436179](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibhkx0W4FwNzqropbibWibibOM5h9oExVKibj1FDNjBzkAkSQ3ZDHykxXPwbYKiaSEcMlISejSj2nz70VIA2EMr5kv64T76RtIt8aqAQ/640?wx_fmt=png&from=appmsg)

在理解了 **LLM (大脑)**、**RAG (知识)**、**Function Calling/MCP (工具接口)** 之后，我们终于来到了 AI 系统的最高级形态：**AI Agent（智能体）**。

如果把之前的组件比作零件，那么 Agent 就是一台能够自主运行的**机器人**。

我们可以用一个极简的公式来定义它：

> ❝
>
> **Agent = LLM + 工具 (Tools) + 循环 (Loop)**

### 常见形态

根据运行环境的不同，Agent 目前主要有三种存在形态：

1. CLI Agent (命令行智能体)

* **代表作：****Claude Code CLI**
* **特点：** 运行在终端。它能直接查看你的代码仓库、运行测试用例、自动修复 Bug 并提交 Git。
* **场景：** 适合重度开发者，直接在生产环境中进行端到端的开发任务。

2. IDE Agent (集成开发环境智能体)

* **代表作：****Cursor**、**Windsurf**
* **特点：** 深度集成在编辑器中。它不仅能写代码，还能理解整个项目的结构，在你改动一处代码时，自动建议并修改相关的其他文件。
* **场景：** 辅助编程，实现“人机结对编程”的最佳体验。

3. 桌面助手 (Desktop/OS Agent)

* **代表作：****Clawdbot**、**Computer Use (Anthropic)**
* **特点：** 运行在操作系统层面。它能像人一样“看”屏幕、挪动鼠标、敲击键盘，跨应用操作（如：从 Excel 提取数据，然后去网页查资料，最后发邮件汇报）。
* **场景：** 自动化繁琐的日常办公流程。

### 工作原理

Agent 的工作本质上是一个闭环的**自适应过程**：

1. \*\*思考 (Thought)\*\*：LLM 分析目标，决定下一步做什么。
2. \*\*行动 (Action)\*\*：根据思考结果，调用工具（如执行一段代码、搜索一个漏洞库）。
3. \*\*观察 (Observation)\*\*：获取工具执行后的反馈（如代码运行报错、搜到了关键信息）。
4. **更新上下文 (Update Context)**：**（这是最关键的一步！）** Agent 将观察到的新信息塞回上下文，开始下一轮“思考”。

**本质洞察：** Agent 其实是一个**“自动化的上下文管理器”**。它通过循环，不断地根据外部反馈来精细化、补全自己的上下文，直到解决问题。

## SKill

### 简介

![image-20260316103754576](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibhR5ck48icy9fhlhS9jRRDBS9dGJWiaL95fhq1oagiamMhaF92GgMN4E2PfZWGhqwPWJUN3GGITDVnu4kicT4t0ROoSQy7tZlFHHUM/640?wx_fmt=png&from=appmsg)

在理解了 Function Calling 和 MCP (连接工具和数据的接口) 之后，我们继续介绍一个新概念`Skill`。

Skill其实是**新瓶装旧酒**的新名词营销，它只是实现提示词精简、工具按需加载的规范。

### 工作原理

传统的`Function Calling`调用：

```
traditional_system = """
你是一个助手。可用工具：
- read_pdf: 读取PDF文件
- parse_pdf: 解析PDF结构
- extract_pdf_text: 提取PDF文本
- analyze_pdf: 分析PDF内容
- convert_pdf: 转换PDF格式
- merge_pdf: 合并PDF文件
- split_pdf: 拆分PDF文件
- encrypt_pdf: 加密PDF文件
- decrypt_pdf: 解密PDF文件
- add_watermark: 添加水印
... (20+ PDF相关工具)
"""
```

`Skill`调用：

```
skill_system = """
你是一个助手。可用技能：
- pdf: 处理PDF文件的综合技能
- code_review: 代码审查技能
- data_analysis: 数据分析技能

提示：需要特定技能时，先用load_skill加载完整指南。
"""
```

当LLM想调用pdf相关工具时，它会先通过`load_skill`工具查询pdf技能的详细信息，如：

```
SKILLS = {
    "pdf": """
【PDF处理完整指南】

可用操作：
1. 读取PDF：使用 read_file 读取PDF二进制内容
2. 提取文本：用 pypdf2 或 pdfplumber 提取
   示例：import PyPDF2; reader = PyPDF2.PdfReader("file.pdf")
3. 解析结构：获取目录、书签、页面大小等
4. ...