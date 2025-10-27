---
title: 带你了解如何发现在 magix.com 和 xara.com 网站中的严重安全漏洞
url: https://www.anquanke.com/post/id/297774
source: 安全客-有思想的安全新媒体
date: 2024-07-11
fetch_date: 2025-10-06T17:38:41.400496
---

# 带你了解如何发现在 magix.com 和 xara.com 网站中的严重安全漏洞

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

# 带你了解如何发现在 magix.com 和 xara.com 网站中的严重安全漏洞

阅读量**117897**

发布时间 : 2024-07-10 19:32:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Proseizala，文章来源：Medium

原文地址：[https://medium.com/@proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e](https://medium.com/%40proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e)

译文仅供参考，具体内容表达以及含义原文为准。

德国 Magix Software GmbH 授予我名人堂名单和免费的 Magix Music Maker 2014 Premium 许可证，以表彰我报告了 magix.com 和 xara.com 在线基础

设施中的几个严重安全问题，这些问题可能被用来彻底破坏这两个网站：

![]()

在此，我要感谢 Magix 安全团队的快速响应和始终透明的响应，以及整体良好的协调流程。这是一个完美的例子，说明漏洞赏金运营商和研究人员之间的沟通如何让双方都满意。在我第一次报告漏洞后仅几天内，就很快修复了关键漏洞（RCE、SQLi、LFI）**，**而修复 XSS 则花费了更长的时间，但对于中等严重性的问题来说，这仍然是可以接受的。

Bug Bounty 计划始终是一个巨大的挑战，有时你会获得非常酷的东西和像这样的很好的参考资料作为回报——现在这里有一个关于已发现漏洞的简短文章，这些漏洞已经被 Magix 修复。

# **europe.magix.com 上的远程代码执行**

这是我在开发这个漏洞赏金计划时发现的最危险的漏洞。我发现了一个脚本，它允许攻击者通过 HTTP POST 请求上传 zip 文件。该脚本接受任何 zip 文件，将其重命名为某个临时名称，最后将 .zip 文件解压到工作目录中，而不检查 zip 文件是否包含有效文件。此外，解压的内容可以通过 www 访问 — 我认为问题很明显。

为了证明 Magix 的可利用性，我编写了一个简短的 Python 脚本。以下代码片段展示了如何使用非常方便的 Python ZipFile 函数在内存中动态生成 zip 文件。.zip 文件包含一个名为“/tmp/test.php”的文件，其中包含自定义 PHP 有效负载。

/usr/bin/python 的 #!

**导入**zip 文件

**从***StringIO***导入**StringIO

**导入**zlib

内存文件 = StringIO()

zipFile = zipfile.ZipFile(inMemoryFile, ‘w’, zipfile.ZIP\_DEFLATED)

zipFile.writestr(‘./tmp/test.php’, ‘<?php echo \”www.rcesecurity.com\”; ?>’)

zipFile.close()

对于 Magix 来说，目标脚本在 POST 任意 zip 文件后会回显一些额外的（且危险的）调试输出：看起来 Magix 忘记停用此输出了——如果没有这个，我可能就不会发现这个缺陷了 🙂

![]()

由于调试输出还公开了提取文件的完整路径，因此这会导致一个很好的 RCE 条件：

![]()

现在想象一下攻击者上传一些恶意的 C99……

# **europe.magix.com 上的 SQL 注入**

此漏洞或多或少与之前描述的 RCE 漏洞类似。如果 zip 文件包含特制的 .ini 文件，则造成 RCE 漏洞的相同脚本会在 SQL 查询中使用未过滤的 .ini 值：

![]()

downloadsv9.xara.com 上的本地文件包含

本地文件包含可能与 RCE 漏洞一样危险，因为攻击者可能会读取 /etc/passwd 等敏感系统文件：

![]()

…如果你有一个懒惰的系统管理员，喜欢对文件和目录使用 chmod 777，那么可能会发现更多信息 😉

# **downloadsv9.xara.com 上的跨站点脚本**

好的 – 我保证不再详细地写有关 XSS 的内容，所以我将给你留下 PoC 屏幕截图：

![]()

对于漏洞赏金猎人和 Magix 来说这真是快乐的一天！

本文翻译自Medium [原文链接](https://medium.com/%40proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297774](/post/id/297774)

安全KER - 有思想的安全新媒体

本文转载自: [Medium](https://medium.com/%40proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e)

如若转载,请注明出处： [https://medium.com/@proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e](https://medium.com/%40proseizala/magix-bug-bounty-magix-com-rce-sqli-and-xara-com-lfi-xss-c4e8492bbf3e)

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [漏洞赏金](/tag/%E6%BC%8F%E6%B4%9E%E8%B5%8F%E9%87%91)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Stealth Falcon 在复杂的网络间谍活动中利用新的零日漏洞 (CVE-2025-33053)](/post/id/308352)

  2025-06-11 16:12:52

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