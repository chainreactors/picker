---
title: Microsoft 警告：Node.js 恶意广告肆虐，加密交易用户信息安全告急
url: https://www.anquanke.com/post/id/306681
source: 安全客-有思想的安全新媒体
date: 2025-04-19
fetch_date: 2025-10-06T22:05:15.727318
---

# Microsoft 警告：Node.js 恶意广告肆虐，加密交易用户信息安全告急

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

# Microsoft 警告：Node.js 恶意广告肆虐，加密交易用户信息安全告急

阅读量**62754**

发布时间 : 2025-04-18 14:36:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/176651/hacking/node-js-malvertising-campaign-targets-crypto-users.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Microsoft 发出警告，称存在一场恶意广告活动，该活动利用 Node.js 通过诸如 Binance 和 TradingView 等虚假的加密货币交易网站来传播窃取信息的恶意软件。

自 2024 年 10 月以来，Microsoft 已观察到 Node.js 在恶意软件活动中被越来越多地使用，其中包括截至 2025 年 4 月仍在持续的以加密货币为主题的恶意广告攻击。

威胁行为者正越来越多地使用 Node.js 来部署恶意软件，逐渐从传统的脚本语言（如 Python 或 PHP）转移。Node.js 使攻击者能够将恶意代码与合法应用程序相融合，绕过安全工具，并在系统中持续驻留。Node.js 是一个开源的跨平台 JavaScript 运行时环境，它允许 JavaScript 代码在 Web 浏览器之外运行。尽管如今基于 Node.js 的威胁还不那么常见，但它们正成为不断演变的攻击格局中一个值得关注的部分。

在 4 月的 Node.js 攻击事件中，威胁行为者利用恶意广告将用户引诱至虚假网站，这些网站提供伪装成合法软件的恶意安装程序。一旦安装程序被执行，它就会释放出一个恶意 DLL（“CustomActions.dll”），该 DLL 通过 Windows 管理规范（WMI）收集系统数据，通过计划任务确保恶意软件能够持续运行，并使用 PowerShell 命令来逃避防御机制并进一步传递有效载荷。

然后，该 DLL 会通过打开一个 msedge\_proxy 窗口来启动一个诱饵程序，该窗口会显示一个合法的加密货币交易网站。

Microsoft 发布的报告中写道：“所创建的计划任务会运行 PowerShell 命令，这些命令旨在将 PowerShell 进程和当前目录排除在 Microsoft Defender for Endpoint 的扫描范围之外。这一操作可防止后续的 PowerShell 执行被标记，从而使攻击能够不受干扰地继续进行。”

这次攻击使用了经过混淆处理的 PowerShell 脚本，从远程 URL 获取代码，收集详细的系统和基本输入输出系统（BIOS）信息，将其打包为 JSON 格式，然后发送给攻击者的命令与控制（C2）服务器。

在这次攻击的阶段中，一个 PowerShell 脚本会从命令与控制服务器下载一个存档文件，其中包含 Node.js 运行时和一个已编译的 JavaScript 文件。Node.js 可执行文件会运行该脚本，该脚本会建立网络连接，并且很可能会提取敏感的浏览器数据。

![]()

研究人员在近期的攻击活动中观察到的另一个值得注意的技术是，通过 Node.js 执行内联 JavaScript 代码来部署恶意有效载荷。在一个有记录的案例中，攻击者使用了 ClickFix 这种社会工程策略，诱骗用户运行一个 PowerShell 命令，该命令会下载并安装 Node.js 组件。然后，该脚本会通过 Node.js 直接执行 JavaScript 代码，从而实现网络侦察，将命令与控制流量伪装成合法的 Cloudflare 活动，并通过修改注册表启动项来实现持续驻留。

Microsoft 还提供了一系列建议，以减轻因 Node.js 被滥用而带来的威胁。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/176651/hacking/node-js-malvertising-campaign-targets-crypto-users.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306681](/post/id/306681)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/176651/hacking/node-js-malvertising-campaign-targets-crypto-users.html)

如若转载,请注明出处： <https://securityaffairs.com/176651/hacking/node-js-malvertising-campaign-targets-crypto-users.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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