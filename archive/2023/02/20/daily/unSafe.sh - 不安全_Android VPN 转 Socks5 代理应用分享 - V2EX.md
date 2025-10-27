---
title: Android VPN 转 Socks5 代理应用分享 - V2EX
url: https://buaq.net/go-150046.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:14.195411
---

# Android VPN 转 Socks5 代理应用分享 - V2EX

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/de4e305ce730b415ee9acfad53d8827a.jpg)

Android VPN 转 Socks5 代理应用分享 - V2EX

大家好，我又来分享轮子啦~SocksTun是我最近开源的一个基于HevSocks5Tunnel实现的 Android VPN ，用于将手机端的 TCP 、UDP 流量通过 Socks5 代理进行转发
*2023-2-19 14:44:21
Author: [v2ex.com(查看原文)](/jump-150046.htm)
阅读量:129
收藏*

---

大家好，我又来分享轮子啦~

[SocksTun](https://github.com/heiher/sockstun)是我最近开源的一个基于[HevSocks5Tunnel](https://github.com/heiher/hev-socks5-tunnel)实现的 Android VPN ，用于将手机端的 TCP 、UDP 流量通过 Socks5 代理进行转发。其实它只是一个参考实现，主要用于演示如何用 HevSocks5Tunnel 实现 VPN 。它可以对接明文的标准 Socks5 协议，比如 Socks5 服务(或映射)部署在本地局域网，也是能具有一些实用性的吧。

## 特性支持

* 支持重定向 TCP 连接。
* 支持重定向 UDP 报文。(Fullcone NAT ，UDP 从 UDP 转发、UDP 从 TCP 转发)
* 支持简单用户名 /密码认证。
* 支持指定 DNS 地址。
* IPv4/IPv6 双栈。
* 全局 /按应用双重模式。

## 使用方法

### 服务端

#### HevSocks5Server

[HevSocks5Server](https://github.com/heiher/hev-socks5-server)支持 UDP 从 TCP 转发，可以运行在 Linux/BSD 和 macOS 系统上，配置、使用方法也比较简单。

```
# 下载、编译
git clone --recursive https://github.com/heiher/hev-socks5-server
cd hev-socks5-server
make

# 运行
hev-socks5-server conf.yml
```

conf.yml:

```
main:
  workers: 4
  port: 1080
  listen-address: '::'

misc:
  limit-nofile: 65535
```

#### 其它

任意支持标准 Socks5 协议的 TCP(Connect)和 UDP(Associate)的服务端即可。

### 手机客户端

![](https://user-images.githubusercontent.com/1407733/219656504-a17cf094-0bb1-4f1c-b79b-e72c718fce31.png)

1. 从项目[发布页](https://github.com/heiher/sockstun/releases)下载 APK 并安装。
2. 打开应用，配置 Socks5 地址、端口和 DNS 地址。
3. 如果使用 HevSocks5Server 服务端，钩选 UDP relay over TCP ；使用其它服务端则去掉。
4. 保存配置后，点击启用开启 VPN 服务。

## 性能评测

Android VPN App 目前还没有做过性能、能耗的评测(其实是不会~)，之前在低性能的 RK3399(AArch64 架构)设备做过几款 tun2socks 的评测，结论是只有 HevSocks5Tunnel 可以几乎跑满物理网卡的最大带宽，并且对应的 CPU 资源使用最少。那么，基于它实现的 Android VPN 应该具有相对较好的节能效果吧。

### 速率

![](https://hev.cc/posts/2023/benchmarking-of-tun2socks-on-rk3399/rk3399-speed.png)

### CPU 使用率

![](https://hev.cc/posts/2023/benchmarking-of-tun2socks-on-rk3399/rk3399-cpu.png)

## 最后

最开心的事情当然是开源的这些小轮子能跑起来，确实对大家有用，期待支持与反馈~

文章来源: https://v2ex.com/t/917046#reply4
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)