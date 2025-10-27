---
title: 利用 Veeam 的关键漏洞传播 Akira 和 Fog 勒索软件
url: https://www.anquanke.com/post/id/300858
source: 安全客-有思想的安全新媒体
date: 2024-10-16
fetch_date: 2025-10-06T18:45:47.930267
---

# 利用 Veeam 的关键漏洞传播 Akira 和 Fog 勒索软件

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

# 利用 Veeam 的关键漏洞传播 Akira 和 Fog 勒索软件

阅读量**49898**

发布时间 : 2024-10-15 15:28:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html>

译文仅供参考，具体内容表达以及含义原文为准。

威胁者正积极试图利用Veeam Backup & Replication中一个现已打补丁的安全漏洞来部署Akira和Fog勒索软件。

网络安全厂商Sophos表示，在过去的一个月里，它一直在追踪一系列利用被泄露的VPN凭证和CVE-2024-40711创建本地帐户并部署勒索软件的攻击。

CVE-2024-40711在CVSS等级中被评为9.8级（满分10.0），是一个允许未经验证的远程代码执行的关键漏洞。2024 年 9 月初，Veeam 在备份与复制 12.2 版本中解决了这一问题。

德国 CODE WHITE 公司的安全研究员 Florian Hauser 是发现并报告该安全漏洞的功臣。

“在每个案例中，攻击者最初都是在未启用多因素身份验证的情况下使用被入侵的 VPN 网关访问目标的，”Sophos 说。“其中一些 VPN 运行的是不支持的软件版本。

“每次，攻击者都在端口 8000 的 URI /trigger 上利用 VEEAM，触发 Veeam.Backup.MountService.exe 生成 net.exe。该漏洞利用程序创建了一个本地账户’point’，并将其添加到本地管理员和远程桌面用户组中。

据说，在导致部署 Fog 勒索软件的攻击中，威胁者将勒索软件投放到未受保护的 Hyper-V 服务器上，同时使用 rclone 实用程序外泄数据。其他勒索软件部署均未成功。

对 CVE-2024-40711 的积极利用促使英国国家医疗服务系统（NHS England）发布了一份警告，指出 “企业备份和灾难恢复应用程序是网络威胁组织的重要目标”。

在披露这一消息的同时，Palo Alto Networks 第 42 部门详细介绍了名为 Lynx 的 INC 勒索软件的后续版本，该版本自 2024 年 7 月以来一直处于活跃状态，其攻击目标是美国和英国的零售、房地产、建筑、金融和环境服务领域的组织。

据说，早在2024年3月，INC勒索软件的源代码就在地下犯罪市场上出售，促使恶意软件作者重新包装锁定器并产生新的变种，从而刺激了Lynx的出现。

“Lynx勒索软件与INC勒索软件共享大量源代码，”Unit 42说。“INC勒索软件最初出现在2023年8月，其变种兼容Windows和Linux。”

在此之前，美国卫生与公众服务部（HHS）卫生部门网络安全协调中心（HC3）也发布警告称，该国至少有一家医疗保健实体已成为 Trinity 勒索软件的受害者，Trinity 勒索软件是另一款相对较新的勒索软件，于 2024 年 5 月首次为人所知，据信是 2023Lock 和 Venus 勒索软件的改版。

“HC3表示：”这是一种通过多种攻击载体渗透系统的恶意软件，包括钓鱼电子邮件、恶意网站和利用软件漏洞。“一旦进入系统，Trinity 勒索软件就会采用双重勒索策略，将受害者作为攻击目标”。

据观察，网络攻击还提供了一种被称为BabyLockerKZ的MedusaLocker勒索软件变种，该变种由一个有经济动机的威胁行为者提供，据悉自2022年10月以来一直很活跃，目标主要位于欧盟国家和南美洲。

“Talos 研究人员表示：”该攻击者使用了几种公开的攻击工具和离岸二进制文件（LoLBins），这是由同一开发者（可能是攻击者）构建的一套工具，用于协助被攻击组织的凭证窃取和横向移动。

“这些工具大多是对公开可用工具的封装，其中包括简化攻击过程的附加功能，并提供图形或命令行界面。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300858](/post/id/300858)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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