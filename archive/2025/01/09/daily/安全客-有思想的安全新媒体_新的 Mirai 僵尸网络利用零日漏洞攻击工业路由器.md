---
title: 新的 Mirai 僵尸网络利用零日漏洞攻击工业路由器
url: https://www.anquanke.com/post/id/303337
source: 安全客-有思想的安全新媒体
date: 2025-01-09
fetch_date: 2025-10-06T20:06:15.057740
---

# 新的 Mirai 僵尸网络利用零日漏洞攻击工业路由器

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

# 新的 Mirai 僵尸网络利用零日漏洞攻击工业路由器

阅读量**61202**

发布时间 : 2025-01-08 10:30:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-mirai-botnet-targets-industrial-routers-with-zero-day-exploits/>

译文仅供参考，具体内容表达以及含义原文为准。

![New Mirai botnet targets industrial routers with zero-day exploits]()

一个相对较新的基于 Mirai 的僵尸网络日益复杂，现在正利用零日漏洞攻击工业路由器和智能家居设备中的安全漏洞。

据监控僵尸网络发展和攻击的 Chainxin X 实验室研究人员称，对以前未知漏洞的利用始于 2024 年 11 月。

其中一个安全问题是 CVE-2024-12856，这是 VulnCheck 在 12 月底发现的 Four-Faith 工业路由器中的一个漏洞，但在 12 月 20 日左右注意到了利用该漏洞的努力。

VulnCheck 在 12 月底发现了 Four-Faith 工业路由器的 CVE-2024-12856 漏洞，但在 12 月 20 日左右发现了利用该漏洞的行为。

**僵尸网络简介**

该僵尸网络的名称暗指同性恋，它还依赖于针对 Neterbit 路由器和 Vimar 智能家居设备中未知漏洞的定制漏洞利用。

它于去年二月被发现，目前每天有 15,000 个活跃的僵尸节点，主要分布在中国、美国、俄罗斯、土耳其和伊朗。

它的主要目标似乎是对指定目标实施分布式拒绝服务（DDoS）以牟利，每天攻击数百个实体，其活动在 2024 年 10 月和 11 月达到高峰。

![Targeted countries]()
**目标国家**
来源：X 实验室

该恶意软件混合利用了 20 多个漏洞的公共和私人漏洞，向暴露在互联网上的设备传播，目标是 DVR、工业和家用路由器以及智能家居设备。

具体来说，它的目标如下：

* 华硕路由器（通过 N-day 漏洞利用）。
* 华为路由器（通过 CVE-2017-17215）
* Neterbit 路由器（自定义漏洞利用）
* LB-Link 路由器（通过 CVE-2023-26801）
* Four-Faith 工业路由器（通过现在被跟踪为 CVE-2024-12856 的零日漏洞）
* PZT 摄像机（通过 CVE-2024-8956 和 CVE-2024-8957）
* Kguard DVR
* Lilin DVR（通过远程代码执行漏洞）
* 通用 DVR（使用 TVT editBlackAndWhiteList RCE 等漏洞利用）
* Vimar 智能家居设备（可能使用了一个未披露的漏洞）
* 各种 5G/LTE 设备（可能通过错误配置或弱凭据进行攻击）

僵尸网络具有针对 Telnet 弱密码的暴力破解模块，使用带有独特签名的定制 UPX 包装，并实施基于 Mirai 的命令结构，用于更新客户端、扫描网络和进行 DDoS 攻击。

![Attack volumes]()
**僵尸网络攻击量**
来源：X 实验室

X Lab 报告称，僵尸网络的 DDoS 攻击持续时间很短，在 10 秒到 30 秒之间，但强度很高，流量超过 100 Gbps，即使对强大的基础设施也会造成破坏。

X Lab 解释说：“攻击目标遍布全球，分布在各个行业。”

研究人员说：“主要攻击目标分布在中国、美国、德国、英国和新加坡。”

总之，僵尸网络展示了一种独特的能力，即利用 n 天甚至零天漏洞，在不同设备类型中保持高感染率。

用户可以按照一般建议保护自己的设备，安装供应商提供的最新设备更新，在不需要时禁用远程访问，并更改默认的管理员账户凭据。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-mirai-botnet-targets-industrial-routers-with-zero-day-exploits/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303337](/post/id/303337)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-mirai-botnet-targets-industrial-routers-with-zero-day-exploits/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-mirai-botnet-targets-industrial-routers-with-zero-day-exploits/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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