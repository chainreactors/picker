---
title: 黑客利用 Linux eBPF 持续传播恶意软件
url: https://www.anquanke.com/post/id/302837
source: 安全客-有思想的安全新媒体
date: 2024-12-20
fetch_date: 2025-10-06T19:36:00.246432
---

# 黑客利用 Linux eBPF 持续传播恶意软件

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

# 黑客利用 Linux eBPF 持续传播恶意软件

阅读量**111440**

|评论**1**

发布时间 : 2024-12-19 10:13:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/hackers-exploit-linux-ebpf-tech-malware-github-blogs/>

译文仅供参考，具体内容表达以及含义原文为准。

**要点概述**

* **新的 Linux 恶意软件活动**： 网络安全研究人员发现了一个利用 eBPF 技术、针对全球企业和用户的活跃 Linux 恶意软件活动。
* **eBPF 漏洞利用**： 黑客正在滥用 eBPF 的低级功能来隐藏活动、收集数据和绕过安全措施，从而使检测变得困难。
* **木马部署**： 攻击者利用 eBPF rootkit 隐藏自己的存在，并投放远程访问木马，这些木马能够在专用网络内传输流量并保持通信。
* **指挥控制公共平台**： 恶意软件配置不存储在专用服务器上，而是存储在 GitHub 和博客等公共平台上，将恶意活动伪装成合法活动。
* **正在兴起的 eBPF 恶意软件**： 基于 eBPF 的恶意软件（包括 Boopkit 和 BPFDoor 等系列）的使用正在增加，仅在 2024 年就发现了 100 多个新漏洞。

网络安全研究人员 Dr. Web 发现了一个针对东南亚企业和用户的新的活跃 Linux 恶意软件活动。这一发现是在对他们的一个客户报告的恶意软件攻击进行调查时发现的。

调查开始时，一位客户向 Dr. Web 表示担心他们的计算机基础设施可能受到攻击。在对客户的数据进行分析后，Dr. Web 发现了多个类似案例，表明这是一个大规模的活跃攻击活动。尽管最初不确定攻击者是如何获得访问权限的，但研究人员成功追踪到了攻击的初始阶段。

**利用 eBPF 技术**

研究人员发现，黑客在攻击中一直在滥用 eBPF（扩展的伯克利数据包过滤器）技术。eBPF 的设计初衷是为了更好地控制 Linux 操作系统的网络功能。

值得注意的是，围绕 eBPF 的关注度越来越高，尤其是在 2021 年 8 月之后，谷歌、Isovalent、Meta、微软和 Netflix 等科技巨头合作在 Linux 基金会下成立了 eBPF 基金会，以支持 eBPF 技术的发展和应用。

然而，在目前的攻击中，eBPF 的低级功能使攻击者得以隐藏网络活动、收集敏感信息并绕过安全措施。这使研究人员难以发现，也为黑客提供了有利可图的机会，特别是对那些希望长期访问目标系统的高级持续威胁（APT）组织而言。

Web 博士在 12 月 10 日发布的报告中详细介绍了这一特定活动，攻击者利用 eBPF 加载了两个 rootkit。第一个 eBPF rootkit 隐藏了第二个 rootkit 的存在，而第二个 rootkit 则投放了一个远程访问木马（Trojan.Siggen28.58279 或 Trojan:Win32/Siggen.GR!MTB），该木马具有隧道流量功能，允许攻击者甚至在专用网络内与受感染设备通信。

**隐藏在众目睽睽之下： 公共平台作为指挥中心**

威胁者还改变了存储恶意软件配置的方式。他们不再依赖私有的指挥控制服务器，而是使用流行的、可公开访问的平台。

网络博士分析的恶意软件被发现从 GitHub 等平台甚至中国的一个网络安全博客中检索设置。这种策略使恶意流量看起来合法，因为它与正常的网络活动结合在一起。它还使攻击者无需维护独立的控制基础设施，从而更容易被发现和关闭。

![Hackers Exploit Linux eBPF Tech to Host Malware on GitHub and Blogs]()
截图显示恶意软件托管在 GitHub 和一个网络安全中文博客上（Via Dr. Web）

然而，自 2023 年以来，恶意 eBPF 软件的使用呈上升趋势，出现了多个恶意软件家族，包括 Boopkit、BPFDoor 和 Symbiote。eBPF 技术中大量漏洞的发现使情况进一步恶化。

这次持续不断的网络攻击再次表明，政府支持的黑客和网络犯罪分子可以无所顾忌。他们的策略，包括利用 eBPF 等先进技术和使用公共平台进行配置存储，都清楚地表明了这一点。

本文翻译自hackread [原文链接](https://hackread.com/hackers-exploit-linux-ebpf-tech-malware-github-blogs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302837](/post/id/302837)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-exploit-linux-ebpf-tech-malware-github-blogs/)

如若转载,请注明出处： <https://hackread.com/hackers-exploit-linux-ebpf-tech-malware-github-blogs/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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