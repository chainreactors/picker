---
title: API NEWS | 关于​Urlscan.io网站泄露敏感URL和数据
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496389&idx=1&sn=2275dfa2bd944449e7e7ce04c5e03a4a&chksm=c0075f59f770d64f083bce8a50ae4c016736ac3c3f66440426ed2bc3f3b837f23e4042effa6d&scene=58&subscene=0#rd
source: 星阑科技
date: 2022-11-12
fetch_date: 2025-10-03T22:32:48.373335
---

# API NEWS | 关于​Urlscan.io网站泄露敏感URL和数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOejMS5G9c3PeiaHV71yRU9Fa6q2yn1lb7xu6E9dJW3QN0nN2SojW4jlibtd2VIZnz5QeGFpY23TtRswA/0?wx_fmt=jpeg)

# API NEWS | 关于​Urlscan.io网站泄露敏感URL和数据

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

欢迎大家围观小阑精心整理的API安全最新资讯，在这里你能看到最专业、最前沿的API安全技术和产业资讯，我们提供关于全球API安全资讯与信息安全深度观察。

**本周，我们带来的分享如下：**

* Urlscan.io泄露敏感URL和数据
* Dropbox网络钓鱼攻击泄露了130个代码存储库
* 微服务合同测试

**Urlscan.io泄露敏感URL和数据**

PortSwigger关于Urlscan.io网站最近漏洞的报告，该漏洞无意中泄露了URL和其他敏感数据，包括电子邮件。Urlscan.io是业内流行的工具，用于在网站上进行自动扫描，以评估它们是否包含恶意内容。Urlscan.io服务提供了一个API，允许用户自动扫描网站，作为防御策略的一部分，例如，在所有传入的电子邮件上。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejMS5G9c3PeiaHV71yRU9Fa6wiaqdq45CroTexpxCDW0ooyVyneiczuRbrlqHUrEYjQa9kKFBkIBcNtw/640?wx_fmt=png)

今年GitHub发出了警报，发现某些GitHub Pages URL被意外泄露。上周，Positive Security发表了一篇详细的博客，讲述了他们如何判断敏感信息被泄露。最令人担忧的是大量泄露的敏感信息，包括密码重置链接、会议邀请、设置页面、DocuSign请求、软件包跟踪链接......这可能得益于Urlscan.io上的搜索功能，该功能允许对手使用“Google dorks”搜索常见链接——例如，此查询显示了URL中大量潜在API密钥列表。

根本原因是Urlscan.io提供的API SDK中配置错误的API调用（他们在术语中调用这些包）。在调用Urlscan.io API时，调用客户端指定要扫描的URL和其他一些参数，包括Urlscan.io平台上扫描结果的可见性——不幸的是，似乎选择了public作为默认值。虽然严格来说，这不是API中的漏洞，但这肯定说明了明智和安全默认值的重要性。

不幸的是，删除敏感URL是一个手动过程，必须与Urlscan.io支持团队一起启动——许多大公司，如苹果，已经删除了他们的URL。

**Dropbox网络钓鱼攻击泄露了130个代码存储库**

据报道，本周的第二个漏洞是，在一次明显的网络钓鱼攻击中复制了属于Dropbox的130个私有GitHub存储库。登记册提供了他们对漏洞的惯常分析，这导致许多秘密API令牌泄露，并需要轮换事件中访问的所有开发人员API凭据。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejMS5G9c3PeiaHV71yRU9Fa6FfzuAzJzzqDz4gILBWMesNJFky92pJnZtibepXuLt7KiaXOFhk8oLfUw/640?wx_fmt=png)

该漏洞遵循了一种相当熟悉的模式，即通过第三方连接服务攻击网站。据报道，Dropbox使用流行的CI/CD平台CircleCI进行内部构建，该平台与他们的私有GitHub代码存储库集成。在这种情况下，攻击者向Dropbox开发人员发送网络钓鱼电子邮件，这诱骗他们访问一个伪造的CircleCI登录页面，在那里他们输入了他们的凭据（包括OTP）。使用泄露的凭据，攻击者可以访问连接的GitHub组织，包括访问私有存储库。

Dropbox忘记了这项活动，直到GitHub的安全监控团队提醒他们存储库上的可疑活动后，漏洞才被曝光。事实上，GitHub最近才发布了关于使用CircleCI作为诱饵的这次攻击的安全警告。

显然，Dropbox在其安全流程中不那么出色——不幸的是，无论提供多少意识培训，网络钓鱼都是不可避免的；然而，人们预计这些虚假的CircleCI URL很容易在电子邮件过滤器中被检测到。更严重的问题是将API令牌存储在代码存储库中；至少在这种情况下，有一个协议可以撤销令牌。请记住，在连接第三方服务时，始终使用范围和生命周期限制在最低限度的令牌。

**微服务合同测试**

本周，TechTarget发表了一篇关于微服务合同测试重要性的文章，对于任何采用API设计第一方法的人来说，这值得一读。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejMS5G9c3PeiaHV71yRU9Fa6nLXElUvtSjelaS8AuCgAMHC6eZaSoYBtHq6egaicYY7al4SKGYEg2OQ/640?wx_fmt=png)

**作者强调了集成商和测试团队在构建大规模基于微服务的系统时面临的一些共同挑战，例如：**

**• 太多的集成无法测试：**随着微服务的持续增长（由API启用），测试单个微服务变得越来越困难，测试人员开始依赖于测试端到端系统，因此很难识别故障点。

**• 不匹配的微服务版本：**由于微服务更新更频繁，管理其版本变得困难，这意味着经常针对较新版本的API运行测试，这可能会导致脆弱的系统。

**• 缺乏明确的测试要求：**除非测试人员对服务的预期行为非常清楚，否则很难确定通过或失败的条件。

**合同测试有几个关键优势：**

**• 规模：**个人服务可以在开发点进行本地测试，而无需等待完整的端到端部署。

**• 可管理的测试：**如果只有两个微服务发生变化，则没有必要测试整个系统；相反，受影响的服务可以根据其合同进行隔离测试。

**• 范围：**合同准确定义了预期行为，消除了测试人员脑海中对测试范围的疑虑。

感谢 APIsecurity.io 提供相关内容

**关于星阑**

星阑科技基于AI深度感知和强大的自适应机器学习技术，帮助用户迅速发现并解决面临的安全风险和外部威胁，并凭借持续的创新理念和以实战攻防为核心的安全能力，发展成为国内人工智能、信息安全领域的双料科技公司。为解决API安全问题，公司从攻防能力、大数据分析能力及云原生技术体系出发，提供全景化API识别、API高级威胁检测、复杂行为分析等能力，构建API Runtime Protection体系。

**星阑科技产品——萤火 (API Intelligence) 拥有不同应用场景的解决方案**，适配服务器、容器集群、微服务架构以及云平台等多种架构。**通过API资产梳理、漏洞管理、威胁监测、运营与响应能力，解决企业API漏洞入侵、数据泄露两大核心风险。**

**往期 · 推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5aaaIEbK8js13dUHyRfibIdUys85kCDVCramykaQGeXgc8p9JQnS1geQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493320&idx=1&sn=41d96f17d2a226c31b23b35d93a36f2a&chksm=c0074b54f770c242d6897443eb4980fb58a0f065ea2d8593cb3b8548b370bc075acc57a7c1c1&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5vlPrkrPnU4NyZ0iczokrvBmOTVJicE184CicXlbFiaZWJOndBYBGicG2hdw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493183&idx=1&sn=2af1758db0a3a191fab5a06c5d42d5e2&chksm=c0074ba3f770c2b5f823d3d51f8dca78e4992fed1af362fd343cccff4869215b4cdd1d530c14&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM52U6A0N7fnFeFsaWichvGj4xZZ3LbRJwc4CT8zvnZw5ZOjVlQ6Fgiczgg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493126&idx=1&sn=58636a0f6eb16b77ab08166257c8ac39&chksm=c0074b9af770c28c03fb7893f6f2f624955bcf1791a34be921b46b139084690227b01e8a79e7&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5DNcU7icAy0S11XGM1klz1juoesMJBlWkgqIZa6amb13MmibdhLwkuGLw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493022&idx=1&sn=a39a77fbab2b9b01c50c77ab9e9f3cda&chksm=c0074802f770c11453cbfb45123934a5fa24979d0a0d779dbb9b390d8a276fd06bc80ffddb4a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOehwcHoxicoOah5mxDjLHMZ9RHUxNeibERphRXOj3AEupxt7JyOt3LF1RmmWQibYmicTv2DxM93iaEJhLxw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

星阑科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

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