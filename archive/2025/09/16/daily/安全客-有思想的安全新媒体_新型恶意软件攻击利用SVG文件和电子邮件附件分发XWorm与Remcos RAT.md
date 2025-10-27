---
title: 新型恶意软件攻击利用SVG文件和电子邮件附件分发XWorm与Remcos RAT
url: https://www.anquanke.com/post/id/312157
source: 安全客-有思想的安全新媒体
date: 2025-09-16
fetch_date: 2025-10-02T20:11:19.015537
---

# 新型恶意软件攻击利用SVG文件和电子邮件附件分发XWorm与Remcos RAT

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

# 新型恶意软件攻击利用SVG文件和电子邮件附件分发XWorm与Remcos RAT

阅读量**51686**

发布时间 : 2025-09-15 18:21:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-malware-attack-leverages-svgs/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现了一起复杂的恶意软件活动，该活动利用**SVG（可缩放矢量图形）文件**和电子邮件附件分发危险的远程访问木马，即**XWorm**和**Remcos RAT**。

这一新兴威胁标志着攻击方法的显著进化，因为威胁行为者越来越多地转向**非传统文件格式**以绕过常规安全防御。

该活动采用多种投递载体，包括包含恶意EML文件的**直接电子邮件附件**，以及托管在ImageKit等可信平台上的**URL**。

这些ZIP压缩包中包含**高度混淆的BAT脚本**，作为初始感染阶段，利用高级技术规避静态检测机制。

恶意软件的**无文件执行方式**使其能够完全在内存中运行，这使得传统端点保护解决方案的检测难度大大增加。

Seqrite研究人员在分析中识别出**两个不同的活动变体**，揭示了攻击者不断改进技术的威胁态势。

第一个活动通过电子邮件附件直接投递BAT脚本，而第二个活动则引入**嵌入JavaScript的SVG文件**作为新的投递机制。

![]()

这些SVG文件看似合法的图像文件，但包含**嵌入的脚本**，当在易受攻击的环境中渲染或嵌入钓鱼页面时，会自动触发恶意载荷下载。

攻击链在执行方法上展现出极高的复杂性。初始ZIP文件解压后，受害者会遇到一个**高度混淆的BAT脚本**，该脚本设计为看似良性，同时执行复杂的恶意操作。

该脚本利用**PowerShell执行内存中载荷注入**，有效绕过传统的基于文件的检测系统。

### **高级规避与持久化机制**

恶意软件采用针对Windows核心安全机制的**复杂规避技术**。PowerShell组件通过**动态.NET反射和委托创建**，以编程方式禁用**AMSI（反恶意软件扫描接口）** 和**ETW（Windows事件跟踪）**。

![]()

攻击解析包括**GetProcAddress、GetModuleHandle、VirtualProtect和AmsiInitialize**在内的原生函数，以定位并在内存中修补**AmsiScanBuffer函数**。

持久化机制涉及在**Windows启动文件夹中创建BAT文件**，确保系统重启或用户登录时自动执行。

PowerShell脚本搜索隐藏在批处理文件注释中的**Base64编码载荷**，专门针对以三冒号标记为前缀的行。

这些载荷经过**多层解密**，包括使用硬编码密钥的**AES解密**和**GZIP解压**，然后才最终执行。

加载器组件作为关键中介，使用**Assembly.Load操作**直接在内存中提取并执行嵌入式.NET程序集。

这种方法消除了对基于磁盘的文件创建的需求，**显著降低了检测概率**，同时保持部署XWorm和Remcos RAT载荷的完整操作能力。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-malware-attack-leverages-svgs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312157](/post/id/312157)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-malware-attack-leverages-svgs/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-malware-attack-leverages-svgs/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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