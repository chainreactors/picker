---
title: “有缺陷”的 Foxit PDF Reader 设计使用户容易受到攻击
url: https://www.anquanke.com/post/id/296555
source: 安全客-有思想的安全新媒体
date: 2024-05-17
fetch_date: 2025-10-06T17:14:24.417033
---

# “有缺陷”的 Foxit PDF Reader 设计使用户容易受到攻击

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

# “有缺陷”的 Foxit PDF Reader 设计使用户容易受到攻击

阅读量**106641**

发布时间 : 2024-05-16 12:15:12

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/news/foxit-pdf-reader-exploit/>

译文仅供参考，具体内容表达以及含义原文为准。

Check Point Research 发现 PDF 漏洞正在广泛传播，主要针对 Foxit Reader 用户。通过触发安全警告，毫无戒心的用户可能会被欺骗执行有害命令。

许多威胁参与者已经在利用该漏洞，该漏洞利用了“福昕阅读器中警告消息的设计缺陷”。

当用户打开已更改的 PDF 文件时，该漏洞会触发安全警告。如果粗心的用户两次使用默认选项（这是最有害的），该漏洞就会从远程服务器下载并执行有效负载。

研究人员表示：“感染成功且检测率低，使得恶意 PDF 可以通过许多非传统方式（例如 Facebook）进行传播，而不会被任何检测规则阻止。”

![]()
该漏洞的用途广泛，从间谍活动到具有多个链接和工具的电子犯罪，可实现令人印象深刻的攻击链。

在一个实例中，标记为 APT-C-35 / DoNot Team 的威胁参与者获得了针对 Windows 和 Android 设备执行混合活动的能力，“这也导致了双因素身份验证 (2FA) 绕过”。

研究人员表示：“各种网络犯罪行为者也利用了这一漏洞，传播最著名的恶意软件系列，例如 VenomRAT、Agent-Tesla、Remcos、NjRAT、NanoCore RAT、Pony、Xworm、AsyncRAT、DCRat。”

在一次恶意活动中，Check Point 跟踪了通过 Facebook 分发的链接，这导致了很长的攻击链，最终丢失了一名信息窃取者和两名加密货币矿工。另一项活动是由威胁参与者 @silentkillertv 发起的，他利用了两个链接的 PDF 文件，其中一个托管在合法网站 trello.com 上

“Check Point 获得了攻击者拥有的多个构建器，这些构建器利用此漏洞创建恶意 PDF 文件。收集到的大多数 PDF 都在执行 PowerShell 命令，该命令从远程服务器下载有效负载然后执行，尽管在某些情况下使用了其他命令，”报告中写道。

研究人员将此 PDF 漏洞归类为针对 Foxit PDF Reader 用户的网络钓鱼或社会工程形式，而不是典型的恶意活动。恶意行为者需要诱骗用户习惯性地单击“确定”，而不了解所涉及的潜在风险。

Foxit Reader承认了该问题，并向Check Point表示将在2024 3版本中解决该问题。同时，建议用户在打开未知来源的PDF文件时注意并谨慎行事。

本文翻译自 [原文链接](https://cybernews.com/news/foxit-pdf-reader-exploit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296555](/post/id/296555)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/news/foxit-pdf-reader-exploit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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