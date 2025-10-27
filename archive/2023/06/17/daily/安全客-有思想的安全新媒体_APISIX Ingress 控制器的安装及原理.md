---
title: APISIX Ingress 控制器的安装及原理
url: https://www.anquanke.com/post/id/289197
source: 安全客-有思想的安全新媒体
date: 2023-06-17
fetch_date: 2025-10-04T11:44:19.913215
---

# APISIX Ingress 控制器的安装及原理

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

# APISIX Ingress 控制器的安装及原理

阅读量**411955**

发布时间 : 2023-06-16 17:50:28

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

简介
APISIX 是动态、实时、高性能的 API 网关。它提供丰富的流量管理功能，比如负载均衡、动态上游、金丝雀发布、熔断、认证、可观测性等。既可以使用 APISIX API 网关处理传统的南北向流量，也可以使用它处理服务间的东西向流量。同时，它也可被用作 Kubernetes Ingress 控制器。
APISIX Ingress 控制器提供 Helm 安装方式，但是使用原生 YAML 安装，更加有助于理解其原理。

使用原生 YAML 安装 APISIX 和 APISIX Ingress 控制器
在本教程中，我们将使用原生 YAML 在 Kubernetes 中安装 APISIX 和 APISIX Ingress 控制器。

先决条件
如果没有 Kubernetes 集群使用，建议使用 kind 创建本地 Kubernetes 集群。

kubectl create ns apisix
在本教程中，我们的所有操作都将在命名空间 apisix 中执行。

ETCD 安装
在这里，我们将在 Kubernetes 集群内部部署不带认证的单节点 ETCD 集群。
在本例中，我们假设你拥有存储部署器。如果你正在使用 Kind，那么将自动创建本地路径部署器。如果没有存储部署器或不想使用持久化存储卷，那么可以使用 emptyDir 作为存储卷。

# etcd-headless.yaml

apiVersion: v1
kind: Service
metadata:
name: etcd-headless
namespace: apisix
labels:
app.kubernetes.io/name: etcd
annotations:
service.alpha.kubernetes.io/tolerate-unready-endpoints: “true”
spec:
type: ClusterIP
clusterIP: None
ports:

```
- name: "client"
  port: 2379
  targetPort: client
- name: "peer"
  port: 2380
  targetPort: peer
```

selector:

```
app.kubernetes.io/name: etcd
```

---

# etcd.yaml

apiVersion: apps/v1
kind: StatefulSet
metadata:
name: etcd
namespace: apisix
labels:
app.kubernetes.io/name: etcd
spec:
selector:
matchLabels:
app.kubernetes.io/name: etcd
serviceName: etcd-headless
podManagementPolicy: Parallel
replicas: 1
updateStrategy:
type: RollingUpdate
template:
metadata:
labels:
app.kubernetes.io/name: etcd
spec:
securityContext:
fsGroup: 1001
runAsUser: 1001
containers:

```
    - name: etcd
      image: docker.io/bitnami/etcd:3.4.14-debian-10-r0
      imagePullPolicy: "IfNotPresent"
      # command:
        # - /scripts/setup.sh
      env:
        - name: BITNAMI_DEBUG
          value: "false"
        - name: MY_POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        - name: MY_POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: ETCDCTL_API
          value: "3"
        - name: ETCD_NAME
          value: "$(MY_POD_NAME)"
        - name: ETCD_DATA_DIR
          value: /etcd/data
        - name: ETCD_ADVERTISE_CLIENT_URLS
          value: "http://$(MY_POD_NAME).etcd-headless.apisix.svc.cluster.local:2379"
        - name: ETCD_LISTEN_CLIENT_URLS
          value: "http://0.0.0.0:2379"
        - name: ETCD_INITIAL_ADVERTISE_PEER_URLS
          value: "http://$(MY_POD_NAME).etcd-headless.apisix.svc.cluster.local:2380"
        - name: ETCD_LISTEN_PEER_URLS
          value: "http://0.0.0.0:2380"
        - name: ALLOW_NONE_AUTHENTICATION
          value: "yes"
      ports:
        - name: client
          containerPort: 2379
        - name: peer
          containerPort: 2380
      volumeMounts:
        - name: data
          mountPath: /etcd
  # If you don't have a storage provisioner or don't want to use persistence volume, you could use an `emptyDir` as follow.
  # volumes:
  #   - name: data
  #     emptyDir: {}
```

volumeClaimTemplates:

```
- metadata:
    name: data
  spec:
    accessModes:
      - "ReadWriteOnce"
    resources:
      requests:
        storage: "8Gi"
```

请注意该 ETCD 安装非常简单，缺乏许多必要的生产特性，仅用于学习场景。如果想部署生产级 ETCD，请参阅 bitnami/etcd。

APISIX 安装
为我们的 APISIX 创建配置文件。我们将部署 2.5 版本的 APISIX。
注意 APISIX Ingress 控制器需要与 APISIX 管理 API 进行通信，因此为进行测试，我们将 apisix.allow\_admin 设置为 0.0.0.0/0。

apiVersion: v1
kind: ConfigMap
metadata:
name: apisix-conf
namespace: apisix
data:
config.yaml: |-
apisix:
node\_listen: 9080 # APISIX listening port
enable\_heartbeat: true
enable\_admin: true
enable\_admin\_cors: true
enable\_debug: false
enable\_dev\_mode: false # Sets nginx worker\_processes to 1 if set to true
enable\_reuseport: true # Enable nginx SO\_REUSEPORT switch if set to true.
enable\_ipv6: true
config\_center: etcd # etcd: use etcd to store the config value

```
  allow_admin:                  # Module ngx_http_access_module
    - 0.0.0.0/0
  port_admin: 9180

  # Default token when use API to call for Admin API.
  # *NOTE*: Highly recommended to modify this value to protect APISIX's Admin API.
  # Disabling this configuration item means that the Admin API does not
  # require any authentication.
  admin_key:
    # admin: can everything for configuration data
    - name: "admin"
      key: edd1c9f034335f136f87ad84b625c8f1
      role: admin
    # viewer: only can view configuration data
    - name: "viewer"
      key: 4054f7cf07e344346cd3f287985e76a2
      role: viewer
  # dns_resolver:
  #   - 127.0.0.1
  dns_resolver_valid: 30
  resolver_timeout: 5

nginx_config:                     # config for render the template to generate nginx.conf
  error_log: "/dev/stderr"
  error_log_level: "warn"         # warn,error
  worker_rlimit_nofile: 20480     # the number of files a worker process can open, should be larger than worker_connections
  event:
    worker_connections: 10620
  http:
    access_log: "/dev/stdout"
    keepalive_timeout: 60s         # timeout during which a keep-alive client connection will stay open on the server side.
    client_header_timeout: 60s     # timeout for reading client request header, then 408 (Request Time-out) error is returned to the client
    client_body_timeout: 60s       # timeout for reading client request body, then 408 (Request Time-out) error is returned to the client
    send_timeout: 10s              # timeout for transmitting a response to the client.then the connection is closed
    underscores_in_headers: "on"   # default enables the use of underscores in client request header fields
    real_ip_header: "X-Real-IP"    # Module ngx_http_realip_module
    real_ip_from:                  # Module ngx_http_realip_module
      - 127.0.0.1
      - 'unix:'

etcd:
  host:
    - "http://etcd-headless.apisix.svc.cluster.local:2379"
  prefix: "/apisix"     # apisix configurations prefix
  timeout: 30   # seconds
plugins:                          # plugin list
  - api-breaker
  - authz-keycloak
  - basic-auth
  - batch-requests
  - consumer-restriction
  - cors
  - echo
  - fault-injection
  - grpc-transcode
  - hmac-auth
  - http-logger
  - ip-restriction
  - jwt-auth
  - kafka-logger
  - key-auth
  - limit-conn
  - limit-count
  - limit-req
  - node-status
  - openid-connect
  - prometheus
  - proxy-cache
  - proxy-mirror
  - proxy-rewrite
  - redirect
  - referer-restriction
  - request-id
  - request-validation
  - response-rewrite
  - serverless-post-function
  - serverless-pre-function
  - sls-logger
  - syslog
  - tcp-logger
  - udp-logger
  - uri-blocker
  - wolf-rbac
  - zipkin
  - traffic-split
stream_plugins:
  - mqtt-proxy
```

请确保 etcd.host 与我们最初创建的无头服务匹配。在我们的例子中，它是 [http://etcd-headless.apisix.svc.cluster.local:2379。](http://etcd-headless.apisix.svc.cluster.local:2379%E3%80%82)

在该配置中，我们在 apisix.admin\_key 部分的下方定义具有 admin 名称的访问密钥。该密钥是我们的 API 密钥，以后将用于控制 APISIX。该密钥是 APISIX 的默认密钥，在生产环境中，应该修改它。

将其保存为 config.yaml，然后运行 kubectl -n apisix create -f config.yaml，创建 ConfigMap。稍后，我们将该 ConfigMap 挂载到 APISIX Deployment 中。

apiVersion: apps/v1
kind: Deployment
metadata:
name: apisix
namespace: apisix
labels:
app.kubernetes.io/name: apisix
spec:
replicas: 1
selector:
matchLabels:
app.kubernetes.io/name: apisix
template:
metadata:
labels:
app.kubernetes.io/name: apisix
spec:
containers:

```
    - name: apisix
      image: "apache/apisix:2.5-alpine"
      imagePullPolicy: IfNotPresent
      ports:
        - name: http
          containerPort: 9080
          protocol: TCP
        - name: tls
          containerPort: 9443
          protocol: TCP
        - name: admin
          containerPort: 9180
          protocol: TCP
      readinessProbe:
        failureThreshold: 6
        initi...