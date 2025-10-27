---
title: Kitex/Hertz 助力大模型：三周年重要特性回顾
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247512321&idx=1&sn=640849f1c1c8027757ebfcbbff7ae06d&chksm=e9d37ae3dea4f3f54d444731f77ffc650389d0a0b8c0e7690ba1020905d8c43896c457cd6dfb&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-12-14
fetch_date: 2025-10-06T19:41:38.629733
---

# Kitex/Hertz 助力大模型：三周年重要特性回顾

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOheOVtKEQTh3tFsiauiblOkaA7u90eVw9PpRtS2dfZF362Zxbv7mpY5bWkLFPnInlzr43wVukYs9gyw/0?wx_fmt=jpeg)

# Kitex/Hertz 助力大模型：三周年重要特性回顾

杨芮

字节跳动技术团队

Kitex 项目地址｜https://github.com/cloudwego/kitex

Hertz 项目地址｜https://github.com/cloudwego/hertz

CloudWeGo 开源走过了三周年，秉持**内外统一**的原则，我们持续在开源仓库迭代，将服务于字节内部的特性发布到外部，23-24 年 Kitex/Hertz 重点关注**大模型**、**用户体验**和**性能**三个方面，帮助新的业务场景快速发展，并在用户体验和性能上持续优化。同时，Kitex/Hertz 在外部企业得到了广泛应用，也吸引了众多外部开发者，持续完善 CloudWeGo 的生态。

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuEsFODiajcPvlsyBy2DvEuCLXwBzwULD6WDJ0J8Mw3OBC4jfb13ff7T3EDpgb7dDL76ghT4iaOiaKHsQ/640?wx_fmt=png&from=appmsg)

本文根据 CloudWeGo 三周年 《Kitex/Hertz 助力大模型：三周年重要特性回顾》 分享整理，介绍近一年来 Kitex/Hertz 的重要特性，希望为企业用户、社区同学在自己的项目中更好的应用 Kitex/Hertz 构建自己的微服务体系提供帮助。

**加强流式能力助力大模型**

大模型快速发展，字节跳动的 AI 应用也发展迅速，而**流式通信**是大模型应用的主要通信模式，为了更好的支持业务发展，我们在近一年对微服务的流式通信在稳定性、工程实践、性能上做了诸多优化。

## **Kitex/Hertz 过去流式能力的支持**

Kitex/Hertz 均支持流式场景，Kitex 支持 gRPC，性能优于官方 gRPC，功能基本对齐；Hertz 支持 HTTP Chunked Transfer Encoding、WebSocket。

但以上能力**不足以支持字节内部 LLM 快速发展**，有以下几点原因：

* **端上****SSE****应用更多**

多模态模型之前，大模型应用主要是文本对话场景，多使用 SSE 协议实时返回服务端结果给客户端。文本推送场景更简单，选择浏览器支持友好的简单协议即可。

* **Thrift****->****Protobuf****切换负担**

虽然 RPC 场景的流式通信普遍使用 gRPC(Protobuf)，Kitex 也支持 gRPC，但字节服务端服务主要使用 Thrift 定义，研发对 Thrift 使用更加熟悉，使用 gRPC 协议的服务并不多。然而，在流式使用诉求变多的情况下，我们需要结合内部实际情况，减少研发切换的心智负担；另一方面，广泛增加 Protobuf 定义的服务，对统一 IDL/接口管理并不友好。

* **缺乏工程实践**

流式通信相比 PingPong 一发一收的模型在**服务治理**和工程实践上增加了复杂度。业界对流式通信的支持缺乏工程实践的沉淀；流式接口很容易用错进而影响到服务的稳定性；从可观测性角度，也没有看到对流式监控的定义。

## **流式能力 - SSE/Thrift Steaming**

### **> Hertz SSE**

SSE(Server-Send Events) 基于 HTTP 协议，支持服务端向客户端单向推送数据，优点是简单易用、对开发者友好，适合文本传输，满足文本对话模型的基本通信需求。

相比于 WebSocket，**SSE 更轻量级**，对于文本对话的大模型应用，服务器只需要推送数据到客户端，无需处理双向通信的复杂性。但在语音对话模型场景，同样浏览器支持友好的 WebSocket 则更适合。

SSE 可以定义不同的事件类型，并在客户端根据事件类型处理数据。这在大模型应用中，可以用来区分不同类型的响应数据（例如，部分输出、错误消息、状态更新等）。

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmYdpUsUvpv76F8CJhqdn87ibia5WkzXn3WTqU832S3SszsZcqvlLtySxg/640?wx_fmt=png&from=appmsg)

但是，**SSE 并不适合服务端**：服务端计算和传输性能要求较高，不适合采用低效的文本协议；JSON 简单但并不适合服务端复杂交互场景，强类型的 RPC 更友好；部分场景需要双向流式通信。

所以，结合字节内部的情况，我们支持了 Thrift Streaming。

### **> Kitex Thrift Streaming**

流式通信的使用场景除了**大模型**应用外，还有其它业务线的使用场景，比如：**抖音搜索**为提升性能，希望 RPC 流式返回结果，如在视频打包阶段，根据召回的视频 ID 获取物料等相关信息，希望一次请求打包服务（10个doc），先打包完的先返回；**飞书 People** 数据导出场景会并发获取数据，如果等待所有数据都获取到后再填充 excel 返回，当数据量过大时会导致 OOM，进程异常退出。所以，增强流式能力，一方面助力大模型快速发展，另一方面也满足其他业务场景发展。

虽然 Kitex 支持 gRPC，但对内我们还是建议使用 Thrift，支持的多可以满足多元需求，但对一个公司内部最好是明确一种最佳实践，尽可能减少研发的选择负担，工具链体系支持也会比较友好。

**Streaming 协议**

字节内流量管控主要依赖 Service Mesh，但为了能快速支持落地，不依赖 Service Mesh 对新协议支持，Kitex 先支持了基于 gRPC(HTTP2) 的 Thrift Streaming。因为官方 gRPC 的协议规范支持扩展 content-type，所以实现方案是**基于 gRPC 的 PRC 通信规范，将 Protobuf 编码改为 Thrift 编码**。

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPm9UWOiaoSKiasLdvQYMCNwcJWxPLG3TChqiamfS6fm6Qic4Ue32amevbTlQ/640?wx_fmt=png&from=appmsg)

**Thrift over gRPC** 在 23 年 12 月开始在字节内部试用，于 24 年 3 月在 Kitex **v0.9.0** 正式发布，目前已经在字节内部大规模使用，使用说明见官网文档。

* **优点：**

+ Service Mesh 兼容：基于 HTTP2 传输，Service Mesh 无需单独支持
+ Kitex 支持成本低：根据 SubContentType 明确解码类型(gRPC 协议规范支持扩展)

* **缺点：**

+ 资源开销大：流控、动态窗口引入额外的开销
+ 延迟影响大：流控机制，流量大一些或发送大包会导致延迟显著劣化，需要用户自行调整 WindowSize
+ 问题排查难：复杂度也增加了问题排查难度

Thrift over gRPC 可以快速落地，但从性能和问题排查的角度，我们自研了 Streaming 协议（Streaming over TTHeader），简化流式通信，目前在内部联调和试用中，预计会在 24 年 11-12 月发布。

**Thrift IDL 如何定义 Streaming**

了解 Thrift 的用户清楚，**原生 Apache Thrift 不支持流式接口的定义**，如果新增关键字，会导致其它 Thrift 通用解析工具无法支持，包括 IDE 的插件解析。

所以通过**注解**的方式对 Thrift 的 RPC 方法定义流式类型，可以保证解析的兼容性：

* streaming.mode="bidirectional"：双向流式
* streaming.mode="client"：Client Streaming
* streaming.mode="server"：Server Streaming

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmEAY8QMicaiaYcV0qH5MoBEccYKGn19kianCYcsO3Sd5ExSjCnOY172rdQ/640?wx_fmt=png&from=appmsg)

当前支持的 Thrift Streaming over gRPC 和即将发布的 Thrift Streaming over TTHeader 都采用这个方式来定义流式方法，预期 Client 端会**提供 Option**来指定采用哪一个 Streaming 协议，Server 端会通过**协议探测**兼容多种协议。

##

## **流式泛化调用**

如果端上采用 SSE 做流式通信，服务端采用 Thrift Streaming 通信，那端上到服务端整体是如何通信的？

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmwoYBia4eDCgoRYr1mVD7FW4bN5g190RRIEbAxThCg5qtv3NIFXNPkNQ/640?wx_fmt=png&from=appmsg)

以内部文本对话模型的场景为例，流量在经过 API 网关后会进行**协议转换**，服务端采用 Server Streaming 的流式类型将数据推送给端上。

其中，比较重要的一个能力是协议转换，除此之外，压测、接口测试平台都需要动态构造数据对服务端的服务测试。

了解 Kitex 的用户清楚，Kitex 针对 Thrift 协议提供了泛化调用的能力，主要就是面向这类通用服务提供支持，原来内部微服务以 Thrift PingPong 服务为主，Kitex 提供了 Map、JSON、HTTP 数据类型的泛化调用，以及面向流量转发场景的二进制泛化。

因此，面向流式接口，**Kitex 新增了流式泛化调用的支持**，相对于 PingPong 的泛化接口，流式泛化需要针对三种流式类型分别提供接口。

* PingPong/Unary 泛化调用接口

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmUAEQIF8Rcajro1aBqibYBRsAkvZz4iazdpsxKGrTkX4NCoSApCSVKFibQ/640?wx_fmt=png&from=appmsg)

* Streaming 泛化调用接口

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmmsmcQjLvQ6AIUjXW8Nezjfee1S6Kwr3QVsNCWJ4PraiaQXfKXJzoiaZA/640?wx_fmt=png&from=appmsg)

目前完成支持的是更为通用的 **JSON** 数据类型，其它数据类型后续也会根据业务需求情况排期支持。（因为 Kitex Streaming v2 接口待发布，避免影响流式泛化的使用体验，所以该支持未正式发布，但功能已就绪，用户可以到官网泛化调用的部分看英文的试用说明）

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPm2CAZS0XrkicESbklc0d3BjpXRicus9ARHib9LKM3qTyqus2rMy4c60ZsQ/640?wx_fmt=png&from=appmsg)

**流式能力用户体验**

虽然针对流式的基本功能场景，我们做了能力完善，以上也介绍了 Kitex/Hertz 过去支持的、新支持的、即将发布的流式能力。但开发过流式接口的同学，包括使用其它框架，如官方 gRPC 框架，大家是否熟悉如何正确使用流式接口，遇到问题是否清楚如何定位？

在字节内部，因为流式服务的发展，明显感觉到反馈的问题数量变多。一方面，相对于 Thrift PingPong，在基础能力层面我们支持的还不完善；另一方面，流式接口的开发需要大家非常熟悉如何正确使用，否则很容易误用而引起问题。

因此，我们在 24 年开启了**流式优化专项**，针对各类问题做了梳理，逐个进行优化。在用户使用体验上，有些问题和流式的接口定义有关，综合考虑决定丢掉流式包袱，发布 Streaming v2 接口。

以下是部分存在的问题，和进行中的优化。如何正确使用流式接口，单纯从框架层面也很难做好约束，所以后续我们会发布流式接口的使用规范和最佳实践，帮助用户开发好流式接口。如果大家有更好的流式使用建议，也欢迎和我们交流~

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmORNfibhLzGwJ4p7MOG8vPt2Me5x4Oef9DbOzv2UODyjOUP2IHqnJiang/640?wx_fmt=png&from=appmsg)

以流式的**可观测性**举例，之前流式接口的监控并没有单独定义，复用 PingPong 上报，所以只有流整体的上报信息，**缺失 Recv/Recv 的监控**。因此，在支持 Thrift Streaming 时，新增了 StreamSend & StreamRecv 事件，框架会记录发生的时间和用户传输数据的大小。企业用户自定义的 Tracer 上报只要新增对 rpcinfo.StreamEventReporter 接口的实现，Kitex 会在每次 Recv、Send 执行完后调用该接口， 在该方法里，可以获取到本次 Recv、Send 的事件信息。如下，是一个 Stream 里 Send/Recv 的 Trace 信息。

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmCcD6peldWicdrxwhpa0icdWdFqoTdHr6VsdmJl8gETyx2LwSQZwOkglQ/640?wx_fmt=png&from=appmsg)

**新功能、用户体验/性能提升回顾**

虽然近一年针对流式能力做了专项支持和优化，但同时，我们也提供了其它新的能力来满足用户需求、增强用户使用体验、继续提升框架性能。

##

**新功能 - Thrift/gRPC 多 Services**

gRPC 官方框架支持多 Service，但 Kitex 之前的版本并未提供多 Service 的支持，主要是为了和 Thrift 使用对齐。**Thrift 的限制是因为支持多 Service 会引入协议不兼容变更**，对用户有影响。在字节内部，TTHeader 协议被广泛使用，所以我们决定通过 TTHeader 传递 IDL Serivce Name，来解决 Thrift 不支持多 Service 问题。

Kitex v0.9.0 版本正式支持在**一个 Server 里注册多个 IDL Service**，包括 Thrift、Protobuf。Thrift 基于 TTHeader 提供了协议层面真正的多 Service 功能，同时兼容旧的 CombineService。

CombineService 这里做一个简单的介绍，之前为了解决 IDL 过大问题（会导致代码产物大、编译速度慢），Kitex 提供了伪多 Service 的功能 - Combine Service，可以让服务端将一个 IDL Service 拆分为多个 IDL Service，但要求多个 IDL Service 不能有同名的方法（协议上没有支持多 Service，无法做方法路由），最终 Kitex 会将多个 IDL Service 合并为一个 Service，所以称为 CombineService。

Kitex 新增的多 Service 支持，服务端**不仅可以注册多个 IDL Service，且可以****同时提供****Thrift 和 Protobuf 接口**，比如，使用 Kitex-gRPC(Protobuf)，但想切换到 Thrift Streaming，又想保证兼容旧接口的流量，那就可以提供两类 IDL 接口过渡。

如下是服务端注册多 Service 的示例：

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmyfesELbX5N2qDmOVPmqB8APXv9pGFbSzoxvGral1Znx72RDPpEDpBQ/640?wx_fmt=png&from=appmsg)

**新功能****-  Mixed Retry**

Kitex 之前提供了两种重试功能：**异常重试**和 **Backup Request**。异常重试可以提高**成功率**（提升服务的 SLA），但大部分是超时重试，延迟会上涨；Backup Request 可以降低请求**延迟**，但如果有失败的返回，会终止重试。

在内部实践中，业务普遍反馈希望能**同时具备两种重试**的能力，相对前两种重试的优势：

* 可以优化 Failure Retry 的整体重试延迟
* 可以提高 Backup Request 的请求成功率

因此，Kitex 在 v0.11.0 版本中支持了 Mixed Retry，同时具备 Failure Retry 和 Backup Request 功能的混合重试功能。

方便理解三种重试的差异，以下给出一个场景：假设第一次请求耗时 1200ms，第二次请求耗时 900ms，配置 RPCTimeout=1000ms、MaxRetryTimes=2、BackupDelay=200ms。

三种重试的结果对比：

![](https://mmbiz.qpic.cn/mmbiz_png/Jn4sedy3xuFPucD2suPamyAO1u3m7DPmuMvwMdEmX1vsLiaLW0GKAicVbMJTG9gQEAQo8BhudTubPPicjic6dmiaddA/640?wx_fmt=png&from=appmsg)

* Mixed Retry: **S...