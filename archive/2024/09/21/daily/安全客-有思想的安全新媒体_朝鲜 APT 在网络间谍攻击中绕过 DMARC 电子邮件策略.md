---
title: 朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略
url: https://www.anquanke.com/post/id/300242
source: 安全客-有思想的安全新媒体
date: 2024-09-21
fetch_date: 2025-10-06T18:24:55.635575
---

# 朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略

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

# 朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略

阅读量**112533**

发布时间 : 2024-09-20 14:33:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sean Costigan ，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/threat-intelligence/north-korean-apt-bypasses-dmarc-email-cyber-espionage-attacks>

译文仅供参考，具体内容表达以及含义原文为准。

随着地缘政治紧张局势的加剧，朝鲜网络间谍组织对美国及其盟友组织的网络攻击激增也就不足为奇了。然而，令人不安的是，一个名为 Kimsuky 的高级持续威胁 （APT） 组织通过将防御优势转化为弱点而取得了显著的成功——利用配置不佳的基于域的消息身份验证、报告和一致性 （DMARC） 策略来执行鱼叉式网络钓鱼活动以获得优势。

5 月 2 日 ，美国联邦调查局 （FBI）、国家安全局 （NSA） 和美国国务院的一份公告指出，Kimsuky 作为朝鲜侦察总局 （RGB） 的一个部门，一直在向知名智库、媒体、非营利组织、学术界和其他组织的个人发送欺骗性电子邮件。这些电子邮件是情报活动的一部分，旨在收集有关地缘政治和外交政策计划的信息，特别是与核政策、制裁和涉及朝鲜半岛的其他敏感问题有关的信息。

随着制裁的严厉打击，朝鲜已经发展出强大的网络犯罪能力，为该政权创造流动性。然而，在这种情况下，我们看到 Kimsuky 威胁行为者将他们的重点转移到情报行动上，以受信任方和知名组织持有的大量信息为目标。尽管正在进行的攻击活动具有复杂的地缘政治影响，但有效防御这些攻击从根本上取决于稳健、可操作且正确执行的网络卫生实践。

## DMARC 错误配置太常见了

Kimsuky 正在使用 DMARC 配置不当或缺失的受信任网络来欺骗合法域并冒充受信任的个人和组织。DMARC 协议的创建是为了阻止用户帐户的泄露，并阻止这里正在运作的社会工程类型。

它应该这样工作：DMARC 允许电子邮件收件人通过域名系统 （DNS） 验证电子邮件的来源，确保威胁行为者无法欺骗合法域。DMARC 会检查传入邮件的发件人策略框架 （SPF） 和域名密钥识别邮件 （DKIM） 记录，如果它看起来不合法，则告诉接收邮件服务器下一步该怎么做。

![DMARC.png]( "DMARC.png")

但正如 Kimsuky 的攻击所表明的那样，这只有在正确配置 DMARC 服务的情况下才能奏效。正如 IC3 公告所详述的那样，错误配置太常见了，或者域所有者对策略的定义很糟糕。对于一些组织来说，自我管理的 DMARC 似乎具有成本效益，但它也可能导致重大疏忽，包括增加漏洞、未能注意不断变化的威胁、缺少健全的合规性报告以及产生虚假的安全感。

## 朝鲜的攻击是什么样子的

Kimsuky 的鱼叉式网络钓鱼活动可能从来自看似可靠来源的无害电子邮件开始，在发送带有恶意链接或附件的后续电子邮件之前建立信任。然后，该组织利用成功的入侵手段，通过针对更高价值目标的更可信的鱼叉式网络钓鱼电子邮件升级攻击。

该组织将情报收集活动的重点针对韩国、日本和美国，目标是被认定为各个领域专家的个人。 根据网络安全和基础设施安全局 （CISA） 随后的公告，智库和韩国政府实体也成为目标。

FBI-NSA 公告中的一个真实示例的主题行是：“[邀请] 美国对朝鲜的政策会议”。这条信息似乎来自一所知名大学，开头是：“我希望您和您的家人度过一个美好的假期和一个宁静的季节。我很荣幸邀请您为由 [合法智库] 主办的私人研讨会发表主题演讲，讨论美国对朝鲜的政策。作为进一步的诱惑，该电子邮件还提供 500 美元的演讲者费。

另一封电子邮件的主题是“关于朝鲜的问题”，作者冒充合法媒体的记者要求采访，然后概述了朝鲜的核活动。

在大学示例中，该电子邮件收到了 SPF 和 DKIM 检查的“通过”，这表明攻击者获得了对大学合法电子邮件客户端的访问权限。尽管 DMARC 返回“失败”，因为发件人的电子邮件域与合法来源的 SPF 和 DKIM 记录不同，但组织的 DMARC 策略未设置为采取过滤操作，因此邮件被投递。在第二种情况下，不存在 DMARC 策略，允许攻击者欺骗记者的姓名和新闻机构的电子邮件域。

## 为什么 DMARC 很重要

美国政府的公告为组织保护其数字资产提供了令人信服的理由。Kimsuky 并不是 APT 中唯一一个，更广泛地说，也不是以营利为目的的网络犯罪分子：他们分享了经验教训，并且都越来越擅长针对错误配置和弱点。

保护和正确配置 DMARC 是关键，因为它可以改善组织的网络卫生，并广泛抵御无处不在的威胁，如商业电子邮件泄露和勒索软件电子邮件攻击。

值得注意的是，行业或法规要求可能已经使 DMARC 成为您组织的要求。截至 2024 年 2 月，谷歌和雅虎已要求发送大量电子邮件的组织使用 DMARC，据报道，Microsoft 正计划效仿。此外，PCI DSS 4.0 需要实施 DMARC。根据 BIMI Radar 的数据，自 FBI 5 月 2 日发布公告以来，截至 6 月 17 日，全球 DMARC 的采用率已从 374 万个组织增长到 571 万个组织。

工作中还有一个商业要务。组织必须优先考虑网络卫生，以保护其数字资产、防止数据泄露并防范不断演变的网络安全威胁。DMARC 应该是您组织网络态势的一部分。如果管理得当，它不仅可以确保更好的送达率，提供针对网络钓鱼和商业电子邮件泄露 （BEC） 的保护，并支持部署用于消息识别的品牌指标 （BIMI），还可以帮助关闭打击民族国家间谍活动和网络犯罪的大门。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/threat-intelligence/north-korean-apt-bypasses-dmarc-email-cyber-espionage-attacks)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300242](/post/id/300242)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/threat-intelligence/north-korean-apt-bypasses-dmarc-email-cyber-espionage-attacks)

如若转载,请注明出处： <https://www.darkreading.com/threat-intelligence/north-korean-apt-bypasses-dmarc-email-cyber-espionage-attacks>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [DMARC 错误配置太常见了](#h2-0)
* [朝鲜的攻击是什么样子的](#h2-1)
* [为什么 DMARC 很重要](#h2-2)

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