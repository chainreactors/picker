---
title: 马自达车载信息娱乐系统 （IVI） 中的多个漏洞
url: https://www.anquanke.com/post/id/301678
source: 安全客-有思想的安全新媒体
date: 2024-11-09
fetch_date: 2025-10-06T19:14:21.892571
---

# 马自达车载信息娱乐系统 （IVI） 中的多个漏洞

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

# 马自达车载信息娱乐系统 （IVI） 中的多个漏洞

阅读量**98611**

发布时间 : 2024-11-08 15:06:18

**x**

##### 译文声明

本文是翻译文章，文章原作者 Dmitry Janushkevich，文章来源：Zero Day Initiative

原文地址：<https://www.thezdi.com/blog/2024/11/7/multiple-vulnerabilities-in-the-mazda-in-vehicle-infotainment-ivi-system>

译文仅供参考，具体内容表达以及含义原文为准。

在多款车型（如 2014-2021 年款马自达 3）上安装的马自达 Connectivity Master Unit (CMU) 系统中发现了多个漏洞。与许多情况一样，这些漏洞是由于在处理攻击者提供的输入时未进行充分的消毒而造成的。实际存在的攻击者可以通过将特制的 USB 设备（如 iPod 或大容量存储设备）连接到目标系统来利用这些漏洞。成功利用其中一些漏洞可导致以 root 权限执行任意代码。

**目标**

作为研究目标的特定 CMU 装置由伟世通公司制造，而软件最初由江森自控公司 (JCI) 开发。研究针对最新可用软件版本（74.00.324A）进行。至少 70.x 以下的早期软件版本也可能受到这些漏洞的影响。

值得注意的是，CMU 的 “修改场景 ”非常活跃，社区发布了多种软件 “调整 ”来改变设备的运行。安装这些调整程序通常依赖于软件漏洞。截至发稿时，我们尚未发现最新固件版本中存在任何公开的已知漏洞。

**硬件设计**

设备外观如下：

![]()

底部有一张贴纸，上面有一些关于设备的技术信息。贴纸上注明 CMU 的具体型号为 MAZDA\_GEN\_65\_CMU。

![]()

设备背面有多个连接器，用于连接电源、音频输入/输出、USB 和 CAN 信号以及串行控制台。

![]()
在内部，该装置构建在一块印刷电路板上，其中包含一个应用 SoC（飞思卡尔零件编号 SCIMX06DAVT10AC）、各种存储器 IC（电路板背面的串行闪存、NAND 闪存和 eMMC）、一个辅助 MCU（瑞萨零件编号 R5F35MCEJFF）和一个蓝牙模块（村田零件编号 LBEE6Z2U0C-584）。

![]()

本研究未探讨边缘连接器的可用功能。

通常情况下，在存在多个处理单元的设计中，会实现一定程度的分离。由丰富的操作系统（如 QNX、Linux、Android 等）处理的面向用户的应用程序在应用 SoC 上运行，而 CAN 连接则由通常运行 RTOS 的 MCU 处理。该设备似乎也是这种情况。

**软件设计**

在软件方面，该设备的主 SoC 正在运行基于 Linux 的操作系统映像，以下通过串行控制台捕获的输出（此处缩写）就是证明：

```
IBC embedded bootloader 1.68.21

(c) 2012 XS Embedded GmbH

Uncompressing Linux... done, booting the kernel.
00:00:01.226 LVDS[61] contrast   : 54 -> 54
00:00:01.227 LVDS[61] (Defaulting) Speed Restriction: Enabled
00:00:01.227 LVDS[61] (Defaulting) Visteon Display.
…
00:00:01.428 LVDS[61] ChangeBrightness_Id:
00:00:01.433 LVDS[61] brightness : 5000 -> 5000
00:00:01.433 LVDS[61] BrightNessLevel = 5000.

FGSN: VPGJ3Fxxxxxxxxyy
cmu login:
```

view rawmazda\_connect-0.txt hosted with ❤ by GitHub

虽然有登录提示，但最新软件版本的验证凭据并不公开。控制台继续提供大量日志输出，这对测试漏洞很有用。

完全启动后，系统挂载了以下文件系统：

```
rootfs on / type rootfs (rw)
none on /sys type sysfs (rw,relatime)
none on /proc type proc (rw,relatime)
none on /dev type devtmpfs (rw,relatime,size=8192k,nr_inodes=95316,mode=755)
/dev/ffx01p1 on / type relfs (ro,noatime)
none on /sys type sysfs (rw,relatime)
none on /proc type proc (rw,relatime)
none on /dev type devtmpfs (rw,relatime,size=8192k,nr_inodes=95316,mode=755)
none on /tmp type tmpfs (rw,relatime,size=95232k)
/dev/ffx01p4 on /tmp/mnt/data type relfs (rw,noatime)
/dev/mmcblk0p2 on /tmp/mnt/data_persist type relfs (rw,noatime)
/dev/mtdblock5 on /config-mfg type squashfs (ro,relatime)
none on /dev/pts type devpts (rw,relatime,mode=600)
none on /dev/mqueue type mqueue (rw,relatime)
none on /tmp/mnt/tmp/race/database type tmpfs (rw,relatime,size=30720k)
/dev/mmcblk0p1 on /tmp/mnt/resources type relfs (ro,noatime)
```

查看由 GitHub ❤ 托管的 rawmazda\_connect-1.txt

操作系统可访问所有持久内存存储。串行闪存以 mtdblock 分区的形式存在，NAND 闪存以 ffx01 分区的形式存在，eMMC 闪存以 mmcblk 分区的形式存在。值得注意的是，有几个文件系统是读写加载的，括号中的 rw 字符串表示了这一点。

**软件更新过程**

可通过诊断菜单更新设备上的软件：

![]()

更新过程需要在通过 USB 连接的大容量存储设备上找到扩展名为 .up 的文件。然后，经销商可以进入诊断菜单并启动更新过程。

软件更新文件是受密码保护的 ZIP 压缩文件，包含更新过程中不同步骤的多个目录，以及说明如何执行更新的 “说明 ”文件。最新更新文件中有 21 个步骤。特别值得关注的是以下目录的内容：

– rootfs1upd 包含整个根文件系统的 .tar.gz 压缩包、
– linux1 包含 Linux 内核 3.0.35、
– ibc1 和 ibc2 包含一个引导加载器、
– bootstrap 包含另一个引导程序、
– passwdupdate 包含替换的 passwd 文件、
– vip 包含辅助 MCU 的更新映像。

更新过程的大部分在几个共享对象中实现。所有业务逻辑都位于 svcjciupdatea.so 和 svcjciupdates.so，它们使用 libjcireflashua.so 和 libjcisecurity.so 中的支持代码。对更新过程的调查仅限于签名验证。进一步的调查将假定能够生成正确签名的更新或绕过签名验证的更新。遗憾的是，前者在本次研究时还不存在，而后者在本次研究中也没有发现。

从高层来看，更新验证过程包含在 svcjciupdates.so:updates\_sys\_srv\_ValidatePackageOperationThread() 函数中，该函数会调用其他函数按指定顺序执行验证步骤：

– updates\_sys\_srv\_LoadUP() 解析指定的更新文件，提取 main\_instructions.ini 和 versions.ini 文件，并将其存储在内存中，以便以后使用。
– updates\_sys\_srv\_ValidateUPStructure() 验证更新文件的内部结构是否与预期布局一致。当按照正确的更新文件格式创建漏洞时，这不是一个问题。
– updates\_sys\_srv\_ExtractCertificates() 从更新文件中提取签名证书链，用于更新验证。该链包含用于签署更新的发布者证书和签发发布者证书的中间 CA 证书。中间 CA 证书由 JCI 根 CA 签发。
– updates\_sys\_sec\_VerifyUPCertificates() 会验证提取的证书链，以确保证书链正确终止于存储在设备上的预期根 CA。
– updates\_sys\_sec\_VerifyUPSignature() 根据发布者证书验证指定更新文件的签名。本例中的签名位于更新文件的末尾，长度为 256 字节。
– updates\_sys\_srv\_RemoveExtractedCertificates() 会在验证过程结束后进行清理。

特别值得注意的是，在对用户提供的文件进行完整性检查之前，ups updates\_sys\_srv\_LoadUP()函数及其调用函数对提供的更新文件执行了多种操作。

**漏洞**

在我们的研究工作中发现了多个漏洞，这些漏洞可以结合使用，以实现对信息娱乐系统的全面和持续控制。

**CVE-2024-8355/ZDI-24-1208: 设备管理器 iAP 序列号 SQL 注入**

该漏洞是研究过程中发现的第一个漏洞，引发了对该设备的深入研究。

具体漏洞存在于 /jci/devicemanager/libdevicemanager.so 库的 eInsertDeviceEntry() 函数中。当尝试向 DeviceDatabase.db SQLite 数据库中插入一个新的苹果设备时，会从设备中获取几个值，并在 SQL 语句中使用，而不进行消毒处理。请参见以下 eInsertDeviceEntry() 函数的伪代码实现：

```
int eInsertDeviceEntry(undefined4 param_1,int param_2)
{
  int iVar1;
  undefined auStack1052 [1024];
  int local_1c;

  local_1c = 0;
  sqlite3_snprintf(0x400,auStack1052,
                   "INSERT INTO DeviceInfo (USBSERIAL,MACADDRESS, IAPSERIAL, UIDVALID) VALUES(\'%s\',%Q,\'%s\',%d)"
                   ,param_2,param_2 + 100,param_2 + 200,*(undefined4 *)(param_2 + 300));
  race_print_log(4,0x11,"eInsertDeviceEntry",0x4c0,"DEVMGR_DATABASE","Query is : %s\n",auStack1052);
  iVar1 = sqlite3_exec(param_1,auStack1052,0,0,&local_1c);
  if (iVar1 != 0) {
    race_print_log(1,0x11,"eInsertDeviceEntry",0x4c5,"DEVMGR_DATABASE","SQL error: %s %d\n",local_1c
                   ,iVar1);
    if (local_1c != 0) {
      sqlite3_free();
    }
  }
  if (iVar1 != 0) {
    iVar1 = 1;
  }
  return iVar1;
}
```

查看由 GitHub ❤ 托管的 rawmazda\_connect-2.c

正因为如此，当信息娱乐系统检测到苹果设备已连接并请求（例如）其 iAP 序列号时，伪造的 iPod 或其他苹果设备可以回复如下字符串：

```
     ' , 0); [ANY SQL STATEMENT];--
```

查看由 GitHub ❤ 托管的 rawmazda\_connect-3.txt

这导致 DeviceManager 以 root 权限在信息娱乐系统上执行注入的 SQL 语句。这可用于操作数据库本身、披露信息、在文件系统上创建任意文件，甚至可能执行代码。由于输入的长度限制为 0x36 字节，因此对该漏洞的利用受到了一定的限制，但这有可能通过让多个伪造的 iPod 相继连接来解决，每个 iPod 都用自己注入的 SQL 语句代替序列号。

**CVE-2024-8359/ZDI-24-1191: REFLASH\_DDU\_FindFile 命令注入 RCE**

libjcireflashua.so 共享对象中的 REFLASH\_DDU\_FindFile() 函数是支持更新过程的众多函数之一。为清晰起见，现将该函数的伪代码复制如下：

```
undefined4 REFLASH_DDU_FindFile(char *_up_path,char *_file_name,int _is_gzipped)
{
  int iVar1;
  undefined4 uVar2;
  char acStack_408 [1023];
  undefined local_9;

  memset(acStack_408,0,0x400);
  if ((_up_path == (char *)0x0) || (_file_name == (char *)0x0)) {
    REFLASH_UL_WriteLog("Core Reflash",0,0,"reflash_ddu.c","REFLASH_DDU_FindFile",0x181,
                        "Some of the input parameters are wrong!");
    uVar2 = 0xffffd8f0;
  }
  else {
    if (_is_gzipped == 1) {
      if (reflash_ddu_password == 0) {
        snprintf(acStack_408,0x400,"%s \"%s\" \"%s.gz\" > /dev/null","unzip -t",_up_path,_file_name)
        ;
      }
      else {
        snprintf(acStack_408,0x400,"%s %s \"%s\" \"%s.gz\" > /dev/null","unzip -t -P",
                 reflash_ddu_password,_up_path,_file_name);
      }
    }
    else if (reflash_ddu_password == 0) {
      snprintf(acStack_408,0x400,"%s \"%s\" \"%s\" > /dev/null","unzip -t",_up_path,_file_name);
    }
    else {
      snprintf(acStack_408,0x400,"%s %s \"%s\" \"%s\" > /dev/null","unzip -t -P",
               reflash_ddu_password,_up_path,_file_name);
    }
    local_9 = 0;
    iVar1 = system(acStack_408);
    if (iVar1 == 0) {
      uVar2 = 0;
    }
    else {
      uVar2 = 0xffffd8fb;
    }
  }
  return uVar2;
}
```

mazda\_connect-4.c 由 GitHub ❤ 托管

该函数尝试在通过提供的文件路径指定的更新包中查找特定文件。这是通过将提供的路径插值到解压缩程序的命令行中来实现的。不幸的是，在此之前没有进行任何消毒处理，攻击者控制的输入（如 /dev/sda1/path/file.up）被传递到 system() 函数。这样，攻击者就可以注入任意操作系统命令，由主机操作系统外壳执行，从而完全入侵系统。攻击者可以控制整个路径中的路径和文件元素。

受影响的函数可通过以下调用图到达：

– svcjciupdates.so 中的 UPDATES\_SYS\_IPC\_INTERFACE\_GetPackageInfo\_svc
– UPDATES\_SYS\_SRV\_GetPackageInfo
– Update\_sys\_srv\_GetPackageInfoOperationThread
– 更新\_sys\_srv\_LoadUP
– libjcireflashua.so 中的 REFLASH\_UA\_LoadUP
– REFLASH\_DDU\_FindFile

**CVE-2024-8360/ZDI-24-1192: REFLASH\_DDU\_ExtractFile 命令注入 RCE**

libjci...