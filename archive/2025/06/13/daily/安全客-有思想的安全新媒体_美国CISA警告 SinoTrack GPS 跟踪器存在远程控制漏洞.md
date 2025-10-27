---
title: 美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞
url: https://www.anquanke.com/post/id/308398
source: 安全客-有思想的安全新媒体
date: 2025-06-13
fetch_date: 2025-10-06T22:51:05.008868
---

# 美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞

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

# 美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞

阅读量**1191023**

发布时间 : 2025-06-12 15:15:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<www.deepl.com/zh/translator#en/zh-hans/CISA Warns of Remote Control Flaws in SinoTrack GPS Trackers>

译文仅供参考，具体内容表达以及含义原文为准。

美国CISA报告了SinoTrack GPS设备中的关键漏洞,这些漏洞可以让攻击者远程控制车辆并跟踪位置。发现漏洞和基本步骤,以保护您的设备。

SinoTrack GPS设备的所有者应该意识到重大的安全漏洞,这些漏洞可能允许未经授权的个人远程跟踪车辆甚至切断燃料。这些漏洞影响了所有已知的SinoTrack设备和SinoTrack IOT PC平台,最近由独立研究员RaúlIgnacioCruzJiménez曝光。美国网络安全和基础设施安全局(CISA)[已就这些问题发出警报。](https://www.cisa.gov/news-events/ics-advisories/icsa-25-160-01)

### **风险是什么?**

已经确定了两个主要问题。[CVE-2025-5484](https://www.tenable.com/cve/CVE-2025-5484)第一个被标记为CVE-2025-5484的是一个弱身份验证缺陷,这意味着登录设备的管理系统太容易了。每个设备都使用其唯一标识符,该标识符作为用户名打印在接收器上。

更令人担忧的是,默认密码是众所周知的,并且对所有设备都是相同的。用户在设置设备时不会被迫更改此密码,这使得攻击者很容易猜测。攻击者可以通过物理查看设备或在线查找设备图片来查找设备标识符,例如在eBay等网站上。

第二个问题[,CVE-2025-5485](https://www.tenable.com/cve/CVE-2025-5485),是一个可观察的响应差异。这个缺陷与用户名的结构有关;它们是数字标识符,长达10位数。这使得恶意行为者可以通过简单地尝试不同的数字序列来猜测有效的用户名,通过从已知标识符中计数或向下计数,或者通过尝试随机数字来猜测有效的用户名。

如果成功,攻击者可以控制联网车辆,可能跟踪它们的行踪,甚至切断对支持的燃油泵的电源。

这些漏洞被认为是非常严重的,其中一个缺陷是CVE-2025-5485,获得8.8的CVSS v4分数。截至目前,CISA尚未收到有关这些特定漏洞在公共攻击中被积极利用的报告。

### **现在该做什么**

SinoTrack尚未回应CISA的信息请求或为这些问题提供修复。因此,强烈建议用户立即采取行动保护其设备。最关键的一步是通过管理界面将默认密码更改为强大的,独特的密码。`sinotrack.com`. .

此外,隐藏设备标识符也很重要。如果任何公开照片中都可以看到带有标识符的贴纸,建议删除或替换这些图片,以防止攻击者找到这些信息。

[CISA还建议采取一般的网络安全做法](https://hackread.com/firmware-security-identifying-risks-cybersecurity-practices/),例如小心点击可疑电子邮件中的链接,以避免进一步的风险。有关保护控制系统的更详细指导可在CISA的网站上找到。

本文翻译自hackread [原文链接](www.deepl.com/zh/translator#en/zh-hans/CISA Warns of Remote Control Flaws in SinoTrack GPS Trackers)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308398](/post/id/308398)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](www.deepl.com/zh/translator#en/zh-hans/CISA Warns of Remote Control Flaws in SinoTrack GPS Trackers)

如若转载,请注明出处： <www.deepl.com/zh/translator#en/zh-hans/CISA Warns of Remote Control Flaws in SinoTrack GPS Trackers>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)
* [漏洞预警](/tag/%E6%BC%8F%E6%B4%9E%E9%A2%84%E8%AD%A6)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53

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