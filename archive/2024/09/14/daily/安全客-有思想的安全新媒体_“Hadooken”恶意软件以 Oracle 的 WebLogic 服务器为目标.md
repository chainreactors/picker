---
title: “Hadooken”恶意软件以 Oracle 的 WebLogic 服务器为目标
url: https://www.anquanke.com/post/id/300069
source: 安全客-有思想的安全新媒体
date: 2024-09-14
fetch_date: 2025-10-06T18:24:09.209471
---

# “Hadooken”恶意软件以 Oracle 的 WebLogic 服务器为目标

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

# “Hadooken”恶意软件以 Oracle 的 WebLogic 服务器为目标

阅读量**81108**

发布时间 : 2024-09-13 15:11:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/hadooken-malware-targets-weblogic-servers>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者正在使用“Hadooken”在 Oracle WebLogic Server 上投放加密挖矿程序和分布式拒绝服务 （DDoS） 恶意软件。

Aqua Nautilus 的研究人员在上个月袭击他们的一个蜜罐时发现了该恶意软件。他们随后的分析表明，Hadooken 是攻击链中的主要有效载荷，该攻击链始于威胁行为者暴力侵入 Aqua 保护较弱的 WebLogic 蜜罐的管理面板。Hadooken 的作者似乎以《街头霸王》系列视频游戏中标志性的 Surge Fist 动作命名了该恶意软件。

一旦进入 Aqua 系统，攻击者就使用两个功能几乎相同的脚本（一个 Python 脚本和一个“c”shell 脚本）将 Hadooken 下载到其中，其中一个脚本可能充当另一个的备份。Aqua 发现这两个脚本都旨在对受感染的蜜罐运行 Hadooken，然后删除该文件。

“此外，shell 脚本版本试图迭代包含 SSH 数据（例如用户凭据、主机信息和机密）的各种目录，并使用这些信息来攻击已知服务器，”Aqua 的首席研究员 Assaf Morag 在一份报告中说。“然后，它会在组织或连接环境中横向移动，以进一步传播 Hadooken 恶意软件。”

## 有价值的目标

Oracle WebLogic Server 允许客户构建和部署 Java 应用程序。数以千计的组织（包括一些世界上最大的银行和金融服务公司、专业服务公司、医疗保健实体和制造公司）已经部署了 WebLogic。这些部署包括实现 Java 企业应用程序环境的现代化、在云中部署 Java 应用程序以及构建 Java 微服务。多年来，关键漏洞（包括那些能够完全接管 WebLogic Server 的漏洞）使该技术成为攻击的常见目标。配置错误（例如弱密码和暴露在 Internet 上的管理控制台）加剧了平台周围的风险。

在 Aqua 的蜜罐攻击中，威胁行为者通过暴力破解安全供应商故意设置的弱密码，获得了对 WebLogic 服务器的初始访问权限。Hadooken 随后删除了两个可执行文件：Tsunami，一种至少可以追溯到十年前用于众多 DDoS 攻击的恶意软件;和一个加密矿工。此外，Aqua 发现恶意软件创建了多个 cron 作业——这些作业安排命令或脚本以特定的时间间隔或时间自动运行——以保持在受感染系统上的持久性。

## 可能带来更多麻烦

Aqua 的分析显示，没有迹象表明对手实际上在攻击中使用了 Tsunami，但安全供应商并不排除这种情况在后期发生的可能性。同样有可能的是，攻击者可以相对容易地调整 Hadooken 以针对其他 Linux 平台，Morag 告诉 Dark Reading。“目前，我们只看到攻击者正在暴力破解 WebLogic 服务器的迹象，”Morag 说。“但根据其他攻击和活动，我们假设攻击者不会将自己局限于 WebLogic。”

攻击者很可能不会在未来的 Hadooken 活动中将自己局限于加密货币和 DDoS 恶意软件。Aqua 对恶意软件的静态分析显示，代码中与 Rhombus 和 NoEscape 勒索软件有链接，但在对其蜜罐的攻击期间没有实际使用代码。Aqua 发现威胁行为者使用两个 IP 地址（一个在德国，另一个在俄罗斯）在受感染的系统上下载 Hadooken。Aqua 表示，德国 IP 地址是另外两个威胁组织——TeamTNT 和 Gang 8220——在以前的活动中使用的地址，但没有迹象表明它们与 Hadooken 活动有关。

该公司建议组织考虑使用基础设施即代码扫描工具、云安全态势管理工具、Kubernetes 安全和配置工具、运行时安全工具和容器安全工具等机制来缓解 Hadoop 等威胁。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/hadooken-malware-targets-weblogic-servers)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300069](/post/id/300069)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cyberattacks-data-breaches/hadooken-malware-targets-weblogic-servers)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/hadooken-malware-targets-weblogic-servers>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [有价值的目标](#h2-0)
* [可能带来更多麻烦](#h2-1)

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