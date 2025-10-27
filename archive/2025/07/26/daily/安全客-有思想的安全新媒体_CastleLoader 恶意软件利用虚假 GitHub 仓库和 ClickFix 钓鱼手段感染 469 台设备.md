---
title: CastleLoader 恶意软件利用虚假 GitHub 仓库和 ClickFix 钓鱼手段感染 469 台设备
url: https://www.anquanke.com/post/id/310566
source: 安全客-有思想的安全新媒体
date: 2025-07-26
fetch_date: 2025-10-06T23:16:41.606515
---

# CastleLoader 恶意软件利用虚假 GitHub 仓库和 ClickFix 钓鱼手段感染 469 台设备

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

# CastleLoader 恶意软件利用虚假 GitHub 仓库和 ClickFix 钓鱼手段感染 469 台设备

阅读量**83277**

发布时间 : 2025-07-25 16:58:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/07/castleloader-malware-infects-469.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员揭示了一种名为**CastleLoader**的新型多功能恶意软件加载器，该加载器已被用于分发多种信息窃取工具和远程访问木马（RAT）等恶意软件。

瑞士网络安全公司PRODAFT在向《The Hacker News》分享的报告中指出，该恶意活动利用了以Cloudflare为主题的ClickFix网络钓鱼攻击以及伪造的GitHub仓库，这些仓库**冒充合法应用程序的名称进行发布**。

CastleLoader首次在今年早些时候被发现，其**被用于传播DeerStealer、RedLine、StealC、NetSupport RAT、SectopRAT**，甚至包括其他加载器如Hijack Loader。

该公司表示：“它采用了死代码注入和加壳技术以阻碍分析。”恶意软件在运行时自我解包后，会连接至命令与控制（C2）服务器，下载目标模块并执行。

CastleLoader的模块化结构使其既能作为交付机制，也能作为预备工具，允许攻击者**将初始感染与有效载荷的部署分开**。这种分离增加了追踪和响应的难度，因为感染途径与最终恶意行为脱钩，使攻击者能更灵活地调整攻击活动。

CastleLoader的有效载荷以**可移植执行文件（PE文件）**的形式分发，内部包含嵌入的shellcode。该shellcode随后调用加载器的主模块，主模块再连接到命令与控制（C2）服务器，以获取并执行后续阶段的恶意软件。

分发该恶意软件的攻击主要依赖广泛流行的**ClickFix技术**，这些攻击利用伪装成软件开发库、视频会议平台、浏览器更新通知或文档验证系统的恶意域名，诱骗用户复制并执行PowerShell命令，从而激活感染链。

受害者通常通过谷歌搜索被引导至这些假冒域名，页面上展示的是由攻击者设计的伪造错误信息和验证码验证框，要求用户按照一系列指示操作，以“解决问题”为由诱导其执行恶意操作。

![]()

CastleLoader还利用伪造的GitHub仓库作为传播途径，这些仓库模仿合法工具，导致用户在不知情的情况下下载后感染恶意软件，从而使其设备遭受攻击。

“这一手法利用了**开发者对GitHub的信任**，以及他们倾向于从看似可信的仓库运行安装命令的习惯，”瑞士安全公司PRODAFT表示。

这种策略性滥用社交工程技术，与初始访问经纪人（IAB）常用的手法类似，凸显了CastleLoader在更大网络犯罪供应链中的角色。

PRODAFT还观察到，Hijack Loader通过**DeerStealer和CastleLoader**传播，后者也在传播DeerStealer的变种。这表明尽管这些活动由不同的威胁行为者操控，但其行动存在重叠。

自2025年5月以来，CastleLoader相关攻击活动共使用了七个不同的C2（命令与控制）服务器，在此期间共记录到1,634次感染尝试。通过对其C2基础设施及其基于Web的管理面板（用于监控和控制感染情况）的分析发现，**共有469台设备被成功感染，感染率达28.7%**。

研究人员还观察到该恶意加载器具备**反沙箱（anti-sandbox）和代码混淆功能**——这类功能通常出现在SmokeLoader或IceID等高级加载器中。结合对PowerShell的滥用、GitHub仿冒以及动态解包等手段，CastleLoader反映出当前恶意软件加载器趋向隐蔽化的演进趋势，其主要作用是在“恶意软件即服务”（Malware-as-a-Service, MaaS）生态系统中充当初始投递平台。

PRODAFT指出：“CastleLoader是一个新出现且仍在活跃传播的威胁，已被多个恶意攻击行动迅速采用，用于部署多种加载器和信息窃取器。其复杂的反分析机制与多阶段感染流程，突显了其在当前威胁格局中作为初始传播工具的高效性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/07/castleloader-malware-infects-469.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310566](/post/id/310566)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/07/castleloader-malware-infects-469.html)

如若转载,请注明出处： <https://thehackernews.com/2025/07/castleloader-malware-infects-469.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**8赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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