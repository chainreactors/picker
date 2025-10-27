---
title: Ubuntu 服务器网卡外网IP丢失问题排查与修复记录
url: https://blog.upx8.com/4759
source: 黑海洋 - Wiki
date: 2025-04-21
fetch_date: 2025-10-06T22:04:25.464385
---

# Ubuntu 服务器网卡外网IP丢失问题排查与修复记录

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Ubuntu 服务器网卡外网IP丢失问题排查与修复记录

发布时间:
2025-04-20

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
76374

## 问题背景

在使用Linux服务器进行程序部署时，经常会遇到各种网络连接问题。最近我在工作中遇到一个比较典型的情况：服务器重启后突然无法通过SSH连接，外网也ping不通，但通过VNC却能正常登录。经过一系列排查，最终发现问题出在网卡IP绑定上。我将详细记录这个问题的排查过程和解决方案。

## 问题现象

服务器出现以下异常情况：

1. 无法通过SSH远程连接服务器
2. 执行ping命令测试外网连通性失败
3. 通过云服务商提供的VNC控制台可以正常登录系统
4. 初步检查了DNS设置、防火墙规则、路由表以及云平台网络配置，均未发现明显异常

## 问题排查过程

首先使用`ip a`命令检查网络接口配置，

输出结果显示`eth0`网卡上没有绑定外网IP地址，这解释了为什么无法通过外网访问服务器。

接着尝试通过DHCP自动获取IP地址：

```
sudo dhclient -v eth0
```

命令返回如下结果：

```
bound to 109.115.15.22 -- renewal in 3600 seconds.
```

这个输出表明：

1. 外网IP地址(101.168.25.154)实际上仍然有效
2. 问题只是IP地址没有被正确绑定到网卡上

## 问题解决方案

### 临时解决方案

强制刷新 DHCP 并重新获取IP进行绑定（临时的）：

```
sudo dhclient -r eth0    # 释放当前 DHCP 租约
sudo dhclient -v eth0    # 重新获取 IP
```

验证网络是否恢复：`ping 8.8.8.8`

如果能够正常ping通，说明网络连接已恢复。

### ![](https://cdn.skyimg.de/up/2025/4/20/28fk5w.webp)

### 永久解决方案

为了防止服务器重启后再次出现IP丢失的问题：

#### **不要混用 `netplan` 和 `interfaces`网络服务，用本文推荐使用 `netplan`**

##### **netplan 操作步骤：**

1. **禁用传统 `interfaces networking` 服务**：

   ```
   sudo systemctl stop networking
   sudo systemctl disable networking
   ```
2. **备份并清空 `/etc/network/interfaces`** ：

   ```
   sudo mv /etc/network/interfaces /etc/network/interfaces.bak
   ```
3. **配置 `netplan`** ：

   ```
   sudo nano /etc/netplan/01-netcfg.yaml
   ```

   写入以下内容（根据你的实际网络参数调整）：

   ```
   network:
     version: 2
     renderer: networkd
     ethernets:
       eth0:
         dhcp4: no
         addresses: [109.115.15.22/24]
         gateway4: 109.115.15.1
         nameservers:
           addresses: [8.8.8.8, 8.8.4.4]
   ```

   完成后，快捷键`Ctrl + O`保存`Ctrl + X`退出
4. **应用配置**：

   ```
   sudo netplan apply
   ```

## 总结

这个案例展示了Ubuntu服务器上一种典型的网络连接问题。通过系统命令排查，我们发现根本原因是网卡没有正确绑定外网IP地址。虽然手动绑定可以临时解决问题，但建议进一步检查系统网络配置，找出IP地址丢失的根本原因，以避免问题再次发生。

[取消回复](https://blog.upx8.com/4759#respond-post-4759)

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