---
title: 美国 CISA 将 TeleMessage TM SGNL 添加到其已知利用漏洞目录中
url: https://www.anquanke.com/post/id/307345
source: 安全客-有思想的安全新媒体
date: 2025-05-14
fetch_date: 2025-10-06T22:23:17.389363
---

# 美国 CISA 将 TeleMessage TM SGNL 添加到其已知利用漏洞目录中

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

# 美国 CISA 将 TeleMessage TM SGNL 添加到其已知利用漏洞目录中

阅读量**58830**

发布时间 : 2025-05-13 15:43:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/177743/hacking/u-s-cisa-adds-telemessage-tm-sgnl-to-its-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 美国网络安全和基础设施安全局 (CISA) 将 TeleMessage TM SGNL 漏洞添加到其已知被利用的漏洞目录中。

美国网络安全和基础设施安全局 (CISA) 将 TeleMessage TM SGNL 漏洞（编号为CVE-2025-47729，CVSS 评分为 1.9）添加到其已知被利用漏洞 (KEV) 目录中。

*安全公告中指出，“TeleMessage 归档后端将保留到 2025 年 5 月 5 日，其中包含来自 TM SGNL（又名 Archive Signal）应用程序用户的消息的明文副本，这与 TeleMessage 文档中描述的功能不同，该文档中描述了“从手机到公司档案的端到端加密”，而该文档在 2025 年 5 月已被广泛利用。”*

上周，一名黑客窃取了 TeleMessage 的客户数据，TeleMessage 是一家以色列公司，向美国政府出售 Signal 和 WhatsApp 等流行消息应用程序的修改版本。

*404media报道称： “黑客窃取的数据包含使用 Signal 克隆版发送的一些私信和群聊内容，以及 WhatsApp、Telegram 和微信的修改版。”   “最近，迈克·沃尔兹在与特朗普总统的内阁会议上意外透露自己使用了 TeleMessage，TeleMessage 成为媒体关注的焦点。”*

此次安全漏洞凸显了依赖热门应用程序修改版本的风险，尤其是在应用程序和存档之间的聊天内容未进行端到端加密的情况下。404 Media 指出，尽管美国高级官员使用了该应用程序，但内阁级别的信息并未受到泄露。然而，海关和边境保护局 (CBP)、Coinbase 和其他金融机构的数据也遭到泄露。

*据 404Media 报道，“黑客访问 TeleMessage 面板的一张截图列出了美国海关和边境保护局 (CBP) 官员的姓名、电话号码和电子邮件地址。” 截图显示“从 747 中选择 0”，这表明数据中可能包含许多 CBP 官员。类似的截图显示了 Coinbase 现任和前任员工的联系信息。*

尽管并非所有数据都被访问，但威胁行为者在短短 20 分钟内就入侵了该公司，引发了国家安全担忧，尤其是包括沃尔兹在内的美国高级官员在敏感讨论中使用该工具。

近日，  404媒体率先报道称 ，美国国家安全顾问沃尔兹在内阁会议期间意外透露自己正在使用TeleMessage修改版的Signal。

*“该工具的使用引发了人们对该应用程序所讨论信息的分类以及这些数据如何得到保护的质疑，此前有消息称美国高级官员 正在使用 Signal 讨论现役作战行动。”帖子继续说道。*

[![电话留言]()](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2025/05/image-10.png?ssl=1)

来源 404 媒体 – 黑客提供的屏幕截图。

泄露的 TeleMessage 数据包括消息内容、政府联系信息、后端凭证和客户端线索。这些消息来自经过修改的 Signal，内容包括政治和加密相关的讨论，例如涉及 Galaxy Digital 和美国参议院法案审议的聊天。

黑客获取了 TeleMessage 的调试数据，其中包括未加密的实时消息片段。404 Media 通过联系数据中列出的美国海关及边境保护局官员证实了此次入侵，并确认了其真实性。

“黑客入侵的服务器托管在位于弗吉尼亚州北部的亚马逊AWS云基础设施上。通过审查 TeleMessage修改后的Android版Signal应用程序的源代码 ，404 Media确认该应用程序确实向该端点发送了消息数据。” 该媒体总结道。“404 Media还向该服务器发出了HTTP请求，以确认其处于在线状态。”

记者 Micah Lee分析了TeleMessage 的 Signal 克隆版本，发现了硬编码的凭证和许可证问题。他通过一个泄露的 URL访问了该版本的Android 源代码。其他研究人员后来发现了 iOS 代码。该应用可能违反了 Signal 的开源条款。与此同时，涉嫌滥用 Signal 的 Waltz 已被调职。

根据 具有约束力的运营指令 (BOD) 22-01：降低已知被利用漏洞的重大风险，FCEB 机构必须在截止日期前解决已发现的漏洞，以保护其网络免受利用目录中的漏洞的攻击。

专家还建议私人组织审查该 目录 并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2025 年 6 月 2 日之前修复这些漏洞。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/177743/hacking/u-s-cisa-adds-telemessage-tm-sgnl-to-its-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307345](/post/id/307345)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/177743/hacking/u-s-cisa-adds-telemessage-tm-sgnl-to-its-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/177743/hacking/u-s-cisa-adds-telemessage-tm-sgnl-to-its-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [美国网络安全和基础设施安全局 (CISA) 将 TeleMessage TM SGNL 漏洞添加到其已知被利用的漏洞目录中。](#h2-0)

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