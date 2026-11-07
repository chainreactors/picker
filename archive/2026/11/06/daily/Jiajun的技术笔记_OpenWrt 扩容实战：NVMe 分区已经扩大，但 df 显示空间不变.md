---
title: OpenWrt 扩容实战：NVMe 分区已经扩大，但 df 显示空间不变
url: https://jiajunhuang.com/articles/2026_11_06-upgrade_openwrt.md.html
source: Jiajun的技术笔记
date: 2026-11-06
fetch_date: 2026-11-07T07:59:26.676207
---

# OpenWrt 扩容实战：NVMe 分区已经扩大，但 df 显示空间不变

[跳到正文](#main-content)

[J.Jiajun的技术笔记](/)

[归档](/archive)
[分享](/sharing)
[随想](/notes)
[友链](/friends)

工具

[面试题库](https://tiku.jiajunhuang.com)
[幻灯片](https://jiajunhuang.com/page/index.md)

[关于](/aboutme)
[EN ↗](https://blog.jiajunhuang.com)

文章目录

* [OpenWrt 扩容实战：NVMe 分区已经扩大，但 df 显示空间不变](#OpenWrt%2b%25E6%2589%25A9%25E5%25AE%25B9%25E5%25AE%259E%25E6%2588%2598%25EF%25BC%259ANVMe%2b%25E5%2588%2586%25E5%258C%25BA%25E5%25B7%25B2%25E7%25BB%258F%25E6%2589%25A9%25E5%25A4%25A7%25EF%25BC%258C%25E4%25BD%2586%2bdf%2b%25E6%2598%25BE%25E7%25A4%25BA%25E7%25A9%25BA%25E9%2597%25B4%25E4%25B8%258D%25E5%258F%2598)
* [一、问题背景](#%25E4%25B8%2580%25E3%2580%2581%25E9%2597%25AE%25E9%25A2%2598%25E8%2583%258C%25E6%2599%25AF)
* [二、确认分区已经扩容](#%25E4%25BA%258C%25E3%2580%2581%25E7%25A1%25AE%25E8%25AE%25A4%25E5%2588%2586%25E5%258C%25BA%25E5%25B7%25B2%25E7%25BB%258F%25E6%2589%25A9%25E5%25AE%25B9)
* [三、确认 OpenWrt 根文件系统](#%25E4%25B8%2589%25E3%2580%2581%25E7%25A1%25AE%25E8%25AE%25A4%2bOpenWrt%2b%25E6%25A0%25B9%25E6%2596%2587%25E4%25BB%25B6%25E7%25B3%25BB%25E7%25BB%259F)
* [四、第一次尝试 resize2fs，失败](#%25E5%259B%259B%25E3%2580%2581%25E7%25AC%25AC%25E4%25B8%2580%25E6%25AC%25A1%25E5%25B0%259D%25E8%25AF%2595%2bresize2fs%25EF%25BC%258C%25E5%25A4%25B1%25E8%25B4%25A5)
* [五、通过 dmesg 找到真正原因](#%25E4%25BA%2594%25E3%2580%2581%25E9%2580%259A%25E8%25BF%2587%2bdmesg%2b%25E6%2589%25BE%25E5%2588%25B0%25E7%259C%259F%25E6%25AD%25A3%25E5%258E%259F%25E5%259B%25A0)
* [六、解决方案：移除 resize\_inode 特性](#%25E5%2585%25AD%25E3%2580%2581%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588%25EF%25BC%259A%25E7%25A7%25BB%25E9%2599%25A4%2bresize_inode%2b%25E7%2589%25B9%25E6%2580%25A7)
* [1. 解决工具缺失问题](#1.%2b%25E8%25A7%25A3%25E5%2586%25B3%25E5%25B7%25A5%25E5%2585%25B7%25E7%25BC%25BA%25E5%25A4%25B1%25E9%2597%25AE%25E9%25A2%2598)
* [2. 移除 resize\_inode](#2.%2b%25E7%25A7%25BB%25E9%2599%25A4%2bresize_inode)
* [3. 执行文件系统检查并重启](#3.%2b%25E6%2589%25A7%25E8%25A1%258C%25E6%2596%2587%25E4%25BB%25B6%25E7%25B3%25BB%25E7%25BB%259F%25E6%25A3%2580%25E6%259F%25A5%25E5%25B9%25B6%25E9%2587%258D%25E5%2590%25AF)
* [4. 再次执行 resize2fs](#4.%2b%25E5%2586%258D%25E6%25AC%25A1%25E6%2589%25A7%25E8%25A1%258C%2bresize2fs)
* [七、几个值得记住的知识点](#%25E4%25B8%2583%25E3%2580%2581%25E5%2587%25A0%25E4%25B8%25AA%25E5%2580%25BC%25E5%25BE%2597%25E8%25AE%25B0%25E4%25BD%258F%25E7%259A%2584%25E7%259F%25A5%25E8%25AF%2586%25E7%2582%25B9)
* [1. 分区扩容不等于文件系统扩容](#1.%2b%25E5%2588%2586%25E5%258C%25BA%25E6%2589%25A9%25E5%25AE%25B9%25E4%25B8%258D%25E7%25AD%2589%25E4%25BA%258E%25E6%2596%2587%25E4%25BB%25B6%25E7%25B3%25BB%25E7%25BB%259F%25E6%2589%25A9%25E5%25AE%25B9)
* [2. df 和分区表查看的是不同东西](#2.%2bdf%2b%25E5%2592%258C%25E5%2588%2586%25E5%258C%25BA%25E8%25A1%25A8%25E6%259F%25A5%25E7%259C%258B%25E7%259A%2584%25E6%2598%25AF%25E4%25B8%258D%25E5%2590%258C%25E4%25B8%259C%25E8%25A5%25BF)
* [3. OpenWrt 的根目录不一定是 SquashFS](#3.%2bOpenWrt%2b%25E7%259A%2584%25E6%25A0%25B9%25E7%259B%25AE%25E5%25BD%2595%25E4%25B8%258D%25E4%25B8%2580%25E5%25AE%259A%25E6%2598%25AF%2bSquashFS)
* [4. 根分区满载时，可以利用 /tmp](#4.%2b%25E6%25A0%25B9%25E5%2588%2586%25E5%258C%25BA%25E6%25BB%25A1%25E8%25BD%25BD%25E6%2597%25B6%25EF%25BC%258C%25E5%258F%25AF%25E4%25BB%25A5%25E5%2588%25A9%25E7%2594%25A8%2b%252Ftmp)
* [5. DNS有问题时，可以命令重置一下nameserver](#5.%2bDNS%25E6%259C%2589%25E9%2597%25AE%25E9%25A2%2598%25E6%2597%25B6%25EF%25BC%258C%25E5%258F%25AF%25E4%25BB%25A5%25E5%2591%25BD%25E4%25BB%25A4%25E9%2587%258D%25E7%25BD%25AE%25E4%25B8%2580%25E4%25B8%258Bnameserver)
* [八、总结](#%25E5%2585%25AB%25E3%2580%2581%25E6%2580%25BB%25E7%25BB%2593)

# OpenWrt 扩容实战：NVMe 分区已经扩大，但 df 显示空间不变

## 一、问题背景

最近升级 OpenWrt 后，发现系统根目录空间不足，只有约 122MB，已经接近 100% 使用率。

我的设备使用 SSD，磁盘容量约 14.4GB。原本以为升级后只需要扩展分区即可，于是执行了：

```
parted -f -s /dev/nvme0n1 resizepart 2 100%
```

命令执行成功，但查看磁盘空间：

```
df -h
```

结果依然是：

```
Filesystem                Size      Used Available Use% Mounted on
/dev/root               122.3M    119.8M     12.0K 100% /
```

明明 NVMe 有十几 GB，为什么 OpenWrt 仍然只有 122MB？

问题实际上出在：**分区已经扩容，但分区内部的 ext4 文件系统没有扩容。**

## 二、确认分区已经扩容

首先查看 GPT 分区表：

```
parted /dev/nvme0n1 print
```

输出：

```
Model: INTEL xxx (nvme)
Disk /dev/nvme0n1: 14.4GB
Partition Table: gpt

Number  Start   End     Size    File system
128     17.4kB  262kB   245kB
1       262kB   17.0MB  16.8MB  fat16
2       17.0MB  14.4GB  14.4GB  ext4
```

可以看到：

* p1：16.8MB，启动分区。
* p2：14.4GB，ext4 根文件系统所在分区。

再查看内核识别的分区：

```
cat /proc/partitions
```

输出：

```
major minor  #blocks  name

259        0   14065664 nvme0n1
259        1      16384 nvme0n1p1
259        2   14049007 nvme0n1p2
259        3        239 nvme0n1p128
```

由此确认，分区本身已经成功扩展。

## 三、确认 OpenWrt 根文件系统

接下来检查挂载信息：

```
cat /proc/mounts | grep -E ' / |nvme'
```

输出：

```
/dev/root / ext4 rw,noatime 0 0
/dev/nvme0n1p1 /boot vfat rw,noatime,...
```

再检查内核启动参数：

```
cat /proc/cmdline
```

输出：

```
BOOT_IMAGE=/boot/vmlinuz root=PARTUUID=xxx rootwait console=tty1 console=ttyS0,115200n8 noinitrd
```

进一步通过 mountinfo 确认根设备：

```
awk '$5=="/"{print $3}' /proc/self/mountinfo
```

输出：

```
259:2
```

对应 `/dev/nvme0n1p2`。

因此可以确认：

**OpenWrt 的根目录直接挂载在 NVMe 第 2 分区上，文件系统类型为 ext4。**

## 四、第一次尝试 resize2fs，失败

既然分区已经扩容，接下来自然想到使用 ext4 的扩容工具：

```
resize2fs /dev/nvme0n1p2
```

但执行后出现：

```
resize2fs 1.47.3 (8-Jul-2025)
Filesystem at /dev/nvme0n1p2 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 1
Performing an on-line resize of /dev/nvme0n1p2 to 3512251 (4k) blocks.
resize2fs: Invalid argument While trying to add group #1
```

扩容失败。

这里有一个重要信息：

```
While trying to add group #1
```

这说明 resize2fs 已经识别到目标分区的容量，但在新增 ext4 block group 时发生错误。

## 五、通过 dmesg 找到真正原因

为了进一步定位问题，检查内核日志：

```
dmesg | grep -iE 'ext4|resize|nvme' | tail -60
```

关键日志：

```
EXT4-fs (nvme0n1p2): resizing filesystem from 32768 to 3512251 blocks

EXT4-fs warning (device nvme0n1p2):
reserve_backup_gdb:1054: reserved block 8 not at offset 7

EXT4-fs warning (device nvme0n1p2):
ext4_resize_fs:2188: error (-22) occurred during file system resize

EXT4-fs (nvme0n1p2): resized filesystem to 32768
```

其中：

```
reserved block 8 not at offset 7
```

是最关键的错误信息。

`-22` 对应 Linux 的 `EINVAL`，即 Invalid argument。

这次问题与 ext4 的 `resize_inode` 特性以及保留备份组描述符（Reserved GDT blocks）的布局有关。

原来的文件系统只有：

```
32768 blocks × 4096 bytes = 128 MiB
```

而现在目标容量为：

```
3512251 blocks × 4096 bytes ≈ 13.4 GiB
```

扩容时，ext4 内核代码在处理保留的 GDT 元数据时出现不兼容，导致在线扩容失败。

## 六、解决方案：移除 resize\_inode 特性

这里参考了 OpenWrt 社区中相同错误的解决方案。

核心思路是移除 ext4 的 `resize_inode` 特性，避免在线扩容时遇到原有保留 GDT 布局问题。

### 1. 解决工具缺失问题

首先检查工具：

```
which tune2fs
which e2fsck
which resize2fs
```

最初系统中只有：

```
/usr/sbin/e2fsck
/usr/sbin/resize2fs
```

没有 `tune2fs`。

由于根分区已经 100% 满载，直接执行 `apk update` 也无法正常完成。

后来先腾出了一些根分区空间，再安装了 `tune2fs`。

这里还有一个值得注意的地方：OpenWrt 的 `/tmp` 是 tmpfs，可以利用内存空间存放临时文件。

```
df -h /tmp
```

我的设备显示：

```
Filesystem  Size  Used Available Use%
tmpfs       1.8G  308K  1.8G       0%
```

### 2. 移除 resize\_inode

执行：

```
tune2fs -O^resize_inode /dev/nvme0n1p2
```

命令没有输出错误信息，操作完成。

### 3. 执行文件系统检查并重启

本次采用的修复流程是先将根目录重新挂载为只读，再执行文件系统检查：

```
mount -o remount,ro /
e2fsck -f -y /dev/nvme0n1p2
```

检查完成后：

```
sync
reboot
```

需要注意，这种方式并不等同于从 Live USB 启动后完全卸载文件系统再检查。对于生产设备，更推荐真正的离线检查，并提前做好完整备份。

### 4. 再次执行 resize2fs

重启后重新 SSH 登录，执行：

```
resize2fs /dev/nvme0n1p2
```

这一次成功完成了扩容！

检查：

```
df -h /
```

根目录终于不再是原来的 122MB，而是扩展到了接近整个 NVMe 分区的容量。

## 七、几个值得记住的知识点

### 1. 分区扩容不等于文件系统扩容

Linux 磁盘扩容通常涉及两个独立操作：

| 操作 | 工具 | 作用 |
| --- | --- | --- |
| 扩大分区 | parted | 修改 GPT 分区边界 |
| 扩大文件系统 | resize2fs | 扩大 ext4 可使用的空间 |

只执行 `parted resizepart`，不会自动改变 ext4 文件系统的容量。

### 2. df 和分区表查看的是不同东西

```
parted /dev/nvme0n1 print
```

查看的是分区容量。

```
df -h
```

查看的是文件系统容量。

两者显示不同并不意味着磁盘故障。

### 3. OpenWrt 的根目录不一定是 SquashFS

OpenWrt 常见的文件系统布局包括 SquashFS + OverlayFS，但也有直接使用 ext4 根文件系统的安装方式。

因此排查时不要想当然，先检查：

```
cat /proc/mounts
cat /proc/cmdline
```

### 4. 根分区满载时，可以利用 /tmp

OpenWrt 的 `/tmp` 通常挂载在 tmpfs 上，使用内存作为临时存储。

在根分区空间不足时，可以将临时下载文件、备份文件放在 `/tmp`，但要注意它不是持久化存储，重启后内容会消失。

### 5. DNS有问题时，可以命令重置一下nameserver

由于我是恢复配置然后把磁盘用满了，结果恢复到一半退出了，导致DNS配置有问题，所以重置了...