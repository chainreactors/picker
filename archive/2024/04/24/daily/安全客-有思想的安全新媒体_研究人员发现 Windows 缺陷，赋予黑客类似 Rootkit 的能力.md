---
title: 研究人员发现 Windows 缺陷，赋予黑客类似 Rootkit 的能力
url: https://www.anquanke.com/post/id/295883
source: 安全客-有思想的安全新媒体
date: 2024-04-24
fetch_date: 2025-10-04T12:14:52.009552
---

# 研究人员发现 Windows 缺陷，赋予黑客类似 Rootkit 的能力

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

# 研究人员发现 Windows 缺陷，赋予黑客类似 Rootkit 的能力

阅读量**64891**

发布时间 : 2024-04-23 10:20:49

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thehackernews.com/2024/04/researchers-uncover-windows-flaws.html>

译文仅供参考，具体内容表达以及含义原文为准。

新研究发现，威胁行为者可以利用 DOS 到 NT 路径转换过程来实现类似 rootkit 的功能，以隐藏和模拟文件、目录和进程。

SafeBreach 安全研究员 Or Yair在黑帽大会上发表的一份分析报告中表示：“当用户在 Windows 中执行带有路径参数的函数时，文件或文件夹所在的 DOS 路径将转换为 NT 路径。”上周的亚洲会议。

“在此转换过程中，存在一个已知问题，即该函数会删除任何路径元素中的尾随点以及最后一个路径元素中的任何尾随空格。此操作由 Windows 中的大多数用户空间 API 完成。”

这些所谓的 MagicDot 路径允许任何非特权用户访问类似 rootkit 的功能，然后这些用户可以将其武器化，在没有管理员权限的情况下执行一系列恶意操作，并且不会被发现。

它们包括“隐藏文件和进程、隐藏档案中的文件、影响预取文件分析、使任务管理器和 Process Explorer 用户认为恶意软件文件是 Microsoft 发布的经过验证的可执行文件、通过拒绝服务 (DoS) 禁用 Process Explorer”的功能）漏洞等等。”

[![类似 Rootkit 的权限]( "类似 Rootkit 的权限")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilK_q3igvvpnT8AnB_zK5eGQwFBan5pPeIuD9rqSPr3KZGJmJXJm7tw5U6fOiijHSks_IH_6E9BAM_s9w70oFcShMuc5VOygHT0tHQMzU9U2a7PduutNmNJOeeC2Bw1JhQSoz0FcBRhZMoJSf6KJAIffMU9MYQPqV3VgUpAeWQV3oXhrOE4dLHbGOBYqlS/s728-rw-e365/rootkit.png)DOS 到 NT 路径转换过程中的根本问题还导致发现了四个安全缺陷，其中三个缺陷已由 Microsoft 解决 –

权限提升 (EoP) 删除漏洞，可用于删除没有所需权限的文件（将在未来版本中修复）
权限提升 (EoP) 写入漏洞，可用于通过篡改卷影副本中先前版本的恢复过程来在没有所需权限的情况下写入文件（CVE-2023-32054，CVSS 评分：7.3）
远程代码执行 (RCE) 漏洞，可用于创建特制存档，在攻击者选择的任何位置提取文件时可能导致代码执行（CVE-2023-36396，CVSS 评分：7.8）
使用名称长度为 255 个字符且没有文件扩展名的可执行文件启动进程时，存在影响 Process Explorer 的拒绝服务 (DoS) 漏洞 (CVE-2023-42757)
“这项研究首次探讨了如何利用看似无害的已知问题来开发漏洞，并最终造成重大安全风险，”Yair 解释道。

[![类似 Rootkit 的权限]( "类似 Rootkit 的权限")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhowYnoQYqzAVtBd2ernubDLshQUU56RPzQrFpulV669tRRpycGpmiP1Sp7K9HF_d5O3g-xbGWMlxXFgYCnEp5wi6xTPZXE9P7uf37bMb9mLHEzyodLq7OZyg7yRGkcZe2COZB2aas_idco499HPuKBb5MkL-8w7XFpgOQdfoACXKSHQzwVHOkWecpKnNVL/s728-rw-e365/SafeBreach.jpg)“我们相信，这些影响不仅与世界上使用最广泛的桌面操作系统 Microsoft Windows 相关，而且与所有软件供应商相关，其中大多数供应商也允许已知问题在其软件版本之间持续存在。”

本文翻译自 [原文链接](https://thehackernews.com/2024/04/researchers-uncover-windows-flaws.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295883](/post/id/295883)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thehackernews.com/2024/04/researchers-uncover-windows-flaws.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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