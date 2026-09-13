---
title: 拆开就能进 root：Oker 摄像头 UART 未认证调试口
url: https://mp.weixin.qq.com/s/Yu-qVXE4XqRRzjDzHyFSBQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:59:50.229797
---

# 拆开就能进 root：Oker 摄像头 UART 未认证调试口

# 拆开就能进 root：Oker 摄像头 UART 未认证调试口

赛博安全攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 拆开就能进 root：Oker 摄像头 UART 未认证调试口

![IoT Pentesting Basics cover](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VV0TIQx2oxUbdXzmD9xN91bf8ct1ppuAW7FRibnhbVjRLRMaZQI5ZwMxBeRg74k3FhwTd1Dcc5VwJ8O2wNEhRRCicmN0NJkfxdM/640?wx_fmt=jpeg&from=appmsg)

IoT Pentesting Basics：从 UART 拿到 root shell

做 IoT 渗透，第一步几乎总是拆机。拆开之后，不妨换个角度：当年开发人员调试时靠什么接口？这些接口会不会还留在量产板上，甚至还开着？

这篇按真实设备走一遍：怎么定位 UART，又怎么从它拿到 root shell。

## 目标设备

![Oker G955v1 IP Camera](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UONibWVSbMgkgx3oQUg4rLXYnyYDQML7qiabficFcKa42Q7JAvgxicGscBQxS0grOhqzyJZtKggan8BUibMq3SZAIjza0mUAOE1nvE/640?wx_fmt=jpeg&from=appmsg)

Oker G955v1 网络摄像头

目标是国产 Oker G955v1，带 Wi‑Fi 的 IP 摄像头。美国市场基本买不到；作者在东南亚期间入手。

## 拆机

![Device teardown of the Oker G955v1](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Xbqa1OqVn9XmGDIhqwXBicaFPYWQScNgiaias2ylhjo4Fb3JqAaCLiacicqNMT6icow74HSRVK1hWBibCRNBicYn1m9wa9azGzUzbomxs/640?wx_fmt=jpeg&from=appmsg)

拆开 Oker G955v1

硬件评估的第一步是碰到 PCB。这台拆起来很直接：

* 底部拧掉 4 颗螺丝
* 小心掰开塑料壳两半
* 找到穹顶内的主板
* 再拧掉固定 PCB 的 2 颗螺丝
* 取出主板分析

![Close-up of the main PCB](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VQgWXicAicRxMYK6DpbUSsD9ubhk2rbAcS7AbBiaCH13SuvMg5q3SJevwttXhh7Hh222l3GqDiaqicca5dWibov1ebyicpPLPx2Rrqec/640?wx_fmt=jpeg&from=appmsg)

主板近景

板上有几组未焊接的排针，对硬件黑客来说是好兆头：调试口往往就藏在这类位置。

## 找到 UART

![Labeled UART pins on the PCB](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WtRJSpQV9oicpdHV3ed7pp3pUggduaok0fTYTCmYf4SBloIY4bJLzw8heFQk5ywXZsNY0rPoO7G41qDwD7csCjtVy7qEfHmr4k/640?wx_fmt=jpeg&from=appmsg)

板上直接丝印了 UART 引脚

很多 IoT 设备要靠测点和反推才能确认 UART；这台省事多了——主板上未焊接的 4 针排针直接标了：

* 3v3（电源）
* TXD（发送）
* RXD（接收）
* GND（地）

接线用了：

* Tigard 多协议工具（硬件 hacking 接口）
* 3 根 PCBite 探针（临时搭在焊盘上）

Tigard 的 UART 接到摄像头对应脚：TXD↔RXD、RXD↔TXD、GND↔GND；3v3 不接，设备自己供电。

硬件连好后，用 picocom 开串口：

```
picocom -b 115200 /dev/ttyUSB0
```

115200 是嵌入式 Linux 最常见的默认波特率，所以先猜它。不行再试 9600、38400、57600。

## 看启动日志

串口开着上电，启动信息立刻刷出来。

U-Boot 识别和打断提示：

```
U-Boot 2013.01 (Jan 09 2015 - 14:10:09)

I2C:   ready
DRAM:  64 MiB
ROM CODE has enable I cache
SPI mode
SF: Got idcodes
00000000: ef 40 18 00    .@..
SF: Detected W25Q128 with page size 64 KiB, total 16 MiB
flash is 3byte mode
In:    serial
Out:   serial
Err:   serial
...
Hit any key to stop autoboot:  0
```

内核命令行：

```
Kernel command line: mem=128M gmmem=90M console=ttyS0,115200 user_debug=31 init=/squashfs_init root=/dev/mtdblock2 rootfstype=squashfs
```

分区布局：

```
SPI_FLASH spi0.0: w25q128bv (16384 Kbytes)
Creating 5 MTD partitions on "nor-flash":
0x000000010000-0x000000060000 : "UBOOT"
0x000000060000-0x000000300000 : "LINUX"
0x000000300000-0x000000f00000 : "FS"
0x000000f00000-0x000001000000 : "USER0"
0x000000000000-0x000001000000 : "ALL"
```

启动日志把固件架构摸了个大概：bootloader 版本、内核参数、文件系统布局。更有意思的是中途这行：

```
Press q -> ENTER to exit boot procedure?
```

这说明可以打断正常启动流程。

## 掉进 root

按提示敲 `q` 再回车，设备立刻停在启动过程里，直接给了 root shell：

```
   Press q -> ENTER to exit boot procedure? / #
/ #
/ # whoami
root
```

没密码，没认证，直接 root。

从这个 shell 可以：

* 读文件系统上所有文件
* 抽固件做分析
* 改系统配置
* 看进程
* 看网络配置

顺手发现硬编码的密码哈希：

```
/ # cat /etc/shadow
root:$6$Iw0BJ8Hu$CtZloGU0BVPpTmiwEZlDzPOvqVKuxTl.EbVjuOUGfAOmUz3kdyZ6J9ilw1FYPfZILvjS617iAJNdsOUontUBm.:16665:0:99999:7:::
bin:*:12963:0:99999:7:::
daemon:*:12963:0:99999:7:::
adm:*:12963:0:99999:7:::
lp:*:12963:0:99999:7:::
sync:*:12963:0:99999:7:::
shutdown:*:12963:0:99999:7:::
halt:*:12963:0:99999:7:::
uucp:*:12963:0:99999:7:::
operator:*:12963:0:99999:7:::
nobody:*:12963:0:99999:7:::
```

这台设备上 root 密码用户改不了：`/etc/shadow` 在 squashfs 里，只读。

## 小结

Oker G955v1 把 IoT 里很常见的一类问题摊开了：UART 调试口好找，而且没有任何认证挡着 root。拆机、接串口、看启动日志——很多量产设备还在把「开发期后门」原样留给攻击者。

更多 IoT / 车联网 / 机器人 / AI 安全资料在星球里，扫码进「车联网攻防日记」。

![知识星球二维码](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84X9tDwu4nAoic0uwWVjYNLbGKyo3KdVQVPL5fZiaLZCJHsNUxPj5OUTlK2tjMy440jriaibROplhWJJcGGnXJuXcx7c5oK3CwajYrA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CBQpMBV9zPvo3ZuxicpWjWwCiaXOPrDAu26fx15icAgD6cJbOG3ZDppXvp3MQeISu15QT18odicltialEibcNsxS0WfA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过