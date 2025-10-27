---
title: Windows驱动程序零日漏洞允许攻击者远程获取系统访问权限
url: https://www.anquanke.com/post/id/304323
source: 安全客-有思想的安全新媒体
date: 2025-02-15
fetch_date: 2025-10-06T20:33:04.508714
---

# Windows驱动程序零日漏洞允许攻击者远程获取系统访问权限

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

# Windows驱动程序零日漏洞允许攻击者远程获取系统访问权限

阅读量**96248**

发布时间 : 2025-02-14 10:31:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/windows-driver-zero-day-vulnerability/>

译文仅供参考，具体内容表达以及含义原文为准。

在一个 Windows 驱动程序中发现了一个严重的零日漏洞，攻击者可利用该漏洞远程访问系统。

这个被标识为 CVE-2025-21418 的漏洞于 2025 年 2 月 11 日被披露，被归类为 “重要” 漏洞，其通用漏洞评分系统（CVSS）评分为 7.8。
该漏洞是一个基于堆的缓冲区溢出漏洞，属于常见弱点枚举（CWE）中的 CWE-122 类别。

该漏洞利用了驱动程序中的一个弱点，使攻击者能够将权限提升至系统（SYSTEM）级别。

这意味着如果攻击成功，攻击者可以完全控制受影响的系统。

微软的分析师确定，此漏洞的 CVSS 向量字符串为 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C，这表明攻击向量是本地的，但影响却很严重。

可利用性及受影响的系统

尽管该漏洞尚未公开披露，但已检测到有利用该漏洞的攻击行为。这表明攻击者已经知晓并正在利用这个漏洞。

该漏洞的临时评分为 7.2，略低一些，这反映了随着更多信息的出现，该威胁的性质也在不断变化。

这个漏洞影响范围广泛的 Windows 系统，包括 Windows 10、Windows 11 以及各种 Windows Server 版本。

微软已经为这些系统发布了安全更新，这对于降低风险至关重要。例如，Windows 11 24H2 版本和 Windows Server 2025 的更新中包含了标识符为 5051987 和 5052105 等的补丁。

为防范此漏洞，建议用户尽快安装最新的安全更新。微软 2025 年 2 月的 “补丁星期二” 更新中包含了针对该漏洞的修复程序。

用户应优先安装最新的安全补丁，以防止潜在的攻击。及时了解漏洞信息并及时应用更新对于维护系统安全至关重要。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/windows-driver-zero-day-vulnerability/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304323](/post/id/304323)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/windows-driver-zero-day-vulnerability/)

如若转载,请注明出处： <https://cybersecuritynews.com/windows-driver-zero-day-vulnerability/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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