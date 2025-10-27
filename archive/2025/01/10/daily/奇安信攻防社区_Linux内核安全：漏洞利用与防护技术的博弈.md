---
title: Linux内核安全：漏洞利用与防护技术的博弈
url: https://forum.butian.net/share/4007
source: 奇安信攻防社区
date: 2025-01-10
fetch_date: 2025-10-06T20:05:58.573895
---

# Linux内核安全：漏洞利用与防护技术的博弈

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Linux内核安全：漏洞利用与防护技术的博弈

* [渗透测试](https://forum.butian.net/topic/47)

内核是操作系统的核心组件，负责管理计算机硬件资源和提供基础服务以支持系统软件和应用程序的运行。它是操作系统中最高权限的部分，直接与硬件交互，并通过抽象硬件功能，为用户态进程提供统一的接口

Kernel 基础
=========
什么是内核？
------
内核是操作系统的核心组件，负责管理计算机硬件资源和提供基础服务以支持系统软件和应用程序的运行。它是操作系统中最高权限的部分，直接与硬件交互，并通过抽象硬件功能，为用户态进程提供统一的接口
内核常用的指令
-------
特权指令：
```php
CLI：清除中断标志，禁止中断
STI：设置中断标志，允许中断
HLT：停止处理器，直到下一个中断发生
IN/OUT：从I/O端口读写数据
LGDT/SGDT：加载/存储全局描述符表（GDT）
LIDT/SIDT：加载/存储中断描述符表（IDT）
LTR：加载任务寄存器
MOV CRx：读取或写入控制寄存器（如CR0、CR3）
```
系统调用相关指令：
```php
SYSCALL/SYSRET：用于快速调用和返回系统调用（在x86\_64架构上）
INT 0x80：通过中断调用系统调用（在x86架构上）
```
页表管理：
```php
MOV CR3：设置页表基地址寄存器，切换页表
INVLPG：无效化某个虚拟地址的页表缓存
```
调试指令：
```php
INT3：触发断点中断，通常用于调试
RDTSC：读取时间戳计数器，测量精确的时间
```
特殊的寄存器
------
cr3 (Control Register 3)寄存器记录页表信息，用于将进程的虚拟地址转换为物理地址，这个寄存器直接用mov指令就能操作，但是要在内核模式下才能访问
MSR LSTAR (Model-Specific Register, Long Syscall Target Address Register)寄存器是基于特定模式的寄存器，它记录了系统调用会跳转到哪里执行，wrmsr指令和rdmsr指令是用来操作这个寄存器的，这两个指令也仅供内存使用的
那么计算机是如何知道用户是否可以访问如cr3之类的只有内核模式才能权限访问的寄存器呢
用户模式特权级别
--------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d985343b6b48ff1235226af419aeb52cba9a4be7.png)
当cpu在执行时，会记录当前程序的权限级别，上图是基于x86架构的，Ring3是最小权限环，在这一环里有很多限制，比如说不能设置cr3寄存器，不能和硬件外设交互，不能执行HLT之类的，当软件在这一环上运行，需要和系统进行交互时，就会转换到Ring0，这里还有Ring2和Ring1，最初它们是为设备驱动准备的，区分了不同的访问级别，但是很少会用到，Ring0是主管模式，在这一环里是没有限制的，可以做任何事，这也是内核运行的地方
```php
Ring 3：用户模式，权限最低，限制较多，无法访问CR3等内核模式寄存器，无法执行HLT指令等。
Ring 0：内核模式，权限最高，可以执行任何指令和访问所有寄存器。
Ring -1：管理模式（主要用于虚拟化），可以拦截敏感操作，确保虚拟机中的用户内核无法无限制地访问主机硬件。
```
Ring -1
-------
还有一个Ring -1环，但是内核是在Ring 0环的，随着虚拟机的兴起，管理模式的特权开始引发问题。虚拟机的“用户”内核不应该能够无限制地访问主机的物理硬件，Ring -1，管理程序模式。能够拦截用户执行的敏感 Ring 0 操作并在主机操作系统中处理它们
不同类型的操作系统模型
-----------
1. 单片内核
所有操作系统级别任务由一个统一的内核二进制文件处理。驱动程序作为库加载到此二进制文件中。示例：Linux、FreeBSD。
2. 微内核
只有一个微小的核心二进制文件，提供进程间通信和与硬件的最小交互。驱动程序作为普通用户空间程序运行，具有稍高的权限。示例：Minux、seL4。
3. 混合内核
结合了微内核和单片内核的特点。示例：Windows NT、MacOS。
环与环之间切换
-------
这里主要展示的是x86\\_64 arm架构，在启动时，在 Ring 0 中，内核将 MSR LSTAR 设置为指向系统调用处理程序例程，当用户空间（Ring 3）进程想要与内核交互时，它可以调用 syscall，具体方式如下：
```php
权限级别切换至 Ring 0
控制流跳转到 MSR LSTAR 的值
返回地址保存到 rcx
https://www.felixcloutier.com/x86/syscall
```
内核返回用户空间时，通过sysret指令完成权限级别切换和控制流跳转
```php
权限级别切换到 Ring 3
控制流跳转到 rcx
https://www.felixcloutier.com/x86/sysret
```
内核与用户空间的关系
----------
用户空间进程的虚拟内存位于低地址。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-057b9e4e78a2a8f7aa1c46c916e9f549727e4b36.png)
内核拥有自己的虚拟内存空间，位于高地址，只有在Ring 0才能访问
攻击方式
----
内核漏洞可能来自以下几个方向：
```php
来自网络：远程触发漏洞，如死亡数据包。
来自用户空间：系统调用和ioctl处理程序中的漏洞。
来自设备：从连接的设备（如USB硬件）触发的漏洞。
```
常见的内核漏洞利用手段：
```php
提升权限、安装rootkit。
获得更多访问权限，攻击系统其他部分，如受信任的执行环境。
```
Kernel 调试环境搭建
=============
虚拟机环境设置
-------
对内核进行开发和利用会产生很多bug。为了避免不断重启，不要在现实环境编译，而是在虚拟机中调试，这里附上环境快捷搭建的github项目地址：
```php
https://github.com/pwncollege/pwnkernel
```
解压后，进入文件夹，执行build.sh脚本，它会为我们自动安装调试内核所需要的程序和编译内核
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-aaf3e85c99f1aeca2be6b9d5449bc0948c97a5be.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a956703e7f62e1a52cc0d40cc2a6d258ef8684a3.png)
运行launch.sh脚本，这个脚本会把用户空间捆绑到一个文件系统中，然后启动qemu，进入虚拟linux系统环境
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-babff571ecb03a79cdbab012b842e171088cd8b8.png)
主机文件目录在
```php
/home/ctf/
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-976b9baa38cb9991dc5dbcbab32e21fd534cee79.png)
调试内核与syscall
------------
在启动qemu时，开启了gdb远程调试与关闭了地址随机化， gdb调试默认端口为1234
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-525f72c3edeae885959a4eb8e4992829c54c97b5.png)
内核文件是
```php
./linux-5.4/vmlinux
```
写了一个简单的调用syscall的程序
```php
.global \_start
.intel\_syntax noprefix
\_start:
xor eax,eax
mov al,60
syscall
```
这些汇编语言只是执行了一个exit(0)，因为qemu里没有lib库，所以要在主机上静态编译这个文件
```php
gcc -static -o exit -nostdlib exit.s
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ebdf2b70cea73445175e59395302edc26c79a535.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-573e2eb816f522fa99ff36e0ae6911308bfdccf3.png)
使用objdump查看这个程序的地址
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f663ca42a8c963b256ef09f7b54dd6b0d8b480ea.png)
程序入口处就在0x401000处，使用gdb导入要调试的内核，并进行远程调试
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1147e4805b6bc4cc693b3352c82d50e4bc0f03a8.png)
gdb提示当前在default\\_idle函数处，因为连接上了远程调试，而现在是gdb是暂停的状态，所以在qemu里无法操作的
查看当前rip寄存器，可以发现地址都是0xFFFFFF起步，说明现在已经在内核空间了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c6c34a1842bab0a13077fe89d57161d51bb95e14.png)
在gdb里输入C运行内核，qemu里才能正常操作，ctrl+c中断，qemu里又无法执行
0x401000地址是程序exit的起始地址，在0x401000地址处打一个断点，这个地址不是内核地址，但是我们现在可以调试整个系统，当运行到0x401000地址处时，内核就会暂停
打完断点后运行程序，然后回到qemu执行exit程序
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4d78aafecf5a41b8a0cd01e1b643c3807f415726.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a7e72831166cac8ae10a4ef66eee66828850ae77.png)
现在触发了断点，回到gdb，查看汇编代码
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6795e3c03503021a670eb26e42b55aea20f4b75c.png)
这些汇编代码就是exit程序里的，这些都是即将执行的程序，输入si，进入syscall
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-afbaa7c8821c8845a857fc4a6a074c73be99258b.png)
可以看到地址都是FFFFF开头的，说明我们现在在内核空间了，syscall会把返回地址放到rcx寄存器里，查看rcx寄存器
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-aef3dab669a9d6aa06653ce18e9c71bbc24c0424.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3499179a7407cc410e3e0ecb10fa3b41efa4f3f1.png)
执行完syscall，它就会返回到0x401006地址处继续执行其他指令
一直输入si，可以跟踪syscall函数执行的一些指令，在其中可以看到push指令，需要注意的是，这里不是push到用户空间的栈里，而是内核栈
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9f53d272a07c466dd7c37608e3abc33d8d8b35f2.png)
查看rsp寄存器，它已经将栈切换到了内核栈
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c0f3ef26be62cfcd8156091b2404e4bf00b07d77.png)
进入这个do\\_syscall\\_64函数，这里面是syscall主要操作的指令
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-37408ef1c6b4a0878b1ecbf39b581db833b78959.png)
输入finish执行完这些指令，来看看之后syscall是如何返回到用户空间的
现在正在恢复这些寄存器状态
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-de430b92ccba612d48f8397ec3c3661646526e1b.png)
还恢复了用户空间的栈指针
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c7a424a0b681d4e454126beeccd1bcaf6896d10a.png)
恢复了rsp，rdi，执行完pop rsp指令后查看rsp寄存器
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-8fb111eeef85a633c91b69ff95e3daa20fba5659.png)
可以看到现在已经回到了用户空间的栈指针，最后调用sysret指令，回到0x401022
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1ac75b2b5923c253f50b75e264c811639a135065.png)
内核模块
====
内核模块是linux生态系统的重要组成部分，主要用于实现设备驱动程序，概念上类似于用户空间的库，内核将内核模块加载到自身以提供各种功能，这些模块是一个ELF文件，扩展名为.ko，模块中的代码会以内核相同的权限运行
输入lsmod，可以查看当前加载到内核的内核模块
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9cb7252d869686b6c740cde17f79db2f84b37516.png)
内核模块中断
------
内核模块中断是指操作系统内核中的一个功能，用于处理中断请求（IRQ，Interrupt Request）。中断是硬件或软件向处理器发送的一种信号，要求处理器暂时停止当前的执行流程，转而处理特定的事件或任务。处理完中断后，处理器会继续执行之前的任务，需要用到LIDT和LGDT指令加载中断描述符表和全局描述符表，然后由int 42指令触发中断
其他用于hook的中断指令：
```php
int3 (0xcc)：会导致SIGTRAP
...