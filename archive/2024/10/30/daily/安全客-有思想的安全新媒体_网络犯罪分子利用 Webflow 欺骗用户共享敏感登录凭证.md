---
title: 网络犯罪分子利用 Webflow 欺骗用户共享敏感登录凭证
url: https://www.anquanke.com/post/id/301360
source: 安全客-有思想的安全新媒体
date: 2024-10-30
fetch_date: 2025-10-06T18:46:47.026176
---

# 网络犯罪分子利用 Webflow 欺骗用户共享敏感登录凭证

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

# 网络犯罪分子利用 Webflow 欺骗用户共享敏感登录凭证

阅读量**60802**

发布时间 : 2024-10-29 11:12:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员警告说，随着威胁行为者继续滥用 Cloudflare 和 Microsoft Sway 等合法服务，使用名为 Webflow 的建站工具创建的钓鱼网页数量激增。

Netskope威胁实验室研究员扬-迈克尔-阿尔坎塔拉（Jan Michael Alcantara）在一份分析报告中说：“这些活动的目标是来自不同加密钱包的敏感信息，包括Coinbase、MetaMask、Phantom、Trezor和Bitbuy，以及多个公司网络邮件平台的登录凭证和微软365的登录凭证。”

这家网络安全公司称，它追踪到，2024 年 4 月至 9 月间，使用 Webflow 制作的钓鱼网页流量增加了 10 倍，攻击目标遍布全球 120 多个组织。其中大部分攻击目标位于北美和亚洲，涉及金融服务、银行和技术领域。

据观察，攻击者利用 Webflow 创建独立的网络钓鱼网页，并将毫无戒心的用户重定向到他们控制的其他网络钓鱼网页。

Michael Alcantara 说：“前者为攻击者提供了隐蔽性和便利性，因为没有钓鱼代码行需要编写和检测，而后者则为攻击者提供了灵活性，可以根据需要执行更复杂的操作。”

Webflow 比 Cloudflare R2 或 Microsoft Sway 更吸引人的地方在于，它允许用户免费创建自定义子域，而不是容易引起怀疑的自动生成随机字母数字子域。

* Cloudflare R2 – https://pub-<32\_alphanumeric\_string>.r2.dev/webpage.htm
* Microsoft Sway – https://sway.cloud.microsoft/{16\_alphanumeric\_string}?ref={sharing\_option}

为了增加攻击成功的可能性，钓鱼网页被设计成模仿合法对应网页的登录页面，以欺骗用户提供他们的凭据，然后在某些情况下，这些凭据会被外泄到不同的服务器上。

Netskope 表示，它还发现了一些 Webflow 加密诈骗网站，这些网站使用合法钱包主页的截图作为自己的登陆页面，访问者点击假网站上的任何地方后都会重定向到实际的诈骗网站。

加密网络钓鱼活动的最终目的是窃取受害者的种子短语，使攻击者能够劫持加密货币钱包的控制权并盗取资金。

在网络安全公司确定的攻击中，最终提供恢复短语的用户会看到一条错误信息，称其账户因 “未经授权的活动和身份验证失败 ”而被暂停。该信息还提示用户通过在 tawk.to 上发起在线聊天来联系他们的支持团队。

值得注意的是，LiveChat、Tawk.to 和 Smartsupp 等聊天服务已被滥用，成为 Avast 称为 CryptoCore 的加密货币诈骗活动的一部分。

迈克尔-阿尔坎塔拉说：“用户在访问银行门户网站或网络邮件等重要页面时，应始终在网络浏览器中直接输入网址，而不是使用搜索引擎或点击任何其他链接。”

就在网络犯罪分子在暗网上大肆宣传新型反僵尸服务的同时，这项服务声称可以绕过谷歌 Chrome 浏览器上的安全浏览警告。

SlashNext在最近的一份报告中说：“反僵尸服务，如Otus Anti-Bot、Remove Red和Limitless Anti-Bot，已经成为复杂网络钓鱼行动的基石。“这些服务旨在防止安全爬虫识别网络钓鱼网页并将其屏蔽。”

“这些工具通过过滤网络安全机器人和伪装网络钓鱼网页，延长了恶意网站的生命周期，帮助犯罪分子更长时间地逃避检测。”

还发现正在进行的恶意垃圾邮件和恶意广告活动在传播一种名为 WARMCOOKIE（又名 BadSpace）的不断演变的恶意软件，该恶意软件随后成为 CSharp-Streamer-RAT 和 Cobalt Strike 等恶意软件的传播渠道。

“WarmCookie 为对手提供了各种有用的功能，包括有效载荷部署、文件操作、命令执行、屏幕截图收集和持久性，这使得它在获得初始访问权限后就能在系统中使用，以方便在被入侵的网络环境中进行长期、持久的访问，”Cisco Talos 说。

对源代码的分析表明，该恶意软件很可能是由与Resident相同的威胁参与者开发的，Resident是一种入侵后植入程序，与Rhadamanthys信息窃取程序一起部署在被称为TA866（又名Asylum Ambuscade）的入侵程序集中。这些活动主要针对制造业，紧随其后的是政府和金融服务业。

“Talos说：”虽然与传播活动相关的长期目标似乎是不加区分的，但观察到后续有效载荷的大多数案例都发生在美国，其他案例遍布加拿大、英国、德国、意大利、奥地利和荷兰。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301360](/post/id/301360)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/cybercriminals-use-webflow-to-deceive.html>

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

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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