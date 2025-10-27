---
title: 重磅！Google Chrome 136 修复长达 20 年的已访问链接隐私漏洞
url: https://www.anquanke.com/post/id/306543
source: 安全客-有思想的安全新媒体
date: 2025-04-16
fetch_date: 2025-10-06T22:02:51.930599
---

# 重磅！Google Chrome 136 修复长达 20 年的已访问链接隐私漏洞

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

# 重磅！Google Chrome 136 修复长达 20 年的已访问链接隐私漏洞

阅读量**52783**

发布时间 : 2025-04-15 09:58:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Balaji N，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/google-chrome-136-getting-update-with-20-year-old-visited-links-privacy-bug-fix/>

译文仅供参考，具体内容表达以及含义原文为准。

2025 年 4 月发布的 Google Chrome 第 136 版引入了已访问链接分区功能，这是一项革命性的特性，修复了困扰网络长达二十多年的一个隐私漏洞。

作为首个采用这一强大防护措施的主流浏览器，Google Chrome 确保用户的浏览历史不会被窥探，标志着网络安全向前迈出了重大一步。

****消除历史记录检测漏洞****

从互联网早期开始，CSS 的 “:visited” 选择器就允许网站对已点击的链接设置样式，通常会将其变为紫色，以方便导航。

这项功能虽然对用户友好，却造成了一个安全漏洞。恶意网站可以检测 “:visited” 样式，从而推断出用户访问过哪些网站。

例如，如果用户从网站 A 点击了一个指向网站 B 的链接，一个恶意网站 Site Evil 之后可以显示同样的链接，并利用其 “已访问” 状态来确认用户访问过网站 B。

之前浏览器采取的缓解措施，比如限制样式选项，虽然减缓了这些历史记录检测攻击，但未能彻底消除它们。

Google Chrome 的 “已访问链接分区” 功能通过存储带有上下文细节（具体来说，就是链接网址、顶级网站和框架来源）的链接历史记录，正面解决了这一漏洞。

现在，一个链接只有在被点击的那个网站上才会显示为 “已访问” 状态，从而防止跨网站泄露信息。在同样的场景中，Site Evil 上指向网站 B 的链接将不会显示为已访问样式，除非用户在 Site Evil 上点击了该链接，这使得利用该漏洞的攻击变得毫无效果。

这种分区功能将 “已访问” 历史记录从一个全局且易受攻击的列表，转变为一个安全且特定于上下文的记录，以前所未有的精准度保护了用户的隐私。

Google 表示：“这是浏览器安全领域的一个决定性时刻。通过已访问链接分区功能，Google Chrome 在消除一个长期存在的隐私风险的同时，保留了用户所期望的无缝浏览体验。我们致力于为每个人打造一个更安全的网络环境。”

****在不牺牲安全性的前提下提升可用性****

Google Chrome 认识到直观导航的重要性，因此引入了 “自身链接” 例外规则，以在隐私和可用性之间取得平衡。

这项功能允许一个网站将指向其自身子页面的链接设置为 “已访问” ，即使这些链接是在不同的上下文中被点击的。例如，当用户浏览 Site.Wiki 网站的 gold 页面时，如果用户之前访问过该网站上关于 chrome 和 brass 的页面，那么指向这些页面的链接将显示为已访问状态，无论用户是从哪个引荐网站进入的。

由于网站本来就可以追踪自己的子页面，这个例外情况不会泄露任何新信息，同时保留了分区功能对隐私的保护。

至关重要的是，这一例外规则不包括第三方链接和内嵌框架（iframe），确保不存在跨网站追踪的漏洞。这种周全的设计在保持网站内熟悉且便捷的导航体验的同时，也坚持了严格的安全标准。

这一修复功能现已在 Google Chrome 的测试版通道中可用，并将于 2025 年 4 月 23 日在 Google Chrome 第 136 版本的稳定版中推出。Google 鼓励用户通过 Chromium 漏洞追踪器提供反馈或报告任何问题。

通过重新定义浏览历史记录的处理方式，Google Chrome 不仅保留了已访问链接样式的实用性，还为所有人提供了一个更安全、更具隐私保护的网络体验。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/google-chrome-136-getting-update-with-20-year-old-visited-links-privacy-bug-fix/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306543](/post/id/306543)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/google-chrome-136-getting-update-with-20-year-old-visited-links-privacy-bug-fix/)

如若转载,请注明出处： <https://cybersecuritynews.com/google-chrome-136-getting-update-with-20-year-old-visited-links-privacy-bug-fix/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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