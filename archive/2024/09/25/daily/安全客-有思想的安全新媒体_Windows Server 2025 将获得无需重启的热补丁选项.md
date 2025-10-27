---
title: Windows Server 2025 将获得无需重启的热补丁选项
url: https://www.anquanke.com/post/id/300354
source: 安全客-有思想的安全新媒体
date: 2024-09-25
fetch_date: 2025-10-06T18:25:33.804774
---

# Windows Server 2025 将获得无需重启的热补丁选项

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

# Windows Server 2025 将获得无需重启的热补丁选项

阅读量**97582**

发布时间 : 2024-09-24 14:23:48

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/09/23/windows-server-2025-hotpatching/>

译文仅供参考，具体内容表达以及含义原文为准。

计划在 Windows Server 2025 正式发布后升级到 Windows Server 2025 的组织将能够通过热补丁正在运行的进程来实施一些安全更新。

![Windows Server 2025 热补丁]( "Windows Server 2025 hotpatching (Source: Microsoft)")

## 什么是热补丁？

“热修补在 Windows Server 2022 Azure 版本中已经存在多年，但始终需要在 Azure 或 Azure Stack HCI 上运行 VM。当Windows Server 2025正式发布时，您将能够在您想要的地方运行您想要的版本 – 无论是在本地，还是在Azure中，还是在其他地方，“ Microsoft的Windows Server，Azure主机操作系统和Windows CoreOS平台的产品总监Hari Pulapaka在周五指出。

“您可以选择对 Windows Server 2025 物理服务器或虚拟机进行热修补，这些虚拟机可以在 Hyper-V、VMware 或支持 Microsoft 以保护为中心的基于虚拟化的安全标准的任何其他平台上运行。”

热补丁 – 即通过修补正在运行的进程的内存代码来实施操作系统安全更新 – 不需要重新启动系统即可应用补丁。

Pulapaka 说，更少的重启意味着服务器管理员的工作量更低，使用的磁盘和 CPU 资源更少。它还使补丁编排和变更控制更加容易。

“热补丁在 Windows Server 2022 Datacenter： Azure Edition 中已经推出几年了，这是一项久经考验的技术。真正的变化是你如何以及在哪里获得这些安全更新，“他补充道。

对于 Windows Server 2025 标准版和数据中心版，将通过 Azure Arc 提供热补丁，它“允许运行热补丁的 Windows Server 内部许可服务，以便将热补丁更新交付给客户”。

不过，请记住，热补丁并不总是可能的，因此“定期”修补和重启不会消失。

## 关于 Windows Server 2025

Windows Server 2025 目前处于预览阶段，计划于 2024 年底完成并发布。

这个最新版本的流行服务器操作系统将带有许多新的和改进的安全功能，一些旧版 Windows Server 功能将被删除或弃用（包括 Windows Server Update Services）。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/09/23/windows-server-2025-hotpatching/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300354](/post/id/300354)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/09/23/windows-server-2025-hotpatching/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/09/23/windows-server-2025-hotpatching/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* [什么是热补丁？](#h2-0)
* [关于 Windows Server 2025](#h2-1)

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