---
title: 新的“Defendnot”工具欺骗Windows禁用Microsoft Defender
url: https://www.anquanke.com/post/id/307626
source: 安全客-有思想的安全新媒体
date: 2025-05-22
fetch_date: 2025-10-06T22:26:46.347206
---

# 新的“Defendnot”工具欺骗Windows禁用Microsoft Defender

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

# 新的“Defendnot”工具欺骗Windows禁用Microsoft Defender

阅读量**110202**

发布时间 : 2025-05-21 16:09:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 劳伦斯 艾布拉姆斯，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/microsoft/new-defendnot-tool-tricks-windows-into-disabling-microsoft-defender/>

译文仅供参考，具体内容表达以及含义原文为准。

![微软 Defender]()

一个名为“Defendnot”的新工具可以通过注册虚假的防病毒产品来禁用Windows设备上的Microsoft Defender,即使没有安装真正的AV。

该技巧利用无证Windows安全中心(WSC)API,防病毒软件用于告诉Windows它已安装,现在正在管理设备的实时保护。

注册防病毒程序时,Windows 会自动禁用 Microsoft Defender,以避免在同一设备上运行多个安全应用程序发生冲突。

[Defendnot tool](https://github.com/es3n1n/defendnot)由研究人员 es3n1n 创建的Defendnot工具通过注册符合所有Windows验证检查的假防病毒产品来滥用此API。

该工具基于之前一个名为“无防御者”的项目,该项目使用来自第三方防病毒产品的代码来欺骗WSC注册。早些时候的工具是在供应商提交DMCA删除后从GitHub中提取的。

“然后,在发布几周后,该项目爆炸了不少,获得了约1.5万颗星,之后,我使用的防病毒软件的开发人员提交了DMCA删除请求,我真的不想做任何事情,所以只是抹去了所有内容并称之为一天t”开发人员在一篇博客文章中解释道。

Defendnot通过虚拟防病毒DLL从头开始构建功能来避免版权问题。

通常,WSC API通过Protected Process Light(PPL),有效的数字签名和其他功能进行保护。

要绕过这些要求,Defendnot 需要管理权限,它可以将其 DLL 注入到系统进程 Taskmgr.exe,该进程已由 Microsoft 签名且已经信任。从该过程中,它可以使用欺骗显示名称注册虚拟防病毒软件。

注册后,Microsoft Defender立即关闭自己,在设备上没有留下任何主动保护。

![在设备上注册的 Defendnot]()

该工具还包括一个加载器,该加载器通过ctx.bin文件传递配置数据,并允许您设置要使用的防病毒名称,关闭注册并启用冗长的日志记录。

对于持久性,Defendnot 会通过 Windows 任务计划程序创建自动运行,以便在登录 Windows 时启动。

虽然Defendnot被认为是一个研究项目,但该工具演示了如何操纵可信的系统功能以关闭安全功能。

Microsoft Defender 目前正在检测和隔离 Defendnot 为 ‘Win32/Sabsik.FL . !ml;检测。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/microsoft/new-defendnot-tool-tricks-windows-into-disabling-microsoft-defender/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307626](/post/id/307626)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/microsoft/new-defendnot-tool-tricks-windows-into-disabling-microsoft-defender/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/microsoft/new-defendnot-tool-tricks-windows-into-disabling-microsoft-defender/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [技术分析](/tag/%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [Cyera融资5.4亿美元，估值翻番，致力于人工智能数据保护](/post/id/308391)

  2025-06-12 14:36:27
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Jenkins Gatling 插件中未修补的 XSS 漏洞会给用户带来风险 (CVE-2025-5806)](/post/id/308251)

  2025-06-09 17:13:32
* ##### [新的 Mirai 僵尸网络变种通过 CVE-2024-3721 瞄准 DVR 系统](/post/id/308245)

  2025-06-09 17:08:32
* ##### [HPE 发布针对 StoreOnce 漏洞的重要补丁程序](/post/id/308181)

  2025-06-06 15:04:41

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