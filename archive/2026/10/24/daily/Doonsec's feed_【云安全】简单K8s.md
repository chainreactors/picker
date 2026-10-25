---
title: 【云安全】简单K8s
url: https://mp.weixin.qq.com/s/_kNZbfPmijQ-eCbi7tAwXA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:08:37.454798
---

# 【云安全】简单K8s

# 【云安全】简单K8s

原创

师傅爱喝水
师傅爱喝水

师傅爱喝水

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 合规提示
> 本文仅用于授权安全测试与学习交流。请勿对未授权资产进行扫描、访问或渗透。
> 读者应自行确保行为合法合规并获得授权；因不当使用产生的一切后果由行为人自行承担。

云安全里，常见两块：**vCenter** 和 **K8s**。
今天把 **K8s** 简单讲清楚。

✦ ───────── 01 ───────── ✦

学习 K8s 的洞，其实可以很简单：**不需要先打靶场**。
直接做互联网资产测绘，就能看到不少目标。

```
title="Kubernetes Dashboard"
```

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbiaf1J661v4YN6nibEpv54UibLVpGu4pPjXvAzcKs8MYow8Ne7dPeiaibNbBaeFW9DbB7RMvAxCrcSUyyLaxWVn16wVSiakorKubkPt4/640?wx_fmt=png&from=appmsg)

这类暴露在互联网上的 Dashboard，往往就是入口。

✦ ───────── 02 ───────── ✦

## K8s最简单的洞：未授权访问

### ① 直接接管

由于管理员配置错误，面板**无需登录**。
进入页面后，点击 **Skip**，就可能直接进入后台。

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbgmNj85Tb7QMr8zo1kJN0y0eiaMbI1eE3eibPRXtWJMq11ENpAzBrtbCgHgs7RFYny5ODOk6fTwHP5HP5P3Fjm4we9lUmrwiaErNs/640?wx_fmt=png&from=appmsg)

### ② 接口泄露凭证

直接访问接口：

```
/api/v1/secret
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbh6Yia91SJgicueOibxW3BY0icUXjyKhCx2RiapVicWezfDCNety0lWz9fKP4D9WcRibakAiade5b5IC5t2scTgn3kt0DcfJMs23naJwjQ/640?wx_fmt=png&from=appmsg)

这个接口可能泄露登录 **Token**。
把返回内容交给 AI 阅读，帮助定位凭证，直接登录。

✦ ───────── 03 ───────── ✦

## 登录之后：先看 Pod

登录后的 K8s 后台大概长这样，面板监控资源运行情况。

左侧有很多模块，是渗透重点要关注的。

其中最重要的对象之一，就是 **Pod**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbia03NmXzXmXZHRe8V1pjtOiaWUV5NCdlAAseMTnHiaLiaY00jWYM6PgPZI5FKAdqoTZMClhxrnVbGBKEiaLYnc3tZEmzOz8aiayZDhc/640?wx_fmt=png&from=appmsg)

说白了：

> **一个 Pod 可以放多个 Docker 容器。**

正常 Docker 基本有的能力，Pod都有：
**看日志、看终端、看挂载文件**。

实际渗透中，Pod 权限有大有小。
拿到 Shell 后，如果 Pod 权限不够，就要想办法：

* **提高权限**
* **容器逃逸**

### Pod的重点

| 看点 | 说明 |
| --- | --- |
| 当前 Pod 权限 | 判断能做什么 |
| 是否 privileged | 是否特权容器 |
| hostPath 挂载 | 是否挂载宿主机路径 |
| 容器逃逸 | 尝试逃逸到 Node 宿主机 |
| sa token | 读取 `/var/run/secrets/` 下的服务账号 Token |

✦ ───────── 04 ───────── ✦

## 读Secrets

K8s 作为控制面板，里面有大量配置文件存储在 **Secrets** 中。

这部分有点像nacos的配置文件，在里面会有很多意想不到的收获。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbgibCdQnuhiavdmKRLQ62XCbfOexVqh7WkKUxTxGH9Tvp6EX1vNLBkxspibwicIjXTxHf4je4jk8mB5F1NOtkpr1CzRpGINUtkWH8A/640?wx_fmt=png&from=appmsg)

Secrets 存放敏感数据：

* 账号密码
* 数据库密码
* Token
* 私钥
* 证书
* 仓库密钥

比如：里面可能有存储桶信息，也可能有云主机的 AK/SK。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbg1Ficbz22gl1n2CVvU0JuicaPYUPAibIdLAWiaCrCmic8KdJ82wAYIdsbUWORZ3SJLEESRWPVSQnhvTS6hXU4wsGwnooibuvmkvmicw8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbiavI8A1EdsQSWUuAM76XKLPp8xARialLFTF0CsKYhfASpYfcNJM4K4FokUicoRenG5wz1N6N4M99NgvY8FjOeKr7u8BToQIx4h8s/640?wx_fmt=png&from=appmsg)

> 总之：**Secrets 里面一切皆有可能。优先读！**

✦ ───────── 05 ───────── ✦

## Service：看内网网段与出入口

接下来看 **Service**。

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbiaLlMDnFyyuVq8kISl1fEWeBPO3gRuVYc11icv3Miax2EcsVP4BW14gjdicTMuibKhLlw0GG2yoyqRIPORErWAg3BK8loyDDSjicWB4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbiarS7Z0iblqhUIHsf41JnhEomMfmExH117dORGyIXcVlicwHtqZJF390A2jPib2rx03NsClrOg1hiceEwcpibOChh8ArEfdRhRS4fzM/640?wx_fmt=png&from=appmsg)

通过 Service 可以看到：

* 服务对应的**内网网段 IP**
* 服务的**出入口**

这对后续横向和定位内网资产很有帮助。

✦ ───────── 06 ───────── ✦

## Cluster Roles / Cluster Role Bindings

这里用来看**集群权限绑定**。

ClusterRole用来看权限角色模板，类似于系统有哪些权限角色。

**ClusterRoleBinding**：**把权限角色绑定到账号主体。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x602SQboUbiagx2NUFOcgDibIGc4ePwHMnnY7hkky4UHzV9umONUYEIyaGw10cOG94WssgKTOrXhSsJLtZ4gp94L4GKibpFUTq68oSdgvfndZY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbgglbIEXjkYpobwGh6hsoM7zGTVAvictaYkCsicVnd2rZu13uhPr9Vh6DepLKeZIIfShEFPMP4engb7wEDrqE0CXfSlCosK2FSK4/640?wx_fmt=png&from=appmsg)

重点记住：

> **cluster-admin 是最高权限，全集群掌控。**

如果账号权限不够，那么面板所有返回内容都可能是 **404**，什么都不可见。

✦ ───────── 07 ───────── ✦

## ServiceAccount：服务账号

![](https://mmbiz.qpic.cn/mmbiz_png/x602SQboUbjLicFP6wDAMgXQwjvS0ACJbBAhnzNyb7jhwHnyBibtjPp5JB7lxMyTiaQV8sfttFPefsib2xm150VjrS7pCaNianrvqNzU78zlDOCw/640?wx_fmt=png&from=appmsg)

**服务账号**可以看到：

* Pod 里面的容器
* 能由哪些账号访问
* 每个账号的权限也不同

### 结合看ServiceAccount + RBAC

### ClusterRoleBinding把权限角色绑定到账号主体 ServiceAccount就是看有哪些账号 三者结合我们就可以找到能访问目标集群权限最高账号

判断当前帐号

* 能不能看 **Secret**
* 能不能创建 **Pod**
* 能不能绑定 **cluster-admin**

> 最后**拿 SA Token → 判断权限大小 → 找提权路径**

✦ ───────── 08 ───────── ✦

## K8s基础渗透路线

记住这张图就好：

```
Pod 权限 → Secrets → ServiceAccount → RBAC → Service      ↓     逃逸 Node → 横向 Pod → 跨 Namespace
```

拥有pod权限之后，再从node逃逸：

* **Nodes**：逃逸成功后拿下节点，再横向其他 Pod。
* **Namespaces**：跨命名空间扩散， 实现对整个集群的掌控。

✦ ───────── END ───────── ✦

> 简单 K8s，先看到这里。
> 下章复现一手接管k8s集群案例。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ydaKj149ibsGfynhmsVMxhfHYSJgTVXAxcYXXIkibdupUE2Vds5FX0ZXUcYmGQa1QmZgELRic5Fbb0xmX6r8a48VA/0?wx_fmt=png)

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