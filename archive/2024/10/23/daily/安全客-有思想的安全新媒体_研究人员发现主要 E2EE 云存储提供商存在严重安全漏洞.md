---
title: 研究人员发现主要 E2EE 云存储提供商存在严重安全漏洞
url: https://www.anquanke.com/post/id/301138
source: 安全客-有思想的安全新媒体
date: 2024-10-23
fetch_date: 2025-10-06T18:48:29.274209
---

# 研究人员发现主要 E2EE 云存储提供商存在严重安全漏洞

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

# 研究人员发现主要 E2EE 云存储提供商存在严重安全漏洞

阅读量**66096**

发布时间 : 2024-10-22 11:17:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/researchers-discover-severe-security.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员在各种端到端加密（E2EE）云存储平台中发现了严重的加密问题，这些问题可能被利用来泄露敏感数据。

苏黎世联邦理工学院的研究人员乔纳斯-霍夫曼（Jonas Hofmann）和Kien Tuong Truong说：“这些漏洞的严重程度不一：在许多情况下，恶意服务器可以注入文件、篡改文件数据，甚至直接访问明文。值得注意的是，我们的许多攻击以同样的方式影响了多个提供商，揭示了独立加密设计中的共同失效模式。”

发现的弱点是对 Sync、pCloud、Icedrive、Seafile 和 Tresorit 等五大提供商进行分析的结果。所设计的攻击技术依赖于对手控制的恶意服务器，然后利用该服务器攻击服务提供商的用户。

云存储系统中发现的漏洞简述如下：

* 同步，恶意服务器可用于破坏上传文件的机密性，以及注入文件和篡改其内容
* pCloud，恶意服务器可被用来破坏上传文件的机密性，以及注入文件和篡改其内容
* Seafile，恶意服务器可用于加速用户密码的暴力破解，以及注入文件和篡改其内容
* Icedrive，恶意服务器可被用来破坏上传文件的完整性，以及注入文件和篡改其内容
* Tresorit：恶意服务器可用于在共享文件时提供非真实密钥，并篡改存储中的某些元数据。

这些攻击属于 10 大类之一，它们违反保密性、以文件数据和元数据为目标，并允许注入任意文件：

* 缺乏对用户密钥材料的验证（同步和 pCloud）
* 使用未经验证的公钥（Sync 和 Tresorit）
* 加密协议降级（Seafile）、
* 链接共享陷阱（同步）
* 使用未经验证的加密模式，如CBC（Icedrive和Seafile）
* 未经验证的文件分块（Seafile 和 pCloud）
* 篡改文件名和位置（同步、pCloud、Seafile和Icedrive）
* 篡改文件元数据（影响所有五个提供商）
* 通过结合元数据编辑攻击和利用共享机制中的怪癖，将文件夹注入用户的存储空间（Sync）
* 将恶意文件注入用户存储（pCloud）

“我们的攻击并非都是复杂的攻击，这意味着不一定精通密码学的攻击者也能做到。事实上，我们的攻击具有很强的实用性，不需要大量资源就能实施，”研究人员在随附的论文中说。

“此外，虽然从密码学的角度来看，其中一些攻击并不新颖，但它们强调了实际部署的 E2EE 云存储在微不足道的层面上就会失败，通常不需要更深入的密码分析就能破解。”

虽然 Icedrive 在 2024 年 4 月底负责任地披露了已发现的问题，但它选择不解决这些问题，Sync、Seafile 和 Tresorit 也承认了这份报告。黑客新闻》已分别联系了这几家公司，希望他们能发表进一步评论，如果有回复，我们将及时更新。

伦敦国王学院（King’s College London）和苏黎世联邦理工学院（ETH Zurich）的一组学者在六个多月前发现了针对 Nextcloud E2EE 功能的三种不同攻击，这些攻击可被滥用来破坏保密性和完整性保证。

研究人员当时表示：“这些漏洞使得恶意的Nextcloud服务器可以轻而易举地访问和操纵用户的数据，”他们强调，要解决这些问题，就必须将所有服务器行为和服务器生成的输入视为对抗性的。

早在 2022 年 6 月，苏黎世联邦理工学院的研究人员也展示了 MEGA 云存储服务中的一些关键安全问题，这些问题可能被用来破坏用户数据的保密性和完整性。

**各公司的回应**

**Icedrive** – 我们知道这篇研究论文。该论文描述了在 “被破坏的服务器 ”威胁模式下可能发生的攻击，即对手获得对文件服务器的完全控制权，可以修改或删除文件。论文还提到使用 MITM 服务器，该服务器必须能够解密 HTTPS/SSL 流量。

我们希望向用户保证，存储在我们服务器上的零知识加密数据不会有任何实际危险–不知道口令就无法解密。如果有人完全控制了文件服务器（这本身就不是一件容易的事）并篡改了用户的文件，我们的应用程序会使用文件完整性检查功能检测到这一情况，并不会解密文件，而是发出错误警告。

我们会不断改进我们的应用程序和服务，修复问题并添加新功能。我们将仔细审查我们的加密方法并进行更新，以符合当前的行业标准。

同步 – 我们的安全团队在 10 月 11 日发现了这些问题，并已迅速采取措施加以解决。我们还与研究团队进行了联系，以分享研究结果并合作制定下一步措施。

链接上的潜在数据泄漏问题（如报告所述）已得到修复，我们正在快速修复其余的潜在问题。正如研究论文所概述的那样，这些漏洞是以服务器被入侵为借口而存在的。没有证据表明这些漏洞已被利用或文件数据已被访问。

我们知道，使用 Sync 意味着对我们的信任。但端到端加密的承诺是，您不需要信任任何人，甚至不需要信任我们。这一理念是我们加密模式的核心，也是我们工作的核心。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/researchers-discover-severe-security.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301138](/post/id/301138)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/researchers-discover-severe-security.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/researchers-discover-severe-security.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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