---
title: Veeam备份软件漏洞引发全球勒索软件攻击浪潮
url: https://www.anquanke.com/post/id/297925
source: 安全客-有思想的安全新媒体
date: 2024-07-17
fetch_date: 2025-10-06T17:41:01.855402
---

# Veeam备份软件漏洞引发全球勒索软件攻击浪潮

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

# Veeam备份软件漏洞引发全球勒索软件攻击浪潮

阅读量**104747**

发布时间 : 2024-07-16 12:15:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/165753/malware/ransomware-groups-target-veeam-backup-replication-bug.html>

译文仅供参考，具体内容表达以及含义原文为准。

漏洞 CVE-2023-275327（CVSS 评分为 7.5）会影响 Veeam Backup & Replication 组件。攻击者可利用此问题获取存储在配置数据库中的加密凭据，从而可能导致访问备份基础结构主机。

该漏洞已于 2023 年 3 月得到解决，不久后，该问题的 PoC 漏洞利用代码被公开发布。

专家观察到，俄罗斯网络犯罪集团 FIN7 自 2023 年 4 月以来一直在利用该漏洞，黑莓的研究人员报告说，2024 年 6 月，一名威胁行为者使用 Akira 勒索软件瞄准了一家拉丁美洲航空公司。对目标网络的最初访问是通过安全外壳 （SSH） 协议进行的，攻击者在第二天部署 Akira 勒索软件之前泄露了关键数据。他们滥用合法工具和生活异地二进制文件和脚本 （LOLBAS） 进行侦察和持久性。数据泄露完成后，攻击者部署勒索软件来加密受感染的系统。Akira 是一种勒索软件即服务 （RaaS），已被 Storm-1567（又名 Punk Spider 和 GOLD SAHARA）使用，该组织自 2023 年以来一直活跃。对 Remmina 相关域的 DNS 查询等指标表明攻击者可能是基于 Linux 的用户。

以下是 Akira 攻击链的第 1 天和第 2 天：

[![Veeam Backup & Replication akira ransomware attack]()](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2024/07/image-16.png?ssl=1)[![Veeam Backup & Replication akira ransomware attack]()](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2024/07/image-17.png?ssl=1)

在对一家拉丁美洲航空公司的攻击中，攻击者首次通过路由器 IP 地址的 SSH 对未打补丁的 Veeam 备份服务器进行可见访问。专家认为，攻击者利用公开可用的漏洞漏洞CVE-2023-27532。

进入网络后，攻击者创建了一个名为“backup”的用户，并将其添加到管理员组以保护提升的权限。攻击者部署了合法的网络管理工具高级 IP 扫描程序来扫描通过“路由打印”识别的本地子网。

攻击者通过访问 Veeam 备份文件夹来控制 Veeam 备份数据，并压缩和上传各种文件类型（包括文档、图像和电子表格），以收集机密和有价值的信息。攻击者使用免费的 Windows 文件管理器 WinSCP 将数据泄露到他们控制的服务器。

从初始登录到数据泄露的整个操作仅用了 133 分钟，最终命令在 UTC 时间下午 4：55 结束。

*“当NetScan在主Veeam备份服务器上运行时，通过防病毒用户界面（UI）和命令行在虚拟机主机上禁用了防病毒（AV）保护，”BlackBerry发布的报告写道。“现在，持久性已经完全到位，威胁行为者试图使用Veeam备份服务器作为控制点，在全网范围内部署勒索软件。我们看到文件“w.exe”（Akira 勒索软件）被部署在受感染的 Veeam 服务器的各种主机上。*

Group-IB 研究人员还发现了一个勒索软件组织利用 Veeam Backup & Replication 实例中的漏洞。专家报告称，2024 年 4 月，EstateRansomware 团伙使用 PoC 漏洞利用代码针对漏洞 CVE-2023-27532。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/165753/malware/ransomware-groups-target-veeam-backup-replication-bug.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297925](/post/id/297925)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/165753/malware/ransomware-groups-target-veeam-backup-replication-bug.html)

如若转载,请注明出处： <https://securityaffairs.com/165753/malware/ransomware-groups-target-veeam-backup-replication-bug.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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