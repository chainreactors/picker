---
title: SSH-Snake：暗中搜索私钥实现横向移动
url: https://www.anquanke.com/post/id/293405
source: 安全客-有思想的安全新媒体
date: 2024-02-24
fetch_date: 2025-10-04T12:05:48.247536
---

# SSH-Snake：暗中搜索私钥实现横向移动

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

# SSH-Snake：暗中搜索私钥实现横向移动

阅读量**142284**

发布时间 : 2024-02-23 10:58:50

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

SSH-Snake 显示了企业网络感染的新水平。

网络安全公司Sysdig 发现了一种名为SSH -Snake 的新恶意工具，该工具用于搜索私钥并在受害者的基础设施中悄悄移动，使其比使用 SSH 的传统病毒危险得多。

SSH-Snake 被描述为“自我修改蠕虫”，与常规 SSH 蠕虫不同，它避免了与脚本攻击相关的常见行为模式，从而提供了更大的隐蔽性。该病毒主动在各个地方寻找私钥，包括shell命令历史文件，并在映射网络后利用它们传播到新系统。

SSH-Snake 作为一种基于 SSH 的自动化网络爬行工具 公开提供。然而，Sysdig 的研究人员强调，该工具通过更彻底地搜索私钥来改进横向移动的概念。

SSH-Snake 于 2024 年 1 月 4 日发布，是一个 bash shell 脚本，其工作是在受感染的系统上自主查找 SSH 凭据并使用它们进行传播。SSH-Snake 的伟大之处在于它能够在首次运行时通过删除代码中的注释、不必要的函数和空格来自我修改和减小其大小。

该工具用途广泛，可以根据特定的操作需求进行定制，包括查找私钥和识别其潜在用途的策略。SSH-Snake 使用各种直接和间接方法来发现受感染系统上的私钥。

Sysdig 分析师在发现操作员使用 命令和控制 ( C2 ) 服务器来存储收集到的数据（包括凭据、IP 地址和受害者历史记录） 后，确认了 SSH-Snake 的运行状态 。此数据表明，主动利用已知的 Confluence 漏洞（以及可能的其他漏洞）进行初始访问，导致端点上部署病毒。

据研究人员称，该工具已被用于攻击大约 100 名受害者。Sysdig 认为 SSH-Snake 是恶意软件领域的“进化一步”，因为它针对的是企业环境中广泛使用的安全连接方法。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/293405](/post/id/293405)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**6赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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