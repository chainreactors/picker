---
title: 新的 Mirai 变体活动针对物联网设备
url: https://www.anquanke.com/post/id/289057
source: 安全客-有思想的安全新媒体
date: 2023-06-02
fetch_date: 2025-10-04T11:45:06.082723
---

# 新的 Mirai 变体活动针对物联网设备

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

# 新的 Mirai 变体活动针对物联网设备

阅读量**464372**

发布时间 : 2023-06-01 17:08:12

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

Palo Alto Networks 威胁研究团队 Unit 42 发现了针对 IoT 设备的新恶意活动，使用Mirai的变体，这是一种恶意软件，可将运行 Linux 的网络设备（通常是小型 IoT 设备）转变为远程控制的机器人，可用于大规模网络攻击。

这个变种被称为 IZ1H9，于 2018 年 8 月首次被发现，此后成为最活跃的 Mirai 变种之一。

Unit 42 研究人员在 4 月 10 日观察到，自 2021 年 11 月以来，一波恶意活动一直在使用 IZ1H9，这些活动全部由同一威胁参与者部署。他们在 5 月 25 日发布了一份恶意软件分析报告。

IZ1H9 最初通过 HTTP、SSH 和 Telnet 协议传播。

一旦安装在物联网设备上，IZ1H9 僵尸网络客户端首先会检查受感染设备 IP 地址的网络部分——就像最初的 Mirai 一样。客户避免执行一系列 IP 块，包括政府网络、互联网提供商和大型科技公司。

然后，它通过在控制台上打印“暗网”一词来使其存在可见。

“该恶意软件还包含一项功能，可确保设备仅运行该恶意软件的一个实例。如果僵尸网络进程已经存在，僵尸网络客户端将终止当前进程并启动一个新进程，”42单元在分析中解释道。

僵尸网络客户端还包含属于其他 Mirai 变体和其他僵尸网络恶意软件家族的进程名称列表。恶意软件会检查受感染主机上正在运行的进程名称以终止它们。

IZ1H9 变体尝试连接到硬编码的 C2 地址：193.47.61[.]75。

连接后，IZ1H9 将初始化一个加密字符串表，并通过索引检索加密字符串。

它在字符串解密过程中使用表密钥：0xBAADF00D。对于每个加密字符，恶意软件使用以下字节运算执行 XOR 解密：cipher\_char ^ 0xBA ^ 0xAD ^ 0xF0 ^ 0x0D = plain\_char。

根据 XOR 运算背后的逻辑，配置字符串密钥等于 0xBA ^ 0xAD ^ 0xF0 ^ 0x0D = 0xEA。

“这种威胁使用的漏洞不那么复杂，但这并没有降低它们的影响，因为它们仍然可能导致远程代码执行。一旦攻击者获得对易受攻击设备的控制权，他们就可以将新受损的设备包括在他们的僵尸网络中。这使他们能够进行进一步的攻击，例如分布式拒绝服务 (DDoS)。为了对抗这种威胁，强烈建议尽可能应用补丁和更新，”Unit 42 研究人员总结道。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/289057](/post/id/289057)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**10赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=168535)

[安全客](/member.html?memberId=168535)

这个人太懒了，签名都懒得写一个

* 文章
* **122**

* 粉丝
* **0**

### TA的文章

* ##### [注册机内藏勒索软件！收款竟用支付宝？](/post/id/292743)

  2024-01-19 11:10:00
* ##### [全球首发！《2023年度统信UOS安全威胁防御报告》来了](/post/id/292263)

  2023-12-29 11:27:27
* ##### [数字安全“奥斯卡”落幕，ISC 2023创新百强重磅出炉](/post/id/292240)

  2023-12-29 10:24:44
* ##### [一个安全运营工程师的自白](/post/id/291372)

  2023-11-15 10:40:17
* ##### [打造实战型安全人才新高地，360发布ISC安全课SaaS化教培平台](/post/id/291209)

  2023-11-03 17:22:35

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