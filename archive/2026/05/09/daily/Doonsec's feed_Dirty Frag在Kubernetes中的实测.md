---
title: Dirty Frag在Kubernetes中的实测
url: https://mp.weixin.qq.com/s/f_lI_m7i7gCSUVgN03tfGQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:40.926217
---

# Dirty Frag在Kubernetes中的实测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Kric7mM9eA5DicdEOicOPS6shY7VFr871w1XpicufajwYiaHAicqsgPgPyDZrad3qcicfeJqxHv3tr09GoBqpGujYekj1sVBsoSroygr3x10sgN2zc/0?wx_fmt=jpeg)

# Dirty Frag在Kubernetes中的实测

Dubito
Dubito

云原生安全指北

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 注：本文翻译自 Juliet 的文章《Dirty Frag in Kubernetes: EKS and GKE Exposed With Unset Seccomp》[1]，可点击文末“阅读原文”按钮查看英文原文。

全文如下：

## 一、引言

Dirty Frag 是 Hyunwoo Kim 在V4bel/dirtyfrag[2]中公开并作为 PoC 发布的一种 Linux 本地提权技术 。上游文章描述了两条页缓存（page-cache）写入路径：一条是 xfrm-ESP 路径，另一条是 RxRPC 路径。xfrm 路径需要创建用户命名空间（user namespace）和网络命名空间（network namespace）。RxRPC 路径本来适用于无法使用命名空间路径的环境，但它的前提是 RxRPC 可用。

上游文章主要关注 Linux。针对 Kubernetes，我们关心的问题更具体：

> 在一个普通 Pod 中，Dirty Frag 攻击链的哪些部分是可以触达的？Kubernetes 或节点的哪些控制措施可以真正阻断它？

我们在真实的 Kubernetes 集群和本地 kind 集群上做了测试。不同云提供商的差异确实有影响：

* • 在 Amazon Linux 2023 上的 EKS：在我们的实验环境中，当 seccomp 未设置或被设为 `Unconfined` 时，可以被利用。
* • 在 Container-Optimized OS 上的 GKE：在我们的实验环境中，当 seccomp 未设置或被设为 `Unconfined` 时，可以被利用。
* • 在我们本地实验室集群的 Talos 上：即使显式设置 seccomp 为 `Unconfined`，所测试的 xfrm 链也会被阻断，因为在节点层面用户命名空间（user namespace）被禁用了。
* • `RuntimeDefault` seccomp 通过拒绝 `unshare(USER|NET)` 的方式，在 EKS、GKE、Talos 以及本地 kind 上都阻断了所测试的 xfrm 链。
* • Pod 安全标准（Pod Security Standards）中的 Restricted 策略在 GKE 上阻断了完整的所测试的 xfrm PoC，在 EKS 和 Talos 上则阻断了所测试的 xfrm 前置条件。

本文的范围是刻意的。我们在 EKS 和 GKE 上证明了可以在受控的 Pod 中获得容器内的 root 权限。但我们没有证明能够获得宿主机的 root 权限，也没有证明能够实现容器逃逸。我们没有测试所有托管 Kubernetes 发行版、所有节点镜像、所有内核构建版本，也没有端到端地测试 RxRPC 备用路径。在我们测试的所有 Kubernetes 环境中，`AF_RXRPC` 都不被支持。

截至 2026 年 5 月 8 日，上游 Dirty Frag 的 README 仍然写着：禁运（embargo）已被打破，没有对应的 CVE 或补丁。请将此视为一个带时间戳的上游状态说明，不能替代厂商的安全公告。

## 二、主要发现

* • 在 EKS 和 GKE 上，seccomp 未设置的 Pod 会以 `Seccomp: 0` 运行。xfrm Dirty Frag 路径可以成功，并拿到容器内的 `uid=0(root)`。
* • 在 EKS 和 GKE 上，显式设置 `seccompProfile.type: Unconfined` 也同样可以成功，并拿到容器内的 `uid=0(root)`。
* • 在 EKS 和 GKE 上，`RuntimeDefault` seccomp 在页缓存标记发生变化之前，于 `unshare(USER|NET)` 这一步就阻断了该 PoC。
* • 在 GKE 上，PSS Restricted 策略通过 `NoNewPrivs: 1`、`Seccomp: 2`、移除能力（dropped capabilities）、拒绝 `unshare` 以及不变的`/usr/bin/su` 的标记字节（unchanged `/usr/bin/su` marker bytes）等方式，阻断了完整的PoC。在 EKS 和 Talos 上，PSS Restricted 则在同样的 `unshare(USER|NET)` 步骤阻断了所测试的 xfrm 前置条件。
* • 在 Talos 上，`user.max_user_namespaces=0` 即使 seccomp 显式设置为 `Unconfined`，也会阻断 xfrm 路径。
* • 在我们测试的 kind、EKS、GKE 和 Talos 环境中，`AF_RXRPC` 均不可用，因此我们不声称对 RxRPC 备用路径进行了覆盖测试。
* • GKE 和 Talos 在我们测试的 Pod 中没有可用的 `pcbc(fcrypt)`。但在 GKE 上，当 seccomp 未设置或设为 `Unconfined` 时，xfrm 路径仍然成功。因此缺少 `pcbc(fcrypt)` 并没有让该 GKE 节点免于被 xfrm 链攻击。
* • 我们观察到 Kubernetes 可移植性方面的一个重要差异：在 EKS 和 GKE 上，不设置 seccomp 意味着 `Seccomp: 0`；而在 Talos 上，一个 seccomp 未设置的 Pod 在我们的测试中仍显示为 `Seccomp: 2`。

## 三、Dirty Frag 是什么

上游的 Dirty Frag 项目描述了一类本地提权漏洞，它是基于页缓存写入原语构建的。其 README 显示，xfrm-ESP 页缓存写入路径自 2017 年 1 月的一个 Linux 提交起就已存在，而 RxRPC 路径自 2023 年 6 月的一个提交起就已存在。作者将 Dirty Frag 定位为与 Dirty Pipe 和 Copy Fail 相关，因为攻击者修改的是文件 backed 的页缓存内容，而不是常规磁盘上的文件字节。

公共 PoC 中的 xfrm 路径使用了用户命名空间和网络命名空间，通过 `NETLINK_XFRM` 配置 xfrm 状态，并对 `/usr/bin/su` 的缓存字节进行修补。在我们成功复现的 EKS 和 GKE 实验室环境中，Pod 以 uid 1000 启动，修改了 `/usr/bin/su` 的缓存字节，然后执行被修改后的路径，最终在容器内拿到 uid 0。

最后一句话需要明确边界：拿到容器内的 uid 0 并不等同于拿到宿主机的 root 权限。Kubernetes Pod 共享节点内核，但容器进程仍然运行在容器命名空间、挂载点以及剩余运行时隔离措施之内。

## 四、为什么 Kubernetes 改变了问题的性质

Kubernetes 团队不仅需要问“Linux 内核是否受影响”，他们还需要问：

* • 一个 Pod 能否创建用户命名空间和网络命名空间？
* • seccomp 是否真的被应用了？
* • seccomp 是未设置、`RuntimeDefault`、`Localhost`，还是 `Unconfined`？
* • 节点是否允许非特权用户命名空间（unprivileged user namespaces）？
* • 内核是否暴露了 `NETLINK_XFRM`、`AF_ALG` 和 `AF_RXRPC`？
* • PSS Restricted 策略是否应用到了该命名空间？
* • 不受信任的工作负载是否与敏感 Pod 被调度到了同一个节点上？

Kubernetes 将 seccomp 定义为一种限制从用户空间进入内核的系统调用的方式。Kubernetes 也支持 `RuntimeDefault` 配置文件和节点本地的 `Localhost` 配置文件。但 `RuntimeDefault` 并不是一个通用的单一配置文件。它是运行时所提供的默认配置文件，依赖于节点环境。

Pod 安全标准中的 Restricted 策略也不是万能的漏洞防护盾。它是一个基线。它要求启用一些在此场景下很重要的控制措施，包括禁止特权提升、启用 seccomp、以及移除所有能力（capabilities）。Kubernetes 规定，Restricted 容器必须删除 `ALL` 能力，并且只能重新添加 `NET_BIND_SERVICE`。在我们对 GKE 进行受限完整PoC的测试中，结果产生了 `CapBnd: 0000000000000000`、`NoNewPrivs: 1` 和 `Seccomp: 2`。

对于 Dirty Frag 的 xfrm 路径而言，在我们的测试中这些控制措施已经足够了。这与我们之前对 Copy Fail 的测试结果不同。在 Copy Fail 中，PSS Restricted 和 `RuntimeDefault` 并没有阻断 `AF_ALG` 的可达性。Dirty Frag 和 Copy Fail 都涉及页缓存相关领域，但它们在 Kubernetes 中的控制点并不相同。

## 五、我们测试了什么

我们使用了上游 commit 中的公开 Dirty Frag PoC 代码：

```
892d9a31d391b7f0fccb333855f6289507186748
```

在撰写本文之前，我们已将该 commit 与上游 `master` 分支进行了比对。

我们为 Kubernetes 测试构建了两个 amd64 二进制文件：

* • 一个探针（probe）二进制文件，用于记录内核/运行时信息，并测试 `AF_RXRPC`、`NETLINK_XFRM`、`AF_ALG`、`pcbc(fcrypt)`、keyring 调用、`unshare(USER|NET)`、uid/gid 映射写入、环回接口（loopback）设置，以及执行 `unshare` 之后的 `NETLINK_XFRM` 的可达性。
* • 一个基于公开 `exp.c` 的PoC二进制文件，强制走 xfrm/ESP 路径，并在执行前后输出 `/usr/bin/su` 标记字节的日志。

每一次执行修改操作的运行（mutating run），我们都使用了一个特权的清理 Pod，在漏洞利用尝试之前和最终结束后分别清理页缓存。我们尽可能选择低密度的节点，使用了以 `jdfrag-*` 命名的短期命名空间，并在事后验证了这些命名空间已被删除。

成功的主要标志不仅仅是“进程退出码为零”。我们将以下所有条件同时满足才认定为可被利用：

* • 初始的 Pod uid 为非 root；
* • seccomp 状态与当前测试的用例相符；
* • `/usr/bin/su` 中的标记字节从 `0300000004000000` 变为了 `31ff31f631c0b06a`；
* • PoC 程序打印了 xfrm 页缓存修补消息；
* • shell 拿到了 `uid=0(root)`；
* • 执行了最终的清理操作。

## 六、EKS 结果：当 seccomp 未设置或为 Unconfined 时可被利用

EKS 的测试使用了一个非生产集群。目标节点是一个低密度的 Amazon Linux 2023 工作节点，在资产盘点时上面运行着 7 个 Pod。

```
Kubernetes:        v1.34.7-eks-40737a8
OS image:          Amazon Linux 2023.11.20260413
Kernel:            6.12.79-101.147.amzn2023.x86_64
Container runtime: containerd 2.2.1
```

### 6.1 EKS RuntimeDefault

`RuntimeDefault` 在命名空间创建阶段就阻断了 xfrm 链：

```
NoNewPrivs: 0
Seccomp:    2
Seccomp_filters: 1
DIRTYFRAG_EXP_BEFORE_MARKER 0300000004000000
[su] unshare: Operation not permitted
dirtyfrag: failed (rc=1)
DIRTYFRAG_EXP_AFTER_MARKER 0300000004000000
```

探针显示，在执行 `unshare` 之前 `NETLINK_XFRM` 和 `AF_ALG` 都是可达的，并且该 EKS 节点上存在 `pcbc(fcrypt)`，但是 `unshare(USER|NET)` 被拒绝。对于 xfrm 链而言，这个拒绝是决定性的。

### 6.2 EKS seccomp 未设置

在未设置 seccomp 配置文件的情况下，Pod 以 `Seccomp: 0` 运行。探针显示 `unshare(USER|NET)` 成功，uid/gid 映射可以被写入，环回接口可以被启动，并且 `unshare` 之后 `NETLINK_XFRM` 也能正常工作。

完整的PoC成功拿到了容器内的 root 权限：

```
DIRTYFRAG_IDS_BEFORE uid=1000 gid=1000 groups=1000
CapEff: 0000000000000000
NoNewPrivs: 0
Seccomp: 0
Seccomp_filters: 0
DIRTYFRAG_EXP_BEFORE_MARKER 0300000004000000
[su] installed 48 xfrm SAs
[su] wrote 192 bytes to /usr/bin/su starting at 0x0
[su] /usr/bin/su page-cache patched (entry 0x78 = shellcode)
# uid=0(root) gid=0(root) groups=0(root)
root
DIRTYFRAG_EXP_AFTER_MARKER 31ff31f631c0b06a
```

### 6.3 EKS Unconfined

显式设置 `seccompProfile.type: Unconfined` 同样拿到了容器内的 root 权限，标记字节的变化和 `uid=0(root)` 的结果与之前一致。

### 6.4 EKS PSS Restricted

在 EKS 的受限（Restricted）探针中，结果为 `NoNewPrivs: 1`、`Seccomp: 2`、无有效能力（effective capabilities），并且 `unshare(USER|NET)` 被拒绝。在 GKE 的受限完整 PoC 确认了同样的失败点之后，我们没有在 EKS 的受限命名空间中运行完整的修改操作 PoC。我们经过验证的 EKS 结论范围更窄：PSS Restricted 阻断了我们测试的 xfrm 路径所需的前置条件。

## 七、GKE 结果：当 seccomp 未设置或为 Unconfined 时可被利用

GKE 的测试使用了一个开发/预发集群。目标节点是资产盘点时密度最低的 Container-Optimized OS 工作节点。

```
Kubernetes:        v1.33.9-gke.1060000
OS image:          Container-Optimized OS from Google
Kernel:            6.6.122+
Container runtime: containerd 2.0.7
```

### 7.1 GKE RuntimeDefault

`RuntimeDefault` 在 `unshare(USER|NET)` 这一步阻断了 xfrm 链：

```
NoNewPrivs: 0
Seccomp: 2
Seccomp_filters: 1
DIRTYFRAG_EXP_BEFORE_MARKER 0300000004000000
[su] unshare: Operation not permitted
dirtyfrag: failed (rc=1)
DIRTYFRAG_EXP_AFTER_MARKER 0300000004000000
```

### 7.2 GKE seccomp 未设置

在 GKE 上未设置 seccomp 的行为与 EKS 类似：Pod 以 `Seccomp: 0` 运行，用户命名空间和网络命名空间的创建成功，并且 `unshare` 之后 `NETLINK_XFRM` 也能正常工作。

完整的PoC成功拿到了容器内的 root 权限：

```
DIRTYFRAG_IDS_BEFORE uid=1000 gid=1000 groups=1000
CapEff: 0000000000000000
NoNewPrivs: 0
Seccomp: 0
Seccomp_filters: 0
DIRTYFRAG_EXP_BEFORE_MARKER 0300000004000000
[su] installed 48 xfrm SAs
[su] wrote 192 bytes to /usr/bin/su starting at 0x0
[su] /usr/bin/su page-cache patched (entry 0x78 = shellcode)
# uid=0(root) gid=0(root) groups=0(root)
root
DIRTYFRAG_EXP_AFTER_MARKER 31ff31f631c0b06a
```

### 7.3 GKE Unconfined

显式设置 `Unconfined` 同样拿到了容器内的 root 权限。其结果与 seccomp 未设置的情况一致：标记字节变为 `31ff31f631c0b06a`，PoC程序拿到了 `uid=0(root)`。

### 7.4 GKE PSS Restricted

我们在一个 PSS Restricted 命名空间中运行了完整的PoC。它在页缓存标记字节发生变化之前就失败了：

```
DIRTYFRAG_...