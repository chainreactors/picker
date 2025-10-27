---
title: [原创]学习Kubernetes笔记——kubeadm安装Kubernetes
url: https://buaq.net/go-143569.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:23.759399
---

# [原创]学习Kubernetes笔记——kubeadm安装Kubernetes

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

[原创]学习Kubernetes笔记——kubeadm安装Kubernetes

apiVersion: v1kind: Namespace metadata:  name: kubernetes-dashboard---apiVersion: v1kind: ServiceAcc
*2022-12-31 14:56:54
Author: [bbs.pediy.com(查看原文)](/jump-143569.htm)
阅读量:19
收藏*

---

`apiVersion: v1`

`kind: Namespace`

`metadata:`

`name: kubernetes``-``dashboard`

`-``-``-`

`apiVersion: v1`

`kind: ServiceAccount`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`-``-``-`

`kind: Service`

`apiVersion: v1`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`spec:`

`ports:`

`-` `port:` `443`

`targetPort:` `8443`

`selector:`

`k8s``-``app: kubernetes``-``dashboard`

`-``-``-`

`apiVersion: v1`

`kind: Secret`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard``-``certs`

`namespace: kubernetes``-``dashboard`

`type``: Opaque`

`-``-``-`

`apiVersion: v1`

`kind: Secret`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard``-``csrf`

`namespace: kubernetes``-``dashboard`

`type``: Opaque`

`data:`

`csrf: ""`

`-``-``-`

`apiVersion: v1`

`kind: Secret`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard``-``key``-``holder`

`namespace: kubernetes``-``dashboard`

`type``: Opaque`

`-``-``-`

`kind: ConfigMap`

`apiVersion: v1`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard``-``settings`

`namespace: kubernetes``-``dashboard`

`-``-``-`

`kind: Role`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`rules:`

`-` `apiGroups: [""]`

`resources: [``"secrets"``]`

`resourceNames: [``"kubernetes-dashboard-key-holder"``,` `"kubernetes-dashboard-certs"``,` `"kubernetes-dashboard-csrf"``]`

`verbs: [``"get"``,` `"update"``,` `"delete"``]`

`-` `apiGroups: [""]`

`resources: [``"configmaps"``]`

`resourceNames: [``"kubernetes-dashboard-settings"``]`

`verbs: [``"get"``,` `"update"``]`

`-` `apiGroups: [""]`

`resources: [``"services"``]`

`resourceNames: [``"heapster"``,` `"dashboard-metrics-scraper"``]`

`verbs: [``"proxy"``]`

`-` `apiGroups: [""]`

`resources: [``"services/proxy"``]`

`resourceNames: [``"heapster"``,` `"http:heapster:"``,` `"https:heapster:"``,` `"dashboard-metrics-scraper"``,` `"http:dashboard-metrics-scraper"``]`

`verbs: [``"get"``]`

`-``-``-`

`kind: ClusterRole`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`rules:`

`-` `apiGroups: [``"metrics.k8s.io"``]`

`resources: [``"pods"``,` `"nodes"``]`

`verbs: [``"get"``,` `"list"``,` `"watch"``]`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: RoleBinding`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`roleRef:`

`apiGroup: rbac.authorization.k8s.io`

`kind: Role`

`name: kubernetes``-``dashboard`

`subjects:`

`-` `kind: ServiceAccount`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`-``-``-`

`apiVersion: rbac.authorization.k8s.io``/``v1`

`kind: ClusterRoleBinding`

`metadata:`

`name: kubernetes``-``dashboard`

`roleRef:`

`apiGroup: rbac.authorization.k8s.io`

`kind: ClusterRole`

`name: kubernetes``-``dashboard`

`subjects:`

`-` `kind: ServiceAccount`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`-``-``-`

`kind: Deployment`

`apiVersion: apps``/``v1`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`name: kubernetes``-``dashboard`

`namespace: kubernetes``-``dashboard`

`spec:`

`replicas:` `1`

`revisionHistoryLimit:` `10`

`selector:`

`matchLabels:`

`k8s``-``app: kubernetes``-``dashboard`

`template:`

`metadata:`

`labels:`

`k8s``-``app: kubernetes``-``dashboard`

`spec:`

`securityContext:`

`seccompProfile:`

`type``: RuntimeDefault`

`containers:`

`-` `name: kubernetes``-``dashboard`

`image: kubernetesui``/``dashboard:v2.``5.0`

`imagePullPolicy: Always`

`ports:`

`-` `containerPort:` `8443`

`protocol: TCP`

`args:`

`-` `-``-``auto``-``generate``-``certificates`

`-` `-``-``namespace``=``kubernetes``-``dashboard`

`volumeMounts:`

`-` `name: kubernetes``-``dashboard``-``certs`

`mountPath:` `/``certs`

`-` `mountPath:` `/``tmp`

`name: tmp``-``volume`

`livenessProbe:`

`httpGet:`

`scheme: HTTPS`

`path:` `/`

`port:` `8443`

`initialDelaySeconds:` `30`

`timeoutSeconds:` `30`

`securityContext:`

`allowPrivilegeEscalation: false`

`readOnlyRootFilesystem: true`

`runAsUser:` `1001`

`runAsGroup:` `2001`

`volumes:`

`-` `name: kubernetes``-``dashboard``-``certs`

`secret:`

`secretName: kubernetes``-``dashboard``-``certs`

`-` `name: tmp``-``volume`

`emptyDir: {}`

`serviceAccountName: kubernetes``-``dashboard`

`nodeSelector:`

`"kubernetes.io/os"``: linux`

`tolerations:`

`-` `key: node``-``role.kubernetes.io``/``master`

`effect: NoSchedule`

`-``-``-`

`kind: Service`

`apiVersion: v1`

`metadata:`

`labels:`

`k8s``-``app: dashboard``-``metrics``-``scraper`

`name: dashboard``-``metrics``-``scraper`

`namespace: kubernetes``-``dashboard`

`spec:`

`ports:`

`-` `port:` `8000`

`targetPort:` `8000`

`selector:`

`k8s``-``app: dashboard``-``metrics``-``scraper`

`-``-``-`

`kind: Deployment`

`apiVersion: apps``/``v1`

`metadata:`

`labels:`

`k8s``-``app: dashboard``-``metrics``-``scraper`

`name: dashboard``-``metrics``-``scraper`

`namespace: kubernetes``-``dashboard`

`spec:`

`replicas:` `1`

`revisionHistoryLimit:` `10`

`selector:`

`matchLabels:`

`k8s``-``app: dashboard``-``metrics``-``scraper`

`template:`

`metadata:`

`labels:`

`k8s``-``app: dashboard``-``metrics``-``scraper`

`spec:`

`securityContext:`

`seccompProfile:`

`type``: RuntimeDefault`

`containers:`

`-` `name: dashboard``-``metrics``-``scraper`

`image: kubernetesui``/``metrics``-``scraper:v1.``0.7`

`ports:`

`-` `containerPort:` `8000`

`protocol: TCP`

`livenessProbe:`

`httpGet:`

`scheme: HTTP`

`path:` `/`

`port:` `8000`

`initialDelaySeconds:` `30`

`timeoutSeconds:` `30`

`volumeMounts:`

`-` `mountPath:` `/``tmp`

`name: tmp``-``volume`

`securityContext:`

`allowPrivilegeEscalation: false`

`readOnlyRootFilesystem: true`

`runAsUser:` `1001`

`runAsGroup:` `2001`

`serviceAccountName: kubernetes``-``dashboard`

`nodeSelector:`

`"kubernetes.io/os"``: linux`

`tolerations:`

`-` `key: node``-``role.kubernetes.io``/``master`

`effect: NoSchedule`

`volumes:`

`-` `name: tmp``-``volume`

`emptyDir: {}`

文章来源: https://bbs.pediy.com/thread-275685.htm
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)