---
title: Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃
url: https://www.anquanke.com/post/id/313486
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:20.314805
---

# Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃

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

# Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃

阅读量**22359**

发布时间 : 2025-11-28 18:05:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/next-js-servers-dos-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Next.js 框架中最新发现的一个 **严重漏洞** 允许攻击者通过 **单个 HTTP 请求** 崩溃自托管服务器，且执行所需资源极少。

该拒绝服务（DoS）漏洞由 Harmony Intelligence 研究员发现，影响框架的广泛版本，包括补丁发布前的最新 **15.x 分支**。

漏洞位于 `body-streams.ts` 文件的 `cloneBodyStream` 函数中，该组件负责在将流式请求传递给中间件前将其复制到内存。与需要泛洪网络的典型资源耗尽攻击不同，此漏洞利用 **内部内存缓冲区缺乏大小限制** 的缺陷。

根据披露信息，攻击者可向服务器发送 **无限数据流块**——攻击者发送后可立即释放自身内存中的每个块，但 Next.js 服务器会尝试在 RAM 中缓冲整个流。这种不对称性意味着，研究人员描述为“智能烤面包机”的低资源设备，就能通过耗尽内存成功崩溃 robust 的企业服务器。

### 漏洞发现过程

Harmony Intelligence 在测试 AI AppSec 代理以对抗另一个已知漏洞（CVE-2025-29927 身份验证绕过）时，意外发现了此缺陷。测试中，代理自主执行了一段概念验证脚本，导致演示应用崩溃，从而揭示了 Next.js 框架中这一零日漏洞。

### 受影响系统与影响范围

Harmony 表示，该漏洞 **专门影响使用中间件的自托管 Next.js 应用**，直接托管在 Vercel 基础设施上的应用不受影响。

鉴于约 **55% 的 Next.js 部署为自托管**（企业环境中高达 80%），潜在攻击面巨大。

目前该漏洞尚未分配 CVE 编号（已提交申请），研究人员建议 CVSS v3.1 severity 评分为 **7.5（高）**，理由是攻击门槛低且无需身份验证。

Vercel 已于 **2025 年 10 月 13 日修复该漏洞**，引入 **10MB 的默认内部缓冲区大小限制**。管理员被敦促立即升级，或实施严格的代理级约束。

![]()

研究人员强调，标准速率限制解决方案对此攻击无效，因为崩溃发生在中间件速率限制器处理请求之前；同样，Next.js 内置的 `bodyParser.sizeLimit` 配置也无法阻止这种特定的内存耗尽向量。

这一发现凸显了自托管架构 **纵深防御策略** 的重要性：虽然升级是根本修复措施，但在应用服务器前部署配置适当的反向代理，在请求到达应用层前拒绝超大请求，仍是关键最佳实践。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/next-js-servers-dos-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313486](/post/id/313486)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/next-js-servers-dos-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/next-js-servers-dos-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
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