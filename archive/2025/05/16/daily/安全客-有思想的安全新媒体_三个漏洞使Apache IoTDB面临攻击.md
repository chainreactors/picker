---
title: 三个漏洞使Apache IoTDB面临攻击
url: https://www.anquanke.com/post/id/307406
source: 安全客-有思想的安全新媒体
date: 2025-05-16
fetch_date: 2025-10-06T22:23:25.174080
---

# 三个漏洞使Apache IoTDB面临攻击

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

# 三个漏洞使Apache IoTDB面临攻击

阅读量**145629**

发布时间 : 2025-05-15 16:25:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 多斯，文章来源：securityonline

原文地址：<https://securityonline.info/three-vulnerabilities-expose-apache-iotdb-to-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Apache IoTDB,安全漏洞]()

Apache IoTDB是一个设计用于管理工业物联网时间序列数据的系统,它面临着一系列安全漏洞,这些漏洞可能会暴露敏感信息并允许远程执行代码。

CVE-2025-26864和CVE-2025-26795强调风险:敏感信息的暴露。该漏洞位于Apache IoTDB及其JDBB驱动程序的OpenID身份验证机制中。此漏洞可能允许未经授权访问敏感数据并将此类数据插入日志文件。

受影响的Apache IoTDB版本包括0.10.0至1.3.3和2.0.1-beta之前2.0.2。同样,Apache IoTDB JDB 驱动程序版本 0.10.0 到 1.3.3 和 2.0.1-beta 之前也容易受到攻击。

CVE-2024-24780 对远程执行代码构成重大威胁。[vulnerability](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)由于 Apache IoTDB 处理用户定义函数 (UDF) 中不受信任的 URI 的方式,此漏洞存在。具有创建 UDF 权限的攻击者可以从不受信任的源注册恶意功能,从而导致远程代码执行。

[此漏洞在](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/) 1.3.4 之前影响 Apache IoTDB 版本 1.0.0。

强烈建议Apache IoTDB的用户立即采取行动来减轻这些风险。升级到 [1.3.4](https://iotdb.apache.org/Download/) 和 [2.0.2](https://iotdb.apache.org/Download/) 版本至关重要,[vulnerabilities](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/)因为这些版本包含针对已识别漏洞的修复。通过应用这些更新,组织可以保护其物联网数据和系统免受潜在攻击。

本文翻译自securityonline [原文链接](https://securityonline.info/three-vulnerabilities-expose-apache-iotdb-to-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307406](/post/id/307406)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/three-vulnerabilities-expose-apache-iotdb-to-attacks/)

如若转载,请注明出处： <https://securityonline.info/three-vulnerabilities-expose-apache-iotdb-to-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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