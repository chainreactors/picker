---
title: Fortra 修复了 FileCatalyst Workflow 中的两个严重漏洞
url: https://www.anquanke.com/post/id/299704
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:24:02.472356
---

# Fortra 修复了 FileCatalyst Workflow 中的两个严重漏洞

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

# Fortra 修复了 FileCatalyst Workflow 中的两个严重漏洞

阅读量**76388**

发布时间 : 2024-09-02 16:49:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源： securityaffairs

原文地址：<https://securityaffairs.com/167838/security/fortra-filecatalyst-critical-workflow.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 网络安全和自动化公司 Fortra 解决了 FileCatalyst Workflow 软件中的两个漏洞，包括一个严重性漏洞。

网络安全和自动化公司 Fortra 发布了针对 FileCatalyst Workflow 中两个漏洞的补丁。漏洞之一是一个关键问题，跟踪为 CVE-2024-6633（CVSS 评分为 9.8），在 FileCatalyst 工作流程设置中被描述为不安全的默认。

该漏洞影响 FileCatalyst Workflow 5.1.6 Build 139 及更早版本。

对 FileCatalyst Workflow 的攻击需要特定条件：该软件必须配置捆绑的 HSQL 数据库（违背建议），攻击者可以访问，攻击者已经在公司网络内部并执行端口扫描，或者将其 HSQLDB 端口暴露给 Internet。

此漏洞允许未经身份验证的攻击者获得对数据库的远程访问，从而可能操纵或泄露数据并创建管理员用户，尽管他们的访问权限仍处于沙盒中。

问题的根本原因是供应商在知识库文章中披露的设置 HSQL 数据库 （HSQLDB） 的默认凭据。

该公司解释说，已弃用的 HSQLDB 包含在 FileCatalyst Workflow 中，其唯一目的是简化安装。但是，如果未配置替代数据库，则使用 HSQLDB 可能会将 FileCatalyst Workflow 实例暴露给黑客。

*“该攻击授予未经身份验证的攻击者对数据库的远程访问权限，包括从数据库操作/泄露数据以及创建管理员用户，尽管他们的访问权限级别仍处于沙盒中。”公告中写道。*

该公司解决的第二个缺陷是被跟踪为 CVE-2024-6632 的高严重性 SQL 注入问题。对 FileCatalyst Workflow 的攻击需要超级管理员凭据才能访问带有易受攻击字段（电话号码）的 UI 屏幕。但是，由于只有一个超级管理员，如果攻击者泄露了这些凭据，他们将不需要 SQL 注入，因为他们已经拥有更危险的权限。

*“FileCatalyst Workflow 中存在一个漏洞，超级管理员可访问的字段可用于执行 SQL 注入攻击，这可能导致机密性、完整性和可用性的损失，”公告中写道。*

Fortra 建议客户更新到 FileCatalyst Workflow 版本 5.1.7 build 156 或更高版本。

目前尚不清楚这些漏洞是否在野外被积极利用。

本文翻译自 securityaffairs [原文链接](https://securityaffairs.com/167838/security/fortra-filecatalyst-critical-workflow.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299704](/post/id/299704)

安全KER - 有思想的安全新媒体

本文转载自:  [securityaffairs](https://securityaffairs.com/167838/security/fortra-filecatalyst-critical-workflow.html)

如若转载,请注明出处： <https://securityaffairs.com/167838/security/fortra-filecatalyst-critical-workflow.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [网络安全和自动化公司 Fortra 解决了 FileCatalyst Workflow 软件中的两个漏洞，包括一个严重性漏洞。](#h2-0)

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