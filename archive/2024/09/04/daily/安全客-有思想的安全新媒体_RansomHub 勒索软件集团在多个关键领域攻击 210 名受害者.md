---
title: RansomHub 勒索软件集团在多个关键领域攻击 210 名受害者
url: https://www.anquanke.com/post/id/299718
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:51.980074
---

# RansomHub 勒索软件集团在多个关键领域攻击 210 名受害者

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

# RansomHub 勒索软件集团在多个关键领域攻击 210 名受害者

阅读量**99174**

发布时间 : 2024-09-03 14:24:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国政府表示，自 2024 年 2 月成立以来，与 RansomHub 勒索软件组织有关的威胁行为者加密并泄露了至少 210 名受害者的数据。

受害者涉及各个领域，包括水和废水、信息技术、政府服务和设施、医疗保健和公共卫生、紧急服务、食品和农业、金融服务、商业设施、关键制造、运输和通信关键基础设施。

政府机构表示：“RansomHub 是一种勒索软件即服务变体——以前称为 Cyclops 和 Knight——它已经确立了自己作为一种高效和成功的服务模式（最近吸引了来自 LockBit 和 ALPHV 等其他著名变体的知名附属公司）。

作为 Cyclops 和 Knight 的后代勒索软件即服务 （RaaS） 变体，在最近的一波执法行动之后，电子犯罪行动吸引了来自 LockBit 和 ALPHV（又名 BlackCat）等其他知名变体的知名附属公司。

ZeroFox 在上月底发布的一份分析中表示，RansomHub 的活动占网络安全供应商观察到的所有勒索软件活动的比例呈上升趋势，约占 2024 年第一季度所有攻击的 2%，第二季度为 5.1%，第三季度迄今为 14.2%。

该公司指出：“大约 34% 的 RansomHub 攻击针对欧洲的组织，而整个威胁形势中只有 25%。

众所周知，该组织采用双重勒索模型来泄露数据和加密系统，以勒索受害者，并敦促受害者通过唯一的 .onion URL 联系运营商。拒绝默许赎金要求的目标公司会在数据泄露网站上发布他们的信息，为期 3 到 90 天。

通过利用 Apache ActiveMQ （CVE-2023-46604）、Atlassian Confluence 数据中心和服务器 （CVE-2023-22515）、Citrix ADC （CVE-2023-3519）、F5 BIG-IP （CVE-2023-46747）、Fortinet FortiOS （CVE-2023-27997） 和 Fortinet FortiClientEMS （CVE-2023-48788） 设备等中的已知安全漏洞，可以方便地对受害者环境进行初始访问。

这一步由附属公司使用 AngryIPScanner、Nmap 和其他离地谋生 （LotL） 方法进行侦察和网络扫描来接替。RansomHub 攻击还涉及使用自定义工具解除防病毒软件的武装，以便在雷达下飞行。

“在初始访问之后，RansomHub 附属公司创建了用于持久性的用户帐户，重新启用已禁用的帐户，并在 Windows 系统上使用 Mimikatz 收集凭据 [T1003] 并将权限升级到 SYSTEM，”美国政府公告中写道。

“然后，附属公司通过远程桌面协议 （RDP）、PsExec、AnyDesk、Connectwise、N-Able、Cobalt Strike、Metasploit 或其他广泛使用的命令和控制 （C2） 方法等方法在网络内横向移动。”

RansomHub 攻击的另一个值得注意的方面是使用间歇性加密来加快流程，通过 PuTTY、Amazon AWS S3 存储桶、HTTP POST 请求、WinSCP、Rclone、Cobalt Strike、Metasploit 和其他方法等工具观察到数据泄露。

这一发展是在 Palo Alto Networks Unit 42 解开与 ShinyHunters 勒索软件相关的策略之际发生的，它将其跟踪为 Bling Libra，突出了它转向勒索受害者，而不是他们出售或发布被盗数据的传统策略。威胁行为者于 2020 年首次曝光。

“该组织从公共存储库获取合法凭证，以获得对组织的 Amazon Web Services （AWS） 环境的初始访问权限，”安全研究人员 Margaret Zimmermann 和 Chandni Vaya 说。

“虽然与泄露凭证相关的权限限制了泄露的影响，但 Bling Libra 渗透到组织的 AWS 环境并进行了侦察行动。威胁行为者组织使用 Amazon Simple Storage Service （S3） 浏览器和 WinSCP 等工具收集有关 S3 存储桶配置的信息、访问 S3 对象和删除数据。

根据 SOCRadar 的说法，它还遵循勒索软件攻击的重大演变，勒索软件攻击已经超越了文件加密，采用了复杂、多方面的勒索策略，甚至采用了三重和四重勒索计划。

“三重勒索提高了赌注，威胁到加密和泄露之外的其他破坏手段，”该公司表示。

“这可能涉及对受害者的系统进行 DDoS 攻击，或向受害者的客户、供应商或其他合作伙伴发出直接威胁，以对勒索计划的最终目标造成进一步的运营和声誉损害。”

四重勒索通过联系与受害者有业务关系的第三方并勒索他们，或威胁受害者公开来自第三方的数据，以进一步向受害者施加压力以支付费用，从而提高赌注。

RaaS 模型的有利可图的性质推动了 Allarich、Cronus、CyberVolk、Datablack、DeathGrip、Hawk Eye 和 Insom 等新勒索软件变体的激增。它还导致伊朗民族国家行为者与 NoEscape、RansomHouse 和 BlackCat 等知名组织合作，以换取非法收益的分成。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299718](/post/id/299718)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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