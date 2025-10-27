---
title: Wi-Fi 标准中的缺陷可能导致 SSID 混淆攻击
url: https://www.anquanke.com/post/id/296552
source: 安全客-有思想的安全新媒体
date: 2024-05-17
fetch_date: 2025-10-06T17:14:25.136015
---

# Wi-Fi 标准中的缺陷可能导致 SSID 混淆攻击

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

# Wi-Fi 标准中的缺陷可能导致 SSID 混淆攻击

阅读量**110495**

发布时间 : 2024-05-16 12:12:33

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybersecuritynews.com/5-common-phishing-vectors/>

译文仅供参考，具体内容表达以及含义原文为准。

比利时鲁汶大学的研究人员发现了 IEEE 802.11 Wi-Fi 标准中的一个基本设计缺陷，该缺陷为攻击者提供了一种方法来诱骗受害者连接到比他们想要连接的网络安全性较低的无线网络。
根据 VPN 评论网站 Top10VPN 的说法，此类攻击可能会使受害者面临更高的流量拦截和操纵风险。该网站与 KU Leuven 的一位研究人员合作，于本周在韩国首尔即将举行的会议上进行演示之前发布了漏洞详细信息。
**设计缺陷**
该漏洞编号为CVE-2023-52424，影响所有操作系统上的所有 Wi-Fi 客户端。受影响的 Wi-Fi 网络包括基于广泛部署的 WPA3 协议、WEP 和 802.11X/EAP 的网络。研究人员提出了 Wi-Fi 标准的更新以及个人和组织可以用来降低风险的方法。
鲁汶大学研究人员 Héloïse Gollier 和 Mathy Vanhoef 在论文中表示：“在本文中，我们证明客户端可能会被诱骗连接到与其想要连接的不同的受保护 Wi-Fi 网络。” “也就是说，客户端的用户界面将显示与其所连接的实际网络不同的 SSID。”
Vanhoef 是 KU Leuven 的教授，他之前的工作包括发现几个值得注意的 Wi-Fi 漏洞和漏洞，例如WPA3 中的 Dragonblood、涉及 WPA2 的所谓Krack 密钥重新安装攻击以及VPN 客户端中的 TunnelCrack 漏洞。
两位研究人员发现的新 Wi-Fi 设计缺陷的根本原因在于，IEEE 802.11 标准并不总是要求在客户端连接到网络时对网络的服务集标识符（或 SSID）进行身份验证。 SSID 唯一地标识无线接入点和网络，以便与附近的其他接入点和网络区分开来。
研究人员写道：“现代 Wi-Fi 网络依靠四次握手来验证自身和客户端的身份，并协商密钥来加密连接。” “四次握手需要一个共享的成对主密钥 (PMK)，根据 Wi-Fi 版本和所使用的特定身份验证协议，可以以不同方式派生该密钥。”
问题在于 IEEE 802.11 标准不强制要求将 SSID 包含在密钥派生过程中。换句话说，SSID 并不总是客户端设备连接到 SSID 时发生的身份验证过程的一部分。在这些实施中，攻击者有机会设置恶意接入点，欺骗受信任网络的 SSID，并用它来将受害者降级到不太受信任的网络。
**开发条件**
攻击者需要满足某些条件才能利用该弱点。它仅适用于组织可能拥有两个具有共享凭据的 Wi-Fi 网络的情况。例如，当环境可能具有 2.4 GHz 网络和单独的 5 GHz 频段，每个频段具有不同的 SSID 但具有相同的身份验证凭据时，就会发生这种情况。通常，客户端设备会连接到安全性更好的 5 GHz 网络。但是，距离目标网络足够近以执行中间人攻击的攻击者可能会使用与 5 GHz 频段相同的 SSID 来攻击恶意接入点。然后，他们可以使用恶意接入点接收所有身份验证帧并将其转发到较弱的 2.4 GHz 接入点，并让客户端设备连接到该网络。
研究人员表示，这种降级可能会使受害者面临更高的已知攻击（例如 Krack 和其他威胁）的风险。值得注意的是，在某些情况下，它还可能使 VPN 保护失效。研究人员表示：“许多 VPN，例如 Clouldflare 的 Warp、hide.me 和 Windscribe，在连接到受信任的 Wi-Fi 网络时可以自动禁用 VPN。”他们指出，这是因为 VPN 可以根据 SSID 识别 Wi-Fi 网络。
研究人员表示，建立报告所描述的多通道中间人存在对于所有现有的 Wi-Fi 实施都是可行的。
Top10VPN 指出了针对研究人员描述的 SSID 混淆攻击的三种防御措施。其中之一是更新 IEEE 802.11 标准，强制执行 SSID 身份验证。另一个是更好地保护接入点定期传输的信标以通告其存在，以便连接的客户端可以检测到 SSID 何时发生变化。第三是避免不同 SSID 之间的凭证重复使用。

本文翻译自 [原文链接](https://cybersecuritynews.com/5-common-phishing-vectors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296552](/post/id/296552)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybersecuritynews.com/5-common-phishing-vectors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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