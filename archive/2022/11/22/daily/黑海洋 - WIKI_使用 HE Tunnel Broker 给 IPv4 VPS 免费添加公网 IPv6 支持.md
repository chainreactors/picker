---
title: 使用 HE Tunnel Broker 给 IPv4 VPS 免费添加公网 IPv6 支持
url: https://blog.upx8.com/3109
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:13.684295
---

# 使用 HE Tunnel Broker 给 IPv4 VPS 免费添加公网 IPv6 支持

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 使用 HE Tunnel Broker 给 IPv4 VPS 免费添加公网 IPv6 支持

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
20307

[![](https://imgcdn.p3terx.com/post/20210225051254.jpg)](https://imgcdn.p3terx.com/post/20210225051254.jpg)

## 前言

[Hurricane Electric](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5b1pTNXVaWFE) (简称：HE) 是一家位于美国的全球互联网服务提供商。该公司运营了世界上以对等数目计算的最大 IPv6 网络，同时也提供免费的 IPv6 隧道服务。早在 IPv6 还未普及的时代，博主曾用它家的服务给家里的宽带接入了 IPv6 网络，优先体验了一把，同时也积累了一些 IPv6 网络的使用经验。虽然经过多年的发展 IPv6 已经相当普及，但依然还是有部分 VPS 商家由于各种各样的原因没有给 VPS 标配 IPv6 地址，有的需要加钱、有的甚至不给加钱。当我们有访问 IPv6 网络的需求，就比如给 IPv6 Only VPS 主机做 SSH 跳板，则可以使用 HE Tun­nel Bro­ker 提供的 IPv6 隧道免费给 IPv4 VPS 主机添加一个公网 IPv6 地址来获得 IPv6 网络的访问能力。

## 创建 Tunnel Broker IPv6 隧道

* 注册 [Tunnel Broker](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5M2QzY3VkSFZ1Ym1Wc1luSnZhMlZ5TG01bGRB) 账号
* 点击左侧的`Create Regular Tunnel`(创建常规隧道)
* 输入 VPS 的公网 IP 地址
* 根据 VPS 的位置选择一个合适的节点
* 页面拉到最下方，点击`Create Tunnel`(创建隧道)[![](https://imgcdn.p3terx.com/post/20210214034651.png#vwid=849&vhei=722)](https://imgcdn.p3terx.com/post/20210214034651.png#vwid=849&vhei=722)
* 在 **Tunnel Details** 页面可以看到创建的 IPv6 隧道的详细信息，其中 **Client IPv6 Address** 是申请到公网 IPv6 地址。[![](https://imgcdn.p3terx.com/post/20210214040003.png#vwid=661&vhei=633)](https://imgcdn.p3terx.com/post/20210214040003.png#vwid=661&vhei=633)

## 获取配置示例

在 **Tunnel Details** 页面有个 **Example Configuration** 选项卡，在这里你可以选择合适的配置示例。就比如这里有 De­bian/Ubuntu 的 `interfaces` 配置文件示例：

[![](https://imgcdn.p3terx.com/post/20210214040002.png#vwid=662&vhei=478)](https://imgcdn.p3terx.com/post/20210214040002.png#vwid=662&vhei=478)

只要基于 De­bian 的发行版和使用 `interfaces` 配置文件的系统理论上都可以使用。其它不兼容的发行版则可以使用 **Linux-net-tools** 或 **Linux-route2** 示例手动输入命令。

由于博主使用的是 De­bian ，所以后面只会讲 De­bian 系发行版的详细操作步骤。~~不会真的有人在用 CentOS 吧？~~

## 添加网络接口

将 `he-ipv6` 配置文件添加到 `/etc/network/interfaces.d/` 目录下。下面是一把梭命令示例，根据实际情况替换文本。

```
sudo tee /etc/network/interfaces.d/he-ipv6 <<EOF
auto he-ipv6
iface he-ipv6 inet6 v4tunnel
        address 2001:xxx:xxxx:xxxx::2
        netmask 64
        endpoint 216.66.84.46
        local 233.233.233.233
        ttl 255
        gateway 2001:xxx:xxxx:xxxx::1
EOF
```

> **TIPS:** 如果是 NAT VPS 或 VPC 内网方案则需要将`local`字段后面的公网 IP 替换为内网 IP （获取命令：`ip route get 8.8.8.8 | grep -oP 'src \K\S+'`）。

## 启用 IPv6 隧道

* 安装网络工具包

  ```
  sudo apt update
  sudo apt install net-tools iproute2 -y
  ```
* 启动 `he-ipv6` 网络接口

  ```
  sudo ifup he-ipv6
  ```

  > **TIPS**：若提示 **ifup: unknown interface he-ipv6** ，则添加`source /etc/network/interfaces.d/*`到`/etc/network/interfaces`文件（一把梭命令：`echo 'source /etc/network/interfaces.d/*' >>/etc/network/interfaces`）后重试，正常情况下无输出。
* 启用后执行 `ifconfig` 命令，这时应该有一个 `he-ipv6` 接口，类似下面这样：

  ```
  he-ipv6: flags=209<UP,POINTOPOINT,RUNNING,NOARP>  mtu 1480
            inet6 2001:xxx:xxxx:xxxx::2  prefixlen 64  scopeid 0x0<global>
            inet6 fe80::xxxx:xxxx  prefixlen 64  scopeid 0x20<link>
            sit  txqueuelen 1000  (IPv6-in-IPv4)
            RX packets 11605  bytes 3127821 (3.1 MB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 13811  bytes 2403522 (2.4 MB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  ```
* 若没有生效可以尝试重启网络

  ```
  sudo systemctl restart networking
  ```

## DNS 设置

编辑 `/etc/resolv.conf` 文件，更改 DNS 解析服务器为支持查询 AAAA 记录的 DNS 服务器，比如 [Google Public DNS](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5a1pYWmxiRzl3WlhKekxtZHZiMmRzWlM1amIyMHZjM0JsWldRdmNIVmliR2xqTFdSdWN3)。

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

> **TIPS:** 不建议使用 IPv6 地址的 DNS ，因为通过 IPv6 隧道去请求可能会拖慢 DNS 解析速度。

## 检测 IPv6 支持

执行 `ping6 google.com` 命令，能 ping 通说明 VPS 已经支持 IPv6 网络了。

如果是 NAT VPS ，除了前面提到的替换 IP 操作以外，可能还需要一些额外的设置，否则可能还是无法访问 IPv6 网络。

NAT VPS 设置 | 点击查看

## 优先使用 IPv4 网络

默认情况下 IPv6 网络优先级会高于 IPv4 ，为了防止 IPv6 隧道拖慢 VPS 的正常网速，可以设置优先使用 IPv4 网络。同时也能减轻了对 HE Tun­nel Bro­ker 节点的网络压力，合理使用宝贵的免费资源。

编辑 `/etc/gai.conf` 文件，在末尾添加下面这行配置：

```
precedence  ::ffff:0:0/96   100
```

一键添加命令如下：

```
echo 'precedence  ::ffff:0:0/96   100' | sudo tee -a /etc/gai.conf
```

完事执行 `curl ip.p3terx.com` 命令，显示 VPS 的 IPv4 地址则代表成功。

> **TIPS:** 这仅限于 VPS 本身发起的网络访问。如果 VPS 用于科学上网，则还取决于本地科学上网工具的 DNS 策略，如有必要可以设置丢弃 AAAA 记录。

## 删除 IPv6 隧道

当你不想用了，或者想使用其它方式访问 IPv6 网络时，记得先删除。

* 停用隧道

  ```
  sudo ifdown he-ipv6
  ```
* 删除 `he-ipv6` 网络接口配置文件（若没有删除重启后会自动启用）

  ```
  sudo rm -f /etc/network/interfaces.d/he-ipv6
  ```

---

## 相关推荐

* [国外便宜高性价比和免费白嫖 VPS 推荐](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2FyY2hpdmVzL2NoZWFwLWFuZC1jb3N0ZWZmZWN0aXZlLXZwcy1yZWNvbW1lbmRlZC5odG1s)
* [使用 Cloudflare WARP 给 VPS 服务器免费添加 IPv4 或 IPv6 网络支持](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2FyY2hpdmVzL3VzZS1jbG91ZGZsYXJlLXdhcnAtdG8tYWRkLWV4dHJhLWlwdjQtb3ItaXB2Ni1uZXR3b3JrLXN1cHBvcnQtdG8tdnBzLXNlcnZlcnMtZm9yLWZyZWUuaHRtbA)

---

本博客已开设 [Telegram 频道](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5MExtMWxMMUF6VkVWU1dGOWFUMDVG)，欢迎小伙伴们订阅关注。

---

## 本文参考资料

* [使用 Tunnel broker 为 VPS 主机免费添加 IPv6 地址实现互联访问](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5M2QzY3VkMkZ1ZG1rdWJtVjBMekUxTWpVMUxtaDBiV3c)
* [利用TunnelBroker给阿里云ECS配置公网IPv6](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5dGFXRnZkRzl1ZVM1NGVYb3ZNakF5TUM4d015OHdNeTlUWlhKMlpYSmZUMkowWVdsdVNWQjJObFpwWVZSMWJtNWxiRUp5YjJ0bGNn)

[取消回复](https://blog.upx8.com/3109#respond-post-3109)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")