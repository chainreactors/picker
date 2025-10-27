---
title: Android 恶意软件使用 NFC 在 ATM 机上窃取资金
url: https://www.anquanke.com/post/id/299438
source: 安全客-有思想的安全新媒体
date: 2024-08-24
fetch_date: 2025-10-06T18:01:10.546767
---

# Android 恶意软件使用 NFC 在 ATM 机上窃取资金

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

# Android 恶意软件使用 NFC 在 ATM 机上窃取资金

阅读量**42860**

发布时间 : 2024-08-23 11:19:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Help Net Security，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/08/22/android-malware-nfc-data-atm-withdrawals/>

译文仅供参考，具体内容表达以及含义原文为准。

ESET研究人员发现了NGate恶意软件，该恶意软件可以通过安装在其Android设备上的恶意应用程序将受害者支付卡中的数据中继到攻击者的rootAndroid手机。

![android malware NFC]( "Attack overview")

攻击概述（来源：ESET）

### 未经授权的自动柜员机取款

该活动针对银行的主要目标是为未经授权的ATM取款提供便利，这些取款人可以合法地从受害者的银行账户中取款。这是通过使用 NGate Android 恶意软件将受害者的实体支付卡的 NFC 数据通过他们受感染的 Android 智能手机中继到攻击者的设备来实现的。

然后，攻击者使用此数据执行 ATM 交易。如果此方法失败，攻击者就会有一个后备计划，将资金从受害者的账户转移到其他银行账户。

“我们还没有在任何以前发现的Android恶意软件中看到这种新颖的NFC中继技术。该技术基于一种名为NFCGate的工具，该工具由德国达姆施塔特工业大学的学生设计，用于捕获、分析或更改NFC流量;因此，我们将这个新的恶意软件家族命名为 NGate，“发现了这种新型威胁和技术的 Lukáš Štefanko 说。

### NGate Android 恶意软件活动

受害者在被欺骗后下载并安装了该恶意软件，以为他们正在与银行通信并且他们的设备遭到入侵。实际上，受害者在不知不觉中破坏了他们自己的 Android 设备，之前通过关于潜在纳税申报表的欺骗性短信中的链接下载和安装应用程序。

需要注意的是，NGate 从未在官方 Google Play 商店中提供过。

NGate Android 恶意软件与自 2023 年 11 月以来在捷克活动的威胁行为者的网络钓鱼活动有关。然而，ESET认为，在2024年3月逮捕一名嫌疑人后，这些活动被搁置了。ESET Research 首先注意到威胁行为者从 2023 年 11 月底开始针对捷克著名银行的客户。该恶意软件是通过冒充合法银行网站或 Google Play 商店中的官方移动银行应用程序的短期域传播的。

攻击者利用了渐进式 Web 应用程序 （PWA） 的潜力，但后来通过采用更复杂的 PWA 版本（称为 WebAPK）来改进其策略。最终，该行动最终以部署 NGate 恶意软件而告终。

### 收集个人信息

2024 年 3 月，ESET Research 发现 NGate Android 恶意软件在以前用于促进提供恶意 PWA 和 WebAPK 的网络钓鱼活动的分发域上可用。安装并打开后，NGate 会显示一个虚假网站，要求用户提供银行信息，然后将其发送到攻击者的服务器。

除了网络钓鱼功能外，NGate 恶意软件还附带一个名为 NFCGate 的工具，该工具被滥用于在两个设备之间中继 NFC 数据——受害者的设备和犯罪者的设备。其中一些功能仅适用于已获得 root 权限的设备;但是，在这种情况下，也可以从非 root 设备中继 NFC 流量。

NGate 还提示受害者输入敏感信息，例如他们的银行客户 ID、出生日期和银行卡的 PIN 码。它还要求他们在智能手机上打开 NFC 功能。然后，指示受害者将他们的支付卡放在智能手机的背面，直到恶意应用程序识别出该卡。

### 物理访问支付卡

除了 NGate 恶意软件使用的技术外，对支付卡具有物理访问权限的攻击者还可以复制和模拟它们。攻击者可能会使用这种技术，试图通过无人看管的钱包、钱包、背包或装有卡片的智能手机壳读取卡片，尤其是在公共和拥挤的地方。但是，这种情况通常仅限于在终端点进行小额非接触式支付。

“确保免受此类复杂攻击需要采取某些积极措施来应对网络钓鱼、社会工程和 Android 恶意软件等策略。这意味着检查网站的 URL、从官方商店下载应用程序、对 PIN 码保密、在智能手机上使用安全应用程序、在不需要时关闭 NFC 功能、使用保护套或使用受身份验证保护的虚拟卡，“Štefanko 建议道。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/08/22/android-malware-nfc-data-atm-withdrawals/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299438](/post/id/299438)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/08/22/android-malware-nfc-data-atm-withdrawals/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/08/22/android-malware-nfc-data-atm-withdrawals/>

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