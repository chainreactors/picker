---
title: 安全外联实验室公布 “Windows 降级” 新攻击方法
url: https://www.anquanke.com/post/id/301312
source: 安全客-有思想的安全新媒体
date: 2024-10-29
fetch_date: 2025-10-06T18:49:04.713893
---

# 安全外联实验室公布 “Windows 降级” 新攻击方法

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

# 安全外联实验室公布 “Windows 降级” 新攻击方法

阅读量**62549**

发布时间 : 2024-10-28 11:02:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/hackers-downgrade-windows-exploit-patched-flaws/>

译文仅供参考，具体内容表达以及含义原文为准。

**安全外联实验室（SafeBreach Labs）公布了 “Windows降级 ”新攻击方法，该方法可通过降级系统组件和恢复DSE绕过等旧/打过补丁的漏洞来破坏Windows 11。**

在最近的一项研究中，SafeBreach 实验室的研究员 Alon Leviev 曝光了一种新的攻击技术，这种技术可能会危及已打补丁的 Windows 11 系统的安全。这种技术被称为 “Windows 降级”（Windows Downdate），涉及操纵 Windows 更新进程来降级关键系统组件，从而有效地复活先前已打补丁的漏洞。

该攻击最初于 2024 年 8 月在 Black Hat USA 2024 和 DEF CON 32 上报告。研究人员现在公布了更多细节，以加深公众对该攻击的了解。

其中一个漏洞是 “ItsNotASecurityBoundary ”驱动程序签名执行（DSE）绕过，允许攻击者加载未签名的内核驱动程序。该绕过漏洞允许攻击者用恶意版本替换已验证的安全目录，从而加载未签名的内核驱动程序。

根据SafeBreach在周六发布之前与Hackread.com共享的博文，通过利用Windows降级，攻击者可以锁定特定组件，如解析安全目录所必需的 “ci.dll ”模块，并将其降级到易受攻击的状态，从而利用这一旁路并获得内核级权限。

需要说明的是，“ItsNotASecurityBoundary ”DSE旁路属于一类新漏洞，被称为 “虚假文件不变性”（FFI），它利用了对文件不变性的不正确假设，允许通过清除系统工作集来修改 “不可变 ”文件。

Leviev 概述了在具有不同级别虚拟化安全（VBS）保护的 Windows 系统中利用漏洞的步骤。他们确定了多种禁用 VBS 关键功能的方法，包括凭证防护（Credential Guard）和管理程序保护代码完整性（HVCI）等功能，甚至首次使用了 UEFI 锁。

“据我所知，这是第一次在没有物理访问的情况下绕过 VBS 的 UEFI 锁。因此，我能够让一台打了完全补丁的 Windows 机器易受过去漏洞的影响，使已修复的漏洞变成未修复的漏洞，并使 “打了完全补丁 ”这一术语在世界上任何一台 Windows 机器上变得毫无意义。”

阿隆-列维夫

要利用没有 UEFI 锁的系统，攻击者必须通过修改注册表设置来禁用 VBS。一旦禁用，他们就可以将 ci.dll 模块降级到有漏洞的版本，并利用 “ItsNotASecurityBoundary ”漏洞。

对于带有 UEFI 锁的系统，攻击者必须使 SecureKernel.exe 文件失效，才能绕过 VBS 保护。然而，带有 UEFI 锁和 “强制 ”标志的 VBS 是最安全的配置，即使锁被绕过，VBS 也不会被禁用。研究人员解释说，目前还没有已知的方法可以在没有物理访问的情况下利用具有这种保护级别的系统。

尽管如此，这种 Windows Update 接管功能仍对企业构成了重大威胁，因为它允许攻击者加载未签名的内核驱动程序、启用自定义 rootkit 以解除安全控制、隐藏进程并保持隐身。

攻击者可以对关键操作系统组件（包括 DLL、驱动程序甚至 NT 内核）进行自定义降级。通过降级这些组件，攻击者可以暴露以前修补过的漏洞，使系统容易被利用。

为降低风险，企业应及时为系统更新最新的安全补丁，以解决漏洞问题。必须部署强大的端点检测和响应（EDR）解决方案，以检测和响应恶意活动，包括降级尝试，并实施强大的网络安全措施，防止未经授权的访问和数据泄露。此外，使用 UEFI 锁定和 “强制 ”标志启用 VBS 还能提供额外的保护，防止攻击。

本文翻译自hackread [原文链接](https://hackread.com/hackers-downgrade-windows-exploit-patched-flaws/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301312](/post/id/301312)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-downgrade-windows-exploit-patched-flaws/)

如若转载,请注明出处： <https://hackread.com/hackers-downgrade-windows-exploit-patched-flaws/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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