---
title: 网络犯罪分子部署10万多个恶意软件Android应用程序来窃取OTC代码
url: https://www.anquanke.com/post/id/298674
source: 安全客-有思想的安全新媒体
date: 2024-08-02
fetch_date: 2025-10-06T18:01:02.550054
---

# 网络犯罪分子部署10万多个恶意软件Android应用程序来窃取OTC代码

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

# 网络犯罪分子部署10万多个恶意软件Android应用程序来窃取OTC代码

阅读量**79025**

发布时间 : 2024-08-01 14:22:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/cybercriminals-deploy-100k-malware.html>

译文仅供参考，具体内容表达以及含义原文为准。

至少自 2022 年 2 月以来，作为大规模活动的一部分，已经观察到一种新的恶意活动，利用恶意 Android 应用程序窃取用户的短信。

这些恶意应用程序涵盖超过 107,000 个独特样本，旨在拦截用于在线帐户验证的一次性密码 （OTP） 以实施身份欺诈。

“在这107,000个恶意软件样本中，超过99,000个应用程序是未知的，并且在通常可用的存储库中不可用，”移动安全公司Zimperium在与The Hacker News分享的一份报告中说。 “这种恶意软件正在监控全球600多个品牌的一次性密码消息，其中一些品牌的用户数量超过数亿用户。”

在113个国家发现了该运动的受害者，其中印度和俄罗斯位居榜首，其次是巴西、墨西哥、美国、乌克兰、西班牙和土耳其。

攻击的起点是安装恶意应用程序，受害者通过模仿 Google Play 商店应用列表的欺骗性广告或伪装成合法服务（例如 Microsoft Word）作为分发渠道的 2,600 个 Telegram 机器人中的任何一个被诱骗安装在他们的设备上。

安装后，该应用程序会请求访问传入 SMS 消息的权限，然后它会访问 13 个命令和控制 （C2） 服务器之一以传输被盗的 SMS 消息。

“恶意软件仍然隐藏着，不断监控新的传入短信，”研究人员说。“它的主要目标是用于在线帐户验证的OTP。”

目前尚不清楚谁是该行动的幕后黑手，尽管已经观察到威胁行为者接受包括加密货币在内的各种支付方式，以推动一项名为快速短信（fastsms[.]Su），允许客户购买对虚拟电话号码的访问权限。

很可能在所有者不知情的情况下，与受感染设备关联的电话号码被用于通过收集双因素身份验证 （2FA） 所需的 OTP 来注册各种在线帐户。

2022 年初，趋势科技揭示了一项类似的以财务为动机的服务，该服务将 Android 设备困在一个僵尸网络中，可用于“批量注册一次性账户或创建经过电话验证的账户以进行欺诈和其他犯罪活动”。

“这些被盗的凭证为进一步的欺诈活动提供了跳板，例如在热门服务上创建虚假账户以发起网络钓鱼活动或社会工程攻击，”Zimperium说。

调查结果凸显了恶意行为者继续滥用Telegram，这是一款流行的即时通讯应用程序，每月活跃用户超过9.5亿，用于从恶意软件传播到C2等不同目的。

本月早些时候，Positive Technologies 披露了两个名为 SMS Webpro 和 NotifySmsStealer 的短信窃取器系列，它们针对孟加拉国、印度和印度尼西亚的 Android 设备用户，旨在向威胁行为者维护的 Telegram 机器人窃取消息。

这家俄罗斯网络安全公司还发现了伪装成 TrueCaller 和 ICICI Bank 的窃取恶意软件，它们能够通过消息传递平台窃取用户的照片、设备信息和通知。

“感染链始于对WhatsApp的典型网络钓鱼攻击，”安全研究员Varvara Akhapkina说。“除了少数例外，攻击者使用冒充银行的网络钓鱼网站来吸引用户从他们那里下载应用程序。”

另一个利用 Telegram 作为 C2 服务器的恶意软件是 TgRAT，这是一种 Windows 远程访问木马，最近已更新为包含 Linux 变体。它配备了下载文件、截取屏幕截图和远程运行命令的功能。

“Telegram在许多公司被广泛用作企业信使，”Doctor Web说。“因此，威胁行为者可以将其用作传播恶意软件和窃取机密信息的载体也就不足为奇了：该程序的受欢迎程度和 Telegram 服务器的常规流量使得在受感染的网络上伪装恶意软件变得容易。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/cybercriminals-deploy-100k-malware.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298674](/post/id/298674)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/cybercriminals-deploy-100k-malware.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/cybercriminals-deploy-100k-malware.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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