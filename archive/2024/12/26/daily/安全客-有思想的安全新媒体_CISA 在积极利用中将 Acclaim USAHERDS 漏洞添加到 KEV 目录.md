---
title: CISA 在积极利用中将 Acclaim USAHERDS 漏洞添加到 KEV 目录
url: https://www.anquanke.com/post/id/303000
source: 安全客-有思想的安全新媒体
date: 2024-12-26
fetch_date: 2025-10-06T19:36:08.718172
---

# CISA 在积极利用中将 Acclaim USAHERDS 漏洞添加到 KEV 目录

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

# CISA 在积极利用中将 Acclaim USAHERDS 漏洞添加到 KEV 目录

阅读量**85043**

|评论**1**

发布时间 : 2024-12-25 11:20:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/cisa-adds-acclaim-usaherds.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全和基础设施安全局（CISA）周一在已知漏洞（KEV）目录中增加了一个影响 Acclaim Systems USAHERDS 的高严重性安全漏洞，该漏洞已得到修补，但仍有证据表明该漏洞仍在被利用。

该漏洞名为 CVE-2021-44207（CVSS 得分：8.1），是 Acclaim USAHERDS 中的一个硬编码静态凭据漏洞，攻击者可利用该漏洞在易受影响的服务器上执行任意代码。

具体来说，它涉及在 7.4.0.1 及以前版本中使用静态 ValidationKey 和 DecryptionKey 值，这些值可被用于在运行应用程序的服务器上实现远程代码执行。也就是说，攻击者首先必须利用其他手段获取密钥。

“这些密钥用于为应用程序 ViewState 提供安全保护，”谷歌旗下的曼迪安特公司（Mandiant）在 2021 年 12 月针对该漏洞发布的公告中说。“掌握这些密钥的威胁行为者可以诱骗应用服务器反序列化恶意制作的 ViewState 数据。”

“知道网络应用程序验证密钥（validationKey）和解密密钥（decryptionKey）的威胁行为者可以构建一个恶意的 ViewState，该 ViewState 可以通过 MAC 检查并被服务器反序列化。这种反序列化可导致在服务器上执行代码。”

虽然没有关于 CVE-2021-44207 在现实世界攻击中被武器化的新报告，但该漏洞早在 2021 年就被与中国有关联的 APT41 威胁行为者确定为零日漏洞，并在针对美国六个州政府网络的攻击中被滥用。

建议联邦文职行政部门（FCEB）机构在 2025 年 1 月 13 日前应用供应商提供的缓解措施，以保护其网络免受主动威胁。

Adobe就ColdFusion（CVE-2024-53961，CVSS评分：7.8）中的一个关键安全漏洞发出警告，称该漏洞已存在一个已知的概念验证（PoC）漏洞，可导致任意文件系统读取。

该漏洞已在 ColdFusion 2021 Update 18 和 ColdFusion 2023 Update 12 中得到解决。建议用户尽快打上补丁，以降低潜在风险。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/cisa-adds-acclaim-usaherds.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303000](/post/id/303000)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/cisa-adds-acclaim-usaherds.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/cisa-adds-acclaim-usaherds.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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