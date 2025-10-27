---
title: DigiCert 因域名验证监督问题撤销 83,000 多份 SSL 证书
url: https://www.anquanke.com/post/id/298657
source: 安全客-有思想的安全新媒体
date: 2024-08-02
fetch_date: 2025-10-06T18:00:58.170508
---

# DigiCert 因域名验证监督问题撤销 83,000 多份 SSL 证书

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

# DigiCert 因域名验证监督问题撤销 83,000 多份 SSL 证书

阅读量**71039**

发布时间 : 2024-08-01 14:24:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html>

译文仅供参考，具体内容表达以及含义原文为准。

证书颁发机构 （CA） DigiCert 警告说，它将在 24 小时内撤销 SSL/TLS 证书的子集，因为它在验证数字证书是否颁发给域的合法所有者方面存在疏忽。

该公司表示，将采取措施撤销没有适当域控制验证（DCV）的证书。

“在向客户颁发证书之前，DigiCert会使用CA /浏览器论坛（CABF）批准的几种方法之一来验证客户对他们请求证书的域名的控制权或所有权，”它说。

其中一种方法取决于客户设置一个DNS CNAME记录，其中包含DigiCert提供给他们的随机值，然后DigiCert对相关域执行DNS查找，以确保随机值相同。

每个 DigiCert 的随机值都带有下划线字符前缀，以防止与使用相同随机值的实际子域发生冲突。

这家总部位于犹他州的公司发现，它未能在一些基于 CNAME 的验证案例中使用的随机值中包含下划线前缀。

该问题的根源在于从 2019 年开始实施的一系列更改，以改进底层架构，作为其中的一部分，添加下划线前缀的代码被删除，随后“添加到更新系统中的某些路径”，但没有添加到一个既不自动添加也不检查随机值是否有预加下划线的路径。

DigiCert表示：“在部署更新系统之前进行的跨职能团队审查中，没有发现自动下划线前缀的遗漏。

“虽然我们进行了回归测试，但这些测试未能提醒我们功能的变化，因为回归测试的范围仅限于工作流和功能，而不是随机值的内容/结构。”

“不幸的是，没有进行任何审查来比较传统的随机值实现与新系统中每种场景的随机值实现。如果我们进行了这些评估，我们就会更早地了解到，系统不会在需要时自动将下划线前缀添加到随机值中。

随后，在 2024 年 6 月 11 日，DigiCert 表示，它改进了随机值生成过程，并取消了在用户体验增强项目的范围内手动添加下划线前缀的做法，但承认它再次未能“将此 UX 更改与遗留系统中的下划线流程进行比较”。

该公司表示，直到“几周前”，当一位不愿透露姓名的客户就验证中使用的随机值提出要求时，它才发现不合规问题，这促使了更深入的审查。

它还指出，该事件影响了大约 0.4% 的适用域验证，根据相关 Bugzilla 报告的更新，这影响了 83,267 个证书和 6,807 个客户。

建议已通知的客户尽快替换其证书，方法是登录其 DigiCert 帐户，生成证书签名请求 （CSR），并在通过 DCV 后重新颁发证书。

这一事态发展促使美国网络安全和基础设施安全局 （CISA） 发布了一份警报，指出“撤销这些证书可能会导致依赖这些证书进行安全通信的网站、服务和应用程序暂时中断。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298657](/post/id/298657)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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