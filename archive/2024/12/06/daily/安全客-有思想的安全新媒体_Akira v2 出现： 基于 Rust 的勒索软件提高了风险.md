---
title: Akira v2 出现： 基于 Rust 的勒索软件提高了风险
url: https://www.anquanke.com/post/id/302453
source: 安全客-有思想的安全新媒体
date: 2024-12-06
fetch_date: 2025-10-06T19:33:55.486460
---

# Akira v2 出现： 基于 Rust 的勒索软件提高了风险

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

# Akira v2 出现： 基于 Rust 的勒索软件提高了风险

阅读量**61895**

发布时间 : 2024-12-05 11:12:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/akira-v2-emerges-rust-based-ransomware-raises-the-stakes/>

译文仅供参考，具体内容表达以及含义原文为准。

![Akira ransomware v2]()

根据 Check Point Research (CPR) 的详细分析，今年早些时候，随着基于 Rust 的新变种的推出，Akira 勒索软件实现了重大飞跃。该版本被称为 “Akira v2”，展示了勒索软件设计的战略性演变，它以 ESXi 裸机管理程序服务器为目标，并利用 Rust 的独特属性来增强其复杂性和跨平台能力。

Rust 在生成高度优化、安全和跨平台的二进制文件方面享有盛誉，这使其成为合法开发者的不二之选。不幸的是，这些特性正日益吸引着网络犯罪分子。正如 CPR 所解释的那样，“用 Rust 编写的可执行文件在逆向工程方面具有特别高的挑战性”。这使得它们成为 Akira 等复杂威胁的理想载体。”

Rust 强大的内联和单态化功能增加了汇编级的复杂性，给研究人员带来了巨大挑战。CPR指出：“语言的本质加上编译器优化输出的驱动力，往往会导致禁止反汇编。”

在其核心部分，Akira v2 展示了一个针对多线程优化的结构化控制流，从而提高了性能。该勒索软件的主执行线程调用了一系列函数–“Main -> default\_action -> lock -> lock\_closure”，这些函数在并行线程中解析参数、收集目标文件并执行加密。

该变种的一个显著特点是专注于 ESXi 服务器。默认情况下，它以 /vmfs/volumes 等目录为目标，这些目录通常与 VMware 虚拟机相关联，但也保留了加密其他 Linux 系统的灵活性。该勒索软件的操作员可以通过命令行标志对其行为进行微调，如 -stopvm 来关闭虚拟机，或 -exclude 来跳过特定文件。

Akira 采用混合加密方法，结合了对称和非对称密码。每个目标文件都会收到一个唯一的对称密钥，并使用硬编码的 Curve25519 公钥进行加密。对于对称加密，Akira 不同寻常地使用了 SOSEMANUK，这种流密码因其复杂性和以前在 Pridelocker 等勒索软件中的使用而闻名。

CPR 的分析显示，“SOSEMANUK 的实现完全是内联的，必须使用传统的识别有罪常量的方法来识别密码”。这种内联加上 Rust 的优化策略，使得破解勒索软件的加密过程成为一项艰巨的任务。

该恶意软件是为方便操作员使用而量身定制的。利用 indicatif 等 Rust 库，Akira 提供了完善的命令行界面（CLI），包括进度条、详细的状态更新和丰富多彩的输出。

勒索软件开发者采用 Rust 标志着网络安全领域的一个关键时刻。虽然 Rust 的设计原则为合法开发者带来了不可否认的好处，但也给安全专业人员带来了独特的挑战。CPR 的报告强调，需要能够 “隔离和识别拼接的内联代码 ”的新工具，以跟上 Rust 在恶意软件生态系统中日益普及的步伐。

通过采用 Rust，其开发者创造出了一种不仅更强大而且更难分析的变种。正如 CPR 总结的那样：“曾几何时，逆向工程 C 二进制文件也是原始而可怕的；最终，人们的理解能力提高了，工具也跟上了，这项任务变得不再那么艰巨。我们只能推断并希望，即使是 Rust 编译器偶尔痛苦的输出，也会遭遇同样的命运。”

本文翻译自securityonline [原文链接](https://securityonline.info/akira-v2-emerges-rust-based-ransomware-raises-the-stakes/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302453](/post/id/302453)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/akira-v2-emerges-rust-based-ransomware-raises-the-stakes/)

如若转载,请注明出处： <https://securityonline.info/akira-v2-emerges-rust-based-ransomware-raises-the-stakes/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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