---
title: KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据
url: https://www.anquanke.com/post/id/313655
source: 安全客-有思想的安全新媒体
date: 2025-12-10
fetch_date: 2025-12-11T03:22:40.205554
---

# KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据

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

# KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据

阅读量**16577**

发布时间 : 2025-12-10 18:32:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta ，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/kimjongrat-attacking-windows-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为 **KimJongRAT** 的新型远程访问木马（RAT）已出现，对 Windows 用户构成严重威胁。

这款精密的恶意软件被认为是由 **Kimsuky 组织**（一个据称具有国家背景的威胁行为体）操控。

攻击活动通常始于一封钓鱼邮件，邮件中包含名为 “国家税务通知（National Tax Notice）” 的欺诈性压缩包，诱骗毫无防备的受害者启动感染链。

用户打开恶意压缩包后，会看到一个伪装成合法 PDF 文档的**快捷方式文件**。

![]()

该快捷方式执行后，会触发一条隐藏命令：解码 Base64 编码的 URL，并滥用微软合法的 HTML 应用程序（HTA）工具与远程服务器建立连接。

这一过程会秘密下载名为 `tax.hta` 的额外恶意载荷，从而有效绕过标准安全检测。

Lyac 安全分析师发现，该加载器脚本基于 **VBScript 编写**，并采用了巧妙的**规避检测技术**。

该恶意软件通过利用 **Google Drive 等合法服务**托管恶意组件，试图躲避安全检测。

加载器激活后，会同时获取用于欺骗用户的**诱饵文档**和攻击下一阶段所需的**实际恶意二进制文件**。

### 敏感数据窃取行为

此次攻击活动的核心目标是**窃取敏感个人与财务数据**。

恶意软件会靶向收集各类信息，包括系统详情、浏览器存储数据及加密密钥。

其重点搜寻**加密货币钱包信息**以及 Telegram、Discord 等通信平台的**登录凭据**，使其成为身份盗窃与金融诈骗的高危工具。

KimJongRAT 最显著的特征是**能够根据目标环境的安全状态调整行为**：

在执行后续操作前，恶意软件会运行特定 VBScript 命令检查 Windows Defender 的状态。

它通过执行代码片段 `Set exec = oShell.Exec(ss)`，再结合 `If InStr(output, "STOPPED") > 0 Then` 判断该安全服务是否处于活跃状态。

* 若 Windows Defender 已禁用，恶意软件会下载名为 `v3.log` 的文件，该文件将执行核心恶意载荷；
* 若安全服务处于活跃状态，则会获取名为 `pipe.log` 的替代文件以规避检测。

无论采用哪种路径，恶意软件都会通过**在系统注册表中注册自身**建立持久控制，确保开机自动运行，并定期传输窃取的数据。

尽管 “恶意软件劫持的加密货币钱包清单” 凸显了其靶向应用的广度，但也揭示了这一针对性威胁背后明确的**财务掠夺意图**。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/kimjongrat-attacking-windows-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313655](/post/id/313655)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/kimjongrat-attacking-windows-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/kimjongrat-attacking-windows-users/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **790**

* 粉丝
* **6**

### TA的文章

* ##### [LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击](/post/id/313652)

  2025-12-10 18:32:53
* ##### [KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据](/post/id/313655)

  2025-12-10 18:32:25
* ##### [新型多阶段 JS#SMUGGLER 恶意软件攻击通过投递 NetSupport RAT 实现系统完全控制](/post/id/313649)

  2025-12-10 18:31:50
* ##### [勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术](/post/id/313647)

  2025-12-10 17:36:18
* ##### [Checkmarx 收购 Tromzo，强化 AI 安全自动化能力](/post/id/313645)

  2025-12-10 17:35:33

### 相关文章

* ##### [LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击](/post/id/313652)

  2025-12-10 18:32:53
* ##### [新型多阶段 JS#SMUGGLER 恶意软件攻击通过投递 NetSupport RAT 实现系统完全控制](/post/id/313649)

  2025-12-10 18:31:50
* ##### [勒索软件团伙 Storm-0249 升级攻击手段：滥用 ClickFix 工具、无文件 PowerShell 与 DLL 劫持技术](/post/id/313647)

  2025-12-10 17:36:18
* ##### [Checkmarx 收购 Tromzo，强化 AI 安全自动化能力](/post/id/313645)

  2025-12-10 17:35:33
* ##### [高危 n8n 远程代码执行漏洞（CVE-2025-65964）可通过操纵 Git 节点配置实现远程代码执行](/post/id/313634)

  2025-12-10 17:35:08
* ##### [FortiOS、FortiWeb 及 FortiProxy 漏洞可导致攻击者绕过 FortiCloud 单点登录（SSO）认证](/post/id/313637)

  2025-12-10 17:33:59
* ##### [Stripe 推出 Tempo 支付区块链并开放公测，万事达卡、瑞银集团已正式接入](/post/id/313639)

  2025-12-10 17:32:42

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