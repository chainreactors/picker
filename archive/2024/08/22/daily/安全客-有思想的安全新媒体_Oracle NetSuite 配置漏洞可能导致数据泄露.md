---
title: Oracle NetSuite 配置漏洞可能导致数据泄露
url: https://www.anquanke.com/post/id/299357
source: 安全客-有思想的安全新媒体
date: 2024-08-22
fetch_date: 2025-10-06T18:01:24.755247
---

# Oracle NetSuite 配置漏洞可能导致数据泄露

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

# Oracle NetSuite 配置漏洞可能导致数据泄露

阅读量**65843**

发布时间 : 2024-08-21 14:09:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167287/hacking/oracle-netsuite-misconfiguration.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 研究人员发现，数以千计的Oracle NetSuite电子商店容易受到数据泄露的影响，敏感的客户信息也面临风险。

AppOmni 的网络安全研究人员警告说，Oracle NetSuite SuiteCommerce 平台中存在潜在问题，可能允许攻击者访问客户敏感数据。

NetSuite 是一个广泛使用的 SaaS 企业资源规划 （ERP） 平台，因其通过 SuiteCommerce 或 SiteBuilder 部署面向外部的在线商店的能力而受到重视。这些商店托管在 NetSuite 租户的子域上，使未经身份验证的客户能够直接从企业浏览、注册和购买产品。

问题不是 NetSuite 解决方案中的漏洞，而是自定义记录类型 （CRT） 上的访问控制配置错误，可能会泄露客户敏感信息。

暴露的敏感数据是注册客户的个人身份信息，包括完整地址和手机号码。

威胁参与者以 NetSuite 中的自定义记录类型 （CRT） 为目标，这些类型使用“无需权限”访问控制，允许未经身份验证的用户通过 NetSuite 的记录和搜索 API 访问数据。但是，要使攻击成功，攻击者必须首先知道正在使用的 CRT 的名称。

*“我们还必须假设未经身份验证的参与者知道 CRT 的名称。在本文发表之前，存在一种可以调用的方法，该方法将返回所有 CRT 的名称。然而，这已经得到了修复，“研究人员发表的[报告](https://appomni.com/blog/oracle-netsuite-data-exposure-analysis/)中写道。“今天，可以使用两种方法检索 CRT 名称。*

* *暴力破解下面第一步中所示的 API 端点，使用由流行的 CRT 名称组成的单词列表，该单词列表已使用 Github 等公共资源进行整理。*
* *通过在与站点交互期间观察 HTTP 流量，在响应中查找以“customrecord\_”为前缀的字符串。*

为了降低风险，管理员应加强对自定义记录类型 （CRT） 的访问控制，限制公众对敏感字段的访问，并考虑暂时使受影响的站点脱机以防止数据泄露。

*“解决这些数据暴露问题的可靠方法是加强对 CRT 的访问控制。从安全角度来看，最简单的解决方案可能涉及将记录类型定义的访问类型更改为’**需要自定义记录条目权限**‘或’**使用权限列表**‘。实际上，许多组织都有真正的业务需求，要求公开记录类型中的某些字段。因此，我强烈建议管理员开始评估字段级别的访问控制，并确定需要公开哪些字段（如果有）。对于必须从公共访问中锁定的字段，管理员必须进行以下两项更改：*

* **默认访问级别**：无
* **搜索/报告的默认级别**：无

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167287/hacking/oracle-netsuite-misconfiguration.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299357](/post/id/299357)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167287/hacking/oracle-netsuite-misconfiguration.html)

如若转载,请注明出处： <https://securityaffairs.com/167287/hacking/oracle-netsuite-misconfiguration.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [研究人员发现，数以千计的Oracle NetSuite电子商店容易受到数据泄露的影响，敏感的客户信息也面临风险。](#h2-0)

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