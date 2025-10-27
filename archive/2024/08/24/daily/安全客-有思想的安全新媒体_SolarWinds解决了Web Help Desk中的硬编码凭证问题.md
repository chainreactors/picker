---
title: SolarWinds解决了Web Help Desk中的硬编码凭证问题
url: https://www.anquanke.com/post/id/299429
source: 安全客-有思想的安全新媒体
date: 2024-08-24
fetch_date: 2025-10-06T18:01:07.654037
---

# SolarWinds解决了Web Help Desk中的硬编码凭证问题

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

# SolarWinds解决了Web Help Desk中的硬编码凭证问题

阅读量**38830**

发布时间 : 2024-08-23 11:20:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167408/hacking/solarwinds-hardcoded-credential-flaw-web-help-desk.html>

译文仅供参考，具体内容表达以及含义原文为准。

## SolarWinds 在其 Web Help Desk （WHD） 软件中修复了一个硬编码凭据缺陷，该漏洞可能允许攻击者未经授权访问易受攻击的实例。

SolarWinds 解决了其 Web Help Desk （WHD） 软件中的一个新安全漏洞，该漏洞被跟踪为 CVE-2024-28987（CVSS 评分为 9.1），该漏洞可能允许未经身份验证的远程攻击者未经授权访问易受攻击的实例。

SolarWinds 将 WHD 描述为一种经济实惠的帮助台票务和资产管理软件，被大型企业和政府组织广泛使用。

*“SolarWinds Web Help Desk （WHD） 软件受到硬编码凭据漏洞的影响，允许未经身份验证的远程用户访问内部功能并修改数据。”*

此问题会影响 WHD 12.8.3 HF1 和所有先前版本，已在版本 12.8.3 HF2 中得到解决。

该漏洞是由 Horizon3.ai 的安全研究员 Zach Hanley 发现的。

上周，美国网络安全和基础设施安全局 （CISA） 在其已知利用漏洞 （KEV） 目录中添加了另一个 SolarWinds Web Help Desk 对不受信任数据漏洞的反序列化，该漏洞被跟踪为 CVE-2024-28986（CVSS 评分为 9.8）。

该漏洞是一个 Java 反序列化问题，攻击者可利用该问题在易受攻击的主机上运行命令，从而导致远程代码执行。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167408/hacking/solarwinds-hardcoded-credential-flaw-web-help-desk.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299429](/post/id/299429)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167408/hacking/solarwinds-hardcoded-credential-flaw-web-help-desk.html)

如若转载,请注明出处： <https://securityaffairs.com/167408/hacking/solarwinds-hardcoded-credential-flaw-web-help-desk.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [SolarWinds 在其 Web Help Desk （WHD） 软件中修复了一个硬编码凭据缺陷，该漏洞可能允许攻击者未经授权访问易受攻击的实例。](#h2-0)

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