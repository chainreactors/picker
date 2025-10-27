---
title: 基于RADIUS协议的重大安全漏洞“BlastRADIUS”被发现
url: https://www.anquanke.com/post/id/297875
source: 安全客-有思想的安全新媒体
date: 2024-07-16
fetch_date: 2025-10-06T17:40:40.463477
---

# 基于RADIUS协议的重大安全漏洞“BlastRADIUS”被发现

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

# 基于RADIUS协议的重大安全漏洞“BlastRADIUS”被发现

阅读量**79455**

发布时间 : 2024-07-15 12:27:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Fiona Jackson，文章来源：TechRepublic

原文地址：<https://www.techrepublic.com/article/blastradius-vulnerability-radius-protocol/>

译文仅供参考，具体内容表达以及含义原文为准。

## 利用 BlastRADIUS 漏洞通过中间人攻击来操纵 RADIUS 认证过程。

网络安全研究人员揭露了 RADIUS 协议中的一个漏洞，被命名为 BlastRADIUS。虽然没有证据表明威胁行为者正在积极利用它，但研究团队呼吁所有 RADIUS 服务器都需要升级。

BlastRADIUS 攻击涉及攻击者拦截客户端（如路由器）与 RADIUS 服务器之间的网络流量。然后，攻击者可以操纵 MD5 哈希算法，使 Access-Denied 网络数据包被解读为 Access-Accept，从而无需正确的登录凭据即可访问客户端设备。

来自波士顿大学、Cloudflare、BastionZero、微软研究院、Centrum Wiskunde & Informatica 和加州大学圣地亚哥分校的研究人员团队首次在二月份发现了该漏洞，并通知了 InkBridge Networks 的首席执行官兼 RADIUS 专家 Alan DeKok。

根据由 DeKok 维护的 RADIUS 服务器 FreeRADIUS 发布的安全公告，BlastRADIUS 缺陷（现追踪为 CVE-2024-3596 和 VU#456537）是由于 RADIUS 协议的“根本设计缺陷”，因此，它不限于单一产品或供应商。

**请参阅：如何使用 FreeRADIUS 进行 SSH 身份验证**

DeKok在一份新闻稿中说：“网络技术人员将不得不安装固件升级，并重新配置全球几乎所有交换机，路由器，GGSN，BNG和VPN集中器。“我们预计在未来几周内会看到很多与RADIUS安全相关的讨论和活动。

## 什么是RADIUS协议？

RADIUS（远程认证拨入用户服务）是一种网络协议，提供集中式认证、授权和计费服务，用于连接到网络服务的用户。它广泛被互联网服务提供商和企业在交换机、路由器、接入服务器、防火墙和 VPN 产品中使用。

## 谁会受到 BlastRADIUS 缺陷的影响？

研究人员发现，使用 PAP、CHAP、MS-CHAP 和互联网上的 RADIUS/UDP 的 RADIUS 部署将受到 BlastRADIUS 缺陷的影响。这意味着 ISP、云身份提供商、电信公司和内部网络的企业面临风险，必须迅速采取行动，特别是如果 RADIUS 用于管理员登录。

家庭用户直接不受影响，但他们依赖 ISP 解决 BlastRADIUS 缺陷，否则他们的流量可能被导向攻击者控制的系统。

## BlastRADIUS攻击是如何工作的？

利用该漏洞通过中间人攻击来操纵 RADIUS 认证过程。关键在于 RADIUS 协议中，一些 Access-Request 数据包未经认证且缺乏完整性检查。

攻击者首先尝试使用错误的凭据登录客户端，生成一个发送给服务器的 Access-Request 消息。消息包含一个名为 Request Authenticator 的 16 字节值，通过 MD5 哈希生成。

Request Authenticator 打算由接收服务器与所谓的“共享秘密”一起计算其响应，只有客户端和服务器知道这个秘密。因此，当客户端收到响应时，它可以使用其 Request Authenticator 和共享秘密解密数据包，验证它是由受信任的服务器发送的。

但在 BlastRADIUS 攻击中，攻击者在消息到达服务器之前拦截并操纵 Access-Request 消息进行 MD5 碰撞攻击。攻击者向 Access-Request 消息添加“垃圾”数据，确保服务器的 Access-Denied 响应也包括此数据。然后，他们操纵此 Access-Denied 响应，使其被客户端解释为有效的 Access-Accept 消息，授予未经授权的访问权限。

尽管 MD5 已知存在弱点，允许攻击者生成碰撞或逆向哈希，但研究人员表示 BlastRADIUS 攻击“比简单应用旧的 MD5 碰撞攻击更复杂”，在速度和规模上更先进。这是第一次对 RADIUS 协议实际演示 MD5 攻击。

![Overview of the BlastRADIUS attack.]()

BlastRADIUS 攻击概述。图片：Cloudflare

Cloudflare 的研究人员在具有五分钟超时期的 RADIUS 设备上进行了攻击。然而，拥有高级计算资源的攻击者有可能在显著较短的时间内执行攻击，可能在 30 到 60 秒之间，这是许多 RADIUS 设备的默认超时期。

InkBridge Networks 的文档中写道：“关键在于，在许多情况下，Access-Request 数据包没有任何认证或完整性检查。攻击者然后可以执行选定前缀攻击，这允许修改 Access-Request 以替换有效响应为攻击者选择的响应。

“尽管响应经过认证并进行了完整性检查，但选定前缀漏洞允许攻击者几乎随心所欲地修改响应数据包。”

## 攻击者利用 BlastRADIUS 漏洞的难易程度如何？

虽然 BlastRADIUS 缺陷普遍存在，但利用它并非易事；攻击者需要能够读取、拦截、阻止和修改进出网络数据包的能力，而且没有公开的利用可供参考。攻击者还必须已经具备网络访问权限，这可能通过利用组织发送 RADIUS/UDP 跨越开放互联网或破坏企业网络的部分获得。

研究人员在专门针对 BlastRADIUS 的网站上表示：“即使 RADIUS 流量仅限于内部网络的受保护部分，配置或路由错误可能会无意中暴露此流量。拥有部分网络访问权限的攻击者可能能够利用 DHCP 或其他机制导致受害者设备将流量发送至专用 VPN 之外。”

此外，攻击者必须资金充足，因为每次 BlastRADIUS 攻击都需要大量的云计算能力。InkBridge Networks 在其 BlastRADIUS 常见问题解答中指出，对于希望针对特定用户的国家来说，此类成本“只是九牛一毛”。

## 组织如何保护自己免受 BlastRADIUS 攻击

安全研究人员为使用 RADIUS 协议的组织提供了以下建议：

* 在供应商提供的所有 RADIUS 客户端和服务器上安装最新更新。已部署补丁，以确保始终发送 Message-Authenticator 属性，并且请求和响应需要这些属性。FreeRADIUS 有一个更新版本可供下载，Palo Alto Networks 还发布了其 PAN-OS 防火墙的修复程序。
* 不要尝试一次更新所有 RADIUS 设备，因为可能会出错。理想情况下，首先集中精力升级 RADIUS 服务器。
* 考虑使用InkBridge Networks的验证工具来评估系统对BlastRADIUS和其他网络基础设施问题的影响。

本文翻译自TechRepublic [原文链接](https://www.techrepublic.com/article/blastradius-vulnerability-radius-protocol/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297875](/post/id/297875)

安全KER - 有思想的安全新媒体

本文转载自: [TechRepublic](https://www.techrepublic.com/article/blastradius-vulnerability-radius-protocol/)

如若转载,请注明出处： <https://www.techrepublic.com/article/blastradius-vulnerability-radius-protocol/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

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

* [利用 BlastRADIUS 漏洞通过中间人攻击来操纵 RADIUS 认证过程。](#h2-0)
* [什么是RADIUS协议？](#h2-1)
* [谁会受到 BlastRADIUS 缺陷的影响？](#h2-2)
* [BlastRADIUS攻击是如何工作的？](#h2-3)
* [攻击者利用 BlastRADIUS 漏洞的难易程度如何？](#h2-4)
* [组织如何保护自己免受 BlastRADIUS 攻击](#h2-5)

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