---
title: [译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）
url: https://arthurchiao.github.io/blog/cilium-tomorrow-networking-data-plane-zh/
source: ArthurChiao's Blog
date: 2022-11-13
fetch_date: 2025-10-03T22:37:02.895817
---

# [译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [译] Cilium 未来数据平面：支撑 100Gbit/s k8s 集群（KubeCon, 2022）

Published at 2022-11-12 | Last Update 2022-11-12

### 译者序

本文翻译自 KubeCon+CloudNativeCon North America 2022 的一篇分享：
[100 Gbit/s Clusters with Cilium: Building Tomorrow’s Networking Data Plane](https://kccncna2022.sched.com/event/182DB)。

作者 Daniel Borkmann, Nikolay Aleksandrov, Nico Vibert 都来自 Isovalent（Cilium 母公司）。
翻译时补充了一些背景知识、代码片段和链接，以方便理解。

翻译已获得 Daniel 授权。

**由于译者水平有限，本文不免存在遗漏或错误之处。如有疑问，请查阅原文。**

以下是译文。

---

* [译者序](#译者序)
* [摘要](#摘要)
* [1 大型数据中心网络面临的挑战](#1-大型数据中心网络面临的挑战)
  + [1.1 Cilium 首次亮相（2016）](#11-cilium-首次亮相2016)
  + [1.2 容器领域（k8s/docker）IPv6 支持状态](#12-容器领域k8sdockeripv6-支持状态)
    - [2016 年](#2016-年)
    - [2022 年](#2022-年)
  + [1.3 用户需求](#13-用户需求)
  + [1.4 解决方案](#14-解决方案)
  + [1.5 互联网服务 IPv6 部署现状](#15-互联网服务-ipv6-部署现状)
* [2 Cilium + `IPv6-only` K8s 集群](#2-cilium--ipv6-only-k8s-集群)
  + [2.1 与传统 IPv4 网络/服务对接：NAT46/64](#21-与传统-ipv4-网络服务对接nat4664)
  + [2.2 内核对 NAT46/64 的支持（`4.8+`）](#22-内核对-nat4664-的支持48)
  + [2.3 Cilium 对 NAT46/64 的支持（`v1.12+`）](#23-cilium-对-nat4664-的支持v112)
    - [2.3.1 工作原理](#231-工作原理)
    - [2.3.2 功能支持](#232-功能支持)
    - [2.3.3 工作机制详解：集群入向（`IPv4 -> IPv6-only`）](#233-工作机制详解集群入向ipv4---ipv6-only)
      * [方式一：有状态 NAT46 网关](#方式一有状态-nat46-网关)
      * [方式二：无状态 NAT46 网关](#方式二无状态-nat46-网关)
    - [2.3.3 工作机制详解：集群出向（`IPv6-only -> IPv4`）](#233-工作机制详解集群出向ipv6-only---ipv4)
  + [2.4 Demo: Cilium NAT46/64 GW（略）](#24-demo-cilium-nat4664-gw略)
  + [2.5 小结](#25-小结)
* [3 Cilium + BIG TCP](#3-cilium--big-tcp)
  + [3.1 BIG TCP](#31-big-tcp)
    - [3.1.1 设计目标](#311-设计目标)
    - [3.1.2 使用场景](#312-使用场景)
    - [3.1.3 技术原理](#313-技术原理)
      * [IPv4 限制：单个包最大 64KB](#ipv4-限制单个包最大-64kb)
      * [解决方式：IPv6 HBH (Hop-By-Hop)，单个包最大 4GB](#解决方式ipv6-hbh-hop-by-hop单个包最大-4gb)
  + [3.2 内核支持（`5.19+`）](#32-内核支持519)
  + [3.3 Cilium 支持（`v1.13+`）](#33-cilium-支持v113)
    - [性能](#性能)
  + [3.4 小结](#34-小结)
* [4 Cilium 未来数据平面](#4-cilium-未来数据平面)
  + [4.1 Cilium 作为独立网关节点（standalone GW）](#41-cilium-作为独立网关节点standalone-gw)
  + [4.2 Cilium 作为 k8s 网络方案](#42-cilium-作为-k8s-网络方案)
  + [4.3 meta device vs. veth pair](#43-meta-device-vs-veth-pair)
    - [4.3.1 复习：veth pair default/bpf-host-routing 模式转发路径](#431-复习veth-pair-defaultbpf-host-routing-模式转发路径)
    - [4.3.2 meta device 转发路径](#432-meta-device-转发路径)
    - [4.3.3 meta device 好处：延迟更低](#433-meta-device-好处延迟更低)
    - [4.3.4 meta device vs. veth pair：实现区别](#434-meta-device-vs-veth-pair实现区别)
    - [4.3.5 meta device 性能](#435-meta-device-性能)
* [5 未来已来](#5-未来已来)
  + [5.1 数据平面核心模块](#51-数据平面核心模块)
  + [5.2 学习与进阶路线](#52-学习与进阶路线)
* [致谢](#致谢)

---

# 摘要

今天的大部分 K8s 用户使用的还是**纯 IPv4 网络**（IPv4-only），或称 **IPv4 单栈网络**；
也有一些用户正在从 IPv4 单栈迁移到 **IPv4/IPv6 双栈**上，
最终目标是实现 IPv6 单栈网络，或称**纯 IPv6 网络**（IPv6-only）。
纯 IPv6 网络的 k8s 集群不仅 IPAM 更加灵活，集群规模更大，而且可以解锁很多新的网络和
eBPF 特性，能更好地满足**数据密集型应用**的需求。

本文将展示纯 IPv6 k8s 集群的优势以其面临的问题，以及 Cilium 的数据平面是如何解决这些问题的。内容包括：

1. Cilium + **`IPv6 + BIG TCP`** 支持 `100Gbps/socket`；提升吞吐的同时还能降低延迟；
2. Cilium 新开发的虚拟网络设备 **`meta device`**，替代 veth pair 取得更极致的网络性能；
3. Cilium 的 eBPF 转发架构如何**通过可编程的方式绕过**（bypass）大部分无关的内核网络栈
   （仍然基于内核网络栈，只是绕过无关部分，与 DPDK 等完全绕过内核的方式存在本质区别），显著提升网络性能。

# 1 大型数据中心网络面临的挑战

当前大型数据中心面临三个方面的问题：

* 规模（scale）
* 性能（performance）
* 运营（operations）及日常维护

其中一个重要原因是它们都构建在 IPv4 基础之上，后者已经发挥到极限了。
那么，换成 IPv6 能解决问题吗？答案是能，而且能同时解决规模和性能需求。
要解释这一点，我们需要回顾一下并不久远的“历史”。

## 1.1 Cilium 首次亮相（2016）

Cilium 是作为一个**纯 IPv6 容器网络**实验项目（”The Cilium Experiment”）启动的，
下面这张截图就是我们在 2016 年 LinuxCon 的分享，
[Cilium: Fast IPv6 Container Networking with BPF and XDP](https://www.slideshare.net/ThomasGraf5/cilium-fast-ipv6-container-networking-with-bpf-and-xdp)，

> 几个开发者来自 RedHat 的内核和 OVS 相关开发团队。

![](/assets/img/cilium-tomorrow-networking-data-plane/cilium-linuxcon-2016.png)

* 由于构建在 IPv6-only 之上，因此 Cilium 自带了很多 IPv6 相比 IPv4 的优势，
  例如扩展更好、更灵活、地址空间充裕，无需 NAT 等等；

  ![](/assets/img/cilium-tomorrow-networking-data-plane/ipv6-only-all-the-things.png)
* 更重要的是，为了取得最高效率，Cilium 将 **datapath 构建在 eBPF 之上**，
  这与之前的网络模型完全不同。

但与大多数过于前卫的项目一样，**纯 IPv6 的前提条件很快被现实打脸**。

## 1.2 容器领域（k8s/docker）IPv6 支持状态

### 2016 年

先来看一下当时（2016）年容器领域的 IPv6 生态：

* K8s (CNI)：基本功能有了

  + 1.3.6+ 支持了 IPv6-only pod
  + kube-proxy (services) 不支持 IPv6
* Docker (libnetwork)：还在实现的路上

  + PR826 - “Make IPv6 Great Again”，还没合并

因此，面对众多实际需求，我们不得不**为 Cilium 添加 IPv4 的支持**。

### 2022 年

现在再来看看 6 年之后的今天（2022），容器领域的 IPv6 支持进展：

* K8s 官方

  + IPv6 Single (GA v1.18)
  + IPv4/IPv6 Dual Stack (**`GA v1.23`**)
* 一些重要的基础服务开始支持 IPv6，但主要还是 IPv4/IPv6 双栈方式，而不是 IPv6-only 方式；
* 托管 K8s 集群（AKS、EKS、GKE）开始提供 IPv6 支持，但具体支持到什么程度因厂商而异。

## 1.3 用户需求

用户的实际需求其实比较明确：通过 IPv6 单栈获得更大的 **IPAM 灵活性**，
以及更多的 headroom 来做一些以前（IPv4）做不到的事情。

## 1.4 解决方案

* 从 IPv4-only 直接切换到 IPv6-only 比较困难，需要 IPv4/IPv6 双栈这样一个过渡状态；
* 但最终期望的还是端到端 IPv6，避免 IPv4/IPv6 双栈的复杂性。

![](/assets/img/cilium-tomorrow-networking-data-plane/deploy-k8s-ipv6-only.png)

实现方式：构建 **IPv6 单栈隔离岛**，作为一个完全没用历史负担的环境（clean-slate），
然后将存量的应用/服务迁移到这个环境中来。当然，这其中仍然有一些地方与 IPv4
打交道，除非真空隔离或者没有任何外部依赖。

## 1.5 互联网服务 IPv6 部署现状

说到外部依赖，我们就来看下如今互联网的 IPv6 部署普及情况。根据
[whynoipv6.com](https://whynoipv6.com) 提供的数据，
当前（2022.11） Alexa 排名前 1000 的网站中，

* 只有 469 个启用了 IPv6，
* 845 个启用了 IPv6 DNS；

总共收录的 90 万个网站中，只有 34% 的有 IPv6。

大量的生态系统还在路上，例如，[GitHub 还不能通过 IPv6 clone 代码](https://github.com/community/community/discussions/10539)。

# 2 Cilium + `IPv6-only` K8s 集群

外部依赖短期内全部支持 IPv6 不现实，但通过 4/6 转换，其实就不影响我们先把数据内的
集群和应用 IPv6 化，享受 IPv6 带来的性能和便利性。
下面就来看如何基于 Cilium 部署一个纯 IPv6 的 k8s 集群，并解决与外部 IPv4 服务的互联互通问题。

## 2.1 与传统 IPv4 网络/服务对接：NAT46/64

IPv6-only K8s 与传统 IPv4 服务的对接，使用的是 **`NAT46/NAT64`**，
也就是做 IPv4/IPv6 地址的转换。

这个听上去可能比较简单，但要在 Linux 内核中实现其实是有挑战的，例如
**基于 iptables/netfilter 架构就无法实现这个功能**，
因为内核网络栈太复杂了，牵一发而动全身；好消息是，基于 eBPF 架构能。

## 2.2 内核对 NAT46/64 的支持（`4.8+`）

我们早在 2016 年就对内核 **tc BPF 层添加了 NAT46/64 的支持**：

* [bpf: add bpf\_skb\_change\_type helper](https://github.com/torvalds/linux/commit/d2485c4242a82)
* [bpf: add bpf\_skb\_change\_proto helper](https://github.com/torvalds/linux/commit/6578171a7ff0c)

通过 **`bpf_skb_change_proto()`** 实现 4/6 转换。

> Android 的 [CLAT](https://dan.drown.org/android/clat/)
> 组件也是通过这个 helper 将手机连接到 IPv6-only 蜂窝网的。

## 2.3 Cilium 对 NAT46/64 的支持（`v1.12+`）

### 2.3.1 工作原理

如下图所示，几个部分：

![](/assets/img/cilium-tomorrow-networking-data-plane/NAT46-NAT64-support-for-Load-Balancer.png)

> [Cilium v1.12 Release Notes](https://isovalent.com/blog/post/cilium-release-112/#nat46-nat64)

* 右边：使用 Cilium 网络的 IPv6-only K8s 集群；
* 左下：集群外的 IPv4 服务；
* 左上：**承担 NAT46/64 功能的 Cilium L4LB 节点**；

思路其实很简单，

* 通过 Cilium L4LB 节点做 NAT46/64 转换；

  将 IPv4 流量路由到数据中心的边缘节点（边界），经过转换之后再进入 IPv6 网络；反向是类似的。
* 具体工作在 tc BPF 或 XDP 层。

  通过 `bpf_skb_change_proto()` 完成 4/6 转换。

### 2.3.2 功能支持

Cilium L4LB 现在的 NAT46/64 功能支持：

* XDP / non-XDP
* Maglev / Random
* 通过 **RPC API** 配置 `{IPv4,6} VIP -> {IPv4,6} Backend` 规则

例子，VIP 是 IPv4，backends 是 IPv6 pods：

```
$ cilium service list
ID   Frontend     Service Type   Backend
1    1.2.3.4:80   ExternalIPs    1 => [f00d::1]:60 (active)
                                 2 => [f00d::2]:70 (active)
                                 3 => [f00d::3]:80 (active)
```

另一个例子，

```
$ cilium service list
ID   Frontend       Service Type   Backend
1    [cafe::1]:80   ExternalIPs    1 => 1.2.3.4:8080 (active)
                                   2 => 4.5.6.7:8090 (active)
```

### 2.3.3 工作机制详解：集群入向（`IPv4 -> IPv6-only`）

这里有两种实现方式，Cilium 都支持，各有优缺点。

#### 方式一：有状态 NAT46 网关

这种模式下，NAT46 网关是有状态的，

![](/assets/img/cilium-tomorrow-networking-data-plane/nat46-gw-1.png)

* 部署在边界上，是唯一的双栈组件；
* 将 IPv4 `VIP:port` 映射到 IPv6 `VIP:port`（exposed to public natively）；
* 只有 IPv4 流量需要经过 GW 这一跳；
* K8s 集群是干净的 IPv6-only 集群，node/pod IP 都是纯 IPv6；
* 基于 eBPF/XDP，高性能；

  [XDP (eXpress Data Path)：在操作系统内核中实现快速、可编程包处理（ACM，2018）](/blog/xdp-paper-acm-2018-zh/)

下面是通过 Service 实现的 NAT46 规则（也就是“状态”）：

![](/assets/img/cilium-tomorrow-networking-data-plane/nat46-gw-2.png)

好处：

1. IPv4 `VIP:port` 到 K8...