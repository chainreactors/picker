---
title: 2023全新高研班！脱壳机更新、iOS/eBPF、云手机...
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458497424&idx=1&sn=85b2123fa34b3ee86fe663681a05052c&chksm=b18e811a86f9080c5b9ab6dd9df526b241ffc29b873f58509b13e7d13fff5e1dbafccc759edd&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-10
fetch_date: 2025-10-04T09:08:58.332075
---

# 2023全新高研班！脱壳机更新、iOS/eBPF、云手机...

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiaEggiacQPG17ZibiaKWPZMJia22uxm7HszYromtUuo4jLqe7mPBqrrlAFzg/0?wx_fmt=jpeg)

# 2023全新高研班！脱壳机更新、iOS/eBPF、云手机...

原创

看雪高研

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HVx2RyIYQqtvrXkM8AeJXlEty7JvU9zicugqqmiaohpp3f7HOo2liaJPEEZyxPQufIItyicWB6sSicpRQ/640?wx_fmt=jpeg)

重要通知！自2023年3月25日12点起，高研班课程价格将作以下调整：

1、月薪三万计划：由【8599元】![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UY7Nf5OMaoMibbudsY5N1Y4TXOicciakr5EZQmPmDNrdfPKc2p6brn5XyA/640?wx_fmt=png)

2、月薪两万计划：由【5599元】![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UY7Nf5OMaoMibbudsY5N1Y4TXOicciakr5EZQmPmDNrdfPKc2p6brn5XyA/640?wx_fmt=png)【5899元】

除此之外，课程内容及开学礼包也作出相应调整![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UibM134tIsO1j5yqHyNhh9arj090oAL7zGhRJRq6cFqFOlDZMleLl4pw/640?wx_fmt=png)

**1、课程内容新增**

2023年在原有基础上，新增以下课程内容![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6U13zvU1fN1qzCbZFougpOky81hlIm3X0kjWBHz7EGGbNic8n7A7H2bew/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aia6311x9HEBaNGkk2TicSlnkCg7FcwzMAzKkYPTZ5YbB6txgpW8ib6AL5Q/640?wx_fmt=jpeg)

* 更新内容采用直播的方式，周末直播，1v1激情连麦！
* 有问必答，知无不言，言无不尽，用心服务！
* 更有职业推介服务，全方位简历指导/服务就业！

**2、开学大礼包**

现在报名送开课礼包![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UibM134tIsO1j5yqHyNhh9arj090oAL7zGhRJRq6cFqFOlDZMleLl4pw/640?wx_fmt=png)

3W班高研网课开学大礼包：香橙派OrangePi 5开发板

2W班高研网课开学大礼包：测试手机一部-pixel 2代

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiayDuAunsnFFOp88pMsgsjOm6rcOa9W4aVCic7Lfsmo2W5NgU8ibRA9ibbw/640?wx_fmt=png)

## **讲师风采：《云手机底层技术揭密 : Android系统启动与Magisk原理》**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FdzZHia6HjsLgggicYmLanezY1QfFS7zT3qicJwC2TArfwpdia7029w9P1UqhzxibBKtibOMIPqK39BcxQ/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：飞翔的猫咪

Android系统启动是个相当复杂的过程,牵扯的技术点很多,如果想实现Android虚拟化云手机技术或者专注于刷机刷系统,理解启动的整个过程更是必需的。

Magisk和Android系统的启动更是息息相关,本文会在系统启动的角度描述一下Magisk的原理。

本文包含如下内容：
一. 磁盘分区表mbr,gpt的概念
二. ramdisk,initrd,ramfs,tmpfs,initramfs,rootfs,根文件系统名词的澄清
三. Linux内核启动init进程的五种不同情况
四. 安卓系统启动的三种不同方式
五. Magisk原理

#

```
一

## 磁盘分区表mbr,gpt
```

##

以下描述中磁盘、硬盘都是通用概念，代表着非易失的存储设备。

说到系统启动，和分区是息息相关的,对磁盘进行分区必然有分区表这样的一个结构，它存放在磁盘当中，分区表所面临的抽象仍然是将整个磁盘视为一个大的字节数组，只不过它通常以扇区为单元，扇区一般为512字节。

老式的磁盘分区方法叫MBR,新式的磁盘分区方法叫GPT。

**MBR：**

MBR的全称为Master Boot Record,它指的是指定开机指定启动硬盘的第一个扇区，通常为512字节，为什么说分区方法也叫MBR呢，因为这个扇区包括了两部分内容: bootstrap code area和partition table。

1. bootstrap code area占据446个字节，包含了启动相关的代码
2. partition table分区表占据了64个字节，包含了四个分区表的内容，每个分区表占据16个字节
3. 446+64 = 510,还剩下最后两个字节的内容为0x55aa,这是MBR的标志

   所以MBR这个名词不仅仅指磁盘的第一个扇区，它还暗指了上面的这种布局以及分区格式。

**读写磁盘逻辑地址：**

C/H/S (Cylinder / Head / Sector) 柱面/磁头/扇区是以前用于读写磁盘的基本逻辑地址结构，比如0/0/1(Cylinder=0,Head=0,Sector=1)就代表MBR。
MBR中的分区表格式就用到了C/H/S的表示方法。

C/H/S是一种老式的逻辑地址方式，它的存在有一定的历史原因，早期磁盘的结构就是柱面，磁头和扇区这些，后面磁盘的物理结构就不一定再是这些了，CHS也就不再对应于磁盘物理上的结构，对于CHS转换到实际磁盘的地址则是磁盘控制器的工作。

新式的逻辑地址表示方法为LBA:Logical Block Addressing,它的想法很简单，就是将磁盘视为一个大的字节数组，LBA从0开始: LBA0,LBA1,..... 每一块LBA的大小通常为512字节(也有以1024字节为块大小的固态硬盘，和4096字节为块大小的flash存储设备)。

**C/H/S到LBA有一个转换公式：**
A = (c ⋅ Nheads + h) ⋅ Nsectors + (s − 1)
A为LBA地址，Nheads为磁盘上的heads个数，Nsectors是每个track里边的最大扇区个数。

理解这个公式可以简单的认为磁盘是这样构成的：

1. 扇区是一块扇形区域，像一块切好的比萨
2. 多个扇区最终组成一个圆，好比组成一个完整的比萨，这块比萨可以分割成多少个扇区由Nsectors表示
3. 磁盘由多个完整的比萨组成(串在一起)，数量共为Nheads个

MBR每个分区表占据16个字节，比如:
80 01 01 00 0B FE BF FC 3F 00 00 00 7E 86 BB 00

含义如下:
80 --> 1字节，分区状态: 00 --> 非活动分区，80 --> 活动分区
01 01 00 --> 3字节, 共同表示分区起始C/H/S(但是并不指C=1,H=1,S=0)
0B --> 文件系统标志位 : "0B"表示分区的系统类型是FAT32，其他比较常用的有04（FAT16）、07（NTFS）

FE BF FC --> 共同表示分区结束C/H/S
3F 00 00 00 --> 分区起始相对扇区号
7E 86 BB 00 --> 分区总的扇区数

由于MBR格式的分区表只能识别四个分区(这些分区叫主分区)，如果想分四个以上的分区，必须创建一个分区，该分区用于存放更多的分区表，这样的分区叫做扩展分区，扩展分区只能有一个: 分区方式为4个主分区或者3个主分区加上一个扩展分区。

由于MBR使用4个字节表示分区总的扇区数,因此它可以表示的最大分区大小为2199023255552字节，约为2T，这也是MBR的一个限制。

由于各种限制，MBR已经成为老式的分区方式，新式的分区方式为GPT。

**GPT：**
GUID Partition Table

GPT采用LBA的地址格式，为了向后兼容以及用来防止不支持GPT的硬盘管理工具错误识别并破坏硬盘中的数据，LBA0仍然给MBR使用,不过MBR里边只有一块分区，分区类型为0xEE,这种MBR又叫"Protective MBR"。

GPT的格式维基百科中有详细描述，它还有一块区域用来备份分区表，在磁盘的末尾部分:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiaXfMqocrALdUIQQ8ic3y1YiamxrAW6aR12zyfa2X5z1uK9th1jVWs3jFA/640?wx_fmt=png)

按照GPT的格式，磁盘真正的分区数据部分从LBA34开始，但分区软件一般将GPT分区边界对齐，比如对齐到2048扇区处:1,048,576 MB，所以一般分区的数据从LBA2048开始，因此从LBA34到LBA2048有一块大约1MB的间隙。

**查看分区表内容：**

安装python的gpt包：
python3 -m pip install gpt

以pixel3Xl手机为例,因为pixel3xl用的是高通的scsi总线的ufs存储设备，所以它的设备名称以"sd"开头(内核drivers/scsi/sd.c的sd\_format\_disk\_name()函数),查看所有的sd设备：

```
ls -l /sys/block/sd*lrwxrwxrwx 1 root root 0 2023-01-11 03:56 /sys/block/sda -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:0/block/sdalrwxrwxrwx 1 root root 0 2023-01-11 10:36 /sys/block/sdb -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:1/block/sdblrwxrwxrwx 1 root root 0 2023-01-11 10:36 /sys/block/sdc -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:2/block/sdclrwxrwxrwx 1 root root 0 2023-01-11 10:36 /sys/block/sdd -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:3/block/sddlrwxrwxrwx 1 root root 0 2023-01-11 10:36 /sys/block/sde -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:4/block/sdelrwxrwxrwx 1 root root 0 2023-01-11 10:36 /sys/block/sdf -> ../devices/platform/soc/1d84000.ufshc/host0/target0:0:0/0:0:0:5/block/sdf
```

ufshc的含义为:ufs host controller,可以看到有6个sd设备,从a到f,并不代表着6个物理ufs设备,而是一块ufs物理设备分出来的逻辑设备,称之为LU(Logical Unit)。

它们的逻辑地址空间是独立的，都是从LBA 0开始，因此都有各自的分区表结构。

先来看一下sda的分区表信息，对应的/dev下面的块设备文件为/dev/block/sda，看一下sda设备的块逻辑大小(内核include/linux/blkdev.h文件的bdev\_logical\_block\_size()函数)：

```
cat /sys/block/sda/queue/logical_block_size4096
```

因此LBA的大小为4096字节。

安卓存储设备采用的是gpt分区，LBA0仍然给MBR使用，叫做"Protective MBR"，dump它的内容查看分区表：

在手机中运行命令:

```
dd if=/dev/block/sda bs=4096 count=1  > /data/local/tmp/lba0
```

在pc运行命令adb pull把/data/local/tmp/lba0文件拉取到pc。

在pc运行命令

```
cat lba0 | print_mbrWarning: Using only the first 512 bytes of input<<< MBR >>>BootCode: 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000UniqueMBRDiskSignature:                                         0x00000000Unknown:                                                            0x0000PartitionRecord: 0x00000200ee00000001000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Signature:                                                          0xAA55<<< MBR Partition #0 >>>#0.BootIndicator:                                                      0x0#0.Is Bootable? (syn):                                                  No#0.StartingCHS:                                                    0, 0, 2#0.OSType:                                                            0xEE#0.OSType (syn):                                            GPT Protective#0.EndingCHS:                                                      0, 0, 0#0.StartingLBA:                                                          1#0.SizeInLBA:                                                   4294967295<<< MBR Partition #1 >>>#1.BootIndicator:                                                      0x0#1.Is Bootable? (syn):                    ...