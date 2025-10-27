---
title: TransferPlayer恶意软件被揭露：启用IPFS的加载器部署具有混淆精度的勒索软件和后门
url: https://www.anquanke.com/post/id/307440
source: 安全客-有思想的安全新媒体
date: 2025-05-17
fetch_date: 2025-10-06T22:26:29.941616
---

# TransferPlayer恶意软件被揭露：启用IPFS的加载器部署具有混淆精度的勒索软件和后门

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

# TransferPlayer恶意软件被揭露：启用IPFS的加载器部署具有混淆精度的勒索软件和后门

阅读量**62454**

发布时间 : 2025-05-16 15:31:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/transferloader-malware-unmasked-ipfs-enabled-loader-deploys-ransomware-and-backdoors-with-obfuscation-precision/>

译文仅供参考，具体内容表达以及含义原文为准。

![TransferLoader, IPFS]()

Zscaler ThreatLabz发现了一个名为TransferLoader的新型危险恶意软件加载器,至少自2025年2月以来在野外积极使用。这种先进的模块化威胁不仅仅是另一个滴管 – 它是一个高度混淆,反分析的恶意软件平台,提供从隐身后门到Morpheus勒索软件的有效载荷,观察到针对美国律师事务所的攻击。

*“TransferLoader是一个新的恶意软件加载器……具有多个组件,包括下载器,后门和后门的加载器*,”ThreatLabz写道。

下载器使用自定义标头通过HTTPS检索恶意有效载荷,并使用bitwise-XOR循环解密它们。它可以显示诱饵 PDF 或静默重新启动资源管理器进程以隐藏其执行。

*“下载器的主要目标是从C2服务器下载额外的有效载荷并执行诱饵文件*,”分析解释说。

专门用于在内存中执行后门,后门加载器组件读取配置数据,确保执行上下文(例如,在 explorer.exe 或 wordpad.exe 内部),并设置 COM 劫持。

它还使用命名的管道进行配置命令,并可以接收更新C2服务器,设置睡眠计时器或在内存中执行任意PE文件的指令。

操作的主要操作,后门执行任务,包括:

* 执行远程 shell 命令
* 文件上传/下载
* 系统侦察和数据收集
* 自我清除和清理

当主C2不可用时,它会联系星际文件系统(IPFS)以检索新的C2位置。

*“后门利用分散的InterPlanetary文件系统(IPFS)点对点平台作为回退通道,用于更新命令和控制(C2)服务器。*

它支持TCP和HTTP,使用自定义流密码加密通信 – 完成错误块交换和嵌套加密层。

TransferLoader旨在逃避静态和动态分析:

* 垃圾代码破坏拆解
* 解密例程依赖于自定义的Base32方案和AES变体
* 命令行参数和进程名称在执行前经过验证
* [Environment](https://securityonline.info/lastpass-your-digital-life-secured-and-simplified-review-recommendation/)通过在过程环境块(PEB)中调试调试检测

*TransferLoader及其有效载荷包含反分析方法……包括垃圾代码块,*动态API分辨率和运行时字符串解密。

[ransomware](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/)虽然报告中没有对Morpheus勒索软件进行深入分析,但通过TransferLoader的交付意味着装载机正在演变成一个多用途的交付平台。

*“考虑到TransferLoader在部署包括勒索软件在内的其他有效载荷方面的一贯使用[ransomware](https://securityonline.info/bitdefender-premium-security-review-the-ultimate-all-in-one-security-privacy-fortress/),*我们预计威胁行为者将在未来的攻击中继续依赖它。

本文翻译自securityonline [原文链接](https://securityonline.info/transferloader-malware-unmasked-ipfs-enabled-loader-deploys-ransomware-and-backdoors-with-obfuscation-precision/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307440](/post/id/307440)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/transferloader-malware-unmasked-ipfs-enabled-loader-deploys-ransomware-and-backdoors-with-obfuscation-precision/)

如若转载,请注明出处： <https://securityonline.info/transferloader-malware-unmasked-ipfs-enabled-loader-deploys-ransomware-and-backdoors-with-obfuscation-precision/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [每日安全热点](/tag/%E6%AF%8F%E6%97%A5%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**5赞

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