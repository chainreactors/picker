---
title: GoldenJackal APT 组织入侵欧洲的空气屏蔽系统
url: https://www.anquanke.com/post/id/300849
source: 安全客-有思想的安全新媒体
date: 2024-10-15
fetch_date: 2025-10-06T18:45:31.849036
---

# GoldenJackal APT 组织入侵欧洲的空气屏蔽系统

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

# GoldenJackal APT 组织入侵欧洲的空气屏蔽系统

阅读量**80880**

发布时间 : 2024-10-14 15:49:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Help Net Security，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/10/09/goldenjackal-air-gapped-systems-compromise/>

译文仅供参考，具体内容表达以及含义原文为准。

ESET 研究人员发现，从 2022 年 5 月到 2024 年 3 月，欧洲发生了一系列攻击事件，攻击者使用的工具集能够攻击欧盟某国政府组织的空中屏蔽系统。

网络间谍活动旨在从孤立网络中窃取敏感数据
ESET 认为该网络间谍活动是 GoldenJackal 所为，这是一个以政府和外交实体为目标的网络间谍 APT 组织。通过分析该组织部署的工具集，ESET 发现 GoldenJackal 早在 2019 年就针对南亚驻白俄罗斯大使馆实施过一次攻击，该攻击利用定制工具瞄准了大使馆的空中屏蔽系统。

GoldenJackal 的最终目标很可能是窃取机密和高度敏感的信息，尤其是从可能没有连接到互联网的高端机器上窃取信息。

为了最大限度地降低泄密风险，高度敏感的网络通常都会进行空气隔离，即与其他网络隔离。通常，企业会对其最有价值的系统（如投票系统和运行电网的工业控制系统）进行空气隔离。这些网络往往正是攻击者感兴趣的网络。与攻破互联网连接的系统相比，攻破空气屏蔽网络的资源密集程度要高得多，这意味着迄今为止，专门用于攻击空气屏蔽网络的框架都是由 APT 组织开发的。此类攻击的目的始终是间谍活动。

“2022年5月，我们发现了一个工具集，我们无法将其归属于任何APT组织。但是，一旦攻击者使用了一种与已公开记录的工具类似的工具，我们就能深入挖掘，发现公开记录的 GoldenJackal 工具集与这种新工具集之间存在联系。ESET研究员马蒂亚斯-波罗利（Matías Porolli）分析了GoldenJackal的工具集，他说：”据此推断，我们设法确定了早先的一次攻击，在那次攻击中部署了公开文档中的工具集，以及一个更早的工具集，该工具集也具有攻击空中封闭系统的功能。

GoldenJackal 的目标是欧洲、中东和南亚的政府实体
GoldenJackal 一直以欧洲、中东和南亚的政府机构为目标。ESET 于 2019 年 8 月和 9 月在南亚驻白俄罗斯大使馆检测到 GoldenJackal 工具，并于 2021 年 7 月再次检测到 GoldenJackal 工具。最近，根据 ESET 的遥测数据，从 2022 年 5 月到 2024 年 3 月，欧洲的另一个政府组织多次成为攻击目标。

就所需的复杂程度而言，GoldenJackal 在五年内成功部署了两个不同的工具集来入侵空气屏蔽系统，这是很不寻常的。这说明了该组织的足智多谋。针对南亚驻白俄罗斯大使馆的攻击使用了定制工具，迄今为止我们只在这一特定案例中见过。该活动使用了三个主要组件： GoldenDealer 用于通过 USB 监控将可执行文件发送到空气屏蔽系统；GoldenHowl 是一个具有各种功能的模块化后门；GoldenRobo 是一个文件收集器和外泄器。

“当受害者将被入侵的 U 盘插入空气屏蔽系统，并点击一个名为文件夹图标但实际上是恶意可执行文件的组件时，GoldenDealer 就会被安装并运行，开始收集空气屏蔽系统的信息，并将其存储在 U 盘中。当再次将 U 盘插入联网的电脑时，GoldenDealer 就会从 U 盘中获取有关空气屏蔽电脑的信息，并将其发送到 C&C 服务器。服务器会回复一个或多个可执行文件，以便在空气屏蔽电脑上运行。最后，当 U 盘再次插入被窃电脑时，GoldenDealer 就会从 U 盘中取出并运行这些可执行文件。由于 GoldenDealer 已经在运行，因此不需要用户交互。

在最近一系列针对欧盟某政府组织的攻击中，GoldenJackal 从最初的工具集转向了高度模块化的新工具集。这种模块化方法不仅适用于恶意工具，也适用于受害主机在被入侵系统中的角色：它们被用于收集和处理有趣的、可能是机密的信息，向其他系统分发文件、配置和命令，以及外泄文件等。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/10/09/goldenjackal-air-gapped-systems-compromise/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300849](/post/id/300849)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/10/09/goldenjackal-air-gapped-systems-compromise/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/10/09/goldenjackal-air-gapped-systems-compromise/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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