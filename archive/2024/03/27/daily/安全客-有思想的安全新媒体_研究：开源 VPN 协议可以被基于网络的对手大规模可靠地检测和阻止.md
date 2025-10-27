---
title: 研究：开源 VPN 协议可以被基于网络的对手大规模可靠地检测和阻止
url: https://www.anquanke.com/post/id/294372
source: 安全客-有思想的安全新媒体
date: 2024-03-27
fetch_date: 2025-10-04T12:07:47.481991
---

# 研究：开源 VPN 协议可以被基于网络的对手大规模可靠地检测和阻止

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

# 研究：开源 VPN 协议可以被基于网络的对手大规模可靠地检测和阻止

阅读量**140270**

发布时间 : 2024-03-26 11:40:55

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://cybernews.com/security/alarming-researchers-fingerprint-vpn-providers-traffic/>

译文仅供参考，具体内容表达以及含义原文为准。

研究发现，OpenVPN 是最广泛使用的用于安全和私密连接的开源 VPN 协议，“可以被基于网络的对手大规模可靠地检测和阻止”。这影响了十大 VPN 提供商中的八家。

如果政府或 ISP 想要阻止通过 OpenVPN 路由的流量，他们可以轻松做到 – 即使使用广泛应用的混淆技术。

来自密歇根大学和其他机构的研究人员演示了一个两阶段系统，该系统执行被动过滤，然后主动探测指纹 OpenVPN 流量。

“我们与一家中型 ISP 合作评估了我们方法的实用性，我们能够识别大多数普通和混淆的 OpenVPN 流，误报率可以忽略不计，这证明我们描述的技术即使对于对手来说也是实用的避免附带损害，”该文件写道。

世界各地的某些政府，包括中国和俄罗斯，正在寻求限制 VPN 访问，以维持控制并防止公民绕过监视和审查措施。

研究表明，使用 OpenVPN（商业 VPN 服务最流行的协议）可以准确地识别连接指纹。

研究人员表示：“我们根据字节模式、数据包大小和服务器响应等协议特征来识别三个指纹。”

在与拥有百万用户的区域 ISP 测试他们的方法时，他们能够识别超过 85% 的 OpenVPN 流量，误报率可以忽略不计。他们的框架还成功识别了 41 个“混淆”VPN 配置中的 34 个连接。

![检测 VPN 的方案]()检测 VPN 的方案

研究人员使用深度数据包检测 (DPI) 技术来识别字节模式、数据包大小以及服务器对指纹 OpenVPN 流量的响应等特征。

作者警告敏感用户，例如记者或政治活动家，不要指望 VPN 的使用会被观察不到。研究人员还敦促 VPN 提供商采用更有原则、更稳健的混淆方法。

令人担忧的是，在 top10vpn.com 排名的“十大”VPN 提供商中，有八家提供某种类型的混淆服务，这表明无法检测是提供商对其客户的威胁模型之内的内容。然而，由于加密（操作码）不足或数据包长度（ACK）混淆不足，所有这些流都被标记为可疑流，”该论文写道。考虑到这些混淆的 VPN 服务通常声称“无法检测”或声称混淆“让您摆脱麻烦”，这一结果令人震惊，因为使用这些服务的用户可能会对隐私和“不可观察性”产生错误的感觉。

该论文还指出，排名前五的 VPN 提供商中有四家使用基于 XOR 的混淆技术，这种方法很容易被识别。

研究人员还提出了几种防止 VPN 流量受到 ISP 或政府限制或阻止的策略。短期内，他们建议将混淆服务器与网络地址空间中的 OpenVPN 实例分开，将混淆服务从静态填充切换为随机填充等。

“从长远来看，我们担心审查机构和翻墙工具（例如防火墙和 Tor）之间的猫捉老鼠游戏也会在 VPN 生态系统中发生，开发者和提供商将不得不调整其混淆策略以适应实际情况。不断演变的对手，”该论文写道。

“我们敦促商业 VPN 提供商采用更标准化的混淆解决方案，例如可插拔传输，并对其混淆服务所使用的技术更加透明。”

本文翻译自 [原文链接](https://cybernews.com/security/alarming-researchers-fingerprint-vpn-providers-traffic/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/294372](/post/id/294372)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://cybernews.com/security/alarming-researchers-fingerprint-vpn-providers-traffic/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

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