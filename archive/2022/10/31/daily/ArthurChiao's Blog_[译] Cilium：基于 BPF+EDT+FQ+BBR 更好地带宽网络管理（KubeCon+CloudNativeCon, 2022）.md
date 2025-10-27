---
title: [译] Cilium：基于 BPF+EDT+FQ+BBR 更好地带宽网络管理（KubeCon+CloudNativeCon, 2022）
url: https://arthurchiao.github.io/blog/better-bandwidth-management-with-ebpf-zh/
source: ArthurChiao's Blog
date: 2022-10-31
fetch_date: 2025-10-03T21:20:36.946740
---

# [译] Cilium：基于 BPF+EDT+FQ+BBR 更好地带宽网络管理（KubeCon+CloudNativeCon, 2022）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译] Cilium：基于 BPF+EDT+FQ+BBR 实现更好的带宽管理（KubeCon, 2022）

Published at 2022-10-30 | Last Update 2023-02-11

### 译者序

本文翻译自 KubeCon+CloudNativeCon Europe 2022 的一篇分享：
[Better Bandwidth Management with eBPF](https://kccnceu2022.sched.com/event/ytsQ/better-bandwidth-management-with-ebpf-daniel-borkmann-christopher-m-luciano-isovalent)。

作者 Daniel Borkmann, Christopher, Nikolay 都来自 Isovalent（Cilium 母公司）。
翻译时补充了一些背景知识、代码片段和链接，以方便理解。

翻译已获得 Daniel 授权。

**由于译者水平有限，本文不免存在遗漏或错误之处。如有疑问，请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [1 问题描述](#1-问题描述)
  + [1.1 容器部署密度与（CPU、内存）资源管理](#11-容器部署密度与cpu内存资源管理)
  + [1.2 网络资源管理：带宽控制模型](#12-网络资源管理带宽控制模型)
  + [1.3 K8s 中的 pod 带宽管理](#13-k8s-中的-pod-带宽管理)
    - [1.3.1 Bandwidth meta plugin](#131-bandwidth-meta-plugin)
    - [1.3.2 入向（ingress）限速存在的问题](#132-入向ingress限速存在的问题)
    - [1.3.3 出向（egress）限速存在的问题](#133-出向egress限速存在的问题)
    - [1.3.4 Bandwidth meta plugin 问题总结](#134-bandwidth-meta-plugin-问题总结)
* [2 解决思路](#2-解决思路)
  + [2.1 回归源头：TCP “尽可能快”发送模型存在的缺陷](#21-回归源头tcp-尽可能快发送模型存在的缺陷)
  + [2.2 思路转变：不再基于排队（queue），而是基于时间戳（EDT）](#22-思路转变不再基于排队queue而是基于时间戳edt)
  + [2.3 3 EDT/timing-wheel 应用到 K8s](#23-3-edttiming-wheel-应用到-k8s)
* [3 Cilium 原生 pod 限速方案](#3-cilium-原生-pod-限速方案)
  + [3.1 整体设计：基于 BPF+EDT 实现容器限速](#31-整体设计基于-bpfedt-实现容器限速)
  + [3.2 工作流程](#32-工作流程)
  + [3.3 数据包处理过程](#33-数据包处理过程)
  + [3.4 性能对比：Cilium vs. Bandwidth meta plugin](#34-性能对比cilium-vs-bandwidth-meta-plugin)
  + [3.4 小结](#34-小结)
* [4 公网传输：Cilium 基于 BBR 的带宽管理](#4-公网传输cilium-基于-bbr-的带宽管理)
  + [4.1 BBR 基础](#41-bbr-基础)
    - [4.1.1 设计初衷](#411-设计初衷)
    - [4.1.2 性能对比：bbr vs. cubic](#412-性能对比bbr-vs-cubic)
  + [4.2 BBR + K8s/Cilium](#42-bbr--k8scilium)
    - [4.2.1 存在的问题：跨 netns 时，`skb->tstamp` 被重置](#421-存在的问题跨-netns-时skb-tstamp-被重置)
    - [4.2.2 为什么被重置](#422-为什么被重置)
    - [4.2.3 能将 `skb->tstamp` 统一到同一种时钟吗？](#423-能将-skb-tstamp-统一到同一种时钟吗)
    - [4.2.4 解决](#424-解决)
  + [4.3 Demo（略）](#43-demo略)
  + [4.4 BBR 使用注意事项](#44-bbr-使用注意事项)
* [5 总结及致谢](#5-总结及致谢)
  + [5.1 问题回顾与总结](#51-问题回顾与总结)
  + [5.2 致谢](#52-致谢)
* [6 Cilium 限速方案存在的问题（译注）](#6-cilium-限速方案存在的问题译注)

---

# 1 问题描述

## 1.1 容器部署密度与（CPU、内存）资源管理

下面两张图来自 Sysdig 2022 的一份调研报告，

![](/assets/img/better-bw-manage-with-ebpf/container-usage-trends.png)

Source: Sysdig 2022 Cloud Native Security and Usage Report

1. 左图是容器的**部署密度分布**，比如 33% 的 k8s 用户中，每个 node 上平均会部署 16~25 个 Pod；
2. 右图是**每台宿主机上的容器中位数**，可以看到过去几年明显在不断增长。

这两个图说明：容器的部署密度越来越高。这导致的 CPU、内存等**资源竞争将更加激烈**，
如何管理资源的分配或配额就越来越重要。具体到 CPU 和 memory 这两种资源，
K8s 提供了 **resource requests/limits** 机制，用户或管理员可以指定一个
Pod **需要用到的资源量（requests）**和**最大能用的资源量（limits）**，

```
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: nginx-slim:0.8
    resources:
      requests:         # 容器需要的资源量，kubelet 会将 pod 调度到剩余资源大于这些声明的 node 上去
        memory: "64Mi"
        cpu: "250m"
      limits:           # 容器能使用的硬性上限（hard limit），超过这个阈值容器就会被 OOM kill
        memory: "128Mi"
        cpu: "500m"
```

* `kube-scheduler` 会将 pod 调度到能满足 `resource.requests` 声明的资源需求的 node 上；
* 如果 pod 运行之后使用的内存超过了 memory limits，就会被操作系统以 OOM （Out Of Memory）为由干掉。

这种针对 CPU 和 memory 的资源管理机制还是不错的，
那么，**网络方面有没有类似的机制呢**？

## 1.2 网络资源管理：带宽控制模型

先回顾下基础的网络知识。
下图是往返时延（Round-Trip）与 TCP 拥塞控制效果之间的关系，

![](/assets/img/better-bw-manage-with-ebpf/tcp-cc-states.png)

结合
[流量控制（TC）五十年：从基于缓冲队列（Queue）到基于时间戳（EDT）的演进（Google, 2018）](/blog/traffic-control-from-queue-to-edt-zh/)，
这里只做几点说明：

1. TCP 的发送模型是**尽可能快**（As Fast As Possible, AFAP）
2. 网络流量主要是靠**网络设备上的出向队列**（device output queue）做**整形**（shaping）
3. **队列长度**（queue length）和**接收窗口**（receive window）决定了传输中的数据速率（in-flight rate）
4. “多快”（how fast）取决于**队列的 drain rate**

现在回到我们刚才提出的问题（k8s 网络资源管理），
在 K8s 中，有什么机制能限制 pod 的网络资源（带宽）使用量吗？

## 1.3 K8s 中的 pod 带宽管理

### 1.3.1 Bandwidth meta plugin

K8s 自带了一个限速（bandwidth enforcement）机制，但到目前为止还是 experimental 状态；
实现上是通过第三方的 bandwidth meta plugin，它会解析特定的 pod annotation，

* **`kubernetes.io/ingress-bandwidth=XX`**
* **`kubernetes.io/egress-bandwidth=XX`**

然后转化成对 pod 的具体限速规则，如下图所示，

![](/assets/img/better-bw-manage-with-ebpf/k8s-bw-plugin.png)

Fig. Bandwidth meta plugin 解析 pod annotation，并通过 TC TBF 实现限速

bandwidth meta plugin 是一个 CNI plugin，底层利用 Linux TC 子系统中的 TBF，
所以最后转化成的是 **TC 限速规则，加在容器的 veth pair 上（宿主机端）**。

这种方式确实能实现 pod 的限速功能，但也存在很严重的问题，我们来分别看一下出向和入向的工作机制。

> 在进入下文之前，有两点重要说明：
>
> 1. 限速只能在出向（egress）做。为什么？可参考 [《Linux 高级路由与流量控制手册（2012）》第九章：用 tc qdisc 管理 Linux 网络带宽](/blog/lartc-qdisc-zh/)；
> 2. veth pair 宿主机端的流量方向与 pod 的流量方向完全相反，也就是
>    **pod 的 ingress 对应宿主机端 veth 的 egress**，反之亦然。
>
> 译注。

### 1.3.2 入向（ingress）限速存在的问题

**对于 pod ingress 限速，需要在宿主机端 veth 的 egress 路径上设置规则**。
例如，对于入向 `kubernetes.io/ingress-bandwidth="50M"` 的声明，会落到 veth 上的 TBF qdisc 上：

![](/assets/img/better-bw-manage-with-ebpf/bw-plugin-ingress-1.png)

TBF（Token Bucket Filter）是个令牌桶，所有连接/流量都要经过**单个队列**排队处理，如下图所示：

![](/assets/img/better-bw-manage-with-ebpf/bw-plugin-ingress-2.png)

在设计上存在的问题：

1. TBF qdisc **所有 CPU 共享一个锁**（著名的 qdisc root lock），因此存在锁竞争；流量越大锁开销越大；
2. **veth pair 是单队列**（single queue）虚拟网络设备，因此物理网卡的
   多队列（multi queue，不同 CPU 处理不同 queue，并发）优势到了这里就没用了，
   大家还是要走到同一个队列才能进到 pod；
3. 在入向排队是不合适的（no-go），会占用大量系统资源和缓冲区开销（bufferbloat）。

### 1.3.3 出向（egress）限速存在的问题

出向工作原理：

* Pod egress 对应 veth 主机端的 ingress，**ingress 是不能做整形的，因此加了一个 ifb 设备**；
* 所有从 veth 出来的流量会被重定向到 ifb 设备，通过 ifb TBF qdisc 设置容器限速。

![](/assets/img/better-bw-manage-with-ebpf/bw-plugin-egress-1.png)

存在的问题：

1. **原来只需要在物理网卡排队**（一般都会设置一个默认 qdisc，例如
   `pfifo_fast/fq_codel/noqueue`），现在又多了一层 ifb 设备排队，缓冲区膨胀（bufferbloat）；
2. 与 ingress 一样，存在 **root qdisc lock 竞争**，所有 CPU 共享；
3. **干扰 TCP Small Queues (TSQ) 正常工作**；TSQ 作用是**减少 bufferbloat**，
   工作机制是觉察到发出去的包还没有被有效处理之后就减少发包；ifb 使得包都缓存在 qdisc 中，
   使 TSQ 误以为这些包都已经发出去了，实际上还在主机内。
4. **延迟显著增加**：每个 pod 原来只需要 2 个网络设备，现在需要 3 个，增加了大量 queueing 逻辑。

![](/assets/img/better-bw-manage-with-ebpf/lots-of-queues.png)

### 1.3.4 Bandwidth meta plugin 问题总结

总结起来：

1. 扩展性差，性能无法随 CPU 线性扩展（root qdisc lock 被所有 CPU 共享导致）；
2. 导致额外延迟；
3. 占用额外资源，缓冲区膨胀。

因此**不适用于生产环境**；

# 2 解决思路

> 这一节是介绍 Google 的基础性工作，作者引用了
> [Evolving from AFAP: Teaching NICs about time (Netdev, 2018)](https://www.youtube.com/watch?v=MAni0_lN7zE)
> 中的一些内容；之前我们已翻译，见
> [流量控制（TC）五十年：从基于缓冲队列（Queue）到基于时间（EDT）的演进（Google, 2018）](/blog/traffic-control-from-queue-to-edt-zh/)，
> 因此一些内容不再赘述，只列一下要点。
>
> 译注。

## 2.1 回归源头：TCP “尽可能快”发送模型存在的缺陷

![](/assets/img/traffic-control-from-queue-to-edt/queue-bottleneck.png)

Fig. 根据排队论，实际带宽接近瓶颈带宽时，延迟将急剧上升

## 2.2 思路转变：不再基于排队（queue），而是基于时间戳（EDT）

两点核心转变：

1. 每个包（skb）打上一个**最早离开时间**（Earliest Departure Time, EDT），也就是最早可以发送的时间戳；
2. 用**时间轮调度器**（timing-wheel scheduler）替换原来的**出向缓冲队列**（qdisc queue）

![](/assets/img/traffic-control-from-queue-to-edt/token-bucket-vs-edt.png)

Fig. 传统基于 queue 的流量整形器 vs. 新的基于 EDT 的流量整形器

## 2.3 3 EDT/timing-wheel 应用到 K8s

有了这些技术基础，我们接下来看如何应用到 K8s。

# 3 Cilium 原生 pod 限速方案

## 3.1 整体设计：基于 BPF+EDT 实现容器限速

Cilium 的 bandwidth manager，

* 基于 eBPF+EDT，实现了**无锁** 的 pod 限速功能；
* **在物理网卡（或 bond 设备）而不是 veth 上限速**，避免了 bufferbloat，也不会扰乱 TCP TSQ 功能。
* **不需要进入协议栈**，Cilium 的 BPF host routing 功能，使得 FIB
  lookup 等过程**完全在 TC eBPF 层完成**，并且能**直接转发到网络设备**。
* 在物理网卡（或 bond 设备）上添加 MQ/FQ，实现**时间轮调度**。

![](/assets/img/better-bw-manage-with-ebpf/cilium-bw-rate-limit.png)

## 3.2 工作流程

在之前的分享
[为 K8s workload 引入的一些 BPF datapath 扩展（LPC, 2021）](/blog/bpf-datapath-extensions-for-k8s-zh/)
中已经有比较详细的介绍，这里在重新整理一下。

Cilium attach 到宿主机的物理网卡（或 bond 设备），在 BPF 程序中为每个包设置 timestamp，
然后通过 earliest departure time 在 fq 中实现限速，下图：

> 注意：容器限速是在**物理网卡**上做的，而不是在每个 pod 的 veth 设备上。这跟之前基于 ifb 的限速方案有很大不同。

![](/assets/img/bpf-datapath-ext-for-k8s/pod-egress-rate-limit.png)

Fig. Cilium 基于 BPF+EDT 的容器限速方案（逻辑架构）

从上到下三个步骤：

1. **BPF 程序**：管理（计算和设置） skb 的 departure timestamp；
2. TC **qdisc (multi-queue) 发包调度**；
3. **物理网卡的队列**。

> 如果宿主机使用了 bond，那么**根据 bond 实现方式的不同，FQ 的数量会不一样**，
> 可通过 **`tc -s -d qdisc show dev {bond}`** 查看实际状态。具体来说，
>
> * Linux bond [默认...