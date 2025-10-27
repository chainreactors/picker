---
title: Sonos智能音箱存在允许窃听用户的漏洞
url: https://www.anquanke.com/post/id/299041
source: 安全客-有思想的安全新媒体
date: 2024-08-13
fetch_date: 2025-10-06T18:00:30.096371
---

# Sonos智能音箱存在允许窃听用户的漏洞

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

# Sonos智能音箱存在允许窃听用户的漏洞

阅读量**39338**

发布时间 : 2024-08-12 14:20:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166823/hacking/sonos-smart-speakers-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

NCC Group 的研究人员在 Sonos 智能扬声器中发现了多个漏洞，包括一个被追踪为 CVE-2023-50809 的漏洞，该漏洞可能允许窃听用户。

研究人员在 BLACK HAT USA 2024 会议上披露了这些漏洞。

漏洞CVE-2023-50809可被攻击者利用，该漏洞位于目标Sonos智能音箱的Wi-Fi范围内，实现远程代码执行并接管设备。

该缺陷存在于设备的无线驱动程序中，该驱动程序在协商 WPA2 四次握手时无法正确验证信息元素。

成功利用此缺陷可让攻击者录制音频并将其泄露到攻击者的服务器。

*“受影响的设备无线驱动程序中存在一个漏洞，该漏洞在协商 WPA2 四次握手时未正确验证信息元素。”“低权限、近距离攻击者可利用此漏洞远程执行任意代码。”*

![Sonos智能音箱]()

该供应商在发布 Sonos S2 版本 15.9 时解决了该漏洞，并通知客户没有可用的解决方法。

为 Sonos 扬声器生产 Wi-Fi SoC 的联发科于 2024 年 3 月发布了安全公告 （CVE-2024-20018）。

NCC Group 还发布了一份白皮书，详细介绍了其专家用于在 Sonos Era-100 和 Sonos One 设备上实现任意代码执行的逆向工程过程和利用技术。

*“然后，这篇论文分为两个主要部分，第一部分涉及内存损坏漏洞，该漏洞是在Sonos One的无线驱动程序的WPA2握手过程中发现的。驱动程序本身是 MediaTek 的第三方芯片组，MediaTek 现在拥有与 2024 年 3 月安全公告 （CVE-2024-20018） 相关的补丁。在本节中，我们将讨论漏洞本身和利用该问题所需的步骤，以及用于实现代码执行的技术的详细列表（例如深入的面向返回的编程有效载荷）。NCC集团表示。*

*“在此之后，我们描述了在设备上获得完整外壳的后开发过程，并描述了我们开发的一种新型植入物，用于从设备的麦克风捕获音频。白皮书的另一个主要部分专门介绍Sonos Era-100设备。NCC Group 之前在设备上的安全启动过程中发现了弱点。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166823/hacking/sonos-smart-speakers-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299041](/post/id/299041)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166823/hacking/sonos-smart-speakers-flaw.html)

如若转载,请注明出处： <https://securityaffairs.com/166823/hacking/sonos-smart-speakers-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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