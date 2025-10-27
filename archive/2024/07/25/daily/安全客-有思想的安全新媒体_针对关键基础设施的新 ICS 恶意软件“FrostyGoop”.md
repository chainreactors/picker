---
title: 针对关键基础设施的新 ICS 恶意软件“FrostyGoop”
url: https://www.anquanke.com/post/id/298276
source: 安全客-有思想的安全新媒体
date: 2024-07-25
fetch_date: 2025-10-06T17:41:24.198985
---

# 针对关键基础设施的新 ICS 恶意软件“FrostyGoop”

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

# 针对关键基础设施的新 ICS 恶意软件“FrostyGoop”

阅读量**124341**

发布时间 : 2024-07-24 14:38:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/new-ics-malware-frostygoop-targeting.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了他们所说的第九种以工业控制系统 （ICS） 为重点的恶意软件，该恶意软件已被用于今年 1 月初针对乌克兰利沃夫市一家能源公司的破坏性网络攻击。

工业网络安全公司 Dragos 将该恶意软件称为 **FrostyGoop**，称其为第一个直接使用 Modbus TCP 通信破坏运营技术 （OT） 网络的恶意软件。该公司于 2024 年 4 月发现了它。

“FrostyGoop 是一种用 Golang 编写的特定于 ICS 的恶意软件，可以通过端口 502 使用 Modbus TCP 直接与工业控制系统 （ICS） 交互，”研究人员 Kyle O’Meara、Magpie （Mark） Graham 和 Carolyn Ahlers 在与 The Hacker News 分享的一份技术报告中说。

据信，该恶意软件主要针对 Windows 系统而设计，已被用于针对 TCP 端口 502 暴露在互联网上的 ENCO 控制器。它未与任何先前确定的威胁参与者或活动集群相关联。

FrostyGoop 具有读取和写入 ICS 设备的功能，该设备保存包含输入、输出和配置数据的寄存器。它还接受可选的命令行执行参数，使用 JSON 格式的配置文件指定目标 IP 地址和 Modbus 命令，并将输出记录到控制台和/或 JSON 文件。

据称，针对市政区能源公司的事件导致600多栋公寓楼的供暖服务中断了近48小时。

研究人员在电话会议上表示：“对手向 ENCO 控制器发送了 Modbus 命令，导致测量不准确和系统故障，”并指出初始访问可能是通过利用 2023 年 4 月 Mikrotik 路由器中的一个漏洞获得的。

“攻击者向ENCO控制器发送Modbus命令，导致测量不准确和系统故障。整治花了将近两天时间。

虽然 FrostyGoop 广泛使用 Modbus 协议进行客户端/服务器通信，但它远非唯一的协议。2022 年，Dragos 和 Mandiant 详细介绍了另一种名为 PIPEDREAM（又名 INCONTROLLER）的 ICS 恶意软件，该恶意软件利用 OPC UA、Modbus 和 CODESYS 等各种工业网络协议进行交互。

它也是继 Stuxnet、Havex、Industroyer（又名 CrashOverride）、Triton（又名 Trisis）、BlackEnergy2、Industroyer2 和 COSMICENERGY 之后的第九个以 ICS 为重点的恶意软件。

Dragos表示，该恶意软件使用Modbus读取或修改ICS设备上的数据的能力对工业运营和公共安全产生了严重后果，并增加了超过46,000个暴露在互联网上的ICS设备通过广泛使用的协议进行通信。

研究人员表示：“在端口502上使用Modbus TCP对ICS的特定目标，以及与各种ICS设备直接交互的可能性，对多个部门的关键基础设施构成了严重威胁。

“组织必须优先实施全面的网络安全框架，以保护关键基础设施免受未来类似威胁。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/new-ics-malware-frostygoop-targeting.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298276](/post/id/298276)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/new-ics-malware-frostygoop-targeting.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-ics-malware-frostygoop-targeting.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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