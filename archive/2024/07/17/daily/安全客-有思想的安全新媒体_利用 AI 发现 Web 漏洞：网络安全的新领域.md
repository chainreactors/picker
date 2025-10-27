---
title: 利用 AI 发现 Web 漏洞：网络安全的新领域
url: https://www.anquanke.com/post/id/297947
source: 安全客-有思想的安全新媒体
date: 2024-07-17
fetch_date: 2025-10-06T17:41:07.820864
---

# 利用 AI 发现 Web 漏洞：网络安全的新领域

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

# 利用 AI 发现 Web 漏洞：网络安全的新领域

阅读量**89795**

发布时间 : 2024-07-16 12:06:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 尼梅什·贾亚西里，文章来源：Medium

原文地址：[https://medium.com/@nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e](https://medium.com/%40nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e)

译文仅供参考，具体内容表达以及含义原文为准。

在快节奏的网络安全世界中，快速识别和缓解漏洞的能力至关重要。但是，我们使用的工具和方法必须符合道德标准和法律界限。这篇博文讲述了我在识别和利用漏洞的过程中使用 AI（特别是 ChatGPT）的实验。这次经历既有启发性，又有警示性，凸显了在网络安全中利用人工智能的巨大潜力和重大风险。

# 实验

作为一名狂热的网络安全爱好者，我经常求助于各种工具来帮助绘制目标系统的攻击面。我的目标一直是通过识别和修复漏洞来提高安全性。在这项任务中，我尝试了 ChatGPT，这是一种由 OpenAI 开发的对话式 AI，以帮助解释扫描结果和识别潜在的攻击媒介。

# 操纵 AI 响应

我遇到的挑战之一是 ChatGPT 的道德护栏，旨在防止 AI 从事或促进非法活动。最初，我的大多数提示都遭到了拒绝，因为 ChatGPT 被编程为避免帮助不道德的行为。我没有气馁，尝试了不同的提示，直到我找到了一种方法来构建我的查询，从而产生了更可操作的建议。

# 突破

经过多次尝试，我成功地提示 ChatGPT 提供“[dorks](https://en.wikipedia.org/wiki/Google_hacking)”，即帮助查找易受攻击网站的特定搜索查询。利用这些傻瓜，我确定了几个潜在的易受攻击的网站。然后，我要求 ChatGPT 分析这些网站的漏洞，并建议用于测试的有效载荷。

令我惊讶的是，ChatGPT 不仅识别了可能易受攻击的网站，还推荐了有效载荷来测试 SQL 注入漏洞。令人鼓舞的是，它还建议使用[SQLmap](https://sqlmap.org/)等自动化工具进行更有效的利用。

有了这些信息，我在一个站点上测试了一个有效负载，并立即收到 SQL 错误，确认了漏洞。使用 SQLmap，我能够访问该站点的数据库并检索有关其后端基础结构的数据和一些敏感信息。

虽然技术上的成功令人振奋，但它也引发了重大的道德问题。我可以轻松绕过 ChatGPT 的保护措施并利用它来促进潜在的非法活动，这既令人震惊又发人深省。

# 反思和经验教训

这一经验凸显了人工智能在网络安全领域的双刃剑性质。一方面，人工智能可以显著增强我们识别和缓解漏洞的能力，从而有可能使系统更加安全。另一方面，它也可能被滥用，这凸显了对强有力的道德准则和控制的必要性。

作为网络安全专业人员，我们必须负责任地使用这些工具。以下是我的经验中的一些关键要点：

* **合乎道德地使用 AI：**始终在合法性和道德准则的范围内使用 AI 工具。目标应该是提高安全性，而不是将漏洞用于恶意目的。
* **意识和教育**：了解人工智能的能力和局限性。持续学习和意识对于有效和合乎道德地利用这些工具至关重要。
* **协作和透明度**：与开发人员、研究人员和道德黑客合作，共享知识并制定更好的保护措施，防止滥用。

# 结论

人工智能和网络安全的交集既带来了令人兴奋的机遇，也带来了重大挑战。我使用 ChatGPT 的旅程提醒了我这些工具的力量以及负责任地使用它们的重要性。随着我们不断创新和探索新的领域，让我们致力于维护最高的道德标准，确保我们的进步为安全领域做出积极贡献。

通过分享这一经验，我希望引发一场关于人工智能在网络安全中的伦理影响的对话，并鼓励我们领域负责任的做法。

本文翻译自Medium [原文链接](https://medium.com/%40nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297947](/post/id/297947)

安全KER - 有思想的安全新媒体

本文转载自: [Medium](https://medium.com/%40nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e)

如若转载,请注明出处： [https://medium.com/@nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e](https://medium.com/%40nimeshjayasiri/using-ai-to-uncover-web-vulnerabilities-a-new-frontier-in-cybersecurity-0d2911e5e88e)

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [人工智能](/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据](/post/id/308092)

  2025-06-04 15:31:41
* ##### [新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备](/post/id/307967)

  2025-05-29 14:59:17
* ##### [APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信](/post/id/307963)

  2025-05-29 14:55:27

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