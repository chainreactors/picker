---
title: 黑客利用提示注射来篡改Gemini AI的长期记忆
url: https://www.anquanke.com/post/id/304276
source: 安全客-有思想的安全新媒体
date: 2025-02-14
fetch_date: 2025-10-06T20:33:23.238691
---

# 黑客利用提示注射来篡改Gemini AI的长期记忆

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

# 黑客利用提示注射来篡改Gemini AI的长期记忆

阅读量**82221**

发布时间 : 2025-02-13 11:09:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-exploit-gemini-prompt-injection/>

译文仅供参考，具体内容表达以及含义原文为准。

一场针对谷歌 Gemini Advanced 聊天机器人的复杂攻击。此次攻击利用了间接提示注入和延迟工具调用的手段，来破坏人工智能的长期记忆，使攻击者能够植入在不同用户会话中持续存在的虚假信息。

这一漏洞引发了人们对生成式人工智能系统安全性的严重担忧，尤其是那些旨在长期保留用户特定数据的系统。

**提示注入和延迟工具调用**

提示注入是一种网络攻击方式，恶意指令被嵌入到人工智能处理的看似无害的输入内容中，比如文档或电子邮件。

间接提示注入是一种更为隐蔽的变种，当这些指令隐藏在外部内容中时就会发生。人工智能会将这些嵌入的指令解释为合法的用户提示，从而导致意外的操作。

根据约翰・雷贝格（Johann Rehberger）的说法，这次攻击基于一种名为延迟工具调用的技术。攻击不是立即执行恶意指令，而是让人工智能在特定用户操作之后才采取行动，比如用户用 “是” 或 “否” 这样的触发词进行回复时。

这种方法利用了人工智能的上下文感知能力以及它优先考虑所感知到的用户意图的倾向，从而绕过了许多现有的防护措施。

此次攻击的目标是谷歌的高端聊天机器人 Gemini Advanced，它具备长期记忆功能。

1.通过不可信内容进行注入：上传一份恶意文档，由 Gemini 进行总结。文档中隐藏着旨在操纵总结过程的隐蔽指令。

2.基于触发条件的激活：总结内容中包含一个隐藏的请求，该请求将记忆更新与特定的用户回复挂钩。

3.记忆破坏：如果用户在不知情的情况下用触发词进行回复，Gemini 就会执行隐藏指令，将虚假信息（比如编造的个人详细信息）保存到其长期记忆中。

例如，雷贝格展示了这种策略如何能诱使 Gemini “记住” 用户 102 岁、相信地球是平的这一观点，并且生活在一个类似于《黑客帝国》的模拟反乌托邦世界中。这些错误记忆会在不同会话中持续存在，并影响后续的交互。

**长期记忆操纵的影响**

像 Gemini 这样的人工智能系统中的长期记忆旨在通过在不同会话中调用相关细节来提升用户体验。然而，当这一功能被利用时，就会成为一把双刃剑。被破坏的记忆可能会导致：

1.错误信息传播：人工智能可能会根据虚假数据给出不准确的回复。

2.用户操纵：攻击者可以让人工智能在特定情况下按照恶意指令行事。

3.数据窃取：敏感信息可能会通过创造性的窃取渠道被提取，比如将数据嵌入指向攻击者控制服务器的 Markdown 链接中。

尽管谷歌已经承认了这个问题，但它淡化了其影响和危险性。根据他们的评估，这种攻击需要通过网络钓鱼或诱骗用户与恶意内容进行交互来实现，而这种情况被认为不太可能大规模发生。

此外，当新的长期记忆被存储时，Gemini 会通知用户，这为警惕性高的用户提供了检测和删除未经授权条目的机会。

尽管有这些缓解措施，专家们认为，只解决表面症状而不解决根本原因会使系统仍然容易受到攻击。

雷贝格指出，虽然谷歌已经限制了特定功能（比如 Markdown 渲染）以防止数据窃取，但生成式人工智能的根本问题尚未得到解决。

这一事件凸显了在保护大型语言模型（LLM）免受提示注入攻击方面存在的持续挑战。

与传统软件漏洞不同，传统软件漏洞通常可以被彻底修复，而大型语言模型由于依赖自然语言处理，本质上很难区分合法输入和恶意提示。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-exploit-gemini-prompt-injection/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304276](/post/id/304276)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-exploit-gemini-prompt-injection/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-exploit-gemini-prompt-injection/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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