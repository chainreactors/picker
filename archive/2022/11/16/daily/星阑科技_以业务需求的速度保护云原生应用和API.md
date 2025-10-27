---
title: 以业务需求的速度保护云原生应用和API
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496434&idx=1&sn=8984251700aae6c4dcdba71910dea2b8&chksm=c0075f6ef770d6788490224d58fcc5368f602f55db569d097f6eb4ee96833f6cdac61950e56a&scene=58&subscene=0#rd
source: 星阑科技
date: 2022-11-16
fetch_date: 2025-10-03T22:53:34.654968
---

# 以业务需求的速度保护云原生应用和API

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOejK4Aa2cAexT83B7GUn8K4tjuW60yjItckILgKqtvWnlfxW1HM8Gib8yZkg6bgcJPOZicARrSfyCibicw/0?wx_fmt=jpeg)

# 以业务需求的速度保护云原生应用和API

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

近年来，云原生开发模式进入主流，微服务和无服务器计算、容器、API 和基础设施即代码 （IaC） 等技术处于这一趋势的最前沿。借助这些新兴技术，组织可以以分布式方式快速构建和运行其应用程序，而无需依赖物理硬件基础架构。但是，虽然这种灵活性有助于在整个软件开发生命周期 （SDLC） 中节省时间和金钱，但它并非没有安全价格标签。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejK4Aa2cAexT83B7GUn8K4tbo0Nn0AZDemdoiaPGhID5eFTib5D6YgvrLP4J83WNDicMpxiaa13MudMZA/640?wx_fmt=png)

**云原生应用程序的安全问题**

例如，保护云原生应用程序需要充分了解微服务向各种使用者公开的接口，以及容器映像的正确安全配置和运行。近年来，拥有内部开发的云原生应用程序的组织面临着各种安全事件，主要原因是 API 使用不安全、源代码易受攻击和帐户凭据泄露。

部署和管理基于云的应用的两个关键问题是扩大的攻击面和更大的复杂性。随着开发人员快速启动云原生（无服务器或基于容器）工作负载，将暴露更多攻击面。云原生应用程序中的每个函数、API 和协议都存在更广泛的潜在攻击媒介。事实上，在ESG对最近安全事件的调查中，API的不安全使用被证明是云原生应用程序堆栈容易受到攻击的主要原因。

云原生架构还增加了安全治理和控制的复杂性，因为组织必须考虑多个权限、身份验证和访问管理问题。随着开发人员越来越多地使用 IaC，由于编码错误而导致 IaC 模板配置错误的可能性更高。不幸的是，关键数据泄露和未经授权访问应用程序和敏感数据等错误直到周期后期才能检测到。这使得组织管理起来更具挑战性和耗时性。

**传统的应用安全工具跟不上**

传统的应用程序安全测试 （AST） 工具不是为云原生应用程序设计的，因此无法提供足够的覆盖范围、速度或准确性来满足这些现代应用程序的需求。旧版 AST 工具对现代应用开发和部署体系结构的可见性较差，因为大多数 API 和无服务器函数调用都是事件驱动的触发器，并且某些函数没有面向公众的终结点或 URL。虽然一些供应商可能会吹捧针对云和无服务器应用程序的最佳静态扫描，但事实是，扫描上下文仅限于零的代码并不是有效的 AST 解决方案。

根据Gartner关于启用云原生DevSecOps的最新报告，绝大多数70%的团队在开发中使用静态应用程序安全测试（SAST）工具，在生产中使用Web应用程序防火墙（WAF）和应用程序监控工具。该报告还显示，在SDLC的开发和测试阶段，API安全测试，IaC扫描和交互式应用程序安全测试（IAST）等较新的工具越来越多地使用。

但是，有效的 API 安全性不能仅仅通过一些 Web 防火墙和监控工具保护和阻止易受攻击的 API 来实现。基于 API 的应用需要作为其自身的完整开发生命周期进行处理和管理。正如软件应用程序开发生命周期要经过前期规划和设计一样，API 生命周期也必须经过。需要有适当的 API 设计，并将 API 策略内置到组织的整体业务风险和连续性计划中。

组织还必须执行一些内部管理，并构建可用于风险评估、分类和质量控制目的的所有基于 API 的应用程序的清单。最终，目标是专注于具有最高风险因素以及时间和专家资源限制的基于 API 的应用。

**必须持续测试和验证**

在我们看来，下一步是最重要的，也是当今API安全性中缺失的一环。有效的 API 安全实践应包括持续实时测试和验证易受攻击的 API（包括自定义、开源和面向公众的 API）的能力。例如，拥有一个 API 工具可以发现每个应用程序的所有 API，并建立防火墙以允许流量仅在遵守定义的风险策略时才访问 API，这是不够的。更好的 API 策略将扩展 API 发现功能，包括在运行时编译时使用其他开源和第三方代码库和 API 进行集成应用程序测试期间持续动态测试、验证和分类。

这是有效的API安全策略的关键本质。组织需要能够在应用进入生产版本之前快速识别并主动测试和修正风险最高的应用（由其安全策略和 API 风险分类定义）。API 风险分类系统可以使用应用程序暴露（面向内部或外部的应用程序）、它处理的信息类型（例如，与 PII/PCI-DSS 支付相关的信息）、应用程序管理的记录大小（可能达到数千和数百万）以及数据泄露、灾难恢复和业务连续性影响的成本等标准。

Gartner最近的云原生调查发现，除了SAST和WAF之外，组织还在整合其他AST解决方案，如软件组合分析（SCA）、IAST和API测试。IAST 等现代应用程序安全测试解决方案可以帮助减轻在 DevOps 环境中执行安全测试的负担，因为它不需要额外的扫描、会审或验证，从而增加连续管道的时间和测试周期。

**新网如何帮助您保护云原生应用**

高级 IAST 工具（如 Synopsys 的搜索器）在保护云原生应用方面是独一无二且有用的。它可以检测、测试和验证所有入站和出站 API 调用，无论它们是应用声明的 API 调用还是未测试的可调用 API。它还跟踪和测试常用的无服务器函数（如 AWS Lambda 和 Azure 函数），而不会向连续管道添加额外的扫描周期和摩擦。

一切都由工具在后台自主完成，而正常的开发和QA测试工作负载则由团队执行。DevOps 和安全团队可以获得所有关键和敏感数据流的高度交互式和可视化地图，包括易受攻击的路径和潜在的敏感数据泄漏。开发团队可获取实时信息 — 从堆栈跟踪到详细的代码行，以及修正指南。

与需要API规范来执行安全测试的传统动态扫描程序不同，使用搜索器IAST，不依赖于OpenAPI或斯瓦格文件。搜索器可以使用其检测代理发现所有可调用的 API，并可以基于邮递员或 HAR 文件生成 OpenAPI 文档。它可以跟踪和检测所有应用程序请求和响应，其中包含 JSON、XML 或更新格式（如图形 QL、gRPC 和 Kafka）的有效负载。它还提供所有端点调用的目录，包括未经测试的可调用 API 和 URL。

除了 Seeker IAST 之外，Synopsys 还提供完整的端到端扫描技术，有助于保护您的云原生应用程序。代码视觉™轻量级 SAST 使开发人员能够立即检测并修复其 IDE 中易受攻击的代码。覆盖性®静态分析和黑鸭软件®成分分析有助于保护IaC、容器化应用程序和图像。Synopsys 提供全面的应用安全测试工具和服务组合，可帮助您的团队快速、轻松地查找和修复关键漏洞，如访问和身份验证问题、跨站点脚本以及各种类型的注入。

微服务风格的体系结构是一种将应用程序构建为一组各种服务的方法。简而言之，这意味着使用许多单功能模块或部件构建应用程序。每个模块都有一个明确定义的接口和预期操作。

**微服务的起源是什么？**

随着组织在早期的企业软件应用程序开发时代从单体架构转向面向服务的架构，微服务应运而生。这种演变继续受到垂直行业企业的多方面需求的推动。

随着开发速度的不断提高，摆脱旧的和功能失调的应用程序的需求也在增加。这些单一的自主单元不容易更改，因此对应用程序的任何升级或增强都很慢，并影响了整个系统。对一段代码的简单更改可能意味着重新部署整个新版本的软件。

微服务通过提供将应用程序构建为可独立部署的小型服务或部件集合的能力解决了这个问题，这些服务或部件可以在不影响整个系统的情况下进行更新和更改。

**微服务如何工作，为什么它很重要？**

微服务以这样一种方式构建应用程序，即它由可以独立部署的各种较小部分或服务构建。

这种结构对现代软件开发至关重要，因为它可以实现敏捷性和速度。

**微服务结构的主要优势包括：**

**微服务是松散耦合的。**松散耦合意味着包含应用程序的服务几乎独立地运行，因此对单个服务的任何更改或更新都不会对整个应用程序产生影响。

**微服务可独立部署。**团队可以部署自己的服务，而无需与其他团队协调，也不必担心对他们或整个应用程序产生负面影响。

**微服务是高度可维护和可测试的。**由于微服务的自主性，可以轻松测试和维护单个部分或服务，而无需团队在执行此操作时接触整个应用程序。

**使用微服务有什么好处？**

**开发人员使用微服务架构的一些原因包括：**

微服务易于迁移和优化。它们使在多团队环境中运营的组织能够以各自组件交付所需的速度和敏捷性工作。每个团队都可以开发自己的一组微服务，并可以灵活地根据自己的需求选择最佳技术堆栈。

微服务体系结构不需要一个团队先完成其分配的活动，然后另一个团队才能执行其活动。

微服务是 DevOps、CI/CD 和自动化的良好补充和推动者。

使用微服务可以节省时间并提高工作效率。由于应用程序某一部分的更改不需要再次部署整个应用程序，因此 QA 和发布周期可以更短。

微服务有助于改善用户体验。开发团队可以不断迭代和改进应用程序，以跟上市场变化和需求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOejK4Aa2cAexT83B7GUn8K4tCib2MTu6tib3FfJbeNg5Eaib8nLzIpJVV5SeQzgGxicfGVHC1kExRU46Jw/640?wx_fmt=jpeg)

**使用微服务有哪些挑战？**

尽管微服务具有许多优势，但它们面临很多挑战。

**挑战包括：**

**增加了保护应用程序的复杂性。**这是因为微服务在基本的多语言体系结构中运行。

**缺乏可见性和可追溯性**。这是由于微服务的高度分布式性质，多个服务和组件相互通信和传递数据。

感谢 synopsys 提供相关内容

**关于星阑**

星阑科技基于AI深度感知和强大的自适应机器学习技术，帮助用户迅速发现并解决面临的安全风险和外部威胁，并凭借持续的创新理念和以实战攻防为核心的安全能力，发展成为国内人工智能、信息安全领域的双料科技公司。为解决API安全问题，公司从攻防能力、大数据分析能力及云原生技术体系出发，提供全景化API识别、API高级威胁检测、复杂行为分析等能力，构建API Runtime Protection体系。

星阑科技产品——萤火 (API Intelligence) 拥有不同应用场景的解决方案，适配服务器、容器集群、微服务架构以及云平台等多种架构。**通过API资产梳理、漏洞管理、威胁监测、运营与响应能力，解决企业API漏洞入侵、数据泄露两大核心风险。**

**往期 · 推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5aaaIEbK8js13dUHyRfibIdUys85kCDVCramykaQGeXgc8p9JQnS1geQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493320&idx=1&sn=41d96f17d2a226c31b23b35d93a36f2a&chksm=c0074b54f770c242d6897443eb4980fb58a0f065ea2d8593cb3b8548b370bc075acc57a7c1c1&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5vlPrkrPnU4NyZ0iczokrvBmOTVJicE184CicXlbFiaZWJOndBYBGicG2hdw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493183&idx=1&sn=2af1758db0a3a191fab5a06c5d42d5e2&chksm=c0074ba3f770c2b5f823d3d51f8dca78e4992fed1af362fd343cccff4869215b4cdd1d530c14&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM52U6A0N7fnFeFsaWichvGj4xZZ3LbRJwc4CT8zvnZw5ZOjVlQ6Fgiczgg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493126&idx=1&sn=58636a0f6eb16b77ab08166257c8ac39&chksm=c0074b9af770c28c03fb7893f6f2f624955bcf1791a34be921b46b139084690227b01e8a79e7&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOeg8a6qhBHC2rMicO0SV9TSM5DNcU7icAy0S11XGM1klz1juoesMJBlWkgqIZa6amb13MmibdhLwkuGLw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247493022&idx=1&sn=a39a77fbab2b9b01c50c77ab9e9f3cda&chksm=c0074802f770c11453cbfb45123934a5fa24979d0a0d779dbb9b390d8a276fd06bc80ffddb4a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOehwcHoxicoOah5mxDjLHMZ9RHUxNeibERphRXOj3AEupxt7JyOt3LF1RmmWQibYmicTv2DxM93iaEJhLxw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

星阑科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

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