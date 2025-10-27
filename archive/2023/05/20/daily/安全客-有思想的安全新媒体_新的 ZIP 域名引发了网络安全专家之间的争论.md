---
title: 新的 ZIP 域名引发了网络安全专家之间的争论
url: https://www.anquanke.com/post/id/288784
source: 安全客-有思想的安全新媒体
date: 2023-05-20
fetch_date: 2025-10-04T11:37:04.287901
---

# 新的 ZIP 域名引发了网络安全专家之间的争论

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

# 新的 ZIP 域名引发了网络安全专家之间的争论

阅读量**220869**

发布时间 : 2023-05-19 11:59:48

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员和 IT 管理员对谷歌新的 ZIP 和 MOV 互联网域提出了担忧，警告称威胁行为者可能会利用它们进行网络钓鱼攻击和恶意软件传播。

本月早些时候， 谷歌推出了 八个新的顶级域 (TLD)，可以购买这些域来托管网站、电子邮件。

虽然 ZIP 和 MOV  TLD 自 2014 年以来一直可用，但直到本月它们才普遍可用，允许任何人为网站购买域，如 bleepingcomputer.zip。

但是，这些域可能被认为具有风险，因为 TLD 也是论坛帖子、消息和在线讨论中通常共享的文件的扩展名，现在某些在线平台或应用程序会自动将其转换为 URL。

##

在线看到的两种常见文件类型是 ZIP 存档和 MPEG 4 视频，其文件名以 .zip（ZIP 存档）或 .mov（视频文件）结尾。因此，人们发布包含扩展名为 .zip 和 .mov 文件名的链接是很常见的。

但是，既然它们是 TLD，一些消息传递平台和社交媒体网站会自动将扩展名为 .zip 和 .mov 的文件名转换为 URL。

例如，在 Twitter 上，如果您向某人发送有关打开 zip 文件和访问 MOV 文件的说明，无害的文件名将转换为 URL，如下所示。

![]()

Twitter 自动链接 .zip 和 .mov 文件名

当人们在说明中看到 URL 时，他们通常认为该 URL 可用于下载相关文件，并可能会点击该链接。例如，将文件名链接到下载是我们通常在文章、教程和论坛中提供有关 BleepingComputer 的说明的方式。

但是，如果威胁行为者拥有与链接文件名同名的 .zip 域，则有人可能会错误地访问该站点并落入网络钓鱼诈骗或下载恶意软件，并认为该 URL 是安全的，因为它来自受信任的来源。

虽然威胁行为者不太可能注册数千个域来捕获少数受害者，但您只需要一名公司员工错误地安装恶意软件就会影响整个网络。

滥用这些域不是理论上的，网络情报公司 Silent Push Labs 已经发现 microsoft-office[.]zip 中似乎是一个网络钓鱼页面，试图窃取 Microsoft 帐户凭据。

![]()

网络安全研究人员也开始研究域名，Bobby Rauch发表了关于使用 Unicode 字符和 URL 中的用户信息分隔符(@)开发令人信服的网络钓鱼链接的研究。

Rauch 的研究表明威胁行为者如何制作看起来像 GitHub 上合法文件下载 URL 的网络钓鱼 URL，但在单击时实际上会将您带到 v1.27.1[.]zip 的网站，如下图所示。

`https://github.com/kubernetes/kubernetes/archive/refs/tags/@v1.27.1.zip`

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288784](/post/id/288784)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**6赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168535)

[安全客](/member.html?memberId=168535)

这个人太懒了，签名都懒得写一个

* 文章
* **122**

* 粉丝
* **0**

### TA的文章

* ##### [注册机内藏勒索软件！收款竟用支付宝？](/post/id/292743)

  2024-01-19 11:10:00
* ##### [全球首发！《2023年度统信UOS安全威胁防御报告》来了](/post/id/292263)

  2023-12-29 11:27:27
* ##### [数字安全“奥斯卡”落幕，ISC 2023创新百强重磅出炉](/post/id/292240)

  2023-12-29 10:24:44
* ##### [一个安全运营工程师的自白](/post/id/291372)

  2023-11-15 10:40:17
* ##### [打造实战型安全人才新高地，360发布ISC安全课SaaS化教培平台](/post/id/291209)

  2023-11-03 17:22:35

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