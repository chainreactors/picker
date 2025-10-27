---
title: CISA警告PHPMailer命令注入漏洞已在攻击中被利用
url: https://www.anquanke.com/post/id/309710
source: 安全客-有思想的安全新媒体
date: 2025-07-11
fetch_date: 2025-10-06T23:16:34.009452
---

# CISA警告PHPMailer命令注入漏洞已在攻击中被利用

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

# CISA警告PHPMailer命令注入漏洞已在攻击中被利用

阅读量**62260**

发布时间 : 2025-07-10 16:19:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源： cybersecuritynews

原文地址：<https://cybersecuritynews.com/phpmailer-command-injection-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

关键要点：

1. PHPMailer中的CVE-2016-10033漏洞允许攻击者通过mail()函数中的命令注入执行任意代码。
2. 该漏洞已在实时网络攻击中被利用，存在系统被入侵和数据泄露的风险。
3. 根据CISA在7月7日发布的警告，组织必须在2025年7月28日前修复此漏洞。
4. 请升级到PHPMailer v5.2.18及以上版本，或立即停止使用受影响的版本。

CISA发布紧急警告，指出PHPMailer中存在一个严重的命令注入漏洞，该漏洞正被网络攻击者积极利用。

该漏洞被追踪为CVE-2016-10033，对全球依赖该流行PHP电子邮件库的Web应用程序构成重大风险。

CISA已将此漏洞添加至其已知被利用漏洞（KEV）目录，并要求各组织在2025年7月28日前实施修复措施。

**PHPMailer命令注入漏洞**

PHPMailer命令注入漏洞源于该库核心功能中的输入验证不足。

具体而言，该漏洞影响class.phpmailer.php脚本中的mail()函数，用户提供的输入在处理之前未经过适当的验证。

这一安全弱点允许攻击者注入恶意命令，在应用程序的上下文中执行，从而可能导致系统完全被攻破。

该漏洞被归类为CWE-77（命令中使用的特殊元素未正确中和）和CWE-88（命令中参数分隔符未正确中和），突出显示了根本的输入验证失败，正是这些失败使得攻击得以发生。

当攻击未能成功时，可能导致拒绝服务（DoS）状态，干扰正常的应用程序操作。

该漏洞的技术性质使其特别危险，因为PHPMailer被广泛集成到内容管理系统、Web应用程序和企业软件解决方案中。

网络犯罪分子正在利用这一漏洞在易受攻击的系统上执行任意代码，尽管目前攻击活动的具体细节仍在调查中。

命令注入发生在恶意输入绕过库的安全控制后，允许攻击者在主机服务器上运行未经授权的命令。

尽管CISA尚未确认此漏洞是否被用于勒索软件攻击，但鉴于PHPMailer的广泛部署，潜在的此类利用仍然是一个重要关注点。

该漏洞的利用可能导致数据泄露、未经授权访问敏感信息和完全接管服务器。

使用受影响版本的组织面临直接风险，特别是那些具有面向互联网的应用程序并通过电子邮件功能处理用户输入的组织。

**缓解策略**

CISA强烈建议组织立即应用厂商提供的缓解措施和安全补丁。

对于云服务部署，管理员应遵循BOD 22-01指南，以确保全面的保护。

对于无法立即实施可用缓解措施的组织，建议在部署适当的安全措施之前，考虑停止使用受影响的PHPMailer版本。

该漏洞影响PHPMailer v5.2.18之前的版本，组织应立即升级到最新的安全版本。

安全团队应在修补计划中优先处理此漏洞，并对所有使用PHPMailer功能的应用程序进行彻底评估，确保在整个基础设施中彻底修复。

本文翻译自 cybersecuritynews [原文链接](https://cybersecuritynews.com/phpmailer-command-injection-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309710](/post/id/309710)

安全KER - 有思想的安全新媒体

本文转载自:  [cybersecuritynews](https://cybersecuritynews.com/phpmailer-command-injection-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/phpmailer-command-injection-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**5赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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