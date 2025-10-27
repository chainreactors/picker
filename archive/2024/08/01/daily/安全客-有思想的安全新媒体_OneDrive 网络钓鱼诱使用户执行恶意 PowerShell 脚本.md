---
title: OneDrive 网络钓鱼诱使用户执行恶意 PowerShell 脚本
url: https://www.anquanke.com/post/id/298605
source: 安全客-有思想的安全新媒体
date: 2024-08-01
fetch_date: 2025-10-06T18:00:03.812680
---

# OneDrive 网络钓鱼诱使用户执行恶意 PowerShell 脚本

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

# OneDrive 网络钓鱼诱使用户执行恶意 PowerShell 脚本

阅读量**125715**

发布时间 : 2024-07-31 11:23:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员警告说，针对 Microsoft OneDrive 用户的新网络钓鱼活动旨在执行恶意 PowerShell 脚本。

“该活动严重依赖社会工程策略来欺骗用户执行PowerShell脚本，从而破坏他们的系统，”Trellix安全研究员Rafael Pena在周一的分析中表示。

这家网络安全公司正在追踪名为OneDrive Pastejacking的“狡猾”的网络钓鱼和下载器活动。

攻击是通过一封包含HTML文件的电子邮件展开的，当打开该文件时，会显示一个模拟OneDrive页面的图像，并显示一条错误消息，上面写着：“无法连接到’OneDrive’云服务。要修复此错误，您需要手动更新 DNS 缓存。

该消息还附带两个选项，即“如何修复”和“详细信息”，后者将电子邮件收件人定向到有关排查 DNS 的合法 Microsoft Learn 页面。

但是，单击“如何修复”会提示用户执行一系列步骤，其中包括按“Windows 键 + X”打开“快速链接”菜单、启动 PowerShell 终端以及粘贴 Base64 编码的命令以解决问题。

“命令 […]首先运行 ipconfig /flushdns，然后在 C： 驱动器上创建一个名为 ‘downloads’ 的文件夹，“Pena 解释道。随后，它将存档文件下载到此位置，重命名它，提取其内容（’script.a3x’和’AutoIt3.exe’），并使用AutoIt3.exe执行script.a3x。

据观察，该活动针对美国、韩国、德国、印度、爱尔兰、意大利、挪威和英国的用户。

该披露建立在 ReliaQuest、Proofpoint 和 McAfee Labs 的类似发现之上，表明采用这种技术的网络钓鱼攻击（也称为 ClickFix）正变得越来越普遍。

这一发展是在发现一项新的基于电子邮件的社会工程活动之际发生的，该活动分发虚假的 Windows 快捷方式文件，导致执行托管在 Discord 内容分发网络 （CDN） 基础设施上的恶意负载。

网络钓鱼活动也越来越多地被观察到，例如从以前被入侵的合法电子邮件帐户发送 Microsoft Office 表单，以诱使目标通过点击看似无害的链接来泄露其 Microsoft 365 登录凭据。

“攻击者在Microsoft Office Forms上创建看起来合法的表单，在表单中嵌入恶意链接，”Perception Point说。“然后，这些表格以合法请求为幌子，例如更改密码或访问重要文档，模仿受信任的平台和品牌（如Adobe或Microsoft SharePoint文档查看器）通过电子邮件大量发送给目标。”

更重要的是，其他攻击浪潮利用以发票为主题的诱饵来诱骗受害者在 Cloudflare R2 上托管的网络钓鱼页面上分享他们的凭据，然后通过 Telegram 机器人将其泄露给威胁参与者。

毫不奇怪，攻击者一直在寻找不同的方法，通过安全电子邮件网关 （SEG） 秘密地走私恶意软件，以增加攻击成功的可能性。

根据 Cofense 最近的一份报告，不良行为者正在滥用 SEG 扫描 ZIP 存档附件的方式，通过 DBatLoader（又名 ModiLoader 和 NatsoLoader）提供 Formbook 信息窃取器。

具体来说，这涉及将 HTML 有效负载冒充 MPEG 文件，以利用以下事实来逃避检测：许多常见的存档提取器和 SEG 会解析文件头信息，但会忽略可能包含有关文件格式的更准确信息的文件页脚。

该公司指出：“威胁行为者利用了.ZIP档案附件，当 SEG 扫描文件内容时，该档案被检测为包含.MPEG视频文件，并且没有被阻止或过滤。

“当使用常见/流行的存档提取工具（例如7-Zip或Power ISO）打开此附件时，它似乎也包含.MPEG视频文件，但无法播放。但是，当在Outlook客户端中或通过Windows Explorer存档管理器打开存档时，.MPEG文件被（正确）检测为.HTML[文件]。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298605](/post/id/298605)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [网络钓鱼](/tag/%E7%BD%91%E7%BB%9C%E9%92%93%E9%B1%BC)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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