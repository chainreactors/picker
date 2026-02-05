---
title: Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序
url: https://www.anquanke.com/post/id/314725
source: 安全客-有思想的安全新媒体
date: 2026-02-04
fetch_date: 2026-02-05T04:07:51.262857
---

# Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序

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

# Open VSX供应链攻击事件，黑客利用遭攻陷开发者账户传播GlassWorm恶意程序

阅读量**17377**

发布时间 : 2026-02-04 11:23:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员披露了一起针对 **Open VSX 插件仓库**的供应链攻击详情，不明身份的威胁攻击者攻陷了一名合法开发者的相关资源，借此向下游用户推送恶意更新包。

“2026 年 1 月 30 日，由开发者 oorzc 发布的四款成熟 Open VSX 插件，被上传了嵌入**GlassWorm 恶意软件加载器**的恶意版本”，Socket 安全研究员基里尔・博伊琴科在周六发布的报告中指出。

“这些插件此前一直以正规开发者工具的身份存在（部分插件发布时间已超过两年），在恶意版本发布前，累计下载量已超 22000 次。”

这家供应链安全公司表示，此次攻击的核心是**开发者的插件发布凭据遭窃取**，Open VSX 安全团队评估认为，攻击者的作案手段要么是利用泄露的令牌，要么是通过其他方式实现了未授权访问。目前，这些恶意插件版本已被从 Open VSX 平台下架。

已确认的涉事插件名单如下：

* FTP/SFTP/SSH 同步工具（oorzc.ssh-tools — 版本 0.5.1）
* 国际化工具（oorzc.i18n-tools-plus — 版本 1.6.8）
* vscode 思维导图（oorzc.mind-map — 版本 1.0.61）
* scss 转 css（oorzc.scss-to-css-compile — 版本 1.3.4）

Socket 指出，这些被篡改的插件版本，其设计目的是投递一款与已知攻击活动相关联的加载器恶意软件，即 GlassWorm。该加载器可在运行时解密并执行嵌入的恶意代码，采用了一种日趋武器化的技术**EtherHiding**来获取命令与控制（C2）服务器地址，最终会执行恶意代码，窃取苹果 macOS 系统的账户凭据以及加密货币钱包数据。

同时，这款恶意软件并非立即触发执行，而是会先对受感染设备进行环境探查，**确认设备不属于俄语区域后才会启动**。这种模式在俄语区相关威胁组织开发的恶意程序中十分常见，目的是避免在本土范围内遭到法律追责。

该恶意软件窃取的信息类型包括：

* 火狐浏览器及基于 Chromium 内核的浏览器数据（登录凭证、Cookie、上网记录，以及 MetaMask 等钱包插件数据）
* 加密货币钱包文件（涵盖 Electrum、Exodus、Atomic、Ledger Live、Trezor Suite、币安、TonKeeper 等主流钱包）
* iCloud 钥匙串数据库
* Safari 浏览器 Cookie
* 苹果备忘录数据
* 桌面、文档、下载文件夹中的用户文件
* FortiClient VPN 配置文件
* 开发者凭据（例如～/.aws 和～/.ssh 目录下的文件）

针对开发者信息的窃取行为存在严重风险，可能导致企业环境面临云账户被攻陷、攻击者横向渗透内网等威胁。

“该恶意载荷包含专门的程序逻辑，可定位并提取日常开发流程中使用的认证信息，包括检查 npm 配置中的\_authToken 令牌、读取 GitHub 认证相关文件等，这些信息可被用于访问私有代码仓库、持续集成密钥以及发布自动化系统。” 博伊琴科补充道。

此次攻击的一个显著特点在于，它与此前发现的 GlassWorm 攻击特征存在差异 ——**攻击者借助遭攻陷的合法开发者账户来传播恶意软件**。而在以往的攻击活动中，该威胁组织通常会采用 “仿冒拼写插件名”“品牌劫持” 的手段，上传伪造插件以实现恶意传播。

“该威胁组织的攻击行为完全融入开发者的日常工作流程，将恶意执行逻辑隐藏在加密的、运行时解密的加载器中，还利用 Solana 区块链备忘录作为动态秘密传输点，无需重新发布插件即可更换中转服务器。”Socket 表示，“这些设计方案降低了静态特征检测的有效性，迫使防御方将防护重心转向行为检测与快速响应。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314725](/post/id/314725)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html)

如若转载,请注明出处： <https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1000**

* 粉丝
* **6**

### TA的文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58

### 相关文章

* ##### [“Exfil Out&Look”漏洞致攻击者可通过OWA隐秘窃取邮件](/post/id/314701)

  2026-02-04 11:28:08
* ##### [新型高级Web后门潜入通信基础设施，利用高危漏洞将电话系统变为持久化后门](/post/id/314704)

  2026-02-04 11:26:44
* ##### [暗网现新型工业控制系统攻击框架，直指能源基础设施](/post/id/314710)

  2026-02-04 11:26:03
* ##### [微软新版Windows 11更新悄然收紧存储设置权限](/post/id/314713)

  2026-02-04 11:25:28
* ##### [Apache Syncope修复高危登录跨站脚本及外部实体注入漏洞](/post/id/314719)

  2026-02-04 11:24:58
* ##### [Notepad++被劫持国家级攻击者投毒更新包，持续数月作恶](/post/id/314722)

  2026-02-04 11:24:22
* ##### [WiFi劫持风险，海康威视修复DS-3WAP系列无线接入点命令注入漏洞](/post/id/314716)

  2026-02-04 11:23:22

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