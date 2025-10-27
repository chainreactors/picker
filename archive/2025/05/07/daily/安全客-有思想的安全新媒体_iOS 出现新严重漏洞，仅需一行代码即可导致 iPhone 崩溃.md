---
title: iOS 出现新严重漏洞，仅需一行代码即可导致 iPhone 崩溃
url: https://www.anquanke.com/post/id/307112
source: 安全客-有思想的安全新媒体
date: 2025-05-07
fetch_date: 2025-10-06T22:24:44.111542
---

# iOS 出现新严重漏洞，仅需一行代码即可导致 iPhone 崩溃

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

# iOS 出现新严重漏洞，仅需一行代码即可导致 iPhone 崩溃

阅读量**86023**

发布时间 : 2025-05-06 15:07:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源： cybersecuritynews

原文地址：<https://cybersecuritynews.com/ios-critical-vulnerability-brick-iphones/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

iOS 中的一个严重漏洞可能允许恶意应用程序仅使用一行代码即可永久禁用 iPhone。

该漏洞的编号为 CVE-2025-24091，利用操作系统的 Darwin 通知系统触发无限重启循环，导致设备“变砖”，需要进行完整的系统还原。

## iOS Darwin 通知漏洞

该漏洞利用了 Darwin 通知，这是 CoreOS 层内的一种低级消息传递机制，允许进程传达系统范围的事件。

与 NSNotificationCenter 或 NSDistributedNotificationCenter 等更常见的通知系统不同，Darwin 通知是 Apple 操作系统中在基础层面上运行的旧式 API 的一部分。

Darwin 通知更加简单，因为它们是 CoreOS 层的一部分。它们提供了一种低级机制，用于在 Apple 操作系统的进程之间进行简单的消息交换。发现该漏洞的安全研究员 Guilherme Rambo 解释道。

这个严重缺陷的根源在于，iOS 上的任何应用程序都可以发送敏感的系统级 Darwin 通知，而无需特殊权限或授权。

 最危险的是，这些通知可以触发强大的系统功能，包括进入“正在恢复”模式。

## 单行漏洞利用

该漏洞利用非常简单——只需一行代码即可触发该漏洞：

![]()![]()

执行此代码后，设备会强制进入“正在恢复”状态。由于实际恢复过程并未发生，因此该过程必然会失败，提示用户重启设备。研究人员创建了一个名为“VeryEvilNotify”的概念验证攻击，并在一个小部件扩展中实现了此漏洞。

研究人员指出：  “iOS 会定期在后台唤醒 Widget 扩展程序。”

“由于系统中小部件的使用非常广泛，当安装并启动包含小部件扩展的新应用程序时，系统非常渴望执行其小部件扩展”。

通过将漏洞利用程序放置在发送通知后反复崩溃的小部件中，研究人员创建了一种在每次重启后都会触发的持续性攻击，从而形成了一个无限循环，导致设备无法使用。

|  |  |
| --- | --- |
| **风险因素** | **细节** |
| 受影响的产品 | iOS（运行 iOS/iPadOS 18.3 之前版本的 iPhone 和 iPad） |
| 影响 | 拒绝服务（DoS） |
| 漏洞利用前提条件 | 任何沙盒应用程序或小部件扩展都可以触发此漏洞；无需特殊权限 |
| CVSS 3.1 评分 | 高的 |

## 缓解措施

苹果通过为敏感的 Darwin 通知实施新的授权系统，解决了 iOS 18.3 中的漏洞。研究人员获得了 17,500 美元的漏洞赏金。

具体来说，系统通知现在需要前缀“com.apple.private.restrict-post”，并且发送进程必须拥有“com.apple.private.darwin-notification.restrict-post.<notification>”形式的受限权限。

这并不是苹果系统中第一个与达尔文相关的漏洞。此前，卡巴斯基实验室发现了一个“达尔文核弹”漏洞，该漏洞可能允许远程攻击者通过特制的网络数据包发起拒绝服务攻击。

强烈建议所有 iPhone 用户立即更新至 iOS 18.3 或更高版本。运行早期版本的设备仍然容易受到此攻击，该攻击可能通过 App Store 或其他分发渠道中看似无害的应用程序或小部件进行部署。

该案例凸显了移动操作系统中持续存在的安全挑战，即使是简单且被忽视的遗留 API，如果保护不当，也可能带来重大风险。

本文翻译自 cybersecuritynews [原文链接](https://cybersecuritynews.com/ios-critical-vulnerability-brick-iphones/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307112](/post/id/307112)

安全KER - 有思想的安全新媒体

本文转载自:  [cybersecuritynews](https://cybersecuritynews.com/ios-critical-vulnerability-brick-iphones/)

如若转载,请注明出处： <https://cybersecuritynews.com/ios-critical-vulnerability-brick-iphones/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [iOS Darwin 通知漏洞](#h2-0)
* [单行漏洞利用](#h2-1)
* [缓解措施](#h2-2)

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