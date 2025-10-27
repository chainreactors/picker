---
title: CISA命令机构修补攻击中利用的Linux内核漏洞
url: https://www.anquanke.com/post/id/303900
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:38.125438
---

# CISA命令机构修补攻击中利用的Linux内核漏洞

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

# CISA命令机构修补攻击中利用的Linux内核漏洞

阅读量**282703**

发布时间 : 2025-02-06 15:34:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-linux-kernel-bug-exploited-in-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![CISA]()

美国网络安全与基础设施安全局（CISA）已责令联邦机构在三周内针对一个在攻击中被积极利用的严重 Linux 内核漏洞，加固其系统安全。

该安全漏洞编号为 CVE – 2024 – 53104，最早出现在内核版本 2.6.26 中，谷歌已于周一为安卓用户修复了该漏洞。

“2025 年 2 月安卓安全更新” 警告称：“有迹象表明，CVE – 2024 – 53104 可能正遭受有限的、有针对性的利用。”

根据谷歌的安全公告，此漏洞是由 USB 视频类（UVC）驱动中的越界写入漏洞导致的，在未打补丁的设备上，这使得 “无需额外执行权限即可实现物理权限提升”。

uvc\_parse\_format 函数中，该驱动无法准确解析 UVC\_VS\_UNDEFINED 帧，从而引发此问题，导致帧缓冲区大小计算错误，并可能出现越界写入情况。

尽管谷歌没有提供关于利用此漏洞的零日攻击的更多信息，但 GrapheneOS 开发团队表示，这个 USB 外围设备驱动漏洞 “很可能是取证数据提取工具利用的 USB 漏洞之一”。

![GrapheneOS CVE-2024-53104]()

根据 2021 年 11 月发布的《约束性操作指令（BOD）22 – 01》，美国联邦机构必须保护其网络，防范针对 CISA “已知被利用漏洞” 目录中新增漏洞的持续攻击。

这家网络安全机构已要求联邦民用执行部门（FCEB）各机构在 2 月 26 日前，为其 Linux 和安卓设备打上补丁。

CISA 今日警告称：“这类漏洞是恶意网络行为者常用的攻击途径，给联邦政府机构带来重大风险。”

周二，CISA 还将微软.NET Framework 和 Apache OFBiz（开放式企业应用平台）软件中的严重及危急漏洞标记为在实际环境中被积极利用。然而，它并未提供有关攻击背后主谋的细节。

CISA 与英国、澳大利亚、加拿大、新西兰和美国的 “五眼联盟” 网络安全机构一道，还发布了针对网络边缘设备的安全指南，敦促制造商提高取证可见性，以帮助防御者检测攻击并调查违规行为。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-linux-kernel-bug-exploited-in-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303900](/post/id/303900)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-linux-kernel-bug-exploited-in-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-orders-agencies-to-patch-linux-kernel-bug-exploited-in-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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