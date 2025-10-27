---
title: 勒索软件团伙利用窃取的Microsoft Entra ID凭证入侵云服务
url: https://www.anquanke.com/post/id/300526
source: 安全客-有思想的安全新媒体
date: 2024-09-30
fetch_date: 2025-10-06T18:20:03.747653
---

# 勒索软件团伙利用窃取的Microsoft Entra ID凭证入侵云服务

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

# 勒索软件团伙利用窃取的Microsoft Entra ID凭证入侵云服务

阅读量**280822**

发布时间 : 2024-09-29 15:50:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Connor Jones，文章来源：theregister

原文地址：<https://www.theregister.com/2024/09/27/microsoft_storm_0501/>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft 最新的威胁情报博客向所有组织发出警告，指出 Storm-0501 最近在策略、目标和后门混合云环境方面的转变。

Storm-0501 使用一系列策略来实现其目标，倾向于通过云入侵来控制整个网络。成员首先可以访问本地环境，然后再转向云、植入后门以实现持久访问并部署勒索软件。

自 2021 年以来，Storm-0501 一直活跃在 Microsoft 看来仍然被视为一个新兴的组，因此“Storm”命名约定是为仍在发展中的组保留的。

尽管地位初出茅庐，但作为 LockBit、ALPHV、Hive 和 Hunters International 勒索软件附属计划的成员，该组织在实施勒索软件攻击方面一直多产。

最近，Microsoft 发现它部署了 Embargo 的勒索软件有效载荷，并将其与更成熟、出于经济动机的团体进行了单独比较，例如 Octo Tempest （Scattered Spider） 和 Manatee Tempest （Evil Corp）。

典型的 Storm-0501 攻击是相当标准的——没有太多的惊喜。在许多情况下，初始访问代理 （IAB） 用于初始访问，而面向公众的服务器中的漏洞也会在需要时被利用。

在此阶段，该组织以权限过高的帐户为目标，一旦其成员获得了对这些帐户的控制权，他们通常会利用 Impacket 的 SecretsDump 模块来扫描可用于入侵更多帐户的其他凭据。此过程会重复进行，直到攻击者控制了大量帐户，在他们的理想环境中，这将包括多个 Domain Admin 帐户。

老忠实的 Cobalt Strike 用于横向移动，这通常以访问域控制器以及随后的数据盗窃和勒索软件部署而告终。

然而，最近的攻击让研究人员有理由感到担忧。在凭据收集阶段，Storm-0501 使用被盗的 Entra ID 凭据从本地转移到云环境，在那里他们将继续植入后门。

攻击者采用两种不同的方法来获得对 Entra ID 的控制权，第一种是入侵 Entra Connect Sync 服务帐户，其凭据以加密形式保存在服务器的磁盘或远程 SQL 服务器上。

“我们可以非常有信心地评估，在最近的 Storm-0501 活动中，威胁行为者专门定位了 Microsoft Entra Connect Sync 服务器，并设法提取了 Microsoft Entra Connect 云和本地同步帐户的纯文本凭据，”Microsoft 写道。

“我们评估认为，威胁行为者之所以能够实现这一目标，是因为本博客文章中描述的先前恶意活动，例如使用 Impacket 窃取凭据和 DPAPI 加密密钥，以及篡改安全产品。

“Microsoft Entra Connect Sync 帐户的泄露给目标带来了高风险，因为它可能允许威胁行为者设置或更改任何混合帐户（同步到 Microsoft Entra ID 的本地帐户）的 Microsoft Entra ID 密码。”

Storm-0501 用于成功转向云的另一种策略是入侵本地域管理员帐户，该帐户在云中具有等效帐户，该帐户不受 MFA 保护，并且还带有全局管理员角色。

同步服务不适用于 Entra 中的此类帐户，因此攻击者必须足够幸运地找到一个既不受 MFA 保护又使用与本地帐户相同密码的帐户。

启用 MFA 会使这种攻击途径更加复杂，并且不太可能成功。在这种情况下，攻击者必须篡改 MFA 保护本身，或者采取额外的步骤来破坏用户的设备，并劫持其云会话或提取 Entra 访问令牌。

无论 Storm-0501 采用哪种方式，它通常都会导致通过创建联合域来植入后门以实现持久访问，从而允许它以任何 Entra ID 租户用户的身份进行身份验证。

一旦目标被彻底入侵并且其数据被窃取，勒索软件就会出现，或者不会。虽然 Storm-0501 现在选择了 Embargo 的有效载荷，它遵循典型的双重勒索模型，但并非所有攻击都会导致勒索软件部署。Microsoft 在其博客中表示，有些攻击在建立后门后才停止，其中还包括威胁搜寻技巧和大量入侵指标。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/09/27/microsoft_storm_0501/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300526](/post/id/300526)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/09/27/microsoft_storm_0501/)

如若转载,请注明出处： <https://www.theregister.com/2024/09/27/microsoft_storm_0501/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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