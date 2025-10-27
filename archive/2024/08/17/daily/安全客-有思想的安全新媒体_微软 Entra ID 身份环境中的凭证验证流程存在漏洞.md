---
title: 微软 Entra ID 身份环境中的凭证验证流程存在漏洞
url: https://www.anquanke.com/post/id/299193
source: 安全客-有思想的安全新媒体
date: 2024-08-17
fetch_date: 2025-10-06T18:02:12.392664
---

# 微软 Entra ID 身份环境中的凭证验证流程存在漏洞

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

# 微软 Entra ID 身份环境中的凭证验证流程存在漏洞

阅读量**37503**

发布时间 : 2024-08-16 14:47:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jai Vijayan，文章来源：DARKREADING

原文地址：[https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds](https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds%20)

译文仅供参考，具体内容表达以及含义原文为准。

研究人员已经找到了一种方法来操纵 Microsoft Entra ID 身份环境中的凭据验证过程，他们说攻击者可以使用这种方法来绕过混合身份基础设施中的身份验证。

该攻击需要攻击者在托管直通身份验证 （PTA） 代理的服务器上拥有管理员访问权限，该代理允许用户使用本地 Microsoft Entra ID（以前称为 Azure Active Directory）凭据登录云服务。然后，他们可以使用该访问权限以Entra ID用户的身份登录不同的本地域，而无需单独进行身份验证，Cymulate的研究人员在本周的一份报告中表示 。

## 将 PTA 转变为双重代理

“这个漏洞有效地将PTA代理变成了双重代理，允许攻击者在不知道实际密码的情况下以任何同步AD用户的身份登录，”Cymulate安全研究员Ilan Kalendarov写道。“如果分配了此类权限，则无论其原始同步的 AD 域如何，这可能会向全局管理员用户授予访问权限”，并允许横向移动到不同的本地域。

Microsoft没有立即回应Dark Reading的置评请求。但根据 Cymulate 的说法，Microsoft 计划在其端修复代码以解决这个问题。然而，这家总部位于以色列的安全供应商表示，该公司还将这种攻击技术描述为仅构成中等严重程度的威胁。

本月早些时候，在 Black Hat USA 2024 上，Semperis 的一名安全研究员披露了 Entra ID 的另一个问题，该问题允许攻击者访问组织的整个云环境。攻击者越来越关注 Entra ID、Okta 和 Ping 等云身份服务，因为一旦他们能够入侵这些提供商之一，他们就可以完全访问 SaaS 应用程序中的企业数据。

Cymulate 的概念验证攻击利用了该公司所说的 Entra ID 中的漏洞，该漏洞是在将多个本地域同步到单个 Azure 租户时。在对Dark Reading的评论中，Kalendarov表示，这是组织在简化不同部门之间的用户访问时经常使用的做法，例如，在简化拥有多个子公司的公司的IT管理时。他说，将多个本地域同步到单个 Azure 租户可实现不同业务部门之间的无缝协作。

## 处理不当的请求

Cymulate 发现，在此配置中，PTA 代理有时可能会错误地处理不同本地域的身份验证请求。该公司的调查显示，当用户尝试登录 Entra ID 时，密码验证请求会被放入服务队列中，并由任何可用的 PTA 从任何同步的本地域中检索。

Cymulate 发现，有时，PTA 代理会从不同的本地域检索用户名和密码，并尝试根据自己的 Windows Server AD 进行验证。 “这会导致身份验证失败，因为服务器无法识别特定用户，”Kalendarov 说。“这取决于哪个 PTA 代理首先收到请求。然而，在我们的测试和研究中，这是一个相当普遍的情况。

Cymulate 的 POC 利用了这个特定问题。为了证明攻击者如何滥用它，研究人员首先将一个不受管理的动态链接库注入到 PTA 代理中。加载后，托管 DLL 会截获负责在开头和结尾检查用户凭据的 ValidateCredential 函数。通过拦截此函数，攻击者可以操纵其结果，始终强制其返回 True，Cymulate 发现。“这意味着，即使我们提供来自不同域的用户的凭据，钩子也会返回 True，”Cymulate 说。“因此，我们将能够以任何同步的本地 AD 中的任何用户身份登录。”

Kalendarov 说，只有当攻击者首先在 PTA 服务器上获得本地管理员访问权限时，攻击才会起作用。“从理论上讲，在有些攻击中，您首先进入PTA服务器并复制证书，然后创建自己的复制服务器。攻击也会在该服务器上起作用。

Kalendarov 表示，Microsoft 可能认为这种威胁是适度的，因为攻击者需要首先获得本地管理员访问权限。此外，Microsoft 建议组织将服务器视为 Tier-0 组件，这意味着他们应实施最高级别的安全控制，例如严格的访问管理、增强的监视和网络隔离。但现实情况是，大多数公司并不将其视为Tier-0组件，他说。Microsoft 还建议组织为所有同步用户实施双因素身份验证。

Cymulate 本身建议 Microsoft 实施域感知路由，以确保将身份验证请求定向到适当的 PTA 代理。“此外，在同一租户内的不同本地域之间建立严格的逻辑分离可能是有益的，”该公司指出。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds%20)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299193](/post/id/299193)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds%20)

如若转载,请注明出处： [https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds](https://www.darkreading.com/application-security/unfixed-microsoft-entra-id-authentication-bypass-threatens-hybrid-clouds%20)

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [将 PTA 转变为双重代理](#h2-0)
* [处理不当的请求](#h2-1)

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