---
title: 观测成本如何优化？APMPlus 尾采样技术的降本增效实践
url: https://mp.weixin.qq.com/s/M7HmYlOS27aH2mTPWk2rTA
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:24:38.964930
---

# 观测成本如何优化？APMPlus 尾采样技术的降本增效实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjFXb7uaGd2UeBbteiabfqvcqKmZkrQ6WfUxuRVUVib7Jvsxw8iazJwbEDJPcYA2JNjgmolkET0OicBiag/0?wx_fmt=jpeg)

# 观测成本如何优化？APMPlus 尾采样技术的降本增效实践

原创

火山引擎可观测
火山引擎可观测

字节跳动技术团队

![]()

在小说阅读器中沉浸阅读

# 前言

在现代软件工程架构实践中，工程师普遍面临一个挑战：如何在海量的请求中精确捕捉异常链路，同时避免数据成本的快速增长。

本文将探讨分布式链路追踪（Distributed Tracing）中的采样（Sampling）技术，并介绍火山引擎 APMPlus 团队在尾采样（Tail-based Sampling）方面的技术实践，以期为解决上述挑战提供一种思路。

# 困境：链路追踪与 R.E.D 指标的矛盾

在微服务环境中，一次用户请求可能触发后台数十个服务的级联调用。为了掌握请求的全过程，分布式链路追踪技术被广泛采用。一次完整的请求链路（Trace）由多个服务站点和内部方法调用（Span）组成，所有 Span 串联起来，便构成了完整的 Trace 路径。

Trace 数据可用于计算衡量服务健康度的三大核心指标——**R.E.D 指标：**

* **R (Rate):** 每秒请求数，即吞吐量。
* **E (Errors):** 每秒错误请求数。
* **D (Duration):** 请求耗时分布，如 P95、P99 延迟。

在 OpenTelemetry 生态中，这些指标通常通过分析全量的 Span 数据生成。例如，`SpanMetricsConnector` 负责统计 Span 的数量、错误状态和耗时，从而计算出 R.E.D 指标。然而，为了保证指标的绝对准确性，理论上需要采集 100% 的 Trace 数据，这在高并发场景下会带来巨大的网络、计算和存储开销。为控制成本，必须进行采样，只保留部分代表性 Trace。

最常见的采样方法是**头采样（Head-based Sampling）**。该方法在链路的第一个 Span（Root Span）产生时，依据固定概率（如 1%）决定该 Trace 的所有后续 Span 是否被采集。这种方法简单直接，但存在明显缺陷：

1. **指标失真：** 如果仅采样 1% 的数据，再通过乘以 100 的方式推算总体指标，那么低概率出现的错误和慢请求 Trace 很容易在采样过程中被忽略。最终得到的指标可能无法真实反映服务的整体状况。
2. **错失关键问题现场：** 一个请求在开始阶段可能表现正常，但在链路末端因下游服务超时而失败。在头采样机制下，这条异常 Trace 很可能在初始阶段就被判定为“无需采集”，导致定位问题的关键线索丢失。

如何在确保 R.E.D 指标准确性、精准捕获异常链路的同时，有效控制数据采集成本，成为一个待解的难题。尾采样（Tail-based Sampling）则提供了一种新的解决思路，它允许在链路结束后，根据完整的 Trace 信息再决定是否保留。

# APMPlus 尾采样技术实践方案

尾采样是一种“先收集，后决策”的策略。它会等待一条 Trace 上的所有（或绝大部分）Span 都生成完毕，然后基于完整的链路信息，例如是否包含错误、总耗时是否超标、是否命中了特定的业务标签等，来做出采样决策。

以下将介绍 APMPlus 内部该机制的设计与实现。

**数据处理主流程**

---

在 APMPlus 中，O11yAgent 是观测数据的核心采集组件。在火山引擎的 VKE（容器服务）环境中，它由两部分组成：

* **O11yAgent Operator:** 负责应用的自动插桩、配置动态更新、版本升级和弹性伸缩。
* **O11yAgent Collector:** 作为数据处理中心，负责接收、处理和转发 APM 数据。

所有应用产生的 Traces、Metrics、Logs 数据都会汇聚到 Collector。Trace 数据除了被正常处理外，还会通过 `SpanToMetrics` 组件实时转换为 Metrics 数据。此设计确保了无论后续采样策略如何，总能基于全量数据计算出准确的 R.E.D 指标。处理流程如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjFXb7uaGd2UeBbteiabfqvcNwAwmWVl0EbU8ialAepCibgvo5oJRBJ7xiaqY8rQKuX70ruzsN7W6OaPw/640?wx_fmt=png&from=appmsg)

该设计的优势在于将指标计算与 Trace 采样解耦，先确保获取准确的全局指标，再决定哪些 Trace 细节值得保留以供深入分析。

**尾采样的基础：汇聚同一 Trace 的所有 Span**

---

尾采样面临的核心挑战是：在分布式环境下，一条 Trace 的不同 Span 可能产生于不同服务的不同 Pod 上，并被不同的 Collector 实例接收。为了对整条 Trace 进行统一决策，必须将这些 Span 聚合在一起。

我们的解决方案是基于 **TraceId 的一致性哈希路由**。当一个 Collector 实例收到一批 Span 后，它会根据每个 Span 的 `TraceId` 计算哈希值，并将该值映射到一个一致性哈希环上的特定节点（即另一个 Collector 实例的 PodIP）。然后，它会将这批 Span 转发给负责处理该 TraceId 的 Collector。通过这种方式，同一条 Trace 的所有 Span 最终都会在同一个 Collector 实例上汇合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjFXb7uaGd2UeBbteiabfqvcDFjTNsU52jKhzHnVj7VciaYW0uiaiauyrLvpibOgoAnbbKtGCRztepCJDQ/640?wx_fmt=png&from=appmsg)![]()

在 K8s 环境下，Pod 的 IP 会动态变化。Collector 通过 ListAndWatch 机制实时感知集群中其他 Collector 节点的增删，动态维护一致性哈希环，从而保证了路由的健壮性。

**采样决策：多级与组合策略**

---

当一个 Collector 收集完一条 Trace 的所有 Span 后，便进入采样决策阶段。在实际业务中，采样需求是多维度的：

* **全局策略：** 希望对所有链路保留 0.1% 的样本。
* **环境策略：** 生产环境（prod）的采样率需要低于测试环境（staging）。
* **服务策略：** 核心服务（如：订单服务）需要 100% 采集所有错误和慢请求。

为满足这些复杂需求，我们设计了**多级采样**机制。用户可以定义多个采样策略，并为其设置**优先级**和**匹配规则**。当一条 Trace 等待决策时，系统会：

1. 按优先级从高到低遍历所有采样策略。
2. 检查 Trace 的属性（如 `service.name`, `env` 等）是否满足当前策略的 `MatchRule`。
3. 一旦匹配成功，则执行该策略，并**停止后续匹配**。
4. 如果所有策略都不匹配，或 Trace 等待超时，则执行一个全局的默认策略。

以下是一个包含多级采样的配置示例：

```
Samplers:
# 全局采样
  - Policies:
      - Type: probabilistic
        SamplingPercentage: 0.1
    Priority: 3
# 环境采样
  - Policies:
      - Type: probabilistic
        SamplingPercentage: 1
    Priority: 2
    MatchRule:
      env: product
# 服务采样
  - Policies:
      - Type: probabilistic
        SamplingPercentage: 100
    Priority: 1
    MatchRule:
      service.name: order
```

此外，每个策略内部都可以是一个**组合策略**。目前支持：

* **Span状态采样 (status\_code)：** 捕获所有包含错误Span的 Trace。
* **耗时采样 (latency)：** 捕获所有总耗时超过阈值的 Trace。
* **概率采样 (probabilistic)：** 按固定比例随机采样。
* **全采样 (always\_sample)：** 100% 采集。

这些策略可以任意组合。一个典型的配置是：“采集所有错误 Trace，或所有慢 Trace，或 1% 的正常 Trace”。只要满足任意一个条件，该 Trace 就会被保留。

下面是一个 YAML 配置示例，展示了组合策略的结构：

```
Samplers:
  - Policies:
      - Type: status_code
        StatusCodes: ["ERROR"] # 采集所有错误链路
      - Type: latency
        ThresholdMs: 1000 # 采集耗时超过 1s 的链路
      - Type: probabilistic
        SamplingPercentage: 5 # 对剩余的采样 5%
```

**性能与资源优化**

---

尾采样需要缓存 Span 并等待 Trace 结束，这会消耗内存和 CPU。为应对此挑战，我们实施了一系列优化措施，目标是在多数场景下将资源开销控制在与不采样时相近的水平。

1. **决策前置 (Decision Preponement):** 在同步调用场景下，Root Span 通常是最后一个到达 Collector 的。一旦收到 Root Span，即可认为该 Trace 的主干部分已完整，此时便可立即进行采样决策，无需等待超时窗口（例如 30 秒）结束，从而显著减少 Span 在内存中的缓存时间。
2. **快速采样 (Fast Sampling):** 如果采样策略中只包含“概率采样”，处理流程可以简化。由于概率采样的哈希算法（使用 FNV）对同一 TraceId 多次计算的结果是确定的，因此无需缓存 Span。每当一批 Span 到达时，直接对每个 TraceId 进行哈希计算，即可确定其是否应被采样，然后直接发送至下一处理环节。此模式下，资源开销极低。
3. **采样结果缓存 (Decision Caching):** 如果一条 Trace 因包含错误 Span 而被决策为“采样”，我们会缓存该决策结果（`TraceId -> Sampled`）。当后续属于该 Trace 的异步 Span 或因网络延迟而“迟到”的 Span 到达时，系统可直接根据缓存结果进行处理，无需重复执行决策逻辑。这既保证了链路的完整性，也避免了不必要的计算开销。

**尾采样的可观测性：实现决策过程监控**

---

为了避免尾采样系统成为一个不易排查问题的“黑盒”，我们在采样器的每个关键环节都嵌入了监控指标，例如：

* 接收/丢弃/采样/转发的 Span 数量
* 当前缓存中的 Trace 数量
* 采样决策的次数和耗时分布
* 每个采样策略的命中次数

通过这些指标，我们可以清晰地了解尾采样器的工作状态，从而快速定位“Trace 未被采集”等问题。

# 性能与资源开销实测

我们在受控环境（4核 CPU, 4GB 内存）下对尾采样能力进行了性能压测。结果如下：

| 测试用例 (10k spans/s) | CPU 平均使用率 (%) | 内存平均使用率 (MB) |
| --- | --- | --- |
| 基线：不开启采样 | 9.5 | 2205.6 |
| 概率采样 (50%) | 9.0 | 2212.7 |
| 概率采样 (100%) | 10.9 | 2410.5 |
| 状态码采样 (仅 ERROR) | 8.2 | 1992.1 |
| 延迟采样 (阈值 > 1s) | 8.1 | 1991.5 |
| 高负载基线：不开启采样 (200k spans/s) | 75.6 | 3016.5 |
| 高负载：概率采样 (50%) | 76.2 | 3019.1 |
| 高负载：概率采样 (100%) | 86.9 | 3019.5 |

测试结论：

* **开销可控：** 在常规负载下，启用尾采样带来的额外资源开销很小。在某些场景下（如仅进行状态码采样），由于提前丢弃了大量正常数据，其资源消耗甚至低于不采样的基线。
* **智能策略效率高：** 精准采样策略（如“只采集错误或慢请求”）在大部分请求正常的情况下，几乎不增加额外负担，可以用较低成本捕获高价值的异常信息。
* **高负载下表现稳定：** 在 200k spans/s 的高压场景下，尾采样系统表现稳定，内存占用保持平稳，证明了相关优化措施在控制缓存大小和防止内存泄漏方面的有效性。

# 落地实践思考

* **尾采样的适用边界：** 尾采样能显著提升捕获关键 Trace 的能力，但它并非适用于所有场景。对于包含大量 Span（例如数万个）的超长链路，尾采样可能带来的内存压力仍需进行评估。
* **头采样与尾采样的结合：** 在某些流量极高的边缘服务上，可以考虑采用“头采样+尾采样”的二级采样架构。在最前端通过头采样削减大部分流量（例如，保留10%），然后再对这10%的数据进行精细化的尾采样。

# 结语

回到最初的问题：如何在保障 R.E.D 指标准确性、提升问题定位效率与控制资源开销之间取得平衡？

APMPlus 的尾采样实践为此提供了一种解决方案。它通过“先计算指标、后智能采样”的模式，在保留100%的错误、慢速等高价值链路的同时，将无效数据的采集成本降至较低水平。该方案已在火山引擎内部及多个外部客户的生产环境中得到应用，在提升问题排查效率和成本节约方面取得了实际效果。

以尾采样为代表的智能采样技术，是未来大规模分布式系统可观测性体系中的一个重要发展方向。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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