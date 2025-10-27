---
title: 警惕！Vidar Stealer 利用新骗术窃取浏览器 Cookie 和存储凭据
url: https://www.anquanke.com/post/id/306311
source: 安全客-有思想的安全新媒体
date: 2025-04-10
fetch_date: 2025-10-06T22:04:01.011109
---

# 警惕！Vidar Stealer 利用新骗术窃取浏览器 Cookie 和存储凭据

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

# 警惕！Vidar Stealer 利用新骗术窃取浏览器 Cookie 和存储凭据

阅读量**55610**

发布时间 : 2025-04-09 11:16:53

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vidar-stealer-with-new-deception-technique/>

译文仅供参考，具体内容表达以及含义原文为准。

Vidar Stealer 是一种信息窃取恶意软件，于 2018 年首次被发现，如今它已演变出一种复杂的新欺骗技术，将目标对准了网络安全专业人员和系统管理员。

这款臭名昭著的恶意软件由 Arkei 木马演变而来，它不断改进，能够从受感染的系统中获取敏感数据，包括浏览器的 Cookies、存储的凭据以及财务信息。

这款信息窃取软件以恶意软件即服务（MaaS）的形式运行，在暗网市场上很容易就能买到，这使得技术水平有限的网络犯罪分子也能够实施复杂的攻击。

其近期的传播方式包括恶意电子邮件附件以及恶意广告活动，目的是诱骗用户下载并执行有效载荷。

2025 年 2 月，发生了一起特别值得关注的事件：在 Steam 上发布的一款免费游戏 PirateFi，其文件中隐藏了 Vidar Stealer，在毫无防备的玩家安装游戏时将其感染。

2025 年 3 月，G Data 安全研究人员发现了一个不同寻常的 Vidar Stealer 样本，它采用了一种特别复杂的欺骗技术。

这个样本最初在 VirusTotal 上仅被检测出有 5 次威胁，这表明它可能经过了混淆处理，或者是出现了一个新的变种。

此次发现特别令人担忧的地方在于，该恶意软件伪装成了合法的 Microsoft  Sysinternals 实用工具 BGInfo.exe。BGInfo.exe 是一款被广泛信任的系统管理工具，用于在桌面背景上显示系统信息。

这一最新的演变标志着该恶意软件在隐蔽策略上有了重大升级，因为恶意软件的编写者专门针对了 IT 专业人员和安全团队常用的工具。

通过入侵安全团队所依赖的实用工具，攻击者增加了成功渗透到拥有大量敏感数据的企业环境中的几率。

### ****欺骗技术****

这个 Vidar Stealer 变种所采用的欺骗技术在细节上非常用心。

这个恶意文件将自己伪装成 2025 年 2 月对合法 BGInfo 实用工具的一次更新，还带有一个已过期的 Microsoft 数字签名。

合法的 BGInfo.exe 大小约为 2.1 兆字节，而恶意变种的大小则明显更大，达到了 10.2 兆字节，这是因为其中隐藏了恶意代码 —— 这是一个表明软件有问题的关键迹象。

一旦被执行，该恶意软件就会修改 BGInfo.exe 的初始化例程，具体来说就是改变进程堆处理方式，以便进行未来的内存分配，并将执行重定向到其恶意函数。

这种巧妙的操纵确保了该文件运行的是恶意代码，而不是预期的 BGInfo 功能。

一个表明系统已被攻陷的明显迹象是，受感染的版本无法更新桌面壁纸 —— 而这是合法工具的一个关键功能。

技术分析显示，该恶意软件使用 VirtualAlloc 函数为其下一阶段的执行创建虚拟内存空间。

这个分配的内存最终会包含有效载荷的证据，在内存中可以看到诸如 “input.exe” 以及 MZ 头部（0x4D 0x5A）这样的字符串。

转储这个二进制文件后，会发现 Vidar Stealer 的核心组件，其编译日期为 2025 年 2 月 3 日。

该恶意软件精心伪装成一款受信任的管理工具，这凸显了威胁行为者不断演变的攻击策略，他们越来越多地将目标对准网络安全专业人员所信任的工具和软件。

建议各组织机构对所有软件更新实施严格的验证程序，即使是对受信任的实用工具也不例外，并且要监控系统是否存在异常行为，尤其是当管理工具无法按预期运行时。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vidar-stealer-with-new-deception-technique/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306311](/post/id/306311)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vidar-stealer-with-new-deception-technique/)

如若转载,请注明出处： <https://cybersecuritynews.com/vidar-stealer-with-new-deception-technique/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

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