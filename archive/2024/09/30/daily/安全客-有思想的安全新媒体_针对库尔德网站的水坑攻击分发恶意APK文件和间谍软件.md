---
title: 针对库尔德网站的水坑攻击分发恶意APK文件和间谍软件
url: https://www.anquanke.com/post/id/300519
source: 安全客-有思想的安全新媒体
date: 2024-09-30
fetch_date: 2025-10-06T18:20:01.161148
---

# 针对库尔德网站的水坑攻击分发恶意APK文件和间谍软件

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

# 针对库尔德网站的水坑攻击分发恶意APK文件和间谍软件

阅读量**289883**

发布时间 : 2024-09-29 15:51:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/watering-hole-attack-on-kurdish-sites.html>

译文仅供参考，具体内容表达以及含义原文为准。

作为旨在收集敏感信息的水坑攻击的一部分，多达 25 个与库尔德少数民族相关的网站遭到入侵，时间已超过一年半。

法国网络安全公司 Sekoia 披露了名为 SilentSelfie 的活动的细节，该公司将入侵集描述为长期持续，最早检测到感染迹象可追溯到 2022 年 12 月。

它补充说，战略性 Web 入侵旨在提供信息窃取框架的四种不同变体。

“这些范围从最简单的，它只是窃取用户的位置，到更复杂的，从自拍相机记录图像并引导选定的用户安装恶意 APK，即在 Android 上使用的应用程序，”安全研究人员 Felix Aimé 和 Maxime A 在周三的一份报告中说。

目标网站包括库尔德新闻和媒体、Rojava 政府及其武装部队、与土耳其和库尔德地区革命极左翼政党和组织相关的网站。Sekoia 告诉 The Hacker News，这些网站最初被入侵的确切方法仍不确定。

这些攻击尚未归因于任何已知的威胁行为者或实体，这表明出现了一个针对库尔德社区的新威胁集群，该集群之前曾被 StrongPity 和 BladeHawk 等组织挑出。

今年早些时候，荷兰安全公司Hunt & Hackett也透露，荷兰的库尔德网站被一个被称为Sea Turtle的土耳其-关系威胁行为者挑出来。

Watering Hole 攻击的特点是部署恶意 JavaScript，负责从网站访问者那里收集各种信息，包括他们的位置、设备数据（例如 CPU 数量、电池状态、浏览器语言等）和公共 IP 地址等。![Watering Hole Attack]( "Watering Hole Attack")

在三个网站 （rojnews[.]新闻， HawarNews[.]com 和 targetPlatform[.]净。还观察到将用户重定向到流氓 Android APK 文件，而其他一些文件包括通过名为“sessionIdVal”的 cookie 进行用户跟踪的能力。

根据 Sekoia 的分析，Android 应用程序将网站本身嵌入为 WebView，同时还根据授予它的权限秘密地徘徊系统信息、联系人列表、位置和存在于外部存储中的文件。

“值得注意的是，这种恶意代码没有任何持久性机制，而仅在用户打开 RojNews 应用程序时执行，”研究人员指出。

“一旦用户打开应用程序，10 秒后，LocationHelper 服务就会开始向 URL rojnews[.] 发送信标。news/wp-includes/sitemaps/ 通过 HTTP POST 请求，共享用户的当前位置并等待命令执行。

关于 SilentSelfie 的幕后黑手知之甚少，但 Sekoia 根据 2023 年 10 月KDP 部队逮捕 RojNews 记者 Silêman Ehmed 的手笔，评估这可能是伊拉克库尔德斯坦地区政府的杰作。他于 2024 年 7 月被判处三年监禁。

研究人员说：“尽管这种水坑活动并不复杂，但它受影响的库尔德网站的数量及其持续时间是值得注意的。“该活动的复杂程度较低，这表明它可能是能力有限且对该领域相对较新的未被发现的威胁行为者所为。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/watering-hole-attack-on-kurdish-sites.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300519](/post/id/300519)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/watering-hole-attack-on-kurdish-sites.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/watering-hole-attack-on-kurdish-sites.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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