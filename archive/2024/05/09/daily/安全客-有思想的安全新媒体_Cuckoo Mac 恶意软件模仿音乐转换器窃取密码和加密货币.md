---
title: Cuckoo Mac 恶意软件模仿音乐转换器窃取密码和加密货币
url: https://www.anquanke.com/post/id/296264
source: 安全客-有思想的安全新媒体
date: 2024-05-09
fetch_date: 2025-10-06T17:13:51.590336
---

# Cuckoo Mac 恶意软件模仿音乐转换器窃取密码和加密货币

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

# Cuckoo Mac 恶意软件模仿音乐转换器窃取密码和加密货币

阅读量**63572**

发布时间 : 2024-05-08 10:51:56

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.hackread.com/cuckoo-mac-malware-music-converter-passwords-crypto/>

译文仅供参考，具体内容表达以及含义原文为准。

Mac 安全提供商 Kandji 的网络安全研究人员发现了一种针对 macOS 用户的名为“Cuckoo”的新恶意软件。该恶意软件伪装成 Spotify 等音乐转换器应用程序，可以在基于 Intel 和 ARM 的 Apple Mac 电脑上运行。

研究人员于 2024 年 4 月 24 日发现了一个恶意 Mach-O 二进制文件，该二进制文件表现出间谍软件和信息窃取行为。其检查发现了一个名为“DumpMedia Spotify Music Converter”的文件，这是基于 Intel 或 ARM 的 Mac 计算机上的通用二进制文件。
[![Cuckoo Mac 恶意软件模仿音乐转换器窃取密码和加密货币]()](https://www.hackread.com/wp-content/uploads/2024/05/cuckoo-mac-malware-music-converter-passwords-crypto-2.jpg)从 dumpmediacom 下载 Spotify 版本时检测到该恶意软件。然后在其他网站上发现它有免费和付费版本。

Kandji 研究人员在博客文章中透露：“到目前为止，我们发现unesolocom、fonedogcom、tunesfuncom、tunefabcom 网站正在托管包含相同恶意软件的恶意应用程序。”

Cuckoo的欺骗策略
Cuckoo 声称可以将 Spotify 音乐转换为 MP3 格式，从而欺骗用户。安装后，它就会开始窃取数据，目标是 macOS 钥匙串、视觉证据、浏览历史记录、消息应用程序数据、加密货币钱包详细信息和身份验证凭据。

它通过请求用户打开应用程序来自行安装，无需经过审查的签名或开发人员 ID。它检查用户的位置并收集主机硬件信息。如果用户接受进一步的提示，则可以访问 Finder、麦克风和下载。

它的目标是什么？
Cuckoo 针对 macOS 的钥匙串（密码、登录凭据和加密密钥的存储库），从而危及在线帐户和敏感数据访问。

它窃取屏幕截图和网络摄像头快照，并针对 WhatsApp 和 Telegram 等消息应用程序，泄露用户的在线活动，并对数字资产所有者构成重大财务威胁。

研究人员发现 Cuckoo 将与 Safari、Notes 和 Keychain 相关的文件复制到临时位置，并创建感兴趣文件的路径。它每 60 秒运行一次启动代理以保持在计算机上的持久性。

背后是谁？
该活动并未明确归因于任何特定的威胁行为者，但研究人员指出，它保护了亚美尼亚、白俄罗斯、哈萨克斯坦、俄罗斯和乌克兰的设备。

此外，它还通过 LaunchAgent 建立持久性，这是 RustBucket、XLoader、JaskaGO 中的一个功能，以及与中国威胁参与者 ZuRu 相关的后门。该恶意软件是使用合法的中国开发者ID（易安科技深圳有限公司（VRBJ4VRP））进行签名的，所有捆绑包（除了fonedogcom上托管的捆绑包）均已签名。

为了保护自己免受 Cuckoo 和其他恶意软件威胁，请谨慎下载软件，避免不受信任的来源，仔细检查电子邮件和附件，并使用可靠的防病毒和反恶意软件解决方案。保持警惕和怀疑对于数字隐私和安全至关重要。

本文翻译自 [原文链接](https://www.hackread.com/cuckoo-mac-malware-music-converter-passwords-crypto/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296264](/post/id/296264)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.hackread.com/cuckoo-mac-malware-music-converter-passwords-crypto/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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