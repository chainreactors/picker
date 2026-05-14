---
title: 4. MCP协议基础与Server开发
url: https://mp.weixin.qq.com/s/0DKFAXsUyaPdc5NeD__yIg
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:41:49.036821
---

# 4. MCP协议基础与Server开发

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4bKA2FWJIkZia7ibAm19lrT57HmVtoD3Gr82LQ1N0hvnOuG2rlJx3wUsjWcFwqkDcnnbmF5vjiabLajbNoD1k81U3tqfJdEZGlbys/0?wx_fmt=jpeg)

# 4. MCP协议基础与Server开发

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

完整docx文件关注公众号回复：从零构建AI驱动的二进制安全系统

在第三章中，你已经学会了如何通过Function Calling让Agent调用外部工具，并在命令行中实现了一个具备基础工具能力的Agent。但那种模式有一个根本性局限：工具的定义、注册和执行都发生在同一个代码库中，Agent和工具之间是**代码级耦合**。当你需要让不同的Agent共享同一套工具，或者想让工具运行在不同的进程甚至不同的机器上时，这种模式就显得力不从心。

这正是MCP（Model Context Protocol，模型上下文协议）要解决的核心问题。MCP将工具从Agent的代码中解耦出来，使其成为独立的、可通过标准协议发现的服务。想象你走进一个图书馆：Function Calling就像是你自带了一箱子书（工具定义嵌在代码里），而MCP则是图书馆本身的检索系统——你只需要知道如何查询，就能找到馆内的任何一本书（动态发现），而且新书不断上架而不需要你重新编译你的程序1^。

在本章中，你将深入理解MCP协议的设计哲学，掌握其核心原语，并最终实现一个**二进制分析MCP Server**——一个能够暴露反汇编、字符串提取、文件信息分析等能力的独立服务。这个Server将通过stdio模式运行，任何兼容MCP的客户端（包括Claude Desktop、Cursor、或你将在第五章中构建的MCP Client）都可以动态发现并调用它的能力。

---

## 4.1 MCP协议概述

### 4.1.1 MCP是什么：协议定义、发起方与设计目标

**MCP（Model Context Protocol，模型上下文协议）** 是一个开放的、标准化的应用层协议，用于连接AI模型与外部数据源和工具2^。它由**Anthropic**于2024年11月首次提出并开源， rapidly evolving into an open industry standard backed by major technology companies including Microsoft、Google、AWS、Cloudflare、Figma和Stripe3^。截至2025年中期，社区已经发布了超过10,000个共享MCP Server4^。这些Server覆盖了从文件系统操作、数据库查询、API集成到专业领域工具（如生物信息学分析、金融数据获取、网络安全扫描）的广泛场景。MCP的快速增长反映了行业对标准化AI工具集成协议的迫切需求——每个团队都不想重复造轮子，而MCP提供了一个"一次编写，到处使用"的解决方案。

MCP的设计目标可以用五个关键词来概括：

**标准化（Standardization）**。MCP消除了每个AI应用重复编写工具集成代码的需求。在没有MCP之前，如果你想让Agent调用Slack API、查询GitHub Issues、读取本地文件，你需要为每个工具编写自定义的适配层——80%的AI Agent开发时间都花在了这种"管道工程"上5^。MCP通过统一协议让工具只需集成一次，就能被任何兼容客户端使用。这种标准化带来的效益是巨大的：一个团队开发的文件系统MCP Server可以立即被使用Claude Desktop、Cursor IDE或自研Agent的其他团队使用，无需任何代码修改。

**解耦（Decoupling）**。工具的实现细节（用什么语言编写、运行在哪个进程、使用什么认证凭证）与工具的消费方（Agent或LLM客户端）完全分离。工具提供者发布一个MCP Server，工具消费者通过MCP Client连接——两者通过标准协议通信，互不关心对方的内部实现。这种解耦使得工具可以独立开发、独立部署、独立更新。你的二进制分析团队可以用Python开发分析引擎，而Agent开发团队用TypeScript构建Client——两者通过MCP协议无缝对接。

**可插拔（Pluggability）**。MCP常被比喻为"AI的USB-C接口"6^。就像USB-C统一了充电和数据传输标准一样，MCP统一了AI工具与模型之间的通信标准。你可以随时插拔新的工具，而不需要修改Agent的代码。当你需要为Agent添加数据库查询能力时，只需让Client连接一个数据库MCP Server即可，Agent本身的代码完全不需要改动。

**安全隔离（Security Isolation）**。每个MCP Server运行在独立的进程中，凭证隔离在Server级别而非应用级别。这意味着Agent不需要直接访问你的GitHub Token或数据库密码——这些敏感信息只保存在对应的MCP Server中7^。此外，Host层可以实施细粒度的访问控制策略，决定哪些Client可以连接哪些Server，哪些操作需要用户确认。这种多层安全模型使得MCP特别适合企业级部署。

**跨模型兼容（Model Agnostic）**。MCP不绑定特定的LLM提供商。无论是Claude、GPT、Gemini还是本地运行的Llama，只要客户端实现了MCP协议，就能使用任何MCP Server暴露的工具8^。这种模型无关性保护了你在工具集成上的投资——即使未来更换了底层LLM，所有的MCP Server和工具集成都可以直接复用。

### 4.1.2 MCP与Function Calling的区别

理解了MCP是什么之后，一个自然的问题是：MCP和第三章学到的Function Calling是什么关系？它们是竞争关系还是互补关系？

答案是：**互补关系**。MCP和Function Calling位于AI工具调用栈的不同层次，各自解决不同的问题9^。

**Function Calling是模型API的特性**，属于工具调用的"第一阶段"——意图生成。当LLM决定需要调用某个工具时，它会输出一个包含工具名称和参数的JSON对象。但Function Calling本身并不规定：工具定义存储在哪里、工具由谁来执行、执行环境如何管理、多个工具如何共享。这些都是应用层需要解决的问题。

**MCP是应用层协议**，属于工具调用的"第二阶段"——标准化执行。它规定了一套完整的通信协议，让工具的发现、调用和执行可以在不同进程、不同语言、不同机器之间标准化进行10^。

以下对比表清晰地展示了两者的核心差异：

| 对比维度 | Function Calling（传统模式） | MCP（Model Context Protocol） |
| --- | --- | --- |
| **协议层级** | 模型API特性（意图生成层） | 应用层协议（执行标准化层） |
| **工具定义位置** | 嵌入每次API请求的`tools`数组中 | 在独立的MCP Server上定义，运行时动态发现 |
| **工具执行环境** | 应用代码内联执行，与Agent同进程 | MCP Server独立进程执行，进程级隔离 |
| **发现机制** | 手动硬编码，每次请求传递工具列表 | 自动动态发现，Client连接Server后获取工具列表 |
| **可移植性** | 模型特定格式（OpenAI、Anthropic格式不同） | 通用开放标准，跨模型兼容 |
| **状态管理** | 每次请求无状态，需重复传递上下文 | 持久化Server连接，维护会话状态 |
| **部署模式** | 内联代码，与Agent同进程部署 | 独立Server进程，可本地或远程部署 |
| **多客户端共享** | 不支持，需复制代码到每个客户端 | 原生支持，任何MCP客户端可连接 |
| **凭证隔离** | 应用级（all-or-nothing） | Server级（最小权限原则） |
| **语言限制** | 与Agent同语言 | 跨语言互操作，Server可用任何语言实现 |
| **生态规模** | 每个应用自定义 | 10,000+共享服务器 |

从架构角度看，Function Calling的完整循环是：

```
应用代码 → 定义工具Schema → 发送给LLM → LLM决定调用 →
应用执行函数 → 结果返回LLM → LLM生成最终响应
```

在这个循环中，所有环节——工具Schema定义、执行逻辑、错误处理、凭证管理——都发生在同一个应用进程中。当你的Agent需要调用50个不同的工具时，这些工具的代码、依赖和凭证都会堆积在你的主应用中。

MCP的Client-Server模型则完全不同：

```
AI应用(Host) → MCP Client → 连接到MCP Server →
Server暴露tools/resources/prompts → Client动态发现 →
LLM决定调用 → Client发送请求 → Server执行 → 结果返回
```

工具在独立进程中运行。AI应用通过MCP Client连接到各个Server，动态发现可用能力。当LLM决定调用某个工具时，Client将请求转发给对应的Server执行，执行结果再返回给LLM。

那么什么时候用Function Calling，什么时候用MCP？一个实用的判断标准是：

* **使用Function Calling**：工具数量少于5个、单一模型和单一应用、延迟敏感路径（每毫秒都重要）、快速原型开发阶段。如果你正在构建一个个人使用的天气查询Agent，只有两个工具（获取天气、搜索城市），Function Calling是最简单直接的选择。
* **使用MCP**：工具数量超过10个、多团队共享工具、多模型架构、需要生产级治理（认证、审计日志、访问控制）、构建工具生态11^。当你正在构建一个企业的AI助手平台，需要连接GitHub、Jira、Slack、内部数据库、文件系统等十几种工具时，MCP的解耦和标准化优势就会充分体现。

在实际项目中，推荐采用**混合架构**：对应用特有的、不需要共享的工具使用Function Calling内联实现；对通用的、多客户端共享的基础设施工具使用MCP Server暴露。例如，一个Agent可能通过Function Calling直接调用内部的业务逻辑API，同时通过MCP Server连接文件系统操作工具、代码搜索工具和外部API。这种分层方法在保持简单性的同时获得了MCP生态的复用优势。

### 4.1.3 MCP架构模型：Client-Host-Server三层架构

MCP采用**Client-Host-Server三层架构模型**，这是理解MCP通信流程的基础12^。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YUcEZzSFgC1v2PiaG3ELZVqwxQJDZuRIpeaLA30APNRzEsZS8onx6ib4dD9IPToVvN0Pic1w8vgBic4hq4lpFbMJzBeq9EIRFnMEE/640?wx_fmt=png&from=appmsg)

Host（宿主）是MCP架构中的顶层容器。它通常是你直接与之交互的AI应用程序——比如Claude Desktop、Cursor IDE、或你自己开发的AI应用。Host的职责包括：创建和管理多个Client实例、控制Client的连接权限和生命周期、强制执行安全策略和同意要求、处理用户授权决策、协调LLM集成和上下文聚合13^。

**Client（客户端）**由Host创建，每个Client维护与单个Server之间的隔离连接。Client的核心职责是：为每个Server建立有状态的会话、处理协议协商和能力交换、双向路由协议消息、管理订阅和通知、维护Server之间的安全边界。关键点：**Host应用创建和管理多个Client，每个Client与特定Server保持1:1关系**14^。

**Server（服务端）**通过MCP原语向客户端暴露资源、工具和提示模板。每个Server独立运行，职责聚焦，可以是本地进程（通过stdio通信）或远程服务（通过HTTP通信）。Server还可以向Client请求采样（Sampling），即在需要时"使用"LLM的能力15^。

MCP的会话生命周期分为三个阶段：

**初始化阶段（Initialization）**。Client发送`initialize`请求，包含支持的协议版本（如`2025-03-26`）和声明的能力（如`sampling`、`roots`）。Server响应匹配的协议版本和自身能力（如`prompts`、`tools`、`resources`）。双方完成能力协商后，Client发送`initialized`通知确认就绪。只有在初始化完成后，有意义的操作才能开始16^。

初始化阶段的设计体现了MCP协议的前向兼容性哲学。协议版本遵循`YYYY-MM-DD`的日期格式，每次规范更新都会修改版本号。当Client和Server的版本不一致时，双方选择都支持的最新版本进行通信。这意味着2025年6月的Client可以连接2024年11月的Server，只要两者在核心协议上兼容。能力协商（Capability Negotiation）则进一步细化了兼容性——Client声明自己支持的功能（如能否处理Server发起的采样请求），Server声明自己提供的功能（如暴露了哪些原语），双方只在交集范围内操作。

**操作阶段（Operation）**。Client和Server根据协商的能力交换请求、通知和响应。Client可以调用`tools/list`发现Server的工具列表，调用`tools/call`执行工具，调用`resources/read`读取资源，调用`prompts/get`获取提示模板。如果协商了采样能力，Server也可以主动发起`sampling/createMessage`请求来使用LLM17^。

**关闭阶段（Shutdown）**。Client或Server可以随时关闭底层传输连接，无需特定的协议消息。建议实现超时机制和健壮的错误处理，确保资源正确释放。

### 4.1.4 MCP核心原语：Resources、Tools、Prompts、Sampling

MCP定义了四个核心原语（Primitives），它们是Server向LLM客户端暴露能力的统一接口18^。理解这些原语的性质和用途，是设计MCP Server的关键。

**Tools（工具）**——主动执行原语。Tools是LLM可以调用的函数或服务，用于执行外部操作。它们的性质是**主动的（Active）**：模型决定何时调用。类比来说，Tools就像公司中的服务工作者——快递员、客服代理、支付系统。当你需要发送包裹时，你主动呼叫快递员；当你需要查询天气时，Agent主动调用天气API。

每个Tool包含三个要素：唯一标识的名称、描述输入参数的JSON Schema、执行实际逻辑的处理函数。Tool的调用数据流是：Client发送请求 → Server执行 → 返回结果。2025年3月的规范新增了Tool注解（Annotations），允许标注工具的行为特征，如`readOnlyHint`（只读操作）、`destructiveHint`（破坏性操作）、`idempotentHint`（幂等）、`openWorldHint`（可能访问外部世界）19^。这些注解帮助LLM更智能地选择工具。

**Resources（资源）**——被动读取原语。Resources是AI模型可以访问的只读数据源，用于获取上下文信息。它们的性质是**被动的（Passive）**：模型可以读取但不需要触发函数调用。类比来说，Resources就像图书馆中的书籍——你可以随时翻阅获取信息。

Resource通过URI寻址（如`file:///config.json`、`db://users/123`、`weather://cities`），Server在注册时声明支持的URI模式和MIME类型。Client通过`resources/read`方法读取资源内容20^。

**Prompts（提示模板）**——标准化交互原语。Prompts是可复用的交互模板，Server可以预定义标准化的交互方式。它们的性质是**模板化的（Template）**：参数化的消息序列。类比来说，Prompts就像客户服务脚本或标准化操作流程——它们确保每次交互的一致性和质量。

Prompts的独特之处在于，Server既了解数据（Resources的内容），也了解让模型处理数据的最佳方式（Prompt的设计）。因此，Prompts可以组合Resources和Tools来创建动态工作流21^。

**Sampling（采样）**——LLM能力委托原语。Sampling是MCP中最独特的原语。它允许Server通过Client请求LLM进行推理——换句话说，Server可以在需要时"使用"LLM的能力。工作机制是：Server发送`sampling/createMessage`请求 → Client转发给LLM → LLM响应 → Client返回结果22^。

Sampling的安全性设计非常重要：Host可以审核、修改或拒绝任何采样请求，控制使用的模型和token限制。这使得Server能够在安全约束下利用LLM的能力进行复杂推理，比如递归分析Agent工作流或工具链中的LLM调用23^。

这四个原语的组合创造了强大的动态工作流能力。例如，一个日志分析Server可以这样工作：首先暴露一个分析日志的Prompt模板，当用户选择该Prompt后，Server调用Sampling让LLM分析日志内容，LLM返回"日志显示重复认证失败，建议检查OAuth配置"，然后Server调用Tool`check_auth_config`来验证OAuth配置，最后LLM审查验证结果并生成总结24^。这种Prompt驱动的Agentic工作流是MCP区别于简单工具调用的核心特征——Server不仅是被动的工具提供者，更是能够主动编排LLM能力的工作流引擎。

理解这四个原语的关系，可以用一个类比：想象你是一位厨师（LLM），Resources是你冰箱里的食材（只读数据），Tools是你的厨具（可执行操作），Prompts是菜谱（标准化流程），Sampling是你在烹饪过程中品尝味道并根据...