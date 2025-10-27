---
title: 恶意广告活动针对Lowe's员工构建钓鱼陷阱
url: https://www.anquanke.com/post/id/299874
source: 安全客-有思想的安全新媒体
date: 2024-09-07
fetch_date: 2025-10-06T18:22:27.726487
---

# 恶意广告活动针对Lowe's员工构建钓鱼陷阱

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

# 恶意广告活动针对Lowe's员工构建钓鱼陷阱

阅读量**114199**

发布时间 : 2024-09-06 11:15:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Nate Nelson，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/malvertising-campaign-phish-lowes-employees>

译文仅供参考，具体内容表达以及含义原文为准。

Lowe’s 员工通过赞助 Google 广告被网络钓鱼以获取他们的证书。

上个月中旬，Malwarebytes 的高级研究总监 Jérôme Segura 发现了一小群恶意网站，这些网站模仿 MyLowesLife，MyLowesLife 是一家市值超过 100 亿美元的公司的员工门户，用于日程安排、工资单等所有内容。拼写错误域名模仿了真实 MyLowesLife 的确切结构，并在 Google 搜索中得到了积极的赞助。在一个案例中，当研究人员搜索“myloweslife”时，排名前三的结果是与恶意活动相关的搜索广告。

关注这些链接的 Lowe’s 员工几乎没有理由对他们的发现持怀疑态度。最终的登录页面模仿了真实的 Lowe’s 员工门户，其中包含供用户提交销售（帐户）编号和密码的字段。然后，那些点击“登录”的人会被要求回答他们的“回答您[原文如此]安全问题”。然后，所有三项数据都将被转发到攻击者控制的网络钓鱼工具包。

“被盗的凭据使威胁行为者能够访问可用于身份盗窃的非常有价值的信息，”Segura 警告说。“受影响的 Lowe’s 员工可能会被骗并遭受金钱损失。在一次成功的运行中，数十个员工账户可能会转化为与其福利或银行详细信息相关的盗窃。

值得注意的是，这些山寨网站的主要主页 — myloveslife[.]网，mylifelowes[.]org， mylifelowes[.]net 和 myliveloves[.]net — 由完全通用的、显然是 AI 生成的零售网站模板填充，与 Lowe’s 没有任何关系。正如 Segura 解释的那样，这完全是战略性的。除了为威胁行为者节省时间和精力外，拥有一个无害的主页可能会让调查人员望而却步，并使与域名注册商一起关闭这些网站的理由更加困难。

## 为什么恶意广告有效

通过快速搜索通常更快、更容易地到达您正在寻找的网站，而不是在浏览器中输入完整的域。

主流搜索引擎中还内置了一个信任因素，其算法旨在将安全、可靠的结果推向任何给定搜索的顶部。赞助结果不会凭价值赢得他们的房地产，但随意的互联网冲浪者可能会不假思索地给予他们相同程度的信任。

除其他原因外，这些原因有助于解释恶意广告作为窃取凭据和用恶意软件感染目标人群的手段的普遍流行，以及为什么即使是精通技术的互联网用户也成为最近活动的受害者。例如，仅在过去几个月内，Malwarebytes 就追踪了针对 IT 人员、Arc 浏览器的技术前沿早期采用者等的不同骗局。

涉及 Lowe’s 员工的案例是独一无二的，因为与 IT 工具和新浏览器不同，向公众宣传公司内部门户在逻辑上没有意义。从理论上讲，这应该使这些虚假广告更容易被发现，无论是对于网络冲浪者和搜索提供商。

“谷歌和其他搜索引擎可以通过监控’广告商’为其购买广告空间的福利门户、单点登录 （SSO） 页面等来防止此类网络钓鱼活动。事实上，我们使用相同的技术来搜寻和查找这些恶意广告，因此我相信它可以用来在账户有机会引诱受害者之前主动禁止它们，“Segura 认为。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/malvertising-campaign-phish-lowes-employees)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299874](/post/id/299874)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/malvertising-campaign-phish-lowes-employees)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/malvertising-campaign-phish-lowes-employees>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

### 热门推荐

文章目录

* [为什么恶意广告有效](#h2-0)

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