---
title: 慢雾：如何评估加密反洗钱工具的有效性
url: https://mp.weixin.qq.com/s/Q4L5Cbyv3JUhmor5BagrJg
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:37:03.396907
---

# 慢雾：如何评估加密反洗钱工具的有效性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCKbLcdh8o8QxiaRpme9ate1AecUQ4ic1zn22ntXCPN9vRM46ZMzyseeh76wKHicOoWlCpPOBxXjqHiaeTSTb59dmGMg8IDPGibt3lVs/0?wx_fmt=jpeg)

# 慢雾：如何评估加密反洗钱工具的有效性

白帽子

![]()

在小说阅读器中沉浸阅读

以下文章来源于慢雾科技
，作者慢雾 AML 团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4FqAumbguXteG2OtztBWwTZ6xLLfTaIQfRvzdJhLZkibQ/0)

**慢雾科技**
.

慢雾科技是一家专注区块链生态安全的公司，成立于 2018 年 1 月，主要通过“威胁发现到威胁防御一体化因地制宜的安全解决方案”服务了全球许多头部或知名的项目，已有商业客户上千家，客户分布在十几个主要国家与地区。

********过去几年，虚拟资产服务提供商(VASP) 在反洗钱(AML) 领域面临的核心问题，已经悄然发生变化。

早期，行业更关注“是否已经部署 AML 能力”；而现在，一个更现实的问题摆在面前——这些能力，是否真正达到了监管可以接受的标准。

[过去的一年里](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504454&idx=1&sn=27742de4ac090d63ca765483be9723e3&scene=21#wechat_redirect)，这种变化变得更加明显。多起处罚案例释放出同一信号：在结果导向的执法框架下，“已经投入但效果不足”，与“未采取措施”，在问责层面并不会被严格区分。

换句话说，监管并不关心你“有没有做”，而更关注你“有没有做到”。

这也意味着，AML 工具的评估，不再只是功能层面的对比，而需要回到一个更本质的问题：这些工具，能否在真实链上环境中识别风险？

基于此，本文将分析导致不同 AML 供应商系统中的风险判定存在差异的原因，并介绍一套标准化评估方法，帮助虚拟资产服务提供商自主测试来选择合适的供应商。

# 名单之外的风险

在很多合规流程中，制裁名单和黑名单筛查依然是基础能力。但如果把评估停留在这一层，很容易产生一种“系统已经覆盖风险”的错觉。

以 OFAC 为例，其公开名单本质上是“已确认风险”的集合，但现实中的风险远不止于此。大量未被列入名单的地址，仍可能通过控制关系或资金往来，与受制裁实体产生关联。

如果一个工具只能识别“已经被标记的风险”，那它在实际业务中的价值是有限的。更关键的问题在于它能不能识别那些还没有被写进制裁名单里的风险。

# 为什么结果不同

在实际选型过程中，一个非常常见的现象是：

同一地址，在不同 AML 供应商系统中的风险判定，可能完全不同。

这种差异通常不是偶然，而是源于底层能力的差别 —— 数据从哪里来，更新是否及时，标签如何生成，模型如何计算风险，以及系统是否具备对资金路径进行分析和穿透的能力。

当这些因素发生变化时，呈现给用户的风险判定，自然也会不同。

问题在于，在缺乏统一评估方法的情况下，这些差异很难通过产品演示或功能清单体现出来。你看到的是功能描述，而不是实际效果。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKtVU6lRtWYR6TwHrIIwEomFEVqfW8pcOfvK1ljQLL4V9WJRicHibudn9AI7rtRMfiaeNib6O3hbWRDoHyM7YX4KVDBcBzcQ0uFG00/640?wx_fmt=png&from=appmsg)

也正是基于这一现实问题，慢雾(SlowMist) 结合长期威胁情报积累与反洗钱追踪经验，整理了《Crypto AML 供应商评估 Checklist 与执行指南》。该指南参考 FATF、Wolfsberg Group，以及 FinCEN、HKMA、MAS 等监管要求，尝试提供一套既符合监管逻辑、又能够落地执行的评估方法。

本文将对评估思路进行简要说明。完整执行方法，可通过以下链接获取：https://github.com/slowmist/crypto-aml-vendor-evaluation

# 用实测检验能力

很多团队在选型 AML 工具时，会停留在两个阶段：看 Demo，或者对比功能列表。可问题在于，这两种方式展示的，往往是产品的“能力上限”，而不是它在真实环境中的表现。

在实际反洗钱场景中，真正影响判断结果的，是一些更细节但更关键的因素：数据是否足够新足够丰富、标签是否持续更新、风险是否能够随着资金路径传导，以及模型在复杂场景下是否稳定。

而这些问题，不测试，是难以得出准确结果的。

在过往的安全分析中，我们反复看到一种情况：某些地址没有出现在任何公开制裁名单中，但其资金路径已经与高风险实体产生明确关联。在部分系统中，这类地址仍然被标记为“低风险”。从系统角度看，一切正常；但从风险角度看，关键问题已经被遗漏。

这也是为什么，单纯依赖名单命中，已经不足以支撑当前的合规要求。真正需要验证的，是工具是否具备识别关联地址、还原资金路径，以及判断多跳间接风险的能力。

基于这些经验，这份指南给出的核心思路其实很简单：用数据去“反推”工具的真实能力。通过标准化评估方法对供应商进行实测，将原本依赖主观判断的选型过程，转化为可量化的决策过程。

你可以准备一小组地址，例如 20 到 50 个，包含三种类型：已知的高风险地址、明确安全的地址，以及介于两者之间的灰度地址。然后把这些地址分别输入不同的 AML 系统，记录每一个系统给出的风险判断结果。

做完这一轮，通常会看到几个很直观的差异：哪些高风险地址没有被识别出来，哪些正常地址被误判为风险，以及灰度地址在不同系统中的风险分层是否合理。

|  |  |  |
| --- | --- | --- |
| 指标 | 含义 | 风险影响 |
| Recall（召回率） | 识别已知高风险地址的能力 | 漏报风险 |
| False Positive（误报率） | 将安全地址误判为风险的比例 | 审核成本与业务影响 |
| 灰度识别能力 | 对非明确违法行为的识别能力 | 风险分层能力 |
| 穿透分析能力 | 多跳路径中的风险识别能力 | 间接风险暴露 |

如果希望进一步验证工具在真实环境中的表现，可以在链上模拟一些典型交易行为，比如刻意拆分金额的结构化转账、与混币合约的交互，或者经过多跳路径再进入目标地址的资金流动。观察系统的警报延迟、风险是否能够沿路径传导、规则是否支持灵活配置，以及 API 的响应速度和稳定性，这些都会直接反映出工具的实战能力。

在完成测试后，可以基于以下评估维度进行打分：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 评估维度 | 权重 | 供应商 A 得分 (1-10) | 供应商 B 得分 (1-10) | 备注 |
| 数据质量 | 30% |  |  | 标签准确度、更新速度 |
| 功能完备性 | 25% |  |  | 聚类分析、跨链追踪 |
| 易用性 | 15% |  |  | UI/UX、案件管理流程 |
| 技术性能 | 15% |  |  | API 延迟、稳定性 |
| 成本 | 10% |  |  | 初始费用、API 调用费 |
| 服务支持 | 5% |  |  | 响应速度、培训支持 |
| 总分 | 100% |  |  |  |

********（评分卡示例）********

此外，为了降低实际执行门槛，我们把整个测试流程整理成了一套可以直接使用的 AI 指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIuAibAHhJlUBfFvLxdI8BetjxJ9cicLmsV1WArQMAcc7gj4rj9bTW2VOkcotWyHghxu71qibLibMqITibCKb8ficBv17HPlM5h5p1C0/640?wx_fmt=png&from=appmsg)

只需要从《Crypto AML 供应商评估 Checklist 与执行指南》的参考数据集中挑选地址或按照《AI 辅助 AML 供应商评估（逐步指南）》的步骤引导 AI 生成地址，将指南中的指令复制出来，把地址和各系统的查询结果提供给 AI（例如 Gemini），就可以自动完成后续工作：包括数据整理、结果对比、关键指标计算，以及基础评估结论的输出。

完整步骤可以参考：

https://github.com/slowmist/crypto-aml-vendor-evaluation/tree/main/AI-Assisted%20AML%20Vendor%20Evaluation%20(Step-by-Step%20Guide)

# 写在最后

在同一套评估框架下，不同 AML 工具之间的差异，通常集中在数据质量、功能完备性、易用性、技术性能、成本和服务支持上。

基于长期的安全研究与威胁情报积累，SlowMist KYT 在这些方面做了针对性的优化，包括多链风险标签的数据覆盖、基于资金贡献度的风险计算方式、多层级的链上路径分析能力，以及持续监控与历史数据自动复筛机制。同时，在合规侧支持 STR 报告生成与审计留痕，以满足监管对可追溯性的要求。

如希望更直观地了解相关能力，点击「阅读原文」填写表单，即可申请免费试用与 Demo 演示，或联系邮箱：kyt@slowmist.com

限时福利： 截止至 2026 年 12 月，采购 SlowMist KYT 享受 8 折优惠！

关于慢雾 AML 能力体系

依托慢雾(SlowMist) 深耕多年的区块链生态安全与威胁情报能力，慢雾(SlowMist) 构建了业内领先的加密货币反洗钱与合规体系。面对日益严格的全球监管环境与复杂的链上洗钱手法，该体系通过旗下两大核心产品 —— 慢雾反洗钱追踪系统 MistTrack 与面向大型机构合规团队的专业、实时反洗钱引擎 SlowMist KYT，为全球交易平台、金融机构、监管单位及个人用户提供覆盖事前、事中、事后的一体化解决方案，帮助用户在复杂多变的链上环境中实现风险可识别、可控制、可追溯。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCJwA3LZbLuN9HOC4DnDvRzqSn2n1pavR0ibcicQQj2af240wK5hqluo4uG1moud9fXxbt8uc7P27VrceRhwK04A1MqRFVibCnZlcY/640?wx_fmt=png&from=appmsg)

作为链上数据分析利器，MistTrack 专注于链上资金追踪、地址调查与标签识别。平台提供科学的风险评分算法与全面的地址概览，通过丰富的地址标签、交易对手与行为分析、地址痕迹剖析，结合强大的可视化交易图谱，帮助用户精准识别复杂的链上资金流向。同时，MistTrack 支持 KYT/KYA 分析、主动监控告警以及便捷的 API 接入，满足用户对链上资金调查与反洗钱的基本需求。

为满足机构用户更高阶的合规审计和风险分析能力的需求，全新的 SlowMist KYT 在 KYT/KYA 风险筛查方面，基于慢雾丰富且动态更新的 AML 数据库，进行上下十层的深度风险分析，精准识别受制裁实体或暗网等高风险源，并利用可视化关联链路实现资金网络分析；支持高度灵活的风险规则配置，可按需加载适配不同司法管辖区的筛查参数，全面掌控风险评分计算逻辑；通过持续监测与自动化回溯，精准捕捉风险敞口变化，并自动生成时间序列 STR 报告，满足“可审计、可追溯”的合规标准；其内置的告警引擎与案件管理模块支持自定义实时告警阈值以过滤噪音，并能自动触发风险工单。从风险识别、追踪调查到工单处置，SlowMist KYT 真正实现了合规操作的完整闭环。

在全球监管不断趋严、链上风险持续演化的背景下，慢雾 AML 团队致力于以技术驱动合规能力升级，将复杂的链上行为转化为清晰、可信的风险洞察，持续为行业提供专业、可靠的安全与合规基础设施，助力构建更加透明、安全、可持续发展的区块链生态。********

**往期回顾**

[活动回顾｜慢雾创始人余弦出席首届 Agentic AI 创新与安全论坛](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504607&idx=1&sn=49e70d092b5e2e4d7278e85d822643f8&scene=21#wechat_redirect)

[Odaily专访余弦：Anthropic核弹级新模型泄漏，如何影响加密安全攻防？](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504594&idx=1&sn=88d0a2ea27ea5f4bd87967e3411848f6&scene=21#wechat_redirect)

[慢雾：Web3 安全年框服务全面升级](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504592&idx=1&sn=5b14e6284530b087155c3c9b13b86e3c&scene=21#wechat_redirect)

[安全预警：Apifox 桌面客户端官方 CDN 脚本遭供应链投毒](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504575&idx=1&sn=fa2ad5b1d103daaa52b67a16aa6fcef8&scene=21#wechat_redirect)

[LiteLLM 供应链攻击事件始末](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504575&idx=2&sn=0602625406cc37b3c62e48b13ce706dd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbEP8f4tadFenoLauzHpicWdWbVap3aia38LUGPflBho9ibDHXjoG5fecGJSaYa4S4zYdoicXibSmjv9tg/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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