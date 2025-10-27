---
title: 新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据
url: https://www.anquanke.com/post/id/301663
source: 安全客-有思想的安全新媒体
date: 2024-11-09
fetch_date: 2025-10-06T19:14:25.987303
---

# 新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

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

# 新型 SteelFox 恶意软件冒充流行软件窃取浏览器数据

阅读量**70121**

发布时间 : 2024-11-08 14:25:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/steelfox-malware-software-to-steal-browser-data/>

译文仅供参考，具体内容表达以及含义原文为准。

**SteelFox 恶意软件通过伪造激活工具、窃取信用卡数据和部署加密矿工来打击软件盗版者。了解影响全球用户的这一新威胁，以及如何保护自己免受这一复杂网络犯罪活动的侵害。**

Securelist 的网络安全研究人员发现了一种新型恶意软件，这种恶意软件通过在线论坛、torrent 跟踪器和博客传播，冒充福昕 PDF 编辑器、AutoCAD 和 JetBrains 等合法软件。

研究人员称其为 “SteelFox”，该恶意软件的主要目标是那些参与下载盗版软件和虚假软件激活工具（破解版）的Microsft Windows用户。

该活动始于 2023 年 2 月，通过伪造软件激活工具将加密货币挖掘和数据窃取功能结合在一起。到目前为止，该恶意软件已经感染了全球 11,000 多名用户。

根据 Securelist 在发布前与 Hackread.com 分享的博文，SteelFox 是一个全功能的 “犯罪软件包”，可以从受感染的设备中提取敏感数据，包括信用卡信息、浏览历史和登录凭证。它还会收集系统信息，如安装的软件、运行的服务和网络配置。

恶意软件的初始攻击载体是虚假的软件激活程序，这些程序在在线论坛和洪流跟踪器上被宣传为可以免费激活合法软件。安装后，恶意软件会创建一个服务，即使在重启后也会留在系统中，并使用易受攻击的驱动程序来提高其权限。

![New SteelFox Malware Posing as Popular Software to Steal Browser Data]()恶意程序广告（通过 Securelist）

该恶意软件通过多阶段攻击链运行，首先是一个需要管理员权限的驱动程序。执行后，它会将自己安装为 Windows 服务，并使用 AES-128 加密来隐藏其组件。该恶意软件通过利用易受攻击的驱动程序实现系统级访问，并通过 SSL pinning 实现 TLS 1.3，以便与其命令服务器进行安全通信。

“SteelFox “高度复杂地使用了现代C++语言和外部库，这赋予了该恶意软件强大的威力。TLSv1.3 和 SSL pinning 的使用确保了安全通信和敏感数据的采集。

安全列表

**全球影响**

SteelFox似乎并不针对特定的个人或组织，而是在更大范围内感染尽可能多的用户。该恶意软件已经感染了 10 多个国家的用户，其中包括以下国家：

* **阿联酋**
* **印度**
* **巴西**
* **中国**
* **俄罗斯**
* **埃及**
* **阿尔及利亚**
* **墨西哥**
* **越南**
* **斯里兰卡**

KnowBe4 的安全意识倡导者 James McQuiggan 强调了企业谨慎对待软件下载来源的重要性。他还强调了通过网络安全意识计划培训员工的必要性。

“SteelFox下载器的双重功能–同时提供软件 “破解 ”和恶意软件–表明了网络犯罪分子使用的复杂工具，并使用过时的驱动程序进行权限升级，这凸显了企业确保实施补丁的迫切需要。”

詹姆斯解释说：“企业必须确保验证软件来源，保持最少的用户权限访问控制，并利用端点保护来检测可疑的安装行为。”

“此外，更重要的是，确保向用户提供网络安全意识计划，让他们了解未经验证的软件（如开源软件或这些常见的应用程序）的危险性。允许 IT 管理软件解决方案安装和监控所有应用程序，”他建议说。

**防范SteelFox**

为避免成为SteelFox的受害者，用户应只从官方渠道下载软件，并使用可靠的安全解决方案，以检测和防止受感染软件的安装。此外，用户在点击不明来源的链接或下载附件时应谨慎，因为这些链接或附件往往会被用来传播恶意软件。

本文翻译自hackread [原文链接](https://hackread.com/steelfox-malware-software-to-steal-browser-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301663](/post/id/301663)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/steelfox-malware-software-to-steal-browser-data/)

如若转载,请注明出处： <https://hackread.com/steelfox-malware-software-to-steal-browser-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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