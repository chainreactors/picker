---
title: API NEWS | 凭证泄漏导致API漏洞上升
url: https://www.anquanke.com/post/id/289376
source: 安全客-有思想的安全新媒体
date: 2023-06-30
fetch_date: 2025-10-04T11:44:59.345786
---

# API NEWS | 凭证泄漏导致API漏洞上升

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

# API NEWS | 凭证泄漏导致API漏洞上升

阅读量**255912**

发布时间 : 2023-06-29 15:54:22

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

欢迎大家围观小阑精心整理的API安全最新资讯，在这里你能看到最专业、最前沿的API安全技术和产业资讯，我们提供关于全球API安全资讯与信息安全深度观察。

**本周，我们带来的分享如下：**

1. 一篇关于凭证泄漏导致API漏洞上升的文章
2. 一篇关于讨论API网关安全性的文章
3. 一篇关于PCI DSS 4.0对API安全影响的文章

## 凭证泄漏导致API漏洞上升

一篇来自Security Week的文章，讨论凭证泄漏导致的API漏洞不断增长。最近的一项调查发现，超过一半的美国专业人士曾遭受过API漏洞，但77％人认为他们的组织有效地管理了API令牌。这听起来有点矛盾，因为很多专业人士对他们的凭证管理很有信心，但还是会发生凭证相关的API漏洞情况。

研究结果表明，这种明显的矛盾背后有三个主要原因：

1. 缺乏对现有API组合的可视性；
2. 使用的API数量太多难以跟踪；
3. 低估了管理API凭证所需的时间和精力。

这项调查还衡量了凭证管理的成本，并发现大多数受访者每周花费超过15小时来管理凭证。这一数字可能并不完全准确，但可以看出凭证管理成本的不断上升。问题将只会加剧，因为API扩散不断增加，构建环境变得更加分散，需要更多的凭证分发和管理。面对这些挑战，组织只能选择忽略问题或投入更多的金钱来解决凭证管理所带来的问题。

![]()

Corsha公司提出可以缓解这种情况的解决方案，就是为API提供多因素认证（MFA）。

这种解决方案有三个优点：

1. 可以进行微段隔离，防止网络中的横向传播；
2. 降低MFA疲劳的风险；
3. 消除凭证轮换问题，因为盗窃或泄漏的凭证无法在满足MFA要求之前使用。

**小阑认为：**

随着API数量的不断增加以及对API安全性的增强需求，MFA将成为一个不可或缺的安全措施。同时，还需要考虑到人工智能和自动化技术等方面的发展，以便找到更好的方法来管理API凭证，并确保API的安全。

另外，MFA疲劳攻击是一种严重的安全威胁，可以通过使用自动化工具对受保护的帐户进行多次MFA尝试来实施。攻击者可能会窃取敏感信息或执行其他不良行为，从而对组织的安全和业务流程造成影响。为了防范MFA疲劳攻击，组织可以采用多种策略，例如使用MFA应用程序、设置帐户锁定策略、使用机器学习技术、增加MFA代码的复杂度以及加强身份验证。通过采取这些措施，组织可以更好地保护其用户和敏感数据，并提高安全性。

## 你的API网关有多安全？

这是一篇来自The New Stack的文章，深入讨论了API网关安全的重要性。作者认为，由于API网关是基础设施中如此关键的一部分，负责部署网关的人必须充分考虑网关本身的安全性。由于它们与组织基础设施的紧密耦合，API网关很少被更改，这使得选择网关时安全性成为首要考虑因素。

![]()

文章提出有四个因素对API网关整体安全性产生影响：

1. API网关一般是在开源实现和私有源代码之上构建的。因此，企业需要使用现代软件材料清单（SBOM）技术来管理整个软件堆栈中的漏洞，以便更好地了解API网关的风险。
2. 除此之外，还需要考虑API网关如何与其他安全防护措施（如Web应用程序防火墙、全局防火墙和负载均衡器、监控平台）集成。这种紧密集成对于保证应用程序的高性能非常重要，并且需要尽量减少在部署混合多云环境时对操作团队的影响。
3. 大型企业应该考虑在整个组织中执行相同的策略可能会遇到的问题，特别是当技术堆栈非常异构的时候。这会导致不同反向代理以不同方式实现相同的策略，从而导致微妙但重要的差异。这种时候的解决方法是，确保在购买前进行彻底的概念验证（PoC）。
4. 最后需要特别关注API网关的速度（延迟），这对长期使用和其安全性至关重要。如果选择的API网关性能不佳，那么API团队最终会寻求调整策略，甚至在极端情况下完全绕过API网关。因此，API的性能通常是API网关成功的关键因素之一。

**小阑解读：**

API网关的访问控制通常以身份验证机制开始，以便确认调用的来源。目前，最受欢迎的网关验证协议是OAuth，它充当访问基于Web的资源的代理而不向服务公开密码，基于密钥的身份验证在用于企业时，也有丢失数据的案例，还不能百分之百保证密钥完全保密。

**API网关的优势：**

1. 在统一的位置管理和实施；
2. 将大部分问题外部化，因此简化了API源代码；
3. 提供API的管理中心和视图，更方便采用一致的策略；

**API网关的缺点：**

1. 容易出现单点故障或瓶颈；
2. 由于所有API规则都在一个位置，因此存在复杂性风险；
3. 被锁定的风险，日后系统迁移并不简单。

安全性是公司首要考虑基础架构中投入的头号关注点。但是，它也是现有API开发者最容易忽视的领域。因为很多公司正在自己构建API作为产品，以部署Web，移动客户端，物联网和其它应用程序，在整个过程中的每一步都须正确保护，API网关是最有效的解决方案之一。

## PCI DSS 4.0对API安全的影响

PCI DSS标准是指支付卡行业数据安全标准（Payment Card Industry Data Security Standard），是由VISA、MasterCard、Discover、JCB和American Express等信用卡品牌共同制定的数据安全标准，旨在确保有关交易的处理和存储数据安全。任何处理信用卡支付的机构都必须遵守该标准。PCI DSS标准包括一些规则和要求，以确保对客户付款信息的保护，防止数据泄漏和欺诈行为。

![]()

最新版本4.0为软件的安全开发和部署提供了具体条款，文章探讨这些条款对API开发人员可能产生的影响。以下是与软件开发和部署相关的关键条款：

1. 6.2 – Bespoke and custom software are developed securely.

这是采用安全SDLC或采用“左移”开发的指导。对于API开发，开发人员必须尽早了解安全需求，并在整个生命周期中使用安全开发方法。

1. 6.2.3 – Bespoke and custom software is reviewed prior to being released into production or to customers, to identify and correct potential coding vulnerabilities.

该条款指导开发人员使用代码审核（包括OAS定义和API代码）来确保尽可能大程度上减少编码漏洞。这些审核可以在开发生命周期的各个阶段自动进行。

1. 6.2.4 – Software engineering techniques or other methods are defined and in use by software development personnel to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software.

在API上下文中，该控件指示使用高级测试方法来识别针对API的各种软件攻击。建议的最佳实践是使用特定的API测试来检测众所周知的漏洞类型（如损坏的对象级别授权和损坏的身份验证），主要是使用自动化测试（专用的API安全扫描工具）或通过定制渗透测试。

1. 6.4 Public-facing web applications are protected against attacks.

该标准规定应保护面向公众的API免受攻击，通常通过API网关或专用API防火墙。

**小阑认为：**

API安全的重要性不言自明，它涉及到数据和信息的保护、合规性以及竞争优势等多个方面，是每个企业在数字化转型过程中必须认真对待和加强的重要环节。随着数字化与智能化进程的加速推进，API成为不同系统、应用和数据的粘合剂，承担着越来越多的业务功能。而这些业务功能往往包括金融交易数据、个人信息等涉及个人隐私和商业机密的数据。因此，确保API的安全性不仅是企业信息安全管理的重要一环，更是整个数字时代信息安全和隐私保护的基石。

*感谢*[*http://*](https://link.zhihu.com/?target=http%3A//APIsecurity.io)[*APIsecurity.io*](https://link.zhihu.com/?target=http%3A//APIsecurity.io)*提供相关内容*

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/289376](/post/id/289376)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [API](/tag/API)

**+1**10赞

收藏

![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)星阑科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t010136e53e1b35516c.png)

[![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)](/member.html?memberId=147620)

[星阑科技](/member.html?memberId=147620)

星阑科技

* 文章
* **119**

* 粉丝
* **46**

### TA的文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [解密与探究：理解WebSocket协议与报文格式](/post/id/290500)

  2023-08-30 14:36:15
* ##### [创新护航：萤火助力守护数据跨境安全](/post/id/290512)

  2023-08-29 16:10:15

### 相关文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [星阑科技受邀专精特新创新策源会，共同探讨网安新生态](/post/id/290481)

  2023-08-29 16:09:31
* ##### [锐意拼搏 开拓奋进 | 星阑科技受邀ISC，共讨数智化生产力变革](/post/id/290475)

  2023-08-22 12:47:46
* ##### [API NEWS | API安全需要重置](/post/id/290291)

  2023-08-15 14:45:10
* ##### [医疗案例分享 | 数据安全流转解决方案](/post/id/290399)

  2023-08-15 14:43:07

### 热门推荐

文章目录

* [凭证泄漏导致API漏洞上升](#h2-0)
* [你的API网关有多安全？](#h2-1)
* [PCI DSS 4.0对API安全的影响](#h2-2)

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