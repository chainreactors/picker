---
title: 懒猫微服外挂虚拟机管理器 WebVirtCloud 启动方法说明
url: https://www.zhaoj.in/read-9096.html
source: glzjin
date: 2025-02-06
fetch_date: 2025-10-06T20:35:24.057647
---

# 懒猫微服外挂虚拟机管理器 WebVirtCloud 启动方法说明

[![glzjin](https://www.zhaoj.in/wp-content/uploads/2016/04/1460635478e753758d45e5fb95f465e8ceaaabe897.png)](https://www.zhaoj.in/ "glzjin")

西兴街道物理安全研究员 | 原学生@北京联合大学 | 信息安全爱好者 | 全栈开发 | OSCP | OSWE | OSEP | OSED | OSCE3 | OSWA | OSWP | OSDA | OSMR | KLCP | CISSP | ASCP | S+ | PMP | 为心中的美好而战

* [上一篇文章](https://www.zhaoj.in/read-9077.html)

* [Glzjin](https://www.zhaoj.in/read-author/glzjin "作者简介")

切换导航

* [首页](https://www.zhaoj.in "首页")
* [Support Me!](https://www.zhaoj.in/support-me "Support Me!")

## [懒猫微服外挂虚拟机管理器 WebVirtCloud 启动方法说明](https://www.zhaoj.in/read-9096.html)

张贴在 [2025年2月5日](https://www.zhaoj.in/read-date/2025/02/05 "懒猫微服外挂虚拟机管理器 WebVirtCloud 启动方法说明") 来自 [Glzjin](https://www.zhaoj.in/read-author/glzjin) in  [技术](https://www.zhaoj.in/read-category/tech "查看技术中的全部文章")

Table of Contents

Toggle

* [前言](#%E5%89%8D%E8%A8%80 "前言")
* [步骤](#%E6%AD%A5%E9%AA%A4 "步骤")
* [参考和致谢](#%E5%8F%82%E8%80%83%E5%92%8C%E8%87%B4%E8%B0%A2 "参考和致谢")

## 前言

懒猫微服用着还不错，但缺个虚拟机管理器。

应用商店里这些应用能启动特定系统的虚拟机，但也只能启动特定系统的，而且没有办法映射虚拟机里的端口出来。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17384238293a8cdcb86fba8abf6aefa7d7e33e6229-1024x551.png)

综合起来猫上最适合这个管虚拟机，pve要创网桥，但网桥出来不过networkmanager会把dns搞坏，virtmanager是桌面端程序，没身份验证，操作起来也不算太方便。

## 步骤

1.申请官方开发者权限，然后按照[这里](https://developer.lazycat.cloud/dockerd-support.html)的说明把 Dockerd 模式打开。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173842397053ee0bd6ae2e407cc79a85520264d615-1024x859.png)

2. 应用里打开 Dockge，把下面的

```
version: "3.8"
services:
  webvirtcloud:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/webvirtcloud:1
    container_name: webvirtcloud
    restart: unless-stopped
    privileged: true
    volumes:
      - /data/document/<你的懒猫微服用户名>/WebVirtCloud/dbconfig:/srv/webvirtcloud/dbconfig
      - /data/document/<你的懒猫微服用户名>/WebVirtCloud/libvirt:/etc/libvirt
      - /data/document/<你的懒猫微服用户名>/WebVirtCloud/images:/var/lib/libvirt/images
      - /dev:/dev
      - /sys/fs/cgroup/:/sys/fs/cgroup/
    environment:
      - TZ=Asia/Shanghai
      - HOST=<分配给 VirtManager 面板的IP>
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
  webvirtcloud:
    image: crpi-3y0s0ug8uy5x8vwi.cn-hangzhou.personal.cr.aliyuncs.com/glzjinglzjin-lzc/webvirtcloud:1
    container_name: webvirtcloud
    restart: unless-stopped
    privileged: true
    volumes:
      - /data/document/glzjin/WebVirtCloud/dbconfig:/srv/webvirtcloud/dbconfig
      - /data/document/glzjin/WebVirtCloud/libvirt:/etc/libvirt
      - /data/document/glzjin/WebVirtCloud/images:/var/lib/libvirt/images
      - /dev:/dev
      - /sys/fs/cgroup/:/sys/fs/cgroup/
    environment:
      - TZ=Asia/Shanghai
      - HOST=192.168.100.52
    networks:
      macvlan_net:
        ipv4_address: 192.168.100.52
networks:
  macvlan_net:
    driver: macvlan
    driver_opts:
      parent: enp2s0
    ipam:
      config:
        - subnet: 192.168.100.0/24
          ip_range: 192.168.100.48/28
          gateway: 192.168.100.1
```

这里的docker-compose.yml是猫插网线连到路由器的情况；如果是无线网络则把 enp2s0 改为 wlp4s0 试试（未测试过）。

粘贴好，修改好之后，点击部署，等待启动完成即可。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387418451275e5a72aea0442bd67fad2b69332a7-1024x384.png)

3. 然后打开刚刚给 WebVirtCloud 配置的IP，使用默认用户名 admin，密码 admin 登录。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738741908e7afbb176fa86d41d64781c683181081-1024x609.png)

a. 点击计算节点。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173874196887c34e76bd6cdcf415d829580554220b-1024x384.png)

然后点击“本地”按钮，输入计算节点名字 local，创建一个本地计算节点。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/173874200421c37ad2f1d8c7bffcdc1afe452af44f-1024x380.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742026b6ccc5ce4093216acfc14a0fc987b0a9-1024x376.png)

b. 然后点击查看按钮，进入计算节点管理页面。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742062d67e0ae5b068caa0eef17ea4410b361f-1024x404.png)

c. 点选到网络选项卡，点选+号，添加一个 macvtap 网络。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387421112646de38a987e3043be9aa4ad8a802fc-827x1024.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387421948ec5cfa85f2a2c1ab8582a1c0764c622-1024x510.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742177ef8b207829478980f02dfbc89f64f113-1024x483.png)

d. 然后点击到储存选项卡，点击 + 号，创建一个储存池。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742248873b15cad045b61c4e08bb53b39b60b5-1024x346.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742283281327a81508edbcd2067d9cc9303b31-1024x446.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742317f918d1c6894a3d1f78f314201d3e900a-1024x577.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387423260be53336d6c26d400a2ac9b5e8e27e78-1024x648.png)

e. 然后就可以把系统镜像放到这个目录下。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387427062cca36999a5604293a82267431179005-1024x630.png)

f. 然后就可以根据自己的需要创建虚拟机，启动使用了。

![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387427344a45c60cb4561b54b638e1534f1a76a2-1024x356.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387427451add945f312d32a9861b67139e4bf2ac-1024x323.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/173874275772bf8d9969e4a945252ee3b09a3162d7-1024x463.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742771f86a8daea27467032bf546995c56b90e-1024x700.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742793edf8fed17ba390f1179004b91927423e-1024x657.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742806a3b68eef983f385caf461bb45f6cfb6b-1024x636.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/1738742833415c537b7a9af3e20bf5b1965c2fbfac-1024x697.png)
![](https://www.zhaoj.in/wp-content/uploads/2025/02/17387429059ddb900c8bf2bd58a1409c3f2a7b4381-1024x622.png)

## 参考和致谢

* <https://github.com/retspen/webvirtcloud>

### 发表回复 [取消回复](/read-9096.html#respond)

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
[![](https://www.zhaoj.in/wp-content/uploads/2023/08/16920252635e4e7eae17044686e7...