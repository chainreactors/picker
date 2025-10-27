---
title: 新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序
url: https://www.anquanke.com/post/id/304015
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:57.630121
---

# 新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序

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

# 新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序

阅读量**296476**

发布时间 : 2025-02-10 10:31:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/malicious-cisco-anyconnect-ads-target-users-with-netsupport-rat/>

译文仅供参考，具体内容表达以及含义原文为准。

![LDAPNightmare]()

一种新的恶意广告活动正在传播一款伪造的思科 AnyConnect 安装程序，该程序会植入 NetSupport RAT 木马。

Malwarebytes 的研究人员发现了一场恶意广告活动，该活动利用谷歌广告来分发一款伪造的思科 AnyConnect 安装程序。这款安装程序使用有效的证书进行数字签名，会植入 NetSupport RAT 远程访问木马，使攻击者能够控制受害者的计算机。

报告称：“这起特殊案例是一则针对思科 AnyConnect 的恶意谷歌广告，思科 AnyConnect 是一款工具，常被员工用于远程连接公司网络，大学也会使用。”

攻击者采用了一种巧妙的技术来躲避安全系统的检测。他们克隆了一所使用思科 AnyConnect 的德国大学的网站，并将其用作 “白页” 来欺骗广告检测系统。

“如果（广告）明显很假很差，就会引起怀疑。我们认为在这个案例中，作案者从一所确实使用思科 AnyConnect 的大学窃取内容，这个主意相当巧妙。”

真正的受害者会被重定向到一个伪造的思科 AnyConnect 下载页面，该页面与合法网站极为相似。此页面上的下载链接指向一个托管在被入侵 WordPress 网站上的恶意安装程序。

![Cisco AnyConnect Ads]()

来源：Malwarebytes

一旦安装程序被执行，它会解压并运行一个名为 client32.exe 的恶意可执行文件，这是 NetSupport RAT 的一个变种。该木马使攻击者能够远程控制受害者的计算机、窃取数据并安装更多恶意软件。

攻击者使用两个 IP 地址来控制 NetSupport RAT，分别是 91.222.173 [.] 67 和 199.188.200 [.] 195。

这场活动提醒我们，即使像谷歌广告这样值得信赖的来源也可能被用于传播恶意软件。用户在点击广告时应保持谨慎，即便它们看起来是合法的。及时更新软件并使用可靠的安全解决方案来防范恶意软件也至关重要。

本文翻译自securityonline [原文链接](https://securityonline.info/malicious-cisco-anyconnect-ads-target-users-with-netsupport-rat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304015](/post/id/304015)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/malicious-cisco-anyconnect-ads-target-users-with-netsupport-rat/)

如若转载,请注明出处： <https://securityonline.info/malicious-cisco-anyconnect-ads-target-users-with-netsupport-rat/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**7赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [新 Eleven11bot 黑客攻击 86,000 台 IP 摄像机，发动大规模 DDoS 攻击](/post/id/308201)

  2025-06-06 15:33:29
* ##### [黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵](/post/id/307477)

  2025-05-16 18:05:26
* ##### [虚假CAPTCHA投递Lumma Stealer窃密木马](/post/id/306195)

  2025-04-03 15:14:44
* ##### [Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测](/post/id/304018)

  2025-02-10 10:47:45
* ##### [ASP.NET漏洞让黑客劫持服务器并注入恶意代码](/post/id/303978)

  2025-02-08 14:42:13
* ##### [“SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载](/post/id/303878)

  2025-02-06 11:12:51
* ##### [400,000+ 系统受感染：DigitalPulse 代理软件带着新技巧回归](/post/id/303738)

  2025-01-23 09:38:26

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