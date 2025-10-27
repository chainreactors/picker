---
title: Nood RAT 攻击 Linux 服务器窃取敏感数据
url: https://www.anquanke.com/post/id/293471
source: 安全客-有思想的安全新媒体
date: 2024-02-28
fetch_date: 2025-10-04T12:06:08.822063
---

# Nood RAT 攻击 Linux 服务器窃取敏感数据

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

# Nood RAT 攻击 Linux 服务器窃取敏感数据

阅读量**180269**

发布时间 : 2024-02-27 12:12:36

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

最近发现 Nood RAT 用于针对 Linux 服务器的恶意软件攻击，以窃取敏感信息。

Gh0st RAT 的 Linux 兼容变体称为 Nood RAT。适用于 Linux 的 Gh0st RAT 不断被获取，尽管其频率低于适用于 Windows 的 Gh0st RAT。

特别是，Nood RAT是一种后门恶意软件，可能会执行下载恶意文件、窃取内部系统文件、执行命令等恶意操作。

尽管其形式很简单，但它可能会接收来自威胁行为者的命令来执行各种有害操作。它配备了加密功能，可以逃避网络数据包识别。

您可以使用ANY.RUN 恶意软件沙箱和威胁情报查找来分析恶意软件文件、网络、模块和注册表活动，威胁情报查找可让您直接从浏览器与操作系统进行交互。

恶意软件的亮点
AhnLab 安全情报中心 (ASEC) 报告称，Nood RAT 的压缩文件包括一个名为“NoodMaker.exe”的构建程序、一份发行说明以及一个名为“Nood.exe”的后门控制程序。

威胁参与者在创建 NoodMaker 时可以根据架构选择并使用与目标系统匹配的 x86 或 x64 二进制文件。

![]()
Nood RAT 生成器

Nood RAT 的功能之一是可以将其冒充为真实的程序。威胁行为者可以在开发阶段选择恶意软件的虚假进程名称。

该恶意软件在首次启动时使用 RC4 算法来解密加密数据。解密后的该字符串包含必须修改的进程的名称。

“恶意软件解密的配置数据主要分为 C&C 服务器地址、激活日期和时间以及 C&C 连接尝试间隔。

威胁行为者可以设置该恶意软件可以与 C&C 服务器通信并接收命令的激活日期和时间”，ASEC 研究人员与《网络安全新闻》分享。

![]()
受感染系统的信息发送到C&C服务器

Nood RAT支持的四个主要功能是端口转发、Socks代理、远程shell、文件管理和远程shell。

威胁行为者可以利用它来上传和下载文件、在受感染的系统上执行恶意命令以及窃取数据。

由于其源代码向公众开放，威胁行为者继续在攻击中使用这些代码，恶意软件开发人员也一直在利用它来创建各种变体。

此前使用Nood RAT的攻击包括WebLogic漏洞攻击（CVE-2017-10271） 和2020年的Cloud Snooper APT攻击。

用户应始终将相关系统升级到最新版本，并检查其凭据或环境配置，以防止此类安全问题。

CyberXtron 披露了妥协指标 (IoC) 信息。

此外，V3需要更新到最新版本以避免恶意软件感染。

您可以使用Perimeter81 恶意软件防护来阻止恶意软件，包括特洛伊木马、勒索软件、间谍软件、rootkit、蠕虫和零日攻击。所有这些都极其有害，可能会造成严重破坏并损坏您的网络。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293471](/post/id/293471)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**8赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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