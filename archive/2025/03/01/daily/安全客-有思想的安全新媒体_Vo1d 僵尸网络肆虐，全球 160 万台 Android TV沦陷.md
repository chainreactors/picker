---
title: Vo1d 僵尸网络肆虐，全球 160 万台 Android TV沦陷
url: https://www.anquanke.com/post/id/304833
source: 安全客-有思想的安全新媒体
date: 2025-03-01
fetch_date: 2025-10-06T21:55:53.950558
---

# Vo1d 僵尸网络肆虐，全球 160 万台 Android TV沦陷

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

# Vo1d 僵尸网络肆虐，全球 160 万台 Android TV沦陷

阅读量**81745**

发布时间 : 2025-02-28 10:42:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/vo1d-malware-botnet-grows-to-16-million-android-tvs-worldwide/>

译文仅供参考，具体内容表达以及含义原文为准。

![Android]()

一种名为 Vo1d 的恶意软件僵尸网络的新变种，已感染了来自 226 个国家的 1590299 台 Android TV设备，并将这些设备纳入其匿名代理服务器网络中。

这是根据 Xlab 的一项调查得出的结论。Xlab 自去年 11 月以来一直在追踪这一新的攻击活动，并报告称该僵尸网络在 2025 年 1 月 14 日达到峰值，目前拥有 80 万个活跃僵尸程序。

2024 年 9 月，Dr. Web的反病毒研究人员发现，有来自 200 个国家的 130 万台设备通过未知的感染途径被 Vo1d 恶意软件入侵。

XLab 最近的报告显示，Vo1d 僵尸网络的新版本仍在大规模运行，并未因之前被曝光而有所收敛。

此外，研究人员强调，该僵尸网络已进行了升级，采用了先进的加密技术（RSA + 自定义 XXTEA）、具备强大恢复能力的基于域名生成算法（DGA）的基础设施，以及增强的隐蔽能力。

![Vo1d botnet size over time]()

**Vo1d 僵尸网络规模随时间**
的变化*来源：XLab*

****庞大的僵尸网络规模****

Vo1d 僵尸网络是近年来出现的最大规模的僵尸网络之一，超过了Bigpanzi、最初的 Mirai僵尸网络，以及去年引发了由 Cloudflare 处理的创纪录的 5.6 Tbps DDoS 攻击的僵尸网络。

截至 2025 年 2 月，近 25% 的受感染设备来自巴西用户，其次是南非（13.6%）、印度尼西亚（10.5%）、阿根廷（5.3%）、泰国（3.4%）和中国（3.1%）的设备。

研究人员报告称，该僵尸网络的感染数量出现过显著激增，例如在印度，短短三天内僵尸程序数量就从 3900 个增加到了 21.7 万个。

最大幅度的波动表明，僵尸网络的操控者可能在 “出租” 这些设备作为代理服务器，而这些代理服务器通常被用于实施进一步的非法活动或自动化攻击。

“我们推测，‘快速激增后又急剧下降’这一现象可能是由于 Vo1d 将其在特定地区的僵尸网络基础设施出租给了其他团伙。以下是这种‘租赁 – 归还’循环的可能运作方式：

****租赁阶段****：

在租赁开始时，僵尸程序会从 Vo1d 的主网络中被转移出来，为承租人的活动服务。这种转移导致 Vo1d 的感染数量突然下降，因为这些僵尸程序暂时从其活跃设备池中被移除。

****归还阶段****：

一旦租赁期结束，这些僵尸程序会重新加入 Vo1d 网络。随着这些僵尸程序重新在 Vo1d 的控制下变得活跃，感染数量会迅速激增。

这种 “租赁和归还” 的循环机制可以解释在特定时间点观察到的 Vo1d 规模的波动情况。”

其命令与控制（C2）基础设施的规模也令人印象深刻，该僵尸网络使用了 32 个域名生成算法（DGA）种子，生成了超过 2.1 万个 C2 域名。

C2 通信由一个 2048 位的 RSA 密钥保护，因此即使研究人员识别并注册了一个 C2 域名，他们也无法向僵尸程序发出命令。

![Most impacted countries]()

**截至 2 月 25 日受影响最大的国家***来源：XLab*

****Vo1d 的功能****

Vo1d 僵尸网络是一种多功能的网络犯罪工具，它将受感染的设备转变为代理服务器，以协助实施非法活动。

受感染的设备会为网络犯罪分子中继恶意流量，隐藏他们活动的来源，并混入住宅网络流量中。这也有助于威胁行为者绕过地区限制、安全过滤和其他防护措施。

Vo1d 的另一个功能是广告欺诈，它通过模拟点击广告或在视频平台上的观看行为来伪造用户交互，从而为欺诈性广告商创造收入。

该恶意软件有特定的插件，可以自动进行广告交互并模拟类似人类的浏览行为，此外还有 Mzmess SDK，它会将欺诈任务分发给不同的僵尸程序。

鉴于感染途径仍然未知，建议Android TV用户采取全面的安全措施来应对 Vo1d 威胁。

第一步是从信誉良好的供应商和值得信赖的经销商处购买设备，以尽量减少恶意软件在出厂时或运输过程中被预装的可能性。

其次，安装固件和安全更新至关重要，这些更新可以填补可能被用于远程感染的漏洞。

第三，用户应避免从谷歌应用商店之外下载应用程序，或安装那些承诺提供扩展功能和 “解锁” 功能的第三方固件镜像。

如果不需要，Android TV设备应禁用其远程访问功能，并且在不使用时将其离线也是一种有效的策略。

最终，物联网设备应在网络层面与存储敏感数据的重要设备隔离开来。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/vo1d-malware-botnet-grows-to-16-million-android-tvs-worldwide/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304833](/post/id/304833)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/vo1d-malware-botnet-grows-to-16-million-android-tvs-worldwide/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/vo1d-malware-botnet-grows-to-16-million-android-tvs-worldwide/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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