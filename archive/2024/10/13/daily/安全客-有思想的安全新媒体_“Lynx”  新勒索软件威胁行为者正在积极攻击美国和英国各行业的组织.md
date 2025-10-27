---
title: “Lynx”  新勒索软件威胁行为者正在积极攻击美国和英国各行业的组织
url: https://www.anquanke.com/post/id/300789
source: 安全客-有思想的安全新媒体
date: 2024-10-13
fetch_date: 2025-10-06T18:47:00.863352
---

# “Lynx”  新勒索软件威胁行为者正在积极攻击美国和英国各行业的组织

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

# “Lynx” 新勒索软件威胁行为者正在积极攻击美国和英国各行业的组织

阅读量**63912**

发布时间 : 2024-10-12 10:56:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/lynx-ransomware-the-evolution-of-inc-ransomware-into-a-potent-cyber-threat/>

译文仅供参考，具体内容表达以及含义原文为准。

Palo Alto Networks 发现了一种名为 “Lynx ”的新型勒索软件威胁行为体，它正积极瞄准美国和英国各行各业的组织。不过，这种新的恶意软件并不是全新的；事实上，它是 2023 年 8 月出现的 INC 勒索软件家族的改版。

自出现以来，Lynx勒索软件已经掀起了波澜，其攻击目标涉及零售、房地产、建筑和金融服务等多个领域。该变种以 “勒索软件即服务”（RaaS）的方式运行，因此其他网络犯罪分子也可以在其攻击中部署该变种。Lynx 勒索软件背后的恶意行为者采用了复杂的技术，包括双重勒索策略，即在加密受害者数据之前先将其流出。如果不支付赎金，被盗数据可能会泄露或在暗网上出售。

Lynx 勒索软件的血统可以直接追溯到 INC 勒索软件，估计有 48% 的代码与之共享。使用开源工具 BinDiff 对这两种恶意软件进行比较，证实了两者的相似性。Palo Alto Networks 发现，许多核心功能（约 70.8%）被重复使用，这表明 Lynx 开发人员严重依赖 INC 的代码库。

![]()
BinDiff 显示的 INC 和 Lynx 勒索软件代码相似性 | 图片： Palo Alto Networks

这种对已有勒索软件代码的依赖在网络犯罪领域并不罕见。正如报告所指出的，“通过利用已有代码并在其他成功勒索软件打下的基础上继续发展，威胁行为者可以节省时间和资源”，从而更快、更有效地发起攻击。这种代码的重复使用导致了勒索软件家族的迅速扩散，随着地下市场上源代码的增多，这种趋势很可能会继续下去。

Lynx 勒索软件最危险的一点是它实施双重勒索。受害者不仅要面对被加密的文件，还要面临敏感数据被暴露的风险。Lynx 背后的组织声称已经入侵了许多公司，并将窃取的数据显示在公共网站上。虽然他们声称自己避开政府机构、医院和非营利组织，但他们的攻击仍对许多行业构成重大威胁。

Palo Alto Networks 强调了 Lynx 勒索软件的广泛部署途径，包括网络钓鱼电子邮件、恶意下载和黑客论坛上的资源共享。因此，企业在防御这些多方面威胁时必须保持警惕。

对Lynx勒索软件的技术分析表明，它使用了先进的加密算法，包括CTR模式下的AES-128和Curve25519 Donna，这使得它在不支付赎金的情况下解密异常困难。该勒索软件专门针对 Windows 系统，据观察，它使用重启管理器 API (RstrtMgr) 来提高加密效率，Conti 和 Cactus 等其他臭名昭著的勒索软件家族也使用了这种技术。

此外，Lynx勒索软件在设计时考虑到了灵活性，允许攻击者通过各种命令行参数自定义执行方式。这样，攻击者就能根据自己的具体需求定制攻击，无论是加密特定目录、网络驱动器还是服务。

![]()
恶意软件中的命令行选项 | 图片： Palo Alto Networks

Lynx 勒索软件的出现凸显了网络威胁不断演变的本质。企业需要保持警惕并积极采取网络安全措施，以降低此类威胁带来的风险。

本文翻译自securityonline [原文链接](https://securityonline.info/lynx-ransomware-the-evolution-of-inc-ransomware-into-a-potent-cyber-threat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300789](/post/id/300789)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/lynx-ransomware-the-evolution-of-inc-ransomware-into-a-potent-cyber-threat/)

如若转载,请注明出处： <https://securityonline.info/lynx-ransomware-the-evolution-of-inc-ransomware-into-a-potent-cyber-threat/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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