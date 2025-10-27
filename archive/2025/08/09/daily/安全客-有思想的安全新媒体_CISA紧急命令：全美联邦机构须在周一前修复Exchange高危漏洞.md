---
title: CISA紧急命令：全美联邦机构须在周一前修复Exchange高危漏洞
url: https://www.anquanke.com/post/id/310946
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:36.939095
---

# CISA紧急命令：全美联邦机构须在周一前修复Exchange高危漏洞

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

# CISA紧急命令：全美联邦机构须在周一前修复Exchange高危漏洞

阅读量**74834**

发布时间 : 2025-08-08 17:04:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-orders-fed-agencies-to-patch-new-cve-2025-53786-exchange-flaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）已发布紧急指令，要求所有联邦文职行政部门（FCEB）机构在美国东部时间周一上午 9 点前修复一个**严重的 Microsoft Exchange 混合部署漏洞**（编号 CVE-2025-53786）。

联邦文职行政部门（FCEB）指的是美国行政部门中非军事机构，包括国土安全部、财政部、能源部以及卫生与公众服务部等。

该漏洞（CVE-2025-53786）**允许攻击者在获得本地部署的 Exchange 服务器管理员权限后，横向渗透到 Microsoft 云环境，可能导致整个域被完全攻陷**。

漏洞影响 **Microsoft Exchange Server 2016、2019 以及订阅版**。在混合部署环境中，Exchange Online 与本地 Exchange 服务器共享同一个服务主体（service principal），它是双方进行身份验证的一种信任关系。攻击者如果在本地 Exchange 服务器上获得管理员权限，就可能伪造或篡改云端可接受的受信令牌或 API 调用，从而实现从本地网络横向渗透到企业云环境，进而危及企业的整个 Active Directory 和基础设施。

更糟糕的是，微软表示，如果恶意活动源自本地 Exchange，基于云的日志工具（如 Microsoft Purview）可能无法记录相关行为，使得攻击难以被发现。

这一漏洞是在微软 2025 年 4 月发布的安全架构更新和 Exchange 补丁之后被披露的。该更新是微软**“安全未来计划”**（Secure Future Initiative）的一部分，引入了专用混合应用程序来取代原先的共享应用程序架构。

昨天，安全研究员 Dirk-Jan Mollema（来自 Outsider Security）在 Black Hat 大会上展示了这种共享服务主体如何在后渗透攻击中被利用。他在接受 BleepingComputer 采访时表示，自己在演讲前三周已将漏洞报告给微软，以便提前预警。微软随后在协调下发布了 CVE-2025-53786 编号及缓解指南。

Mollema 解释道：

> “我最初并不认为这是一个漏洞，因为该攻击使用的协议本来就具备这些功能，只是整体上缺乏关键安全控制。我向微软安全响应中心（MSRC）发送了报告，提醒他们可能存在的攻击途径。除了发布缓解指南外，微软还修补了一条可能导致从本地 Exchange 升级到全局管理员权限、从而完全攻陷租户的攻击路径。”

好消息是，那些在此前已按照 4 月的指南部署补丁的 Exchange 客户，已经免受这一新型后渗透攻击的威胁。但尚未实施缓解措施的组织仍然受影响，必须尽快安装补丁，并按照微软文档（doc 1 和 doc 2）的说明部署专用混合应用。

Mollema 提醒，仅安装补丁并不足以防御，还需要手动执行后续操作，**将服务主体迁移到专用模式**。他补充说：

> “从安全角度看，紧迫程度取决于管理员对本地 Exchange 资源与云端资源隔离的重视程度。在旧架构下，Exchange 混合模式对 Exchange Online 和 SharePoint 中的所有资源都拥有完全访问权限。”

需要注意的是，这是一种后渗透攻击方式——也就是说，攻击者必须已经攻陷本地环境或 Exchange 服务器，并且具备管理员权限，才能利用该漏洞。

根据 CISA 的《紧急指令 25-02》，联邦机构需**先使用微软的 Health Checker 脚本清点 Exchange 环境**。对于已不受 4 月补丁支持的版本（如已停用的 Exchange 版本），必须断开连接。

其余服务器则必须更新至最新的累积更新版本（Exchange 2019 为 CU14 或 CU15，Exchange 2016 为 CU23），并安装 4 月的补丁。之后，管理员需运行微软的 `ConfigureExchangeHybridApplication.ps1` PowerShell 脚本，将 Entra ID 中的共享服务主体切换为专用服务主体。

CISA 警告称，若未实施这些缓解措施，混合部署环境可能会被完全攻陷。所有机构必须在周一上午完成技术修复，并在当天美国东部时间下午 5 点前向 CISA 提交报告。

虽然非政府组织不在该指令的强制范围内，CISA 仍敦促所有组织立即采取措施。CISA 代理局长 Madhu Gottumukkala 表示：

> “这一 Microsoft Exchange 漏洞的风险，影响到所有使用该环境的组织和行业。虽然联邦机构是强制执行对象，但我们强烈建议所有组织都采取本紧急指令中的防护措施。”

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-orders-fed-agencies-to-patch-new-cve-2025-53786-exchange-flaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310946](/post/id/310946)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-orders-fed-agencies-to-patch-new-cve-2025-53786-exchange-flaw/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-orders-fed-agencies-to-patch-new-cve-2025-53786-exchange-flaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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