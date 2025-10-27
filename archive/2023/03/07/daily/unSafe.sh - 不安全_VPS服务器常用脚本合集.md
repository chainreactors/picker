---
title: VPS服务器常用脚本合集
url: https://buaq.net/go-152245.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:22.344155
---

# VPS服务器常用脚本合集

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/85ac14a8b852cf4b4d33bdf33171374d.jpg)

VPS服务器常用脚本合集

本帖所有脚本均来自互联网，本站仅对这些脚本进行收集，以方便自己及各位基友使用。本站不对其可用性负责，也不对其安全性等任何方面负责。目录查看CPU信息
*2023-3-6 21:53:45
Author: [blog.upx8.com(查看原文)](/jump-152245.htm)
阅读量:91
收藏*

---

本帖所有脚本均来自互联网，本站仅对这些脚本进行收集，以方便自己及各位基友使用。本站不对其可用性负责，也不对其安全性等任何方面负责。

## 目录

* 查看CPU信息
* 查看当前内核信息
* 关键字查找进程
* 内核更改 [开启BBR、更换BBRplus等]
* Linux修改主机名
* 一键开启/关闭Swap
* 缝合怪测评
* IP质量测试
* Bench – 系统信息+I/O+测速
* SuperBench – 系统信息+I/O+测速
* HyperSpeed 一键测速
* Besttrace 直接显示回程线路
* Backtrace 三网回程路由测试
* BestTrace 回程测试
* 回程测试 [Nanqinlang大佬作品]
* UnixBench.sh [秋水逸冰大佬作品]
* LemonBench.sh
* Yabs.sh [Masonr大佬作品]
* 流媒体解锁测试 [Lmc999大佬作品]
* 流媒体解锁测试 [LovelyHaochi大佬作品]
* 推荐杜甫使用-本脚本支持查看I/O bench以及system info
* 测试25端口是否开放

## 查看CPU信息

![](https://cnboy.org/wp-content/uploads/eb0b187edcf0b30.jpg)

## 查看当前内核信息

![](https://cnboy.org/wp-content/uploads/c81e728d9d4c2f6-6.jpg)

## 关键字查找进程

## 内核更改 [开启BBR、更换BBRplus等]

**复制

```
Centos
yum install ca-certificates wget -y && update-ca-trust force-enable
Debian/Ubuntu：
apt-get install ca-certificates wget -y && update-ca-certificates

不卸载内核版本：
wget -O tcpx.sh "https://github.com/ylx2016/Linux-NetSpeed/raw/master/tcpx.sh" && chmod +x tcpx.sh && ./tcpx.sh

卸载内核版本：
wget -O tcp.sh "https://github.com/ylx2016/Linux-NetSpeed/raw/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
```

![](https://cnboy.org/wp-content/uploads/0211e8160d7f43c.jpg)

## Linux修改主机名

首先执行

**复制

```
hostnamectl set-hostname <newhostname>
```

然后执行下面的命令

在第二行增加一个 `127.0.0.1 <newhostname>`，同时将文件中的原主机名修改为刚设置的新主机名

![](https://cnboy.org/wp-content/uploads/a87ff679a2f3e71-5.jpg)

## 一键开启/关闭Swap

**复制

**复制

```
wget https://www.moerats.com/usr/shell/swap.sh && bash swap.sh
```

## 缝合怪测评

* 自由组合测试方向和单项测试以及合集收录第三方脚本–原创
* 基础系统信息–感谢teddysun和superbench和yabs开源
* CPU测试–感谢lemonbench开源
* 内存测试–感谢lemonbench开源
* 磁盘IO读写测试–感谢lemonbench开源
* 硬盘IO读写测试–感谢yabs开源
* 御三家流媒体解锁–感谢sjlleo的二进制文件
* 常用流媒体解锁–感谢RegionRestrictionCheck开源
* Tiktok解锁–感谢lmc999的开源
* 三网回程以及路由延迟–感谢zhanghanyun/backtrace开源
* 回程路由以及带宽类型检测(商宽/家宽/数据中心)–由fscarmen的PR以及本人的技术思路提供
* 端口检测(检测是否被墙)–由fscarmen的PR以及作者的技术思路提供 – 待修复
* IP质量检测(检测IP白不白)(含IPV4和IPV6)–独创，感谢互联网提供的查询资源
* speedtest测速–由teddysun和superspeed的开源以及整理
* 全国网络延迟测试–感谢IPASN开源

**复制

```
bash <(wget -qO- --no-check-certificate https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh)
或
bash <(wget -qO- --no-check-certificate https://github.com/spiritLHLS/ecs/raw/main/ecs.sh)
```

## IP质量测试

**复制

```
bash <(wget -qO- --no-check-certificate https://gitlab.com/spiritysdx/za/-/raw/main/qzcheck.sh)
或
bash <(wget -qO- --no-check-certificate https://github.com/spiritLHLS/ecs/raw/main/qzcheck.sh)
```

![](https://cnboy.org/wp-content/uploads/3805675944f69b5.jpg)

## Bench – 系统信息+I/O+测速

**复制

```
wget -qO- bench.sh | bash
```

![](https://cnboy.org/wp-content/uploads/66fc2fcd68a9228.jpg)

## SuperBench – 系统信息+I/O+测速

**复制

```
wget -qO- git.io/superbench.sh | bash
或
wget -qO- --no-check-certificate https://raw.githubusercontent.com/oooldking/script/master/superbench.sh | bash
```

![](https://cnboy.org/wp-content/uploads/adc6dec04348608.jpg)

## HyperSpeed 一键测速

* 支持单线程、8线程测速，显示延迟与抖动

**复制

```
bash <(curl -Lso- https://bench.im/hyperspeed)
或
bash <(wget -qO- https://bench.im/hyperspeed)
```

![](https://cnboy.org/wp-content/uploads/b2f4ab52cb094b3.jpg)

## Besttrace 直接显示回程线路

**复制

```
wget -qO- git.io/besttrace | bash
```

### ![](https://cnboy.org/wp-content/uploads/45c48cce2e2d7fb-1-e1675141478275.jpg)

**（**\* ***部分截图*）**

## Backtrace 三网回程路由测试

**复制

```
curl https://raw.githubusercontent.com/zhanghanyun/backtrace/main/install.sh -sSf | sh
```

### ![](https://cnboy.org/wp-content/uploads/3732dc439f152a5.jpg)

## BestTrace 回程测试

* ipip.net 提供的手动输入IP测试回程线路工具

**复制

```
mkdir /root/besttrace
cd /root/besttrace
wget https://cdn.ipip.net/17mon/besttrace4linux.zip
unzip besttrace4linux.zip

解压之后会看到几个二进制文件,根据自己的系统选择对应文件。常用的：

Linux X64系统：
chmod +x besttrace
./besttrace xxx.xxx.xxx.xxx   # 此处输入需测试IP

Linux X32位系统：
chmod +x besttrace32
./besttrace32 xxx.xxx.xxx.xxx   # 此处输入需测试IP

ARM机型：
chmod +x besttracearm
./besttracearm xxx.xxx.xxx.xxx   # 此处输入需测试IP
```

## 回程测试 [Nanqinlang大佬作品]

* 支持选择节点测试，四网快速测试，手动输入IP测试三种模式

**复制

```
wget https://raw.githubusercontent.com/nanqinlang-script/testrace/master/testrace.sh && bash testrace.sh
```

### ![](https://cnboy.org/wp-content/uploads/6512bd43d9caa6e-1.jpg)

**（**\* ***部分截图*）**

## UnixBench.sh [秋水逸冰大佬作品]

* UnixBench是一个类unix系（Unix，BSD，Linux）统下的性能测试工具，一个开源工具，被广泛用与测试Linux系统主机的性能。Unixbench的主要测试项目有：系统调用、读写、进程、图形化测试、2D、3D、管道、运算、C库等系统基准性能提供测试数据。

**复制

```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/unixbench.sh && chmod +x unixbench.sh && ./unixbench.sh
```

### ![](https://cnboy.org/wp-content/uploads/c20ad4d76fe9775-1.jpg)

## LemonBench.sh

* LemonBench工具(别名LBench、柠檬Bench)，是一款针对Linux服务器设计的服务器性能测试工具。通过综合测试，可以快速评估服务器的综合性能，为使用者提供服务器硬件配置信息。目前涵盖的测试有：服务器基础信息 (CPU信息/内存信息/Swap信息/磁盘空间信息/网络信息等)，流媒体解锁测试 (目前支持HBO Now/动画疯/B站港澳台/B站台湾限定)，系统性能测试 (CPU/内存/磁盘)，Speedtest网速测试 (本地到最近源及国内各地域不同线路的网速)，路由追踪测试 (追踪到国内和海外不同线路的路由信息)。

**复制

```
快速测试：
curl -fsL https://ilemonra.in/LemonBenchIntl | bash -s fast

完整测试：
curl -fsL https://ilemonra.in/LemonBenchIntl | bash -s full
```

## Yabs.sh [Masonr大佬作品]

* 又一个 Linux VPS 一键测评脚本，可以一键测试 VPS 硬盘的读写速度、网络带宽也就是下载速度、CPU 跑分（包括 Geekbench 4 和 Geekbench 5），以及各种性能测试等。

**复制

```
wget -qO- yabs.sh | bash
或
curl -sL yabs.sh | bash
```

## 流媒体解锁测试 [Lmc999大佬作品]

* 本脚本基于CoiaPrant/MediaUnlock\_Test代码进行修改，支持OS/Platform：CentOS 6+, Ubuntu 14.04+, Debian 8+, MacOS, Android with Termux。
* Github项目地址：<https://github.com/lmc999/RegionRestrictionCheck>

**复制

```
bash <(curl -L -s check.unlock.media)

尾部添加参数的释义：
-M 4      只检测IPv4结果
-M 6      只检测IPv6结果
-I eth0    指定检测的网卡名称（例：eth0）
-E        选择脚本语言为英文
```

![](https://cnboy.org/wp-content/uploads/155e331eb64216b.jpg)

## 流媒体解锁测试 [LovelyHaochi大佬作品]

* 支持多个流媒体的ipv4与ipv6解锁情况

**复制

```
bash <(curl -sSL "https://git.io/JswGm")
```

### ![](https://cnboy.org/wp-content/uploads/aab3238922bcc25-4.png)

## 推荐杜甫使用-本脚本支持查看I/O bench以及system info

* 支持查看硬件信息，硬盘通电时间，io等脚本，适合独立服务器使用，vps也能用。
* Github项目地址：<https://github.com/Aniverse/A>

**复制

```
wget -q https://github.com/Aniverse/A/raw/i/a && bash a
```

### ![](https://cnboy.org/wp-content/uploads/9bf31c7ff062936-1.jpg)

## 测试25端口是否开放

**复制

```
telnet smtp.aol.com 25
```

如果看到类似下面的回显，则说明端口是开放的：

`Trying 74.6.141.50…`

`Connected to smtp.aol.g03.yahoodns.net.`

`Escape character is ‘^]’.`

`220 smtp.mail.yahoo.com ESMTP ready`

如果显示 `Connection timed out` ，说明25端口不开放。需要注意的是：部分服务商或是系统，需要在控制后台开放25端口，或需要开放系统防火墙端口。

文章来源: https://blog.upx8.com/3253
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)