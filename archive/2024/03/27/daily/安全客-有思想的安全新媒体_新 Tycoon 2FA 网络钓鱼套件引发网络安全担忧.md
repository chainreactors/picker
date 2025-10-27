---
title: 新 Tycoon 2FA 网络钓鱼套件引发网络安全担忧
url: https://www.anquanke.com/post/id/294349
source: 安全客-有思想的安全新媒体
date: 2024-03-27
fetch_date: 2025-10-04T12:07:54.252587
---

# 新 Tycoon 2FA 网络钓鱼套件引发网络安全担忧

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 新 Tycoon 2FA 网络钓鱼套件引发网络安全担忧

阅读量**108039**

发布时间 : 2024-03-26 11:05:38

**x**

##### 译文声明

本文是翻译文章，文章来源：https://www.infosecurity-magazine.com/news/new-tycoon-2fa-phishing-kit/

译文仅供参考，具体内容表达以及含义原文为准。

一种名为 Tycoon 2FA 的新型网络钓鱼工具包引起了网络安全界的严重担忧。

 该工具包由 Sekoia 威胁检测与研究 (TDR) 团队于 2023 年 10 月发现，并在今天发布的一份公告中进行了讨论，该工具包与中间对手 (AiTM) 技术相关，据称被多个威胁行为者利用来策划广泛的攻击和有效的攻击。

 根据 Sekoia 的调查，Tycoon 2FA（双因素身份验证）平台至少自 2023 年 8 月起就一直活跃。自发现以来，该公司一直在积极监控与 Tycoon 2FA 相关的基础设施。

 分析显示，该工具包已成为最流行的 AiTM 网络钓鱼工具包之一，在 2023 年 10 月至 2024 年 2 月期间检测到了 1,100 多个域名。

 Tycoon 2FA 网络钓鱼工具包通过多个阶段运行，以有效执行其恶意活动。

 最初，受害者通过电子邮件附件或二维码被引导至一个包含 Cloudflare Turnstile 挑战的页面，该挑战旨在阻止不需要的流量。成功完成后，用户会遇到一个虚假的 Microsoft 身份验证页面，他们的凭据将在其中被获取。

 随后，网络钓鱼工具包将此信息中继到合法的 Microsoft 身份验证 API，拦截会话 cookie 以绕过多重身份验证 (MFA)。

 在今天的通报中，Sekoia 表示，它于 2024 年 2 月发现了 Tycoon 2FA 的新版本，其 JavaScript 和 HTML 代码发生了重大变化，增强了其网络钓鱼功能。值得注意的是，它重新组织了资源检索并扩展了流量过滤，以阻止机器人活动和分析尝试。

 与之前的版本相比，显着的变化包括：

* 初始 HTML 页面类似于第一阶段，保留其功能，但排除了 Cloudflare Turnstile 挑战。
* 随后的有效负载以可识别的模式命名，包含第 4 阶段（虚假登录页面）和新版本第 1 阶段（Cloudflare Turnstile 挑战）的元素。省略了反混淆中不必要的数学运算。
* 以前单独的 JavaScript 下载被合并到阶段 4 和阶段 5。这些阶段现在处理 2FA 实施和数据传输。
* 隐形策略得到改进，将恶意资源提供延迟到 Cloudflare 挑战解决之后。 URL 现在是随机命名的。
* 此外，该套件还可以通过识别和绕过各种流量模式（包括来自数据中心、Tor 和特定机器人用户代理的流量模式）来逃避分析。

 Sekoia 还警告 Tycoon 2FA 与其他已知网络钓鱼平台之间的潜在联系，建议共享基础设施和可能共享的代码库。

 该咨询补充道：“通过研究据称由 Saad Tycoon Group 进行的比特币交易，Sekoia 分析师认为，Tycoon Group 的业务利润丰厚。 ” “我们预计 Tycoon 2FA PhaaS 到 2024 年仍将是 AiTM 网络钓鱼市场的主要威胁。”

本文翻译自https://www.infosecurity-magazine.com/news/new-tycoon-2fa-phishing-kit/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294349](/post/id/294349)

安全KER - 有思想的安全新媒体

本文转载自: https://www.infosecurity-magazine.com/news/new-tycoon-2fa-phishing-kit/

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)