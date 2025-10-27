---
title: SEXi 勒索软件持续攻击 VMware Hypervisor
url: https://www.anquanke.com/post/id/295333
source: 安全客-有思想的安全新媒体
date: 2024-04-08
fetch_date: 2025-10-04T12:14:48.709389
---

# SEXi 勒索软件持续攻击 VMware Hypervisor

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

# SEXi 勒索软件持续攻击 VMware Hypervisor

阅读量**86125**

发布时间 : 2024-04-07 11:16:38

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/threat-intelligence/sexi-ransomware-desires-vmware-hypervisors>

译文仅供参考，具体内容表达以及含义原文为准。

Babuk 勒索软件的新变种已经出现，可以攻击多个国家/地区的 VMware ESXi 服务器，其中包括已确认对智利数据中心托管公司 IxMetro PowerHost 的攻击。该变体称自己为“SEXi”，是其选择的目标平台上的一个游戏。

据 CronUp 网络安全研究员Germán Fernández称，PowerHost 首席执行官 Ricardo Rubem 发表声明，确认新的勒索软件变种已使用 .SEXi 文件扩展名锁定了该公司的服务器，但对内部网络的初始访问向量尚不清楚。袭击者索要 1.4 亿美元的赎金，鲁本表示不会支付。

SEXi 的出现正处于两大勒索软件趋势的十字路口：基于 Babuk 源代码开发恶意软件的威胁行为者的涌现；以及对破坏诱人的 VMware EXSi 服务器的渴望。

## IX PowerHost 攻击是更广泛的勒索软件活动的一部分

与此同时，Equinix 的 CTI 研究员 Will Thomas 发现了一个他认为与攻击中使用的二进制文件有关的二进制文件，该二进制文件被称为“LIMPOPOx32.bin”，并在 VirusTotal 中标记为 Babuk 的 Linux 版本。截至发稿时，该恶意软件在 VT 上的检测率为 53%，自 2 月 8 日首次上传以来，64 个安全供应商中有 34 个将其标记为恶意软件。MalwareHunterTeam在情人节那天发现了该恶意软件，当时该恶意软件正在未经许可的情况下使用针对泰国实体的攻击中的“SEXi”句柄。

但托马斯进一步发现了其他相关的双星。他在推特上写道：“针对 IXMETRO POWERHOST 的 SEXi 勒索软件攻击与影响至少三个拉丁美洲国家的更广泛的活动有关。”这些人称自己为索科特拉岛（3 月 23 日在智利发生的一次袭击中使用过）；再次林波波（在 2 月 9 日秘鲁的一次袭击中使用）；和福尔摩沙（用于 2 月 26 日墨西哥的一次袭击）。值得关注的是，截至发稿时，所有三个 VT 均检测到零。

总之，这些发现展示了使用各种 SEXi 迭代开发的新颖活动，所有这些迭代都可追溯到 Babuk。

## SEXi 攻击中出现神秘 TTP

没有迹象表明恶意软件操作者来自何处或他们的意图是什么。但慢慢地，一套战术、技术和程序正在出现。其一，双星的命名来自地名。林波波省是南非最北端的省份；索科特拉岛是也门印度洋上的一个岛屿； 1800 年代末，中国清朝放弃对台湾的统治后，福尔摩沙是位于台湾的一个短命共和国。

而且，正如 MalwareHunterTeam 在 X 上指出的那样，“也许有趣/值得一提的是，这个‘SEXi’勒索软件的攻击者在注释中指定的通信方法是 Session。虽然我们甚至在几年前就看到一些攻击者使用它已经，我[不]记得看到过它与任何重大/严重的案件/演员有关。”

Session是一个跨平台、端到端的加密即时通讯应用程序，强调用户的保密性和匿名性。 IX PowerHost 攻击中的勒索字条敦促该公司下载该应用程序，然后发送带有代码“SEXi”的消息；泰国攻击中的早期说明敦促下载会话，但要包含代码“Limpopo”。

## EXSi 对网络攻击者来说很性感

VMware 的 EXSi 虚拟机管理程序平台在 Linux 和类 Linux 操作系统上运行，可以托管多个数据丰富的虚拟机 (VM)。多年来，它一直是勒索软件攻击者的热门目标，部分原因是攻击面的规模：根据 Shodan 搜索，有数万台 ESXi 服务器暴露在互联网上，其中大多数运行旧版本。这还没有考虑到在公司网络首次访问遭到破坏后可以访问的网络。

该平台不支持任何第三方安全工具，这也导致勒索软件团伙对 EXSi 的兴趣日益浓厚。

根据Forescout去年发布的一份报告，“ESXi 服务器等非托管设备是勒索软件威胁者的重要目标”。 “这是因为这些服务器上有宝贵的数据、越来越多的影响它们的被利用漏洞、它们频繁暴露在互联网上以及在这些设备上实施端点检测和响应 (EDR) 等安全措施的难度。ESXi 是一个高- 由于它托管多个虚拟机，因此成为攻击者的目标，允许攻击者一次部署恶意软件并使用单个命令加密大量服务器。”

VMware 提供了保护 EXSi环境的指南。具体建议包括： 确保 ESXi 软件已打补丁并且是最新的；强化密码；从互联网上删除服务器；监控网络流量和 ESXi 服务器上的异常活动；并确保 ESXi 环境之外的虚拟机有备份以实现恢复。

本文翻译自 [原文链接](https://www.darkreading.com/threat-intelligence/sexi-ransomware-desires-vmware-hypervisors)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295333](/post/id/295333)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/sexi-ransomware-desires-vmware-hypervisors>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [勒索软件组织攻击药物滥用治疗服务机构](/post/id/303119)

  2024-12-30 11:11:06
* ##### [勒索软件攻击暴露了 560 万 Ascension 患者的数据](/post/id/302957)

  2024-12-24 10:53:52
* ##### [被武器化的 Windows 工具 Wevtutil.exe 在新型攻击中被利用](/post/id/302321)

  2024-12-02 11:19:00
* ##### [CyberVolk：模糊在行动主义、勒索软件和地缘政治之间的黑客主义集体](/post/id/302214)

  2024-11-27 10:44:25
* ##### [德国大型药品批发商遭勒索攻击，欲扰乱超6000家药房供应](/post/id/301584)

  2024-11-06 10:55:18
* ##### [8Base 勒索软件团伙声称窃取大众汽车大量文件并威胁公布](/post/id/301054)

  2024-10-18 11:21:49

### 热门推荐

文章目录

* [IX PowerHost 攻击是更广泛的勒索软件活动的一部分](#h2-0)
* [SEXi 攻击中出现神秘 TTP](#h2-1)
* [EXSi 对网络攻击者来说很性感](#h2-2)

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