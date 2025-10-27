---
title: API安全性：不能只是下一代WAF上的附加组件
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121926&idx=1&sn=461ab198caedebb87fb2b7f76182887e&chksm=bd1459d58a63d0c316525232d11f72252232dd1e542c1a5404ddbcea951cc77641fa132a5938&scene=58&subscene=0#rd
source: 安全牛
date: 2023-02-15
fetch_date: 2025-10-04T06:37:35.602982
---

# API安全性：不能只是下一代WAF上的附加组件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDzb9p6R504wzYfz2O9DLibJxewj0LaSJjR7Jcl7ibXQAxqE6THe863Rvt78vbexENn2vicVBJ0b5icWw/0?wx_fmt=jpeg)

# API安全性：不能只是下一代WAF上的附加组件

安全牛

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkDzb9p6R504wzYfz2O9DLibJBkhicLvDZreEf17vbKzicHIDB2Q432X47lAxFrBibEyiakY8eF2DMhmvjw/640?wx_fmt=jpeg)

WAAP（Web应用和API保护平台）是带着“下一代WAF”光环出道的，旨在超越传统WAF基于签名的攻击防护方式，并为用户提供额外的API保护功能。从本质上看，WAAP是一种更高级的WAF方案。那么，如果企业使用了WAAP方案，是否还需要部署专用的API安全性产品？在WAAP方案中所融合的API防护能力，可以实现企业所需要的整体API安全防护策略吗？

目前，WAAP方案所覆盖的API安全能力主要包括了API文档支持、模式分析和验证以及API资产发现，这对于保护API应用免受一系列预先设置的攻击（包括SQL注入、代码执行和DDoS攻击）至关重要。但是需要指出的是，目前的WAAP方案只能解决API安全威胁中的一部分，因为每个API应用都有自己的底层业务逻辑和功能。为了防止API被滥用，企业需要充分了解其应用流量的变化，而这并不是WAF或其进化产物WAAP所能够实现的。

因此，随着现代企业组织API应用的激增，基于WAF或WAAP的防御措施不足以应对如今更复杂和多样化的API攻击威胁。WAAP是在传统WAF方案上的发展演进，添加一些特定的API保护功能。但如果企业组织想要对所有的API安全威胁都有可见性，那仅靠WAAP方案的API防护能力是远远不够的。

API攻击的方式与传统的应用程序攻击有很大不同。随着企业组织数字化转型的深入发展，其业务系统上的API应用数量也在不断激增，改变和扩大了组织的攻击面。由于每个API应用都有自己独特的业务逻辑，所以每次API攻击都是唯一性的，攻击者会做大量的探测来发现可以利用的API漏洞。这种侦察活动可能需要几天、几周甚至几个月的执行时间。如果不借助适当的上下文信息检测，攻击者可以很轻松地在整个攻击生命周期中隐藏或伪装他们的攻击行为。

就API安全防护而言，组织需要深入和广泛的上下文分析来发现潜在的威胁，仅仅依靠WAAP来提供运行时保护会使API应用存在几个关键的安全隐患。具体来说，WAAP通常缺乏上下文和智能驱动的能力，因此难以实现以下防护能力：

**01**

**WAAP无法监控较长时间的API攻击**

API攻击的生命周期一般很长，因为攻击者需要不断地探测API，以发现可被利用的漏洞。由于WAAP方案缺乏对长期业务活动的可见性，因此它们无法发现恶意行为者为攻击API所进行的持续性侦察活动。为了保护API及其所传输的敏感数据，企业不能只是在攻击危害产生后才开始被动应对。即使没有API攻击的所有细节，但企业通过分析适当的API应用上下文，也应该更早地识别出攻击。

**02**

**WAAP无法识别API的行为异常**

除了随时间建立的可见性，API安全解决方案还必须能够精确识别与API攻击活动相关的异常行为，包括扩展侦察活动、API滥用以及业务逻辑操纵攻击。许多API应用都在假设存在业务逻辑缺陷和滥用可能性的情况下运行。这是因为企业知道，在开发和测试周期中识别和清除所有的业务逻辑缺陷和漏洞是非常困难的。因此，准确识别行为异常和用户意图的能力是API安全策略中最关键的部分。API攻击是基于一系列活动的行为攻击，高级API安全解决方案可以判断生态系统中什么代表“正常”行为，什么代表可能潜在威胁的“异常”行为。而WAAP方案更善于寻找已知的攻击模式，由于缺乏行为上下文，WAAP无法可靠地区分“普通”和“异常”的API行为，从而触发危险信号。

**03**

**WAAP缺乏主动学习能力**

基于人工智能的安全解决方案，最大特点就是可以从各种遇到的安全问题中主动“学习”。在安全系统中使用这种学习能力可以更准确地检测并驱动更有效的响应措施。利用云级（cloud-scale）大数据的力量，在一个客户的环境中学习不仅可以丰富算法，反过来也可以使其他客户受益，因为学习来带的能力提升是以指数级方式增长的。但很可惜，目前的WAAP方案仍然缺乏这种主动学习的能力。

**04**

**WAAP不能辨别用户的意图**

云级、成熟的AI和ML模型可以分析大量的数据和流量，在大量的结构和行为属性中搜索签名和模式。但这并非WAAP所能做的事情。由于API经常被滥用，即便人们完全按照设计使用它们。如果攻击者出于恶意目的窃取并使用合法访问凭证针对特权API，WAAP通常无法发现攻击者未经授权的访问及其伪装攻击。如果没有用户行为的上下文，这些访问行为对于WAAP的检测机制来说都是合法的。因为WAAP不能在应用程序堆栈的不同应用层之间提供完整可见性，所以它们不能信息关联发现潜在的威胁。

**结语**

不可否认，WAAP比WAF更先进，也可以在企业完整的API安全防护体系中发挥着重要作用，但它并不能全面解决API安全问题。WAAP方案很难具备深度和广度的可见性，以及智能并随时间变化的上下文分析能力，来防御不断演变的API攻击。仅仅依靠WAAP来保护API安全将会留下大量的安全盲点，将组织置于危险之中。为了全面保护企业的API生态系统，除了应用WAAP之外，组织还需要适当的API安全运行时保护措施。

**参考链接：**

**https://salt.security/blog/critical-api-security-gaps-in-waaps?**

相关阅读

[7种最危险的API安全风险与防护建议](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651121097&idx=1&sn=774cf4d7ab629547798689d892e2b19b&chksm=bd14551a8a63dc0c2a8082ac579da76967a71526cfecf337101935ab5537a6a63aaab3275a3d&scene=21#wechat_redirect)

[API应用数量已近2亿，如何应对API蔓延的安全风险与挑战？](http://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651119607&idx=1&sn=ac6b26bb8668cb2ea394e7f47f67982d&chksm=bd146f248a63e632568673a701febf3b49fc4b57d9d4870148d81745cc268d4371ce4000f27c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAZYNibk7aDDd0hAkQGzOfLPfjXUPaypbuDrr5exabqWXmSOeZVUZtP6zqw9YGWib9xNQdvx1iaCicTUA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过