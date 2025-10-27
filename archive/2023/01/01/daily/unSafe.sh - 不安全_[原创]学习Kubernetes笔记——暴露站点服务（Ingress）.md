---
title: [原创]学习Kubernetes笔记——暴露站点服务（Ingress）
url: https://buaq.net/go-143565.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:22.815428
---

# [原创]学习Kubernetes笔记——暴露站点服务（Ingress）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

[原创]学习Kubernetes笔记——暴露站点服务（Ingress）

apiVersion: v1kind: ServiceAccountmetadata:  labels:    helm.sh/chart: ingress-nginx-4.0.1    app.ku
*2022-12-31 14:56:54
Author: [bbs.pediy.com(查看原文)](/jump-143565.htm)
阅读量:19
收藏*

---

`apiVersion: v1`

`kind: ServiceAccount`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx`

`namespace: ingress``-``nginx`

`automountServiceAccountToken: true`

`-``-``-`

`apiVersion: v1`

`kind: ConfigMap`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx``-``controller`

`namespace: ingress``-``nginx`

`data:`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: ClusterRole`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`name: ingress``-``nginx`

`rules:`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `configmaps`

`-` `endpoints`

`-` `nodes`

`-` `pods`

`-` `secrets`

`verbs:`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `nodes`

`verbs:`

`-` `get`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `services`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingresses`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `events`

`verbs:`

`-` `create`

`-` `patch`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingresses``/``status`

`verbs:`

`-` `update`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingressclasses`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: ClusterRoleBinding`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`name: ingress``-``nginx`

`roleRef:`

`apiGroup: rbac.authorization.k8s.io`

`kind: ClusterRole`

`name: ingress``-``nginx`

`subjects:`

`-` `kind: ServiceAccount`

`name: ingress``-``nginx`

`namespace: ingress``-``nginx`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: Role`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx`

`namespace: ingress``-``nginx`

`rules:`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `namespaces`

`verbs:`

`-` `get`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `configmaps`

`-` `pods`

`-` `secrets`

`-` `endpoints`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `services`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingresses`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingresses``/``status`

`verbs:`

`-` `update`

`-` `apiGroups:`

`-` `networking.k8s.io`

`resources:`

`-` `ingressclasses`

`verbs:`

`-` `get`

`-` `list`

`-` `watch`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `configmaps`

`resourceNames:`

`-` `ingress``-``controller``-``leader`

`verbs:`

`-` `get`

`-` `update`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `configmaps`

`verbs:`

`-` `create`

`-` `apiGroups:`

`-` `''`

`resources:`

`-` `events`

`verbs:`

`-` `create`

`-` `patch`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: RoleBinding`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx`

`namespace: ingress``-``nginx`

`roleRef:`

`apiGroup: rbac.authorization.k8s.io`

`kind: Role`

`name: ingress``-``nginx`

`subjects:`

`-` `kind: ServiceAccount`

`name: ingress``-``nginx`

`namespace: ingress``-``nginx`

`-``-``-`

`apiVersion: v1`

`kind: Service`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx``-``controller``-``admission`

`namespace: ingress``-``nginx`

`spec:`

`type``: ClusterIP`

`ports:`

`-` `name: https``-``webhook`

`port:` `443`

`targetPort: webhook`

`appProtocol: https`

`selector:`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``component: controller`

`-``-``-`

`apiVersion: v1`

`kind: Service`

`metadata:`

`annotations:`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``description: NGINX Ingress Controller`

`load balancer`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``name: nginx``-``ingress``-``controller`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``service``-``healthcheck``-``interval:` `10s`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``service``-``healthcheck``-``mode: tcp`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``service``-``healthcheck``-``retries:` `'1'`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``service``-``healthcheck``-``timeout:` `3s`

`service.beta.kubernetes.io``/``exoscale``-``loadbalancer``-``service``-``strategy: source``-``hash`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``version:` `1.0``.``0`

`app.kubernetes.io``/``managed``-``by: Helm`

`app.kubernetes.io``/``component: controller`

`name: ingress``-``nginx``-``controller`

`namespace: ingress``-``nginx`

`spec:`

`type``: LoadBalancer`

`externalTrafficPolicy: Local`

`ports:`

`-` `name: http`

`port:` `80`

`protocol: TCP`

`targetPort: http`

`appProtocol: http`

`-` `name: https`

`port:` `443`

`protocol: TCP`

`targetPort: https`

`appProtocol: https`

`selector:`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io``/``component: controller`

`-``-``-`

`apiVersion: apps``/``v1`

`kind: DaemonSet`

`metadata:`

`labels:`

`helm.sh``/``chart: ingress``-``nginx``-``4.0``.``1`

`app.kubernetes.io``/``name: ingress``-``nginx`

`app.kubernetes.io``/``instance: ingress``-``nginx`

`app.kubernetes.io`...