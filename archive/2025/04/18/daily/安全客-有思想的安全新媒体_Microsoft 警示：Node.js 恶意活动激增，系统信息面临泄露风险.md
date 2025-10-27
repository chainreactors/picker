---
title: Microsoft 警示：Node.js 恶意活动激增，系统信息面临泄露风险
url: https://www.anquanke.com/post/id/306628
source: 安全客-有思想的安全新媒体
date: 2025-04-18
fetch_date: 2025-10-06T22:02:48.566874
---

# Microsoft 警示：Node.js 恶意活动激增，系统信息面临泄露风险

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

# Microsoft 警示：Node.js 恶意活动激增，系统信息面临泄露风险

阅读量**71047**

发布时间 : 2025-04-17 11:17:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/node-js-misused-in-malvertising-campaigns-to-deliver-stealthy-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Node.js malware, malvertising attacks]()

Microsoft Defender 专家（DEX）观察到，利用 Node.js 来传播恶意软件和其他有害有效载荷的恶意活动有所增加。这些恶意活动旨在从受攻击的系统中窃取信息并泄露数据。

尽管像 Python 和 PHP 这样的传统脚本语言仍然是攻击者常用的工具，但现在存在一种日益增长的趋势，即利用已编译的 JavaScript 或直接在命令行中使用 Node.js 运行脚本。

Node.js 是开发者构建 Web 应用程序时的可靠工具，但其优势 —— 跨平台兼容性、无需浏览器即可执行以及能够访问系统资源，同样对攻击者具有吸引力。

报告指出：“威胁行为者也在利用 Node.js 的这些特性，试图将恶意软件与合法应用程序混为一体，绕过传统的安全控制措施，并在目标环境中持续存在。”

Microsoft 发现了一场针对 Binance 和 TradingView 等加密货币平台用户的活跃恶意广告活动。受害者会被虚假广告诱骗下载恶意安装程序，该安装程序会部署一个基于 Node.js 的恶意软件链条。

攻击链条包括：

1.由 Wix 构建的安装程序下载恶意的 CustomActions.dll。

2.该 DLL 使用 Windows 管理规范（WMI）查询来收集系统信息，并创建一个计划的 PowerShell 任务以实现持续控制。

3.与此同时，一个虚假的浏览器窗口会打开一个合法的加密货币网站来分散用户的注意力。

一旦计划好 PowerShell 命令，它会：

1.将 PowerShell 进程和目录排除在 Microsoft Defender 的扫描范围之外。

2.启动经过混淆处理的脚本，从远程服务器获取更多命令。

3.收集大量的系统、基本输入输出系统（BIOS）和操作系统信息。

4.通过 HTTP POST 以 JSON 格式构建并泄露数据。

最后阶段包括下载并启动：

1.Node.js 运行时（node.exe）

2.一个已编译的 JavaScript 文件（JSC）

3.支持的库模块

一旦恶意软件被执行，它会：

1.加载额外的模块

2.建立网络连接

3.安装证书

4.窃取浏览器凭据和敏感数据

这些行为与传统的凭据窃取和间谍活动策略一致，只不过现在是通过 JavaScript 和 Node.js 来实施的。

Microsoft发现的一种新出现的策略涉及直接从 PowerShell 内联执行 JavaScript，从而完全绕过基于文件的检测。

![]()

恶意脚本摘录，突出显示了硬编码的命令与控制（C2）服务器 | 图片来源：Microsoft

在一次名为 ClickFix 的社会工程攻击活动中，用户被诱骗执行 PowerShell 命令，这些命令会：

1.下载 Node.js

2.通过内联命令执行 JavaScript

3.进行域名侦察

4.将流量伪装成 Cloudflare 的活动

如今，攻击者能够轻松地将强大的 JavaScript 逻辑嵌入日常脚本中，这意味着防御者必须领先一步 —— 不仅要在浏览器层面，还要在shell层面做好防范。

本文翻译自securityonline [原文链接](https://securityonline.info/node-js-misused-in-malvertising-campaigns-to-deliver-stealthy-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306628](/post/id/306628)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/node-js-misused-in-malvertising-campaigns-to-deliver-stealthy-malware/)

如若转载,请注明出处： <https://securityonline.info/node-js-misused-in-malvertising-campaigns-to-deliver-stealthy-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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