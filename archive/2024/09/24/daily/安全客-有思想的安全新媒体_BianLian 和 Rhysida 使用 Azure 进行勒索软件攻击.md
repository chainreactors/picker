---
title: BianLian 和 Rhysida 使用 Azure 进行勒索软件攻击
url: https://www.anquanke.com/post/id/300308
source: 安全客-有思想的安全新媒体
date: 2024-09-24
fetch_date: 2025-10-06T18:22:40.519462
---

# BianLian 和 Rhysida 使用 Azure 进行勒索软件攻击

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

# BianLian 和 Rhysida 使用 Azure 进行勒索软件攻击

阅读量**65635**

发布时间 : 2024-09-23 15:47:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Do son ，文章来源：securityonline

原文地址：<https://securityonline.info/bianlian-and-rhysida-use-azure-for-ransomware-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

modePUSH 的安全专家最近发现，BianLian 和 Rhysida 等勒索软件组织正在积极使用 Microsoft Azure Storage Explorer 和 AzCopy 等工具从受感染的网络中窃取数据并将其存储在 Azure Blob 云存储中。

存储资源管理器是 Azure 的图形管理工具，而 AzCopy 是用于将数据大规模传输到云的命令行实用程序。使用这些工具，犯罪分子将被盗数据上传到 Azure Blob 容器，然后可以轻松地将其传输到其他存储位置。

modePUSH 专家指出，为了使用 Azure 存储资源管理器，攻击者必须安装额外的依赖项并将 .NET 升级到版本 8。这凸显了勒索软件操作中对数据盗窃的日益重视，其中被盗信息成为后续勒索阶段的主要杠杆。

虽然每个勒索软件组织都使用自己的工具进行数据泄露，但 Azure 因其作为企业服务的声誉而对网络犯罪分子特别有吸引力。由于它被许多公司广泛使用，因此其流量不太可能被公司防火墙和安全系统阻止，从而大大简化了数据传输过程。

此外，Azure 的可扩展性和性能非常有利，尤其是在需要快速传输大量文件时。modePUSH 专家还观察到，犯罪分子同时利用 Azure Storage Explorer 的多个实例来加快将数据上传到 Blob 容器的速度。

研究人员发现，在使用 AzCopy 和存储资源管理器时，攻击者会启用默认日志记录级别“Info”，该级别将操作详细信息记录在日志文件中。此文件可以帮助事件响应专家快速确定哪些数据被盗以及哪些文件可能已上传到受害者的设备。

为了防范此类威胁，建议监视 AzCopy 执行情况，跟踪到 Azure Blob 存储终结点的出站流量，并为涉及关键服务器上的文件复制或访问的异常活动设置警报。已在使用 Azure 的组织应在关闭应用程序后启用自动注销选项，以防止攻击者利用活动会话窃取数据。

本文翻译自securityonline [原文链接](https://securityonline.info/bianlian-and-rhysida-use-azure-for-ransomware-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300308](/post/id/300308)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/bianlian-and-rhysida-use-azure-for-ransomware-attacks/)

如若转载,请注明出处： <https://securityonline.info/bianlian-and-rhysida-use-azure-for-ransomware-attacks/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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