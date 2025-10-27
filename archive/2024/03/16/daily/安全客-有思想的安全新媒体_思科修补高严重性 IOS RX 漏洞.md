---
title: 思科修补高严重性 IOS RX 漏洞
url: https://www.anquanke.com/post/id/293995
source: 安全客-有思想的安全新媒体
date: 2024-03-16
fetch_date: 2025-10-04T12:08:47.632597
---

# 思科修补高严重性 IOS RX 漏洞

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

# 思科修补高严重性 IOS RX 漏洞

阅读量**126777**

发布时间 : 2024-03-15 11:11:18

**x**

##### 译文声明

本文是翻译文章，文章来源：https://www.securityweek.com/cisco-patches-high-severity-ios-rx-vulnerabilities/

译文仅供参考，具体内容表达以及含义原文为准。

思科发布了针对 IOS RX 软件中多个漏洞的补丁，其中包括三个导致拒绝服务 (DoS) 和特权提升的高严重性缺陷。

最严重的高严重性错误是 CVE-2024-20320，这是 IOS RX 的 SSH 功能中的一个问题，攻击者可以通过向 CLI 发送精心设计的 SSH 命令来将权限提升到 root。

该安全漏洞影响了 8000 系列路由器以及网络融合系统 (NCS) 540 系列和 5700 系列路由器，随着 IOS RX 版本 7.10.2 的发布，该安全漏洞已得到修补。运行旧版本操作系统的设备应升级到已修补的版本。

第二个高严重性缺陷（编号为 CVE-2024-20318）会影响启用了第 2 层服务功能的线卡。攻击者可以通过易受攻击的设备发送特定的以太网帧，导致线卡网络处理器重置，并且可以重复该过程来重置线卡，从而导致 DoS 情况。

该漏洞已在 IOS RX 软件版本 7.9.2 和 7.10.1 中得到解决。思科还发布了软件维护升级（SMU）来解决该错误。

这家科技巨头还修补了 CVE-2024-20327，这是一个影响 ASR 9000 系列路由器的以太网 PPP (PPPoE) 终止功能的高严重性 DoS 错误。对格式错误的 PPPoE 数据包处理不当会导致攻击者导致 ppp\_ma 进程崩溃，从而导致 PPPoE 流量出现 DoS 状况。

思科表示，该问题影响路由器“在基于 Lightspeed 或 Lightspeed-Plus 的线卡上运行带有 PPPoE 终端的宽带网络网关 (BNG) 功能”。IOS RX 软件版本 7.9.21、7.10.1 和 7.11.1 包含针对此缺陷的补丁。

思科还宣布修复了 IOS XR 软件中的几个中等严重程度的漏洞，这些漏洞可能允许攻击者绕过保护、导致 DoS 情况或安装未经验证的软件映像。

这些缺陷已作为思科 2024 年 3 月半年度 IOS RX安全建议包的一部分得到解决，其中包括八项建议。

这家科技巨头没有提及任何这些漏洞正在被利用。

本文翻译自https://www.securityweek.com/cisco-patches-high-severity-ios-rx-vulnerabilities/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293995](/post/id/293995)

安全KER - 有思想的安全新媒体

本文转载自: https://www.securityweek.com/cisco-patches-high-severity-ios-rx-vulnerabilities/

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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