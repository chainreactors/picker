---
title: 俄罗斯 Sandworm 黑客瞄准了乌克兰 20 个关键组织
url: https://www.anquanke.com/post/id/295905
source: 安全客-有思想的安全新媒体
date: 2024-04-24
fetch_date: 2025-10-04T12:14:46.280924
---

# 俄罗斯 Sandworm 黑客瞄准了乌克兰 20 个关键组织

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

# 俄罗斯 Sandworm 黑客瞄准了乌克兰 20 个关键组织

阅读量**73668**

发布时间 : 2024-04-23 10:54:08

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cert.gov.ua/article/6278706>

译文仅供参考，具体内容表达以及含义原文为准。

乌克兰CERT-UA政府计算机应急响应小组披露了Sandworm组织的恶意计划，旨在破坏约20个能源、水和热力供应（OKI）的信息和通信系统（ICS）的稳定运行。 ）乌克兰十个地区的企业。

除了自 2022 年以来已知的 QUEUESEED（KNUCKLETOUCH、ICYWELL、WRONGSENS、KAPEKA）后门之外，还发现攻击者在立即事件响应期间安装了新工具，即 LOADGRIP 和 BIASBOAT（QUEUESEED 的 Linux 变体）。计算机（Linux操作系统）设计用于使用国内生产的专用软件（SPZ）实现工艺过程管理（ASUTP）过程的自动化。值得注意的是，BIASBOAT 是作为针对特定服务器的加密文件呈现的，攻击者使用了之前获得的“machine-id”值。

CERT-UA 专家已经确认了至少三个“供应链”受到损害的事实，与此相关的是，最初未经授权的访问的情况要么与包含软件书签和漏洞的 SDR 的安装有关，要么与 SDR 的安装有关。由于供应商员工的全职技术能力能够访问 ICS 组织以获得支持和技术支持。

考虑到 OKI ICS 内带有 SDR 的 PC 的运行，犯罪分子利用它们进行横向移动并开发与企业网络相关的网络攻击。例如，在此类计算机的 SDR 目录中发现了预先创建的 PHP Web shell WEEVELY、PHP 隧道 REGEORG.NEO 或 PIVOTNACCI。

在2024年3月7日至2024年3月15日期间，CERT-UA专家采取措施通知所有已识别的企业，并调查和应对相关ICS中的网络威胁，其中确定了主要危害的情况，恶意软件被删除和分析，构建事件事件年表，提供服务器和活动网络设备配置方面的帮助，并安装安全技术（在一些企业中，LOADGRIP/BIASBOAT于2023年创建）。

应该强调的是，攻击者在运行 Windows 操作系统的 PC 上使用了恶意软件 QUEUESEED 和 GOSSIPFLOW，自 2022 年以来，在 UAC-0133 组织对供水设施进行破坏性网络攻击的背景下，这些软件一直被追踪，特别是使用 SDELETE 。因此，UAC-0133 是 UAC-0002 (Sandworm/APT44) 的子簇，具有很高的置信度。

请注意，以下因素促成了网络攻击的实施：

在限制访问/访问互联网和组织本身的 ICS（它们在其中发挥作用）的情况下，服务器与供应商 SDR 的服务器不正确的分割（缺乏隔离），用作 ACS 的一个要素
供应商对向消费者提供的软件安全的疏忽态度；特别是，在对源代码进行粗略分析时，会发现允许远程代码执行（RCE）的平庸漏洞。
CERT-UA 假设，未经授权访问大量供热、供水和能源供应设施的 ICS，将用于增强 2024 年春季导弹袭击乌克兰基础设施的效果。

QUEUESEED是一个使用C++编程语言开发的恶意程序。获取有关计算机的基本信息（操作系统、语言、用户名），执行从管理服务器接收的命令并发送结果。功能：读/写文件、执行命令（作为单独的进程或通过 %COMSPEC% /c）、更新配置、自删除。 HTTPS 用于与管理服务器交互。数据以JSON格式传输，并使用RSA+AES加密。后门的配置文件，特别是包含管理服务器的 URL，使用 AES 加密（密钥在程序中静态设置）。实现了未处理的传入命令/结果的队列 – 它以 AES 加密形式存储在 Windows 注册表中（%MACHINEGUID% 值用作密钥）。后门持久性由植入程序提供，该植入程序在 Windows 注册表的“运行”分支中创建相应的计划任务或条目。

BIASBOAT – 使用 C 编程语言开发的恶意程序 (ELF)，是 QUEUESEED 的 Linux 变体。使用 LOADGRIP 注入器在计算机上启动。

LOADGRIP 是使用 C 编程语言开发的恶意程序（ELF），主要功能是使用 ptrace API 通过注入来启动有效负载。有效负载通常以加密形式（AES128-CBC）呈现，其解密密钥是根据代码中静态输入的常量和计算机的“machine-id”值形成的。

GOSSIPFLOW是一个使用Go编程语言开发的恶意程序。提供隧道构建（使用 Yamux 多路复用器库）并执行 SOCKS5 代理功能。

本文翻译自 [原文链接](https://cert.gov.ua/article/6278706)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295905](/post/id/295905)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cert.gov.ua/article/6278706>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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