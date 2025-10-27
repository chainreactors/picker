---
title: FINALDRAFT 恶意软件：借 Outlook 草稿为通道的跨平台间谍威胁
url: https://www.anquanke.com/post/id/304374
source: 安全客-有思想的安全新媒体
date: 2025-02-18
fetch_date: 2025-10-06T20:36:09.735099
---

# FINALDRAFT 恶意软件：借 Outlook 草稿为通道的跨平台间谍威胁

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

# FINALDRAFT 恶意软件：借 Outlook 草稿为通道的跨平台间谍威胁

阅读量**53992**

发布时间 : 2025-02-17 10:31:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/finaldraft-malware-exploits-outlook-drafts-for-covert-communication/>

译文仅供参考，具体内容表达以及含义原文为准。

![FINALDRAFT Malware]()

来源：Elastic 安全实验室

在最近对 REF7707 入侵组织的调查中，Elastic 安全实验室发现了一个新的恶意软件家族，该家族利用微软 Outlook 的草稿功能，通过微软图形 API（Microsoft Graph API）作为隐蔽的通信渠道。这个被称为 “最终草稿（FINALDRAFT）” 的攻击后利用工具包由一个加载器、一个后门程序以及多个为高级网络间谍活动设计的子模块组成。

Elastic 团队发现了该恶意软件的 Windows 和 Linux 版本，有证据表明它经过了长期开发，并且投入了大量的工程精力。Elastic 安全实验室指出：“这些工具的完备性以及所涉及的工程水平表明，开发者组织有序。” 并补充道，“从该活动的时间跨度以及我们的监测数据来看，这很可能是一场以间谍活动为目的的行动。”

![]()

“路径加载器（PATHLOADER）” 与 “最终草稿（FINALDRAFT）” 执行流程图 | 来源：Elastic 安全实验室

“最终草稿” 恶意软件通过 “路径加载器（PATHLOADER）” 进行部署，这是一个轻量级的 Windows PE 可执行文件（206 KB），作为第一阶段加载器。它从攻击者控制的基础设施下载经过 AES 加密的外壳代码，对其进行解密，然后在内存中执行。该恶意软件通过 API 哈希、混淆和沙箱逃避技术来躲避静态分析。
Elastic 安全实验室强调了 “路径加载器” 嵌入的配置中包含两个模仿安全厂商的拼写错误域名：

1.poster.checkponit [.] com（对 Check Point 的欺骗性模仿）

2.support.fortineat [.] com（模仿 Fortinet）

这种欺骗策略旨在逃避检测，并将恶意流量与合法的安全厂商活动混在一起。

“最终草稿” 是一款用 C++ 编写的 64 位恶意软件，主要侧重于数据窃取和进程注入。它通过加载加密配置、生成会话 ID，并通过 Outlook 草稿与命令控制（C2）服务器进行交互来运行。

报告解释称：“‘最终草稿’与命令控制服务器之间通信所使用的会话 ID 是通过创建一个随机的全局唯一标识符（GUID）生成的，然后使用福勒 – 诺尔 – 沃（Fowler-Noll-Vo，FNV）哈希函数对其进行处理。”

“最终草稿” 的一个显著特点是它能够利用 Outlook 的邮件草稿作为命令控制通道。该恶意软件不进行直接的网络通信，而是：

1.如果不存在会话草稿邮件，则创建一个。

2.读取并删除攻击者生成的命令请求草稿。

3.执行命令，如进程注入、文件操作和网络代理。

4.将响应内容写为草稿邮件，确保攻击者能够在不引起警觉的情况下获取结果。

这种方法最大限度地减少了网络流量痕迹，使得传统安全解决方案更难检测到它。

“最终草稿” 包含 37 个命令处理程序，使其能够执行进程注入、TCP/UDP 代理、文件操作和权限提升等操作。值得注意的是，该恶意软件的进程注入技术依赖于 VirtualAllocEx、WriteProcessMemory 和 RtlCreateUserThread 等 API 调用。

报告指出：“目标进程要么是作为命令参数提供的可执行文件路径，要么默认使用 mspaint.exe 或 conhost.exe 作为备用选项。”

除了在 Windows 系统上的功能外，“最终草稿” 的 ELF 版本也被发现，它支持除 Outlook 草稿之外的多种命令控制传输协议，包括：

1.HTTP/HTTPS

2.反向 UDP

3.ICMP 和绑定 TCP

4.反向 TCP 和 DNS

这表明它具有跨平台适应性，使 “最终草稿” 成为攻击者针对 Windows 和 Linux 环境的多功能工具。

Elastic 安全实验室强烈怀疑 “最终草稿” 是一场更大规模间谍活动的一部分。该恶意软件复杂的设计、持久化技术以及对隐蔽通信方法的依赖，表明其背后是一个资金雄厚且能力极强的对手。

安全研究人员敦促各组织监控 Outlook API 的活动，实施强大的端点检测解决方案，并屏蔽已知的命令控制域名，以降低风险。

本文翻译自securityonline [原文链接](https://securityonline.info/finaldraft-malware-exploits-outlook-drafts-for-covert-communication/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304374](/post/id/304374)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/finaldraft-malware-exploits-outlook-drafts-for-covert-communication/)

如若转载,请注明出处： <https://securityonline.info/finaldraft-malware-exploits-outlook-drafts-for-covert-communication/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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