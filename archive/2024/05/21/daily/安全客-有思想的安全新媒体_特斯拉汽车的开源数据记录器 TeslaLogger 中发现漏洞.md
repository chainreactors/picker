---
title: 特斯拉汽车的开源数据记录器 TeslaLogger 中发现漏洞
url: https://www.anquanke.com/post/id/296623
source: 安全客-有思想的安全新媒体
date: 2024-05-21
fetch_date: 2025-10-06T16:49:04.999279
---

# 特斯拉汽车的开源数据记录器 TeslaLogger 中发现漏洞

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

# 特斯拉汽车的开源数据记录器 TeslaLogger 中发现漏洞

阅读量**99493**

发布时间 : 2024-05-20 11:37:50

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/30-tesla-cars-hacked/>

译文仅供参考，具体内容表达以及含义原文为准。

一名安全研究人员发现 TeslaLogger（用于从 Tesla 车辆收集数据的第三方软件）中存在一个漏洞，该漏洞利用不安全的默认设置，可被利用来获得对 TeslaLogger 实例的未经授权的访问。

向 TeslaLogger 维护人员报告了该问题，后者采取了措施来降低风险，因为需要注意的是，该漏洞并不存在于 Tesla 车辆或 Tesla 基础设施中。

在搜索有趣的汽车项目时，特斯拉汽车的开源数据记录器 TeslaLogger 中发现了漏洞。

使用 Docker 将其安装到笔记本电脑上后，研究人员使用 nmap 来识别 MariaDB 数据库（端口 3306）、Graphana 可视化工具（端口 3000）和管理面板（端口 8888）中正在运行的服务。

![]()
Nmap结果
出于对 MariaDB 和 Graphana 的兴趣，他利用 DBweaver 使用项目存储库中找到的默认凭据连接到数据库，并希望提取 Tesla 汽车 API 密钥，执行 SQL 查询以检索“cars”表中的所有数据。

利用 Tesla API 的 Tesla 集成中存在漏洞，因为受损的 Tesla 令牌（包括访问令牌和刷新令牌）使攻击者能够完全远程控制汽车。

![]()

数据库
虽然 Tesla 的 API 采用基于角色的访问控制 (RBAC)，但 Tesla 记录器应用程序经常请求过多的权限，从而允许攻击者利用 API 密钥来操纵汽车的状态（例如，添加驾驶员、解锁车门、控制气候）。

即使数据库未公开，此问题仍然存在，因为存在获取 API 密钥的替代方法。 Raspberry Pi 设备上的某些 Tesla 记录器实现会因疏忽而暴露 API 密钥而进一步加剧问题。

![]()

需要权限才能正常运行
Harish SG发现了一个具有默认凭据的易受攻击的 Grafana 仪表板，允许访问Tesla API 令牌。 TeslaLogger 是用于 Tesla 数据记录的第三方软件，由于以纯文本形式存储凭据且默认配置不安全，因此存在漏洞。

通过利用这些漏洞，识别出超过 30 个易受远程攻击的 TeslaLogger 实例，可能授予 Tesla 车辆的控制权，并在发现 TeslaLogger 开发人员的联系信息后，负责任地将调查结果报告给 TeslaLogger 开发人员。

![]()

公共互联网普查系统
披露了 TeslaLogger（特斯拉汽车的第三方软件）中的一个漏洞，如果攻击者破坏了 TeslaLogger 数据库，则可能允许攻击者窃取 Tesla API 凭证。

![]()

发现
他与 TeslaLogger 维护人员合作解决了该问题，其中涉及对数据库中的 API 凭证进行加密并向管理窗格添加身份验证，因为他没有直接向 Tesla 报告该问题，因为他们过去从 Tesla 收到了无益的回复关于另一个第三方软件的类似问题。

本文翻译自 [原文链接](https://cybersecuritynews.com/30-tesla-cars-hacked/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296623](/post/id/296623)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/30-tesla-cars-hacked/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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