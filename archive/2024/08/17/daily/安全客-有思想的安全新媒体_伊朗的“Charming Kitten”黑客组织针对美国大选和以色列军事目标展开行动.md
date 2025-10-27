---
title: 伊朗的“Charming Kitten”黑客组织针对美国大选和以色列军事目标展开行动
url: https://www.anquanke.com/post/id/299225
source: 安全客-有思想的安全新媒体
date: 2024-08-17
fetch_date: 2025-10-06T18:02:10.615702
---

# 伊朗的“Charming Kitten”黑客组织针对美国大选和以色列军事目标展开行动

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

# 伊朗的“Charming Kitten”黑客组织针对美国大选和以色列军事目标展开行动

阅读量**39461**

发布时间 : 2024-08-16 15:00:29

**x**

##### 译文声明

本文是翻译文章，文章原作者 Elizabeth Montalbano，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/google-iran-charming-kitten-targets-presidential-elections-israeli-military>

译文仅供参考，具体内容表达以及含义原文为准。

与伊朗伊斯兰革命卫队（IRGC）有关联的一个威胁组织最近发起了新的网络攻击，目标是与即将到来的美国总统选举相关的电子邮件账户，以及以色列的高调军事和政治目标。这些活动主要表现为社交工程钓鱼攻击，是对以色列在加沙地带持续军事行动以及美国对此的支持的一种报复，随着该地区紧张局势的升级，预计此类活动将持续下去。

据谷歌威胁分析小组（TAG）昨日发布的一篇博客文章显示，与伊朗支持的APT42（更广为人知的名字是“迷人小猫”）有关联的“大量”尝试登录约十多名与拜登总统和前总统特朗普有关联人士的个人电子邮件账户已被检测并阻止。攻击的目标包括现任和前任美国政府官员以及与各自竞选团队相关的人士。

此外，该威胁组织在其持续努力中仍然坚持不懈，试图入侵与现任美国副总统、现总统候选人卡马拉·哈里斯以及前总统特朗普有关联的个人账户，包括现任和前任政府官员以及与竞选团队相关的人士。

这一发现是在一个基于Telegram的服务“IntelFetch”也被发现正在汇总与民主党全国委员会（DNC）和民主党网站相关的被攻破的凭据的同时出现的。

## Charming Kitten持续针对以色列目标进行活动

除了与选举相关的攻击外，TAG研究人员还一直在追踪针对以色列军事和政治目标的各种网络钓鱼活动，包括与国防部门有联系的人，以及外交官、学者和非政府组织，这些活动自4月以来已大幅增加。

据该帖子称，谷歌最近删除了该组织创建的多个 Google Sites 页面，“这些页面伪装成合法的以色列犹太机构的请愿书，呼吁以色列政府进行调解以结束冲突”。

Charming Kitten 还在 4 月份针对以色列军方、国防、外交官、学术界和民间社会的网络钓鱼活动中滥用了 Google 协作平台，通过发送电子邮件冒充记者要求对最近针对以色列前高级军事官员和航空航天高管的空袭发表评论。

“在过去的六个月里，我们已经系统地破坏了这些攻击者在 50 多个类似活动中滥用 Google 协作平台的能力，”Google TAG 表示。

其中一个活动涉及网络钓鱼诱饵，该诱饵具有攻击者控制的 Google 站点链接，该链接会将受害者定向到虚假的 Google Meet 登录页面，而其他诱饵包括 OneDrive、Dropbox 和 Skype。

## 新的和正在进行的 APT42 网络钓鱼活动

在其他攻击中，Charming Kitten 在网络钓鱼活动中采用了各种社会工程策略，这些策略反映了其地缘政治立场。根据谷歌TAG的说法，在可预见的未来，这种活动不太可能放松。

他们发现，最近针对以色列外交官、学者、非政府组织和政治实体的运动来自各种电子邮件服务提供商托管的账户。尽管这些消息不包含恶意内容，但 Google TAG 推测它们“可能是为了在 APT42 试图破坏目标之前引起收件人的参与”，谷歌暂停了与 APT 关联的 Gmail 帐户。

6 月的另一项活动针对以色列非政府组织，使用一个善意的 PDF 电子邮件附件，冒充合法政治实体，其中包含一个缩短的 URL 链接，该链接重定向到旨在收集 Google 登录凭据的网络钓鱼工具包登录页面。事实上，研究人员指出，APT42 经常使用直接嵌入电子邮件正文中的网络钓鱼链接，或者作为其他无害的 PDF 附件中的链接。

“在这种情况下，APT42 会通过社会工程诱饵吸引他们的目标，以设置视频会议，然后链接到一个登录页面，在该页面中，目标被提示登录并发送到网络钓鱼页面，”该帖子称。

另一个 APT42 活动模板正在发送合法的 PDF 附件，作为社会工程诱饵的一部分，以建立信任并鼓励目标在 Signal、Telegram 或 WhatsApp 等其他平台上参与，根据 Google TAG 的说法，这很可能是发送网络钓鱼工具包以获取凭据的一种方式。

## 出于政治动机的袭击仍在继续

所有这些都是对 APT42/Charming Kitten 的常见狩猎，它以出于政治动机的网络攻击而闻名。最近， 自以色列为报复哈马斯10月7日对以色列的袭击而在加沙采取军事行动以来，它一直非常积极地打击以色列、美国和其他全球目标。

总体而言 ，伊朗长期以来一直通过对以色列和美国的网络攻击来应对该地区的紧张局势。根据 Google TAG 的数据，仅在过去六个月中，美国和以色列就占 APT42 已知地理目标的约 60%。在以色列最近在伊朗领土上暗杀哈马斯最高领导人之后，预计会有更多活动，因为专家认为网络空间仍将是伊朗支持的威胁行为者的主要战场。

“APT42 是一个复杂、持续的威胁行为者，他们没有迹象表明会停止针对用户和部署新策略的尝试，”Google TAG 表示。“随着伊朗和以色列之间的敌对行动加剧，我们可以预期 APT42 在那里的活动会增加。”

研究人员还在其帖子中包含了一份妥协指标 （IoC） 列表，其中包括 APT42 已知使用的域和 IP 地址。可能成为目标的组织也应对该组织在其最近发现的威胁活动中使用的各种社会工程和网络钓鱼策略保持警惕。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/google-iran-charming-kitten-targets-presidential-elections-israeli-military)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299225](/post/id/299225)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cyberattacks-data-breaches/google-iran-charming-kitten-targets-presidential-elections-israeli-military)

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/google-iran-charming-kitten-targets-presidential-elections-israeli-military>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [Charming Kitten持续针对以色列目标进行活动](#h2-0)
* [新的和正在进行的 APT42 网络钓鱼活动](#h2-1)
* [出于政治动机的袭击仍在继续](#h2-2)

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