---
title: 一款伪装成 NFT 游戏应用程序的恶意软件能绕过 Microsoft Defender 和2FA，窃取了用户价值 2.4 万美元的加密货币
url: https://www.anquanke.com/post/id/302147
source: 安全客-有思想的安全新媒体
date: 2024-11-26
fetch_date: 2025-10-06T19:12:14.385585
---

# 一款伪装成 NFT 游戏应用程序的恶意软件能绕过 Microsoft Defender 和2FA，窃取了用户价值 2.4 万美元的加密货币

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

# 一款伪装成 NFT 游戏应用程序的恶意软件能绕过 Microsoft Defender 和2FA，窃取了用户价值 2.4 万美元的加密货币

阅读量**69988**

发布时间 : 2024-11-25 10:52:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/malware-bypasses-microsoft-defender-2fa-crypto/>

译文仅供参考，具体内容表达以及含义原文为准。

**恶意软件绕过 Microsoft Defender 和 2FA，通过伪造的 NFT 游戏应用程序窃取 2.4 万美元的加密货币。了解它是如何入侵设备并逃避安全防护的。**

SafetyDetectives 的网络安全研究人员发现，默认的 Windows 杀毒软件 Microsoft Defender 被恶意软件欺骗，导致一名毫无戒心的用户的加密货币被盗。这个问题是在分析一个看似无害的 NFT 游戏应用程序时发现的，该应用程序实际上是为了窃取加密货币而设计的。

该应用程序还通过绕过谷歌的双因素身份验证入侵了设备，并窃取了超过 24,000 美元的加密货币。据研究人员称，恶意软件一旦安装，就会在后台悄悄运行，收集敏感信息，甚至可能劫持用户受双因素身份验证（2FA）保护的谷歌账户。它通过安装一个伪装成谷歌 Keep 的恶意 Chrome 扩展程序，绕过 2FA 安全措施来实现这一目的。

在调查过程中，SafetyDetectives 的团队使用 Wireshark 监控网络流量并检测恶意软件的位置，测试了 Microsoft Defender 对恶意软件应用程序的防护能力。

令人惊讶的是，Microsoft Defender 在安装和执行过程中未能阻止病毒，允许恶意软件访问系统操作、下载可疑文件、收集敏感信息，甚至确定用户的位置。

可能是由于恶意软件的来源，如果用户在俄罗斯、乌克兰或白俄罗斯，恶意软件就会被编程为关闭。假冒的 Chrome 浏览器扩展使恶意软件能够访问访问的每个网站、窃取登录数据并监控从浏览器复制的任何内容。病毒收集了远程控制系统所需的一切，而微软卫士却没有发出警报。

**比特梵德和 Malwarebytes 的救援**

为了评估其他防病毒解决方案的有效性，研究小组还测试了 Malwarebytes 和 Bitdefender。虽然这两种杀毒软件都无法阻止最初的安装，但它们确实在攻击的后期阶段进行了干预。Bitdefender 阻止了恶意软件访问关键信息的尝试，而 Malwarebytes 则完全阻止了安装。

“虽然 Malwarebytes 比 Bitdefender 更快地阻止了漏洞的入侵，但在处理这种特定恶意软件方面，二者都没有本质上的优势，因为二者都能阻止关键漏洞的入侵。”他们在博文中解释说：“Bitdefender 的优势甚至在于误报率较低。”

这可能是因为近年来微软Exchange服务器受到了一系列零日漏洞的攻击，其中一些漏洞可能影响了微软Defender保护系统的能力。或者供应链攻击，如 SolarWinds 黑客攻击，会破坏软件更新和工具，从而可能影响 Microsoft Defender 等安全解决方案的完整性。

尽管如此，调查强调了投资更强大的杀毒软件的重要性，以及在下载和安装应用程序时保持谨慎的重要性，尤其是从未经验证的来源下载和安装。随时了解网络威胁并采取积极措施，可以大大降低恶意攻击的风险。

本文翻译自hackread [原文链接](https://hackread.com/malware-bypasses-microsoft-defender-2fa-crypto/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302147](/post/id/302147)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/malware-bypasses-microsoft-defender-2fa-crypto/)

如若转载,请注明出处： <https://hackread.com/malware-bypasses-microsoft-defender-2fa-crypto/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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