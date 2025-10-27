---
title: API应用数量已近2亿，如何应对API蔓延的安全风险与挑战？
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247532448&idx=3&sn=0367c65f09cc555f09c18de87328a3ef&chksm=c1e9f3f1f69e7ae7d2d91b8cd5fbb8967e602dc48d69e3c2144dd8cef9de82549e13ae159359&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-11-05
fetch_date: 2025-10-03T21:45:59.141931
---

# API应用数量已近2亿，如何应对API蔓延的安全风险与挑战？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogv8ibqmDUicVic8NtZicIT5M47Yqn1umM6SEPpSNH9PGXJw1JEHFRITumqicOicgqJXZKG9I1hSqpicknNRQ/0?wx_fmt=jpeg)

# API应用数量已近2亿，如何应对API蔓延的安全风险与挑战？

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogv8ibqmDUicVic8NtZicIT5M47YtU1zRR718fdicIolc7ibb5FE1l1VRhbK5jPEciazJFiaaTUTx1HGJfJfLQ/640?wx_fmt=jpeg)

万圣节并非僵尸、影子和幽灵出没的唯一时刻。其实，这些令人厌恶的问题正以API的形式隐藏在企业的数字化基础设施中，不断扩展组织的网络攻击面。而产生这些可怕的僵尸API、影子API和幽灵API的主要原因就是API蔓延（API Sprawl），这已经成为现代企业数字化转型发展的重大挑战。

**API蔓延的原因**

当组织缺乏适当的API可见性、治理机制和生命周期策略时，僵尸、影子和幽灵等可怕的API威胁就会出现，并给企业业务开展造成损害。

**挥之不去的“僵尸”API（Zombie API）**

僵尸API是指一些暴露的API或已经过时、被抛弃的API端点。当一个组织没有对迁移、弃用和淘汰的旧API进行适当控制时，这些API可能会永远存在，并由此形成“僵尸”API。因为它们基本上被遗忘和忽略了，没有任何功能或安全方面的持续补丁、维护或更新，因此僵尸API会带来严重的安全风险。事实上，据Salt Security State发布的《API安全研究报告》显示，僵尸API是组织需要关注的首要API安全问题。

**藏匿风险的“影子”API（Shadow API）**

影子API是创建和部署在安全监控范围外的API端点，这些令人厌恶的API有时是从影子IT中产生的。开发人员通常希望更快地部署API或端点这也造成了影子API大量出现。影子API会带来的安全风险包括：

* 没有适当的身份验证和授权；
* 不正确地暴露敏感数据；
* 没有遵循最佳实践，更容易受到攻击。

**无所不在的“幽灵”API（Ghost API）**

幽灵API的概念是指第三方开发（或代写）的API，并在组织生产环境中公开使用。幽灵API可以暴露在任何地方：打包的应用程序（商业的和开源的）、基于SaaS的服务、基于本地和云的基础设施组件（例如虚拟设备上的admin API）等等。许多组织有意地在其扩展基础设施中依赖第三方开发的API，作为其功能数字供应链和日常基础设施管理的一部分。然而，有时第三方API会在无意中暴露。此外，由于第三方开发的API并非在完善的devops周期中发布，因此它们通常没有得到适当的治理、测试、监视和维护，这也为应用程序带来了大量的安全风险。

根据最新研究数据统计，目前公共和私人API的应用数量已接近2亿，而到2031年，这个数字可能会超过10亿。鉴于这种快速的应用增长趋势，API蔓延问题在各种组织中已经表现得非常广泛，其主要原因包括：

* 缺乏关于API的全球标准是API蔓延如此普遍的原因之一。标准缺失意味着需要创建多个独立的API来服务于一个功能。如果没有将API配置为协同工作，就会导致兼容性问题；
* 大多数企业都在向微服务体系结构发展，而API通常是微服务体系结构和容器化的重要组成部分，这也导致它们的受欢迎程度有所上升；
* 持续的软件开发是API蔓延的另一个常见原因。每个新版本都会有新的API，或者需要现有API版本升级；
* 不同部门之间缺乏沟通也是API蔓延的一个常见原因，因为每个部门可能会开发自己的API；
* 边缘计算或“一切即服务”（EaaS）等新技术的兴起导致更多的API被创建应用。

**API蔓延的风险**

企业如今依赖的许多服务都依赖API。如果组织不能将适当的API治理部署到位，整个数字化业务系统就会有崩溃的可能。以下是API蔓延带来的主要风险：

**1. 浪费时间和资源**

在当今高度饱和的商业世界中，保持竞争力对企业来说可谓前所未有的重要。因此，领导者必须考虑每一个减少开支和削减成本的机会。开发、实现和部署不需要的软件，无疑是在烧钱。通过减少API蔓延来节省资金，可以让企业将这些资源投资到更有价值的追求上，从而帮助实现业务增长。

**2. 表现不佳或使产品受损**

未受管理或管理不当的API容易导致服务中断。通常，API基础设施就像纸牌搭成的房子，某一块的损坏，都可能让整座房子倒塌。考虑到用户对系统正常运行的期望和需求，这就是为什么需要在API失控之前阻止它蔓延的另一个原因。

**3. 引发安全风险**

未经管理和过时的API是网络中常见的安全风险来源。了解所有API的位置、它们在做什么，以及什么在与什么交互，这对于保障系统安全非常重要。随着API的数量和应用程序的复杂性不断增长，跟踪API位置将变得愈发困难。在组织内外发现它们可能很困难，并且会影响到端到端连通性。此外，API还容易出现欺诈和恶意行为。外部API访问必须持续验证才能获得信任，但如果内部API密钥被泄露，攻击者就能够轻松访问关键的基础设施和数据。

**API蔓延的防护措施**

API蔓延会加剧企业在业务开展和安全运营方面的挑战，需要尽早采取积极的措施应对API蔓延。

**1. 制定API治理计划**

指定一个集中式API管理计划在防止API失控方面有很大帮助。它还使查找、连接和保护API变得更加容易，这也有助于避免API蔓延。拥有集中式API治理策略可以帮助组织概念化诸如API架构、层次结构等内容。实现企业范围的API策略（如速率限制或授权）也更容易。

**2. 集中统一管理API**

跟踪API本就是件棘手的事情，当API蔓延失控时，它会变得更加复杂。拥有一个集中式API发现和管理解决方案可以实现所有API的集中统一管理，这样每个人都可以快速找到并使用它们，此举也有助于避免影子API或有风险的僵尸端点。

**3. 跟踪API指标**

API架构可能很快就变得非常复杂。根据规模的不同，组织可能需要一个完整的开发人员团队来跟踪每个API的位置以及它们的交互方式。通过监测API指标，企业可以看到所有API在整个组织中的执行情况。没有这一点，想要优化或保护网络应用系统将非常困难。

**4. 在整个组织中规范API安全性**

目前，90%使用了API的组织都经历了某种不同程度的安全事件。可以说，每创建一个新的API，就可能会为网络犯罪分子创造更多的可利用空间。这也可能导致API被误用和滥用，从而导致API进一步蔓延。

**5. 寻求通用的解决方案**

API的采用只会日益增加。因此，最好在问题失控之前就解决API蔓延问题。创建一个通用的解决方案，确保所有API都是可发现的，并且能够彼此通信，这将有助于阻止API的蔓延，并缓解许多其他问题。

**6. 遵循API规范**

遵循API规范（如OpenAPI）并不复杂，但却可以有效减少API的蔓延，因为它使观察发现API及其所有组件变得更加容易。这大大降低了API在混乱中丢失或被遗忘的可能性。此外，遵循API规范可以使API应用生成自动化文档，从而进一步降低API蔓延的风险。

**参考链接：**

https://salt.security/blog/are-you-haunted-by-zombie-shadow-and-ghost-apis

https://nordicapis.com/7-methods-to-prevent-api-sprawl-within-your-organization/

原文来源：安全牛

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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