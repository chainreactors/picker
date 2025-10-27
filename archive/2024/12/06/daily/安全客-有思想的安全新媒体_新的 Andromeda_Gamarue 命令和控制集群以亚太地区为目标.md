---
title: 新的 Andromeda/Gamarue 命令和控制集群以亚太地区为目标
url: https://www.anquanke.com/post/id/302450
source: 安全客-有思想的安全新媒体
date: 2024-12-06
fetch_date: 2025-10-06T19:33:56.760499
---

# 新的 Andromeda/Gamarue 命令和控制集群以亚太地区为目标

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

# 新的 Andromeda/Gamarue 命令和控制集群以亚太地区为目标

阅读量**82256**

发布时间 : 2024-12-05 11:02:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/new-andromeda-gamarue-command-and-control-cluster-targets-apac-industries/>

译文仅供参考，具体内容表达以及含义原文为准。

![Andromeda malware]()

在最近的一份报告中，赛博瑞安全服务团队公布了与臭名昭著的 “Andromeda”（又名 Gamarue）恶意软件家族相关联的一个新的命令与控制（C2）服务器集群。这种恶意软件至少从 2011 年开始活跃，以模块化设计和适应性强而著称，是网络犯罪分子的多面手。Cybereason 的最新发现显示，该恶意软件的目标活动集中在亚太地区，重点是制造业和物流业。

Andromeda病毒历来通过恶意电子邮件附件、受感染的 USB 驱动器和次级有效载荷传播，现在它仍在继续发展。Cybereason解释说：“后门具有下载和执行其他恶意软件、窃取密码等敏感信息和创建远程访问后门的能力。这种灵活性使其成为工业间谍活动的一致选择。”

报告揭示了威胁行为者采用的复杂方法。最初的感染载体主要包括 “USB Drop 攻击”，即被入侵的 USB 驱动器在连接后自动执行恶意文件。一旦被感染，rundll32.exe 就会被用来加载伪装的 DLL，通常以 ~$W\*.USBDrv 或 ~$W\*.FAT32 等模式命名。

一项重要发现强调了 “desktop.ini ”文件是如何作为有效载荷启动恶意软件活动的，这些文件通常伪装成无害的系统文件。这些文件经常通过 WebDAV 下载，网络活动表明，它们连接到了用\*.malware.com 等常见名称下的证书注册的恶意域。

新的 C2 服务器集群展示了复杂的基础设施。在赛博瑞调查期间，一个 C2 域名 suckmycocklameavindustry[.]in解析到了多个IP地址。这种适应性实现了动态命令传递，确保了恶意软件与其操作者之间的不间断通信。

Cybereason 的团队强调说：“我们已经确定了一组 IP 地址，它们与 Andromeda 后门一起被用作 C2。”

报告指出了与臭名昭著的 Turla 组织（又名 UNC4210）的潜在联系。“报告指出：“这一特殊活动似乎是对旧版 Andromeda 样本的重新利用，其 C2 被 UNC4210 劫持。”

该活动的重点是破坏亚太地区的制造和物流公司，其动机涉嫌工业间谍活动。攻击者利用 Andromeda 的模块化设计来渗透网络、渗出敏感数据并执行进一步的有效载荷。

本文翻译自securityonline [原文链接](https://securityonline.info/new-andromeda-gamarue-command-and-control-cluster-targets-apac-industries/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302450](/post/id/302450)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-andromeda-gamarue-command-and-control-cluster-targets-apac-industries/)

如若转载,请注明出处： <https://securityonline.info/new-andromeda-gamarue-command-and-control-cluster-targets-apac-industries/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

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