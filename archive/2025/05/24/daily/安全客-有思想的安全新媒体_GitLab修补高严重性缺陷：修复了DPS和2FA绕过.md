---
title: GitLab修补高严重性缺陷：修复了DPS和2FA绕过
url: https://www.anquanke.com/post/id/307704
source: 安全客-有思想的安全新媒体
date: 2025-05-24
fetch_date: 2025-10-06T22:27:11.841411
---

# GitLab修补高严重性缺陷：修复了DPS和2FA绕过

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

# GitLab修补高严重性缺陷：修复了DPS和2FA绕过

阅读量**132904**

发布时间 : 2025-05-23 17:09:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/gitlab-patches-high-severity-flaws-dos-and-2fa-bypass-fixed/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2023-7028 & CVE-2023-5356 GitLab 漏洞,DoS 漏洞]()

GitLab宣布发布其社区版(CE)和企业版(EE)的18.0.1、17.11.3和17.10.7版本,解决各种高、中度严重度的安全漏洞。

[高严重性漏洞](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)(跟踪为CVE-2025-0993(CVSS 7.5)),存在于17.10.7、17.11.3和18.0.1之前的所有版本中。该漏洞允许经过身份验证的攻击者通过未受保护的大型 Blob 端点耗尽服务器资源,*从而导致拒绝服务:“这可能允许经过身份验证的攻击者通过耗尽服务器资源来导致拒绝服务条件。*

另一个关键问题,跟踪为CVE-2024-12093,影响了基于SAML的身份验证。由于XPath验证不当[,](https://securityonline.info/bitdefender-gravityzone-small-business-security-review-enterprise-grade-protection-without-the-enterprise-headache/)攻击者可以操纵SAML响应以绕过双因素身份验证(2FA)*:“不当的XPath验证允许在特殊条件下修改SAML响应以绕过2FA要求。*

这个中等严重性缺陷(CVSS 6.8)影响了可以追溯到GitLab 11.1的版本。

[修补了其他几个DoS和访问控制漏洞](https://securityonline.info/hostedscan-review-proactive-vulnerability-management-for-a-bulletproof-digital-presence/),包括:

* **CVE-2024-7803** : 不和谐的webhook集成可能会触发DoS(CVSS 6.5 ) 。
* **CVE-2025-3111** :无界Kubernetes集群令牌可能会耗尽资源(CVSS 6.5)。
* **CVE-2025-2853** :启用 DoS 的未验证的备注位置(CVSS 6.5)。
* **CVE-2025-4979** :通过UI行为(CVSS 4.9)暴露的蒙面CI/CD变量。
* **CVE-2025-0605** :组访问控制允许用户绕过2FA(CVSS 4.6)。
* **CVE-2025-0679** :完整的电子邮件地址暴露给未经授权的用户(CVSS 4.3)。
* **CVE-2024-9163** :机密MRs(CVSS 3.5)中的分支名称混淆。
* **CVE-2025-1110** :通过 GraphQL 查询(CVSS 2.7)未经授权的作业数据访问。

*GitLab敦促所有自我管理的用户立即升级:“我们强烈建议所有运行受以下问题影响的版本的安装尽快升级到最新版本。*

本文翻译自securityonline [原文链接](https://securityonline.info/gitlab-patches-high-severity-flaws-dos-and-2fa-bypass-fixed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307704](/post/id/307704)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/gitlab-patches-high-severity-flaws-dos-and-2fa-bypass-fixed/)

如若转载,请注明出处： <https://securityonline.info/gitlab-patches-high-severity-flaws-dos-and-2fa-bypass-fixed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞分析](/tag/%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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