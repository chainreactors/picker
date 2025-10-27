---
title: 通过ROP实现RCE的一次技术探索之旅
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247510554&idx=1&sn=42c98f4263928e124525e90ee39adbc6&chksm=fa527fa4cd25f6b24ecff2015fd9c0adae0adf7f648e7d55c4ce7824d72ea227aac38fd43b44&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2025-02-26
fetch_date: 2025-10-06T20:38:02.958029
---

# 通过ROP实现RCE的一次技术探索之旅

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSWGjiaxicD2QJYKeDNqbShKjYT18B5ztazBWLat9ENGbRUYcQYKuY638d7WbL2T7SUlJdjpfDxfxGQ/0?wx_fmt=jpeg)

# 通过ROP实现RCE的一次技术探索之旅

山石网科

山石网科安全技术研究院

![图片](https://mmbiz.qpic.cn/mmbiz_gif/NGIAw2Z6vnKvXxzN9syadS6NM2YvjAFg2NBLDqDGZVP1U0V8gHOVwgkjJ2wpWTDz4YRA2t8rlEWdxNWIhnnhpA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8Jb8ZACqDjPdMzgicp2SzdZ19mFnVcBO53s1uA2cSfarQkwibVUeCeH9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**ROP实现RCE：这不是魔法，这是技术的魅力！**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NGIAw2Z6vnLKuKAwMiaYedpTAYugKibaTBsHzf5pDuztECgfIgOfpG5DRF31jzhosMEj23dlx186q0zgLaIZj9lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

在网络安全领域，远程代码执行（RCE）一直是攻击者和防御者关注的焦点。今天，为大家带来一篇深度文章[1]，它将引领我们深入探讨如何通过ROP（Return-Oriented Programming）实现RCE。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**一、前言**

在红队演练中，仅仅发现一个XSS漏洞或基本配置错误通常是不够的，真正的目标是实现远程代码执行(RCE)。在一次这样的评估中，我们遇到了雄迈(厂商)的uc-httpd，这是一个轻量级的Web服务器，被全球无数的IP摄像头使用。根据Shodan的数据，大约有7万个该软件的实例在互联网上公开暴露。虽然该软件历史上存在严重漏洞，但没有现成的Exp能够实现代码执行，因此我决定自己开发一个。最初的计划是针对CVE-2018-100881[2]，这是一个缓冲区溢出漏洞，现有的Exp[3]只能使服务器崩溃，但无法实现RCE。但正如大多数探索之旅一样，很少有直通终点的路径，更多时候需要灵活应对。于是，在这个过程中，我发现了新的路径，学习了ARM架构的知识，并构建了一个ROP链。这个ROP链通过Web请求传递，并巧妙地重用了相同的连接作为Shell。毕竟，谁还需要反向Shell呢？不过，让我们从故事的开头讲起。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**二、分析**

在尝试利用漏洞之前，我们需要先理解漏洞的原理。因此，首先我需要获取uc-httpd的源代码或编译后的二进制文件。不出所料，该软件并不开源。但幸运的是，存在一个非常简单的路径遍历漏洞—CVE-2017-75773[4]，允许从受影响的uc-httpd服务器下载任意文件。通过访问/proc/self/exe，可以下载当前正在运行的可执行文件（通常名为Sofia）进行分析。我使用file和checksec[5]对目标二进制文件进行了常规检查。如下所示，这是一个ARM32位动态链接的可执行文件。

```
$ file Sofia
Sofia: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically
linked, interpreter /lib/ld-uClibc.so.0, stripped
```

```
$ checksec --file=Sofia
RELRO           STACK CANARY     NX           PIE
No RELRO       No canary found   NX disabled   No PIE
```

没有重定位只读(RELRO)保护，这意味着全局偏移表(GOT)是可写的；没有栈保护机制（stackcanary）来检测栈溢出；不可执行（NX）保护也被禁用，允许在栈上执行shellcode。此外，由于它不是位置无关可执行文件（PIE），该二进制文件总是被加载到一个固定的内存地址。

我启动Ghidra来反编译二进制文件并探索其内部工作原理。通过触发漏洞并查看日志输出的字符串的交叉引用，我能够精确定位一个似乎充当HTTP调度者的函数（关于具体的调试环境，稍后会详细介绍）。‍

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSWGjiaxicD2QJYKeDNqbShKjKDddQ7bAsdnp3aOuPN307y1IJwJgAZKjapa5uSkPT5kz9ecT5iacg4A/640?wx_fmt=png&from=appmsg)

在这个函数中，CVE-2018-10088[2]很容易被发现。常见的可疑函数strcpy被用来将http请求体中的用户名和密码参数复制到某些数据段中。

```
substring = strtok((char *)0x0,"&")；
strcpy(&DATA_USERNAME,substring + 9)；
substring = strtok((char *)0x0,"&")；
strcpy(&DATA_PASSWORD,substring + 9)；
```

通过检查这些数据段，我发现这些缓冲区的长度均为20字节。因此，超过20个字符的用户名和密码会导致相应的缓冲区溢出。我还发现这些缓冲区位于二进制文件的.bss数据段中，这对于劫持程序执行流来说显然不是理想的情况。不过，我注意到在该段的下方有一些函数指针，通过溢出覆盖这些指针，理论上可以重定向程序执行流。

‍

然而，在浏览了调度器函数的其余部分后，我发现了另一个漏洞（后来我才知道这是CVE-2022-45460），这个漏洞似乎更符合我的目标。让我们来看看它。‍

```
iVar1 = strcmp((char *)__s1,".lang")；
if (iVar1 == 0) {
    sprintf(filepath,"%s/%s","/mnt/custom",&DAT_FILEPATH)；
}
else {
    substring = strstr((char *)uri,"mns.cab")；
    if (substring == (char *)0x0) {
        strstr((char *)uri,"logo/")；
 sprintf(filepath,"%s/%s")；
   }
    else {
        sprintf(filepath,"%s/%s","/usr/mobile",uri)；
   }
}
iVar1 = stat(filepath,&stat_struct)；
if (iVar1 != 0) {
    if ((filepath[0] != '\0') && (iVar1 = atoi(filepath), 0 < iVar1)) {
        DAT_006e9324 = iVar1；
        sprintf((char *)&uStack_68,".%s","/index.htm")；
        FUN_003376cc(socket_stream,&uStack_68,0)；
        return 0；
   }
    write_response_header(socket_stream,0x68)；
    fwrite("<html><head><title>404 File Not Found</title>
</head>\n",1,0x35,socket_stream)；
    fwrite("<body>The requested URL was not found on this server</body>
</html>\n",1,0x43,socket_stream)；
    return 0；
}
```

这段代码中，URI和文件路径使用sprintf进行拼接，且没有任何边界检查。特别有趣的是，当用户控制的URI与字符串/usr/mobile拼接时，会发生溢出。在这种情况下，溢出发生在我称为filepath的栈变量上。栈溢出非常强大，因为通常函数的返回地址存储在栈上，这使得在溢出期间可以覆盖这些地址并重定向程序的执行流。由于没有栈保护机制（stackcanary）的阻碍，因此这个漏洞应该相对容易利用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**三、调试环境**

在深入研究漏洞之前，我希望建立一个专门的测试环境用于调试。我的目标是避免依赖任何硬件设备。由于没有任何现有Exp，我无法访问设备来部署调试器。

‍

因此，我首先利用之前提到的路径遍历漏洞（CVE-2017-75773）来转储文件系统。然后，我尝试使用chroot和QEMU的ARM系统模拟器[6]来构建一个完全虚拟化的环境。这种方法在一段时间内运行良好，但最终表现出一些看似奇怪的行为，特别是在内存地址方面。

‍

我手头还有一个闲置的树莓派，于是决定尝试用它来搭建环境。我将获取到的rootfs复制到树莓派上，并下载了静态编译的gdbserver[7]和bash（gdb所需）二进制文件。接着，我在树莓派上的chroot环境中启动了gdbserver。

```
$ sudo mount --bind /proc/ rootfs/proc
mount: (hint) your fstab has been modified, but systemd still uses
       the old version；use 'systemctl daemon-reload' to reload.
pwn@raspberrypi:~ $ sudo chroot rootfs/ sh
# ls
bin       dev       gdbserver linuxrc   proc       tmp       utils
boot       etc       lib       mnt       sbin       usr       var
# ./gdbserver :8888 Sofia
Process Sofia created；pid = 911
Listening on port 8888
Remote debugging from host 192.168.2.1, port 64996
```

然后，我使用gdb-multiarch从我的机器连接到树莓派上的gdbserver。

```
$ gdb-multiarch
GNU gdb (Debian 15.2-1+b1) 15.2
Copyright (C) 2024 Free Software Foundation, Inc.
(...)
gef➤ gef-remote 192.168.2.2 8888
```

因此，最终的调试环境大致如下[8][9]：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSWGjiaxicD2QJYKeDNqbShKj7TRty2nqLQkvuZo7dc040cQUmNXXdibcRnCU1Lgvegvd0zdu1lx53UQ/640?wx_fmt=png&from=appmsg)

这种配置允许在攻击者的机器上使用GEF[10]来设置断点并远程调试树莓派上的目标程序，非常完美。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**四、触发漏洞**

在完成上述调试环境配置后，可以首次尝试触发已识别的漏洞。这个过程与任何此类二进制漏洞利用(Pwn)挑战并无不同。为了控制程序执行流，我们首先需要确定输入在栈上的哪个位置覆盖了特定偏移量，最终该偏移量会被pop到指令计数器PC中。通过发送独特的字符序列并观察程序崩溃时PC寄存器中的字节，我们可以精确地找到偏移量。唯一需要注意的是，URI必须以.mns.cab结尾，以确保命中正确的代码路径。

```
import sys
import socket
payload = b""
payload += 304 * b"A" + b"BBBB"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((sys.argv[1], int(sys.argv[2])))
    sock.send(b"GET /" + payload + b".mns.cab HTTP/1.1")
    sock.send(b"\r\n\r\n")
print(sock.recv(1024))
```

为了观察服务器端的情况，我在漏洞代码段之后的返回语句处（即第二次调用fwrite之后）设置了一个断点。如下图所示，寄存器r4到r10依次从栈中弹出，随后是PC寄存器。使用上述Python脚本，这些寄存器被填充为字符A，而PC寄存器被设置为BBBB，这标志着控制流劫持的入口点。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSWGjiaxicD2QJYKeDNqbShKjGzEbSQZib1iafibQ2lstcgoqqg7guj6gZ4t4yDa6PU4ctv1HgtcU1hgew/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**五、构造Exp**

这里有件事需要说明一下。尽管NX保护被禁用，理论上栈应该是可执行的，但我对此并不十分确定。在我的树莓派设置中，栈始终被标记为rw，而不是rwx。尝试从栈上执行shellcode失败了。因此，我（错误地）认为在真实设备上也会是同样的情况。我没有过多思考这个问题，而是继续按照计划构建ROP链。ROP（Return-OrientedProgramming，面向返回编程）是一种漏洞利用技术，攻击者利用程序中已经存在的小段代码片段（称为gadgets）。通过将这些gadgets链接在一起，攻击者可以执行任意代码，而无需注入新的代码。此外，尽管Sofia二进制文件本身禁用了PIE，但其包含的库启用了PIE，因此我也假设ASLR是启用的。这意味着在构建ROP链时需要绕过ASLR，以便使用来自库（如libc）的gadgets。另一个需要注意的重要问题是，由于我们使用sprintf进行溢出，因此payload不能包含空字节\x00，否则会被截断。此外，在进一步检查反编译的代码段后，我发现空格也会被去除。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**六、ASLR绕过**

由于Sofia二进制文件未启用PIE，即使启用了ASLR，它也会始终加载到相同的内存区域。然而，由于二进制文件映射到的地址区域仅覆盖地址空间的低3字节，因此每个地址的最高有效字节都包含一个空字节\x00。这意味着，至少在ROP链的入口点，无法使用Sofia二进制文件本身的gadgets。因此，我将注意力转向了包含的libc库，但由于libc编译时是开启PIE的，绕过ASLR变得至关重要。你可能已经猜到，我们的路径遍历漏洞再次派上了用场，这次是为了绕过ASLR。其实并没有什么神奇之处，只是通过转储/proc/self/maps来获取Sofia进程的内存映射，从而确定所有包含库的基地址。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8lvpAJHElQA6DiaJniaZb0daO3Kppz9ndV9Z2hHsjMuH61r2hu0jesGSg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**七、ARM架构**

由于构建ROP链需要对底层架构有一定的了解，我们需要先介绍一些关于ARM架构的基本概念。如果你已经熟悉这些内容，可以跳过这部分。ARM是一种精简指令集(RISC)架构，这意味着它使用少量的简单...