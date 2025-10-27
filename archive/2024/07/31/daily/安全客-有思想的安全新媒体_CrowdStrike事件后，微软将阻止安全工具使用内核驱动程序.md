---
title: CrowdStrike事件后，微软将阻止安全工具使用内核驱动程序
url: https://www.anquanke.com/post/id/298581
source: 安全客-有思想的安全新媒体
date: 2024-07-31
fetch_date: 2025-10-06T17:41:45.641573
---

# CrowdStrike事件后，微软将阻止安全工具使用内核驱动程序

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

# CrowdStrike事件后，微软将阻止安全工具使用内核驱动程序

阅读量**90484**

发布时间 : 2024-07-30 14:32:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 Simon Sharwood，文章来源：theregister

原文地址：<https://www.theregister.com/2024/07/29/microsoft_crowdstrike_kernel_mode/>

译文仅供参考，具体内容表达以及含义原文为准。

更新Microsoft发誓要减少网络安全供应商对内核模式代码的依赖，这是本月CrowdStrike超级骗局的核心。

雷德蒙德周六分享了一篇技术事件响应文章——标题为“集成和管理安全工具的 Windows 安全最佳实践”——其中企业和操作系统安全的 veep David Weston 解释了 Microsoft 如何衡量灾难的影响：通过访问客户共享的崩溃报告。

但是，当然，正如 Weston 所指出的，并非每个 Windows 客户都会分享崩溃报告。

“值得注意的是，生成崩溃报告的设备数量是Microsoft之前共享的受影响设备数量的子集，”他写道。这意味着这家 IT 巨头估计有 850 万台 Windows 计算机受到 CrowdStrike snafu 的影响，而每台计算机都没有提供崩溃报告。这家软件巨头没有详细说明用于计算这一数字的方法。

Weston 的帖子证明了 Windows 的性能，理由是内核级驱动程序（如 CrowdStrike 采用的驱动程序）可以提高性能并防止篡改安全软件。然而，他指出，信息安全供应商必须将这些好处合理化，以应对对复原力的潜在负面影响。

如果内核模式代码中断，就像 CrowdStrike 发生的情况一样，当其 Falcon 套件试图解析推送到数百万台 Windows 机器的错误配置文件时，由此产生的崩溃将摧毁整个操作系统及其应用程序。

因此，在内核之外可以完成的越多越好;如果该处理在用户模式下偏离轨道，则系统的其余部分至少应保持滴答作响，并且能够优雅地处理故障。

这是因为 Windows 内核模式是一个功能强大、受信任的环境，其中代码在硬件附近运行，没有太多的防护措施;它是一种软件，可以管理您的设备，使 CPU 内核忙于处理应用程序的工作，并根据需要将程序和用户彼此分开，以及其他任务。

这是恶意软件检测引擎以内核驱动程序的形式运行的好地方，因为它们可以很好地了解整个计算机，以嗅探出入侵和其他威胁。

但不利的一面是，如果这些引擎受到损害或发生故障，它们可能会撞倒整个盒子，或者更糟糕的是，打开系统以进一步攻击。因此，建议将辅助功能（例如配置文件解析）从内核中移出，并移动到用户空间中，这样可以限制损害。

尤其是在 CrowdStrike 的情况下，其数字签名的驱动程序级代码（通常由 Microsoft 批准）通过以更新形式推出的数据文件进行扩展;一个流氓更新将取消 Windows 对 CrowdStrike 内核级代码的任何信任。

在这种情况下，Falcon 驱动程序是一个文件系统过滤器驱动程序，它通常允许防病毒产品查找恶意文件操作;本月的错误文件更新导致该驱动程序访问了它不应该访问的内存，从而触发了越界读取异常和系统崩溃。

正如 Weston 所说：“由于内核驱动程序在最受信任的 Windows 级别上运行，其中包含和恢复能力本质上受到限制，因此安全供应商必须仔细平衡可见性和防篡改等需求与在内核模式下运行的风险。

他观察到，安全供应商可以找到正确的平衡点。

他解释说：“例如，安全供应商可以使用在内核模式下运行的最小传感器来收集和执行数据，从而限制可用性问题的风险。“关键产品功能的其余部分包括管理更新、解析内容，以及其他可以在可恢复性的用户模式下单独发生的操作。”

他建议，这种安排“展示了最小化内核使用的最佳实践，同时仍然保持强大的安全态势和强大的可见性。

你在做笔记吗，CrowdStrike？

这也是一个值得注意的好时机，CrowdStrike 确实尝试在发布之前测试其错误的更新，尽管该验证管道未能检测、标记和阻止损坏的数据流向所有人。更有理由将这种配置解析代码置于用户模式，而不是敏感的内核模式，更有理由让 CrowdStrike 通过沙盒等方式改进其测试实践。

CrowdStrike 是否可以轻松地将其配置解析与其检测代码分开是另一回事;我们希望供应商至少在考虑一下。

韦斯顿还提醒读者，雷德蒙德运营着一个名为Microsoft病毒计划（MVI）的行业论坛，在这个论坛上，安全供应商和操作系统巨头共同努力，“定义可靠的扩展点和平台改进，并分享有关如何最好地保护我们的客户的信息。

Microsoft veep 列出了 Microsoft 多年来所做的许多与安全相关的增强功能，并透露这家软件巨头现在计划“与反恶意软件生态系统合作，利用这些集成功能来现代化他们的方法，帮助支持甚至提高安全性和可靠性。

这项工作将涉及四项努力，即：

1. 提供安全推出指南、最佳实践和技术，以便更安全地执行安全产品的更新;
2. 减少对内核驱动程序访问重要安全数据的需求;
3. 通过最近宣布的 VBS 飞地等技术提供增强的隔离和防篡改功能;
4. 启用零信任方法，如高完整性证明，它提供了一种根据 Windows 本机安全功能的运行状况确定计算机安全状态的方法。

第二点似乎旨在确保未来不太可能发生类似 CrowdStrike 的事件。

韦斯顿没有解释如何减少依赖性——可能需要对 Windows 进行一些重新调整才能实现这一目标。

Microsoft 和 Windows 在安全陷阱方面有着悠久而不光彩的历史。如果雷德蒙德的更改出错，它不会让 CrowdStrike 为任何新问题负责。®

### 在 1930 UTC 更新

本文的标题和文本被修改是因为，坦率地说，我们将 Microsoft 关于崩溃报告计数是一个子集的披露视为承认或暗示这家 IT 巨头低估了受 CrowdStrike snafu 影响的 Windows 机器数量。转念一想，我们不确定这一点，因此我们很高兴在没有这种假设的情况下澄清这篇文章。

本文翻译自theregister [原文链接](https://www.theregister.com/2024/07/29/microsoft_crowdstrike_kernel_mode/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298581](/post/id/298581)

安全KER - 有思想的安全新媒体

本文转载自: [theregister](https://www.theregister.com/2024/07/29/microsoft_crowdstrike_kernel_mode/)

如若转载,请注明出处： <https://www.theregister.com/2024/07/29/microsoft_crowdstrike_kernel_mode/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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