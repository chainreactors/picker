---
title: mbNET.mini工业路由器发现严重漏洞，可能导致全面系统接管
url: https://www.anquanke.com/post/id/301009
source: 安全客-有思想的安全新媒体
date: 2024-10-18
fetch_date: 2025-10-06T18:49:54.530203
---

# mbNET.mini工业路由器发现严重漏洞，可能导致全面系统接管

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

# mbNET.mini工业路由器发现严重漏洞，可能导致全面系统接管

阅读量**74782**

发布时间 : 2024-10-17 13:57:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-vulnerabilities-found-in-mbnet-mini-industrial-routers-could-allow-for-full-system-takeover/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-45274 & CVE-2024-45275]()

CERT@VDE 发布的安全公告揭示了 mbNET.mini 工业路由器中的多个关键漏洞，该路由器是一种广泛使用的设备，专为安全远程访问工业机器和系统而设计。该路由器由 MB connect line 生产，对于远程管理设备至关重要，但这些新漏洞暴露了重大风险，允许远程代码执行（RCE）和未经授权的访问。

**公布的漏洞：**

* **CVE-2024-45274 （CVSS 9.8）：** 这个严重漏洞允许未经认证的攻击者通过 UDP 远程执行任意操作系统命令，从而有效地完全控制设备。
* **CVE-2024-45275（CVSS 9.8）：** mbNET.mini包含带有默认密码的硬编码用户账户，为攻击者提供了一个轻松入侵设备的途径，这加剧了漏洞的严重性。
* **CVE-2024-45271 （CVSS 8.4）：** 即使是本地攻击者也能利用该设备。该漏洞可通过部署恶意配置文件实现未经授权的权限升级。
* **CVE-2024-45273（CVSS 8.4）：** 薄弱的加密实施允许攻击者解密设备的配置文件，从而可能暴露敏感信息并为进一步攻击提供便利。
* **CVE-2024-45276（CVSS 7.5）：** 攻击者可在未经授权的情况下读取存储在“/tmp ”目录中的文件，从而可能泄露敏感数据。

**影响和补救措施：**

这些漏洞影响重大。成功利用可导致

* **完全接管系统：** 攻击者可完全控制 mbNET.mini 和任何连接的工业设备。
* **数据泄露：** 敏感的操作数据和配置文件可能被窃取或篡改。
* **运行中断：** 攻击者可能会破坏工业流程，导致停机和经济损失。

MB connect line 已在 2.3.1 版 mbNET.mini 固件中解决了这些漏洞。强烈建议用户立即更新设备，以降低被利用的风险。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-vulnerabilities-found-in-mbnet-mini-industrial-routers-could-allow-for-full-system-takeover/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301009](/post/id/301009)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-vulnerabilities-found-in-mbnet-mini-industrial-routers-could-allow-for-full-system-takeover/)

如若转载,请注明出处： <https://securityonline.info/critical-vulnerabilities-found-in-mbnet-mini-industrial-routers-could-allow-for-full-system-takeover/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
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