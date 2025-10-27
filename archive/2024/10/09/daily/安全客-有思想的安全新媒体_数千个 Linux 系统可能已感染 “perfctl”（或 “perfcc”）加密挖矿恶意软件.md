---
title: 数千个 Linux 系统可能已感染 “perfctl”（或 “perfcc”）加密挖矿恶意软件
url: https://www.anquanke.com/post/id/300621
source: 安全客-有思想的安全新媒体
date: 2024-10-09
fetch_date: 2025-10-06T18:48:38.767172
---

# 数千个 Linux 系统可能已感染 “perfctl”（或 “perfcc”）加密挖矿恶意软件

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

# 数千个 Linux 系统可能已感染 “perfctl”（或 “perfcc”）加密挖矿恶意软件

阅读量**116773**

发布时间 : 2024-10-08 15:00:49

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2024/10/07/perfctl-perfcc-cryptomining-linux/>

译文仅供参考，具体内容表达以及含义原文为准。

上周， Aqua Security的研究人员透露，数以千计的Linux系统可能感染了高度难以捉摸且持久的“perfctl”（或“perfcc”）加密挖矿恶意软件，而其他许多系统仍可能面临被入侵的风险。

“在所有观察到的攻击中，恶意软件被用来运行加密挖矿程序，在某些情况下，我们还检测到代理劫持软件的执行，”他们分享道。

“Perfctl”恶意软件

虽然实际的加密挖掘是由 XMRIG Monero加密挖掘软件执行的，但恶意软件Perf ctl的名称来自于在受影响系统上建立的加密挖矿程序的名称。（受影响的用户反复提及这个过程，多年来他们一直在网上论坛上寻找补救建议。）

“通过将“perf”（Linux性能监控工具）和“ctl”（通常用于指示命令行工具中的控制）结合起来，恶意软件作者设计了一个看起来合法的名字。这使得用户或管理员在初始调查期间更容易忽略，因为它与典型的系统进程融合在一起，”研究人员解释道。

威胁行为者通过利用已知漏洞（例如 RocketMQ）或20000种错误配置（例如Selenium Grid的默认配置中缺乏身份验证）安装恶意软件。

初始下载的有效载荷（安装二进制文件，实际上是一个多用途的恶意软件放入器）从内存中复制到/tmp目录中的新位置，并从那里运行新的二进制代码。原来的进程和二进制文件被终止/删除，新的进程作为一个滴执行器和一个本地命令与控制（C2）进程起作用。

隐密术

![]()

“perfctl”攻击流程（来源:Aqua Security）

恶意软件：

包含并使用CVE-2021-4034（又名PwnKit）的漏洞，试图获取完整根权限

修改现有脚本，以确保恶意软件的执行并抑制mesg错误（可能指向恶意执行），并丢弃一个二进制，用于验证主负载的执行

将自己从内存复制到其他六个位置（文件名模仿常规系统文件的名称）

丢弃rootkit以隐藏其存在并确保持久性、改变网络流量等。

丢弃几个木马化的Linux实用程序，以隐藏特定的攻击元素（例如，在攻击过程中创建的cron作业、加密程序的CPU消耗、恶意软件使用的恶意库和依赖项），以防止开发人员或安全工程师指向攻击机器的对象

在TOR上使用Unix插座进行外部通信

丢弃并执行 XMRIG 加密算法，偶尔还会执行代理劫持软件（将机器绑定到代理网络中）

这个恶意软件的另一个有趣之处在于，它在新用户登录服务器时会低调（即停止所有加密挖矿活动），正如受影响的用户所指出的那样。

检测、移除和缓解

在加密劫持中，攻击者设法对用户隐瞒妥协的时间越长，他们最终“赚”的钱就越多。

这就是为什么攻击者不遗余力地做到隐蔽和坚持。

虽然一些用户可能暂时不会太担心他们的系统被用于加密或代理，但他们应该重新考虑自己的立场，因为危险可能比他们想象的更大。

“（我们）还观察到恶意软件充当安装其他恶意软件系列的后门，”研究人员指出。

可以通过检查目录、进程、系统日志和网络流量来发现系统中的“perfctl”恶意软件。Aqua为Linux系统的用户和管理员分享了妥协指标和风险缓解建议。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2024/10/07/perfctl-perfcc-cryptomining-linux/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300621](/post/id/300621)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2024/10/07/perfctl-perfcc-cryptomining-linux/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/10/07/perfctl-perfcc-cryptomining-linux/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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