---
title: Telegram Android 版本发现 0day 漏洞允许将恶意文件伪装成视频
url: https://www.anquanke.com/post/id/298336
source: 安全客-有思想的安全新媒体
date: 2024-07-26
fetch_date: 2025-10-06T17:40:20.502353
---

# Telegram Android 版本发现 0day 漏洞允许将恶意文件伪装成视频

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

# Telegram Android 版本发现 0day 漏洞允许将恶意文件伪装成视频

阅读量**106864**

发布时间 : 2024-07-25 15:05:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lukas Stefanko，文章来源：welivesecurity

原文地址：<https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

ESET 研究人员发现了一个针对 Android 版 Telegram 的零日漏洞，该漏洞出现在 2024 年 6 月 6 日的一个地下论坛帖子中，以未指定的价格出售。攻击者利用该漏洞滥用我们命名为 EvilVideo 的漏洞，可以通过 Telegram 频道、群组和聊天共享恶意 Android 负载，并使其显示为多媒体文件。

我们找到了该漏洞的一个示例，从而可以进一步分析它，并于2024 年 6 月 26 日向 Telegram 报告。7 月 11 日，他们发布了一个更新，修复了 Telegram 10.14.5 及以上版本中的漏洞。

> **博文的要点：**
>
> * 2024 年6 月 26 日，我们在一个地下论坛上发现了一个针对 Android 版 Telegram 的零日漏洞广告。
> * 我们将其利用的漏洞命名为 EvilVideo，并报告给 Telegram；他们的团队于 2024 年 7 月 11 日对其进行了修补。
> * EvilVideo 允许攻击者发送恶意负载，这些负载以视频文件的形式出现在未修补的 Android 版 Telegram 中。
> * 该漏洞仅适用于 Android Telegram 10.14.4 及更早版本。

## 发现

我们发现该漏洞正在地下论坛上出售：见图 2。

*![]()
图 2. 地下论坛上的帖子*

在帖子中，卖家展示了在公共 Telegram 频道中测试漏洞的截图和视频。我们能够识别出有问题的频道，漏洞仍然可用。这使我们能够获得有效载荷并自行测试。

## 分析

我们对该漏洞的分析显示，该漏洞适用于 Telegram 10.14.4 及更早版本。我们推测特定负载很可能是使用 Telegram API 制作的，因为它允许开发人员以编程方式将特制的多媒体文件上传到 Telegram 聊天或频道。

该漏洞似乎依赖于威胁者能够创建一个有效负载，该负载将 Android 应用程序显示为多媒体预览而不是二进制附件。一旦在聊天中共享，恶意负载就会显示为 30 秒的视频（图 3）。

*![]()
图 3. 漏洞示例*

默认情况下，通过 Telegram 接收的媒体文件设置为自动下载。这意味着启用该选项的用户一旦打开共享的对话，就会自动下载恶意负载。可以手动禁用该选项 – 在这种情况下，仍然可以通过点击共享视频左上角的下载按钮来下载负载，如图 3 所示。

如果用户尝试播放“视频”，Telegram 会显示一条消息，提示无法播放，并建议使用外部播放器（见图 4）。这是我们在合法 Telegram for Android 应用程序源代码中发现的原始 Telegram 警告；它不是由恶意负载制作和推送的。

![]()

*图 4. Telegram 警告无法播放“视频”*

然而，如果用户点击显示消息中的“打开”按钮，他们将被要求安装伪装成上述外部播放器的恶意应用程序。如图5所示，在安装之前，Telegram会要求用户启用未知应用程序的安装。

![]()

*图 5. Telegram 请求用户允许其安装未知应用程序*

此时，涉案恶意应用程序已作为视频文件下载，但扩展名为.apk。有趣的是，漏洞的性质使得共享文件看起来像视频 – 实际的恶意应用程序并未被修改为多媒体文件，这表明上传过程很可能被利用。恶意应用程序的安装请求可以在图 6 中看到。

![]()

*图6. 请求安装恶意负载，利用后检测为Android/Spy.SpyMax.T*

不幸的是，我们无法复制该漏洞，只能检查并验证卖家共享的样本。

### Telegram 网页版和桌面版

尽管该有效载荷仅针对 Android 版 Telegram，但我们仍尝试在其他 Telegram 客户端上测试其行为。我们测试了 Telegram Web 客户端和 Windows 版 Telegram 桌面客户端 – 正如预期的那样，该漏洞在它们中均不起作用。

对于 Telegram Web 来说，在我们尝试播放“视频”后，客户端会显示一条错误消息，提示我们尝试使用桌面应用打开视频（见图 7）。手动下载附件后，我们发现其名称和扩展名为Teating.mp4。虽然文件本身实际上是一个 Android 可执行二进制文件 (APK)，但 Telegram 将其视为 MP4 文件，从而阻止了漏洞利用：要想成功利用该漏洞，附件必须具有 .apk 扩展名。

Windows 版 Telegram Desktop 客户端也发生了类似的事情：下载的文件名为Teating.apk.mp4，因此它再次是一个扩展名为.mp4的 APK 二进制文件。这表明，即使攻击者制作了一个 Windows 可执行文件来代替 Android APK，它仍将被视为多媒体文件，漏洞利用将无法奏效。

![]()

*图 7. 触发漏洞时 Telegram Web 发出的错误消息*

## 威胁行为者

虽然我们对威胁行为者了解不多，但我们根据卖家在论坛帖子中分享的 Telegram 账号找到了他们提供的另一项可疑服务。除了漏洞之外，自 2024 年 1 月 11 日起，他们一直在使用同一个地下论坛来宣传他们声称完全无法检测 (FUD) 的 Android 加密即服务。论坛帖子如图8所示。

![]()

*图 8. 地下论坛帖子宣传 Android 加密即服务*

## 漏洞报告

在 2024 年 6 月 26日发现 EvilVideo 漏洞后，我们遵循协调披露政策并将其报告给 Telegram，但当时没有收到任何回复。我们于 7 月 4日再次报告了该漏洞，当时 Telegram 在同一天联系我们，确认其团队正在调查 EvilVideo。他们修复了该问题，于 7 月 11 日发布了 10.14.5 版本，并通过电子邮件通知了我们。

该漏洞影响了 Android 版 Telegram 的所有版本，最高版本为 10.14.4，但从 10.14.5 版本开始已修复。经我们验证，聊天多媒体预览现在正确显示共享文件是一个应用程序（图 9），而不是视频。

![]()

*图 9. Telegram 版本 10.14.5 聊天正确显示共享二进制文件的性质*

## 结论

我们在一个地下论坛上发现了一个用于 Android 的零日 Telegram 漏洞。它利用的漏洞允许通过 Telegram 聊天发送看起来像多媒体文件的恶意负载。如果用户尝试播放看似视频的视频，他们将收到安装外部应用程序的请求，该应用程序实际上会安装恶意负载。幸运的是，在我们向 Telegram 报告该漏洞后，该漏洞已于 2024 年7 月 11日得到修复。

本文翻译自welivesecurity [原文链接](https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298336](/post/id/298336)

安全KER - 有思想的安全新媒体

本文转载自: [welivesecurity](https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/)

如若转载,请注明出处： <https://www.welivesecurity.com/en/eset-research/cursed-tapes-exploiting-evilvideo-vulnerability-telegram-android/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

### 热门推荐

文章目录

* [发现](#h2-0)
* [分析](#h2-1)
  + [Telegram 网页版和桌面版](#h3-2)
* [威胁行为者](#h2-3)
* [漏洞报告](#h2-4)
* [结论](#h2-5)

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