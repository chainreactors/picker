---
title: 应急响应-主机安全告警K8s恶意DNS请求排查
url: https://zgao.top/%e5%ba%94%e6%80%a5%e5%93%8d%e5%ba%94-%e4%b8%bb%e6%9c%ba%e5%ae%89%e5%85%a8%e5%91%8a%e8%ad%a6k8s%e6%81%b6%e6%84%8fdns%e8%af%b7%e6%b1%82%e6%8e%92%e6%9f%a5/
source: Zgao's blog
date: 2022-12-13
fetch_date: 2025-10-04T01:16:00.477435
---

# 应急响应-主机安全告警K8s恶意DNS请求排查

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 应急响应-主机安全告警K8s恶意DNS请求排查

* [首页](https://zgao.top)
* [应急响应-主机安全告警K8s恶意DNS请求排查](https://zgao.top:443/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8%E5%91%8A%E8%AD%A6k8s%E6%81%B6%E6%84%8Fdns%E8%AF%B7%E6%B1%82%E6%8E%92%E6%9F%A5/)

[12月 12, 2022](https://zgao.top/2022/12/)

### 应急响应-主机安全告警K8s恶意DNS请求排查

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8%E5%91%8A%E8%AD%A6k8s%E6%81%B6%E6%84%8Fdns%E8%AF%B7%E6%B1%82%E6%8E%92%E6%9F%A5/)

![](https://zgao.top/wp-content/uploads/2022/12/image-4-1024x372.png)

单机场景下的恶意dns请求排查

> k8s集群中某台主机请求恶意域名触发主机安全告警，但是排查发现被告警的是负责集群dns解析的主机，并发真正发起恶意请求的主机/容器。这类场景下如何才能快速排查出存在漏洞的业务或服务？
>
> k8s场景下如何应急响应？

![](https://zgao.top/wp-content/uploads/2022/12/image-5-1024x447.png)

k8s场景下的恶意dns请求排查

k8s使用coreDNS或者kube-dns来作为集群内部的dns解析服务，这类云原生场景下的恶意请求排查会相对麻烦些，所有业务都是容器化部署，并且k8s中dns服务默认未开启日志。

文章目录

[ ]

* [思路一：开启coreDNS解析日志](#%E6%80%9D%E8%B7%AF%E4%B8%80%EF%BC%9A%E5%BC%80%E5%90%AFcoreDNS%E8%A7%A3%E6%9E%90%E6%97%A5%E5%BF%97 "思路一：开启coreDNS解析日志")
  + [测试域名解析来自哪个pod？](#%E6%B5%8B%E8%AF%95%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90%E6%9D%A5%E8%87%AA%E5%93%AA%E4%B8%AApod%EF%BC%9F "测试域名解析来自哪个pod？")
* [思路二：tcpdump抓包](#%E6%80%9D%E8%B7%AF%E4%BA%8C%EF%BC%9Atcpdump%E6%8A%93%E5%8C%85 "思路二：tcpdump抓包")
  + [nsenter 安装](#nsenter_%E5%AE%89%E8%A3%85 "nsenter 安装")
  + [nsenter 进入容器网络空间](#nsenter_%E8%BF%9B%E5%85%A5%E5%AE%B9%E5%99%A8%E7%BD%91%E7%BB%9C%E7%A9%BA%E9%97%B4 "nsenter 进入容器网络空间")

## 思路一：开启coreDNS解析日志

找到coredns所在的容器。

```
kubectl get pods -A -o wide | grep dns
```

![](https://zgao.top/wp-content/uploads/2022/12/image-6-1024x385.png)

默认coredns未开启日志，执行logs命令没有解析记录。注意：执行命令要带上 -n kube-system （命名空间）。

![](https://zgao.top/wp-content/uploads/2022/12/image-7-1024x245.png)

修改coredns配置文件加入log。

```
kubectl edit configmap coredns -n kube-system
```

![](https://zgao.top/wp-content/uploads/2022/12/image-8-1024x644.png)

coredns默认配置

![](https://zgao.top/wp-content/uploads/2022/12/image-9-1024x664.png)

加入log，不添加配置会有默认规则

修改配置coredns会自动重启。

注意开启日志可能的影响：

* 重启coredns可能短暂影响集群域名解析
* 域名解析量大，开启日志可能会影响到服务性能

![](https://zgao.top/wp-content/uploads/2022/12/image-10-1024x506.png)

### 测试域名解析来自哪个pod？

![](https://zgao.top/wp-content/uploads/2022/12/image-11-1024x565.png)

我们在开启日志后，使用另一个容器发起dns请求，可以看到对应的容器ip。

## 思路二：tcpdump抓包

在coredns的宿主机上抓53端口的流量。但需要结合恶意请求的告警定位到准确时间的报文信息。

但是k8s场景下，容器内部很多命令都是没有。这个时候就需要用到nsenter进行到容器内部的网络空间进行抓包。一个比较典型的用途就是进入容器的网络命名空间。通常容器为了轻量级，大多都是不包含较为基础网络管理调试工具，比如：ip、ping、telnet、ss、tcpdump 等命令，给调试容器内网络带来相当大的困扰。

### **nsenter 安装**

nsenter 位于 util-linux 包中，一般常用的 Linux 发行版都已经默认安装。如果你的系统没有安装，可以使用以下命令进行安装：

```
 yum install util-linux -y
```

### **nsenter** 进入容器网络空间

```
nsenter -t <PID> -n bash
```

![](https://zgao.top/wp-content/uploads/2022/12/image-17-1024x625.png)

```
tcpdump -i any port 53 -C 20 -W 200 -w /tmp/client_dns.pcap
```

在正常情况下，抓包对业务无影响，仅会增加小部分的CPU负载和磁盘写入。该命令会对抓取到的包进行rotate，最多可以写200个20 MB的.pcap文件。

但是上面的命令将包内容输出到了文件，无法在标准输出上看到记录。不想要完整的数据包，可以用下面的命令。

```
tcpdump -i any port 53 -vvv | tee -a /tmp/dns.log
```

![](https://zgao.top/wp-content/uploads/2022/12/image-12-1024x670.png)

此时也能捕获到coredns内部的域名请求ip。

Post Views: 2,915

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8%E5%91%8A%E8%AD%A6k8s%E6%81%B6%E6%84%8Fdns%E8%AF%B7%E6%B1%82%E6%8E%92%E6%9F%A5/#respond)

Δ

版权©2020 Author By : Zgao