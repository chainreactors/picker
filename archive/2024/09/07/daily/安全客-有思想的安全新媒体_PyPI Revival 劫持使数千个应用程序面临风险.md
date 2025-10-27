---
title: PyPI Revival 劫持使数千个应用程序面临风险
url: https://www.anquanke.com/post/id/299868
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:26.485689
---

# PyPI Revival 劫持使数千个应用程序面临风险

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

# PyPI Revival 劫持使数千个应用程序面临风险

阅读量**100877**

发布时间 : 2024-09-06 11:15:51

**x**

##### 译文声明

本文是翻译文章，文章来源：infosecurity magazine

原文地址：<https://www.infosecurity-magazine.com/news/pypi-revival-hijack/>

译文仅供参考，具体内容表达以及含义原文为准。

据安全研究人员称，一种新的软件供应链攻击正在被广泛利用。

该技术针对通过 Python 包索引 （PyPI） 分发的 Python 应用程序。

软件供应链安全公司 JFrog 的研究人员认为，这次被称为“Revival Hijack”的攻击可能会影响 22,000 个现有的 Python 包。反过来，这可能导致数千万次受感染的下载。

Revival Hijack 利用了作者从 PyPI 存储库中删除项目时产生的潜在安全漏洞。

开发人员从 PyPI 中删除包后，任何其他用户都可以注册包名称。然后，黑客可以劫持软件包名称并使用它来分发恶意代码。

## “曾经安全”的供应链攻击风险

Revival Hijack 利用了受害者可以在不知道它已被更改或感染的情况下不知不觉地更新“曾经安全”的软件包这一事实。此外，CI/CD 计算机通常设置为自动安装软件包更新。

JFrog 研究人员 Brian Moussalli 和 Andrey Polkovnichenko 警告说，这比以前的软件供应链攻击构成的风险要大得多，这些攻击依赖于拼写错误，因此是人为错误来分发恶意代码。

研究团队使用名称相同但版本号不同、代码完全不同的冒名顶替包重现了这次攻击。在进一步的测试中，他们发现 “安全劫持” 的程序包在三个月内被下载了 200,000 次。

“Revival Hijack 不仅仅是一种理论攻击——我们的研究团队已经看到它在野外被利用，”JFrog 研究团队负责人 Brian Moussalli 解释说。

“在处理已删除的软件包时使用易受攻击的行为允许攻击者劫持现有软件包，从而可以在没有用户交互的情况下将其安装到目标系统。”

## 面向开发人员的受感染代码警告

据 JFrog 研究人员称，网络安全团队已经降低了拼写错误的风险。这迫使恶意黑客寻找其他方法将受感染的代码放入存储库，例如 Revival Hijack。

尽管 PyPI 确实警告删除包的开发人员，其名称可以重复使用，并限制替换包的特定版本，但 JFrog 研究人员呼吁“制定更严格的政策，完全禁止重复使用包名称”。

云安全专家 Sysdig 威胁研究总监 Michael Clark 告诉 *Infosecurity*，使用代码存储库的开发人员也需要保持警惕。

“PyPI 等存储库在安全性方面提出了严峻的挑战，因为它们通常受到开发人员的隐式信任，”他说。

“只要名字没错，危险感就很低。Revival Hijack 攻击演示了此问题，因为恶意存储库的名称将与以前受信任的名称匹配。必须对这些存储库中的依赖项进行静态和运行时分析，以防止使用此向量的攻击。

本文翻译自infosecurity magazine [原文链接](https://www.infosecurity-magazine.com/news/pypi-revival-hijack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299868](/post/id/299868)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity magazine](https://www.infosecurity-magazine.com/news/pypi-revival-hijack/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/pypi-revival-hijack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [“曾经安全”的供应链攻击风险](#h2-0)
* [面向开发人员的受感染代码警告](#h2-1)

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