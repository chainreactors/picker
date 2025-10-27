---
title: 名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标
url: https://www.anquanke.com/post/id/300090
source: 安全客-有思想的安全新媒体
date: 2024-09-15
fetch_date: 2025-10-06T18:20:06.996578
---

# 名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标

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

# 名为Hadooken的新型Linux恶意软件以Oracle WebLogic服务器为目标

阅读量**209456**

发布时间 : 2024-09-14 14:59:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/168364/malware/hadooken-targets-oracle-weblogic-servers.html>

译文仅供参考，具体内容表达以及含义原文为准。

Aqua Security Nautilus 研究人员发现了一种名为 Hadoop 的新型 Linux 恶意软件，该恶意软件以 Weblogic 服务器为目标。这个名字来自于《街头霸王》系列中的攻击“浪涌拳头”。执行后，该恶意软件会放置 Tsunami 恶意软件并部署加密挖矿程序。

WebLogic Server 是由 Oracle 开发的企业级 Java EE 应用程序服务器，旨在构建、部署和管理大规模分布式应用程序。

在针对 Weblogic 蜜罐公司的攻击中，暴露了漏洞和弱密码，威胁行为者利用弱密码获得了对服务器的初始访问权限并实现了远程代码执行。

![Hadooken malware attack chain]()

一旦入侵了 WebLogic 服务器，威胁行为者就会使用 shell 脚本和 Python 脚本（分别称为“c”和“y”）来下载和执行 Hadooken 恶意软件。这两个脚本都通过将其下载到临时文件夹来用于恶意软件部署。此 Python 代码尝试通过迭代多个路径然后删除文件来下载和运行 Hadooken 恶意软件。shell 脚本还以包含 SSH 数据的目录为目标，以允许在组织内横向移动并破坏其他服务器。然后，恶意代码会清除日志以隐藏活动。

*“Hadooken 恶意软件本身同时包含加密挖矿程序和 Tsunami 恶意软件。当 Hadooken 恶意软件被执行时，它会丢弃两个 elf 文件。第一个文件是一个打包的加密挖矿程序，以 3 个不同的名称分为 3 个路径：’/usr/bin/crondr’、’/usr/bin/bprofr’ 和 ‘/mnt/-java’。“Aqua Security 发布的报告写道。第二个文件是 Tsunami 恶意软件，生成随机名称后，它被丢弃到 ‘/tmp/<<random>>”。我们没有看到任何迹象表明攻击者在攻击期间使用了 Tsunami 恶意软件。不过，它可以在以后的攻击中使用。*

两个 IP 地址用于下载 Hadooken 恶意软件;第一个 89.185.85.102 仍然有效，并在德国注册为 Aeza International LTD，而第二个 185.174.136.204 为非活动状态，在俄罗斯注册为 AEZA GROUP Ltd。活动 IP 之前曾与 TeamTNT 和 Gang 8220 相关联，但研究人员表示，没有足够的证据将这次攻击归因于任何一个组织。

报告表明，使用 Hadooken 恶意软件的威胁行为者将 Windows 端点作为勒索软件攻击的目标，以及大型组织通常使用的 Linux 服务器来部署后门和加密挖矿程序。对 Hadooken 二进制文件的静态分析揭示了与 RHOMBUS 和 NoEscape 勒索软件的联系，尽管动态分析显示没有积极使用。

*“在 Shodan（用于查找互联网连接设备和系统的搜索引擎）中搜索表明，有超过 230K 互联网连接的 Weblogic 服务器。”该报告总结道，该报告还提供了妥协迹象 （IOC）。“进一步的分析表明，他们中的大多数都受到了保护，这非常好。我们看到了几百个连接互联网的 Weblogic 服务器管理控制台。这些可能会受到利用漏洞和错误配置的攻击。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/168364/malware/hadooken-targets-oracle-weblogic-servers.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300090](/post/id/300090)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/168364/malware/hadooken-targets-oracle-weblogic-servers.html)

如若转载,请注明出处： <https://securityaffairs.com/168364/malware/hadooken-targets-oracle-weblogic-servers.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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