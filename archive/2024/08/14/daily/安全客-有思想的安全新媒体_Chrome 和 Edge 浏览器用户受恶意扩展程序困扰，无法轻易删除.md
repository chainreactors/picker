---
title: Chrome 和 Edge 浏览器用户受恶意扩展程序困扰，无法轻易删除
url: https://www.anquanke.com/post/id/299068
source: 安全客-有思想的安全新媒体
date: 2024-08-14
fetch_date: 2025-10-06T18:02:05.081147
---

# Chrome 和 Edge 浏览器用户受恶意扩展程序困扰，无法轻易删除

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

# Chrome 和 Edge 浏览器用户受恶意扩展程序困扰，无法轻易删除

阅读量**86581**

发布时间 : 2024-08-13 11:05:34

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/08/12/chrome-edge-malicious-browser-extensions/>

译文仅供参考，具体内容表达以及含义原文为准。

研究人员发现，一个以恶意安装程序为特色的广泛活动，使用户背负难以删除的恶意 Chrome 和 Edge 浏览器扩展程序。

Reason Labs研究团队说：“特洛伊木马恶意软件包含不同的可交付成果，从劫持搜索的简单广告软件扩展到提供本地扩展以窃取私人数据并执行各种命令的更复杂的恶意脚本。

“我们目睹了恶意软件和扩展程序的广泛分布——总共至少有 300,000 名用户在 Google Chrome 和 Microsoft Edge 上受到影响。”

### 感染

该活动背后的威胁行为者已经建立了欺骗性网站，提供 VLC 或 KeePass 等流行软件供下载，但下载的安装程序甚至不会尝试安装用户想要的程序。

相反，一旦运行，该程序就会注册一个计划任务，该任务将下载 PowerShell 脚本，然后该脚本从远程服务器下载有效负载并在内存中执行它。

该脚本会添加注册表键以强制从 Chrome Web Store 和 Edge Add-ons 页面安装扩展程序，并且用户无法禁用它们，因为它们不会显示在浏览器的扩展程序管理页面上 – 即使激活了开发者模式。

研究人员指出：“该脚本继续禁用浏览器的所有更新，因为在每次更新期间，默认设置都会恢复，这将干扰恶意软件的活动。

该脚本还会下载一个本地扩展程序（“Google Updater”），该扩展程序会劫持浏览器的默认搜索（Bing 或 Google）并将其重定向到攻击者的搜索门户。

### 如何删除恶意软件和恶意扩展？

“在撰写本文时，大多数AV引擎无法检测到安装程序和扩展程序，”研究团队说。“安装人员由 Tommy Tech LTD 签名。自 2021 年以来，由同一签名者签名的其他安装人员一直存在。

恶意 Chrome 扩展程序的名称中通常包含“搜索”（例如，“自定义搜索栏”、“您的搜索栏”等）。Edge 扩展的名称中包含“搜索”或“选项卡”（例如，“Simple New Tab”、“NewTab Wonders”、“EXYZ Search”等）。他们中的大多数现在已经被谷歌和Microsoft从各自的商店中删除。

![恶意浏览器扩展]( "The malicious Simple New Tab extension in the store (Source: Reason Labs)")

商店中的恶意 Simple New Tab 扩展（来源：Reason Labs）

研究人员估计，这两种浏览器至少有 300,000 名用户受到影响，有些人在网上抱怨他们找不到删除恶意扩展的方法。

研究人员分享了一份广泛的妥协指标清单，并概述了消除威胁的过程。

他们指出：“成功删除这种恶意软件的唯一方法是确保它的持久性机制消失了，”这意味着删除计划任务、注册表键和删除恶意软件文件。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/08/12/chrome-edge-malicious-browser-extensions/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299068](/post/id/299068)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/08/12/chrome-edge-malicious-browser-extensions/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/08/12/chrome-edge-malicious-browser-extensions/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* ##### [AI即万物：ISC.AI 2025的跨越变迁](/post/id/308744)

  2025-06-20 18:39:26
* ##### [热点 | 利用AI造谣幼儿园大火被抓，大模型内容安全谁来守护？](/post/id/308685)

  2025-06-20 16:47:19
* ##### [黑客通过恶意简历瞄准求职者](/post/id/308388)

  2025-06-12 14:31:49
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [德克萨斯州警告30万份事故报告通过受影响的用户帐户窃取](/post/id/308363)

  2025-06-11 16:42:18
* ##### [新型 Mirai 僵尸网络通过命令注入漏洞感染 TBK DVR 设备](/post/id/308303)

  2025-06-10 13:35:25
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03

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