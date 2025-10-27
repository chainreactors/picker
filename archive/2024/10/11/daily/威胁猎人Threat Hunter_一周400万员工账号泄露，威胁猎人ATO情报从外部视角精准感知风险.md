---
title: 一周400万员工账号泄露，威胁猎人ATO情报从外部视角精准感知风险
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498043&idx=1&sn=8f4e37c5ab24865ea4e0be28b83d73a2&chksm=eb12df00dc65561679ddbad536a937d5a9e4088513c6ee3d6fe30746ea73b56b70f8977e8b2e&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2024-10-11
fetch_date: 2025-10-06T18:53:14.313886
---

# 一周400万员工账号泄露，威胁猎人ATO情报从外部视角精准感知风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGCibG8nfEybRpzeU3awfLRHkrM2ye4lTPjHZNy3Swu7RiaZqvY9nUFHeg/0?wx_fmt=jpeg)

# 一周400万员工账号泄露，威胁猎人ATO情报从外部视角精准感知风险

原创

猎人君

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/4mAgZtBianqHwB5L4n1SdUaicvcFspoC5LC0sR6QhONHlmxKqJbr50j9XvHibLLDeVM6GzOPt57raMG2kxzAuFfoA/640?wx_fmt=gif)

随着企业线上业务增长，账号接管（Account Takeover, ATO）风险呈“指数级”增长，Digital Shadows公布的数据显示，暗网上有150亿条个人账户信息出售，价格从不到2美元到14万美元不等。**企业员工账号，特别是具有对企业内部系统和数据的高级访问权限的特权账号**，一旦被攻击者掌控，可能导致企业核心数据的泄露、系统瘫痪或被恶意操作。

*2022年思科公司遭遇的一次安全事件中，攻击者通过钓鱼邮件获取了员工的登录凭证进入了公司内网网络，并进一步利用特权账户横向移动，最终导致公司大量敏感数据泄露和系统失陷。*

企业内部即使采取了ATO防范方案，如通过部署IAM、零信任等进行内部管控，但还是有可能被绕过，**攻击者通过钓鱼短信/邮件、AI换脸等技术获取到高价值账号信息或直接通过“木马、蠕虫病毒”入侵个人终端**。一旦企业内部设备被入侵，不仅设备自身存储的敏感数据存在极大的泄露风险，若攻击者进一步获取了内部设备的账号密码，则可**以此为“跳板”渗透企业内部系统并开展大规模攻击**。

威胁猎人ATO情报服务持续对企业账号泄露风险进行监测，**仅一周时间就监测到了被泄露的企业员工账号数量超400万，涉及社交、电商、教育等行业近****20万****家企业**。

**一、特权账号泄露风险监测情况**

***1、*****一周超400万员工账号泄露，涉及社交、电商、教育等行业近20万家企业**

近期，威胁猎人ATO情报服务对监测到的已泄露的企业相关账号进行统计分析，发现**仅一周**就有**近****1.8亿**账号在黑产交易市场售卖，其中企业员工账号数量**超400万，涉及企业近20万家**。

进一步分析发现，**涉及企业所属行业Top10覆盖了社交、电商、教育、金融、短视频、支付、航空、旅行、物流、招聘等**。尤其是社交和电商，这两个行业在数字化进程中处于前沿，积累了海量的用户数据和交易信息，电商行业因涉及大量的在线交易和金融信息，成为了黑产眼中的“肥肉”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGeofaN6jT8CiagsOuR2UfSG6r6dmxZaLUicTVlf38OGUxAibA0T6Vp61Yw/640?wx_fmt=png&from=appmsg)

**2、泄露账号的企业外部软件类型分布：第三方办公协同工具成高风险区域**

威胁猎人安全研究人员对已泄露的企业账号信息进一步分析发现，泄露的账号涉及大量第三方软件账号，其中**Zoom平台**（视频会议软件）数量最多，其次是**Slack平台**（AI工作管理和工作效率工具）、**Salesforce**（客户关系管理CRM）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGuMMHjZfJJQJJYwwDVCFv2lsjcxPTtdG5Sbqo2FuutRb8ia5mLXkQYHQ/640?wx_fmt=png&from=appmsg)

这些平台均存在大量敏感账号数据，包括但不限于用户身份信息、企业机密、客户信息、财务信息以及通信内容等，一旦这些数据的安全防线被突破，账号被恶意接管，将给企业和用户带来一系列严重问题。

**3、泄露账号的企业内部系统类型分布：安全性普遍面临挑战**

除了企业外部软件账号信息，企业内部系统，如企业邮箱、招聘系统、OA系统等关键业务系统，都出现了不同程度的账号泄露情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGTPaawBV5cUE4LWDaPwrJ344FuZS6YbqB3gibkJ6ib9NNGib47pYL7v2Cw/640?wx_fmt=png&from=appmsg)

这些系统作为企业内部通信、业务流程管理及知识资产存储的核心，普遍承载着大量敏感数据和关键信息。一旦某个员工的账号被恶意接管，便如同为企业的大门洞开了一道缝隙，让攻击者有机会窥探、窃取甚至篡改这些敏感数据，进而给企业带来损失。

这也说明，在数字化时代，企业员工的每一个账户都是企业安全防线的一环。任何一个环节的薄弱，都可能成为整个安全体系的突破口。

**二、威胁猎人ATO情报服务：**

**从外部视角及时、精准感知特权账号泄露风险**

**威胁猎人ATO情报监测解决方案**基于**多渠道海量情报**和**智能分析引擎**，通过**7×24小时实时监控和分析**暗网、匿名群聊等地下市场交易的账号泄露情报，能够快速识别与企业相关的账号信息泄露，从外部视角帮助合作客户了解其用户和员工账号的安全状态，及时预防和应对可能的ATO事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGDmBC50qjbOicrJBicezdrl72DBjicCJhvdUNticNKPiaP7Z2hxIHSTShC3w/640?wx_fmt=webp&from=appmsg)

**1、公开+私密情报持续拓源，实现情报源宽度与深度双重覆盖**

**在情报监测上，**威胁猎人覆盖了近200个黑产账号交易渠道，尤其是那些深藏于暗网及匿名群聊私域群的私密情报源，这些渠道往往掌握着非法获取或待售的企业特权账号信息，但因其严格的准入门槛而难以被常规手段触及。

通过深度挖掘这些私密情报源，威胁猎人能够提前预警潜在的账号泄露风险，**有效弥补了市面上其他仅依赖公开情报源方案在深度与广度上的不足**。

**在数据处理上，** 威胁猎人情报研究团队还会将来自不同渠道、类型、结构及模态的源数据高效整合，通过精细的**数据清洗、去重、关联分析和挖掘**，**提炼出与特权账号泄露事件相关的核心信息**，还可以提供特权账号泄露事件的安全报告服务，帮助企业快速响应、有效遏制特权账号泄露事件的发展。

**2、7\*24h数字风险应急响应，实时预警账号泄露威胁**

**服务能力建设上，**威胁猎人ATO情报监测解决方案集成了**实时预警与账号审计**两大核心功能。

实时预警功能可对企业特权账号的泄露情况进行实时监控，一旦发现异常，即可立即触发预警机制，迅速识别并防止账户接管攻击，帮助企业在账号被利用作恶之前采取措施，有效防止潜在的安全事件发生和经济损失。

此外，威胁猎人在深圳、重庆两地的**数字风险应急响应中心（DRRC）**运营团队**7\*24小时全天候**不间断地响应客户在账号接管情报监测中的服务需求，包括有效账号获取、情报分析、应急响应支持等。企业可以借助威胁猎人全面的情报和快速的响应机制，快速提高整体安全防护能力，将更多精力集中于自身业务发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqGlYlAq9Cicib1vlLFz7j4rgGiaibUaoApjBJWrkpMx8MYhUUgTMibp9zUiaM4OHlMKdDkqQFYic7EWibC5eA/640?wx_fmt=png&from=appmsg)

**特权账号管理对企业来说是一项关键的安全防护措施，**尤其在网络攻防演练中，特权账号已经成为攻击者入侵的首要目标**。**攻击者通过窃取合法用户或员工的账户凭据，进行未经授权的访问，窃取敏感信息，甚至进行欺诈性交易，不仅容易导致企业财务损失，还可能严重损害品牌声誉和客户信任。

因此，构建并实施一套全面而高效的特权账号管理体系，对企业而言，已不再是可选项，而是保障业务连续性、维护数据安全与合规性的必要基石。企业需要从战略高度出发，持续投入资源，不断优化完善，才能在数字化转型的浪潮中稳健前行，确保业务安全、数据无忧。

**最新动****态**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/4mAgZtBianqF8WeribLEjEd9PBGkiaN2jw4STHtj69gXB6uLSNY8z1tKB806BxJcman0YMy1ggDCIY4CBaT9t5tmg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247497933&idx=1&sn=ba4428c538b6ffd59873b4735fc145bd&chksm=eb12def6dc6557e0257e46994cdf2c5c051615d6968bda71c91d6566a02c151a3e887b6ff100&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqE6gJ7xBjpqStZvDJqarH2VfmKYEBicV0tqbD6NAKV2ibIhnDXM2asDbS5f98vyDicDdhOB2fiaicVyibwQ/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247498021&idx=1&sn=5af4d05557ccc404dfd60c7c1b3a77b3&chksm=eb12df1edc6556085378b613413e52d30c5f2449404d3d66259926af2623331bda28e784e417&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4mAgZtBianqGlofibYdicGYcWEGygCNQfLLGzicHIcZVPvpYjAJ2FQJcPY6ickJibez6NicG36cByX4YRVu22VMdesoUw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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