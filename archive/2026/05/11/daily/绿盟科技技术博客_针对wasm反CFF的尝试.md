---
title: 针对wasm反CFF的尝试
url: https://blog.nsfocus.net/%e9%92%88%e5%af%b9wasm%e5%8f%8dcff%e7%9a%84%e5%b0%9d%e8%af%95/
source: 绿盟科技技术博客
date: 2026-05-11
fetch_date: 2026-05-12T05:37:42.774264
---

# 针对wasm反CFF的尝试

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

# 针对wasm反CFF的尝试

### 针对wasm反CFF的尝试

[2026-05-11](https://blog.nsfocus.net/%E9%92%88%E5%AF%B9wasm%E5%8F%8Dcff%E7%9A%84%E5%B0%9D%E8%AF%95/ "针对wasm反CFF的尝试")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 33

☆ 背景介绍

参看

《WEB前端逆向TS PES NALU解密》
https://scz.617.cn/web/202408231518.txt

文中提及h5.worker.wasm，某些解密算法在wasm中实现。逆向工程发现，该wasm用
Emscripten开发所得，且被实施过”控制流平坦化”，比如func54\_vodplay。

想反CFF，再理解func54\_vodplay的逻辑。这是两年前搞wasm逆向工程时冒出来的想
法，当时没有这方面经验，未展开，只在Chrome F12中动态调试过该函数。

据说Angr可直接模拟执行wasm，但不如模拟执行ELF成熟，未求证，未实践。

有种变通方案，用wasm2c得到.c，编译出.o，用Angr模拟执行.o，对.o反CFF。

☆ 准备工作

1) wasm -> c

wasm2c -o h5\_worker.c h5.worker.wasm

上述命令可得到h5\_worker.c、h5\_worker.h。比较wasm2c 1.0.34与1.0.36的输出，
有差别，但单就所关心的w2c\_h50x2Eworker\_0x5Fvodplay\_0()，完全一样。

2) c -> o

将h5\_worker.c编译成h5\_worker\_pub.o。

3) 反编译.o

用反编译工具分析h5\_worker\_pub.o。一般来说，从.c到.o，再反汇编、反编译，不
会提供增益信息，相反，可能损失信息。当初这么干，主要是为借助反编译工具的符
号改名、交叉引用、Findcrypt或Signsrch插件，正是这样注意到TEA算法。

wasm-objdump -j Export -x h5.worker.wasm | less

查看wasm导出表，对h5\_worker.c/h5\_worker\_pub.o中若干函数进行简化表述

func54\_vodplay w2c\_h50x2Eworker\_0x5Fvodplay\_0
func121\_malloc w2c\_h50x2Eworker\_f121
func123\_memcpy w2c\_h50x2Eworker\_0x5Fmemcpy\_0
func30 w2c\_h50x2Eworker\_f30
func120\_free w2c\_h50x2Eworker\_0x5Ffree\_0
func77 w2c\_h50x2Eworker\_f77
func52 w2c\_h50x2Eworker\_f52
func125\_memset w2c\_h50x2Eworker\_0x5Fmemset\_0
func60\_TEA w2c\_h50x2Eworker\_f60
func59 w2c\_h50x2Eworker\_f59
func58\_TEA w2c\_h50x2Eworker\_f58
func40 w2c\_h50x2Eworker\_f40
func114 w2c\_h50x2Eworker\_f114

在反编译工具中查看func54\_vodplay，伪代码约1925行，大量嵌套的while、if以及
状态变量，表明其被实施过”控制流平坦化”。

完整测试用例

https://scz.617.cn/web/202604271701.7z

☆ h5\_worker\_cff\_pub.py

————————————————————————–
#!/usr/bin/env python
# -\*- coding: cp936 -\*-

#
# h5\_worker\_cff\_pub.py
#

import logging
import collections
import keystone
import angr, claripy

def get\_block\_from\_ea ( ea ) :
f = ida\_funcs.get\_func( ea )
if not f :
assert False
blocks = ida\_gdl.FlowChart( f )
for block in blocks :
if block.start\_ea <= ea < block.end\_ea :
return block
assert False

def set\_block\_color ( ea, bg\_color=0xffcc33 ) :
block = get\_block\_from\_ea( ea )
f = ida\_funcs.get\_func( block.start\_ea )
if not f :
assert False
node\_info = ida\_graph.node\_info\_t()
node\_info.bg\_color \
= bg\_color
ida\_graph.set\_node\_info( f.start\_ea, block.id, node\_info, ida\_graph.NIF\_BG\_COLOR )

def set\_insn\_color ( ea, color=0x00ffff ):
ida\_nalt.set\_item\_color( ea, color )

def get\_dispatchers ( addr ) :
dispatchers = set()
queue = collections.deque()
block = get\_block\_from\_ea( addr )
queue.append( ( block, [] ) )
while len( queue ) > 0 :
block, path = queue.popleft()
if block.start\_ea in path :
dispatchers.add( block.start\_ea )
continue
path = path + [block.start\_ea]
queue.extend( ( succ, path ) for succ in block.succs() )
dispatchers = list( dispatchers )
dispatchers.sort()
return dispatchers

def get\_ret\_block ( addr ) :
f = ida\_funcs.get\_func( addr )
if not f :
assert False
blocks = ida\_gdl.FlowChart( f )
for block in blocks :
last\_insn = ida\_bytes.prev\_head( block.end\_ea, block.start\_ea )
if last\_insn == ida\_idaapi.BADADDR :
continue
insn = ida\_ua.insn\_t()
if ida\_ua.decode\_insn( insn, last\_insn ) == 0 :
continue
if ida\_idp.is\_ret\_insn( insn ) :
return block.start\_ea
return None

def is\_block\_0 ( block ) :
block\_size = block.end\_ea – block.start\_ea
if block\_size == 0x52 :
return False
if block\_size < 0x31 :
return False
heads = list( idautils.Heads( block.start\_ea, block.end\_ea ) )
if len( heads ) < 2 :
return False
ea\_last = heads[-1]
ea\_prev = heads[-2]
insn\_last = ida\_ua.insn\_t()
if ida\_ua.decode\_insn( insn\_last, ea\_last ) <= 0 :
return False
if insn\_last.itype != ida\_allins.NN\_jmp :
return False
insn\_prev = ida\_ua.insn\_t()
if ida\_ua.decode\_insn( insn\_prev, ea\_prev ) <= 0 :
return False
if not ida\_idp.is\_call\_insn( insn\_prev ) :
return False
target\_ea = ida\_idaapi.BADADDR
op = insn\_prev.ops[0]
if op.type in [ida\_ua.o\_near, ida\_ua.o\_far] :
target\_ea = op.addr
if target\_ea == ida\_idaapi.BADADDR :
target\_ea = ida\_xref.get\_first\_fcref\_from( ea\_prev )
if target\_ea != ida\_idaapi.BADADDR :
name = ida\_name.get\_name(target\_ea)
if name :
clean\_name = name.lstrip( ‘\_.’ ).split( ‘@’ )[0]
if clean\_name == “i32\_store” :
return True
return False

def is\_block\_1 ( block ) :
heads = list( idautils.Heads( block.start\_ea, block.end\_ea ) )
if len( heads ) < 3 :
return False
ea\_last = heads[-1]
ea\_prev = heads[-2]
if ida\_bytes.get\_bytes( ea\_last, 2 ) != b’\x74\x05′ :
return False
insn\_prev = ida\_ua.insn\_t()
if ida\_ua.decode\_insn( insn\_prev, ea\_prev ) <= 0 :
return False
if insn\_prev.itype != ida\_allins.NN\_cmp :
return False
op0 = insn\_prev.ops[0]
op1 = insn\_prev.ops[1]
if op1.type != ida\_ua.o\_imm or op1.value != 0 :
return False
if op0.type not in ( ida\_ua.o\_displ, ida\_ua.o\_phrase ) :
return False
if op0.addr not in (-0x3c, -60, 0xc4, 0xffffffc4, 0xffffffffffffffc4) :
return False
for ea in reversed( heads[:-2] ) :
insn = ida\_ua.insn\_t()
if ida\_ua.decode\_insn( insn, ea ) <= 0 :
continue
if ida\_idp.is\_call\_insn( insn ) :
target\_ea = ida\_idaapi.BADADDR
op = insn.ops[0]
if op.type in [ida\_ua.o\_near, ida\_ua.o\_far] :
target\_ea = op.addr
if target\_ea == ida\_idaapi.BADADDR :
target\_ea = ida\_xref.get\_first\_fcref\_from( ea )
if target\_ea != ida\_idaapi.BADADDR :
name = ida\_name.get\_name( target\_ea )
if name :
clean\_name = name.lstrip( ‘\_.’ ).split( ‘@’ )[0]
if clean\_name.startswith( ( “i32\_load”, “i64\_load” ) ) :
return True
return False
return False

def get\_real\_block ( func\_ea ) :
f = ida\_funcs.get\_func( func\_ea )
if not f :
assert False
dispatchers \
= get\_dispatchers( func\_ea )
print( f”dispatchers[{len(dispatchers)}]:” )
for i, dispatcher in enumerate( dispatchers ) :
print( f”[{i}] {dispatcher:#x}” )
set\_block\_color( dispatcher, 0xff00ff )
real\_block\_list \
= [func\_ea, 0xbfe7a]
blocks = ida\_gdl.FlowChart( f )
for block in blocks :
if block.start\_ea in dispatchers :
continue
if is\_block\_0( block ) :
real\_block\_list.append( block.start\_ea )
elif is\_block\_1( block ) :
real\_block\_list.append( block.start\_ea )
real\_block\_list.sort()
ret\_block\_ea \
= get\_ret\_block( func\_ea )
assert ret\_block\_ea is not None
real\_block\_list.append( ret\_block\_ea )
print( [hex(x) for x in real\_block\_list] )
print( f”real\_block\_list[{len(real\_block\_list)}]:” )
for i, ea in enumerate( real\_block\_list ) :
set\_block\_color( ea )
print( f”[{i}] {ea:#x}” )
return real\_block\_list

def get\_info\_from\_jz\_angr ( state ) :
block = state.project.factory.block( state.addr, num\_inst=1 )
target\_false \
= state.addr + block.size
target\_true \
= None
for target in block.vex.consta...