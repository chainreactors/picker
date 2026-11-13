---
title: 记录某系统实战内网K8S渗透
url: https://mp.weixin.qq.com/s/9zwNzuPplAlh9oyLoHvxtw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:00:36.692316
---

# 记录某系统实战内网K8S渗透

# 记录某系统实战内网K8S渗透

原创

zkaq - newugly
zkaq - newugly

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **newugly 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（   https://bbs.zkaq.cn   **）****

# 一、前期踩点

   在完成前期信息收集后，发现目标系统可能存在安全隐患。

该系统基于 Spring 框架构建，使用 SpringBoot-Scan 和 YYBaby\_v0.7\_Spring\_Scan 等工具对其进行目录扫描，最终确认系统存在 heapdump 信息泄露 问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJUkl5kI02Zr4DjrlRBrC2oDia4nAksZdCcuYBSujXJRYHTu4Wibuo88Hw/640?wx_fmt=png&from=appmsg)

将 heapdump 文件下载并进行内存分析后，在其中发现了应用配置中使用的 Shiro Key 等敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJL21Iqel1mkViab5dMGvSkfp9OSia4tX9hV2YUSRtCuC73YcaqLaUSKicw/640?wx_fmt=png&from=appmsg)

随后使用 Shiro 反序列化相关工具对获取到的 Key 进行验证，确认其是否有效以及是否具备命令执行能力。在验证成功后，即可通过反序列化漏洞执行系统命令，进一步反弹 Shell 到自己的 VPS 上。取得初始权限后，可以搭建代理进入内网进行横向渗透，或直接上线 vShell 进一步搭建代理。此外，也可以借助自动化工具上传内存马，再通过 WebShell 管理工具进行连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJRoDA2os2Rg897eSvonAKmE1HtUO4IwicgvXmJOtFWNJSBvuVAGbS23A/640?wx_fmt=png&from=appmsg)

一、内网k8s渗透

进入内网后，首先会对当前主机进行基础信息收集，包括查看网卡信息以确认可达的网段、当前用户所具备的权限，以及主机上运行的服务和应用情况。同时尝试查阅配置文件，重点关注其中是否包含账号密码、接口密钥等敏感信息。如果目标主机为 Windows 且具备外连能力，可以尝试开启并使用 RDP 进行远程连接，相比 Linux 系统，Windows 主机往往能够获取到更多有价值的信息和进一步利用的机会。最后，根据实际情况上传 fscan 等内网扫描工具，进行探测、扫描。

在扫描过程中发现 C 段中的一个 ip 存在 2379 端口和 6443 端口未授权，那么就可以直接拿到集群中的主机权限

第一步

`etcdctl.exe --endpoints=目标 ip:2379 get / --prefix --keys-only | findstr secrets`

从 etcd 中把所有配置项的“名字”都列出来，并筛选出和 secrets 相关的内容。这样做可以快速判断 etcd 里是否存放着 Kubernetes 的敏感信息，比如账号密码、Token 等，而不需要一开始就读取具体数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJn8XA1dCGHWvn60fkq5DaAQd0qYLl6x9Kic3GriaHL1RZXpAE681p3aCw/640?wx_fmt=png&from=appmsg)

第二步

`etcdctl.exe --endpoints=目标 ip:2379 get /registry/secrets/base-service/backuprecovery-admin-token-zltg8`

连接目标主机上的 etcd 服务，并按照指定路径读取名为 backuprecovery-admin-token-zltg8 的 Secret 数据。这个 Secret 通常对应的是 Kubernetes 中某个 ServiceAccount 的访问凭据，里面往往包含 Token、证书等敏感信息。如果该命令能够成功返回结果，说明已经可以从 etcd 中直接获取集群的认证信息，后续即可利用这些 Token 访问 Kubernetes API Server，进一步枚举资源甚至控制整个集群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJm4Ph1gsyVtk75ibQYZL48GUlSFvLpuTRcOxzY5HINhjOO6dbfPvIURg/640?wx_fmt=png&from=appmsg)

第三步

`kubectl.exe --insecure-skip-tls-verify -s https://目标 ip:6443/ --token="获取到的token" get pods,svc --all-namespaces -o wide`

在从 etcd 中拿到 ServiceAccount 的 Token 之后，使用 kubectl 携带该 Token 直接访问 Kubernetes 的 API Server。通过在命令中跳过 TLS 证书校验，成功连接到了集群，并一次性查看了所有命名空间下的 Pod 和 Service 信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJkQMRS2ObsI4rIJnwPF2ePuTHNJEMoUHLSCoTT0xHwnvddsXkkTT0BA/640?wx_fmt=png&from=appmsg)

第四步

`kubectl.exe --insecure-skip-tls-verify -s https://目标ip:6443/ --token="获取到的token" exec -n base-service -it 服务name -- bash`

在确认获取到的 Token 具备足够权限后，继续使用 kubectl exec 命令尝试进入集群内的容器。通过指定命名空间和目标服务对应的 Pod，并在跳过 TLS 校验的情况下执行交互式 Shell，成功进入了容器内部，获得了该服务运行环境的命令行权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpiaXwp5KiawSib8IlCDz3NRYJEpCVB4ibKbxIcDWPcbIicExQbleOhltg4lQpJzdUBRdZ0kQSowfsRdow/640?wx_fmt=png&from=appmsg)

通过上述攻击链，成功在 100 多个 Kubernetes 集群中获取了容器执行权限，部分集群进一步实现了节点级控制。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=36)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

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