---
title: 大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件
url: https://www.anquanke.com/post/id/313473
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:15.700052
---

# 大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件

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

# 大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件

阅读量**23119**

发布时间 : 2025-11-28 18:08:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/dead-mans-switch-npm-supply-chain-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

GitLab 漏洞研究团队发现了一起大规模供应链攻击，通过 npm 生态系统传播一种 **破坏性恶意软件变体**。

该恶意软件是“沙虫蠕虫（Shai-Hulud）”的进化版本，包含一个危险功能：若攻击者失去基础设施控制权，将 **销毁用户数据**。恶意软件通过多阶段流程在受感染的 npm 包中传播。

当开发者安装受感染的包时，脚本会自动下载看似合法的 **Bun JavaScript 运行时**——但这只是恶意软件实际 payload 的伪装。这个经过高度混淆的 **10MB 文件** 会在受害者系统上执行。

### 受影响的 npm 包

一旦运行，恶意软件会从多个来源 **主动窃取凭据**，包括 GitHub 令牌、npm 身份验证密钥以及 AWS、Google Cloud 和 Microsoft Azure 的账户信息。它甚至会下载合法安全工具 **TruffleHog**，扫描整个主目录以寻找配置文件中隐藏的 API 密钥和密码。

利用窃取的 npm 令牌，恶意软件会 **自动感染受害者维护的所有其他包**：修改 `package.json` 文件以植入恶意脚本、递增版本号，并将所有内容重新发布到 npm。这种蠕虫式行为使攻击在生态系统中呈指数级传播。

被盗凭据会被泄露至攻击者控制的 GitHub 仓库，仓库标记为“**Sha1-Hulud: The Second Coming**”。这些仓库形成类似僵尸网络的弹性网络，受感染系统在其中共享访问令牌。

![]()

最关键的是，恶意软件包含一个旨在保护攻击基础设施的 **破坏性 payload**：若受感染系统同时失去对 GitHub 和 npm 的访问权限，将立即触发数据销毁。在 Windows 系统上，恶意软件会尝试删除所有用户文件并覆盖磁盘扇区；在 Linux 和 Mac 系统上，则使用高级擦除技术使文件恢复变得不可能。

这造成了一个危险场景：如果 GitHub 删除恶意仓库或 npm 吊销受损令牌，互联网上成千上万的受感染系统可能会同时销毁用户数据。

GitLab 建议在项目中启用 **依赖项扫描**，以便在受感染包进入生产环境前自动检测。安全团队还应监控可疑的 npm 预安装脚本和依赖项中异常的版本递增。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/dead-mans-switch-npm-supply-chain-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313473](/post/id/313473)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/dead-mans-switch-npm-supply-chain-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/dead-mans-switch-npm-supply-chain-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
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