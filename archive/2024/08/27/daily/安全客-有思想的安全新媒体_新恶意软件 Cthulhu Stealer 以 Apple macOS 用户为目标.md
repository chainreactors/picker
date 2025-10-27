---
title: 新恶意软件 Cthulhu Stealer 以 Apple macOS 用户为目标
url: https://www.anquanke.com/post/id/299490
source: 安全客-有思想的安全新媒体
date: 2024-08-27
fetch_date: 2025-10-06T18:00:48.637066
---

# 新恶意软件 Cthulhu Stealer 以 Apple macOS 用户为目标

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

# 新恶意软件 Cthulhu Stealer 以 Apple macOS 用户为目标

阅读量**59173**

发布时间 : 2024-08-26 14:24:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167454/malware/cthulhu-stealer-targets-apple-macos.html>

译文仅供参考，具体内容表达以及含义原文为准。

## Cato Security 发现了一个名为 Cthulhu Stealer 的新信息窃取程序，它以 Apple macOS 为目标并窃取了大量信息。

Cado Security 研究人员发现了一种针对 macOS 用户的恶意软件即服务 （MaaS），称为 Cthulhu Stealer。

**Cthulhu Stealer** 通过伪装成合法软件的 Apple 磁盘映像 （DMG） 以 macOS 用户为目标。研究人员发现 Cthulhu Stealer 冒充 Adobe GenP、CleanMyMac 和 Grand Theft Auto IV 等合法软件的磁盘映像。

恶意代码是用 GoLang 编写的，挂载 dmg 后，它会提示用户使用 macOS 工具输入他们的系统和 MetaMask 密码。

![克苏鲁窃贼]()

一旦用户输入了他们的凭据，恶意软件就会将它们存储在一个目录中，并使用 Chainbreak 转储钥匙串密码。然后，恶意软件会创建被盗数据的 zip 存档，其中包括系统和网络信息，并向命令和控制 （C2） 服务器发送通知。该恶意软件还会收集系统信息，包括 IP 地址和硬件/软件信息。

*“Cthulhu Stealer 的主要功能是从各种商店（包括游戏帐户）窃取凭据和加密货币钱包。如图 10 所示，有多个检查器功能可以检查目标文件存储的安装文件夹，通常在“Library/Application Support/[file store]”中。“在 /Users/Shared/NW 中创建一个目录，并将安装文件夹的内容转储到每个存储的文本文件中。”*

该恶意软件可以从广泛的来源窃取各种类型的信息。其中包括浏览器 cookie，它可以让攻击者访问用户会话和存储的密码，以及众多加密货币钱包，例如 Coinbase、MetaMask、Wasabi、Binance、Daedalus、Electrum、Atomic、Harmony、Enjin、Hoo、Dapper、Coinomi、Trust、Blockchain 和 XDeFI 钱包，突出了恶意软件专注于利用金融数据。

此外，该恶意软件针对特定的应用程序和服务，从 Telegram 的 Tdata 帐户信息、Minecraft 用户帐户甚至 Battlenet 中的游戏相关文件中窃取数据，这表明它有可能破坏个人和游戏活动。该恶意软件还可以转储 Keychain 和 SafeStorage 密码。

Cthulhu Stealer 与 Atomic Stealer 信息窃取程序具有相似的功能和特性，导致专家推测它可能是由同一开发人员创建的。这两个窃取者都使用 macOS 命令行工具 *osascript* 提示用户输入密码，甚至在提示中包含相同的拼写错误。

Cthulhu Stealer 的开发人员和附属公司以 Cthulhu 团队的身份运营，通过 Telegram 进行通信，并以每月 500 美元的价格出租他们的恶意软件。

附属公司负责部署恶意软件并从主要开发人员那里获得一定比例的收入。Cthulhu Stealer 已在两个知名恶意软件市场上出售，并在 Telegram 上做广告。然而，在 2024 年，附属公司开始抱怨没有收到付款，指责被称为“Cthulhu”或“Balaclavv”的开发商是骗子。这导致开发人员被永久禁止进入市场。

*“总之，虽然 macOS 长期以来一直被认为是一个安全的系统，但针对 Mac 用户的恶意软件的存在仍然是一个日益严重的安全问题。尽管 Cthulhu Team 似乎不再活跃，但这提醒我们 Apple 用户也不能免受网络威胁。保持警惕并谨慎行事至关重要，尤其是在安装来自非官方来源的软件时。“报告总结道。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167454/malware/cthulhu-stealer-targets-apple-macos.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299490](/post/id/299490)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167454/malware/cthulhu-stealer-targets-apple-macos.html)

如若转载,请注明出处： <https://securityaffairs.com/167454/malware/cthulhu-stealer-targets-apple-macos.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [Cato Security 发现了一个名为 Cthulhu Stealer 的新信息窃取程序，它以 Apple macOS 为目标并窃取了大量信息。](#h2-0)

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