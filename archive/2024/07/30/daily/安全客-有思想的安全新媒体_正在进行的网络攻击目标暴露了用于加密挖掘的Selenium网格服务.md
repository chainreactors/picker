---
title: 正在进行的网络攻击目标暴露了用于加密挖掘的Selenium网格服务
url: https://www.anquanke.com/post/id/298530
source: 安全客-有思想的安全新媒体
date: 2024-07-30
fetch_date: 2025-10-06T17:40:47.575750
---

# 正在进行的网络攻击目标暴露了用于加密挖掘的Selenium网格服务

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

# 正在进行的网络攻击目标暴露了用于加密挖掘的Selenium网格服务

阅读量**77493**

发布时间 : 2024-07-29 15:01:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员正在对正在进行的活动发出警报，该活动正在利用互联网暴露的 Selenium Grid 服务进行非法加密货币挖掘。

云安全公司 Wiz 正在以 **SeleniumGreed** 的名义跟踪该活动。该活动针对旧版本的 Selenium（3.141.59 及更早版本），据信至少从 2023 年 4 月开始进行。

“大多数用户不知道，Selenium WebDriver API可以与机器本身进行完全交互，包括读取和下载文件，以及运行远程命令，”Wiz研究人员Avigayil Mechtinger，Gili Tikochinski和Dor Laska说。

“默认情况下，未为此服务启用身份验证。这意味着许多可公开访问的实例配置错误，任何人都可以访问并被滥用于恶意目的。

Selenium Grid 是 Selenium 自动化测试框架的一部分，支持跨多个工作负载、不同浏览器和各种浏览器版本并行执行测试。

项目维护者在一份支持文档中警告说：“必须使用适当的防火墙权限保护Selenium Grid免受外部访问”，并指出如果不这样做，可能会允许第三方运行任意二进制文件并访问内部Web应用程序和文件。

目前尚不清楚究竟谁是这次袭击活动的幕后黑手。但是，它涉及威胁参与者针对公开暴露的 Selenium Grid 实例，并利用 WebDriver API 运行负责下载和运行 XMRig 矿工的 Python 代码。

它首先由攻击者向易受攻击的 Selenium Grid 中心发送请求，旨在执行包含 Base64 编码有效载荷的 Python 程序，该有效载荷会向攻击者控制的服务器生成反向 shell （“164.90.149[.]104“） 为了获取最终有效载荷，开源 XMRig 矿工的修改版本。

研究人员解释说：“他们不是在矿工配置中对矿池IP进行硬编码，而是在运行时动态生成它。“他们还在添加的代码（以及配置中）设置了 XMRig 的 TLS 指纹功能，确保矿工只与威胁行为者控制的服务器通信。”

据说有问题的 IP 地址属于已被威胁行为者破坏的合法服务，因为它还被发现托管了一个公开暴露的 Selenium Grid 实例。

Wiz表示，在较新版本的Selenium上执行远程命令是可能的，并且它识别了超过30,000个暴露于远程命令执行的实例，因此用户必须采取措施关闭错误配置。

研究人员说：“Selenium Grid不是为暴露在互联网上而设计的，其默认配置没有启用身份验证，因此任何可以通过网络访问中心的用户都可以通过API与节点进行交互。

“如果服务部署在具有防火墙策略不足的公共 IP 的计算机上，这将带来重大的安全风险。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298530](/post/id/298530)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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