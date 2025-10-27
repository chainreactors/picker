---
title: mavinject.exe 遭利用，黑客绕过安全防线入侵系统
url: https://www.anquanke.com/post/id/306961
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:16.820299
---

# mavinject.exe 遭利用，黑客绕过安全防线入侵系统

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

# mavinject.exe 遭利用，黑客绕过安全防线入侵系统

阅读量**107313**

发布时间 : 2025-04-28 10:48:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/windows-ms-utility-tool/>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者越来越多地利用 mavinject.exe（一款 Microsoft 的合法工具）来绕过安全控制并入侵系统。

这种复杂的攻击技术使黑客能够将恶意活动隐藏在受信任的 Windows 进程背后。

mavinject.exe 是Microsoft应用程序虚拟化注入器，作为Microsoft App – V 环境的一部分，它旨在将代码注入到外部进程中。

自 Windows 10 版本 1607 起，该工具就被默认包含在系统中。由于它是Microsoft进行数字签名的工具，通常会被安全解决方案列入白名单，这使得它成为攻击者绕过检测机制的理想途径。

因为 mavinject.exe 由Microsoft进行了数字签名，通过这种方式代理执行可能会避开安全产品的检测，因为执行过程被伪装在一个合法进程之下。

****技术利用方法****

AhnLab报告称，攻击者主要通过两种方法滥用 mavinject.exe：

****通过 / INJECTRUNNING 进行 DLL 注入****

最常见的技术是使用以下命令将恶意 DLL 注入到正在运行的进程中：

这条命令会强制目标进程加载并执行任意代码。实际上，mavinject 利用了通常在恶意软件中会被标记的 Windows 应用程序编程接口（API）：

1.OpenProcess：获取目标进程的句柄。

2.VirtualAllocEx：在目标进程中分配内存。

3.WriteProcessMemory：将 DLL 路径写入已分配的内存。

4.CreateRemoteThread：创建线程来加载并执行 DLL。

****通过 / HMODULE 进行导入表操作****

一种更为复杂的方法涉及操纵可执行文件的导入地址表：

这种方法会将由指定 DLL 组成的导入表项注入到给定基地址的模块中，从而对攻击实现更精确的控制。

就在两个月前，趋势科技的研究人员揭露了一场由 “Earth Preta”（也被称为 “Mustang Panda”）发起的复杂攻击活动，这是一个高级持续性威胁（APT）组织。

该活动主要针对亚太地区的政府机构，包括越南和马来西亚。

当在受害者系统中检测到 ESET 杀毒软件运行时，“Earth Preta” 利用 mavinject.exe 将恶意有效载荷注入到 waitfor.exe 中。这种注入技术有效地将命令与控制通信隐藏在合法进程之下。

****缓解措施****

安全专家建议采取以下几种应对措施：

1.监控 mavinject.exe 带 / INJECTRUNNING 和 / HMODULE 等参数的命令行执行情况。

2.部署规则来检测与 DLL 注入相关的可疑 API 调用模式。

3.如果在你的环境中不使用Microsoft App – V，考虑删除或禁用 mavinject.exe。

4.实施应用程序控制，在不需要 mavinject.exe 的地方阻止其执行。

研究人员表示：“应对高级威胁的关键在于识别那些看似正常的异常活动。”

随着威胁行为者继续利用 “利用现有资源” 的技术，防御者必须对攻击链中合法系统工具的滥用保持警惕。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/windows-ms-utility-tool/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306961](/post/id/306961)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/windows-ms-utility-tool/)

如若转载,请注明出处： <https://cybersecuritynews.com/windows-ms-utility-tool/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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