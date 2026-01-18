---
title: AI软件工程实践：构建企业级Agentic SOC平台
url: https://mp.weixin.qq.com/s/c5jl82qwRyktYCl3vasG_g
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:36:25.412411
---

# AI软件工程实践：构建企业级Agentic SOC平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvlFOVaKhdYNaQ9vWWZpmy7VlNDYjK0O9lyibOftpFWYncrrU41ic5qib4w/0?wx_fmt=jpeg)

# AI软件工程实践：构建企业级Agentic SOC平台

原创

放之
放之

放之

![]()

在小说阅读器中沉浸阅读

> 在刚刚过去的一期项目中，我们消耗了约23亿Token，使用Cursor Ultra与Claude Code构建了一个企业级 Agentic SOC平台。本文从软件工程的角度，复盘如何通过架构约束、测试驱动与文档管理，驾驭AI完成从35万行生成代码到8万行核心代码的提炼。

# 0x00 前言

2025年底，Agentic SOC 平台的一期开发终于快要收官。回顾这两个月，我最大的感受不是在和智能体（Agent）对话，而是在和美元（$）对话。即便使用了Cursor Ultra会员和Claude Code的代理，Token消耗依然惊人。粗略测算下来，项目初期构建框架时，代码成本高达3-5元/行；后期功能实现阶段降至0.5元/行；而文档编写成本约为0.1元/行。好处就是某些特性原本可能是需要数月的开发，通过AI Coding可以压缩至一两周。这笔昂贵的学费教会了我一个道理：AI编程可以使10倍工程师进化为100倍，也能让1倍工程师退化为0.5倍。区别在于你是在用软件工程鞭策AI，还是被AI产生的数据所左右。

本篇就结合近期实践和总结，介绍一下如何有效鞭策AI完成大型项目的设计及落地。

# 0x01 Agentic SOC案例介绍

> 懂业务才能做出好产品：真正懂得安全的人更能做出优秀的安全产品。

通过为Agent设置增强的Prompt，引入RAG的知识库，并读取企业资产列表（作为授权的一部分）同时使用特定的MCP Tools来实现以**Model As Agent，Agent As Engineer**为设计理念的Agentic SOC平台。传统的自动化是**系统执行任务，人工分析结果**，而Agentic SOC旨在实现**AI执行系统任务，AI分析结果**。在这个设计理念里，Agent不再是简单的聊天机器人，而是被赋予了具体职能的虚拟工程师：换句话说，Agent就是SOC Engineer，就是告警分析师，应急响应专家，报告分析师，就是潜在的从L1-L3线的每个角色。除此之外，还可以是架构评审专家，解决方案专家等。不同的Agent共同构成了一个虚拟SOC团队用来处理日常任务。

一期的设计实现过程中，依旧是遵循传统的Agent对话的形式，用来完成日常任务的处理。输入层统一收敛至AgentRunner实现调度，通过判断任务复杂实现不同的对话模式（Direct/ReAct/Workflow）。针对任务的处理，以及Agent的记忆管理，MCP的执行等等细节也不在此赘述。不过有时虽然引入了所谓新的设计，但实际效果可能反而大打折扣。例如在开启ReAct模式之后，Agent反而在思考/观察/执行的过程中开始持续放大幻觉。所以也要注意，在AI类的产品使用中，无论是代码实现，还是用于对话处理其他任务，都一定要优先选择聪明好用的模型。**优先选择聪明好用的模型（如Gemini 3 Pro, Claude 4.5 Sonnet）比复杂的Prompt工程更重要**。

先看一下其在不同场景的实现：

* 直接在聊天中进行代码审计
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvttacXo1RKD4CKSVnhTnj2C8kd4TGibdBicpY6MwK9LGsmvRWeYPodDNA/640?wx_fmt=png&from=appmsg)
* 进行源代码扫描并生成报告
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRv6SAx8zVlkHMAibonN2icuPiaBUSj3cXwC2tpeMVNI9hP6TsxxSyWBQy4A/640?wx_fmt=png&from=appmsg)
* 查询威胁情报
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvM09RCxnuOjzmNZFqVlhqlczicqFRtFS6E8vZMnDHiczhhjV6icuT6Hg1g/640?wx_fmt=png&from=appmsg)
* 知识库功能
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvCynsTkvlMETJWTe77FKJcsUiaPznibTh9JHHvx5VTcztzA9KHbFXZN8g/640?wx_fmt=png&from=appmsg)
* 敏感信息泄漏检测
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRviaU6IFVdxiaVa6zSVzhfiaY6lWN3HWukNf4SNibTLvkZyk7YDrhaKbs6cg/640?wx_fmt=png&from=appmsg)
* 工作流调度执行
  ![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvYepMbRbHIA7qibKPWpMYXQLG44u4iclLTAqZcaXKGiantON00hfr113GA/640?wx_fmt=png&from=appmsg)

# 0x02 从Vibe Coding到构建企业级SOC平台的软件工程实战

使用AI Coding仍需要懂得软件工程，懂得使用AI的人才不会被AI取代。然而从需求到产品的过程中，最重要的不是代码功底实现，也不是对AI编程工具的使用。而是能够理解自己的业务场景，并且知道能如何转换为平台产品。人人都是产品经理到人人都是全栈工程师的转变，恰恰需要对软件工程深入的了解。一个人配合AI是如何从产品架构设计到UI分区的解耦，从前端API路由再到后端的逻辑实现。如何管理实现自己的AI项目等等。另外因为主要关注在AI软件工程的实践，整体将按照**架构设计-编程实现-测试-文档以及常见问题**的流程去介绍相关内容。

## 1. 架构：从需求到产品

> 架构设计是一种平衡的艺术：AI可以辅助设计和平衡；但前提使用者要有判断的能力；

在对产品的架构设计，其实应该要拒绝Vibe Coding。先不用急着反驳，这并不是否认Vibe Coding的优势，而是说应该在合适的地方使用Vibe Coding，在后续章节也可以看到大量关于Vibe Coding的经验介绍。回到关于产品本身的架构设计，更多的是需要对业务需求本身的深刻理解以及差距分析，当然我在最初也使用了Gemini的Deep Research做了可行性分析。 而到技术架构层面，则需要能够选择合适的技术栈，尤其是要和企业内部的技术栈相结合。AI是可以帮助评估技术栈的优劣，但前提更需要使用者拥有对应的判断能力。千万不要陷入模型的花式马屁之中。

![](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvumNElk0TTScYFPT4VAicicib4tCwFicyF9ibPLduQPPZ8TKtgu21iaaGeFuQ/640?wx_fmt=png&from=appmsg)

以上图Agentic SOC Architecutre为例，其实并没有使用过多的AI辅助（当然最初画的也不是这样的），基本都是纸上写写画画，包括UI布局，技术栈，功能模块等。之后逐步添加对应的功能模块。从经验上看通过分层架构的形式逐步迭代产品的功能（这要求设计之初具备可扩展性）并使用领域驱动架构的设计方法论是完全可行的。以下是一些使用AI在架构设计方面的经验之谈：

* 在整体架构设计阶段推荐使用`Gemini 3 Pro`做可行性分析（Deep Research），并选择`Opus4.5`做组件/领域细化，不建议直接开始编程实现；
* 领域驱动架构设计：可以通过细分到每个领域来实现具体框架内的代码：比如代理领域->执行和推理、验证领域->反幻觉、知识领域->RAG和文档、工具领域->调用执行等；
* 架构设计结束之后，会意味着有多个方向的特征需要编程实现，可以使用 Opus 完成Phase拆分，并记录成文档。要把文档作为模型的“记忆库”，通过组织文档目录结构，记录文档状态（状态跟踪表）以便实现丝滑的代码实现。详细参考文档章节 ；

对于文档和绘图相关（要把架构设计相关的文档经常丢给AI检查，是否实现逻辑一致，有无GAP并进行分析等，即时刻关注编程实现过程中的架构review）：

* 使用`Mermaid`比`Plantuml`的效果更好一些，但是注意Gemini生成的`Mermaid`的语法错误次数要比Opus高很多；
* 对汇报的架构图的绘制，则可以通过使用Gemini对Mermaid架构图的描述之后丢给AI实现，效果还是非常符合技术范的：参考此处。甚至需要各种高大上的奇怪图也是可以的。

另附上一些常见的Prompt针对后续类似场景（已经有了架构，在架构里面填充内容，或者是分析实现及差距）：

| Task | Prompt Pattern |
| --- | --- |
| New Feature | “Design [feature] following the domain pattern in COMPLETE\_ARCHITECTURE.md” |
| Gap Analysis | “What’s missing from Phase X? Suggest implementation” |
| Integration | “How should [new component] integrate with [existing domain]?” |
| Refactor | “Refactor [component] to match the layered anti-hallucination pattern” |
| Review | “Review this architecture for security/scalability issues” |

最后如果你完全不懂架构设计，那就尽可能的把需求描述给AI吧，多对比不同AI模型的Research结果和架构推荐。毕竟产品之初，Idea反而并不是那么重要，更在乎的是谁先行动。

## 2. 编程：意图即代码

> 软件工程驱动AI编程：AI编程可以使10倍工程师变成100倍工程师，也可以使1倍工程师变成0.5倍工程师。

我在小红书上看到一个Gemini制作手势交互的粒子教程，其中博主讲了一个很重要的点，就是有一句提示词用来避免AI使用React，而是使用单个的Html文件。这在早期进行demo非常有效，作为玩具来说也无可厚非。但是在真正的产品设计和实现里显然是无法满足业务需求的。那么问题来了？AI懂技术栈，你懂吗？AI可以帮你选型技术栈，你吗？能够review代码，能够判断技术栈的合理程度吗？AI编程可以使10倍工程师变成100倍工程师，也可以使1倍工程师变成0.5倍工程师。那些非常头疼于Vibe Coding 10分钟，调试三天的就属于这种情况。

### 2.1 编程的一些技巧

1. 使用Gemini3 Pro编写框架代码，完成初期架构的实现；
2. 使用Opus 4.5进行具体的功能实现，例如多个MCP Server的编写，调度任务的优化。之后使用Gemini3 Pro去Review架构设计和具体的功能实现。判断优化的点；
3. 每次实现一个独立的feature，或者是功能相关联的feature实现；当你不确定feature设计是否完善时，可以指定先用Agent模式生成文档；
4. 使用独立的Agent对话，用Gemini3 Pro去修复backend error以及frontend的error；
5. 确保编写Test Case以及Document，需要**Trust but Verify**
6. 测试案例通过后，手工Review这个独立Feature的代码实现以及文档是不是可行的，有没有导致意外修改；
7. 进行Commit提交；重复以上步骤；

### 2.2 功能设计的一些技巧

1. 初期的UI界面设计会面临多次的调试。因为框架没有被填充完整之前，会被AI出现意外发挥。需要在样式固定完之前，多次检查前端的页面交互逻辑；关于产品设计的前端相关，可以访问此处Product Design Learning Hub，里面有介绍常见布局，样式，行为，框架等知识。
2. 即便是为了完成最快的原型MVP，也要使用可迁移的接口，这种实现看似成本较高，实则更便于后续的迁移。例如使用ORM框架，MVP时用Sqlite，之后migrate到Pg；（人眼中的成本更高实际对于AI实现而言，有时候差别并不大）
3. 在引入新的组件时一定要先阅读分析，判断新的组件的可行性。例如使用Qdrant还是Milvus，低估了Milvus搭建的复杂度，SDK的差劲之后，就会耗费大量的精力在AI重复修复代码上；
4. 复杂的功能组件在前后端实现之前，记得再读读SOLID五大原则：单一职责（SRP）、开闭（OCP）、里氏替换（LSP）、接口隔离（ISP）和 依赖反转（DIP），不能完全依赖AI帮你进行平衡设计；

### 2.3 Curosr 使用的一些技巧

* Curosr会自动忽略Gitignore内的文件不被index到Vector store；
* 如果某些时候，你开了很多个Agent之后，发现内容不同步了。记得进入cursor settings-> Indexing & Docs, 手动Sync, 或者Delete Index 重来；
* 点击Agent对话框里的Brower Tab，使用选取框直接勾选对应的样式，代入对应的代码进入对话框。尤其是你需要A元素去遵循B元素的样式和布局时非常好用。比直接文字描述使A和B一样时更有效；
* 如果一次实现了多个Feature（不建议，参考前面的编程技巧），但也记不清是啥了，记得新开一个窗口问一下Agent。

### 2.4 Claude使用的一些技巧

* Claude Code的CLI里模型只有200K窗口，所以`CLAUDE.md`千万不要太大；我之前迁移Cursor Rule到CLAUDE规则时写了大概990行的Rule，效果不差，但是浪费Context，auto-compact次数增加。不如移动到独立的rules里面。
  `.claude`的目录结构

```
.claude
├── rules
│   ├── agents
│   │   └── agent-development.md
│   ├── backend
│   │   └── python-standards.md
│   ├── docs
│   │   └── documentation-standards.md
│   ├── frontend
│   │   └── typescript-standards.md
│   └── metabrain
│       └── metabrain-standards.md
└── settings.local.json

7 directories, 6 files
```

`.claude/rules/backend/python-standards.md`, 可以看到其只作用于后端代码

```
---
paths:
  - "backend/**/*.py"
  - "*.py"
---

# Python Backend Standards
```

* 如果你需要并行使用Claude CLI进行编程，可以在每个字文件夹建立对应的`CLAUDE.md`
* 如果使用三方代理商的Claude模型，注意使用的接口是否带缓存命中机制； 初期使用的三方代理不提供缓存命中也许提供，但是命中率为0，后期又突然能够命中。
* 在Cursor里安装ClaudeCode插件后通过在claude cli里使用`/ide` 命令能够连接到Cursor的IDE，然后通过`Super+Shift+ESC`在Cursor内打开界面
* 如果你使用较为便宜的代理商的模型，可以只用来整理文档，避免编写代码；

### 2.5 并行鞭策AI进行编程（结合Cursor和Claude）

`Agentic SOC`的目录结构

```
Agentic SOC
├── backend
│   ├── __pycache__
│   ├── core
│   ├── data
│   ├── features
│   ├── scripts
│   ├── tests
│   └── venv
├── docs
├── frontend
│   ├── dist
│   ├── node_modules
│   ├── public
│   ├── src
│   └── tests
├── Brain
├── nginx
└── scripts
    └── systemd
42 directories
```

我通常会开四个ClaudeCode CLI的窗口，一个Cursor的窗口。 Agentic SOC的CLI窗口和backend, frontend, brain三个CLI的窗口，然后每个都会建立独立的CLAUDE规则，方便快速的分别实现各个新功能的开发。同时使用Agentic SOC窗口进行全局文档的更新。不过后来发现backend的代码更新经常会触发到frontend的代码更新，而当前的frontend的cli窗口可能并不会主动的发现更新。于是便通过增加`sync-context` Skill的方式，在一个窗口鞭策完AI，如果另一个窗口归属的文档发生了变化就先执行一个`sync-context`的方式进行。 （`/compact` 和 `claude --resume`对于我来说用处不大，我一般会持续的开着窗口鞭策AI，很少有resume的情况）

下图一个周末的鞭策统计
![img](https://mmbiz.qpic.cn/mmbiz_png/rmc0P5ibISkB1jNXztTMKialDibXTcOgYRvv1PG9NBNoPanKS5yS6mLUcGibribr9hEg2DD18ymy50HBFibW...