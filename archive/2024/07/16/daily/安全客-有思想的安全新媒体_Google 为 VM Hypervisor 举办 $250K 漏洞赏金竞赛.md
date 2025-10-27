---
title: Google 为 VM Hypervisor 举办 $250K 漏洞赏金竞赛
url: https://www.anquanke.com/post/id/297897
source: 安全客-有思想的安全新媒体
date: 2024-07-16
fetch_date: 2025-10-06T17:40:46.134120
---

# Google 为 VM Hypervisor 举办 $250K 漏洞赏金竞赛

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

# Google 为 VM Hypervisor 举办 $250K 漏洞赏金竞赛

阅读量**52692**

发布时间 : 2024-07-15 12:24:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Staff，文章来源：DARKREADING

原文地址：<https://www.darkreading.com/cloud-security/google-opens-250k-bug-bounty-contest-for-vm-hypervisor>

译文仅供参考，具体内容表达以及含义原文为准。

为了鼓励人们在开源的基于内核的虚拟机（KVM）虚拟机管理程序中发现安全漏洞，谷歌推出了一项漏洞奖励计划（VRP），最高奖金高达一百万美元。VRP 被设置为夺旗竞赛，测试人员以访客身份登录并尝试在 KVM 主机内核中查找零日漏洞。

KVM 是一个开源项目，Google 是该项目的积极贡献者，自 2007 年以来一直包含在主线 Linux 中。它允许 Intel 或 AMD 驱动的设备运行多个虚拟机 （VM），并具有可自定义的硬件仿真以支持多个传统操作系统。谷歌在其 Android 和 Google Cloud 平台中使用它，这就是为什么它在确保其安全方面拥有既得利益的原因。

去年10月首次宣布，“kvmCTF”竞赛于6月27日正式拉开帷幕。参与者保留时隙（以 UTC 格式）登录到裸机主机上运行的客户机虚拟机，然后尝试客户机到主机攻击。

“攻击的目标必须是利用主机内核的KVM子系统中的零日漏洞，”谷歌在比赛的发布会上说。为此，竞赛中未涵盖从 QEMU 仿真器开始的漏洞或依赖于主机到 KVM 技术的漏洞。完整的规则详细说明了整个过程，从如何下载必要的文件到如何正确证明漏洞利用成功。

此奖励列表出现在 6 月 27 日的 Google Security 博客文章中：

* 完整的虚拟机逃逸：250,000 USD
* 任意内存写入：100,000 USD
* 读取的任意内存：50,000 美元
* 相对内存写入：50,000 美元
* 拒绝服务：20,000 美元
* 相对内存读取：10,000 美元

奖励不会叠加——道德黑客只能获得终点奖励，而不是中间步骤的奖励。此外，根据 kvmCTF Discord 频道上的讨论，只有第一个成功的提交才能获得奖励，但截至发稿时，尚未收到任何提交。

本文翻译自DARKREADING [原文链接](https://www.darkreading.com/cloud-security/google-opens-250k-bug-bounty-contest-for-vm-hypervisor)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297897](/post/id/297897)

安全KER - 有思想的安全新媒体

本文转载自: [DARKREADING](https://www.darkreading.com/cloud-security/google-opens-250k-bug-bounty-contest-for-vm-hypervisor)

如若转载,请注明出处： <https://www.darkreading.com/cloud-security/google-opens-250k-bug-bounty-contest-for-vm-hypervisor>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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