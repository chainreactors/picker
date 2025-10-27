---
title: K8s 调度框架设计与 scheduler plugins 开发部署示例（2024）
url: https://arthurchiao.github.io/blog/k8s-scheduling-plugins-zh/
source: ArthurChiao's Blog
date: 2024-02-26
fetch_date: 2025-10-04T12:05:46.439138
---

# K8s 调度框架设计与 scheduler plugins 开发部署示例（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# K8s 调度框架设计与 scheduler plugins 开发部署示例（2024）

Published at 2024-02-25 | Last Update 2024-02-25

本文代码见 [github](https://github.com/ArthurChiao/arthurchiao.github.io/tree/master/assets/code/k8s-scheduling-plugins)。

---

* [1 引言](#1-引言)
  + [1.1 调度框架（sceduling framework）扩展点](#11-调度框架sceduling-framework扩展点)
    - [1.1.1 影响调度决策的扩展点](#111-影响调度决策的扩展点)
    - [1.1.2 不影响调度决策的扩展点（informational）](#112-不影响调度决策的扩展点informational)
  + [1.2 调度插件分类](#12-调度插件分类)
    - [1.2.1 `in-tree` plugins](#121-in-tree-plugins)
    - [1.2.2 `out-of-tree` plugins](#122-out-of-tree-plugins)
  + [1.3 每个扩展点上分别有哪些内置插件](#13-每个扩展点上分别有哪些内置插件)
* [2 Pod 调度过程](#2-pod-调度过程)
  + [2.1 等待调度阶段](#21-等待调度阶段)
    - [2.1.1 `PreEnqueue`](#211-preenqueue)
    - [2.1.2 `QueueSort`](#212-queuesort)
  + [2.2 调度阶段（scheduling cycle）](#22-调度阶段scheduling-cycle)
    - [2.2.1 `PreFilter`：pod 预处理和检查，不符合预期就提前结束调度](#221-prefilterpod-预处理和检查不符合预期就提前结束调度)
    - [2.2.2 `Filter`：排除所有不符合要求的 node](#222-filter排除所有不符合要求的-node)
    - [2.2.3 `PostFilter`：`Filter` 之后没有 node 剩下，补救阶段](#223-postfilterfilter-之后没有-node-剩下补救阶段)
    - [2.2.4 `PreScore`](#224-prescore)
    - [2.2.5 `Score`](#225-score)
    - [2.2.6 `NormalizeScore`](#226-normalizescore)
    - [2.2.7 `Reserve`：Informational，维护 plugin 状态信息](#227-reserveinformational维护-plugin-状态信息)
    - [2.2.8 `Permit`：`允许/拒绝/等待`进入 binding cycle](#228-permit允许拒绝等待进入-binding-cycle)
  + [2.3 绑定阶段（binding cycle）](#23-绑定阶段binding-cycle)
    - [2.3.1 `PreBind`：`Bind` 之前的预处理，例如到 node 上去挂载 volume](#231-prebindbind-之前的预处理例如到-node-上去挂载-volume)
    - [2.3.2 `Bind`：将 pod 关联到 node](#232-bind将-pod-关联到-node)
    - [2.3.3 `PostBind`：informational，可选，执行清理操作](#233-postbindinformational可选执行清理操作)
* [3 开发一个极简 sticky node 调度器插件（out-of-tree）](#3-开发一个极简-sticky-node-调度器插件out-of-tree)
  + [3.1 设计](#31-设计)
    - [3.1.1 背景知识](#311-背景知识)
    - [3.1.2 业务需求](#312-业务需求)
    - [3.1.3 技术方案](#313-技术方案)
  + [3.2 实现](#32-实现)
    - [3.2.1 `Prefilter()`](#321-prefilter)
    - [3.2.2 `Filter()`](#322-filter)
    - [3.2.3 `PostBind()`](#323-postbind)
    - [3.2.4 其他说明](#324-其他说明)
  + [3.3 部署](#33-部署)
    - [3.3.1 配置](#331-配置)
    - [3.3.2 运行](#332-运行)
  + [3.4 测试](#34-测试)
    - [3.4.1 首次创建 VM](#341-首次创建-vm)
    - [3.4.2 删掉 VMI/Pod，重新调度时](#342-删掉-vmipod重新调度时)
* [4 总结](#4-总结)
* [参考资料](#参考资料)

---

# 1 引言

K8s 调度框架提供了一种扩展**调度功能**的插件机制，
对于想实现自定义调度逻辑的场景非常有用。

* 如果 pod spec 里没指定 **`schedulerName`** 字段，则使用默认调度器；
* 如果指定了，就会走到相应的调度器/调度插件。

本文整理一些相关内容，并展示如何用 300 来行代码实现一个简单的固定宿主机调度插件。
代码基于 k8s `v1.28`。

## 1.1 调度框架（sceduling framework）扩展点

如下图所示，K8s 调度框架定义了一些**扩展点**（extension points），

![](/assets/img/k8s-scheduling-plugins/scheduling-framework-extensions.png)

Fig. Scheduling framework extension points.

用户可以编写自己的**调度插件**（scheduler plugins）注册到这些扩展点来实现想要的调度逻辑。
每个扩展点上一般会有**多个 plugins**，按注册顺序依次执行。

扩展点根据是否影响调度决策，可以分为两类。

### 1.1.1 影响调度决策的扩展点

大部分扩展点是**影响调度决策**的，

* 后面会看到，这些函数的返回值中包括一个成功/失败字段，决定了是允许还是拒绝这个 pod 进入下一处理阶段；
* 任何一个扩展点失败了，这个 pod 的调度就失败了；

### 1.1.2 不影响调度决策的扩展点（informational）

少数几个扩展点是 informational 的，

* 这些函数**没有返回值**，因此**不能影响调度决策**；
* 但是，在这里面**可以修改 pod/node 等信息**，或者执行清理操作。

## 1.2 调度插件分类

根据是否维护在 k8s 代码仓库本身，分为两类。

### 1.2.1 `in-tree` plugins

维护在 k8s 代码目录 [`pkg/scheduler/framework/plugins`](https://github.com/kubernetes/kubernetes/tree/v1.28.4/pkg/scheduler/framework/plugins) 中，
**跟内置调度器一起编译**。里面有十几个调度插件，大部分都是常用和在用的，

```
$ ll pkg/scheduler/framework/plugins
defaultbinder/
defaultpreemption/
dynamicresources/
feature/
imagelocality/
interpodaffinity/
names/
nodeaffinity/
nodename/
nodeports/
noderesources/
nodeunschedulable/
nodevolumelimits/
podtopologyspread/
queuesort/
schedulinggates/
selectorspread/
tainttoleration/
volumebinding/
volumerestrictions/
volumezone/
```

in-tree 方式每次要添加新插件，或者修改原有插件，都需要修改 kube-scheduler 代码然后编译和
**重新部署 kube-scheduler**，比较重量级。

### 1.2.2 `out-of-tree` plugins

out-of-tree plugins 由**用户自己编写和维护**，**独立部署**，
不需要对 k8s 做任何代码或配置改动。

本质上 out-of-tree plugins 也是跟 kube-scheduler 代码一起编译的，不过 kube-scheduler
相关代码已经抽出来作为一个独立项目 [github.com/kubernetes-sigs/scheduler-plugins](https://github.com/kubernetes-sigs/scheduler-plugins)。
用户只需要引用这个包，编写自己的调度器插件，然后以普通 pod 方式部署就行（其他部署方式也行，比如 binary 方式部署）。
编译之后是个包含**默认调度器和所有 out-of-tree 插件**的总调度器程序，

* 它有内置调度器的功能；
* 也包括了 out-of-tree 调度器的功能；

用法有两种：

* 跟现有调度器并行部署，只管理特定的某些 pods；
* 取代现有调度器，因为它功能也是全的。

## 1.3 每个扩展点上分别有哪些内置插件

内置的调度插件，以及分别工作在哪些 extention points：
[官方文档](https://kubernetes.io/docs/reference/scheduling/config/#scheduling-plugins)。
比如，

* node selectors 和 node affinity 用到了 **`NodeAffinity`** plugin；
* taint/toleration 用到了 **`TaintToleration`** plugin。

# 2 Pod 调度过程

一个 pod 的完整调度过程可以分为两个阶段：

1. **`scheduling cycle`**：为 pod 选择一个 node，类似于**数据库查询和筛选**；
2. **`binding cycle`**：落实以上选择，类似于**处理各种关联的东西并将结果写到数据库**。

例如，虽然 scheduling cycle 为 pod 选择了一个 node，但是在接下来的 binding cycle 中，
在这个 node 上给这个 pod 创建 persistent volume 失败了，
那整个调度过程也是算失败的，需要回到最开始的步骤重新调度。
以上两个过程加起来称为一个 **`scheduling context`**。

另外，在进入一个 scheduling context 之前，还有一个**调度队列**，
用户可以编写自己的算法对队列内的 pods 进行排序，决定哪些 pods 先进入调度流程。
总流程如下图所示：

![](/assets/img/k8s-scheduling-plugins/scheduling-framework-extensions.png)

Fig. queuing/sorting and scheduling context

下面分别来看。

## 2.1 等待调度阶段

### 2.1.1 `PreEnqueue`

Pod 处于 ready for scheduling 的阶段。
内部工作原理：[sig-scheduling/scheduler\_queues.md](https://github.com/kubernetes/community/blob/f03b6d5692bd979f07dd472e7b6836b2dad0fd9b/contributors/devel/sig-scheduling/scheduler_queues.md)。

这一步没过就不会进入调度队列，更不会进入调度流程。

### 2.1.2 `QueueSort`

对调度队列（scheduling queue）内的 pod 进行排序，决定先调度哪些 pods。

## 2.2 调度阶段（scheduling cycle）

### 2.2.1 `PreFilter`：pod 预处理和检查，不符合预期就提前结束调度

这里的插件可以对 Pod 进行预处理，或者条件检查，函数签名如下：

```
// https://github.com/kubernetes/kubernetes/blob/v1.28.4/pkg/scheduler/framework/interface.go#L349-L367

// PreFilterPlugin is an interface that must be implemented by "PreFilter" plugins.
// These plugins are called at the beginning of the scheduling cycle.
type PreFilterPlugin interface {
    // PreFilter is called at the beginning of the scheduling cycle. All PreFilter
    // plugins must return success or the pod will be rejected. PreFilter could optionally
    // return a PreFilterResult to influence which nodes to evaluate downstream. This is useful
    // for cases where it is possible to determine the subset of nodes to process in O(1) time.
    // When it returns Skip status, returned PreFilterResult and other fields in status are just ignored,
    // and coupled Filter plugin/PreFilterExtensions() will be skipped in this scheduling cycle.
    PreFilter(ctx , state *CycleState, p *v1.Pod) (*PreFilterResult, *Status)

    // PreFilterExtensions returns a PreFilterExtensions interface if the plugin implements one,
    // or nil if it does not. A Pre-filter plugin can provide extensions to incrementally
    // modify its pre-processed info. The framework guarantees that the extensions
    // AddPod/RemovePod will only be called after PreFilter, possibly on a cloned
    // CycleState, and may call those functions more than once before calling
    // Filter again on a specific node.
    PreFilterExtensions() PreFilterExtensions
}
```

* 输入：

  + `p *v1.Pod` 是**待调度的 pod**；
  + 第二个参数 `state` 可用于保存一些状态信息，然后在后面的扩展点（例如 `Filter()` 阶段）拿出来用；
* 输出：

  + 只要有**任何一个 plugin 返回失败，这个 pod 的调度就失败了**；
  + 换句话说，所有已经注册的 `PreFilter` plugins 都成功之后，pod 才会进入到下一个环节；

### 2.2.2 `Filter`：排除所有不符合要求的 node

这里的插件可以**过滤掉那些不满足要求的 node**（equivalent of Predicates in a scheduling Policy），

* 针对每个 node，调度器会按配置顺序依次执行 filter plugins；
* **任何一个插件** 返回失败，这个 node 就被排除了；

```
// https://github.com/kubernetes/kubernetes/blob/v1.28.4/pkg/scheduler/framework/interface.go#L349C1-L367C2

// FilterPlugin is an interface for Filter plugins. These plugins are called at the
// filter extension point for filtering out hosts that cannot run a pod.
// This concept used to be called 'predicate' in the original scheduler.
// These plugins shoul...