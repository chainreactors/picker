---
title: 新的 HTML 走私活动向讲俄语的用户提供 DCRat 恶意软件
url: https://www.anquanke.com/post/id/300564
source: 安全客-有思想的安全新媒体
date: 2024-10-01
fetch_date: 2025-10-06T18:50:51.613188
---

# 新的 HTML 走私活动向讲俄语的用户提供 DCRat 恶意软件

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

# 新的 HTML 走私活动向讲俄语的用户提供 DCRat 恶意软件

阅读量**298126**

发布时间 : 2024-09-30 15:01:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html>

译文仅供参考，具体内容表达以及含义原文为准。

讲俄语的用户已成为一项新活动的一部分，该活动通过一种称为 HTML 走私的技术分发名为 DCRat（又名 DarkCrystal RAT）的商品木马。

这一发展标志着恶意软件首次使用这种方法进行部署，与以前观察到的传递媒介不同，例如受感染或虚假网站，或带有 PDF 附件或带有宏的 Microsoft Excel 文档的网络钓鱼电子邮件。

“HTML 走私主要是一种有效载荷传递机制，”Netskope 研究员 Nikhil Hegde 在周四发表的分析中说。“有效负载可以嵌入到 HTML 本身中，也可以从远程资源中检索。”

反过来，HTML 文件可以通过虚假网站或恶意垃圾邮件活动传播。一旦通过受害者的 Web 浏览器启动文件，隐藏的有效载荷就会被解码并下载到机器上。

该攻击随后依靠某种程度的社会工程来说服受害者打开恶意负载。

Netskope 表示，它发现在俄语中模仿 TrueConf 和 VK 的 HTML 页面，当在 Web 浏览器中打开时，它们会自动将受密码保护的 ZIP 存档下载到磁盘，以试图逃避检测。ZIP 有效负载包含一个嵌套的 RarSFX 存档，最终导致 DCRat 恶意软件的部署。

DCRat 于 2018 年首次发布，能够作为一个成熟的后门运行，可以与其他插件配对以扩展其功能。它可以执行 shell 命令、记录击键以及泄露文件和凭据等。

建议组织检查 HTTP 和 HTTPS 流量，以确保系统不会与恶意域通信。

这一发展是在俄罗斯公司成为一个名为 Stone Wolf 的威胁集群的目标之际，通过发送伪装成合法工业自动化解决方案提供商的网络钓鱼电子邮件，用 Meduza Stealer 感染它们。

“攻击者继续使用包含恶意文件和合法附件的档案，以分散受害者的注意力，”BI 说。ZONE 说。通过使用真实组织的名称和数据，攻击者有更大的机会诱骗受害者下载和打开恶意附件。

它还遵循恶意活动的出现，这些活动可能利用生成式人工智能 （GenAI） 来编写 VBScript 和 JavaScript 代码，负责通过 HTML 走私传播 AsyncRAT。

“脚本的结构、注释以及函数名称和变量的选择是威胁行为者使用 GenAI 创建恶意软件的有力线索，”HP Wolf Security 表示。“该活动展示了 GenAI 如何加速攻击并降低网络犯罪分子感染端点的门槛。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300564](/post/id/300564)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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