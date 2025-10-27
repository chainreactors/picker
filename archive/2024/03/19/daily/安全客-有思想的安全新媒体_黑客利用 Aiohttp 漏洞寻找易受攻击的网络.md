---
title: 黑客利用 Aiohttp 漏洞寻找易受攻击的网络
url: https://www.anquanke.com/post/id/294023
source: 安全客-有思想的安全新媒体
date: 2024-03-19
fetch_date: 2025-10-04T12:07:52.154485
---

# 黑客利用 Aiohttp 漏洞寻找易受攻击的网络

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

# 黑客利用 Aiohttp 漏洞寻找易受攻击的网络

阅读量**79715**

发布时间 : 2024-03-18 10:29:28

**x**

##### 译文声明

本文是翻译文章，文章来源：https://www.bleepingcomputer.com/news/security/hackers-exploit-aiohttp-bug-to-find-vulnerable-networks/

译文仅供参考，具体内容表达以及含义原文为准。

勒索软件攻击者“ShadowSyndicate”正在扫描易受 CVE-2024-23334（aiohttp Python 库中的目录遍历漏洞）影响的服务器。

Aiohttp 是一个构建在 Python 异步 I/O 框架 Asyncio 之上的开源库，用于处理大量并发 HTTP 请求，而无需传统的基于线程的网络。

2024 年 1 月 28 日，aiohttp 发布了版本 3.9.2，解决了 CVE-2024-23334，这是一个高严重性路径遍历缺陷，影响 3.9.1 及更早版本的所有 aiohttp 版本，允许未经身份验证的远程攻击者访问易受攻击的服务器上的文件。

该缺陷是由于当静态路由的“follow\_symlinks”设置为“True”时验证不充分，从而允许未经授权访问服务器静态根目录之外的文件。

2024 年 2 月 27 日，一名研究人员在 GitHub 上发布了 CVE-2024-23334 的概念验证 (PoC) 漏洞利用，并于 3 月初在 YouTube 上发布了展示分步利用说明的详细视频。

Cyble 的威胁分析师报告称，他们的扫描仪从 2 月 29 日开始捕获了针对 CVE-2024-23334 的利用尝试，并以更高的速度持续到 3 月。

关于攻击面，Cyble 的互联网扫描仪 ODIN 显示全球大约有 44,170 个暴露在互联网上的 aiohttp 实例。

无法识别运行在互联网上的实例的版本，因此很难确定易受攻击的 aiohttp 服务器的数量。

黑客利用 Bricks WordPress 网站构建器中的关键 RCE 缺陷。

本文翻译自https://www.bleepingcomputer.com/news/security/hackers-exploit-aiohttp-bug-to-find-vulnerable-networks/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294023](/post/id/294023)

安全KER - 有思想的安全新媒体

本文转载自: https://www.bleepingcomputer.com/news/security/hackers-exploit-aiohttp-bug-to-find-vulnerable-networks/

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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