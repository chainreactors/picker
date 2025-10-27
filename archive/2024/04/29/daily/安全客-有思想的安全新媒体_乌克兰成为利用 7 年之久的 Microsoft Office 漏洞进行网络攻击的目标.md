---
title: 乌克兰成为利用 7 年之久的 Microsoft Office 漏洞进行网络攻击的目标
url: https://www.anquanke.com/post/id/296074
source: 安全客-有思想的安全新媒体
date: 2024-04-29
fetch_date: 2025-10-04T12:14:37.713191
---

# 乌克兰成为利用 7 年之久的 Microsoft Office 漏洞进行网络攻击的目标

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

# 乌克兰成为利用 7 年之久的 Microsoft Office 漏洞进行网络攻击的目标

阅读量**71778**

发布时间 : 2024-04-28 10:44:21

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了针对乌克兰的一项有针对性的行动，该行动利用了 Microsoft Office 中近七年的缺陷，在受感染的系统上提供 Cobalt Strike。

据 Deep Instinct 称，该攻击链发生于 2023 年底，采用 PowerPoint 幻灯片文件（“signal-2023-12-20-160512.ppsx”）作为起点，文件名暗示它可能已通过 Signal 即时通讯应用程序共享。

尽管如此，没有实际证据表明 PPSX 文件是以这种方式分发的，尽管乌克兰计算机紧急响应小组 (CERT-UA) 发现了两个使用该消息应用程序作为恶意软件传递的不同活动过去的向量。

就在上周，该机构披露，乌克兰武装部队越来越多地成为 UAC-0184 组织的攻击目标，该组织通过消息传递和约会平台为HijackLoader（又名GHOSTPULSE和SHADOWLADDER）、XWorm和Remcos RAT等恶意软件以及开源软件提供服务sigtop和tusc等程序可从计算机中窃取数据。

“PPSX（PowerPoint 幻灯片）文件似乎是美国陆军坦克扫雷刀片（MCB）的旧说明书，”安全研究员伊万·科萨列夫（Ivan Kosarev）说。 “PPSX 文件包含与外部 OLE 对象的远程关系。”

这涉及利用CVE-2017-8570（CVSS 分数：7.8），这是 Office 中现已修补的远程代码执行错误，该错误可能允许攻击者在说服受害者打开特制文件、加载远程脚本托管在 weavesilk[.]space 上。

严重混淆的脚本随后启动一个包含 JavaScript 代码的 HTML 文件，该文件反过来通过 Windows 注册表在主机上设置持久性，并丢弃模拟 Cisco AnyConnect VPN 客户端的下一阶段有效负载。

[![]()](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzQhiC8JugT6hoQFPQSCkMkE6s8De2iIeMPIRoGqhQIoYziOnukKVeXTRP2qZ4tjbJTjXxzHYn2PXJd87y-B02hZIzzDq2mtc8RBNsN-yAIrx0xdZkSREn67UyyMAbl-lXTtE16Rem-3aLsh2pF-oIvdFFsrx2ba1GZFjUaeaG97JgKNz13ERUmFLUn1gv/s728-rw-e365/fig1-campaign-attack-flow.png)

有效负载包括一个动态链接库（DLL），最终将破解的Cobalt Strike Beacon（一种合法的笔测试工具）直接注入系统内存，并等待来自命令和控制（C2）服务器（“petapixel[.]fun”）的进一步指令。

该 DLL 还包含一些功能来检查它是否在虚拟机中执行并逃避安全软件的检测。

Deep Instinct 表示，它既不能将这些攻击与特定的威胁行为者或组织联系起来，也不能排除红队演习的可能性。同样不清楚的是入侵的确切最终目标。

[![]()](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiP9z1weia0vRoToKgwQQkrr9F1xF7EWlcS0P951uNXYl9689DjdUz_4tXNoBZdRUgUH6wIX_rjQAHsKt31D2Qps0v2yrowB-ILyIeaqhOL3O-Fy0AkwDS-vA6AVU4cfN7beiojj7YnMamsgmlaYx2e3e-HaCEw8pYOBAFt_rdRGnsaJJqlGer37F48pOUF/s728-rw-e365/apt44-fig1.max-2100x2100.jpg)

科萨列夫说：“该诱饵包含与军事相关的内容，表明它的目标是军事人员。”

“但是域名 weavesilk[.]space 和 petapixel[.]fun 被伪装成一个不起眼的生成艺术网站 (weavesilk[.]com) 和一个流行的摄影网站 (petapixel[.]com)。这些是不相关的，而且有点令人费解的是，为什么攻击者会专门使用这些来愚弄军事人员。”

此次披露之际，CERT-UA透露，乌克兰约 20 家能源、水和供暖供应商已成为俄罗斯国家支持的名为 UAC-0133 的组织的攻击目标，UAC-0133 是Sandworm（又名 APT44、FROZENBARENTS、Seashell Blizzard、 UAC-0002 和 Voodoo Bear），它对针对该国的所有破坏性和破坏性行动负责。

这些攻击旨在破坏关键操作，涉及使用Kapeka（又名 ICYWELL、KnuckleTouch、QUEUESEED 和rongsens）等恶意软件及其 Linux 变体 BIASBOAT，以及 GOSSIPFLOW 和 LOADGRIP。

GOSSIPFLOW 是一个基于 Golang 的 SOCKS5 代理，而 LOADGRIP 是一个用 C 语言编写的 ELF 二进制文件，用于在受感染的 Linux 主机上加载 BIASBOAT。

Sandworm 是一个多产且高度适应性的威胁组织，与俄罗斯联邦武装部队总参谋部 (GRU) 的 74455 部队有联系。据了解，该组织至少自 2009 年起就一直活跃，其对手还与XakNet Team、Cyber​​ArmyofRussia\_Reborn和Solntsepek等三个黑客和泄密黑客活动人物有关。

Mandiant表示： “APT44 受到俄罗斯军事情报部门的支持，是一个充满活力、操作成熟的威胁行为者，积极参与全方位的间谍活动、攻击和影响行动。”他将高级持续威胁 (APT) 描述为从事多种活动。 ——自2022年1月以来，多管齐下帮助俄罗斯获得战时优势。

“APT44 的行动范围是全球性的，反映了俄罗斯广泛的国家利益和野心。随着时间的推移，APT44 的活动模式表明，APT44 的任务是执行一系列不同的战略优先事项，并且很可能被克里姆林宫视为一种灵活的权力工具，能够满足持久和新兴的情报需求。”

本文翻译自 [原文链接](https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296074](/post/id/296074)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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