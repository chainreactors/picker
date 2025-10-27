---
title: xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标
url: https://www.anquanke.com/post/id/306953
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:19.443897
---

# xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标

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

# xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标

阅读量**100025**

发布时间 : 2025-04-28 10:29:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html>

译文仅供参考，具体内容表达以及含义原文为准。

Ripple 加密货币的 npm JavaScript 库 xrpl.js 已被未知的威胁行为者入侵，这是一场旨在获取和窃取用户私钥的软件供应链攻击的一部分。

已发现恶意活动影响了该软件包的五个不同版本：4.2.1、4.2.2、4.2.3、4.2.4 和 2.14.2。此问题已在 4.2.5 和 2.14.3 版本中得到解决。

xrpl.js 是一个流行的 JavaScript 应用程序编程接口（API），用于与 XRP 账本区块链（也称为瑞波协议）进行交互，该区块链是瑞波实验室（Ripple Labs）于 2012 年推出的一个加密货币平台。迄今为止，该软件包的下载量已超过 290 万次，每周吸引超过 13.5 万次下载。

合气道安全公司（Aikido Security）的查理・埃里克森（Charlie Eriksen）表示：“官方的 XPRL（瑞波）NPM 软件包被技术精湛的攻击者入侵，他们植入了一个后门程序，以窃取加密货币私钥并获取对加密货币钱包的访问权限。”

已发现恶意代码更改是由一个名为 “mukulljangid” 的用户于 2025 年 4 月 21 日开始引入的，威胁行为者引入了一个名为 checkValidityOfSeed 的新函数，该函数旨在将窃取到的信息传输到一个外部域名（“0x9c [.] xyz”）。

值得注意的是，“mukulljangid” 很可能是瑞波公司的一名员工，这表明他们的 npm 账户被黑客攻击，从而实施了这次供应链攻击。

据说攻击者尝试了不同的方法来偷偷植入后门程序，同时试图逃避检测，短时间内发布的不同版本就证明了这一点。目前没有证据表明相关的 GitHub 存储库也被植入了后门。

尚不清楚这次攻击背后的主使是谁，但据合气道安全公司称，据信威胁行为者设法窃取了开发者的 npm 访问令牌，以便篡改该库。

鉴于这一事件，建议依赖 xrpl.js 库的用户将其使用的版本更新到最新版本（4.2.5 和 2.14.3），以减轻潜在威胁。

XRP 账本基金会在 X 平台（原推特）上的一篇帖子中表示：“此漏洞存在于 xrpl.js 中，这是一个用于与 XRP 账本交互的 JavaScript 库。它不会影响 XRP 账本的代码库或 GitHub 存储库本身。使用 xrpl.js 的项目应立即升级到 v4.2.5 版本。”

****最新消息****

xrpl.js 的供应链被入侵事件已被赋予 CVE 标识符 CVE-2025-32965（通用漏洞评分系统（CVSS）评分为 9.3）。

根据 GitHub 的一则安全公告：“xrpl.js 的 4.2.1、4.2.2、4.2.3 和 4.2.4 版本已被篡改，包含旨在窃取私钥的恶意代码。如果您正在使用这些版本中的任何一个，请立即停止使用，并轮换受影响系统中使用的任何私钥或机密信息。”

“2.14.2 版本也是恶意的，不过由于它与其他 2.x 版本不兼容，被利用的可能性较小。为了确保资金安全，请仔细考虑是否有任何密钥可能已被这次供应链攻击所泄露，并通过将资金转移到安全钱包和 / 或轮换密钥来降低风险。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306953](/post/id/306953)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html)

如若转载,请注明出处： <https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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