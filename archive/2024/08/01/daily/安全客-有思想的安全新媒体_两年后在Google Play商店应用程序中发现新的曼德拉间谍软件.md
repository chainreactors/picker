---
title: 两年后在Google Play商店应用程序中发现新的曼德拉间谍软件
url: https://www.anquanke.com/post/id/298616
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:06.795730
---

# 两年后在Google Play商店应用程序中发现新的曼德拉间谍软件

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

# 两年后在Google Play商店应用程序中发现新的曼德拉间谍软件

阅读量**154936**

发布时间 : 2024-07-31 11:21:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 拉维·拉克什马南，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html>

译文仅供参考，具体内容表达以及含义原文为准。

在五个应用程序中发现了名为 **Mandrake** 的复杂 Android 间谍软件的新迭代，这些应用程序可从 Google Play 商店下载，并且两年未被发现。

卡巴斯基在周一的一篇文章中表示，这些应用程序在从应用商店下架之前总共吸引了超过32,000次安装。大部分下载来自加拿大、德国、意大利、墨西哥、西班牙、秘鲁和英国。

研究人员Tatyana Shishkova和Igor Golovin说：“新样本包括新的混淆和规避技术层，例如将恶意功能移动到混淆的本地库，使用证书固定进行C2通信，以及执行各种测试以检查Mandrake是在有根设备上运行还是在模拟环境中运行。

罗马尼亚网络安全供应商 Bitdefender 于 2020 年 5 月首次记录了 Mandrake，描述了自 2016 年以来其故意感染少数设备的方法，同时设法潜伏在阴影。

更新后的变体的特点是使用 OLLVM 来隐藏主要功能，同时还结合了一系列沙盒规避和反分析技术，以防止代码在恶意软件分析师操作的环境中执行。

包含 Mandrake 的应用程序列表如下 –

* AirFS （com.airft.ftrnsfr）
* 琥珀色 （com.shrp.sght）
* Astro 浏览器 （com.astro.dscvr）
* 脑矩阵 （com.brnmth.mtrx）
* 加密脉冲 （com.cryptopulsing.browser）

这些应用程序分为三个阶段：一个滴管，在从命令和控制 （C2） 服务器下载和解密恶意软件后，启动负责执行恶意软件核心组件的加载程序。

第二阶段有效载荷还能够收集有关设备的连接状态、已安装的应用程序、电池百分比、外部 IP 地址和当前 Google Play 版本的信息。此外，它可以擦除核心模块并请求权限以绘制覆盖层并在后台运行。

第三阶段支持其他命令，用于在 WebView 中加载特定 URL，并启动远程屏幕共享会话，以及录制设备屏幕，目的是窃取受害者的凭据并丢弃更多恶意软件。

研究人员说：“Android 13 引入了’受限设置’功能，该功能禁止侧载应用程序直接请求危险权限。“为了绕过此功能，Mandrake 使用’基于会话’的包安装程序处理安装。”

这家俄罗斯安全公司将曼德拉草描述为动态演变的威胁的一个例子，该威胁不断改进其交易技巧，以绕过防御机制并逃避检测。

“这凸显了威胁行为者的强大技能，而且在发布到市场上之前对应用程序进行更严格的控制只会转化为更复杂、更难检测的威胁潜入官方应用程序市场，”它说。

当被要求发表评论时，谷歌告诉The Hacker News，随着新的恶意应用程序被标记，它正在不断加强Google Play Protect防御，并且正在增强其能力，包括实时威胁检测，以解决混淆和反规避技术。

谷歌发言人表示：“Google Play Protect会自动保护Android用户免受此恶意软件的已知版本的侵害，该保护在具有Google Play服务的Android设备上默认处于开启状态。“Google Play 保护机制可以警告用户或阻止已知表现出恶意行为的应用，即使这些应用来自 Play 之外的来源也是如此。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298616](/post/id/298616)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/new-mandrake-spyware-found-in-google.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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
* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [新型 Mirai 僵尸网络通过命令注入漏洞感染 TBK DVR 设备](/post/id/308303)

  2025-06-10 13:35:25

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