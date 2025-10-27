---
title: Gunra勒索软件:新的威胁分析揭示了逃避策略
url: https://www.anquanke.com/post/id/307146
source: 安全客-有思想的安全新媒体
date: 2025-05-08
fetch_date: 2025-10-06T22:24:33.412864
---

# Gunra勒索软件:新的威胁分析揭示了逃避策略

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

# Gunra勒索软件:新的威胁分析揭示了逃避策略

阅读量**57242**

发布时间 : 2025-05-07 16:42:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/gunra-ransomware-new-threat-analysis-reveals-evasion-tactics/>

译文仅供参考，具体内容表达以及含义原文为准。

![Gunra Ransomware,勒索软件分析]()

CYFIRMA发布了对新出现的网络威胁的深入分析:Gunra Ransomware。本报告详细介绍了勒索软件的先进技术,对各个行业的影响,以及它给全球组织带来的重大风险。Gunra勒索软件是一个相对较新的威胁,通过先进的加密和数据泄漏策略相结合来针对Windows系统。这种“双重勒索”方法是一个关键特征,因为勒索软件不仅加密受害者的文件,而且还有可能在其Tor托管的勒索网站上泄露被盗数据。

分析显示,Gunra勒索软件已经投下了广泛的网络,影响了全球的不同行业。房地产,制药和制造业等行业都成为其攻击的受害者。日本、埃及、巴拿马、意大利和阿根廷的公司也受到影响。

Gunra 采用一系列恶意行为来渗透和破坏系统。这些包括:

* 枚举运行过程
* 通过 Windows 管理仪器 (WMI) 删除阴影副本
* 检索系统信息
* 检测调试器
* 列举文件

[根据该报告](https://www.cyfirma.com/research/gunra-ransomware-a-brief-analysis/),*Gunra勒索软件“采用先进的规避和反分析技术,用于感染Windows操作系统,同时最大限度地降低检测风险。**这包括“混淆恶意活动,避免基于规则的检测系统,强大的加密方法,赎金要求以及在地下论坛上发布数据的警告”。*一旦系统被感染,Gunra勒索软件就会加密文件并附加“。ENCRT”文件名的扩展名。例如,一个名为“document.docx”的文件将变成“document.docx.ENCRT”。在文件加密的每个目录中,勒索软件会丢弃名为“R3ADM3.txt”的赎金票据。本说明包含有关受害者如何恢复其文件的说明,其中包括支付赎金。这些攻击背后的主要动机是经济利益。

*“您的所有数据已被登记!*它宣称,*“我们已经抛弃了你的敏感业务数据,然后加密了你的整个数据。*这张纸条迫使受害者迅速采取行动,*说:“你只有5天时间与我们联系!**它还警告受害者不要试图自己恢复文件:“不要改变或尝试自己恢复任何文件。*“我们不可能恢复它们。

Gunra勒索软件集成了几种技术来逃避检测和阻碍分析。

* 它使用 Windows API 函数`IsDebuggerPresent`检测它是否在调试器下运行。
* 它利用`GetCurrentProcess`和`TerminateProcess`过程操纵、特权升级和反分析的功能。

[cybersecurity](https://securityonline.info/pentest-tools-com-review-your-all-in-one-platform-for-streamlined-penetration-testing-and-vulnerability-management/)CYFIRMA建议组织加强网络安全态势,以抵御Gunra勒索软件。主要建议包括:

* 加强网络钓鱼防御
* 监控内部网络移动
* 实施强大的备份策略

Gunra勒索软件的出现凸显了网络威胁的日益复杂。正如报告所总结的那样*cybersecurity,“Gunra勒索软件体现了网络安全领域日益增长的复杂性,展示了与现代勒索软件活动相一致的先进恶意行为。*

本文翻译自securityonline [原文链接](https://securityonline.info/gunra-ransomware-new-threat-analysis-reveals-evasion-tactics/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307146](/post/id/307146)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/gunra-ransomware-new-threat-analysis-reveals-evasion-tactics/)

如若转载,请注明出处： <https://securityonline.info/gunra-ransomware-new-threat-analysis-reveals-evasion-tactics/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全知识](/tag/%E5%AE%89%E5%85%A8%E7%9F%A5%E8%AF%86)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [论韧性数字安全体系（第十三章）](/post/id/309219)

  2025-07-01 15:03:14
* ##### [起亚厄瓜多尔无钥匙进入系统漏洞导致数千辆车辆被盗](/post/id/308480)

  2025-06-16 15:48:35
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24

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