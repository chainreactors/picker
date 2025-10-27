---
title: 新网络钓鱼攻击利用 Microsoft Office 来部署 NetSupport RAT
url: https://www.anquanke.com/post/id/294129
source: 安全客-有思想的安全新媒体
date: 2024-03-21
fetch_date: 2025-10-04T12:11:15.136959
---

# 新网络钓鱼攻击利用 Microsoft Office 来部署 NetSupport RAT

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

# 新网络钓鱼攻击利用 Microsoft Office 来部署 NetSupport RAT

阅读量**89019**

发布时间 : 2024-03-20 10:49:08

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/03/new-phishing-attack-uses-clever.html

译文仅供参考，具体内容表达以及含义原文为准。

[![网络支持RAT]( "网络支持RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcVPcQR4zsxsRuCOV212HAnLxhRUOiKxkvnlTZJui4qWjY32Z-q3ro47393ovcV8p5YQim8oyo-lPNuFcO4FUGPdYU-5J3q5QElbJSn7BbtexvQsvAOyZg1fdZq6PtKn7BdqO888q7XpLaZrb79W0uc6jxbSnGl6KqF2k-MuT224hxho129pVTxRWvwP8l/s728-rw-e365/cyber.jpg)

以色列网络安全公司 Perception Point 正在追踪名为“Operation PhantomBlu”的活动，这是一项新的网络钓鱼活动针对美国组织，旨在部署名为 NetSupport RAT 的远程访问木马。

安全研究员 Ariel Davidpur表示：“PhantomBlu 操作引入了一种微妙的利用方法，与 NetSupport RAT 的典型交付机制不同，它利用 OLE（对象链接和嵌入）模板操作，利用 Microsoft Office 文档模板执行恶意代码，同时逃避检测。 ”

NetSupport RAT 是合法远程桌面工具（称为 NetSupport Manager）的恶意分支，允许威胁参与者在受感染的端点上执行一系列数据收集操作。

起点是一封以薪资为主题的网络钓鱼电子邮件，该电子邮件自称来自会计部门，并敦促收件人打开随附的 Microsoft Word 文档以查看“月度薪资报告”。

对电子邮件标头（尤其是 Return-Path 和 Message-ID 字段）的仔细分析表明，攻击者使用名为 Brevo（以前称为 Sendinblue）的合法电子邮件营销平台来发送电子邮件。

Word 文档打开后，会指示受害者输入电子邮件正文中提供的密码并启用编辑，然后双击文档中嵌入的打印机图标以查看工资图表。

[![微软办公软件]( "微软办公软件")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigKsZ0DBQj6eIXdw0GuOpPSC3-Vyk1Ela8M7V6myHjNfUMSd0T0JrO1GyY9oiB6UST4Jqr56KiDgTNqFMnb6N_blSqwzQPMMeIiRCvm9sLTguU-x568I2-K0M65dXsnjtvbc7tZxTdP0bj5yc5qiH779K7Zt8HgTrCm4QeiUX4rHZE56O2dHRho9ZqBNyx/s728-rw-e365/dropbox.jpg)

这样做会打开一个 ZIP 存档文件（“Chart20072007.zip”），其中包含一个 Windows 快捷方式文件，该文件充当 PowerShell 释放器，用于从远程服务器检索并执行 NetSupport RAT 二进制文件。

Davidpur 表示：“通过使用加密的 .docs 通过 OLE 模板和模板注入来提供 NetSupport RAT，PhantomBlu 标志着与 NetSupport RAT 部署通常相关的传统 TTP 的背离。”他补充道，更新后的技术“展示了 PhantomBlu 在融合复杂规避策略方面的创新”与社会工程。”

Resecurity 透露，威胁行为者越来越多地滥用 Dropbox、GitHub、IBM Cloud 和 Oracle Cloud Storage 等公共云服务，以及 Pinata 等基于星际文件系统 (IPFS) 协议构建的 Web 3.0 数据托管平台。使用现成的工具包生成完全无法检测 (FUD) 的网络钓鱼 URL。

BulletProofLink 、FUDLINKSHOP、FUDSENDER、ONNX 和 XPLOITRVERIFIER等地下供应商在 Telegram 上提供此类 FUD 链接，作为订阅模式的一部分，价格从每月 200 美元起。这些链接在反机器人屏障后面得到进一步保护，以过滤传入流量并逃避检测。

HeartSender 等工具也是对这些服务的补充，可以大规模分发生成的 FUD 链接。与 HeartSender 相关的Telegram 群组拥有近 13,000 名订阅者。

该公司表示：“FUD 链接代表了[网络钓鱼即服务]和恶意软件部署创新的下一步。”并指出攻击者正在“为恶意用例重新利用高信誉的基础设施”。

“最近的一次恶意活动利用了 Rhadamanthys Stealer 来针对石油和天然气行业，使用了一个嵌入式 URL，该 URL 利用了合法域（主要是 Google 地图和 Google 图片）上的开放重定向。这种域嵌套技术使恶意 URL 不那么引人注目，并且更有可能诱骗受害者。”

本文翻译自https://thehackernews.com/2024/03/new-phishing-attack-uses-clever.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294129](/post/id/294129)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/03/new-phishing-attack-uses-clever.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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