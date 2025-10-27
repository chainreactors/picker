---
title: 警惕！SVG 附件钓鱼攻击威胁登录数据安全
url: https://www.anquanke.com/post/id/306821
source: 安全客-有思想的安全新媒体
date: 2025-04-24
fetch_date: 2025-10-06T22:04:19.453017
---

# 警惕！SVG 附件钓鱼攻击威胁登录数据安全

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

# 警惕！SVG 附件钓鱼攻击威胁登录数据安全

阅读量**61882**

发布时间 : 2025-04-23 14:12:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaleah Salmon，文章来源：securitybrief

原文地址：<https://securitybrief.asia/story/rise-in-phishing-scams-as-svg-attachments-target-login-data>

译文仅供参考，具体内容表达以及含义原文为准。

![Story image]()

Kaspersky 观察到，通过可缩放矢量图形（SVG）图像文件发起的网络钓鱼攻击数量急剧上升，2025 年 3 月的相关事件数量相比前一个月几乎增长了五倍（是前一个月的近六倍）。

这家网络安全公司报告称，攻击者正在向个人和组织发送网络钓鱼电子邮件，邮件中带有 SVG（可缩放矢量图形）文件附件 —— 这种格式通常用于图像存储 —— 以此引诱收件人泄露敏感信息。

据 Kaspersky 称，打开这些恶意的 SVG 文件会将毫无防备的用户引导至模仿 Google 和 Microsoft 等公司热门服务的网络钓鱼网站。这些欺诈性页面旨在获取用户的登录凭据，使受害者面临严重的个人和经济损失风险。自 2025 年初以来，该公司已在全球范围内检测到超过 4000 封此类电子邮件。

SVG 文件使用可扩展标记语言（XML），这是一种支持定义各种数据类型规则的标记语言。虽然这种格式旨在帮助设计师将文本、公式和交互功能融入图像中，但它与 JavaScript 和超文本标记语言（HTML）的兼容性使其对网络犯罪分子具有吸引力。攻击者可以在 SVG 文件中嵌入脚本，当文件被打开时，这些脚本会将受害者重定向到网络钓鱼网站，他们常常利用收件人对图像附件的好奇心来达到目的。

在 Kaspersky 描述的一个典型场景中，SVG 附件充当了一个不包含任何实际图形的 HTML 页面。当打开该文件时，会显示一个网页，上面有一个声称是音频文件的链接。点击该链接会将用户重定向到一个设计得像 Google Voice 的网络钓鱼页面，而所谓的音频实际上只是一张静态图片。

进一步的交互操作，比如按下 “播放音频” 按钮，会将用户引导至一个虚假的企业电子邮件登录页面。这个冒牌网站会提及 Google Voice，并使用目标公司的标志来增强其可信度，从而诱使用户输入他们的凭据。

Kaspersky 还记录了这种攻击方式的一个变体，攻击者发送的网络钓鱼电子邮件看似是来自一家电子签名服务公司的通知。在这种情况下，SVG 附件被伪装成一份需要查看和签名的文档。该 SVG 文件并不充当 HTML 页面，而是包含 JavaScript 代码，一旦被打开，就会触发一个浏览器窗口，显示另一个虚假的登录页面 —— 这次模仿的是 Microsoft 的一项服务。

Kaspersky 的反垃圾邮件专家 Roman Dedenok 评论道：“网络钓鱼者正在不懈地探索新的技术来规避检测。他们会改变策略，有时会利用用户重定向来制造混淆，有时则会尝试使用不同的附件格式。带有 SVG 附件的攻击呈现出明显的上升趋势。虽然目前这些攻击相对基础，SVG 文件要么包含一个网络钓鱼链接页面，要么包含一个重定向到欺诈网站的脚本，但 SVG 作为恶意内容的载体，也可能被用于更复杂的定向攻击。”

Kaspersky 提供了一些建议，以帮助个人和企业避免成为这些攻击活动的受害者。相关指导包括：仅在发件人可信的情况下打开电子邮件并点击链接；通过其他通信方式仔细核实可能存在异常的邮件；仔细检查网站的统一资源定位符（URL），留意细微的错误，比如用一个看起来相似的数字替换字母；以及在浏览互联网时使用可靠的安全解决方案。

本文翻译自securitybrief [原文链接](https://securitybrief.asia/story/rise-in-phishing-scams-as-svg-attachments-target-login-data)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306821](/post/id/306821)

安全KER - 有思想的安全新媒体

本文转载自: [securitybrief](https://securitybrief.asia/story/rise-in-phishing-scams-as-svg-attachments-target-login-data)

如若转载,请注明出处： <https://securitybrief.asia/story/rise-in-phishing-scams-as-svg-attachments-target-login-data>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**8赞

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