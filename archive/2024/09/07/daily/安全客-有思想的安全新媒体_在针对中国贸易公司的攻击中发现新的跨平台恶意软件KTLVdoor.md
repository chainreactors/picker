---
title: 在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor
url: https://www.anquanke.com/post/id/299863
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:25.487542
---

# 在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor

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

# 在针对中国贸易公司的攻击中发现新的跨平台恶意软件KTLVdoor

阅读量**114309**

发布时间 : 2024-09-06 11:16:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-cross-platform-malware-ktlvdoor.html>

译文仅供参考，具体内容表达以及含义原文为准。

已知使用中文的威胁行为者Earth Lusca被观察到在针对中国一家未具名贸易公司的网络攻击中使用了一种新的后门程序，名为KTLVdoor。

这款此前未被报告的恶意软件是用Golang编写的，因此是一种跨平台武器，能够针对Microsoft Windows和Linux系统。

趋势科技的研究员Cédric Pernet和Jaromír Horejsí在周三发布的一份分析中表示：“KTLVdoor是一种高度混淆的恶意软件，伪装成不同的系统工具，允许攻击者执行各种任务，包括文件操作、命令执行和远程端口扫描。”

KTLVdoor冒充的一些工具包括sshd、Java、SQLite、bash和edr-agent等，恶意软件以动态链接库（.dll）或共享对象（.so）的形式分发。

这次活动集群中最不同寻常的方面之一是发现了超过50个命令与控制（C&C）服务器，所有这些服务器都托管在中国公司阿里巴巴上，并被确认与该恶意软件变种通信，这表明该基础设施可能与其他中国威胁行为者共享。

自2021年以来，Earth Lusca已知活跃于亚洲、澳大利亚、欧洲和北美的公共和私营部门实体的网络攻击中。据评估，它与其他入侵集合RedHotel和APT27（又称为Budworm、Emissary Panda和Iron Tiger）在战术上有一定的重叠。

KTLVdoor是该组织最新加入的恶意软件库，高度混淆，并因在其配置文件中使用了一个名为“KTLV”的标记而得名，该配置文件包含实现其功能所需的各项参数，包括要连接的C&C服务器。

一旦初始化，恶意软件就会循环与C&C服务器建立联系，等待进一步指令在受感染的主机上执行。所支持的命令允许它下载/上传文件、枚举文件系统、启动交互式shell、运行shellcode，并使用ScanTCP、ScanRDP、DialTLS、ScanPing和ScanWeb等工具发起扫描。

尽管如此，关于该恶意软件是如何分发的，以及它是否被用来针对世界各地的其他实体，目前尚不清楚。

研究人员指出：“这种新工具被Earth Lusca使用，但可能也会与其他使用中文的威胁行为者共享。鉴于所有C&C服务器都在来自中国提供商阿里巴巴的IP地址上，我们怀疑这种新恶意软件及其C&C服务器的出现是否是测试新工具的早期阶段。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-cross-platform-malware-ktlvdoor.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299863](/post/id/299863)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-cross-platform-malware-ktlvdoor.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-cross-platform-malware-ktlvdoor.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37

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