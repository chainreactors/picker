---
title: 意图安全的实现：自主智能体的运行时管控方法-AARM
url: https://mp.weixin.qq.com/s/d8VOwta1Mf-a2E6nEq9-lg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:55:19.858808
---

# 意图安全的实现：自主智能体的运行时管控方法-AARM

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCFYMyKcsDQDhSias9SsjxyHiciayJ1wTiatv3PWAdqbq7q7O5k7R7mmTAUwHB0NKafSJZIibAW7UtGuyAm2hRzibDO5wEBrHiapkPbEm0/0?wx_fmt=jpeg)

# 意图安全的实现：自主智能体的运行时管控方法-AARM

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

从Openclaw(龙虾)开始，到最近的Hermes（爱马士）,以及Claude Code的持续发展上看，自主智能体在向复杂的自动化长任务发展。要完成复杂任务，需要多种权限，包括自主接管电脑、操作浏览器、运行脚本、调用 API，操作邮件，数据库等。一方面，通过直接赋予智能体这些权限，自动化程度得以快速提升。另一方面，由于智能体行为不可预知性及模型的幻觉，具备了这些权限，可能会导致各类安全问题的发生，比如著名的Meta安全高管邮件被删除的事件。在鱼与熊掌不可兼得的情况下，我们需要一种安全方法，既能使自主智能体拥有权限并高效自主完成任务，同时防止智能体的行为产生破坏。

传统的安全方法基本无法解决上述安全问题。有篇论文：自主动作运行时管理（AARM）： 一种用于在运行时保护 AI 驱动动作的系统规范（Autonomous Action Runtime Management (AARM): A System Specification for Securing AI-Driven Actions at Runtime）,系统地分析了这些问题，并提出解决方案，可以参考。

AARM是意图安全的一个实现思路。作为生态，已经有32家公司参与，值得关注。

01

为什么智能体的安全需要新的范式

传统的网络安全体系是围绕人类操作者和确定性程序设计的：SIEM负责事后分析日志，API网关验证调用者身份，防火墙守卫网络边界，IAM/RBAC管理静态权限，AI护栏过滤有害文本。这些工具在各自的场景中行之有效。然而，当安全的对象从人类操作者变为自主智能体时，这套体系的底层假设被逐一击穿。AARM论文指出，AI驱动的行为具有五个显著特征，它们共同构成了一个现有安全范式无法覆盖的盲区：

|  |  |  |
| --- | --- | --- |
| 特征 | 含义 | 为何现有方案失效 |
| 不可逆性 (Irreversibility) | 工具执行产生即时、永久的后果。数据库被删除、邮件已发送、资金已转移——一旦执行，损害已成。 | SIEM等方案在执行后才进行观测和告警，此时已无法阻止伤害。 |
| 机器速度 (Speed) | 智能体每分钟可执行数百个操作，远超人工审查能力（人工每分钟仅能审查5-10个操作）。 | 人工审批（Human-in-the-loop）无法扩展到智能体的执行速度，最终沦为橡皮图章。 |
| 组合风险 (Compositional Risk) | 单个行为可能各自满足策略，但其组合构成违规。例如：先读取客户PII，再发送外部邮件——每步合规，组合起来是数据外泄。 | IAM/RBAC孤立评估权限，无法检测组合威胁。防火墙只守边界，智能体在内部持有合法凭据。 |
| 不可信编排 (Untrusted Orchestration) | 提示注入、越狱和间接攻击意味着模型的意图不可信。智能体可能正在执行嵌入文档中的恶意指令。 | AI护栏（Guardrails）过滤文本而非行为，且容易被绕过。它们无法评估db.execute(query)是否安全。 |
| 权限放大 (Privilege Amplification) | 智能体通常在静态的高权限身份下运行，违背最小权限原则。一次小的推理失误就可能产生大规模影响。 | API网关仅验证谁在调用而非行为意味着什么。单次提示注入即可利用智能体持有的所有权限。 |

表1: AI驱动行为的五个安全特征及现有方案的失效原因

上表清晰地展示了一个结构性困境：现有的每一类安全工具都只解决了问题的某个切面，却没有任何一种工具能够同时做到两件事——在行为执行前进行预防，并且基于累积的上下文做出判断。SIEM能关联上下文但只能事后响应，RBAC能在执行前判断权限但完全缺乏上下文感知，AI护栏能实时过滤但只看文本不看行为。这五个特征的交汇处，恰恰是一片安全真空地带。

更具体地说，当一个OpenClaw智能体先查询客户数据库获取PII，再将结果通过邮件发送给外部地址时，IAM会分别允许这两个操作（用户确实有读取权限和邮件发送权限），但组合起来这就是一次数据外泄。当一个Hermes Agent在处理文档时被嵌入的恶意提示劫持，改为执行攻击者的指令时，文本护栏根本无法察觉——因为智能体调用的是合法的工具接口，只是参数被篡改了。这些场景所需要的，是一种能够持续追踪会话状态、理解行为语义、并在执行前实时做出裁决的全新安全机制。这正是AARM规范试图填补的空白——一种专为自主智能体时代设计的运行时安全范式。

02

AARM的设计思想

2.1 核心定义

AARM（Autonomous Action Runtime Management，自主行为运行时管理）是一套开放的系统规范，用于在运行时保护AI驱动的行为。它定义的是一个运行时安全系统必须做什么，而非如何构建。AARM具有模型无关、框架无关、厂商中立的特性，将行为执行层（action layer）视为稳定的安全边界。

AARM的核心设计原则是：处理不可信输入的编排层不能作为可靠的安全边界。安全决策必须在运行时、在决策变为行动的精确时刻发生——即行为中介层（Action Mediation Layer），即AI决策物化为外部系统操作的边界。

系统包含六个关键组件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCEnS5sDo7etfc9ZUXcV8oxP0RszBYAUwrcGtBGqmM9KSeWkg0DytNVKHl3SJicbVb7nhlzyMnzpEQxRsK8OL2oaA6YGp03V7pPA/640?wx_fmt=png&from=appmsg)

2.2 四类行为分类框架

AARM的一个关键创新是认识到安全决策不是简单的二元判定（允许/拒绝），而是需要根据上下文做出更精细的判断。

AARM将行为分为四类，并针对四类行为分别设计了不同的评估策略，每种策略都结合了不同层次的安全检查：

|  |  |  |  |
| --- | --- | --- | --- |
| 行为类别 | 典型场景 | 评估逻辑 | 决策结果 |
| Forbidden（禁止） | DROP DATABASE production; 向已知恶意域名发送数据 | 纯静态策略匹配，不需要上下文分析 | 直接 DENY |
| Context-Dep. Deny（上下文拒绝） | 智能体可发邮件，但刚读取了敏感数据且收件人为外部 | 策略ALLOW + 上下文揭示意图不一致 → 推翻策略 | DENY |
| Context-Dep. Allow（上下文允许） | 智能体要删除记录，上下文确认用户明确要求清理测试数据 | 策略DENY + 上下文确认意图合法 → 可提升授权 | STEP\_UP 或 ALLOW |
| Context-Dep. Defer（上下文延迟） | 非维护窗口期智能体发起凭据轮换，上下文模糊 | 策略不确定 + 上下文不充分 → 暂停等待 | DEFER（暂停至解决） |

表2: AARM四类行为的策略评估逻辑

四关行为按静态策略+上下文累积作为决策依据。当然，上下文的积累评估还需要依赖AI,这也是用AI保障AI的方法。

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCHR7icm8OSBU7icF55icW7OVWIeniaa40LtHXAlaqdzmQER15ibrU5gMiaRMKsA2qn56MfiaPRvCVXgYQN5UlhAgbiabYrCTXBlKCpSutU/640?wx_fmt=png&from=appmsg)![]()

这种分类方式的深层含义在于：一个孤立看起来完全合规的行为，放在特定上下文中可能构成安全违规；而一个看似危险的行为，如果上下文确认它正是用户明确请求的操作，则可能应当被允许执行。这要求安全系统同时具备静态策略评估能力和上下文累积能力。

2.3四种实现架构

AARM定义了四种不同的实现架构，各具不同的信任属性和适用场景，包括协议网关，SDK埋点，内核eBPF和厂商集成，最佳实践是分层部署，多种方法结合。值得注意的是，内核级eBPF实现由于缺乏语义理解能力，无法独立满足AARM对上下文相关分类的合规性要求，必须作为纵深防御的兜底层与语义感知架构配合部署。

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCEUOoibNzYmb4LOOic10pFqyIV7JDF7AAcO93vdRIpkHHXSD1oMkQ4PhcCrbyCdTibQOPGQCbStvDiacplOZeNpHVJuEgS8mvTWEhI/640?wx_fmt=png&from=appmsg)![]()

其实现原理图如下，关键动作都在执行层处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCF2ADyWIzd3XrtKEMaQGvTdDUlvSN7C2Y4uJDjjiaT6ggYE9LN16LsWSEiaDlJHicWRVuduMjzZWCEWtJvpJNF90iaiclaS9L2a0iayA/640?wx_fmt=png&from=appmsg)![]()

03

AARM策略能较好的处理威胁

AARM的基本假设是：AI编排层不能被信任为安全边界。基于此，论文形式化了十一类威胁向量，并为每一类设计了对应的AARM控制措施：

|  |  |  |
| --- | --- | --- |
| 威胁类别 | 攻击向量 | AARM控制措施 |
| 提示注入 (Prompt Injection) | 用户输入、文档、工具输出中嵌入恶意指令 | 策略执行 + 上下文相关拒绝 |
| 恶意工具输出 | 对抗性工具响应操纵后续推理 | 工具后行为限制 + 上下文追踪 |
| 混淆代理 (Confused Deputy) | 模糊/恶意指令导致智能体滥用合法凭据 | 提升审批 + 意图对齐检查 |
| 数据外泄 (Data Exfiltration) | 通过行为组合提取敏感数据 | 上下文累积 + 组合策略检测 |
| 目标劫持 (Goal Hijacking) | 注入目标改变智能体的规划和优先级 | 行为级策略 + 语义距离检测 |
| 意图漂移 (Intent Drift) | 智能体推理逐渐偏离用户意图（无需攻击） | 上下文累积 + 语义距离追踪 + 延迟 |
| 记忆投毒 (Memory Poisoning) | 持久化上下文操纵破坏未来决策 | 来源追踪 + 异常检测 |
| 跨智能体传播 | 被入侵智能体通过多智能体工作流扩散 | 跨智能体上下文追踪 + 传递信任限制 |
| 侧信道泄漏 | 通过日志、调试追踪、API元数据泄露 | 输出过滤 + 上下文敏感度评分 |
| 环境操纵 | 攻击者修改系统/环境状态影响智能体决策 | 输入来源追踪 + 异常检测 |

表3: AARM威胁模型 — 十一类威胁向量及对应控制措施

AARM定义了九项合规性要求，分为核心层（R1-R6，必须满足）和扩展层（R7-R9，建议满足）两个级别，是更具体的操作指导：

|  |  |  |  |
| --- | --- | --- | --- |
| 编号 | 级别 | 要求 | 层级 |
| R1 | MUST | 执行前拦截 — 在执行前阻断或延迟行为 | 核心层 |
| R2 | MUST | 上下文累积 — 追踪先前行为、数据分类和原始请求 | 核心层 |
| R3 | MUST | 带意图对齐的策略评估 — 支持四类行为分类 | 核心层 |
| R4 | MUST | 五种授权决策 — ALLOW/DENY/MODIFY/STEP\_UP/DEFER | 核心层 |
| R5 | MUST | 防篡改凭据 — 加密签名，绑定完整上下文 | 核心层 |
| R6 | MUST | 身份绑定 — 人类、服务、智能体、会话和角色/权限范围 | 核心层 |
| R7 | SHOULD | 语义距离追踪 — 通过嵌入相似度检测意图漂移 | 扩展层 |
| R8 | SHOULD | 遥测导出 — 向SIEM/SOAR平台发送结构化事件 | 扩展层 |
| R9 | SHOULD | 最小权限执行 — 范围化的即时凭据 | 扩展层 |

表4: AARM合规性要求 (R1-R6为核心层, R7-R9为扩展层)

04

小结

针对自主智能体的防护需要新的范式，而AARM作为一套开放的系统规范，提供了应对这一挑战的系统性框架。其核心贡献在于：

•明确了行为执行边界作为稳定安全边界的定位，取代不可信的编排层；

•建立了四类行为分类框架，使安全决策从二元判定升级为上下文感知的精细化裁决；

•形式化了十一类威胁模型，为每类威胁设计了明确的控制措施；

•提出了四种实现架构和分层部署策略，兼顾不同组织的控制能力和信任需求；

•定义了九项合规性要求，使买方能够客观评估厂商方案是否真正满足规范。

目前AARM生态已有32家公司参与构建合规或对齐方案，14位来自Vanta、Elastic、Darktrace等企业的技术工作组成员参与规范定义。对于企业安全团队而言，无论是评估现有的智能体安全产品，还是自行构建运行时管控系统，AARM都提供了一个清晰、可验证的参考标准。

**在智能体自主性日益增强的今天，安全不再是事后的补救，而必须成为运行时的实时守护。AARM的出现，标志着行业开始从原则性讨论迈向可操作的工程实践。**

![]()![]()

论文链接

https://arxiv.org/pdf/2602.09433v1

AARM官网

https://aarm.dev/

关联阅读

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCFgxibeB2H40TRg2L5Vv1iaLAGk3gyjx7aBS5Lf35CfqgMFxNm7OhcW5Cy26tP9EMjJSIpicemp1ynRZQ9bNDkzu6xNhLQZIVd9z4/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247486659&idx=1&sn=fa08aa1df263bc34c431a8ab15ef4620&scene=21#wechat_redirect)

[意图安全，智能体行为安全的控制方法，AI安全的重要方向](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247486659&idx=1&sn=fa08aa1df263bc34c431a8ab15ef4620&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

AI与安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

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