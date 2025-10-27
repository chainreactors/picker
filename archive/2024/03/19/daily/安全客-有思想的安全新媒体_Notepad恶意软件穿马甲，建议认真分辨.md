---
title: Notepad恶意软件穿马甲，建议认真分辨
url: https://www.anquanke.com/post/id/294020
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:51.173031
---

# Notepad恶意软件穿马甲，建议认真分辨

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

# Notepad恶意软件穿马甲，建议认真分辨

阅读量**120575**

发布时间 : 2024-03-18 10:30:45

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/546796.php>

译文仅供参考，具体内容表达以及含义原文为准。

最近的研究发现，通过百度等搜索引擎搜索 Notepad++ 和 VNote 等官方版本程序的中国用户越来越多地中招。

这些攻击是利用搜索引擎上的欺诈性广告以及分发这些程序的木马版本的虚假链接来进行的。最终目标是安装 Geacon，Cobalt Strike 的 Golang 实现。

![]()广告导致虚假网站

卡巴斯基实验室的专家 发现 Notepad++ 搜索结果中出现了一个欺诈网站。该网站值得注意的是，其地址中提到了 VNote，并且该网站上提供的下载程序使用了 Notepad++ 徽标。

但更进一步，更有趣的是：下载的软件包已经包含“Notepad–”，但这并不是网络犯罪分子的发明，因为这是一个 完全现有的 合法文本编辑器，它几乎是 Notepad++ 的完整副本。

![]()诈骗网站上有趣的不一致之处

尽管可以在恶意网站上下载该程序的三个版本（适用于 Windows、Linux 和 macOS），但出于某种原因，Windows 的链接会指向带有合法记事本安装程序的官方 Gitee 存储库。同时，Linux和macOS版本导致第三方资源上存在恶意安装包。

第二个假页面是通过在百度搜索引擎中查询“vnote”找到的，而该页面又试图模仿VNote程序的官方网站，完全复制其风格。当然，该页面上也存在恶意软件。

对特洛伊木马安装程序的研究表明，它们旨在从远程服务器下载额外的恶意代码。该代码能够创建 SSH 连接、执行文件操作、枚举进程、访问剪贴板内容、启动程序、下载和上传文件、截屏，甚至休眠。通过HTTPS协议进行管理。

此处讨论的示例只是通过广告活动分发恶意软件的更大操作的一部分，这些广告活动以前曾用于使用伪装成 Microsoft OneNote、Notion 和 Trello 应用程序的 MSIX 安装文件来传播 FakeBat（也称为 EugenLoader）等病毒。

卡巴斯基实验室专家打算继续调查这一恶意活动，以确定攻击的其他阶段并防止恶意软件在用户之间传播。

建议用户在从互联网下载软件时要格外小心，并留意提供流行软件的网站上的任何可疑细节（从地址不一致到可疑设计或明显错误）。

本文翻译自 [原文链接](https://www.securitylab.ru/news/546796.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294020](/post/id/294020)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/546796.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**4赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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