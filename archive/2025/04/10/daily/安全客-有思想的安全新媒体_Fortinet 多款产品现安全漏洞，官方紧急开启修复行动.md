---
title: Fortinet 多款产品现安全漏洞，官方紧急开启修复行动
url: https://www.anquanke.com/post/id/306300
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:04.904891
---

# Fortinet 多款产品现安全漏洞，官方紧急开启修复行动

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

# Fortinet 多款产品现安全漏洞，官方紧急开启修复行动

阅读量**54768**

发布时间 : 2025-04-09 10:26:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/fortinet-multiple-vulnerabilities-fortios/>

译文仅供参考，具体内容表达以及含义原文为准。

Fortinet 已披露并修复了其产品套件中的多个漏洞，涉及的产品包括 FortiAnalyzer、FortiManager、FortiOS、FortiProxy、FortiVoice、FortiWeb 以及 FortiSwitch。

这些漏洞涵盖了从日志输出的不当处理到未经验证的密码修改，以及对凭据保护不足等方面。该公司已发布了补丁和缓解策略，以保护用户免受潜在的漏洞利用威胁。

### ****FortiOS 中凭据保护不足漏洞****

在 FortiOS 中发现的一个关键漏洞是关于凭据保护不足（CWE-522）的问题。这一缺陷可能使经过身份验证的特权攻击者通过将配置中的轻量级目录访问协议（LDAP）服务器 IP 地址重定向到恶意服务器，从而获取 LDAP 凭据。

****受影响版本****：

1.FortiOS 7.4、7.2、7.0 和 6.4 的所有版本均存在漏洞。

2.FortiOS 7.6 版本不受影响。

建议用户使用 Fortinet 的升级工具迁移到已修复的版本。Fortinet 感谢 Vladislav Driev 和 Oleg Labyntsev 以负责任的态度报告了这一漏洞。

### ****FortiManager 和 FortiAnalyzer 中日志输出处理不当漏洞****

另一个漏洞（CWE-117）影响到了 FortiManager 和 FortiAnalyzer，可能会让未经身份验证的远程攻击者通过精心构造的登录请求来污染日志。

****受影响版本****：

1.这两款产品的 7.6.0 至 7.6.1 版本均存在漏洞。

2.更早的版本，如 7.4.x 和 7.2.x 也受到影响。

用户应将 FortiManager 和 FortiAnalyzer 升级到 7.6.2 或更高版本。Fortinet 感谢来自 A1 Digital International 的 Alexandre Labb 发现了这一问题。

### ****多款产品存在中间人攻击漏洞****

在包括 FortiOS、FortiProxy、FortiManager 等在内的多款产品中发现了一个中间人攻击漏洞（CWE-923）。

这一漏洞可能使攻击者通过拦截被管理设备与管理系统（如 FortiCloud 或 FortiManager）之间的身份验证请求，来冒充管理设备。

****受影响版本****：

1.受影响的版本涵盖了 FortiOS（6.x 至 7.x）、FortiProxy（2.x 至 7.x）的多个版本，以及其他产品如 FortiVoice 和 FortiWeb。

2.用户应按照安全公告中的指定升级到已修复的版本。这一漏洞是由 Fortinet 产品安全团队的 Théo Leleu 和开发团队的 Stephen Bevan 在公司内部发现的。

### ****FortiSwitch GUI 中未经验证的密码修改漏洞****

Fortinet 还披露了其 FortiSwitch 产品 GUI 中存在的未经验证的密码修改漏洞（CWE-620）。这一问题可能会让远程未经身份验证的攻击者通过精心构造的请求来修改管理员密码。

****受影响版本****：

1.6.4.x 至 7.x 版本存在漏洞。

2.可升级到已修复的版本，或者作为临时解决方案，禁用管理界面的 HTTP/HTTPS 访问。这一漏洞是由 FortiSwitch Web UI 开发团队的 Daniel Rozeboom 发现的，Fortinet 对其表示感谢。

Fortinet 强烈建议用户立即使用其升级工具对系统进行升级，或者在无法打补丁的情况下采用可用的临时解决方案。

该公司与研究人员和国际机构密切合作，以确保及时披露漏洞并制定缓解策略。

在负责任的漏洞披露实践中，Fortinet 认可 Vladislav Driev、Oleg Labyntsev、Alexandre Labb、Théo Leleu、Stephen Bevan 和 Daniel Rozeboom等安全研究人员的贡献，这凸显了在解决这些漏洞方面的协作努力。

所有安全公告均于 2025 年 4 月 8 日发布，这是在维护透明度和确保其产品生态系统中客户安全方面迈出的重要一步。

用户可以参考 Fortinet 的官方文档，以获取有关升级或缓解与这些漏洞相关风险的详细指导。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/fortinet-multiple-vulnerabilities-fortios/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306300](/post/id/306300)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/fortinet-multiple-vulnerabilities-fortios/)

如若转载,请注明出处： <https://cybersecuritynews.com/fortinet-multiple-vulnerabilities-fortios/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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