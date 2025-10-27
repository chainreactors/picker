---
title: 网络攻击者在窃取活动中利用 Microsoft SmartScreen 漏洞
url: https://www.anquanke.com/post/id/298375
source: 安全客-有思想的安全新媒体
date: 2024-07-26
fetch_date: 2025-10-06T17:40:23.835149
---

# 网络攻击者在窃取活动中利用 Microsoft SmartScreen 漏洞

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

# 网络攻击者在窃取活动中利用 Microsoft SmartScreen 漏洞

阅读量**72543**

发布时间 : 2024-07-25 15:00:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/vulnerabilities-threats/cyberattackers-exploit-microsoft-smartscreen-bug-in-stealer-campaign>

译文仅供参考，具体内容表达以及含义原文为准。

2 月份修补的 Microsoft Defender SmartScreen 漏洞仍在全球范围内用于信息窃取攻击。

CVE-2024-21412 是 SmartScreen 中一个严重性为“高”的 CVSS 评分为 8.1 的安全绕过漏洞，于 2 月 13 日首次披露并修复。从那时起，它已被用于涉及 Lumma Stealer、Water Hydra 和 DarkGate 等知名信息窃取者的活动。

现在，五个月后，Fortinet 标记了另一个涉及另外两个偷窃者的活动：Meduza 和 ACR。到目前为止，袭击已经到达美国、西班牙和泰国。

有时，组织会花时间更新第三方软件。相比之下，“在这种情况下，攻击者正在利用 Microsoft Windows 上的原生软件，这些软件将在正常的 Microsoft 补丁周期内更新，”Fortinet 全球安全策略师兼研究员 Aamir Lakhani 指出。“当这些漏洞没有得到修补时，这有点不清楚和令人担忧，因为这可能表明还有其他Microsoft漏洞也没有得到修补。

## CVE-2024-21412攻击链

如果您访问的网站或下载的文件或程序已知不安全，或者由于任何其他原因而可疑，SmartScreen 将介入并向您显示著名的蓝屏消息：“Windows 保护了您的电脑。这是一种简单、有效的方法，可以提醒用户注意潜在危险的网络威胁。

因此，请考虑一下，如果攻击者可以简单地禁用该通知，那么对他们有多大用处。这就是 CVE-2024-21412 允许他们做的事情。

在 Fortinet 确定的最新活动中，攻击者正在“通过结合 PowerShell 诡计和在图像中隐藏攻击并利用这些图像的处理方式”击败 SmartScreen，Lakhani 解释说。

首先，他们通过触发快捷方式 （LNK） 文件下载的 URL 引诱受害者。LNK 下载带有 HTML 应用程序 （HTA） 脚本的可执行文件，其中包含用于检索诱饵 PDF 文件和恶意代码注入器的 PowerShell 代码。

其中一个喷油器比另一个更有趣。在运行反调试检查后，它会下载一个 JPG 图像文件，然后使用 Windows API 访问其像素并解码其字节，其中隐藏着恶意代码。

“这些类型的基于图像的攻击已经存在了很长时间，虽然它们不像我们通常观察到的其他类型的攻击那样常见，但我们仍然看到它们随着时间的推移而出现，因为它们非常有效，”Lakhani指出。“看到这种攻击并不奇怪，特别是因为与其他攻击场景相比，[隐写术]检测经常被忽视。”

## 对未修补的后果

在这种情况下，通过图像文件走私进来的窃取者被植入合法的 Windows 进程中，此时数据的收集和泄露开始。

他们所针对的信息种类很广泛。例如，ACR 从数十种浏览器（Google Chrome、Firefox）、数十种加密钱包（Binance、Ledger Live）、信使应用程序（Telegram、WhatsApp）、密码管理器（Bitwarden、1Password）、虚拟专用网络 （VPN） 应用程序、电子邮件客户端、文件传输协议 （FTP） 客户端等中窃取。

只有远远落后于标准 Windows 补丁的组织才需要担心。不过，显然，这些组织就在那里。

Lakhani说：“我能理解小公司的个别软件更新可能会被遗漏，但大多数组织都会定期更新Microsoft软件补丁，而且这个特殊的漏洞仍然容易受到攻击。为了鼓励更好的补丁实践，他补充说，“我认为在所有情况下，软件供应商都需要向用户发出警报和通知，告知存在关键的安全补丁，并且应该在启动或使用软件时安装。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/vulnerabilities-threats/cyberattackers-exploit-microsoft-smartscreen-bug-in-stealer-campaign)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298375](/post/id/298375)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/vulnerabilities-threats/cyberattackers-exploit-microsoft-smartscreen-bug-in-stealer-campaign)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/cyberattackers-exploit-microsoft-smartscreen-bug-in-stealer-campaign>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25

### 热门推荐

文章目录

* [CVE-2024-21412攻击链](#h2-0)
* [对未修补的后果](#h2-1)

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