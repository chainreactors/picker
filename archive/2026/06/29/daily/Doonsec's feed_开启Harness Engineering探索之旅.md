---
title: 开启Harness Engineering探索之旅
url: https://mp.weixin.qq.com/s/uhc7_-0Vm_cw9p17b9VyJA
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:19.941757
---

# 开启Harness Engineering探索之旅

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KVER9adz90626sjIWc4PZhyeC3xI7IYTVgKY73LM0BJa9ZRu7SoFicsAK9ZGOMlgyX4bXmvBZxBicSlfUJiaWlE2Qq47iagN5ZJiabovnChkyOsY/0?wx_fmt=jpeg)

# 开启Harness Engineering探索之旅

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：fanniemeng

过去两年，AI Coding 从"能写出能跑的代码"走到"能放手让它写一整段功能"。但把这个能力放进真实业务、放进多人协作、放进存量系统里跑时我们发现一件怪事——AI 写得越快，整体节奏并没有同步加快。盘点下来，单看"AI 写出来的代码占比"这个数字一路走高，可真正落到版本节奏上，提效却远没有这个数字好看。出码率和提效之间，裂开了一道缝。从 OpenAI Codex 团队那篇 Harness 工程博客里反复强调的一个观察——"早期进展比预期慢，并不是因为 Codex 不具备相应的能力，而是因为环境的规范不够明确"——开始，整个行业都在补同一件事：给模型搭一套能稳定干活的"工作环境"。这一层最近被业界命名为 Harness Engineering——它不是教模型怎么回答，而是设计模型怎么工作。 在这里，也分享下我们的探索之旅，是踩过的坑、做过的取舍、和到现在还没解决的问题。

### **序章：Harness Engineering 是怎么"结晶"出来的**

#### **0.1 先把话说清楚：Harness 到底是什么**

Harness Engineering 一句话能讲完：

*不是教模型"怎么回答"，而是设计模型"怎么工作"。*

用一个正在被广泛引用的等式表达就是：

*Agent = Model（模型）+ Harness（模型外的运行框架）*

命名者 Mitchell Hashimoto 给出的定义更朴素，也更直指核心：

"It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."—— 每当你发现 Agent 犯了一个错，你就花时间在它外面工程化一个方案，让它永远不再犯同样的错。

它把工程关注点从"模型这一句说得对不对"，挪到了"模型这一整段活干得稳不稳"。换个视角看，这其实是 AI 工程关注点连续迁移的第三站——

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz90403zSOXbXAx1MVpmKpRfm8heZaCremH3WRU7tZSS6ywfGVMSjJpPwbm0xLBKvb6KNMAXllxMKCib84wsYoVdul0Nr7EicjNE1Ng/640?wx_fmt=png&from=appmsg)

*图 1 · AI 工程关注点的三次迁移：Prompt → Context → Harness*

* Prompt Engineering（2022–2024）：关心单次调用——这一句话怎么说，模型这一次输出得更好。
* Context Engineering（2025）：关心每一步——该把什么信息、以什么形式喂给模型。
* Harness Engineering（2026）：关心整个任务——当 Agent 要跑长链条、多步骤的活，可靠性已经不取决于模型本身，而取决于模型外面那一整套工程化框架：执行环境、工具协调、状态管理、反馈注入、约束施加、进展验证。

一句话概括三者关系：Prompt 教模型怎么说话，Context 保证它上班有足够信息，Harness 给它搭一套能持续干活的工作环境。 三层不是替代关系，而是层层叠加——Harness 时代到来，意味着前两层已经基本成熟，短板被挤到了"模型外面"。

#### **0.2 概念结晶时间线：仍在结晶中**

有意思的是，"Harness Engineering"这个词不是某个人一拍脑袋造出来的，而是先有实践、后有命名、再被推广、最近才开始被学术界系统梳理——一个典型的"概念结晶"过程（还在过程中）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906icffqGWibOzyrJeA9j60eUibmxvL6OFJwzJLDBn0DlHD7ecshOiaib64qHzJ2oBvpfmSMACXKuPr2TudVgfCRvdb0MIDLtTrePQy4/640?wx_fmt=png&from=appmsg)

2025 年8月起，OpenAI Codex 团队在 agent-first 内部实验中验证：模型能力之外，环境设计、上下文组织、工具抽象、反馈回路和控制系统同样决定 Agent 能否稳定工作。2026 年2月，Mitchell Hashimoto 将这类“发现 Agent 犯错后，用工程手段让它不再犯同类错误”的实践称为 harness engineering。随后 LangChain 用 “Agent = Model + Harness” 明确边界， Böckeler / Thoughtworks将其拆解为 guides 与 sensors，学界也开始用 ETCLOVG 七层分类做系统化梳理。  Harness Engineering 没有标准定义，但它有一条清晰的实践路径： 为Agent搭建可执行、可约束、 可验证、可反馈的工程环境。

Harness Engineering 没有标准定义，但它有一条清晰的实践路径： 为Agent搭建可执行、可约束、 可验证、可反馈的工程环境。

#### **0.3 回到我们自己——AI 写得快了，研发整体没快多少**

回到我们自己：团队很多人都已经离不开 AI Coding 了——一个独立小模块从想法到能跑，一杯咖啡的时间。但盘点产出时我们发现一件怪事：单看"AI 写出来的代码占比"，这个数字一路走高，可真正落到版本节奏上，提效却远没有这个数字好看。 出码率和提效之间，裂开了一道缝。分析根因是三件事:

* 根因一：研发从来不是"写代码"这一个环节。 早在《人月神话》和《没有银弹》里，Brooks 就把软件难题拆成两层：附属复杂度（accidental，语法、工具、平台带来的"翻译成本"）和本质复杂度（essential，概念结构的构造、对外部世界的顺应、需求的可变性）。AI 砍掉的恰好是附属那一层，本质复杂度一分没少——甚至因为代码产出更多，下游的对齐、review、维护反而更重了。"没有银弹"从来不是因为银弹造得不够好，而是因为狼根本不在编码这一层。
* 根因二：局部加速只会让瓶颈转移，不会让它消失。 把"写"这一环踩到十倍速，理解、对齐、验证、沉淀这些环节一步没动——整条链的总时长由没被加速的部分决定。于是写得越快，下游的 review、测试、维护越被动，瓶颈只是从"写"挪到了"收"，整体没动几分。
* 根因三：AI 看不见我们工程体系里的隐性约束。 团队规范、领域知识、历史依赖，这些没被显式喂进去的东西，AI 一概看不见。

**换个说法**：当 AI 把"写代码"这一格的成本压到接近零，研发的瓶颈就显形了——真正的瓶颈本来就不在写，在于"理解、对齐、追溯、沉淀、验证"这一连串"非编码工作"。

真正限制研发节奏的是理解、对齐、追溯、沉淀、验证——这些恰恰是当前 AI 工具做得最差的部分。换成上一节的术语：我们撞上的，正是 Harness 这一层。我们不是在解决 Prompt（模型已经够聪明）；也不是在解决 Context（检索、长上下文这些工具已经成熟）；我们撞上的、想解决的，是怎么让 AI 在我们自己的工程体系里，能验证、能反馈、能修复、能循环、能持续地跑下去。

### **一、我们的探索**

#### **1.0 先定目标是什么？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905l26ViaZZNChNicoXMjAA99f1JlT7jl52uObP2hPUgzOfUXjJdghf2jAObpXPSv5wTv5y3IUK9n7910F2zn9EKtxcTMONOhBaL8/640?wx_fmt=png&from=appmsg)

我们的目标，用一句话说就是：**「AI 驱动研发全链路 · 人提需求 → AI 理解 → AI 执行 → 人确认」**。从 P1 需求澄清 → P2 方案 → P3 实现 → P4 测试 → P5 部署 → P6 归档，前端 / 后端并行，覆盖 DEV / TEST / OPS 三段，及线上运营告警闭环。

#### **2.0 整套体系： 2条轨道+1个长期记忆**

要让它真正跑起来， 把整套体系拆成2个轨道+1个长期记忆，轨道1：研发端到端交付，轨道2：线上运营，长期记忆(知识库)：它让 AI 真正"懂"我们的业务、系统、线上质量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz9064DNtJgredgVmJEsMu0tsGj0fgPd1hpnFBmPOsYtuBaQrelI1fRicpe8g0jtUTmKKU4vV3ktac5HZHvhrgHdc2iae8iawWVWIMbc/640?wx_fmt=png&from=appmsg)

##### **2.1 轨道 1：研发端到端交付--项目工程落地在SpecWorker上**

研发端到端交付要考虑的是 换任何人来用、用在任何项目上，AI 的产出质量是稳定的、可预期的。考虑的是3个层面的事：

###### ***2.1.1 协议层：AI 每一步的输入输出契约***

协议层--管的是一件事：AI 每一步的输入和输出必须是什么样的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906jDiaS7OvnWdy8eOuhibe6ymM8SDZds2zbZfiavAIyNX7VjXG4rubYtNBUiccLEQakaAlQ5vQ1wMI0nuTcTj0biaia4lNYrQN2NLY8Y/640?wx_fmt=png&from=appmsg)

为什么需要协议层？因为你和 AI 之间没有契约。你以为说清楚了，它以为理解了，做出来才发现对不上。人和人协作可以靠默契，人和 AI 协作必须靠契约。协议层就是这份契约。

它规定了四件事：每一步必须产出什么格式的文档、文档必须用标准模板写、写完机器自动校验是否达标、每次变更只记增量保留完整历史。预期的效果就是：AI 不再自由发挥，而是在明确的框架内输出。 格式是确定的，内容是可校验的，历史是可追溯的。出了问题能查到是哪一步导致的。

###### ***2.1.2 管线层：标准化"需求 → 上线"6+1 阶段***

**管线层——标准化整条链路工序， 让AI 在跑"需求 → 上线"这条长链，如何跑，在跑的过程中不要丢了上下文、丢了证据、丢了纪律。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz907gza4V1rlrPADqb8xEgpQicMuTD4iawAWzPILVPPFN7ZgBrS8lgWngIekLtlbqT05w6q84my90zuge2xKJuiaXgpWACQl33wC5ibg/640?wx_fmt=png&from=appmsg)

从"需求→上线"历经 6 个核心阶段 + 1 个可选前置：P0 brainstorming（可选）→ P1 requirements → P2 design → P3 implementation → P4 e2e-test → P5 deploy → P6 archive。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz907ibpt70Elcapf0yAzb1D9tdl5g3d4rVafVsPJtaMOUo3VJqAN6DOdR7kkzJ7hia3VSfnNYEZyLYWqy7FBwKndnmgBhR6Hfn2jGY/640?wx_fmt=png&from=appmsg)

6 张阶段能力深化卡片：P1/P2/P3/P4/P5/P6，P2/P3/P4/P5 标注前端/后端双流程

###### ***2.1.2.1 P1 需求：TAPD 拉取 + AC 可测 + test-cases 同源***

**问题**：研发的"理解、对齐"环节，在 AI Coding 里是最容易塌方的——AI 把功能写出来了，但"为什么这样写"没人能复述；同一个需求，A 同学昨天理解的和 B 同学今天理解的不一样。**核心痛点是：需求口径在 P1 阶段就要钉死，否则下游全部跑偏。**

**做法**：

1. TAPD 拉取做需求底稿：P1 阶段第一步是从 TAPD 拉取本次需求的官方描述，作为 [requirements.md](http://requirements.md/) 的"原始口径"段落——不允许 AI 自己复述用户的话，只允许它从 TAPD 引用。
2. AC（Acceptance Criteria）必须可测：每条需求拆成 **WHEN（前置条件）→ THEN（系统 SHALL ...）** 形式（含 AND 连接子句），禁止"性能要好"这种不可测描述；不可测的 AC 必须改写或拆细。
3. **[test-cases.md](http://test-cases.md/)****与****[requirements.md](http://requirements.md/)****同源**：P1 阶段同时产出 [requirements.md](http://requirements.md/)（给 P2 用）+ [test-cases.md](http://test-cases.md/)（给 P4 用），**两份文档共用同一份 AC 列表**——下游 P4 不再"理解一遍需求自己写测试"，而是直接拿 test-cases 跑。
4. 双 SubAgent 串联：P1 阶段不是 AI 一气呵成出稿，而是 **specworker-requirement-analyzer**（生成澄清问题 → 主流程让用户回答）+ **specworker-integration-testcase-generator**（基于澄清后的需求生成 [test-cases.md](http://test-cases.md/)）两个 SubAgent 串联。澄清 → 用户确认 → 测试用例同步生成，三步走完才算 P1 通过。

**权衡 / 边界**：P1 不解决"用户真正想要什么"——这件事必须人来做，我们只解决"AI 怎么不歪曲已经表达出来的需求"。

###### ***2.1.2.2 P2 设计：契约先行 + sandbox\_mode + D-x 改动点***

**问题**：传统 [design.md](http://design.md/) 是给人读的——讲背景、讲思路、讲架构图。但 AI 读不懂这种文档，它需要的是**机器可读的契约**：接口签名、错误码、状态机、字段必填项。如果 P2 不把这些钉死，P3 实现时 AI 会自己发明一套——下游 code-reviewer 也就无从比对。

**做法**：

1. 契约先行（[design.md](http://design.md/) 不是设计文档，是契约）：接口签名 / 数据模型 / 字段必填项一律写死成 **Markdown 表格 + Mermaid 时序图 / 数据流图**，下游 P3 实现 / code-reviewer 都拿同一份契约比对——[design.md](http://design.md/) 是契约，不是说明。
2. sandbox\_mode 字段标记写入模式（前端）：前端 P2 [design.md](http://design.md/) 顶部强制有 `sandbox_mode: true / false` 字段——`true` 时 P3 把改动先写入沙箱目录（不影响主链路），`false` 时直写项目目标文件。这个字段会贯穿到 P3，让 AI 在改代码时知道"该不该先隔离"。
3. D-x 改动点拆解：[design.md](http://design.md/) 里有一个 D-1 / D-2 / D-3 … 改动点列表，逐项标注 **「文件:行号 @ 函数名」+「目的」+「实现」+「关键代码片段」**。P3 实现时按 D-x 列表逐项勾掉，code-reviewer 也按 D-x 列表逐项 review——改动点不是流水账，是 P3 的工单池。
4. specworker-clarify-design 单 SubAgent + 两道 STOP：P2 不是一次出稿——`specworker-clarify-design` SubAgent 先做一轮代码分析、按 **P0（阻断）/ P1（高优先）/ P2（中优先）** 三档抛出技术澄清问题（如"这个接口的并发场景考虑了吗""这个状态转移的边界条件呢"），写入澄清草稿；主流程让用户回答 → 用户确认摘要方案 → 才生成 [design.md](http://design.md/)。**两道 STOP 卡点**强制把"代码分析的疑问"和"用户的业务约束"对齐后再落地。

**权衡 / 边界**：[design.md](http://design.md/) 不强求"完美"，只强求"机器可读"——任何"等实现时再说"的字段必须显式标注"待澄清"或"待确认"，不允许暗藏。

###### ***2.1.2.3 P3 实现：D2C + UI 95% 五轮 + code-reviewer 三档***

**问题**：实施阶段是最容易翻车的一格——AI 写得快，但写得对不对、像不像、改得稳不稳，全靠下游兜底。我们在这一格里做了三套兜底：D2C 把"从 Figma 还原 UI代码"、UI 双 95% 五轮校准把"像不像"做成可量化的闭环、code-reviewer 三档分级把"对不对"做成可机读的契约比对。

**做法（前端 D2C+UI较准）**：

![](https://mmbiz.qpic.cn/...