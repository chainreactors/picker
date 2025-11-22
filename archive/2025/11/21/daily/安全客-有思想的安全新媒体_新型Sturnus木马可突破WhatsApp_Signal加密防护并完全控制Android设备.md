---
title: 新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备
url: https://www.anquanke.com/post/id/313302
source: 安全客-有思想的安全新媒体
date: 2025-11-21
fetch_date: 2025-11-22T03:06:42.918178
---

# 新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备

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

# 新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备

阅读量**13569**

发布时间 : 2025-11-21 17:51:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/sturnus-trojan-bypasses-whatsapp-signal-encryption-takes-over-android-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

MTI Security 研究人员在移动领域发现了一种复杂的新威胁：**Sturnus**，这是一个私人运营的 Android 银行木马。该恶意软件不仅以金融欺诈为目标，还具备**高级的全设备接管能力**，其关键差异点在于：**能够绕过加密消息**。

Sturnus 最令人担忧的功能是其**可入侵 WhatsApp、Telegram 和 Signal 等平台的通信**。该木马并非尝试破解网络加密，而是利用 **Android 辅助功能（Accessibility Service）** 在合法应用为用户解密后捕获屏幕内容。这使攻击者能直接、实时查看本应私密的对话、联系人以及所有进出消息的内容。

正如 ThreatFabric 的报告所指出，此能力“通过访问合法应用解密后的消息，完全规避了端到端加密，让攻击者直接窥视本应私密的对话”。

该恶意软件专为综合欺诈而设计：

1. 通过名为 **“覆盖攻击（Overlay attacks）”** 的逼真伪造登录界面窃取银行凭证。
2. 攻击者获得对受感染设备的 **广泛远程控制权**，包括观察所有用户活动，关键是“在后台执行欺诈交易时黑屏——不让受害者察觉”。这种“黑屏覆盖”机制使攻击者能执行设备接管（DTO）欺诈，同时向受害者隐藏恶意活动。

Sturnus 为远程会话同时采用 **基于像素的屏幕流传输** 和 **高效的 UI 树控制层**。第二种方法传输界面元素的结构化描述，可实现点击、文本输入等精确操作，且带宽消耗极小，不会触发标准屏幕捕获指示器。

尽管 MTI Security 指出该恶意软件“可能处于部署前状态”，但它已完全具备功能，部分方面甚至比成熟恶意软件家族更先进。Sturnus 被配置用于针对 **南欧和中欧金融机构的定向攻击**，暗示其正准备更广泛的攻击活动。

该木马通过滥用 **Android 设备管理员权限** 确保持久化。获得权限后，当用户尝试进入设置界面禁用其状态时，恶意软件会主动监控并自动跳转以阻止移除。此外，其命令与控制（C2）连接采用 **HTTP 和 WebSocket 混合的复杂高级通信协议**，并结合强 AES 加密，实现实时命令控制和战术动态调整。

Sturnus 代表了一种高度复杂的综合威胁，结合多种攻击向量实现近乎完全的设备控制和数据窃取。该恶意软件利用键盘记录和辅助功能从加密消息应用捕获敏感信息，为移动银行威胁树立了危险的新先例。

本文翻译自securityonline [原文链接](https://securityonline.info/sturnus-trojan-bypasses-whatsapp-signal-encryption-takes-over-android-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313302](/post/id/313302)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sturnus-trojan-bypasses-whatsapp-signal-encryption-takes-over-android-devices/)

如若转载,请注明出处： <https://securityonline.info/sturnus-trojan-bypasses-whatsapp-signal-encryption-takes-over-android-devices/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **716**

* 粉丝
* **6**

### TA的文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23

### 相关文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23
* ##### [“Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张](/post/id/313308)

  2025-11-21 17:53:47
* ##### [WSUS中存在关键远程代码执行漏洞（CVE-2025-59287），正被积极利用以部署ShadowPad后门](/post/id/313305)

  2025-11-21 17:52:53

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