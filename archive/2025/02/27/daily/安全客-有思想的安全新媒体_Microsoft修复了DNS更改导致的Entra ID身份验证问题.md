---
title: Microsoft修复了DNS更改导致的Entra ID身份验证问题
url: https://www.anquanke.com/post/id/304770
source: 安全客-有思想的安全新媒体
date: 2025-02-27
fetch_date: 2025-10-06T20:35:18.692697
---

# Microsoft修复了DNS更改导致的Entra ID身份验证问题

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

# Microsoft修复了DNS更改导致的Entra ID身份验证问题

阅读量**58693**

发布时间 : 2025-02-26 11:17:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-entra-id-authentication-issue-caused-by-dns-change/>

译文仅供参考，具体内容表达以及含义原文为准。

![Microsoft sign in]()

Microsoft 已修复一个问题，该问题导致在使用公司的Seamless SSO和Microsoft Entra Connect Sync时，Entra ID 的 DNS 身份验证失败。

在其 Azure 状态页面的更新中，Microsoft 表示，这些问题是由近期的一次 DNS 更改引发的。在 2025 年 2 月 25 日协调世界时间 17 点 18 分至 18 点 35 分期间，当客户尝试访问 Azure 服务时，该更改导致autologon.microsoftazuread.sso.com域的 DNS 解析失败。

Microsoft 解释称：“到目前为止我们了解到什么？作为删除重复 IPv6 CNAME 记录清理工作的一部分，进行了一项更改，该更改移除了Microsoft Entra ID 无缝单点登录功能身份验证过程中使用的一个域名。一旦该域名被移除，就无法再解析，身份验证请求也就会失败。”

“这些问题是由近期的一次 DNS 更改导致的，目前该更改已被回滚，服务已完全恢复。此时，客户不应再遇到 DNS 解析失败的情况。”

尽管Microsoft 尚未透露哪些地区和 Azure 服务受到了影响 Entra ID（前身为 Azure Active Directory）的这些身份验证失败的影响，但Microsoft 表示，Azure 状态页面仅用于跟踪 “大规模事件”。

虽然Microsoft 还承诺在接下来的 60 分钟内分享更多细节，但在更新状态页面后，它立即删除了事件报告。

**更多 DNS 事件和近期故障**

这并非Microsoft 首次处理由 DNS 问题导致的故障和事件。2023 年 8 月，该公司修复了一个配置错误的 DNS SPF 记录，该错误导致 Hotmail 电子邮件在全球范围内无法投递。两年前，即 2021 年 4 月，一个代码缺陷引发了一次全球范围的故障，由于 Azure DNS 服务器过载，许多Microsoft 服务受到影响。

上个月，Microsoft 还回滚了一项网络配置更改，该更改在 1 月 8 日至 1 月 10 日期间给美国东部 2 地区的客户使用多个 Azure 服务时造成了连接问题、长时间超时、连接中断和资源分配失败。

受影响的 Azure 服务包括 Azure Databricks、Azure OpenAI、Azure 应用服务、Azure 容器应用、Azure SQL 数据库、Azure DevOps、Azure NetApp Files、Azure 流分析等等。

1 月下旬的一次Microsoft  365 故障还导致管理员无法访问Microsoft  365 管理中心，而两周前的一次多因素身份验证（MFA）故障则使客户无法访问Microsoft  365 办公应用程序。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-entra-id-authentication-issue-caused-by-dns-change/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304770](/post/id/304770)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-entra-id-authentication-issue-caused-by-dns-change/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-entra-id-authentication-issue-caused-by-dns-change/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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