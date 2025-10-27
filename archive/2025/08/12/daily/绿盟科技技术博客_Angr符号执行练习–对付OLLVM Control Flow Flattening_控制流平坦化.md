---
title: Angr符号执行练习–对付OLLVM Control Flow Flattening/控制流平坦化
url: https://blog.nsfocus.net/angr%e7%ac%a6%e5%8f%b7%e6%89%a7%e8%a1%8c%e7%bb%83%e4%b9%a0-%e5%af%b9%e4%bb%98ollvm-control-flow-flattening-%e6%8e%a7%e5%88%b6%e6%b5%81%e5%b9%b3%e5%9d%a6%e5%8c%96/
source: 绿盟科技技术博客
date: 2025-08-12
fetch_date: 2025-10-07T00:48:23.589369
---

# Angr符号执行练习–对付OLLVM Control Flow Flattening/控制流平坦化

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

# Angr符号执行练习–对付OLLVM Control Flow Flattening/控制流平坦化

### Angr符号执行练习–对付OLLVM Control Flow Flattening/控制流平坦化

[2025-08-11](https://blog.nsfocus.net/angr%E7%AC%A6%E5%8F%B7%E6%89%A7%E8%A1%8C%E7%BB%83%E4%B9%A0-%E5%AF%B9%E4%BB%98ollvm-control-flow-flattening-%E6%8E%A7%E5%88%B6%E6%B5%81%E5%B9%B3%E5%9D%A6%E5%8C%96/ "Angr符号执行练习–对付OLLVM Control Flow Flattening/控制流平坦化")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 677

创建: 2025-07-31 12:22
更新:

————————————————————————–

目录:

☆ 背景介绍
☆ hello.c
☆ hello\_fla
☆ hello\_fla\_patch.py
☆ IDAPython插件D810
1) 安装D810插件
2) 使用D810插件
3) 借助AI理解D810框架结构
☆ 后记

————————————————————————–

☆ 背景介绍

参看

————————————————————————–
Control Flow Flattening (CFF)
https://github.com/obfuscator-llvm/obfuscator/wiki/Control-Flow-Flattening

Deobfuscation: recovering an OLLVM-protected program – Francis Gabriel [2014-12-04]
https://blog.quarkslab.com/deobfuscation-recovering-an-ollvm-protected-program.html
————————————————————————–

控制流平坦化将正常控制流转换成状态变量驱动，夹杂状态变量混淆，使得IDA F5结
果非人类可读，但不影响原有代码逻辑，顶多有些性能损耗。CFF目的是对抗静态分
析。

本文以学习angr进阶用法为目的，借CFF反混淆为靶标。

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

clang -pipe -O0 -s -mllvm -passes=fla -o hello\_fla hello.c

用某版OLLVM启用fla编译，得到hello\_fla。

完整测试用例打包

https://scz.617.cn/unix/202507311222.txt
https://scz.617.cn/unix/202507311222.7z

☆ hello\_fla

$ file -b hello\_fla
ELF 64-bit LSB executable, x86-64, …, stripped

IDA64反汇编hello\_fla

————————————————————————–
\_\_int64 \_\_fastcall main(int a1, char \*\*a2, char \*\*a3)
{
int v3;
int v5;
unsigned int v6;
unsigned int v7;
unsigned int v8;

v8 = 0;
v5 = 0xF2AB2D56;
while ( 1 )
{
while ( v5 == 0xA6509F46 )
{
fprintf(stderr, “Usage: %s <num>\n”, \*a2);
v8 = -1;
v5 = 0xE926118E;
}
if ( v5 == 0xE926118E )
break;
if ( v5 == 0xF2AB2D56 )
{
v3 = 0x64B7B86A;
if ( a1 < 2 )
v3 = 0xA6509F46;
v5 = v3;
}
else
{
v7 = strtoul(a2[1], 0LL, 0);
v6 = sub\_401270(v7);
fprintf(stdout, “n=%#x ret=%#x\n”, v7, v6);
v8 = 0;
v5 = 0xE926118E;
}
}
return v8;
}

\_\_int64 \_\_fastcall sub\_401270(int a1)
{
int v1;
int v2;
int v3;
int v5;
unsigned int v6;
int v7;

v7 = a1 & 3;
v6 = 0;
v5 = 0x1D861884;
while ( v5 != 0x95AD57E0 )
{
switch ( v5 )
{
case 0xBBF4F2F8:
v6 = (a1 + 3) \* (a1 & 0xBAAAD0BF);
v5 = 0xCE9DE31;
break;
case 0xC915711E:
v3 = 0x54BE0661;
if ( v7 == 2 )
v3 = 0xD6927C4E;
v5 = v3;
break;
case 0xD6927C4E:
v6 = (a1 | 4) \* (a1 ^ 0xBAAAD0BF);
v5 = 0x5B1C3258;
break;
case 0xCE9DE31:
v5 = 0x95AD57E0;
break;
case 0x134D92DC:
v6 = (a1 ^ 2) \* (a1 | 0xBAAAD0BF);
v5 = 0x95AD57E0;
break;
case 0x1D861884:
v1 = 0x1F74CBC8;
if ( (a1 & 3) == 0 )
v1 = 0x134D92DC;
v5 = v1;
break;
case 0x1F74CBC8:
v2 = 0xC915711E;
if ( v7 == 1 )
v2 = 0xBBF4F2F8;
v5 = v2;
break;
case 0x54BE0661:
v6 = (a1 & 5) \* (a1 – 0x45552F41);
v5 = 0x5B1C3258;
break;
default:
v5 = 0xCE9DE31;
break;
}
}
return v6;
}
————————————————————————–

F5的伪代码没必要深究，看个大概即可。

☆ hello\_fla\_patch.py

这是对付hello\_fla的完整代码，演示性质，非通用实现。

hello\_fla\_patch.py实际源自

https://github.com/cq674350529/deflat/blob/master/flat\_control\_flow/deflat.py

am\_graph模块实际源自

https://github.com/angr/angr-management/blob/master/angrmanagement/utils/graph.py

————————————————————————–
#!/usr/bin/env python
# -\*- encoding: utf-8 -\*-

import sys, collections
import angr, claripy, pyvex
import am\_graph

def get\_func\_from\_addr ( proj, addr ) :
try :
return proj.kb.functions.get\_by\_addr( addr )
except KeyError :
return proj.kb.functions.floor\_func( addr )

#
# threshold是所有”有效块”中最小字节长度
#
def get\_relevant\_nop\_nodes ( supergraph, pre\_dispatcher\_node, prologue\_node, retn\_node, threshold ) :
#
# relevant\_nodes = list( supergraph.predecessors( pre\_dispatcher\_node ) )
#
relevant\_nodes = []
nop\_nodes = []
for node in supergraph.nodes() :
if node.addr in ( prologue\_node.addr, retn\_node.addr, pre\_dispatcher\_node.addr ) :
continue
#
# 靠threshold快速过滤、排除”非有效块”
#
if supergraph.has\_edge( node, pre\_dispatcher\_node ) and node.size > threshold :
relevant\_nodes.append( node )
else :
nop\_nodes.append( node )
return relevant\_nodes, nop\_nodes

#
# 通过符号执行寻找下一跳
#
# 若CFF的状态转换变量在某个case中不是简单赋值，而是与当前case值进行计算所
# 得，下面的符号执行方案可能有问题，涉及如何初始化的问题。
#
def symbolic\_execution ( proj, keep\_blocks, start\_addr, hook\_addrs, set\_value=None ) :

def retn\_procedure ( state ) :
#
# ip = state.solver.eval( state.regs.ip )
# proj.unhook( ip )
#
proj.unhook( state.addr )
return

def statement\_inspect ( state ) :
#
# state.scratch.irsb是正在处理的IR SuperBlock (IRSB)的VEX IR表示。
# 一个IRSB包含一系列IR语句。
#
# 当’statement’类型的检查点触发时，在state.inspect.statement中存储
# 当前正在处理的IR语句的索引。
#
# state.scratch.irsb.statements[]是个数组
# state.inspect.statement是int，是个索引
#
# 每个IR语句可能包含一个或多个表达式(expressions)
#
expressions = list( state.scratch.irsb.statements[state.inspect.statement].expressions )
#
# if…then…else
#
if len( expressions ) != 0 and isinstance( expressions[0], pyvex.expr.ITE ) :
#
# state.scratch.temps[]用于存储VEX IR临时变量值
#
# ITE表达式的cond属性代表条件表达式本身。下面这个值决定ITE表达
# 式走then分支还是else分支。
#
state.scratch.temps[expressions[0].cond.tmp] = set\_value
state.inspect.\_breakpoints[‘statement’] = []

if hook\_addrs :
for addr in hook\_addrs :
#
# 假设call指令占5字节
#
proj.hook( addr, retn\_procedure, length=5 )

init\_state = proj.factory.blank\_state(
addr = start\_addr,
add\_options = {
angr.options.SYMBOL\_FILL\_UNCONSTRAINED\_MEMORY,
angr.options.SYMBOL\_FILL\_UNCONSTRAINED\_REGISTERS,
angr.options.BYPASS\_UNSUPPORTED\_SYSCALL,
},
remove\_options = {
angr.options.LAZY\_SOLVES,
}
)
if set\_value is not None :
init\_state.inspect.b( ‘statement’, when=angr.BP\_BEFORE, action=statement\_inspect )

sm = proj.factory.simulation\_manager( init\_state )
sm.step()
while len( sm.active ) > 0 :
for state in sm.active :
if state.addr in keep\_blocks :
return state.addr
sm.step()

return None

#
# 恢复控制流
#
def get\_flow ( proj, prologue\_node, relevant\_nodes, retn\_node ) :

#
# 本例实测下来，target不含序言块也可以，但稳妥起见，还是含序言块
#
symbolic\_execution\_target \
= [prologue\_node]
symbolic\_execution\_target.extend( relevant\_nodes )

keep\_blocks = [node.addr for node in relevant\_nodes]
#
# keep\_blocks包含返回块，不包含主分发器、预处理器
#
keep\_blocks.extend(...