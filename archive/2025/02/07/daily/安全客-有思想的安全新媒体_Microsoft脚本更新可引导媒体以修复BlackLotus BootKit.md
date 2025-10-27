---
title: Microsoft脚本更新可引导媒体以修复BlackLotus BootKit
url: https://www.anquanke.com/post/id/303889
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:42.564164
---

# Microsoft脚本更新可引导媒体以修复BlackLotus BootKit

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

# Microsoft脚本更新可引导媒体以修复BlackLotus BootKit

阅读量**521158**

发布时间 : 2025-02-06 14:45:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/new-microsoft-script-updates-windows-media-with-bootkit-malware-fixes/>

译文仅供参考，具体内容表达以及含义原文为准。

![Windows logo]()

微软发布了一个 PowerShell 脚本，以帮助 Windows 用户和管理员更新可引导介质，以便在今年晚些时候针对 BlackLotus UEFI 引导工具包的缓解措施实施之前，让可引导介质使用新的 “Windows UEFI CA 2023” 证书。

BlackLotus 是一种 UEFI 引导工具包，能够绕过安全启动（Secure Boot）并控制操作系统的启动过程。一旦获得控制权，BlackLotus 可以禁用 Windows 安全功能，如 BitLocker、基于虚拟机监控程序的代码完整性（HVCI）以及微软 Defender 防病毒软件，从而使其能够在最高权限级别部署恶意软件且不被察觉。

2023 年 3 月以及 2024 年 7 月，微软针对一个被追踪为 CVE – 2023 – 24932 的安全启动绕过漏洞发布了安全更新，该更新撤销了 BlackLotus 所使用的存在漏洞的引导管理器。然而，此修复默认处于禁用状态，因为错误地应用更新或设备上出现冲突可能导致操作系统无法再加载。相反，分阶段推出修复措施可让 Windows 管理员在 2026 年之前某个时间强制实施该修复之前对其进行测试。

启用后，该安全更新会将 “Windows UEFI CA 2023” 证书添加到 UEFI 的 “安全启动签名数据库” 中。然后，管理员可以安装使用此证书签名的更新版本引导管理器。

这个过程还包括更新安全启动禁止签名数据库（DBX），以添加 “Windows Production CA 2011” 证书。此证书用于对较旧的、存在漏洞的引导管理器进行签名，一旦被撤销，这些引导管理器将变得不可信且无法加载。

但是，如果应用缓解措施后设备启动出现问题，你必须首先更新可引导介质，以使用 Windows UEFI CA 2023 证书来解决 Windows 安装过程中的故障。微软在一份关于 CVE – 2023 – 24932 修复措施分阶段推出的支持公告中解释道：“如果在应用缓解措施后设备出现问题且无法启动，你可能无法从现有介质启动或恢复设备。恢复或安装介质需要更新，以便在已应用缓解措施的设备上正常使用。”

昨天，微软发布了一个 PowerShell 脚本，帮助你更新可引导介质，使其使用 Windows UEFI CA 2023 证书。

![Script to apply CVE-2023-24932 mitigations to bootable Windows media]()

用于将 CVE – 2023 – 24932 缓解措施应用于可引导 Windows 介质的脚本
来源：BleepingCompute

一份关于该脚本的新支持公告解释说：“本文所述的 PowerShell 脚本可用于更新 Windows 可引导介质，以便该介质可在信任 Windows UEFI CA 2023 证书的系统上使用。”

该 PowerShell 脚本可从微软下载，可用于更新 ISO CD/DVD 镜像文件、USB 闪存驱动器、本地驱动器路径或网络驱动器路径的可引导介质文件。

要使用此工具，你必须首先下载并安装 Windows ADK，这是此脚本正确运行所必需的。

运行该脚本时，它将更新介质文件以使用 Windows UEFI CA 2023 证书，并安装使用此证书签名的引导管理器。

强烈建议 Windows 管理员在安全更新进入强制实施阶段之前测试此过程。微软表示这将在 2026 年底前完成，并将在开始前提前六个月发出通知。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-script-updates-windows-media-with-bootkit-malware-fixes/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303889](/post/id/303889)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/new-microsoft-script-updates-windows-media-with-bootkit-malware-fixes/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/new-microsoft-script-updates-windows-media-with-bootkit-malware-fixes/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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