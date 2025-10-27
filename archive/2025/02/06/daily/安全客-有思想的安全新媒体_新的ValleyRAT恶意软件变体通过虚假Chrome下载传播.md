---
title: 新的ValleyRAT恶意软件变体通过虚假Chrome下载传播
url: https://www.anquanke.com/post/id/303844
source: 安全客-有思想的安全新媒体
date: 2025-02-06
fetch_date: 2025-10-06T20:34:27.019140
---

# 新的ValleyRAT恶意软件变体通过虚假Chrome下载传播

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

# 新的ValleyRAT恶意软件变体通过虚假Chrome下载传播

阅读量**407170**

发布时间 : 2025-02-05 16:50:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/author/deeba/>

译文仅供参考，具体内容表达以及含义原文为准。

Morphisec 发现了 ValleyRAT 恶意软件的一个新变种，该变种具备先进的规避策略、多阶段感染链以及针对系统的全新传播方式。

Morphisec 威胁实验室的网络安全研究人员发现了这种复杂的 ValleyRAT 恶意软件的新版本，它通过网络钓鱼邮件、即时通讯平台以及被攻陷的网站等多种渠道进行传播。ValleyRAT 是一种多阶段恶意软件，与臭名昭著的 “银狐” 高级持续性威胁（APT）组织有关联。

根据 Morphisec 与[Hackread.com](https://hackread.com/)分享的调查结果，此次攻击活动的主要目标是各组织内的重要人员，尤其是财务、会计和销售部门的人员，目的是窃取敏感数据。

![New ValleyRAT Malware Variant Spreading via Fake Chrome Downloads]()

早期的 ValleyRAT 版本利用伪装成合法软件安装程序的 PowerShell 脚本，常常通过 DLL 劫持手段，将其有效载荷注入 WPS Office 甚至火狐（Firefox）等程序的签名可执行文件中。2024 年 8 月，[Hackread.com](https://hackread.com/)报道过一个 ValleyRAT 版本，该版本使用外壳代码将恶意软件组件直接注入内存。

相反，当前版本利用一个假冒的中国电信公司 “Karlos” 的网站（karlostclub/）来分发恶意软件，该网站会下载一系列文件，其中包括一个.NET 可执行文件，它会检查管理员权限并下载其他组件，包括一个 DLL 文件。

研究人员在博客文章中写道：“有趣的是，攻击者在新旧版本的攻击中都复用了相同的 URL。”

据研究人员称，从 anizomcom / 下载假冒的 Chrome 浏览器是攻击链中的初始感染途径，诱使受害者下载并执行恶意软件。名为 sscronet.dll 的文件故意取了个看似合法的标识符以避免引起怀疑，它会将代码注入合法的 svchost.exe 进程，充当监控程序，终止预定义排除列表中的任何进程，以防止其干扰恶意软件的运行。接下来，恶意软件利用经过修改的抖音（中国版 TikTok）可执行文件进行 DLL 侧加载，并借助 Valve 游戏（特别是《求生之路 2》和《杀戮空间 2》）中的合法 Tier0.dll 文件，在 nslookup.exe 进程中执行隐藏的代码。该进程从 mpclient.dat 中检索并解密 ValleyRAT 的主要有效载荷。

![]()

解密后的有效载荷使用 Donut 外壳代码在内存中执行恶意软件，绕过传统的基于磁盘的检测方法。它还试图禁用诸如反恶意软件扫描接口（AMSI）和 Windows 事件跟踪（ETW）等安全机制。

需要说明的是，ValleyRAT 是一款基于 C++ 的远程访问木马，具备基本的远程访问木马功能，比如能够访问 WinSta0 窗口站，实现对屏幕、键盘和鼠标的交互操作，并监控受害者的屏幕。它包含大量针对 VMware 的反检测机制，以逃避在虚拟化环境中的检测，并在安装过程中使用代码内初始化的 IP 地址和端口与命令控制（C2）服务器建立连接。

研究人员指出：“如果恶意软件未检测到自己在虚拟机（VM）内运行，它会尝试连接[baidu.com](https://baidu.com/)，作为其网络通信检查的一部分。”

“银狐” APT 组织不断变化的策略和规避技术表明，新型攻击正变得越来越复杂。各组织应采取恰当的安全策略，包括更严格的端点保护、员工培训以及持续监控，以降低风险。

本文翻译自hackread [原文链接](https://hackread.com/author/deeba/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303844](/post/id/303844)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/author/deeba/)

如若转载,请注明出处： <https://hackread.com/author/deeba/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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