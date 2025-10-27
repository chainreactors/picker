---
title: 研究人员发现威胁行为者使用多年的 MotW 绕过技术
url: https://www.anquanke.com/post/id/298906
source: 安全客-有思想的安全新媒体
date: 2024-08-08
fetch_date: 2025-10-06T17:59:28.213197
---

# 研究人员发现威胁行为者使用多年的 MotW 绕过技术

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

# 研究人员发现威胁行为者使用多年的 MotW 绕过技术

阅读量**80891**

发布时间 : 2024-08-07 15:40:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/08/06/motw-bypass-lnk-stomping/>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者一直在滥用 Windows 如何处理具有非标准目标路径和内部结构的 LNK 文件的错误，以防止内置保护阻止恶意负载并诱骗用户运行它们。

“我们在VirusTotal中发现了多个样本，这些样本表现出该漏洞，表明存在野外使用。已确定的最早样本是在 6 年前提交的，“Elastic Security Labs 研究人员发现。

### Windows 的内置保护

攻击者不断想出新的方法来绕过 Microsoft 的防御措施，包括 SmartScreen 和 Smart App Control （SAC） 。

SmartScreen 是一种较旧的安全功能，旨在保护 Windows 用户免受从 Internet 或受限制站点下载的潜在恶意网页和文件的侵害。

前者是根据报告的网络钓鱼站点和恶意软件站点的动态列表进行检查的，而后者默认情况下会向其添加 Web 标记 （MotW） 元数据，SmartScreen 会根据已知可执行文件的允许列表进行检查。如果未列出该文件，SmartScreen 将阻止执行该文件并显示警告。如果企业管理员尚未设置策略来阻止他们这样做，则用户可以覆盖警告并继续操作。

Microsoft （Defender） SmartScreen 根据允许列表检查标有 MOTW 的文件。如果未列出该文件，SmartScreen 会提醒用户该文件是未知的，并阻止它执行，除非用户坚持运行它。

同样，较新的智能应用控制 （SAC） 会根据已知安全应用列表检查用户想要运行的应用。 “[SAC] 的工作原理是在执行应用程序时查询 Microsoft 云服务。如果已知它们是安全的，则允许它们执行;但是，如果它们是未知的，则只有在它们具有有效的代码签名时才会执行它们。启用 SAC 后，它会替换和禁用 Defender SmartScreen，“研究人员解释说。

### LNK 踩踏 = 简单的 MotW 旁路

攻击者通过使用有效的代码签名证书对恶意软件进行签名，重新利用具有良好声誉的应用程序，或者找到使二进制文件看起来是良性的，以便将它们添加到已知的安全应用程序列表中，从而绕过这些保护措施。

这项最新技术被研究人员命名为“LNK stomping”，它允许攻击者通过制作 LNK（即 Windows 快捷方式）文件来绕过 Web 标记 （MOTW） 控制，使它们具有非标准的目标路径或内部结构。

此类文件强制 Windows 规范化/“修复”路径/结构，从而“重写”文件并删除 MotW 元数据。如果没有它，SmartScreen 和 SAC 将认为文件是安全的，并在不发出警告的情况下运行它。

“这个问题最简单的演示是在目标可执行文件路径（例如，*powershell.exe.*）后附加一个点或空格。或者，可以创建一个包含相对路径的 LNK 文件*，例如 .\target.exe，“*他们解释说。“另一种变体涉及在 LNK 目标路径阵列的单个条目中制作多级路径。”

研究人员已经向Microsoft安全响应中心披露了该错误的详细信息，该中心显然表示可能会在未来的Windows更新中修复该漏洞。

不过，与此同时，他们敦促安全团队“仔细审查其检测堆栈中的下载内容，而不是仅仅依赖操作系统原生安全功能来提供该领域的保护。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/08/06/motw-bypass-lnk-stomping/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298906](/post/id/298906)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/08/06/motw-bypass-lnk-stomping/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/08/06/motw-bypass-lnk-stomping/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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