---
title: 警惕！虚假 PDFCandy 网站传播 ArechClient2 恶意软件
url: https://www.anquanke.com/post/id/306587
source: 安全客-有思想的安全新媒体
date: 2025-04-17
fetch_date: 2025-10-06T22:02:48.830126
---

# 警惕！虚假 PDFCandy 网站传播 ArechClient2 恶意软件

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

# 警惕！虚假 PDFCandy 网站传播 ArechClient2 恶意软件

阅读量**46356**

发布时间 : 2025-04-16 10:51:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/fake-pdfcandy-websites-spread-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

CloudSEK 揭露了一场复杂的恶意软件攻击活动，在该活动中，攻击者冒充他人，通过 PDFCandy.com 来分发名为 ArechClient2 的信息窃取软件。攻击者利用了 PDFCandy.com 这一在线文件转换工具的高人气。该工具的用户数量超过 250 万，其中仅印度用户就超过 50 万。

根据他们与 Hackread.com 分享的研究，攻击者正在分发 ArechClient2 恶意软件，以窃取诸如浏览器用户名和密码之类的私人信息。ArechClient2 是自 2019 年起就活跃的 SectopRAT 家族恶意软件，通过 Google Ads 上的欺骗性在线广告或虚假软件更新进行传播。

据报道，攻击者创建了一个虚假的 PDF 转 DOCX 转换器网站，该网站与合法的 pdfcandy.com 十分相似。他们费尽心思模仿了真实网站的外观和感觉。CloudSEK 的研究人员在博客文章中指出，例如，他们使用相似的网址来欺骗毫无防备的用户，并且 “精心复制了正版平台的用户界面，还注册了外观相似的域名来误导用户”。

一旦用户进入这些虚假网站中的一个，他们会立刻被要求上传一个 PDF 文件进行转换，这正是利用了许多互联网用户的常见需求。网站甚至还会显示一个虚假的加载动画，就好像真的在进行转换一样，这可能是为了建立用户的信任。

然后，出乎意料的是，网站会弹出一个验证码验证界面，就像合法网站为了安全所设置的那样。报告中写道，这标志着攻击的关键一步，即 “从社会工程学手段过渡到对系统的入侵”。这意味着这次攻击依赖于对用户与网站典型交互方式的操控。

![]()

引入验证码有两个目的：一是让虚假网站看起来更真实，二是让用户不假思索地点击。接下来，网站会指示用户使用 Windows 内置工具 PowerShell 运行一条命令，从而导致系统被入侵。对该命令的分析显示，这是一系列的重定向操作，从一个看似无害的链接开始，最终指向一个名为 “adobe.zip” 的文件，该文件托管在 1728611543 这个地址上，并且已被多个安全服务机构标记为恶意文件。

该文件包含一个名为 “SoundBAND” 的文件夹，里面有一个危险的可执行文件 “audiobit.exe”。攻击者利用一个合法的 Windows 程序和一个 Windows 工具发起了一场多阶段攻击，从而启动了 ArechClient2 信息窃取恶意软件。

![Fake PDFCandy Websites Spread Malware via Google Ads]()

值得注意的是，美国联邦调查局（FBI）在 2025 年 3 月 17 日曾发出警告，称恶意在线文件转换器正被用于分发有害软件，所以这种威胁并非新出现的。

该机构解释道：“全球的网络犯罪分子正在利用各种类型的免费文档转换器或下载工具。这可能是一个声称可以将一种类型的文件转换为另一种类型文件的网站，比如将.doc 文件转换为.pdf 文件。它也可能声称可以合并文件，比如将多个.jpg 文件合并为一个.pdf 文件。可疑程序可能声称是一个 MP3 或 MP4 下载工具。”

为了防范此类威胁，在使用在线文件转换服务时应该保持谨慎，在上传文件之前核实网站的合法性，留意网址，并对意外出现的提示保持警惕。

本文翻译自hackread [原文链接](https://hackread.com/fake-pdfcandy-websites-spread-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306587](/post/id/306587)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-pdfcandy-websites-spread-malware/)

如若转载,请注明出处： <https://hackread.com/fake-pdfcandy-websites-spread-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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