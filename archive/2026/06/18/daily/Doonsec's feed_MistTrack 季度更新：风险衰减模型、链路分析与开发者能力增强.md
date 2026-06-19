---
title: MistTrack 季度更新：风险衰减模型、链路分析与开发者能力增强
url: https://mp.weixin.qq.com/s/s2CKPZ-LthjxU9GQOlBxDw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:01.634313
---

# MistTrack 季度更新：风险衰减模型、链路分析与开发者能力增强

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCK70lNEibpQB84Fsa9bKEaYeiaDWPlGhfP7yJpKtpe2mJtLXkf1m0f6Bn7LUmNveFQh7crZq4zabj09Vc4Q4P8q3PgO8uYvCoia8U/0?wx_fmt=jpeg)

# MistTrack 季度更新：风险衰减模型、链路分析与开发者能力增强

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

******************# 在链上合规与风险分析的实际场景中，地址的风险得分只是基础判断，更关键的是如何在复杂的资金流转中衡量风险传导的强弱和识别风险的传导路径，并在效率与准确性之间取得平衡。********

********# **围绕这一核心问题，MistTrack 近期集中推出多项功能更新，从链路分析能力到开发者接入体验进行系统性优化，帮助用户在不同业务场景下实现更精细、可解释的链上风险判断。主要更新包括： * 支持间接风险衰减设置 * 新增风险资金的关联链路分析 * 上线 Telegram AML Bot，提升查询效率 * 推出按量付费的开发者版，优化低用量用户的接入体验 欢迎通过该链接注册并体验：https://dashboard.misttrack.io/ **间接风险衰减设置** **在反洗钱分析中，跳数(Hops) 是衡量地址与风险实体关联程度的重要指标。一个地址距离风险源越近，其风险暴露通常越高；反之，随着中间路径的增加，风险的实际影响也可能逐步减弱。** **但在实际业务中，不同机构对风险的容忍度与评估标准并不相同：** * **有的场景更偏向审慎合规，需要放大所有潜在风险** * **有的场景更强调精细判断，避免远距离关联带来的误报** **基于此，MistTrack 本次新增「间接风险衰减设置」，支持用户根据自身策略，自主调整风险传导模型。** **![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCIvExmv24wxdEQHhpewAibUD9awLDmGS3EKXBMPaEKvOs1bAvLB61LBp3p9o08cdzC8ID49OZjcdeicqXVn0j5rIqxJibCUWMfpIo/640?wx_fmt=png&from=appmsg)** **两种模式说明** **1、衰减模式** **适用于需要更贴近真实风险暴露程度、降低误报的场景。系统将按照预设算法对风险权重进行递减：每增加一跳，该路径对最终风险评分的贡献降低 40%。** **2、不衰减模式（默认）** **适用于强监管或高敏感业务场景。在该模式下，无论中间经过多少跳，风险权重均按 100% 计算，不进行衰减。** **应用范围** **该设置一经调整，将同步作用于：** * **MistTrack 网页版风险评分查询** * **Risk Score API 调用结果** **设置路径** **https://dashboard.misttrack.io/risk-setting** **风险资金关联链路** **在链上分析过程中，复杂的交易图谱使人工追溯变得低效且易出错。在处理高频交易地址时，一个地址可能有成千上万个交易对手方。如果试图在交易图谱中拓展节点，屏幕会迅速被填满。而且，人工追溯这类复杂结构易出错，一旦漏掉一个中间节点，线索可能就断了。** **为此，MistTrack 新增关联链路，直观呈现地址与风险源头之间的资金路径关系。在撰写可疑交易报告 (STR) 或向监管机构汇报时，合规官可以引用具体的链路层级（如 Layer-1 到 Layer-3），提供确定性的证据，满足审计与监管合规的可解释性要求。** **![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKhSK9J88roONbpKg7MjlCWYqvWG2z4uZUJznuZgLN87C2akKVBa31agcH2Rmu2fp08xKFibCo1EgdiayooibKXTNeKTUibNj84KzY/640?wx_fmt=png&from=appmsg)** **链路还清晰展示了是直接关联还是间接关联。直接关联(Direct) 意味着该用户直接与风险关联。间接关联(Indirect) 可能是由于资金污染导致。** ![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKcSjqLicqftkc42dWKsvZicI4NhXVicq1QEhjQe7kFvsGbSkBQicl0V8WqZPNMXZQnDXkj4icCN2VFBP2JhGPY3QTBFdGacCOp97E4/640?wx_fmt=png&from=appmsg) **合规官可以根据跳数的多少，结合资金的数额与占比，来决定是进行增强型尽职调查(EDD) 还是直接采取限制措施。这样可以避免“误杀”普通用户，同时确保高风险目标不被遗漏。** **此外，在链上分析过程中，复杂的交易结构有时难以通过列表形式直观呈现。为此，MistTrack 新增风险资金关联图谱，以可视化方式还原与风险地址之间的资金流转关系，点击“风险图谱”按钮即可查看完整的风险资金交易关系、交易金额和风险实体地址，快速理解整体结构并定位关键风险路径。** ![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKhcZYcsMDzjibsmEGcib4BQS19fHpQlVhsaSufsAzsYzMMonUBTQnadISDNeX5uSXktAc63PsiaGaLQ3jmt9MVibsvn140fdGKrgo/640?wx_fmt=png&from=appmsg)**********

********# ****按量付费的开发者版套餐** **越来越多开发者与中小团队希望将链上风险分析能力集成到自身业务中，但传统订阅模式在价格与使用灵活性上仍存在一定门槛。** **基于此，MistTrack 正式推出按量付费的开发者版套餐(Developer Plan)，每年 $20 起，以更低门槛、更高灵活性的方式开放核心链上风控能力。** **![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKkb1RubzBImE8wjgtF6CB0nx5Ll8W8GB0FBJUJrLyPcpILJUlLibRAWibSTmXW4Juww5iabWwE9VRBRMZa0YibSQfQgoUOJsAfMMc/640?wx_fmt=png&from=appmsg)** **用户仅需采购预期要使用的 API 次数，无需承担闲置成本，特别适合业务量波动较大的使用场景。支持最高 10 QPS 的并发调用能力，能够满足中小规模业务的实时风控需求，兼顾效率与稳定性。** **采购页面：https://dashboard.misttrack.io/upgrade** **MistTrack AML Bot** **我们新推出了 MistTrack AML Bot，将链上风险分析能力延伸至 Telegram。** **![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKCC1pACj1WfcJj8jKYvtCiahOFq9CQbOxBzl3MDSEmbUGkP6Nico20G79CQppIkNPqb9CzMnB0Lxxt7qdq8o4Nk51ibqhrCoianibg/640?wx_fmt=png&from=appmsg)** **对于已开通支持 API 套餐的用户（标准版/合规版/企业版/开发者版），连接好 MistTrack AML Bot 后，无需登录 MistTrack 后台，在 Telegram 中发送地址，即可快速获取风险评分及相关分析结果。** **![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKjIJZZwSQ90cmnCReiaibSdJA1ibJnbe3UP3rJafcyfic5JRWXSbUeEDmmNZ9czM9MQsC94RGibzhu2dRAic7aATQmxDhfZf6osG5ZY/640?wx_fmt=png&from=appmsg)** **配置页面：https://dashboard.misttrack.io/apikeys** **写在最后** **无论是通过“间接风险衰减设置”实现更符合业务场景的风险建模，还是通过“风险资金关联链路”提升分析的可解释性，亦或是通过 Telegram Bot 与 Developer Plan 降低使用门槛，这些更新都指向同一个目标——让链上风险分析从结果判断走向过程可解释。** **这一能力的背后，源自慢雾(SlowMist) 长期积累的安全情报与合规实践。基于八年的技术沉淀，我们已构建起覆盖 4 亿+ 地址标签、1 万+ 实体、50 万+ 威胁情报、9000 万+ 风险地址的数据体系，支持 19 条主流公链、100+ Token、14 种稳定币及 25 类风险类型，为链上风险识别提供持续、可靠的底层支撑。** **同时，这一实践能力也获得了外部权威认可——慢雾在“香港资讯及通讯科技奖(HKICT Awards)”中荣获[金融科技金奖（监管科技：监管及风险管理）](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247503777&idx=1&sn=09757385d04ebfe193404c3bb1cf43cd&scene=21#wechat_redirect)，体现了其在链上合规领域的技术价值与落地能力。** **在此基础上，慢雾(SlowMist) 推出的[新一代区块链反洗钱合规系统](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504461&idx=1&sn=245db26fb01a7da89e732ef1ca28b422&scene=21#wechat_redirect) SlowMist KYT 进一步将这些能力整合为一套覆盖“风险识别、深度调查、自动化处置与审计留痕”的全生命周期反洗钱解决方案，帮助 VASP 在不断演进的监管环境中，建立可配置、可审计的合规能力体系。** **![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLnnlVs1GV1MjregscmsgwaY4dyZD20739vx8NNqQrLka4lrwAmOyyj110epwyBBSDoaYjLHcqdfOBKuhibGmownLn3rK8aN7J0/640?wx_fmt=png&from=appmsg)** **如需了解 SlowMist KYT 的产品细节、申请试用或讨论采购方案，欢迎直接发送邮件至 kyt@slowmist.com，我们的产品团队将尽快与您取得联系。**********************

**往期回顾**

[威胁情报｜Arch Linux AUR 供应链投毒关联恶意 npm 包分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505220&idx=1&sn=1774b88eb9daff2dad7fb7f498b14ce7&scene=21#wechat_redirect)

[专精百强发布：慢雾科技荣获区块链安全领域单项冠军](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505178&idx=1&sn=5e087a0c19a023e5c2859bbf25637b12&scene=21#wechat_redirect)

[Aztec Connect 被盗 219 万美元资产分析：ZK-Rollup 结算边界绕过致 L1/L2 状态分歧](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505168&idx=1&sn=ab2d4ffdc96532ad2ed42501f1a28e3f&scene=21#wechat_redirect)

[威胁情报｜从 Python 到 Bun：Shai-Hulud Hades 变种跨运行时攻击链分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505155&idx=1&sn=c7e75283dea7f30f070386750851bc28&scene=21#wechat_redirect)

[威胁情报｜Red Hat Cloud Services npm 包供应链投毒](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505135&idx=1&sn=cb2fb9283b84262e0c3364ba753e3057&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLqYqc9l9poJTcO8JBsibl6nSSJoiaasoqFToYClTV5oAl2oE6IcqhNsiciagmyhOAsRCrdxdrOKqxpZicVQqlu0WrcOb5vDfKMGsSc/640?wx_fmt=png&from=appmsg)

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

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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