---
title: Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞
url: https://www.anquanke.com/post/id/314719
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:46.632536
---

# Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞

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

# Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞

阅读量**22974**

发布时间 : 2026-02-04 11:24:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/identity-at-risk-apache-syncope-patches-critical-login-xss-xxe-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

阿帕奇软件基金会针对旗下开源数字身份管理核心系统**Apache Syncope**，发布了重要安全更新。此次补丁修复了两类不同的漏洞，这两类漏洞均可被攻击者利用，实现劫持用户会话或泄露服务器敏感数据的恶意操作。

其中危害更为严重的漏洞编号为**CVE-2026-23794**，这是一个存在于终端用户登录页面的**反射型跨站脚本（XSS）漏洞**，危险等级被评定为 “重要”。而登录页面恰恰是用户进入身份管理系统的第一道入口。

安全公告指出，该漏洞是一个典型的攻击陷阱：**“攻击者诱骗合法用户点击特制链接后，即可在该用户的浏览器中执行任意 JavaScript 代码”**。

一旦攻击成功，黑客就能窃取用户的会话 Cookie、将用户重定向至恶意网站，或是在用户不知情的情况下以其名义执行各类操作。由于漏洞直接影响登录页面，它会在用户身份认证的关键环节，对用户会话的安全性构成重大威胁。

另一项漏洞编号为**CVE-2026-23795**，危险等级为 “中等”，但针对特权用户的攻击场景十分危险。这是一个存在于控制台组件内、具体位于密钥管理器参数模块的**XML 外部实体注入（XXE）漏洞**。

该漏洞的利用门槛相对更高：攻击者必须是 “拥有足够权限，能够创建或编辑密钥管理器参数的管理员”**。**

**但如果是恶意管理员，或是管理员账户已遭攻击者攻陷，此人就可以**“构造恶意 XML 文本发起 XXE 攻击，进而造成敏感数据泄露”。借助这种方式，攻击者可强制服务器泄露内部文件，或是与本不应访问的外部系统建立交互。

项目维护团队敦促所有用户，立即将自身的 Apache Syncope 部署版本升级至最新的安全版本：

* 对于 3.0.x 分支：升级至 3.0.16 版本
* 对于 4.0.x 分支：升级至 4.0.4 版本

此次更新会对 `syncope-client-idrepo-common-ui` 和 `syncope-client-idrepo-console` 两个组件进行补丁修复，能够彻底消除登录页面 XSS 攻击陷阱与 XXE 数据泄露这两类风险。

本文翻译自securityonline [原文链接](https://securityonline.info/identity-at-risk-apache-syncope-patches-critical-login-xss-xxe-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314719](/post/id/314719)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/identity-at-risk-apache-syncope-patches-critical-login-xss-xxe-flaws/)

如若转载,请注明出处： <https://securityonline.info/identity-at-risk-apache-syncope-patches-critical-login-xss-xxe-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [Notepad++被劫持国家级攻击者投毒更新包，持续数月作恶](/post/id/314722)

  2026-02-04 11:24:22
* ##### [Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序](/post/id/314725)

  2026-02-04 11:23:54
* ##### [WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞](/post/id/314716)

  2026-02-04 11:23:22

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