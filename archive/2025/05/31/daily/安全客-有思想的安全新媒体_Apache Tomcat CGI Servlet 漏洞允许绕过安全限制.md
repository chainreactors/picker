---
title: Apache Tomcat CGI Servlet 漏洞允许绕过安全限制
url: https://www.anquanke.com/post/id/308023
source: 安全客-有思想的安全新媒体
date: 2025-05-31
fetch_date: 2025-10-06T22:24:41.481748
---

# Apache Tomcat CGI Servlet 漏洞允许绕过安全限制

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

# Apache Tomcat CGI Servlet 漏洞允许绕过安全限制

阅读量**167302**

发布时间 : 2025-05-30 17:44:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/apache-tomcat-cgi-servlet-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Apache Tomcat 的 CGI servlet 实现中发现了一个新的安全漏洞,该漏洞可能允许攻击者在特定条件下绕过配置的安全约束。

该漏洞名为CVE-2025-46701,于2025年5月29日披露,并影响流行的Java应用程序服务器的多个版本。

该漏洞源于Apache Tomcat的CGI servlet中对案例敏感度的不当处理,特别是影响映射到CGI servlet的URL的pathInfo组件。

当 Tomcat 对为 pathInfo 组件配置安全约束的大小写不敏感文件系统运行时,特制的 URL 可以规避这些保护措施。

安全研究人员将这种漏洞归类为低严重程度,尽管它代表了依赖基于CGI的应用程序并具有严格访问控制的组织的重大问题。

该漏洞特别影响启用 CGI 支持的环境,Tomcat 安装中默认禁用该环境。

### **Apache Tomcat CGI Servlet 漏洞**

该漏洞影响了三个主要版本分支中广泛的Apache Tomcat版本。受影响的版本包括Apache Tomcat 11.0.0-M1至11.0.6,101.0-M1至10.1.40和9.0.0-M1至9.0.104。

这种广泛的范围意味着许多生产环境可能容易受到攻击,特别是那些支持CGI支持旧应用程序或特定开发工作流的生产环境。

Apache软件基金会强调,此漏洞仅影响明确启用CGI支持的系统,因为该功能在所有Tomcat版本中默认保持禁用。

使用 Tomcat 主要用于没有 CGI 功能的标准 Web 应用程序托管的组织不会暴露在此特定攻击向量。

Apache软件基金会发布了补丁版本,解决了所有受影响分支机构的此漏洞。组织应升级到 Apache Tomcat 11.0.7、10.1.41 或 9.0.105,具体取决于其当前部署。

这些更新的版本包括 CGI servlet 实现中适当的案例敏感处理。

安全研究员Greg K负责任地披露了该漏洞,他的GitHub个人资料显示了安全研究方面的专业知识。这一发现强调了对广泛部署的软件组件进行持续安全评估的重要性,即使对于生产环境中可能不常用的功能也是如此。

系统管理员应立即评估其 Tomcat 部署,以确定是否启用了 CGI 支持,以及是否将安全约束应用于 pathInfo 组件。

使用CGI功能的组织应优先升级到修补版本,而那些不需要CGI支持的组织应确保它作为额外的安全措施保持禁用。

定期进行安全审计和保持供应商安全咨询状态仍然是在企业环境中维护安全 Apache Tomcat 部署的关键做法。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/apache-tomcat-cgi-servlet-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308023](/post/id/308023)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/apache-tomcat-cgi-servlet-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/apache-tomcat-cgi-servlet-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**4赞

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [无文件 AsyncRAT 活动利用隐蔽的 PowerShell 有效载荷攻击德国用户](/post/id/308562)

  2025-06-18 15:22:31
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52

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