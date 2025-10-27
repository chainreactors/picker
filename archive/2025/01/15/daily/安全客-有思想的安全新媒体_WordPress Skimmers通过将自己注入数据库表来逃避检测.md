---
title: WordPress Skimmers通过将自己注入数据库表来逃避检测
url: https://www.anquanke.com/post/id/303463
source: 安全客-有思想的安全新媒体
date: 2025-01-15
fetch_date: 2025-10-06T20:07:24.183534
---

# WordPress Skimmers通过将自己注入数据库表来逃避检测

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

# WordPress Skimmers通过将自己注入数据库表来逃避检测

阅读量**43867**

发布时间 : 2025-01-14 10:02:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员警告说，一种新的隐蔽式信用卡盗刷活动以 WordPress 电子商务结账页面为目标，在与内容管理系统（CMS）相关的数据库表中插入恶意 JavaScript 代码。

“这种针对 WordPress 网站的信用卡盗刷恶意软件会在数据库条目中悄无声息地注入恶意 JavaScript，以窃取敏感的支付信息，”Sucuri 研究员 Puja Srivastava 在一份新的分析报告中说。

“该恶意软件专门在结账页面上激活，要么劫持现有的支付字段，要么注入虚假的信用卡表单。”

这家 GoDaddy 旗下的网站安全公司表示，它发现该恶意软件嵌入了 WordPress wp\_options 表中的 “widget\_block ”选项，从而使其能够避开扫描工具的检测，并在被入侵网站上持续存在而不引起注意。

这样做的目的是通过 WordPress 管理面板（wp-admin > widgets）将恶意 JavaScript 插入 HTML 块部件中。

JavaScript 代码的工作原理是检查当前页面是否为结账页面，并确保只有在网站访问者即将输入支付信息时才会启动，此时它会动态创建一个模仿 Stripe 等合法支付处理程序的虚假支付屏幕。

该表单旨在获取用户的信用卡号、有效期、CVV 码和账单信息。另外，流氓脚本还能实时捕获在合法支付屏幕上输入的数据，以最大限度地提高兼容性。

窃取的数据随后会进行 Base64 编码，并结合 AES-CBC 加密，使其看起来无害并抵御分析尝试。在最后阶段，数据会被传输到攻击者控制的服务器（“valhafather[.]xyz ”或 “fqbe23[.]xyz”）。

Sucuri 在一个多月前也曾报道过类似的活动，利用 JavaScript 恶意软件动态创建虚假信用卡表单或提取在结账页面支付字段中输入的数据。

获取的信息在外泄到远程服务器（“staticfonts[.]com”）之前会经过三层混淆处理，首先将其编码为 JSON，然后用密钥 “script ”进行 XOR 加密，最后使用 Base64 编码。

斯里瓦斯塔瓦指出：“该脚本旨在从结账页面的特定字段中提取敏感的信用卡信息。然后，恶意软件通过 Magento 的 API 收集其他用户数据，包括用户姓名、地址、电子邮件、电话号码和其他账单信息。这些数据是通过Magento的客户数据和报价模型获取的。”

在此次披露之前，还发现了一个以财务为动机的网络钓鱼电子邮件活动，该活动以未清偿付款请求为幌子，诱骗收件人点击 PayPal 登录页面，金额高达近 2200 美元。

Fortinet FortiGuard 实验室的卡尔-温莎（Carl Windsor）说：“骗子似乎只是注册了一个微软 365 测试域名（免费使用三个月），然后创建了一个包含受害者电子邮件的分发列表（Billingdepartments1[@]gkjyryfjy876.onmicrosoft.com）。在 PayPal 门户网站上，他们只需请求付款，并将分发列表添加为地址。”

该活动的狡猾之处在于，这些邮件来自一个合法的 PayPal 地址 (service@paypal.com)，并包含一个真实的登录 URL，这使得这些邮件能够通过安全工具。

更糟糕的是，一旦受害者试图登录他们的 PayPal 账户，了解付款请求，他们的账户就会自动链接到分发列表的电子邮件地址，从而允许威胁行为者劫持账户控制权。

最近几周，还观察到恶意行为者利用一种名为交易模拟欺骗的新技术从受害者钱包中窃取加密货币。

Scam Sniffer 说：“现代 Web3 钱包将交易模拟作为一项用户友好功能。这项功能允许用户在签署交易之前预览交易的预期结果。虽然设计的目的是提高透明度和用户体验，但攻击者已经找到了利用这一机制的方法。”

感染链涉及利用交易模拟和执行之间的时间差，允许攻击者模仿去中心化应用程序（DApps）建立虚假网站，以实施欺诈性钱包抽水攻击。

Web3 反诈骗解决方案提供商表示：“这种新的攻击载体代表了网络钓鱼技术的重大演变。攻击者现在不再依靠简单的欺骗，而是利用用户所依赖的可信钱包功能来确保安全。这种复杂的方法使侦测变得特别具有挑战性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303463](/post/id/303463)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html)

如若转载,请注明出处： <https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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