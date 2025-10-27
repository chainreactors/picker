---
title: 紧急！ViPNet 网络漏洞致政企核心数据面临全面失窃风险
url: https://www.anquanke.com/post/id/306829
source: 安全客-有思想的安全新媒体
date: 2025-04-24
fetch_date: 2025-10-06T22:04:16.997717
---

# 紧急！ViPNet 网络漏洞致政企核心数据面临全面失窃风险

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

# 紧急！ViPNet 网络漏洞致政企核心数据面临全面失窃风险

阅读量**58096**

发布时间 : 2025-04-23 14:48:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/sophisticated-backdoor-attack-targets-vipnet-networks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Backdoor ViPNet]()

在最近的一起网络安全事件中，一种针对俄罗斯大型组织的复杂后门程序被揭露。受影响的领域包括政府、金融和工业部门。Kaspersky Labs 在调查攻击的同时，已经发布了初步调查结果，以帮助处于风险中的组织采取防护措施。

调查发现，该后门程序的攻击目标是连接到 ViPNet 网络的计算机。ViPNet 是一套用于创建安全网络的软件套件。其传播方式涉及 LZH 格式的压缩档案，这些档案被精心伪装成合法的软件更新。这些档案中包含多种文件，有 “action.inf：文本文件”、“lumpdiag.exe：合法可执行文件”、“msinfo32.exe：小型恶意可执行文件” 以及 “包含有效载荷的加密文件”。ViPNet 的开发者已确认了这些针对性攻击，并已为其用户提供了安全更新和相关建议。

此次攻击采用了一种巧妙的执行方法。“action.inf” 文本文件中包含一个由 ViPNet 更新服务组件（“itcsrvup64.exe”）处理的操作：

[ACTION]

action=extra\_command

extra\_command=lumpdiag.exe –msconfig

这条命令会使用 “–msconfig” 参数来启动合法文件 “lumpdiag.exe”。然而，“lumpdiag.exe” 存在路径替换漏洞，这使得攻击者能够执行恶意文件 “msinfo32.exe”。

“msinfo32.exe” 文件充当了加载器的角色，它会对后门程序进行解密并将其加载到内存中。这个后门程序能够通过传输控制协议（TCP）连接到命令与控制（C2）服务器，使攻击者能够窃取文件并启动更多恶意组件。Kaspersky 的解决方案将这种威胁检测为 HEUR:Trojan.Win32.Loader.gen。

Kaspersky Labs 强调，网络攻击正变得日益复杂。“攻击者可以以极不寻常且出人意料的方式针对组织发起攻击”，这凸显了采用多层纵深防御安全策略的必要性。

本文翻译自securityonline [原文链接](https://securityonline.info/sophisticated-backdoor-attack-targets-vipnet-networks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306829](/post/id/306829)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sophisticated-backdoor-attack-targets-vipnet-networks/)

如若转载,请注明出处： <https://securityonline.info/sophisticated-backdoor-attack-targets-vipnet-networks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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