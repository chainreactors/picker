---
title: Google Play、Apple App Store应用程序被发现窃取加密钱包
url: https://www.anquanke.com/post/id/303863
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:49.964038
---

# Google Play、Apple App Store应用程序被发现窃取加密钱包

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

# Google Play、Apple App Store应用程序被发现窃取加密钱包

阅读量**361483**

发布时间 : 2025-02-06 10:15:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/mobile/crypto-stealing-apps-found-in-apple-app-store-for-the-first-time/>

译文仅供参考，具体内容表达以及含义原文为准。

![Cryptocurrency falling]()

谷歌 Play 商店和苹果 App Store 上的安卓和 iOS 应用程序中，含有一种恶意软件开发工具包（SDK），该工具包旨在利用光学字符识别（OCR）窃取器，盗取加密货币钱包的恢复短语。

这场恶意活动被称为 “星火猫（SparkCat）”，名称源于受感染应用程序中恶意 SDK 的一个组件名 “星火（Spark）”，开发者很可能是在不知情的情况下参与到这场活动中的。

据卡巴斯基公司称，仅在可公开获取下载量数据的谷歌 Play 商店上，这些受感染应用的下载量就超过了 24.2 万次。

卡巴斯基解释说：“我们发现安卓和 iOS 应用嵌入了恶意 SDK / 框架，用于窃取加密货币钱包的恢复短语，其中一些应用在谷歌 Play 商店和 App Store 上都能找到。”

“受感染的应用在谷歌 Play 商店的下载量超过了 24.2 万次。这是已知的首次在 App Store 中发现此类窃取器。”

“星火” SDK 窃取你的加密货币
受感染安卓应用中的恶意 SDK 利用了一个名为 “星火” 的恶意 Java 组件，该组件伪装成一个分析模块。它使用存储在 GitLab 上的加密配置文件，该文件提供指令和操作更新。

在 iOS 平台上，该框架有不同的名称，如 “Gzip”“googleappsdk” 或 “stat”。此外，它利用一个基于 Rust 语言的网络模块 “im\_net\_sys”，来处理与命令控制（C2）服务器的通信。

![]()

该模块使用谷歌 ML Kit OCR 从设备上的图像中提取文本，试图找到恢复短语，这样攻击者无需知道密码，就能在自己的设备上加载加密货币钱包。

卡巴斯基解释说：“（恶意组件）会根据系统语言加载不同的 OCR 模型，以识别图片中的拉丁文、韩文、中文和日文字符。”

“然后，SDK 会沿着 /api/e/d/u 路径，将设备信息上传到命令服务器，作为回应，它会收到一个对象，该对象控制着恶意软件的后续操作。”

![URLs used to connect to Command and control servers]()

恶意软件通过使用不同语言的特定关键词，搜索包含机密信息的图像，这些关键词会因地区（欧洲、亚洲等）而异。

卡巴斯基表示，虽然一些应用表现出特定地区的针对性，但不能排除它们在指定地理区域之外也能运行的可能性。

受感染的应用程序

据卡巴斯基称，有 18 个受感染的安卓应用和 10 个 iOS 应用，其中许多在各自的应用商店中仍然可以找到。

卡巴斯基报告的受感染应用之一是安卓版 ChatAi 应用，其安装量超过 5 万次。该应用现已从谷歌 Play 商店下架。

![Laced app with 50,000 downloads on Google Play]()

卡巴斯基报告的末尾可找到受影响应用的完整列表。

如果你设备上安装了这些应用中的任何一个，建议你立即卸载，并使用移动杀毒工具扫描是否有残留。也可以考虑恢复出厂设置。

一般来说，应避免将加密货币钱包恢复短语存储在截图中。

相反，应将它们存储在物理离线介质、加密移动存储设备，或自托管的离线密码管理器的保险库中。

BleepingComputer 已联系苹果和谷歌，就各自应用商店中列出的这些应用的情况请求置评，我们将在收到他们的回复后更新此文章。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/mobile/crypto-stealing-apps-found-in-apple-app-store-for-the-first-time/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303863](/post/id/303863)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/mobile/crypto-stealing-apps-found-in-apple-app-store-for-the-first-time/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/mobile/crypto-stealing-apps-found-in-apple-app-store-for-the-first-time/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [数据泄露](/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [德克萨斯州交通部 (TxDOT) 数据泄露事件暴露了 30 万份车祸报告](/post/id/308355)

  2025-06-11 16:33:57
* ##### [税务解决方案公司 Optima Tax Relief 遭勒索软件攻击，数据泄露](/post/id/308262)

  2025-06-09 17:29:27
* ##### [美国电话电报公司（AT&T）再次遭遇大规模身份数据泄露事件](/post/id/308193)

  2025-06-06 15:22:45
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [DeepSeek数据泄露——12000个硬编码的有效API密钥和密码遭曝光](/post/id/304864)

  2025-02-28 15:37:26

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