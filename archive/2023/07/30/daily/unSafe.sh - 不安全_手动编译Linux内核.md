---
title: 手动编译Linux内核
url: https://buaq.net/go-173206.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:50:56.522433
---

# 手动编译Linux内核

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

![]()

手动编译Linux内核

前言：Linux内核是操作系统的核心，也是操作系统最基本的部分。操作系统是一个用来和硬件打交道并为用户程序提供一个有限服务集的低级支撑软件。一个计算机系
*2023-7-29 23:3:14
Author: [blog.upx8.com(查看原文)](/jump-173206.htm)
阅读量:41
收藏*

---

#### 前言：

Linux内核是操作系统的核心，也是操作系统最基本的部分。

操作系统是一个用来和硬件打交道并为用户程序提供一个有限服务集的低级支撑软件。一个计算机系统是一个硬件和软件的共生体，它们互相依赖，不可分割。计算机的硬件，含有外围设备、处理器、内存、硬盘和其他的电子设备组成计算机的发动机。但是没有软件来操作和控制它，自身是不能工作的。完成这个控制工作的软件就称为操作系统，在Linux的术语中被称为“内核”，也可以称为“核心”。Linux内核的主要模块（或组件）分以下几个部分：存储管理、CPU和进程管理、文件系统、设备管理和驱动、网络通信，以及系统的初始化（引导）、系统调用等。

#### 准备工具

Linux操作系统 Debian 11

[Linux内核源代码](https://www.kernel.org/)

#### 1.配置需要安装的环境

`nano /etc/apt/sources.list`

**添加软件源:**

> deb http://mirrors.163.com/debian/ stretch main
>
> deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib
>
> deb-src http://mirrors.163.com/debian/ stretch-updates main non-free contrib
>
> deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib

**更新软件列表:**

*`apt-get update`*

**更新软件:**

*`apt-get upgrade`*

**配置内核编译环境:**

`apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison libncurses5-dev gcc`

#### 2.编译内核

**下载并解压内核**

内核下载官网：https://www.kernel.org/

**配置内核**

复制原配置文件并重命名文件

*`cp -v /boot/config-5.10.0-10-amd64 /root/Kernel/.config`* (*`/root/Kernel/`* 为内核源代码所在目录)

**定制内核，启用或者禁用你需要或者不需要的模块**

*`make menuconfig`*

**编译内核和模块**

`make -j 8 deb-pkg`

make -j 选项表示并行编译。

make -j8，让make最多允许8个编译命令同时执行，这样可以更有效的利用CPU资源。

在多核CPU上，适当的进行并行编译可以明显提高编译速度。但并行的任务不宜太多，一般是以CPU核心数目的两倍为宜。

#### 3.编译完成

编译需要花费很长的时间，编译完成，会在源文件外生成四个deb包

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-05_21-26-09.png)

**执行命令升级内核**

*`dpkg -i *.deb`*

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-05_21-30-54.png)

**更新 grub**

`update-grub`

**重启系统，查看内核版本**

`uname -a`

![](https://loukas.cn/wp-content/uploads/2022/02/image_2022-02-05_21-34-34.png)

#### 解决编译过程中遇到的问题

**问题一:**

BTF: .tmp\_vmlinux.btf: pahole (pahole) is not available
Failed to generate BTF for vmlinux
Try to disable CONFIG\_DEBUG\_INFO\_BTF

**解决办法:**

修改配置文件

`CONFIG_DEBUG_INFO_BTF=y`

改成

`CONFIG_DEBUG_INFO_BTF=n`

文章来源: https://blog.upx8.com/3723
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)