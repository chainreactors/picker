---
title: eBPF on Android之编译内核与打补丁（解决触摸和WIFI失效问题）
url: https://buaq.net/go-134742.html
source: unSafe.sh - 不安全
date: 2022-11-09
fetch_date: 2025-10-03T22:04:25.814090
---

# eBPF on Android之编译内核与打补丁（解决触摸和WIFI失效问题）

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

![](https://8aqnet.cdn.bcebos.com/5bf5c7d1d6d2e29acc4d3c7136b4e19c.jpg)

eBPF on Android之编译内核与打补丁（解决触摸和WIFI失效问题）

本文为看雪论坛优秀文章看雪论坛作者ID：seeeseee一前言在之前的这篇文章中尝试了ptach内核，但是尝试开启CONFIG\_KRETPROBES后出现了触摸和WIFI失效的情况。eBPF on A
*2022-11-8 17:59:15
Author: [mp.weixin.qq.com(查看原文)](/jump-134742.htm)
阅读量:16
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FVxohib5yALmewhGYeLiaHcPlhndfzE5C2rjzLC5UKtWPlVnFFiaugaCicquBZvMxjvZzuqH3d4garUg/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：seeeseee

```
一

前言
```

在之前的这篇文章中尝试了ptach内核，但是尝试开启CONFIG\_KRETPROBES后出现了触摸和WIFI失效的情况。

* eBPF on Android之打补丁和编译内核

（*https://blog.seeflower.dev/archives/139*）

后来和missking交流之后，发现文章中修改内核编译选项的操作是不标准的，具体可以参考下面的文章：

* 修改Linux Kernel defconfig的标准方法

（*https://adtxl.com/index.php/archives/124.html*）

简单来说正确的步骤如下：

cd private/msm-google

进入内核源码目录。

make ARCH=arm64 floral\_defconfig

生成floral\_defconfig对应的.config配置文件；

这一步是基于arch/arm64/configs/floral\_defconfig配置文件进行的生成。

make ARCH=arm64 menuconfig

打开内核编译配置的可视化界面。

make ARCH=arm64 savedefconfig

根据.config配置文件生成defconfig配置文件。

cp defconfig arch/arm64/configs/floral\_defconfig

覆盖原有的floral\_defconfig配置文件。

这里当然可以用mv命令。

rm .config

删除.config配置文件，不然编译时会提示你需要清理。

然而即使这样我编译出来的内核还是会导致触摸和WIFI失效，后来在参考了下面的几个帖子之后，把触摸修好了，但是WIFI始终没有修好。

刷自编译内核导致屏幕触控失灵的问题 Google pixel 4XL

*https://www.akr-developers.com/d/440*

Pixel3 Aosp自编译内核如何正确的驱动设备正常运行

*https://www.akr-developers.com/d/526*

求助:刷入内核后触摸屏失灵

*https://www.akr-developers.com/d/469*

实操篇- pixel 2 刷8.0.0/8.1.0 AOSP +4.4 Kernel (重点解决刷完触屏失灵问题)

*https://bbs.pediy.com/thread-264295.htm*

编译内核(Pixel 2)

*https://bbs.pediy.com/thread-255846.htm*

android内核编译问题，多谢

*https://bbs.pediy.com/thread-273148.htm*

修好触摸主要参考第一个帖子第四楼

*https://www.akr-developers.com/d/440/4*

先在.repo/manifests/default.xml里面进行配置fts\_touch这些。

但是发现这些驱动代码目录不对，然后用git submodule命令去把代码同步过去、或者手动复制。

在一系列操作之后，终于触摸能用了，后面接着看了下怎么修WIFI，但是涉及的内容实在是太多了，就暂时搁置没有再研究了。

也正是这一番操作，我注意到build/build.sh还有个设定是BUILD\_BOOT\_IMG，也就是单独编译内核的时候，是可以构建出boot.img的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6FYp1WszWS8OEpACwkvkicsMwBBhHh7kIEVVZ2hkjuqXJ0micgzBl8zJQ/640?wx_fmt=png)

网上没有找到关于BUILD\_BOOT\_IMG这个选项的用法，虽然脚本中有说明，但是当时已经是筋疲力尽，对于里面提到的GKI\_RAMDISK\_PREBUILT\_BINARY和VENDOR\_RAMDISK\_BINARY更是一头雾水。

最近假期又有点时间了，于是认真看了脚本说明和逻辑，结合boot.img解包的信息，终于搞清楚单独编译内核且触摸和WIFI都正常的正确姿势了。

**操作其实很简单，不需要大改特改。**

本文将就正确单独编译安卓内核和给内核打bpf\_probe\_read\_user补丁进行详细指南。

博客中以下两篇文章步骤或多或少存在问题，请勿参考，以本文为准。

eBPF on Android之打补丁和编译内核（*https://blog.seeflower.dev/archives/139/*）

android-msm-crosshatch-4.9-pie-qpr2内核编译记录（*https://blog.seeflower.dev/archives/17/*）

```
二

环境
```

仅供参考

* Pixel 4XL
* coral-tp1a.220905.004 最新版系统，Android 13
* Linux localhost 4.14.276-ge333cb8619d0-ab8811257 #1 SMP PREEMPT Fri Jul 8 12:00:53 UTC 2022 aarch64 Toybox
* Ubuntu 20.04

```
三

步骤
```

该使用代理连接的时候请自行加代理。

## **准备环境和同步代码**

## *https://source.android.com/setup/build/initializing*

首先根据官方指南安装必要库和软件。

```
sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig
```

创建一个工作目录，后面的文件都会放这下面。

```
mkdir ~/Desktop/p4xlexport WORK_DIR=~/Desktop/p4xlcd ${WORK_DIR}
```

*https://source.android.com/setup/build/building-kernels*

根据官方的说明，我这里选择Pixel 4XL对应的分支android-msm-coral-4.14-android13。

为了能对应上手机的内核版本，这里没有加上--depth=1，后面需要checkout。

```
repo init -u https://android.googlesource.com/kernel/manifest -b android-msm-coral-4.14-android13repo sync
```

repo不会设置？请参考：

*https://lug.ustc.edu.cn/wiki/mirrors/help/aosp/*

最新版的内核编译脚本会使用自带的编译工具，不需要自己设置clang环境变量。

如果你同步的内核源代码没有编译工具，需要自己手动同步一下，如下：

```
cd prebuiltsgit clone https://android.googlesource.com/kernel/prebuilts/build-toolsmv build-tools kernel-build-toolsexport PATH=${WORK_DIR}/prebuilts/kernel-build-tools/linux-x86/bin:$PATH
```

代码同步好之后，进入private/msm-google文件夹，通过下面的命令切换到和手机内核版本一致的commit。

我的内核版本是4.14.276-ge333cb8619d0-ab8811257，那么对应的commit id就是e333cb8619d0。

```
git checkout e333cb8619d0
```

## **修改编译脚本和准备文件**

### 脚本分析

如果对这个部分不感兴趣，请直接查看脚本修改小节。

首先将手机当前的boot.img用Android-Image-Kitchen解包，会得到一堆文件，终端会给出这些信息：

```
ANDROID! magic found at: 0BOARD_KERNEL_CMDLINE console=ttyMSM0,115200n8 androidboot.console=ttyMSM0 printk.devkmsg=on msm_rtb.filter=0x237 ehci-hcd.park=3 service_locator.enable=1 androidboot.memcg=1 cgroup.memory=nokmem usbcore.autosuspend=7 androidboot.usbcontroller=a600000.dwc3 swiotlb=2048 androidboot.boot_devices=soc/1d84000.ufshc loop.max_part=7 buildvariant=userBOARD_KERNEL_BASE 0x00000000BOARD_NAMEBOARD_PAGE_SIZE 4096BOARD_HASH_TYPE sha1BOARD_KERNEL_OFFSET 0x00008000BOARD_RAMDISK_OFFSET 0x01000000BOARD_SECOND_OFFSET 0x00000000BOARD_TAGS_OFFSET 0x00000100BOARD_OS_VERSION 13.0.0BOARD_OS_PATCH_LEVEL 2022-09BOARD_HEADER_VERSION 2BOARD_HEADER_SIZE 1660BOARD_DTB_SIZE 1048284BOARD_DTB_OFFSET 0x01f00000
```

在build/build.sh中查找BUILD\_BOOT\_IMG，在脚本末尾的代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6DxyIDB935CTOorIUNfCWmy0mMWutAG9NNPBwlxGqmq0AibaHic1zYvYQ/640?wx_fmt=png)

对代码阅读后可知：当BOOT\_IMAGE\_HEADER\_VERSION为3的时候才会检查GKI\_RAMDISK\_PREBUILT\_BINARY和KERNEL\_VENDOR\_CMDLINE。

但是解包的结果中可以看到BOARD\_HEADER\_VERSION是2。

脚本的帮助信息中说，如果BOOT\_IMAGE\_HEADER\_VERSION值小于3，那么还需要指定BASE\_ADDRESS和PAGE\_SIZE。

这两个选项的值其实就是解包信息中的BOARD\_KERNEL\_BASE和BOARD\_PAGE\_SIZE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6MlaIB5ic0lzyXjTWzKjg06tAC9JlhOk9r0icrLh464rOP6WnEqBaqEdg/640?wx_fmt=png)

解包信息中的BOARD\_KERNEL\_CMDLINE则就是KERNEL\_CMDLINE。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6NCEsyGGGquiaUNu7JcPePpuBeMRDbHoA3ohermlhgCKia8NZb3hicODZA/640?wx_fmt=png)

KERNEL\_BINARY的值直接说了是Image.lz4或者Image.gz，我们知道编译产物中有Image.lz4，所以指定为Image.lz4。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6icSkmeseIqfApfjpVKTiaKWiaP0BCZP8O4NKbcW3shAa3RlJvnSkjtkzA/640?wx_fmt=png)

MKBOOTIMG\_PATH默认是tools/mkbootimg/mkbootimg.py，但是我发现同步下来的代码并没有这个脚本，这个我们去AOSP之类的代码中找一个就行了，比如：

*http://aospxref.com/android-11.0.0\_r21/xref/system/tools/mkbootimg/mkbootimg.py*

或者直接同步下官方的代码。

```
git clone https://android.googlesource.com/platform/system/tools/mkbootimg
```

我这里直接把脚本放在了${WORK\_DIR}，也就是整个代码的根目录下面。

那么问题来了，VENDOR\_RAMDISK\_BINARY应该是什么呢，哪里找，脚本里面的说明如下：

```
Name of the vendor ramdisk binary which includes the device-specific components of ramdisk like the fstab file and the device-specific rc files.
```

最开始我也是迷糊的，boot.img解包出来的文件有一个是boot.img-ramdisk.cpio.gz。

看build/build.sh的逻辑是要和initramfs.cpio甚至GKI\_RAMDISK\_PREBUILT\_BINARY一起打包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6tNiaaVZr8tc7OUXR5PVhX0Ql8rB4EcgpOReFPUcLqmLfU9c9sjI9leA/640?wx_fmt=png)

那么解包出来的boot.img-ramdisk.cpio.gz是需要更新内容吗，还是接着用呢？

在此之前的经验告诉我，肯定不是直接接着用解包出来的boot.img-ramdisk.cpio.gz。

注意到BUILD\_INITRAMFS的描述是if defined, build a ramdisk containing all .ko files and resulting depmod artifacts。

就是说会打包出一个ramdisk包含所有.ko也就是驱动模块文件。

虽然之前编译的时候没有定义这个，但是产物确实有initramfs.img。

发现原来是private/msm-google/build.config.common文件中设置了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6ZOqW2knpxIzSo8fic49FI0x1MFHvuH4sLvV7NLOpxj3ybh4K95pxQIg/640?wx_fmt=png)

而脚本中也确实是这样，可以看到中途会产生initramfs.cpio。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6mniaOr7WdodxkBtItcLbfXP9ic8uib46T3icMiaxrX0ibhVdIxuEzx7C4mNQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6U2KrlMokDbQbricSBH6uUADCjVAJQyVArKFdlqaXEQpjCcibS7YibOrvw/640?wx_fmt=png)

而initramfs.cpio正好是和VENDOR\_RAMDISK\_BINARY一起打包的，也就是说VENDOR\_RAMDISK\_BINARY应该是.cpio文件。

boot.img-ram...