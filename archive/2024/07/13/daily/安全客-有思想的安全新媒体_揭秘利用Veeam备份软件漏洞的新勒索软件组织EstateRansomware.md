---
title: 揭秘利用Veeam备份软件漏洞的新勒索软件组织EstateRansomware
url: https://www.anquanke.com/post/id/297835
source: 安全客-有思想的安全新媒体
date: 2024-07-13
fetch_date: 2025-10-06T17:39:38.380646
---

# 揭秘利用Veeam备份软件漏洞的新勒索软件组织EstateRansomware

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

# 揭秘利用Veeam备份软件漏洞的新勒索软件组织EstateRansomware

阅读量**116006**

发布时间 : 2024-07-12 09:56:27

**x**

##### 译文声明

本文是翻译文章，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html>

译文仅供参考，具体内容表达以及含义原文为准。

已被修补的一个安全漏洞现正被一个新兴的勒索软件团伙EstateRansomware所利用，该团伙的目标是Veeam Backup & Replication软件。

总部位于新加坡的 Group-IB 于 2024 年 4 月初发现了该威胁行为者，该公司表示，作案手法涉及利用 CVE-2023-27532（CVSS 评分：7.5）进行恶意活动。

据称，攻击者通过使用一个休眠账户，借助Fortinet FortiGate防火墙SSL VPN设备获得了对目标环境的初始访问权。

“威胁行为者从FortiGate防火墙通过SSL VPN服务横向移动，以访问故障转移服务器，”安全研究员Yeo Zi Wei在今日发布的一份分析报告中表示。

在勒索软件攻击发生前，2024年4月记录到了使用名为‘Acc1’的休眠账户进行的VPN暴力破解尝试。几天后，使用‘Acc1’成功登录VPN的记录追溯到了远程IP地址149.28.106[.]252。

接下来，威胁行为者从防火墙建立了到故障转移服务器的RDP连接，然后部署了一个名为“svchost.exe”的持久性后门，该后门通过计划任务每天执行。

随后，利用这个后门实现了对网络的进一步访问，以此躲避检测。后门的主要作用是通过HTTP连接到命令与控制（C2）服务器，并执行攻击者发出的任意命令。

Group-IB观察到，该行为者利用了Veeam漏洞CVE-2023-27532，目的是在备份服务器上启用xp\_cmdshell，并创建一个名为“VeeamBkp”的恶意用户账户，同时使用诸如NetScan、AdFind和NitSoft等工具通过新创建的账户进行网络发现、枚举和凭据收集活动。

Zi Wei推测，“这种利用可能涉及到从文件服务器上的VeeamHax文件夹发起的攻击，针对安装在备份服务器上的Veeam Backup & Replication软件的易受攻击版本。”

“这一活动促进了xp\_cmdshell存储过程的激活，随后创建了‘VeeamBkp’账户。”

在部署勒索软件之前，攻击者采取了削弱防御措施的步骤，使用被攻破的域账户从AD服务器横向移动到所有其他服务器和工作站。

Group-IB表示：“Windows Defender使用DC.exe [Defender Control]永久禁用，然后使用PsExec.exe部署和执行勒索软件。

思科 Talos 透露，大多数勒索软件团伙优先考虑使用面向公众的应用程序、网络钓鱼附件或破坏有效帐户中的安全漏洞来建立初始访问权限，并规避其攻击链中的防御措施以增加受害者网络的停留时间。

在加密文件之前泄露数据的双重勒索模型进一步催生了由参与者开发的自定义工具（例如 Exmatter、Exbyte 和 StealBit），用于将机密信息发送到对手控制的基础设施。

这需要这些电子犯罪集团建立长期访问以探索环境，以了解网络结构，找到可以支持攻击的资源，提升他们的特权，或允许他们混入其中，并识别可能被盗的价值数据。

“在过去的一年里，我们目睹了勒索软件领域的重大变化，出现了多个新的勒索软件组织，每个组织都表现出独特的目标、运营结构和受害者学，”Talos说。

“这种多元化凸显了向更多精品目标网络犯罪活动的转变，因为 Hunters International、Cactus 和 Akira 等团体开辟了特定的利基市场，专注于不同的运营目标和风格选择，以区分自己。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297835](/post/id/297835)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Gunra Ransomware集团声称从美国医院泄露了40 TB数据](/post/id/308534)

  2025-06-17 16:00:49
* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24

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