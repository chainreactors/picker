---
title: 可控涌现：AVL Code 的工程范式（上） ——涌现不是魔法，而是系统属性
url: https://mp.weixin.qq.com/s/DkPkLMrR7ooyC2PRyR2I8g
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:41:35.924604
---

# 可控涌现：AVL Code 的工程范式（上） ——涌现不是魔法，而是系统属性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk8FP41ymuzahIXPIanquUwhBMh1PUvINgfk9wf9t7FQNRNbKn3DCZgGMdqMykNQEpFWltpMRZcfib6icuiasAkL3SkF7o2tqiblcco/0?wx_fmt=jpeg)

# 可控涌现：AVL Code 的工程范式（上） ——涌现不是魔法，而是系统属性

AVL Code小组
AVL Code小组

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

按语：2026 世界人工智能大会今日在上海开幕，习近平主席出席开幕式并发表主旨讲话。作为国内「人工智能 + 网络安全」的实践探索者，我们深受鼓舞。我们将研发运营 AVL Code 智能体与澜砥模型的心得整理成《可控涌现：AVL Code 的工程范式》，分三天连载——愿人工智能成为可托付的伙伴，与工程师们共创未来。

本文原载于安天AVL Code编程智能体技术blog，原文地址为：https://avlcode.cn/blog/controlled-emergence-1/

![可控涌现：AVL Code 的工程范式（上）——涌现不是魔法，而是系统属性](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkibylHqicamxniaaGwRRHdKt0iabdC4cib3eeEtLNoaW39csRtWibxzW6bibFmYvQXYjG5hRTWAB5G3yH92zdcWQ8oDHwcBmd9JFG1xxE/640?wx_fmt=other&from=appmsg)

> 本文是《可控涌现：AVL Code 的工程范式》系列的**上篇**，全系列分三天发布：上篇（本文，7 月 16 日）· 中篇《Harness 工程与 Loop 工程》（7 月 17 日）· 下篇《从理论到实践与七条工程原则》（7 月 18 日）。

当大语言模型进入代码仓库，获得 Context、Tool、权限和事实反馈后，它开始表现出单次文本生成所不具备的能力：读取工程、规划步骤、修改文件、运行测试，再根据错误继续修复。面对这种现象，真正值得讨论的不是“模型是否突然觉醒”，也不能用“不过是下一个 Token 预测”将其一笔抹平，而是三个更具体的问题：**这些新能力属于谁，如何产生，又怎样被约束为可验证、可停止、可交付的工程行为？**

答案首先取决于我们怎样划定系统边界。如果把研究对象从孤立的 LLM 扩大为完整的生成式 AI 系统，许多现象会清楚得多：模型生成候选内容，Context 提供当前条件，Tool 把符号输出变成外部行动，运行时组织循环，权限与测试约束行动边界，人在关键节点确认目标和风险。单看其中任何一个部分，都没有“自主完成软件工程任务”的能力；这些部分按特定结构连接后，系统整体却能表现出这种能力。

这正是“涌现”一词在系统工程中的正常含义。本系列的核心观点可以概括为：

1. **涌现是系统整体产生部分所不具备的新属性，不是伪科学，也不是对未知机制的神秘化命名；**
2. **LLM 与 Context、Tool、运行时结合后出现的是可观察、可测量的功能性行为涌现，不能据此直接推断认知、意识或主体性已经涌现；**
3. **生成式 AI 的工程对象不是裸模型，而是模型外部的 Harness（挽具、驾驭层）及其包围的完整系统；**
4. **Loop 工程把反馈、误差、状态、控制量和停止条件引入概率性 AI 系统，是控制工程思想在不可完全建模对象上的实践；**
5. **Claude Code、Codex 和 AVL Code 等 Agent 的工程价值，正在于把模型能力组织成一个有阶段、有工具、有反馈、有门禁、有预算、可恢复的 Harness。**

其中第 1、2 点是本篇（上篇）的内容；第 3、4 点在中篇展开；第 5 点在下篇落到 AVL Code 的具体机制上。

> 本系列中“功能性行为涌现”和“认知性智能涌现”是为澄清工程边界提出的工作性区分，不是 SEBoK 已有的术语分类。

![可控涌现：AVL Code 将 Context、Tool、Loop 与 V&V 组织成受控的 Agent Harness](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicwo2d4qyXvpSeiaC60MQ9k84Lyl7bicLbdxjEloekCbEquSrJWicVChSY7FCEvibBD7oIN7rCIuFRRvG4ibQAiaYlvdORHgJSNzhN30/640?wx_fmt=other&from=appmsg)

图 1：AVL Code Harness 将 Context、Tool、Loop 与 V&V 组织起来，使大量局部单元形成可验证的系统级行为。

## 一、涌现不是魔法，而是系统属性

SEBoK 的 Emergence 条目将涌现概括为：某些属性只有归属于整体时才有意义，而不是其组成部分各自拥有的属性；Emergent Property 术语表进一步强调，这类属性只有在系统组织的更高层次上才具有意义。系统级行为来自元素的属性、元素之间的关系、系统结构以及环境刺激的共同作用。

飞机的机翼不会独自“受控飞行”，发动机和控制系统也不会；当气动结构、推进、控制、传感器和驾驶操作以正确关系结合时，飞行才成为飞机整体的属性。同样，一次北美大停电不一定源于某个设备单点损坏，也可能由系统连接方式与运行条件共同触发级联失效。涌现既可能是设计者追求的能力，也可能是设计者必须抑制的风险。

因此，涌现并不是“无法解释，所以归因于神秘力量”。一个有工程意义的涌现命题，至少应回答五个问题：

| 问题 | 工程含义 |
| --- | --- |
| 系统边界是什么 | 被观察的是模型、Agent 运行时，还是包含人和组织流程的更大系统 |
| 组成部分是什么 | 模型、Context、Tool、状态、权限、测试、用户分别承担什么职责 |
| 关系是什么 | 信息和控制如何在部分之间流动，哪些关系形成反馈 |
| 新属性是什么 | 系统整体比单个部分多出了什么可观察、可测量的能力 |
| 在什么条件下出现 | 哪些任务、环境、阈值和评价指标会触发或掩盖该属性 |

如果这些问题无法回答，“涌现”就可能只是修辞；如果能够回答，它就是普通而严肃的系统科学概念。

### 1. 三种经常被混淆的“涌现”

围绕大模型的讨论至少混用了三种不同问题：

| 讨论对象 | 所谓“涌现” | 应如何验证 |
| --- | --- | --- |
| 模型规模 | 大模型在某项基准上突然超过阈值 | 检查尺度、数据、指标连续性和统计方法 |
| AI 系统 | LLM、Context、Tool、Loop 组合后完成单体不能完成的任务 | 在系统边界上做任务测试、消融实验和运行观测 |
| 认知哲学 | 系统是否具有理解、意向性、自我意识或主观体验 | 需要额外的认知理论和证据，不能由任务成绩直接推出 |

关于第一种含义，Wei 等人的论文 Emergent Abilities of Large Language Models将某些小模型没有、较大模型才出现的基准能力称为“涌现能力”；Schaeffer 等人的 Are Emergent Abilities of Large Language Models a Mirage?则指出，部分突变可能来自非连续评价指标，换成连续指标后性能变化会变得平滑。这个争论说明：**“跨过评价阈值”与“系统产生了新的本体属性”不是一回事。**

本系列讨论的重点是第二种：工程系统的功能性行为涌现。它不依赖“规模曲线是否突然跳变”，也不要求先证明机器具有心智；只要求我们诚实地描述整体系统相对于部分增加了哪些功能，并用测试和运行证据检验这些功能。

### 2. “可控”不等于每个 Token 都可预测

SEBoK 区分了较易预测的简单涌现、只能预期但难以精确预测其水平的弱涌现，以及在仿真、测试乃至运行时才暴露的意外涌现。它同时强调，期望的涌现通常要通过建模、迭代以及 build/test 循环逐步获得。

所以“可控涌现”并不是声称工程师能预先确定模型的每一个输出，而是指：

> **通过系统结构、上下文、权限、反馈、验证、预算和人工决策，提升期望行为出现并通过验收的概率，同时限制非期望行为的影响范围。**

控制对象不是单个 Token，而是任务轨迹和系统结果；控制目标也不是绝对确定性，而是可接受的成功率、风险、成本、时延与可恢复性。

## 二、LLM + Context 涌现的是功能行为，不是认知结论

一次 LLM 生成可以抽象为：

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHk86AQtVx0MsgEww5dicl3bzf6PESP42ksSHyelSx2dof90En4tHUhRTag3SDW2vMRhMDS1UnpbzukuEVCxWJAULJciauKLrRE3mw/640?wx_fmt=png&from=appmsg)

其中，参数 θθ 保存训练形成的统计结构，Ct是本轮可见的， Context，ytytt 是模型生成的文本或结构化动作建议。仅凭这个过程，模型不能直接读取一个未提供的本地仓库，不能真正执行编译器，不能知道命令是否成功，也不能让错误修改自动回滚。

但是，当工程系统把仓库文件、用户目标、项目规范、Tool Schema、执行结果和测试反馈持续写入 Context，再由运行时执行模型提出的动作时，系统整体可以形成这样的轨迹：

```
理解目标 → 检索仓库 → 制定计划 → 修改代码 → 运行测试
        → 读取失败 → 定位原因 → 再次修改 → 验收交付
```

这条轨迹不是任何单个组件独自拥有的能力：LLM 不执行命令，Shell 不理解需求，测试框架不制定修复策略，权限模块不写代码。**“围绕目标进行多步软件工程并根据真实结果纠错”是这些部分按特定关系组合后才成立的系统级功能。**

它也不是纸上推演。官网公开案例里的每一次会话回放，都是这条轨迹在真实仓库、真实样本上跑完的记录——例如把一张需求脑图端到端做成企业级监控系统，或者在只有一个离线安装包、没有源码的前提下核验一款闭源客户端的数据边界。推理、工具调用、报错与恢复全程可查，包括走错又退回的地方。

### 1. Context 是模型的运行条件，也是 Agent 的状态载体

Context 对输出分布的影响可以写成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHkicJI5mOhXqmOClW3LQcQn6TBgY3shUK1icPK1HWK1VPUW1MmjxTlf26WGEVTibhnzViaTHC0ZicOhFuOCGh552lOJWsaowhuA2O0F8/640?wx_fmt=png&from=appmsg)

Pθ(yt∣Ct)≠Pθ(yt∣Ct+ΔC)![Context、LLM、Tool 与运行时之间的关系](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkiccj103UQkZaXIGe5eP4yXqmNTI4NeslTadVLbKeLkRA1S6bCBUKXfFMZJ2bkV9aXzJ1pZaf2njatbovP3iagnSTUicpicpnU4A1E/640?wx_fmt=other&from=appmsg)

图 2：LLM 基于当前 Context 生成 Tool 调用建议，运行时执行动作并把结果写回 Context。

加入项目规范、相关代码或一次测试失败，不会修改模型参数，却会改变下一步输出和行动的条件。Context 在工程系统中至少承担三种角色：

* **任务条件：目标、范围、约束、验收标准；**
* **状态估计：已经做了什么、当前做到哪一步、哪些假设已被证伪；**
* **外部观测：文件内容、命令输出、测试结果、用户审批。**

这也是为什么“同一个模型”放进不同 Harness 后表现会显著不同。模型能力提供可能性空间，Context 决定当前可见的局部条件，运行时则决定哪些输出能成为现实动作。

### 2. 必须把几种“知识”分开

在 AI 讨论中，“模型知道”“Context 给了知识”“系统学会了”经常被当作同一件事。工程上更适合分层描述：

| 层次 | 载体 | 作用 | 局限 |
| --- | --- | --- | --- |
| 参数化统计知识 | 模型权重 | 提供语言、代码与任务模式的先验 | 可能过时、失真，来源通常不可逐条追溯 |
| 上下文知识 | 当前提示与消息 | 提供任务相关事实、规则和示例 | 受窗口容量、排序和噪声影响 |
| 外部可验证知识 | 文件、数据库、文档、Tool 结果 | 提供当前环境中的事实证据 | 需要权限、检索、时效和来源校验 |
| 运行状态知识 | Plan、Todo、调用结果、错误记录 | 让多步任务保持连续性 | 需要结构化保存、压缩与恢复机制 |
| 组织知识 | AGENTS.md、Skill、流程、门禁策略 | 固化团队做事方式和质量标准 | 软性说明仍可能被模型偏离，硬要求需运行时执行 |

![不同知识如何进入 Agent，并在 Context、运行状态与长期记忆之间流动](https://mmbiz.qpic.cn/mmbiz_jpg/XBFaicYdOHk9icVTf23HNJq8sBy4UMayVJc0lsedUiagkXicWxibWjick9XAcFyDGdVPS7o1WDMia3P943C8HY31dTRF8YGyfDeShzaoy1KiarqShQ8/640?wx_fmt=other&from=appmsg)

图 3：不同知识并不是同一层东西。模型权重提供先验，外部事实与组织知识进入当前 Context，运行状态在行动与反馈中持续更新，跨会话经验则通过审核后的长期记忆按需召回。

知识在系统中的价值，不只取决于“有没有”，还取决于它是否在正确时刻被召回、是否与任务相关、是否可验证、是否能进入反馈闭环。

#### AVL Code 的“记忆宫殿”

如果把跨会话知识看作一座需要路线和门禁的“记忆迷宫”，那么 AVL Code 用户手册中的正式名称是“记忆宫殿”。会话结束后，`HookStop` 会提取记忆候选，先放入 `_pending/` 草稿盒；只有经过用户审阅批准，候选才进入相应房间。用户也可以用 `/memorize <text>` 主动写入，用 `/memory` 打开管理面板。

真正进入下一轮的不是整座宫殿，而是与当前问题相关的少量记忆：系统综合召回次数与使用成效调整排序，减少无关注入；遇到重复或冲突时先放入待审区，而不是直接覆盖旧知识。这个“候选—审核—入库—召回—成效反馈”闭环，改善的是事实与经验的反馈质量，而不是无限加长提示词。

### 3. 行为能力不能直接证明认知状态

当系统能够解释代码、调用工具、修复测试时，说它“表现出编程能力”是一个可检验的功能描述；说它“理解了代码”“知道自己犯错”“产生了自我意识”，则引入了更强的认知和哲学主张。

Bender 与 Koller提醒研究者区分语言形式与意义，Shanahan则提醒人们谨慎使用“知道”“相信”“思考”等容易造成拟人化的词。对这些问题可以继续研究和争论，但工程上应守住一条证据边界：

> **能够产生与理解相似的行为，不等于已经证明系统具有与人同类的理解机制；能够执行智能任务，也不等于已经证明主体性或意识涌现。**

因此，本系列所说的“智能”优先指可测量的任务能力，而不是对系统内在体验的断言。

## 小结与下篇预告

到这里，我们确定了两件事：涌现是系统整体相对于部分多出来的、可观察可测量的属性；LLM 与 Context、Tool、运行时结合后涌现的是功能性行为，而不是认知结论。

但“功能行为可以涌现”只回答了现象是什么，没有回答工程该怎么做。如果模型只是提出建议，那么真正决定这些建议能否变成受约束的现实动作的，是模型之外的那一层结构。中篇《Harness 工程与 Loop 工程》（7 月 17 日发布）将讨论：Harness 如何把模型能力接到真实世界，以及 Loop 如何在一个无法完全建模的对象上实施反馈控制、并给出明确的停止条件。

## 参考资料

### 系统工程主要资料

* SEBoK：Emergence
* SEBoK：Emergent Property (glossary)

### 补充论文

* Wei, J. et al.（2022）：Emergent Abilities of Large Language Models，arXiv:2206.07682。
* Schaeffer, R., Miranda, B. & Koyejo, S.（2023）：Are Emergent Abilities of Large Language Models a Mirage?，arXiv:2304.15004。
* Bender, E. M. & Koller, A.（2020）：Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data，ACL 2020，DOI: 10.18653/v1/2020.acl-main.463。
* Shanahan, M.（2022，2023 年修订）：Talking About Large Language Models，arXiv:2212.03551。

---

*AVL Code，AVL 安全引擎，与智能随行。安天澜砥团队出品。*

安天AVL Code官网链接：https://www.avlcode.cn

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHk8PT5nqiaDOuVwSp5Yh8bbK9OZSKPOOvVygZmtrGWu1EoQ2WSvouP8ASaN9U4MvwhOlhZyOLia4ILUAZqIrDp3LzOJMaBwqYOY00/640?wx_fmt=jpeg&from=appmsg)

**安天AVL Code网站二维码**

**往期推荐:**

[用AVL Code验证Grok Build CLI上传用户代码仓库事件](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215084&idx=1&sn=b34818a548fe48b2beeb5c8a9f522175&scene=21#wechat_redirect...