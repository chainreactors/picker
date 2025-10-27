---
title: 新的 Android 间谍软件 LianSpy 使用 Yandex Cloud 逃避检测
url: https://www.anquanke.com/post/id/298909
source: 安全客-有思想的安全新媒体
date: 2024-08-08
fetch_date: 2025-10-06T17:59:28.937072
---

# 新的 Android 间谍软件 LianSpy 使用 Yandex Cloud 逃避检测

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

# 新的 Android 间谍软件 LianSpy 使用 Yandex Cloud 逃避检测

阅读量**70155**

发布时间 : 2024-08-07 15:40:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html>

译文仅供参考，具体内容表达以及含义原文为准。

至少自 2021 年以来，俄罗斯用户一直是以前未记录的 Android 入侵后间谍软件的目标，称为 LianSpy。

网络安全供应商卡巴斯基于 2024 年 3 月发现了该恶意软件，并指出它使用俄罗斯云服务 Yandex Cloud 进行命令和控制 （C2） 通信，作为避免拥有专用基础设施和逃避检测的一种方式。

“这种威胁可以捕获截屏视频，泄露用户文件，并收集通话记录和应用程序列表，”安全研究员德米特里·加里宁（Dmitry Kalinin）在周一发布的一份新技术报告中说。

目前尚不清楚间谍软件是如何分发的，但这家俄罗斯公司表示，它可能是通过未知的安全漏洞或对目标手机的直接物理访问来部署的。带有恶意软件的应用程序伪装成支付宝或 Android 系统服务。LianSpy 一旦激活，它就会确定它是否作为系统应用程序运行，以使用管理员权限在后台运行，或者请求广泛的权限，允许它访问联系人、通话记录和通知，并在屏幕上绘制叠加层。

它还会检查它是否在调试环境中执行，以设置在重新启动后仍然存在的配置，然后从启动器和触发器活动中隐藏其图标，例如截取屏幕截图、泄露数据以及更新其配置以指定需要捕获的信息类型。

在某些变体中，已发现这包括从俄罗斯流行的即时通讯应用程序收集数据的选项，以及仅在连接到 Wi-Fi 或移动网络等时允许或禁止运行恶意软件。

“为了更新间谍软件配置，LianSpy 每 30 秒在威胁参与者的 Yandex 磁盘上搜索与正则表达式”^frame\_.+\\.png$“匹配的文件，”Kalinin 说。“如果找到，文件将下载到应用程序的内部数据目录中。”

收集的数据以加密形式存储在 SQL 数据库表中，指定记录类型及其 SHA-256 哈希，这样只有拥有相应私钥的威胁参与者才能解密被盗信息。

LianSpy 展示其隐身性的地方在于它能够绕过 Google 在 Android 12 中引入的隐私指示器功能，该功能要求请求麦克风和摄像头权限的应用程序显示状态栏图标。

“LianSpy开发人员通过将投射值附加到Android安全设置参数icon\_blacklist，成功地绕过了这种保护，这可以防止通知图标出现在状态栏中，”Kalinin指出。

“LianSpy 通过利用 NotificationListenerService 来隐藏它调用的后台服务的通知，该服务处理状态栏通知并能够抑制它们。”

该恶意软件的另一个复杂方面是需要使用修改后名称为“mu”的 su 二进制文件来获得 root 访问权限，这增加了它可能通过以前未知的漏洞利用或物理设备访问提供的可能性。LianSpy 强调在雷达下飞行也体现在 C2 通信是单向的，恶意软件不会接收任何传入的命令。Yandex Disk 服务用于传输被盗数据和存储配置命令。

Yandex Disk 的凭据是从硬编码的 Pastebin URL 更新的，该 URL 因恶意软件变体而异。使用合法服务增加了一层混淆，有效地掩盖了归因。

LianSpy 是不断增长的间谍软件工具列表中的最新成员，这些工具通常通过利用零日漏洞提供给目标移动设备（无论是 Android 还是 iOS）。

加里宁说：“除了收集通话记录和应用程序列表等标准间谍策略外，它还利用root权限进行秘密屏幕录制和逃避。“它对重命名的 su 二进制文件的依赖强烈表明，在最初的妥协之后，继发感染。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298909](/post/id/298909)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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