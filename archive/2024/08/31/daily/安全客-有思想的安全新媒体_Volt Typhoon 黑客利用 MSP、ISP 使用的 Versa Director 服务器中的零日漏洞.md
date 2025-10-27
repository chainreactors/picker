---
title: Volt Typhoon 黑客利用 MSP、ISP 使用的 Versa Director 服务器中的零日漏洞
url: https://www.anquanke.com/post/id/299663
source: 安全客-有思想的安全新媒体
date: 2024-08-31
fetch_date: 2025-10-06T17:59:26.965769
---

# Volt Typhoon 黑客利用 MSP、ISP 使用的 Versa Director 服务器中的零日漏洞

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

# Volt Typhoon 黑客利用 MSP、ISP 使用的 Versa Director 服务器中的零日漏洞

阅读量**94544**

发布时间 : 2024-08-30 14:43:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 菲奥娜·杰克逊，文章来源： techrepublic

原文地址：<https://www.techrepublic.com/article/volt-typhoon-exploits-versa-director/>

译文仅供参考，具体内容表达以及含义原文为准。

全球大约有 163 台设备仍面临 CVE-2024-39717 漏洞的攻击。

中国国家资助的黑客组织 Volt Typhoon 被发现利用托管服务提供商和互联网服务提供商使用的 Versa Director 服务器中的零日漏洞。在 Lumen Technologies 发现 CVE-2024-39717 的主动利用后，CVE-2024-39717 于 8 月 23 日被添加到 CISA 的“已知利用漏洞目录”中。

来自 Censys 的数据显示，尽管 Versa Networks 发布了 Versa Director 版本 21.2.3、22.1.2 和 22.1.3 的补丁，但美国、菲律宾、上海和印度仍有 163 台设备暴露在风险中。这家安全公司敦促这些设备的用户将它们划分到受保护的网络中，并将它们与互联网隔离开来。

## 为什么网络犯罪分子以 Versa Director 服务器为目标

Versa Director 服务器使 MSP 和 ISP 能够集中管理运行 SD-WAN 软件的设备的网络配置。它们成为黑客的热门目标，因为它们可用于利用多个系统。

由于存在大规模攻击的可能性，Versa Networks 已将该漏洞评为“高严重性”，尽管它相对难以利用。

CVE-2024-39717 影响 22.1.4 之前的所有 Versa Director 版本。网络犯罪分子使用定制的 Web Shell 来利用它，Lumen Technologies 的网络研究部门 Black Lotus Labs 将其称为“VersaMem”。Web Shell 会拦截凭据，然后攻击者可以使用这些凭据来获得对其他用户网络的授权访问。

根据 Black Lotus Labs 的漏洞报告，他们将 CVE-2024-39717 的利用与 Volt Typhoon 联系起来，并且具有“中等可信度”。它还表示，“可能正在针对未修补的 Versa Director 系统进行攻击”。

Versa 坚持认为，只有一个已确认的 Advanced Persistent Threat 参与者利用它的实例。它还表示，该客户“未能实施分别于 2017 年和 2015 年发布的系统强化和防火墙指南”——这意味着管理端口暴露在外。此端口为威胁行为者提供了初始访问权限，而无需 Versa Director GUI。

然而，Black Lotus Labs 团队表示，它已经在四家美国公司和一家非美国公司发现了利用该漏洞的威胁行为者。自 6 月 12 日起在 ISP、MSP 和 IT 领域开展业务。Versa 表示，基于第三方提供商的观察的实例“迄今为止未经证实”。

分析师在他们的报告中写道：“威胁行为者通过暴露的 Versa 管理端口获得初始管理访问权限，该端口旨在实现 Director 节点的高可用性 （HA） 配对，从而导致 VersaMem Web Shell 的利用和部署。

CISA 建议作为公司漏洞管理实践的一部分，快速修复已知已利用漏洞目录中包含的所有漏洞。

如何利用 CVE-2024-39717？

CVE-2024-39717 允许具有高级权限的经过身份验证的用户上传恶意文件，有时伪装成图像，然后可以执行有害代码。一旦被利用，该漏洞可用于获得未经授权的访问和提升权限。

Volt Typhoon 威胁行为者通过利用暴露的 Versa 管理端口获得了对 Versa Director 的特权访问，该端口旨在实现 Director 节点的高可用性配对。然后，他们在 Apache Tomcat Web 服务器上部署了一个自定义 Web shell，为他们提供远程控制，然后使用内存注入技术将恶意代码插入合法的 Tomcat 进程。这种注入的代码允许他们运行命令并控制受感染的系统，同时与正常流量混在一起。

最后，他们修改了 Versa 的“setUserPassword”身份验证功能，以明文形式拦截和捕获客户端凭证，然后他们可以使用这些凭证来破坏客户端基础设施。

该 Web shell 还用于挂接 Tomcat 的“doFilter”请求过滤功能并拦截入站 HTTP 请求。然后，威胁行为者可以检查它们是否有敏感信息或动态加载内存中的 Java 模块。

## 谁是 Volt Typhoon？

Volt Typhoon 是一个由中国政府支持的黑客组织，自 2021 年年中活跃以来，已对关键基础设施进行了数百次攻击。2023 年 5 月，Microsoft 发布了关于该组织的警告，称其使用“离地生活”数据提取和网络间谍技术。

2023 年 12 月，FBI 的一项调查发现了该团伙发起的广泛僵尸网络攻击，该攻击由美国及其海外领土的数百台私有路由器创建。接下来的一个月，司法部调查人员表示，该恶意软件已从受影响的路由器中删除，从而消除了僵尸网络。

## 保护 Versa Director 服务器的建议

Versa Networks 和 Lumen Technologies 都向 Versa Director 服务器的用户提出了许多建议：

1. **立即修补：**提供了版本 21.2.3、22.1.2 和 22.1.3 的补丁。
2. **应用强化最佳实践：**Versa Networks 建议遵循其防火墙和系统强化要求。
3. **检查漏洞是否已被利用：**
   a） 检查“/var/versa/vnms/web/custom\_logo/”是否有任何可疑文件。运行命令 “file -b –mime-type <.png file>” 将文件类型报告为 “image/png”。
   b） 从非 Versa 节点 IP（例如 SOHO 设备）搜索与 Versa Director 服务器上端口 4566 的交互。
   c） 检查新创建的用户帐户和其他异常文件。
   d） 查看现有帐户、日志和凭据，并在检测到入侵迹象时对任何横向移动尝试进行分类。
4. **阻止对端口 4566 和 4570 的外部访问：**确保端口仅在活动和备用 Versa Director 节点之间为 HA 配对流量打开。阅读名为 Versa Director HA 端口漏洞利用 – 发现和补救的客户支持文章。

本文翻译自 techrepublic [原文链接](https://www.techrepublic.com/article/volt-typhoon-exploits-versa-director/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299663](/post/id/299663)

安全KER - 有思想的安全新媒体

本文转载自:  [techrepublic](https://www.techrepublic.com/article/volt-typhoon-exploits-versa-director/)

如若转载,请注明出处： <https://www.techrepublic.com/article/volt-typhoon-exploits-versa-director/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [为什么网络犯罪分子以 Versa Director 服务器为目标](#h2-0)
* [谁是 Volt Typhoon？](#h2-1)
* [保护 Versa Director 服务器的建议](#h2-2)

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