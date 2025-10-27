---
title: ESET Research 发现了首个专为 Linux 系统设计的 UEFI 引导工具包 Bootkitty
url: https://www.anquanke.com/post/id/302267
source: 安全客-有思想的安全新媒体
date: 2024-11-29
fetch_date: 2025-10-06T19:14:43.519571
---

# ESET Research 发现了首个专为 Linux 系统设计的 UEFI 引导工具包 Bootkitty

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

# ESET Research 发现了首个专为 Linux 系统设计的 UEFI 引导工具包 Bootkitty

阅读量**61932**

发布时间 : 2024-11-28 15:05:22

**x**

##### 译文声明

本文是翻译文章，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/11/27/linux-uefi-bootkit-bootkitty/>

译文仅供参考，具体内容表达以及含义原文为准。

ESET Research 发现了首个专为 Linux 系统设计的 UEFI 引导工具包，其创建者将其命名为 Bootkitty。研究人员认为，这个引导工具包很可能只是一个初步的概念验证，根据 ESET 的遥测技术，它还没有在野外部署过。

![Linux UEFI bootkit]()

Bootkitty 执行概述（来源：ESET）

然而，这是 UEFI bootkit 不再局限于 Windows 系统的第一个证据。该引导工具包的主要目标是禁用内核的签名验证功能，并通过 Linux “init ”进程（Linux 内核在系统启动时执行的第一个进程）预加载两个未知的 ELF 二进制文件。

此前未知的 UEFI 应用程序名为 “bootkit.efi”，已被上传到 VirusTotal。Bootkitty 由自签名证书签名，因此无法在默认启用 UEFI 安全启动的系统上运行。不过，无论是否启用 UEFI 安全启动，Bootkitty 都能无缝启动 Linux 内核，因为它在内存中修补了负责完整性验证的必要功能。

Bootkitty 是一种先进的 rootkit，能够替换引导加载器，并在执行内核前打补丁。Bootkitty 允许攻击者完全控制受影响的计算机，因为它可以控制计算机的启动过程，并在操作系统启动之前执行恶意软件。

在分析过程中，ESET发现了一个可能相关的无签名内核模块，ESET将其命名为BCDropper，有迹象表明它可能是由Bootkitty的同一作者开发的。它部署了一个ELF二进制文件，负责加载另一个在分析时未知的内核模块。

“Bootkitty包含许多人工制品，这表明它更像是一个概念验证，而非威胁行为者的作品。”分析 Bootkitty 的 ESET 研究员 Martin Smolár 说：“尽管 VirusTotal 的当前版本目前还不能对大多数 Linux 系统构成真正的威胁，因为它只能影响几个 Ubuntu 版本，但它强调了为未来潜在威胁做好准备的必要性。”他补充说：“为了保证 Linux 系统免受此类威胁，请确保 UEFI 安全启动已启用，系统固件、安全软件和操作系统都是最新的，UEFI 撤销列表也是最新的。”

在 ESET 测试环境中用 Bootkitty 启动系统后，研究人员注意到内核被标记为污点（可使用命令检查污点值），而没有 Bootkitty 时则没有这种情况。在启用 UEFI 安全启动的系统中，判断引导工具包是否存在的另一种方法是在运行时尝试加载未签名的虚假内核模块。如果存在，模块将被加载；如果不存在，内核将拒绝加载。当 Bootkit 被部署为“/EFI/ubuntu/grubx64.efi ”时，摆脱 Bootkit 的简单方法是将合法的“/EFI/ubuntu/grubx64-real.efi ”文件移回其原始位置，即“/EFI/ubuntu/grubx64.efi”。

在过去的几年里，UEFI 威胁，尤其是 UEFI 引导程序的威胁，已经发生了很大的变化。这一切都始于 Andrea Allievi 在 2012 年描述的首个 UEFI 引导工具包概念验证（PoC），它是在基于 UEFI 的现代 Windows 系统上部署引导工具包的演示，之后又有许多其他 PoC（EfiGuard、Boot Backdoor、UEFI-bootkit）。

几年后，人们才在野外发现了前两个真正的 UEFI 引导工具包（其中一个是 ESET 于 2021 年发现的 ESPecter），又过了两年，臭名昭著的 BlackLotus（第一个能在最新系统上绕过 UEFI 安全引导的 UEFI 引导工具包）才出现（ESET 于 2023 年发现）。这些公开的引导工具包有一个共同点，即它们都专门针对 Windows 系统。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/11/27/linux-uefi-bootkit-bootkitty/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302267](/post/id/302267)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/11/27/linux-uefi-bootkit-bootkitty/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/11/27/linux-uefi-bootkit-bootkitty/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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