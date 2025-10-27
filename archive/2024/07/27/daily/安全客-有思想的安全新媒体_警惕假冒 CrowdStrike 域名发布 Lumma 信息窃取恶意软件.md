---
title: 警惕假冒 CrowdStrike 域名发布 Lumma 信息窃取恶意软件
url: https://www.anquanke.com/post/id/298453
source: 安全客-有思想的安全新媒体
date: 2024-07-27
fetch_date: 2025-10-06T17:41:19.983739
---

# 警惕假冒 CrowdStrike 域名发布 Lumma 信息窃取恶意软件

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

# 警惕假冒 CrowdStrike 域名发布 Lumma 信息窃取恶意软件

阅读量**157566**

发布时间 : 2024-07-26 11:25:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源：The Register

原文地址：<https://www.theregister.com/2024/07/25/crowdstrike_lumma_infostealer/>

译文仅供参考，具体内容表达以及含义原文为准。

据安全商店的威胁情报团队称，CrowdStrike 是用于诱骗 Windows 用户下载和运行臭名昭著的 Lumma 信息窃取恶意软件的最新诱饵，该团队在 Falcon 传感器更新惨败几天后发现了该骗局。

像 Lumma 这样的信息窃取者会搜索受感染的机器以查找任何存储的敏感信息，例如站点登录详细信息和浏览器历史记录。然后，这些数据被悄悄地泄露给恶意软件的运营商，用于欺诈、盗窃和其他犯罪。

更具体地说，这些被盗信息用于非法访问受害者的在线银行账户和加密货币钱包，以及电子邮件收件箱、远程桌面账户以及其他需要合法登录凭据的应用程序和服务，这使得这种类型的恶意软件在网络骗子中特别受欢迎。

Lumma 是一种相对流行的窃取器，自 2022 年以来在勒索软件团队中的需求量很大。Mandiant表示，这也是犯罪团伙UNC5537用来获取凭据的信息窃取者之一，然后这些凭据随后被用于在今年春天早些时候闯入Snowflake云存储环境。

在 CrowdStrike 活动中，Lumma 构建时间戳“表明演员极有可能在确定 CrowdStrike 的 Falcon 传感器的单一内容更新后的第二天构建了用于分发的样本，”安全商店指出。

域名，crowdstrike-office365[.]com 于 7 月 23 日注册，就在 CrowdStrike 7 月 19 日的错误更新导致 850 万台 Windows 机器崩溃的几天后。据推测，该域名背后的组织与 6 月份早些时候的社会工程攻击有关，该攻击还分发了 Lumma 恶意软件。

在这些早期的信息窃取活动中，不法分子向网络钓鱼电子邮件发送垃圾邮件，然后跟进声称来自 Microsoft Teams 服务台员工的电话。

CrowdStrike 团队报告说：“基于活动之间的共享基础设施和企业网络的明显目标，CrowdStrike Intelligence 以适度的信心评估该活动可能归因于同一未具名的威胁行为者。

虚假的 CrowdStrike 域试图诱骗用户点击并获取一个.zip文件，声称这是一个恢复工具，用于修复由错误的传感器更新引起的启动循环。该存档包含一个 Microsoft 安装程序文件 WidowsSystem-update[.]MSI，它实际上是一个恶意软件加载器。

加载器被标记执行后，它会丢弃并运行自解压 RAR 文件 plenrco[.]exe，具有一个名为 SymposiumTaiwan[.] 的 Nullsoft 可编程安装系统 （NSIS） 安装程序。exe文件。该文件包含合法 AutoIt 可执行文件的一些代码片段，该可执行文件经过严重混淆，如果受害者的计算机正在运行防病毒软件，则该可执行文件将终止。

但是，假设海岸是清晰的，并且恶意软件可以在未被发现的情况下继续存在，则AutoIt加载程序会运行两个shellcode之一，具体取决于它是32位还是64位系统，并最终部署Lumma恶意软件。

就在 CrowdStrike 狡猾的传感器更新使 Windows 机器陷入蓝屏漩涡几个小时后，有报道称诈骗电子邮件利用停电作为诱饵，并声称来自 CrowdStrike 支持或 CrowdStrike Security。该安全公司声称，97%的受影响系统现在已重新上线。

本文翻译自The Register [原文链接](https://www.theregister.com/2024/07/25/crowdstrike_lumma_infostealer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298453](/post/id/298453)

安全KER - 有思想的安全新媒体

本文转载自: [The Register](https://www.theregister.com/2024/07/25/crowdstrike_lumma_infostealer/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/25/crowdstrike_lumma_infostealer/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
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