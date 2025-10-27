---
title: “SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载
url: https://www.anquanke.com/post/id/303878
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:45.643196
---

# “SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载

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

# “SparkCat” 恶意软件攻击：安卓与 iOS 用户受威胁，超 24.2 万次下载

阅读量**117809**

发布时间 : 2025-02-06 11:12:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/242000-times-downloaded-malicious-apps-from-android-and-ios/>

译文仅供参考，具体内容表达以及含义原文为准。

一项惊人的发现表明，研究人员揭露了一场广泛针对安卓和 iOS 用户的恶意软件攻击活动。

这场恶意活动被称为 “星火猫（SparkCat）”，涉及一些嵌入了恶意软件开发工具包（SDK）的应用程序，该 SDK 旨在窃取加密货币钱包的恢复短语。

部分受感染的应用程序在谷歌应用商店（Google Play）和苹果应用商店（App Store）均可获取，下载量已超过 24.2 万次。

安全信息与事件管理即服务（SIEM as a Service）

卡巴斯基实验室（Kaspersky Labs）的安全列表（SecureList）研究人员指出，这是已知的首例基于光学字符识别（OCR）技术的加密货币钱包间谍软件潜入苹果应用商店的案例。

“星火猫” 分析

“星火猫” 恶意软件使用了基于谷歌机器学习工具包（Google’s ML Kit）库构建的光学字符识别（OCR）插件，扫描设备相册中的图片，寻找与加密货币恢复短语相关的关键词。

该恶意软件利用了一个恶意的软件开发工具包 / 框架，该框架整合了谷歌机器学习工具包库以实现光学字符识别功能。

这些关键词包括 “助记词”（中文 “mnemonic” 的意思）、“ニーモニック”（日语 “mnemonic” 的意思）以及英文的 “Mnemonic”。一旦识别到相关图片，就会将其发送到命令与控制（C2）服务器进行进一步分析。在安卓系统中，恶意代码被发现在下载量超过 1 万次的 “ComeCome” 外卖应用程序（包名：com.bintiger.mall.android）中。

{
“keywords”: [“助记词”, “助記詞”, “ニーモニック”, “기억코드”, “Mnemonic”,
“Mnemotecnia”, “Mnémonique”, “Mnemotechnika”, “Mnemônico”,
“클립보드로복사”, “복구”, “단어”, “문구”, “계정”, “Phrase”]
}

下载量超 1 万次的 “ComeCome” 应用（来源 —— 安全列表）

在 iOS 系统中，恶意框架在多个苹果应用商店的应用程序中被发现，这些应用程序使用了如下名称：

* GZIP
* googleappsdk
* stat

苹果应用商店中的 “ComeCome” 页面（来源 —— 安全列表）

iOS 版本包含的调试符号显示其开发源自中文环境，路径包括 “/Users/qiongwu/” 和 “/Users/quiwengjing/”。

该恶意软件使用一种用 Rust 语言实现的未知协议与命令与控制服务器进行通信，Rust 语言在移动应用程序中并不常见。

包含恶意负载的热门应用（来源 —— 安全列表）

此协议涉及使用 AES – 256 加密算法的 CBC 模式对数据进行加密，并使用一个自定义库将自身伪装成一种常见的安卓混淆器。

围绕 viewDidLoad 方法的恶意包装器代码片段（来源 —— 安全列表）

在与 “rust” 服务器通信时，恶意软件遵循一个三阶段过程：

1. 加密：使用 AES – 256 加密算法的 CBC 模式对数据进行加密。
2. 压缩：使用 ZSTD 对加密后的数据进行压缩。
3. 传输：使用一个自定义库通过 TCP 套接字发送压缩后的数据。

{
“path”: “upload@<PATH>”,
“method”: “POST”,
“contentType”: “application/json”,
“data”: “<DATA>”
}

官方应用商店中出现此类恶意软件，表明威胁形势不断变化，加强安全措施势在必行。

建议用户谨慎授予应用程序权限，特别是那些请求访问如相册等敏感数据的权限。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/242000-times-downloaded-malicious-apps-from-android-and-ios/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303878](/post/id/303878)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/242000-times-downloaded-malicious-apps-from-android-and-ios/)

如若转载,请注明出处： <https://cybersecuritynews.com/242000-times-downloaded-malicious-apps-from-android-and-ios/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**7赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [新 Eleven11bot 黑客攻击 86,000 台 IP 摄像机，发动大规模 DDoS 攻击](/post/id/308201)

  2025-06-06 15:33:29
* ##### [黑客发起全球间谍行动，政府邮箱被利用XSS漏洞入侵](/post/id/307477)

  2025-05-16 18:05:26
* ##### [虚假CAPTCHA投递Lumma Stealer窃密木马](/post/id/306195)

  2025-04-03 15:14:44
* ##### [Hugging Face 上的恶意ML模型利用Pickle Format 格式来逃避检测](/post/id/304018)

  2025-02-10 10:47:45
* ##### [新的恶意广告活动正在分发假冒的 Cisco AnyConnect 安装程序](/post/id/304015)

  2025-02-10 10:31:39
* ##### [ASP.NET漏洞让黑客劫持服务器并注入恶意代码](/post/id/303978)

  2025-02-08 14:42:13
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