---
title: 恶意广告：虚假流行软件广告提供新的 MadMxShell 后门
url: https://www.anquanke.com/post/id/295890
source: 安全客-有思想的安全新媒体
date: 2024-04-24
fetch_date: 2025-10-04T12:14:48.811655
---

# 恶意广告：虚假流行软件广告提供新的 MadMxShell 后门

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

# 恶意广告：虚假流行软件广告提供新的 MadMxShell 后门

阅读量**65778**

发布时间 : 2024-04-23 10:35:11

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.hackread.com/fake-popular-software-ads-madmxshell-backdoor/>

译文仅供参考，具体内容表达以及含义原文为准。

在最近一波网络攻击中，IT 专业人员已成为Zscaler ThreatLabz 研究人员 Roy Tay 和 Sudeep Singh 发现的狡猾恶意广告活动的目标。

根据该公司的研究，该活动利用欺骗性在线广告来传播一个名为“MadMxShell”的前所未见的后门。这一切都始于 2024 年 3 月，当时 Zscaler ThreatLabz 发现一个威胁参与者使用相似的域来分发 MadMxShell，利用 DLL 侧载、DNS 协议滥用和内存取证安全解决方案。

研究人员认为，攻击者展示了一种经过精心策划的方法。 2023 年 11 月至 2024 年 3 月期间，攻击者注册了多个与流行 IP 扫描仪和网络管理软件非常相似的域名，包括 Advanced IP Scanner、Angry IP Scanner、Paessler 的 PRTG IP Scanner、Manage Engine 以及与 VLAN 相关的网络管理任务。

这种策略被称为“错字抢注”。这使得域名很有可能出现在热门搜索中，并且 IT 专业人员可能会错误地点击恶意广告。

一旦点击，广告就会将用户重定向到一个看起来像正版软件供应商网站的登陆页面。在这里，他们会看到一个可下载的文件，但他们并不知道该文件包含 MadMxShell 后门。

[![虚假流行软件广告提供新的 MadMxShell 后门]()](https://www.hackread.com/wp-content/uploads/2024/04/fake-popular-software-ads-madmxshell-backdoor-2.jpg)

根据 Zscaler 的博客文章，MadMxShell 后门采用多阶段部署过程，旨在逃避传统安全解决方案的检测。初始有效负载利用 DLL 侧面加载，这是一种欺骗合法程序加载恶意库文件的技术。然后，该恶意库会下载其他组件，与攻击者的命令和控制 (C2) 服务器建立通信。

MadMxShell 最令人关注的方面之一是它使用 DNS MX 记录查询进行 C2 通信。该技术以非常规方式利用标准域名系统 (DNS) 协议来掩盖与攻击者基础设施的通信。此外，MadMxShell 采用反转储技术来阻止内存分析，使安全研究人员难以了解其内部工作原理。

为了降低风险，请警惕不请自来的广告，启用弹出窗口拦截器，维护强大的安全软件，并教育员工了解恶意广告和社会工程策略的危险。

Sectigo 产品高级副总裁Jason Soroko对新活动发表了评论。 “防御者通常不会在电子邮件交换 DNS 流量中寻找恶意控制通信 (C2)，因此在这种情况下，攻击者找到了隐藏的地方。攻击者还采用了一种阻止内存“转储”的技术，以供端点安全解决方案进行分析。”Jason 解释道。

“恶意广告并不新鲜，然而，这里使用的恶意软件技术表明攻击者的技术管道很深，并且大量的思想已经隐藏在网络和操作系统的黑暗角落，”他希望。

本文翻译自 [原文链接](https://www.hackread.com/fake-popular-software-ads-madmxshell-backdoor/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295890](/post/id/295890)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.hackread.com/fake-popular-software-ads-madmxshell-backdoor/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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