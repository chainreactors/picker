---
title: SambaSpy RAT 在独特的恶意软件活动中以意大利用户为目标
url: https://www.anquanke.com/post/id/300259
source: 安全客-有思想的安全新媒体
date: 2024-09-21
fetch_date: 2025-10-06T18:24:58.391474
---

# SambaSpy RAT 在独特的恶意软件活动中以意大利用户为目标

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

# SambaSpy RAT 在独特的恶意软件活动中以意大利用户为目标

阅读量**134018**

发布时间 : 2024-09-20 14:29:31

**x**

##### 译文声明

本文是翻译文章，文章来源：securityonline

原文地址：<https://securityonline.info/sambaspy-rat-targets-italian-users-in-a-unique-malware-campaign/>

译文仅供参考，具体内容表达以及含义原文为准。

2024 年 5 月，卡巴斯基实验室发现了一个专门针对意大利用户的复杂恶意软件活动。该活动对于网络犯罪活动来说并不常见，它只针对意大利受害者，部署了一种名为 SambaSpy 的新远程访问木马 （RAT）。使该活动脱颖而出的是攻击者确保其恶意软件仅感染意大利语用户的精确性，正如卡巴斯基的最新报告所详述的那样。

虽然许多恶意软件活动针对广泛的地理区域，但该活动专门设计用于仅感染意大利用户。在感染链的多个阶段，实施了检查以验证系统语言是否设置为意大利语。如果目标不符合这些标准，恶意软件就会简单地停止执行，表现出高度的定制性。

SambaSpy 是通过一封似乎来自合法意大利房地产公司的恶意电子邮件发送的，该电子邮件以完美的意大利语编写。这些电子邮件通常包含一个查看发票的链接，将用户重定向到意大利企业使用的合法文档共享平台。然而，在这个看起来合法的外表下，攻击者嵌入了一个恶意链接，该链接指向 JAR 文件，这是 SambaSpy 感染的第一阶段。

![]()

SambaSpy 感染链 2 |图片来源： Kaspersky Labs

安装后，SambaSpy 将授予攻击者对受感染设备的几乎完全控制权。SambaSpy 用 Java 编写并使用 Zelix KlassMaster 保护程序进行混淆，配备了一系列功能，使其能够：

* 管理文件和进程
* 上传和下载文件
* 控制网络摄像头
* 记录击键和剪贴板活动
* 截取屏幕截图
* 从 Chrome、Edge 和 Brave 等流行浏览器中窃取凭据
* 执行远程桌面操作
* 启动远程 shell

该恶意软件的功能扩展到在运行时加载其他插件，根据受害者的环境进一步扩大其攻击范围。

卡巴斯基在此次活动中发现了两条感染链，均以电子邮件开头。在更复杂的案例中，受害者会收到一封来自德国地址但用意大利语写的电子邮件，敦促他们查看发票。单击该链接后，受害者将被重定向到合法的意大利云发票服务 FattureInCloud 以显示实际发票。然而，在幕后，与意大利语检查匹配的受害者将被重定向到恶意 OneDrive 链接，从而导致 SambaSpy 投放器。

有趣的是，如果受害者的系统不符合特定标准（例如在语言设置为意大利语的情况下运行 Edge、Chrome 或 Firefox），他们将被留在合法网站上，从而避免感染。这种目标定位的精确度凸显了攻击者的专业知识。

尽管该活动只关注意大利受害者，但卡巴斯基发现了指向巴西的痕迹。在恶意软件和恶意域中发现了巴西葡萄牙语工件，例如代码注释和错误消息。该活动的基础设施还包含与其他地区（包括西班牙和巴西）的联系，这表明攻击者可能在意大利之外有更广泛的野心。

本文翻译自securityonline [原文链接](https://securityonline.info/sambaspy-rat-targets-italian-users-in-a-unique-malware-campaign/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300259](/post/id/300259)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sambaspy-rat-targets-italian-users-in-a-unique-malware-campaign/)

如若转载,请注明出处： <https://securityonline.info/sambaspy-rat-targets-italian-users-in-a-unique-malware-campaign/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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