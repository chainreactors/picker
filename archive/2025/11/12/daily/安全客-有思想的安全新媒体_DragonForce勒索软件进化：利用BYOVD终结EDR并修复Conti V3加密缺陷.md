---
title: DragonForce勒索软件进化：利用BYOVD终结EDR并修复Conti V3加密缺陷
url: https://www.anquanke.com/post/id/313189
source: 安全客-有思想的安全新媒体
date: 2025-11-12
fetch_date: 2025-11-13T03:14:09.958079
---

# DragonForce勒索软件进化：利用BYOVD终结EDR并修复Conti V3加密缺陷

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

# DragonForce勒索软件进化：利用BYOVD终结EDR并修复Conti V3加密缺陷

阅读量**13032**

发布时间 : 2025-11-12 17:55:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/dragonforce-ransomware-evolves-with-byovd-to-kill-edr-and-fixes-encryption-flaws-in-conti-v3-codebase/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Acronis威胁研究团队（TRU）近日发现，DragonForce勒索软件出现了显著的技术和组织结构升级。最新变种不仅采用“自带漏洞驱动”（BYOVD）技术来关闭安全软件、终止受保护进程**，还修复了其基于**Conti V3代码的加密缺陷**，此前这些问题曾与Akira勒索软件有关。

研究报告指出：“最新样本利用了存在漏洞的驱动程序（如 **truesight.sys** 与 **rentdrv2.sys**），用于关闭安全防护、终止受保护进程，并修复先前在Akira中暴露的加密问题。新的加密方案针对Habr文章中披露的弱点进行了修正。”

![]()

## 从黑客行动组织到勒索“集团”

DragonForce最早于2023年出现，最初以勒索软件即服务（RaaS）的形式运营，与黑客激进组织“DragonForce Malaysia”存在一定关联。早期加密器基于LockBit 3.0泄露的构建工具开发，随后过渡到Conti v3代码。

进入2025年初，DragonForce完成品牌重塑，自称为“勒索集团”（Cartel），以吸引更多加盟者。**其通过提供可定制的加密器、攻击基础设施接入权限，以及高达80%的分成比例，迅速在勒索生态中崛起。**
自重组以来，该组织愈发激进，全球受害者数量上升，并开始与其他攻击团体展开合作。其最引人注目的攻击事件是与Scattered Spider组织联合攻击英国零售巨头Marks & Spencer。

## 技术演进：从Conti继承到自研工具链

Acronis分析人员发现，新版本的DragonForce二进制文件体积显著增大，表明开发工具链发生了变化。新的样本由MinGW编译，显示出该组织正在整合其多平台勒索软件代码库。

尽管框架有所更新，但代码仍继承自Conti泄露源码，复用了如`InitializeApiModule`与`DisableHooks`等函数。然而，新版本增加了加密配置文件，无需命令行参数即可运行，从而增强了操作隐蔽性。

**其加密系统采用ChaCha20 + RSA混合加密机制：**
每个文件会生成独立的ChaCha20密钥，并使用公钥RSA加密。加密文件中包含结构化头部，用于存储元数据和加密信息。

配置文件允许加盟者自定义扩展名、黑名单和进程终止列表，目标包括Microsoft Defender（MsMpEng.exe）、Oracle服务及SQL数据库服务等。**其中最值得注意的是，use\_sys标志位可启用BYOVD机制，利用Truesight与BadRentdrv2驱动强制终结防病毒与EDR进程。**

**通过向这些驱动发送特制的DeviceIoControl指令，恶意软件能够终结系统级受保护进程——这是普通终止调用无法做到的。**这种滥用驱动的手法，与BlackCat、AvosLocker等高级勒索软件家族如出一辙。

## 分支与联盟：Devman的出现

Acronis还发现，DragonForce与一个新兴勒索家族**Devman**存在技术联系，其样本基于DragonForce的构建器与基础设施。
研究人员指出：“该样本的加密文件扩展名为‘.devman’，但图标、壁纸和勒索信模板均来自DragonForce。”

Devman的勒索说明与早期基于LockBit的DragonForce版本几乎完全一致，暗示其是**DragonForce生态内的加盟分支**，在保留核心技术的同时尝试独立品牌化。

**这种结构反映出勒索圈的“集团化趋势（cartelization）”——类似Scattered Spider、LAPSUS$、ShinyHunters等组织，它们不再单纯竞争，而是协作共享攻击资源与受害者渠道。**

## 组织冲突与版图扩张

Acronis报告称，DragonForce的崛起也引发了与其他勒索集团的“地盘争夺战”。该组织曾篡改或接管竞争对手（如BlackLock和RansomHub）的基础设施，以彰显主导地位。
不久后，DragonForce甚至尝试对RansomHub服务器进行“恶意接管”，导致后者暂时中断运行，部分加盟成员因此转向DragonForce与Qilin阵营。

## 结论

Acronis TRU的评估认为，**DragonForce的最新进化标志着其已成为当前最具组织化与技术适应性的勒索软件生态系统之一**。
从BYOVD攻击防御体系，到加密机制的修复与联盟扩张，DragonForce正在向更成熟、更隐蔽、更商业化的网络犯罪集团演化。

本文翻译自securityonline [原文链接](https://securityonline.info/dragonforce-ransomware-evolves-with-byovd-to-kill-edr-and-fixes-encryption-flaws-in-conti-v3-codebase/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313189](/post/id/313189)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/dragonforce-ransomware-evolves-with-byovd-to-kill-edr-and-fixes-encryption-flaws-in-conti-v3-codebase/)

如若转载,请注明出处： <https://securityonline.info/dragonforce-ransomware-evolves-with-byovd-to-kill-edr-and-fixes-encryption-flaws-in-conti-v3-codebase/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **683**

* 粉丝
* **6**

### TA的文章

* ##### [一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证](/post/id/313153)

  2025-11-12 17:56:49
* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%](/post/id/313167)

  2025-11-12 17:55:43
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21

### 相关文章

* ##### [一场通过Telegram传播的网络钓鱼活动正针对欧洲企业，利用HTML附件窃取用户凭证](/post/id/313153)

  2025-11-12 17:56:49
* ##### [Devolutions Server存在严重漏洞（CVE-2025-12485，CVSS 9.4），可通过预MFA Cookie劫持实现用户冒充](/post/id/313156)

  2025-11-12 17:56:29
* ##### [CMMC新规出台，国防供应链面临网络安全合规挑战](/post/id/313163)

  2025-11-12 17:56:08
* ##### [被动 Wi-Fi 嗅探攻击：识别智能手机用户准确率高达 98%](/post/id/313167)

  2025-11-12 17:55:43
* ##### [黑客入侵网站注入恶意链接，借机操纵搜索引擎优化](/post/id/313169)

  2025-11-12 17:55:21
* ##### [SuiteCRM中存在SQL注入漏洞（CVE-2025-64492与CVE-2025-64493），致客户数据面临泄露风险](/post/id/313150)

  2025-11-12 17:54:44
* ##### [Triofox零日漏洞（CVE-2025-12480）正遭积极利用：主机头验证绕过可导致未授权管理员接管](/post/id/313147)

  2025-11-12 17:54:22

### 热门推荐

文章目录

* [从黑客行动组织到勒索“集团”](#h2-0)
* [技术演进：从Conti继承到自研工具链](#h2-1)
* [分支与联盟：Devman的出现](#h2-2)
* [组织冲突与版图扩张](#h2-3)
* [结论](#h2-4)

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