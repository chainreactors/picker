---
title: 黑客利用 Windows SmartScreen 漏洞投放 DarkGate 恶意软件
url: https://www.anquanke.com/post/id/293916
source: 安全客-有思想的安全新媒体
date: 2024-03-15
fetch_date: 2025-10-04T12:07:52.055164
---

# 黑客利用 Windows SmartScreen 漏洞投放 DarkGate 恶意软件

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

# 黑客利用 Windows SmartScreen 漏洞投放 DarkGate 恶意软件

阅读量**75157**

发布时间 : 2024-03-14 10:38:11

**x**

##### 译文声明

本文是翻译文章，文章来源：https://www.trendmicro.com/en\_us/research/24/c/cve-2024-21412--darkgate-operators-exploit-microsoft-windows-sma.html

译文仅供参考，具体内容表达以及含义原文为准。

DarkGate 恶意软件操作发起的新一波攻击利用现已修复的 Windows Defender SmartScreen 漏洞来绕过安全检查并自动安装虚假软件安装程序。SmartScreen 是一项 Windows 安全功能，当用户尝试运行从 Internet 下载的无法识别或可疑文件时，它会显示警告。被追踪为 CVE-2024-21412 的缺陷是 Windows Defender SmartScreen 缺陷，允许特制的下载文件绕过这些安全警告。

攻击者可以通过创建指向远程 SMB 共享上托管的另一个 .url 文件的 Windows Internet 快捷方式（.url 文件）来利用该缺陷，这将导致最终位置的文件自动执行。

微软于 2 月中旬修复了该漏洞，趋势科技透露，出于经济动机的 Water Hydra 黑客组织此前曾利用该漏洞作为零日漏洞，将其 DarkMe 恶意软件植入交易者的系统中。今天，趋势科技分析师报告称，DarkGate 操作者正在利用相同的缺陷来提高他们在目标系统上成功（感染）的机会。这是该恶意软件的一项重大发展，它与 Pikabot 一起填补了去年夏天 QBot 破坏造成的空白，并被多个网络犯罪分子用于分发恶意软件。

**DarkGate 攻击细节**

该攻击从一封恶意电子邮件开始，其中包含一个 PDF 附件，其中的链接利用 Google DoubleClick 数字营销 (DDM) 服务的开放重定向来绕过电子邮件安全检查。当受害者点击该链接时，他们会被重定向到托管互联网快捷方式文件的受感染 Web 服务器。 此快捷方式文件 (.url) 链接到托管在攻击者控制的 WebDAV 服务器上的第二个快捷方式文件。

![]()

                                                   “JANUARY-25-2024-FLD765.url”的内容

使用一个 Windows 快捷方式在远程服务器上打开第二个快捷方式可有效利用 CVE-2024-21412 缺陷，导致恶意 MSI 文件在设备上自动执行。

![]()

                                                                     “gamma.url”的内容

这些 MSI 文件伪装成来自 NVIDIA、Apple iTunes 应用或 Notion 的合法软件。

执行 MSI 安装程序后，涉及“libcef.dll”文件和名为“sqlite3.dll”的加载程序的另一个 DLL 侧载缺陷将解密并在系统上执行 DarkGate 恶意软件负载。

一旦初始化，恶意软件就可以窃取数据，获取额外的有效负载并将其注入正在运行的进程中，执行按键日志记录，并为攻击者提供实时远程访问。

自 2024 年 1 月中旬以来，DarkGate 运营商采用的复杂且多步骤的感染链总结如下：

![]()

                                                                                   攻击链架构

趋势科技表示，该活动采用了 DarkGate 6.1.7 版本，与旧版本 5 相比，该版本具有 XOR 加密配置、新配置选项以及命令和控制 (C2) 值的更新。

DarkGate 6 中提供的配置参数使其操作员能够确定各种操作策略和规避技术，例如启用启动持久性或指定最小磁盘存储和 RAM 大小以规避分析环境。

![]()

                                        DarkGate 版本 6 的关键配置设置

减轻这些攻击风险的第一步是应用 Microsoft 的 2024 年 2 月补丁星期二更新，该更新修复了 CVE-2024-21412。

趋势科技已在此网页上发布了此 DarkGate 活动的完整入侵指标 (IoC) 列表。

本文翻译自https://www.trendmicro.com/en\_us/research/24/c/cve-2024-21412--darkgate-operators-exploit-microsoft-windows-sma.html 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293916](/post/id/293916)

安全KER - 有思想的安全新媒体

本文转载自: https://www.trendmicro.com/en\_us/research/24/c/cve-2024-21412--darkgate-operators-exploit-microsoft-windows-sma.html

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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