---
title: 基于Linux系统的联想网络摄像头漏洞可被远程利用发起BadUSB攻击
url: https://www.anquanke.com/post/id/311064
source: 安全客-有思想的安全新媒体
date: 2025-08-12
fetch_date: 2025-10-07T00:16:37.628412
---

# 基于Linux系统的联想网络摄像头漏洞可被远程利用发起BadUSB攻击

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

# 基于Linux系统的联想网络摄像头漏洞可被远程利用发起BadUSB攻击

阅读量**73576**

发布时间 : 2025-08-11 17:22:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：thehackernews

原文地址：<https://thehackernews.com/2025/08/linux-based-lenovo-webcams-flaw-can-be.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员披露称，部分联想摄像头型号存在漏洞，可能被攻击者**转化为 BadUSB 攻击设备**。

“这使得远程攻击者能够**隐蔽地注入按键指令**，并在**不依赖宿主操作系统**的情况下发动攻击。”固件安全公司 Eclypsium 的研究员 Paul Asadoorian、Mickey Shkatov 和 Jesse Michael 在与 The Hacker News 分享的报告中表示。该漏洞被命名为 **BadCam**，并于今日在 DEF CON 33 安全大会上首次公布。

这很可能是首次证明，威胁行为者一旦掌控了已经连接到计算机的基于 Linux 的 USB 外设，就能将其武器化用于恶意行为。

在假设的攻击场景中，攻击者可以利用该漏洞**向受害者寄送植入后门的摄像头**，或在获得物理接触的情况下将其接入目标电脑，然后通过远程指令控制计算机并开展后续攻击。

BadUSB 攻击最早在 2014 年由安全研究员 Karsten Nohl 和 Jakob Lell 在 Black Hat 大会上演示。这类攻击利用了 **USB 固件层面的先天漏洞**，可对其重新编程，从而在受害者电脑上悄悄执行命令或运行恶意程序。

正如 Ivanti 公司上月末在一份威胁解读中所述：“与传统存在于文件系统、可被杀毒软件发现的恶意软件不同，BadUSB **潜藏在固件层**。一旦连接到计算机，BadUSB 设备可以模拟键盘输入恶意指令、安装后门或键盘记录器、重定向网络流量，甚至窃取敏感数据。”

![]()

近年来，谷歌旗下的 Mandiant 与美国联邦调查局（FBI）均曾警告，名为 FIN7 的以经济利益为动机的威胁团伙曾通过邮寄“BadUSB”恶意 USB 设备给美国企业，以投递名为 **DICELOADER** 的恶意软件。

Eclypsium 的最新发现表明，一些运行 Linux 的 USB 外设（如网络摄像头）即便最初并无恶意用途，也可能被远程劫持并转化为 BadUSB 设备，而**无需被物理拔出或替换**。这意味着攻击手法有了重大升级。

![]()

研究人员指出：“攻击者一旦在系统上获得远程代码执行权限，就能重刷已连接的基于 Linux 的摄像头固件，使其**伪装成恶意的人机接口设备（HID）**或模拟其他 USB 设备。”

一旦被武器化，这样一台看似普通的摄像头不仅能注入按键、投递恶意载荷，还能成为长期潜伏的据点，而且对外依然保持普通摄像头的外观和功能。

此外，能够修改摄像头固件的攻击者还能实现更高等级的**持久化攻击**——即便受害者清空硬盘、重装操作系统，仍可能再次被感染。

此次发现的漏洞存在于 **Lenovo 510 FHD 与 Lenovo Performance FHD 摄像头**中，问题源于设备未对固件进行有效验证，因此在运行带有 USB Gadget 支持的 Linux 系统时，容易被彻底攻陷并用于 BadUSB 攻击。

在 2025 年 4 月向联想进行负责任披露后，该公司已发布固件更新（版本 4.8.0）以修复漏洞，并与中国芯片厂商 SigmaStar 合作推出了修补工具。

Eclypsium 表示：“这种首次被验证的攻击方式揭示了一个隐蔽但极具危害的途径：无论在企业还是消费领域，计算机往往会**信任其内部和外部外设**，即便这些外设本身能运行独立操作系统并接受远程指令。”

“在基于 Linux 的摄像头场景下，未签名或保护不足的固件允许攻击者不仅能控制当前宿主，还能在摄像头连接到其他设备时继续传播感染，从而绕过传统安全防护。”

本文翻译自thehackernews [原文链接](https://thehackernews.com/2025/08/linux-based-lenovo-webcams-flaw-can-be.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311064](/post/id/311064)

安全KER - 有思想的安全新媒体

本文转载自: [thehackernews](https://thehackernews.com/2025/08/linux-based-lenovo-webcams-flaw-can-be.html)

如若转载,请注明出处： <https://thehackernews.com/2025/08/linux-based-lenovo-webcams-flaw-can-be.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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