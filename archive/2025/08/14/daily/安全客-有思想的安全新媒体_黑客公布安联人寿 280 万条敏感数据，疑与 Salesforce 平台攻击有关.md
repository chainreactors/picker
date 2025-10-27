---
title: 黑客公布安联人寿 280 万条敏感数据，疑与 Salesforce 平台攻击有关
url: https://www.anquanke.com/post/id/311161
source: 安全客-有思想的安全新媒体
date: 2025-08-14
fetch_date: 2025-10-07T00:18:08.237267
---

# 黑客公布安联人寿 280 万条敏感数据，疑与 Salesforce 平台攻击有关

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

# 黑客公布安联人寿 280 万条敏感数据，疑与 Salesforce 平台攻击有关

阅读量**71887**

发布时间 : 2025-08-13 16:30:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hackers-leak-allianz-life-data-stolen-in-salesforce-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

黑客近日公布了美国保险巨头**安联人寿 （Allianz Life）** 被盗的数据，其中包含 **280 万条**涉及业务合作伙伴和客户的敏感记录。这是正在进行的 Salesforce 数据窃取攻击的一部分。

上个月，Allianz Life 披露，其 **“大多数”140 万客户**的个人信息于 7 月 16 日从一家第三方云端 CRM 系统中被窃取，构成数据泄露事件。

虽然公司当时并未公开该服务提供商的名称，但 **BleepingComputer** 最先报道称，该事件属于 **ShinyHunters 勒索组织**针对 Salesforce 的一系列攻击之一。

上周末，ShinyHunters 与其他声称与 **“Scattered Spider”** 和 **“Lapsus$”** 有重叠的威胁行为者创建了一个名为 **“ScatteredLapsuSp1d3rHunters”** 的 Telegram 频道，在那里嘲讽网络安全研究人员、执法机构和记者，并为多起重大入侵事件“认领责任”。

他们声称的一些攻击此前从未被归因于任何特定威胁组织，包括对 **Internet Archive**、**Pearson** 和 **Coinbase** 的攻击。

在这些“认领”事件中，就包括安联人寿。黑客称已将该公司 Salesforce 实例中被窃取的完整数据库泄露出来。

泄露的文件包括 Salesforce 中的 **“Accounts”** 和 **“Contacts”** 数据表，总计约 280 万条涉及个人客户及业务合作伙伴（如财富管理公司、经纪人、理财顾问等）的记录。

这些 Salesforce 数据包含大量敏感个人信息，例如姓名、地址、电话号码、出生日期、税务识别号（TIN），以及执业许可证、公司隶属关系、产品授权、营销分类等职业信息。

**BleepingComputer** 已联系多名出现在泄露文件中的人员，并确认其电话号码、电子邮件、税务识别号及其他信息均属真实。

BleepingComputer 就数据库泄露事宜联系安联人寿，但公司表示因调查尚在进行，暂不发表评论。

## Salesforce 数据窃取攻击背景

据信，这波 Salesforce 数据窃取攻击始于今年年初。威胁行为者通过**社会工程攻击**，诱骗员工将恶意的 OAuth 应用与其公司 Salesforce 实例绑定。

一旦绑定成功，攻击者便利用该连接下载并窃取数据库，随后通过电子邮件对公司进行勒索。

勒索邮件以 ShinyHunters 的名义发送。这个臭名昭著的组织多年来与多起重大攻击有关，包括针对 **AT&T**、**PowerSchool** 和 **Snowflake** 的事件。

虽然 ShinyHunters 过去以攻击云端 SaaS 应用和网站数据库闻名，但并不擅长此类社会工程攻击，因此不少研究人员和媒体将部分 Salesforce 攻击归因于 **Scattered Spider**。

不过，ShinyHunters 向 BleepingComputer 表示：“**ShinyHunters 和 Scattered Spider 是同一个组织**。”

他们补充称：“他们为我们提供初始访问权限，我们则负责导出和窃取 Salesforce CRM 实例的数据，就像我们在 Snowflake 事件中做的那样。”

此外，据信该组织的许多成员来自另一黑客组织 **Lapsus$**。后者在 2022 至 2023 年间制造了多起重大攻击事件，部分成员此后被捕。

Lapsus$ 曾入侵 **Rockstar Games**、**Uber**、**2K**、**Okta**、**T-Mobile**、**Microsoft**、**Ubisoft** 和 **NVIDIA** 等公司。

与 Scattered Spider 类似，Lapsus$ 擅长社会工程和 **SIM 卡交换攻击（SIM Swap）**，能够突破市值数十亿美元甚至数万亿美元公司的 IT 防御。

过去几年，已有与这三个组织相关的多起逮捕事件。但目前尚不清楚，当前的威胁行为者是这些组织的原成员、新加入的黑客，还是仅仅借用这些名号来制造“假旗”混淆视听。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hackers-leak-allianz-life-data-stolen-in-salesforce-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311161](/post/id/311161)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hackers-leak-allianz-life-data-stolen-in-salesforce-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hackers-leak-allianz-life-data-stolen-in-salesforce-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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

* [Salesforce 数据窃取攻击背景](#h2-0)

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