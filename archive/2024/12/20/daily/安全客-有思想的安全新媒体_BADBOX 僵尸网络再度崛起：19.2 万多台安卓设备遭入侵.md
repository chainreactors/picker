---
title: BADBOX 僵尸网络再度崛起：19.2 万多台安卓设备遭入侵
url: https://www.anquanke.com/post/id/302834
source: 安全客-有思想的安全新媒体
date: 2024-12-20
fetch_date: 2025-10-06T19:36:02.028005
---

# BADBOX 僵尸网络再度崛起：19.2 万多台安卓设备遭入侵

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

# BADBOX 僵尸网络再度崛起：19.2 万多台安卓设备遭入侵

阅读量**82227**

|评论**1**

发布时间 : 2024-12-19 10:06:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/badbox-botnet-rises-again-192000-android-devices-compromised/>

译文仅供参考，具体内容表达以及含义原文为准。

BADBOX 僵尸网络又回来了，而且比以往任何时候都更加危险。这一网络犯罪活动原本被认为已经被瓦解，但现在不仅死灰复燃，而且规模不断扩大，已入侵全球超过 192,000 台基于 Android 的设备。Bitsight 安全研究公司的最新报告揭示了该僵尸网络死灰复燃、日益复杂的惊人细节。

BADBOX 是一种大规模恶意软件行动，直接在供应链层面入侵安卓设备，包括电视盒、智能手机和现在的高端智能电视。这意味着设备在到达消费者手中之前就已经感染了恶意软件，通常是通过被篡改的固件或预装的应用程序。

正如 Bitsight 所解释的那样，“这些设备成为复杂犯罪计划的受害者，它们要么在供应链中被篡改，要么被制造商出售，并在未经用户同意的情况下安装 APK。”

僵尸网络在最高峰时估计有 74,000 台设备，现在全球受感染的设备已超过 192,000 台，遥测数据显示这一数字还在稳步增长。与以往主要针对低成本、非品牌设备的活动不同，BADBOX 已将其覆盖范围扩大到 Yandex 4K QLED 智能电视和海信 Instawall T963 智能手机等高端设备。受感染设备最集中的国家是俄罗斯、中国、印度、白俄罗斯、巴西和乌克兰，美国和法国等国家也有残余活动。

BADBOX 恶意软件利用其在设备固件中的存在执行恶意活动，包括：

* **住宅代理**： 将被入侵的设备用作代理端点。
* **远程代码安装**： 允许威胁行为者在未经用户同意的情况下部署新的恶意软件模块。
* **广告欺诈和账户滥用**： 利用受感染设备进行欺诈活动。

恶意软件启动后会立即连接到命令与控制（C2）服务器，从而下载并执行新的有效载荷。Bitsight 的报告强调：“威胁行为者可以构建、下载和执行全新的有效载荷，以实施我们目前无法看到的新计划。”

BADBOX 感染凸显了与供应链受损相关的风险。Bitsight 指出，感染方法包括制造商的故意修改和开发或运输阶段的篡改。这些做法使检测对消费者和企业都极具挑战性。

该报告发现了Yandex 4K QLED智能电视与BADBOX C2域（coslogdydy[.]in）之间的通信。研究人员写道：“这是第一次看到大品牌智能电视与 BADBOX 命令和控制（C2）域进行如此大规模的直接通信。一天之内就检测到了来自 Yandex 设备的 10 万多个独立 IP。”

虽然德国等一些国家在瓦解僵尸网络方面取得了长足进步，最近已影响到 3 万台设备，但 BADBOX 在全球的传播仍是一项重大挑战。Bitsight 的研究人员在短短 24 小时内就在一个 BADBOX 域名上发现了漏洞，捕获了超过 16 万个独特的 IP 地址，凸显了该僵尸网络的庞大规模。

Bitsight 警告说：“您的数据不仅面临风险，还可能被用于牟利和掩护恶意操作。”

本文翻译自securityonline [原文链接](https://securityonline.info/badbox-botnet-rises-again-192000-android-devices-compromised/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302834](/post/id/302834)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/badbox-botnet-rises-again-192000-android-devices-compromised/)

如若转载,请注明出处： <https://securityonline.info/badbox-botnet-rises-again-192000-android-devices-compromised/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**5赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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