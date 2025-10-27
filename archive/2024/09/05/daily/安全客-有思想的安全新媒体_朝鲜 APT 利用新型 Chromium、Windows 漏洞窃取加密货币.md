---
title: 朝鲜 APT 利用新型 Chromium、Windows 漏洞窃取加密货币
url: https://www.anquanke.com/post/id/299776
source: 安全客-有思想的安全新媒体
date: 2024-09-05
fetch_date: 2025-10-06T18:20:03.432742
---

# 朝鲜 APT 利用新型 Chromium、Windows 漏洞窃取加密货币

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

# 朝鲜 APT 利用新型 Chromium、Windows 漏洞窃取加密货币

阅读量**95711**

发布时间 : 2024-09-04 14:49:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/vulnerabilities-threats/north-korean-apt-exploits-novel-chromium-windows-bugs-steal-crypto>

译文仅供参考，具体内容表达以及含义原文为准。

上个月，一名隶属于朝鲜情报机构的威胁行为者利用两个新漏洞试图从加密货币行业窃取资金。

大多数金融网络犯罪是由一些中级和低级别的网络罪犯所为，他们寻求快速获利。然而，据美国当局表示，朝鲜的情况并非如此，其对西方私营企业实施的复杂、涉及数百万甚至数十亿美元的网络攻击帮助资助了其核武器计划。

其最新的行动是迄今为止最先进的一次，首先在Windows和Chromium浏览器中串联利用之前未知的问题，然后加入rootkit以获得深层系统访问权限，从而对目标进行盗窃。

## 第 1 步：积极利用 Chromium 零日漏洞

8 月 21 日，谷歌发布了 Chrome 的更新，其中包括 38 个安全修复程序。不过，其中的亮点是 CVE-2024-7971。

CVE-2024-7971 是在 Chrome 和其他基于 Chromium 的浏览器中运行 JavaScript 的 V8 引擎中的一个类型混淆问题。通过使用特制的 HTML 页面，攻击者可以破坏浏览器的内存堆，并利用它来获得远程代码执行 （RCE） 功能。该问题获得了 CVSS 评级中的 8.8 分（满分 10 分）的“高”严重性。

不仅这个漏洞很严重，而且还被积极利用。

Microsoft — 其威胁情报中心 （MSTIC） 和安全响应中心 （MSRC） 最初向 Google 报告了该问题 — 现在已经在字里行间进行了着色。 在 8 月 30 日的一篇博文中，Microsoft 透露，朝鲜侦察总局 121 局内的一个实体——一个被追踪为 Citrine Sleet（又名 AppleJeus、Labyrinth Chollima、UNC4736 和 Hidden Cobra）的 APT——在针对加密公司以获取经济利益的活动中使用了 CVE-2024-7971。

Microsoft 拒绝向 Dark Reading 提供有关该活动的受害者或对这些受害者的后果的更多信息。

## 第 2 步：Windows 内核漏洞

典型的 Citrine Sleet 攻击以金融机构为目标，它从一个伪装成加密货币交易平台的虚假网站开始。它可以将该网站用作虚假职位空缺的启动板，或诱骗受害者下载带有其自定义木马 AppleJeus 的虚假加密钱包或交易应用程序。

在最近的这次活动中，受害者通过未知的社会工程策略被引诱到域名 voyagorclub[.]空间。那些连接到该域的人会自动触发 Chromium 中的零日内存损坏漏洞。

Citrine Sleet 几乎不满足于单个高严重性错误，将其 Chromium RCE 漏洞链接到第二个高严重性错误 CVE-2024-38106。CVE-2024-38106 是 Windows 内核中的权限提升，允许攻击者获得有价值的系统级权限。（其 CVSS 分数为 7.0，这可归因于其复杂性，以及它对目标计算机的现有本地访问的要求。

Microsoft 于 8 月 13 日修补了 CVE-2024-38106，距离发现最新的黄水晶雨夹雪活动不到一周。值得注意的是，它最近似乎也被一个完全不同的威胁行为者利用了。

## 第 3 步：获利？

“攻击链从直接破坏沙盒 Chrome 渲染器进程转变为破坏 Windows 内核，而不是以 Chrome 浏览器进程为目标，”Menlo Security 的首席安全架构师 Lionel Litty 解释说。“这意味着使用观察 Chrome 应用程序行为的工具检测异常的机会非常有限。”

“他补充说，”一旦进入内核，攻击者就处于一个公平的竞争环境中，端点上的安全工具，甚至可能占上风，检测到它们变得非常具有挑战性。

作为其权限提升的一部分，Citrine Sleet 部署了 FudModule，这是它与 APT Diamond Sleet 共享的 rootkit。FudModule 使用直接内核对象操作 （DKOM） 技术来优化内核安全检查，自三年前首次发现以来，至少在两个值得注意的实例中得到了改进。例如，今年早些时候，Avast 研究人员指出，它在 Microsoft Defender、Crowdstrike Falcon 和 HitmanPro 中具有破坏受保护流程轻量级 （PPL） 进程的新功能。

在到达目标系统的最内层后，Citrine Sleet 通常会部署其 AppleJeus 木马。AppleJeus 旨在获取窃取受害者的加密货币和加密货币相关资产所需的信息。

尽管如此，“在一些黑市中，Chrome 中的远程代码执行成本高达 100,000 美元——准确地说是 150,000 美元，”Avast 威胁情报总监 Michal Salát 指出。“Lazarus 在这些漏洞上消耗的金额相当大。我们在这里问自己的问题是：这对他们来说有多可持续？

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/vulnerabilities-threats/north-korean-apt-exploits-novel-chromium-windows-bugs-steal-crypto)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299776](/post/id/299776)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/vulnerabilities-threats/north-korean-apt-exploits-novel-chromium-windows-bugs-steal-crypto)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/north-korean-apt-exploits-novel-chromium-windows-bugs-steal-crypto>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [第 1 步：积极利用 Chromium 零日漏洞](#h2-0)
* [第 2 步：Windows 内核漏洞](#h2-1)
* [第 3 步：获利？](#h2-2)

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