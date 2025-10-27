---
title: Byakugan：针对葡语国家的恶意软件
url: https://www.anquanke.com/post/id/295322
source: 安全客-有思想的安全新媒体
date: 2024-04-08
fetch_date: 2025-10-04T12:14:51.655156
---

# Byakugan：针对葡语国家的恶意软件

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

# Byakugan：针对葡语国家的恶意软件

阅读量**118486**

发布时间 : 2024-04-07 10:54:07

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.securitylab.ru/news/547307.php>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全专家警告称，葡萄牙语国家将遭受新一波攻击，利用假冒 Adob​​e Reader 安装程序传播名为 Byakugan 的多功能恶意软件。

攻击从PDF文件开始，该文件打开后会显示模糊的图像，并提示受害者下载第三方应用程序以查看其内容。

[![]()](https://www.securitylab.ru/upload/medialibrary/618/k1k21g2ndor9tks6vyk2i988x30yhj40.png)

虚假通知（葡萄牙语翻译）

据Fortinet 的研究人员称，点击铭文会下载一个安装程序，启动感染过程。 网络情报中心ASEC上个月 首次发布了有关此活动的信息 。

该攻击技术涉及使用DLL 劫持和 Windows 用户帐户控制 ( UAC ) 绕过 等技术来下载恶意 DLL 文件，从而激活底层恶意代码。该过程还涉及 Wondershare PDFelement PDF 阅读器的合法安装程序。

该二进制文件能够收集系统元数据并将其传输到管理服务器，并加载主模块“chrome.exe”，该模块还充当管理服务器来接收文件和命令。

[![]()](https://www.securitylab.ru/upload/medialibrary/733/phatdnpl7lvgrb17o4dmjvuxgb5508lq.png)

*完整的攻击方案*

Byakugan 基于Node.js，包含多个负责各种功能的库：在系统中建立持久性、使用 OBS Studio 监控用户桌面、捕获屏幕截图、加载加密货币矿工、记录击键、库存和文件下载以及存储数据的盗窃在网络浏览器中。

在分析恶意软件的连接时，研究人员能够启动 Byakugan Web 控制面板，该面板会通过授权屏幕迎接不速之客。在打开的选项卡的一角，您可以看到一个白眼忍者的图标，这明显参考了火影忍者动漫。实际上，就像恶意软件本身的名称一样。

[![]()](https://www.securitylab.ru/upload/medialibrary/caf/2o2n7ek0ix8d0xrhiluhrzi2i8raquhh.png)

*恶意软件授权面板*

Fortinet 发现勒索软件中使用完全合法组件的趋势不断增长，这使得分析和检测威胁变得更加困难。

今天 我们写了一篇关于假冒安装程序的类似威胁 ： 美国石油和天然气公司部门面临网络钓鱼攻击，其中包含据称涉及受害者或她的汽车的事故通知。在可下载的 PDF 文件中，黑客同样使用背景模糊和模拟 Adob​​e Reader 的虚假通知来诱骗用户单击链接并安装 Rhadamanthys 恶意软件，该恶意软件会从受感染的系统收集数据。

本文翻译自 [原文链接](https://www.securitylab.ru/news/547307.php)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/295322](/post/id/295322)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.securitylab.ru/news/547307.php>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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