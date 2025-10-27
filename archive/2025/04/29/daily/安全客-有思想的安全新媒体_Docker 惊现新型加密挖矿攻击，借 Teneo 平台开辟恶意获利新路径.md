---
title: Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径
url: https://www.anquanke.com/post/id/306959
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:17.562029
---

# Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径

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

# Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径

阅读量**104818**

发布时间 : 2025-04-28 10:39:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全研究人员详细披露了一场恶意软件攻击活动，该活动采用一种此前未被记录的技术，针对 Docker 环境进行加密货币挖掘。

根据 Darktrace 和 Cado Security 的研究，与其他直接部署如 XMRig 等挖矿程序、非法利用计算资源获利的加密劫持活动不同，此次攻击活动发生了新变化。

此次攻击涉及部署一种恶意软件，该软件会连接到一个名为 Teneo 的新兴 Web3 服务平台。Teneo 是一个去中心化物理基础设施网络（DePIN），用户可以通过运行社区节点来获取公共社交媒体数据的收益，获得的奖励被称为 Teneo 积分，这些积分可兑换成 $TENEO 代币。

该节点本质上是一个分布式社交媒体数据采集器，用于从 Facebook、X（原推特）、Reddit 和 TikTok 等平台提取帖子内容。

对 Darktrace 蜜罐收集到的相关数据进行分析后发现，攻击始于一个从 Docker Hub 注册中心拉取 “kazutod/tene:ten” 容器镜像的请求。该镜像于两个月前上传，截至目前已被下载 325 次。

这个容器镜像旨在运行一个经过深度混淆处理的嵌入式 Python 脚本，该脚本需要经过 63 次解包操作才能还原出实际代码，而实际代码的作用是建立与 teneo [.] pro 的连接。

Darktrace 在与《黑客新闻》分享的一份报告中指出：“恶意软件脚本只是连接到 WebSocket 并发送心跳包，以此从 Teneo 获取更多积分，它并不进行任何实际的数据采集操作。从该平台的网站信息来看，大部分奖励都与执行的心跳次数挂钩，这很可能就是这种攻击方式奏效的原因。”

这场攻击活动让人联想到另一起恶意威胁事件，在那起事件中，配置错误的 Docker 实例被 9Hits Viewer 软件感染，该软件通过为特定网站引流来获取积分。

此次入侵手段也与其他诸如代理劫持等带宽共享攻击类似，这些攻击都是通过下载特定软件，利用未使用的网络资源来获取某种经济利益。

Darktrace 表示：“通常情况下，传统的加密劫持攻击依赖于使用 XMRig 直接挖掘加密货币，但由于 XMRig 很容易被检测到，攻击者正在转向其他获取加密货币的方法。这种新方法是否更有利可图还有待观察。”

就在这一消息披露之际，Fortinet FortiGuard Labs 披露了一个名为 RustoBot 的新僵尸网络。该僵尸网络利用 TOTOLINK（CVE-2022 – 26210 和 CVE-2022 – 26187）和 DrayTek（CVE-2024 – 12987）设备的安全漏洞进行传播，目的是发动分布式拒绝服务（DDoS）攻击。研究发现，这些攻击主要针对日本、越南和墨西哥的科技行业。

安全研究员 Vincent Li 表示：“物联网和网络设备通常是防护薄弱的端点，这使它们成为攻击者利用并传播恶意程序的诱人目标。加强端点监测和认证能够显著降低被攻击的风险，并有助于抵御恶意软件攻击活动。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306959](/post/id/306959)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html)

如若转载,请注明出处： <https://thehackernews.com/2025/04/ripples-xrpljs-npm-package-backdoored.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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