---
title: 未修补的漫威游戏RCE漏洞可能会让黑客接管PC和PS5
url: https://www.anquanke.com/post/id/304032
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:51.469985
---

# 未修补的漫威游戏RCE漏洞可能会让黑客接管PC和PS5

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

# 未修补的漫威游戏RCE漏洞可能会让黑客接管PC和PS5

阅读量**249697**

发布时间 : 2025-02-10 14:37:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/unpatched-marvel-game-rce-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

热门在线游戏《漫威对决》（Marvel Rivals ）中发现了一个严重的安全漏洞，这引发了对黑客可能利用不知情玩家的担忧。

该漏洞被认定为远程代码执行（RCE）漏洞，同一网络中的攻击者可借此在其他玩家设备上运行任意代码。这一缺陷凸显了游戏行业安全措施方面一直存在的问题。

### ****远程代码执行漏洞****

问题源于《漫威对决》的热修复补丁系统，该系统使用远程代码执行来更新游戏。

然而，该系统并未验证其连接的是否为合法游戏服务器。雪上加霜的是，游戏在玩家设备上以管理员权限运行，这一举措本是为了防止作弊，但却极大地增加了被利用的风险。

这种不安全的服务器验证与提升的权限相结合，为攻击者创造了绝佳机会。

黑客只需与受害者处于同一 Wi-Fi 网络，就能在受害者不知情的情况下在其设备上执行有害命令。

RCE 漏洞是软件中最危险的漏洞之一，因为它们能让攻击者完全控制一个系统。

这个漏洞的影响范围不止于个人电脑。研究人员分享的一个概念验证视频显示，该漏洞还可能成为攻击运行《漫威对决》的 PlayStation 5 主机的切入点。

这引发了对更广泛平台安全的担忧，以及对其他游戏或系统中可能存在类似漏洞的担忧。

这个漏洞的发现凸显了游戏行业反复出现的一个问题：对安全的关注不足。发现该漏洞的研究人员对开发者对漏洞报告的无动于衷表示失望。

他们透露，在过去一年里，他们在多款大型游戏中至少发现了五个严重漏洞，其中三个因开发者反应迟缓或漠不关心而仍未修复。

许多游戏公司缺乏漏洞赏金计划，这使得问题更加严重。如果没有激励措施或明确的报告渠道，安全研究人员往往不愿负责任地披露漏洞。相反，一些人可能会制作作弊程序或机器人，这可能更有利可图，但对玩家群体有害。

研究人员表示：“对大多数游戏开发公司来说，安全研究人员很难向他们报告漏洞。除此之外，大多数公司都没有漏洞赏金计划。”

开发者必须优先验证服务器连接、限制管理员权限，并建立明确的漏洞报告渠道。像一些公司成功实施的漏洞赏金计划，在鼓励负责任的漏洞披露和提高整体游戏安全性方面能发挥很大作用。

这个漏洞的发现得益于与几位贡献者的合作，包括 AeonLucid、LukeFZ、nitro 和 sanktanglia，他们协助进行了网络加密分析。

随着在线游戏越来越受欢迎，它作为网络攻击目标的吸引力也在增加。开发者必须积极主动采取措施，确保在类似这样的漏洞被大规模利用之前，他们的游戏对玩家来说是安全的。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/unpatched-marvel-game-rce-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304032](/post/id/304032)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/unpatched-marvel-game-rce-exploit/)

如若转载,请注明出处： <https://cybersecuritynews.com/unpatched-marvel-game-rce-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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