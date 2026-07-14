---
title: 腾讯Ray团队实践：K8s + Ray如何支撑超大规模AI Workload
url: https://mp.weixin.qq.com/s/j1pq-Fus3Rr-9ATsIQYKwg
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:35.381802
---

# 腾讯Ray团队实践：K8s + Ray如何支撑超大规模AI Workload

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz906lUYLYVpjGicVeTJibIa1QCHXia2GADwndc8icY0ZwJRLAODibYOLiazmsrYuLc8ic3GCly8kOu0JbBibKVmXKpibkicTDMyFQKicJp3YjHA/0?wx_fmt=jpeg)

# 腾讯Ray团队实践：K8s + Ray如何支撑超大规模AI Workload

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：charliecli

> 随着大模型时代的到来，AI 基础设施（AI Infra）正在经历深刻的变革。面对日益复杂的计算需求，传统上与单一计算范式深度耦合的调度系统已难以应对全局性挑战。本文结合开源社区的演进趋势与工业界的超大规模落地实践，深入探讨 Ray 的技术定位与核心设计逻辑，并阐述它如何与 Kubernetes（以下简称 K8s）进行协同设计（co-design），共同构建大模型时代 AI Workload 调度的通用范式。 注：文章的图片内容来源于腾讯 Ray 团队在 Qcon 全球软件开发大会的分享：
>
>  https://qcon.infoq.cn/2026/beijing/presentation/7002

### 一、 大模型时代 AI 基础设施的技术栈演进

要理解这一全新的调度范式，首先需要审视当前大模型基础设施的技术栈现状。借助蚂蚁开源技术委员会绘制的 AI Infra 开源生态全景图 [1]，我们可以全面了解当下 AI Infra 领域的主要开源项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905LWEc6uHibIUKH7YZ2pMkWYPpnF2R16IeYPWxLMYULelhuOINfb8TMhQLfc7rfr0X8dJ0IuTGwejRGicayWKdxE8uoGNFlg8x7c/640?wx_fmt=png&from=appmsg)

从这张全景图中可以提炼出一条典型的 AI Infra 技术栈：**Ray + PyTorch + vLLM**。值得一提的是，这三个项目目前均隶属于 PyTorch 基金会（其中 Ray 于 2025 年 PyTorch 大会上正式作为托管项目加入）。在此之上，再叠加工业界事实标准的部署与调度底座 **K8s**，便构成了 **K8s + Ray + PyTorch + vLLM** 的黄金组合。这套技术栈贯穿大模型生命周期的全链路，涵盖数据处理、预训练、后训练、在线推理与 Agent 等场景。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907Y04B0fGnnhJia2cag4nS791UJOsBOqmicWGxsjkAyRfn3YlSicxX8ReqUWEVT1LqKQlc8YUbDIaHibIUaAVGlsNEV7Cv5icib1HOYE/640?wx_fmt=png&from=appmsg)

为更直观地理解这套技术栈的运作方式，我们以强化学习（RLHF）为例。当前主流的 RL 训练框架普遍采用"**训推分离**"架构：

* **训练端**：依托 PyTorch 生态（如 Megatron、DeepSpeed）提供高性能训练能力。
* **推理端**：以 vLLM 作为核心推理后端（Backend）。
* **编排与调度**：由 Ray 串联全局，承担训推流程的编排以及角色间的复杂通信。
* **底层基座**：K8s 作为应用部署的事实标准，提供底层物理资源支撑。

目前，业界 90% 以上的 RL 训练框架均构建于这套 K8s + Ray + PyTorch + vLLM 黄金组合之上。关于该组合的深度探讨，可参见四个项目的技术负责人在 Ray Summit 2025 上的对谈 [2]，本文不再赘述。

这套技术栈也已经过开源社区的真实检验。从 2021—2025 年的开源活跃度（以 Commit 数为指标）来看：

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz904sRby5s31xKvMEJv2eibzVzlK1xEjJicibaS17NclL7xKAZmTBPZSg7YZUShVFmssyicXJoFIya3QnbToNZzdMPLowtPXZSHxVZpw/640?wx_fmt=png&from=appmsg)

作为 AI 应用时代最关键的推理引擎，vLLM 在过去一年贡献了超过 8000 个 Commit，活跃度极高；Kubernetes 始终保持极高且稳定的活跃度，与其云原生部署事实标准的地位相称；而 Ray 作为通用计算引擎，活跃度已明显超越 Spark、Flink 等传统大数据计算引擎。

让 Ray 在近两年迎来爆发的，正是它在两类核心场景中的不可替代性：**多模态数据处理** 与 **后训练/强化学习**。下图梳理了基于 Ray 构建的 AI Infra 开源项目，可以看出 Ray 在 **数据处理** 与 **后训练/强化学习** 这两个方向上的生态最为活跃。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz904Aqqdc8tu1ibSdu5DOzyNrfjicFeHzicNYLHykbYuSJd0q6XNuIeiau5mtJqRx4eC0gQJnhe3iadYqibIrDN4FibP4E1e0DD6q2rwRho/640?wx_fmt=png&from=appmsg)

此外，我们也汇总了 Ray 在国内主要企业的落地情况：

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz904Pulxwve4MkqiaicSyKM9yZry2kAxw7gC0YepRVYwk1UL16yVGw9Z6PCfQImibxsribcHpIzkf23GJJAbF4sJic8SPdv1dxEEKh0FE/640?wx_fmt=png&from=appmsg)

如今，国内头部厂商（包括 DeepSeek、月之暗面等）在多模态数据处理上几乎全面采用 Ray；90% 以上的 RL 训练框架基于 Ray 构建；主流云厂商均已提供 Ray 托管服务；阿里等企业也开始探索基于 Ray 构建 Agent Sandbox。在非 AI 场景方面，蚂蚁集团早在 2017—2018 年便已将 Ray 应用于图计算与隐私计算。

接下来，我们将从 AI Workload 调度的视角，深入解析大模型时代的 AI Infra 为何选择 Ray，以及 Ray 究竟解决了哪些传统计算引擎难以应对的调度痛点。

---

### 二、 基于 Ray 的 AI Workload 调度

我们首先通过两个典型场景，归纳当下 AI Workload 提出的调度需求。

#### 1. 多模态数据处理

下图展示了多模态数据处理的典型 Pipeline：系统需要持续读取、处理并输出大批量多模态数据。整条 Pipeline 由多个 Stage 串联组成，其中既包含 CPU 密集型算子（如抽帧、格式转换），也包含强依赖 GPU 的算子（如 OCR、语音识别、大语言模型推理）。所有算子需要在统一的资源池内参与调度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz906vdz2cSF1p84xeNB667VWeQ4gLZdBnAo2MxxgZqxZghPaDzJh62tNHYSoLOh3zxkalfzUwXU84ryYd3cPhicgickePlrmqDb80c/640?wx_fmt=png&from=appmsg)

这带来了三大挑战：

* **异构调度**：CPU 与 GPU 算子需要被高效地匹配到对应的异构节点；
* **动态分配**：需根据实时负载动态调整各 Stage 的资源量与并发度，以打破吞吐瓶颈；
* **高容错**：由于链路长、耗时久，单点故障（如 OOM、GPU Error、Spot Instance 回收）几乎不可避免。因此容错粒度必须下探到 Stage、Pod 乃至进程级，避免单点故障拖垮整条 Pipeline。

#### 2. 强化学习（RLHF）

以 RLHF 中一次典型的 PPO Training Step 为例：用户的 Prompt 经 Actor 推理生成 Response 后，需并发分发给 Reference、Reward 与 Critic 进行打分评估，再经 Advantage 计算回传给 Actor 与 Critic 完成参数更新。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz904rZ84jDtLbloetywiaSB02sT3S4ytJq2medNmtNUEwHEzruZBS2uF3yrG0kNCWOIjXndExQnsS2aGDQYEtZ21t6uiaAYTibURjwM/640?wx_fmt=png&from=appmsg)

这本质上是一个**多异构角色的协同调度问题**。它不仅涉及多种角色（其中 Actor 还可能进一步拆分为训练与推理两部分），而且各角色依赖的运行时完全不同（例如推理需拉起 vLLM/SGLang，训练需加载 FSDP/Megatron），并发设置与资源需求也各不相同。更复杂的是，任务流转并非简单的线性 DAG，而是需要在多角色之间以复杂的多播（multicast）形式传递。

面对后训练/RLHF 中"异构、多角色协同"的调度需求，预训练阶段长期沿用的计算范式变得难以匹配。主流预训练框架（如 FSDP、Megatron）通常采用 **Multi-Controller / SPMD（Single Program, Multiple Data）** 范式，要求每个计算单元运行同构进程，并依赖同步 Barrier 与集合通信。这种范式存在三方面局限：灵活性差（难以表达异构角色）、容错率低（单点故障会导致整个通信组崩溃）、缺少一个能够以全局视角统一编排复杂任务流的中心角色。

为突破这一限制，大模型时代的强化学习框架（ 如 veRL[3]、SkyRL[4] ）纷纷转向 **Single-Controller / MPMD（Multiple Program, Multiple Data）** 范式：引入一个中心 Driver（Single-Controller）来统一编排多个异构角色。Driver 能够以全局视角组织跨角色的复杂任务流；各异构角色内部仍可保留 SPMD 架构以获取局部高性能。借助中心 Driver，异构角色之间得以松耦合，容错也能在角色粒度上独立完成。

#### 3. AI Workload 调度需求小结

基于上述两个典型场景，我们将大模型时代 AI Workload 的调度需求归纳为四点：

* **异构资源**：将异构算子/角色高效地调度到异构节点上
* **动态分配**：根据实时负载，为每个算子/角色动态分配计算资源，避免出现局部吞吐瓶颈
* **高容错**：局部故障不影响全局任务，出错的计算单元支持自动重新调度并恢复状态
* **原生支持 Single-Controller**：由 Single-Controller 统一编排跨角色/跨算子的复杂任务流

#### 4. Ray 核心 API 设计

本节通过 Ray 的核心 API，展示上述四项调度需求如何在 Ray 中被一一满足。下面的 Python 代码片段简要模拟了 RLHF 训推分离场景：

```
import ray

def main():
    # 主函数中声明当前进程为中心 Driver
    ray.init()

    # 定义一个 Rollout 角色 (类），该角色的每个实例需要：
    # 1. 分配 2 个 CPU 和 1 个 GPU
    # 2. 出错后无限次自动重启
    @ray.remote(num_cpus=2, num_gpus=1, max_restarts=-1)
    class RolloutWorker:
        def __init__(self):
            # 如果当前实例为重启状态（非首次创建）
            if ray.get_runtime_context().was_current_actor_reconstructed:
                # 自定义状态恢复行为
                self._recover_state()

        def generate(self, prompt):
            return"Hi there"

    # 定义一个 Trainer 角色（类），该角色的每个实例需要分配 2 个 GPU
    @ray.remote(num_gpus=2)
    class Trainer:
        def fit(self, experience):
            return 0

    # 创建 2 个 RolloutWorker 远程实例，组成 rollout worker group
    rollout_worker_group = [RolloutWorker.remote() for _ in range(2)]

    # 创建 1 个 Trainer 远程实例
    trainer = Trainer.remote()

    # 开始 RL 训练流程
    while True:
        for rollout_worker in rollout_worker_group:
            # 远程调用 (异步) RolloutWorker 实例的 generate 方法
            response = rollout_worker.generate.remote("Hello")
            # 将 RolloutWorker 实例的 response 派发给 Trainer 实例
            ret = trainer.fit.remote(response)

        # 动态增加远程实例（提升 rollout 并发度）
        rollout_worker_group.append(RolloutWorker.remote())
```

在上述代码中，我们首先通过 `ray.init` 将当前进程声明为中心 Driver（**Single-Controller**）。然后通过 `@ray.remote` 装饰器定义**异构**角色（类定义），并声明每个角色实例的**资源**与**容错**需求。对每个角色，我们都可以通过 `remote()` 接口创建任意数量的远程实例（进程），并按需分组管理。在训练循环中，可以调用任意远程实例的方法，并将上游返回值（`ObjectRef`）派发给指定下游实例，从而编排任意形式的任务流。运行过程中也可以**动态**增减角色实例，以调节各角色的并发度。

本质上，Ray 作为分布式计算引擎，其调度的核心对象是"进程级计算单元"。在进程粒度上，Ray 同时实现了 **异构资源调度**、**动态分配** 与 **高容错** 能力。中心 Driver（**Single-Controller**）则可充分利用这些调度能力，灵活编排任务流。

#### 5. 分布式计算引擎对比：调度能力

总结完 AI Workload 的调度需求与 Ray 的对应支持之后，我们进一步将 Ray 与其他主流分布式计算引擎（Spark、Flink、PyTorch）在调度能力上进行对比：

|  | Spark | Flink | PyTorch | Ray |
| --- | --- | --- | --- | --- |
| *计算范式* | BSP（批处理） | 流式 Dataflow | SPMD | 无范式（通用分布式） |
| *异构资源* | 粗粒度（Stage 内同构） | 粗粒度（Slot 切分） | 不支持 | 细粒度（进程级） |
| *动态分配* | 粗粒度（AQE，Stage 间生效） | 支持 | 不支持（静态通信组） | 细粒度（进程级） |
| *容错* | 粗粒度（RDD Lineage 重算） | 粗粒度（Checkpoint 回滚） | 粗粒度（整组重启） | 细粒度（进程级） |
| *Single-Controller* | 支持 | 支持 | 不支持 | 支持 |

从计算范式来看，Spark 绑定了 BSP 批处理，Flink 绑定了流式 Dataflow，PyTorch 绑定了 SPMD；而 Ray 本身是无范式的——基于其提供的进程级计算单元，用户可以根据业务形态自由构建任意计算范式。反过来看，正因为 Spark、Flink、PyTorch 与固定计算范式深度耦合，它们在 **异构资源调度**、**动态分配** 与 **容错能力** 方面均缺乏足够细粒度的支持，难以全面覆盖大模型时代 AI Workload 的多样化需求。

综合来看，Ray 凭借进程级调度的灵活性，成为复杂 AI Workload 调度的最优解。

#### 6. Ray 架构与调度实现

在本章最后，我们简要介绍一下 Ray 的整体架构与调度实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz905VN495Cbia6XqWrAhHOz3QTwcctjiaTrMKV96iahA3jIxTxDiaBw1FVLoNrukj5KticuyJNG7ysMtBGBrWlNxrcx5zl4vvsUURHiaxo/640?wx_fmt=png&from=appmsg)

Ray 集群架构如上图所示。其中，Head 节点上运行 Global Control Store（GCS），负责集群元数据管理与节点状态同步；每个 Worker 节点上运行 Raylet，负责调度决策与本地进程管理。当用户的中心 Driver 创建角色实例时，调度会经历以下流程（实际略有差异，此处仅作示意）：

1. 调度请求首先发送至本地 Raylet，由其做出调度决策，选择目标节点
2. 调度请求被转发至目标节点的 Raylet
3. 目标节点 Raylet 根据本地资源状...