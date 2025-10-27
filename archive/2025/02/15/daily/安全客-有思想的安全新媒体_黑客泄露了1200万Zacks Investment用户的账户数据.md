---
title: 黑客泄露了1200万Zacks Investment用户的账户数据
url: https://www.anquanke.com/post/id/304347
source: 安全客-有思想的安全新媒体
date: 2025-02-15
fetch_date: 2025-10-06T20:32:56.740229
---

# 黑客泄露了1200万Zacks Investment用户的账户数据

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

# 黑客泄露了1200万Zacks Investment用户的账户数据

阅读量**103185**

发布时间 : 2025-02-14 17:04:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/hacker-leaks-account-data-of-12-million-zacks-investment-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![Hacker leaks account data of 12 million Zacks Investment users]()

据报道，扎克斯投资研究公司（Zacks Investment Research，简称 Zacks）去年再次遭遇数据泄露事件，约 1200 万个账户的相关敏感信息被泄露。

扎克斯是一家美国投资研究公司，它通过一款名为 “扎克斯评级（Zacks Rank）” 的专有股票表现评估工具，为客户提供基于数据的洞察分析，以帮助客户做出明智的财务决策。

今年 1 月下旬，一名威胁行为者在一个黑客论坛上发布了数据样本，声称在 2024 年 6 月对扎克斯公司发动了攻击，导致数百万客户的数据被泄露。

这些发布的数据可供论坛成员获取，只需支付少量加密货币即可。数据内容包括全名、用户名、电子邮件地址、实际地址和电话号码。

![Threat actor's post on BreachForums]()

威胁行为者在 “数据泄露论坛（BreachForums）” 上的帖子
来源：BleepingComputer）

BleepingComputer多次联系扎克斯公司，询问这些数据的真实性，但尚未收到回复。

然而，该威胁行为者告诉 BleepingComputer，他们以域管理员的身份访问了该公司的活动目录，然后窃取了主网站（[Zacks.com](https://zacks.com/)）以及包括一些内部网站在内的其他 16 个网站的源代码。他们还分享了所窃取的源代码样本，以此作为这次新的数据泄露事件的证据。

今天早些时候，被泄露的扎克斯公司数据库被添加到了 “我是否已遭泄露（Have I Been Pwned，简称 HIBP）” 网站上，用户可以在该网站上查询自己的个人数据是否已被泄露。

HIBP 证实，该文件包含 1200 万个唯一的电子邮件地址，以及 IP 地址、姓名、未加盐的 SHA-256 哈希形式的密码、电话号码、实际地址和用户名。

不过，该服务也指出，大约 93% 的被泄露电子邮件地址已经存在于其数据库中，这些地址此前在该平台或其他服务的数据泄露事件中已被泄露过。

**尚无官方确认**

扎克斯公司尚未确认这起所谓的数据泄露事件，但如果事实证明这次数据泄露是一次新的黑客攻击导致的，那么这可能是该公司在过去四年里遭遇的第三起重大数据泄露事件。

2023 年 1 月，扎克斯公司披露，黑客在 2021 年 11 月至 2022 年 8 月期间侵入了其网络，并获取了 82 万名客户的敏感信息。

几个月后的 2023 年 6 月，HIBP 验证了另一个源自扎克斯公司的数据库，该数据库此前已被泄露。

该数据库包含了 880 万名使用扎克斯公司服务的用户的电子邮件地址、用户名、未加盐的 SHA256 密码、地址、电话号码和全名。

据 HIBP 服务的创建者特洛伊・亨特（Troy Hunt）称，这些数据似乎是在 2020 年 5 月被泄露的，这表明它是一起更早发生的事件的结果。

扎克斯公司客户数据的这次最新泄露事件，虽然尚未得到官方证实，但在被添加到 HIBP 服务之前已经过该平台的验证，而且有很大把握认为这些数据来自一起新的事件。

需要注意的是，也存在一种可能性，即威胁行为者从其他服务中抓取信息，并汇编成了一个包含与扎克斯公司相关用户信息的数据库。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/hacker-leaks-account-data-of-12-million-zacks-investment-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304347](/post/id/304347)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/hacker-leaks-account-data-of-12-million-zacks-investment-users/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/hacker-leaks-account-data-of-12-million-zacks-investment-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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