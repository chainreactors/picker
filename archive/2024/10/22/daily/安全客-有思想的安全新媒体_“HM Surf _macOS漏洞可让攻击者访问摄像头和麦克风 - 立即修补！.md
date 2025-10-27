---
title: “HM Surf "macOS漏洞可让攻击者访问摄像头和麦克风 - 立即修补！
url: https://www.anquanke.com/post/id/301075
source: 安全客-有思想的安全新媒体
date: 2024-10-22
fetch_date: 2025-10-06T18:48:09.839804
---

# “HM Surf "macOS漏洞可让攻击者访问摄像头和麦克风 - 立即修补！

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

# “HM Surf "macOS漏洞可让攻击者访问摄像头和麦克风 - 立即修补！

阅读量**58927**

发布时间 : 2024-10-21 10:39:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Waqas，文章来源：hackread

原文地址：<https://hackread.com/hm-surf-macos-flaw-attackers-access-camera-mic/>

译文仅供参考，具体内容表达以及含义原文为准。

**微软的研究人员发现了一个新的 macOS 漏洞 “HM Surf”（CVE-2024-44133），它绕过了 TCC 保护，允许未经授权访问摄像头和麦克风等敏感数据。现在就打补丁以保持防护。**

Microsoft Threat Intelligence 的网络安全研究人员在 macOS 中发现的漏洞允许攻击者绕过操作系统的透明、同意和控制（TCC）技术，未经授权访问敏感的用户数据。

该漏洞被研究人员称为 “HM Surf”；研究人员警告说，该漏洞可能正在被主动利用。该漏洞已被指定为 CVE-2024-44133。

HM Surf 漏洞涉及移除 Safari 浏览器目录的 TCC 保护和修改配置文件，使攻击者能够在未经用户同意的情况下访问用户的浏览历史、摄像头、麦克风和位置。该漏洞非常严重，因为它还允许攻击者收集敏感信息并将其用于恶意目的。

**漏洞如何工作**

TCC 技术可防止应用程序在未经用户事先同意和不知情的情况下访问其个人信息。然而，HM Surf 漏洞利用了 TCC 保护 Safari 浏览器目录方式中的一个弱点。通过移除 TCC 保护并修改配置文件，攻击者可以访问敏感的用户数据。

微软在2024年10月18日发布前与Hackread.com共享的博文中检测到了与Adload（一种流行的macOS恶意软件（广告软件）家族）相关的 “潜在利用 ”活动。

该公司在 Microsoft Defender for Endpoint 中的行为监控保护发现了可疑活动，包括通过 HM Surf 或其他方法对偏好设置文件进行异常修改。

Bambenek Consulting 公司总裁 John Bambenek 对此发表了看法，敦促用户安装补丁并保存数据，尤其是视频。

约翰警告说：“从本质上讲，这是一个权限升级漏洞，需要在受害者机器上执行恶意指令，而运行恶意软件可以做到这一点，这里最明显的风险是针对家庭用户，试图捕捉受害者处于危险位置的视频，以便日后进行色情勒索。安全团队应该进行更新，然而，重要的是要有防御措施，从一开始就防止恶意软件进入机器。”

**苹果公司的回应**

作为 2024 年 9 月 16 日发布的 macOS Sequoia 安全更新的一部分，苹果发布了漏洞修复程序。该公司还为应用程序组容器引入了新的 API，使系统完整性策略（SIP）能够保护配置文件不被外部攻击者修改。

为了保护自己免受该漏洞的攻击，我们敦促 macOS 用户尽快应用安全更新。此外，用户在向应用程序授予权限时应谨慎行事，确保只在必要时才允许访问敏感信息。

**尽快安装补丁！**

HM Surf 漏洞的识别、报告和修补突出了一个关键点：跨平台威胁情报共享对未来的网络安全至关重要。企业和用户应安装苹果公司 9 月份发布的安全补丁。今后，建议在 macOS 设备上启用自动更新功能，以便通过新的安全更新自动解决此类威胁。

本文翻译自hackread [原文链接](https://hackread.com/hm-surf-macos-flaw-attackers-access-camera-mic/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301075](/post/id/301075)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hm-surf-macos-flaw-attackers-access-camera-mic/)

如若转载,请注明出处： <https://hackread.com/hm-surf-macos-flaw-attackers-access-camera-mic/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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