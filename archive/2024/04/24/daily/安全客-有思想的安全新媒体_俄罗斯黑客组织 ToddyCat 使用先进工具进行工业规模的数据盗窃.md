---
title: 俄罗斯黑客组织 ToddyCat 使用先进工具进行工业规模的数据盗窃
url: https://www.anquanke.com/post/id/295886
source: 安全客-有思想的安全新媒体
date: 2024-04-24
fetch_date: 2025-10-04T12:14:51.296510
---

# 俄罗斯黑客组织 ToddyCat 使用先进工具进行工业规模的数据盗窃

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

# 俄罗斯黑客组织 ToddyCat 使用先进工具进行工业规模的数据盗窃

阅读量**72024**

发布时间 : 2024-04-23 10:25:28

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html>

译文仅供参考，具体内容表达以及含义原文为准。

据观察，名为ToddyCat的威胁行为者使用各种工具来保留对受感染环境的访问权限并窃取有价值的数据。

俄罗斯网络安全公司卡巴斯基将对手描述为依靠各种程序从位于亚太地区的主要政府组织（其中一些与国防相关）收集“工业规模”的数据。

安全研究人员 Andrey Gunkin、Alexander Fedotov 和 Natalya Shornikova 表示：“为了从许多主机收集大量数据，攻击者需要尽可能自动化数据收集过程，并提供多种替代方法来持续访问和监控他们攻击的系统。”说。

该公司于 2022 年 6 月首次记录ToddyCat，该攻击与至少自 2020 年 12 月以来针对欧洲和亚洲政府和军事实体的一系列网络攻击有关。这些入侵利用了一个名为 Samurai 的被动后门，允许远程访问受感染的系统主持人。

此后，对威胁行为者的间谍技术进行了更仔细的检查，发现了其他数据泄露工具，例如 LoFiSe 和 Pcexter，用于收集数据并将存档文件上传到 Microsoft OneDrive。

最新的一组程序需要混合隧道数据收集软件，这些软件在攻击者已经获得对受感染系统中特权用户帐户的访问权限后才可以使用。这包括 –

使用 OpenSSH 反向 SSH 隧道
SoftEther VPN，被重命名为看似无害的文件，如“boot.exe”、“mstime.exe”、“netscan.exe”和“kaspersky.exe”
Ngrok 和 Krong 将命令和控制 (C2) 流量加密并重定向到目标系统上的某个端口
FRP客户端，一个基于Golang的开源快速反向代理
Cuthead，.NET 编译的可执行文件，用于搜索与特定扩展名或文件名或修改日期匹配的文档
WAExp，一个 .NET 程序，用于捕获与 WhatsApp Web 应用程序相关的数据并将其保存为存档，以及
TomBerBil 从 Google Chrome 和 Microsoft Edge 等网络浏览器中提取 cookie 和凭据
卡巴斯基说：“攻击者正在积极使用绕过防御的技术，试图掩盖他们在系统中的存在。”

[![俄罗斯黑客组织 ToddyCat]( "俄罗斯黑客组织 ToddyCat")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWOezATBE8M1c-paWkS3QXZC0dc-hjRCiq6q-ubApSz3h2YReci8CtWZYi2rmPZaDqERPzCqOyGnAl9lyRRjq-X6FbUZN26yGxgzrjHgJ1Zlyslt2gaxgjdtD4Bdz6Ob6gCTNZw8RbvQ_8pgWele70KozyDVgOMH3QoaCBtt3ch0YurXs45zfahcqm3PE8/s728-rw-e365/tool.png)

“为了保护组织的基础设施，我们建议将提供流量隧道的云服务的资源和 IP 地址添加到防火墙拒绝名单中。此外，必须要求用户避免在浏览器中存储密码，因为这有助于攻击者访问敏感信息”。

本文翻译自 [原文链接](https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295886](/post/id/295886)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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