---
title: APT-C-60 Group 利用 WPS Office 漏洞部署 SpyGlace 后门
url: https://www.anquanke.com/post/id/299628
source: 安全客-有思想的安全新媒体
date: 2024-08-30
fetch_date: 2025-10-06T18:01:25.840442
---

# APT-C-60 Group 利用 WPS Office 漏洞部署 SpyGlace 后门

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

# APT-C-60 Group 利用 WPS Office 漏洞部署 SpyGlace 后门

阅读量**78160**

发布时间 : 2024-08-29 15:54:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/apt-c-60-group-exploit-wps-office-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

与韩国结盟的网络间谍活动与零日利用金山 WPS Office 中现已修补的关键远程代码执行漏洞以部署名为 SpyGlace 的定制后门有关。

据网络安全公司 ESET 和 DBAPPSecurity 称，该活动被归因于一个名为 **APT-C-60** 的威胁行为者。已发现这些攻击会用恶意软件感染中国和东亚用户。

有问题的安全漏洞是 CVE-2024-7262（CVSS 分数：9.3），这是由于缺乏对用户提供的文件路径的正确验证。这个漏洞本质上允许对手上传任意 Windows 库并实现远程代码执行。

ESET 表示，该错误“允许通过劫持 WPS Office 插件组件的控制流来执行代码promecefpluginhost.exe”，并补充说它找到了另一种实现相同效果的方法。第二个漏洞被跟踪为 CVE-2024-7263 （CVSS 评分：9.3）。

APT-C-60 构思的攻击将漏洞武器化为一键式漏洞利用，该漏洞采用 2024 年 2 月上传到 VirusTotal 的诱杀电子表格文档的形式。

具体来说，该文件嵌入了一个恶意链接，单击该链接时，会触发多阶段感染序列以传递 SpyGlace 木马，这是一个名为 TaskControler.dll 的 DLL 文件，具有文件窃取、插件加载和命令执行功能。

“漏洞利用开发人员在电子表格中嵌入了电子表格行和列的图片，以欺骗并说服用户该文档是常规电子表格，”安全研究员 Romain Dumont 说。“恶意超链接链接到图像，因此单击图片中的单元格会触发漏洞利用。”

据总部位于北京的网络安全供应商 ThreatBook 称，APT-C-60 据信自 2021 年以来一直活跃，早在 2022 年 6 月就在野外检测到 SpyGlace。

Dumont 说：“无论该组织是开发还是购买了 CVE-2024-7262 漏洞，它肯定需要对应用程序的内部进行一些研究，但也需要了解 Windows 加载过程的行为方式。

“这个漏洞很狡猾，因为它具有足够的欺骗性，可以诱骗任何用户点击看起来合法的电子表格，同时也非常有效和可靠。MHTML 文件格式的选择使攻击者能够将代码执行漏洞转化为远程漏洞。

这家斯洛伐克网络安全公司指出，名为 ScreenShareOTR（或 ss-otr）的 Pidgin 消息传递应用程序的恶意第三方插件包含负责从命令和控制 （C&C） 服务器下载下一阶段二进制文件的代码，最终导致部署 DarkGate 恶意软件。

“正如宣传的那样，该插件的功能包括使用安全的不记录消息 （OTR） 协议的屏幕共享。但是，除此之外，该插件还包含恶意代码，“ESET 说。“具体来说，某些版本的 pidgin-screenshare.dll 可以从 C&C 服务器下载并执行 PowerShell 脚本。”

该插件还包含键盘记录器和屏幕截图捕获功能，此后已从第三方插件列表中删除。建议已安装该插件的用户立即将其删除。

此后，ESET 发现，在一个名为 Cradle 的应用程序（“cradle[.]im“） 的 Git，它声称是 Signal 消息应用程序的开源分支。该应用程序从 2023 年 9 月起可供下载近一年。

恶意代码通过运行一个PowerShell脚本下载，该脚本随后获取并执行一个编译后的AutoIt脚本，最终安装DarkGate。Cradle的Linux版本则传送一个ELF可执行文件，该文件下载并执行shell命令，并将结果发送到远程服务器。

另一个常见的指示迹象是，插件安装程序和Cradle应用程序都使用了一个有效的数字证书进行签名，该证书颁发给了名为“INTERREX – SP. Z O.O.”的一家波兰公司，这表明犯罪者正在使用不同的方法来传播恶意软件。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/apt-c-60-group-exploit-wps-office-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299628](/post/id/299628)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/apt-c-60-group-exploit-wps-office-flaw.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/apt-c-60-group-exploit-wps-office-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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