---
title: SpyNote 恶意软件：虚假防病毒软件在复杂的新活动中以 Android 用户为目标
url: https://www.anquanke.com/post/id/301691
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:22.720857
---

# SpyNote 恶意软件：虚假防病毒软件在复杂的新活动中以 Android 用户为目标

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

# SpyNote 恶意软件：虚假防病毒软件在复杂的新活动中以 Android 用户为目标

阅读量**69937**

发布时间 : 2024-11-11 14:22:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/spynote-malware-fake-antivirus-targets-android-users-in-sophisticated-new-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

![SpyNote malware]()

来自 Cyfirma 的最新报告详细描述了 SpyNote 的死灰复燃，这是一种高度先进的安卓恶意软件，它冒充伪造的杀毒应用程序，专门伪装成 “Avast Mobile Security for Android ”来欺骗用户。这种恶意软件会伪装自己、获取权限并在设备上保持持久存在，使其能够进行广泛的数据窃取、监视和指挥控制操作。

SpyNote 采用了一种巧妙的策略来引诱用户授予权限。一旦安装，它就会显示自己为 “Avast Mobile Security”，并配有一个看起来合法的图标。根据 Cyfirma 的说法，“SpyNote 利用可访问性权限，将自己广泛的控制权授予设备，包括将自己排除在电池优化之外”。通过模拟用户操作，它可以在用户不知情的情况下悄悄地在后台授予自己更多权限，从而实现对位置跟踪、摄像头访问和信息阅读等敏感功能的控制。

一旦 SpyNote 获得权限，它就会开始拦截和收集数据。Cyfirma 的报告强调了它的功能，指出 “SpyNote 会收集数据，如外部存储（sdcard）上的凭证，并在稍后删除它们以消除痕迹”。该恶意软件积极寻求从其他应用程序中窃取凭证、加密货币钱包详情和数据，以流行品牌为目标，并通过利用特定设备的漏洞最大限度地扩大其影响范围。

SpyNote 还试图与其命令控制服务器保持开放的通信渠道。Cyfirma 观察到 “发送到 C2 的 SYN 请求（45[.]94[.]31[.]96[:]7544）”，这表明即使服务器处于离线状态，它仍在不断尝试重新连接。

SpyNote 具有多种自我防御功能，旨在阻止清除。Cyfirma 解释说，如果用户试图删除它，“恶意软件会使用可访问性功能模拟用户的触摸手势，阻止用户执行这些操作”。此外，它还会显示有关虚假系统更新的误导性通知，创建一个持续的无声通知，在误导用户的同时强化其在设备上的存在。

SpyNote 能够伪装自己、获得广泛控制并在受感染设备上持续存在，这凸显了移动恶意软件不断发展的复杂性。Cyfirma 强调了提高网络安全意识的必要性，建议用户谨慎使用不熟悉的应用程序，并加强合法杀毒解决方案的重要性，以应对 SpyNote 等威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/spynote-malware-fake-antivirus-targets-android-users-in-sophisticated-new-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301691](/post/id/301691)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/spynote-malware-fake-antivirus-targets-android-users-in-sophisticated-new-campaign/)

如若转载,请注明出处： <https://securityonline.info/spynote-malware-fake-antivirus-targets-android-users-in-sophisticated-new-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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