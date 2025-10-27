---
title: APT42 黑客冒充记者获取凭证并访问云数据
url: https://www.anquanke.com/post/id/296255
source: 安全客-有思想的安全新媒体
date: 2024-05-09
fetch_date: 2025-10-06T17:13:53.131442
---

# APT42 黑客冒充记者获取凭证并访问云数据

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

# APT42 黑客冒充记者获取凭证并访问云数据

阅读量**61562**

发布时间 : 2024-05-08 10:45:28

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/05/apt42-hackers-pose-as-journalists-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

伊朗国家支持的黑客组织APT42正在利用增强的社会工程方案渗透目标网络和云环境。

谷歌云子公司 Mandiant 在上周发布的一份报告中表示，攻击的目标包括西方和中东非政府组织、媒体组织、学术界、法律服务和活动人士。

该公司表示：“据观察，APT42冒充记者和活动组织者，通过持续通信与受害者建立信任，并发送会议邀请或合法文件。 ”

“这些社会工程方案使 APT42 能够获取凭据并使用它们来获得对云环境的初始访问权限。随后，威胁行为者秘密窃取了对伊朗具有战略利益的数据，同时依靠内置功能和开源工具来避免检测”。

APT42（又名 Damselfly 和 UNC788）于 2022 年 9 月首次由该公司记录，是一个伊朗国家支持的网络间谍组织，其任务是针对伊朗政府具有战略利益的个人和组织进行信息收集和监视行动。

它被评估为另一个臭名昭著的威胁组织 APT35 的子集，该组织也有各种名称 CALANQUE、CharmingCypress、Charming Kitten、ITG18、Mint Sandstorm（以前称为 Phosphorus）、Newcaster、TA453 和 Yellow Garuda。

这两个组织都隶属于伊朗伊斯兰革命卫队（IRGC），但有着不同的目标。

而 Charming Kitten 则更侧重于针对美国和中东的组织和公司窃取数据的长期恶意软件密集型操作。相比之下，APT42 针对的是政权出于国内政治、外交政策和政权稳定的目的而关注的特定个人和组织。

今年 1 月初，微软将这位 Charming Kitten 演员归咎于自 2023 年 11 月以来针对比利时、法国、加沙、以色列、英国和美国的大学和研究组织中从事中东事务的知名人士发起的网络钓鱼活动。

[![网络间谍活动]( "网络间谍活动")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXKt55Q7o8pHm-LAdTLA5as_LDUcqBLTc0VWOBSDJRrlW6cM4D3gWNRorniGKTHsBG0MeFFDanRMTB2z7OBLzFz1RXgTHEPC_fjdsAq3ahyoeeNHV17-AZVrVpBs45RT55sUr6HT1Osx3fFjBNL8k1wUCwx-ajEtGI0MNgJjkvNiK99-T7QP6tcaWG6IBk/s728-rw-e365/malware-2.png)
据了解，该组织发动的攻击涉及广泛的凭据收集操作，通过包含恶意链接的鱼叉式网络钓鱼电子邮件收集 Microsoft、Yahoo 和 Google 凭据，以引诱将收件人重定向到虚假登录页面的文档。

在这些活动中，我们观察到对手从对原始实体进行拼写错误并伪装成新闻媒体的域发送电子邮件； Dropbox、Google Meet、LinkedIn 和 YouTube 等合法服务；以及邮件程序守护进程和 URL 缩短工具。

夺取凭证的攻击还辅以针对受害者公共云基础设施的数据泄露活动，以获取伊朗感兴趣的文件，但前提是要获得伊朗的信任——这是 Charming Kitten 所擅长的。

曼迪安特说：“这些行动始于增强的社会工程计划，以获得对受害者网络的初步访问，通常涉及与受害者持续建立信任的通信。”

“只有这样，才能获取所需的凭据，并通过提供克隆网站来捕获 MFA 令牌（失败），然后向受害者发送 MFA 推送通知（成功），从而绕过多重身份验证 (MFA)。”

为了掩盖其踪迹并融入其中，攻击者被发现依赖公开可用的工具，将文件窃取到伪装成受害者组织的 OneDrive 帐户，并使用 VPN 和匿名基础设施与受感染的环境进行交互。

APT42 还使用两个自定义后门，它们充当部署其他恶意软件或在设备上手动执行命令的跳转点 –

NICECURL（又名 BASICSTAR） – 用 VBScript 编写的后门，可以下载要执行的附加模块，包括数据挖掘和任意命令执行
TAMECAT – 可以执行任意 PowerShell 或 C# 内容的 PowerShell 立足点
值得注意的是，NICECURL此前曾于 2024 年 2 月被网络安全公司 Volexity 剖析，原因​​是该网络与一系列针对中东政策专家的网络攻击有关。

Mandiant 总结道：“尽管以色列与哈马斯的战争导致其他与伊朗有联系的行为体通过进行破坏性、破坏性和黑客泄露活动来适应，但APT42 仍然相对专注于情报收集和针对类似的受害者。”

“APT42 部署的方法留下的足迹最小，可能会使网络防御者检测和缓解其活动变得更具挑战性。”

本文翻译自 [原文链接](https://thehackernews.com/2024/05/apt42-hackers-pose-as-journalists-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296255](/post/id/296255)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/05/apt42-hackers-pose-as-journalists-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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