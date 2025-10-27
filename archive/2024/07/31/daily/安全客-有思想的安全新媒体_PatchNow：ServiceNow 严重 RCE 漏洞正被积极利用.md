---
title: PatchNow：ServiceNow 严重 RCE 漏洞正被积极利用
url: https://www.anquanke.com/post/id/298577
source: 安全客-有思想的安全新媒体
date: 2024-07-31
fetch_date: 2025-10-06T17:41:44.771707
---

# PatchNow：ServiceNow 严重 RCE 漏洞正被积极利用

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

# PatchNow：ServiceNow 严重 RCE 漏洞正被积极利用

阅读量**83621**

发布时间 : 2024-07-30 14:33:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/patchnow-servicenow-critical-rce-bugs-active-exploit>

译文仅供参考，具体内容表达以及含义原文为准。

BreachForums 上的一名威胁行为者声称，在利用基于云的 IT 服务管理平台中最近披露的两个关键漏洞后，已从超过 105 个 ServiceNow 数据库中收集了电子邮件地址和相关哈希值。

Resecurity 的 HUNTER 威胁团队的研究人员上周晚些时候警告说，两个 ServiceNow 漏洞（CVE-2024-4879，CVSS 评分为 9.3 分，满分 10 分;CVE-2024-5217，CVSS 评分为 9.2）正在野外被积极利用，并表示他们看到 BreachForums 成员将数据以 5,000 美元的价格出售。

与此同时，美国网络安全和基础设施安全局 （CISA） 今天将这两个漏洞添加到其已知的被利用漏洞目录中，因为最近几天有多份关于其他利用这些漏洞的尝试的报告。联邦文职行政部门机构必须在 8 月 19 日之前应用 ServiceNow 的补丁，或者停止使用该平台，直到他们能够解决问题。

重新安全研究人员表示，对ServiceNow的攻击应该是意料之中的。他们写道：“在暗网上的多个地下论坛上已经发现了喋喋不休的喋喋不休，突出了威胁行为者寻求对IT服务台、公司门户和其他企业系统的妥协访问，这些系统通常为员工和承包商提供远程访问。“这些系统可用于预先定位和攻击计划，以及侦察。

## 未经身份验证的 RCE 链允许完全访问

CVE-2024-4879 是 ServiceNow 的“温哥华”和“华盛顿特区”版本平台中的输入验证漏洞。它使未经身份验证的远程攻击者能够执行任意代码。供应商已评估该漏洞易于利用，并且不需要用户交互或特殊条件。CVE-2024-5217 是温哥华、华盛顿特区和早期版本的 Now 中类似的严重输入验证缺陷，该漏洞还允许远程代码执行 （RCE） 并且很容易被利用。

ServiceNow 于 7 月 10 日发布了针对这两个漏洞的修补程序，并针对同一软件中的第三个（不太严重）漏洞 （CVE-2024-5178） 进行了修复。AssetNote 发现了这三个漏洞，并于 5 月将其报告给 ServiceNow，将这些问题描述为“允许完全数据库访问和完全访问任何服务器的漏洞链”，组织可能使用这些漏洞来访问云托管实例。

一个公开的概念验证漏洞 （PoC） 很快发布，为野外的广泛攻击铺平了道路。

## 野外攻击开始升级

Resecurity上周报告说，观察到多个攻击者探测ServiceNow实例，以检查它们是否容易受到攻击。“最初，威胁行为者正在注入有效载荷并检查响应中的特定乘法结果，”Resecurity说。接下来，攻击者注入了一个有效载荷，该有效载荷检查了数据库的内容并将其提取出来。“最后阶段涉及倾倒用户列表并从受感染的实例中收集相关的元数据。”

Resecurity研究人员在给Dark Reading的电子邮件评论中指出，到目前为止，这些攻击已经针对Resecurity的客户（包括一家能源公司、一个数据中心组织、一个中东政府机构和一家软件开发商）、关键基础设施、外国政府以及金融机构。研究人员说，根据多名受害者的反馈，他们中的一些人似乎一直在使用ServiceNow的本地或自托管版本，或者由于某种原因选择不再接收公司的自动更新。

“值得注意的是，他们中的一些人不知道发布的补丁，在某些情况下，他们的开发人员和软件工程师使用了过时或维护不善的实例，”该公司指出。

Imperva在7月23日还表示，它已经观察到有人试图利用针对金融部门和其他多个行业组织的漏洞。当时，Imperva报告说，在多达6,000个地点观察到了开采尝试。

“攻击者主要利用自动化工具来针对登录页面，”Imperva说。“我们在攻击中看到了两种常见的有效载荷：一种用于测试远程代码执行（RCE）是否可行，另一种用于显示数据库用户和密码的命令。

对 Internet 扫描可见的 ServiceNow 实例数量的估计值（因此可能是利用尝试的目标）从高端的 297,700 多个到另一端的不到 10,000 个不等。

“不幸的是，对于有动机的攻击者来说，找到并利用这些易受攻击的系统并不是特别困难，”DoControl的联合创始人兼CRO Omri Weinberg说。

## 自托管 MID 服务器可能成为目标

Weinberg说，ServiceNow是一个广泛使用的平台，其实例通常具有面向公众的组件，威胁行为者可以使用自动扫描工具相对容易地找到这些组件。一旦攻击者能够找到易受攻击的实例，“漏洞利用链就不需要高水平的技术复杂性，使其能够被广泛的攻击者访问。

Weinberg 建议无法立即修补的组织将重点放在基本的安全卫生上，例如加强访问控制、增加监控，并在可能的情况下将访问限制为仅受信任的 IP 范围。

Contrast Security的产品安全总监Naomi Buckwalter表示，使用自托管代理服务器（ServiceNow称为MID服务器）将内部系统连接到ServiceNow基于云的平台的组织应特别注意新的缺陷。

Buckwalter说：“虽然MID服务器不会直接暴露在互联网上，但设法破坏内部网络的攻击者可能会利用这些漏洞来访问敏感数据，并破坏在Now平台上运行的关键业务运营。“在最坏的情况下，攻击者可能会泄露数据、操纵文件并未经授权访问机密信息，”她说。“ServiceNow 已经发布了补丁来解决这些漏洞，但如果没有应用更新，使用自托管 MID 服务器的组织可能仍面临风险。”

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/patchnow-servicenow-critical-rce-bugs-active-exploit)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298577](/post/id/298577)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/patchnow-servicenow-critical-rce-bugs-active-exploit)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/patchnow-servicenow-critical-rce-bugs-active-exploit>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
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

* [未经身份验证的 RCE 链允许完全访问](#h2-0)
* [野外攻击开始升级](#h2-1)
* [自托管 MID 服务器可能成为目标](#h2-2)

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