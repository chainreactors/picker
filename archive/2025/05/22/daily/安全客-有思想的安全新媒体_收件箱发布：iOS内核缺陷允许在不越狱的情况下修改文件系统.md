---
title: 收件箱发布：iOS内核缺陷允许在不越狱的情况下修改文件系统
url: https://www.anquanke.com/post/id/307609
source: 安全客-有思想的安全新媒体
date: 2025-05-22
fetch_date: 2025-10-06T22:26:50.065385
---

# 收件箱发布：iOS内核缺陷允许在不越狱的情况下修改文件系统

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

# 收件箱发布：iOS内核缺陷允许在不越狱的情况下修改文件系统

阅读量**62146**

发布时间 : 2025-05-21 15:30:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/poc-released-ios-kernel-flaw-allows-file-system-modification/>

译文仅供参考，具体内容表达以及含义原文为准。

![iOS 内核漏洞 dirtyZero 漏洞利用]()

修补的内核漏洞CVE-2025-24203引起了安全社区以及苹果生态系统中越狱社区的极大关注。在野外称为“dirtyZero”或“mdc0”,此漏洞允许应用程序修改文件系统的保护区域,从而实现一波系统自定义,而无需越狱。

由着名的Google Project Zero研究员Ian Beer披露,该漏洞对iOS和iPadOS版本16.0-16.7.10,17.0-17.7.5和18.0-18.3.2产生了严重影响。

*“应用程序可以修改文件系统的受保护部分。这个问题通过改进检查来解决*,“苹果在iPadOS 17.7.6的安全内容中写道。

该漏洞利用了VM\_BEHAVIOR\_ZERO\_WIRED\_PAGES的行为,这是苹果内存管理系统中很少经过审查的标志。正如 Beer *所解释的:“vm\_behavior VM\_BEHAVIOR\_ZERO\_WIRED\_PAGES 可以由其地图中任何 vm\_entry 上的任务设置;没有权限检查。它导致 entry->zero\_wired\_pages 标志被设置。*

这有效地允许恶意应用程序将内存支持系统文件的页面归零 – 这是攻击者或系统调整器的强大工具。

啤酒技术文章的关键细节:

* 1-许可检查在多个阶段丢失。
* 2-页面可以“归零”,即使它们来自根拥有的,只读的文件。
* 3-利用 mlock(()(用户可访问的 syscall) 绕过对 root 或主机权限的需求。
* 4-漏洞可以针对从 vnode 寻呼机文件映射的内存区域,即 UBC(统一缓冲区缓存)页面。

啤酒在以下网站上测试了概念验证(PoC):

* 1-macOS 15.2 (24C101)
* 2-MacBook Pro 13英寸2019(英特尔)

Apple [已经修补了此漏洞:](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)

* 1-iPadOS/iOS 17.7.6
* 2-iPadOS/iOS 18.4

在这些版本下方运行固件的用户容易受到攻击。

跟随MacDirtyCow的脚步,这个漏洞已经使开发人员能够创建自定义工具 – 调整系统行为,更改UI元素等的应用程序 – 所有这些都需要一个完整的越狱。

虽然该漏洞被爱好者使用,但访问的便利性和缺乏权限检查也为嵌入到流氓应用程序中的潜在恶意滥用打开了大门。

本文翻译自securityonline [原文链接](https://securityonline.info/poc-released-ios-kernel-flaw-allows-file-system-modification/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307609](/post/id/307609)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/poc-released-ios-kernel-flaw-allows-file-system-modification/)

如若转载,请注明出处： <https://securityonline.info/poc-released-ios-kernel-flaw-allows-file-system-modification/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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