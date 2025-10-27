---
title: Windows 10紧急更新修复了MIDI恢复问题
url: https://www.anquanke.com/post/id/307671
source: 安全客-有思想的安全新媒体
date: 2025-05-23
fetch_date: 2025-10-06T22:27:00.629044
---

# Windows 10紧急更新修复了MIDI恢复问题

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

# Windows 10紧急更新修复了MIDI恢复问题

阅读量**64978**

发布时间 : 2025-05-22 15:33:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 塞尔吉乌·加特兰，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-fix-bitlocker-recovery-issues/>

译文仅供参考，具体内容表达以及含义原文为准。

![视窗]()

微软已经发布了带外更新,以修复导致Windows 10系统在安装2025年5月安全更新后启动BitLocker恢复的已知问题。

要修复卡在 BitLocker 恢复提示符下的系统,请安装今天的 KB5061768 紧急更新,仅通过 Microsoft 更新目录提供。这也是一个累积更新,这意味着在部署影响设备的 BitLocker 恢复问题修复之前,您无需安装任何先前的更新。

微软表示,这个已知的问题会影响运行Windows 10 22H2,Windows 10 Enterprise LTSCT 2021和Windows 10 IoT Enterprise LTSC 2021的系统,这些系统具有英特尔vPro处理器(第10代或更高版本),并启用了英特尔可信执行技术(TXT).

运行Windows 10的家庭和Pro版本的消费者设备也不太可能受到影响,因为家庭用户通常不使用英特尔vPro处理器。

“在这些系统上,安装2025年5月13日,Windows安全更新(KB5058379)可能会导致本地安全局子系统服务(LSASS)流程意外终止,触发自动修复提示BitLocker恢复密钥继续,[”该公司在今天发布的咨询中说。](https://support.microsoft.com/en-us/topic/may-19-2025-kb5061768-os-builds-19044-5856-and-19045-5856-out-of-band-75b27cbd-072e-4c5a-b40e-87e00aaa42dd#id0elbj=windows_10%2C_version_21h2)

如果无法立即安装 KB5061768 更新以恢复受影响的设备,Microsoft 建议在 BIOS/UEFI 设置中禁用 Intel VT for Direct I/O(又名 VTD 或 VTX)和英特尔可信执行技术 (TXT) 以在 BIOS/UEFI 设置中,并在安装更新后切换回来。

![BitLocker 恢复屏幕]()

*BitLocker 恢复屏幕(Microsoft)*

该公司承认了这个问题,此前Windows用户和管理员在进入Windows恢复环境(WinRE)后意外地显示了BitLocker恢复屏幕,[并安装了KB5058379累积更新](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5058379-update-fixes-sgrmbroker-errors-in-event-viewer/)[,](https://www.bleepingcomputer.com/news/microsoft/microsoft-may-2025-patch-tuesday-fixes-5-exploited-zero-days-72-flaws/)[作为2025年5月补丁星期二的一部分发布。](https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5058379-update-fixes-sgrmbroker-errors-in-event-viewer/)

根据Redmond的说法,在系统事件日志中查看Windows事件查看器的受影响用户可以看到带有0x800F0845错误的LSASS错误和安装故障事件。

“在受影响的设备上,在安装更新时,Windows可能无法启动足够的时间来触发自动修复[,”该公司在Windows版本健康更新中说。](https://learn.microsoft.com/en-us/windows/release-health/status-windows-10-22h2#windows-10-might-repeatedly-display-the-bitlocker-recovery-screen-at-startup)“在启用 BitLocker 的设备上,BitLocker 需要输入 BitLocker 恢复密钥才能启动自动修复。

2022年8月,Windows设备遭遇类似问题,[导致设备在安装KB5012170安全更新后启动到BitLocker恢复屏幕。](https://www.reddit.com/r/pcmasterrace/comments/wkqkmg/is_the_windows_update_kb5012170_safe_to_install/)

去年8月,[微软在安装2024年7月Windows安全更新后](https://www.bleepingcomputer.com/news/microsoft/windows-july-security-updates-send-pcs-into-bitlocker-recovery/)[,](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-issue-that-sent-pcs-into-bitlocker-recovery/)修复了Windows 10,Windows 11和Windows [Server系统上触发BitLocker恢复提示的另一个已知问题。](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-issue-that-sent-pcs-into-bitlocker-recovery/)

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-fix-bitlocker-recovery-issues/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307671](/post/id/307671)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-fix-bitlocker-recovery-issues/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/windows-10-emergency-updates-fix-bitlocker-recovery-issues/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [再添数字政府新名片！深圳“深治慧”平台入选2025数博会创新案例](/post/id/311777)

  2025-09-02 15:37:49
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/310525)

  2025-07-24 10:24:57
* ##### [ISC.AI 2025国际人工智能发展高峰论坛：凝聚全球共识，点亮AI未来](/post/id/310510)

  2025-07-24 09:47:17
* ##### [ISC.AI大咖来了——国家网络安全守卫者 周鸿祎](/post/id/310504)

  2025-07-24 09:43:28
* ##### [攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）](/post/id/310339)

  2025-07-21 17:41:39
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/309947)

  2025-07-11 16:10:36
* ##### [报名开启！ISC.AI训练营助力AI与数字安全人才培养](/post/id/309827)

  2025-07-10 17:42:56

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