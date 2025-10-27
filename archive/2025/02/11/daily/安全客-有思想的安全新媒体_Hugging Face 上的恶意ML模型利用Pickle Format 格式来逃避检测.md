---
title: Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测
url: https://www.anquanke.com/post/id/304018
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:56.417550
---

# Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测

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

# Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测

阅读量**298835**

发布时间 : 2025-02-10 10:47:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员在 Hugging Face 上发现了两个恶意机器学习（ML）模型，这些模型利用一种不同寻常的 “损坏” 的 pickle 文件技术来逃避检测。

“从上述 PyTorch 存档中提取的 pickle 文件在文件开头就显示出恶意的 Python 内容，”ReversingLabs 研究员卡罗・赞基（Karlo Zanki）在与《黑客新闻》分享的一份报告中说道，“在这两个案例中，恶意负载是一种典型的可感知平台的反向 shell，它会连接到一个硬编码的 IP 地址。”

这种方法被称为 nullifAI，因为它明显试图绕过现有的用以识别恶意模型的防护措施。以下是相关的 Hugging Face 代码库：

1.glockr1/ballr7

2.who-r-u0000/0000000000000000000000000000000000000

据信，这些模型更多是概念验证（PoC），而非实际的供应链攻击场景。

pickle 序列化格式常用于分发机器学习模型，但人们反复发现它存在安全风险，因为一旦加载并反序列化，它就提供了执行任意代码的途径。

这家网络安全公司检测到的两个模型以 PyTorch 格式存储，其实就是压缩的 pickle 文件。虽然 PyTorch 默认使用 ZIP 格式进行压缩，但已发现被识别的模型是使用 7z 格式压缩的。

因此，这种行为使得这些模型能够躲过检测，避免被 Picklescan 标记为恶意文件，Picklescan 是 Hugging Face 用于检测可疑 pickle 文件的工具。

赞基说：“关于这个 pickle 文件，有趣的一点是，对象序列化（pickle 文件的目的）在恶意负载执行后不久就中断了，导致对象反编译失败。”

进一步分析表明，由于 Picklescan 与反序列化实际工作方式之间的差异，这种损坏的 pickle 文件仍可部分反序列化，尽管该工具会抛出错误消息，但恶意代码仍会被执行。此后，这个开源工具已更新以修复此漏洞。

赞基指出：“这种行为的解释是，对象反序列化是按顺序对 pickle 文件执行的。”

“pickle 操作码在遇到时就会执行，直到所有操作码执行完毕或遇到损坏的指令。在发现的模型案例中，由于恶意负载被插入到 pickle 流的开头，Hugging Face 现有的安全扫描工具不会将模型的执行检测为不安全。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304018](/post/id/304018)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html)

如若转载,请注明出处： <https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [新 Eleven11bot 黑客攻击 86,000 台 IP 摄像机，发动大规模 DDoS 攻击](/post/id/308201)

  2025-06-06 15:33:29
* ##### [黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵](/post/id/307477)

  2025-05-16 18:05:26
* ##### [虚假CAPTCHA投递Lumma Stealer窃密木马](/post/id/306195)

  2025-04-03 15:14:44
* ##### [新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序](/post/id/304015)

  2025-02-10 10:31:39
* ##### [ASP.NET漏洞让黑客劫持服务器并注入恶意代码](/post/id/303978)

  2025-02-08 14:42:13
* ##### [“SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载](/post/id/303878)

  2025-02-06 11:12:51
* ##### [400,000+ 系统受感染：DigitalPulse 代理软件带着新技巧回归](/post/id/303738)

  2025-01-23 09:38:26

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