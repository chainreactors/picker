---
title: Otelier 数据泄露事件暴露了数百万人的信息和酒店预订信息
url: https://www.anquanke.com/post/id/303627
source: 安全客-有思想的安全新媒体
date: 2025-01-21
fetch_date: 2025-10-06T20:08:09.908180
---

# Otelier 数据泄露事件暴露了数百万人的信息和酒店预订信息

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

# Otelier 数据泄露事件暴露了数百万人的信息和酒店预订信息

阅读量**113747**

发布时间 : 2025-01-20 10:29:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/>

译文仅供参考，具体内容表达以及含义原文为准。

![Otelier]()

酒店管理平台 Otelier 遭受数据泄露，因为威胁者入侵了其亚马逊 S3 云存储，窃取了数百万客人的个人信息以及万豪、希尔顿和凯悦等知名酒店品牌的预订信息。

据称，漏洞首次发生在 2024 年 7 月，一直持续到 10 月，威胁者声称从 Otelier 的亚马逊 AWS S3 存储桶中窃取了近 8 TB 的数据。

在给 BleepingComputer 的一份声明中，Otelier 证实了此次入侵事件，并表示正在与受影响的客户进行沟通。

Otelier 告诉 BleepingComputer：“我们的首要任务是保护我们的客户，同时加强系统的安全性，以防止未来出现问题。”

“Otelier一直在与信息可能受到影响的客户进行沟通。针对此次事件，我们聘请了一支由顶尖网络安全专家组成的团队，对我们的系统进行全面的取证分析和验证。”

“调查确定，未经授权的访问已经终止。为了防止今后发生类似事件，Otelier 关闭了涉案账户，并继续努力加强网络安全协议。”

Otelier 以前的名称是 MyDigitalOffice，是一个基于云的酒店管理解决方案，全球有 10,000 多家酒店使用它来管理预订、交易、夜间报告和发票。

包括万豪、希尔顿和凯悦在内的许多知名酒店品牌都在使用或曾经使用过该公司，被盗信息中就有这些品牌的数据。

**通过被盗凭证入侵**

Otelier 入侵事件的幕后威胁者告诉 BleepingComputer，他们最初是利用一名员工的登录账号入侵了该公司的 Atlassian 服务器。这些凭据是通过信息窃取恶意软件盗取的，而这种恶意软件在过去几年里已成为企业网络的祸根。

当 BleepingComputer 向 Otelier 公司求证这一消息时，该公司的一位代表表示，他们无法就这一事件发表任何进一步的评论。不过，BleepingComputer 在 Flare 威胁情报平台上发现，Otelier 的员工信息已被信息窃取恶意软件窃取。

威胁者称，他们利用这些凭证搜刮了票据和其他数据，其中包含该公司 S3 存储桶的进一步凭证。

黑客利用这些访问权限，声称从该公司的亚马逊云存储中下载了 7.8TB 的数据，其中包括由 Otelier 管理的 S3 存储桶中属于万豪的数百万份文件。这些文件包括酒店夜报、轮班审计和会计数据。

万豪已向 BleepingComputer 证实，Otelier 的网络攻击对他们造成了影响，并在 Otelier 完成调查期间暂停了自动服务。该公司强调，在这次攻击中，公司没有任何系统被攻破。

万豪发言人告诉《BleepingComputer》：“当我们得知这次涉及 Otelier 的事件后，我们立即联系了这家与众多酒店公司合作的供应商，并确认他们正在与网络安全专家合作调查一起影响其系统的安全事件。”

“万豪还采取了适当的预防措施，包括暂停 Otelier 提供的自动服务，直到他们完成调查，这些服务目前仍处于暂停状态。”

该威胁行为者称，他们试图敲诈万豪酒店，认为S3桶属于他们，并留下了赎金纸条，要求用加密货币支付，不要泄露数据。然而，双方没有进行任何沟通，他们表示在 9 月份凭证轮换后就失去了访问权限。

虽然万豪酒店告诉 BleepingComputer，没有迹象表明敏感信息在漏洞中被盗，但 BleepingComputer 和 Have I Been Pwned 的 Troy Hunt 分享的被盗数据样本中包含了酒店客人的个人信息。

BleepingComputer 所看到的少量样本包含广泛的数据，包括酒店客人预订、交易、员工电子邮件和其他内部数据。

暴露的部分个人信息包括酒店客人的姓名、地址、电话号码和电子邮件地址。

被盗数据还包括与凯悦、希尔顿和温德姆有关的信息和电子邮件地址。BleepingComputer 就此次信息泄露事件联系了凯悦酒店和希尔顿酒店，但没有得到回应。

特洛伊-亨特（Troy Hunt）告诉 BleepingComputer，他收到了一组广泛的数据，其中预订表包含 3,900 万行，用户表包含 2.12 亿行。

亨特说，尽管数据量很大，他还是发现了 130 万个唯一的电子邮件地址，因为很多地址都是重复的。

被曝光的个人信息被添加到 Have I Been Pwned 中，任何人都可以查看自己的电子邮件地址是否在被曝光的数据中。亨特删除了 Booking.com 和 Expedia.com 在预订过程中生成的电子邮件地址，总共留下了 437,000 个唯一的电子邮件地址。

好消息是，密码和账单信息似乎没有在这次攻击中被窃取，但威胁者仍可能在有针对性的网络钓鱼攻击中使用这些信息。

因此，您应该警惕冒充受此次漏洞影响的酒店品牌的可疑电子邮件。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303627](/post/id/303627)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/otelier-data-breach-exposes-info-hotel-reservations-of-millions/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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