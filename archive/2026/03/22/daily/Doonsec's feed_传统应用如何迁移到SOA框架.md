---
title: 传统应用如何迁移到SOA框架
url: https://mp.weixin.qq.com/s/31vvsv3fhVFe9guwei1RvQ
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:43.851650
---

# 传统应用如何迁移到SOA框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDIZBL5rUlgzJaPINk9oFA2ptm4ibibanialgKcsLhJzOkjTbfJiaoyJ2cFYzr76gl9iaeSW0pSEKm6oHrl1ibghL2xTSNYrlryJoZOk/0?wx_fmt=jpeg)

# 传统应用如何迁移到SOA框架

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

软件定义汽车 (SDV) 的特点是 AI、自主、连接和电气化。最近，汽车行业已开始采用“基于服务”的方法来设计 SDV 的现代应用。这种称为面向服务的架构 (SOA) 的方法为开发软件应用提供了一种新范式，其特点是高重用性、易于更新以及与硬件的松散耦合。SOA 的构建原则是一个应用由一组服务组成，这些服务可以被动态地发现、发布、订阅和在运行时重新配置。SOA 的概念已被广泛纳入行业标准，包括 AUTomotive Open System ARchitecture (AUTOSAR)。

在 SOA 框架中，服务具有自包含、模块化、松散耦合等特征，这使得创建本质上非一体式的复杂分布式应用成为可能。基于 SOA 的应用可以使用自上而下或自下而上的方法来开发。在标准 SOA 软件堆栈中，应用软件由服务、平台服务和中间件组成。它们都运行在高性能硬件或虚拟机上。

**01**

**将旧应用迁移到 SOA 面临的挑战**

由于旧应用的若干特性，将其迁移到 SOA 可能颇具挑战性。这些特性包括：

一体式设计：旧应用通常采用一体式设计（图 1），组件的耦合和互连均很紧密。这使得很难将其分解成若干单独的服务，因为功能是相互交错的，而不是模块化的。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUsKyo3M3gEWWFNS0icA9sMVSa91V0vBYxTxCSnI2OCAsPVK9lK8krYfQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

图 1. 组件紧密耦合的一体式设计

执行顺序：旧应用的组件通常有预定义的执行顺序。这种顺序执行方式使得应用难以转换为可动态发现和在运行时重新配置的独立服务。

基于信号和基于时间的通信：旧应用通常依赖组件之间基于信号或基于时间的通信。在 SOA 中，通信通常基于服务接口和交换消息。将旧应用的通信机制调整到面向服务的方法需要仔细考虑各个事项，甚至可能需要重新设计通信协议。

克服这些挑战通常需要全面分析旧应用的架构，并仔细确定组件之间的服务边界和依存关系。这可能需要将应用重构为更加模块化和松散耦合的若干单元，进而将这些单元封装为 SOA 框架中的各个服务。

将旧应用组合转换为服务是一项复杂的任务。例如，以前设计的一体式应用组合（如高速公路车道跟踪应用）可以变换为单个服务，也可以分解为多个服务，如相机服务、视觉服务、雷达和车道导航服务。

系统专业知识和基于模型的设计有助于把一体式应用设计分解为若干服务函数，从而将各个逻辑组件进行封装和抽象分离。它可以助力信号到服务接口的迁移并确定正确的执行顺序。在本文中，我们将介绍一个基于模型的设计工作流。此工作流可对新服务进行建模，亦可将您的传统应用组合转换为基于软件定义汽车的 AUTOSAR Adaptive 概念的服务。

**02**

**将传统应用软件组合分解成服务**

将传统应用软件组合分解成 SOA 应用的服务涉及将一体式架构分解成更小、更模块化的组件（图 2）。这对 SDV 来说意味着更大的灵活性、可扩展性和自适应性。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUueyZNhxcPAWNFCqFiaZYfEC1CaVboZkphibKiaspKPia9ibqobaYY1zQ9DA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

图 2. 将传统应用软件组合分解成服务的步骤

将传统应用软件组合分解为 SOA 应用的服务涉及四个步骤。

识别和分析服务：识别组成 SOA 的服务、组件、功能、执行顺序和依存关系。对于工程师来说，这是最困难的部分。完成之后，他们必须分析服务，以将传统的一体式应用分解成更小的组件（图 3）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUibQLtKiaZ3GCHiaTWGiab57OHiboujaIWiaibyiciaXYsrdB3utC2PhxrZtwib3A/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

图 3. 将软件组件分解为服务

定义服务和接口：在识别服务后，必须定义它们之间的接口。这涉及指定用于服务间通信的协议和数据格式，以及定义指定服务间交互的条款和条件的服务合约。

定义服务合约：此步骤指定服务之间交互的条款和条件。AUTOSAR 架构版本 22-11 中引入了这些概念。该架构指定服务的版本控制，支持在不破坏现有客户端兼容性的情况下发布新版本的服务。

实现和部署服务：实现服务并将其部署为独立应用，具有自己的工件，包括接口描述。

**03**

**使用基于模型的设计迁移到服务**

基于模型的设计已用于开发非 AUTOSAR 框架和 AUTOSAR Classic 框架的应用。它还可用于为 AUTOSAR Adaptive 和通用 SOA 框架开发基于 SOA 的应用。对于 SDV 应用，业界通常利用通用 SOA 或基于 AUTOSAR Adaptive 平台的 SOA。基于模型的设计的优势在于可以提供统一的开发平台，有效地处理所有类型平台（包括 SOA、AUTOSAR Classic 和 AUTOSAR Adaptive）的整个开发过程，能够确保全面的一致性和效率。

使用基于模型的设计将一体式应用组件分解为服务涉及以下步骤：

识别和分析服务：了解各种组件、其功能、执行顺序以及它们之间的依存关系。一个一体式应用的所有组件均部署为一个可执行文件进行部署（图 4）。然而，当分解成服务时，每个单独的服务均独立部署。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUN5erR5FCMZQfqnSTPtQukoNNssBl7gCF48eVOfz8qsHD6x39eEJrxQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

图 4. 所有 Simulink 模型作为一个可执行文件进行部署

例如，图 4 中有一个在 Simulink® 中开发的高速公路车道跟随应用，它作为一个一体式应用组合进行部署。使用 Simulink 将这样的一体式组件分解成服务（图 5）需要依据单一职责原则和依赖倒置原则。根据这些原则，高速公路车道跟随模型可分解为多项服务，如雷达、视觉和车道。这些服务具有良好定义的职责和松散耦合的依存关系，支持隔离对服务的更改，并且最小化更改对其他服务的影响。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUAkicT7Nt39KjNbuqCicZ70pcYhnHG702U1uLq0sDDMPNUyvytOuYyMxg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

图 5. 使用基于模型的设计将一体式旧应用分解为服务

一体式应用分解成若干基于 SOA 的服务，并用客户端-服务器端口将它们连接起来

定义服务和接口：使用接口定义的服务是服务边界的一部分。服务边界同样定义了服务与其他服务交互的通信通道。服务边界还封装功能，以实现重用、可维护性、版本控制、可见性、编排和其他好处。使用 System Composer™，您可以配置相关服务组件的端口以实现数据一致性，并通过原型来表示这些服务之间的交互方式。这提供了服务之间依存关系和交互的可视化表示（图 6）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUWOtFyrunUjBAB6wt2ibXmgabNo3qGLtocoMHhARY20AUaXkxcaiaU3ug/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

图 6. 在 Simulink 中配置服务组件的服务接口和端口

定义服务合约：我们建议为服务建立清晰的边界，定义其输入、输出和行为。这让服务可以独立地开发、测试和部署，而不需要与架构的其他部分紧密耦合。通过定义服务合约，您可以了解服务的功能和限制，并且可以更轻松地与它们集成。此外，服务合约可以在不破坏与现有客户端的兼容性的情况下发布新版本的服务。

实现和部署：使用基于模型的设计中的客户端-服务器接口，您可以创建 SOA 软件架构模型。图 8 展示了在 Simulink 中作为服务实现的 LaneGuidanceApp、DetectionApp、雷达和视觉算法。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUwAN4p4BT2MHbdXOVGL0ErfpUced3OOr9AKynbg8KxYhwApFcQzvsxw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

图 8. Simulink 中 SOA 服务的算法实现

**04**

**为 AUTOSAR Adaptive 应用配置服务**

您可以使用 Simulink 建模结构为 AUTOSAR Adaptive 无缝配置这些服务。如图 9 所示，我们使用 System Composer 中直观的 AUTOSAR 编辑器，成功地将所有服务作为 AUTOSAR Adaptive 服务进行了集成。随后，我们为每个端口和接口建立了必要的映射，确保它们与对应的 AUTOSAR Adaptive 属性保持一致。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUdIWrgMwv9iciawj17w0biafPo1v7L4ZvM5AHO0brL44wNNbNYbTcV30fg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

图 9. 设计、开发 AUTOSAR Adaptive 应用的服务并为其生成 C++ 代码

以雷达服务为例，它链接到一个 Simulink 模型。该模型在根级使用 Simulink Function 模块来创建Adaptive methods (3:50)服务接口。此处，AUTOSAR 服务接口的方法定义了一个软件组件（建模为提供接口的服务器）和另一个软件组件（建模为需要接口的客户端）之间的交互。

在 Simulink 中，客户端-服务器通信可以用同步或异步调用行为进行建模。同步客户端模型导致客户端执行阻塞，也就是说客户端会向服务器发送请求并等待响应。异步客户端模型不会导致执行阻塞，也就是说客户端会发送请求、在发送请求后继续当前执行并在收到服务器响应后进行处理。

雷达服务是一个使用客户端-服务器通信的服务器。在图 9 中，代码映射 UI 显示了 Simulink Function 模块和函数元素端口的映射 - radarCtrl.Adjust 和 radarCtrl.Calibrate 及其各自的 Adaptive 端口。

此外，您还可以在 Methods 服务接口的 AUTOSAR 字典中查看和编辑 AUTOSAR 属性（图 10）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUghIt0cUWTZcvbtfZWdAFO1ibib0H95hP6j0F9948bvicYn6OJVUj5KNtg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

图 10. 用于查看/编辑属性的 AUTOSAR 字典

LaneGuidanceApp 服务作为客户端运行，并通过异步调用利用客户端-服务器通信（图 11）。此示例中的客户端使用异步通信，并受益于非阻塞执行，能够在向服务器发送请求后继续执行。在 Simulink 模型中，它使用带有 Message Triggered Subsystem 模块的 Function-Call Subsystem 模块来异步执行函数调用。代码映射 UI 显示 Simulink 函数调用方与对应 AUTOSAR Adaptive 端口。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUJkyo9yIQIZM61XttoBTC6MUR1SLqkoNxI9X7xMrziaY6gHVP89wP28w/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

图 11. 映射到 LaneGuidanceApp 服务的 AUTOSAR 属性的 Simulink 模型

同样，所有其他 SOA 服务都是根据 Simulink 中的 AUTOSAR Adaptive 概念进行配置的。

经过验证和仿真后，每个 AUTOSAR Adaptive 服务都可以作为独立应用程序进行部署，并具有自己的工件，包括 C++ 代码和 AUTOSAR 接口描述，其中包含机器、执行和 ServiceInstanceManifest 文件。最后，使用 Embedded Coder 生成 AUTOSAR Adaptive C++ 代码以及对应的软件描述和清单文件，以便进一步集成到工作流中（图 12）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicCheUyzk3KDMSwGsiaQ4xibUuF4wibRZKpY251k592hNqZRSNFGBOLwV0H4649n6FKOxosMWpiaD7kNw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

图 12. AUTOSAR Adaptive 应用程序的 C++ 代码接口文件生成

**05**

**结论和将来的工作**

基于模型的设计为系统开发提供了一种结构化方法，支持创建表示应用架构、组件和交互的模型。在本文中，我们通过高速公路车道跟随参考示例说明了如何使用基于模型的设计将传统一体式应用分解为服务，然后将它们配置为 AUTOSAR Adaptive 应用程序。这些模块化服务可作为一个开端，使工程师能够创建、仿真和生成 C++ 代码以及清单文件，以便进一步集成到工作流中。

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFG...