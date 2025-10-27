---
title: Salesforce 修复了 Tableau Server 中 8 个严重漏洞：RCE、SSRF 和数据泄露
url: https://www.anquanke.com/post/id/310627
source: 安全客-有思想的安全新媒体
date: 2025-07-29
fetch_date: 2025-10-06T23:50:16.504194
---

# Salesforce 修复了 Tableau Server 中 8 个严重漏洞：RCE、SSRF 和数据泄露

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

# Salesforce 修复了 Tableau Server 中 8 个严重漏洞：RCE、SSRF 和数据泄露

阅读量**75086**

发布时间 : 2025-07-28 16:41:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/rce-ssrf-data-exposure-salesforce-patches-8-serious-flaws-in-tableau-server/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Salesforce发布了一项安全公告，解决了影响多个版本Tableau Server（广泛使用的数据可视化和商业智能平台）的8个严重漏洞。这些漏洞已在2025年6月26日的维护版本中披露并修复，涉及的漏洞包括可能导致远程代码执行（RCE）、生产数据库暴露和服务器端请求伪造（SSRF）等问题。

**CVE-2025-52446、CVE-2025-52447、CVE-2025-52448 – 通过任意SQL访问未经授权的数据库**

这三项漏洞源于Tableau的tab-doc API、set-initial-sql和validate-initial-sql功能中的不当授权控制。攻击者利用这些漏洞可以操控会话级别的设置，向生产数据库集群发送任意SQL语句。这意味着攻击者可能获得更高权限，进而窃取或修改关键数据。这些漏洞特别危险，因为它们绕过了用户与生产基础设施之间预定的隔离边界。

**CVE-2025-52449 – 通过恶意文件上传执行远程代码**

Salesforce报告指出，在Tableau的可扩展协议服务（Extensible Protocol Service）中发现了一项严重漏洞，允许不受限制的文件上传。攻击者可以通过伪装可执行文件的文件名上传恶意负载并在服务器上触发执行。系统未能验证上传文件的完整性或意图，使其容易受到远程代码执行（RCE）的攻击。

**CVE-2025-52452 – 绝对路径遍历导致敏感文件暴露**

另一个关键漏洞影响了tabdoc API中的duplicate-data-source模块。该绝对路径遍历漏洞允许攻击者构造请求绕过目录限制，从主机系统中读取任意文件。此类访问可能暴露敏感的配置文件、存储凭据或内部日志，供后续攻击使用。

**CVE-2025-52453、CVE-2025-52454、CVE-2025-52455 – 多个组件中的服务器端请求伪造（SSRF）**

这三个相关的SSRF漏洞分别出现在Flow数据源、Amazon S3连接器和EPS服务器模块中。攻击者可以构造请求，迫使Tableau Server启动未经授权的网络连接，访问内部或外部系统。通过SSRF，攻击者可以针对云元数据服务、内部管理端点或受限数据库，绕过防火墙规则，并可能进一步深入组织的基础设施。

这些漏洞影响的Tableau Server版本包括：

1. 2025.1.3之前
2. 2024.2.12之前
3. 2023.3.19之前

根据安全公告，攻击者可以利用这些漏洞，未经授权访问生产数据库、上传并执行恶意文件、通过SSRF伪造资源位置。

Salesforce敦促所有管理员更新到最新的受支持版本，以避免潜在的利用风险。

本文翻译自securityonline [原文链接](https://securityonline.info/rce-ssrf-data-exposure-salesforce-patches-8-serious-flaws-in-tableau-server/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310627](/post/id/310627)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/rce-ssrf-data-exposure-salesforce-patches-8-serious-flaws-in-tableau-server/)

如若转载,请注明出处： <https://securityonline.info/rce-ssrf-data-exposure-salesforce-patches-8-serious-flaws-in-tableau-server/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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