---
title: Turla APT 组织涉嫌利用 MSBuild 微小后门进行隐秘攻击
url: https://www.anquanke.com/post/id/296639
source: 安全客-有思想的安全新媒体
date: 2024-05-22
fetch_date: 2025-10-06T16:48:59.227150
---

# Turla APT 组织涉嫌利用 MSBuild 微小后门进行隐秘攻击

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

# Turla APT 组织涉嫌利用 MSBuild 微小后门进行隐秘攻击

阅读量**198956**

发布时间 : 2024-05-21 10:31:48

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/new-turla-apt-groups-tiny-backdoor-tactics/>

译文仅供参考，具体内容表达以及含义原文为准。

Cyble 研究与情报实验室 (CRIL) 发现了一项复杂的网络攻击活动，该活动使用恶意 LNK 文件，可能通过垃圾邮件进行分发。这项复杂的攻击活动可能是由臭名昭著的 Turla 高级持续性威胁 (APT) 组织策划的，它利用人权研讨会邀请和公共咨询作为诱饵，利用恶意负载入侵用户系统。

威胁行为者 (TA) 通过在 .LNK 文件中嵌入诱饵 PDF 和 MSBuild 项目文件来展示高水平的复杂性，确保无缝执行过程。利用 Microsoft 构建引擎 (MSBuild)，TA 执行这些项目文件以部署隐秘的无文件最终有效负载，充当后门以方便对受感染系统进行远程控制。

## Turla APT 组织感染链

![]()
攻击以隐藏在 ZIP 存档中的恶意 .LNK 文件展开，可能通过网络钓鱼电子邮件发送。执行后，.LNK 文件会触发 PowerShell 脚本，启动一系列操作。这些操作包括从 .LNK 文件中提取内容并在 %temp% 位置创建三个不同的文件：诱饵 PDF、加密数据和自定义 MSBuild 项目。

![图拉APT集团]()
来源：Cyble
伪装的 .LNK 文件会触发 PowerShell 脚本，然后该脚本会打开诱饵 PDF，同时静默执行嵌入式 MSBuild 项目。

![图拉APT集团]()
来源：Cyble
该项目文件包含加密内容，采用 Rijndael 算法来解密数据，随后执行最终的后门有效负载。

![诱饵 pdf]()
来源：Cyble
使用 MSBuild.exe 执行解密的 MSBuild 项目文件时，会直接在内存中运行内联任务。此任务使后门能够启动各种操作，包括监视进程、执行命令以及与命令和控制 (C&C) 服务器通信以获取进一步指令。

## Turla APT 组织的威胁行为者归因

据CRIL称，由于代码中的俄语注释以及与之前的 Turla 活动的行为相似，此次活动背后的威胁行为者是 Turla APT 组织。该组织针对非政府组织的重点与引用人权研讨会的诱饵文件一致。

MSBuild 和其他合法应用程序的利用凸显了威胁行为者的持久性。通过利用固有功能，Turla APT 组织可以逃避传统的安全措施。组织必须采用多层安全方法来有效降低风险。

为了加强对 Turla APT 组织等复杂威胁的防御，组织应采取关键的网络安全措施。这包括实施强大的电子邮件过滤功能以阻止恶意附件，并在处理来自未知来源的电子邮件附件时保持谨慎。

将 MSBuild 等开发工具的访问权限限制为授权人员有助于防止滥用，同时禁用 PowerShell 等不必要的脚本语言可降低被利用的风险。建立网络级监控对于快速检测和响应异常活动至关重要。这些做法共同增强了安全态势，保护敏感数据和系统免受网络威胁。

本文翻译自 [原文链接](https://thecyberexpress.com/new-turla-apt-groups-tiny-backdoor-tactics/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296639](/post/id/296639)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/new-turla-apt-groups-tiny-backdoor-tactics/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [APT](/tag/APT)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [猎影计划：从密流中捕获 Cobalt Strike 的隐秘身影](/post/id/310538)

  2025-07-24 12:50:35
* ##### [APT-C-55（Kimsuky）组织在RandomQuery活动中投递开源RAT的攻击活动分析](/post/id/297233)

  2024-06-13 10:15:14
* ##### [Andariel APT 使用 DoraRAT 和 Nestdoor 恶意软件监视韩国企业](/post/id/297004)

  2024-06-03 10:52:13
* ##### [发现针对印度大学的 SideCopy APT 活动](/post/id/296541)

  2024-05-16 11:47:09
* ##### [俄罗斯黑客 APT28 对波兰政府发动恶意软件攻击](/post/id/296335)

  2024-05-09 11:10:37
* ##### [透明部落：针对印度国防部门的难以捉摸的威胁](/post/id/295858)

  2024-04-22 11:09:46
* ##### [沙鹰：源自中东还是美国？](/post/id/293799)

  2024-03-12 10:54:16

### 热门推荐

文章目录

* [Turla APT 组织感染链](#h2-0)
* [Turla APT 组织的威胁行为者归因](#h2-1)

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