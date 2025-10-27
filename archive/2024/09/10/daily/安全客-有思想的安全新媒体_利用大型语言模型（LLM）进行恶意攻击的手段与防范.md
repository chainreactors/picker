---
title: 利用大型语言模型（LLM）进行恶意攻击的手段与防范
url: https://www.anquanke.com/post/id/299912
source: 安全客-有思想的安全新媒体
date: 2024-09-10
fetch_date: 2025-10-06T18:23:56.184779
---

# 利用大型语言模型（LLM）进行恶意攻击的手段与防范

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

# 利用大型语言模型（LLM）进行恶意攻击的手段与防范

阅读量**107867**

发布时间 : 2024-09-09 16:01:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Peter Garraghan，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/09/09/ai-cybersecurity-needs/>

译文仅供参考，具体内容表达以及含义原文为准。

网络犯罪分子开始利用大型语言模型 （LLM） 为他们提供的新恶意选项。LLM 可以上传包含隐藏指令的文档，这些指令由连接的系统组件执行。这对网络犯罪分子来说是一个福音，因此对使用它们的企业来说也是一个实质性的风险。

LLM 可以通过多种方式进行欺骗。网络犯罪分子可以输入恶意提示，诱骗 LLM 覆盖其护栏（即生成有害输出），这一过程称为越狱。它们还可以影响模型的功能、使数据中毒或指示 LLM 根据攻击者的请求执行恶意指令。恶意提示还可能导致模型和数据提取，并且模型本身可能包含启用后门程序的功能。所有这些攻击都会使敏感信息面临风险。

过去两年中发生的针对 AI 系统的攻击使用了某种形式的对抗性机器学习 （ML）。这些攻击的示例包括中国的全面税务欺诈，攻击者通过创建虚假的空壳公司并向税务系统认可的客户向受害者发送发票，欺诈性地获得了 7700 万美元，以及加利福尼亚州的失业申请欺诈，攻击者通过收集真实身份来制作假驾驶执照，提取了 340 万美元的伪造失业救济金。 从而利用系统身份验证过程中的缺陷。

要防范此类攻击，首先要了解安全漏洞及其可能产生的网络危害的频率、来源和程度。从那里开始，网络安全解决方案分为四个关键类别：设计、开发、部署和运营。

### 设计

通过在训练和部署 AI 之前更改 AI 的技术设计和开发，公司可以在开始之前减少其安全漏洞。例如，即使选择正确的模型架构也会产生相当大的影响，每个 AI 模型都表现出特定的亲和力，以缓解特定类型的提示注入或越狱。为给定用例确定正确的 AI 模型对其成功非常重要，安全性同样如此。

### 发展

开发具有嵌入式网络安全的 AI 系统从如何准备和处理训练数据开始。必须清理训练数据，并且必须使用过滤器来限制摄取的训练数据。输入恢复通过添加额外的随机性层来混淆对手评估 AI 模型的输入-输出关系的能力。

公司应该创建约束条件，通过 Reject-On-Negative-Impact 训练来减少学习模型的潜在扭曲。之后，应持续对 AI 模型进行定期安全测试和漏洞扫描。

在部署期间，开发人员应通过加密检查来验证修改和可能的篡改。可以通过严格限制软件加载非结构化代码的能力来防止库加载滥用。敏感数据的加密是没有商量余地的。

### 部署

组织应保持良好的安全卫生习惯。他们的 AI 生命周期应该有据可查，并应提供与组织的 AI 风险治理相一致的 AI 计划的全面清单。必须收集外部利益相关者的反馈并将其整合到系统设计中。员工培训、红队、对 AI 威胁形势的持续研究以及强大的供应链安全性必须成为常见做法。

### 操作

最重要的是，AI 网络安全需要工具和方法的组合。这是贯穿整个运营和维护的持续过程。这可能包括限制用户可以执行的查询总数。

模型混淆有效地改变了模型属性，使其偏离了提取网络攻击预期的典型操作。内容安全系统可以清理 LLM 的输入和输出，对抗性输入检测可以在将查询流量发送到模型进行推理之前对其进行筛选。

防止新技术面临的网络安全威胁显现并非易事。这是一个需要同时使用多种工具和方法的过程。这些 AI 安全工具和策略确实存在，并且每天都在变得越来越成熟，缺少的一个关键组成部分是整个行业都在推动将其使用作为优先事项。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/09/09/ai-cybersecurity-needs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299912](/post/id/299912)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/09/09/ai-cybersecurity-needs/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/09/09/ai-cybersecurity-needs/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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