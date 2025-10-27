---
title: 新型 “Helldown ”勒索软件变种将攻击范围扩大到 VMware 和 Linux 系统
url: https://www.anquanke.com/post/id/302098
source: 安全客-有思想的安全新媒体
date: 2024-11-22
fetch_date: 2025-10-06T19:13:12.440125
---

# 新型 “Helldown ”勒索软件变种将攻击范围扩大到 VMware 和 Linux 系统

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

# 新型 “Helldown ”勒索软件变种将攻击范围扩大到 VMware 和 Linux 系统

阅读量**79810**

发布时间 : 2024-11-21 15:53:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种名为 “Helldown ”的新型勒索软件的 Linux 变种，这表明威胁分子正在扩大其攻击重点。

“Helldown 部署了源自 LockBit 3.0 代码的 Windows 勒索软件，”Sekoia 在与 The Hacker News 分享的一份报告中说。“鉴于最近针对 ESX 的勒索软件的发展，该组织似乎可能正在发展其当前的行动，以通过 VMware 来攻击虚拟化基础设施。”

Halcyon于2024年8月中旬首次公开记录了Helldown，将其描述为一个 “侵略性勒索软件组织”，通过利用安全漏洞渗透目标网络。该网络犯罪集团的主要目标行业包括 IT 服务、电信、制造和医疗保健。

与其他勒索软件团伙一样，Helldown 以利用数据泄露网站威胁公布被盗数据，迫使受害者支付赎金而闻名，这种策略被称为双重勒索。据估计，它在三个月内至少攻击了 31 家公司。

Truesec 在本月早些时候发布的一份分析报告中详细介绍了 Helldown 攻击链，据观察，该攻击链利用面向互联网的 Zyxel 防火墙获取初始访问权限，然后进行持久性攻击、凭证收集、网络查点、防御规避和横向移动活动，最终部署勒索软件。

Sekoia的最新分析显示，攻击者正在滥用Zyxel设备中已知和未知的安全漏洞来入侵网络，利用这个立足点窃取凭证并与临时用户创建SSL VPN隧道。

Windows 版本的 Helldown 一旦启动，就会在渗出和加密文件之前执行一系列步骤，包括删除系统阴影副本和终止与数据库和 Microsoft Office 有关的各种进程。在最后一步，它会删除勒索软件二进制文件以掩盖踪迹，并丢弃一张赎金纸条，然后关闭机器。

法国网络安全公司称，该勒索软件的Linux对应程序缺乏混淆和反调试机制，同时包含一套简洁的功能来搜索和加密文件，但在此之前不会列出并杀死所有活动的虚拟机（VM）。

“静态和动态分析没有发现任何网络通信，也没有发现任何公开密钥或共享秘密，”它说。“这一点值得注意，因为它提出了攻击者如何提供解密工具的问题。”

“在加密前终止虚拟机可授予勒索软件写入镜像文件的权限。然而，静态和动态分析都显示，虽然代码中存在这一功能，但实际上并未调用。所有这些观察结果表明，勒索软件并不复杂，可能仍在开发中。”

Helldown Windows人工制品与DarkRace在行为上有相似之处，后者于2023年5月出现，使用了LockBit 3.0的代码，后来改名为DoNex。早在 2024 年 7 月，Avast 就提供了 DoNex 的解密程序。

Sekoia说：“这两种代码都是LockBit 3.0的变种。鉴于 Darkrace 和 Donex 的品牌重塑历史及其与 Helldown 的显著相似性，不能排除 Helldown 是另一个品牌重塑的可能性。不过，这种联系在现阶段还无法得到明确证实。”

思科塔洛斯（Cisco Talos）披露了另一个名为 “Interlock ”的新兴勒索软件家族，该家族专门针对美国的医疗保健、技术和政府部门以及欧洲的制造业实体。它能够加密 Windows 和 Linux 机器。

据观察，传播勒索软件的攻击链使用了一个假冒的谷歌 Chrome 浏览器更新程序二进制文件，该二进制文件托管在一个合法但已损坏的新闻网站上，运行时会释放一个远程访问木马（RAT），允许攻击者提取敏感数据并执行 PowerShell 命令，该命令旨在投放有效载荷，以获取凭据并进行侦察。

“在他们的博客中，Interlock 声称他们利用未解决的漏洞来攻击组织的基础设施，并声称他们的行动除了金钱利益外，部分动机是希望让公司对糟糕的网络安全负责，”Talos 的研究人员说。

该公司补充说，据评估，Interlock 是一个从 Rhysida 操作员或开发人员中衍生出来的新组织，他们在手法、工具和勒索软件行为方面存在重叠。

“Interlock可能隶属于Rhysida的操作者或开发者，这与网络威胁领域的几大趋势相吻合，”该公司说。“我们观察到，勒索软件组织的能力正在多样化，以支持更先进、更多样的操作，勒索软件组织的孤岛化程度也在降低，因为我们观察到，操作人员越来越多地与多个勒索软件组织合作。”

在 Helldown 和 Interlock 出现的同时，另一个名为 SafePay 的勒索软件也加入了勒索软件生态系统。根据 Huntress 的说法，SafePay 也使用 LockBit 3.0 作为基础，这表明 LockBit 源代码的泄露已经催生了多个变种。

在该公司调查的两起事件中，“发现威胁行为者的活动源自 VPN 网关或门户，因为所有观察到的分配给威胁行为者工作站的 IP 地址都在内部范围内，”Huntress 研究人员说。

Huntress 研究人员说：“威胁行为者能够使用有效凭证访问客户端点，而且没有观察到启用 RDP、创建新用户账户或创建任何其他持久性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302098](/post/id/302098)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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