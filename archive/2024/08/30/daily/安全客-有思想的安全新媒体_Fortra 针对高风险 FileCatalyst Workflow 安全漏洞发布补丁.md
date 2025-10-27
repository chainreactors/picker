---
title: Fortra 针对高风险 FileCatalyst Workflow 安全漏洞发布补丁
url: https://www.anquanke.com/post/id/299625
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:24.803495
---

# Fortra 针对高风险 FileCatalyst Workflow 安全漏洞发布补丁

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

# Fortra 针对高风险 FileCatalyst Workflow 安全漏洞发布补丁

阅读量**49620**

发布时间 : 2024-08-29 15:54:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/fortra-issues-patch-for-high-risk.html>

译文仅供参考，具体内容表达以及含义原文为准。

Fortra 解决了影响 FileCatalyst Workflow 的关键安全漏洞，远程攻击者可能会滥用该漏洞来获得管理访问权限。

该漏洞被跟踪为 CVE-2024-6633，CVSS 评分为 9.8，源于使用静态密码连接到 HSQL 数据库。

“FileCatalyst Workflow 的设置 HSQL 数据库 （HSQLDB） 的默认凭据发布在供应商知识库文章中，”Fortra 在公告中说。“滥用这些凭证可能会导致软件的机密性、完整性或可用性受到损害。”

“HSQLDB 只是为了便于安装而包含的，已弃用，并且根据供应商指南不打算用于生产。但是，未将 FileCatalyst Workflow 配置为根据建议使用替代数据库的用户容易受到来自任何可以到达 HSQLDB 的来源的攻击。

因发现和报告该漏洞而受到赞誉的网络安全公司 Tenable 表示，默认情况下，HSQLDB 可以通过 TCP 端口 4406 远程访问，从而允许远程攻击者使用静态密码连接到数据库并执行恶意操作。

继 2024 年 7 月 2 日负责任地披露后，Fortra 发布了一个补丁来填补 FileCatalyst Workflow 5.1.7 或更高版本中的安全漏洞。

“例如，攻击者可以在 DOCTERA\_USERS 表中添加管理员级别的用户，从而允许以管理员用户身份访问 Workflow Web 应用程序，”Tenable 说。

版本 5.1.7 中还解决了一个高严重性 SQL 注入缺陷（CVE-2024-6632，CVSS 评分：7.2），该漏洞在设置过程中滥用表单提交步骤，对数据库进行未经授权的修改。

“在 FileCatalyst Workflow 的设置过程中，系统会提示用户通过提交表单来提供公司信息，”Dynatrace 研究员 Robin Wyss 说。

“提交的数据用于数据库语句，但用户输入没有经过适当的输入验证。因此，攻击者可以修改查询。这允许对数据库进行未经授权的修改。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/fortra-issues-patch-for-high-risk.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299625](/post/id/299625)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/fortra-issues-patch-for-high-risk.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/fortra-issues-patch-for-high-risk.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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