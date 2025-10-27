---
title: AsyncRAT 恶意软件活动利用 Bitbucket 发起多阶段攻击
url: https://www.anquanke.com/post/id/300743
source: 安全客-有思想的安全新媒体
date: 2024-10-12
fetch_date: 2025-10-06T18:51:44.055808
---

# AsyncRAT 恶意软件活动利用 Bitbucket 发起多阶段攻击

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

# AsyncRAT 恶意软件活动利用 Bitbucket 发起多阶段攻击

阅读量**73734**

|![](https://p0.ssl.qhimg.com/sdm/30_30_100/t01f942715e2a0f1a23.png)

发布时间 : 2024-10-11 10:31:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/asyncrat-malware-campaign-exploits-bitbucket-to-deliver-multi-stage-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

G DATA 安全实验室（G DATA Security Lab）最近发现了一个利用流行代码托管平台 Bitbucket 部署著名远程访问木马（RAT）AsyncRAT 的复杂恶意软件活动。报告称，攻击者采用了多阶段攻击策略，利用 Bitbucket 托管和分发恶意有效载荷，同时躲避检测。

![AsyncRAT analysis]()

恶意软件操作员使用多层 Base64 编码来混淆代码，掩盖攻击的真实性质。“报告解释说：”在剥开这些层级后，我们能够揭开整个事件的来龙去脉，以及我们在分析 AsyncRAT 有效载荷传输时发现的关键入侵指标（IOC）。

Bitbucket 作为软件开发平台的合法声誉使其成为网络犯罪分子青睐的目标。攻击者利用 Bitbucket 资源库托管各种恶意有效载荷，包括 AsyncRAT。研究人员指出：“攻击者转向 Bitbucket 这个流行的代码托管平台来托管恶意有效载荷，”他们强调，这种方法为传播恶意软件提供了 “合法性 ”和 “可访问性”。

攻击开始于一封包含恶意 VBScript 文件的钓鱼邮件，该文件名为 “01 DEMANDA LABORAL.vbs”，可执行 PowerShell 命令。这个初始阶段通过多层字符串操作和 Base64 编码混淆和传递有效载荷。“报告指出：”VBScript 构建并执行 PowerShell 命令，有效地将攻击过渡到下一阶段。

在第二阶段，PowerShell 脚本从 Bitbucket 资源库下载一个文件。这个名为 “dllhope.txt ”的文件是一个 Base64 编码的有效载荷，它被解码为一个 .NET 编译文件，从而揭示了 AsyncRAT 恶意软件的真实本质。

一旦成功发送，AsyncRAT 就能让攻击者完全远程控制受感染的系统。“G DATA 的分析证实：”AsyncRAT 为攻击者提供了对受感染机器的广泛控制，使他们能够执行各种恶意活动。这些活动包括远程桌面控制、文件管理、键盘记录、网络摄像头和麦克风访问以及执行任意命令。

报告还强调了攻击者利用反虚拟化检查来避免在沙盒环境中被发现。“G DATA 表示：”如果标志参数包含‘4’，代码就会检查是否存在 VMware 或 VirtualBox 等虚拟化工具，从而避免分析。持续性是通过多种机制建立的，包括修改 Windows 注册表和创建启动快捷方式，确保恶意软件即使在系统重启后也能保持活跃。

本文翻译自securityonline [原文链接](https://securityonline.info/asyncrat-malware-campaign-exploits-bitbucket-to-deliver-multi-stage-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300743](/post/id/300743)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/asyncrat-malware-campaign-exploits-bitbucket-to-deliver-multi-stage-attack/)

如若转载,请注明出处： <https://securityonline.info/asyncrat-malware-campaign-exploits-bitbucket-to-deliver-multi-stage-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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