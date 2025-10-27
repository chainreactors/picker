---
title: SystemTap在应急排查中的应用
url: https://buaq.net/go-130896.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:55:06.528113
---

# SystemTap在应急排查中的应用

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

![](https://8aqnet.cdn.bcebos.com/678ca05ae9ee20ef6473b5b1508504c2.jpg)

SystemTap在应急排查中的应用

阅读：16假如现在有这么一个需求：需要获取正在运行的 Linux 系统的信息，如我想知道系统什么时候发生系统调用，发生的是什么系统调用等这些信息，
*2022-10-14 18:50:7
Author: [blog.nsfocus.net(查看原文)](/jump-130896.htm)
阅读量:27
收藏*

---

阅读：
16

假如现在有这么一个需求：需要获取正在运行的 Linux 系统的信息，如我想知道系统什么时候发生系统调用，发生的是什么系统调用等这些信息，有什么解决方案呢？

通俗一点讲，上面的需求可以转化为应对日常应急可能遇到的一些场景：

1、谁在Linux系统上谁在发送DNS（UDP）、ICMP、ARP请求？例如挖矿病毒（矿池失活）、PingTunnel等。

2、哪个进程在对某个文件进行写入？

3、在没有网络设备的情况下，监控所有外对内的连接尝试（无论成功与否）。

4、进程创建、终止，进程模块的加载、卸载。

5、检测rootkit

6、等等

以上需求都可以总结为：对Linux内核调用进行调试跟踪。

## ****Linux下内核调试技术的发展****

Linux下的调试技术分为动态调试和静态调试。

### 静态调试

静态调试又名 “插桩”，tracepoint。在Linux发展的早期，实现对Linux内核的调试，需要编写内核模块，对开发要求比较高，同时容易干扰内核的稳定运行。编写、编译、安装到内核，过程繁琐、效率低下、灵活性差。

### 动态调试

类似Win下的动态调试。更加灵活地捕获内核调用，使用门槛低，稳定且几乎无干扰。早期的动态调试器有GDB、KDB等。

动态追踪技术的鼻祖是Dtrace，它于 21 世纪初诞生于 Solaris 操作系统，是由原来的 Sun Microsystems 公司的工程师编写的，先后被移植到 Linux、FreeBSD、NetBSD 及 Mac OS X 等操作系统上。iOS 系统上大名鼎鼎的 Instrument 工具就是基于 DTrace 实现的。Mac OS X 默认安装了dtrace工具；脚本使用D语言编写，也叫 d 脚本，Mac OS X的/usr/share/examples/DTTk/目录下有很多例子。Dtrace技术原理如下图：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image1-300x247.png)

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image2-300x168.png)

Linux 在过去十多年的发展中, 演化了很多追踪与调试技术, 不过一直没有一款可以媲美 DTrace 的工具, 直到 Linux 4.1+ 版本 eBPF 机制的出现, 这种情况才得到了极大的改善. 不过 eBPF 也不是一蹴而就的, 而是经过了漫长的过程才得以完善。Linux下动态调试技术出现时间：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image3-300x90.png)

### kprobe是什么

* kprobe调试技术是专门为了便于跟踪内核函数执行状态所设计的一种轻量级内核调试技术。
* 利用kprobe技术，可以在内核的绝大多数指定函数中动态的插入探测点来收集所需的调试状态信息而基本不影响内核原有的执行流程。
* kprobe技术目前提供了3种探测手段：kprobe、jprobe和kretprobe，其中jprobe和kretprobe是基于kprobe实现的，他们分别应用于不同的探测场景中。

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image4-300x63.png)

### ****SystemTap是什么****

systemtap 是利用Kprobe 提供的API来实现动态地监控和跟踪运行中的Linux内核的工具，相比Kprobe，systemtap更加简单，提供给用户简单的命令行接口，以及编写内核指令的脚本语言，类似C语言、D语言。

### ****systemtap原理****

SystemTap 基本思想是命名事件，并为它们提供处理程序。每当发生指定的事件时，内核都会将处理程序视为子例程运行，然后继续运行。有一系列的事件，例如进入或退出函数，计时器到期或整个SystemTap会话的开始和停止。处理程序是一系列脚本语言语句，用于指定事件发生时要完成的工作。这项工作通常包含从事件上下文中提取数据，将其存储到内部变量或打印结果。

SystemTap 的工作原理是将脚本翻译成C语言，执行C编译器创建一个内核模块。当模块被加载后，通过挂载到内核来激活所有的探测事件。然后，当事件发生再任何处理器上时，编译后的处理程序就运行，最终，SystemTap会话停止，Hook取消，内核模块被移除，整个过程由命令行程序stap驱动。

原理如下图所示：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image5-300x231.png)

## ****systemtap实践****

### 安装

以较老的系统（CentOS6.8 x64为例），查看内核版本，并下载与内核版本完全一致调试依赖包：

kernel-debuginfo

kernel-debuginfo-common

kernel-devel

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image7-300x43.png)

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image8-300x23.png)

****手动安装：****

rpm -ivh kernel-debuginfo-common-x86\_64-2.6.32-642.el6.x86\_64.rpm

rpm -ivh kernel-debuginfo-2.6.32-642.el6.x86\_64.rpm

rpm -ivh kernel-devel-2.6.32-642.el6.x86\_64.rpm

yum install systemtap systemtap-runtime       **#yum安装systemtap**

****测试：****

stap -V

stap -h

stap -e ‘probe begin{printf(“Hello, World\n”); exit();}’

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image9-300x45.png)

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image10-300x17.png)

****如果提示**** Incorrect version or missing kernel-devel package, use: yum install kernel-devel-xxxxx

则安装的kernel-devel版本与内核不匹配。

### 工作流程解释

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image11-300x44.png)

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image12-300x62.png)

### 重要文件和目录

|  |  |
| --- | --- |
| ****/lib/modules/KERNEL\_VERSION/systemtap/**** | 保存 SystemTap 工具模块。 |
| ****/usr/share/systemtap/tapset/**** | 保存标准的 tapset 库。 |
| ****/usr/share/doc/packages/systemtap/examples**** | 保存用于各种目的的多个示例 SystemTap 脚本。仅当已安装 systemtap-docs 软件包时才可用。 |
| ****~/.systemtap/cache**** | 缓存的 SystemTap 文件的数据目录。 |
| ****/tmp/stap\***** | SystemTap 文件的临时目录，包含已转换的 C 代码和内核对象。 |

### 脚本

systemtap脚本默认文件后缀为.stp，文件内容有固定的格式，有完整的语法（变量、常量、注释、条件、循环、数组等等）。begin/end, 分别是systemtap会话的起始和结尾，IDE推荐VSCode。如下图所示：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image13-300x255.png)

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image14-300x176.png)

systemtap脚本编写****参考****： https://sourceware.org/systemtap/tutorial/

### 可探测事件

Kprobes允许你为任何内核指令以及函数入口和函数返回处理程序安装预处理程序和后处理程序。

常用的可探测事件如下：

|  |  |
| --- | --- |
| tid() | 当前线程的 ID。 |
| pid() | 当前线程的进程 ID。 |
| uid() | 当前用户的 ID。 |
| cpu() | 当前 CPU 编号。 |
| execname() | 当前进程的名称。 |
| gettimeofday\_s() | 自 Unix 纪元（1970 年 1 月 1 日）起经过的秒数。 |
| ctime() | 将时间转换为字符串。 |
| pp() | 用于描述当前正在处理的探测点的字符串。 |

函数大全：https://sourceware.org/systemtap/tapsets/index.html

### 实际应用

* 监控DNS请求

脚本原理：判断外联目标端口为53

#! /usr/bin/env stap

global the\_dport = 53

probe netfilter.ip.local\_out {

if (the\_dport == dport)

printf(“%s[PID:%d,TID:%d] sent packet to %s:%d\n”, execname(), pid(),  tid(), daddr, dport)

}

效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image16-300x21.png)

* 监控ICMP请求

脚本原理： netfilter.ip.local\_out 为所有协议外联，ICMP的目标端口为0

#! /usr/bin/env stap

probe ****netfilter.ip.local\_out****{

if (0 == dport)

printf(“%s[PID:%d,TID:%d] sent %d to %s:%d\n”, execname(), pid(),  tid(),length, daddr, dport)

}

probe ****netfilter.ip.local\_in****{

if (0 == sport)

printf(“%s recv %d from %s:%d\n”, execname(),length, saddr, sport)

}

监控ping得到的效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image17-300x43.png)

* 监控传入TCP连接（连接成功的）

脚本原理：传入握手成功，会有accept标识

#! /usr/bin/env stap

probe begin {

printf(“%6s %16s %6s %6s %16s\n”,

“UID”, “CMD”, “PID”, “PORT”, “IP\_SOURCE”)

}

probe kernel.function(“tcp\_accept”).return?,

kernel.function(“inet\_csk\_accept”).return? {

sock = $return

if (sock != 0)

printf(“%6d %16s %6d %6d %16s\n”, uid(), execname(), pid(),inet\_get\_local\_port(sock), inet\_get\_ip\_source(sock))

}

效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image18-300x33.png)

* 监控传入TCP连接尝试（不管成功与否）

脚本原理：监控receive，如果是传出则用sendmsg

#! /usr/bin/env stap

probe tcp.receive {

if(dport!=22) #exclude 22 port

printf(“%s:%d –> %s:%d\n”, saddr, sport, daddr, dport)

}

效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image19-300x105.png)

* 监控TCP连出（不管成功与否）

脚本原理：监控receive，如果是传出则用sendmsg

probe begin {

printf(“ok\n”);

}

probe syscall.connect {

if (uaddr\_af == “AF\_INET” || uaddr\_af == “AF\_INET6”)

printf(“%s[%d]: %s\n”, execname(), pid(), argstr);

}

curl baidu.com效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image20-300x74.png)

nc 8.8.8.8 9999，无法连接成功的端口，效果：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image21-300x14.png)

* 监控对文件的操作

#!/usr/bin/stap

probe vfs.{write,read}

{

# dev and ino are defined by vfs.write and vfs.read

if (dev == MKDEV($1,$2) && ino == $3)

printf (“%s(%d) %s(%d) %s 0x%x/%u\n”,execname(), pid(), pexecname(), ppid(), ppfunc(), dev, ino)

}

步骤：

先获取要监控的文件信息：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image22-300x34.png)

使用df查看log.txt 所在的设备

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image23-300x90.png)

log.txt在/的子文件夹下，所以要找/dev/mapper/centos-root的主从设备号

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image24-300x18.png)

得到根目录的主从设备号为253 0

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image25-300x35.png)

所以inodewatch.stp的参数为253 0 36398378

执行stap /usr/share/systemtap/examples/io/inodewatch.stp 253 0 52092325，效果如下：

![](http://blog.nsfocus.net/wp-content/uploads/2022/10/image26-300x103.png)

SystemTap的功能远不止这些，除了内核调试，还可以实现用户态的调试。本文仅抛砖引玉。更多学习资料参考下一章节。

### 相关****参考****

debuginfo下载

https://mirrors.ocf.berkeley.edu/centos-debuginfo/

https://oss.oracle.com/el6/debuginfo/

http://debuginfo.centos.org/6/x86\_64/

kernel-devel下载

ftp://ftp.pbone.net/mirror/ftp.scientificlinux.org/linux/s...