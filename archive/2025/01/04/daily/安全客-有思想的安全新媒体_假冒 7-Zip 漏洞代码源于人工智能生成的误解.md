---
title: 假冒 7-Zip 漏洞代码源于人工智能生成的误解
url: https://www.anquanke.com/post/id/303224
source: 安全客-有思想的安全新媒体
date: 2025-01-04
fetch_date: 2025-10-06T20:08:57.054558
---

# 假冒 7-Zip 漏洞代码源于人工智能生成的误解

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

# 假冒 7-Zip 漏洞代码源于人工智能生成的误解

阅读量**66741**

发布时间 : 2025-01-03 10:12:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/fake-7-zip-exploit-code-ai-generated-misinterpretation/>

译文仅供参考，具体内容表达以及含义原文为准。

**摘要**

* X 上的一个用户（@NSA\_Employee39）声称发现了一个针对 7-Zip 的零日漏洞，声称存在严重的缓冲区溢出漏洞。
* 据称，该漏洞利用一个带有畸形 LZMA 流的伪造 .7z 压缩包来执行任意代码。
* 网络安全专家和 7-Zip 创建者伊戈尔-帕夫洛夫（Igor Pavlov）以不存在的功能和失败的复制尝试为由，驳斥了这一说法。
* 研究人员认为，漏洞利用代码可能是由人工智能生成的，这削弱了其可信度。
* 这一事件凸显了零日漏洞利用的持续威胁，以及采取强有力的网络安全措施的重要性。

最近，社交媒体平台 X（Twitter 的前身）上的一名用户声称拥有针对流行文件归档器 7-Zip 的零日漏洞，这在网络安全界引起了轩然大波。

该用户以 @NSA\_Employee39 为代号，声称他们发现了一个关键漏洞，攻击者可以利用 7-Zip 软件中的缓冲区溢出在受害者系统上执行任意代码。该用户在 Pastebin 上提供了一段代码，据称演示了这一漏洞。

“该漏洞利用的是 7-Zip 软件 LZMA 解码器中的一个漏洞。它使用带有畸形LZMA流的伪造.7z归档文件，在RC\_NORM函数中触发缓冲区溢出条件。”该用户在 Pastebin 上写道：“通过对齐偏移量和有效载荷，该漏洞操纵内部缓冲区指针来执行 shellcode，从而导致任意代码执行。”

尽管最初受到了关注，但网络安全专家很快开始对该漏洞的有效性表示怀疑。复制该漏洞的尝试未获成功，导致人们对代码的有效性产生怀疑。

后来，7-Zip 的创建者伊戈尔-帕夫洛夫（Igor Pavlov）驳斥了这一说法，他表示，所谓的漏洞依赖于一个函数（“RC\_NORM”），而这个函数在 7-Zip LZMA 解码器中并不存在。帕夫洛夫认为，该代码很可能是由人工智能模型生成的，这进一步削弱了其可信度。

此外，安全研究人员 @LowLevelTweets 报告称无法重现声称的漏洞，并表示在他们的测试过程中没有出现崩溃、挂起或超时的情况。这些发现表明，所报告的 7-Zip 零日漏洞可能是虚惊一场，可能是人为生成的代码或对软件内部工作原理的误解所致。

![Fake 7-Zip Exploit Code Traced to AI-Generated Misinterpretation]()
虽然这一特殊事件被证明是虚惊一场，但零日漏洞的威胁仍然令人严重担忧。这些漏洞非常危险，因为它们不为软件开发者所知，因此缺乏任何预先存在的防御措施。

上个月，Hackread 报告了一个 Windows 零日漏洞，允许攻击者通过欺骗方法窃取 NTLM 凭据。该漏洞影响了多个 Windows 系统，包括 Windows Server 2022、Windows 11（最高 v24H2）、Windows 10（多个版本）、Windows 7 和 Server 2008 R2。

要想远离零日漏洞，全面的安全软件非常重要，因为它可以针对各种威胁（包括病毒、恶意软件和零日漏洞）提供必要的保护。这些解决方案通常包括实时威胁检测、高级威胁防御和强大的隐私功能等功能，以保护用户免受网络安全威胁。

本文翻译自hackread [原文链接](https://hackread.com/fake-7-zip-exploit-code-ai-generated-misinterpretation/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303224](/post/id/303224)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-7-zip-exploit-code-ai-generated-misinterpretation/)

如若转载,请注明出处： <https://hackread.com/fake-7-zip-exploit-code-ai-generated-misinterpretation/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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