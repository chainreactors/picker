---
title: 懒猫微服外挂ProxmoxVE启动方法说明
url: https://www.zhaoj.in/read-9077.html
source: glzjin
date: 2025-02-04
fetch_date: 2025-10-06T20:35:41.071419
---

# 懒猫微服外挂ProxmoxVE启动方法说明

[![glzjin](https://www.zhaoj.in/wp-content/uploads/2016/04/1460635478e753758d45e5fb95f465e8ceaaabe897.png)](https://www.zhaoj.in/ "glzjin")

西兴街道物理安全研究员 | 原学生@北京联合大学 | 信息安全爱好者 | 全栈开发 | OSCP | OSWE | OSEP | OSED | OSCE3 | OSWA | OSWP | OSDA | OSMR | KLCP | CISSP | ASCP | S+ | PMP | 为心中的美好而战

* [上一篇文章](https://www.zhaoj.in/read-9046.html)
* [下一篇文章](https://www.zhaoj.in/read-9096.html)

* [Glzjin](https://www.zhaoj.in/read-author/glzjin "作者简介")

切换导航

* [首页](https://www.zhaoj.in "首页")
* [Support Me!](https://www.zhaoj.in/support-me "Support Me!")

## [懒猫微服外挂ProxmoxVE启动方法说明](https://www.zhaoj.in/read-9077.html)

张贴在 [2025年2月3日](https://www.zhaoj.in/read-date/2025/02/03 "懒猫微服外挂ProxmoxVE启动方法说明") 来自 [Glzjin](https://www.zhaoj.in/read-author/glzjin) in  [技术](https://www.zhaoj.in/read-category/tech "查看技术中的全部文章")

**说明：接下来的操作会造成懒猫短暂失联，内网IP变化，请做好重新连接懒猫的准备。请确保猫是通过网线连接的，当前方式创建网桥时命令是针对有线连接的，无线连接请自行打开 nmtui 进行网桥配置。**

**说明：接下来的操作会造成懒猫短暂失联，内网IP变化，请做好重新连接懒猫的准备。请确保猫是通过网线连接的，当前方式创建网桥时命令是针对有线连接的，无线连接请自行打开 nmtui 进行网桥配置。**

**说明：接下来的操作会造成懒猫短暂失联，内网IP变化，请做好重新连接懒猫的准备。请确保猫是通过网线连接的，当前方式创建网桥时命令是针对有线连接的，无线连接请自行打开 nmtui 进行网桥配置。**

Table of Contents

Toggle

* [前言](#%E5%89%8D%E8%A8%80 "前言")
* [步骤](#%E6%AD%A5%E9%AA%A4 "步骤")
* [参考和致谢](#%E5%8F%82%E8%80%83%E5%92%8C%E8%87%B4%E8%B0%A2 "参考和致谢")

## 前言

懒猫微服用着还不错，但缺个虚拟机管理器。

应用商店里这些应用能启动特定系统的虚拟机，但也只能启动特定系统的，而且没有办法映射虚拟机里的端口出来。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17384238293a8cdcb86fba8abf6aefa7d7e33e6229-1024x551.png)

所以还是用官方提供的 Dockge，打算配合 VirtManager 和 KVM 来自由地启动虚拟机。

之前在 <https://www.zhaoj.in/read-9046.html> 这里有移植 VirtManager 过来，但觉得还是差点意思，想着 iStore 上有 Proxmox，找了下找到 <https://github.com/GreenDamTan/DockerFile/tree/c8dc3b2ff86384e579991b0edf8192e6a2faaf96/ProxmoxVE> 这里，就想着弄过来，方便管理虚拟机。

## 步骤

1.申请官方开发者权限，然后按照[这里](https://developer.lazycat.cloud/dockerd-support.html)的说明把 Dockerd 模式打开。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173842397053ee0bd6ae2e407cc79a85520264d615-1024x859.png)

2. 在官方VIP群里联系官方推送升级猫的 baseos 版本，说明要手工开启网桥。

3. 确保猫插着网线，然后 SSH 连进猫，输入如下命令配置网桥。

```
nmcli con add type bridge ifname br-lan con-name br-lan
nmcli con mod br-lan bridge.stp no
nmcli con modify br-lan ipv4.method auto
nmcli con modify br-lan ipv6.method auto
nmcli con add type bridge-slave ifname enp2s0 master br-lan
nmcli con up br-lan
reboot
```

这里启动之后，会导致猫重新分配IP，因为桥接之后MAC地址变了，需要到路由器上看下新的IP。

4. 应用里打开 Dockge，把下面的

```
version: "3.8"
services:
  pve:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/pve:4
    shm_size: 4gb
    hostname: pve
    privileged: true
    devices:
      - /dev/dri
      - /dev/fuse
      - /dev/kvm
      - /dev/vfio
      - /dev/nvidia0
      - /dev/nvidiactl
      - /dev/nvidia-uvm
      - /dev/nvidia-uvm-tools
      - /dev/nvidia-vgpu1
    volumes:
      - /data/document/<你的懒猫微服用户名>/PVE/pve-cluster:/var/lib/pve-cluster
      - /data/document/<你的懒猫微服用户名>/PVE/vz:/var/lib/vz
    environment:
      root_password: <PVE root密码>
    network_mode: host
```

在粘贴到里面之后，有几个需要修改设置的地方：

* 你的懒猫微服用户名：你的懒猫微服用户名。例：glzjin
* PVE root密码: 想要设置的root密码。

整体填写完例子如下：

```
version: "3.8"
services:
  pve:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/pve:4
    shm_size: 4gb
    hostname: pve
    privileged: true
    devices:
      - /dev/dri
      - /dev/fuse
      - /dev/kvm
      - /dev/vfio
      - /dev/nvidia0
      - /dev/nvidiactl
      - /dev/nvidia-uvm
      - /dev/nvidia-uvm-tools
      - /dev/nvidia-vgpu1
    volumes:
      - /data/document/glzjin/PVE/pve-cluster:/var/lib/pve-cluster
      - /data/document/glzjin/PVE/vz:/var/lib/vz
    environment:
      root_password: root
    network_mode: host
```

这里的docker-compose.yml是猫插网线连到路由器，路由器DHCP分配IP的情况；如果是无线网络则把 enp2s0 改为 wlp4s0 试试（未测试过）。

粘贴好，修改好之后，点击部署，等待启动完成即可。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173881916184030b232c78757fa8994cb15151d0b9-1024x567.png)

4. 打开 https://猫新的IP:8006，即可打开 Proxmox 界面。

用户名：root

密码：在部署时候设置的密码

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738551569e1e3926ff775d0798a1234e9aa144718-1024x530.png)

5. 然后就可以创建虚拟机了。

a. 右键点击“创建虚拟机”按钮。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738551698cd3b94a33c2f5ccbad439fc30fad5468-1024x523.png)

b. 根据自己需求自由配置即可。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173855173729add5aefb9ebb0e8130ab33aa1a455c-1024x780.png)

系统镜像这里，把镜像拷贝到网盘这个目录下就可以看到了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17385517894c8b6f82a82f2bd74769d552bd0bd56f-1024x643.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/173855176102352cd8a5cff880aecef697f20a0ac9-1024x709.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/173855180334018cb98f5fabd5488eade14786564a-1024x773.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17385518263d787fd0016da2bc3bbba860c3a161e5-1024x788.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17385518361dd153640c5b8686a17e6f063a29627d-1024x770.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17385518466dab6278f4555acef64eeb10676d941c-1024x769.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/173855185757848de41d0577254d00e126ceed9150-1024x764.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738551869e7697b51d2443c8d720e267656b539e8-1024x775.png)

c. 然后就可以启动虚拟机了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738551909f9ab04a5e2a08bf398b59083f8f088eb-1024x519.png)

## 参考和致谢

* <https://github.com/GreenDamTan/DockerFile/tree/c8dc3b2ff86384e579991b0edf8192e6a2faaf96/ProxmoxVE>

### 发表回复 [取消回复](/read-9077.html#respond)

[ ]

Δ

这个站点使用 Akismet 来减少垃圾评论。[了解你的评论数据如何被处理](https://akismet.com/privacy/)。

搜索：

## 徽章

[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734445325571d75c6436fa548006cddc04f6ef1c-300x300.png)](https://www.credential.net/654f2e4d-5a2e-459d-94fb-e117222189e9)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673444615edb40fbf418bc270edb03369b4b7bbc3-300x300.png)](https://www.credential.net/7e97fcef-5e89-40af-b1f4-44c47c1769a2)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673445191c6c3ab3b6e1d855d4792b4ba2d27b500.png)](https://www.credential.net/32a355ca-b457-441c-b389-9d4f6366309a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734452706cbff8050d185a5d2ca8b9692bd97028.png)](https://www.credential.net/2db25872-7a1d-4dc0-86d5-15b791f4a61a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/167344535978763b8411b74ea06bed1717e8074d75.png)](https://www.credential.net/dc62a4d2-6dc6-4228-9239-41b0da2be656)
[![](https://www.zhaoj.in/wp-content/uploads/2023/02/1676555742e09433176ae66bc87039f0b7b0422118.png)](https://www.credential.net/06524a6d-c8a3-4038-a8eb-090b096a2262)
[![](https://www.zhaoj.in/wp-content/uploads/2023/02/1676555747cb011870763281fa215d0c9455c5e3c1.png)](https://www.credential.net/0bf8a228-9ce4-4483-a8c3-f4ee75f56a5d)
[![](https://www.zhaoj.in/wp-content/uploads/2023/03/1677771656d2008b9c0d3c40d41c002c0864debaf3.png)](https://www.credential.net/8534d4fe-0f91-4681-9b7f-997d198df348)
[![](https://www.zhaoj.in/wp-content/uploads/2023/05/1683419874c9a3e47c563365b54d1b984805089b65.png)](https://www.credential.net/323868a7-3020-4f71-8a6c-8f35c7b9f16e)
[![](https://www.zhaoj.in/wp-content/uploads/2023/08/16920252635e4e7eae17044686e78ab5e5320ec13e.png)](https://www.credential.net/c6114609-71cf-45bd-afd5-1b81279e08fd)
[![](https://www.zhaoj.in/wp-content/uploads/2023/05/168315770646f0d8a9332b8a7dc7279c768e506133.png)](https://www.credly.com/badges/b184262f-6522-4510-a8c7-e6c78f51a3b6/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/10/16974592460a56d06d649541552c71a8b681de164f.png)](https://www.credly.com/badges/7b7bc694-9783-46f8-8f32-2f138abb0139/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734456142f9c80ea30c2f23de9e687e64aa2d9cb.png)](https://www.credly.com/badges/d68f72b5-55c6-4f32-8323-b979d9f46987/public_url)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673446237b5cd39a62b1f9bae1ce7b867b9deb321.png)](https://www.credly.com/badges/2cf7a1cb-1265-4de1-...