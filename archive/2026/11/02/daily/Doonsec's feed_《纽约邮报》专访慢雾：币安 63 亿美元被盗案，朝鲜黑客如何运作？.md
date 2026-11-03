---
title: 《纽约邮报》专访慢雾：币安 63 亿美元被盗案，朝鲜黑客如何运作？
url: https://mp.weixin.qq.com/s/bg35jNCniqHNB-BfmT1dlA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:08.177218
---

# 《纽约邮报》专访慢雾：币安 63 亿美元被盗案，朝鲜黑客如何运作？

# 《纽约邮报》专访慢雾：币安 63 亿美元被盗案，朝鲜黑客如何运作？

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**************近日，美国知名媒体《纽约邮报》(New York Post) 发布报道《How North Korea’s ruthless state-sponsored hackers, main suspects in the $6.3B Binance heist, operate》，聚焦朝鲜黑客组织在加密货币盗窃活动中的运作方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCLtian0eUP0ouRkBL0HjSJnTIK50B9xyOPcIficibtyvjLHO6tMKFM9oLpMxdrEoA5iaDgBFaI7mfwJt5T75cCQ1z7FiaNfITxfNuBE/640?wx_fmt=jpeg)

(https://nypost.com/2026/10/30/tech/how-north-koreas-ruthless-state-sponsored-hackers-main-suspects-in-the-6-3b-binance-heist-operate/)

报道将朝鲜黑客组织列为币安(Binance) 约 63 亿美元被盗事件的主要嫌疑人，并采访了慢雾(SlowMist) 安全运营负责人 Lisa 和创始人 Cos。两位受访者围绕朝鲜黑客组织的攻击手法、链上资金追踪、跨国攻击网络及 AI 技术对网络攻击的影响等话题，分享了慢雾的调查发现与分析。

## 币安 63 亿美元被盗案：朝鲜黑客成为主要嫌疑人************

************##

慢雾安全运营负责人 Lisa 在采访中透露，慢雾**旗下反洗钱 & 链上追踪工具  MistTrack**在追踪被盗资金时发现，与币安被盗资金相关的地址与 2025 年初 Phemex 被盗事件中涉及的地址存在关联。此前，慢雾的调查已发现 Phemex 被盗事件与朝鲜黑客组织存在关联。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJWoR7h156yfFSuWUXtTzFHqNIyOjbEAicotDjM4eoRG5Vxic0ItibXtDGQiaLK1455kmYP5WGZMefo5YbRib3R9lwBfYFeJic44JIcM/640?wx_fmt=png&from=appmsg)

(https://x.com/MistTrack\_io/status/2116021647279005841)

Lisa 强调，朝鲜黑客组织的优势不仅体现在攻击能力上，也体现在长期积累的资金转移与洗钱基础设施上。被盗加密资产通常会在不同数字钱包之间快速转移，并通过兑换其他加密货币等方式，增加后续追踪和拦截的难度。

## 攻击从社会工程开始，人员防护同样关键************

************##

谈及朝鲜黑客组织的攻击手段，Lisa 指出，与传统黑客组织直接寻找代码漏洞不同，朝鲜黑客往往从针对人员的社会工程攻击入手。

在具体实施过程中，攻击者通常会先通过伪装身份与开发人员建立信任。慢雾在 2025 年开展的一项[调查](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501259&idx=1&sn=0b2183929367aa5845f0a9e1d1a42e74&scene=21#wechat_redirect)发现，攻击者曾冒充项目团队，以付费修复软件为由联系开发人员；也有攻击者伪装成投资者，向开发人员提供交易软件供其测试。部分攻击者甚至会提前支付报酬，以此建立信任。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJ4g6W3F16wvxF6JH5IPwdQmyianvqtCtIQW6tHYw6AfwXkFA25Kic8q4whmzxyyyR3j2PbmATUbvVTNXR5qMkNGyRLmjaamotBg/640?wx_fmt=png&from=appmsg)

取得信任后，攻击者便可能进一步将恶意代码植入正常的软件开发和协作流程中。 他们会对真实且公开可用的软件项目进行修改，并将恶意代码隐藏其中。从表面来看，调试代码、测试功能或修改配置等操作，都可能只是正常开发流程的一部分。

即使开发人员采取了安全措施，也未必能够完全规避此类攻击。 Lisa 举例称，部分开发人员会选择在隔离环境中运行软件，但攻击者可能随后以项目无法正常运行为由，要求其进行看似合理的配置调整，进而削弱原有隔离环境的防护效果，并逐步获取更多控制权限。一旦进入目标公司的内部网络，攻击者便可能进一步窃取凭证，尝试接近与公司资金管理相关的关键系统，同时利用企业自身的工具掩饰攻击活动。

此外，攻击者还会利用受害者的心理弱点，进一步增加事件调查的难度。Lisa 提到，部分员工在意识到自己可能遭到欺骗后，会因为担心承担责任而主动删除相关记录，甚至未能及时报告安全事件。这不仅增加了后续调查和证据收集的难度，也可能为攻击者争取更多时间。

## 跨国网络为攻击活动提供更多入口************

************##

慢雾创始人 Cos 在采访中指出，朝鲜黑客组织，包括 Lazarus Group（及其下属分支 Bluenoroff 和 Andariel 等），会利用其他国家和地区的网络环境作为攻击跳板，以此扩大攻击范围。

例如，攻击者可能先入侵美国境内的某个系统，再利用该系统作为跳板，将攻击活动延伸至欧洲、日本等其他地区。

Cos 表示，外界通常认为朝鲜是一个相对封闭、与世界联系有限的国家，但这并不意味着其黑客组织的活动范围也受到限制。即使是身处美国的个人所使用的计算机，也可能成为攻击者实施攻击的入口。

他强调，这类活动有国家力量作为支撑，攻击者能够通过多个中间节点构建跨国攻击网络，使其具备触及全球不同地区目标的能力。

## AI 技术正在扩大攻击活动的规模************

************##

采访中，Cos 还谈到了 AI 技术对网络攻击活动带来的影响。

随着 AI 工具的应用，攻击者能够更高效地完成恶意代码编写、攻击载荷准备等工作。过去需要人工投入大量时间的代码编写和重复性操作，如今也可以借助 AI 提高效率。

Cos 指出，过去一个黑客组织可能需要花费六个月至一年的时间，将攻击目标集中在 5 至 10 个对象上；而在 AI 的辅助下，未来攻击者可能将目标数量扩大至 50 至 100 个。这意味着，AI 不仅能够降低攻击活动的时间和人力成本，也可能进一步扩大攻击者能够覆盖的目标范围。

结语

**********此次《纽约邮报》的报道从社会工程攻击、链上资金追踪、跨国攻击网络及 AI 技术应用等多个角度，呈现了朝鲜黑客组织的行动特点，也反映出当前加密资产安全威胁背后的组织化运作与技术演变。**********

面对不断演变的攻击手段，安全防护不能只关注代码与基础设施层面的风险，还需要重视人员安全意识、链上资金监测和跨团队情报协作。慢雾将持续通过安全事件分析、威胁情报挖掘与链上追踪，关注相关攻击组织的活动及其资金流向，为 Web3 生态安全提供支持。

**最后，感谢《纽约邮报》的专访报道！**

原文报道：https://nypost.com/2026/10/30/tech/how-north-koreas-ruthless-state-sponsored-hackers-main-suspects-in-the-6-3b-binance-heist-operate/**************

**往期回顾**

[一鱼多吃 —— zkLink 被盗 78 万美元事件解析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247506498&idx=1&sn=a7646de265d6c5c01cf91b8b5cb91480&scene=21#wechat_redirect)

[倒计时 3 天｜2026 香港 RWA 与稳定币支付机构闭门峰会议程公布](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247506498&idx=2&sn=428e017919b0d41244bd1083735f96b1&scene=21#wechat_redirect)

[MistTrack 季度更新：KYA 批量筛查与追踪画布上线](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247506463&idx=1&sn=f5023f07f88a65589cb3858da51ae3f2&scene=21#wechat_redirect)

[威胁情报｜Udesk 加载恶意 JS，窃密篡改转账地址](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247506417&idx=1&sn=32e30273fd88ef1fce4d2777602b7408&scene=21#wechat_redirect)

[架构破局，风控筑底｜慢雾将举办 2026 香港 RWA 与稳定币支付机构闭门峰会](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247506411&idx=1&sn=1c22b44195fa686f055b08dc2cb129c8&scene=21#wechat_redirect)

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

阅读原文

不喜欢

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