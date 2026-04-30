---
title: 【首发】从APIServer到Kubelet：K8sPenTool如何串起一条云原生攻击链？
url: https://mp.weixin.qq.com/s/l0lfe6LbD5BHT89dl650qQ
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:25:05.063130
---

# 【首发】从APIServer到Kubelet：K8sPenTool如何串起一条云原生攻击链？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IjKZbibec2gDEnqDRW4wPia0gJibf9W3uXNuza1ZLgYTYat6IQhicxKqs3Siamr4Ls5tiaW87HlbxO5McTnA8GETTytakhV1U1UDpBTyPfmDnP0Kg/0?wx_fmt=jpeg)

# 【首发】从APIServer到Kubelet：K8sPenTool如何串起一条云原生攻击链？

原创

Zacarx
Zacarx

Zacarx随笔

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近我朋友写了个名为K8sPenTool的工具，我浅看了一下，发现其对云原生安全显然有点说法，下面我带各位师傅们以批判性眼光来学习一下这个**工具以及云原生攻击链**。

## 概述

K8sPenTool 不是传统意义上的“单点利用器”，而是一套把 Kubernetes 常见攻击链压缩进单一 的操作编排器：从容器环境辨别、端口探测、APIServer/Kubelet/etcd/Dashboard  初始访问，到命令执行、权限维持、容器逃逸、横向移动，再到 kubectl 落地操作，几乎把云原生渗透测试里最常见的路径都串起来了。

**当然，如果你不是很了解云原生，下面我会结合具体攻击链来讲解这个工具。**

## 仔细剖析

K8sPenTool 最值得研究的，不是“界面上有几页 Tab”，而是它如何把零散的 Kubernetes 风险面串成顺手的攻击链。最典型的链路有两条：**APIServer 路径**和 **Kubelet 路径**。前者偏控制面权限与资源操作，后者偏节点侧未授权接口与容器执行。二者再叠加持久化与横向移动模块，就形成了完整闭环。

如图所示，其包含了下面四条路，如果你一脸懵逼，千万别急。**后面我给大家简单讲解，因为概念很多人不熟，我会避免生词，当你看完这篇文章，希望你也会对云原生安全不再陌生、不再心怀畏惧**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IjKZbibec2gB5cYicVwHt7r7q4nmt7xIaupuUDa7tTFVEgvcw4l1WaHVugNrcQHxuTOZOTTIueiaygRYARKGW1WBITg7WfUkILhh5skPxlhQbw/640?wx_fmt=png&from=appmsg)

### 第一条路：从 APIServer 进去

APIServer 可以理解为 Kubernetes 的“总入口”。如果 APIServer 暴露得太宽，或者某个 ServiceAccount Token 权限过大，工具就可以顺着控制面一路往下走。当然，这小工具实现其实还是先生成临时kubeconfig，再调用内置或外部的 kubectl 去执行操作，**本质上就是把攻击者平时手敲的一堆命令包装成按钮。**

虽然不是什么黑科技，但也减少了各位学习成本不是。

![image-20260429212432785](https://mmbiz.qpic.cn/sz_mmbiz_png/IjKZbibec2gD3Bd4oTCfNdlH0OEvt3EjNAf4jWsLJPXOqNMJMdaSBpB0J19XhmhEq21icq8iaArR8KVzebUY5cdsA2mR6icYgYkmHYUkbqHM738/640?wx_fmt=png&from=appmsg)

### 第二条路：从 Kubelet 进去

Kubelet 是跑在每个节点上的组件，负责管理这个节点上的 Pod 和容器。如果 Kubelet 的认证和授权配置不严，攻击者可能不需要先拿到完整的集群控制权，就能直接和节点上的容器打交道。

那么，显然易见Kubelet 一旦配置不当，它暴露的不是“信息”，而是执行能力。

![image-20260429212239057](https://mmbiz.qpic.cn/mmbiz_png/IjKZbibec2gAB4RVgekOc6aICt4wDrKgo76rvGprUrkg6VWONRALId0G9B9jibhpkeFd2cGVoouLocqprEpfPVfbvibvgJHZ0NcbuGXwFv4HTA/640?wx_fmt=png&from=appmsg)

### 第三条路：读 Secret，找横向移动机会

Kubernetes 里的 Secret 是非常敏感的资源。数据库密码、镜像仓库凭证、ServiceAccount Token、第三方服务密钥，都可能放在里面。

一般来说，横向移动除了依靠漏洞，还可以靠权限过宽、网络过平、Secret 管理混乱慢慢滚雪球，直至雪崩。

### 第四条路：持久化

一听名字就很红队，简单概括来说就是留后门。

它会生成一些 Kubernetes 资源模板，ServiceAccount、CronJob等，简单来说：

高权限 ServiceAccount 可以长期保留访问能力。  CronJob 可以周期性执行任务。  DaemonSet 可以让工作负载跑到多个节点。  影子 kubeconfig 可以把已有 Token 包装成新的访问入口。

## 总结一下

K8sPenTool 不是创造了一条新攻击链，而是把 Kubernetes 里常见的错误配置、过度授权和暴露面，整理成了一条更容易操作的链路。其包含信息收集、初始访问、命令执行、权限维持、权限提升、横向移动等模块，属于极为标准的all in one型红队工具，在强对抗的攻防演练中，个人觉得还是很有价值的。

**如果你喜欢这个工具，请给本文一键三连&&直接移步：**

**https://github.com/trymonoly/K8sPenTool**

如果你有任何建议，可以提交issue，我们会第一时间解决。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

Zacarx随笔

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

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