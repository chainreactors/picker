---
title: Tailscale 异地组网/P2P内网穿透
url: https://y4er.com/posts/tailscale/
source: Y4er的博客
date: 2023-01-05
fetch_date: 2025-10-04T03:03:48.540492
---

# Tailscale 异地组网/P2P内网穿透

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [前言](#前言)
* [注册](#注册)
* [原理](#原理)
* [配置](#配置)
* [MagicDNS](#magicdns)
* [延迟](#延迟)
* [exit node](#exit-node)
* [Subnet routers](#subnet-routers)
* [中继服务器](#中继服务器)
* [竞品](#竞品)
* [参考](#参考)

## 目录

* [前言](#前言)
* [注册](#注册)
* [原理](#原理)
* [配置](#配置)
* [MagicDNS](#magicdns)
* [延迟](#延迟)
* [exit node](#exit-node)
* [Subnet routers](#subnet-routers)
* [中继服务器](#中继服务器)
* [竞品](#竞品)
* [参考](#参考)

# Tailscale 异地组网/P2P内网穿透

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [瞎折腾](/categories/%E7%9E%8E%E6%8A%98%E8%85%BE/)

2023-01-04  2023-01-04  约 1018 字
 预计阅读 5 分钟

目录

* [前言](#前言)
* [注册](#注册)
* [原理](#原理)
* [配置](#配置)
* [MagicDNS](#magicdns)
* [延迟](#延迟)
* [exit node](#exit-node)
* [Subnet routers](#subnet-routers)
* [中继服务器](#中继服务器)
* [竞品](#竞品)
* [参考](#参考)

警告

本文最后更新于 2023-01-04，文中内容可能已过时。

# # 前言

疫情居家办公期间，折腾了一段时间的cloudflare tunnel，但是网速时好时坏，rdp卡成ppt，向日葵在mac上也不好用，后来在v2ex上发现了Tailscale和ZeroTier两款点对点穿透工具，折腾一下发现比cf tunnel好用一万倍，nat打洞成功之后ping只有5ms，这里记录下折腾的笔记。

# # 注册

用GitHub账号登录就行

# # 原理

传统的vpn结构如图

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4bf1249c-9b9f-db7b-3196-d6b28db9a2f1.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/4bf1249c-9b9f-db7b-3196-d6b28db9a2f1.png "image.png")

image.png

Tailscale的网络结构如图

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/522f27bc-7ba7-3711-7570-07d424093673.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/522f27bc-7ba7-3711-7570-07d424093673.png "image.png")

image.png

就近原则

两台机器链接如果可以穿透nat打洞成功，那么就是直连，否则就是走Tailscale的中继服务器（derp）。

两台机器其实都是基于wireguard的实现，链接上Tailscale的机器会加一个网卡用于wireguard链接。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/04757853-500a-d707-fd59-79bf4c0c3f42.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/04757853-500a-d707-fd59-79bf4c0c3f42.png "image.png")

image.png

更详细的原理见官方的博客 <https://tailscale.com/blog/how-nat-traversal-works/>

# # 配置

没啥好讲的，安装对应的客户端，然后登录账号就行了。

# # MagicDNS

Tailscale提供了一个类似内网dns的服务，将所有加入到Tailscale网络中的节点分配一个对应的ip和dns，这样用户不需要记ip了。

# # 延迟

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ee143f59-4aac-7292-b760-c438cc4c2a98.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ee143f59-4aac-7292-b760-c438cc4c2a98.png "image.png")

image.png

自动打洞，work机器和poop机器在同一局域网，所以打洞用的192的段，我测试公司电脑和家里电脑同城打洞成功后只有5ms延迟，没打洞成功就是走的图中的中继DERP服务器了。

# # exit node

tailscale可以实现FQ，需要先开启ip转发 <https://tailscale.com/kb/1103/exit-nodes/#enable-ip-forwarding>

bash

```
If your Linux system has a /etc/sysctl.d directory, use:

echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.d/99-tailscale.conf
sudo sysctl -p /etc/sysctl.d/99-tailscale.conf

Otherwise, use:

echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p /etc/sysctl.conf
If your Linux node uses firewalld, you may need to also allow masquerading due to a known issue. As a workaround, you can allow masquerading with this command:

firewall-cmd --permanent --add-masquerade
```

通过在国外vps上运行

text

```
sudo tailscale up --advertise-exit-node
```

然后网页控制台中这个节点点击`Edit route settings`开启此功能

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/dc347832-b4b6-5d2a-dfef-4efc71aaeaeb.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/dc347832-b4b6-5d2a-dfef-4efc71aaeaeb.png "image.png")

image.png

然后在windows的托盘图标中，可以选择本机所有流量走出口节点

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7b179313-9d03-e6a8-1915-b49121fc9195.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/7b179313-9d03-e6a8-1915-b49121fc9195.png "image.png")

image.png

# # Subnet routers

因为每个账号只有20台设备数，所以可能会遇到需要开放一整个网段192.168.1.1/24的情况，我还没遇到，读者看文档自己配置吧。

<https://tailscale.com/kb/1019/subnets/>

# # 中继服务器

打洞成功率和网络情况有关系，所以为了链接成功率和保证低延迟，可以自建derp中继服务器，我不需要，所以读者移步 <https://icloudnative.io/posts/custom-derp-servers/>

# # 竞品

向日葵、蒲公英、anydesk、todesk什么的都不考虑

1. parsec
2. n2n
3. Nebula
4. ZeroTier
5. tinc

相对来说tailscale界面好看，功能也不差，主要是稳定。

# # 参考

1. <https://icloudnative.io/posts/custom-derp-servers/>
2. <https://tailscale.com/kb/>
3. <https://tailscale.com/blog/how-nat-traversal-works/>

这篇文章更多是记录一下自己折腾的东西，水文。

文笔垃圾，措辞轻浮，内容浅显，操作生疏。不足之处欢迎大师傅们指点和纠正，感激不尽。

![](/img/avatar.jpg)

*如果你觉得这篇文章对你有所帮助，欢迎赞赏或关注微信公众号～*

![](/img/reward/wechat.png)![](/img/reward/alipay.png)![](/img/reward/weixin_mp.jpg)

更新于 2023-01-04

LINE

[内网穿透](/tags/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/), [P2p](/tags/p2p/), [Tailscale](/tags/tailscale/)

返回 | [主页](/)

[dotnet host startup hook](/posts/dotnet-host-startup-hook/ "dotnet host startup hook")
[Java静态分析框架Tai-e的简单使用](/posts/simple-use-of-the-java-static-analysis-framework-tai-e/ "Java静态分析框架Tai-e的简单使用")

Please enable JavaScript to view the comments powered by [Utterances](https://utteranc.es/).

由 [Hugo](https://gohugo.io/ "Hugo 0.148.2") 强力驱动 | 托管在 [Cloudflare Pages](https://pages.cloudflare.com/ "Cloudflare Pages") 上 | 主题 -  [DoIt](https://github.com/HEIGE-PCloud/DoIt "DoIt 0.4.2")

2018 - 2025 [Y4er](https://github.com/Y4er) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)