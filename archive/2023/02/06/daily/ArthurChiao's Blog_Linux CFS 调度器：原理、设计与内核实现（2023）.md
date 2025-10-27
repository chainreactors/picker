---
title: Linux CFS 调度器：原理、设计与内核实现（2023）
url: https://arthurchiao.github.io/blog/linux-cfs-design-and-implementation-zh/
source: ArthurChiao's Blog
date: 2023-02-06
fetch_date: 2025-10-04T05:47:16.841316
---

# Linux CFS 调度器：原理、设计与内核实现（2023）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# Linux CFS 调度器：原理、设计与内核实现（2023）

Published at 2023-02-05 | Last Update 2023-10-03

整理一些 Linux 默认调度器 CFS 相关的东西。CFS、cgroup 等内核技术合力实现了进程的
CPU 资源限额（**CPU 带宽控制**），这是容器的基础之一。

---

* [1 概念及关系](#1-概念及关系)
  + [1.1 CFS：进程（task）的公平调度](#11-cfs进程task的公平调度)
  + [1.2 CFS 扩展](#12-cfs-扩展)
    - [1.2.1 前提：`CONFIG_CGROUPS`](#121-前提config_cgroups)
    - [1.2.2 前提：`CONFIG_CGROUP_SCHED`](#122-前提config_cgroup_sched)
    - [1.2.3 扩展：支持实时进程组（`CONFIG_RT_GROUP_SCHED`）](#123-扩展支持实时进程组config_rt_group_sched)
    - [1.2.4 扩展：支持常规进程组（`CONFIG_FAIR_GROUP_SCHED`）](#124-扩展支持常规进程组config_fair_group_sched)
  + [1.3 常规进程组 CFS 再扩展：支持 CPU 带宽控制（限额）](#13-常规进程组-cfs-再扩展支持-cpu-带宽控制限额)
    - [1.3.1 CFS 存在的问题](#131-cfs-存在的问题)
    - [1.3.2 `CONFIG_CFS_BANDWIDTH`](#132-config_cfs_bandwidth)
  + [1.4 CFS BANDWITH 近几年改进](#14-cfs-bandwith-近几年改进)
  + [1.5 小结：CFS 相关内核编译选项的关系](#15-小结cfs-相关内核编译选项的关系)
* [2 CFS 相关设计](#2-cfs-相关设计)
  + [2.1 设计目标和基本原理](#21-设计目标和基本原理)
  + [2.2 核心概念](#22-核心概念)
    - [2.2.1 `vruntime`](#221-vruntime)
    - [2.2.2 `runqueue`](#222-runqueue)
    - [2.2.3 基于时序的红黑树](#223-基于时序的红黑树)
  + [2.3 调度策略（scheduling policy）](#23-调度策略scheduling-policy)
    - [2.3.1 实时进程调度策略](#231-实时进程调度策略)
      * [`SCHED_FIFO`](#sched_fifo)
      * [`SCHED_RR`](#sched_rr)
    - [2.3.2 常规进程调度策略](#232-常规进程调度策略)
      * [`SCHED_NORMAL`](#sched_normal)
      * [`SCHED_BATCH`](#sched_batch)
      * [`SCHED_IDLE`](#sched_idle)
    - [2.3.3 常规进程 `SCHED_NORMAL` 和实时进程 `SCHED_RR` 调度策略的区别](#233-常规进程-sched_normal-和实时进程-sched_rr-调度策略的区别)
    - [2.3.4 查看或修改进程的调度属性](#234-查看或修改进程的调度属性)
  + [2.4 调度类（scheduling class）](#24-调度类scheduling-class)
  + [2.5 进程组调度器扩展（group scheduler extensions）](#25-进程组调度器扩展group-scheduler-extensions)
  + [2.6 CFS 配置项](#26-cfs-配置项)
    - [例子](#例子)
  + [2.7 CPU 带宽控制设计（`CONFIG_CFS_BANDWIDTH`）](#27-cpu-带宽控制设计config_cfs_bandwidth)
    - [新配置项](#新配置项)
    - [查看 k8s pod 的 CPU throttle 统计](#查看-k8s-pod-的-cpu-throttle-统计)
    - [更多设计细节](#更多设计细节)
  + [2.9 问题](#29-问题)
    - [CPU throttle 是怎么来的](#cpu-throttle-是怎么来的)
    - [上下文切换开销](#上下文切换开销)
* [3 内核实现](#3-内核实现)
  + [3.1 CFS 第一版实现](#31-cfs-第一版实现)
  + [3.2 核心数据结构](#32-核心数据结构)
    - [3.2.1 `struct task_struct`](#321-struct-task_struct)
    - [3.2.2 `struct task_group`](#322-struct-task_group)
    - [3.2.3 `struct sched_entity`](#323-struct-sched_entity)
    - [3.2.4 `struct cfs_rq`](#324-struct-cfs_rq)
    - [3.2.5 `struct sched_class`](#325-struct-sched_class)
  + [3.3 CFS CPU 带宽控制实现](#33-cfs-cpu-带宽控制实现)
* [4 使用](#4-使用)
  + [4.1 模拟 throttle 场景](#41-模拟-throttle-场景)
  + [4.2 k8s 相关问题](#42-k8s-相关问题)
    - [Pod cpu throttle](#pod-cpu-throttle)
    - [k8s pod 使用 cpuset 的条件](#k8s-pod-使用-cpuset-的条件)
    - [生产例子](#生产例子)
* [参考资料](#参考资料)

---

# 1 概念及关系

首先理清几个概念和它们之间的关系。

## 1.1 CFS：进程（task）的公平调度

CFS（Completely Fair Scheduler）是 Linux 内置（也是目前默认）的一个**内核调度器**，
如名字所示，它实现了所谓的“完全公平”调度算法，将 CPU 资源均匀地分配给各进程（
在内核代码中称为“任务”，task）。
简单来说，如果一台机器有一个 CPU 多个（计算密集型）进程，那采用 CFS 调度器时，

![](/assets/img/linux-cfs-design-and-implementation/cfs.png)

* 两个进程：每个进程会各占 50% CPU 时间；
* 四个进程：每个进程会各占 25% CPU 时间；

这个很好理解。接下来看第二个概念。

## 1.2 CFS 扩展

最初的 CFS 管理的是单个任务（进程）的调度，给每个进程分配公平的 CPU 时间。
但很多情况下，进程会组织成进程组（task group）的形式，
用户希望先对进程组分配 CPU 份额，再**在每个进程组里面实现公平调度**。

举个具体例子，多个用户使用同一台机器时，可能希望，

* 首先按 user 公平（也可以不公平）分配 CPU；
* 针对每个 user，再对其所有进程公平分配这个 user 的总 CPU 时间。

为此，**CFS 引入了几项扩展**，例如

* 实时任务的组调度（RT group）
* 常规进程的组调度（task group）

但实现这几个扩展是需要一些前提的。

### 1.2.1 前提：`CONFIG_CGROUPS`

要实现按进程组分配和管理 CPU 份额的功能，首先要能够控制（**control**）
进程组（task **group**）的资源限额，
这种技术在 Linux 内核中已经有了，叫**控制组（control group）**，缩写是 cgroup。
（**`CONFIG_CGROUPS`**）。

* cgroup 有两个版本，分别称为 cgroup v1 和 cgroup v2。这两个版本**不兼容**，现在默认都是用的 v1；
* 有了 `cgroup`，调度器就能通过 `cgroup` 伪文件系统来管理进程组占用的资源（我们这里关心的是CPU 资源）了；
* 更多信息见 Documentation/admin-guide/cgroup-v1/cgroups.rst。

### 1.2.2 前提：`CONFIG_CGROUP_SCHED`

cgroup 是按资源类型（cpu/memory/device/hugetlb/…）来做资源限额的，每种资源
类型会有一种对应的控制器（controller），有独立的开关。
控制**进程或进程组能使用的 CPU 时间**，对应的开关是 `CONFIG_CGROUP_SCHED`。

至此，支持进程组级别资源控制的基础就具备了。接下来就是 CFS 扩展代码的实现，
添加对于 realtime/conventional task group 的支持。下面分别来看下。

### 1.2.3 扩展：支持实时进程组（`CONFIG_RT_GROUP_SCHED`）

`CONFIG_RT_GROUP_SCHED` 支持对 real-time (SCHED\_FIFO and SCHED\_RR) 任务进行分组 CFS。

实时进程有严格的响应时间限制，不管机器的 load 有多高，都应该确保这些进程的响应实时性。
例子：内核中的 **`migration`** 进程，负责在不同 CPU 之间分发任务（进程负载均衡）。

```
$ ps -ef | grep migration
root          12       2  0       00:00:01 [migration/0]
```

### 1.2.4 扩展：支持常规进程组（`CONFIG_FAIR_GROUP_SCHED`）

实时进程之外的进程就是所谓的**常规进程**，它们没有严格的响应时间限制，
当系统繁忙时，响应延迟就会增加。

在 cgroup 技术基础上上，再对 CFS 代码做一些增强，就能够支持进程组内的公平调度了。
这些增强代码是通过编译选项 **`CONFIG_FAIR_GROUP_SCHED`** 控制的。
支持对普通 CFS (SCHED\_NORMAL, SCHED\_BATCH) 任务进行分组。

至此，我们已经能对进程和进程组进行 CFS 调度。

## 1.3 常规进程组 CFS 再扩展：支持 CPU 带宽控制（限额）

### 1.3.1 CFS 存在的问题

CFS 自己也存在一些问题或限制：

1. 某些情况下做不到真正的公平。

   CFS 本质上是会把 CPU 用满的（work-conserving）。具体来说，如果一个 CPU 上
   有两个任务，理论上应该各占用 50% 的 CPU；但如果其中一个任务有很多 sleep/wait 时间，
   CFS 就会把多余的时间给到第二个进程，导致第二个进程实际使用的时间超过一半。
2. 优先级高的进程仍然可能获得更大的时间片。

   内核中有两中调度类（scheduling class）：SCHED\_RT 和 SCHED\_NORMAL，前者的优先级更大。
   当一个 CPU 上有 RT 类型任务时，永远是它们先执行。优先级可以通过 `nice(2)` 控制。
3. 无法设置 CPU 使用上限。

   CFS **只关注 CPU 平均分配，并不保证 CPU 时间**（上下限）。
   换句话说，CPU share/quota 只有相对意义，share 大的一定比 share 小的能分到更多 CPU，仅此而已。
   进程越多，每个进程分到的 CPU 时间越少。
   CPU 限额（上限）对**按 CPU 时间计费**的场景非常关键，例如公有云。

   ![](/assets/img/linux-cfs-design-and-implementation/cfs-share-hierarchy.png)

   图片来自 google paper [5]。注意：严格来说，这里的相对时间还只是在 SCHED\_NORMAL 里的时间，不包括 SCHED\_RT 进程占掉的 CPU 时间。

### 1.3.2 `CONFIG_CFS_BANDWIDTH`

> 严格来说，Linux 中的调度单位是线程（thread），因此在调度上下文中并没有进程（process）的概念。

基于以上原因，Google 提出了 **CFS CPU 带宽控制**（CFS bandwidth control）方案，并合并到了主线内核。
这里的“CPU 带宽”指的就是 CPU 份额，或者说的更清楚点，CPU 比例。
SCHED\_RT 中其实已经有这个功能，这里指的是 SCHED\_NORMAL 支持这个功能。

这个功能的好处主要是给服务器，不是给桌面电脑。
好处：

* 能精确控制一个进程使用的 CPU 带宽上限；比如设置一个容器只能使用 0.2 CPU，
  那它的总时间就不能超过这个比例，即使这个 CPU 非常空闲；
* 对容量规划非常有用（例如 OpenStack 调度 VM，k8s 调度 pod）；
* 延迟更有保证；

## 1.4 CFS BANDWITH 近几年改进

* burst 特性：允许借用前一个进程剩下的带宽。

## 1.5 小结：CFS 相关内核编译选项的关系

总结一下前面提到的 CFS 相关功能，它们的配置选项或依赖关系如下：

```
CONFIG_CGROUPS                     # 1. 是否支持 cgroup，下面进一步区分 cpu/memory/hugetlb/...
  |-CONFIG_MEMCG                   #   1.1 是否支持 memory cgroup
  |-CONFIG_BLK_CGROUP              #   1.2 是否支持 blkio cgroup
  |-CONFIG_CGROUP_SCHED            #   1.3 是否支持 cpu cgroup
  |   |-CONFIG_RT_GROUP_SCHED      #     1.3.1 是否支持 realtime scheduler cpu cgroup
  |   |-CONFIG_FAIR_GROUP_SCHED    #     1.3.2 是否支持 cfs for task cgroup
  |       |-CONFIG_CFS_BANDWIDTH   #       1.3.2.1 是否支持 cfs cpu bandwidth
  |
  |-CONFIG_CGROUP_PIDS             #   1.4 是否支持 pid cgroup
  |-CONFIG_CPUSETS                 #   1.5 是否支持 cpuset cgroup
  |-CONFIG_CGROUP_DEVICE           #   1.6 是否支持 device cgroup
  |-CONFIG_CGROUP_CPUACCT          #   1.7 是否支持 cpu,acc cgroup
  |-...                            #   1.8 是否支持 ... cgroup
```

这些宏定义（编译开关）的层次关系在 `init/Kconfig` 中可以看出来，在父一级开关为 yes 的条件下，才会有子一级的开关。
例如，要启用 CFS CPU 带宽控制功能，就必须要有：
`CONFIG_CGROUPS=y && CONFIG_CGROUP_SCHED=y && CONFIG_FAIR_GROUP_SCHED=y && CONFIG_CFS_BANDWIDTH=y`
这是本文接下来将重点关注的部分（**`1 -> 1.3 -> 1.3.2 -> 1.3.2.1`**）。

各开关的详细解释：

```
// init/Kconfig

menuconfig CGROUPS
    bool "Control Group support"
    help
      This option adds support for grouping sets of processes together, for
      use with process control subsystems such as Cpusets, CFS, memory controls or device isolation.
      See
        - Documentation/scheduler/sched-design-CFS.rst    (CFS)
        - Documentation/admin-guide/cgroup-v1/ (features for grouping, isolation and resource control)

if CGROUPS
    config MEMCG
        bool "Memory controller"
        select PAGE_COUNTER
        help
          Provides control over the memory footprint of tasks in a cgroup.
    config BLK_CGROUP
        bool "IO controller"
        depends on BLOCK
        help
          Generic block IO controller cgroup interface. This is the common
          cgroup interface which should be used ...