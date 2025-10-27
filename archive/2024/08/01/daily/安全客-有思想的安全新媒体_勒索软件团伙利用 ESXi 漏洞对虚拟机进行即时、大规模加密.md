---
title: 勒索软件团伙利用 ESXi 漏洞对虚拟机进行即时、大规模加密
url: https://www.anquanke.com/post/id/298620
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:08.446760
---

# 勒索软件团伙利用 ESXi 漏洞对虚拟机进行即时、大规模加密

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

# 勒索软件团伙利用 ESXi 漏洞对虚拟机进行即时、大规模加密

阅读量**74294**

发布时间 : 2024-07-31 11:20:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/ransomware-gangs-exploit-esxi-bug-for-instant-mass-encryption-of-vms>

译文仅供参考，具体内容表达以及含义原文为准。

多个勒索软件组织一直在利用 VMware ESXi 虚拟机管理程序中的身份验证绕过漏洞，以在虚拟化环境中快速部署恶意软件。

VMware 在 CVSS 量表上为该漏洞 （CVE-2024-37085） 打了“中”6.8 分（满分 10 分）。平均分数很大程度上是因为它要求攻击者在目标的 Active Directory （AD） 中拥有现有权限。

但是，如果他们确实具有 AD 访问权限，攻击者可能会造成重大损害。无需任何技术诡计，他们就可以使用 CVE-2024-37085 立即将其 ESXi 权限扩展到最大，从而为勒索软件部署、数据泄露、横向移动等打开大门。Storm-0506（又名 Black Basta）、Storm-1175、Manatee Tempest（Evil Corp 的一部分）和 Octo Tempest（又名 Scattered Spider）等组织已经尝试过，部署了 Black Basta 和 Akira 等勒索软件。

博通（Broadcom）最近在其网站上发布了一个修复程序。

## CVE-2024-37085 的工作原理

某些组织将其 ESXi 虚拟机管理程序配置为使用 AD 进行用户管理。事实证明，通过这样做，组织将自己暴露在意想不到的事情中。默认情况下，ESXi 虚拟机管理程序向名为“ESX Admins”的 AD 域组的任何成员授予完全管理访问权限。

正如 Microsoft 在一篇博客文章中指出的那样，没有特别的理由说明为什么虚拟机管理程序应该期待这样的域组，或者有关于如何处理它的规则。“此组不是 Active Directory 中的内置组，默认情况下不存在。当服务器加入域时，ESXi 虚拟机监控程序不会验证此类组是否存在，并且仍然以完全管理访问权限对待具有此名称的组的任何成员，即使该组最初不存在，“威胁情报团队写道。“此外，组中的成员身份由名称确定，而不是由安全标识符 （SID） 确定。”

Dark Reading 已联系 Broadcom，询问这个问题最初是如何产生的。

利用 CVE-2024-37085 完全是微不足道的。只要攻击者在 AD 中拥有足够的权限，他们只需在目标域中创建一个“ESX 管理员”组并向其添加用户，即可获得 ESXi 管理员权限。他们还可以将任何现有组重命名为“ESX Admins”，并使用其现有用户之一或添加新用户。

## 虚拟机管理程序的风险

“针对 ESXi 和虚拟机的勒索软件攻击越来越普遍，尤其是自 2020 年左右以来，当时企业加大了数字化转型的步伐，并利用了现代混合云和虚拟化本地环境，“Sectigo 产品高级副总裁 Jason Soroko 解释道。

尽管虚拟化环境具有所有的商业意义，但它也为黑客提供了独特的好处。虚拟机管理程序倾向于同时运行多个虚拟机，这使它们成为尽可能广泛地攻击勒索软件的一站式商店，而这些虚拟机通常托管关键服务和业务数据。

正如Microsoft在其博客中指出的那样，它们对黑客的效用使得更加令人不安的是，安全产品对虚拟机监控程序的可见性和保护有限。索罗科解释说，这是“由于他们的孤立性、复杂性以及保护他们所需的专业知识。这种隔离使得传统的安全工具难以监控和保护整个环境，而API集成的限制进一步加剧了这个问题。

为了弥补这些缺点，Microsoft 强调了及时更新补丁的重要性，并围绕关键和易受攻击的资产实施更广泛的网络卫生。Soroko 指出：“攻击者喜欢使用阻力最小的路径，以提供最大的机会，”他补充说，勒索软件攻击者将来只会越来越多地针对这些系统。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/ransomware-gangs-exploit-esxi-bug-for-instant-mass-encryption-of-vms)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298620](/post/id/298620)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/ransomware-gangs-exploit-esxi-bug-for-instant-mass-encryption-of-vms)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/ransomware-gangs-exploit-esxi-bug-for-instant-mass-encryption-of-vms>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [CVE-2024-37085 的工作原理](#h2-0)
* [虚拟机管理程序的风险](#h2-1)

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