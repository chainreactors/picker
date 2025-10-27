---
title: Debian 安装使用 Cloud内核降低内存消耗
url: https://blog.upx8.com/4216
source: 黑海洋 - WIKI
date: 2024-07-14
fetch_date: 2025-10-06T17:41:10.262543
---

# Debian 安装使用 Cloud内核降低内存消耗

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Debian 安装使用 Cloud内核降低内存消耗

发布时间:
2024-07-13

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
16161

最近为 Vultr 主机升级到 Debian 11，升级之后发现内存的消耗很多，基本上运行的应用很容易会被 Stop。

512M 内存明显不够，直到有人在 hostloc 论坛上安利了 cloud 内核，安装之后内存占用明显下降。

### 更新系统和安装最新软件

```
apt update -y && apt dist-upgrade -y
```

### 查看系统现在内核情况

```
~# dpkg -l|grep linux-image

linux-image-5.10.0-20-amd64          5.10.158-2                      amd64        Linux 5.10 for 64-bit PCs (signed)
linux-image-5.10.0-21-amd64          5.10.162-1                      amd64        Linux 5.10 for 64-bit PCs (signed)
linux-image-amd64                    5.10.162-1                      amd64        Linux for 64-bit PCs (meta-package)
```

### 查看 cloud 内核版本

```
~# apt-cache search linux-image | grep cloud

linux-headers-6.1.0-7-cloud-amd64 - Header files for Linux 6.1.0-7-cloud-amd64
linux-image-6.1.0-7-cloud-amd64-dbg - Debug symbols for linux-image-6.1.0-7-cloud-amd64
linux-image-6.1.0-7-cloud-amd64-unsigned - Linux 6.1 for x86-64 cloud
linux-image-cloud-amd64-dbg - Debugging symbols for Linux cloud-amd64 configuration (meta-package)
linux-image-6.1.0-7-cloud-amd64 - Linux 6.1 for x86-64 cloud (signed)
linux-image-cloud-amd64 - Linux for x86-64 cloud (meta-package)
```

### 安装 Cloud 内核

```
apt install linux-headers-6.1.0-7-cloud-amd64  \
    linux-image-cloud-amd64 -y
```

或者使用官方源的简单安装，不安装内核头文件只安装内核

```
apt install linux-image-cloud-amd64 -y
```

### 更新引导文件

```
update-grub
```

### 关机重启

```
reboot
```

### 验证是否安装成功

```
uname -r
```

### 卸载旧内核

```
dpkg --get-selections | grep linux
apt autoremove --purge linux-image-5.10.0-20-amd64
apt autoremove --purge linux-image-5.10.0-21-amd64
apt autoremove
apt autoclean
```

#### cloud 内核简介

cloud 内核是专门为云平台优化的，Cloud 内核剔除了这些无用模块的同时添加了几乎只有云平台会用到的驱动程序。裁剪掉云环境下用不到的像蓝牙、声音的支持等等这些。在 **KVM/Xen** 虚拟化的机器中，**cloud 内核**表现良好。已测试不支持 **VMware** 虚拟化，会找不到根文件系统。

1. ![Pan](https://gravatar.loli.net/avatar/avatar/f7fca928255325a30046f87e0c9e9e4e?s=32&r=&d=)

   **Pan**

   2024-12-22 11:29:50

   [回复](https://blog.upx8.com/4216/comment-page-1?replyTo=30374#respond-post-4216)

   Cloud内核有些VPS安装完后外网就无法连接了

[取消回复](https://blog.upx8.com/4216#respond-post-4216)

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