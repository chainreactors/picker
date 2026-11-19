---
title: K8s容器编排系统安全：从架构基础到漏洞利用与横向移动（上）
url: https://mp.weixin.qq.com/s/0impnmiWyeBw7z9q4_OpzQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:42.248962
---

# K8s容器编排系统安全：从架构基础到漏洞利用与横向移动（上）

# K8s容器编排系统安全：从架构基础到漏洞利用与横向移动（上）

原创

安全攻防屋
安全攻防屋

安全攻防屋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文系统梳理 Kubernetes 容器编排安全知识：先介绍 K8s 架构与核心组件、Pod/Service/Namespace 等基础概念，再结合环境复盘配置文件泄露、API Server 未授权访问、特权 Token、kubelet 匿名访问四类常见攻击面的利用过程，最后介绍 K8s 环境下的横向上线思路。

## 一、K8s 基础

### 01 架构概述

Kubernetes 简称 K8s，是用于自动部署、扩缩和管理容器化应用程序的开源系统，起源于 Google 的集群管理工具 Borg。简单来说，K8s 用于对容器进行部署、扩展和管理，并提供容器自动重启、自动重建等能力。

Kubernetes 集群组件逻辑图：

![Kubernetes集群组件逻辑图](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccibtaMxLa4rfY5s170ezHUEU7aA9HlwncWPjL1hseGhXvo6iaRmPpp0pQmeGP15LzHmjcxS8gNBhU6iaGLXEcR96ibE3Xib3p4e48jU/640?wx_fmt=png&from=appmsg)

一个节点（Node）一般就是一台物理机或虚拟机，节点里面有多个 Pod（K8s 的最小调度单元）。Pod 是一个或多个容器的组合（一般建议一个 Pod 只放一个容器）。Pod 在创建时会被分配 IP 地址，同一节点内的 Pod 之间可以通过该 IP 直接通信。

Pod 并不是一个稳定的实体：如果 Pod 在运行过程中发生故障，K8s 会自动将其销毁并创建一个新的 Pod，而新 Pod 被重新分配的 IP 可能与原来不同，所以 K8s 提供了 Service（svc）资源对象来解决这一问题。

K8s 集群属于 Master-Slave 主从架构：Master 节点负责集群管理和资源调度，运行控制平面组件；Slave 节点即工作负载节点，一般称为 Node 节点（也叫 Worker 节点），主要负责运行 Pod。一个 Pod 里可以同时运行多个容器，容器一般封装的是基于 Docker 打包的应用。Pod 英文原意为"豌豆荚"，每个容器就像是一颗豌豆，简单来说 Pod 就是一组容器。

![控制平面组件](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccic7Dwc5rTvY1kUib588HqxCUgkv65NUKia1HhIHBOwEPlj8Hhiasibf6dq7D9K7p99ER8Qnqlm5TINAB9g9eYQlyhmkyCyDnTYM7To/640?wx_fmt=png&from=appmsg)

| 组件 | 说明 |
| --- | --- |
| API Server | 集群的唯一入口点，提供统一的 REST API，所有集群管理和控制操作都通过 API Server 进行。我们通常使用 kubectl 工具控制集群，kubectl 正是通过 API Server 来操作集群的。 |
| etcd | 控制平面的后端数据库，采用分布式键值存储架构，用于保存集群的配置和状态信息。 |
| kube-scheduler | 负责 Pod 调度，根据资源需求和其他策略将 Pod 分配到合适的节点上。它会评估每个节点的资源利用率与可用性，管理员也可以通过配置调度策略和优先级来自定义调度过程。 |
| kube-controller-manager | 内置多个控制器（节点控制器、副本控制器、服务控制器等），用于监控和维护集群状态，使应用保持在期望状态。例如 Deployment 控制器，用于管理长期运行的无状态应用。 |
| cloud-controller-manager | 与云服务商的 API 交互以管理云资源，属于可选组件，根据集群运行环境决定是否部署。 |

![工作节点组件](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc8AB13kh8gh2SW07xyA17Qc9SwBK4P18boomLUnaaQ8mxr4L1XYib1qU8C1LB4zfX0euv7qHibtBKccnTSYicKdwLKeoPCa4CibItE/640?wx_fmt=png&from=appmsg)

| 组件 | 说明 |
| --- | --- |
| kubelet | 运行在每个工作节点上的节点代理，负责与主节点通信，管理 Pod 的生命周期（启动、停止和监控）。 |
| kube-proxy | 节点上的网络代理和负载均衡器，负责 Service 的实现，具体包括集群内部从 Pod 到 Service 的访问，以及外部从 NodePort 到 Service 的访问。 |
| 容器运行时（Container Runtime） | 用于运行容器的软件，如 Docker、containerd 或 CRI-O，容器运行时在工作节点上启动和管理容器。 |
| Pod | 最小部署单位，包含一个或多个容器，共享网络命名空间和存储卷，工作节点上运行的容器都在 Pod 中。 |

### 02 Pod 概念

Kubernetes 有很多技术概念，同时对应很多 API 对象，其中最重要、最基础的是 Pod。Pod 资源对象是一种集合了一到多个应用容器、存储资源、专用 IP 及支撑容器运行的其他选项的逻辑组件。

Pod 的特点：

* Kubernetes 集群中最小的部署单位；
* 一个 Pod 中可以拥有多个容器；
* 同一个 Pod 内的容器共享网络和存储；
* 每一个 Pod 都会有一个 Pause 容器；
* Pod 的生命周期只跟 Pause 容器一致，与其他应用容器无关。

Pod 可以由用户直接创建，也可以由控制器对象（如 Deployment、StatefulSet、DaemonSet 等）创建，由此分为两种类型：

| 类型 | 特点 |
| --- | --- |
| 自主式 Pod | 由用户直接创建，不受任何控制器管理，可以直接使用 `kubectl apply -f <pod-spec.yaml>` 创建。这种 Pod 在节点宕机或者由于某种原因被删除后，Kubernetes 不会尝试重新创建它。 |
| 控制器管理的 Pod | 由控制器（如 Deployment、ReplicaSet、StatefulSet、DaemonSet 等）创建和管理。控制器会根据配置创建 Pod，并确保始终有指定数量的 Pod 在运行；如果 Pod 崩溃、被删除或所在节点宕机，控制器会自动创建新的 Pod 来替换它。 |

创建自主式 Pod 的方式是通过 kubectl apply -f  命令，其中  是一个包含 Pod 定义的 YAML 文件。例如，下面是一个创建自主式 Pod 的示例 YAML 文件：

```
apiVersion: v1 # Kubernetes API 的版本，v1 是核心 API，包括 Pod、Service 等基础对象kind: Pod # 对象类型，这里是一个 Podmetadata: # 对象的元数据，包括对象的名称、标签等  name: standalone-pod  labels:    app: standalone-podspec: # 对象的规格，描述对象应该是什么样子  containers: # Pod 中的容器列表  - name: nginx # 容器名称    image: nginx:1.14.2 # 容器镜像    ports:    - containerPort: 80 # 容器监听的端口
```

在这个例子中，创建了一个名为 standalone-pod 的 Pod，里面运行了一个 nginx 容器。这种 Pod 的重要特性是：如果它因为某种原因被删除（例如 Node 宕机或手动删除），Kubernetes 不会尝试重新创建它。

控制器管理的 Pod 由 Kubernetes 控制器（如 Deployment、ReplicaSet、StatefulSet 等）创建和管理，可以自动确保指定数量的 Pod 在运行；如果 Pod 崩溃、被删除或所在节点宕机，控制器会自动创建新的 Pod 来替换它。下面是一个典型的 Deployment 示例：

```
apiVersion: apps/v1 # 使用 apps/v1，这是 Deployment 资源对应的 API 版本kind: Deployment # 创建的资源类型为 Deploymentmetadata: # 元数据  name: nginx-deploymentspec: # Deployment 的规格  replicas: 3 # 期望运行的 Pod 副本数量  selector: # 定义 Deployment 如何找到它要管理的 Pod    matchLabels:      app: nginx  template: # Deployment 创建的 Pod 模板    metadata:      labels:        app: nginx    spec:      containers:      - name: nginx        image: nginx:1.14.2        ports:        - containerPort: 80
```

实验准备：在每个节点（主节点以及工作节点）上传并导入 shiro.tar 镜像（后续将副本分布到多个节点，因此每个节点都需要导入）。

1. 主节点导入镜像

```
docker load --input shiro.tar
```

![docker load 导入镜像](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc9snpDAekd2nfFfxAe8Mopicic3NWnJXrJTrxZsAtwicpClIcbhibIzXupkbYVlOex2eOvibpzA5EUcARvPWgJjW4oMXMuOyib8QwicHA/640?wx_fmt=png&from=appmsg)

2. 上传 shiro.yaml 并部署（YAML 文件只需在主节点上传执行），内容如下：

```
apiVersion: apps/v1 # 指定 API 版本kind: Deployment # 定义资源类型为 Deploymentmetadata: # 元数据部分  name: shiro-deployment # Deployment 的名称spec: # 规格部分  replicas: 1 # 设置副本数量为 1  selector: # 定义选择器，用于选择管理的 Pods    matchLabels:      app: shiro  template: # 模板部分    metadata:      labels:        app: shiro    spec:      containers: # 容器定义部分      - name: shiro # 容器名称        image: vulhub/shiro:1.2.4 # 使用的镜像及版本        imagePullPolicy: IfNotPresent # 仅在本地镜像不存在时拉取，其他选项 Always、Never        ports: # 容器端口配置        - containerPort: 8080 # 容器内部的端口---apiVersion: v1 # 指定 API 版本kind: Service # 定义资源类型为 Servicemetadata:  name: shiro-service # Service 的名称spec:  type: NodePort # Service 类型为 NodePort  selector: # 选择标签为 app: shiro 的 Pods    app: shiro  ports: # 端口配置    - port: 8080 # Service 公开的端口      targetPort: 8080 # 容器内的端口      nodePort: 30011 # 映射到物理机的端口
```

3. 主节点上部署服务

```
kubectl apply -f shiro.yaml
```

![kubectl apply 部署](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccicQ9XkNiavXhs9QibicnibEDVKX6sADy5Xh9L9pazvBRNy6MWGKgSFp0Xzcg4Sj7yV8Y5kogfeF94mWd12yRwF0N2Wl9NSBicEIjKoU/640?wx_fmt=png&from=appmsg)

4. 主节点上查看 Pod

```
kubectl get pods
```

![kubectl get pods](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMicc8tyMFHhq2QruOBsSvptLFXoPdSe9lZHAwmWib1xrQAJKILFYs7JuJmhgMbQuk7XNvmWGfZ0QicY47qHM6BevxQLL6jqGjUQHwOI/640?wx_fmt=png&from=appmsg)

5. 访问对应的 30011 端口（NodePort），出现如下页面说明部署成功

![Shiro 登录页](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc80QL9yYo4MaH8OpppGIyNCicpZPcaZDGX1TtM2wwQhkEHHNYWJMSibAjicJqk6opG7ibjFaujXa23vSNE8XjibQ8n3wnELicibap6nB0/640?wx_fmt=png&from=appmsg)

6. 尝试利用

使用 Shiro 反序列化漏洞综合利用工具对目标进行检测，成功识别出 Shiro 框架、RememberMe 密钥，并爆破出利用链 CommonsBeanutils1、回显方式 TomcatEcho：

![Shiro 工具检测](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccicd2USbhicqAMjefcJDfZp7X4cPtL5ibuz4ArVofNIdmG3jiaUxd7RCw3MaiaYiavicibpdq1nibsNI1p9vzL2pXSB86Fb5CrrCsNMkJZ4/640?wx_fmt=png&from=appmsg)

通过命令执行功能执行【export】，输出中包含 KUBERNETES\_SERVICE\_HOST=10.96.0.1、KUBERNETES\_SERVICE\_PORT=443 等环境变量，说明当前 shell 大概率处于 K8s 集群当中：

![export 环境变量](https://mmbiz.qpic.cn/sz_mmbiz_png/wXKQNXqMiccicY5n0dvElUDXaak1brliaSIGTwXy3nl4pHjugzAHpBVOJyCIjeMLJRTevVAhpBFSYJXxRoDYCliaaCAibnBhB2Zd7icoeQl3QwNUQ/640?wx_fmt=png&from=appmsg)

执行【hostname -I】命令，无论执行多少次，结果始终为 10.244.2.3，说明当前只有一个业务 Pod 在响应：

![hostname -I 固定 IP](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMicc9nf71sd3a6ysDgdXaRft9JGKytM0DkmfkVRDsdWjsaY2DQYsbFqeLbhSaaR53zREonnGdQS6LicJdzxWPlazGFrlRM4zQIBJE8/640?wx_fmt=png&from=appmsg)

7. 主节点执行回收命令

```
kubectl delete -f shiro.yaml
```

![kubectl delete 回收环境](https://mmbiz.qpic.cn/mmbiz_png/wXKQNXqMiccibOUBPaturUE2mb5aBFqQep2CRpwztcpDvZrgYyvibe35oO23FxodsFnUHcibp2v8cnJn6zBT9viaLNfVllKr1T9lYZBKBm5cCeSo/640?wx_fmt=png&from=appmsg)

8. 修改 shiro.yaml，将副本数量改为 3（replicas: 3）

```
apiVersion: apps/v1 # 指定 API 版本kind: Deployment # 定义资源类型为 Deploymentmetadata:  name: shiro-deploymentspec:  replicas: 3 # 设置副本数量为 3，确保 Pod 分布到多个节点  selector:    matchLabels:      app: shiro  template:    metadata:      labels:        app: shiro    spec:      containers:      - name: shiro        image: vulhub/shiro:1.2.4        imagePullPolicy: IfNotPresent # 仅在本地镜像不存在时拉取        ports:        - containerPort: 8080---apiVersion: v1kind: Servicemetadata:  name: shiro-servicespec:  type: NodePort  selector:    app: shiro  ports:    - port: 8080      targetPort: 8080      nodePort: 30011
```

9. 主节点重新部署服务

```
kubectl apply -f shiro.yaml
```

10. 再次利用并多次执行【hostname -I】此时 IP 在 10.244.x.x 网段内变动——由于存在多个副本，Service 的访问请求存在负载均衡。若想要获取稳定的控制权限，建议多次写入木马，或直接反弹 shell：

![hostname -I 多 IP 变动](https://mmbiz.qpic.cn/mmbiz_png/wXK...