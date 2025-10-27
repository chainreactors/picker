---
title: 新型安卓恶意软件 “Ajina.Banker ”利用Telegram渠道传播钓鱼页面与窃取2FA信息
url: https://www.anquanke.com/post/id/300077
source: 安全客-有思想的安全新媒体
date: 2024-09-14
fetch_date: 2025-10-06T18:24:11.653817
---

# 新型安卓恶意软件 “Ajina.Banker ”利用Telegram渠道传播钓鱼页面与窃取2FA信息

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

# 新型安卓恶意软件 “Ajina.Banker ”利用Telegram渠道传播钓鱼页面与窃取2FA信息

阅读量**134268**

发布时间 : 2024-09-13 15:07:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/09/new-android-malware-ajinabanker-steals.html>

译文仅供参考，具体内容表达以及含义原文为准。

至少自 2024 年 11 月以来，中亚地区的银行客户已成为代号为 **Ajina.Banker** 的新型 Android 恶意软件的目标，其目标是收集财务信息和拦截双因素身份验证 （2FA） 消息。

总部位于新加坡的 Group-IB 于 2024 年 5 月发现了该威胁，该公司表示，该恶意软件是通过威胁行为者建立的 Telegram 频道网络传播的，该网络伪装成与银行、支付系统和政府服务或日常公用事业相关的合法应用程序。

“攻击者有一个受经济利益驱使的附属网络，传播针对普通用户的 Android 银行家恶意软件，”安全研究人员 Boris Martynyuk、Pavel Naumov 和 Anvar Anarkulov 说。

正在进行的活动的目标包括亚美尼亚、阿塞拜疆、冰岛、哈萨克斯坦、吉尔吉斯斯坦、巴基斯坦、俄罗斯、塔吉克斯坦、乌克兰和乌兹别克斯坦等国家。

有证据表明，基于 Telegram 的恶意软件分发过程的某些方面可能已经自动化以提高效率。众多的 Telegram 帐户旨在向不知情的目标提供包含链接（指向其他 Telegram 频道或外部来源）和 APK 文件的精心制作的消息。

使用指向托管恶意文件的 Telegram 频道的链接还有一个额外的好处，因为它绕过了许多社区聊天施加的安全措施和限制，从而允许帐户在触发自动审核时逃避禁令。

除了滥用用户对合法服务的信任以最大限度地提高感染率外，作案手法还涉及在本地 Telegram 聊天中共享恶意文件，将它们冒充为声称提供丰厚奖励和独家服务访问权限的赠品和促销活动。

“事实证明，使用主题消息和本地化推广策略在区域社区聊天中特别有效，”研究人员说。“通过根据当地居民的兴趣和需求定制他们的方法，Ajina 能够显著提高成功感染的可能性。”

还观察到威胁行为者使用多个帐户用多条消息轰炸 Telegram 频道，有时是同时进行的，这表明可能采用了某种自动分发工具的协调努力。

该恶意软件本身相当简单，因为一旦安装，它就会与远程服务器建立联系，并请求受害者授予其访问 SMS 消息、电话号码 API 和当前蜂窝网络信息等的权限。

Ajina.Banker 能够收集 SIM 卡信息、已安装的金融应用程序列表和 SMS 消息，然后将这些信息泄露到服务器。

新版本的恶意软件还被设计为提供网络钓鱼页面，以试图收集银行信息。此外，他们可以访问通话记录和联系人，以及滥用 Android 的辅助功能服务 API 来阻止卸载并授予自己额外的权限。

研究人员说：“雇用 Java 编码员，以赚取一些钱的提议创建了 Telegram 机器人，这也表明该工具正在积极开发过程中，并得到了附属员工网络的支持。

“对攻击者的文件名、样本分发方法和其他活动的分析表明，他们对他们活动的地区的文化熟悉。”

披露之际，Zimperium 发现了两个被跟踪为 SpyNote 和 Gigabud（属于 GoldFactory 家族的一部分，还包括 GoldDigger）之间的联系。

“具有真正相似结构的域（使用与子域相同的不寻常关键字）和目标用于传播 Gigabud 样本，也用于分发 SpyNote 样本，”该公司表示。“这种分布重叠表明，两个恶意软件系列的背后很可能是同一个威胁行为者，这表明这是一个协调良好且广泛的活动。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/09/new-android-malware-ajinabanker-steals.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300077](/post/id/300077)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/09/new-android-malware-ajinabanker-steals.html)

如若转载,请注明出处： <https://thehackernews.com/2024/09/new-android-malware-ajinabanker-steals.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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