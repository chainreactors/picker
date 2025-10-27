---
title: RansomHub 集团在最新网络攻击中部署了新的 EDR 杀毒工具
url: https://www.anquanke.com/post/id/299202
source: 安全客-有思想的安全新媒体
date: 2024-08-17
fetch_date: 2025-10-06T18:02:13.573658
---

# RansomHub 集团在最新网络攻击中部署了新的 EDR 杀毒工具

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

# RansomHub 集团在最新网络攻击中部署了新的 EDR 杀毒工具

阅读量**59020**

发布时间 : 2024-08-16 14:45:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html>

译文仅供参考，具体内容表达以及含义原文为准。

已经观察到一个与 RansomHub 勒索软件有链接的网络犯罪集团使用一种新工具，该工具旨在终止受感染主机上的端点检测和响应 （EDR） 软件，加入 AuKill（又名 AvNeutralizer）和 Terminator 等其他类似程序的行列。

网络安全公司 Sophos 将 EDR 杀死工具称为 EDRKillShifter，该公司在 2024 年 5 月的一次失败的勒索软件攻击中发现了该工具。

安全研究员Andreas Klopsch说：“EDRKillShifter工具是一个’加载器’可执行文件–一种容易被滥用的合法驱动程序的交付机制（也称为’自带易受攻击的驱动程序’或BYOVD工具）。“根据威胁参与者的要求，它可以提供各种不同的驱动程序有效载荷。”

RansomHub 疑似是 Knight 勒索软件的更名，于 2024 年 2 月浮出水面，利用已知的安全漏洞获得初始访问权限并丢弃 Atera 和 Splashtop 等合法远程桌面软件以进行持续访问。

上个月，Microsoft 透露，臭名昭著的电子犯罪集团 Scattered Spider 已将 RansomHub 和 Qilin 等勒索软件菌株纳入其武器库。

通过命令行和密码字符串输入执行，可执行文件解密名为 BIN 的嵌入式资源并在内存中执行它。BIN 资源解压缩并运行基于 Go 的最终混淆有效负载，然后利用不同的易受攻击的合法驱动程序来获得提升的权限并撤防 EDR 软件。

“二进制文件的语言属性是俄语，表明恶意软件作者在具有俄语本地化设置的计算机上编译了可执行文件，”Klopsch说。“所有解压缩的 EDR 杀手都在 .data 部分嵌入了一个易受攻击的驱动程序。”

为了缓解威胁，建议使系统保持最新状态，在 EDR 软件中启用篡改保护，并对 Windows 安全角色采取严格的卫生措施。

“只有当攻击者升级他们控制的权限，或者他们能够获得管理员权限时，这种攻击才有可能，”Klopsch说。“用户和管理员权限之间的分离有助于防止攻击者轻松加载驱动程序。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299202](/post/id/299202)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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