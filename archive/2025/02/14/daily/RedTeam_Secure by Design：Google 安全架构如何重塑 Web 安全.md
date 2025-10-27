---
title: Secure by Design：Google 安全架构如何重塑 Web 安全
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484083&idx=1&sn=7067593adcad3d8319128185ec0693ec&chksm=c006ca43f77143559e67827a760b824d8a8b59d2ad2c9f329801869b09dc7e3f215015e4cf29&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-14
fetch_date: 2025-10-06T20:39:35.642013
---

# Secure by Design：Google 安全架构如何重塑 Web 安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk4e3icibiaFicz9xSwuS3SWiagEu82b3yAp0PIagmeniaLZPej1nABKBMzA6VWibBgB9aVQG9ZlMVInWnu1g/0?wx_fmt=jpeg)

# Secure by Design：Google 安全架构如何重塑 Web 安全

原创

tonghuaroot

RedTeam

## 概述

**Google 每年平均收到的 XSS 漏洞报告不到一个，不是每个应用程序，而是所有应用程序加起来！**

Google 通过构建高可信 Web 安全框架，将 XSS 漏洞发生率降至年均个位数，实现安全能力与开发效率的范式级突破，验证了 "Secure by Design" 架构在企业级场景的可行性。

## 前言

Google 维护着世界上最大的 Web 应用生态。根据统计方式的不同，Google 拥有数百个或数千个不同的 Web 服务，其中大多数从安全角度来看都是敏感的。在过去十年中，Google 的 Web 应用生态系统规模显著增长，人们可能会认为这会导致影响Google 服务的安全漏洞数量出现类似的增长。但实际上，Google 设法将应用程序中的关键 Web漏洞（如 XSS）的数量减少了一个数量级以上，同时还支持这个不断增长的生态系统。

![image](https://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk4e3icibiaFicz9xSwuS3SWiagEufrd1C4DicwrcEEabyZQhDic5NIR54h5qKXj3uuuPYygK8XJR9RfItARA/640?wx_fmt=png&from=appmsg)

image

该图显示了随着时间的推移，通过Google 的漏洞奖励计划向Google 报告的XSS漏洞数量。尽管 Web 应用程序数量增加且奖金金额增加，但报告的漏洞数量一直呈下降趋势。值得注意的是，对于完全采用推荐的高保证 Web 框架的数百个服务，XSS漏洞的数量甚至更低（在整个Google 每年约1个）。

这一显著的安全改进可以直接归因于Google 对"默认安全设计"原则的承诺，Google 在最近的这篇白皮书中对此进行了阐述。

这篇博文旨在提供一个详细的蓝图，说明Google 如何创建和部署一个高保证的 Web 安全框架，几乎完全消除了可利用的 Web 漏洞。

## Web 安全面临的挑战

Web 最初被设想为一个链接和共享信息的系统，它在这些目标上表现出色。随着时间的推移，Web 的范围不断扩大，现在它已成为用户与许多应用程序交互的标准渠道，其中一些应用程序管理着用户最敏感的个人数据。这使得 Web 安全至关重要，但它需要建立在一个最初并非为此类应用程序设计的平台之上，Google 称之为"Web 平台"。这造成了一种情况，即安全性基本上是 Web 平台的事后考虑，并导致了 Google 所说的 Web 安全的"3个原罪"：

* （缺乏）加密：很容易在没有传输中加密的情况下构建应用程序
* 注入：Web 的核心构建块（HTML、JS、URL）允许混合代码和数据
* （缺乏）隔离：默认允许不同应用程序之间的跨源交互

这些因素中的每一个都使 Web 平台易于采用，并有助于 Web 的爆炸式增长。同时，这些因素也导致了一系列关键的漏洞类型：

* （缺乏）加密：很容易在没有传输中加密的情况下构建应用程序 → 默认情况下，Web 是未加密的，数据在网络上是可见的。未加密的数据允许 MITM 攻击者以各种恶意方式拦截和修改 Web 应用程序。
* 注入：Web的 核心构建块（HTML、JS、URL）允许轻松混合代码和数据 → 混合代码和数据使得数据（例如相册或博客的标题）可能被误解为代码，导致 XSS 漏洞等问题。
* （缺乏）隔离：默认允许跨源交互 → 不同应用程序之间的跨源交互允许恶意网站与敏感应用程序交互，并导致 XSRF、点击劫持和几种类型的 XS-Leaks 等问题。

值得注意的是，几乎所有的Web漏洞都可以与这些风险之一联系起来。这就是为什么 Google 采取以平台为中心的安全方法，Google 与Chrome、W3C和 其他 Web 浏览器供应商密切合作，以改进 Web 平台，目标是尽可能多地在 Web 平台中修复这些风险。但是，在无法默认做到这一点的情况下，Google 需要确保 Google 的 Web 应用程序仍然能够全面防御此类漏洞。这就是Google 构建高保证 Web 框架蓝图的用武之地。

关于 Web 安全的一个快速说明：Google 在这里关注 Web 安全漏洞，是因为几乎所有Google 服务都以 Web 应用的形式公开，其中客户端漏洞（如 XSS）可能完全危及用户的数据。因此，虽然 XSS可能看起来没有直接针对 Web 服务器执行的攻击（如 RCE 或 SQL 注入）那么严重，但对Google 来说，XSS 漏洞是极其关键的，Google 会不遗余力地防范。同样值得注意的是，类似的推理是为什么MITRE 目前将 XSS 列为整个行业的头号软件安全漏洞。

## 高保证 Web 框架的要素

根据Google 的经验，有三个关键组件共同构成了高保证 Web 框架：

### #1：安全编码

"安全编码"是Google 用来确保开发人员能够以安全设计的方式编写代码的术语，而无需考虑安全性。安全编码的根本目标是确保安全对开发人员来说是简单和自动的。

这是通过确保默认行为是安全的，并且存在防止安全漏洞回归的门禁来实现的。Google 的目标是确保如果代码成功编译和运行，它就是安全的。虽然这看起来很简单，但 Google 了解到，在保持积极的开发人员体验的同时实现这一点是困难的，但却是至关重要的。归根结底，开发人员只是想实现为Google 的用户构建和交付满足用户需求的 Web 应用程序的目标。Google 需要确保，Google 总是可以说"是的!安全的方式是……"，而不是对开发人员的问题说"不"。这植根于 Google 团队的一个座右铭："对开发人员的同理心"。

### #2：适应性

由于 Web 平台的变化和新颖的安全研究，安全是一个不断变化的目标，这意味着 Google 需要确保Google 的Web安全方法是可适应的，允许Google 适应未来可能发生的任何情况。Google 不断进行深入研究，以确保Google 的Web框架能够防御经典和新出现的安全漏洞。当Google 发现差距时，Google 会经历以下过程：

* 设计新的安全机制。这通常从为Google 自己的框架和库设计新的有针对性的缓解措施开始，以测试Google 的想法并证明它们是有效的。但从那里开始，Google 经常尝试将Google 的解决方案上游到Web平台，在那里它们可以使尽可能多的人受益。
* 默认启用这些新的安全缓解措施，并添加代码门禁以防止回归（参见#1安全编码）
* 运行大规模更改，为现有服务启用这些新的安全缓解措施
* 衡量Google 推广的进展，以了解缓解覆盖率（参见#3可观察性）

这个过程的目标是，一旦应用程序建立在高保证Web框架上，应用程序所有者通常不必担心跟上安全性的步伐。采用新的安全缓解措施是透明和集中完成的，不需要应用程序所有者采取任何行动。有关Google 如何处理这个问题的更详细描述，请参阅这篇文章。

### #3：可观察性

高保证Web框架的最后一个关键组成部分是可观察性。为了使上述组件发挥作用，安全团队必须深入了解每个应用程序的安全状况。当然，可观察性的手动方法是无法扩展的，因此Google 依赖于在框架和基础设施中构建可观察性功能，使Google 能够了解框架行为、安全功能采用情况等等。Google 的 Security Signals \*\*\*\*论文中解释了Google 如何在Google 实现Web安全的可衡量性。

## 关键安全控制

在这一点上，人们可能会问：那么构成高保证Web框架的安全控制到底是什么?Google 想强调，这是一个不断发展的列表，启用下表中的每个功能还不足以保证应用程序是安全的。真正的高保证Web框架需要启用这些功能，但也要以可扩展和可适应的方式做到这一点，以保持开发人员的体验并防止回归。

在此背景下，以下是Google 的高保证 Web 框架自动启用的当前功能列表：

| Control | Risk Category | 描述 |
| --- | --- | --- |
| Secure cookies | Encryption | 所有cookies应使用`Secure`属性，以确保它们只对使用HTTPS的页面可用。 |
| HTTPS Redirects | Encryption | 所有HTTP响应应将HTTP请求重定向到HTTPS。 |
| HSTS | Encryption | 所有HTTP响应应使用HSTS，以确保浏览器默认使用HTTPS URL。 |
| XSRF Protection | Isolation | 所有状态更改端点应部署强XSRF漏洞防护。 |
| SameSite cookies | Isolation | 所有cookies应使用`SameSite`属性，以确保它们不会附加到跨站点请求。 |
| Framing Protections | Isolation | 所有页面应部署framing protections，以防止不受信任的第三方在敏感页面中使用iframe。 |
| Cross-Origin Opener Policy | Isolation | 所有页面应部署COOP，以防止不受信任的第三方页面在弹出窗口中打开它们并与之交互。 |
| Fetch Metadata Protections | Isolation | 所有页面应部署Fetch Metadata protections，默认阻止跨站点请求。 |
| Cross-Origin Resource Policy | Isolation | 所有页面应设置CORP header，以防止它们在意外的跨站点上下文中加载。 |
| Hostname Validation | Isolation | 所有服务应验证`Host` header，并拒绝具有意外值的请求。 |
| JS/TS Conformance | Injection | 所有服务应使用compile-time conformance来阻止JS/TS代码使用不安全的模式。 |
| SafeResponse Types | Injection | 自动conformance check应确保所有HTTP响应都是通过API abstractions构建的，这些abstractions保证以无XSS的方式构建，例如通过安全的auto-escaping template system。 |
| Contextual Auto-Escaping Template System | Injection | 所有HTML响应应由支持contextual auto-escaping的template system构建，以保证响应不存在XSS漏洞。 |
| Default Content-Type | Injection | 所有HTTP响应应显式设置`Content-Type` header。如果缺少此header，响应应默认为安全值(例如`text/plain`)。 |
| HttpOnly cookies | Injection | 所有cookies应使用`HttpOnly`属性，以确保客户端JS无法访问它们。 |
| Strict CSP | Injection | 所有页面应部署基于nonce的Strict CSP，以缓解XSS漏洞。 |
| Trusted Types | Injection | 所有页面应部署Trusted Types，以缓解DOM-XSS漏洞。 |
| Allowlist CSP | Injection | 所有页面应部署allowlist CSP，将允许的JS源集限制为经过审查和可信的JS serving hosts。这有助于缓解runtime supply chain attacks。 |
| Strict dependency controls | Injection | 应审查build-time使用的所有libraries，以缓解build-time supply chain attacks。 |
| JS Integrity Validation | Injection | 所有页面应验证所有included scripts的integrity，以确保它们在build-time和runtime之间没有被修改。 |
| Prototype Pollution Mitigations | Injection | 所有页面应部署针对Prototype Pollution的mitigations。 |

值得强调的是：这个列表中的所有内容都由安全团队维护。使用Google 的高保证Web框架，应用程序所有者不需要了解任何这些功能——它们都是默认启用的，并且开箱即用。其中一些功能确实限制了应用程序所有者编写的代码（例如，它们会阻止编写诸如document.body.innerHTML = "foo"之类的代码），但这是Google 在之前的文章中描述的"安全编码"方法的有目的的一部分。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk4e3icibiaFicz9xSwuS3SWiagEuia0a13yknNgT18icWAIibdNbOaic9RQic3a5yoqesqgvA3WcPwXdwrQ6tCQ/640?wx_fmt=jpeg&from=appmsg)

image

在Google 的高保证Web框架上构建的应用程序的典型响应，其中安全相关HTTP响应头是默认启用的。

## 案例研究：XSS缓解措施

Google 可以通过一个简短的案例研究来检查这些不同的安全控制如何协同工作以提供高保证保护。Google 可以检查这个问题：在启用所有这些缓解措施的情况下，XSS需要什么条件才能发生?

经典的XSS向量都得到了缓解：

* 反射型和持久型XSS：通过安全响应类型、上下文自动转义模板系统和严格CSP缓解

+ 要发生反射型或持久型XSS，需要涉及安全响应绕过、模板系统中的漏洞以及严格CSP的绕过。

* DOM XSS：通过JS/TS一致性、严格CSP和可信类型缓解

+ 要发生DOM XSS，需要绕过Google 的编译时JS/TS一致性、严格CSP和可信类型。

除此之外，其他类型的XSS也得到了缓解：

* 原型污染→XSS：通过冻结和密封原型链缓解。
* 供应链攻击→XSS：通过允许列表CSP缓解。

综合起来，上述缓解措施使Google 能够非常自信地认为，建立在高保证Web框架上的应用程序不存在XSS缺陷。

## 结论

Google 希望Google 构建和部署高保证Web框架的方法可以作为一个存在证明，证明可以大规模地构建安全的Web应用程序。

在过去的3年里，对于建立在Google 的高保证Web框架上的数百个复杂的Web应用程序，**Google 每年平均收到的XSS报告不到一个，不是每个应用程序，而是所有应用程序加起来！**

这表明，通过高保证Web框架大规模构建安全Web应用程序确实是切实可行的（并且具有成本效益）。这些框架的主要优势在于它们提供：

* 高保证和减少漏洞：Google 分析了来自VRP和内部研究的数据，数据清楚地表明：安全框架大大减少了可利用的Web漏洞数量。
* 多层保护：Google 在编译时和运行时部署多层保护，以确保纵深防御。这确保了如果Google 的任何保护措施存在差距，它很可能会被多个重叠的保护层阻止。
* 提高开发人员的生产力：通过让框架处理安全问题，Google 使开发人员不必考虑安全问题，使他们能够专注于核心产品目标。Google 还通过为建立在安全框架上的产品启用自动化发布审查，加快了产品发布速度。
* 改进可维护性：得益于内置的适应性和可观察性，Google 的安全框架易于维护，并且可以根据需要在未来进行扩展。

**安全没有银弹。**但 Google 相信，以框架为中心的安全方法是 Google 一劳永逸地消除 XSS 和 XSRF 等几十年前的漏洞的最佳途径。Google 在内部构建了这些框架，Google 坚信，更广泛的 Web 生态系统也将受益于采用其中的许多想法，以提供高安全性保证，Google 的目标是在未来将这一想法带到外部开源 Web 生态系统中。

*以上内容编译自 Google*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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