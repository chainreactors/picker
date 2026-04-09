---
title: 【风险预警】美国会使用 claude 最新模型Mythos 攻击其他国家吗？
url: https://mp.weixin.qq.com/s/R7Rt5ndWPPTZsuNHvCFlvA
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:26:35.061190
---

# 【风险预警】美国会使用 claude 最新模型Mythos 攻击其他国家吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAj7ERR1cib6ZdcVF1WT8ltAp0o4KOcsTQcyHrFF2uKNJBd4EibE2ZQCkFsoGHQnb4stBo5ia84qoXJibx0wJR19T2uru6CeoqoC2mI/0?wx_fmt=jpeg)

# 【风险预警】美国会使用 claude 最新模型Mythos 攻击其他国家吗？

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAiazIX2jG0feKibqdBmvibVtibPyRu9FQa5aet9X4KIOicZF9xJaicvCiaBJgdxPp9yeuiazZZqAypZZ8XYHYaEntqjiaQ8LqFzXvDn68Iw/640?wx_fmt=jpeg&from=appmsg)

核心问题：在 Anthropic 与美国国防部正处于司法纠纷、Project Glasswing 的官方定位是「防御优先」的当下，NSA、CIA、U.S. Cyber Command 等美国情报与网络作战机构是否会、以及如何可能使用 Claude Mythos Preview 对外国目标开展进攻性网络行动？

## 背景介绍

2026 年 4 月 7 日 Anthropic 发布的 Project Glasswing 与 Claude Mythos Preview，在官方叙事里是一场「把前沿模型的网络安全能力优先交到防御者手中」的合作。但这份叙事背后埋着一个无法回避的问题——当一个模型被自己的制造商承认「大约等于一件网络战级武器」，而这家制造商与自己国家的国防与情报机构之间正同时存在**深度合作**与**激烈纠纷**的双重关系时，这件武器最终会不会以某种形式被用于攻击其他国家？

**核心研判一**（中高置信度）：NSA 通过「公开的 Glasswing 计划」合法获得 Claude Mythos Preview API 访问权的短期概率较低。12 家创始伙伴名单中没有任何美国情报或军事机构，Anthropic 公开披露的政府讨论对象仅限于 CISA、CAISI 两家定位为防御性的机构，Anthropic 自身使用政策明确禁止「未经系统所有者授权发现或利用漏洞」。Anthropic 与国防部自 2026 年 1 月起的冲突，以及 3 月 24 日加州北区法院批准的初步禁令，证明 Anthropic 在红线问题上具有相对稳定的立场。

**核心研判二**（中置信度）：然而，这个问题的答案不取决于 Mythos Preview 的 API 是否对 NSA 开放，而取决于三条**间接路径**。其一，Mythos 发现的漏洞在补丁发布前存在一个时间窗口，NSA 有能力、有意愿、也有历史先例去利用这个窗口；其二，Anthropic 明确支持「合法的外国情报与反情报任务」，这条政策例外给未来与情报机构的定制合作留下了合法通路；其三，Anthropic 国家安全顾问委员会成员中，包括前 NSA 网络安全总监、前 U.S. Cyber Command 执行主任 Dave Luber，这使得双方的人员与知识交换渠道独立于任何正式合同存在。

**核心研判三**（中低置信度）：比「NSA 是否使用 Mythos」更值得关注的，是 **NSA 是否需要 Mythos**。NSA 长期囤积漏洞、具备自研漏洞挖掘能力、拥有 EternalBlue 级别的历史先例。即便 NSA 永远拿不到一个字节的 Mythos Preview 权重，它也有充分的动力与资源自建一个对等能力的模型——用开源权重（Llama、DeepSeek、Mistral 等）作为起点、用自有算力与专业数据做微调、用它与 Anthropic 之间的人才流动补齐工程细节。从这个角度看，Glasswing 更像是一次「我们抢跑、你们也抢跑吧」的同步动员，而不是一次防御方对进攻方的单方面优势。

**整体置信度**：中。一手源（Anthropic 官方政策、官方博客、法院文件、DoD 声明）与权威媒体（Reuters、Fortune、Lawfare、Council on Foreign Relations、NBC News、The Intercept、TIME）提供了多源交叉验证的基础，但本分析所触及的几个核心问题——情报机构的真实意图、尚未公开的合同细节、漏洞信息在披露前的实际流动——本质上属于难以被外部独立验证的范畴。

**建议动作**：关注未来 90 天 Anthropic 承诺的公开复盘报告中对「与政府的合作结构」的描述；关注 Anthropic 诉五角大楼案的后续进展；关注 Mythos Preview 向「关键基础设施维护者」扩散的实际名单是否出现任何与情报社区关联的实体；关注美国国会围绕 VEP（漏洞处置流程）可能出现的新立法动议。

## 一、为什么这个问题值得严肃回答

先把问题摆清楚。这不是阴谋论式的猜测，而是一个有合理疑问基础、有历史先例可循、有政策文本可查的严肃分析问题。提出这个问题的依据来自三个完全公开的事实：

第一，Anthropic 自己在 Frontier Red Team 博客中写明，Mythos Preview 在通用 coding 与 reasoning 能力提升下出现的安全能力是**双刃的**——同样的能力既能修补漏洞，也能利用漏洞。原文的表述是「the same improvements that make the model substantially more effective at patching vulnerabilities also make it substantially more effective at exploiting them」。这不是对手或批评者的话，这是 Anthropic 自己的话。

第二，Anthropic 承认已经与美国政府官员就 Mythos Preview 的进攻与防御能力进行了持续讨论。Anthropic 官方 Glasswing 公告的原文把 Mythos 定义为「美国及其盟友必须保持 AI 技术决定性领先」的国家安全优先级问题。这段文字本身就是对「Mythos 不会只是一个防御工具」的暗示——它在用地缘政治语言为这个模型定位。

第三，NSA 过去十年有明确的漏洞囤积实践。2017 年 EternalBlue 通过 Shadow Brokers 泄露导致 WannaCry 与 NotPetya 两场全球性网络灾难的历史，是这个问题最重要的背景。任何涉及「先发现漏洞、后决定披露」的机制，都要在 EternalBlue 的阴影下被评估。

这三个事实合在一起，使得「NSA 等机构会不会使用 Mythos」成为一个必须认真回答的问题，而不是一个可以用「Anthropic 说它只用于防御」一句话打发的问题。

## 二、表层图景：Glasswing 说了什么，没说什么

先把 Anthropic 自己在 4 月 7 日公开的信息拆开，特别注意它没说的部分。

**说了什么**

* Mythos Preview 不向公众开放，仅向 12 家创始 partner（AWS、Anthropic 自身、Apple、Broadcom、Cisco、CrowdStrike、Google、JPMorganChase、Linux Foundation、Microsoft、NVIDIA、Palo Alto Networks）及另外约 40 家关键软件维护者开放；
* Anthropic 承诺最高 1 亿美元 API 使用信用额度；
* Anthropic 自称与 CISA（网络安全与基础设施安全局）与 CAISI（AI 标准与创新中心）等机构进行持续讨论；
* Anthropic 在公告中明确提到「securing critical infrastructure is a top national security priority for democratic countries—the emergence of these cyber capabilities is another reason why the US and its allies must maintain a decisive lead in AI technology」；
* Mythos Preview 会通过 Claude API、Amazon Bedrock、Google Cloud Vertex AI、Microsoft Foundry 四条路径向 partner 提供服务。

**没说什么**

* 是否向美国情报社区（Intelligence Community，简称 IC）提供任何形式的访问权；
* Anthropic 与 CISA、CAISI 之间的「持续讨论」具体涉及什么——是政策协调？是漏洞情报共享？是访问权协商？是安全评估？原文都没有说明；
* 40 家尚未公开名单的「关键软件基础设施维护者」中是否包含与情报社区有关联的实体；
* Mythos Preview 发现的漏洞在补丁发布之前的信息流——具体谁知道、谁不知道、按什么时间表披露、披露给谁；
* 除 Glasswing 之外，是否存在另一套针对政府客户的 Claude Gov 定制版本同样具备 Mythos 级能力，或计划在未来获得这种能力。

**研判**：Glasswing 官方叙事有意把焦点压缩在「防御」一个维度上，但它没有回答的问题恰恰是最值得追问的。尤其是第二点和第四点——CISA/CAISI 的讨论具体内容、漏洞披露前的信息流——决定了这个计划在事实层面的真实定位。不回答这些问题，就无法判断 Glasswing 是一个纯粹的防御项目，还是一个**定位为防御、但运作中客观上也为进攻方创造信息优势**的项目。

## 三、Anthropic 与美国安全国家的真实关系：一份被公开记录

要评估 Anthropic 会不会把 Mythos 直接或间接交给 NSA，必须先搞清楚 Anthropic 与美国国安体系的真实关系。以下均为多源交叉验证过的事实。

**与 CIA 和盟国情报机构的合作（2023 年底起）**

Anthropic 自 2023 年底起与美国中央情报局（CIA）和澳大利亚国家情报办公室（ONI）合作。公司雇用了前 Palantir 员工 Steve Sloss 作为对接美国情报机构的专人。这部分合作的细节公开披露极少，但 Anthropic 从未否认其存在。

**与国防部的合同链条（2024–2025）**

* 2024 年：Anthropic 首次与 Palantir 合作，允许国防部在 classified 网络上使用 Claude；
* 2025 年 7 月：国防部首席数字与 AI 办公室（CDAO）授予 Anthropic 一份两年期、上限 2 亿美元的 Other Transaction Agreement（OTA），用于原型化「推进美国国家安全」的前沿 AI 能力；
* 2025 年：Anthropic 向国防情报机构提供定制 Claude Gov 模型；
* 2025 年：Claude 被部署给劳伦斯利弗莫尔国家实验室（LLNL）的 10,000 名科学家使用，覆盖核威慑、能源安全、材料科学等方向；
* Anthropic 明确对外表态：Claude 已在 DoD 内部用于**情报分析、建模仿真、作战规划、网络作战（cyber operations）**。

注意最后一项——「网络作战」。这是 Anthropic 自己的表述，不是外部推测。

**Amodei 的公开立场（2026 年 2 月 26 日）**

2026 年 2 月 26 日，Anthropic CEO Dario Amodei 在与国防部谈判破裂的前一天发表声明，明确表示：「我们支持将 AI 用于**合法的外国情报与反情报任务**（lawful foreign intelligence and counterintelligence missions）。」Amodei 同时区分了两条他不会妥协的红线——针对美国人的大规模监控，以及完全自主的致命武器系统。

**研判**：Amodei 这段话的重要性怎么强调都不为过。Anthropic 的红线从来不是「不为美国政府的对外情报服务」，而是「不帮助美国政府监视自己的公民、不帮助美国政府打造无人干预的杀伤系统」。把这两个问题分开看，Anthropic 的立场其实非常清晰——**对内克制，对外开放**。这条立场在下一节会变得更重要。

**Anthropic 对 NSA 的直接表态**

根据 TIME 杂志引用 New York Times 的报道，Anthropic 在与五角大楼的谈判中明确告诉国防部，它愿意让国家安全局（NSA）将其技术用于**在 FISA 框架下收集的机密材料**。这句话的分量极大——它意味着 Anthropic 从未反对 NSA 使用其模型，它反对的只是 NSA 越过 FISA 授权边界去监视美国人。

**前 NSA 高官加入顾问委员会（2025 年 8 月）**

2025 年 8 月，Anthropic 成立国家安全与公共部门顾问委员会。委员会成员中包括 **Dave Luber，前 NSA 网络安全总监（Director of Cybersecurity at the National Security Agency）与前 U.S. Cyber Command 执行主任（former Executive Director of U.S. Cyber Command）**。Luber 有 38 年的情报界服务背景，专注于网络安全行动、国家级网络威胁与公私合作。

委员会其他成员还包括前 CIA 副局长 David Cohen、前代理国防部长 Patrick Shanahan、前参议员 Roy Blunt（前参议院情报委员会成员）、前参议员 Jon Tester（前参议院拨款委员会国防分委员会主席）等。

**研判**：一家 AI 公司的国安顾问委员会中出现前 NSA 网络安全总监 + 前 Cyber Command 执行主任的组合，说明 Anthropic 与 NSA/Cyber Command 之间存在制度化的、高级别的专业对话渠道。**这条渠道独立于任何正式合同存在**——也就是说，即使 Anthropic 与国防部的合同全部终止，这种知识与判断的交换也不会停止。Luber 的职责被官方描述为帮助 Anthropic「识别和开发高影响力应用，以加强美国及其盟友在网络安全到情报分析等关键领域的能力」。这段描述中「情报分析」是明确点名的方向之一。

## 四、NSA 的历史：为什么漏洞信息的时间窗口值得警惕

理解 NSA 是否会使用 Mythos，必须理解 NSA 在「拿到漏洞」与「披露漏洞」之间的历史行为模式。

**Vulnerabilities Equities Process（VEP）**

VEP 是美国政府用于决定「发现的零日漏洞是否向厂商披露」的跨机构流程。根据公开资料，VEP 由白宫国家安全委员会牵头，NSA 是其执行秘书处，由一个股权审查委员会（ERB）权衡每个漏洞的情报价值与公共风险。前 NSA 副局长 Richard Ledgett 公开声称「我们披露我们发现的大约 90% 的漏洞」——这个数字被多方引用，但从未被独立验证。

**NOBUS 原则**

NSA 历史上使用 NOBUS（nobody but us）原则作为是否保留一个漏洞的决策依据：如果一个漏洞被评估为「除了我们这样的国家级机构之外没有人能发现和利用」，它就倾向于被保留而非披露。这个原则被前 NSA 局长 Michael Hayden 公开讨论过。

**EternalBlue 先例**

NSA 发现 Microsoft Windows SMB 协议中的远程代码执行漏洞后，**将其保留了超过五年**，仅在发现 Shadow Brokers 已经窃取相关工具后才通知 Microsoft。Microsoft 在 2017 年 3 月发布补丁，Shadow Brokers 在 4 月公开 EternalBlue 漏洞利用代码，5 月 WannaCry 爆发，感染超过 150 个国家、超过 23 万台设备，英国国家医疗服务（NHS）大面积瘫痪。同年晚些时候 NotPetya 使用同一漏洞发动针对乌克兰的攻击，造成数十亿美元的全球连带损失。

**研判**：EternalBlue 的历史不是过去的阴影，而是对未来的警告。它确立了三个事实：

1. NSA 有能力发现高价值零日漏洞；
2. NSA 的默认倾向是保留而非立即披露，只有在保留的风险超过利用的收益时才会改变决策；
3. NSA 的"武器库"存在被泄露的风险，一旦泄露，全球平民与关键基础设施会承担主要后果。

**把这三点放回 Glasswing 的语境**：Mythos Preview 在几周内发现了数千个零日漏洞，其中许多是「跨度 10 年以上、分布在每一款主流操作系统与浏览器」的关键漏洞。Anthropic 承诺通过协调披露流程与厂商合作修补，并在 90 天后发布公开复盘。但**从漏洞被发现到补丁部署到全球多数系统，这个时间窗口通常以月甚至年为单位计**——尤其是在企业 legacy system、嵌入式设备、工业控制系统等领域。在这个窗口里，漏洞信息的知情范围越小越好。但 Glasswing 的结构意味着 12 家 partner + 40 家维护者 + 各家内部的安全团队会同时知情。这个知情面虽然小于完全公开，但远大于 NSA 内部的严控级别——客观上形成了一个**中等规模的漏洞情报共享圈**。

这个共享圈里是否会有信息以任何形式流向情报社区？这是本分析无法直接回答的问题，但必须提出的问题。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

微信扫一扫可打开此内容...