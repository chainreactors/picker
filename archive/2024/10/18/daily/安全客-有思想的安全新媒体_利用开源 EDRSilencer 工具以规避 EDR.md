---
title: 利用开源 EDRSilencer 工具以规避 EDR
url: https://www.anquanke.com/post/id/301012
source: 安全客-有思想的安全新媒体
date: 2024-10-18
fetch_date: 2025-10-06T18:49:53.042955
---

# 利用开源 EDRSilencer 工具以规避 EDR

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

# 利用开源 EDRSilencer 工具以规避 EDR

阅读量**94905**

发布时间 : 2024-10-17 14:21:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/10/15/edr-evasion-edrsilencer/>

译文仅供参考，具体内容表达以及含义原文为准。

趋势科技研究人员注意到，威胁行为者正在利用开源 EDRSilencer 工具躲避端点检测和响应系统。

**关于 EDRSilencer**

该软件用于红队，被滥用于 “压制 ”EDR 解决方案。

它的工作原理是利用 Windows 过滤平台（WFP），该平台允许创建自定义规则来监控、阻止和修改网络流量。

研究人员解释说：“代码利用 WFP（Windows 过滤平台），动态识别正在运行的 EDR 进程，并创建 WFP 过滤器来阻止它们在互联网协议 IPv4 和 IPv6 上的出站网络通信，从而有效阻止 EDR 向其管理控制台发送遥测或警报。”

![EDR evasion]()

EDRSilencer 目前可以检测多种 EDR 产品的进程： Carbon Black EDR、Cybereason、ESET Inspect、SentinelOne、Trellix EDR、Microsoft Defender for Endpoint 和 Microsoft Defender Antivirus、Tanium、TrendMicro Apex One 等。

趋势科技的研究人员还发现，当某些进程没有被硬编码到工具的列表中时，可以通过附加规则来阻止它们。

**EDR 规避工具的兴起**

FIN7 从 2023 年初开始向多个勒索软件组织出售 AvNeutralizer（又名 AuKill）。该工具使用 Windows 的 TTD 监控驱动程序和（Sysinternals）进程资源管理器驱动程序来 “挂起 ”或崩溃受保护的 EDR 进程。

RansomHub RaaS 一直在使用 EDRKillShifter，各种 RaaS 行为者一直在利用 PoorTry（又名 BurntCigar），这是一种针对安全产品的驱动程序，用于终止安全产品。

Qilin 勒索软件攻击者一直在利用 “Killer Ultra”，它使用易受攻击的 Zemana 驱动程序来终止 EDR 和防病毒进程。

各种工具采用的机制可能不同，但效果是一样的：端点安全解决方案无法正常运行。

“EDR规避工具通常以订购服务的形式出售，起价低至每月350美元或单次绕过300美元。”ExtraHop的研究人员分享说：“低廉的价格使得这些工具非常容易被勒索软件关联公司和其他威胁行为者获取，包括那些技术水平较低的人。”

在高端产品方面，ExtraHop注意到最近有几款产品，威胁者将其EDR绕过产品的价格定在7500美元，而将EDR规避功能打包到加密锁中的产品价格则高达10000美元。

趋势科技的研究人员建议，企业应该采用先进的检测机制和威胁猎杀策略来对抗 EDR 杀毒工具。

Intel471 的研究人员最近介绍了如何猎杀 EDRKillshifter，ConnectWise Cyber Research 也分享了保护组织免受基于 BYOVD 的工具攻击的建议。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/10/15/edr-evasion-edrsilencer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301012](/post/id/301012)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/10/15/edr-evasion-edrsilencer/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/10/15/edr-evasion-edrsilencer/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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