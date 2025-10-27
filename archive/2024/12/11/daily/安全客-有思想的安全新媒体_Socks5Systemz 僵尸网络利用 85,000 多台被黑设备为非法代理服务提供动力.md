---
title: Socks5Systemz 僵尸网络利用 85,000 多台被黑设备为非法代理服务提供动力
url: https://www.anquanke.com/post/id/302574
source: 安全客-有思想的安全新媒体
date: 2024-12-11
fetch_date: 2025-10-06T19:36:46.538697
---

# Socks5Systemz 僵尸网络利用 85,000 多台被黑设备为非法代理服务提供动力

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

# Socks5Systemz 僵尸网络利用 85,000 多台被黑设备为非法代理服务提供动力

阅读量**51980**

发布时间 : 2024-12-10 11:20:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/socks5systemz-botnet-powers-illegal.html>

译文仅供参考，具体内容表达以及含义原文为准。

根据 Bitsight 的最新发现，一个名为 Socks5Systemz 的恶意僵尸网络正在为一个名为 PROXY.AM 的代理服务提供支持。

该公司的安全研究团队在上周发布的一份分析报告中说：“代理恶意软件和服务使其他类型的犯罪活动成为可能，为威胁行为者增加了不受控制的匿名层，因此他们可以利用受害者系统链执行各种恶意活动。”

在披露这一消息仅仅几周前，Lumen Technologies 公司的 Black Lotus 实验室团队披露，被另一个名为 Ngioweb 的恶意软件入侵的系统正被滥用为 NSOCKS 的住宅代理服务器。

Socks5Systemz 最初早在 2013 年 3 月就在地下网络犯罪活动中被公布，BitSight 以前曾记录它被部署为网络攻击的一部分，目标是分发 PrivateLoader、SmokeLoader 和 Amadey。

该恶意软件的主要目的是将受损系统变成代理出口节点，然后为其他行为者（通常是那些希望掩盖其攻击来源的网络犯罪分子）做广告。自 2016 年以来，非法代理服务一直存在。

受感染主机数量最多的国家是印度、印度尼西亚、乌克兰、阿尔及利亚、越南、俄罗斯、土耳其、巴西、墨西哥、巴基斯坦、泰国、菲律宾、哥伦比亚、埃及、美国、阿根廷、孟加拉国、摩洛哥和尼日利亚。

据说到 2024 年 1 月，僵尸网络的规模已经猛增到日均约 25 万台机器，但目前的估计是 8.5 万到 10 万台不等。截至发稿时，PROXY.AM 声称它拥有来自 31 个不同国家的 80,888 个代理节点。

“2023 年 12 月，威胁行为者失去了对 Socks5Systemz V1 的控制，不得不使用完全不同的[命令与控制]基础设施从头开始重建僵尸网络–我们称之为 Socks5Systemz V2 僵尸网络，”Bitsight 解释了数量减少的原因。

“由于 Socks5Systemz 是由持续存在于系统中的加载器（如 Privateloader、SmokeLoader 或 Amadey）投放的，因此新的分发活动被用来用新的有效载荷替换旧的感染。”

PROXY.AM （proxy[.]am 和 proxyam[.]one）自称提供 “精英、私人和匿名代理服务器”，价格在 126 美元/月（无限包）和 700 美元/月（VIP 包）之间。

Trend Micro 的一份报告详细描述了威胁行为者正在试图利用 Gafgyt 僵尸网络恶意软件针对配置错误的 Docker 远程 API 服务器实施分布式拒绝服务（DDoS）攻击。

虽然 Gafgyt 有针对易受攻击的物联网设备的记录，但该恶意软件对 SSH 弱密码和 Docker 实例的利用表明其攻击范围正在扩大。

安全研究员苏尼尔-巴蒂（Sunil Bharti）说：“我们注意到，攻击者以公开暴露的配置错误的Docker远程API服务器为目标，通过创建基于合法‘高山’Docker镜像的Docker容器来部署恶意软件。在部署 Gafgyt 恶意软件的同时，攻击者还使用 Gafgyt 僵尸网络恶意软件感染受害者。”

事实证明，对于那些希望部署加密货币矿工、窃取数据并将其纳入僵尸网络进行 DDoS 攻击的威胁行为者来说，云错误配置是一个极具吸引力的攻击面。

莱顿大学（Leiden University）和代尔夫特理工大学（TU Delft）的一组研究人员进行了一项新的实证分析，发现多达 215 个实例暴露了敏感凭据，这些凭据可能会让攻击者在未经授权的情况下访问数据库、云基础设施和第三方 API 等服务。

大部分实例位于美国、印度、澳大利亚、英国、巴西和韩国，涉及信息技术（IT）、零售、金融、教育、媒体和医疗保健等多个行业。

莫达特小组说：“这些发现强调了加强系统管理和警惕监督以防止数据泄露的迫切需要。泄露这些机密的影响可能是巨大的，从完全控制组织的安全基础设施，到冒名顶替和渗透到受保护的云基础设施。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/socks5systemz-botnet-powers-illegal.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302574](/post/id/302574)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/socks5systemz-botnet-powers-illegal.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/socks5systemz-botnet-powers-illegal.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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