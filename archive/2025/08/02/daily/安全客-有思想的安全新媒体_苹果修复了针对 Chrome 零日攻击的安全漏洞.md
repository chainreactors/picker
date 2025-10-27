---
title: 苹果修复了针对 Chrome 零日攻击的安全漏洞
url: https://www.anquanke.com/post/id/310792
source: 安全客-有思想的安全新媒体
date: 2025-08-02
fetch_date: 2025-10-07T00:18:04.116038
---

# 苹果修复了针对 Chrome 零日攻击的安全漏洞

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

# 苹果修复了针对 Chrome 零日攻击的安全漏洞

阅读量**84758**

发布时间 : 2025-08-01 17:12:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/apple-patches-security-flaw-exploited-in-chrome-zero-day-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

苹果发布安全更新，修复一个已被用于针对 Google Chrome 用户的零日攻击的高危漏洞。

该漏洞编号为 **CVE-2025-6558，存在于 ANGLE（Almost Native Graphics Layer Engine）开源图形抽象层中**。ANGLE 主要负责处理 GPU 命令，并将 OpenGL ES API 调用转换为 Direct3D、Metal、Vulkan 和 OpenGL 等图形接口。**由于 ANGLE 未正确验证不受信任的输入**，攻击者可通过特制的 HTML 页面远程执行任意代码，从而在浏览器的 GPU 进程中实现代码执行，进而有可能绕过浏览器进程与操作系统之间的沙箱隔离机制。

该漏洞由 Google 威胁分析小组（TAG）的 Vlad Stolyarov 和 Clément Lecigne 于 2025 年 6 月发现并报告给 Chrome 团队。Google 随后于 7 月 15 日发布修复补丁，并将该漏洞标记为“已在攻击中被利用”。

尽管 Google 尚未披露具体的攻击细节，但 Google TAG 一贯致力于发现由国家支持的攻击者发起的零日漏洞利用行动，这类攻击通常面向政治异见人士、反对派政治人物以及记者等高风险群体，目的是在其设备上部署间谍软件。

本周二，苹果公司发布了 WebKit 安全更新，以修复编号为 **CVE-2025-6558** 的安全漏洞，涉及以下软件和设备：

* **iOS 18.6 和 iPadOS 18.6**：适用于 iPhone XS 及后续机型、iPad Pro 13 英寸、iPad Pro 12.9 英寸第三代及以上、iPad Pro 11 英寸第一代及以上、iPad Air 第三代及以上、iPad 第七代及以上、以及 iPad mini 第五代及以上机型；
* **macOS Sequoia 15.6**：适用于运行 macOS Sequoia 的 Mac 设备；
* **iPadOS 17.7.9**：适用于 iPad Pro 12.9 英寸第二代、iPad Pro 10.5 英寸，以及 iPad 第六代；
* **tvOS 18.6**：适用于 Apple TV HD 及所有型号的 Apple TV 4K；
* **visionOS 2.6**：适用于 Apple Vision Pro；
* **watchOS 11.6**：适用于 Apple Watch Series 6 及以上型号。

苹果公司在说明 **CVE-2025-6558** 的影响时表示：“处理恶意构造的网页内容可能导致 Safari 意外崩溃。”苹果强调，这是一个源自开源代码的漏洞，Apple 的软件项目是受影响的其中之一。

此外，美国网络安全和基础设施安全局（CISA）也于 7 月 22 日将该漏洞列入其“已被利用的漏洞”目录，并要求联邦机构必须在 **8 月 12 日前**完成补丁更新。

尽管《绑定操作指令》(BOD) 22-01 仅适用于联邦政府机构，但 CISA 也建议所有网络防御人员**优先修复 CVE-2025-6558 漏洞**，以防止被恶意攻击者利用。

CISA 上周在警告中指出：“此类漏洞经常被恶意网络行为者利用，对联邦信息系统构成重大风险。”

值得注意的是，自今年年初以来，苹果已修复了 **5 个被用于定向攻击的零日漏洞**，分别是 1 月的 **CVE-2025-24085、2 月的 CVE-2025-24200**、3 月的 **CVE-2025-24201**，以及 4 月的 **CVE-2025-31200 和 CVE-2025-31201**。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/apple-patches-security-flaw-exploited-in-chrome-zero-day-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310792](/post/id/310792)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/apple-patches-security-flaw-exploited-in-chrome-zero-day-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/apple-patches-security-flaw-exploited-in-chrome-zero-day-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**9赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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