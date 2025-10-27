---
title: 流氓WordPress插件揭秘：秘密恶意软件窃取信用卡并窃取凭据
url: https://www.anquanke.com/post/id/309001
source: 安全客-有思想的安全新媒体
date: 2025-06-27
fetch_date: 2025-10-06T22:50:10.772705
---

# 流氓WordPress插件揭秘：秘密恶意软件窃取信用卡并窃取凭据

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

# 流氓WordPress插件揭秘：秘密恶意软件窃取信用卡并窃取凭据

阅读量**60262**

发布时间 : 2025-06-26 14:02:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/rogue-wordpress-plugin-unmasked-stealthy-malware-skims-credit-cards-steals-credentials/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Wordfence 威胁情报团队公布了一个以流氓 WordPress 插件为幌子的强大恶意软件框架。该活动是在 2025 年 5 月 16 日的一次网站清理中首次发现的，它揭示了一个多功能的恶意软件系列，能够进行信用卡盗刷、WordPress 凭据窃取、广告欺诈和远程命令执行，同时还能完美地融入合法网站的运营。

“报告解释说：”最令人惊讶的是，其中一个变种将直接托管在受感染网站上供攻击者使用的实时后台系统（这是以前从未见过的方法）打包伪装成一个流氓 WordPress 插件。

虽然该恶意软件是在 2025 年 5 月曝光的，但有证据表明，该活动早在 2023 年 9 月就开始了，这表明这是一个长期且不断演变的行动。

这个假插件很有说服力：它遵循了 WordPress 开发的最佳实践，将管理文件夹和面向公众的文件夹分开，甚至还模仿了插件的模板结构。然而，正如分析师们所指出的，“大多数文件都只是空洞的脚手架”。

> “很明显，这个假插件与 WordPress 或 WooCommerce 没有任何关联……这是攻击者用来欺骗受害者的一种相当常见的手段”。

这次行动的核心是在欺诈插件（wordpress-core-public.js）中嵌入了一个 JavaScript 窃取器，它只在结账页面上激活。为了逃避检测，该恶意软件：

* 避免在 WordPress 管理面板中执行。
* 禁用右键单击、F12、Ctrl+Shift+I 和 Ctrl+U。
* 使用窗口大小检查检测浏览器开发人员工具。
* 插入无限循环或调试器陷阱以使开发工具崩溃。
* 重新绑定浏览器控制台方法以挫败逆向工程。

“分析的所有恶意软件样本都采用了相同的混淆技术……包括开发人员工具检测和控制台重新绑定*，*“报告披露。

该恶意软件采用多种技术来捕获敏感数据：

* 劫持 WooCommerce 表单的覆盖攻击。
* Base64 注入的虚假表单，模仿合法支付界面。
* 显示红色或绿色以提供虚假合法性的伪验证脚本。

捕获的数据（包括姓名、卡号、CVV 代码、地址和电子邮件）使用一种狡猾的方法进行编码和泄露：作为附加到虚假图像 （image-view.php） 的查询字符串，触发 GET 请求。

> “*被盗数据被编码并作为查询参数附加到虚假图像 URL 中……触发 HTTP GET 请求以泄露数据*。”

威胁并不止于表单劫持。Wordfence 团队发现了该恶意软件的至少三个主要变体：

1. 信用卡撇渣器 – 窃取支付数据并悄无声息地泄露。
2. 恶意广告注入器 – 仅在从搜索引擎或社交媒体重定向的移动用户上显示欺诈性广告。
3. 凭据收集器 – 以 WordPress 登录页面为目标，并通过 Telegram 将被盗的凭据发送到攻击者控制的服务器。

一些变体甚至动态替换文件下载链接，分发武器化的 ZIP 文件而不是合法内容。

该恶意软件不仅在前端运行。流氓插件中的 PHP 文件会创建一个服务器端基础结构，使攻击者能够持续访问：

* register-messages-posttype.php 为被盗订单数据定义自定义 POST 类型。
* wordpress-core.php 使用 WooCommerce 钩子悄无声息地完成欺诈性订单，从而延迟商家检测。

> “*这个流氓 WordPress 插件代表了信用卡撇油器的重大升级……有效地将受感染的网站转换为可供攻击者使用的自定义界面*。”

以下是已识别的一些恶意域和基础设施：

* `advertising-cdn.com`
* `chaolingtech.com`
* `contentsdeliverystat.com`
* `graphiccloudcontent.com`
* `imageresizefix.com`
* `vectorimagefabric.com`
* 电报机器人：`api.telegram.org/bot7468776395[…]chat_id=-4672047987`

Wordfence 指出，这些示例中使用的混淆技术在商业插件中也很流行，这使得检测特别具有挑战性。

本文翻译自securityonline [原文链接](https://securityonline.info/rogue-wordpress-plugin-unmasked-stealthy-malware-skims-credit-cards-steals-credentials/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309001](/post/id/309001)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/rogue-wordpress-plugin-unmasked-stealthy-malware-skims-credit-cards-steals-credentials/)

如若转载,请注明出处： <https://securityonline.info/rogue-wordpress-plugin-unmasked-stealthy-malware-skims-credit-cards-steals-credentials/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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