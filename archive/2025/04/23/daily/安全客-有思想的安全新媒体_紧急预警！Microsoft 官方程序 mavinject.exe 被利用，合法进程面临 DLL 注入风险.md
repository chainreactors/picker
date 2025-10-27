---
title: 紧急预警！Microsoft 官方程序 mavinject.exe 被利用，合法进程面临 DLL 注入风险
url: https://www.anquanke.com/post/id/306763
source: 安全客-有思想的安全新媒体
date: 2025-04-23
fetch_date: 2025-10-06T22:04:49.152695
---

# 紧急预警！Microsoft 官方程序 mavinject.exe 被利用，合法进程面临 DLL 注入风险

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

# 紧急预警！Microsoft 官方程序 mavinject.exe 被利用，合法进程面临 DLL 注入风险

阅读量**56498**

发布时间 : 2025-04-22 11:10:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/legitimate-windows-tool-abused-mavinject-exe-used-for-stealthy-dll-injection-by-threat-actors/>

译文仅供参考，具体内容表达以及含义原文为准。

![mavinject.exe, DLL Injection]()

图片来源： ASEC

AhnLab 安全应急响应中心（ASEC）报告称，威胁行为者滥用了 Microsoft 的一款合法实用程序 mavinject.exe，将恶意动态链接库（DLL）有效载荷注入到合法进程中。这种技术使攻击者能够绕过安全措施并隐藏他们的恶意活动。

mavinject.exe 是 Microsoft 提供的一款合法的命令行实用程序。它旨在将动态链接库（DLL）注入到应用程序虚拟化（App-V）环境中的特定进程中。自 Windows 10 1607 版本以来，该实用程序一直是 Windows 操作系统的默认组件，并且是一个由 Microsoft 签名的受信任可执行文件。因此，许多安全解决方案往往将 mavinject.exe 视为一个安全的应用程序。

ASEC 在其详细分析中指出：“威胁行为者利用这一漏洞，使用 mavinject.exe 将恶意 DLL 有效载荷注入到合法进程中。”

攻击者利用 mavinject.exe 的合法功能，将恶意 DLL 注入到良性进程中。该报告概述了 mavinject.exe 在此过程中使用的以下关键 Windows 应用程序编程接口（API）：

1.OpenProcess（打开进程）：检索目标进程的句柄。

2.VirtualAllocEx（在外部虚拟分配内存）：在目标进程的虚拟内存空间内分配内存。

3.WriteProcessMemory（写入进程内存）：将 DLL 路径写入已分配的内存中。

4.CreateRemoteThread（创建远程线程）：在目标进程中创建一个新线程，并调用 LoadLibraryW 函数来加载并执行恶意 DLL。

通过使用 mavinject.exe，攻击者可以实现外部代码执行并逃避检测。

ASEC 的报告提供了威胁行为者在实际攻击中如何使用 mavinject.exe 的示例：

1.Earth Preta（Mustang Panda）：已观察到这个高级持续性威胁（APT）组织使用 mavinject.exe 将恶意 DLL（如一个后门程序）注入到诸如 waitfor.exe 这样的合法进程中。

2.Lazarus Group：这个威胁组织也使用 mavinject.exe 将恶意 DLL 注入到 explorer.exe 进程中。

在这两种情况下，攻击者都利用了 mavinject.exe 是 Microsoft 合法实用程序这一事实，来绕过安全解决方案并隐藏他们的恶意活动。

ASEC的报告提出了以下检测和响应措施：

****检测措施：****

1.监控使用特定参数（/INJECTRUNNING、/HMODULE）的 mavinject.exe 命令行执行情况。

2.监控诸如 OpenProcess、VirtualAllocEx、WriteProcessMemory 和 CreateRemoteThread 这样的 API 调用情况。

3.追踪 LoadLibraryW 函数的调用路径，查找异常情况。

****响应措施：****

1.实施相关策略，在不使用应用程序虚拟化（App-V）功能时阻止 mavinject.exe 的执行。

2.制定规则以检测进程间的 DLL 注入行为。

3.定期检查正常进程中是否存在异常的 DLL 加载历史记录。

本文翻译自securityonline [原文链接](https://securityonline.info/legitimate-windows-tool-abused-mavinject-exe-used-for-stealthy-dll-injection-by-threat-actors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306763](/post/id/306763)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/legitimate-windows-tool-abused-mavinject-exe-used-for-stealthy-dll-injection-by-threat-actors/)

如若转载,请注明出处： <https://securityonline.info/legitimate-windows-tool-abused-mavinject-exe-used-for-stealthy-dll-injection-by-threat-actors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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