---
title: 【AI安全】AWS Continuum出手！安全进入机器速度
url: https://mp.weixin.qq.com/s/BOm6CBZki-bK-odTZtbrcg
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:22.233965
---

# 【AI安全】AWS Continuum出手！安全进入机器速度

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHRG0jicReMIxxFRO15jUOGn5e6XPvZte12ibb7Kac1ISM3XribibU1XFj1fA7xicemmhKa3sM2AMFTfg4hl7EYBEMZvgB8saA7NcusA/0?wx_fmt=jpeg)

# 【AI安全】AWS Continuum出手！安全进入机器速度

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、漏洞暴增，旧安全流水线失速了 🔥

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

###### 免费课程持续更新

https://space.bilibili.com/452583051/lists/7870008?type=season

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

2026 年 6 月 17 日，AWS 发布了 **AWS Continuum**。它瞄准的并不是一个新扫描器，而是一个越来越明显的矛盾：AI 已经能以“机器速度”发现漏洞、推演攻击路径，企业却仍在用人工工单、跨团队会议和周期性审计处理风险。攻击与发现进入高速路，修复还堵在收费站。🚧

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHTX0oX0wUwv2nRh0zn9qf3EOozmXzRQMgujDAET6LrXLIGnGl09hy1nlxQGrBpGZWLfvLeT1Ze0LicRW9xVohVRLoWEdlobUq5Q/640?wx_fmt=png&from=appmsg)

AWS 对旧模式的概括很直接：收集遥测数据、存储数据、查询数据，再制作仪表盘盯着数据。这套方法在过去十年支撑了大量安全运营，但它主要交付的是**更多信号和更多待办项**，而不是最终结果。

问题在于，前沿网络安全模型正在快速扩大漏洞供给。它们能阅读代码、寻找缺陷，也能串联多个弱点形成复杂攻击路径。模型能力越强，安全团队面对的 backlog 反而可能越长。📈

一个典型场景是：扫描器一天报出 3000 条结果，其中既有未部署代码里的理论风险，也有公网可达生产系统中的真实漏洞。若团队仍按严重等级逐条排队，最危险的问题可能和大量误报一起被淹没。

| 旧安全运营 | Continuum 试图建立的新模式 |
| --- | --- |
| 收集遥测并展示告警 | 汇聚遥测、业务语境与风险背景 |
| 按固定规则打分 | 结合可达性、部署状态和业务影响推理 |
| 把发现交给人工确认 | 在隔离环境中验证可利用性 |
| 用工单推动跨团队修复 | 给出缓解、补丁、回滚与影响范围 |
| 定期扫描、阶段性审计 | 持续发现、验证、修复与复查 |

**真正的瓶颈已经从“能否发现漏洞”，转向“能否证明哪个漏洞真的重要，并安全地推动它被修复”。** ⚠️

**AWS Continuum 的野心，是把安全产品从“告警生产工具”变成“风险闭环执行系统”。** 这也是理解它的第一把钥匙：它卖的不是更多扫描结果，而是从发现到行动的连续性。

需要注意的是，当前最核心的 **Continuum for code vulnerabilities 仍处于 gated preview**，只向部分客户开放。AWS 公布了 Capital One、MongoDB、Rivian 和 Robinhood 等设计合作伙伴，但真实环境中的准确率、治理成本与规模化收益，仍需更多客户实践验证。🔍

# 二、它不是扫描器，而是一条安全闭环 🔄

把 Continuum 理解为“AI 漏洞扫描器”，会低估它的产品设计。更准确的类比是：**它像一支不会下班的虚拟安全小组**，既看代码和基础设施，也理解权限、网络拓扑、文档、沟通信息与业务优先级，然后沿着固定闭环处理问题。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHTcrHFNuldHiahlibsln7cSbTfJEmzkQT0PWSofrZ29iaWaibPKlWicSuTzJNkgJibev7lvfsXpsmjKQMUwHAkicmTaYyo5nj1APYdExY/640?wx_fmt=png&from=appmsg)

AWS 将这个闭环拆成四个连续阶段：

1. 🔎 **Discovery（发现）**：导入企业已有漏洞积压，同时扫描环境，补齐漏洞与攻击路径视图。
2. 🎯 **Prioritization（优先级排序）**：判断受影响组件是否已部署、是否可达、是否位于生产路径，以及被利用后的业务影响。
3. 🧪 **Validation（验证）**：结合实际环境排除误报，并在沙箱中构造可复现的利用示例，提供具体证据。
4. 🛠️ **Mitigation and remediation（缓解与修复）**：评估现有阻断、补偿控制和检测机制，再建议网络变更、策略变更或代码补丁。

这四步形成了一个关键转变：安全团队不再只问“代码里有没有缺陷”，而是连续追问——它是否存在？是否可利用？是否影响核心业务？现有防线能否挡住？什么修改最安全？修复失败如何回滚？

Continuum 处理的上下文分为两类。第一类是 AWS 中已有的结构化信息，例如基础设施、权限、网络拓扑和代码；第二类是描述组织如何运作的非结构化信息，例如设计文档、沟通记录、风险偏好和业务优先级。🧭

为什么这很重要？假设两个服务都存在同一个高危依赖漏洞：A 服务从未部署且没有外部入口，B 服务承载支付并暴露在公网。传统评分可能给出相同的 CVSS 等级，Continuum 则试图用环境证据把 B 提到最前面。

**优先级不再只由漏洞自身决定，而由“漏洞 × 环境 × 业务影响”共同决定。** 这能减少团队在低价值告警上的消耗，也让排序依据更接近真实风险。💡

**验证环节是整个闭环最关键的质量门。** 如果系统不能稳定地区分真实漏洞与误报，后续自动修复越快，制造事故的速度也可能越快。AWS 因此强调在沙箱中构造可复现证据，并用同一套系统再次验证补丁。

AWS 还将原来的 AWS Security Agent 能力纳入 Continuum：渗透测试成为 Continuum for penetration testing，代码扫描成为 Continuum for code scanning，同时新增预览版威胁建模能力。后者可以从设计文档或代码生成上下文相关的 STRIDE 威胁模型，覆盖欺骗、篡改、抵赖、信息泄露、拒绝服务和权限提升六类威胁。🛡️

# 三、四类能力怎样拼成“机器速度” ⚙️

**🎯【四类能力怎样拼成“机器速度” ⚙️】**

这一节真正关键的不是「四类能力怎样拼成“机器速度” ⚙️」这个概念本身，而是它背后的判断路径、执行边界和可复用方法。

它怎样落到真实安全团队的工作流里？哪些细节会直接影响 AI 代理的可靠性？

加入 `Oxo AI Security 知识星球`，可查看本节完整内容，系统掌握「四类能力怎样拼成“机器速度” ⚙️」的完整拆解与实战用法。

📚 **AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛 **AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡 **AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠 **AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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