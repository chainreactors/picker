---
title: Debian Linux VPS 服务器 WireGuard 安装教程
url: https://blog.upx8.com/3139
source: 黑海洋 - WIKI
date: 2022-12-07
fetch_date: 2025-10-04T00:43:04.811311
---

# Debian Linux VPS 服务器 WireGuard 安装教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Debian Linux VPS 服务器 WireGuard 安装教程

发布时间:
2022-12-06

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
18788

## 前言

WireGuard 想必不用过多介绍了，目前网上的 Wire­Guard 教程有的是一键脚本、有的是老方法，安装慢而且会带入了一堆乱七八糟的东西，而官方文档并没有详细说明安装方法。对于 VPS 而言则还要考虑一些实际因素，不然随意安装只有报错等着你。所以博主根据实际经验写了这篇适用于通用操作系统 De­bian 10+ 的 Wire­Guard 安装教程，适合有手动配置 Wire­Guard 需求的小伙伴。

## 准备工作

* 安装 `sudo` 和 `lsb_release`

  ```
  apt install sudo lsb-release -y
  ```
* 添加 back­ports 源

  ```
  echo "deb http://deb.debian.org/debian $(lsb_release -sc)-backports main" | sudo tee /etc/apt/sources.list.d/backports.list
  sudo apt update
  ```

## 安装依赖组件

* 安装必要的网络工具

  ```
  sudo apt install iproute2 openresolv -y
  ```
* 安装 **wireguard-tools** (Wire­Guard 配置工具：`wg`、`wg-quick`)

  ```
  sudo apt install wireguard-tools --no-install-recommends
  ```

## 安装 WireGuard

先执行 `uname -r` 命令查看内核版本。如果是 5.6 及以上内核则已经集成了 Wire­Guard ，就不需要安装了。

当然看到这篇教程的小伙伴肯定大多数都不是这个情况，因为目前 De­bian 10 自带的内核版本是 4.19。所以有如下几个安装方法可供选择：

1. 安装版本高于 5.6 的内核
2. 安装 wireguard 内核模块
3. 安装 wireguard-go

理论网络性能：**内核集成** ≥ **内核模块** ＞ **wireguard-go**

不过并不是所有 VPS 都能随便装，最终选择还要看 VPS 所使用的虚拟化技术：

* KVM / HyperV / XEN HVM 等完整虚拟化的 VPS 主机，以上都是可选项，根据实际情况任选其一，后面有相关说明。
* OpenVZ / LXC 等非完整虚拟化 VPS 主机，由于是共享宿主机内核，故无法对内核进行修改，就只能安装 **wireguard-go**。

如果只要安装方便快捷，对网络性能没有极致追求，又或者对以上信息一脸懵逼，请直接移步到 **安装 wireguard-go** 章节。

### 安装新版内核

KVM / Hy­perV / XEN HVM 等完整虚拟化的 VPS 主机，且能应对更换内核可能带来的不良后果则可以这个方式。

为了系统的稳定性推荐安装 back­ports 仓库中的内核 (截止发文版本为 5.9)。以下是一把梭命令：

```
sudo apt -t $(lsb_release -sc)-backports install linux-image-$(dpkg --print-architecture) linux-headers-$(dpkg --print-architecture) --install-recommends -y
```

安装完重启，并执行 `uname -r` 命令查看内核版本来确认新内核是否被启用。

### 安装 wireguard 内核模块

这个安装方式博主个人并不是很推荐，对于 Linux 不熟悉的人很容易出错，尤其是使用过改内核的脚本一顿骚操作改了一些未知来源的 “BBR 减速内核”。

KVM / Hy­perV / XEN HVM 等完整虚拟化的 VPS 主机，内核版本 5.6 以下可以尝试执行以下命令安装 wire­guard 动态内核模块。

```
sudo apt install wireguard-dkms -y
```

安装后执行 `modprobe wireguard` 命令加载 Wire­Guard 内核模块。

最后执行 `lsmod | grep wireguard` 命令检查是否成功加载。

### 安装 wireguard-go

OpenVZ 或 LXC 的 VPS 与不想折腾内核、追求稳定的小伙伴可以安装 `wireguard-go`。理论网络性能可能不及内核集成方案，不过对于正常使用而言还是绰绰有余的。

> **TIPS:** 对于 OpenVZ 或 LXC 的 VPS 需要先执行`lsmod | grep tun`命令来检查 TUN/TAP 功能是否正常启用，若没有请自行咕鸽搜索开启方法，否则安装了也是不能使用的。

自己编译或者使用博主写的一把梭脚本来安装已编译好的最新稳定版 `wireguard-go` 二进制文件：

```
curl -fsSL git.io/wireguard-go.sh | sudo bash
```

## 尾巴

安装完成你就可以开始你的 Wire­Guard 折腾之旅了。

[取消回复](https://blog.upx8.com/3139#respond-post-3139)

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