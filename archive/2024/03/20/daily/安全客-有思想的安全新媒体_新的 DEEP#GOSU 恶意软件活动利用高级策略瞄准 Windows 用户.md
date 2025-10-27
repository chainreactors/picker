---
title: 新的 DEEP#GOSU 恶意软件活动利用高级策略瞄准 Windows 用户
url: https://www.anquanke.com/post/id/294085
source: 安全客-有思想的安全新媒体
date: 2024-03-20
fetch_date: 2025-10-04T12:09:33.190648
---

# 新的 DEEP#GOSU 恶意软件活动利用高级策略瞄准 Windows 用户

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

# 新的 DEEP#GOSU 恶意软件活动利用高级策略瞄准 Windows 用户

阅读量**82143**

发布时间 : 2024-03-19 10:44:04

**x**

##### 译文声明

本文是翻译文章，文章来源：https://thehackernews.com/2024/03/new-deepgosu-malware-campaign-targets.html

译文仅供参考，具体内容表达以及含义原文为准。

网络安全公司 Securonix 观察到一种新的精心设计的攻击活动“DEEP#GOSU”，该活动利用 PowerShell 和 VBScript 恶意软件来感染 Windows 系统并获取敏感信息。此外，安全公司表示该活动可能与朝鲜国家资助的名为Kimsuky的组织有关。

安全研究人员 Den Iuzvyk、Tim Peck 和 Oleg Kolesnikov 在技术分析中表示：“ DEEP#GOSU中使用的恶意软件有效负载代表了一种复杂的多阶段威胁，旨在在 Windows 系统上秘密运行，尤其是从网络监控的角度来看。”

“它的功能包括键盘记录、剪贴板监控、动态有效负载执行和数据泄露，以及使用 RAT 软件进行完全远程访问、计划任务以及使用作业自动执行 PowerShell 脚本的持久性。”

感染过程的一个值得注意的方面是，它利用 Dropbox 或 Google Docs 等合法服务进行命令和控制 (C2)，从而允许威胁行为者在未检测到的情况下融入常规网络流量。

最重要的是，使用此类云服务来暂存有效负载可以更新恶意软件的功能或提供其他模块。

据说起点是一个恶意电子邮件附件，其中包含一个 ZIP 存档，其中包含伪装成 PDF 文件（“IMG\_20240214\_0001.pdf.lnk”）的恶意快捷方式文件 (.LNK)。

.LNK 文件嵌入了一个 PowerShell 脚本以及一个诱饵 PDF 文档，前者还可以访问参与者控制的 Dropbox 基础设施来检索和执行另一个 PowerShell 脚本（“ps.bin”）。

第二阶段的 PowerShell 脚本从 Dropbox 获取一个新文件（“r\_enc.bin”），这是一个二进制形式的 .NET 程序集文件，实际上是一个名为TruRat（又名 TutRat 或 C#）的开源远程访问木马RAT）具有记录击键、管理文件和促进远程控制的功能。

值得注意的是，Kimsuky 在AhnLab 安全情报中心 (ASEC) 去年发现的至少两次 活动中使用了 TruRat。

PowerShell 脚本还从 Dropbox 检索到 VBScript（“info\_sc.txt”），该脚本又被设计为运行从云存储服务检索到的任意 VBScript 代码，包括 PowerShell 脚本（“w568232.ps12x”）。

VBScript 还设计为使用 Windows Management Instrumentation ( WMI ) 在系统上执行命令，并在系统上设置计划任务以实现持久性。

VBScript 的另一个值得注意的方面是使用 Google Docs 动态检索 Dropbox 连接的配置数据，从而允许威胁参与者更改帐户信息，而无需更改脚本本身。

下载的 PowerShell 脚本可以收集有关系统的大量信息，并通过向 Dropbox 发出 POST 请求来泄露详细信息。

研究人员表示：“该脚本的目的似乎是作为一种工具，通过 Dropbox 与命令和控制 (C2) 服务器进行定期通信。” “其主要目的包括加密、窃取或下载数据。”

换句话说，它充当控制受感染主机的后门，并持续保留用户活动日志，包括击键、剪贴板内容和前台窗口。

安全研究人员 Ovi Liber 详细介绍了与朝鲜有关的ScarCruft在网络钓鱼电子邮件中的韩文文字处理器 (HWP) 诱饵文档中嵌入恶意代码，以传播 RokRAT 等恶意软件。

“该电子邮件包含一个 HWP 文档，其中嵌入了 BAT 脚本形式的 OLE 对象，”Liber说。“一旦用户单击 OLE 对象，BAT 脚本就会执行，进而在受害者计算机上创建基于 PowerShell 的反射 DLL 注入攻击。”

它还利用了名为MeshAgent的合法远程桌面解决方案来安装AndarLoader 和 ModeLoader（一种旨在执行命令的 JavaScript 恶意软件）等恶意软件。

“这是Andariel 集团首次确认使用 MeshAgent ，”ASEC表示。“Andariel 集团不断滥用国内公司的资产管理解决方案，在横向移动过程中传播恶意软件，从过去的 Innorix Agent 开始。”

本文翻译自https://thehackernews.com/2024/03/new-deepgosu-malware-campaign-targets.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294085](/post/id/294085)

安全KER - 有思想的安全新媒体

本文转载自: https://thehackernews.com/2024/03/new-deepgosu-malware-campaign-targets.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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