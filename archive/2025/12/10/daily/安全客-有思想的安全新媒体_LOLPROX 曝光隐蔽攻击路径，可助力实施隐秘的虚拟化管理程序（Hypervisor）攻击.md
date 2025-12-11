---
title: LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击
url: https://www.anquanke.com/post/id/313652
source: 安全客-有思想的安全新媒体
date: 2025-12-10
fetch_date: 2025-12-11T03:22:38.084049
---

# LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击

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

# LOLPROX 曝光隐蔽攻击路径，可助力实施隐秘的虚拟化管理程序（Hypervisor）攻击

阅读量**17336**

发布时间 : 2025-12-10 18:32:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源： cybersecuritynews

原文地址：<https://cybersecuritynews.com/lolprox-exposes-hidden-exploitation-paths/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Proxmox 虚拟环境（Proxmox Virtual Environment）已成为企业构建私有云基础设施与虚拟机管理系统的热门选择。

然而，一项最新分析显示，一旦攻击者获得系统的**初始访问权限**，该虚拟化管理程序（Hypervisor）存在重大安全漏洞，可被攻击者利用实施攻击。

该研究曝光了一系列**攻击向量**，攻击者可借助这些向量在虚拟机间横向移动、窃取敏感数据，并维持持久控制，且不会触发传统安全告警。

这些漏洞的核心在于研究人员所称的 “**依托虚拟化管理程序驻留（Living off the hypervisor）** ” 技术 —— 即滥用 Proxmox 的合法工具与功能实施恶意行为。

与旨在检测外部威胁的安全措施不同，这些攻击手段利用的是系统管理员日常用于合法操作的**内置功能**，这使得攻击检测难度大幅增加。

Proxmox 对攻击者极具吸引力的原因在于其架构特性：与运行专用微内核的专有虚拟化管理程序不同，Proxmox 本质上是一个完整的 Debian Linux 发行版，仅在其上叠加了虚拟化工具。

这种架构融合形成了独特的**攻击面**—— 标准的 Linux 权限提升技术可与虚拟化管理程序专属功能相结合，而防御者通常未能对这些功能进行有效监控。

一旦攻击者攻陷 Proxmox 主机，理论上即可获得对该主机管理的**所有虚拟机**的访问权限。

安全工程师安迪・吉尔（Andy Gill）在其全面的技术研究中，识别并记录了这些攻击路径。

吉尔的分析表明，攻击者可**绕过网络检测系统**、在隔离的虚拟机内执行代码、从虚拟机内存与磁盘存储中窃取敏感信息，且上述行为均不会触发传统安全告警。

### 无网络痕迹的直接虚拟机执行

研究指出，**QEMU 客户机代理（QEMU guest agent）** 是一个尤其值得警惕的攻击向量。当虚拟机启用该客户机代理时（在虚拟机配置中显示为 `agent: 1`），虚拟化管理程序可直接在客户机操作系统内执行**任意命令**。

这类命令执行通过专用虚拟通道完成，**完全绕过网络协议栈**，不会留下防御者通常监控的网络连接日志、防火墙记录或典型认证事件。

命令执行权限与 QEMU 客户机代理服务权限一致 —— 在 Windows 和 Linux 系统中，该权限通常为**系统级访问权限**。

一旦攻击者发现启用了客户机代理的虚拟机，将几乎不会面临任何基于网络的检测障碍。

该研究还提供了在整个集群中识别脆弱目标的实用技术，并展示了与合法管理员自动化操作**无缝融合**的命令执行模式。

这种攻击方式无需借助网络跳转或传统漏洞利用手段，即可让攻击者在所有被攻陷的虚拟机上获得**完整代码执行权限**，从根本上破坏了大多数企业依赖的基于网络的检测策略。

本文翻译自 cybersecuritynews [原文链接](https://cybersecuritynews.com/lolprox-exposes-hidden-exploitation-paths/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313652](/post/id/313652)

安全KER - 有思想的安全新媒体

本文转载自:  [cybersecuritynews](https://cybersecuritynews.com/lolprox-exposes-hidden-exploitation-paths/)

如若转载,请注明出处： <https://cybersecuritynews.com/lolprox-exposes-hidden-exploitation-paths/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* ##### [KimJongRAT 利用武器化 .hta 文件攻击 Windows 用户，窃取登录凭据](/post/id/313655)

  2025-12-10 18:32:25
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