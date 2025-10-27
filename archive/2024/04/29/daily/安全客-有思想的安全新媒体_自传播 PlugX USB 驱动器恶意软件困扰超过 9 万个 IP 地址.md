---
title: 自传播 PlugX USB 驱动器恶意软件困扰超过 9 万个 IP 地址
url: https://www.anquanke.com/post/id/296086
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:33.031670
---

# 自传播 PlugX USB 驱动器恶意软件困扰超过 9 万个 IP 地址

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

# 自传播 PlugX USB 驱动器恶意软件困扰超过 9 万个 IP 地址

阅读量**83912**

发布时间 : 2024-04-28 11:34:17

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securityweek.com/self-spreading-plugx-usb-drive-malware-plagues-over-90k-ip-addresses/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全公司 Sekoia 报告称，与 90,000 多个唯一 IP 地址相关的系统仍然受到 PlugX 蠕虫变体的感染，该变体通过受感染的 USB 驱动器绕过气隙进行传播。

在过去的六个月中，Sekoia一直在监控与该蠕虫相关的 Sinkhole IP 的连接，识别出超过 250 万个随着时间的推移与其连接的 IP 地址。

其中，90,000 到 100,000 个唯一 IP 仍然每天向 Sinkhole 发送请求，这表明僵尸网络仍然活跃，尽管其运营商不再控制它。

然而，“任何具有拦截能力或拥有该服务器的人都可以向受感染的主机发送任意命令，以将其重新用于恶意活动，” Sekoia 说。

虽然 PlugX 远程访问木马 (RAT) 自 2008 年以来就已存在，但自传播变种是由与中国相关的威胁行为者于 2020 年发布的，被追踪为Mustang Panda，可能会从未连接到互联网的网络中窃取数据。

该蠕虫向连接的闪存驱动器添加一个带有驱动器名称的 Windows 快捷方式文件，以及三个用于 DLL 旁加载的文件，即驱动器 RECYCLER.BIN 隐藏文件夹中的合法可执行文件、恶意库和二进制 blob。它还会将驱动器的内容移动到新目录。

当用户单击快捷方式文件时，恶意软件会打开一个显示驱动器内容的新窗口，然后将自身复制到系统并创建一个新的注册表项以进行持久化。接下来，它从系统中重新执行自身，每 30 秒检查一次连接的 USB 驱动器是否受到感染。

Sekoia 指出，这种自我传播技术导致僵尸网络在网络中不受控制地扩展，可能会迫使其运营商放弃命令与控制 (C&C) 服务器，因为该服务器无法再用于管理数千台受感染的主机。

在识别出不再使用的 C&C IP 后，Sekoia 获得了该地址的所有权，然后创建了管理连接尝试并映射其来源所需的基础设施。

该安全公司能够在全球 170 多个国家/地区识别出大约 250 万台受感染的主机，并观察到该蠕虫病毒仍在以平均每天 20,000 例感染的速度传播。

![]()

然而，调查仅限于使用 IP 地址，因为该蠕虫不使用受害者的唯一标识符。因此，受感染系统的总数可能会有所不同，因为某些 IP 可能被多个工作站使用，而某些系统可能依赖于动态 IP。

然而，在 4 月初，该安全公司检测到有超过 100,000 个唯一 IP 连接到污水坑。大多数受害者位于中国“一带一路”战略重要地区的国家。

Sekoia 指出：“随着中国在各地进行投资，这种蠕虫病毒的开发是为了在各国收集有关‘一带一路’倡议相关战略和安全问题的情报，但这一点似乎是合理的，尽管并不确定，但主要是在海事和经济方面。” 。

该公司对该 PlugX 变体的分析揭示了自删除命令的存在以及可用于将该命令传递到所有受感染主机并从中删除恶意软件的潜在机制。

通过提供精心设计的有效负载，在消毒时连接到受感染计算机的任何受感染 USB 驱动器也可以被清理，并且这些驱动器上的用户文件也可以完全恢复。

然而，由于删除有效负载不包括持久性机制，因此该蠕虫可能无法完全根除，因为它会在消毒期间未连接到系统的受感染闪存驱动器上保持活动状态。此外，恶意软件还可能持续存在于气隙系统上，因为它们不会收到命令。

考虑到发送消毒命令的法律影响，Sekoia 决定联系受影响国家的计算机应急响应小组 (CERT) 和执法机构，向他们提供来自污水坑的数据，并要求他们决定是否应该进行消毒。

本文翻译自 [原文链接](https://www.securityweek.com/self-spreading-plugx-usb-drive-malware-plagues-over-90k-ip-addresses/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296086](/post/id/296086)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securityweek.com/self-spreading-plugx-usb-drive-malware-plagues-over-90k-ip-addresses/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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