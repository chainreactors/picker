---
title: SVG 图像沦为网络钓鱼新载体，HTML/JS 暗藏其中窃取用户凭据
url: https://www.anquanke.com/post/id/306784
source: 安全客-有思想的安全新媒体
date: 2025-04-23
fetch_date: 2025-10-06T22:04:45.647559
---

# SVG 图像沦为网络钓鱼新载体，HTML/JS 暗藏其中窃取用户凭据

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

# SVG 图像沦为网络钓鱼新载体，HTML/JS 暗藏其中窃取用户凭据

阅读量**63397**

发布时间 : 2025-04-22 12:37:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/svg-files-weaponized-phishing-attacks-embed-html-code/>

译文仅供参考，具体内容表达以及含义原文为准。

![phish-svg]()

网络钓鱼已不再仅仅局限于那些可疑的链接和措辞拙劣的电子邮件。根据 Kaspersky 的一份新报告，威胁行为者现在正将超文本标记语言（HTML）和 JavaScript 代码嵌入到可缩放矢量图形（SVG）文件中，从而将简单的图像变成了悄无声息且有效的网络钓鱼武器。

SVG 是一种使用可扩展标记语言（XML）来描述二维矢量图形的格式。虽然它通常用于图像，但与像 JPEG 或 PNG 这样的格式不同，SVG 基于 XML 的特性使其能够支持 JavaScript 和 HTML。这种原本是为了让设计师能够处理文本和交互式内容等元素而具备的灵活性，如今正被攻击者利用。

攻击者正在精心制作包含嵌入脚本的 SVG 文件，这些脚本中带有指向网络钓鱼页面的链接。在一个典型的场景中，用户会收到一封带有 SVG 附件的电子邮件。虽然这封邮件可能会将附件标识为一张图片，但在文本编辑器中打开它时就会显示出 HTML 代码。

![]()

模仿 Google Voice 的网络钓鱼网页 |图片来源： Kaspersky

Kaspersky 的报告用一个例子来说明了这一点：一个 SVG 文件看起来像是一个 HTML 页面，上面有一个指向音频文件的链接。点击这个链接会将用户重定向到一个伪装成 Google Voice 的网络钓鱼页面。这个旨在窃取用户凭据的页面，甚至还包含了目标公司的标志，使其看起来更加可信。

在另一个例子中，攻击者使用了一个 SVG 附件来模仿一项电子签名服务，利用 JavaScript 弹出一个带有虚假微软登录表单的浏览器窗口。

![]()

网络钓鱼登录表单 |图片来源： Kaspersky

Kaspersky 的遥测数据显示，利用 SVG 进行的网络钓鱼活动大幅增加。报告中指出：“我们的遥测数据表明，在 2025 年 3 月期间，利用 SVG 进行的攻击活动显著增多。仅在今年的第一季度，我们就发现了 2825 封这类电子邮件。” 这种上升趋势一直持续到了 4 月，这表明威胁在不断加剧。

该报告强调了网络钓鱼者的适应性：“网络钓鱼者正在不懈地探索新的技术来规避检测。” 虽然目前利用 SVG 进行的网络钓鱼攻击相对简单，通常涉及网络钓鱼链接或重定向脚本，但可能出现更复杂攻击的潜在风险令人担忧。

将 SVG 用作恶意内容的载体带来了巨大的风险。正如报告所总结的那样：“SVG 格式具备在图像中嵌入 HTML 和 JavaScript 代码的能力，而攻击者正是在滥用这一特性。”

本文翻译自securityonline [原文链接](https://securityonline.info/svg-files-weaponized-phishing-attacks-embed-html-code/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306784](/post/id/306784)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/svg-files-weaponized-phishing-attacks-embed-html-code/)

如若转载,请注明出处： <https://securityonline.info/svg-files-weaponized-phishing-attacks-embed-html-code/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**7赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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