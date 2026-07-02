---
title: “AI 就绪度”是未来评估防火墙的重要指标
url: https://mp.weixin.qq.com/s/wtuF1nHPl9nhFesIxq94qg
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:55:19.942771
---

# “AI 就绪度”是未来评估防火墙的重要指标

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SLl77fibWWLZCOLoAntzxkN3RZbQpAOeLib6ROpVz4svVRChlbC9eCQCX1ffIeKDPUAVWs5sFVMA5ibUz54cT4K3YIuzIqSKoic1Bl66SHgiaib4s/0?wx_fmt=jpeg)

# “AI 就绪度”是未来评估防火墙的重要指标

原创

高级产品经理陈晨
高级产品经理陈晨

新华三主动安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLZxw6pibq0j3oaTLkNuPRG8wthIJI4JosYcr41Cl531Zf22OSptgdlrGv57vI9WiaIN3MzwuuOib3c9Dl5A1aoyTttMvFicHlrXVYk/640?wx_fmt=png&from=appmsg)

AI Agent 来了，防火墙准备好了吗？

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLbtD7ccUUJlXvpLspKhW9wibSCwyPicIx9DLcojH2TsSmyG5v0QfM32BF6tYtVXAZkx2DHb3WRsmicHB40fibcxPbe14eicSu3KPkqE/640?wx_fmt=png&from=appmsg)

2026年，两个看似无关的事件指向了同一个趋势。

事件一：2026 年 4 月，Google、飞书、钉钉、企业微信、WPS 先后推出各自的 CLI 工具。飞书的 lark-cli 开源后不到三个月 GitHub Star 数突破 10,000，提供 200+ 条命令和24 个 AI Agent Skill。

事件二：同一时期，香港大学数据科学实验室（HKUDS）在 arXiv 上发表论文 CLI-Anything，提出了一句极具冲击力的核心观点：

"以 GUI 为中心的设计范式从根本上与 AI Agent 的能力不匹配。"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SLl77fibWWLbFaB0D0iclfmSm5kRrR2rcwr2yLP5GOcg4qDv1yeMwygUjZbxvwqdQda3kYWiaDFyt8tuED6mKUleASLFSvPpogRtmQGdwp7KwE/640?wx_fmt=png&from=appmsg)

论文揭示了一个惊人的效率差距：使用 MCP 方案（基于 GUI截图+视觉识别）执行一次合规检查任务消耗约 14.5 万 Token，而使用 CLI 方案仅需 4,150 Token——差距高达 35 倍。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLbkhcic1iaYJ4MGAeMsa1Xg6LLBsh8nmhZr9ITsdL6HMeFU717jfJCs4FiaNBrXrVchXgQYEAHib61uNUibJpItqzW4oVwibAEEImuOQ/640?wx_fmt=png&from=appmsg)

AI Agent 正在从概念走向生产。当 AI 开始接管网络运维，一个新问题浮出水面：你的防火墙，能被 AI 高效管理吗？

结论很清晰：防火墙的设计基因——是 CLI 原生还是 WEB 优先——将决定它在 AI Agent 时代的竞争力。这正是“AI 就绪度（AI-Ready）”成为防火墙新考题的原因。

![](https://mmbiz.qpic.cn/mmbiz_gif/SLl77fibWWLYUrsWfdrcicCycFzmWvC3RIJ33KFOWg1hc1ia0ThiaaI0rxCuGicx78HNgSOfE3WsrbGCXIU0v8fvT6H2r4ZicYViaibcefDzdOpc3hw/640?wx_fmt=gif&from=appmsg)

01

什么是 AI 就绪度？

面向网安融合领域，新华三率先提出“AI就绪度”概念，衡量一款防火墙能否被 AI Agent 高效理解、可靠调用、自主运维。它包含四个维度，缺一不可：

|  |  |
| --- | --- |
| **维度** | **说明** |
| **CLI 完整度** | 所有功能通过命令行暴露，无隐藏死角 |
| **可编程接口** | 支持NETCONF / YANG / RESTful API |
| **结构化输出** | 输出天然支持SYSLOG / SNMP / XML / JSON机器可读格式 |
| **AI 内置能力** | 设备本身内置大模型，能理解意图、自主研判 |

下面，我们以新华三防火墙为例，逐一拆解这四个维度——看一款“AI 就绪”的防火墙，究竟长什么样。

维度一：CLI 完整度——从 CLI 长出来的防火墙

AI-Ready 的第一条标准：所有功能必须通过 CLI 暴露，零 WEB 独占。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLZVUPKqaO88AtgcrBYWCgpB38jJy9T1e9E2GCJdztr47OLorDkzVQCExOnyoE4dxWdQuWt4IX2GfE7St0ibd8X9WmmJafAT6c7M/640?wx_fmt=png&from=appmsg)

新华三防火墙运行的是新华三Comware 操作系统——一套类比 Cisco IOS、Juniper JUNOS 的网络操作系统。Comware从诞生第一天起就以 CLI 为核心设计，提供层次化的视图系统：用户视图（<>）、系统视图（[ ]）、接口视图、策略视图等。这种结构清晰、层次分明的命令行体系，被网络工程师公认为业界最完整的命令行体系之一。

新华三防火墙拥有完善的 WEB 图形化管理界面，但 WEB 是 CLI 之上的封装，而非底层设计。这意味着 CLI 不是“能用”，而是“完整”——每一个功能、每一个参数都通过命令行暴露，没有任何隐藏的 WEB 独占能力。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLZt0CWmEGgCe6cHr5RCfsunZKickRvtkD7nIVvXsUh6HPuiaK8iadB6WGMxB4KPGawjWAhcicOMHbnVHWiaJrmfOUJ9XvCJZgcg0GUk/640?wx_fmt=png&from=appmsg)![]()

两种设计基因：CLI 原生 vs WEB 优先

相比之下，国内很多安全厂商基于工控机架构的防火墙在设计理念上走了完全不同的路：默认管理方式是 WEB 界面，CLI 仅作为补充品存在，功能受到限制。当管理方从“人”变成“AI Agent”时，这种设计理念的差异就被急剧放大——AI Agent 无法“点击”一个 WEB 界面，但它可以完美执行一条 CLI 命令。

维度二：可编程接口——让 AI Agent 能“程序化调用”

AI-Ready 的第二条标准：具备标准化、结构化的可编程接口。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLblOOesWAxrBToNmSdl6Hib8Urolwblia00m6FZDibmy4n9EqVQngUFmTJ5vbgCNtY7R11FEcrbuCg6tvMl3uvGxVPoASpjHWxaV0/640?wx_fmt=png&from=appmsg)

CLI 完整是基础，但 AI Agent 时代需要的不只是能敲命令，而是能被程序化调用。H3C在 Comware CLI 体系之上，构建了完整的可编程能力栈：

|  |  |  |
| --- | --- | --- |
| **NETCONF**  基于 XML 的网络配置协议，提供完整 API | **YANG 模型**  数据建模语言，与 NETCONF 配合实现结构化配置 | **RESTful API**  完善的 RESTful 接口，支持 HTTP 协议调用 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SLl77fibWWLZOL32UzNUOicEn7aHp51VUtMaWDibtClbRcTZkQj5ibQiaRSa8N7wjl8vMyHXpymgADIuKU3ibAfkYfT0VcoCtJD6hEkvWWPao2cAI/640?wx_fmt=png&from=appmsg)![]()

H3C SecPath Firewall：CLI 原生 + 三层可编程架构

这意味着新华三防火墙不仅 CLI 强大，它的结构化输出能力也是业界领先的——而这正是 AI Agent 最需要的。

```
# M9000 NETCONF 调用示例：查询安全策略curl -X POST https://m9000/api/netconf \    -H"Content-Type: application/xml"\    -d'<rpc><get><filter>security-policy</filter></get></rpc>'
```

AI Agent 可以通过 NETCONF 接口批量管理数百台设备，通过 YANG 模型理解设备的数据结构，通过 RESTful API 实现与 SIEM、SOAR 等安全组件的深度集成。标准化接口让 AI Agent 可以用同一套逻辑管理整个安全栈，复杂度从指数级降为线性。

维度三：结构化输出——让 AI Agent“直接消费”

AI-Ready 的第三条标准：所有输出天然支持机器可读格式。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLYTh5tZXaUPAGhHgzuNpBf1GWUZpJ9J3SmetlETjh8BhMTLzBvHtVsSOsCXTY2icVmBl3Ev6P3gJPia6Kf1jrzO20shTGP4micdvQ/640?wx_fmt=png&from=appmsg)

CLI 日志、MIB、报表的输出格式，决定了 AI Agent 的解析成本。防火墙所有命令均支持标准 SYSLOG / SNMP / XML / JSON 格式输出，AI Agent 可以直接消费，无需额外的解析层。

![](https://mmbiz.qpic.cn/mmbiz_jpg/SLl77fibWWLZYrEibTzbgNC9Xhzq3hBnunicTYE6LUhIk6NukRtGOoyriamgSPsjIiac93ZGFibwVNIVSvrOVT8uEsHkSlT4zkJNLCniawpP1K1s8k/640?wx_fmt=jpeg)![]()

结构化数据直达 AI vs GUI 截图层层解析：两种输出方式的效率差距

例如，查询一条安全策略命中统计，新华三防火墙通过 CLI 直接输出结构化 JSON，AI Agent 拿到后即可直接判断、决策：

```
// M9000 CLI 输出示例：安全策略命中统计（JSON 格式）{   "policy-hit-statistics": {    "rule-id": 15,        "action": "deny",    "hit-count": 12847,    "last-hit-time":"2026-06-30T14:23:11+08:00",    "source-zone": "Untrust",    "destination-zone": "Trust",    "top-source-ip": "203.0.113.45",    "anomaly-score": 0.92  }}
```

相比之下，GUI / WEB 界面的输出是像素，AI Agent 需要经过“截图 → 目标检测 → 坐标计算 → 模拟点击 → 再次截图”的复杂流程才能获取信息。结构化输出不仅降低了 AI Agent 的解析成本，更重要的是提供了确定性的执行结果——每一次调用返回的都是精确的数据，而非可能存在识别误差的屏幕截图。

维度四：AI 集成能力——设备本身具备 AI 推理能力

AI-Ready 的第四条标准：设备本身具备 AI 推理能力，而不仅仅是被 AI 管理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SLl77fibWWLayGF9JuZElY2vcyJ3umHgcREr3Ig7Olm0BN3TNgMmDlMGv1wEMzKHfNpm8w1EF3KPJRMJL8DdhlVx5cg3XdXiajhhrbsjV4rQg/640?wx_fmt=png&from=appmsg)

前三个维度回答了“设备能否被 AI 高效管理”的问题，而第四个维度则更进一步：设备本身是否具备 AI 能力？

![](https://mmbiz.qpic.cn/mmbiz_jpg/SLl77fibWWLaRo8SZaoIKfN1wxicKuQQiagRVpDqcnM9DOZNfPd4XaFTMJntY9K6Lp8dlR7457yCDibibv2QKn0pc2prW5DFNoHlkPeiaInZFXvho/640?wx_fmt=jpeg)![]()

新华三安全运维智能体：从“执行命令”到“理解网络”

新华三防火墙为 AI Agent 决策提供更多有价值的数据：

* 设备本地智能体：学习统计安全策略中高频命中的网络资产安全状况

* 设备本地智能体：自动化生成安全策略明细，细化安全策略内容

* 设备本地智能体：针对防护不足的安全策略，给出安全深度检测防护建议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SLl77fibWWLbQP0rOh0cGvq3YeEXaqCZUMdaHCd6sgjrdCatXm3T0RtZZJJ4mrc14BY3MAfibQiaKDyZhfFo1q950kd8TFWX57LzAp0cTuR614/640?wx_fmt=png&from=appmsg)![]()

安全运维智能体基于新华三 23 年 ICT 运维经验和 1.2 亿台在网设备的运维数据训练。它不只是在执行命令，而是在理解网络——通过分析历史流量模式预判攻击、自动调整防御策略、主动优化性能参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SLl77fibWWLaVJtt4FQEdMnmWHolzjNb2Rj9qTARZn6O6mU2VTpszjTpaIvtibfPLyKPQuvF5ewVEzVbaIZaSTxX1qMFiaK0NKHvoOlpo42lQA/640?wx_fmt=gif&from=appmsg)

02

AI 就绪不只是概念，是正在发生的未来

场景一：消除专业门槛——“说话”就能管理防火墙

“0门槛”运维，工程师不再需要记住上千条命令：

通过成熟的SKILL调用方案，防火墙可以适配主流的Codex、Claude Code、WorkBuddy等AI Agent，团队测试、运维效率极大提高。

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLZ68zpUMgZF4nZq1EWnxgvlU5DKGibPnJedXH7LVwQ43Etqu1ibMBxdChflL3ib94LbJjI2GTpIv75VuEZmDmbRp0CaOfibYfSEmGE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLZiaw8rusGricRYuw37lc8CslbDiaYj7sCLiaIOHzzXwFwdoXvcsxvJsSl31oOqeQ5pTD3URibknjlTfWvcwicHx2CpIZaeS8yibVW9sU/640?wx_fmt=png&from=appmsg)![]()

新华三防火墙功能CLI能力覆盖率：100%

AI Agent + CLI原生基因共同实现的能力——无需专业技能，想法即动作。

场景二：定制化自己的“AI 运维 SKILL”——从发现问题到自动修复

|  |  |  |
| --- | --- | --- |
| **方式** | **效率** | **过程** |
| **传统方式** | 3 人，耗时 2 周 | 逐台登录、手动截图、人工比对 |
| **AI Ready 方式** | **AI Agent，耗时 1 小时** | 自动巡检 + 自动修复 + 自动验证 |

AI Agent通过新华三防火墙的可编程接口，固化重复性运维动作，形成专属自己的 AI SKILL，实现“检查→ 修复 → 验证”全闭环，无需人工逐台操作。

场景三：自愈网络，意图驱动编排——整网协同防御

![](https://mmbiz.qpic.cn/mmbiz_png/SLl77fibWWLb8YJ1NxeVGoDAwdun0ia9jcsHTJN6Dnm8TS98Ihd3ibMDmDCuWbUW5LriaLdYNJGdMsibibvz4TNbpia6Ql6icSYiapRnEdhicX68pF440/640?wx_fmt=png&from=appmsg)

传统单点防护 vs AI-Ready 全自动协同防御

如果你拥有整网“AI 就绪”的网络+安全设备，那么当新华三防火墙检测到可疑行为时，AI Agent 将会自主启动跨设备协同防御——联动防火墙、交换机、BRAS、终端杀毒等产品，秒级形成多层防御网。

|  |  |  |
| --- | --- | --- |
|  | **传统方式** | **AI-Ready 方式** |
| **响应时间** | 人工分析 + 逐台配置，数小时 | **全自动协同防御，30 秒** |
| **安全等级** | 单点防护 | **网+安融合联动** |

AI Agent自由组合联动所有“AI 就绪”的设备，按用户意图自动编排生成并下发配置，打通不同品牌、不同设备的壁垒，创造立体协同的自愈网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/SLl77fibWWLYT1SoK6ibrzPUt614NmpVagUkYgHYshCPYuicmicy0Yw2HibCqvgVoGK22gcuxUft05KUqomgvsb7ia9axBowAYCw5oaHXB1wiaib85M/640?wx_fmt=gif&from=appmsg)

03

AI 就绪度，从加分项到必选项

新华三认为，当 AI Agent 成为网络运维的核心执行者，防火墙的“AI就绪度”将决定你的运维体系能否真正实现 AI 驱动的闭环。

给网络安全从业者的建议：

1. 在...