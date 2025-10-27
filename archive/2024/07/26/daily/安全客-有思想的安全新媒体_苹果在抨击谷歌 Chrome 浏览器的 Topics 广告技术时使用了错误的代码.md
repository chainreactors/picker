---
title: 苹果在抨击谷歌 Chrome 浏览器的 Topics 广告技术时使用了错误的代码
url: https://www.anquanke.com/post/id/298367
source: 安全客-有思想的安全新媒体
date: 2024-07-26
fetch_date: 2025-10-06T17:40:23.294564
---

# 苹果在抨击谷歌 Chrome 浏览器的 Topics 广告技术时使用了错误的代码

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

# 苹果在抨击谷歌 Chrome 浏览器的 Topics 广告技术时使用了错误的代码

阅读量**65549**

发布时间 : 2024-07-25 15:01:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Thomas Claburn，文章来源：theregister

原文地址：<https://www.theregister.com/2024/07/24/apple_google_topics/>

译文仅供参考，具体内容表达以及含义原文为准。

上周，苹果庆祝了其Safari浏览器即将推出的一系列隐私变更，并借此机会抨击竞争对手谷歌的Topics系统，该系统根据您的Chrome浏览历史投放在线广告。

这家iPhone制造商引用了威斯康星大学麦迪逊分校的Yohan Beugin和Patrick McDaniel的一篇研究论文，声称Topics有助于数字指纹识别，广告商可以使用这些指纹识别来识别以前未知的网络用户，这是许多人长期以来关注的问题。人们担心，使用Chrome中的Topics API仍然可以在网络上跟踪网民，或者可以使用该技术重新发现那些试图向广告商隐藏身份的人。

我们被告知，谷歌试图利用一点随机性来阻止这种指纹识别是不够的。

“作者使用大规模的真实用户浏览数据（自愿捐赠）来展示如何击败应该为用户提供合理否认的百分之五的噪音，以及如何使用Topics API来指纹识别和重新识别用户，”Apple WebKit团队的报告指出。

但是，所谓的指纹识别风险似乎被大大夸大了，这是由于该研究论文中依赖于不正确的随机化代码。

Topics 是 Google 的 Privacy Sandbox API 之一，旨在为广告商提供一种保护隐私的方式，让广告商可以根据他们的兴趣定制在线用户投放广告，这些广告是从他们的浏览活动中推断出来的。

当您使用 Chrome 访问使用 Topics 的网站时，该网站可以使用 API 根据您之前阅读过的页面直接询问您的浏览器您喜欢什么，以便选择最适合您兴趣的广告。如果你一直在阅读有关奶酪和葡萄酒的内容，你会看到基于此的广告，例如，因为Chrome会告诉网站你一直在浏览这类材料。

Topics旨在替代第三方cookie，这是一种传统的跟踪和定位机制，直到本周，Google还计划从Chrome中删除该机制，因为它有可能否认隐私。Chrome 不允许使用第三方 Cookie 来跟踪人们上网时的情况，从而建立他们的兴趣档案，而是将 Topics 作为用户活动的热线提供。

唉，广告商和监管机构的抵制促使谷歌重新考虑其取消第三方cookie支持。因此，现在 Privacy Sandbox API 将作为一种选项与传统的基于 cookie 的定位技术一起存在。谷歌最近发布的广告收入测试表明，保留第三方 cookie 的另一个原因，即更高的程序化广告收入，尽管当第三方 cookie 不是一种选择时，至少 Topics 的表现总比没有好。

去年，Chrome 中出现了主题支持。但在前一年，即使是广告行业的开发人员——比如广告平台公司Criteo的高级数据科学家和软件工程师Alexandre Gilotte——也对Topics带来的指纹威胁表示担忧。

具体来说，您仍然可以根据他们的主题数据识别和定位单个网民，因为他们随着时间的推移从一个站点移动到另一个站点。

这并不是谷歌广告技术首次提出指纹识别的隐私风险。2022 年，隶属于 Apple 的开发人员公开了 Cook & Co 对 Topics 的反对意见。而Topics的前身基于兴趣的API，即队列联合学习（FLoC），在一定程度上由于对指纹识别的担忧而被放弃。

正如 Apple 在其文章中所观察到的那样，许多不同的 Web API 可用于浏览器指纹识别，减少误用的可能性是一项持续的努力。

“对于未来的网络隐私来说，关键是不要用新的、可指纹识别的API来加剧指纹问题，”苹果的帖子解释说。“在某些情况下，权衡告诉我们，丰富的网络体验或增强的可访问性可以激发一定程度的指纹识别能力。但总的来说，我们的立场是，我们应该在不增加指纹识别性的情况下推进网络。

iThing 对 Topics 的反对是有充分理由的，尽管 API 带来的隐私风险似乎比最初假设的要小。

继四个月前Beugin和McDaniel的论文中的主题分析代码发布后，Google Topics工程师Josh Karlin上周在GitHub上提出了一个问题，对研究方法提出了挑战。

Karlin写道：“在相关论文中看到相当令人惊讶的结果后，我简要地看了一下您的代码，指出我遇到的一个问题很重要，因为它对仿真（以及论文的）结果有重大影响。

“您正在使用工作线程池为站点 A 和 B 上的每个用户创建主题，但您没有在每个工作线程上重新设定随机数生成器的种子（该生成器是从原始进程中分叉出来的）。结果是每个工人都创建相同的随机数流！

Karlin解释说，修复这个错误可以将重新识别率从大约57%降低到大约3%。

Beugin在回应中承认了这一点，并确认了建议的修复方法，该修复方法显示，当运行修订后的模拟时，指纹识别风险大大降低。

“虽然我们现在获得的结果在数量上发生了变化;这些用户中有2.3%、2.9%和4.1%分别在对他们的主题进行一次、两次和三次观察后被唯一重新识别，我们的发现没有质的变化：真实用户可以通过Topics API进行指纹识别，并且随着更多用户被唯一重新识别，信息泄漏会随着时间的推移而恶化，“Beugin写道。

据估计，Chrome 用户约有 35 亿，其中 4% 仍为 1.4 亿人，但至少没有最初担心的 20 亿。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/07/24/apple_google_topics/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298367](/post/id/298367)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/07/24/apple_google_topics/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/24/apple_google_topics/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

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