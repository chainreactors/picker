---
title: 干货 | 200G内存尖峰、数十万Pod迁移：携程Karmada规模化治理实录
url: https://mp.weixin.qq.com/s/bMt3ZP3-oqQzZr2ihdC6xA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:03:05.777473
---

# 干货 | 200G内存尖峰、数十万Pod迁移：携程Karmada规模化治理实录

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/h6WFQibcNiae4orjS9ibkb3GGG18lxsrc6Z9XibrhcKexmdlYdibmoLk8kE0oL0sxan0jcaXouE7BK7zGx8wvmdqlj5jsjibPWfQBeckxF038micJ4/0?wx_fmt=jpeg)

# 干货 | 200G内存尖峰、数十万Pod迁移：携程Karmada规模化治理实录

原创

扎克
扎克

携程技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**作者简介**

扎克，携程资深云原生研发工程师。长期关注 Kubernetes 多集群、弹性调度与控制面稳定性建设，深耕复杂基础设施系统在真实业务流量下的落地与演进。

导读：多集群治理并不只是把应用分发到多个 Kubernetes 集群这么简单。

在大型在线业务场景下，基础设施平台既要统一分发资源，又要在容量变化、集群拆分、故障切换和基础组件交付过程中保持足够稳定。尤其是交易型业务，对弹性、可用性和变更平滑度都有很高要求：联邦控制面不能成为运行时强依赖，也不能在规模扩大后成为新的性能瓶颈。

携程很早就开始了 Kubernetes 集群联邦实践。早期，我们主要使用 Kubefed 解决跨集群资源同步和统一管理问题。随着业务规模增长，多集群逐步从“资源分发”走向“生产调度与规模化治理”，平台侧需要更主动地控制应用跨集群分布，并在容量变化或异常场景下完成平滑调整。

在这个过程中，我们逐步引入 Karmada，并将其作为新一代多集群联邦控制面的基础。如今，Karmada 已在携程用于多集群高可用、跨集群迁移以及基础组件统一交付等场景：累计完成数十万个 Pod 迁移，并将新集群 baseline 组件的初始化时间从数天缩短到数小时。

本文会围绕三个层面展开：

* 架构演进：为什么从 Kubefed 走向 Karmada，原有联邦模型在哪些生产场景下遇到边界；
* 生产落地：如何支撑多集群高可用、跨集群平滑迁移和新集群基线组件初始化；
* 规模化治理：几十万级资源规模下，如何优化控制面状态同步、启动成本、内存压力和策略权限边界。

一、为什么从 Kubefed 走向 Karmada

二、Karmada 在携程的生产落地

三、规模化使用中的问题与优化

四、后续方向

# **一、为什么从 Kubefed 走向****Karmada**

# **在携程早期的集群联邦实践中，Kubefed 承担了部分资源联邦分发和多集群管理职责。它当时主要承担跨集群资源同步和统一管理的工作，也支撑了早期联邦能力建设。**

# **但随着多集群场景从简单资源分发扩展到容量调度、应用迁移和弹性治理，平台侧对联邦能力的要求发生了变化。Kubefed 的模型开始暴露出一些局限。**

# **1.1 资源模型引入额外适配成本**

# **Kubefed 通过 FederatedDeployment、FederatedConfigMap 等 federated 对象描述联邦资**源。原生 Kubernetes 资源需要被转换成对应的 federated 资源后，才能参与多集群分发。

# 这会带来额外的模型适配成本。原有围绕 Kubernetes 原生对象构建的发布、审计、运维链路，以及平台侧基于原生资源扩展的增强能力，都需要做相应改造。对于已经沉淀了大量 Kubernetes 原生能力的平台来说，这类改造成本并不低。

# 1.2 平台策略与业务配置耦合

# 在 Kubefed 模型中，业务资源定义、分发策略和集群差异配置往往集中在同一个 federated 对象中。

# 当平台侧需要调整调度策略时，通常只能通过修改 federated workload 实现，而这类对象又通常由业务侧维护。这会增加变更成本，也不利于平台侧统一治理。随着多团队、多集群共用同一套联邦能力，这种耦合会进一步放大协作复杂度。

# 1.3 缺少控制实例分布的上游入口

# 在携程的联邦 HPA 场景中，成员集群必须保留本地扩缩容能力。扩缩容是高频核心链路，不能强依赖联邦控制面；否则一旦联邦控制面不可用，业务应用的自动扩缩容也会受到影响。因此，我们将实时扩缩容保留在成员集群内，由各成员集群 HPA 根据本地指标独立完成；联邦层则用于表达资源分发策略和跨集群调度意图。

# 在携程旧有的 Kubefed 体系中，各成员集群可以独立扩缩容，但联邦层只能把当前副本结果记录回 federated workload。这能反映现状，却不方便表达平台侧的分布目标。比如管理员希望应用实例在两个集群中的比例按 3:7 分布时，Kubefed 缺少类似 weight 的配置入口。

# 基于以上原因，我们开始采用 Karmada 作为新一代多集群联邦控制面的基础。

# 与 Kubefed 不同，Karmada 并不是通过为每类资源重新定义 federated 对象来完成分发，而是尽量保持原生 Kubernetes 资源不变，并将业务对象、平台策略和调度结果拆开管理。

# 业务资源仍以 Deployment、Service、ConfigMap、HPA 等原生 Kubernetes 对象存在；平台侧通过 PropagationPolicy、OverridePolicy 等策略对象描述分发范围、分布权重和集群差异配置。这样，业务对象不需要为了联邦分发改变形态，平台侧也可以在业务对象之外独立表达调度策略。

# 对于携程需要控制实例分布、进行跨集群 Rebalance 的业务场景，Karmada 也提供了更明确的策略入口，例如通过 weight 描述应用在不同集群之间的目标分布。

# 二、**Karmada****在携程的生产落地**

**引入 Karmada 之后，它最早承担的是资源分发入口，后来逐渐覆盖到多集群高可用、跨集群迁移和基础组件交付等场景。**

**我们在架构设计中始终坚持一个核心原则：**

> 低频、全局、跨集群的能力放在联邦层；高频、局部、运行时强依赖的能力保留在成员集群内。

这条边界决定了 Karmada 在携程生产环境中的角色：它负责全局策略、资源分发、状态聚合和跨集群调度意图，但不直接接管实时流量决策和成员集群内的实时扩缩容链路。

2.1 韧性优先的多集群高可用架构

携程有大量交易型业务，流量高峰明显，容量需求也具有很强的弹性。对这类业务来说，多集群架构不能只解决“资源分发到哪里”的问题，还必须保证故障发生时业务可以快速恢复。

具体来说，我们会将无状态应用部署到多个成员集群中，每个成员集群都运行独立的 HPA 组件。正常情况下，各集群根据本地指标独立完成扩缩容。当某个承载线上流量的成员集群发生故障时，流量侧会基于实例健康状态摘除故障集群中的实例，并自动切换到其他健康集群；同时，健康集群中的 HPA 被触发扩容，完成自愈过程。

![](https://mmecoa.qpic.cn/mmecoa_png/h6WFQibcNiae72ZxF2392jr1oLQ3IYLY4iaia4LSdUalmagPG82kJJJkOeUgpUL2V2G4UsBN1b37ibNF60K0sDkn9ic1mtnbrqe1iayQ0uR1Dfa9Hs/640?wx_fmt=png&from=appmsg)

在这个架构中，Karmada 负责分发应用资源和 HPA 对象，联邦层控制器负责状态聚合和 Rebalance 计算，但不直接接管实时流量决策和成员集群内的实时扩缩容。即使 Karmada 控制面短时间不可用，也只会影响应用更新和自动 Rebalance，不会影响已经运行服务的流量切换和本地 HPA 扩缩容能力。

这也是我们在生产中非常看重的一点：联邦层需要足够可靠，但核心运行链路不应该把它作为实时强依赖。当前内部设计允许联邦控制面达到小时级别不可用，因为核心服务运行、流量切换和成员集群内扩缩容都不依赖联邦层的实时可用。

这样的架构让故障影响面可以被限制在单个成员集群内，也让核心服务具备更强的高可用和容灾能力。

2.2 权重驱动的平滑跨集群迁移

随着业务规模快速增长，我们的部分 Kubernetes 集群曾经达到 5000 个节点以上。单集群规模继续扩大后，容量、运维和故障隔离都会遇到边界。因此，我们经常需要拆分集群，把应用逐步迁移到新的集群中。

过去，这类迁移缺少管理员侧的统一能力，往往需要业务负责人通过重新发布应用来触发迁移。这个过程既耗时，也会增加业务侧的理解和操作成本。

在 Karmada 体系下，我们在联邦层引入自研 fed-hpa-controller 和 Rebalance 状态机，用于聚合各成员集群的副本状态，并在迁移过程中按灰度批次推进实例分布调整。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/h6WFQibcNiae4iaibvLibniam39MIzs0mFBkIZT1p94PicLdic7uv6L0zQq7kICa35pibKX25e322cXmJ5ojgGXm6v71rFIZkWBn950XpW1kHa3Hgj1Y/640?wx_fmt=png&from=appmsg)

管理员可以通过 PropagationPolicy 中的 weight 声明应用在不同集群之间的目标分布比例，状态机会根据目标权重自动推进迁移。在生产操作中，目标权重也可以按阶段设置，用于控制整体迁移节奏。

对于使用 HPA 的 workload，fed-hpa-controller 会结合 PropagationPolicy 中的 weight、各成员集群的实际副本数，以及 HPA 的扩缩容约束，驱动状态机计算每一批 Rebalance 的目标。

执行时，状态机会优先扩容目标集群，使整体副本数在短时间内高于实际负载需求；随后源集群实例的平均负载就会下降，并由源集群本地 HPA 按缩容策略自然缩容。迁移节奏会与 HPA 的缩容稳定窗口对齐，避免副本数在集群之间来回抖动。

对于不具备 HPA 的 workload，我们也在内部版本的 resourcebinding-controller 中补充了灰度控制逻辑，由控制器按固定步进自动推进副本分布调整。这样，跨集群平滑迁移能力不再局限于 HPA 场景。

如果迁移过程中需要回退，也可以通过恢复上一版本 weight 触发反向 Rebalance，或者中止 Rebalance 后将期望状态重新对齐当前实际分布。

目前，这套机制已经支撑我们在多个集群之间完成了大规模迁移，累计涉及超过数十万个 Pod。

2.3 基础组件统一分发：从数天到数小时

在多集群体系中，新集群创建完成并不意味着可以立刻承载业务。一个 Kubernetes 集群真正进入可用状态之前，还需要完成一组 baseline 组件的安装和初始化，包括网络、监控、日志、RBAC、Operator、平台插件以及其他支撑资源。

这些组件数量多、来源分散，并且存在明确的依赖关系：有些组件必须先就绪，后续组件才能继续安装。

在引入 Karmada 之前，这部分工作通常需要多个团队分别处理。不同团队维护各自的配置和发布流程，初始化过程中既要关注安装顺序，也要反复确认配置一致性。一次新集群交付往往需要持续数天。

引入 Karmada 后，我们将基础组件分发收敛到统一入口。管理员只需要在控制面声明目标集群和分发策略，后续组件分发过程就可以自动推进。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/h6WFQibcNiae4R58S5rUXEfscRmiaCONepNhL0y8tOnJ0iaHGM4klzWqIjo71n5Kuhia8LIweFEDvIWAiaX5vkQca7HH5YWqGuicV2CxYWn7ole77s/640?wx_fmt=png&from=appmsg)

具体来说，组件之间的依赖和安装顺序由上层的 Trip Cluster Components Controller 负责编排。当前置组件就绪后，上层控制器再将后置组件纳入 Karmada 的分发范围，并通过 PropagationPolicy 下发到目标集群。Karmada 负责资源分发和状态保持，资源下发到成员集群后，继续按照 Kubernetes 原生方式运行。

目前，这套能力已经覆盖数十个集群，新集群 baseline 初始化时间也从原来的数天缩短到数小时内，这让新集群从创建完成到具备业务承载能力的周期大幅缩短，也减少了扩容高峰期对多个团队串行配合的依赖。

三、规模化使用中的问题与优化

随着 Karmada 覆盖的集群和资源数量不断增加，我们遇到的问题也从“能力是否可用”逐渐转向“控制面能否在更大规模下稳定运行”。

这些问题主要集中在三个方面：控制面高频状态同步、控制器启动成本、单实例内存压力。此外，多团队共用控制面后，策略权限边界也需要额外治理。

3.1 高频状态同步带来的控制面压力

Karmada 标准分发链路中，Work 是面向成员集群的资源载体，与成员集群对象存在 1:1 的映射关系；早期我们的 fed-hpa-controller 也沿用了 Work 进行分发。

在 HPA 场景中，成员集群中的副本数、HPA status、ready pod 数量等状态会持续频繁变化。如果这些运行时状态都沿着联邦链路同步回 Karmada 控制面，Work 就会从资源分发载体变成高频更新对象。

在生产中，这类高频更新曾经带来明显的控制面压力。部分场景下，Karmada 控制面中对应 Work 资源的更新频率可以达到每秒数百次。频繁读写会推动 etcd db size 增长，进而引发写入延迟劣化；Work 更新过快也会导致 karmada-controller-manager 的 informer cache 长时间滞后，进而出现大量 409 冲突。冲突后的重试又会继续放大整体负载，形成正反馈。

针对这类问题，我们的优化思路是缩短高频链路，减少不必要的控制面写入：

* 在内部版本 Karmada 中，弃用 Work 资源，将 Work 相关逻辑折叠进 resourcebinding-controller 和 fed-hpa-controller，避免每一次运行时状态变化都转化为 Work 更新；
* 降低 HPA status 更新频率，减少联邦控制面的状态写入频率；
* 对 watch event 做 batch 和去重，例如在短时间窗口内合并同一个对象的多次事件，减少 reconciliation 触发；
* 升级 etcd 到 3.4，降低 db size 增长后对写入性能的影响。

3.2 启动成本随资源规模放大

karmada-controller-manager 启动时，需要先通过 List/Watch 建立控制面对象和成员集群对象的 informer cache。资源规模越大，首次 List 进行 cache 同步和存量对象入队处理的耗时就越长。在滚动发布或重启 controller 时，这部分启动成本会直接传导为业务用户感知到的发布延迟。

这里的延迟主要来自三部分。

第一，List 本身会随着对象数量增长而变慢，informer cache 同步时间随之变长，会延长 controller 新实例就绪所需时间。

第二，如果 List 时间超过 kube-apiserver watch cache 能覆盖的时间窗口，后续 Watch 就容易出现 too old resource version，触发重新 List，并伴随 409 冲突和重试，进一步放大同步成本。

第三，存量对象进入队列后仍然需要 controller 逐个处理。worker 并发、client QPS 和单次 reconcile 成本都不可能随资源量无限增长，因此资源量上来后，存量队列清空本身也会成为发布链路中的耗时点。

对此，我们主要做了几类优化：

* 启动阶段预加载 informer，等待 cache 同步完成后再上报 ready 并参与选主，从而在滚动更新过程中保留旧实例继续处理事件，降低新旧实例切换时的感知影响；
* 调整 kube-apiserver watch cache 时间窗口，避免 too old resource version 错误。（在社区版本 v1.33 起可通过 --request-timeout 参数调整）
* 对存量对象对账和新增变更事件区分优先级，引入优先级队列，优先处理新增和变更事件，将存量对象对账放到最后，降低业务用户的可感知延迟；
* 写入前增加 deepEqual check，跳过无变化对象，减少无效 update 对 HTTP 请求 QPS 的占用，加快存量对账速度。

3.3 karmada-controller-manager 内存压力

随着纳管资源数量增加，karmada-controller-manager 的内存压力也会变得明显。内存占用主要来自几类对象和过程：

* 需要 Karmada 进行分发的资源；
* Karmada 控制面资源，例如 Work、ResourceBinding、PropagationPolicy、OverridePolicy；
* 成员集群被纳管对象的 informer cache，且不仅包括被纳管对象，还包括该类别在成员集群的所有资源；
* List/Watch 过程中的对象反序列化。

在大规模下，启动或 cache 重建阶段的瞬时内存峰值会明显高于常态。尤其是在 dynamic informer 和 unstructured 对象路径中，数据从 JSON 字节流反序列化为 unstructured 对象进入 informer cache，会带来较高的对象化成本。

当前线上较大规模下，Karmada 纳管资源量已经达到几十万级，karmada-controller-manager 在控制面启动时内存尖峰可达 200G。压测也表明，资源规模继续翻倍甚至数倍增长后，单实例内存会成为更明确的容量边界。

当前可优先利用 watch list 相关能力。我们在基于 Kubernetes 1.36 的环境中验证后，观察到该能力可将启动时内存尖峰降低约 15%。

此外，还有一些方向后续会继续评估：

* 使用 CBORServingAndStorage feature gate，进一步降低传输以及编解码开销；
* 对成员集群 informer 中冷数据使用 metadata informer，减少完整对象缓存；
* 对类型固定、字段访问稳定的对象使用 typed informer，降低 unstructured 带来的编解码和内存开销；
* 对部分大对象链路探索 bytes cache，减少不必要的编解码和 unstructured 对象化成本；
* controller 分片，避免单进程承载过多对象。

## **3.4 策略权...