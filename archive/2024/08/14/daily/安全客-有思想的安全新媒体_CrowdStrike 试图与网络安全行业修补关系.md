---
title: CrowdStrike 试图与网络安全行业修补关系
url: https://www.anquanke.com/post/id/299071
source: 安全客-有思想的安全新媒体
date: 2024-08-14
fetch_date: 2025-10-06T18:02:06.142073
---

# CrowdStrike 试图与网络安全行业修补关系

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

# CrowdStrike 试图与网络安全行业修补关系

阅读量**69418**

发布时间 : 2024-08-13 11:05:20

**x**

##### 译文声明

本文是翻译文章，文章原作者 Dark Reading Staff，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cybersecurity-operations/crowdstrike-tries-patch-things-up-cybersecurity-industry>

译文仅供参考，具体内容表达以及含义原文为准。

CrowdStrike 上周在对该事件的根本原因分析中表示，多种因素导致 Falcon EDR 传感器崩溃，导致全球停电影响了 7 月份超过 850 万个 Windows 系统。与此同时，CrowdStrike 首席技术官乔治·库尔茨 （George Kurtz） 和总裁迈克尔·森托纳斯 （Michael Sentonas） 在拉斯维加斯公开指责。

CrowdStrike 在其根本原因分析中指出，内容验证器验证的输入与提供给内容解释器的输入之间存在不匹配，并且内容解释器中存在越界覆盖问题。更新的测试和部署方式存在问题。

“接收到携带有问题内容的新版本通道文件 291 的传感器在内容解释器中暴露于潜在的越界读取问题。在来自操作系统的下一个 IPC 通知中，将评估新的 IPC 模板实例，并指定与第 21 个输入值进行比较。Content Interpreter 预计只有 20 个值，“CrowdStrike 说。“因此，尝试访问第 21 个值会产生超出输入数据数组末尾的越界内存读取，并导致系统崩溃。”

虽然CrowdStrike表示这种情况不会再次发生，但该公司正在改变其流程并采取缓解措施，以“确保进一步增强弹性”，该公司表示。CrowdStrike还聘请了两家软件安全供应商，对Falcon传感器代码进行广泛的审查，以确保安全和质量保证，并且正在对从开发到部署的端到端质量过程进行独立审查 。

## “承认”自己的错误

在拉斯维加斯举行的Black Hat USA会议的创新者与投资者峰会上，主持人Chenxi Wang以向CrowdStrike首席技术官George Kurtz提出的一个问题拉开了她的小组讨论序幕：“发生了什么？库尔茨向房间道歉 – 这一行动似乎受到观众的欢迎 – 并指出该公司已经公布了根本原因分析的结果。

几天后，该公司再次承认了自己的失败，因为 CrowdStrike 总裁迈克尔·森托纳斯 （Michael Sentonas） 周六在 DEF CON 黑客大会上接受了 2024 年 Pwnie 最史诗般的失败奖。Pwnie 奖旨在表彰过去一年在网络安全领域取得最杰出成就和最大失败的奖项。根据 Pwnie 奖的描述，“最史诗般的失败”类别是“壮观的史诗般的失败——那种让整个信息安全行业失望的失败”。

Pwnie Awards 早在 7 月就表示，大规模的全球停电使 CrowdStrike 自动成为赢家。停电对全球的影响突出了，因为 CrowdStrike 被授予两层奖杯，而不是传统的小马形奖杯授予其他类别的获胜者。森托纳斯表示，奖杯将在德克萨斯州奥斯汀的公司总部展出，以提醒员工“这些事情不可能发生”。

“绝对不是值得骄傲的奖项，”森托纳斯在他的获奖感言中说。“我认为当我直接说我会来得到它时，团队感到惊讶。我们大错特错了，我们已经说过很多次了。当你把事情做好时，拥有它非常重要，当你做错事时，拥有它非常重要，我们在这种情况下就是这样做的。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cybersecurity-operations/crowdstrike-tries-patch-things-up-cybersecurity-industry)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299071](/post/id/299071)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cybersecurity-operations/crowdstrike-tries-patch-things-up-cybersecurity-industry)

如若转载,请注明出处： <https://www.darkreading.com/cybersecurity-operations/crowdstrike-tries-patch-things-up-cybersecurity-industry>

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

* [“承认”自己的错误](#h2-0)

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