---
title: 新的攻击显示浏览器允许网站访问GPU存在风险
url: https://www.anquanke.com/post/id/294088
source: 安全客-有思想的安全新媒体
date: 2024-03-20
fetch_date: 2025-10-04T12:09:31.608617
---

# 新的攻击显示浏览器允许网站访问GPU存在风险

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

# 新的攻击显示浏览器允许网站访问GPU存在风险

阅读量**84070**

发布时间 : 2024-03-19 11:06:11

**x**

##### 译文声明

本文是翻译文章，文章来源：https://www.securityweek.com/new-attack-shows-risks-of-browsers-giving-websites-access-to-gpu/

译文仅供参考，具体内容表达以及含义原文为准。

来自奥地利格拉茨科技大学和法国雷恩大学的研究人员团队展示了一种新的图形处理单元 (GPU) 攻击，该攻击会影响多种流行的浏览器和显卡。

该研究重点关注 WebGPU，这是一种 API，使 Web 开发人员能够使用底层系统的 GPU 在 Web 浏览器中执行高性能计算。通过利用此 API，他们演示了一种完全通过使用 JavaScript 从 Web 浏览器进行的攻击。这使得远程执行变得更加容易，但与之前需要访问本机 GPU API 的攻击相比，也限制了潜在影响。

学术研究人员将他们的工作描述为来自浏览器内的首批 GPU 缓存侧通道攻击之一。展示了如何利用该方法进行远程攻击，方法是让目标用户访问托管恶意 WebGPU 代码的网站，并在执行漏洞利用时在该网站上停留几分钟。

例如，当受害者正在阅读恶意网站上的文章时，可以执行该漏洞利用。进行攻击不需要其他类型的用户交互。

专家证明，这种新方法可用于击键间计时攻击，从而可以根据击键计时数据推断密码等敏感信息。它还可用于在几分钟内获取基于 GPU 的 AES 加密密钥，以及传输速率高达 10 Kb/s 的隐蔽数据泄露通道。

研究人员指出：“我们的工作强调，浏览器供应商需要像对待其他安全和隐私相关资源一样对待对 GPU 的访问。”

参与该项目的研究人员之一卢卡斯·吉纳 (Lukas Giner) 告诉《安全周刊》，虽然他们展示的攻击并不是“非常强大”，但它们确实展示了浏览器在未经明确请求许可的情况下允许任何网站访问主机系统显卡所带来的潜在风险。

“这可能会导致像我们这样的秘密攻击（或者将来可能会发生更严重的攻击），或者网站只是使用 GPU 进行加密货币挖掘等操作，而用户却完全不知情，”Giner 解释道。

该研究针对 11 种桌面显卡：其中 2 款来自 AMD 的 RX 系列产品，以及 9 款来自 NVIDIA 的 GTX、RTX 和 Quadro 系列产品。该攻击针对支持 WebGPU 的浏览器，包括 Chrome、Chromium、Edge 和 Firefox Nightly。

“通过针对网络浏览器，我们的威胁模型包括浏览器在处理敏感信息时可能运行的任何场景。由于整个系统通常共享 GPU，因此这可以包括渲染的任何内容（例如网站或应用程序）和通用计算操作，”研究人员在详细介绍其工作的 论文中写道。

Mozilla、AMD、NVIDIA 和 Chromium 开发人员已收到通知。AMD 发布了一份咨询报告，表示“研究人员并未证明任何针对 AMD 产品的利用”。

研究人员表示，其他公司也不打算采取任何行动。

吉纳说，他们建议在浏览器中弹出一个权限弹出窗口，例如请求访问麦克风或摄像头的窗口。然而，Chromium 团队表示，他们发现，要求用户做出他们不理解其含义的安全决策会增加摩擦，而不会让他们更安全。

一个小型的概念验证 ( PoC ) 已经推出。它显示WebGPU是否可用并在浏览器中进行无害的攻击。

\*更新以改写 Chromium 团队的回复。还更新了第三段，以澄清这是来自浏览器内的第一个 GPU 缓存侧通道攻击，而不是此类攻击的“第一个”攻击。这是撰写论文时的第一次攻击，但此后其他人针对不同的目标进行了类似的研究。

本文翻译自https://www.securityweek.com/new-attack-shows-risks-of-browsers-giving-websites-access-to-gpu/ 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294088](/post/id/294088)

安全KER - 有思想的安全新媒体

本文转载自: https://www.securityweek.com/new-attack-shows-risks-of-browsers-giving-websites-access-to-gpu/

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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