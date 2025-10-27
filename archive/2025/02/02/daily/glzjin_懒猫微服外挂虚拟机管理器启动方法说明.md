---
title: 懒猫微服外挂虚拟机管理器启动方法说明
url: https://www.zhaoj.in/read-9046.html
source: glzjin
date: 2025-02-02
fetch_date: 2025-10-06T20:36:04.547410
---

# 懒猫微服外挂虚拟机管理器启动方法说明

[![glzjin](https://www.zhaoj.in/wp-content/uploads/2016/04/1460635478e753758d45e5fb95f465e8ceaaabe897.png)](https://www.zhaoj.in/ "glzjin")

西兴街道物理安全研究员 | 原学生@北京联合大学 | 信息安全爱好者 | 全栈开发 | OSCP | OSWE | OSEP | OSED | OSCE3 | OSWA | OSWP | OSDA | OSMR | KLCP | CISSP | ASCP | S+ | PMP | 为心中的美好而战

* [上一篇文章](https://www.zhaoj.in/read-9027.html)
* [下一篇文章](https://www.zhaoj.in/read-9077.html)

* [1](#com_container "显示评论")
* [Glzjin](https://www.zhaoj.in/read-author/glzjin "作者简介")

切换导航

* [首页](https://www.zhaoj.in "首页")
* [Support Me!](https://www.zhaoj.in/support-me "Support Me!")

## [懒猫微服外挂虚拟机管理器启动方法说明](https://www.zhaoj.in/read-9046.html)

张贴在 [2025年2月1日](https://www.zhaoj.in/read-date/2025/02/01 "懒猫微服外挂虚拟机管理器启动方法说明") 来自 [Glzjin](https://www.zhaoj.in/read-author/glzjin) in  [技术](https://www.zhaoj.in/read-category/tech "查看技术中的全部文章")

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

## 步骤

1.申请官方开发者权限，然后按照[这里](https://developer.lazycat.cloud/dockerd-support.html)的说明把 Dockerd 模式打开。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173842397053ee0bd6ae2e407cc79a85520264d615-1024x859.png)

2. 应用里打开 Dockge，把下面的

```
version: "3.8"
services:
  virt-manager:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/virtmanager:8cf5a0c04f58c4216bc5f98ccb8dc4d5_1
    restart: always
    # network_mode: host
    environment:
      # Set DARK_MODE to true to enable dark mode
      DARK_MODE: false
      # If connecting to remote libvirtd, you can use a qemu+ssh string like below. Default qemu:///system will connect to local libvirtd:
      # HOSTS: "['qemu+ssh://user@host1/system', 'qemu+ssh://user@host2/system']"
      HOSTS: "['qemu:///system']"
    # If on an Ubuntu host (or any host with the libvirt AppArmor policy, you will need to use an ssh connection to localhost
    # or use qemu:///system and uncomment the below line to run the container in privileged mode:
    privileged: true
    volumes:
      # Volumes needed if connecting to local qemu:///system
      # - "/var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock"
      - /data/document/<你的懒猫微服用户名>/VirtManager/images:/var/lib/libvirt/images
      - /data/document/<你的懒猫微服用户名>/VirtManager/etc:/etc/libvirt
      - /data/document/<你的懒猫微服用户名>/VirtManager/run:/var/run/libvirt
      - /dev:/dev
      - /sys/fs/cgroup:/sys/fs/cgroup
    # If connecting to remote libvirtd, substitute location of ssh private key, e.g.:
    # - /home/user/.ssh/id_rsa:/root/.ssh/id_rsa:ro
    device_cgroup_rules:
      - c *:* rwm
      #devices:
      # Not needed if connecting to remote libvirtd
      #  - /dev:/dev
    networks:
      macvlan_net:
        ipv4_address: <分配给 VirtManager 面板的IP>
networks:
  macvlan_net:
    driver: macvlan
    driver_opts:
      parent: enp2s0
    ipam:
      config:
        - subnet: <路由器网段>
          ip_range: <分配给 VirtManager 面板的IP>/32
          gateway: <路由器网关IP>
```

在粘贴到里面之后，有几个需要修改设置的地方：

* 分配给 VirtManager 面板的IP：局域网内直接访问这个IP打开 VirtManager。例：192.168.31.108
* 路由器网段：路由器的LAN网段。例：192.168.31.0/24
* 路由器网关IP：路由器的LAN网关IP。例：192.168.31.1
* 你的懒猫微服用户名：你的懒猫微服用户名。例：glzjin

整体填写完例子如下：

```
version: "3.8"
services:
  virt-manager:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/virtmanager:8cf5a0c04f58c4216bc5f98ccb8dc4d5_1
    restart: always
    # network_mode: host
    environment:
      # Set DARK_MODE to true to enable dark mode
      DARK_MODE: false
      # If connecting to remote libvirtd, you can use a qemu+ssh string like below. Default qemu:///system will connect to local libvirtd:
      # HOSTS: "['qemu+ssh://user@host1/system', 'qemu+ssh://user@host2/system']"
      HOSTS: "['qemu:///system']"
    # If on an Ubuntu host (or any host with the libvirt AppArmor policy, you will need to use an ssh connection to localhost
    # or use qemu:///system and uncomment the below line to run the container in privileged mode:
    privileged: true
    volumes:
      # Volumes needed if connecting to local qemu:///system
      # - "/var/run/libvirt/libvirt-sock:/var/run/libvirt/libvirt-sock"
      - /data/document/glzjin/VirtManager/images:/var/lib/libvirt/images
      - /data/document/glzjin/VirtManager/etc:/etc/libvirt
      - /data/document/glzjin/VirtManager/run:/var/run/libvirt
      - /dev:/dev
      - /sys/fs/cgroup:/sys/fs/cgroup
    # If connecting to remote libvirtd, substitute location of ssh private key, e.g.:
    # - /home/user/.ssh/id_rsa:/root/.ssh/id_rsa:ro
    device_cgroup_rules:
      - c *:* rwm
      #devices:
      # Not needed if connecting to remote libvirtd
      #  - /dev:/dev
    networks:
      macvlan_net:
        ipv4_address: 192.168.31.108
networks:
  macvlan_net:
    driver: macvlan
    driver_opts:
      parent: enp2s0
    ipam:
      config:
        - subnet: 192.168.31.0/24
          ip_range: 192.168.31.108/32
          gateway: 192.168.31.1
```

这里的docker-compose.yml是猫插网线连到路由器的情况；如果是无线网络则把 enp2s0 改为 wlp4s0 试试（未测试过）。

粘贴好，修改好之后，点击部署，等待启动完成即可。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17384615052872d80824a2ce3908282d7326ef7400-1024x579.png)

3. 然后打开刚刚给 VirtManager 配置的IP，开始创建虚拟机。

a. 点击+号，新建虚拟机。选择安装媒体来源是本地安装媒体，然后点击下一步按钮。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173846152777d6e6772023e4d72bae90f985dd54fb-966x1024.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17384615666ac224769eea313971dfdaee6cadb3d9.png)

b. 然后这时就可以把安装系统要用的 ISO 文件拷贝到懒猫网盘里这个目录下了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738424969697680784d3bbb64d75938bd7c130514-1024x633.png)

点击 浏览按钮，就可以选择到这个 ISO 文件了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173846161127d2d134d184c0bddce09e7b26a8044e-1024x553.png)

选择好安装镜像之后，点击下一步。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738461689ec9d3b2bb8b3e2f5548c057d7c9fad88.png)

c. 然后选择虚拟机的内存大小和CPU核心数。选择完点击下一步。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173846172157f96b9048eb1f77a20de089ffcd3acf.png)

d. 然后输入虚拟机磁盘大小。选择完点击下一步。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738461760fafef16d8b349c433ed59bea2f5358ff.png)

e. 到最后一步，确认信息，然后在这里就可以选择网络类型了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738461816cb0d753027955159011ec161579105e2-774x1024.png)

网络选择 macvtap这种模式，也就是图上这种模式，这种情况下相当于虚拟机网线直接插到路由器网口上了，可以直接在路由器内网里进行访问，方便。

点击 FInish，即可启动。

f. 等待磁盘初始化完毕，即可安装系统，正常使用。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173846185747859f052ae6cd9b71dca88517c570a2-1024x527.png)

## 参考和致谢

* <https://github.com/m-bers/docker-virt-manager>

### 1 个评论

1. #### [懒猫微服外挂Proxmox启动方法说明 – glzjin](https://www.zhaoj.in/read-9077.html)

   [2025年2月3日](https://www.zhaoj.in/read-9046.html#comment-112609)

   […] 上一篇文章 […]

   [回复](https://www.zhaoj.in/read-9046.html?replytocom=112609#respond)

### 发表回复 [取消回复](/read-9046.html#respond)

[ ]

Δ

这个站点使用 Akismet 来减少垃圾评论。[了解你的评论数据如何被处理](https://akismet.com/privacy/)。

搜索：

## 徽章

[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734445325571d75c6436fa548006cddc04f6ef1c-300x300.png)](https://www.credential.net/654f2e4d-5a2e-459d-94fb-e117222189e9)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673444615edb40fbf418bc270edb03369b4b7bbc3-300x300.png)](https://www.credential.net/7e97fcef-5e89-40af-b1f4-44c47c1769a2)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/1673445191c6c3ab3b6e1d855d4792b4ba2d27b500.png)](https://www.credential.net/32a355ca-b457-441c-b389-9d4f6366309a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/16734452706cbff8050d185a5d2ca8b9692bd97028.png)](https://www.credential.net/2db25872-7a1d-4dc0-86d5-15b791f4a61a)
[![](https://www.zhaoj.in/wp-content/uploads/2023/01/167344535978763b8411b74ea06bed1717e8074d75...