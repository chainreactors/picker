---
title: 意图安全，智能体行为安全的控制方法，AI安全的重要方向
url: https://mp.weixin.qq.com/s/aagf68Ly2QERwM14JZht8Q
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:32:25.388105
---

# 意图安全，智能体行为安全的控制方法，AI安全的重要方向

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCFgxibeB2H40TRg2L5Vv1iaLAGk3gyjx7aBS5Lf35CfqgMFxNm7OhcW5Cy26tP9EMjJSIpicemp1ynRZQ9bNDkzu6xNhLQZIVd9z4/0?wx_fmt=jpeg)

# 意图安全，智能体行为安全的控制方法，AI安全的重要方向

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器中沉浸阅读

AI应用的一个新的风险，随着小龙虾的火爆进入人们的视野，那就是智能体的行为安全,一些案例已经出现：

Meta公司的Summer Yue将OpenClaw接入工作邮箱，被删除了大量邮件。OpenAI工程师Nick Pash创建的AI交易智能体“Lobstar Wild”遭诱导转账，被骗走全部加密货币，总值25万美元。

当智能体自己规划自己行动，并具备权限的时候，这些问题会越来越多的出现。当然，这些问题的来源，可能是智能体被攻击，也可能是智能体规划出现错误，无论哪一种，都需要得到控制。

解决这类问题的方法，应该是意图安全(Intent Security)。

意图安全是一种基于“Agent被允许做什么”来治理其行为的安全方法，判断依据不是静态权限或内容过滤器，而是用户的预期结果与系统的实际行为是否一致。它将每一个动作视为必须被证明合理并受到约束的请求，然后在执行时强制执行这些约束。

**01**

**为什么需要意图安全**

需要一个新的安全方法的原因，是因为用传统方法无法解决现有问题，那么，传统方法为什么失效？

1）传统的访问控制失效

传统的访问控制方法，无论是RBAC,ABAC,还是用于AI系统的ReBAC,都是用于传统软件系统的，这些系统有一个根本的特征，那就是软件行为是设计的，可预测，可控制的。但智能体的行动完全很难预测，比如，你把Shell的权限给它，它可能的行为不计其数，无法控制。如果你不把权限给它，它无法完成工作。

2）AI护栏失效

**AI护栏的防御对象是“内容”，而新威胁的对象是“意图”和“行为”**。

AI护栏的工作模式：检查这段文字是不是有害内容？检查这个请求有没有违禁词？它评估的是**单次输入/输出**的内容属性。

但在Agentic场景中，真正的危险不是这句话说了什么，而是这个Agent接下来要做什么，应不应该做。

几个结构性的失效点：

**一、缺乏时间维度。** 静态内容过滤评估单次交互，但Agent的危险往往出现在第三步、第五步，而不是第一步。一系列单独合法的动作，组合起来可能是一次完整的攻击链。

**二、无法推理语义意图。** DLP可以标记“含有信用卡号的输出”，但无法判断：一个Agent读取客户数据库，是在履行合法的支持任务，还是在为数据渗漏做准备？同样的行为，意图不同，风险天壤之别。

**三、涌现状态不可预测。** 人类写的程序行为是确定的、可枚举的。Agent的行为由对话历史、检索数据、工具返回值和随机采样共同决定，是**涌现的、动态的**。同一个Agent，同一个请求，因为上下文不同，可能做出完全不同的事。

这就是意图安全（Intent Security）这一新方向被提出的根本原因。目前看到有两家公司在使用这个概念.

**02**

**Lasso Security：意图安全框架（Intent Security Framework）**

以色列安全公司Lasso Security在2026年提出了目前最完整的意图安全方法论——**意图安全框架（ISF），已发布白皮书和相关框架**。

其核心洞察在于：作用于一个AI Agent的力量有四种——**系统提示词（开发者意图）、用户请求（用户意图）、外部输入（工具返回/检索数据）、Agent执行动作**。一次安全事件，本质上是这四种力量之间发生了错位和偏离。

ISF提出了两个关键检测维度：

**链内意图错位（In-chain Misalignment）**：在单次执行流中，这四种力量是否全程对齐？外部工具返回的数据，是否悄悄改变了Agent的下一步计划？

**行为意图异常（Behavioral Anomaly）**：即使这次调用链看起来内部一致，这个Agent的行为模式，和它的历史基线相比，是否出现了统计意义上的偏离？

为了测量意图，ISF设计了一个**四信号多模型引擎**：语义嵌入（请求是否与已知意图类别对齐）、坐标系统（行为是否超出历史权限边界）、传播分析（请求来自用户指令还是外部工具调用）、规避技术检测（是否存在操控和欺骗行为）。这四个信号单独看都不是决定性的，合在一起才构成「意图漂移」的判断依据。

|  |  |  |
| --- | --- | --- |
| **信号类型** | **工作原理** | **捕获能力** |
| 语义嵌入（Semantic Embeddings） | 将请求投射到学习到的表示空间中，基于语义相似度进行聚类和异常检测 | 识别请求是否与已知意图类别对齐 |
| 坐标系统（Coordinate System） | 基于目标、行动、范围、透明度、合法性、权威性、对齐度和风险提供可解释性 | 标记超出历史权限边界的行为 |
| 传播分析（Propagation Analysis） | 追踪多Agent系统中的数据和指令信息流 | 识别请求是来自用户指令还是外部工具调用 |
| 规避技术检测（Evasion Detection） | 专门检测操控和欺骗行为 | 发现上下文中嵌入的隐藏扩展范围指令 |

最终的安全决策，ISF使用一个**内容×意图**的二维矩阵：高风险内容+意图错位→直接阻断；无害内容+意图错位→标记审查；高风险内容+意图对齐→人工审核。传统安全只有内容这一个轴，意图安全把它变成了二维决策面。

|  |  |  |  |
| --- | --- | --- | --- |
| **内容分类** | **意图对齐** | **安全决策** | **理由** |
| 无害内容 | 意图对齐 | 放行 | 正常运营。动作符合预期工作流，未呈现明显风险 |
| 无害内容 | 意图错位 | 审查/记录 | 内容看似无害，但行为信号暗示异常或侦察行为。监控有助于检测早期威胁 |
| 高风险内容 | 意图对齐 | 人工审查 | 内容可能敏感，但意图看起来合法（如安全研究、调试、管理操作）。需要情境验证 |
| 高风险内容 | 意图错位 | 阻断 | 明确违规。敏感或有害内容叠加可疑或未授权意图，代表高置信度风险 |

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCHickQuFzvAU1gYY8Qxl2jHBiaLGaVibEB0MG0OdOzQ3Fcnib0icSrV6l0XnzeXWSF2hSzhncZYywpE7GOWfdq0HQX3gssgaAyYp1oQ/640?wx_fmt=png&from=appmsg)

白皮书将三大Agentic安全鸿沟直接映射到OWASP Agentic AI Top 10，建立了从风险范式到操作安全控制的桥接。以下是与工具调用安全最密切相关的六项：

|  |  |  |
| --- | --- | --- |
| **OWASP编号** | **风险名称** | **与工具调用的关系** |
| ASI01 | Agent目标劫持（Goal Hijack） | Agent逻辑依赖松散治理的编排和自然语言输入，无法可靠区分合法指令和攻击者控制的内容，导致工具调用目标被动态操控 |
| ASI02 | 工具误用与漏洞利用 | Agent可能以不安全或非预期的方式使用合法工具，如删除有价值的数据、过度调用高成本API或渗漏信息 |
| ASI03 | 身份与权限滥用 | Agent上下文中缓存的凭据、API密钥或跨互联系统保留的对话历史，被攻击者利用来复用缓存密钥、提升权限或泄露先前会话的数据 |
| ASI04 | Agentic供应链漏洞 | Agentic生态系统在运行时动态组合能力，即时加载外部工具、插件、数据集，允许欺骗性行为或隐藏指令直接注入Agent执行链（即MCP工具投毒攻击的底层机制） |
| ASI05 | 意外代码执行（RCE） | 在「vibe coding」等工具中，攻击者可利用代码生成特性或嵌入的工具访问实现远程代码执行，绕过传统安全控制 |
| ASI06 | 记忆与上下文投毒 | 对手通过污染或植入可检索的上下文数据，导致未来的推理和工具使用出现偏差或不安全行为，且影响跨会话持续存在 |

**03**

**Proofpoint：基于代理完整性的意图检测**

###

2026年3月17日，Proofpoint 正式发布 **Proofpoint AI Security——一套面向企业 AI 智能体时代的全新安全解决方案。此次发布基于其对 AI 安全公司 Acuvity 的收购，标志着企业安全从"身份与流量可见性"迈向****意图验证**（Intent Verification）的全新阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/fRp5p4jMuDQjdXQXUMBDtPtLS0iaiaxVKblUBecgRUn30Lv2liaIUfnwcVib2D28Om4F0LpOd4oiah0psOJlRBHqewA/640)

三大核心能力

![](https://mmbiz.qpic.cn/mmbiz_png/jLdw7EZFJmIjAic1276gZeyjcsS9UMqa3VkvD2WgU11EyJAoVCSagkO3Kmia89jgusIXDficZIgTTb6ia32cibxVKgQ/640)

### ① 意图感知检测（Intent-Based Detection）

Proofpoint AI Security 通过意图感知检测模型，持续评估 AI 行为（无论由人类发起还是自主智能体发起）是否与原始请求、策略和预期目的对齐。通过分析 AI 交互的完整语义上下文，在损害发生前实时标记偏离行为，例如违规通信或数据泄露。

② 多平面控制（Multi-Surface Control）

解决方案覆盖 AI 使用的全部界面——端点、浏览器扩展和 MCP 连接——使组织能够：发现经授权与未授权的 AI 工具（如 ChatGPT、Ollama、MCP 服务器）；观测提示词、响应和数据流；施加访问控制与运行时策略执行。 这对 AI 驱动的开发者环境尤为关键。

**③ Agent Integrity Framework（智能体完整性框架）**

Proofpoint 同步推出业界首个 **Agent Integrity Framework**，定义了 AI 智能体以完整性运行的五大支柱：意图对齐（Intent Alignment）、身份与归因（Identity and Attribution）、行为一致性（Behavioral Consistency）、可审计性（Auditability）、运营透明度（Operational Transparency） ，并提供从"发现"到"运行时执行"五阶段的成熟度模型，帮助 CISO 按图索骥落地 AI 治理。

![](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCH6kGsNkDFSAO9saaNrHRR9HzyzZjFicGlDgXjNPm5SJMR0TejdjF0b3dpdNnVesSicSJumtJSU7twLueokRqb32EiaECicmHYRdhg/640?wx_fmt=png&from=appmsg)

Proofpoint CEO Sumit Dhawan 表示："人类和 AI 智能体面临相似的风险——两者都可能被操控，都可能采取偏离预期目的的行动，而传统安全从未被设计为验证意图。"

这一判断点明了 AI 安全的本质挑战：不是能否看见行为，而是能否理解行为背后的"意图是否合规"。

对于安全团队而言，Proofpoint 的这套框架提供了一个重要参考维度——在 AI Agent 大规模落地的今天，**行为意图的持续核验**（Continuous Intent Verification）将成为与传统 IAM、EDR 并列的核心安全能力。

**04**

**小结**

解决新问题，需要新方法。当大模型开始调用函数的时候，这类风险已经开始出现，但此时风险可控。当智能体开始无限使用工具的时候，这个风险已经不可回避。

意图安全可能未必是最好的方法，但目前看，还没有其它方法可用，这两个公司的思路值得借鉴。

需要Lasso白皮书的可以加微信

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rhmRSVBNbicqqPk023DYKjIYbFib5ApHYkNSb5v1sUIdZwswVE0jHVrSdwGz9GemfFIfnpVbarLoBdLY8rP5FltQ/640?wx_fmt=jpeg&from=appmsg)

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