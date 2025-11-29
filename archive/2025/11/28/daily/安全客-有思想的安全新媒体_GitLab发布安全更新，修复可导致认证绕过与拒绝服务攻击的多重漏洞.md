---
title: GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞
url: https://www.anquanke.com/post/id/313477
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:17.688094
---

# GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞

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

# GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞

阅读量**22849**

发布时间 : 2025-11-28 18:07:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/gitlab-patches-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

GitLab 已为其社区版（CE）和企业版（EE）发布 **关键安全更新**，以修复多个 **高严重性漏洞**。

此次发布的 18.6.1、18.5.3 和 18.4.5 版本补丁，修复了可能允许攻击者绕过身份验证、窃取用户凭据或通过拒绝服务（DoS）攻击崩溃服务器的安全缺陷。安全专家和 GitLab 管理员被敦促 **立即升级自托管实例**，GitLab.com 已完成补丁部署以保护用户。

### 凭据窃取与系统崩溃风险

![]()

本次更新中最值得关注的漏洞是 **CVE-2024-9183**，这是一个标记为 CI/CD 缓存中“竞争条件”的高严重性问题。该缺陷可使 **已认证攻击者窃取更高权限用户的凭据**，恶意用户通过利用此时间差错误，可能接管管理员账户或执行未授权操作。

另一重要修复针对 **CVE-2025-12571**，一个危险的 DoS 漏洞。此漏洞允许 **未认证攻击者（无需用户名密码）通过发送恶意 JSON 请求崩溃 GitLab 实例**，可能导致组织的代码仓库离线，中断开发工作流。

### 身份验证绕过漏洞

更新还解决了 **CVE-2025-12653**，一个中严重性问题：未认证用户可通过操纵网络请求头 **绕过安全检查并加入任意组织**。尽管严重性低于崩溃漏洞，但这种绕过对组织隐私和访问控制构成重大风险。

GitLab 强烈建议所有运行受影响版本的客户 **立即升级至最新补丁版本**（18.6.1、18.5.3 或 18.4.5）。升级影响：单节点实例将因数据库迁移经历停机，多节点实例可执行零停机升级。

若不及时更新，攻击者可通过分析公开补丁逆向工程漏洞利用方法，使实例持续暴露风险。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/gitlab-patches-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313477](/post/id/313477)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/gitlab-patches-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/gitlab-patches-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **750**

* 粉丝
* **6**

### TA的文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22

### 相关文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22
* ##### [逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下](/post/id/313462)

  2025-11-28 18:02:37
* ##### [纳闽再保险启用绿色数据中心，实现效能提升与运营成本优化](/post/id/313459)

  2025-11-28 18:00:45
* ##### [遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态](/post/id/313453)

  2025-11-28 18:00:14

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