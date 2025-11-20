---
title: Windows 11 新增云重建与时间点还原系统恢复工具
url: https://www.anquanke.com/post/id/313271
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:13.516630
---

# Windows 11 新增云重建与时间点还原系统恢复工具

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

# Windows 11 新增云重建与时间点还原系统恢复工具

阅读量**23941**

发布时间 : 2025-11-19 17:41:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/windows-11-gets-new-cloud-rebuild-point-in-time-restore-tools/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软在今日的 Ignite 开发者大会上宣布了 Windows 11 的两项新恢复功能，名为 **Cloud Rebuild（云重建）** 和 **Point-in-Time Restore（PITR，时间点恢复）**，旨在减少停机时间，并简化系统故障或错误更新后的恢复流程。

这两项新恢复功能是微软 **Windows Resiliency Initiative（Windows 弹性计划）** 的一部分，旨在帮助组织在设备无法启动或正常运行时快速恢复设备。

### Point-in-Time Restore（PITR）

第一项功能 **时间点恢复（PITR）** 允许用户和 IT 管理员在几分钟内将 Windows 11 系统回滚到 earlier、健康的快照。

与系统还原类似，PITR 可将操作系统、其设置和系统文件恢复到先前存储的状态。但 **时间点恢复在系统还原功能的基础上进行了增强**，它会在不同时间点拍摄系统的完整快照，因此还可以恢复本地文件和应用程序。

微软表示，该功能将于本周在即将发布的 Windows 11 Insider 预览版中进入预览阶段。

### Cloud Rebuild（云重建）

微软还推出了 **Cloud Rebuild（云重建）**，这是一种可远程触发从云端完全重新安装 Windows 11 的工具，适用于遇到持续问题或无法运行的设备。

微软解释道：“通过 Intune 门户，管理员可以选择所需的 Windows 版本和语言，触发电脑下载安装介质并自行重建。”

“该过程利用 Autopilot 实现零接触配置，确保重建后 MDM 注册和策略合规性。通过 OneDrive 和 Windows Backup for Organizations，用户数据和设置的恢复流程得到简化。这种方法将把停机时间从几小时或几天减少到其中的一小部分。”

### 集成与未来计划

微软表示，这两项功能都将在 **2026 年上半年直接集成到 Microsoft Intune 中**，使 Windows 管理员能够远程触发恢复操作、协调企业范围的修复，并直接从 Intune 控制 Windows 恢复环境（WinRE）功能。

本月早些时候，微软开始测试 **Quick Machine Recovery（QMR，快速机器恢复）** 的更新版本，这是一种旨在帮助管理员解决 Windows 启动故障的工具，无需物理访问设备。

![]()

当 Windows 11 遇到由配置更改、有问题的驱动器或更新导致的启动故障时，它将自动启动 Windows 恢复环境，加载 QMR，并将崩溃信息发送给微软。

基于对这些数据的分析，微软可以远程应用修复，例如删除有问题的驱动程序或更新，以及更改配置设置。

微软表示，最新版本改进了 QMR 启动修复流程，通过执行 **单次扫描来检测和解决问题**，而不是循环重复搜索解决方案。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/windows-11-gets-new-cloud-rebuild-point-in-time-restore-tools/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313271](/post/id/313271)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/windows-11-gets-new-cloud-rebuild-point-in-time-restore-tools/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/windows-11-gets-new-cloud-rebuild-point-in-time-restore-tools/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10
* ##### [macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词](/post/id/313255)

  2025-11-19 17:39:45
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员](/post/id/313249)

  2025-11-19 17:37:58
* ##### [SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过](/post/id/313245)

  2025-11-19 17:37:15

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