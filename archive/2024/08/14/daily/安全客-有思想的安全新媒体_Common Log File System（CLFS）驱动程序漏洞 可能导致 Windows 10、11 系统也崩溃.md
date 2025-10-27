---
title: Common Log File System（CLFS）驱动程序漏洞 可能导致 Windows 10、11 系统也崩溃
url: https://www.anquanke.com/post/id/299078
source: 安全客-有思想的安全新媒体
date: 2024-08-14
fetch_date: 2025-10-06T18:02:08.136983
---

# Common Log File System（CLFS）驱动程序漏洞 可能导致 Windows 10、11 系统也崩溃

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

# Common Log File System（CLFS）驱动程序漏洞 可能导致 Windows 10、11 系统也崩溃

阅读量**38374**

发布时间 : 2024-08-13 11:03:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/vulnerabilities-threats/clfs-bug-crashes-even-updated-windows-10-11-systems>

译文仅供参考，具体内容表达以及含义原文为准。

通用日志文件系统 （CLFS） 驱动程序中的一个简单的错误可以立即触发任何最新版本的 Windows 中臭名昭著的蓝屏死机。

CLFS 是一种用户模式和内核模式的日志服务，可帮助应用程序记录和管理日志。它也是黑客攻击的热门目标。

去年，在对其驱动程序进行实验时，Fortra的一名研究人员发现输入数据中对指定数量的验证不正确，这使他能够随意触发系统崩溃。他的概念验证 （PoC） 漏洞适用于所有经过测试的 Windows 版本（包括 10、11 和 Windows Server 2022），即使在最新的系统中也是如此。

“运行起来非常简单：运行一个二进制文件，调用一个函数，然后该函数会导致系统崩溃，”Fortra安全研发副总监Tyler Reguly解释道。为了证明它是多么简单，他补充说：“我可能不应该承认这一点，但是今天在从一个系统拖放它时，我不小心双击了它，我的服务器崩溃了。

## CLFS 的 BSoD

标记为 CVE-2024-6768 的根本问题与基本日志文件 （BLF） 有关，这是一种包含用于管理日志的元数据的 CLFS 文件。

CLFS.sys驱动程序似乎没有充分验证 BLF 中特定字段（“IsnOwnerPage”）中的数据大小。任何可以访问 Windows 系统的攻击者都可以制作一个包含错误大小信息的文件，实际上可以混淆驱动程序。然后，由于无法解决不一致问题，它会触发 KeBugCheckEx，该函数会触发蓝屏崩溃。

CVE-2024-6768 在 CVSS 量表上获得了“中等”的 6.8 分（满分 10 分）。它不会影响数据的完整性或机密性，也不会导致任何未经授权的系统控制。但是，它确实允许肆意崩溃，这可能会中断业务运营或可能导致数据丢失。

或者，正如 Reguly 所解释的那样，它可以与其他漏洞配对以产生更大的效果。“对于攻击者来说，这是一个很好的方式，可以掩盖他们的踪迹，或者在他们不应该这样做的地方关闭一项服务，我认为这就是真正的风险所在，”他说。“这些系统意外重启，[你]忽略了崩溃，因为它又回来了，现在没事了，但这可能是有人隐藏了他们的活动——隐藏了他们希望它重启的事实，以便新设置生效。

## 看不到修复

Fortra 于去年 12 月 20 日首次报告了其调查结果。Reguly说，经过几个月的反复，Microsoft在没有承认这是一个漏洞或应用修复程序的情况下就结束了他们的调查。因此，在撰写本文时，无论它们如何更新，它都会在 Windows 系统中持续存在。

最近几周，Windows Defender一直在将Fortra的PoC识别为恶意软件。但是，除了运行 Windows Defender 并尝试避免运行任何利用它的二进制文件之外，在 Microsoft 发布补丁之前，组织无法处理 CVE-2024-6768。

Dark Reading 已联系 Microsoft 就 CVE-2024-6768 提供意见。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/vulnerabilities-threats/clfs-bug-crashes-even-updated-windows-10-11-systems)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299078](/post/id/299078)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/vulnerabilities-threats/clfs-bug-crashes-even-updated-windows-10-11-systems)

如若转载,请注明出处： <https://www.darkreading.com/vulnerabilities-threats/clfs-bug-crashes-even-updated-windows-10-11-systems>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06

### 热门推荐

文章目录

* [CLFS 的 BSoD](#h2-0)
* [看不到修复](#h2-1)

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