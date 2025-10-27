---
title: PyPI 恶意包对 MEXC 交易 API 发动攻击，订单重定向与凭证失窃风险骤升
url: https://www.anquanke.com/post/id/306594
source: 安全客-有思想的安全新媒体
date: 2025-04-17
fetch_date: 2025-10-06T22:02:46.996282
---

# PyPI 恶意包对 MEXC 交易 API 发动攻击，订单重定向与凭证失窃风险骤升

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

# PyPI 恶意包对 MEXC 交易 API 发动攻击，订单重定向与凭证失窃风险骤升

阅读量**56027**

发布时间 : 2025-04-16 11:25:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员披露，有一个恶意软件包被上传至 Python 软件包索引（PyPI）存储库，其设计目的是将在 MEXC 加密货币交易所下达的交易订单重定向到一个恶意服务器，并窃取加密代币。

这个名为 ccxt-mexc-futures 的软件包声称是在一个名为 ccxt（即 “加密货币交易” 的英文缩写）的流行 Python 库基础上构建的扩展。ccxt 库用于连接多个加密货币交易所并进行交易，同时还能为支付处理服务提供便利。

目前，这个恶意软件包已从 PyPI 上移除，但 pepy.tech 网站上的统计数据显示，它至少已被下载了 1065 次。

JFrog 的研究人员 Guy Korolevski 在与 The Hacker News 分享的一份报告中表示：“恶意软件包 ccxt-mexc-futures 的作者在其 README 文件中声称，该软件包扩展了 CCXT 库，以支持在 MEXC 上进行‘期货’交易。”

然而，对该库的深入检查发现，它专门覆盖了与 MEXC 接口相关的两个应用程序编程接口（API）——contract\_private\_post\_order\_submit 和 contract\_private\_post\_order\_cancel，并引入了一个名为 spot4\_private\_post\_order\_place 的新 API。

这样做的意图是诱使开发人员调用这些 API 端点，以便在 MEXC 交易所创建、取消或下达交易订单，同时在后台秘密执行恶意操作。

这些恶意修改特别针对原始 ccxt 库中与 MEXC 相关的三个不同函数，即 describe、sign 和 prepare\_request\_headers。

这使得在安装了该软件包的本地机器上执行任意代码成为可能，它能有效地从一个冒充 MEXC 的虚假域名（“v3.mexc.workers [.] dev”）获取一个 JSON 负载，该负载包含一种配置，可将被覆盖的 API 定向到一个恶意的第三方平台（“greentreeone [.] com”），而非实际的 MEXC 网站。

Korolevski 说：“这个软件包使用一个 API 创建了与 MEXC 集成的 API 条目，而该 API 将请求定向到域名 greentreeone [.] com，而不是 MEXC 网站mexc.com。”

“所有请求都被重定向到攻击者设置的域名，这使他们能够劫持受害者在请求中传输的所有加密代币以及包括 API 密钥和机密信息在内的敏感信息。”

此外，这个欺诈性软件包被设计为，每当发送创建、取消或下达订单的请求时，就将 MEXC 的 API 密钥和机密密钥发送到攻击者控制的域名。

建议已安装 ccxt-mexc-futures 软件包的用户立即撤销任何可能已遭泄露的代币，并移除该软件包。

这一事件发生之际，Socket 披露，威胁行为者正在利用 npm、PyPI、Go 和 Maven 生态系统中的假冒软件包来启动一个反向 shell，以维持对系统的控制并窃取数据。

这家软件供应链安全公司表示：“毫无防备的开发人员或组织可能会在无意中将漏洞或恶意依赖项纳入他们的代码库中，如果未能检测到，这可能会导致敏感数据泄露或系统遭到破坏。”

此前还有一项新的研究，深入探讨了为生成式人工智能（AI）工具提供支持的大语言模型（LLM）如何通过 “幻想” 出不存在的软件包并将其推荐给开发人员，从而危及软件供应链安全。

当恶意行为者以这些 “幻想” 出来的名称注册并发布含有恶意软件的软件包到开源存储库时，供应链威胁就会显现，在此过程中感染开发人员的系统 —— 这种技术被称为 “仿冒域名攻击（slopsquatting）”。

这项学术研究发现，“对于商业模型来说，‘幻想’出来的软件包的平均比例至少为 5.2%，而对于开源模型来说则为 21.7%，其中包括令人震惊的 205474 个独特的‘幻想’软件包名称示例，这进一步凸显了这种威胁的严重性和普遍性。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306594](/post/id/306594)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html)

如若转载,请注明出处： <https://thehackernews.com/2025/04/malicious-pypi-package-targets-mexc.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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