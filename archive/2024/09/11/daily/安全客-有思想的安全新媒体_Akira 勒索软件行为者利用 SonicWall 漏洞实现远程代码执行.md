---
title: Akira 勒索软件行为者利用 SonicWall 漏洞实现远程代码执行
url: https://www.anquanke.com/post/id/299950
source: 安全客-有思想的安全新媒体
date: 2024-09-11
fetch_date: 2025-10-06T18:21:04.079488
---

# Akira 勒索软件行为者利用 SonicWall 漏洞实现远程代码执行

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

# Akira 勒索软件行为者利用 SonicWall 漏洞实现远程代码执行

阅读量**90885**

发布时间 : 2024-09-10 14:20:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/ics-ot-security/akira-ransomware-actors-exploit-sonicwall-bug-for-rce>

译文仅供参考，具体内容表达以及含义原文为准。

包括 Akira 勒索软件附属公司在内的威胁行为者已开始利用 SonicWall 上个月在其第 5 代、第 6 代和第 7 代防火墙产品的某些版本中披露并修补的一个关键远程代码执行 （RCE） 漏洞。

该攻击活动促使美国网络安全和基础设施安全局 （CISA） 将标识为 CVE-2024-40766 的漏洞添加到其已知已利用漏洞 （KEV） 数据库中。该漏洞是 CISA 本周添加到其 KEV 目录中的三个漏洞之一，并希望联邦民事行政部门 （FCEB） 机构在 9 月 30 日之前解决。

## 不正确的访问控制错误

CVE-2024-40766 是 SonicWall SonicOS 管理访问组件中的一个不当访问控制错误，该组件运行在公司的 SonicWall Firewall 第 5 代和第 6 代设备，以及运行 SonicOS 7.0.1-5035 及更早版本的第 7 代设备。它允许攻击者完全控制受影响的设备，并在某些情况下导致防火墙完全崩溃。

SonicWall 于 8 月 22 日首次披露了该漏洞，并为其分配了 9.3 级的严重性评级，在 CVSS 量表上可能的最高等级为 10。9 月 6 日，网络安全供应商更新了公告，将本地 SSLVPN 帐户也列为容易受到 CVE-2024-40766 攻击。该公告还警告客户注意针对该漏洞的攻击活动，并敦促组织立即应用该公司建议的缓解措施。

Artic Wolf 周五表示，它观察到 Akira 勒索软件附属公司滥用该漏洞来入侵 SonicWall 设备上的 SSLVPN 帐户。“在每种情况下，被盗用的帐户都是设备本身的本地帐户，而不是与 Microsoft Active Directory 等集中式身份验证解决方案集成，”Arctic Wolf 说。“此外，所有被盗账户的 MFA 都被禁用了。”

SonicWall 希望受影响设备的客户尽快更新到该技术的修复版本。该公司还建议组织将防火墙管理功能限制为受信任的来源，并禁用通过 Internet 的 WAN 管理。“同样，对于 SSLVPN，请确保访问仅限于受信任的来源，或禁用来自 Internet 的 SSLVPN 访问，”SonicWall 建议道。

该公司还“强烈”倡导该公司的 Gen 5 和 Gen6 防火墙的管理员确保拥有本地管理帐户的 SSLVPN 用户立即更改密码，以防止未经授权的访问。此外，SonicWall 还建议组织为所有 SSLVPN 用户启用多因素身份验证 （MFA）。

## SonicWall：热门目标

SonicWall 的防火墙产品（如路由器、VPN 和其他网络安全技术）是一个有吸引力的攻击目标，因为威胁行为者可以通过破坏这些产品之一在目标网络上获得提升的权限。许多网络安全产品使攻击者能够访问流入和流出网络的所有流量，以及设备背后的宝贵资产和数据。近年来，Cisco 等安全供应商以及 CISA 和英国国家网络安全中心 （NCSC） 等实体一再警告称，攻击者将网络设备中的漏洞作为在目标设备上获得初步立足点的手段。

例如，今年早些时候，CISA 发现臭名昭著的伏特台风组织经常以 Fortinet、Ivanti、NetGear、Cisco 和 Citrix 等供应商的网络设备为目标，以获得初始访问权限。 思科在 2023 年的一份报告中表示，它观察到世界各地国家资助的行为者和情报机构持续存在恶意活动，包括流量操纵和复制、基础设施侦察以及积极尝试削弱网络防御 。该公司评估认为，攻击者喜欢以路由器和交换机等网络技术为目标，因为它们可以在受害者网络上实现深度可见性，而且组织通常无法正确保护和修补设备。

由于担心政府更容易受到此类攻击，CISA 于 6 月下旬发布了一项具有约束力的操作指令，要求 FCEB 机构实施强有力的措施来保护特定网络设备的管理接口，例如防火墙、路由器、交换机、VPN 集中器、负载均衡器和代理。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/ics-ot-security/akira-ransomware-actors-exploit-sonicwall-bug-for-rce)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299950](/post/id/299950)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/ics-ot-security/akira-ransomware-actors-exploit-sonicwall-bug-for-rce)

如若转载,请注明出处： <https://www.darkreading.com/ics-ot-security/akira-ransomware-actors-exploit-sonicwall-bug-for-rce>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [不正确的访问控制错误](#h2-0)
* [SonicWall：热门目标](#h2-1)

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