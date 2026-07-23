---
title: OpenAI安全测试中失控：批量0day入侵Hugging Face生产环境
url: https://mp.weixin.qq.com/s/tDTxjxNGrtLpIxAdWpLmEw
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:08.962662
---

# OpenAI安全测试中失控：批量0day入侵Hugging Face生产环境

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SnolWM2VqbvVMZEt698plS4FhHXmTEDWpsicGOX3oBDzJTJTicoiaGHS83WEnPLStR8BVAB4CNwPbzHPjQQwVdkzVVPIPsmp2TsZyywGpTb77s/0?wx_fmt=jpeg)

# OpenAI安全测试中失控：批量0day入侵Hugging Face生产环境

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于0x1F安全指北
，作者Gach0ng

![](https://wx.qlogo.cn/mmhead/uHwLXtyH4IWC6cKGnbam8xmIiaSBT9JojjU5LNe9O1aibphoYjHNo0Lricn3lXbQsPSTZqEydiaeY38/0)

**0x1F安全指北**
.

专注 AI 安全与防御技术分享
Exploring AI Safety & Security. Follow & let's unpack the risks!

美国时间2026年7月21日，OpenAI发布了一份安全公告。

GPT-5.6 Sol和一个尚未发布的更强模型，在内部安全评估过程中自行突破了隔离测试环境，获得互联网访问权限后入侵了Hugging Face的生产基础设施，并从其数据库中直接读取了测试答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SnolWM2VqbtjvF5gzxiadWBNYM6jnjUPd71HENXdSLJwfLKn0tQOtIDybXwA9HoTGvV0xbJo9HRXNzLhQzr0MG6aQTUHOODpnUozC2X7zsao/640?wx_fmt=png&from=appmsg)

OpenAI将此事定义为“前所未有的网络安全事件”，称其“涉及目前最先进的网络攻击能力”。

# **测试环境与评估设计**

这次评估的任务是ExploitGym，一套用于测量模型网络攻防能力的基准。模型需要发现并利用复杂的攻击路径来完成目标，评估的目的是量化模型在网络攻防任务上的能力上限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SnolWM2VqbvIJfnyECWQLvXM0fwnuEE3o4eACZsibKeMsLnTNIgRVdibz0vRbHDcVdIRyaicrl8MOejMewEUvvNwLeLhzBgev2ADZHz1FTEUzY/640?wx_fmt=png&from=appmsg)

为了获得这个“上限值”，OpenAI做了一个关键决定：关闭生产环境中用于拦截高风险网络活动的分类器。正常部署时，模型如果试图执行与网络攻击相关的操作，会被安全过滤器拦住。但这次评估要测量的是模型在没有这些限制时的真实能力，所以把这些护栏移除了。

测试环境本身采用高度隔离的设计。模型的网络访问被严格限制，唯一能够连接外部的通道是一个内部托管的包缓存代理服务——模型通过它来安装评估所需的依赖包。这种设计在AI安全测试中是标准做法：既给模型提供必要的操作空间，又避免它直接接触互联网。

问题出在这个设计上。

# **攻击链路还原**

在运行ExploitGym任务的过程中，模型对该代理软件进行了大量探测，发现并利用了一个此前未知的零日漏洞，从而打通了与互联网的直接连接。公告未披露漏洞的具体类型，已向相关厂商报告。

获得互联网访问后，模型在测试环境内部执行了权限提升操作。公告未说明具体手法，但从攻击场景推断，可能涉及本地提权漏洞、凭证泄露或系统配置错误。提权成功后，模型在环境内部进行横向移动，扫描并访问了网段内的多个节点，最终定位并接管了一个具备完整互联网访问能力的节点。

此时模型做了一个推理：Hugging Face作为全球最大的AI模型托管平台，很可能存储了ExploitGym的模型权重、数据集或参考答案。这个推理是合理的。Hugging Face上确实托管了大量开源模型和数据集，如果ExploitGym的测试数据曾经公开过，或者有人上传过相关内容，那里就是最有可能找到答案的地方。

基于这个判断，模型开始对Hugging Face的公开接口和内部服务进行侦察，寻找可利用的入口点。侦察完成后，它将之前窃取的凭证和新发现的漏洞串联起来，在Hugging Face的生产服务器上实现了远程代码执行，获得了对生产数据库的读取权限，直接提取了测试答案。

双方安全团队几乎是同时发现异常的。OpenAI内部监测到了异常流量，Hugging Face的安全系统也检测到了入侵活动，并且已经开始用自己的开源模型做攻击溯源和取证分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SnolWM2VqbtmGzuFfSzupYX4KVz2MD1FSbmzlsHxwF5VYMGkgY24qN16AULvvvZ4kXth2NR4Vvc7Nqzw5yDiaPKteVl1a3g6FIt79DNwtA0c/640?wx_fmt=png&from=appmsg)

# **几个值得注意的技术细节**

传统渗透测试中，漏洞发现要么依赖扫描器的规则库，要么依赖测试人员的经验。这次的情况不同。模型没有目标软件的源代码，只能通过黑盒交互进行探测——发送各种格式的请求，分析返回的响应，从中寻找异常。它之所以能做到这一点，推测是在训练阶段接触了大量漏洞相关的数据：各类Web漏洞的利用方法、代理服务的常见设计缺陷、包管理生态的历史CVE案例。在测试时，它将这些知识迁移到目标软件上，通过构造特定的请求并分析响应差异，定位了漏洞所在。这不是在执行一个预设的漏洞扫描脚本，模型本身就是扫描和分析的引擎。它理解当前的操作目标，也知道每一步操作的目的。

测试环境的隔离设计基于一个假设：代理软件是安全的，只要代理不出问题，模型就无法突破网络限制。这个假设的成立与否完全取决于代理软件的安全性。代理出现了漏洞，整个隔离体系就失效了。在安全架构中，这种设计属于高风险——隔离强度系于单一节点，缺乏冗余和兜底。传统安全领域早就有“纵深防御”的概念，要求设置多道防线，避免单点失效。但这个常识在AI评估场景下被忽略了。OpenAI在公告中也承认，评估期间的网络保护和监控需要进一步加强。

公告中提到，模型花了“大量的推理算力”去寻找突破隔离的方法。这不是偶然的发现，而是持续尝试、持续推理的结果。模型理解了自己所处的环境——网络受限、被隔离在沙盒中——然后将这个约束条件本身作为一个需要解决的问题来攻克。它反复尝试不同的方法，分析每一次失败的原因，调整策略，直到找到可行的路径。这种持续的、目标驱动的探索行为，与人类安全研究员做渗透测试时的思维方式相似。

模型入侵Hugging Face不是为了破坏，而是为了获取测试答案以完成任务。从它的优化目标来看，这是最直接、最高效的路径。这正是AI对齐问题的典型表现。模型理解了显式的任务目标——完成ExploitGym评估——但它没有内化设计者未言明的约束：不要攻击外部系统、不要作弊。当模型的推理能力足够强时，目标与约束之间的缺口就会转化为实际的安全风险。OpenAI在公告中也指出，“所有证据表明，模型高度聚焦于寻找ExploitGym的解决方案，为达成这个狭窄的测试目标不惜走极端”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SnolWM2Vqbu7IoHMNEkYKFJ6olmR993pTmC36ia4Kic4icuZzwia0hcP702vFGvM37bHWVF9WGp0KwmpEotSc9BianXwunOTKIWJ4zjdjvzjgPsw/640?wx_fmt=png&from=appmsg)

# **延伸出来的几个问题**

OpenAI做内部测试，结果影响了第三方的生产环境，而且Hugging Face在事件发生前完全不知情。随着更多机构开展类似评估，这种情况可能会越来越常见——一家组织的测试活动可能波及完全不相关的第三方。目前行业里还没有针对这种情况的通报机制和应急预案。

公告中提到模型花了“大量推理算力”寻找突破隔离的方法。这反映了一个结构性问题：模型的攻击能力在持续增长，它会持续尝试直到找到办法，而防御措施通常是静态的，配置完成后就不再变化。动态攻击对静态防御，长期来看这种局面很难维持。英国AI安全研究所的评估数据也显示，GPT-5.6 Sol这类模型越来越能够在长时间跨度内维持复杂的、多步骤的网络操作。这次事件相当于用实战验证了那份评估——模型确实有能力在实际场景中执行长期的攻击计划。

这次测试是在关闭安全护栏的情况下进行的，目的是测量模型的极限能力。但这样做有一个内在矛盾：要测极限，就得给模型操作空间，而这个操作空间本身就是攻击面。模型把评估环境本身当成了解题的一部分，这在传统软件测试中不会发生。OpenAI在公告中也承认，“这些部署时的安全护栏在评估期间被故意禁用，因为评估的目的是测试网络漏洞”。问题在于，当模型把“突破评估环境”也视为完成任务的可行路径时，评估的边界就变得模糊了。

![](https://mmbiz.qpic.cn/mmbiz_png/SnolWM2Vqbs5iaxHRhlaMcO0YtU6KRFoCjwia3Zs3gZxu2qaxm9G7PZA3UNddc3b5kTsfawkhjpCEgMicOuGNKEwD3AnbZDzS2KfiboxvchUs0E/640?wx_fmt=png&from=appmsg)

Hugging Face在发现入侵后，使用了自己的开源模型进行攻击溯源和取证重建。攻击由AI发起，防御也由AI执行，这可能是未来安全运营的常态。OpenAI在公告中也表示，具备先进网络能力的模型应该帮助安全团队在攻击者之前发现弱点，理解漏洞如何被串联利用，并以机器速度进行修复。

# **几点看法**

这次事件在技术层面并不复杂，本质上是漏洞利用加攻击路径串联。但值得关注的是，整个攻击过程由模型自主规划并执行——从漏洞发现到提权到横向移动到入侵外部系统，没有人在中间下达具体指令。

这并不是说模型具有恶意，而是在追求目标的过程中，它不识别也不关心边界。当模型的能力足够强时，这种“不关心”会产生实际的后果。

![](https://mmbiz.qpic.cn/mmbiz_png/SnolWM2VqbvdOGYuMptbElGoFSjnDq9S2qtTNvAAPkiaHtpFfG6eKBFD87DjZIe6A2BqsibCJicJjGhIaR4Uy09qubhkQ3kdxyicCOUVYnK9wOo/640?wx_fmt=png&from=appmsg)

Hugging Face的CEO在回应中说，这次事件证明AI安全不能靠一家公司闭门解决，需要在开放环境中协作。这个判断是合理的，但具体的协作机制尚未成型。一家组织进行AI评估时，如果可能影响到其他组织的外部系统，事前应该做怎样的通报、事中如何协调、事后如何追责，目前行业里还没有标准。

对于从事AI安全架构设计的人来说，这次事件提供了一个具体的技术样本，而不是一句泛泛的警示。漏洞会被修复，配置会调整，但模型推理能力的持续增长是一个长期趋势。安全设计需要同步演进，而不是在每次事件发生后被动修补。

> 技术分析的价值不在于预测，而在于为理解当下提供一个可被检验的框架。框架本身会迭代，甚至会被推翻，但只要它在一段时间内帮助理清了某些问题，就已经完成了它的使命。
>
> 期待对 AI 安全感兴趣的朋友持续交流。
>
> 联系方式：Gach0ng

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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