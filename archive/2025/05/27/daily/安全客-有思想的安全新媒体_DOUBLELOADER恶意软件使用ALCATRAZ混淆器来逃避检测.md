---
title: DOUBLELOADER恶意软件使用ALCATRAZ混淆器来逃避检测
url: https://www.anquanke.com/post/id/307752
source: 安全客-有思想的安全新媒体
date: 2025-05-27
fetch_date: 2025-10-06T22:23:26.632181
---

# DOUBLELOADER恶意软件使用ALCATRAZ混淆器来逃避检测

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

# DOUBLELOADER恶意软件使用ALCATRAZ混淆器来逃避检测

阅读量**102784**

发布时间 : 2025-05-26 13:14:31

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/doubleloader-malware-uses-alcatraz-obfuscator-to-evade-detection/>

译文仅供参考，具体内容表达以及含义原文为准。

![DOUBLELOADER 恶意软件,ALCATRAZ 混淆器]()

Elastic Security Labs已经确定了一个名为“DOUBLELOADER”的新恶意软件家族,它利用ALCATRAZ(一种游戏黑客启发的混淆者)与RHADAMANTHYS信息窃取器一起部署高级规避技术。

虽然ALCTRAZ起源于游戏黑客场景,但它现在已被网络犯罪分子和高级持续威胁(APT)参与者选中,允许恶意软件作者应用分层混淆技术,[显着延迟检测和分析。](https://securityonline.info/mcafee-premium-review-all-around-protection-for-your-digital-life-but-is-it-the-best/)

*“DOUBLELOADER的一个有趣的属性是,它受到开源混淆器ALCATRAZ的保护……在电子犯罪领域观察到并用于有针对性的入侵*,”Elastic Security reportedLabs报道。

该恶意软件于12月首次出现,其特征是通用后门,通常与已知的信息窃取者RHADAMANTHYS配对。DOUBLELOADER 使用直接系统调用,如 NtOpenProcess、NtWriteVirtualMemory 和 NtCreateThreadEx 将无后端代码注入 explorer.exe。

*[“恶意软件收集主机信息](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/),请求自己的更新版本,并开始向硬编码IP(185.147.125.81)信标*,”Elastic的研究人员指出。

ALCATRAZ于2023年首次发布,为用户提供了bin2bin转换流程,使他们能够混淆已经编译的二进制文件,而无需更改源代码。这种便利性使其在业余爱好者和威胁行为者中都很受欢迎。

Elastic Labs 识别了嵌入在 DOUBLELOADER 中的多种混淆技术,包括:

* 入口点混淆: 隐藏实际的程序开始使用计算的跳跃和位数技巧。
* 反拆卸:添加误导性跳转指令(0xEB)以破坏IDA等工具中的线性拆解。
* 指令突变:用复杂的指令链替换简单的操作(例如,添加)。
* 不断展开:通过位操作模糊已知的常数,使值乍一看是无法读的值。
* LEA混淆:在间接内存荷载和算术中隐藏值。
* 控制流扁平化:使用基于调度器的循环破坏可读分支逻辑,该循环使用状态变量。

*“控制流量扁平化等混淆技术继续成为分析师的障碍*,”报告警告说。

弹性安全实验室并没有停止分析——他们发布了IDA Python脚本的工具和示例[,](https://github.com/elastic/labs-releases/tree/main/tools/alcatraz)以帮助逆向工程师和恶意软件分析师消除受ALCATRAZ保护的二进制文件。

他们还使用社区工具,如D810 IDA插件,对混淆的控制流进行逆向工程,展示如何扁平化和清洁复杂的结构。

*“虽然恶意软件分析报告通常显示最终结果,但很大一部分时间往往用于预先消除混淆*,”该团队解释说。

本文翻译自securityonline [原文链接](https://securityonline.info/doubleloader-malware-uses-alcatraz-obfuscator-to-evade-detection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307752](/post/id/307752)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/doubleloader-malware-uses-alcatraz-obfuscator-to-evade-detection/)

如若转载,请注明出处： <https://securityonline.info/doubleloader-malware-uses-alcatraz-obfuscator-to-evade-detection/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Stealth Falcon 在复杂的网络间谍活动中利用新的零日漏洞 (CVE-2025-33053)](/post/id/308352)

  2025-06-11 16:12:52

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