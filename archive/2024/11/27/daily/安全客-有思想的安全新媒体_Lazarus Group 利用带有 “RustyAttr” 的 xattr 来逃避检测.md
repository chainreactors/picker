---
title: Lazarus Group 利用带有 “RustyAttr” 的 xattr 来逃避检测
url: https://www.anquanke.com/post/id/302179
source: 安全客-有思想的安全新媒体
date: 2024-11-27
fetch_date: 2025-10-06T19:12:22.534475
---

# Lazarus Group 利用带有 “RustyAttr” 的 xattr 来逃避检测

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

# Lazarus Group 利用带有 “RustyAttr” 的 xattr 来逃避检测

阅读量**51851**

发布时间 : 2024-11-26 10:47:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/lazarus-group-exploits-xattr-with-rustyattr-to-evade-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![RustyAttr]()

臭名昭著的朝鲜网络间谍组织 “拉扎罗斯集团”（Lazarus Group）的武器库中又多了一项隐蔽技术：在基于 Unix 的系统（如 macOS 和 Linux）中滥用 xattr（即扩展文件属性）。根据安全研究员 Tonmoy Jitu 的分析，这种被称为 RustyAttr 的方法利用 macOS 元数据隐藏恶意有效载荷，躲避传统检测工具和杀毒软件的攻击。

xattr 命令通常用于存储 Finder 标记或隔离标志等元数据，它还可以在不改变文件可见内容的情况下将二进制数据嵌入文件。虽然对合法目的有用，但它也为攻击者提供了隐藏恶意脚本的途径。正如 Jitu 解释的那样： “xattr 与 Windows 备用数据流（ADS）非常相似，它提供了一种在不改变文件可见内容的情况下将元数据嵌入文件的机制。”

据报道，由 Lazarus Group 开发的 RustyAttr 木马利用这种元数据在被入侵系统中持续存在。由于嵌入了扩展属性，它的恶意有效载荷可以绕过 macOS Gatekeeper 等传统文件扫描工具。Jitu 的分析强调了该木马的能力： “RustyAttr木马能够绕过文件系统的传统监控工具，直接从扩展属性中获取并执行恶意脚本。”

Jitu 对恶意文件 DD Form Questionnaire.zip 的调查揭示了 RustyAttr 的感染链。该木马隐藏在与应用程序文件（如 .app 捆绑程序）链接的元数据中。一个突出的发现是测试属性，它包含一个恶意 shell 命令，用于下载和执行其他有效载荷。

该过程包括：

1. **在元数据中嵌入命令**： 恶意 shell 命令存储在 com.example.hidden\_data 等属性中。
2. **执行隐藏有效载荷**： 这些命令会下载诱饵文件（如 PDF），并通过 AppleScript 执行 shell 脚本。该命令将 PDF 文件下载到特定位置……然后从 URL 获取 shell 脚本并通过 AppleScript 执行。
3. **通过泄漏的证书持久化**： 该木马最初使用泄露的证书签名，可绕过安全检查，直到证书被吊销。

与 RustyAttr 相关联的恶意基础架构进一步将其与 Lazarus Group 联系起来。Jitu 指出 “恶意 curl 命令中使用的域被标记为恶意域……与已知威胁行为者基础设施相关的 IP 地址相连。”

此外，该组织还采用了社会工程学策略，将 RustyAttr 伪装成合法的 PDF 文件或系统实用程序，诱骗用户执行。

尽管功能强大，但 RustyAttr 的技术仍未列入 MITRE ATT&CK Framework，这让防御者对这种微妙的攻击毫无准备。吉图强调了其中的风险： “通过将关键数据和有效载荷隐藏在文件元数据中，RustyAttr 可以躲避检测……允许攻击者长时间保持对被入侵系统的控制。”

本文翻译自securityonline [原文链接](https://securityonline.info/lazarus-group-exploits-xattr-with-rustyattr-to-evade-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302179](/post/id/302179)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lazarus-group-exploits-xattr-with-rustyattr-to-evade-detection/)

如若转载,请注明出处： <https://securityonline.info/lazarus-group-exploits-xattr-with-rustyattr-to-evade-detection/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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