---
title: Agent Harness 实战：两阶段 ReAct 引擎
url: https://mp.weixin.qq.com/s/00y6RmK1hNOJABBY8OH1mQ
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:45.630943
---

# Agent Harness 实战：两阶段 ReAct 引擎

# Agent Harness 实战：两阶段 ReAct 引擎

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/0LGiaGIrzXunUC4icH4HPHiae1DyP6hkVCR0w1Wh4rgCsz2MjMkJstnyhvtAJzxwwYticBj8F0x2XVeah4ltLa7qiay8Kibqz2v5J6MsLOTEVRoak/640?wx_fmt=jpeg)

两阶段引擎概念：左侧思考节点与右侧执行节点通过数据流管道连接

在生产环境中跑 ReAct 循环时，开发者很快会遇到一个问题：让模型在同一次输出里同时"想清楚"和"调对工具"，两件事都容易做不好——要么推理仓促急着调工具，要么参数瞎编执行报错。两阶段 ReAct 引擎（Two-Stage ReAct Engine）把这一步拆成 Think 和 Act 两次独立调用，中间留一个可插拔的检查点，是当前 Agent Harness 中比较成熟的工程化模式。

1. 为什么需要两阶段

传统 ReAct 要求模型在单次输出中同时完成两件事：写出 Thought（推理过程）和 Action（工具调用）。这个设计在论文演示中跑得通，但落地到真实任务时暴露了三个问题。

一是推理被压缩。模型知道"接下来要输出 Action"，往往会跳过仔细分析当前状态和观察结果，直接生成一个看起来合理的工具调用。Thought 变成了走过场的格式填空，而不是真正的推理。

二是无法在行动前拦截。生产环境经常需要在执行危险操作（删除文件、发邮件、调用付费 API）前插入人工审批或安全校验。单阶段 ReAct 把推理和行动绑在一次输出里，没有天然的"中间停顿点"。

三是参数生成缺乏约束。模型在自由文本中写 Action，参数格式全靠 Prompt 描述，容易出现类型错误、枚举值错误、必填字段遗漏。等到执行时才发现，已经浪费了一次调用和一轮延迟。

两阶段的核心思路很直接：让模型先只负责想，再只负责做。两件事用不同的 Prompt、不同的输出 Schema、甚至不同大小的模型来做。

2. 整体工作流程

下图展示两阶段 ReAct 引擎的完整工作循环。每一轮迭代都经过 Think → 检查点 → Act 三个环节，执行工具后把观察结果回填，进入下一轮。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXumK9YUHX6XGaqdYRjBXLd5bUTjGKiaxNe1Mefg8AJhxTicOrRZneMIMfHAW0WJ6iaGzEAo1OtkI2IJE9mib4p9HeRp7G4DNkHesy0A/640?wx_fmt=png&from=appmsg)

循环的终止条件有三个：Think 阶段判断任务已完成并输出最终答案；步数达到上限；或检查点人工终止。

3. 与传统单阶段 ReAct 的对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXukpJB5vKEplvheavvgg4XRSm6HF5dmYXbibuf061sfw2l3WwHXicWPZdf9vJ1VkB9QXcoxqFw9s2ibBWYPWA15JJCa54xcMRGL8z0/640?wx_fmt=png&from=appmsg)

两阶段不是免费的午餐：每一步从一次调用变成两次，延迟和 Token 消耗大约是单阶段的 1.5 到 2 倍。它的价值在于把"能不能做对"这件事从赌模型一次输出，变成了有中间检查、可单独优化的流水线。

4. 核心组件详解

4.1 Stage 1 · Think：只推理，不行动

Think 阶段的输入是用户任务目标、当前会话状态、历史观察结果和已完成步骤摘要。模型的任务不是"调用什么工具"，而是回答三个问题：

1现在在哪：基于已有观察，当前进展到哪一步了？

1下一步往哪走：要完成目标，接下来需要获取什么信息或完成什么动作？

1够不够：现有信息是否已经足以直接给出最终答案？

Think 阶段的输出是一个结构化 JSON，而不是自由文本。典型的 Schema 包括：

|  |
| --- |
| json                   Think 阶段输出示例                   {                     "current\_status": "已查询到订单状态为已发货",                     "next\_intent": "需要确认快递配送时间",                     "suggested\_tool": "query\_shipping\_eta",                     "should\_answer": false,                     "reasoning": "用户问的是到货时间，已有物流单号但缺少 ETA"                   } |

这里的关键设计是 should\_answer 字段——Think 阶段可以直接判定任务完成并给出最终答案，不需要再走 Act。这把"什么时候停"的决策权也交给了推理阶段。

4.2 中间检查点：可插拔的拦截层

Think 和 Act 之间的位置是整个架构最有价值的"插槽"。这个位置可以插入不同类型的检查逻辑：

|  |  |  |
| --- | --- | --- |
| 检查类型 | 做什么 | 适用场景 |
| Schema 校验 | 用 JSON Schema 校验 Think 输出是否完整，字段是否齐全 | 所有场景，作为第一道防线 |
| 安全策略 | 检查 suggested\_tool 是否在白名单内，是否属于高危操作 | 生产环境，防止误调用删除/支付类工具 |
| 语义验证器 | 用另一个轻量模型判断 Think 的推理是否合理，是否有明显跑偏 | 长链路任务，防止规划错误累积 |
| 人工审批 | 暂停循环，将 Think 结果展示给用户确认后再继续 | 高风险操作、金额变更、对外发送内容 |

检查点不通过时，流程不是直接报错，而是把验证结果作为额外上下文退回 Think 阶段，让模型修正后重新推理。

4.3 Stage 2 · Act：只决策工具与参数

Act 阶段拿到 Think 输出的 suggested\_tool 和 reasoning，以及完整的工具 Schema 定义。模型的任务变得非常聚焦：根据工具名称，生成符合 JSON Schema 的调用参数。

这一阶段的 Prompt 不需要让模型理解业务目标，只需要告诉它"要调用这个工具，参数格式如下，上下文是这些，请填好参数"。由于任务边界收窄，参数准确率显著提升。

Act 阶段的输出直接用 JSON Schema 做机器校验：字段类型不对、枚举值不在范围内、必填字段缺失，在调用工具前就被拦截，不会把错误参数发给外部系统。

5. 实战中的关键决策

5.1 何时用两阶段，何时用单阶段

两阶段不是万能的。以下情况建议用单阶段 ReAct：

1任务链路短（3 步以内），延迟敏感

1工具数量少（3 个以内），参数简单

1原型验证阶段，需要快速迭代

以下情况强烈建议用两阶段：

1任务链路长，容易在中途跑偏

1工具多、参数复杂，参数错误代价高

1需要插入人工审批或安全校验

1生产环境对可靠性要求高

5.2 模型选择策略

两阶段架构的一个优势是可以分别选模型。Think 阶段需要推理能力，可以用更大的模型；Act 阶段本质是"按 Schema 填参数"，可以用更小、更快、更便宜的模型。这种分工在长任务中能显著降低整体成本。

反过来，如果 Think 阶段发现模型推理质量不足，可以单独升级 Think 的模型，而不必让整个引擎都跑大模型。

5.3 错误处理与回退

两阶段 ReAct 的错误处理比单阶段更精细，因为每个阶段都有独立的失败模式：

Think 阶段失败：输出不合法、推理明显跑偏、陷入重复思考。处理方式是把验证错误反馈给模型重试，超过重试次数后降级为人工介入。

Act 阶段失败：参数 Schema 校验不通过。处理方式是把校验错误信息返回给 Act 阶段重新生成参数，而不是退回 Think——因为思考方向本身没问题，只是参数填错了。

工具执行失败：外部 API 返回错误。这和单阶段 ReAct 一样，把错误信息作为 Observation 回填到下一轮 Think。

6. 最小实现骨架

|  |
| --- |
| python                   两阶段 ReAct 引擎最小骨架                   def two\_stage\_react\_loop(task, tools, max\_steps=10):                       context = init\_context(task)                        for step in range(max\_steps):                           # Stage 1: Think                           thought = think\_llm(context)                           if thought.should\_answer:                               return thought.final\_answer                            # 检查点                           if not validator.check(thought):                               context.add\_validation\_error(thought.error)                               continue                            # Stage 2: Act                           action = act\_llm(thought.suggested\_tool, thought.reasoning, tools)                           if not validate\_schema(action, tools):                               context.add\_schema\_error(action.errors)                               continue                            # 执行工具                           observation = execute\_tool(action)                           context.add\_observation(observation)                        return "达到最大步数，任务未完成" |

这个骨架只有三十行左右，但它把 Think、检查点、Act、执行回填四个环节拆成了独立可测试的函数。每个环节都可以单独替换实现：Think 可以换成更强的模型，检查点可以加上人工审批，Act 可以换成函数调用能力更强的模型，互不影响。

7. 小结

两阶段 ReAct 引擎的本质不是让 Agent 多做一次 LLM 调用，而是把"推理"和"执行"这两件不同认知负荷的事解耦。推理阶段需要慢思考，执行阶段需要快决策；把它们绑在一次输出里，结果就是两件事都做不好。拆开之后，每个阶段都可以用最合适的 Prompt、模型和校验方式来优化，中间还留了一个插入安全策略和人工审批的位置——这正是 Agent Harness 从 demo 走向生产的关键一步。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过