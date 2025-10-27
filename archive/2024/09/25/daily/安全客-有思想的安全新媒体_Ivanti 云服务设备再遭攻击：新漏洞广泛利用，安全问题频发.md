---
title: Ivanti 云服务设备再遭攻击：新漏洞广泛利用，安全问题频发
url: https://www.anquanke.com/post/id/300339
source: 安全客-有思想的安全新媒体
date: 2024-09-25
fetch_date: 2025-10-06T18:25:30.269407
---

# Ivanti 云服务设备再遭攻击：新漏洞广泛利用，安全问题频发

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

# Ivanti 云服务设备再遭攻击：新漏洞广泛利用，安全问题频发

阅读量**92952**

发布时间 : 2024-09-24 14:24:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kristina Beek，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/ivanti-cloud-service-appliance-attacked-vuln>

译文仅供参考，具体内容表达以及含义原文为准。

在修补一个漏洞后不到两周，Ivanti 于 9 月 19 日宣布，第二个关键的云服务设备 （CSA） 漏洞正在被广泛利用。

漏洞（CVE-2024-8963、CVSS 9.4）是 Ivanti CSA 中的一种路径遍历，允许未经身份验证的远程攻击者访问受限功能。攻击者已将其与之前披露的漏洞 CVE-2024-8190 联系起来，这是一个高度严重的操作系统命令注入漏洞，可能允许对设备进行未经授权的访问。如果攻击者具有管理员级别的权限，则可以利用该链进行远程代码执行 （RCE）。

“如果 CVE-2024-8963 与 CVE-2024-8190 结合使用，攻击者可以绕过管理员身份验证并在设备上执行任意命令，”该公司表示。

该消息发布之际，Ivanti 自 2023 年以来一直面临一系列安全问题。

## 不是第一个，也可能不是最后一个

仅今年一年，Ivanti 就面临着一个又一个的漏洞；今年 2 月，网络安全和基础设施安全局 （CISA） 下令在 48 小时内断开 Ivanti VPN 设备的连接、重建和重新配置，因为人们担心多个威胁行为者正在利用系统中发现的安全漏洞。

4 月，外国民族国家黑客利用易受攻击的 Ivanti 网关设备攻击了 MITRE，打破了其 15 年无事故的记录。在这方面，MITRE 并不孤单，因为数千个 Ivanti VPN 实例因两个未修补的零日漏洞而遭到入侵。

8 月，Ivanti 的 Virtual Traffic Manager （vTM） 隐藏了一个严重漏洞，该漏洞可能导致绕过身份验证，并在没有企业提供的补丁的情况下创建管理员用户。

“这些已知但未修补的漏洞已成为攻击者最喜欢的目标，因为它们很容易被利用，而且组织通常不知道带有 EOL 系统的设备仍在他们的网络中运行，”Sevco Security 的联合创始人 Greg Fitzgerald 在给 Dark Reading 的电子邮件声明中说。

## 在持续的风暴中提供保护

为了缓解这种威胁，Ivanti 建议其客户将 Ivanti CSA 4.6 升级到 CSA 5.0。他们还可以将 CSA 4.6 补丁 518 更新到补丁 519;但是，此产品已进入生命周期结束，因此建议升级到 CSA 5.0。

除此之外，Ivanti 建议所有客户确保双宿主 CSA 配置，并将 eth0 作为内部网络。

如果客户担心管理员可能已泄露，则应查看 CSA 中是否有已修改的或新添加的管理员。如果用户安装了终端节点检测和响应 （EDR），则建议同时查看这些警报。

用户可以通过 Ivanti 的成功门户记录案例或请求呼叫来请求帮助或提出问题。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/ivanti-cloud-service-appliance-attacked-vuln)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300339](/post/id/300339)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cyberattacks-data-breaches/ivanti-cloud-service-appliance-attacked-vuln)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/ivanti-cloud-service-appliance-attacked-vuln>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [再添数字政府新名片！深圳“深治慧”平台入选2025数博会创新案例](/post/id/311777)

  2025-09-02 15:37:49
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/310525)

  2025-07-24 10:24:57
* ##### [ISC.AI 2025国际人工智能发展高峰论坛：凝聚全球共识，点亮AI未来](/post/id/310510)

  2025-07-24 09:47:17
* ##### [ISC.AI大咖来了——国家网络安全守卫者 周鸿祎](/post/id/310504)

  2025-07-24 09:43:28
* ##### [攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）](/post/id/310339)

  2025-07-21 17:41:39
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/309947)

  2025-07-11 16:10:36
* ##### [报名开启！ISC.AI训练营助力AI与数字安全人才培养](/post/id/309827)

  2025-07-10 17:42:56

### 热门推荐

文章目录

* [不是第一个，也可能不是最后一个](#h2-0)
* [在持续的风暴中提供保护](#h2-1)

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