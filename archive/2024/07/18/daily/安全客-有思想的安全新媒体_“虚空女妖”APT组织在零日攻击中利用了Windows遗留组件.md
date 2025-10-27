---
title: “虚空女妖”APT组织在零日攻击中利用了Windows遗留组件
url: https://www.anquanke.com/post/id/297999
source: 安全客-有思想的安全新媒体
date: 2024-07-18
fetch_date: 2025-10-06T17:38:37.829579
---

# “虚空女妖”APT组织在零日攻击中利用了Windows遗留组件

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

# “虚空女妖”APT组织在零日攻击中利用了Windows遗留组件

阅读量**75989**

发布时间 : 2024-07-17 12:33:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/07/16/cve-2024-38112-void-banshee/>

译文仅供参考，具体内容表达以及含义原文为准。

用于利用 CVE-2024-38112（最近修补的 Windows MSHTML 漏洞）的零日漏洞被一个名为 Void Banshee 的 APT 组织利用，向北美、欧洲和东南亚的目标提供恶意软件，趋势科技的 Zero Day Initiative 威胁猎人分享。

### Void Banshee 如何使用 CVE-2024-38112

正如Check Point研究员Haifei Li之前所解释的那样，攻击者使用了专门为利用该漏洞而精心制作的文件，但看起来像PDF。

“威胁行为者利用 CVE-2024-38112 通过互联网快捷方式 （URL） 文件滥用 MHTML 协议处理程序和 x-usc 指令来执行恶意代码。使用这种技术，威胁行为者能够直接通过 Windows 计算机上禁用的 Internet Explorer 实例访问和运行文件，“趋势科技研究人员指出。

[![]()](https://helpnet.link/4d2df8)

“这个MHTML代码执行漏洞被用来用[Atlantida恶意软件](https://www.rapid7.com/blog/post/2024/01/17/whispers-of-atlantida-safeguarding-your-digital-treasure/)感染用户和组织。”

攻击链（来源：趋势科技）

威胁行为者使用鱼叉式网络钓鱼策略将目标定向到包含 PDF 格式书籍副本的 ZIP 文件，以及伪装成 PDF 的恶意文件。ZIP 文件托管在在线图书馆、云共享网站、Discord 和受感染的网站上。

“我们在分析虚空女妖活动时发现的一些PDF诱饵包括教科书和参考资料，如临床解剖学，这表明该活动针对的是经常使用参考资料的高技能专业人士和学生，以及收集书籍数字副本的地方，”威胁猎人说。

受害者以为他们正在打开 PDF 文件，但实际上正在执行一个互联网快捷方式文件，该文件利用漏洞触发 Internet Explorer 浏览器的残余物，导致托管恶意 HTML 应用程序的受感染网站。

HTA 文件包含一个 Visual Basic 脚本，该脚本使用 PowerShell 下载并执行它，为其创建新进程，下载其他特洛伊木马加载程序，最后交付 Atlantida 窃取程序。

“[窃取者]针对来自各种应用程序的敏感信息，包括 Telegram、Steam、FileZilla、各种加密货币钱包和网络浏览器。他们指出，这种恶意软件专注于提取存储的敏感和潜在有价值的数据，例如密码和 cookie，它还可以从受感染系统的桌面上收集具有特定扩展名的文件。

“此外，恶意软件会捕获受害者的屏幕并收集全面的系统信息。然后，被盗数据被压缩成ZIP文件，并通过TCP传输给攻击者。

根据 Check Point 的说法，Void Banshee 利用 CVE-2024-38112 已经一年多了。

“像 Void Banshee 这样的 APT 组织利用 IE 等禁用服务的能力对全球组织构成了重大威胁，”趋势科技威胁猎人指出。

“由于IE等服务具有较大的攻击面，并且不再接收补丁，因此对Windows用户来说是一个严重的安全问题。此外，威胁行为者访问不受支持和禁用的系统服务以规避现代网络沙箱（例如 Microsoft Edge 的 IE 模式）的能力凸显了行业的一个重大问题。

### Microsoft 未能协调漏洞披露

Check Point 和 Trend Micro 研究人员都在 2024 年 5 月中旬注意到 CVE-2024-38112 被利用，并向 Microsoft 披露了他们的发现。Microsoft 在 2024 年 7 月的周二补丁中发布了针对该漏洞的修复程序，使 MHTML 无法再在互联网快捷方式文件 （.url） 中使用，并将前者归功于该漏洞的安全公告。

但是，当Microsoft在没有提醒的情况下发布修复程序时，两家公司都感到惊讶。

“这不是 [Microsoft] 第一次告诉我们他们将在 X 月修补该问题，但在没有通知我们的情况下提前发布了补丁，”李说，并指出“协调披露不能只是单方面的协调。

ZDI威胁意识负责人达斯汀·柴尔兹（Dustin Childs）指出了研究人员抱怨Microsoft缺乏沟通的其他例子，并指出，使协调漏洞披露（CVD）过程对研究人员来说令人沮丧可能会对Microsoft产生负面影响。

“如果你不提供赏金，不与研究人员协调或适当地归功于他们，为什么世界上会有人向你报告错误？”他问道。

他指出，为了让协调的漏洞披露发挥作用，双方——供应商和研究人员——都负有一定的责任，“现在是时候让供应商站出来做他们的工作了。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/07/16/cve-2024-38112-void-banshee/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297999](/post/id/297999)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/07/16/cve-2024-38112-void-banshee/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/07/16/cve-2024-38112-void-banshee/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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