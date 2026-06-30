---
title: K8s 滥用 RBAC 权限实现容器逃逸
url: https://mp.weixin.qq.com/s/LWS5tGoRzvB3rO6plhCUag
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:40.110676
---

# K8s 滥用 RBAC 权限实现容器逃逸

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNgA8clCnqcJZiasDCtzIicHa4zib8ic8tR9YWE7z9SM3xbYy5K9gRGMgneaS45JjcCnPxQmXxbQvId9MszSNS6Jq05xOlB1wOfEno/0?wx_fmt=jpeg)

# K8s 滥用 RBAC 权限实现容器逃逸

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

Kubernetes这东西，这几年火得一塌糊涂，大大小小的公司都在往上面迁。但是有一个数据说出来你可能不太信——超过六七成的K8s集群，存在着至少一项高危的配置方面的问题。注意，我说的不是那种需要很高技术含量才能利用的漏洞，就是单纯的配置没配好，等于门没锁。

之前做过一阵子的K8s安全审计，跑了一圈下来，十个集群里面六七个都有毛病。有的是API Server大敞着门，谁都能过来看看。有的是ServiceAccount权限给得大手大脚的，一个普通Pod拿着的居然是cluster-admin。还有etcd那边，数据裸着跑，连个TLS都没套。

这些可都不是小事。

**这是一个 Kubernetes 的“权限配置错误”导致的特权提升漏洞的漏洞环境搭建过程**

## 环境搭建

```
# 1. 安装 Docker（如果已装可跳过）
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER && newgrp docker

# 2. 安装 kubectl 它是 Kubernetes 的命令行管理工具，用于与集群交互。
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

# 3. 安装 kind 使用 Docker 容器模拟 Kubernetes 节点来运行本地集群的工具
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x kind && sudo mv kind /usr/local/bin/
```

![image-20260626193325670](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNEjMowbj1UzRLLoZFWpEICibu7LbXMhbagfwtNtIged5gPpZKblLyn5MYexaXm0TU40V3TCvibRzhl2Cdyg9vicKdhWDKNw9UVv4/640?wx_fmt=other&from=appmsg)

image-20260626193325670

创建“不安全”集群，使用以下 `kind` 配置文件，**开启 API Server 匿名认证**，并预留 etcd 端口供检查（实际不暴露，但保持结构）。

```
cat > insecure-cluster.yaml <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 6443
        hostPort: 6443
        protocol: TCP
kubeadmConfigPatches:
  - |
    apiVersion: kubeadm.k8s.io/v1beta3
    kind: ClusterConfiguration
    metadata:
      name: config
    etcd:
      local:
        # 保留默认配置，实际上 kind 会自己生成证书，但我们可以查看清单
        dataDir: /var/lib/etcd
  - |
    apiVersion: kubeadm.k8s.io/v1beta3
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  - |
    # 关键：修改 API Server 参数，开启匿名认证
    apiVersion: kubeadm.k8s.io/v1beta3
    kind: ClusterConfiguration
    metadata:
      name: config
    apiServer:
      extraArgs:
        anonymous-auth: "true"
EOF
```

![image-20260627133549553](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauOaxfXFDYbibWyzSQtVHBYeib5PGqj1kNajbe4OaAm0S68V7R8Licib4BVPds3cwq9xnUDQ5N4OdyxtE9Fb6VOUQFVtzDr8daEdQe8/640?wx_fmt=other&from=appmsg)

image-20260627133549553

```
# 创建集群
kind create cluster --name insecure-k8s --config insecure-cluster.yaml
```

![image-20260627133736777](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauPGJnMKobJsfriaYmxQusqErnA8pXHQ3sttlEbiaISsOve76r2OuZ74VdUOQevkGuy1zQHl8C9b3FcOD5ibs7wF9qdlQP86H9cnkY/640?wx_fmt=other&from=appmsg)

image-20260627133736777

```
# 验证集群状态
kubectl cluster-info
kubectl get nodes
```

若出现如下错误

![image-20260627134025810](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNI034XGhlPPz9oKqyHHYs7MdCu1jTRaiatQXibCHjU71bk2y36OIuh0VEXY8naXPkOc6uZa4QzspgCfydzZB72vuOxicHRAVB5nI/640?wx_fmt=other&from=appmsg)

image-20260627134025810

请继续执行命令

```
kubectl config set-cluster kind-insecure-k8s --server=https://127.0.0.1:6443
```

![image-20260627134011962](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMEW9Kk8AOlD2DXQovUdcaLJo8l4eZCTKMtbsEpZPkiaiaQp14eZG8886Uzq3YCiaYSHOqRdh0VJvMREl9EvF5oNvpvlibVrKSRIqU/640?wx_fmt=other&from=appmsg)

image-20260627134011962

重新检测是否正常连接，这时候应该会正常显示连接状态

```
kubectl cluster-info
kubectl get nodes
```

![image-20260627134152823](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauPuuZOn5cdmJmPYedyb9eZm2LfOvS67iapabYhI3Te1j8NvnOVdSBm1zNX9GoYVMuDeabrP7IuZ7CPktqqmLQrA3KAaRxkyH3l8/640?wx_fmt=other&from=appmsg)

image-20260627134152823

模拟“未认证用户获得权限”的问题，创建一个 `ClusterRoleBinding`，将 `system:unauthenticated` 组绑定到 `view` 角色（允许读取所有资源），模拟文中“把 ClusterRole 绑定到了 system:unauthenticated”的场景。

![image-20260627162734761](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOjOZbmP7TmghXm3JzFlHaIhFWe2Syf0B4hfhyHx1cWotsYMzj9XGsj10RpGweNJ2l9LFqMaSiafZj1EEZgU4E3sVhhjiasM2Rds/640?wx_fmt=other&from=appmsg)

image-20260627162734761

模拟“default ServiceAccount 获得 cluster-admin”

![image-20260627162800051](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauMicycpzKPEbxfNibt4CjMIvFCS6YEyyFmwgXCIFd2jaJecbw0SDicp03CpwAT5efvQCuf0lYUbJ9lI8RnukPs3bAHuCUicBuVU4hs/640?wx_fmt=other&from=appmsg)

image-20260627162800051

**模拟通配符权限的角色**

在 `default` 命名空间下创建一个角色，包含 `resources: ["*"]` 和 `verbs: ["get", "list"]`，并绑定给默认 ServiceAccount。

```
# 创建通配符 Role
kubectl create role wide-reader \
  --verb=get,list \
  --resource='*' \
  --namespace=default

# 绑定到 default ServiceAccount
kubectl create rolebinding wide-reader-binding \
  --role=wide-reader \
  --serviceaccount=default:default \
  --namespace=default
```

![image-20260627162948996](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNvOvAvOmY29UMYQOzacfKgfnXKgVZ5YwhExibwEMocn0gv2fUUPnGApVicMvYTQbMnpyn64y1Ij931snDvuJV4067aAJibClcXiaU/640?wx_fmt=other&from=appmsg)

image-20260627162948996

确认环境符合要求

```
kubectl cluster-info dump | grep anonymous-auth
```

![image-20260627163014587](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauN9iat77RRaeWxI3GOUP0LaFBUoxiaB9524SsibhUYmicZia5stJrFBe4QGVkl3pjvDFBicPhMiccKHqZ52LH7ToaFnj2yBo6OByb8uzM/640?wx_fmt=other&from=appmsg)

image-20260627163014587

查看绑定给未认证用户的权限

```
kubectl get clusterrolebindings -o json | \
  jq '.items[] | select(.subjects[]?.kind=="Group" and .subjects[]?.name=="system:unauthenticated")'
```

![image-20260627163112365](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNO98CEH5yUGoF8h8FAfv4Wpw0c7Ric2ynRJMlia715ecNc2FaMqFDFcH85MGjdicEhAfWiaDYzwsoV81FjI29UpDYnjcIKkNvIhcI/640?wx_fmt=other&from=appmsg)

image-20260627163112365

检查 default ServiceAccount 是否拥有 cluster-admin

```
kubectl get clusterrolebindings -o json | \
  jq '.items[] | select(.subjects[]?.kind=="ServiceAccount" and .subjects[]?.name=="default")'
```

![image-20260627163231902](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOSRhsyu7rc5ShgSjQtiab52j7l5o4rJUiaeRn2b1SibCryDchDdxKU0LXk5BYpNjQYRib6W4xj9julgmas5L8G9gBIcHXn20sdlYU/640?wx_fmt=other&from=appmsg)

image-20260627163231902

这种宽泛的权限（`resources: ["*"]`，`verbs: ["get", "list"]`）可以让 Pod 读取命名空间内所有敏感信息，包括 ConfigMap 和 Secret。

检查通配符角色

```
kubectl get clusterroles,roles --all-namespaces -o json | \
  jq '.items[] | select( (.rules // [])[]? | (.resources[]? == "*" or .verbs[]? == "*") ) | {name: .metadata.name, rules: .rules}'
```

![image-20260627163413658](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNg50Ld5FMqiaYB8jTB681JUnicbuekWUoRyTmZMNLDy3qUkTPXjwvQN1QGT9ibvhqkDaEGjr73BmSa6ZwxURiaCccPeFpNFWCIP4c/640?wx_fmt=other&from=appmsg)

image-20260627163413658

使用docker拉取alpine/k8s:1.29.2

```
docker pull alpine/k8s:1.29.2
```

![image-20260629140224527](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauPp8akUnhM1KYysOVvfwyib9xuAWrRExPp8QcWXpRxic9oaBp6wN7ToDQQA5sHiaKibv3MZvnkCuCMXdjB0s7BjO1wO4zq15TkgLQA/640?wx_fmt=other&from=appmsg)

image-20260629140224527

创建被攻破的普通 Pod（test-pod）

```
kubectl run test-pod --image=alpine/k8s:1.29.2 --restart=Never -- sleep 3600
```

![image-20260629140446444](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauNrL6XomBHSyQ9NMiaJFnRAg3ZPwsmiaHyargpbDSYvvxzYryex53slvQKxL6nsFzLLRabNbSWApO06dKrBVIdpLjR5ictUnO7LWs/640?wx_fmt=other&from=appmsg)

image-20260629140446444

## 漏洞复现

### 模拟攻击者已获得一个普通 Pod 的 shell

攻击者通常通过 Web 漏洞、弱密码等方式进入某个 Pod。我们通过 `kubectl exec` 来模拟这一步。

首先确保 `test-pod` 存在并运行，处于`Running`状态：

![image-20260629154536244](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibzm8nWOdauP6fvJ9hFZnegUtRslgtSibKwuVNrSdgKnyCLbtXFJV0eTTGZuSQ69byMG37v0yoXSpCdtRyfF4cicljUjoTPPyACRfRsKbNTbxE/640?wx_fmt=other&from=appmsg)

image-20260629154536244

进入pod，现在你就是在攻击者已经拿下的那个普通容器里面了

```
kubectl exec -it test-pod -- sh
```

![image-20260629154622970](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMxbPzrUnnCxntvEIpnapiadBRmNTLzGsslZpGvIWSbI4mib34MA7aQoBlcZs7jNaHFDT1HUoR7icdbZ6iblobCk8794Y0U3u8k020/640?wx_fmt=other&from=appmsg)

image-20260629154622970

尝试查看物理磁盘设备**...