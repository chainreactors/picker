---
title: Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞
url: https://www.anquanke.com/post/id/308359
source: 安全客-有思想的安全新媒体
date: 2025-06-12
fetch_date: 2025-10-06T22:47:56.375847
---

# Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞

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

# Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞

阅读量**179003**

发布时间 : 2025-06-11 16:37:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/06/adobe-releases-patch-fixing-254.html>

译文仅供参考，具体内容表达以及含义原文为准。

[Adobe周二推送了安全更新](https://helpx.adobe.com/security.html),以解决影响其软件产品的254个安全漏洞,其中大部分影响了Experience Manager(AEM)。

在254个缺陷中,225个位于AEM,影响AEM云服务(CS)以及之前的所有版本,包括6.5.22。问题已在 AEM Cloud Service Release 2025.5 和 6.5.23 版本中得到解决。

“成功利用这些漏洞可能导致任意执行代码,权限升级和安全功能绕过[,”Adobe在一份咨询中说。](https://helpx.adobe.com/security/products/experience-manager/apsb25-48.html)

几乎所有225个漏洞都被归类为跨站点脚本(XSS)漏洞,特别是存储的XSS和基于DOM的XSS的混合,可以利用这些漏洞来实现任意代码执行。

Adobe认为安全研究人员Jim Green(绿色干扰),Akshay Sharma(匿名\_blackzero)和lpi发现并报告了XSS漏洞。

作为本月更新的一部分,该公司修补的最严重的缺陷涉及Adobe Commerce和Magento Open Source中的代码执行漏洞。

关键级别的漏洞CVE-2025-47110(CVSS评分:9.1)是一个反映的XSS漏洞,可能导致任意代码执行。还解决了不当授权缺陷(CVE-2025-43585,CVSS评分:8.2),可能导致安全功能绕过。

以下版本受到影响 –

* ①Adobe Commerce (2.4.8, 2.4.7-p5 及更早版本, 2.4.6-p10 及更早版本, 2.4.5-p12 及更早版本,2.4.4-p13 及更早版本)
* ②Adobe Commerce B2B(1.5.2及更早,1.4.2-p5及更早,1.3.5-p10及更早,1.3.4-p12及更早版本,1.3.3-p13及更早)
* ③Magento开源(2.4.8,2.4.7-p5及更早,2.4.6-p10及更早,2.4.5-p12及更早)

在剩余的更新中,有四个涉及Adobe InCopy(CVE-2025-30327,CVE-2025-47107,CVSS评分:7.8)和Substance 3D Sampler(CVE-2025-43581,CVE-2025-43588,CVSS评分:7.8)中的代码执行缺陷。

虽然没有一个错误被列为在野外公开或被利用,但建议用户将其实例更新到最新版本,以防止潜在威胁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/06/adobe-releases-patch-fixing-254.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308359](/post/id/308359)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/06/adobe-releases-patch-fixing-254.html)

如若转载,请注明出处： <https://thehackernews.com/2025/06/adobe-releases-patch-fixing-254.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [安全漏洞](/tag/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E)
* [技术分析](/tag/%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**5赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38

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