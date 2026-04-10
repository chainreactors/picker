---
title: 发现 33 个 OpenClaw 与 Linux 内核漏洞后，我们也从 Claude Mythos 看到了安全攻防的下半场
url: https://mp.weixin.qq.com/s/Nh8sx89AaMTlhSu4YdtqWA
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:37.090143
---

# 发现 33 个 OpenClaw 与 Linux 内核漏洞后，我们也从 Claude Mythos 看到了安全攻防的下半场

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9icASLQUQzvagsuKAGgLxMSfU1QNAuf5sfjHOKMoltFNNWhlIEPb62wwcHabFeRmaa5nwAiaU2j4Qn2nQw4oaaCHJEJyRFW2ibokiaelpxE5P8Y/0?wx_fmt=jpeg)

# 发现 33 个 OpenClaw 与 Linux 内核漏洞后，我们也从 Claude Mythos 看到了安全攻防的下半场

腾讯安全应急响应中心

![]()

在小说阅读器中沉浸阅读

2026 年 4 月 7 日，Anthropic 联合 Apple、Google、Microsoft 等 45 家机构发布 Project Glasswing 计划，并宣布其尚未公开发行的前沿模型 Claude Mythos Preview 在所有主要操作系统和浏览器中发现了数千个 0day 漏洞，并能全自主完成漏洞利用代码的开发。有安全专家判断：开源权重模型可能会在 6 个月后追平，届时每个勒索软件团伙都能将漏洞快速、低成本武器化。漏洞攻防的整条时间链正在被 AI 整体压缩，速度比大多数人预期的更快。

近期，朱雀实验室蓝军 Bot（基于多Agent的自动化漏洞挖掘与攻防演练平台） 也完成了对 OpenClaw 与 Linux 内核等目标的快速挖掘，累计发现了 33 个 0day 漏洞，其中包含 17 个严重与高危漏洞。全部漏洞均已提交上游社区修复并获得 OpenClaw、Linux 内核等项目的官方公开致谢。

坦率地讲，数字本身不是最关键的。真正值得关注的，是这批结果和 Mythos 的发布指向了同一个结论：安全攻防下半场拼的已经不是能不能找到洞——是谁能先于攻击者把关键风险打出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvaCf7At0KrQabBvypBcImrndHcvh1nnLmG2RpGM8m1h7E2qmXUu7Xs0Bg87EqKK8F7rSNpqqVdjxf9HlKV7e0TH9iagoKmHRRIo/640?wx_fmt=png)

朱雀实验室报告的多个 OpenClaw  高危漏洞获得官方致谢

**1**

**变化的不只是洞的数量**

**是整个攻防节奏**

很多人觉得现在就是洞变多了。不只是。真正变的是整条链的节奏。

以前挖 0day 更像老师傅手工打磨一把刀，你得有手感、有经验，在同一个代码库里泡很久才能摸到一个像样的口子。现在，这门手艺正在被 Agent 批量复制。被改写的不只是漏洞数量，是从漏洞被引入、被发现、被验证到被利用准备的整条时间链。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvbdn1J3iahWPtibf6pqOQ8RhYKDDvndgia6UNQg0gFEWVBKU9KXkG2CSPHJVLMgyauDfiaWI2G9AjNyf5LukB2F58uibiawTFqdoE6icI/640?wx_fmt=png)

**1.1**

**漏洞为什么来得更快**

Vibe Coding 时代下一个越来越普遍的现实正在被摆到台面上：代码生成越来越快，但整体安全性没有同步变强。云安全联盟 2026 年 4 月的报告给了侧证：AI 辅助开发后的代码提交速度是传统的 3 到 4 倍，但安全风险发现率增长了 10 倍，特别是架构设计缺陷增加了 153%。大模型擅长避免输出 SQL 注入这类明显的漏洞代码，但容易忽略架构层的系统性安全缺陷。进入业务环境的，不只是更多代码，而是更容易带着缺陷一起进入生产的代码。

**1.2**

**漏洞为什么被更快发现**

知名安全研究员 Thomas Ptacek 的判断很关键：漏洞研究里大量工作本质上就是模式匹配、约束求解和不厌其烦地试，恰好适合交给大模型。过去因为不热门、太分散、人工上不划算而逃过审计的那些目标，现在全进了自动化扫描清单。去年 Google Big Sleep 能发现传统 Fuzzing 长时间没触发的问题，已经不只是提效——这是把漏洞发现从手工作坊推向工业化。Claude Mythos 就是这条线上最新的里程碑。

**1.3**

**企业为什么必须正面接招**

该警惕的不只是开源维护者忙不过来，而是外部黑客也在用同样的 AI 能力做大规模、自动化的攻击准备。麦肯锡内部 AI 平台就曾被黑客 Agent 在 2 小时内全自动打穿——利用 Agent 实现了机器速度的 API 测绘、漏洞链利用与数据窃取，甚至直接篡改了其 AI 业务平台的 System Prompt。

这就是我们说的下半场。过去安全团队更像定期巡检，现在更像在和一条不断提速的风险流水线赛跑。而流水线另一头，是同样在提速的自动化攻击能力。

**2**

**33 个 0day 漏洞背后：**

**蓝军 Bot 如何排雷**

朱雀实验室从 2023 年开始做蓝军 Bot，经过多个版本迭代，最新版本聚焦两条主线：一条是**AI 基础设施的软件供应链漏洞排雷**——33 个 0day 均已进入公开或修复流程，其中包含 17 个严重与高危漏洞，涉及OpenClaw、Linux内核、Langflow等项目；另一条是**真实业务系统实战演练**——蓝军 Bot 已在多个重点业务的蓝军演习中发现了大量有实际影响的漏洞并协助修复。

**2.1**

**软件供应链排雷：****先把 AI 基础设施安全里的坑排出来**

像 OpenClaw 这样的开源 AI Agent 框架增长快、进入业务栈快，同时处在沙箱、插件、认证、配置这些高风险边界上。一旦进入真实业务环境，风险会直接传导到企业自己的身份体系、敏感配置和供应链安全。蓝军 Bot 的第一大目标，就是把软件供应链里最值得优先排的雷排出来。

**在短时间内，蓝军 Bot 累计发现了18个OpenClaw漏洞，其中包含了10个高危漏洞，均已修复并获得了OpenClaw官方的公开致谢，大家可以通过A.I.G（AI-Infra-Guard）(https://github.com/Tencent/AI-Infra-Guard)的“OpenClaw安全体检”功能进行快速风险自查。** 这意味着这些修复不只保护了腾讯自身的业务环境，而是直接回馈到了 OpenClaw、Linux、Langflow 等开源生态的每一个下游用户。对于正在大规模采用这些 AI 基础设施组件的全球企业和开发者来说，这批修复就是他们软件供应链上少踩的雷。

展开三个最有代表性的 case——它们各自说明了不同层面的价值。

**OpenClaw 环境变量泄露漏洞（高危，GHSA-jccr-rrw2-vc8h，官方致谢）。** OpenClaw 是目前最活跃的开源 AI Agent 框架之一，大量企业基于它构建云上 Agent 产品。它真正危险的地方不只是"很火"，而是一旦部署，就能调用云服务器上各种敏感数据与工具权限。这个漏洞的问题出在 jq safe-bin 策略上：OpenClaw 为了避免数据泄露，在默认可执行的白名单工具参数中禁掉了 env 关键字，但漏掉了 jq 内置的 $ENV 对象，攻击者借此绕过安全策略读取服务器环境变量中的配置信息与密钥。一旦攻击者拿到 AK/SK、Git 凭证、模型 API Key 等密钥，往往就是后续更多深度渗透动作的起点。**该漏洞已获 OpenClaw 官方致谢，安全补丁已合入主线，所有使用 OpenClaw 的企业和开发者都能直接获益于这次修复。**

**Langflow Agentic Assistant 执行链漏洞（严重，CVE-2026-33873）。** 这个洞有意思的地方在于，它不是传统意义上的老洞型，问题出在 AI 功能链本身：Agentic Assistant 的验证阶段会直接执行 LLM 生成的 Python 代码，已认证用户无需管理员权限就能通过影响模型输出在服务端执行任意代码。它代表的是一类通用 Agent 框架共有的新风险——模型输出、工具调用和执行环境之间的边界被打穿。这些漏洞已同步更新至我们开源的 AI 红队安全测试平台 A.I.G（AI-Infra-Guard）(https://github.com/Tencent/AI-Infra-Guard) 的 AI 基础设施漏洞库中，**为社区用户提供更早的风险预警与检测能力，推动整个 Agent 框架生态的安全水位提升。**

**Linux 内核 Bluetooth 漏洞（高危，CVE-2025-39981/39982）。** 蓝牙 MGMT 模块的 use-after-free，竞态条件下 pending 结构被提前释放，可导致内核崩溃乃至提权，影响服务器可用性与数据安全。我们还在 Rxrpc 等多个内核模块中有更多发现。Linux 内核这种被全球安全团队反复锤炼多年的目标，代码规模大，审计历史长，修复链路复杂——蓝军 Bot 结合 Agent 的代码理解能力与 Fuzzing 框架针对性优化了底层内核漏洞的挖掘能力。**这些补丁已合入 Linux 内核主线，受益的不只是腾讯自身的服务器集群，而是每一台运行 Linux 的设备。**

三个 case 覆盖了三层：热门 AI Agent 框架的上游排雷、通用 Agent 框架生态的风险打样、底层操作系统基础设施的供应链安全。而它们的共同点是：**每一个修复都通过负责任的漏洞披露流程回馈到了开源社区，惠及全球开发者。**

**2.2**

**真实业务系统实战演练：****把自动化渗透测试能力打进业务现场**

除了通过供应链排雷解决上游风险，业务系统演练解决落地实战也同样重要。

朱雀蓝军 Bot 已在腾讯内部业务系统演习中广泛落地使用。由于每一个漏洞都经过了真实验证，大大降低的了蓝军专家人工介入成本。

此外，为了验证与同类 AI 自主渗透工具的对比效果，朱雀蓝军 Bot 还测试了 XBOW Security Benchmark 共 104 个题目，成功完成了其中的 102 个挑战（98%），超过了最热门的开源 AI 渗透项目 Shannon（GitHub Star 37.4k），在基础覆盖率上也超越了传统人工黑盒测试水平。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvbvict6fbee4unBWacstr2eNpKMogxzGibolgz2rhCJJ7IOXicsPFnOWRjA04pB3Priav32oP1wAOJS9lS1t0dtLIawFzS3tOxJ3oI/640?wx_fmt=png)

这些成果背后是蓝军 Bot 4.0 的 Agent Teams 和 Harness Engineering 体系，当前这套方案已经能在黑盒、白盒和真实业务环境里稳定运行。复杂漏洞的自动化验证与利用还有不少硬骨头要啃，但每一轮模型升级都在让 Harness 的放大效应更明显。

**3**

**安全攻防下半场的**

**三个判断**

**3.1**

**漏洞的货架期正在快速缩短，传统的安全演习节奏已经 Cover 不住风险了。**

过去一个漏洞从引入到被发现，缓冲期可能长达几个月甚至几年。现在这个窗口在急剧压缩：Mythos 在多个项目中挖出存在 10 到 27 年的高危漏洞，全球安全团队多年审计、数百万次 fuzzing 都没找到；CrowdStrike 的判断更直接——漏洞从被发现到被利用，窗口已从数月缩短至数分钟。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9icASLQUQzvZXNVqpozTvSvPIynZvcicHNoPBPaYL8DLvh6gxn4nbpCcqeP12EB0AFFYxkUMGNXiazyu0Q5Xgd5OhPr4oBsxzGUlTbL6iamKjIM/640?wx_fmt=png)

HackerOne IBB 暂停接收报告、Google 叫停 AI 提交漏洞报告、cURL 关闭赏金通道，信号很一致：发现速度已经快过旧有处理链路。当外部黑客也可以用 AI 持续扫描你依赖的每一个开源组件，甚至把漏洞发现、验证和利用准备串成自动化流程，企业自己的前置发现能力就必须跟上。否则攻击者会比你先到。

**3.2**

**能找到洞越来越不稀缺，差距在谁能更早、更准地把有价值的风险打出来**

发现漏洞的门槛正在被 AI 大幅拉低。Thomas Ptacek 说得直接：现在所有人都有了一个通用的拼图求解器。以后最不值钱的，可能就是"我又扫出一堆漏洞"。

但这不等于真正的能力差距消失了。拉开距离的是谁能更早盯住最值得打的目标，谁能把结果做成必须认真对待的可信输入。Anthropic 发布 Glasswing 时的做法就是同一个逻辑：最强能力先交给 45 家核心厂商与防御方，让它们在攻击者获得同等能力之前完成关键基础设施的排查和加固。这套"防御者先手"的思路和朱雀的定位一致，就是先于攻击者把关键风险打出来帮助业务加固，同时也**通过****负责任的漏洞披露，让整个开源生态更安全。**

**3.3**

**AI 拉低了找洞门槛，但安全专家的判断力和 Harness 工程化能力依然稀缺**

很多人看到 AI 能批量找漏洞，第一反应是普通人是不是也能带着 Agent 下场了。能下场，但很难真正打出有价值的结果。因为真正难的部分，从来不只是把问题扫出来。

同一个模型配不同的 harness，效果差距是数量级的。Anthropic 自己的数据就是例证：Opus 4.6 裸跑做 exploit 开发成功率接近零，但在人工指导 harness 下成功利用了 FreeBSD NFS 远程代码执行漏洞。蓝军 Bot 从 1.0 到 4.0 也是同理——能力跳变不只因为换了更强的模型，更因为 harness 从单 Agent 裸跑进化到了全自主多 Agent 编排。

扫出问题只是起点，harness 背后的专家判断力体现在三件事上：

* **选对方向。** 我们这次优先盯 OpenClaw，不是因为它热，而是因为它已经进入大量企业的技术栈，沙箱、插件、认证边界本身就是高风险攻击面；Linux 内核纳入目标，因为它直接处在业务和终端的底层依赖上。真正的能力不是目标越多越好，而是知道先打哪里最有价值。
* **从点打到面。** 普通人用 Agent 常见的是扫到一个点报一个点，拿到一个中危就换下一个目标。Mythos 给出了行业级参考：自主将 3-4 个内核漏洞链成完整提权链，把 4 个浏览器漏洞串成从 JIT heap spray 到沙箱逃逸的全链 exploit。蓝军 Bot 在 OpenClaw 这轮审计中，同样在关键攻击面上做到了持续追打和系统性覆盖——18 个漏洞不是 18 次独立扫描的结果，而是顺着同一类防护机制持续深挖的产出。
* **严格验真。** AI 能产出大量"像漏洞的东西"，但不是每个都值得进入正式链路。Anthropic 在 Glasswing 中用最强模型扫出数千个 0day，仍要求专业安全承包商逐份人工审核——198 份已审报告中 89% 的严重等级与人类专家完全一致，但他们明确表示目前仍不敢放松人工验证标准。**我们的 33 个 0day 全部获得上游项目官方确认与致谢，靠的是把验证标准和结果交付做得足够准确和严格**——这也是为什么这些修复能被上游社区快速采纳并合入主线，真正转化为整个生态的安全收益。

我们相信，朱雀蓝军 Bot 这次的 33 个 0day 只是一个开始。当 AI 把找漏洞的门槛拉低，真正拉开差距的是谁更知道让 Agent 去打哪里、打多深、怎么稳定可控地打、哪些结果值得交付。 能驾驭 AI、能把前置风险发现做得更早、更准、更适配业务的安全蓝军团队，会让业务团队在 AI 时代跑得更快的同时也跑得更安全。

**腾讯朱雀实验室**

腾讯朱雀实验室（Tencent Zhuque Lab）是腾讯安全平台部于 2019 年成立的顶尖 AI 安全实验室，专注于 AI 安全领域的实战攻防与前沿技术研究，研究方向涵盖大模型安全、AI 智能体安全、AI 赋能安全与 AI 生成检测等领域。团队多次协助英伟达、谷歌、微软等知名厂商以及OpenClaw、Linux、Hugginface等开源社区修复大量高危漏洞，并获得官方公开致谢。先后推出开源 AI 红队安全测试平台 A.I.G（AI-Infra-Guard）及朱雀 AI 检测助手等标志性AI安全产品。研究成果广泛发表于 Black Hat、DEF CON、ICLR、CVPR、NeurIPS、ACL 等国际顶级安全与 AI 学术会议，并出版专著《AI 安全：技术与实战》。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

腾讯安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

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