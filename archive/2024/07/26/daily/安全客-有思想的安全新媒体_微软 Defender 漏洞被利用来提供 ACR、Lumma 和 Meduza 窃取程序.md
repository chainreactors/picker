---
title: 微软 Defender 漏洞被利用来提供 ACR、Lumma 和 Meduza 窃取程序
url: https://www.anquanke.com/post/id/298308
source: 安全客-有思想的安全新媒体
date: 2024-07-26
fetch_date: 2025-10-06T17:40:19.353705
---

# 微软 Defender 漏洞被利用来提供 ACR、Lumma 和 Meduza 窃取程序

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

# 微软 Defender 漏洞被利用来提供 ACR、Lumma 和 Meduza 窃取程序

阅读量**92621**

发布时间 : 2024-07-25 15:06:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html>

译文仅供参考，具体内容表达以及含义原文为准。

Microsoft Defender SmartScreen 中现已修补的安全漏洞已被利用，作为旨在提供 ACR Stealer、Lumma 和 Meduza 等信息窃取程序的新活动的一部分。

Fortinet FortiGuard Labs 表示，它检测到针对西班牙、泰国和美国的窃取活动，该活动使用利用 CVE-2024-21412 的诱杀文件（CVSS 评分：8.1）。

高严重性漏洞使得攻击者能够绕过 SmartScreen 保护并丢弃恶意负载。Microsoft 在 2024 年 2 月发布的月度安全更新中解决了这个问题。

“最初，攻击者引诱受害者点击一个精心制作的链接，指向一个旨在下载LNK文件的URL文件，”安全研究员Cara Lin说。“然后，LNK 文件会下载一个包含 [HTML 应用程序] 脚本的可执行文件。”

HTA 文件用作解码和解密 PowerShell 代码的管道，该代码负责获取诱饵 PDF 文件和 shellcode 注入器，这反过来又导致部署 Meduza Stealer 或 Hijack Loader，随后启动 ACR Stealer 或 Lumma。

ACR Stealer 被评估为 GrMsk Stealer 的进化版本，于 2024 年 3 月下旬由一个名为 SheldIO 的威胁行为者在俄语地下论坛 RAMP 上做广告。

“这个ACR窃取者在Steam社区网站上用死掉解析器（DDR）技术隐藏了它的[命令和控制]，”Lin说，并称它能够从网络浏览器、加密钱包、消息传递应用程序、FTP客户端、电子邮件客户端、VPN服务和密码管理器中窃取信息。

值得注意的是，根据 AhnLab 安全情报中心 （ASEC） 的说法，最近还观察到了使用相同技术的 Lumma Stealer 攻击，使对手更容易随时更改 C2 域并使基础设施更具弹性。

CrowdStrike透露，威胁行为者正在利用上周的中断来分发一个名为Daolpu的以前未记录的信息窃取程序，使其成为导致数百万Windows设备瘫痪的错误更新导致的持续影响的最新例子。

该攻击涉及使用带有宏的 Microsoft Word 文档，该文档伪装成 Microsoft 恢复手册，列出了 Windows 制造商为解决问题而发布的合法指令，并利用它作为诱饵来激活感染过程。

DOCM文件在打开时，运行宏以从远程中检索第二阶段DLL文件，该远程器被解码以启动Daolpu，这是一种窃取恶意软件，可从Google Chrome，Microsoft Edge，Mozilla Firefox和其他基于Chromium的浏览器中收集凭据和cookie。

它还遵循Braodo和DeerStealer等新的窃取恶意软件系列的出现，即使网络犯罪分子正在利用恶意广告技术推广合法软件（如Microsoft Teams）来部署Atomic Stealer。

“随着网络犯罪分子加大他们的分发活动，通过搜索引擎下载应用程序变得更加危险，”Malwarebytes研究员JérômeSegura说。“用户必须在恶意广告（赞助结果）和SEO中毒（受感染的网站）之间导航。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298308](/post/id/298308)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/microsoft-defender-flaw-exploited-to.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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