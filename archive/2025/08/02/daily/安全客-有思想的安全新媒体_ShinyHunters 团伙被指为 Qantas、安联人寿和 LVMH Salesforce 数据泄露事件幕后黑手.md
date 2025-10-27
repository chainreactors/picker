---
title: ShinyHunters 团伙被指为 Qantas、安联人寿和 LVMH Salesforce 数据泄露事件幕后黑手
url: https://www.anquanke.com/post/id/310770
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:17:58.715978
---

# ShinyHunters 团伙被指为 Qantas、安联人寿和 LVMH Salesforce 数据泄露事件幕后黑手

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

# ShinyHunters 团伙被指为 Qantas、安联人寿和 LVMH Salesforce 数据泄露事件幕后黑手

阅读量**105294**

发布时间 : 2025-08-01 17:20:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一波针对 Qantas、安联人寿、LVMH 以及 Adidas 等公司的数据泄露事件已被追踪至勒索团伙 **ShinyHunters**，该团伙通过语音钓鱼（vishing）攻击手段从 Salesforce 客户关系管理系统中窃取数据。

今年 6 月，谷歌威胁情报小组（GTIG）曾发出预警，指出一支被追踪编号为 **UNC6040** 的威胁行为者正针对 Salesforce 客户发起社会工程攻击。

在这类攻击中，攻击者冒充 IT 支持人员致电受害员工，试图诱导其访问 Salesforce 的“连接应用设置”页面，并在页面中输入一组“连接代码”，从而将一个恶意版本的 Salesforce Data Loader OAuth 应用接入目标的 Salesforce 环境。有时，为提高迷惑性，该组件还会被伪装成“My Ticket Portal”（我的工单门户）等名称。

![]()

GTIG 表示，这些攻击通常通过语音钓鱼实施，但攻击者也曾使用仿冒 Okta 登录页面的钓鱼站点窃取受害者的登录凭据和多因素认证（MFA）令牌。

在本次报告发布前后，多家公司通报了涉及第三方客户服务或基于云的客户关系管理（CRM）系统的数据泄露事件。

LVMH 旗下品牌路易威登（Louis Vuitton）、迪奥（Dior）以及蒂芙尼（Tiffany & Co.）均披露了客户信息数据库遭到未经授权访问的情况。其中，蒂芙尼韩国向客户通报称，攻击者入侵的是“用于管理客户数据的第三方平台”。

此外，Adidas、澳洲航空（Qantas）和安联人寿（Allianz Life）也报告了与第三方系统相关的数据泄露事件。安联方面确认，所涉为一家第三方客户关系管理平台。

“2025 年 7 月 16 日，一名恶意威胁行为者入侵了北美安联人寿保险公司（Allianz Life Insurance Company of North America）使用的第三方云端 CRM 系统。”安联人寿发言人对 BleepingComputer 表示。

尽管 BleepingComputer 获悉，Qantas 的数据泄露同样涉及第三方客户关系管理平台，但该公司未确认是否为 Salesforce。然而，当地媒体此前的报道指出，相关数据确实是从 Qantas 的 Salesforce 系统中被盗。

进一步的法院文件显示，攻击者针对的数据库表为**“Accounts”和“Contacts”**，这两项正是 Salesforce 中的对象。

虽然上述公司均未在公开声明中点名 Salesforce，但 BleepingComputer 已确认，它们全部为谷歌此前通报的同一攻击活动的受害者。

这些攻击尚未公开索要赎金或泄露数据。BleepingComputer 了解到，攻击者正通过电子邮件私下向受害公司勒索，声明自己为 ShinyHunters。

据推测，如果勒索未果，攻击者将像此前针对 Snowflake 发动的攻击那样，以长波次方式公开泄露窃取的数据。

### **谁是 ShinyHunters？**

这轮攻击让网络安全界和媒体产生了混淆，包括 BleepingComputer 在内，一度将其归因于同一时期对航空、零售和保险行业发动攻击、采用相似战术的 Scattered Spider（Mandiant 跟踪代号 UNC3944）。然而，Scattered Spider 通常执行全面的网络入侵，最终盗取数据并有时部署勒索软件；而被跟踪为 UNC6040 的 ShinyHunters 则专注于针对特定云平台或 Web 应用的数据窃取及勒索。

BleepingComputer 及部分安全研究人员认为，**UNC6040 与 UNC3944** 在成员上存在重叠，他们活跃于相同的网络社区。此威胁组织也可能与“ The Com ”——一个经验丰富、以英语为主要语言的网络犯罪集团——有交集。Recorded Future 的情报分析师 Allan Liska 告诉 BleepingComputer：“已知的 Scattered Spider 和 ShinyHunters 攻击在战术、技术与程序（TTPs）上的重合，表明两者之间极有可能存在交叉。”

其他研究人员也向 BleepingComputer 表示，ShinyHunters 与 Scattered Spider 在相同时间针对相同行业展开行动，且行事步调相似，增加了归因难度。

还有观点认为，这两支团伙都与现已解散的 Lapsus$ 黑客组织有关，报道显示，近期被逮捕的部分 Scattered Spider 成员曾参与 Lapsus$ 活动。

另一种猜测是，**ShinyHunters 充当勒索即服务（Extortion-as-a-Service）平台**，代表其他威胁行为者向企业索要赎金，并从中分成，类似于勒索软件即服务（RaaS）团伙的运营模式。这一说法得到了 BleepingComputer 与 ShinyHunters 早前对话的印证：他们声称自己并非攻击发起者，仅是贩售被窃数据的渠道。

ShinyHunters 曾涉及的攻击目标包括 PowerSchool、Oracle Cloud、“Snowflake”数据窃取事件、AT&T、NitroPDF、Wattpad、MathWay 等多家知名机构。

![]()

为了进一步混淆视听，与 “ShinyHunters” 名称有关的人员已被多次逮捕，其中包括涉嫌 Snowflake 数据窃取攻击、PowerSchool 入侵事件，以及运营黑客论坛 Breached v2 的个人。然而，即便在多起逮捕行动后，仍有新的攻击事件发生，且受害企业收到勒索邮件时，对方仍自称“We are ShinyHunters”，并称自己为“一个集体”。

### **如何防范对 Salesforce 实例的攻击**

Salesforce 在接受 BleepingComputer 采访时强调，Salesforce 平台本身并未遭到入侵，用户账户是通过社会工程手段被攻破的。Salesforce 向 BleepingComputer 表示“Salesforce 平台未被攻陷，所述问题并非源于我们平台的已知漏洞。虽然 Salesforce 在平台设计中已融入企业级安全保障，但在当前鱼叉式钓鱼和社会工程攻击激增的背景下，客户自身在数据保护方面也扮演着至关重要的角色。”

“我们持续建议所有客户遵循安全最佳实践，包括启用多因素认证（MFA）、贯彻最小权限原则、并严格管理已连接的应用程序。详情可访问：https://www.salesforce.com/blog/protect-against-social-engineering/”。为提升 Salesforce 实例的安全性，Salesforce 建议用户采取以下防护措施：

* **强制限制登录的可信 IP 范围；**
* **按照最小权限原则配置应用程序权限；**
* **启用多因素认证（MFA）；**
* **限制已连接应用的使用，并制定访问控制策略；**
* **使用 Salesforce Shield 进行高级威胁检测、事件监控与事务策略管理；**
* **指定安全联系人，用于安全事件的沟通响应。**

上述防护措施的更多细节可在 Salesforce 官方安全指南中获取。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310770](/post/id/310770)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/shinyhunters-behind-salesforce-data-theft-attacks-at-qantas-allianz-life-and-lvmh/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

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