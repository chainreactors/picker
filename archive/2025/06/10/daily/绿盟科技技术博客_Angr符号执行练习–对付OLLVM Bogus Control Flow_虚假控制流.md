---
title: Angr符号执行练习–对付OLLVM Bogus Control Flow/虚假控制流
url: https://blog.nsfocus.net/angr-4/
source: 绿盟科技技术博客
date: 2025-06-10
fetch_date: 2025-10-06T22:55:57.156584
---

# Angr符号执行练习–对付OLLVM Bogus Control Flow/虚假控制流

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

# Angr符号执行练习–对付OLLVM Bogus Control Flow/虚假控制流

### Angr符号执行练习–对付OLLVM Bogus Control Flow/虚假控制流

[2025-06-09](https://blog.nsfocus.net/angr-4/ "Angr符号执行练习–对付OLLVM Bogus Control Flow/虚假控制流")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 1,886

目录:

☆ 背景介绍
☆ hello.c
☆ hello\_bcf
☆ hello\_bcf\_patch.py
☆ get\_cond\_jmp\_list的技术原理

————————————————————————–

☆ 背景介绍

OLLVM支持”Bogus Control Flow/虚假控制流”。启用bcf编译源码，生成的二进制用
IDA反汇编时，会看到许多实际执行时永不可达的基本块。冗余的不可达块对IDA F5
带来干扰，肉眼看不出原始代码逻辑，同时不影响实际执行逻辑。bcf目的就是对抗
静态分析。

OLLVM项目提供过一张示意图

————————————————————————–
原始流程

entry
|
\_\_\_\_\_\_v\_\_\_\_\_\_
| original |
|\_\_\_\_\_\_\_\_\_\_\_\_\_|
|
v
return
————————————————————————–
启用bcf之后的流程

entry
|
\_\_\_\_v\_\_\_\_\_
|condition\*| (false)
|\_\_\_\_\_\_\_\_\_\_|—-+
(true)| |
| |
\_\_\_\_\_\_v\_\_\_\_\_\_ |
+–>| original\* | |
| |\_\_\_\_\_\_\_\_\_\_\_\_\_| (true)
| (false)| !———–> return
| \_\_\_\_\_\_v\_\_\_\_\_\_ |
| | altered |<–!
| |\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\_\_\_\_\_\_\_\_\_\_|
————————————————————————–

上图那些条件判断，实际恒为true，执行时沿true前进，与原始逻辑无异。但静态分
析时，受false干扰，并不知道false路径永不可达。

参看

————————————————————————–
利用angr符号执行去除虚假控制流 – 34r7hm4n [2021-02-10]
https://bbs.kanxue.com/thread-266005.htm
————————————————————————–

作者用「angr符号执行」识别目标程序中不可达块，静态Patch目标程序，将不可达
块NOP化。虽然IDA反汇编结构图仍然显乱，但F5比较智能，已能去干扰，显示出原始
逻辑。

————————————————————————–
NOP化之后的流程

entry
|
\_\_\_\_v\_\_\_\_\_
|condition\*| (false)
|\_\_\_\_\_\_\_\_\_\_|—-+
(true)| |
| |
\_\_\_\_\_\_v\_\_\_\_\_\_ |
+–>| original\* | |
| |\_\_\_\_\_\_\_\_\_\_\_\_\_| (true)
| (false)| !———–> return
| \_\_\_\_\_\_v\_\_\_\_\_\_ |
| | nop |<–!
| |\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\_\_\_\_\_\_\_\_\_\_|
————————————————————————–

假设angr符号执行能精确识别干扰性质的条件跳转指令，我选择将所有干扰性质的条
件跳转指令静态Patch成无条件跳转指令，直接跳向相应可达块；此方案本质上等价
于NOP化不可达块。

————————————————————————–
JMP化之后的流程

entry
|
\_\_\_\_v\_\_\_\_\_
|condition\*|
|\_\_\_\_\_\_\_\_\_\_|
(jmp)|
|
\_\_\_\_\_\_v\_\_\_\_\_\_
+–>| original\* |
| |\_\_\_\_\_\_\_\_\_\_\_\_\_| (jmp)
| !———–> return
| \_\_\_\_\_\_ \_\_\_\_\_\_
| | altered |
| |\_\_\_\_\_\_\_\_\_\_\_\_\_|
|\_\_\_\_\_\_\_\_\_\_|
————————————————————————–

本文以学习angr进阶用法为目的，借bcf反混淆为靶标，演示JMP化思路。

$ pip3 show angr | grep Version
Version: 9.2.125.dev0

☆ hello.c

————————————————————————–
#include <stdio.h>
#include <stdlib.h>

static unsigned int foo ( unsigned int n )
{
unsigned int mod = n % 4;
unsigned int ret = 0;

if ( mod == 0 )
{
ret = ( n | 0xbaaad0bf ) \* ( 2 ^ n );
}
else if ( mod == 1 )
{
ret = ( n & 0xbaaad0bf ) \* ( 3 + n );
}
else if ( mod == 2 )
{
ret = ( n ^ 0xbaaad0bf ) \* ( 4 | n );
}
else
{
ret = ( n + 0xbaaad0bf ) \* ( 5 & n );
}
return ret;
}

int main ( int argc, char \* argv[] )
{
unsigned int n,
ret;

if ( argc < 2 )
{
fprintf( stderr, “Usage: %s <num>\n”, argv[0] );
return -1;
}
n = (unsigned int)strtoul( argv[1], NULL, 0 );
ret = foo( n );
fprintf( stdout, “n=%#x ret=%#x\n”, n, ret );
return 0;
}
————————————————————————–

clang -pipe -O0 -s -mllvm -passes=bcf -o hello\_bcf hello.c

用某版OLLVM启用bcf编译，得到hello\_bcf。

完整测试用例打包

https://scz.617.cn/unix/202505281714.txt
https://scz.617.cn/unix/202505281714.7z

☆ hello\_bcf

$ file -b hello\_bcf
ELF 64-bit LSB executable, x86-64, …, stripped

IDA64反汇编hello\_bcf

————————————————————————–
\_\_int64 \_\_fastcall main(int a1, char \*\*a2, char \*\*a3)
{
…
v24 = a1;
v25 = a2;
//
// unk\_4040??位于.bss，实际运行时初始化为0。下列布尔值恒false
//
if ( ((unk\_404098 \* (unk\_404098 + 1)) & 1) != 0 && unk\_4040F8 >= 10 )
//
// 此跳转永不发生
//
goto LABEL\_11;
while ( 1 )
{
v3 = v25;
v19 = (unsigned int \*)(&v17 – 2);
v20 = (const char \*\*\*)(&v17 – 2);
v21 = (unsigned int \*)(&v17 – 2);
v22 = (unsigned int \*)(&v17 – 2);
\*((\_DWORD \*)&v17 – 4) = 0;
v17 = v3;
v23 = (int)v3 < 2;
//
// 下列布尔值恒true
//
if ( ((unk\_404120 \* (unk\_404120 + 1)) & 1) == 0 || unk\_4040C4 < 10 )
//
// 此break必发生
//
break;
LABEL\_11:
//
// 永可不达的基本块
//
LODWORD(v17) = v24;
\*(&v17 – 2) = v25;
}
if ( v23 )
{
//
// 下列布尔值恒false
//
if ( ((unk\_40411C \* (unk\_40411C + 1)) & 1) != 0 && unk\_4040C0 >= 10 )
//
// 此跳转永不发生
//
goto LABEL\_12;
while ( 1 )
{
fprintf(stderr, “Usage: %s <num>\n”, \*\*v20);
\*v19 = -1;
//
// 下列布尔值恒true
//
if ( ((unk\_404110 \* (unk\_404110 + 1)) & 1) == 0 || unk\_4040B8 < 10 )
//
// 此break必发生
//
break;
LABEL\_12:
//
// 永可不达的基本块
//
fprintf(stderr, “Usage: %s <num>\n”, \*\*v20);
\*v19 = -1;
}
}
else
{
…
}
do
v18 = \*v19;
//
// 下列布尔值恒false
//
while ( ((unk\_4040E8 \* (unk\_4040E8 + 1)) & 1) != 0 && unk\_404138 >= 10 );
return v18;
}
————————————————————————–

F5的伪代码没必要深究，看个大概即可。

☆ hello\_bcf\_patch.py

这是对付hello\_bcf的完整代码，演示性质，非通用实现。

————————————————————————–
#!/usr/bin/env python
# -\*- encoding: utf-8 -\*-

import sys, logging
import angr

def get\_func\_from\_addr ( proj, addr ) :
try :
return proj.kb.functions.get\_by\_addr( addr )
except KeyError :
return proj.kb.functions.floor\_func( addr )

class PrivateHelper ( angr.ExplorationTechnique ) :

def \_\_init\_\_ ( self, cond\_jmp\_set, hooksub, hooksubset ) :
super().\_\_init\_\_()
self.cond\_jmp\_set = cond\_jmp\_set
self.hooksub = hooksub
self.hooksubset = hooksubset

def successors ( self, sm, state, \*\*kwargs ) :
if self.hooksub and 0 != state.callstack.ret\_addr :
proj = state.project
target = state.addr
if target not in self.hooksubset :
proj.hook( target, angr.SIM\_PROCEDURES[‘stubs’][‘ReturnUnconstrained’](), replace=True )
self.hooksubset.add( target )
ret = sm.successors( state, \*\*kwargs )
if not self.hooksub or 0 == state.callstack.ret\_addr :
i = len( ret.all\_successors )
j = len( ret.successors )
k = len( ret.unsat\_successors )
if i == 2 and j == 1 and k == 1 :
j\_from = ret.successors[0].history.jump\_source
j\_to = ret.successors[0].addr
self.cond\_jmp\_set.add( ( j\_from, j\_to ) )
return ret

def get\_cond\_jmp\_list ( proj, func, hooksub, hooksubset ) :
cond\_jmp\_set = set()
init\_state = proj.factory.blank\_state(
addr = func.addr,
add\_options = {
angr.options.SYMBOL\_FILL\_UNCONSTRAINED\_MEMORY,
angr.options.SYMBOL\_FILL\_UNCONSTRAINED\_REGISTERS,
angr.options.BYPASS\_UNSUPPORTED\_SYSCALL,
}
)
sm = proj.factory.simulation\_manager( init\_state )
sm.use\_technique( angr.exploration\_techniques.DFS() )
sm.use\_technique( PrivateHelper( cond\_jmp\_set, hooksub=hooksub, hooksubset=hooksubset ) )
sm.run()
return sorted( cond\_jmp\_set )

def patch\_buf ( proj, buf, cond\_jmp\_list ) :
#
# 本例简单处理，假设都能用EB短跳转
#
for j\_from, j\_to in cond\_jmp\_list :
j\_off = j\_to – ( j\_from + 2 )
assert j\_off <= 0x7f and j\_off >= -0x80
off = proj.loader.main\_object.addr\_to\_offset( j\_from )
buf[off:off+2] \
= bytes( [0xeb, j\_off] )

def dosth ( proj, buf, addr, hooksub, hooksubset ) :
func = get\_func\_from\_addr( proj, addr )
cond\_jmp\_list = get\_cond\_jmp\_list( proj, func, hooksub, hooksubset )
print( f’cond\_jmp\_list[{len(cond\_jmp\_list)}]’ )
for j in cond\...