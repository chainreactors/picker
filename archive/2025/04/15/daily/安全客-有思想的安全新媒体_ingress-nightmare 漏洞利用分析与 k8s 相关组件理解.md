---
title: ingress-nightmare 漏洞利用分析与 k8s 相关组件理解
url: https://www.anquanke.com/post/id/306494
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:10.432546
---

# ingress-nightmare 漏洞利用分析与 k8s 相关组件理解

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# ingress-nightmare 漏洞利用分析与 k8s 相关组件理解

阅读量**208900**

发布时间 : 2025-04-14 15:24:44

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

作者：Clifford[@360SRC](https://github.com/360SRC "@360SRC")

> 作者：Clifford[@360SRC](https://github.com/360SRC "@360SRC")

# 前言

在当今的云计算和微服务架构中，Ingress 控制器作为 Kubernetes 集群的关键组件，负责管理进出集群的流量，而近期，一个与其相关的漏洞席卷了云安全圈，让攻击者能够绕过集群的安全防护，获取 Kubernetes 集群中的敏感数据，甚至接管整个集群，CVSS 评分高达 9.8。更为可怕的是，这个漏洞的影响范围极广，涉及到大量使用 Ingress-nginx 的 k8s 集群，不仅影响企业生产环境，也可能波及到数百万个容器化的应用。

目前该漏洞的 poc 和一键利用脚本，在网上已经公布。我们发现在看似简单的利用中，还有不少坑点。该漏洞不同于普通的 web 漏洞，利用过程比较抽象，不是通过简单的抓包改包等方式就能完成的，并且其中涉及到不少 k8s 集群的概念理解。正好借此漏洞分析的机会，来一起梳理一下 kubernetes 中的相关组件。

对于一键利用的脚本，大家可以参考 [git 项目](https://github.com/Clifford-prog/IngressNightmare-PoC) 。这里我们主要专注于将该漏洞的利用过程中抽象的部分通过一些小技巧透明化，分析一些踩坑点，完整的还原出复现过程，并加深对 k8s 概念的理解，阅读时可以结合 k8s 的[官方文档](https://kubernetes.io/zh-cn/docs)来理解。

# 漏洞原理

顾名思义，ingress-nightmare ，这是一个和 ingress 相关的漏洞。这里会有疑问，ingress 是什么呢？[官方文档](https://kubernetes.io/zh-cn/docs/concepts/services-networking/ingress/) 中讲的很详细（ k8s 的官方文档写的和清楚，而且中文翻译的到位，不清楚的概念最好直接看官方文档）。ingress 是 k8s 中的一个组件，而它有一个实现，叫做 ingress-nginx，是通过 nginx 来在集群中实现 ingress 的功能。而这个 ingress-nginx 则是这个漏洞的重点。

当在集群中创建一个 ingress 时，其实是新增了一个 nginx 的配置文件并应用。这里我们思考到，nginx 的配置文件中，可以通过 load\_module，ssl\_engine 等函数来加载动态链接库，如果可以在配置文件中加载一个恶意的动态链接库，就可以实现命令执行的目的。可惜的是，在集群中创建 ingress 是需要高权限的，我们无法直接创建ingress。但 ingress-nginx 有一个接口，该接口在创建 ingress 之前，会先验证 nginx 的配置文件是否正确，实际就是使用 nginx -t 检验配置文件，而这个接口是不需要鉴权的。因此，我们可以构造一个合适的请求发送到这个接口，直接触发检验，从而执行 ssl\_engine 加载恶意的动态链接库实现命令执行。

完成了配置文件的注入，如何将恶意的动态链接库传到 ingress-nginx 的 pod 中呢？这里就需要用到一个针对 nginx 的老方法，nginx 在接受到请求时，如果请求体过大，会将内容保存到临时文件中，等请求处理完后，删除该文件。而在 ingress-nginx 的 pod 中，刚好运行着 nginx 。利用方式就很明确了，首先通过 nginx 保存临时文件的方式上传恶意的 so 文件，再通过构造请求触发 nginx 校验 执行 nginx -t，从而执行 ssl\_engine 加载 so 文件，实现命令执行。接下来，我们就一步步的来研究一下完整的流程。

# 环境准备

在开始之前，先简单准备一下漏洞利用的环境，最好直接在一个 k8s 集群中来实践，如果没有的话也可以用 minikube 来[快速搭建一个简单的集群环境。](https://kubernetes.io/zh-cn/docs/tutorials/hello-minikube/) 我使用的环境中，ingress-nginx 的版本为 1.9.4，使用 1.11.5 以下的版本（以上的版本修复了），不同的版本可能有差异，但相信看完之后也可以自己处理这些问题。

前面一直提到 ingress-nginx ，这里我们来看看它具体是什么。ingress-nginx 在集群中体现出来就是一个 pod，这个 pod 可能属于 daemonset 或者 deployment，但功能都是一样的。在这个 pod 中，运行了两个关键的服务。一个是 nginx，了解了 ingress 后会理解，ingress 实际上是在做流量转发，而 ingress-nginx 作为它的实现，就是通过 nginx 来实现流量转发的功能。第二个服务叫做 ingress-nginx-controller，这个服务用来接受 apiserver 的请求并控制 nginx。简单来说就是，在集群中创建一个 ingress 时，apiserver 会发送请求到 ingress-nginx-controller， ingress-nginx-controller 根据这个请求内容生成相应的 nginx 配置，应用到 nginx 上来实现流量转发逻辑的更新，当删除或修改 ingress 时同理。

# 利用探索

## 1. 校验请求构造

首先，为了触发 nginx 检验配置文件，先来看看这里的检验具体是怎么样的。从正常情况开始考虑，我们通过命令创建一个 ingress 。

```
kubectl apply -f ./ingress.yaml
```

**ingress.yaml**

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-ingress
  annotations:
    nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"
    nginx.ingress.kubernetes.io/auth-tls-secret: "default/ca-secret"
    nginx.ingress.kubernetes.io/auth-tls-error-page: "https://example.com/403"
spec:
  ingressClassName: nginx
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app-service
                port:
                  number: 80
```

当创建 ingress时，apiserver 会先给 ingress-nginx-controller 的校验接口发送一个请求，ingress-nginx-controller 根据内容生成配置文件并校验，然后 apiserver 发送应用请求给 ingress-nginx-controller 实现 ingress 创建，这里只关注校验的过程。所以我们的目的是构造一个校验请求，在其中植入恶意代码发送给 ingress-nginx-controller。而构造这个请求便是第一个难点。由于请求是在集群内，直接通过 apiserver 发给 ingress-nginx-controller 的，不能通过常规的抓包手段拿到请求内容，不知道请求格式也就无法构建请求。

这里需要理解以下 apiserver 是怎么发送请求给 ingress-nginx-controller 的。这个涉及到 k8s 中的另一个概念， [service](https://kubernetes.io/zh-cn/docs/concepts/services-networking/service/) （这里刚接触集群的同学可以关注一下，为什么在集群里请求服务需要用 service 这个概念，而不直接用 ip 加端口来请求）。apiserver 通过将请求发送给 service，由 service 转发给 ingress-nginx-controller。

```
kubectl get svc -n ingress-nginx
```

可以看到 ingress-nginx 的命名空间下有两个 service。
![]()
其中 ingress-nginx-controller-admission 便是将校验请求转发到 ingress-nginx-controller 的。通过这个命令可以看看 service 的详细内容。

```
 kubectl get svc -n ingress-nginx ingress-nginx-controller -o yaml | less
```

![]()
通过 selector 选择了 ingress-nginx-controller 的 pod，将 443 端口的流量转发到 webhook 端口。看看 pod 的配置，定义了 webhook 代表 8443 端口。也就是这个校验接口开放在 pod 的 8443 端口上。如果要获取请求内容，可以抓取这个端口上的请求就可以了

```
kubectl get pods -n ingress-nginx ingress-nginx-controller-m45pv -o yaml | less
```

![]()
但需要注意，这里是 https，要抓包的话还需要加载证书。在 ingress-nginx 的 pod 中可以看到启动命令。其中指定了端口和证书地址，直接加载这些证书即可。于是思路是，进入这个 pod，停掉原本的 nginx-ingress-controller（为了避免端口冲突）,开启抓包软件监听 8443 端口（可以简单的写一个 https 服务，直接输出请求体即可）并加载这些证书，然后用命令创建 一个 ingress 即可获取到请求。

这里提供一个[用 go 实现的简单的 https 服务。](https://github.com/Clifford-prog/IngressNightmare-PoC/blob/main/catch.go)

![]()
但实际操作会发现，在 pod 中停掉 nginx-ingress-controller 这个进程，会导致 pod 直接重启。这是因为 pod 设置了 [存活检测 livenessProbe](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)。于是换一个思路，既然 apiserver 是发送请求到 service，service 转发到 nginx-ingress-controller 的 8443 端口，那直接修改 service 的配置，让它转发请求到 7443 端口，而我们的抓包服务运行到 pod 中的 7443 端口上，就不会发生端口冲突，并且能接受数据。也可以通过修改 pod 的配置，关掉存活检测来防止重启，可以研究试试。注意这些修改在完成抓包后要立刻恢复，不然会影响 ingress 的正常创建。

```
kubectl edit svc ingress-nginx-controller-admission -n ingress-nginx
```

修改 webhook 为 7443。

![]()
抓到的请求包如下。

```
{"kind":"AdmissionReview","apiVersion":"admission.k8s.io/v1","request":{"uid":"a6432f64-2306-45cd-986f-eacd8f3b6109","kind":{"group":"networking.k8s.io","version":"v1","kind":"Ingress"},"resource":{"group":"networking.k8s.io","version":"v1","resource":"ingresses"},"requestKind":{"group":"networking.k8s.io","version":"v1","kind":"Ingress"},"requestResource":{"group":"networking.k8s.io","version":"v1","resource":"ingresses"},"name":"secure-ingress","namespace":"default","operation":"CREATE","userInfo":{"username":"kubernetes-admin","groups":["system:masters","system:authenticated"]},"object":{"kind":"Ingress","apiVersion":"networking.k8s.io/v1","metadata":{"name":"secure-ingress","namespace":"default","uid":"044a82d0-f873-44b9-9654-ff3f8d999c2c","generation":1,"creationTimestamp":"2025-04-01T13:22:59Z","annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"networking.k8s.io/v1\",\"kind\":\"Ingress\",\"metadata\":{\"annotations\":{\"nginx.ingress.kubernetes.io/auth-tls-error-page\":\"https://example.com/403\",\"nginx.ingress.kubernetes.io/auth-tls-match-cn\":\"user1.example.com\",\"nginx.ingress.kubernetes.io/auth-tls-verify-client\":\"on\"},\"name\":\"secure-ingress\",\"namespace\":\"default\"},\"spec\":{\"ingressClassName\":\"nginx\",\"rules\":[{\"host\":\"example.com\",\"http\":{\"paths\":[{\"backend\":{\"service\":{\"name\":\"my-app-service\",\"port\":{\"number\":80}}},\"path\":\"/\",\"pathType\":\"Prefix\"}]}}]}}\n","nginx.ingress.kubernetes.io/auth-tls-error-page":"https://example.com/403","nginx.ingress.kubernetes.io/auth-tls-match-cn":"user1.example.com","nginx.ingress.kubernetes.io/auth-tls-verify-client":"on"},"managedFields":[{"manager":"kubectl-client-side-apply","operation":"Update","apiVersion":"networking.k8s.io/v1","time":"2025-04-01T13:22:59Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{},"f:nginx.ingress.kubernetes.io/auth-tls-error-page":{},"f:nginx.ingress.kubernetes.io/auth-tls-match-cn":{},"f:nginx.ingress.kubernetes.io/auth-tls-verify-client":{}}},"f:spec":{"f:ingressClassName":{},"f:rules":{},f:ingressClassName":{}}}}]},"spec":{"ingressClassName":"nginx","rules":[{"host":"example.com","http":{"paths":[{"path":"/","pathType":"Prefix","backend":{"service":{"name":"my-app-service","port":{"number":80}}}}]}}]},"status":{"l...