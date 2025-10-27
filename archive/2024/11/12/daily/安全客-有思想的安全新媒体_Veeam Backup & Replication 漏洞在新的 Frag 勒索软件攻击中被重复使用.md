---
title: Veeam Backup & Replication 漏洞在新的 Frag 勒索软件攻击中被重复使用
url: https://www.anquanke.com/post/id/301700
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:19.894856
---

# Veeam Backup & Replication 漏洞在新的 Frag 勒索软件攻击中被重复使用

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

# Veeam Backup & Replication 漏洞在新的 Frag 勒索软件攻击中被重复使用

阅读量**52757**

发布时间 : 2024-11-11 14:42:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/170717/malware/veeam-backup-replication-flaw-frag-ransomware.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**最近，Veeam Backup & Replication (VBR)中一个被追踪为CVE-2024-40711的关键漏洞也被利用来部署Frag勒索软件。**

10月中旬，Sophos研究人员警告说，勒索软件运营商正在利用Veeam Backup & Replication中的关键漏洞CVE-2024-40711创建流氓账户并部署恶意软件。

2024 年 9 月初，Veeam 发布了安全更新，以解决影响其产品的多个漏洞，该公司修复了 Veeam Backup & Replication、Service Provider Console 和 One 中的 18 个高严重性和关键严重性漏洞。

2024年9月安全公告中最严重的漏洞是一个重要的远程代码执行（RCE）漏洞，该漏洞被追踪为CVE-2024-40711（CVSS v3.1得分：9.8），影响了Veeam Backup & Replication (VBR)。

Veeam Backup & Replication 是 Veeam 开发的一款全面的数据保护和灾难恢复软件。它使企业能够跨物理、虚拟和云环境备份、恢复和复制数据。

“漏洞允许未经验证的远程代码执行（RCE）。”

CODE WHITE Gmbh 公司的网络安全研究员 Florian Hauser 报告了这一漏洞。

该漏洞影响 Veeam Backup & Replication 12.1.2.172 和所有早期版本 12 的构建。

Sophos X-Ops研究人员观察到最近的攻击利用了被泄露的凭证和Veeam漏洞CVE-2024-40711来部署勒索软件，包括Fog和Akira。攻击者通过缺乏多因素身份验证的VPN网关访问目标，其中一些网关运行过时的软件。重叠指标将这些案例与之前的 Fog 和 Akira 勒索软件攻击联系起来。

“Sophos X-Ops MDR 和 Incident Response 正在追踪上个月发生的一系列攻击事件，这些攻击利用被泄露的凭证和 Veeam 中的一个已知漏洞（CVE-2024-40711）创建账户并试图部署勒索软件。

“在一个案例中，攻击者投放了Fog勒索软件。同一时间段的另一起攻击则试图部署 Akira 勒索软件。所有 4 个案例中的迹象都与早期的 Akira 和 Fog 勒索软件攻击重叠。在每个案例中，攻击者最初都是使用未启用多因素身份验证的受损 VPN 网关访问目标。其中一些 VPN 运行的是不支持的软件版本。”

威胁者利用端口 8000 上的 Veeam URI /trigger 启动 net.exe，并创建一个名为 “point ”的本地账户，将其添加到本地管理员和远程桌面用户组中。在一个案例中，攻击者在未受保护的 Hyper-V 服务器上部署了 Fog 勒索软件，并使用 rclone 进行数据外渗。

现在，在 Akira 和 Fog 勒索软件攻击之后，专家警告说，威胁者正试图利用 CVE-2024-40711 积极部署 Frag 勒索软件。

Sophos 最近发现，一个被追踪为 STAC 5881 的威胁者利用 CVE-2024-40711 在被入侵网络上部署 Frag 勒索软件。

“CVE-2024-40711漏洞被用作我们命名为STAC 5881的威胁活动集群的一部分。攻击利用被入侵的 VPN 设备进行访问，并利用 VEEAM 漏洞创建名为 “point ”的新本地管理员账户。该群组中的一些案例导致了 Akira 或 Fog 勒索软件的部署。Akira 于 2023 年首次出现，自 10 月中旬以来似乎已不再活跃，其信息泄漏网站现已下线”，Sophos 发布的一份报告中写道。“在最近的一个案例中，MDR 分析师再次观察到了与 STAC 5881 相关的策略，但这次观察到的是部署了一种以前未记录的名为 “Frag ”的勒索软件。”

在最近的一次攻击中，威胁组织 STAC 5881 通过被入侵的 VPN 设备访问网络，利用 VEEAM 漏洞，然后创建了名为 “point ”和 “point2 ”的账户。使用加密设置执行的 Frag 勒索软件在文件中添加了 \*.frag 扩展名，但最终被 Sophos 的 CryptoGuard 阻止。

![Veeam Backup & Replication (VBR) Frag ransomware]()
网络安全公司 Agger Labs 的研究人员还详细介绍了 Frag 背后的行为者与 Akira 和 Fog 威胁行为者在战术、技术和做法上的相似之处。

“Frag 勒索软件隐身的一个关键原因是它依赖于 LOLBins，这是一种被更多传统威胁行为者广泛采用的策略。通过使用大多数网络中已经存在的熟悉的合法软件，攻击者可以在绕过端点检测系统的同时进行恶意操作。“Agger Labs 表示，”虽然这在威胁行为者领域肯定不是什么新鲜事，但它确实表明了勒索软件制作者正在如何调整他们的方法。“使用 LOLBins 并不是 Frag 独有的做法；Akira 和 Fog 等勒索软件也采用了类似的策略，重点是混入正常的网络活动并隐藏在众目睽睽之下。通过使用 LOLBins，这些运营商利用可信软件达到恶意目的，增加了及时发现的难度。”

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/170717/malware/veeam-backup-replication-flaw-frag-ransomware.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301700](/post/id/301700)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/170717/malware/veeam-backup-replication-flaw-frag-ransomware.html)

如若转载,请注明出处： <https://securityaffairs.com/170717/malware/veeam-backup-replication-flaw-frag-ransomware.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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