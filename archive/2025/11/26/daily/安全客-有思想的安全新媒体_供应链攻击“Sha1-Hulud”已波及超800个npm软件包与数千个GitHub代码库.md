---
title: 供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库
url: https://www.anquanke.com/post/id/313439
source: 安全客-有思想的安全新媒体
date: 2025-11-26
fetch_date: 2025-11-27T03:10:59.758114
---

# 供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库

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

# 供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库

阅读量**16702**

发布时间 : 2025-11-26 18:26:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/sha1-hulud-attack-hits-800-npm-packages/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**沙虫蠕虫（Shai-Huluda）**——一种以《沙丘》中的沙虫命名的自复制 npm 蠕虫——再度爆发。

此次攻击规模和复杂度极具破坏性，已入侵 **800 余个 npm 包**，生态系统内月下载量合计达 **1.32 亿次**。

攻击时机颇具策略性：正值 npm 12 月 9 日吊销传统令牌（classic tokens）的截止日前几周——该举措本旨在打击供应链攻击。许多开发者尚未准备好可信发布替代方案，这一窗口期成为攻击者扩大影响的理想机会。

![]()

### 蠕虫传播机制

据 Aikido Security 分析，沙虫蠕虫的传播效率极高。一旦感染开发者系统，恶意软件会在 **包安装过程中自动执行**（甚至在安装完成前），并同时部署多种攻击技术：

1. **机密窃取**：使用 TruffleHog 扫描暴露的密钥，包括 API 密钥、身份验证令牌、GitHub 凭据和云访问令牌。所有发现的敏感信息均被泄露至名为“Sha1-Hulud: The Second Coming”的公开 GitHub 仓库，研究人员已识别出 26,300 个攻击者创建的受损仓库。
2. **自我传播**：尝试将恶意副本发布至 npm，实现链式感染更多包和开发者。若身份验证失败，恶意软件会 **删除用户主目录文件**，以“焦土战术”造成最大破坏。

### 攻击技术升级与影响范围

此次变体比前几波更复杂：

1. 通过 `setup_bun.js` 安装 bun（JavaScript 运行时），再通过 `bun_environment.js` 执行实际有效载荷。
2. 不再使用硬编码仓库名，而是生成 **随机仓库标识符**，增加溯源和检测难度。
3. 攻击范围大幅扩大：每次感染目标从之前的 20 个 npm 包增至 **100 个**。

![]()

防御者还发现，部分受损包仅包含暂存代码而无完整蠕虫载荷，显示攻击者可能存在操作失误，在某些情况下限制了影响范围。

受影响的包来自多家大型科技组织，包括 AsyncAPI（36 个包）、PostHog（多个分析包）、Zapier（多个 SDK 和插件组件）、Postman（集合和工具包）、ENS（以太坊域名服务包）以及无数小型组织。AsyncAPI 团队证实，攻击者甚至在其 CLI 仓库中创建了恶意分支，表明 GitHub 凭据可能已被直接攻陷。

### 生态系统脆弱性与启示

1.32 亿次受影响下载意味着潜在影响波及数千家组织，其中许多尚未意识到系统可能已感染蠕虫。npm 社区的脆弱性部分源于 **依赖链过深**——开发者很少审计所有间接依赖包；加之 **密钥管理 practices 不足**，供应链攻击依然极具破坏性。

组织必须认识到：包安装不再仅是管理操作，而是 **关键安全事件**，需要主动威胁监控和凭据保护。

本文翻译自gbhackers [原文链接](https://gbhackers.com/sha1-hulud-attack-hits-800-npm-packages/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313439](/post/id/313439)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/sha1-hulud-attack-hits-800-npm-packages/)

如若转载,请注明出处： <https://gbhackers.com/sha1-hulud-attack-hits-800-npm-packages/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **740**

* 粉丝
* **6**

### TA的文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44

### 相关文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44
* ##### [高级威胁组织ToddyCat升级攻击工具库，新型工具专门窃取Outlook邮件并劫持Microsoft 365访问令牌](/post/id/313434)

  2025-11-26 18:27:40
* ##### [威胁行为体利用Blender基金会官方文件作为载体，传播臭名昭著的StealC V2信息窃取木马](/post/id/313427)

  2025-11-26 18:26:53

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