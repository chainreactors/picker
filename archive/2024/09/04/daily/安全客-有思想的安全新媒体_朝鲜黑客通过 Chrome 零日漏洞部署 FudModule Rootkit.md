---
title: 朝鲜黑客通过 Chrome 零日漏洞部署 FudModule Rootkit
url: https://www.anquanke.com/post/id/299731
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:55.510102
---

# 朝鲜黑客通过 Chrome 零日漏洞部署 FudModule Rootkit

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

# 朝鲜黑客通过 Chrome 零日漏洞部署 FudModule Rootkit

阅读量**109603**

发布时间 : 2024-09-03 14:22:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/north-korean-hackers-deploy-fudmodule.html>

译文仅供参考，具体内容表达以及含义原文为准。

最近修补的 Google Chrome 和其他 Chromium Web 浏览器中的安全漏洞被朝鲜行为者利用为零日漏洞，用于提供 FudModule rootkit。

这一发展表明了民族国家对手的不懈努力，近几个月来，它已经养成了将大量 Windows 零日漏洞纳入其武器库的习惯。

Microsoft 于 2024 年 8 月 19 日检测到该活动，并将其归因于其跟踪的威胁行为者 Citrine Sleet（以前称为 DEV-0139 和 DEV-1222），也称为 AppleJeus、Labyrinth Chollima、Nickel Academy 和 UNC4736。它被评估为 Lazarus 组（又名 Diamond Sleet 和 Hidden Cobra）中的一个子星团。

值得一提的是，卡巴斯基此前还将 AppleJeus 恶意软件的使用归因于另一个名为 BlueNoroff（又名 APT38、Nickel Gladstone 和 Stardust Chollima）的 Lazarus 子组，这表明这些威胁行为者之间共享基础设施和工具集。

“Citrine Sleet 总部位于朝鲜，主要针对金融机构，特别是管理加密货币的组织和个人，以获取经济利益，”Microsoft 威胁情报团队表示。

“作为其社会工程策略的一部分，Citrine Sleet 对加密货币行业和与之相关的个人进行了广泛的侦察。”

攻击链通常涉及建立伪装成合法加密货币交易平台的虚假网站，旨在诱骗用户安装武器化的加密货币钱包或交易应用程序，从而促进数字资产的盗窃。

Citrine Sleet 观察到的零日漏洞利用攻击涉及对 CVE-2024-7971 的利用，这是 V8 JavaScript 和 WebAssembly 引擎中的一个高严重性类型混淆漏洞，可能允许威胁行为者在沙盒 Chromium 渲染器进程中获得远程代码执行 （RCE）。它是由 Google 作为上周发布的更新的一部分修补的。

正如 The Hacker News 之前所说，CVE-2024-7971 是继 CVE-2024-4947 和 CVE-2024-5274 之后，Google 今年解决的 V8 中第三个被积极利用的类型混淆错误。

目前尚不清楚这些攻击的范围有多广，也不清楚谁是目标，但据说受害者已被定向到一个名为 voyagorclub[.] 的恶意网站。空间，从而触发 CVE-2024-7971 漏洞。

就其本身而言，RCE 漏洞为检索包含 Windows 沙盒逃逸漏洞 （CVE-2024-38106） 和 FudModule rootkit 的 shellcode 铺平了道路，该漏洞用于“建立对基于 Windows 的系统的管理员到内核访问，以允许读/写基元函数并执行 [直接内核对象操作]”。

CVE-2024-38106 是一个 Windows 内核权限提升错误，是 Microsoft 在其 2024 年 8 月补丁星期二更新中修复的六个积极利用的安全漏洞之一。也就是说，已发现与 Citrine Sleet 相关的漏洞利用发生在修复程序发布后。

“这可能表明存在’漏洞冲突’，即相同的漏洞由不同的威胁行为者独立发现，或者一个漏洞研究人员将漏洞知识分享给多个行为者，”Microsoft 表示。

CVE-2024-7971 也是继 CVE-2024-21338 和 CVE-2024-38193 之后，朝鲜威胁行为者今年利用的第三个漏洞来删除 FudModule rootkit，这两个漏洞都是两个内置 Windows 驱动程序（appid.sys 和 AFD.sys）中的权限提升缺陷，并由 Microsoft 于 2 月和 8 月修复。

“CVE-2024-7971 漏洞利用链依靠多个组件来破坏目标，如果这些组件中的任何一个被阻止，包括 CVE-2024-38106，这个攻击链就会失败，”该公司表示。

“零日漏洞不仅需要使系统保持最新状态，还需要安全解决方案，为整个网络攻击链提供统一的可见性，以检测和阻止入侵后的攻击者工具和利用后的恶意活动。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/north-korean-hackers-deploy-fudmodule.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299731](/post/id/299731)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/north-korean-hackers-deploy-fudmodule.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/north-korean-hackers-deploy-fudmodule.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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