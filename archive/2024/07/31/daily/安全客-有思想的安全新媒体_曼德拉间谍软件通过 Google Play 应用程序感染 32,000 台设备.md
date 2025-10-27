---
title: 曼德拉间谍软件通过 Google Play 应用程序感染 32,000 台设备
url: https://www.anquanke.com/post/id/298592
source: 安全客-有思想的安全新媒体
date: 2024-07-31
fetch_date: 2025-10-06T17:41:49.352575
---

# 曼德拉间谍软件通过 Google Play 应用程序感染 32,000 台设备

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

# 曼德拉间谍软件通过 Google Play 应用程序感染 32,000 台设备

阅读量**77102**

发布时间 : 2024-07-30 14:28:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Alessandro Mascellino，文章来源：infosecurity

原文地址：<https://www.infosecurity-magazine.com/news/mandrake-spyware-infects-32000/>

译文仅供参考，具体内容表达以及含义原文为准。

安全研究人员揭示了 Mandrake 的全新迭代，Mandrake 是一种复杂的 Android 网络间谍恶意软件工具。Bitdefender 于 2020 年 5 月初步分析，曼德拉草至少在四年内未被发现。

2024 年 4 月，卡巴斯基研究人员发现了可疑样本，这些样本被确认为 Mandrake 的新版本。从 2022 年到 2024 年，这种最新变种隐藏在 Google Play 上的五个应用程序中，积累了超过 32,000 次下载，同时没有被其他网络安全供应商发现。

卡巴斯基今天发布的公告中描述了更新的曼德拉草样本，显示了增强的混淆和规避策略。主要更改包括将恶意函数移动到经过混淆的本机库，使用证书固定与命令和控制 （C2） 服务器进行安全通信，以及实施各种测试以避免在已取得 root 权限或模拟的设备上进行检测。

据报道，这些应用程序在 Google Play 上保留了长达两年的时间，下载次数最多的应用程序 AirFS 在 2024 年 3 月下架之前累计安装了超过 30,000 次。

## 复杂的感染链

从技术角度来看，新的曼德拉草版本通过多阶段感染链运行。最初，恶意活动隐藏在原生库中，与之前的第一阶段在 DEX 文件中的活动相比，它更难分析。

执行时，第一阶段库解密并加载第二阶段，然后启动与 C2 服务器的通信。如果认为相关，C2 服务器会命令设备下载并执行核心恶意软件，该恶意软件旨在窃取用户凭据并部署其他恶意应用程序。

卡巴斯基警告说，曼德拉草的规避技术已经变得更加复杂，包括对仿真环境、根设备和分析师工具的检查。这些增强功能使网络安全专家难以检测和分析恶意软件。

值得注意的是，Mandrake 背后的威胁行为者还采用了一种新颖的数据加密和解密方法，混合使用自定义算法和标准 AES 加密。

“Mandrake 间谍软件正在动态发展，改进其隐藏、沙盒规避和绕过新防御机制的方法。在第一个活动的应用程序四年未被发现之后，当前的活动在阴影中潜伏了两年，但仍然可以在Google Play上下载，“卡巴斯基解释说。

“这凸显了威胁行为者的强大技能，而且在应用程序发布到市场之前对应用程序进行更严格的控制只会转化为更复杂、更难检测的威胁潜入官方应用程序市场。”

本文翻译自infosecurity [原文链接](https://www.infosecurity-magazine.com/news/mandrake-spyware-infects-32000/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298592](/post/id/298592)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity](https://www.infosecurity-magazine.com/news/mandrake-spyware-infects-32000/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/mandrake-spyware-infects-32000/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [复杂的感染链](#h2-0)

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