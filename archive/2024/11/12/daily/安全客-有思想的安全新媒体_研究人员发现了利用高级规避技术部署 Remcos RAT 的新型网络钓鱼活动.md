---
title: 研究人员发现了利用高级规避技术部署 Remcos RAT 的新型网络钓鱼活动
url: https://www.anquanke.com/post/id/301709
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:17.628622
---

# 研究人员发现了利用高级规避技术部署 Remcos RAT 的新型网络钓鱼活动

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

# 研究人员发现了利用高级规避技术部署 Remcos RAT 的新型网络钓鱼活动

阅读量**53217**

发布时间 : 2024-11-11 15:12:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/researcher-uncovers-new-phishing-campaign-deploying-remcos-rat-with-advanced-evasion-techniques/>

译文仅供参考，具体内容表达以及含义原文为准。

![Remcos RAT phishing campaign]()

Fortinet 的 FortiGuard 实验室发现了利用 Remcos RAT（远程管理工具）新变种的复杂网络钓鱼活动。该活动以一封包含恶意 Excel 文档的钓鱼电子邮件开始，该文档利用了 CVE-2017-0199 漏洞，允许攻击者在受害者的设备上远程执行代码。Fortinet 的报告指出：”Remcos 是一种商用 RAT……然而，威胁行为者滥用 Remcos 收集受害者的敏感信息，并远程控制他们的计算机以实施进一步的恶意行为。

一旦打开所附的 Excel 文件，CVE-2017-0199 漏洞就会激活，悄无声息地下载一个 HTA（HTML 应用程序）文件。“HTA文件是一个由Windows本地应用程序（mshta.exe）执行的HTML应用程序文件，”Fortinet的报告详细指出，该文件随后会下载一个名为dllhost.exe的文件到受害者的设备上。该文件用多种语言启动一系列脚本，包括 JavaScript、VBScript 和 PowerShell，以隐藏恶意代码并逃避检测。

![]()

一旦 dllhost.exe 被执行，它就会启动进程空洞化，这是一种将恶意代码注入新创建的进程 Vaccinerende.exe 的技术。该进程会隐藏代码，使其无法被标准监控工具发现。据 Fortinet 称，“恶意代码执行进程空洞化，将自己放入一个新创建的 Vaccinerende.exe 进程中”–这种技术增强了攻击的隐蔽性。为了保持持久性，恶意软件在 Windows 注册表中创建了一个自动运行条目，使其即使在系统重新启动后也能重新激活。

设置完成后，恶意软件会解密并完全在内存中运行 Remcos 有效载荷，从而避免了可能引起怀疑的传统文件存储方式。然后，Remcos RAT 会连接到一个命令与控制（C2）服务器，发送有关受害者系统的数据，如 Fortinet 所描述的 “处理器信息、内存状态、用户权限级别以及 C&C 服务器的 IP 地址”。

Remcos 的功能扩展到一系列间谍和控制功能，从键盘记录和截屏到收集运行进程列表和控制受害者设备上的程序。正如 Fortinet 指出的那样，Remcos 可以执行 “来自服务器的控制命令数据，然后在受害者的设备上执行相应的操作”，这表明了它在各种情况下的适应性。

为了保持隐蔽性，该活动采用了先进的反分析方法，包括定向异常处理、动态 API 调用和反调试技术。Fortinet 强调了 “它如何对多个 API 使用 API 挂钩技术 ”来逃避检测并阻止分析工具监控其行为。

本文翻译自securityonline [原文链接](https://securityonline.info/researcher-uncovers-new-phishing-campaign-deploying-remcos-rat-with-advanced-evasion-techniques/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301709](/post/id/301709)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/researcher-uncovers-new-phishing-campaign-deploying-remcos-rat-with-advanced-evasion-techniques/)

如若转载,请注明出处： <https://securityonline.info/researcher-uncovers-new-phishing-campaign-deploying-remcos-rat-with-advanced-evasion-techniques/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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