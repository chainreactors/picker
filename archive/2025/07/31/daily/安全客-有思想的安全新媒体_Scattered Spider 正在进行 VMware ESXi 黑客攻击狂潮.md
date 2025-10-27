---
title: Scattered Spider 正在进行 VMware ESXi 黑客攻击狂潮
url: https://www.anquanke.com/post/id/310711
source: 安全客-有思想的安全新媒体
date: 2025-07-31
fetch_date: 2025-10-06T23:16:53.936077
---

# Scattered Spider 正在进行 VMware ESXi 黑客攻击狂潮

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

# Scattered Spider 正在进行 VMware ESXi 黑客攻击狂潮

阅读量**68987**

发布时间 : 2025-07-30 16:48:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Scattered Spider 黑客团伙一直在积极针对虚拟化环境，攻击美国零售、航空、运输和保险行业公司的 VMware ESXi 超级管理程序。

根据谷歌威胁情报组（GITG）的报告，攻击者继续采用他们一贯的手段，这些手段不涉及漏洞利用，而是依靠精心执行的社交工程手段，“即使是成熟的安全程序也难以绕过。”

### Scattered Spider 攻击

研究人员表示，该团伙开始攻击时，通过伪装成员工拨打 IT 帮助台电话。攻击者的目的是说服接线员更改员工的 Active Directory 密码，从而获得初步访问权限。

这使得 Scattered Spider 能够扫描网络设备，以寻找提供高价值目标的 IT 文档，例如域名或 VMware vSphere 管理员的姓名，以及能够提供虚拟环境管理权限的安全组。

与此同时，他们还会扫描特权访问管理（PAM）解决方案，寻找可能存储着有助于进一步渗透到有价值网络资产的敏感数据。

“掌握了特定高价值管理员的姓名后，他们会再次拨打帮助台电话。这次，他们伪装成该特权用户，请求密码重置，从而控制特权账户。”——谷歌威胁情报组

接着，黑客继续渗透，最终获得对公司的 VMware vCenter Server Appliance (vCSA) 访问权限——这是一台虚拟机，用于管理 VMware vSphere 环境，其中包括用于管理所有虚拟机的 ESXi 超级管理程序。

Scattered Spider黑客团伙通过攻击VMware ESXi超级管理程序获得的访问权限，能够在ESXi主机上启用SSH连接并重置root密码。此外，他们还执行所谓的“磁盘交换”攻击，以提取Active Directory的关键NTDS.dit数据库。

磁盘交换攻击发生在攻击者关闭域控制器虚拟机（VM）并卸下其虚拟磁盘后，再将其附加到他们控制的另一个未受监控的虚拟机上。攻击者复制敏感数据（例如NTDS.dit文件）后，反转操作并重新启动域控制器虚拟机。

需要注意的是，Scattered Spider对虚拟基础设施的控制使得他们能够管理所有可用资产，包括备份机器，这些备份机器的备份任务、快照和存储库被清除。

在攻击的最后阶段，Scattered Spider利用他们的SSH访问权限交付并部署勒索软件二进制文件，进而加密数据存储区中检测到的所有虚拟机文件。

![]()

根据GTIG研究人员的观察，Scattered Spider攻击包括五个不同的阶段，使得黑客能够从低级访问权限过渡到对超级管理程序的完全控制。完整的Scattered Spider攻击链，从初步访问到数据外泄和勒索软件部署，可能在几个小时内完成。即使没有利用任何软件漏洞，威胁行为者也能获得“对整个虚拟化环境前所未有的控制级别，从而绕过许多传统的虚拟机内安全控制”，谷歌的一位代表告诉BleepingComputer。

虽然针对ESXi超级管理程序的攻击并不新鲜（例如Scattered Spider在2023年MGM度假村攻击中就有所表现），GTIG指出，越来越多的勒索软件团伙采用这一战术，并预计这一问题将进一步加剧。

其中一个原因可能是攻击者发现VMware基础设施通常对组织而言理解不深，因此防御措施不够强大。

为帮助组织防范这些攻击，谷歌发布了一个技术文章，详细描述了Scattered Spider攻击的各个阶段，解释了其高效性，并提供了公司可以采取的措施，以便在早期阶段发现漏洞。

提出的防护措施可以概括为三个主要支柱：

**1. 加固vSphere**：启用execInstalledOnly、VM加密，并禁用SSH。避免在ESXi上直接加入AD，删除孤立的虚拟机，执行严格的多因素认证（MFA）和访问控制策略。持续监控配置漂移。

**2. 使用抗钓鱼的MFA**：在VPN、AD和vCenter中使用抗钓鱼的MFA。隔离Tier 0资产（域控制器、备份、PAM），避免将它们与所保护的基础设施托管在同一环境中。考虑使用独立的云身份提供商，打破AD依赖。

**3. 集中日志管理**：将日志集中到SIEM中，并对关键行为（如管理员组变化、vCenter登录和SSH启用）进行告警。使用不可变的、隔离的备份，并测试针对超级管理程序层攻击的恢复能力。

Scattered Spider（也称为UNC3944、Octo Tempest、0ktapus）是一个经济动机驱动的威胁团体，专门从事社会工程学攻击，能够通过使用适当的词汇和口音伪装成公司员工。该团体最近加强了活动，攻击了大型英国零售公司、航空和运输实体以及保险公司。

尽管英国国家犯罪局逮捕了该团体的四名疑似成员，但源自其他集群的恶意活动仍未减弱。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310711](/post/id/310711)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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