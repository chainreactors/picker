---
title: RisePro：承诺提供免费破解软件作为诱饵
url: https://www.anquanke.com/post/id/294067
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:38.074059
---

# RisePro：承诺提供免费破解软件作为诱饵

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

# RisePro：承诺提供免费破解软件作为诱饵

阅读量**121174**

发布时间 : 2024-03-18 19:24:28

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/546827.php>

译文仅供参考，具体内容表达以及含义原文为准。

免费CCleaner、Daemon Tools 和 AVAST 被恶意软件用作诱饵。

安全研究人员在GitHub 上发现了多个存储库，这些存储库以流行软件的黑客版本为幌子传播恶意软件。

作为名为“gitgub”的恶意操作的一部分，德国G DATA 公司的专家发现了 与 11 个不同帐户相关的 17 个存储库，这些存储库长期分发信息窃取程序RisePro，该程序 于 2022 年 12 月首次出现在信息领域。

据专家称，所有恶意代码库已从 GitHub 上删除，以防止感染传播。

所有存储库都有非常相似的设计，包括一个“README.md”文件，其中承诺提供免费破解软件。为了增加合法性和相关性，攻击者使用 Unicode 字符系统 (U+1F7E2) 中的绿色圆圈来模拟状态指示器以及当前日期。

![]()存储库列表范围从音频增强软件到数据恢复和保护、系统优化和分区工具。特别引人注目的是“AVAST”、“AOMEI-Backupper”、“IObit-Smart-Defrag-Crack”、“Ccleaner”、“EaseUS-Partition-Master”、“Daemon-Tools”等存储库。这些名称和品牌为许多 Windows 用户所熟悉，自然而然地激发了他们中大多数人的信任。

恶意活动的受害者还被从看似合法的“digitalxnetwork[.]com”网站下载 RAR 存档的链接所吸引，并且需要“README.md”中的密码才能访问安装文件。

该恶意软件伪装成安装程序，大小为 699 MB，使专用工具的分析变得复杂，但实际上仅包含 3.43 MB 的有用数据。该数据用作注入 RisePro 恶意软件版本 1.6 的加载程序。

与此同时，用 C++ 编写的 RisePro 专门从受感染的主机收集敏感信息并将其导出到攻击者的 Telegram 频道。

据 Specops 称，RedLine、Vidar 和 Raccoon 等数据窃取程序正变得越来越流行，并且往往是勒索软件攻击和其他严重数据安全漏洞的主要载体。在过去六个月中，仅 RedLine 就窃取了超过 1.7 亿个密码。

反过来，Flashpoint 专家 强调 ，当前信息窃取恶意软件的流行程度清楚地提醒人们，数字威胁正在不断演变。与此同时，黑客使用此类软件的主要动机几乎总是对经济利益的渴望，而此类工具的可用性和易用性只会不断增长。

本文翻译自 [原文链接](https://www.securitylab.ru/news/546827.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294067](/post/id/294067)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/546827.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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