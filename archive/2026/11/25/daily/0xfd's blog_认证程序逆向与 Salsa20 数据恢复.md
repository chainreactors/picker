---
title: 认证程序逆向与 Salsa20 数据恢复
url: https://lucifer11.xyz/knowledge/crypto/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:56.056982
---

# 认证程序逆向与 Salsa20 数据恢复

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [Salsa20 参数与认证比较](#Salsa20-%E5%8F%82%E6%95%B0%E4%B8%8E%E8%AE%A4%E8%AF%81%E6%AF%94%E8%BE%83)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# 认证程序逆向与 Salsa20 数据恢复

发表于
2026-11-25

分类于

[二进制安全](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/)
，
[逆向与密码](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/%E9%80%86%E5%90%91%E4%B8%8E%E5%AF%86%E7%A0%81/)

阅读次数：

本文字数：
1.4k

阅读时长 ≈
5 分钟

Rauth 的认证比较依赖加密后的输入。本章保留条件跳转分析和实际密钥恢复两个过程，核对 Salsa20 的 key、nonce、rounds 与字节序，最后以程序比较结果验证。

Rauth 的认证比较依赖加密后的输入。本章保留条件跳转分析和实际密钥恢复两个过程，核对 Salsa20 的 key、nonce、rounds 与字节序，最后以程序比较结果验证。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/crypto/source.md)
展开全部技术记录

## 分析重点

修改条件跳转可以观察后续代码，真正的输入验证仍要恢复数据关系。

SIMD 数据显示和整数显示之间的字节序差异会影响密钥提取。

原调试截图、提取值与脚本保持一一对应。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [Salsa20 参数与认证比较](#case-rauth) | rauth | 逆向、Salsa20、字节序 |

## Salsa20 参数与认证比较

先定位条件跳转，再恢复密钥、nonce 和字节序，最后验证真正的认证输入。原文对补丁绕过与密码恢复的不同结果均保留。

来源 rauth · 原记录 2021-11-20 · 5 个代码块 · 9 处图片引用

查看分析过程、攻击步骤与完整代码

#### step1

You should always check the file type first with a tool like Detect it Easy. Also, make sure to run these in a sandboxed environment. In this case it was a Linux executable — an ELF file. By giving it the correct permissions, you can run it.

Although, on the surface, it looks like a regular password bypass challenge, this one has a few tricks up its sleeve.

#### Initial debugging

My tool of choice for this challenge was IDA Free, but you can use something like Ghidra or Radare2. Take note that, in IDA, if you wish to debug an interactive program and need input/output, you should open it in a terminal with this command:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cat | ./ida64 ``` |

After importing the file, we can dive into the decompiled code. We need to find the “main” function, and try and make sense of the program structure from there.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth.png)

The first time we run, we can already start annotating (as seen in purple), what each function does.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth1.png)

#### Challenge complete?

After debugging for a few minutes, we come to the conclusion that there are two jumps — jump if zero, to be more precise — that keep us from bypassing the verification. We’ll invert those assembly instructions to JNZ — jump if not zero.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth2.png)

And… voilá. Challenge complete… Or so it would seem.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth3.png)

As expected, there’s a twist. This is a mock development environment. If we want to have any chance at getting the flag, we’ll have to get it from the production environment — the server that was mentioned at the start.

This means we need to find out the actual password, not just bypass it. So let’s go back and retrace our steps.

#### Cryptography 101

But how far do we need to go back? We need to find out where and how the password we enter is verified.
Shortly after we enter our password, we can find this function:

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth4.png)

Notice how it says “Salsa20”. I’ve heard this term before to describe a cryptographic algorithm.

If we check Wikipedia, or some other similar source, we can verify Salsa20 is a variation of the Salsa stream cipher algorithm with 20 rounds.

In Wikipedia’s Salsa article, you can find the following table:

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth5.png)

This essentially means that, before the Salsa algorithm can be applied to encrypt a piece of data, it needs to create a matrix with the following information. So, ideally we should be able to find and easily identify each individual piece in memory. Let’s take a look at our registers:

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth6.png)

There it is! The Salsa20 function we paused the debugging at, was actually responsible for generating this matrix. All that was left to do was to find the right register containing the information, in this case it was the RSP register.

So from: expaef39f4f20e76e33bnd 3d4c270a32-byd25f4db338e81b10te k

We can extract the following components:

* Key: ef39f4f20e76e33bd25f4db338e81b10
* Nonce: d4c270a3

So now, we have all we need to decrypt the password data, except for the encrypted password data itself. Bummer. Here’s where the next challenge lies.

#### Single Challenge Multiple Problems

As the program has the Salsa matrix fully built, we can deduce that it will soon enough execute its algorithm over the password we entered and compare its encrypted data to the actual encrypted passsword itself. So let’s explore the decompiled code a little more.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth7.png)

Alright, somewhere along the next few lines, we see some pointer arithmetic and, afterwards, two comparisons. One of these, should compare both encrypted keys and validate our authentication.

If we run the next few lines and pay attention to the general registers, nothing will show up. The tip is the “xmm” keyword that keeps popping up.

These XMM registers are actually specific registers for Streaming SIMD Extensions, or SSE, for short. An Intel designed set of additional CPU instructions that rely on specific registers — XMM 0 through 15. These are used in order to achieve Instruction Level Parallelism, by executing some operation over a vector of values.

If we take a look a few lines back, we can actually detect a few xmm constants.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/rauth8.png)

The ones we need to pay attention to are the first two.

* 55EF11039CC0: 0F331CBA656F5D958D5A829A3B15F0505h
* 55EF11039CD0: 0F91BAD626FB63EE372EC9DC9312A4324h

We can remove the “h” at the end, which only tells us the value is in hexadecimal, meaning each byte is represented by two letters/numbers. So let’s separate the value by bytes as well. While we’re at it, we’ll also remove the initial 0 that isn’t doing anything there.

* 55EF11039CC0: F3 31 CB A6 56 F5 D9 58 D5 A8 29 A3 B1 5F 05 05
* 55EF11039CD0: F9 1B AD 62 6F B6 3E E3 72 EC 9D C9 31 2A 43 24

The problem now is that IDA was representing the value in big-endian (most significant bytes at the end), while x86 memory is in little-endian (most significant bytes at the start). This means that we need to invert the bytes, but not the string itself, as the byte pairs are self-contained.

What we’re left with is this:

* 55EF11039CC0: 05 05 5F B1 A3 29 A8 D5 58 D9 F5 56 A6 CB 31 F3
* 55EF11039CD0: 24 43 2A 31 C9 9D EC 72 E3 3E B6 6F 62 AD 1B F9

Since the data is still encoded and encrypted, we need to create a small program to decode and then decrypt it and verify if we’ve found the encrypted password. I chose to write a small program in Python using Spyder, but you can use whatever you feel most comfortable with.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` from Cryptodome.Cipher import Salsa20 import codecs  def UnHex(s):     return codecs.decode(s.replace(" ", "")...