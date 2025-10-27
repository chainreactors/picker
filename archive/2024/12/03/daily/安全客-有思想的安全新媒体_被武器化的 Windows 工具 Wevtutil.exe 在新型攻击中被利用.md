---
title: 被武器化的 Windows 工具 Wevtutil.exe 在新型攻击中被利用
url: https://www.anquanke.com/post/id/302321
source: 安全客-有思想的安全新媒体
date: 2024-12-03
fetch_date: 2025-10-06T19:33:15.662683
---

# 被武器化的 Windows 工具 Wevtutil.exe 在新型攻击中被利用

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

# 被武器化的 Windows 工具 Wevtutil.exe 在新型攻击中被利用

阅读量**98381**

发布时间 : 2024-12-02 11:19:00

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/windows-tool-weaponized-wevtutil-exe-exploited-in-novel-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

![Windows Tool]()

安全研究人员揭示了 Living Off the Land 二进制文件和脚本 （LOLBAS） 武器库中的一个新方面：Windows wevtutil.exe 在秘密、恶意操作方面鲜为人知的潜力。Tonmoy Jitu 的深入分析揭示了这个专为事件日志管理而设计的合法实用程序如何成为攻击者手中的危险工具。

Wevtutil.exe 是 Windows 捆绑的命令行工具，主要用于系统管理员的事件日志管理。其功能包括

* 将日志导出为 XML。
* 清除整个事件日志。
* 使用特定条件查询日志。

然而，正如 Jitu 所指出的，“这些功能使 wevtutil.exe 成为一把双刃剑：虽然对合法操作非常宝贵，但它们也可以帮助攻击者掩盖踪迹或渗漏信息。”

攻击者越来越多地采用 LOLBAS 技术，通过使用可信的预装工具来逃避检测。Wevtutil.exe存在于所有Windows系统中，这使它成为此类漏洞利用的热门候选工具。

**清除日志以规避检测**

wevtutil cl Application 等命令允许攻击者清除事件日志，使防御者难以追踪恶意活动。
然而，正如报告强调的那样，试图清除安全日志会生成可检测的事件 ID 1102： “清除安全日志会生成事件 ID 1102……使防御者非常容易察觉。

**导出日志进行数据渗透**

使用 wevtutil qe Security /f:xml > exported\_logs.xml 等命令，攻击者可以导出日志来分析敏感数据或外泄关键信息。
这项活动需要提升权限，以确保防止未经授权的使用。

**通过日志查询进行侦察**
攻击者可以精确地查询日志，以深入了解系统或用户活动。例如

```
wevtutil qe Security /q:"*[System[EventID=4624]]"
```

该命令可检索成功登录事件，为后续行动提供有价值的情报。

与 PowerShell 等被广泛监控的工具不同，wevtutil.exe 经常逃过检查。Jitu 指出：“使用不太常见的实用程序可以躲过主要针对广泛使用的工具的传统检测机制。”

为了应对 wevtutil.exe 的滥用，企业应该考虑以下几点：

1. **加强监控**
   跟踪通过 wevtutil.exe 执行的异常命令。
   为合法使用设置基线，以检测异常情况。
2. **集中日志记录**
   集中汇总日志，防止攻击者在本地掩盖踪迹。
3. **行为分析**
   利用分析来识别显示 LOLBAS 技术的模式。

Jitu 在报告中总结道： “了解这些行为对于利用这一工具的红色团队和旨在检测并减少其滥用的防御者来说都至关重要。”

本文翻译自securityonline [原文链接](https://securityonline.info/windows-tool-weaponized-wevtutil-exe-exploited-in-novel-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302321](/post/id/302321)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/windows-tool-weaponized-wevtutil-exe-exploited-in-novel-attack/)

如若转载,请注明出处： <https://securityonline.info/windows-tool-weaponized-wevtutil-exe-exploited-in-novel-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [勒索攻击](/tag/%E5%8B%92%E7%B4%A2%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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