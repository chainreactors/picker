---
title: pwnable.tw tcache_tear
url: https://www.o2oxy.cn/4226.html
source: print("")
date: 2024-12-02
fetch_date: 2025-10-06T19:36:35.099542
---

# pwnable.tw tcache_tear

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

# pwnable.tw tcache\_tear

作者: print("")
分类: [PWN](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/pwn)
发布时间: 2024-12-01 13:18
阅读次数: 1,075 次

## 这道题对于初学的我来说花了几个小时去理解。利用到的知识点如下：

**1.使用tcache dup实现任意地址写**

**2.使用****unsorted bin 双向链表特性获取到****unsorted bin 头部指针泄露、计算libc的基地址得到system地址**

**3.将free替换为system指针、获取到权限**

## 一、题目环境搭建

题目中给了一个libc 为2.27 的libc 又标明为tcache

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201111532.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201111532.jpg)

这里使用patchelf 进行替换libc

面对堆题的时候，本地上的libc往往无法满足需求(版本过高漏洞被修复)，

切换本地libc为题目给定libc，在切换之前需要准备。

<https://github.com/NixOS/patchelf>

<https://github.com/matrix1001/glibc-all-in-one>

首先需要弄清楚libc版本

strings libc.so |grep “GLIBC ”

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201111746.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201111746.jpg)

然后寻找对应的glibc版本。

```
cd glibc-all-in-one-master
python update_list
cat list
```

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201111849.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201111849.jpg)

下载指定的libc

建议把源换到阿里云

download 文件修改成阿里云的地址

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201111949.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201111949.jpg)

```
./download 2.27-3ubuntu1_amd64
```

下载完成之后查看一下。

```
ls libs/2.27-3ubuntu1_amd64
```

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201112110.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201112110.jpg)

设置libc的版本

```
patchelf --set-interpreter /home/pwn/glibc-all-in-one/libs/2.27-3ubuntu1_amd64/ld-2.27.so /home/pwn/桌面/head/tcache_tear/tcache_tear
patchelf --set-rpath  /home/pwn/glibc-all-in-one/libs/2.27-3ubuntu1_amd64 /home/pwn/桌面/head/tcache_tear/tcache_tear
ldd /home/pwn/桌面/head/tcache_tear/tcache_tear
    linux-vdso.so.1 (0x00007ffdfff8b000)
    libc.so.6 => /home/pwn/glibc-all-in-one/libs/2.27-3ubuntu1_amd64/libc.so.6 (0x00007fb353fb2000)
    /home/pwn/glibc-all-in-one/libs/2.27-3ubuntu1_amd64/ld-2.27.so => /lib64/ld-linux-x86-64.so.2 (0x00007fb3543a5000)
```

成功设置完libc的版本

但是gdb 调试的时候会有问题。暂时还没有得到解决

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241201112226.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241201112226.jpg)

## 二、题目解析

首先checksec 一下

```
tcache_tear$ checksec tcache_tear
[*] '/home/pwn/桌面/head/tcache_tear/tcache_tear'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x3fe000)
    RUNPATH:  b'/home/pwn/glibc-all-in-one/libs/2.27-3ubuntu1_amd64'
    FORTIFY:  Enabled
tcache_tear$

```

运行一下程序 一共就是3个选择。1个是申请内存、一个是释放、第三个是查看内容

```
tcache_tear$ ./tcache_tear
Name:1
$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :1
Size:1
Data:1
Done !
$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :3
Name :1$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :2
$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :
```

64位的程序。打开IDA发现是没有符号表的。然后自己改了一下让能看的清晰点

Main 函数

```
void __fastcall __noreturn main(__int64 a1, char **a2, char **a3)
{
  const char *name; // rdi
  __int64 v4; // rax
  unsigned int count; // [rsp-Ch] [rbp-Ch]

  set_clear();
  printf("Name:", a2);
  name = (const char *)&name_address;
  read_name((__int64)&name_address, 0x20u);
  count = 0;
  while ( 1 )
  {
    while ( 1 )
    {
      menu();
      v4 = read_num();
      if ( v4 != 2 )
        break;
      if ( count <= 7 )
      {
        name = (const char *)ptr_address;
        free(ptr_address);
        ++count;
      }
    }
    if ( v4 > 2 )
    {
      if ( v4 == 3 )
      {
        Infos();
      }
      else
      {
        if ( v4 == 4 )
          exit(0);
LABEL_14:
        name = "Invalid choice";
        puts("Invalid choice");
      }
    }
    else
    {
      if ( v4 != 1 )
        goto LABEL_14;
      Add(name, 32LL);
    }
  }
}
```

ADD函数

```
int Add()
{
  unsigned __int64 num; // rax
  int size; // [rsp-10h] [rbp-10h]

  printf("Size:");
  num = read_num();
  size = num;
  if ( num <= 0xFF )
  {
    ptr_address = malloc(num);
    printf("Data:");
    read_name((__int64)ptr_address, size - 16);
    LODWORD(num) = puts("Done !");
  }
  return num;
}
```

INFO函数

```
ssize_t sub_400B99()
{
  printf("Name :");
  return write(1, &name_address, 0x20uLL);
}
```

**分析漏洞点**

1、可以看到在Mian 函数中是只是free 了地址、但是没有free掉引用、这里就会出现UAF漏洞

```
 if ( v3 != 2 )
        break;
      if ( count <= 7 )
      {
        free(ptr_address);
        ++count;
      }
```

但是这有一个限制、就是count 最大只能7次。

2、在add 函数中。如果size 小于16 那么得到的结果就会为负数、那么此刻就可以实现栈溢出了

```
read_name((__int64)ptr_address, size - 16);
```

但是在此处是没用、可以演示一下

```
head$ gdb tcache_bak
pwndbg> r
Starting program: /home/pwn/桌面/head/tcache_bak
Name:n
$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :1
Size:1
Data:1222222222222222222222222222222
Done !
$$$$$$$$$$$$$$$$$$$$$$$
      Tcache tear
$$$$$$$$$$$$$$$$$$$$$$$
  1. Malloc
  2. Free
  3. Info
  4. Exit
$$$$$$$$$$$$$$$$$$$$$$$
Your choice :^C
Program received signal SIGINT, Interrupt.
__read_chk (fd=0, buf=0x7fffffffdf80, nbytes=23, buflen=<optimized out>) at read_chk.c:33
33	read_chk.c: 没有那个文件或目录.
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─────────────────────────────────[ REGISTERS ]──────────────────────────────────
 RAX  0xfffffffffffffe00
 RBX  0x400c90 ◂— push   r15
 RCX  0x7ffff7ef39cd (__read_chk+13) ◂— cmp    rax, -0x1000 /* 'H=' */
 RDX  0x17
 RDI  0x0
 RSI  0x7fffffffdf80 —▸ 0x400840 ◂— xor    ebp, ebp
 R8   0xd
 R9   0xd
 R10  0x400db6 ◂— pop    rcx /* 'Your choice :' */
 R11  0x246
 R12  0x400840 ◂— xor    ebp, ebp
 R13  0x7fffffffe0b0 ◂— 0x1
 R14  0x0
 R15  0x0
 RBP  0x7fffffffdfa0 —▸ 0x7fffffffdfc0 ◂— 0x0
 RSP  0x7fffffffdf68 —▸ 0x4009fb ◂— lea    rax, [rbp - 0x20]
 RIP  0x7ffff7ef39cd (__read_chk+13) ◂— cmp    rax, -0x1000 /* 'H=' */
───────────────────────────────────[ DISASM ]───────────────────────────────────
 ► 0x7ffff7ef39cd <__read_chk+13>    cmp    rax, -0x1000
   0x7ffff7ef39d3 <__read_chk+19>    ja     __read_chk+32 <__read_chk+32>
    ↓
   0x7ffff7ef39e0 <__read_chk+32>    mov    rdx, qword ptr [rip + 0xbd489]
   0x7ffff7ef39e7 <__read_chk+39>    neg    eax
   0x7ffff7ef39e9 <__read_chk+41>    mov    dword ptr fs:[rdx], eax
   0x7ffff7ef39ec <__read_chk+44>    mov    rax, -1
   0x7ffff7ef39f3 <__read_chk+51>    ret

   0x7ffff7ef39f4 <__read_chk+52>    push   rax
   0x7ffff7ef39f5 <__read_chk+53>    call   __chk_fail <__chk_fail>

   0x7ffff7ef39fa                    nop    word ptr [rax + rax]
   0x7ffff7ef3a00 <__pread_chk>      endbr64
───────────────────────────────────[ STACK ]────────────────────────────────────
00:0000│ rsp  0x7fffff...