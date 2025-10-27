---
title: PVE设置显卡直通 - 山中书
url: https://buaq.net/go-157022.html
source: unSafe.sh - 不安全
date: 2023-04-05
fetch_date: 2025-10-04T11:29:16.561413
---

# PVE设置显卡直通 - 山中书

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

![](https://8aqnet.cdn.bcebos.com/c7f21844eda09f90bdd91a96e5e0b1df.jpg)

PVE设置显卡直通 - 山中书

0x01 准备事项0x02 开启IOMMU功能编辑文件/etc/default/grub，修改GRUB\_CMDLINE\_LINUX\_DEFAULT字段值如果为Intel的CPU GR
*2023-4-4 23:12:55
Author: [www.wangsansan.com(查看原文)](/jump-157022.htm)
阅读量:29
收藏*

---

![xx.jpg](https://www.wangsansan.com/usr/uploads/2022/05/2284877373.jpg)

## 0x01 准备事项

## 0x02 开启IOMMU功能

编辑文件*/etc/default/grub*，修改`GRUB_CMDLINE_LINUX_DEFAULT`字段值

如果为Intel的CPU

```
  GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"
```

如果为AMD的CPU

```
  GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"
```

## 0x03 添加`VT-D`功能的内核模块

打开文件`/etc/modules`，新增以下4行内容

```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

## 0x04 屏蔽显卡驱动

```
# 屏蔽镭龙显卡驱动
echo "blacklist radeon" >> /etc/modprobe.d/pve-blacklist.conf

# 屏蔽英伟达显卡的开源nouveau驱动
echo "blacklist nouveau" >> /etc/modprobe.d/pve-blacklist.conf

# 屏蔽英伟达显卡驱动
echo "blacklist nvidia" >> /etc/modprobe.d/pve-blacklist.conf
```

## 0x05 其它参数

```
# 允许不安全的中断
echo "options vfio_iommu_type1 allow_unsafe_interrupts=1" > /etc/modprobe.d/iommu_unsafe_interrupts.conf

# 忽略异常，防止虚拟机异常导致宿主机崩溃
#   ignore_msrs             :   忽略异常
#   report_ignored_msrs     :   是否报告异常
echo "options kvm ignore_msrs=1 report_ignored_msrs=0" > /etc/modprobe.d/kvm.conf
```

## 0x06 配置VFIO

*ps：执行此操作后可能无法输出到外接显示器，若出现此情况，请撤回该步骤*

- **1、查看显卡ID**

```
  [email protected]:~# lspci -nn | grep VGA
  # 前缀02:00.0是设备编号，最后*.0为子编号
  # 末尾[10de:2489]是设备ID
  02:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:2489] (rev a1)
  08:00.0 VGA compatible controller [0300]: Matrox Electronics Systems Ltd. G200eR2 [102b:0534] (rev 01)
  [email protected]:~#
```

N卡编号为02:00，搜索对应的设备ID和音频设备ID

```
  [email protected]:~# lspci -n -s 02:00
  02:00.0 0300: 10de:2489 (rev a1)
  02:00.1 0403: 10de:228b (rev a1)
  [email protected]:~#
```

**或者直接以`NVIDIA`为关键词搜索相关的设备，其中一个是音频**

```
  [email protected]:~# lspci -nn | grep NVIDIA
  02:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:2489] (rev a1)
  02:00.1 Audio device [0403]: NVIDIA Corporation GA104 High Definition Audio Controller [10de:228b] (rev  a1)
  [email protected]:~#
```

**得到显卡的设备ID和显卡内置音频设备ID为：**

- `显卡ID`： *10de:2489*

- `音频ID`： *10de:228b*

- **2、将设备ID添加到`vfio.conf`**

```
  # 添加PCI设备
  echo "options vfio-pci ids=10de:2489,10de:228b disable_vga=1" > /etc/modprobe.d/vfio.conf
```

如果无法输出到外接显示器，取消`disable_vga=1`参数试试

```
  echo "options vfio-pci ids=10de:2489,10de:228b" > /etc/modprobe.d/vfio.conf
```

## 0x07 应用更改

- **1、刷新更改**

```
  update-grub
  update-initramfs -u -k all
```

- **2、重启PVE**

```
  reboot
```

- **3、检查是否配置成功**

```
  [email protected]:~# lspci -nnk
  02:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:2489] (rev a1)
          Subsystem: CardExpert Technology Device [10b0:153c]
          Kernel driver in use: vfio-pci
          Kernel modules: nvidiafb, nouveau
  02:00.1 Audio device [0403]: NVIDIA Corporation GA104 High Definition Audio Controller [10de:228b] (rev a1)
          Subsystem: CardExpert Technology Device [10b0:153c]
          Kernel driver in use: vfio-pci
          Kernel modules: snd_hda_intel
  [email protected]:~#
```

如果看到`Kernel driver in use: vfio-pci`，表示应用成功

## 0x09 添加显卡到虚拟机中

完成上述步骤配置后，在PVE-web图形化端添加PCI-E设备到虚拟机中即可

***ps:***

***1、我同时添加显卡和音频之后，开机遇报错：`TASK ERROR: start failed: QEMU exited with code 1`，如果遇到同样的报错，尝试把音频设备从硬件中移除***

***2、我本次安装的win11，好像`msdn i'tell u`下载的无法安装，建议下载官方镜像尝试，或者下载2021年8月份版本***

---

文章来源: https://www.wangsansan.com/archives/181/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)