---
title: WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞
url: https://www.anquanke.com/post/id/314716
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:53.229597
---

# WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞

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

# WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞

阅读量**19432**

发布时间 : 2026-02-04 11:23:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/wifi-hijack-hikvision-patches-command-injection-in-ds-3wap-access-points/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

尽管该漏洞的利用前提是攻击者需完成身份验证，但安全专家警示，这并不意味着风险有所降低。在诸多攻击场景中，该漏洞可能成为攻击链上的关键一环：攻击者先攻陷低权限账户（或使用默认凭据登录），再借助这一漏洞获得对设备底层操作系统的完全控制权。

安全公告指出，该漏洞可直接导致**任意命令执行**。一旦攻击者在无线接入点这类网络设备上实现代码执行，就有可能拦截网络流量、横向渗透至内网中的其他设备，或是直接瘫痪整个无线服务。

该安全漏洞影响海康威视**DS-3WAP 系列**多款无线接入点，具体来看，运行以下型号且固件版本为 **V1.1.6303 build250812 及更早版本**的设备均存在风险：

* DS-3WAP521-SI
* DS-3WAP522-SI
* DS-3WAP621E-SI
* DS-3WAP622E-SI
* DS-3WAP623E-SI

海康威视已发布适用于所有受影响型号的统一修复版本，网络管理员需立即将设备固件更新至**V1.1.6601 build251223 版本**，以封堵这一攻击入口。

本文翻译自securityonline [原文链接](https://securityonline.info/wifi-hijack-hikvision-patches-command-injection-in-ds-3wap-access-points/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314716](/post/id/314716)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/wifi-hijack-hikvision-patches-command-injection-in-ds-3wap-access-points/)

如若转载,请注明出处： <https://securityonline.info/wifi-hijack-hikvision-patches-command-injection-in-ds-3wap-access-points/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1000**

* 粉丝
* **6**

### TA的文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58

### 相关文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58
* ##### [Notepad++被劫持国家级攻击者投毒更新包，持续数月作恶](/post/id/314722)

  2026-02-04 11:24:22
* ##### [Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序](/post/id/314725)

  2026-02-04 11:23:54

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