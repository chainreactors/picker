---
title: 物联网终端安全入门与实践之玩转物联网固件（下）DIY篇
url: https://www.secpulse.com/archives/197408.html
source: 安全脉搏
date: 2023-03-15
fetch_date: 2025-10-04T09:33:51.262281
---

# 物联网终端安全入门与实践之玩转物联网固件（下）DIY篇

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 物联网终端安全入门与实践之玩转物联网固件（下）DIY篇

[IOT安全](https://www.secpulse.com/archives/category/iot-security)

[知微攻防实验室](https://www.secpulse.com/newpage/author?author_id=40030)

2023-03-14

18,722

上一篇文章主要介绍了终端设备固件常见的加密和解密方法，并结合实例带领读者了解了某些场景下固件完整的解密流程。本篇将着重介绍终端设备固件常见的DIY方法，最后通过对ASUS AC68U路由器进行固件修改带领读者走进固件DIY的世界。

**01**

**背 景**

官方固件不给力，没有自己想要的功能？作为一个懒人，想要远程快速重启设备？随着万物互联时代的到来，越来越多的奇思妙想出现在人们的脑海中。今天我们就带领大家通过魔改固件的方法实现这些想法。

**02**

**固件DIY流程**

关于固件的知识可以阅读我们之前的文章：**《物联网终端安全入门与实践之了解物联网终端》下 固件篇。**

DIY意思是英文Do It Yourself的缩写，可以正式译为自己动手做，也可译为亲力亲为。固件DIY通俗来讲就是自己动手做固件，泛指所有对固件进行改动的行为。

固件DIY目的是满足自己的特殊需要，做你需要的，做你想要的，做市场上绝无仅有、独一无二属于你自己的作品，这个是固件DIY的追求。固件DIY不仅可以在原有固件基础上新增某些功能，还可以减少某些不必要的功能，使得固件简洁、轻量化更适配设备，让设备发挥更大的效能。

**固件通常分为开源固件与闭源固件。**大部分厂商的代码都是没有开源的，提供给我们的只有已经编译打包后的固件，只有极少数厂商会把源代码开源提供给大家，例如华硕AsusWrt、起源于Linksys的OpenWRT等。本文会分别讲解开源固件与闭源固件的DIY方法。

**2.1**

**闭源固件DIY方法**

对于厂商未公开源代码的固件我们称之为闭源固件，闭源固件的DIY流程通常有三个：**固件解包、修改固件、固件重打包**。

1

**固件解包**

固件解包，顾名思义，就是对固件进行解压获取原始文件，部分厂商还会对固件进行加密处理，所以在此步骤有时还需要对固件进行解密才能正常解包，我们常用的固件解包工具有Binwalk。

2

**修改固件**

通过对固件中的文件修改或增加以实现想要的目的功能。

3

**固件重打包及刷入**

对解包后的固件文件系统进行重打包还原操作，还需要把重打包后的固件刷入目标设备。刷入新固件的时候可能会遇到固件校验不通过的问题，这个时候就需要去官网或官方论坛查找其他方法，一般设备都有救砖方法，可以通过**救砖**刷入固件。

```
救砖：目标设备无法正常使用需要通过特殊方法恢复设备
```

**2.2**

**开源固件DIY方法**

开源固件的DIY主要流程包括：获取源码与编译环境搭建、修改代码、固件编译。

1

**获取源码与编译环境搭建**

开源的设备固件源代码一般都会在一些知名代码托管平台中找得到，例如Github、国内的Gitee等，下面是一些常见的设备固件源代码地址。

* **AsusWRt**：https://github.com/hajuuk/asuswrt（已停止更新）
* **RMerl**（梅林）：https://github.com/RMerl/asuswrt-merlin（老版本，已停止更新）
* **RMerl**（梅林）：https://github.com/RMerl/asuswrt-merlin.ng（新版本）
* **OpenWRT**：https://github.com/openwrt/openwrt

各种IoT设备并不是常见的X86架构，他们的固件编译一般都是跨平台编译，所以我们需要搭建相对应的编译环境。一般都是在Linux系统上进行编译，需要根据不同固件要求安装对应依赖文件，这部分都有Wiki文档或者官方教程，参考官方教程即可完成环境部署工作，这里不再赘述。

2

**修改代码与编译固件**

该环节的主要目的是通过新增代码或修改代码的方式实现新功能。关键在于找到合适的代码修改位置。特别是逻辑上不能出现问题，不能影响固件的正常使用。

官方源代码会自带打包工具，所以使用官方源代码编译的固件能通过设备后台的固件校验算法，利用这个特性我们可以通过管理页面刷入固件而无需实际接触设备使用救砖方法。

**03**

**实战AC68U固件远程管理功能植入**

**3.1**

**闭源固件植入**

其实AC68U固件代码是开源的，不过这里我们当做未开源固件给大家进行演示。

**3.1.1 固件解包**

设备固件一般可以在官网下载，然后我们可以通过Binwalk对固件进行解包，这里推荐使用Firmware-Mod-Kit（简称FMK）对固件进行解包分析，FMK具有固件文件的解包和打包、固件提取文件系统的解压和压缩、DD-WRT Web Pages的修改等功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197408-1678760430.png)

这里我们看到固件由3部分组成，分别是TRX Firmware header 、LZMA 压缩文件、Squashfs （文件系统）组成。

**3.1.2 修改固件**

**植入自启动脚本思路**

很多路由器在启动服务的时候会使用Shell脚本去启动，这刚好给了我们可乘之机。如果我们顺利找到路由器启动过程中执行的脚本并植入我们想要执行的程序，那么路由器启动时会执行我们自定义的脚本程序，实现远程设备管理的功能。

我们应该怎样查找自启动的Shell脚本呢？有两个方法：

1. **系统日志分析。**很多路由器都提供日志的功能，我们可以通过系统启动日志查看系统运行过程中所执行的操作；
2. **系统进程分析。**系统日志不是所有信息都会记录，部分自启动服务系统日志是无法记录的，这个时候我们可以通过查看系统进程信息去查找。

**3.1.2.1 系统日志分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197408-1678760438.png)

```
May  5 13:05:20 wsdd2[524]: error: wsdd-mcast-v4: wsd_send_soap_msg: send
May  5 13:05:21 lldpd[544]: cannot get ethtool link information with GLINKSETTINGS (requires 4.9+): Operation not permitted
May  5 13:05:21 lldpd[544]: cannot get ethtool link information with GSET (requires 2.6.19+): Operation not permitted
May  5 13:05:23 custom_script: Running /jffs/scripts/services-start
May  5 13:05:23 admin: [软件中心]-[ks-services-start.sh]: /koolshare/init.d/V01softok.sh
May  5 13:05:23 kernel: et0: et_mvlan_netdev_event: event 8 for vlan2 mvlan_en 0
May  5 13:05:23 kernel: et0: et_mvlan_netdev_event: event 13 for vlan2 mvlan_en 0
May  5 13:05:23 kernel: et0: et_mvlan_netdev_event: event 1 for vlan2 mvlan_en 0
May  5 13:05:23 admin: [软件中心]-[V01softok.sh]: skipd进程准备就绪！
May  5 13:05:24 admin: [软件中心]-[V01softok.sh]: httpdb进程准备就绪！
May  5 13:05:24 kernel: xhci_hcd 0000:00:0c.0: Failed to enable MSI-X
May  5 13:05:24 kernel: xhci_hcd 0000:00:0c.0: failed to allocate MSI entry
May  5 13:05:24 kernel: usb usb1: No SuperSpeed endpoint companion for config 1  interface 0 altsetting 0 ep 129: using minimum values
May  5 13:05:24 Mastiff: init
May  5 13:05:25 kernel: SCSI subsystem initialized
May  5 13:05:25 kernel: csw_retry 100
May  5 13:05:25 syslog:  event: wl_chanspec_changed_action
May  5 13:05:25 syslog: skip event due no re
May  5 13:05:26 syslog: fwver: 386.5_2 (sn: /ha:04:D4:C4:BC:A2:F0 )
May  5 13:05:31 roamast: ROAMING Start...
```

我们发现在系统启动过程中会运行/koolshare/init.d/V01softok.sh 脚本文件。

**3.1.2.2 系统进程分析**

大部分设备都有Telnet或者SSH服务，我们需要开启对应服务，并连接设备观察系统启动时的进程信息，所以需要提前在路由器后台页面开启对应服务，然后重启路由器，当设备重启完成后立刻进行连接，这里在进行操作时手速要快，因为Shell脚本执行时间比较短，执行完成就退出了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197408-1678760441.png)

通过查看系统进程发现系统启动过程中会运行 /usr/sbin/getrealip.sh。知道了系统启动时所执行的Shell脚本，我们就可以直接修改对应的脚本文件，植入自定义功能，例如：定时发起心跳包监控设备存活状态、远程管理等。

不过，实际过程中一般不会直接修改当前的Shell脚本，而是分析系统调用关系反向查找，找到源头文件，直接修改源文件内容，这样更隐蔽，而且在路由器重置的时候植入的脚本不会丢失。

当设备处于内网环境的时候，我们想要远程进入设备终端是一件很困难的事情，这里我们使用Shell脚本实现一个远程终端管理的功能，让设备通过反弹的方式定时回连到我们公网服务器，这样我们只需要在公网服务器监听即可连接内网设备，实现远程管理，脚本内容如下。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/image.png "image.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/image.png)

**3.1.3 固件重打包与刷入**

1

**固件重打包**

使用FMK对固件进行重打包，直接执行build-firmware.sh 对文件进行重打包操作，这里大家可能会遇到的重打包后固件大小与原固件大小不一致导致打包失败问题，解决方法是使用 -min 参数进行打包即可。

2

**刷入固件**

在路由器后台页面进行固件更新时发现使用FMK打包的固件未能通过后台页面的固件校验，在查阅相关资料后发现ASUS路由器可以通过救援模式绕过固件校验更新固件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197408-1678760442.png)

3

**救援模式刷入固件**

救援模式参考：*https://www.asus.com.cn/support/FAQ/1000814/*

这里使用救援模式后成功刷入我们重打包的固件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197408-1678760443.png)

**3.1.4 实际效果**

* 路由器正常连接公网服务器实现远程管理功能
* 重启后路由器也能连接公网服务器实现远程管理功能

**3.2**

**开源固件植入**

**3.2.1 前期准备**

我们需要按照官方教程搭建编译环境，由于华硕官方已经对AC68U固件停止更新，所以我们使用由开源社区更新维护的梅...