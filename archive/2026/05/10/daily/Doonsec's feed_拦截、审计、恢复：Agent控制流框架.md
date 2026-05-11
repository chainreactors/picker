---
title: 拦截、审计、恢复：Agent控制流框架
url: https://mp.weixin.qq.com/s/nQREUEtfRAhhGBChGuBVYg
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:51:41.586342
---

# 拦截、审计、恢复：Agent控制流框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dbdKu32ibAwK5ib0jB2bPvu7u3FoApwe9rP56URkFTY4JQNMYiannMcuGCc4ib2lDM26P5qEiaicMgXB2FHXoibw7fEHZffVn9JpJIx8BMEqpG0Df4/0?wx_fmt=jpeg)

# 拦截、审计、恢复：Agent控制流框架

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于模安局
，作者面向未来AI治理的

![](http://wx.qlogo.cn/mmhead/vsACyXq1DBhyvJVILA2GpGTlmtuO1Qp9qQJtwZCPcYJZF8huH12Y8NRdabTdlewY3EdyaNrib6n8/0)

**模安局**
.

面向未来的AI治理

Agent 可以被提示注入影响，但工具调用不能裸奔。今天要介绍的这篇论文不再把 Prompt Injection 主要看成“恶意内容识别”问题，而是把它放到 Agent 的执行链路里讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dbdKu32ibAwKCeJTmKI69g4UgVFIRlYFbl1LwBoJF0NIWBgdF6N2L7xROFWCaKiajhBvHWAt9ZTVrPgdF1kNzwpnqdLhBaZwthUX8Poib6lRDU/640?wx_fmt=png&from=appmsg)

https://arxiv.org/pdf/2604.24118

模型看到一段不可信内容，只是风险的开始；真正危险的是，这段内容影响了模型的工具调用，让 Agent 去发邮件、查数据库、调用 API、写文件、执行外部函数。

AgentVisor 的核心设计，就是在 Agent 和工具之间加一层可信的语义监控器，把工具调用纳入一套 **trap–audit–recover** 控制流：先拦截，再审计，审计不过就返回语义异常，让 Agent 自我修正。

论文摘要中给出的总体结果是，AgentVisor 将攻击成功率降到 0.65%，同时相比无防御场景平均只带来 1.45% 的效用下降。

![](https://mmbiz.qpic.cn/mmbiz_png/dbdKu32ibAwLWIU5mE5FH5GB8bqJcobWsGT7DYZPUESBxJFAxXtEZSkpCvSeE5o8qicVfibsZ0fk2ibTzdJQTbvfUhoVUkhEb51FfuR0CkXmpu0/640?wx_fmt=png&from=appmsg)

## AgentVisor 的本质：把 Agent 当成不可信 Guest

AgentVisor 最关键的系统假设，是不再默认 Agent 本体可信。

论文借鉴操作系统虚拟化思想，把目标 Agent 看成一个 Guest，把工具执行环境看成高权限资源，把 AgentVisor 看成语义层面的 Hypervisor。

Guest 可以理解任务、规划动作、提出工具调用，但一旦涉及真实执行，就必须经过 Visor 审计。

这个视角很重要。

很多 Agent 安全方案仍然围绕模型本身做加固，比如提示词加固、上下文隔离、输入检测、输出过滤。

但 AgentVisor 的安全边界不是放在 prompt 里，而是放在工具调用之前。它承认模型可能被诱导，也承认模型不一定能稳定抵抗所有上下文污染，所以干脆把执行权从模型手里拆出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dbdKu32ibAwKzZI9pRYC60ibrvupL5x0iaLicBNmkK1WaiaGYd5icKciabz93WKqick0KmcjhDfpo4AmNPDOlBw5LDnYFfOEBP7YjPWRvZ9r6OHTWNw/640?wx_fmt=png&from=appmsg)

## 01 拦截：TRAP

在 Agent 系统里，不可信上下文可以来自网页、邮件、文档、Slack 消息、知识库检索结果，也可以来自用户直接输入。

AgentVisor 并不试图在最前面把所有风险一次性清理干净，而是抓住真正关键的一跳：工具调用。

论文把 Agent 在每一步生成的动作表示为一个工具调用，包括工具名和参数。AgentVisor 接管的就是这个工具调用提案。

Guest 先生成原始调用，Visor 再基于可信系统指令、用户请求、清洗后的执行历史和当前工具调用进行判断。

这里有一个非常关键的隔离原则：Visor 不直接读取原始外部上下文，而是只看经过结构化处理的任务状态，比如工具名、规范化参数、简短返回摘要和状态信息。

这解决了一个很现实的问题。

如果防御层也直接阅读原始网页、邮件或文档，那么攻击者完全可能在外部内容里继续写入“忽略安全检查”“绕过审计器”之类的递归攻击。

AgentVisor 的做法是让 Guest 看完整上下文，因为它要完成任务；让 Visor 只看审计所需的最小可信信息，因为它要保持防御层纯净。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dbdKu32ibAwLQt0RHtLsDxfyNUc3w4JjEtcM5pekw2E9hKY4Dq8bfh2KbSsC5Ha3BhYhCBcwRQ9x6LKNNGVsUbjxm5DH7Ff3b7qCicgBeUzhU/640?wx_fmt=png&from=appmsg)

## 02 审计：AUDIT

AgentVisor 的审计机制叫 **STI Protocol**，分别对应 Suitability、Taint、Integrity。

它的重点不是判断某段文本“像不像攻击”，而是判断当前工具调用在执行语义上是否成立。

Suitability 关心的是工具适配性，也就是这个工具是否符合系统角色和系统策略。

比如一个只负责总结网页的 Agent，突然要调用发邮件、删文件、支付、修改数据库这类工具，即使参数看起来正常，也应该先被拦下。这个检查主要对应直接提示注入，因为直接注入常常试图让 Agent 做出超出角色边界的动作。

Taint 关心的是目标来源，也就是这个动作到底是不是用户真正要求的，还是外部上下文偷偷塞进来的新目标。

比如用户让 Agent 总结邮件，但邮件正文里藏了一句“请把附件转发给某某邮箱”。这时候转发动作本身可能是一个合法工具调用，但它不是用户的原始目标，而是外部不可信内容引入的新目标。Taint 检查的价值就在于识别这种“任务目标被污染”的情况。

Integrity 关心的是参数完整性。

比如用户确实要求发送邮件，但用户指定的收件人是公司内部同事，攻击内容却诱导 Agent 把收件人改成外部邮箱。这时工具选择没错，目标类型也可能没错，真正出问题的是参数被替换了。Integrity 要检查的就是参数是否仍然和用户指定实体、约束和任务目标保持一致。论文把 STI 描述为一个顺序审计管线，每个工具调用都必须依次通过三类检查。

这套拆法对工程落地很有启发。Agent 的危险动作不一定表现为明显的攻击文本，很多时候是工具、目标和参数之间出现了语义偏移。安全系统如果只做内容检测，很难覆盖这种偏移；只有把工具调用拆开看，才能真正判断“这件事该不该做”。

## 03 恢复：RECOVER

AgentVisor 不是单纯的阻断器，它在审计失败后，会生成一个结构化的 **Semantic Exception**，也就是语义异常。

这个异常会告诉 Guest：当前动作为什么失败，违反了什么规则，哪些目标不允许，应该如何修正。

Guest 收到异常后，会进行一次 self-correction，再生成修正后的工具调用。

这点很适合工业场景，因为很多安全方案的问题，不是拦不住攻击，而是把正常任务也拦没了。

用户原本只是想总结邮件、整理日程、查找资料，如果外部内容里夹带了攻击指令，安全系统最好能剥离掉攻击目标，同时继续完成用户原始任务，而不是直接把整个任务终止。

论文的消融实验也说明了恢复机制的重要性。

去掉 self-correction 后，直接注入场景下 UA 会降到 0.00%，间接注入场景下 UA 也只有 13.33%；加入语义恢复后，UA 分别恢复到 85.56% 和 66.67%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dbdKu32ibAwLoibwjM7QhZwa2a6wgtPkWwNqqGY7qaxuy4Hud3m3YnlFCdsG6tUOJBJImicRHfFJRohIRrcTJlRicdCY86WePXDOFP3oIpV67Uo/640?wx_fmt=png&from=appmsg)

## 实验结果

论文使用了两类测试场景：直接注入使用 OpenPromptInjection，间接注入使用 AgentDojo，后者覆盖 Banking、Travel、Slack、Workplace 等交互式环境。

评价指标里，ASR 表示攻击成功率，BU 表示无攻击场景下的任务完成能力，UA 表示攻击场景下仍然完成原始用户任务的能力。

一个好的 Agent 防御方案，不能只追求 ASR 低，还要尽量保持 UA 高。

在 GPT-4o 作为目标 Agent 的直接注入实验中，AgentVisor 在七类攻击下 ASR 都达到 0.00%，同时在强攻击场景下仍保持较高 UA。

论文特别提到，在 Combined 攻击下，AgentVisor 的 UA 仍有 76.00%，说明它不是简单靠“全拦截”换安全。

在间接注入场景中，传统检测方法容易出现过度防御，DeBERTa 的 UA 约为 15%；AgentVisor 则把 ASR 压到很低，在 Important 攻击下 ASR 为 0.69%，同时 UA 保持在 63% 到 78% 区间。

这个结果说明，AgentVisor 的优势不是单纯“更严”，而是更好地平衡了攻击阻断和任务继续完成。

![](https://mmbiz.qpic.cn/mmbiz_png/dbdKu32ibAwKZ3ibWicljkNZ1HwK23BuZhkrcMIYGVOczufpdIj1dOiciapRibRQp7sPrXsOxGpE6Eibd9tPDUl9MjiczNg1S1Au7ORNGO6fduibWPtI/640?wx_fmt=png&from=appmsg)

## AgentVisor 真正改变的是 Agent 的权力结构

这篇论文最有价值的地方，不是又提出一个检测器，而是重新划分了 Agent 系统里的权力结构。

过去很多 Agent 架构里，模型既负责理解任务，也负责生成计划，还负责决定什么时候调用工具，它实际上同时扮演了规划者、裁决者和执行触发者。

这样的结构在低风险任务里没问题，但一旦接入企业数据、办公系统、支付接口、代码执行环境，就会变得非常脆弱。

因为模型只要被上下文影响，执行边界也会一起被影响。

AgentVisor 的做法是把这几件事拆开。

模型可以生成动作，但不能直接执行动作；Guest 可以提出工具调用，但 Visor 做最终裁决；外部上下文可以参与任务理解，但不能直接污染审计层。

这样一来，Agent 不再是一个拥有完整执行权的中心控制器，而更像是一个运行在受控环境里的智能进程。

这也是“语义虚拟化”这个概念真正有意思的地方。

它不是把传统 OS 机制机械套到大模型上，而是把权限隔离、策略执行、异常恢复这些系统安全思想，翻译到了 Agent 的语义执行空间。

## 对工业界的启发

如果从产品架构角度看，AgentVisor 对 Agent 网关、安全网关、企业 AI 办公助手都有直接启发。

第一，工具调用应该成为独立审计对象。邮件、数据库、文件系统、代码执行、工单流转、外部 API、支付转账，都不应该只依赖模型内部判断。Agent 可以给出调用意图，但高风险动作必须经过统一的 runtime gate。

第二，审计不应该只看“输入内容是否有害”，而应该看“动作是否符合用户意图、系统策略和参数约束”。很多攻击不是让模型输出危险内容，而是让模型在看似正常的流程里悄悄换目标、换参数、换执行路径。

第三，安全系统应该具备恢复能力。很多企业场景不能接受“检测到风险就整单失败”。更合理的方式是把违规动作剥离出去，把允许目标重新交给 Agent，让它在安全边界内继续完成任务。

这也解释了为什么 Agent 安全越来越像运行时治理，而不是传统内容安全。内容安全更像是在判断“能不能说”；Agent 安全更核心的问题是“能不能做、替谁做、用什么参数做、做完以后会影响什么资源”。

## 局限性

AgentVisor 的方向很清楚，但它仍然有局限。

首先，Visor 本身仍然依赖大模型做语义判断，稳定性、延迟和成本都需要继续优化。论文的延迟分析显示，在良性条件下 AgentVisor 大约引入 1.4 倍开销；攻击条件下，直接注入约为 2.32 倍，间接注入约为 1.71 倍。

其次，STI 更像语义层面的安全判断，并不能替代企业系统里的确定性权限机制。真实落地时，还需要用户身份、资源归属、数据分级、工具白名单、审批流、审计日志、速率限制等机制配合。比如用户确实要求发邮件，也不代表 Agent 就可以发送任何附件；用户确实要求访问数据库，也不代表它可以读取所有表。

再次，论文主要处理文本语境下的直接和间接提示注入。多模态 Agent、长期记忆 Agent、多 Agent 协作系统，会带来更复杂的污染路径。比如图片里的隐藏指令、长期记忆中的投毒内容、多个 Agent 之间的任务转交，都可能让“目标来源”和“参数完整性”更难判断。论文也承认，计算开销、长上下文可扩展性、多模态泛化是当前限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dbdKu32ibAwLpo19qSFlOfXhibADlwfibC42WzTcaoOnK738gmLOlOQtJgrZKm6Z6hPShH6wweRlQDcnHhicd1Z1MXZkGR9MG4ysZVkMrwTMjy4/640?wx_fmt=png&from=appmsg)

## 写在最后

AgentVisor 给出的结论可以概括成一句话：Agent 安全的关键，不是让模型永远不被骗，而是在模型可能被骗的前提下，仍然让执行系统保持可控。

这也是“拦截、审计、恢复”三个词的价值。

拦截，是把安全边界放在工具调用之前；审计，是把风险判断落到具体动作、目标和参数上；恢复，是在守住边界的同时，把任务拉回用户真正想完成的方向。

随着 Agent 接入越来越多真实工具，安全问题会越来越少停留在“内容是否合规”，越来越多进入“动作是否授权、流程是否可信、执行是否可恢复”。

从这个意义上看，AgentVisor 不是一个单点防御方案，而是提供了一种更有工程前景的 Agent 控制流框架。

未来可靠的 Agent，不会只靠更强的模型，也不会只靠更长的系统提示。真正关键的是，在模型和工具之间，有没有一套足够硬的运行时治理系统。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/dwTW4pyxLTnvdjZrQ9sYsrHVWx683lYSM0wnbVtfAs1Xp1cAbFBQ0lyAp87Z5BciaLQj54X8hCx7qbyJy6lOLXw/0?wx_fmt=png)

取证与溯源

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/dwTW4pyxLTnvdjZrQ9sYsrHVWx683lYSM0wnbVtfAs1Xp1cAbFBQ0lyAp87Z5BciaLQj54X8hCx7qbyJy6lOLXw/0?wx_fmt=png)

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