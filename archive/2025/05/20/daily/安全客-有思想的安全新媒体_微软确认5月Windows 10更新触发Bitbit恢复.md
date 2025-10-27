---
title: 微软确认5月Windows 10更新触发Bitbit恢复
url: https://www.anquanke.com/post/id/307519
source: 安全客-有思想的安全新媒体
date: 2025-05-20
fetch_date: 2025-10-06T22:23:50.299738
---

# 微软确认5月Windows 10更新触发Bitbit恢复

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

# 微软确认5月Windows 10更新触发Bitbit恢复

阅读量**63720**

发布时间 : 2025-05-19 16:11:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 塞尔吉乌·加特兰，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-may-windows-10-updates-trigger-bitlocker-recovery/>

译文仅供参考，具体内容表达以及含义原文为准。

![微软]()

微软已经确认,一些Windows 10和Windows 10 Enterprise LTSC 2021系统将在安装2025年5月的安全更新后启动BitLocker恢复。

BitLocker Windows安全功能加密存储驱动器以防止数据被盗,Windows计算机通常在TPM(可信平台模块)更新或硬件更改等事件后进入BitLocker恢复模式,以重新获得对受保护驱动器的访问。

今天,微软证实了这个问题,并表示正在调查有关“少数”Windows 10 PC在安装KB5058379更新后显示BitLocker恢复屏幕的报道。

在受影响的设备上,在安装更新时,Windows可能无法启动足够的时间来触发自动修复。在启用了BitLocker的设备上,BitLocker需要输入BitLocker恢复密钥才能启动自动修复,[“该公司在Windows版本健康更新中说。](https://learn.microsoft.com/en-us/windows/release-health/status-windows-10-22h2#windows-10-might-repeatedly-display-the-bitlocker-recovery-screen-at-startup)

检查 Windows 事件查看器的受影响用户还将在系统事件日志中看到带有 0x800F0845 错误的 LSASS 错误和安装故障事件。此外,虽然一些设备在启动修复无法启动自动修复后将进入BitLocker恢复循环,但其他设备将在多次尝试安装KB5058379后成功回滚到之前安装的更新。

您可以通过 Microsoft 帐户登录 [BitLocker](https://account.microsoft.com/devices/recoverykey) 恢复屏幕门户来检索 BitLocker 恢复密钥。[support page](http://support.microsoft.com/windows/finding-your-bitlocker-recovery-key-in-windows-6b71ad27-0b89-ea08-f143-056f5ab347d6)此支持页面提供了有关如何在 Windows 中找到恢复密钥的更多详细信息。

微软表示正在调查这个问题,一旦有关根本原因的更多信息可用,它将提供更新。

![BitLocker 恢复屏幕]()

*BitLocker 恢复屏幕(Microsoft)*

微软承认这个问题之前,[许多Windows用户和管理员报告说](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5058379-update-triggering-bitlocker-recovery-after-install/),在安装了作为2025年5月补丁星期二的一部分发布的KB5058379累积更新后,看到设备意外进入Windows恢复环境(WinRE)[KB5058379 cumulative update](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5058379-update-fixes-sgrmbroker-errors-in-event-viewer/)[May 2025 Patch Tuesday](https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2025-patch-tuesday-fixes-5-exploited-zero-days-72-flaws/)并显示BitLocker恢复屏幕。

目前,这些报告指出,联想、戴尔和惠普的各种系统配置和设备都受到了影响,因此目前还不清楚这是否是由特定的硬件或软件问题引起的。

5月13日发布的最新KB5058379质量更新在Windows 10设备中失败。重新启动后,它导致触发了触发了bitlocker键窗口的一些设备[Microsoft’s forums](https://answers.microsoft.com/en-us/windows/forum/all/may-13-kb5058379-windows-10-leads-to-corruption/58b3b179-70a0-4bd8-abae-c9b89dd9c9b9),”一位用户在微软的论坛上说。

“我们有大约六款笔记本电脑在收到相同的KB后经历了各种间歇性问题 – 有些需要bitlocker键才能启动,其他笔记本电脑则拒绝启动[Reddit](https://old.reddit.com/r/sysadmin/comments/1klcpkl/patch_tuesday_megathread_20250513/ms7rei0/),”Windows管理员在Reddit上补充道。

要在 BitLocker 恢复提示符卡住的系统上返回 Windows,您可以尝试从 BIOS 禁用英特尔可信执行技术 (TXT)。如果失败,如 [Microsoft 支持建议](https://www.reddit.com/r/sysadmin/comments/1klcpkl/patch_tuesday_megathread_20250513/msb8rny/),您还可以尝试禁用安全引导、虚拟化技术(如果问题仍然存在)或固件保护。

2024年8月,微软修复了另一个在安装2024年7月Windows安全更新后,在Windows 10、Windows 11和Windows [Server系统上触发BitLocker恢复提示的问题。](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-issue-that-sent-pcs-into-bitlocker-recovery/)[installing the July 2024 Windows security updates](https://www.bleepingcomputer.com/news/microsoft/windows-july-security-updates-send-pcs-into-bitlocker-recovery/)

两年前,即2022年8月,[在KB5012170安全更新导致一些设备启动到BitLocker恢复屏幕后](https://www.reddit.com/r/pcmasterrace/comments/wkqkmg/is_the_windows_update_kb5012170_safe_to_install/),Windows设备受到类似问题的影响。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-may-windows-10-updates-trigger-bitlocker-recovery/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307519](/post/id/307519)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-may-windows-10-updates-trigger-bitlocker-recovery/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-may-windows-10-updates-trigger-bitlocker-recovery/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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