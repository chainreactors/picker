---
title: 针对Microsoft OneDrive用户的网络钓鱼活动
url: https://www.anquanke.com/post/id/298628
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:09.553024
---

# 针对Microsoft OneDrive用户的网络钓鱼活动

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

# 针对Microsoft OneDrive用户的网络钓鱼活动

阅读量**144359**

发布时间 : 2024-07-31 11:19:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166312/hacking/microsoft-onedrive-phishing.html>

译文仅供参考，具体内容表达以及含义原文为准。

在过去的几周里，Trellix 高级研究中心观察到针对 Microsoft OneDrive 用户的复杂网络钓鱼活动。威胁行为者依靠社会工程策略来诱骗用户执行 PowerShell 脚本，从而导致他们的系统受到威胁。

攻击链首先诱骗收件人点击一个按钮，该按钮声称可以解释如何修复 DNS 问题，这表明解决此问题将授予对所需文件的访问权限。

*“攻击按如下方式展开：受害者收到一封包含.html文件的电子邮件。当打开此.html文件时，它会显示一个图像，旨在创建访问文档的紧迫感，从而增加用户按照提供的说明进行操作的可能性。“该图像模拟一个Microsoft OneDrive 页面，其中显示一个名为”Reports.pdf“的文件和一个名为”错误 0x8004de86“的窗口，其中包含以下错误消息：”无法连接到’OneDrive’云服务。要修复此错误，您需要手动更新 DNS 缓存。此窗口有两个按钮：“详细信息”和“如何修复”。值得注意的是，错误 0x8004de80 是登录 OneDrive 时可能发生的合法问题。*

![Microsoft OneDrive 网络钓鱼]()

单击“详细信息”按钮可将用户定向到“DNS 疑难解答”上的合法 Microsoft Learn 页面。

单击“如何修复”后，收件人将被指示遵循一系列步骤，其中包括打开快速链接菜单（Windows 键 + X）、访问 Windows PowerShell 终端、粘贴命令并执行它以解决问题的具体说明。

*“如上图所示，该命令首先运行 ipconfig /flushdns，然后在 C： 驱动器上创建一个名为”downloads“的文件夹。随后，它将存档文件下载到此位置，重命名它，提取其内容（“script.a3x”和“AutoIt3.exe”），并使用 AutoIt3.exe 执行 script.a3x。最后，将显示以下消息：“操作已成功完成，请重新加载页面。*

Trellix 报告称，该活动针对的大多数用户位于美国 （40%）、韩国 （17%）、德国 （14%） 和印度 （10%）。

*报告总结道：“这次攻击的全球分布凸显了国际合作和情报共享的必要性，以有效应对这些威胁，”该报告还提供了妥协指标（IoC）。*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166312/hacking/microsoft-onedrive-phishing.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298628](/post/id/298628)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166312/hacking/microsoft-onedrive-phishing.html)

如若转载,请注明出处： <https://securityaffairs.com/166312/hacking/microsoft-onedrive-phishing.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络钓鱼](/tag/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)
* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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