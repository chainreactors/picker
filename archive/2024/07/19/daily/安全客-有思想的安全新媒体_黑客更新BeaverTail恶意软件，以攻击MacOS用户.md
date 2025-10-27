---
title: 黑客更新BeaverTail恶意软件，以攻击MacOS用户
url: https://www.anquanke.com/post/id/298041
source: 安全客-有思想的安全新媒体
date: 2024-07-19
fetch_date: 2025-10-06T17:40:49.272937
---

# 黑客更新BeaverTail恶意软件，以攻击MacOS用户

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

# 黑客更新BeaverTail恶意软件，以攻击MacOS用户

阅读量**100895**

发布时间 : 2024-07-18 15:23:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Newsroom，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员发现了一种已知窃取恶意软件的更新变体，该恶意软件是隶属于朝鲜民主主义人民共和国 （DPRK） 的攻击者在之前针对求职者的网络间谍活动中提供的。

安全研究员帕特里克·沃德尔（Patrick Wardle）说，有问题的工件是一个名为“MiroTalk.dmg”的Apple macOS磁盘映像（DMG）文件，它模仿了同名的合法视频通话服务，但实际上，它是提供BeaverTail本机版本的渠道。

BeaverTail 指的是一种 JavaScript 窃取恶意软件，该恶意软件于 2023 年 11 月由 Palo Alto Networks Unit 42 首次记录，作为一项名为 Contagious Interview 的活动的一部分，该活动旨在通过假定的工作面试过程用恶意软件感染软件开发人员。Securonix 正在以 DEV#POPPER 的绰号跟踪相同的活动。

除了从网络浏览器和加密钱包中窃取敏感信息外，该恶意软件还能够提供额外的有效载荷，例如 InvisibleFerret，这是一个 Python 后门，负责下载 AnyDesk 以进行持久的远程访问。虽然 BeaverTail 是通过 GitHub 和 npm 包注册表上托管的虚假 npm 包分发的，但最新的发现标志着分发向量的转变。

“如果我不得不猜测，朝鲜黑客可能通过下载并执行mirotalk上托管的MiroTalk（受感染版本）来接近他们的潜在受害者，要求他们参加招聘会议。净，“沃德尔说。

对未签名的 DMG 文件的分析表明，它有助于从 Google Chrome、Brave 和 Opera、加密货币钱包和 iCloud 钥匙串等网络浏览器窃取数据。此外，它旨在从远程服务器（即 InvisibleFerret）下载和执行其他 Python 脚本。

“朝鲜黑客是一群狡猾的人，非常擅长黑客攻击macOS目标，尽管他们的技术通常依赖于社会工程学（因此从技术角度来看相当不起眼），”沃德尔说。

Phylum 发现了一个名为 call-blockflow 的新恶意 npm 包，该包与合法的调用绑定几乎相同，但包含下载远程二进制文件的复杂功能，同时努力在雷达下飞行。

“在这次攻击中，虽然调用绑定包没有受到损害，但武器化的调用块流包复制了原始包的所有信任和合法性，以支持攻击的成功，”它在一份声明中说。

该软件包被怀疑是与朝鲜有联系的Lazarus集团的作品，在上传到npm后大约一个半小时后未发布，总共吸引了18次下载。有证据表明，自 2023 年 9 月以来，该活动由三十多个恶意软件包组成，一直在一波又一波地进行。

“这些软件包一旦安装，就会下载一个远程文件，解密它，从中执行导出的功能，然后通过删除和重命名文件来精心掩盖它们的踪迹，”这家软件供应链安全公司表示。“这使得包目录在安装后处于看似良性的状态。”

它还遵循 JPCERT/CC 的公告，警告朝鲜 Kimsuky 演员针对日本组织策划的网络攻击。

感染过程从冒充安全和外交组织的网络钓鱼邮件开始，并包含恶意可执行文件，打开该可执行文件后会导致下载 Visual Basic 脚本 （VBS），而 Visual Basic 脚本 （VBS） 又会检索 PowerShell 脚本以收集用户帐户、系统和网络信息以及枚举文件和进程。

然后，收集的信息将泄露到命令和控制 （C2） 服务器，该服务器会使用第二个 VBS 文件进行响应，然后执行该文件以提取并运行名为 InfoKey 的基于 PowerShell 的键盘记录器。

“虽然很少有关于Kimsuky针对日本组织的攻击活动的报道，但日本也有可能成为积极的目标，”JPCERT / CC说。

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298041](/post/id/298041)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html)

如若转载,请注明出处： <https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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