---
title: 新的 Android SpyAgent 恶意软件使用 OCR 窃取加密钱包恢复密钥
url: https://www.anquanke.com/post/id/299939
source: 安全客-有思想的安全新媒体
date: 2024-09-11
fetch_date: 2025-10-06T18:20:59.335624
---

# 新的 Android SpyAgent 恶意软件使用 OCR 窃取加密钱包恢复密钥

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

# 新的 Android SpyAgent 恶意软件使用 OCR 窃取加密钱包恢复密钥

阅读量**73163**

发布时间 : 2024-09-10 14:21:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-android-spyagent-malware-uses-ocr.html>

译文仅供参考，具体内容表达以及含义原文为准。

韩国的 Android 设备用户已成为一种新的移动恶意软件活动的目标，该活动提供了一种称为 **SpyAgent** 的新型威胁。

McAfee Labs 研究员 SangRyol Ryu 在一项分析中表示，该恶意软件“通过扫描设备上可能包含助记键的图像来瞄准助记键”，并补充说目标范围已扩大到包括英国。

该活动利用伪装成看似合法的银行、政府设施、流媒体和实用程序的虚假 Android 应用程序，试图诱骗用户安装它们。自今年年初以来，已检测到多达 280 个虚假应用程序。

这一切都始于带有诱杀链接的 SMS 消息，这些链接敦促用户以托管在欺骗性网站上的 APK 文件的形式下载有问题的应用程序。安装后，它们旨在请求侵入性权限以从设备收集数据。

这包括联系人、短信、照片和其他设备信息，所有这些都被泄露到威胁行为者控制下的外部服务器。

最显着的特点是它能够利用光学字符识别 （OCR） 来窃取助记词，助记词是指允许用户重新获得对其加密货币钱包的访问权限的恢复或助记词。

因此，未经授权访问助记词密钥可以让威胁行为者控制受害者的钱包并窃取其中存储的所有资金。

McAfee Labs 表示，命令和控制 （C2） 基础设施存在严重的安全漏洞，不仅允许在未经身份验证的情况下导航到网站的根目录，而且还暴露了从受害者那里收集的数据。

该服务器还托管一个管理员面板，该面板充当远程征用受感染设备的一站式商店。如果 Apple iPhone 设备运行 iOS 15.8.2，且面板内系统语言设置为简体中文 （“zh”），则表明该设备也可能以 iOS 用户为目标。

“最初，该恶意软件通过简单的 HTTP 请求与其命令和控制 （C2） 服务器进行通信，”Ryu 说。“虽然这种方法很有效，但安全工具也相对容易跟踪和阻止。”

“在一个重大的战术转变中，该恶意软件现在已经采用 WebSocket 连接进行通信。此升级允许与 C2 服务器进行更高效、实时的双向交互，并帮助它避免被基于 HTTP 的传统网络监控工具检测到。

至少自 2024 年 2 月以来，Group-IB 曝光了另一个称为 CraxsRAT 的 Android 远程访问木马 （RAT），该木马至少自 2024 年 2 月以来使用网络钓鱼网站针对马来西亚的银行用户。值得指出的是，此前也发现 CraxsRAT 活动不迟于 2023 年 4 月针对新加坡。

“CraxsRAT 是一个臭名昭著的 Android 远程管理工具 （RAT） 恶意软件系列，具有远程设备控制和间谍软件功能，包括键盘记录、执行手势、记录摄像头、屏幕和通话，”这家新加坡公司表示。

“下载包含 CraxsRAT 安卓恶意软件的应用程序的受害者将遇到凭据泄露和非法提款。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-android-spyagent-malware-uses-ocr.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299939](/post/id/299939)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-android-spyagent-malware-uses-ocr.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-android-spyagent-malware-uses-ocr.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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