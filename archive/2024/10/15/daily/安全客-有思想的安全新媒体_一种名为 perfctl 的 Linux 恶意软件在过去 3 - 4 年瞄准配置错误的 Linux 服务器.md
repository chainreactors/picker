---
title: 一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器
url: https://www.anquanke.com/post/id/300851
source: 安全客-有思想的安全新媒体
date: 2024-10-15
fetch_date: 2025-10-06T18:45:31.330578
---

# 一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器

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

# 一种名为 perfctl 的 Linux 恶意软件在过去 3 - 4 年瞄准配置错误的 Linux 服务器

阅读量**74440**

发布时间 : 2024-10-14 15:52:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/169351/malware/perfctl-malware-targets-misconfigured-linux-servers.html>

译文仅供参考，具体内容表达以及含义原文为准。

perfctl 恶意软件以配置错误的 Linux 服务器为目标，持续部署加密货币矿工和代理劫持软件。
Aqua Nautilus 的研究人员揭露了一种被称为 perfctl 恶意软件的 Linux 恶意软件，在过去 3-4 年中，该恶意软件以配置错误的 Linux 服务器为目标。

恶意代码被用来投放加密货币矿机和代理劫持软件。

Perfctl 是一种针对 Linux 服务器的难以捉摸的持久性恶意软件，它利用 rootkit 隐藏自己的存在，并在新用户登录时停止任何 “嘈杂 ”的活动，一直休眠到服务器再次闲置。在通信方面，它在内部使用 Unix 套接字，在外部使用 TOR。执行后，perfctl 会删除其二进制文件，并作为一项服务在后台运行。

尽管该恶意软件的主要目标是运行加密程序，但专家警告说，它还会执行代理劫持软件。在一次沙盒测试中，一名威胁行为者出于侦察目的访问了该恶意软件的后门。攻击者对服务器进行了分析，并部署了实用程序来调查其环境，更好地了解恶意软件是如何被研究的。

一旦攻击者利用了漏洞或错误配置，perfctl 恶意软件就会从攻击者控制的 HTTP 服务器下载主要有效载荷。有效载荷采用了多层技术，以确保持久性并躲避检测。它将自身移动到 /tmp 目录，以执行它的进程（如 sh）重命名自身，并删除原始二进制文件以掩盖其踪迹。该恶意软件既是下载器，又是本地命令与控制（C2）进程，试图利用 Polkit 漏洞 CVE-2021-4043（又名 PwnKit）进行 root 访问。

恶意代码使用欺骗性的名称将自身复制到不同的磁盘位置，并在服务器上建立后门以进行 TOR 通信。

该恶意软件在投放rootkit的同时，还投放了经过修改的Linux实用程序（如ldd、losof），这些实用程序具有用户地rootkit功能。

![perfctl malware]()

Linux 恶意软件经过打包和加密，以逃避检测。它使用先进的规避技术，如在检测到新用户时停止活动，恶意代码还可以终止竞争恶意软件，以保持对受感染系统的独占访问权。

“作为其命令和控制操作的一部分，恶意软件会打开一个 Unix 套接字，在 /tmp 目录下创建两个目录，并在其中存储影响其操作的数据。这些数据包括主机事件、自身副本的位置、进程名称、通信日志、令牌和其他日志信息。此外，恶意软件还使用环境变量来存储数据，从而进一步影响其执行和行为。报告指出：”所有二进制文件都经过打包、剥离和加密，这表明恶意软件在绕过防御机制和阻碍逆向工程尝试方面做出了巨大努力。该恶意软件还使用了先进的规避技术，例如在检测到 btmp 或 utmp 文件中有新用户时暂停其活动，并终止任何竞争恶意软件，以保持对受感染系统的控制。

为了保持持久性，攻击者修改了 ~/.profile 脚本，以便在用户登录时执行恶意软件，检查 /root/.config/cron/perfcc 是否可执行。如果是，恶意软件就会在合法服务器工作负载之前运行。它还会在 Bash 环境中执行 ~/.bashrc 文件，以在恶意软件后台工作时维持服务器的正常运行。脚本会抑制错误以避免警告。

一个名为 wizlmsh（12kb）的小型二进制文件被放入 /usr/bin，在后台运行，以确保 perfctl 恶意软件的持久性，并验证主要有效载荷（httpd）的执行情况。

“攻击的主要影响是资源劫持。在所有案例中，我们都观察到一个 Monero 加密程序 (XMRIG) 被执行并耗尽了服务器的 CPU 资源。该加密器还进行了打包和加密。报告总结道：”一旦解包和解密，它就会与加密矿池通信。“研究人员说：”要检测 perfctl 恶意软件，可以查看 CPU 使用率是否出现异常峰值，或者如果 rootkit 已经部署在服务器上，系统速度是否变慢。“这些可能表明存在加密货币挖掘活动，尤其是在空闲时间。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/169351/malware/perfctl-malware-targets-misconfigured-linux-servers.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300851](/post/id/300851)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/169351/malware/perfctl-malware-targets-misconfigured-linux-servers.html)

如若转载,请注明出处： <https://securityaffairs.com/169351/malware/perfctl-malware-targets-misconfigured-linux-servers.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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