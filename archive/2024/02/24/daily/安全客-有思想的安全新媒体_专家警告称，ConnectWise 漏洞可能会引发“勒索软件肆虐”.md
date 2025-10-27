---
title: 专家警告称，ConnectWise 漏洞可能会引发“勒索软件肆虐”
url: https://www.anquanke.com/post/id/293407
source: 安全客-有思想的安全新媒体
date: 2024-02-24
fetch_date: 2025-10-04T12:05:47.569257
---

# 专家警告称，ConnectWise 漏洞可能会引发“勒索软件肆虐”

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

# 专家警告称，ConnectWise 漏洞可能会引发“勒索软件肆虐”

阅读量**121693**

发布时间 : 2024-02-23 11:08:04

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

ConnectWise 周二表示，一个严重的 ConnectWise ScreenConnect 漏洞正在被广泛利用，该漏洞使数千台服务器面临被接管的风险。

ConnectWise周一发布了 ScreenConnect 23.9.7 的安全修复程序，披露了两个漏洞，其中包括一个 CVSS 最高得分为 10 的严重错误。该安全公告后来更新为已知针对该漏洞的三个 IP 地址。

Huntress 的研究人员表示，这个被追踪为CVE-2024-1709 的严重缺陷使得绕过身份验证并获得 ScreenConnect 实例的管理访问权限变得“微不足道且极其容易” 。

第二个错误（编号为CVE-2024-1708）是一个路径遍历漏洞，可能允许恶意 ScreenConnect 扩展在其预期子目录之外实现远程代码执行 (RCE)。

然而，Huntress 研究人员指出，仅利用 CVE-2024-1709 就足以实现 RCE。

本地 ConnectWise ScreenConnect 实例的管理员应立即升级到版本 23.9.8，以防止服务器受到损害。据 ConnectWise 称，云实例已经被修补。

**ScreenConnect 漏洞威胁无数下游端点**
ConnectWise ScreenConnect 通常被托管服务提供商 (MSP) 用于远程访问客户端点以获取 IT 支持等服务。

截至周三上午，Shadowserver 检测到约 3,800 个易受最新漏洞影响的 ScreenConnect 实例——估计占所有检测到实例的 93%。该组织在 X 上发布消息称，Shadowserver 周三也开始收到对其蜜罐的攻击请求。

由于每个 ScreenConnect 实例可能为数百或数千个端点提供服务，CVE-2024-1709 可能会为重大供应链攻击奠定基础，这与 Cl0p 勒索软件组织实施的MOVEit 黑客攻击不同，该攻击自2023 年 5 月以来已影响了 2,500 多个组织。

“我不能粉饰它——这太糟糕了，”Huntress 首席执行官凯尔·汉斯洛万 (Kyle Hanslovan) 在一份声明中告诉 SC Media。“该软件的广泛流行以及该漏洞提供的访问权限表明我们正处于勒索软件肆虐的风口浪尖。”

Huntress 也参与了 MOVEit 黑客攻击后的事件响应，并指出由于概念验证 (POC) 漏洞的存在而增加了危险，只有在其他供应商发布自己的 POC 后才决定发布自己的 POC。

Huntress 发言人表示，该公司与 ConnectWise 密切合作，研究该漏洞及其潜在影响。

“双用途软件会带来清算；就像今年夏天通过 MOVEit 发现的 Huntress 一样，它为 IT 团队提供的无缝功能也为黑客提供了同样的功能，”Hanslovan 说道。“利用远程访问软件，坏人可以像好人推送补丁一样轻松地推送勒索软件。一旦他们开始推广他们的数据加密器，我敢打赌 90% 的预防性软件不会捕获它，因为它来自可信的来源。”

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293407](/post/id/293407)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**7赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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