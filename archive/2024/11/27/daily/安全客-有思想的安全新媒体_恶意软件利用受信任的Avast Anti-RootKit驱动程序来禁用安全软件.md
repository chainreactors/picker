---
title: 恶意软件利用受信任的Avast Anti-RootKit驱动程序来禁用安全软件
url: https://www.anquanke.com/post/id/302192
source: 安全客-有思想的安全新媒体
date: 2024-11-27
fetch_date: 2025-10-06T19:12:18.939494
---

# 恶意软件利用受信任的Avast Anti-RootKit驱动程序来禁用安全软件

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

# 恶意软件利用受信任的Avast Anti-RootKit驱动程序来禁用安全软件

阅读量**74050**

发布时间 : 2024-11-26 14:24:17

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/malware-avast-anti-rootkit-driver-bypass-security/>

译文仅供参考，具体内容表达以及含义原文为准。

恶意软件利用合法的 Avast 反 rootkit 驱动程序禁用安全软件。Trellix 研究人员发现了这一攻击并提供了缓解步骤。

摘要：

* 恶意软件利用合法的 Avast Anti-Rootkit 驱动程序获得内核级访问权限。
* 驱动程序被用来终止关键安全进程并夺取系统的控制权。
* BYOVD（自带漏洞驱动程序）保护机制可防止基于驱动程序的攻击。
* 可以部署专家规则来识别和阻止易受攻击的驱动程序。

Trellix 的网络安全研究人员发现了一种恶意活动，它利用合法的 Avast Anti-Rootkit 驱动程序 aswArPot.sys 来禁用安全软件并控制受感染的系统。

**攻击如何运作：**

该恶意软件被称为 “kill-floor.exe”，它首先将 aswArPot.sys 驱动程序放入一个看似无害的 Windows 目录，并将其伪装成 “ntfs.bin”。然后，它将驱动程序注册为服务，授予恶意软件内核级访问权限–这是系统权限的最高级别，允许它终止关键安全进程并控制系统。

![Malware Exploits Avast Anti-Rootkit Driver to Bypass Security Software]()
该恶意软件包含一个硬编码的 142 个安全应用程序列表，它的目标是终止这些应用程序。恶意软件持续监控活动进程，并将其与该列表进行比较。当发现匹配时，恶意软件会使用 Avast Anti-Rootkit 驱动程序终止安全进程。

简单地说：Avast 驱动程序旨在清除恶意 rootkit，却无意中禁用了合法的安全软件。恶意软件利用这个可信的驱动程序来躲避检测，并在系统中悄无声息地运行。

**技术分析**

Trellix 对 Avast 驱动程序的技术分析揭示了负责终止安全进程的特定函数 “FUN\_14001dc80”。该函数利用标准的 Windows 内核函数（KeAttachProcess 和 ZwTerminateProcess）进行终止，进一步将恶意活动掩盖为正常的系统操作。

**自我保护**

为防止此类基于驱动程序的攻击，Trellix 建议使用 BYOVD（自带脆弱驱动程序）保护机制。这些机制可以根据独特的签名或哈希值识别并阻止特定的易受攻击驱动程序。

一旦将这些规则集成到防病毒解决方案中，企业就能防止恶意软件利用合法驱动程序、提升权限或禁用安全措施。Trellix 还提供了一个特定的 BYOVD 专家规则，用于检测和阻止对 aswArPot.sys 驱动程序的恶意使用。

本文翻译自hackread [原文链接](https://hackread.com/malware-avast-anti-rootkit-driver-bypass-security/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302192](/post/id/302192)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/malware-avast-anti-rootkit-driver-bypass-security/)

如若转载,请注明出处： <https://hackread.com/malware-avast-anti-rootkit-driver-bypass-security/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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