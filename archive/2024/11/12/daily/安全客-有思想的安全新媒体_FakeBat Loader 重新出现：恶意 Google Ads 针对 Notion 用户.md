---
title: FakeBat Loader 重新出现：恶意 Google Ads 针对 Notion 用户
url: https://www.anquanke.com/post/id/301685
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:24.716374
---

# FakeBat Loader 重新出现：恶意 Google Ads 针对 Notion 用户

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

# FakeBat Loader 重新出现：恶意 Google Ads 针对 Notion 用户

阅读量**65967**

发布时间 : 2024-11-11 14:11:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/fakebat-loader-reemerges-malicious-google-ads-target-notion-users/>

译文仅供参考，具体内容表达以及含义原文为准。

![FakeBat loader]()

臭名昭著的 FakeBat 载入器（又称 Eugenloader 或 PaykLoader）在中断数月后又卷土重来，通过冒充 Notion（一款流行的生产力应用程序）的恶意谷歌广告传播恶意软件。据 Malwarebytes 实验室称，“FakeBat 是一种独特的加载器，曾被用于投放 Lumma stealer 等后续有效载荷”，这表明威胁行为体再次转向恶意广告来分发恶意有效载荷。

这一活动展示了 FakeBat 操作员如何利用谷歌的广告平台来掩饰其恶意意图。最近出现在 “Notion ”搜索结果顶部的一则广告看起来是真实的，带有 Notion 的官方徽标，URL 看起来也是真实的。Malwarebytes 研究人员发现，该广告引导用户进行了一连串复杂的重定向。报告详细指出：“如果用户不是目标受害者，跟踪模板会将他们重定向到合法的 notion.so 网站，”这增加了检测难度。

![]()恶意广告 | 图片： 恶意软件比特实验室

FakeBat 加载器会下载 LummaC2，这是一款功能强大的数据窃取恶意软件，专门用于捕获凭证、cookie 和财务信息。在通过指纹识别躲过安全沙箱后，加载器使用 PowerShell 脚本绕过微软的反恶意软件扫描接口 (AMSI)，使其在未被发现的情况下运行。Malwarebytes解释说：“加载器使用.NET Reactor进行混淆，它使用AES解密嵌入式资源，然后通过进程空洞化将其注入MSBuild.exe”，突出了FakeBat用于部署其有效载荷的复杂技术。

Malwarebytes警告说：“通过谷歌广告冒充品牌仍然是个问题，因为任何人都可以利用内置功能来显示合法并诱骗用户下载恶意软件。”

本文翻译自securityonline [原文链接](https://securityonline.info/fakebat-loader-reemerges-malicious-google-ads-target-notion-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301685](/post/id/301685)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/fakebat-loader-reemerges-malicious-google-ads-target-notion-users/)

如若转载,请注明出处： <https://securityonline.info/fakebat-loader-reemerges-malicious-google-ads-target-notion-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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