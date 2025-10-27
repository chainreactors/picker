---
title: Microsoft 365 Copilot 中漏洞允许攻击者窃取用户敏感信息
url: https://www.anquanke.com/post/id/299574
source: 安全客-有思想的安全新媒体
date: 2024-08-29
fetch_date: 2025-10-06T17:59:22.985437
---

# Microsoft 365 Copilot 中漏洞允许攻击者窃取用户敏感信息

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

# Microsoft 365 Copilot 中漏洞允许攻击者窃取用户敏感信息

阅读量**60736**

发布时间 : 2024-08-28 12:51:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 亚历山德罗·马斯切利诺，文章来源：infosecurity magazine

原文地址：<https://www.infosecurity-magazine.com/news/microsoft-365-copilot-flaw-exposes/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员披露了 Microsoft 365 Copilot 中允许攻击者窃取用户敏感信息的漏洞。

发现该漏洞的 Johann Rehberger 在 8 月 26 日发表的一篇博文中描述了漏洞利用链。该攻击结合了多种高级技术，包括提示注入、自动工具调用和一种称为 ASCII 走私的新方法，该方法将数据暂存以进行泄露。

攻击从通过恶意电子邮件或共享文档发送的提示注入开始。触发后，此注入会提示 Microsoft 365 Copilot 在未经用户同意的情况下搜索其他电子邮件和文档。

然后，攻击者可以利用 ASCII 走私，它使用不可见的 Unicode 字符将敏感信息嵌入看似良性的超链接中。当用户点击这些链接时，嵌入的数据会传输到攻击者控制的第三方服务器。

### **漏洞报告和 Microsoft 补丁**

Rehberger 最初于 2024 年 1 月向 Microsoft 报告了该漏洞。尽管其性质复杂，但该问题最初被归类为低严重性。然而，Rehberger 展示了这个漏洞利用链如何泄露敏感数据，例如多因素身份验证 （MFA） 代码，促使 Microsoft 重新考虑并最终在 2024 年 7 月之前修补该漏洞。

*阅读有关 Microsoft 补丁的更多信息：Microsoft 在 7 月补丁星期二修复四个零日漏洞*

据研究人员称，该漏洞凸显了 Microsoft 365 Copilot 等 AI 工具带来的潜在危险，这些工具依赖大型语言模型 （LLM） 来处理用户内容。

特别是，该事件凸显了实施强大的安全措施以防止及时注入和相关攻击的重要性，尤其是在 AI 工具越来越多地集成到企业环境中的情况下。

Microsoft 尚未透露补丁的细节，但 Rehberger 证实该漏洞不再构成威胁。

“目前尚不清楚 Microsoft 究竟是如何修复该漏洞的，以及实施了哪些缓解建议，”研究人员写道。“但是我在 1 月和 2 月构建并与他们分享的漏洞已经不起作用了，而且似乎从几个月前开始就不再呈现链接了。”

为了抵御类似的攻击，Rehberger 建议企业评估其风险承受能力和风险敞口，以防止 Copilot 的数据泄露，并实施数据丢失防护 （DLP） 和其他安全控制措施来管理这些工具的创建和发布。

本文翻译自infosecurity magazine [原文链接](https://www.infosecurity-magazine.com/news/microsoft-365-copilot-flaw-exposes/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299574](/post/id/299574)

安全KER - 有思想的安全新媒体

本文转载自: [infosecurity magazine](https://www.infosecurity-magazine.com/news/microsoft-365-copilot-flaw-exposes/)

如若转载,请注明出处： <https://www.infosecurity-magazine.com/news/microsoft-365-copilot-flaw-exposes/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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