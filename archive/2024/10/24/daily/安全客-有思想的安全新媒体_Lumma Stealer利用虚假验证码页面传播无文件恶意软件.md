---
title: Lumma Stealer利用虚假验证码页面传播无文件恶意软件
url: https://www.anquanke.com/post/id/301189
source: 安全客-有思想的安全新媒体
date: 2024-10-24
fetch_date: 2025-10-06T18:46:08.483654
---

# Lumma Stealer利用虚假验证码页面传播无文件恶意软件

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

# Lumma Stealer利用虚假验证码页面传播无文件恶意软件

阅读量**98351**

发布时间 : 2024-10-23 16:05:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/fake-captcha-pages-lumma-stealer-fileless-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![Fake CAPTCHA Pages Used by Lumma Stealer to Spread Fileless Malware]()

**Lumma Stealer 恶意软件使用伪造的验证码欺骗受害者。这种窃取信息的恶意软件以密码和加密货币详细信息等敏感数据为目标。**

Qualys 威胁研究部门（TRU）发现，通过恶意软件即服务（MaaS）模式提供的恶意软件 Lumma Stealer 在欺骗用户的手段上有了很大的改进。

Qualys与Hackread.com分享了它的发现，该发现涉及一个活跃的Lumma Stealer活动，它使用虚假的验证码页面诱骗用户执行持久性有效载荷。该攻击使用多级无文件技术，具有欺骗性和持久性。

**虚假验证码验证**

Qualys TRU 解释说，用户通常通过被破解的合法软件或面向公众的应用程序被诱骗到虚假验证码验证页面。点击 “我不是机器人 ”按钮会触发一个恶意 PowerShell 命令，该命令会将一个初始暂存器（恶意软件下载器）下载到目标计算机上。下载的有效载荷是一个精心制作的 PE 文件，其中嵌入了混淆的 JavaScript 代码。

点击验证按钮会触发下载 Base64 编码的 PowerShell 脚本。该脚本利用可信的 Windows 工具 “mshta.exe ”下载伪装成合法 Windows 工具 “Dialer.exe ”的远程有效负载。下载的有效载荷是一个精心制作的 PE 文件，其中嵌入了混淆的 JavaScript 代码。

有趣的是，嵌入的脚本使用了一种名为 polyglot 的技术，即在可执行文件中隐藏有效的 HTA 内容。触发后，脚本会使用 PowerShell 下载并执行另一个混淆 JavaScript 代码。该脚本会解密最终有效载荷，并下载包含实际 Lumma Stealer 可执行文件（Vectirfree.exe）的两个压缩包。

**信息收集和规避技术**

Vectirfree.exe采用恶意软件常用的 “进程空洞化 ”策略，将恶意代码注入到 “BitLockerToGo.exe ”等合法程序中。 恶意软件会在临时目录中放置 “Killing.bat ”和 “Voyuer.pif ”等文件，检查并终止杀毒软件进程，以逃避检测。

在攻击的下一阶段，Lumma Stealer 会搜索与加密货币和密码相关的敏感文件和数据。窃取的数据会被发送到命令和控制 (C2) 服务器，通常使用“.shop ”顶级域，以外泄窃取的数据。

![Fake CAPTCHA Pages Used by Lumma Stealer to Spread Fileless Malware]()
Lumma Stealer 是一种无文件恶意软件，可直接在内存中执行，不会创建永久文件。它的目标是密码、浏览器信息和加密货币钱包详细信息等敏感数据。通过使用多语言和混淆脚本等技术来阻碍分析，并通过进程空洞化将其恶意活动隐藏在合法进程中，该恶意软件将自己表现为一种持续性威胁。

研究人员在报告中指出：“我们对其感染链的分析强调了无文件恶意软件如何利用 PowerShell 和 mshta.exe 等常用工具，以及嵌入式有效载荷和进程注入在其运行中的关键作用。”

通过了解 Lumma Stealer 的攻击过程并实施强大的安全措施，企业可以有效地防范这种不断演变的威胁。

本文翻译自hackread [原文链接](https://hackread.com/fake-captcha-pages-lumma-stealer-fileless-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301189](/post/id/301189)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-captcha-pages-lumma-stealer-fileless-malware/)

如若转载,请注明出处： <https://hackread.com/fake-captcha-pages-lumma-stealer-fileless-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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