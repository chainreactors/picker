---
title: 臭名昭著的黑客组织 TeamTNT 启动新的加密货币挖矿云攻击
url: https://www.anquanke.com/post/id/301317
source: 安全客-有思想的安全新媒体
date: 2024-10-29
fetch_date: 2025-10-06T18:49:02.504727
---

# 臭名昭著的黑客组织 TeamTNT 启动新的加密货币挖矿云攻击

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

# 臭名昭著的黑客组织 TeamTNT 启动新的加密货币挖矿云攻击

阅读量**64728**

发布时间 : 2024-10-28 11:11:32

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html>

译文仅供参考，具体内容表达以及含义原文为准。

臭名昭著的加密劫持组织 TeamTNT 似乎正准备发起一场新的大规模攻势，目标是在云原生环境中挖掘加密货币，并将被攻破的服务器出租给第三方。

云安全公司 Aqua 的威胁情报总监 Assaf Morag 在周五发布的一份报告中说：“该组织目前正以暴露的 Docker 守护进程为目标，部署 Sliver 恶意软件、网络蠕虫和加密矿机，利用被入侵的服务器和 Docker Hub 作为传播恶意软件的基础设施。”

该攻击活动再次证明了威胁行为者的持久性及其不断改进战术和发动多阶段攻击的能力，其目标是入侵 Docker 环境并将其纳入 Docker Swarm。

除了使用 Docker Hub 托管和分发恶意有效载荷外，据观察，TeamTNT 还将受害者的计算能力提供给其他方进行非法加密货币挖矿，使其货币化策略多样化。

本月早些时候，Datadog 披露了将受感染的 Docker 实例集中到 Docker Swarm 中的恶意尝试，暗指这可能是 TeamTNT 所为，但同时也没有做出正式归因。但直到现在，这一行动的全部范围还不清楚。

莫拉格告诉《黑客新闻》，Datadog “在非常早期的阶段就发现了基础设施”，他们的发现 “迫使威胁行为者稍微改变了一下活动”。

这些攻击需要使用masscan和ZGrab识别未经身份验证和暴露的Docker API端点，并将其用于加密矿机部署，然后在一个名为Mining Rig Rentals的挖矿租赁平台上将被攻陷的基础设施出售给他人，有效地卸载了必须自己管理的工作，这是非法商业模式成熟的标志。

具体来说，这是通过一个攻击脚本来实现的，该脚本会扫描近 1670 万个 IP 地址的 2375、2376、4243 和 4244 端口上的 Docker 守护进程。随后，它部署了一个运行带有恶意命令的 Alpine Linux 映像的容器。

该镜像是从其控制下的一个受攻击 Docker Hub 账户（“nmlm99”）中获取的，它还执行了一个名为 Docker Gatling Gun 的初始 shell 脚本（“TDGGinit.sh”），以启动后剥削活动。

Aqua 观察到的一个显著变化是从 Tsunami 后门转向开源的 Sliver 命令与控制（C2）框架，用于远程控制受感染的服务器。

莫拉格说：“此外，TeamTNT 继续使用其既定的命名惯例，如 Chimaera、TDGG 和 bioset（用于 C2 操作），这强化了这是一个典型的 TeamTNT 活动的想法。”

“在这次活动中，TeamTNT 还使用了 anondns（AnonDNS 或匿名 DNS 是一种概念或服务，旨在解决 DNS 查询时提供匿名性和隐私性），以便指向他们的网络服务器。”

在趋势科技公布这些发现的同时，还揭露了一个新的活动，该活动涉及对一个未具名客户进行有针对性的暴力破解攻击，以提供 Prometei 加密挖矿僵尸网络。

该公司表示：“Prometei 通过利用远程桌面协议（RDP）和服务器消息块（SMB）中的漏洞在系统中传播，”它强调了威胁行为者在设置持久性、逃避安全工具以及通过凭证转储和横向移动更深入地访问组织网络方面所做的努力。

“受影响的机器会连接到一个矿池服务器，该服务器可用于在受害者不知情的情况下在受影响的机器上挖掘加密货币（Monero）”。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301317](/post/id/301317)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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