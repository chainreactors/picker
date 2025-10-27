---
title: APT28 黑客利用 Signal 聊天工具对乌克兰发动新的恶意软件攻击
url: https://www.anquanke.com/post/id/308975
source: 安全客-有思想的安全新媒体
date: 2025-06-26
fetch_date: 2025-10-06T22:52:11.348058
---

# APT28 黑客利用 Signal 聊天工具对乌克兰发动新的恶意软件攻击

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

# APT28 黑客利用 Signal 聊天工具对乌克兰发动新的恶意软件攻击

阅读量**58757**

发布时间 : 2025-06-25 15:59:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/apt28-hackers-use-signal-chats-to-launch-new-malware-attacks-on-ukraine/>

译文仅供参考，具体内容表达以及含义原文为准。

俄罗斯国家支持的威胁组织 APT28 正在使用 Signal 聊天工具针对乌克兰的政府目标，这两个恶意软件家族以前未被记录在案，分别名为 BeardShell 和 SlimAgent。

明确地说，这不是 Signal 的安全问题。相反，由于世界各国政府越来越多地使用该平台，威胁行为者更多地将其作为网络钓鱼攻击的一部分。

乌克兰计算机和应急响应中心（CERT-UA）于 2024 年 3 月首次发现了这些攻击，但当时揭露的有关感染载体的细节非常有限。

一年多后，即 2025 年 5 月，ESET 通知 CERT-UA 有人未经授权访问了 gov.ua 电子邮件帐户，从而引发了新的事件响应。

在这次新的调查中，CERT-UA 发现通过加密信使应用程序 Signal 发送的信息被用于向目标发送恶意文档 (Акт.doc)，该文档使用宏来加载名为 Covenant 的内存驻留后门。

![]()

```
APT28 通过 Signal 进行攻击 来源：CERT-UA CERT-UA
```

Covenant 充当恶意软件加载器，下载一个 DLL (PlaySndSrv.dll) 和一个加载了 shellcode 的 WAV 文件 (sample-03.wav)，加载 BeardShell（一种以前未记录的 C++ 恶意软件）。对于加载器和主要恶意软件有效载荷，都是通过在 Windows 注册表中劫持 COM 来确保持久性的。

![]()

```
为 BeardShell 建立持久性 来源：CERT-UA CERT-UA
```

BeardShell 的主要功能是下载 PowerShell 脚本，使用 “chacha20-poly1305 ”解密并执行这些脚本。执行结果会外泄到命令与控制（C2）服务器，通过 Icedrive API 与服务器进行通信。

在 2024 次攻击中，CERT-UA 还发现了一个名为 SlimAgent 的屏幕截图捕获器，它使用一系列 Windows API 函数（EnumDisplayMonitors、CreateCompatibleDC、CreateCompatibleBitmap、BitBlt、GdipSaveImageToStream）捕获屏幕截图。

这些图像使用 AES 和 RSA 加密，并存储在本地，可能会通过单独的有效载荷/工具外泄到 APT28 的 C2 服务器。

CERT-UA 将此活动归咎于 APT28（他们将其追踪为 UAC-0001），并建议潜在目标监控与 app.koofr.net 和 api.icedrive.net 的网络交互。

APT28 长期以来一直以乌克兰以及美国和欧洲的其他重要组织为目标，主要从事网络间谍活动。

他们是俄罗斯最先进的威胁组织之一，在 2024 年 11 月被 Volexity 曝光使用新颖的 “近邻 ”技术，通过利用附近的 Wi-Fi 网络远程入侵目标。

2025 年，Signal 意外成为与俄罗斯和乌克兰有关的网络攻击的核心。

这一流行的通信平台被滥用于鱼叉式网络钓鱼攻击，这些攻击利用平台的设备链接功能劫持账户，并针对乌克兰的主要目标分发黑暗水晶 RAT。

乌克兰政府代表曾对 Signal 停止与他们合作阻止俄罗斯攻击表示失望。乌克兰官员后来对 Signal 在阻止俄罗斯行动方面缺乏合作表示失望。

不过，Signal 总裁梅雷迪斯-惠特克（Meredith Whittaker）对这一说法表示惊讶，称该平台从未与乌克兰或任何其他国家的政府共享过通信数据。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/apt28-hackers-use-signal-chats-to-launch-new-malware-attacks-on-ukraine/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308975](/post/id/308975)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/apt28-hackers-use-signal-chats-to-launch-new-malware-attacks-on-ukraine/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/apt28-hackers-use-signal-chats-to-launch-new-malware-attacks-on-ukraine/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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