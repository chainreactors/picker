---
title: 车联网安全入门之从CAN模拟环境搭建到重放攻击
url: https://www.secpulse.com/archives/197219.html
source: 安全脉搏
date: 2023-03-10
fetch_date: 2025-10-04T09:06:09.955772
---

# 车联网安全入门之从CAN模拟环境搭建到重放攻击

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

# 车联网安全入门之从CAN模拟环境搭建到重放攻击

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-09

12,967

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331422.png)

# 前言

车联网安全最近几年成为了各大汽车厂商以及安全厂商的关注热点，但是作为一个穷苦的无车一族想要入门车联网安全该怎么办？那当然是靠模拟器了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331422.jpeg "null")

本文将介绍如何通过Ubuntu模拟车载CAN总线的收发包来进行操作学习。话不多说，芜湖，起飞?️～

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331423.jpeg "null")

# CAN总线介绍

## 什么是CAN总线

CAN总线又称为控制器局域网是Controller Area Network的缩写。CAn总线是一种用于实时应用的串行通讯协议总线，它可以使用双绞线来传输信号，是世界上应用最广泛的现场总线之一，在1991年呗大规模应用于汽车，从那儿以后，CAN总线成为汽车的标配。

CAN协议用于汽车中各种不同元件之间的通信，以此取代昂贵笨重的配电线束。该协议的健壮性使其用途延伸到其他自动化和工业应用。简单来说就是用来控制车辆功能的通信协议，比如车门解锁、转向灯、刹车、油门等。

## CAN总线特性

安全性：CAN是低级协议，不支持任何内在的安全功能。在标准的CAN中也没有加密，使得网络数据能被截取。在大多数应用中，应用程序需要部署自己的安全机制，例如认证传入命令或网络上某些设备的存在。若不执行适当的安全措施，其他人可能设法在总线上插入消息。尽管一些安全关键功能（如修改固件，编程键或控制防抱死制动）存在密码，但这些系统并未普遍实施，并且密钥对的数量有限。

通信机制：多主机，即每个节点都有接入总线的能力

寻址机制：消息区别，不设节点的地址，通过消息的标志符来区别消息。

帧类型：数据帧、远程帧、错误帧、超载帧、帧间隔

攻击方式：应用报文模糊攻击、DOS攻击测试、重放攻击

由于CAN总线上的数据包没有进行过任何的加密处理，因此这些数据包是能够被截取窃听。由于车载网络使用CAN协议进行通信，所以我们可以联想到车联功能也是通过CAN网络进行数据发送和交换。

# 攻击方式

CAN总线攻击方式包括应用报文模糊测试、DOS攻击测试、重放攻击等。

# 攻击实战

在接下来的文章里我们将通过模拟软件模拟真实的汽车，并对其进行重放攻击

## 实验环境

* • Ubuntu16.04
* • ICSim（仪表盘模拟器）
* • Socketcand（CAN网络）
* • Kayak（一款基于SocketCAN的CAN总线分析工具）

## 安装ICSim

安装依赖

```
# 安装依赖
sudo apt install libsdl2-dev libsdl2-image-dev can-utils maven autoconf -y
# 下载ICSim
git clone https://github.com/zombieCraig/ICSim.git
# 编译安装
cd ICSim/
sudo make
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331423.png "null")

## 安装socketcand

```
# 下载socketcand
git clone https://github.com/linux-can/socketcand.git
cd socketcand

# 获取缺少的文件
wget https://raw.githubusercontent.com/dschanoeh/socketcand/master/config.h.in

# 编译安装
autoconf
./configure
make clean
make
sudo make install
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331425.png "null")

## 安装Kayak

```
# 下载
git clone https://github.com/dschanoeh/Kayak.git
# 安装jdk
sudo apt-get install openjdk-8-jdk
# 安装
cd Kayak
mvn clean package
```

## 启动模拟器

```
# 设置vcan（虚拟CAN）接口
sudo modprobe can
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331428.png "null")

```
# 打开仪表盘模拟器
./icsim vcan0
# 打开仪表盘控制器
./controls vcan0
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331431.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331432.png "null")

仪表盘控制器，操作说明

| 功能 | 控制按钮 |
| --- | --- |
| 转向 | 键盘左右 |
| 速度 | 键盘上下 |
| 开/关左前车门 | 右shift/左shit+A |
| 开/关右前车门 | 右shift/左shit+B |
| 开/关左后车门 | 右shift/左shit+X |
| 开/关右后车门 | 右shift/左shit+Y |
| 开启全部车门 | 左shift+右shift |
| 关闭全部车门 | 右shift+左shift |

## 抓取CAN数据包

```
# 使用candump抓包
candump vcan0 -l
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331435.png "null")

由于CAN在不停进行通信，故抓取到的包将会非常大

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331436.png "null")

尝试重放刚才抓取到的数据包

```
canplayer -I candump-2023-01-12_151749.log
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331441.png "null")

可以看到左前侧车门被成功打开

通过二分法我们找到了左前侧开门的数据包，如图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331444.png "null")

```
(1673507873.514241) vcan0 19B#00000E000000
```

其中的19B是设备标识符，在数据包中查找19B

```
grep 19B candump-2023-01-12_151749.log
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331447.png "null")

通过分析和尝试我们可知

`19B#00000E000000`为开启左前侧车门，`19B#00000F000000`为关闭所有车门

将其分解为二进制可得出16种可能的开关门组合

| 二进制 | 十六进制 |
| --- | --- |
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |
| 0101 | 5 |
| 0110 | 6 |
| 0111 | 7 |
| 1000 | 8 |
| 1001 | 9 |
| 1010 | a |
| 1011 | b |
| 1100 | c |
| 1101 | d |
| 1110 | e |
| 1111 | f |

尝试字符控制的不同车门

| 字符 | 车门 |
| --- | --- |
| 8 | 右后侧车门 |
| 4 | 左后侧车门 |
| 2 | 右前侧车门 |
| 1 | 左前侧车门 |

假设1是关门，0是开门

```
右后侧车门 左后侧车门 右前侧车门 左前侧车门
        8     4    2     1
        1     0    0     0
```

此时的值为8，结果为

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197219-1678331452.png "null")

至此我们就可以操控每个门的开关了。

按照同样的思路我们将转向的数据包找出来

左转向：`188#01000000`

右转向：`188#02000000`

参考链接：

https://www.freebuf.com/articles/network/281831.html

https://article.itxueyuan.com/ZoxRvk

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197219.html**](https://www.secpulse.com/archives/197219.html)

Tags: [CAN](https://www.secpulse.com/archives/tag/can)、[Controller Area Network](https://www.secpulse.com/archives/tag/controller-area-network)、[socketcand](https://www.secpulse.com/archives/tag/socketcand)、[Ubuntu](https://www.secpulse.com/archives/tag/ubuntu)、[模拟环境搭建](https://www.secpulse.com/archives/tag/%E6%A8%A1%E6%8B%9F%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)、[车联网安全](https://www.secpulse.com/archives/tag/%E8%BD%A6%E8%81%94%E7%BD%91%E5%AE%89%E5%85%A8)、[重放攻击](https://www.secpulse.com/archives/tag/%E9%87%8D%E6%94%BE%E6%94%BB%E5%87%BB)

点赞：
0
[评论：0](#goComment)...