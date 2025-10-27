---
title: SnakeKeylogger潜入Windows 收件箱以窃取敏感机密
url: https://www.anquanke.com/post/id/298826
source: 安全客-有思想的安全新媒体
date: 2024-08-07
fetch_date: 2025-10-06T18:02:15.561233
---

# SnakeKeylogger潜入Windows 收件箱以窃取敏感机密

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

# SnakeKeylogger潜入Windows 收件箱以窃取敏感机密

阅读量**78498**

发布时间 : 2024-08-06 11:33:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Jessica Lyons，文章来源： theregister

原文地址：<https://www.theregister.com/2024/08/05/snakekeylogger_malware_windows/>

译文仅供参考，具体内容表达以及含义原文为准。

犯罪分子再次掠夺 Windows 用户，这一次是为了用键盘记录器打击他们，该键盘记录器还可以窃取凭据并截取屏幕截图。

在本月的警报中，Fortinet 的 FortiGuard Labs 警告说，SnakeKeylogger 感染率有所上升。一旦在某人的 PC 上运行，这种恶意软件就会在受害者登录时记录他们的击键，从他们的文件中获取用户名和密码，并截取屏幕截图以窥探人们，然后将所有这些敏感信息发送给欺诈者。

“根据 FortiGuard 遥测数据，有数百次零日检测命中，”威胁情报组织表示，并补充说，发现记录器多次联系外部服务器。

在这种情况下，Fortinet 所说的零日检测是指行为可疑的软件，尽管尚未在其已知软件的数据库中，这表明其防病毒软件遇到的 SnakeKeylogger 是一种新菌株，就 Fortinet 而言。7 月 31 日，FortiGuard 的检测引擎中添加了用于检测恶意软件的签名，版本为 92.06230。

SnakeKeylogger，又名 KrakenKeylogger，是 Microsoft .基于NET的窃取程序，已经以凭据盗窃和键盘记录功能而闻名。它最初是在俄罗斯犯罪论坛上以订阅方式出售的。

根据 Splunk 的威胁研究团队的说法，该恶意软件于 2020 年 11 月成为“重大威胁”，它以狡猾地从受害者设备中泄露数据而闻名。它使用FTP来传输人们的私人文件，并使用SMTP来发送包含敏感数据的电子邮件，并与消息应用程序Telegram集成，使骗子可以实时接收被盗信息。

“此外，它在收集剪贴板数据、浏览器凭据以及进行系统和网络侦察方面表现出熟练程度，”Splunk 的安全研究人员指出。

此外，该团队补充说，该恶意软件“通过利用各种加密器或加载器来混淆其代码并逃避沙箱的检测，表现出显着的复杂性”。虽然 Fortinet 警报没有具体说明犯罪分子如何闯入机器以部署 SnakeKeylogger，但这种窃取程序通常通过网络钓鱼活动传播。我们已经询问了有关这些攻击的更多详细信息，如果我们收到 Fortinet 的回复，我们将更新这个故事。

在关于SnakeKeylogger用于劫持受害者的在线帐户，使用他们被盗的信条的另一份警报中，Check Point表示，恶意代码通常隐藏在恶意制作的Office文档或附加到电子邮件的PDF中，一旦收件人打开该文档，有效载荷就会找到一种方法来获取和运行记录器。

“嵌入在文档中的恶意软件通常是下载器，”安全商店解释说。“它使用 PowerShell 脚本将 Snake Keylogger 的副本下载到受感染的系统并执行它。”

在最近的感染潮中可能也是如此。在网络防御者为保护其组织免受键盘记录器攻击而采取的其他步骤中，FortiGuard Labs 建议：“打开电子邮件、点击链接和下载附件时要小心。

此外，该组织还提供其他提醒，适用于防止各种恶意软件投放攻击。

其中包括使用最新版本的数据库和引擎使安全服务保持最新状态。此外，在本地和网络策略中启用防病毒和沙盒功能，并使用端点安全产品在攻击前和攻击后保护用户。

本文翻译自 theregister [原文链接](https://www.theregister.com/2024/08/05/snakekeylogger_malware_windows/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298826](/post/id/298826)

安全KER - 有思想的安全新媒体

本文转载自:  [theregister](https://www.theregister.com/2024/08/05/snakekeylogger_malware_windows/)

如若转载,请注明出处： <https://www.theregister.com/2024/08/05/snakekeylogger_malware_windows/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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