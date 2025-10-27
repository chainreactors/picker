---
title: VexTrio曝光：Infoblox揭露了大规模的恶意Adtech生态系统，为全球恶意软件提供动力
url: https://www.anquanke.com/post/id/308492
source: 安全客-有思想的安全新媒体
date: 2025-06-17
fetch_date: 2025-10-06T22:47:54.660922
---

# VexTrio曝光：Infoblox揭露了大规模的恶意Adtech生态系统，为全球恶意软件提供动力

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

# VexTrio曝光：Infoblox揭露了大规模的恶意Adtech生态系统，为全球恶意软件提供动力

阅读量**41458**

发布时间 : 2025-06-16 16:01:38

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/vextrio-exposed-infoblox-uncovers-massive-malicious-adtech-ecosystem-powering-global-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![VexTrio, Malicious Adtech]()

当 Infoblox 研究人员着手破坏臭名昭著的流量分配系统 （TDS） VexTrio 时，他们没想到会发现现存最庞大、最持久的恶意软件生态系统之一。最初的“观察*和观察*”实验变成了对恶意广告技术、基于 DNS 的恶意软件活动和全球网站入侵的深刻纠缠世界的全面揭露。

2024 年 11 月 13 日，Qurium 曝光：瑞士-捷克广告技术公司 Los Pollos 与已知最大的恶意 TDS VexTrio 有关。仅仅几天后，Los Pollos 突然关闭了他们的“*推送链接货币化*”服务。在外人看来，这似乎是捍卫者的胜利。但正如 Infoblox 所观察到的那样，犯罪网络并没有瓦解——它只是改变了方向。

到 11 月 20 日，多个长期活跃的恶意软件活动（如 DollyWay、Balada 和 Sign1）同时停止将受害者重定向到 VexTrio，而是将他们引流到一项“新”服务中：Help TDS。但这根本不是什么新鲜事。

“*Help TDS 并不新鲜，但多年来一直与 VexTrio 交织*在一起，”研究人员发现。事实上，它与以前被称为一次性 TDS 的系统相同，只是更名但架构相同。

这项调查的主要部分围绕基于 DNS 的命令和控制 （C2） 基础设施展开。嵌入在超过 25,000 个 WordPress 网站中的恶意软件使用 DNS TXT 记录来中继编码的重定向指令。这些 C2 服务器（分为两个独立托管的集群）曾经将流量路由到 VexTrio，但在 Los Pollos 关闭后，它们同步了作以转向 Help TDS。

![]()

联属网络在恶意广告技术中的作用概要 |图片来源： Infoblox

> “*通过分析 450 万条 DNS TXT 记录响应…我们发现，营销活动中使用的域分为两个不同的集合，每个集合都有不同的 C2 服务器*。
>
> 这种转变不仅显示了技术协调，还显示了组织的弹性。尽管 GoDaddy 的研究人员证实 DollyWay 已从 VexTrio 过渡，但 Infoblox 指出，一些基于 DNS 的活动在 2025 年 5 月之前继续引导受害者帮助 TDS。
>
> 该报告揭开了推动这些活动的阴暗商业模式的面纱：恶意广告技术。
>
> 核心是伪装成联盟广告网络的商业运营商 Los Pollos、Taco Loco、BroPush、Partners House 和 RichAds。他们以在线广告为幌子分发恶意负载、虚假抽奖和推送通知诈骗。
>
> > “*这些公司在允许网络附属公司加入之前会对其进行审查——我们知道，我们已经尝试过了——他们维护有关附属公司及其付款的个人信息，这可能会导致他们的身份*。”
>
> 所谓的“*发布附属公司*”——通常是网站黑客——将流量重定向到 TDS，根据受害者的互动来赚钱。交付的内容很少是无辜的。它是武器化的广告、信息窃取程序和伪装成 CAPTCHA 的浏览器劫持推送通知。
>
> 技术工件进一步证实了这些恶意网络之间的深度互连。Infoblox 发现了用于在诈骗页面上诱捕用户的罕见 JavaScript 以及 logo.png 和 bot.png 等独特诱饵图像，这些图像在 VexTrio、Help TDS 和 RichAds 等六个 TDS 之间共享。
>
> > “*这六个 TDS 共享图像诱饵……它们的 SHA256 文件哈希值匹配…所有这些都由专门从事推送广告的大型公共联盟网络运营*。
>
> 这些公司甚至使用相同的基础设施怪癖：DNS 配置错误、PowerDNS 安装以及跨平台跟踪受害者的自定义 URL 参数。
>
> 利用数十万个网站的恶意软件行为者对与他们合作的广告技术公司来说并不是匿名的。
>
> “*广告技术公司知道。他们审查他们的出版附属公司并收集 Telegram 帐户和加密货币钱包等信息*。
>
> 像 Los Pollos 这样的公司在合法性的外衣下运营，但对恶意软件分发者和诈骗运营商的身份保持充分了解。
>
> Infoblox 报告不仅剖析了 VexTrio 的机器，还揭露了一个建立在剥削性广告、大规模网站入侵和 DNS 欺骗之上的整个黑社会。虽然像 Los Pollos 这样的个人行为者可能会在审查下关闭运营，但核心网络仍在继续——敏捷、适应性强且非常有效。
>
> 除非商业广告技术公司被追究责任，否则 VexTrio 及其众多克隆产品将持续存在于互联网的阴影中，从毫无戒心的用户的痛苦中获利。

本文翻译自securityonline [原文链接](https://securityonline.info/vextrio-exposed-infoblox-uncovers-massive-malicious-adtech-ecosystem-powering-global-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308492](/post/id/308492)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/vextrio-exposed-infoblox-uncovers-massive-malicious-adtech-ecosystem-powering-global-malware/)

如若转载,请注明出处： <https://securityonline.info/vextrio-exposed-infoblox-uncovers-massive-malicious-adtech-ecosystem-powering-global-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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