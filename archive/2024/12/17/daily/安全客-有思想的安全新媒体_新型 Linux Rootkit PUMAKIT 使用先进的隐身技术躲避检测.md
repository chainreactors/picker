---
title: 新型 Linux Rootkit PUMAKIT 使用先进的隐身技术躲避检测
url: https://www.anquanke.com/post/id/302745
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:42.229918
---

# 新型 Linux Rootkit PUMAKIT 使用先进的隐身技术躲避检测

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

# 新型 Linux Rootkit PUMAKIT 使用先进的隐身技术躲避检测

阅读量**87313**

发布时间 : 2024-12-16 11:23:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种名为 PUMAKIT 的新型 Linux rootkit，它具有升级权限、隐藏文件和目录、从系统工具中隐藏自身等功能，同时还能躲避检测。

Elastic 安全实验室的研究人员 Remco Sprooten 和 Ruben Groenewoud 在周四发布的一份技术报告中说：“PUMAKIT 是一种复杂的可加载内核模块（LKM）rootkit，它采用先进的隐身机制来隐藏自己的存在，并保持与命令控制服务器的通信。”

该公司的分析来自今年 9 月初上传到 VirusTotal 恶意软件扫描平台的人工制品。

该恶意软件的内部结构基于一个多阶段架构，包括一个名为 “cron ”的滴管组件、两个内存驻留可执行文件（“/memfd:tgt ”和“/memfd:wpn”）、一个LKM rootkit（“puma.ko”）和一个名为Kitsune（“lib64/libs.so”）的共享对象（SO）用户域rootkit。

它还使用 Linux 内部函数跟踪器（ftrace）挂钩多达 18 种不同的系统调用和各种内核函数，如 “prepare\_creds ”和 “commit\_creds”，以改变核心系统行为并实现其目标。

研究人员说：“PUMA 使用独特的方法进行交互，包括使用 rmdir() 系统调用进行权限升级，以及使用专门的命令提取配置和运行时信息。”

研究人员说：“通过分阶段部署，LKM rootkit 确保只有在满足特定条件（如安全启动检查或内核符号可用性）时才会激活。这些条件通过扫描Linux内核来验证，所有必要的文件都以ELF二进制文件的形式嵌入到滴管中。”

可执行文件“/memfd:tgt ”是默认的 Ubuntu Linux Cron 二进制文件，未作任何修改，而“/memfd:wpn ”则是 rootkit 的加载器，前提是满足条件。LKM rootkit 包含一个嵌入式 SO 文件，用于从用户空间与菜鸟进行交互。

Elastic 公司指出，感染链的每个阶段都旨在隐藏恶意软件的存在，并在释放 rootkit 之前利用内存驻留文件和特定检查。该公司告诉《黑客新闻》，现阶段还不能将 PUMAKIT 归咎于任何已知的威胁行为者或组织。

“PUMAKIT是一种复杂而隐蔽的威胁，它使用了系统调用挂钩、内存驻留执行和独特的权限升级方法等先进技术。它的多体系结构设计凸显了针对 Linux 系统的恶意软件日益复杂，”研究人员总结道。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302745](/post/id/302745)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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