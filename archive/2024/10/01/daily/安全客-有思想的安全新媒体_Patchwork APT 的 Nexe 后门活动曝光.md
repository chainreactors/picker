---
title: Patchwork APT 的 Nexe 后门活动曝光
url: https://www.anquanke.com/post/id/300549
source: 安全客-有思想的安全新媒体
date: 2024-10-01
fetch_date: 2025-10-06T18:50:40.763424
---

# Patchwork APT 的 Nexe 后门活动曝光

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

# Patchwork APT 的 Nexe 后门活动曝光

阅读量**437307**

发布时间 : 2024-09-30 15:03:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Do son，文章来源：securityonline

原文地址：<https://securityonline.info/advanced-cyberattacks-patchwork-apts-nexe-backdoor-campaign-exposed/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Cyble Research and Intelligence Labs （CRIL） 的一份新报告中，臭名昭著的 Patchwork APT 组织通过部署“Nexe”后门的复杂活动再次展示了其网络间谍实力。该组织也被称为 Falling Elephant，自 2009 年以来一直活跃，专注于知名组织，包括政府、国防和外交实体，尤其是在南亚和东南亚。

CRIL 于 2024 年 7 月确定的最新活动似乎针对中国实体，特别关注航空航天、技术研究和政府部门。这并不奇怪，因为 Patchwork 长期以来一直与针对地缘政治对手的网络间谍活动有关。该活动以第七届中国商飞国际科技创新周为中心，使用了一个伪装成标题为“COMAC\_Technology\_Innovation.pdf.lnk”的 PDF 文档的恶意 LNK 文件。这个诱饵利用一个备受瞩目的事件来欺骗受害者执行恶意负载。

该活动的核心是启动感染的 LNK 文件。打开后，该文件将运行 PowerShell 脚本，下载两个组件：一个看起来合法的 PDF 以分散用户的注意力，以及一个用于执行攻击的恶意动态链接库 （DLL）。Patchwork 采用 DLL 旁加载，这是一种利用合法系统文件（在本例中为“WerFaultSecure.exe”）来执行恶意 DLL 而不会引起怀疑的技术。

加载恶意 DLL 后，它会解密并执行隐藏的 shellcode，修改 AMSIscanBuffer 和 ETWEventWrite 等关键 API 以绕过检测系统。这允许恶意软件在受感染的系统内秘密运行，避开通常会标记此类行为的防病毒和安全解决方案。

该活动的目的是 Nexe 后门，这是一种展示 Patchwork 集团持续发展的新变体。该恶意软件旨在从受害者的机器上收集敏感的系统信息，包括进程 ID、公共和私有 IP 地址、用户名和其他关键数据。收集数据后，使用 Salsa20 算法对其进行加密，使用 Base64 编码进一步混淆，然后传输到该组的命令和控制 （C2） 服务器。

Nexe 融入受害者系统的能力是其最危险的功能之一。通过使用合法的系统工具和 DLL 旁加载，恶意软件能够在后台运行，在逃避检测的同时窃取数据。后门还利用多层加密和内存驻留有效负载执行来确保持久性和隐身性，使攻击者能够保持对受感染系统的长期访问。

Patchwork APT 小组在本次活动中使用内存补丁的做法特别值得注意。通过操纵 AMSI 和 ETW API，该恶意软件有效地禁用了 Windows 的内置安全机制，这些机制旨在检测和阻止恶意脚本和进程。这种方法确保恶意软件可以在内存中执行而不会被常见的防病毒程序检测到，从而允许 Patchwork 在受害者的机器上长时间保持立足点。

本文翻译自securityonline [原文链接](https://securityonline.info/advanced-cyberattacks-patchwork-apts-nexe-backdoor-campaign-exposed/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300549](/post/id/300549)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/advanced-cyberattacks-patchwork-apts-nexe-backdoor-campaign-exposed/)

如若转载,请注明出处： <https://securityonline.info/advanced-cyberattacks-patchwork-apts-nexe-backdoor-campaign-exposed/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
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