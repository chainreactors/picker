---
title: Kubernetes RBAC 最佳安全实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247509700&idx=1&sn=b946f830ca55b21eb4a8b7db9ec31fe5&chksm=e9d36d26dea4e43007a4e848a65ec4a7d4d18960a250d03e0fbefb77aab34f9ea195e2bbd5cb&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-28
fetch_date: 2025-10-06T18:05:04.050103
---

# Kubernetes RBAC 最佳安全实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjYjz8xfopAlRtibAmEgibFeg32xcficpoL89IdbM1AA1lU4EnRW6WAyvfLoFrSVPAQfQyMWf6VPBGlQ/0?wx_fmt=jpeg)

# Kubernetes RBAC 最佳安全实践

韦伟、李昌昊

字节跳动技术团队

# **「引言」**

Kubernetes 是一个开源的容器编排平台，用于自动化部署、扩展和管理容器化应用程序。它提供了丰富的功能，如服务发现、负载均衡、自动缩放等。随着 Kubernetes 在云原生领域的广泛应用，**「有效管理谁可以对 Kubernetes 集群执行何种操作变得至关重要」**。本文将简要介绍 Kubernetes的认证与授权体系以及RBAC授权原理。通过实际案例展示RBAC管理不当可能导致的安全风险，然后向大家分享RBAC安全研发与运维的最佳实践，以及我们在字节跳动内部的安全防护和治理经验。

# 背景知识

> ❝
>
> 如果您对相关背景知识比较了解，可直接跳转到“RBAC 安全风险剖析”、“RBAC 安全研发与运维最佳实践” 章节阅读。
>
> ❞

本章节将对 Kubernetes 的认证和授权体系进行概述，了解这些机制的原理有助于理解不同场景下集群权限的安全风险。特别是那些能够被轻易利用的未授权访问漏洞，以及那些容易被忽视的权限提升与横向移动攻击风险。

## Kubernetes 认证与授权体系

Kubernetes 的认证与授权体系主要用于满足对关键服务 API（API Server、Kubelet Server）的访问控制。在经过多年的发展后，Kubernetes 已经实现了一套比较完善的认证与授权机制，可以满足用户大多数场景的使用需求。

**「API Server」**

Kubernetes 是一个以容器技术为基础，以声明式 API Server 为核心的分布式容器编排系统。Kubernetes 几乎所有的功能都通过 API Server 对外暴露。而 API Server 支持了多种认证机制，内置了多种授权模式和准入控制器，允许用户根据需要灵活配置和使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegAFkmbuVvwbdWyA1MlaicCEN7GKSTdn1AyLhjvc030Y3icwVz2iaXL8kcQ/640?wx_fmt=png&from=appmsg)

简单来说，当一个用户访问 Kubernetes 的 API Server 时，API Server 会使用启用的认证器依次对请求进行身份认证，API Server 使用第一个成功认证的身份来标识请求者；然后再使用启用的授权器依次对请求进行授权策略的检查，当有任意一个授权器显式地允许、拒绝一个请求时，则立刻返回当前授权结果（如果没有授权器显式地授权，那么请求也将被拒绝）。除此之外，在 API Server 真正处理请求前，它还会使用启用的准入控制器对请求进一步变异和验证。只有所有的准入控制器都验证通过后，请求才会被真正处理。

> ❝
>
> 注意：API Server 不保证认证器和准入控制器的执行顺序，但会按照授权模式的配置顺序进行鉴权。
>
> ❞

**「Kubelet****Server」**

Kubernetes 中还有一个非常重要的组件，那就是 Kubelet。它充当了分布式系统中的 Agent 角色，并使用节点专属的用户证书访问 API Server，管理节点上的资源。但 Kubelet 自身也会作为服务端，对外提供服务。从而实现在容器内执行命令、获取指标信息、容器日志、宿主机日志等功能。

Kubernetes 也为 Kubelet Server 提供了多种认证和授权模式。值得一提的是其中的 webhook 认证和 webhook 授权，它们本质上是向 API Server 发送 TokenReview 和 SubjectAccessReview 请求，对客户端的身份进行认证与授权。

**「小结」**

Kubernetes 为 API Server 和 Kubelet Server 支持了多种认证机制、授权机制、准入控制器，以及灵活的自定义接口。这些机制虽然能够满足各种用户需求，但也给用户带来了困扰。因为如果不了解这些机制的原理和负面影响，就很容易为集群引入安全风险和入侵检测盲点。特别是那些能够被轻易利用的未授权访问漏洞，以及那些容易被忽视的提权与横向移动攻击风险。

请参见附录和参考文献，了解更多 API Server 和 Kubelet Server 的认证、授权、准入控制的技术细节。

## Kubernetes RBAC 授权原理

RBAC 是 Kubernetes 默认启用的授权机制，也是 Kubernetes 核心组件所使用的授权机制。用户在使用集群时，往往需要使用 RBAC 授权机制来为其用户账号授权，以便部署、运维工作负载及所需的各种资源。各类云原生应用的 Operator、Controller 往往也需要利用 RBAC 授权机制来为其服务账户授权，以确保它们能够访问必要的资源，从而实现其功能。

下面的示意图展示了用户账号和服务账号访问 API Server 时的认证、授权、准入控制过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegwP3PgTZDqq75Y2qKtcD3rBg9hlUfOH9yk1qsLiaWRKFVPwicghTMIUSw/640?wx_fmt=png&from=appmsg)

在 Kubernetes 的 RBAC 授权体系中，引入了以下几种概念：

* **「Subject」**

在 Kubernetes 环境中有三类 Subject 可以被授予 RBAC 角色权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegpicH6ZMeQXeG4mILzUQBKGxK5sMibNXk8FtL2SOCxcl5sB4xYGDy27Uw/640?wx_fmt=png&from=appmsg)

* **「Rule」**

用于在 `Role`, `ClusterRole` 内部定义具体权限，每一个 rule 都可以通过 apiGroups, resources, resourcesName, verbs, nonResourceURLs 来定义允许对什么资源（API 组，资源类型，资源名称 ）执行什么操作（动词）。

注意：rule中的apiGroups, resources, resourcesNames, verbs, nonResourceURLs 支持使用通配符

* **「Role & ClusterRole」**

+ `Role` 用来定义当前命名空间范围内资源的角色，它通过 `Rules` 显式地定义权限。
+ `ClusterRole` 用来定义集群范围内资源的角色，它通过 `Rules` 显式地定义权限。

* **「Role & ClusterRoleBinding」**

+ `RoleBinding` 将某个 `ClusterRole` 或当前命名空间中的某个 `Role` 绑定到 subjects，使 subjects 获得当前命名空间中的 `ClusterRole`、`Role`所定义的角色权限，例如可以在命名空间 A 中创建 RoleBinding，将命名空间 A 中的 Role 与命名空间 B 中的 ServiceAccount 绑定。那么命名空间 B 中的 ServiceAccount 将获得命名空间 A 中的 Role 定义的权限。
+ `ClusterRoleBinding` 将某个 `ClusterRole` 绑定到 subjects，使 subjects 获得 `ClusterRole` 所定义的角色权限。

由以上可知，`Role` 和 `ClusterRole` 内的 `rules` 代表一系列显式授予的权限，遵从 Deny-by-Default 安全模型。由于不支持 "deny" 规则，因而不支持显式的排除某些权限。

这一特点使得某些应用场景无法利用 RBAC 授权机制实现：在授予所有已知、未知 CRD 资源操作权限的同时，显式地排除某些敏感权限。但我们可以借助 ABAC、Webhook 授权模式，结合准入控制器来为此类场景的服务账号进行权限管理，从而缓解这类问题。

下面是一个通过 RBAC 授权机制为 ServiceAccount 绑定权限的示例：

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: example-clusterrole
  namespace: example-ns
rules:
- apiGroups:
  - apps
  resources:
  - daemonsets
  - deployments
  - replicasets
  - statefulsets
  resourcesNames:
  - test
  verbs:
  - '*'
- nonResourceURLs:
  - /healthz
  - /healthz/*
  verbs:
  - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: example-rolebinding
  namespace: example-ns
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: example-clusterrole
subjects:
- kind: ServiceAccount
  name: example-sa
  namespace: example-ns
```

# RBAC 安全风险剖析

Kubernetes 是一个分布式的容器编排系统。除了要确保 Kubernetes 基础组件的配置安全（例如 API Server、Kubelet Server 基本的认证授权配置等，对应 CIS Kubernetes Benchmark 中的第一至第四章中的要求）外，我们还需要对其 RBAC 授权配置进行精细化管理。

正确的授予主体 RBAC 权限能够避免为集群引入不必要的稳定性 & 安全性风险，而不恰当的权限设置可能导致敏感数据泄露、资源滥用、权限提升，甚至威胁整个集群的安全。接下来我们将借助文献和案例来进一步说明其安全风险。

## 概述

在 Kubernetes 中，可以通过对资源的操作来实现信息窃取、权限提升、横向移动等攻击。例如可以利用 pods/exec 资源的 create 权限通过 API Server 在指定容器内执行任意命令，也可以利用 nodes/proxy 资源的 create 权限直接访问 Kubelet Server 在指定容器内执行任意命令，还可以利用 pods 的 create 权限创建具有安全风险的容器、利用 pods 的 patch 权限在指定 Pod 的容器内执行代码......**「随着 Kubernetes 的广泛使用，此类风险在云厂商、****PaaS****平台、****云原生****应用、****SaaS****产品中愈演愈烈，轻则被用于后渗透入侵，重则会给产品引入安全漏洞。」**

Palo Alto Networks 的安全研究员深入分析了 Kubernetes 中的所有敏感权限，并根据其危害类型将其分类和分级[2]（严重等级请参考开源项目 rbac-police 的风险权限扫描策略集[3]）。如下图所示，在这些敏感权限中，有许多都可以被攻击者用于信息泄漏、权限提升、横向移动等攻击，最终实现整个集群的接管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegtzbicEOHOZu0Q7HrwkOh6AnSlsXgtqtgovmB4ssySZLichFZ41E7owUA/640?wx_fmt=png&from=appmsg)

Palo Alto Networks 的研究结果表明，在针对主流公有云、CNI 厂商的分析中，有将近 50% 的厂商存在容器逃逸后轻易导致集群沦陷的安全问题。另外有 25% 的厂商存在容器逃逸后在一定条件下导致集群沦陷的安全风险[2]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegTlyvLicxr2CkOpg1IzYPAsGESJ7MyCiaGS5RCSel2nuwFicwx3HwRB2mQ/640?wx_fmt=png&from=appmsg)

## 公开案例

* RBAC Buster：来自 Aqua Sec 的研究者通过蜜罐首次捕获到利用 Kubernetes 的 RBAC 配置漏洞进行攻击的行为，黑客通过创建后门访问集群，导致未授权访问和数据泄露的风险。详见 First-Ever Attack Leveraging Kubernetes RBAC to Backdoor Clusters[5]
* Sys:All：研究团队 The Orca Research Pod 扫描了 250,000 个 GKE 集群（约总数的 2%），发现其中 1300 个集群存在错误配置的角色绑定，其中有 108 个集群允许攻击者使用任何有效的谷歌帐号接管集群。详见：How A Simple Loophole in Google Kubernetes Engine Puts Clusters at Risk of Compromise[6] & GCP-2024-003 security-bulletins[7]
* 在 OWASP Kubernetes Top 10 安全风险中，RBAC 配置错误导致的“权限过多”问题排名第三，可能引发未授权操作和权限提升。详见 OWASP Kubernetes Top 10[8]

## 风险示例

下面的示例演示了攻击者可以利用任意 secrets 的 create 权限，来获取了包含敏感权限的 ServiceAccount（这里以窃取 prometheus-agent SA 的 token 为例）的 token。对此，我们建议使用专用命名空间中的 Role 来定义所需权限，从而与 kube-system 等敏感命名空间隔离。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5EcwYhllQOjYjz8xfopAlRtibAmEgibFeg8eLYCsLSQs08HaqlbBoPL5Ks8ibW8uIwMQbhLLd8bIJF4hhGJtC7CHg/640?wx_fmt=gif&from=appmsg)

下面的示例演示了攻击者可以利用任意 secrets 的 get 权限，来爆破获取保存 SA token 的 secrets。虽然爆破 SA token 需要较长时间（爆破一个拥有 5 个随机字符串的 SA token 最多需要 27^5 次），但此权限也可能被用于窃取其他已知名称的 secrets 资源。对此，我们建议使用 Role 定义角色，或者通过 resourceNames 对 secrets 的权限范围进行约束，而非授予全部命名空间中任意 secrets 的 get 权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5EcwYhllQOjYjz8xfopAlRtibAmEgibFeg30czibC4SLlRSD82DF3KXvdzvpwMnQpLagKlQXGJwpC4icCaKo4ye9TA/640?wx_fmt=gif&from=appmsg)

以上数据和案例表明，Kubernetes RBAC 权限管理已成为一个必须认真对待并及时采取有效防御措施的安全问题。

# RBAC 安全研发与运维最佳实践

基于我们在字节跳动内部的安全实践，我们为 RBAC 授权配置总结了如下原则，以指引大家进行 Kubernetes RBAC 权限管理，从而降低由此为集群引入的安全风险。

## 遵循最小权限原则

在 RBAC 角色中分配权限时，请遵循最小权限原则授予执行任务所需的最低权限。例如：

* 优先使用 Role, RoleBinding 授予一个、多个特定命名空间中的权限。
* 定义 rule 时，使用明确的 apiGroups, resources, verbs 以及 resourceNames 来限定权限范围。

> ❝
>
> 注意：
>
> 如果设置了 resourceNames 字段，那么请求权限不能是 list、watch、create、deletecollection，否则请求将不会被允许（**「当使用 resourceNames 限制 list、watch 权限范围时，客户端必须在请求参数中指定 fieldSelector=metadata.name%3D{RESOURCENAME} 用于通过授权」**）。但当 resourceNames 字段中包含 "" 时，将允许 list 请求。
>
> 虽然 RBAC 授权模式不支持通过 resourceNames 来约束 create、deletecollection 权限，但仍然建议通过 resourceNames 来约束 update、patch、get 等权限。
>
> ❞

RBAC 权限最小化不应被视作“非黑即白”，哪怕组件的某些敏感权限无法收敛，最小化权限仍然对降低风险、增加入侵检测的机率有重要作用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOjYjz8xfopAlRtibAmEgibFegwTFW5hyJzVUnRTarNlVSpQvetEa9AbxoQn8CiaRvuHAxXsZmrOIutPw/640?wx_fmt=png&from=appmsg)

## 避免使用默认角色/用户/用户组

一般情况下，Kubernetes 和基于 Kubernetes 的 PaaS 平台会自动将一些默认角色绑定到默认用户和用户组，以保证系统的正常运行。如需查看 Kubernetes 创建的默认角色和绑定的完整列表，请参阅 Defa...