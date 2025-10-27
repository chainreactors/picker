---
title: Microsoft 七月补丁为 Windows 安全事件添加新字段
url: https://www.anquanke.com/post/id/298135
source: 安全客-有思想的安全新媒体
date: 2024-07-23
fetch_date: 2025-10-06T17:42:16.306466
---

# Microsoft 七月补丁为 Windows 安全事件添加新字段

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

# Microsoft 七月补丁为 Windows 安全事件添加新字段

阅读量**98327**

发布时间 : 2024-07-22 11:26:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 SOC Inspiration，文章来源：Medium

原文地址：<https://soc-inspiration.medium.com/microsoft-july-patch-adds-new-fields-to-windows-security-events-what-does-it-mean-for-a-soc-dfir-441b063a3e45>

译文仅供参考，具体内容表达以及含义原文为准。

在运营网络安全团队中工作的人员都知道，在了解 **Active Directory**域内发生（或发生）的情况时，Windows 事件是多么重要。域控制器**上的安全**通道提供了多个与域身份验证相关的事件，包括我们将在这篇简短的文章中讨论的以下三个事件：

* **4768**：请求了 Kerberos 身份验证票证 （TGT）
* **4769**：请求了 Kerberos 服务票证
* **4770**：续订了 Kerberos 服务票证

在过去的几个月里，我们向 Microsoft 表达了有关 Active Directory 事件的几个缺点。其中之一是需要**唯一**标识 **Kerberos 票证**，我们将了解为什么它很重要。

## 需求

想象一下，从可疑的 AD 事件开始的调查，假设是 **Kerberoasting** 警报。在可疑的 4769 事件中，作为起点，您通常会公开发出 TGS 请求**的用户**以及该请求的**源 IP**。

如果还有来自该 IP 的**合法用户活动**，例如，在到达 DC 之前，已知设备执行 **SNAT**，该怎么办？您将如何区分合法和恶意的 AD 活动？

![]()

IP 和用户不足以隔离合法和恶意操作的设置

但是，如果我们能够**唯一地识别**为执行任何进一步操作（例如请求 TGS）而呈现的 TGT，我们将能够正确地分离活动。

![]()

相同的设置，具有唯一的 TGT 标识符

另一种情况是，两个会话（合法和恶意）确实来自同一资产。下面给出了一个示例，其中我们有一个使用 **AD 凭据**（VPN 设备、Web 服务等）的公开服务，该服务完全**遭到破坏**。攻击者可以决定**直接从同一台机器**打开一个新会话，从 DC 的角度来看，我们也无法将合法行为与恶意行为区分开来。

![]()

同一资产产生合法和恶意操作的设置

## 解决方案

在其最新补丁中，Microsoft 从**安全**通道发布了 Windows 事件 4768、4769 和 4770 的新字段。活动**的“票证信息**”部分中的这些字段如下：

* 存在于 4769 和 4770 中：**请求票证哈希**
* 存在于 4768、4769 和 4770 中：**响应票证哈希**

![]()

具有响应票证哈希的 4768 事件 （TGT）

![]()

具有请求票证哈希 （TGT） 和响应票证哈希 （TGS） 的 4769 事件

顾名思义，第一个是提供给 DC 的 Kerberos 票证**的唯一标识符**，用于执行与事件相关的操作（即获取 4769 的 TGS，或续订 4770 的 TGS）。

第二个是 DC 签发的机票**的唯一标识符**，它可以是 TGT （4768） 或 TGS （4769 & 4770），具体取决于相关事件。

# 我们如何使用它们？

## 响应

第一次直接申请是在调查期间。与在进程 ID 之间切换以查找可疑进程的整个进程树的方式相同，您将能够找到 **Kerberos 票证树**并回答 IR 中可能出现的关键问题，例如：在可疑会话期间执行的其他操作是什么？

在以下示例中，让我们回看 **Kerberoasting** 警报的示例。能够绘制整个**票证树**使我们能够显示攻击者在其恶意会话期间执行的**所有其他操作**，从而显示可能需要进一步调查的其他潜在**影响操作**。

![]()

使用 Kerberos 票证的透视示例，显示未触发任何警报的其他可疑操作

## 检波

您还可以构建一些检测用例，这些用例或多或少是可行的，具体取决于您自己的边界。

第一个是关于检测**伪造TGT**（又名金票）的新机会。这个想法很简单：既然你有你的配送中心签发**的所有TGT的指纹**，如果你看到**一个你不知道的指纹**是为了获得TGS票而出示的，那么它一定是**伪造**的。

挑战是多方面的，这就是为什么它或多或少是可行的：

* 由于这些是 Microsoft 引入的新字段，它们是否可靠（请参阅下一段和登录 GUID）？
* TGT 在我的环境中的生存期是多久？我是否有多个生存期不同的环境？
* 要获得 TGT 指纹的完整列表，我们不仅应该查看 4768 事件，还应该查看 **krbtgt**服务的 4769 事件，以及**krbtgt** **的 TGS** **门票续订**的 4770 事件

该搜索的草稿是这样的，TGT 默认生存期为 10 小时。我正在使用 **Splunk 查询语言**。

```
EventCode=4769 最早=-1h
NOT [ 搜索 EventCode=4768 最早=-11h
 |桌子Response_ticket_hash
 |重复数据Response_ticket_hash
 |重命名Response_ticket_hash as Request_ticket_hash ]
NOT [ search EventCode=4769 Service_Name=krbtgt* earliest=-11h
 |桌子Response_ticket_hash
 |重复数据Response_ticket_hash
 |重命名Response_ticket_hash as Request_ticket_hash ]
NOT [ search EventCode=4770 Service_Name=krbtgt* earliest=-11h
 |桌子Response_ticket_hash
 |重复数据Response_ticket_hash
 |重命名Response_ticket_hash Request_ticket_hash]
```

此查询中仍存在一个打开的窗口，该窗口可能允许攻击者仍使用伪造的 TGT 来**获取未检测到**的 TGS。我会让读者找到破绽！

第二个用例示例是检测 **Pass-The-Ticket**场景的新机会。攻击者可以选择**窃取现有票证**并重新使用它，而不是请求新票证，可能来自其他资产。为了检测这一点，我们可以简单地查看给定票证在其生命周期内使用**的不同源 IP**。

挑战也是多方面的：

* 再说一次，SNAT呢？
* 人们的笔记本电脑在工单的生命周期内被分配了多个IP（例如，如果他们在建筑物内移动）怎么办？

我再次猜测，回复将取决于您自己的环境。解决方法的一个示例是简单地将此搜索限制为**服务帐户**，这些帐户仍经常成为攻击者的目标。

![]()

简单的 Pass-The-Ticket 方案

## 与登录 GUID 有什么区别？

其中一些人可能已经使用**登录 GUID** 字段来执行本文中介绍的一些透视。如 Microsoft 文档所述，登录 GUID 在技术上允许将 4769 与身份验证事件链接。

实际上，众所周知，通常**不可能这样做**，例如[在Windows](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=4624)事件圣经中解释的那样。不过，如果您不相信自己，我鼓励您自己进行测试。

![]()

Windows 事件圣经中的登录 GUID 字段说明 （Ultimate Windows Security）

但是，4624 事件*本身*非常重要，因为它提供了有关**会话级别**本身的重要信息（是否提升了令牌等），而 4768 事件提供了**票证级别的**信息。换句话说，如果您能够关联 4624 事件，它总是有用的。

本文翻译自Medium [原文链接](https://soc-inspiration.medium.com/microsoft-july-patch-adds-new-fields-to-windows-security-events-what-does-it-mean-for-a-soc-dfir-441b063a3e45)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298135](/post/id/298135)

安全KER - 有思想的安全新媒体

本文转载自: [Medium](https://soc-inspiration.medium.com/microsoft-july-patch-adds-new-fields-to-windows-security-events-what-does-it-mean-for-a-soc-dfir-441b063a3e45)

如若转载,请注明出处： <https://soc-inspiration.medium.com/microsoft-july-patch-adds-new-fields-to-windows-security-events-what-does-it-mean-for-a-soc-dfir-441b063a3e45>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [热点 | 利用AI造谣幼儿园大火被抓，大模型内容安全谁来守护？](/post/id/308685)

  2025-06-20 16:47:19
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [德克萨斯州警告30万份事故报告通过受影响的用户帐户窃取](/post/id/308363)

  2025-06-11 16:42:18
* ##### [新型 Mirai 僵尸网络通过命令注入漏洞感染 TBK DVR 设备](/post/id/308303)

  2025-06-10 13:35:25
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03

### 热门推荐

文章目录

* [需求](#h2-0)
* [解决方案](#h2-1)
* [响应](#h2-2)
* [检波](#h2-3)
* [与登录 GUID 有什么区别？](#h2-4)

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