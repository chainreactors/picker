---
title: SECCON 2024：动态二进制插桩trace 破解函数式编程混淆
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587582&idx=1&sn=a0c75ea7c6980a2c5993cee7693ac0e9&chksm=b18c213486fba822b28c8f00c676f6d418df6aa83af0e5467ca1e3da806cd291fe0af57a3d28&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-21
fetch_date: 2025-10-06T19:38:36.120201
---

# SECCON 2024：动态二进制插桩trace 破解函数式编程混淆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FLwf0ibWjyRXdhX5Ph4UU8KGiaMhtEM9tRBGg1fCUAXuqGsHSxI6MeqQYZBCPyyjhqqicUJElfkJjbA/0?wx_fmt=jpeg)

# SECCON 2024：动态二进制插桩trace 破解函数式编程混淆

SleepAlone

看雪学苑

这道F is for flag（正餐），卡的时间比较久，一开始打算硬逆奈何功力不够（我知道有其他大佬硬逆做出来的），最后选择使用trace工具碰碰运气，然后又在frida和pyda之间来回反复，frida的hook效果不尽人意，最终选择pyda。

pyda是一款动态二进制插桩工具，可以通过编写python代码的方式实现hook非常方便。

`官网介绍：Pyda combines Dynamorio-based instrumentation with a CPython interpreter, allowing you to write hooks in Python that directly manipulate registers/memory in the target, without going through GDB or ptrace.`

https://github.com/ndrewh/pyda

## 题目背景

经典的flag检查：

```
/f
FLAG: SECCON{fUnCt10n4l_pRoGr4mM1n6_1s_pR4c7iC4lLy_a_pUr3_0bfu5c4T1oN}
"Correct"
```

##

#

```
一

ida 逆向初探
```

##

题目由c++编写，ida打开点开main函数，会发现main函数里面发现里面有大量的std:variant, lambda闭包调用，并且其他函数都是被mangle过的。

```
  v84 = 0;
  std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::variant<unsigned int,void,void,unsigned int,void>(
    (__int64)v106,
    (__int64)&v84);
  v83 = 0xB7E9A2A4;
  std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::variant<unsigned int,void,void,unsigned int,void>(
    (__int64)v105,
    (__int64)&v83);
  main::{lambda(std::variant<unsigned int,std::string,std::shared_ptr<Cons>>,std::variant<unsigned int,std::string,std::shared_ptr<Cons>>)#19}::operator()(
    (__int64)v107,
    (__int64)&v78,
    (__int64)v105,
    (__int64)v106,
    v3,
    v4);
```

在lamba#19中又有std::make\_shared, std::variant,std::shared\_ptr

```
    std::make_shared<Cons,std::variant<unsigned int,std::string,std::shared_ptr<Cons>> &,std::variant<unsigned int,std::string,std::shared_ptr<Cons>> &>(
        (__int64)v7,
        a3,
        a4);
    std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::variant<std::shared_ptr<Cons>,void,void,std::shared_ptr<Cons>,void>(
      a1,
      (__int64)v7);
    std::shared_ptr<Cons>::~shared_ptr(v7);
```

std::make\_shared经过一层层调用，最终会call到Cons::Cons，将v83（0xB7E9A2A4）存到cons里，后面的逻辑以此类推。

```
    v5 = operator new(0x50uLL, a1);
    v6 = std::forward<std::variant<unsigned int,std::string,std::shared_ptr<Cons>> &>(a3);
    std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::variant((__int64)v11, v6);
    v7 = std::forward<std::variant<unsigned int,std::string,std::shared_ptr<Cons>> &>(a2);
    std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::variant((__int64)v10, v7);
    Cons::Cons(v5, (__int64)v10, (__int64)v11);
    std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::~variant((__int64)v10);
    std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::~variant((__int64)v11);
```

到这里分析还算顺利，知道跟到这个std::function()(lambda#1)

```
std::function<std::variant<unsigned int,std::string,std::shared_ptr<Cons>> ()(void)>::function<main::{lambda(void)#1},void>(
    (std::_Function_base *)v127,
    (__int64)v95);
```

每一个std:function至少需要三层调用才能到达真实逻辑：

```
// level 1
*((_QWORD *)a1 + 3) = std::_Function_handler<std::variant<unsigned int,std::string,std::shared_ptr<Cons>> ()(void),main::{lambda(void)#1}>::_M_invoke;

//level 2
std::__invoke_r<std::variant<unsigned int,std::string,std::shared_ptr<Cons>>,main::{lambda(void)#1} &>(a1, pointer);

//level 3
std::__invoke_impl<std::variant<unsigned int,std::string,std::shared_ptr<Cons>>,main::{lambda(void)#1} &>(a1, v2);

//level 4
main::{lambda(void)#1}::operator()(a1, v2);

//level5
v8 = __readfsqword(0x28u);
  v2 = *(_QWORD **)a2;
  v3 = *(_QWORD *)(a2 + 32);
  v4 = *(_QWORD *)(a2 + 8);
  ZNKR3fixIZ4mainEUlT_St7variantIJjNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESt10shared_ptrI4ConsEEESB_E_EclIJRS7_EEEDcDpOT_(
    v6,
    *(_QWORD *)(a2 + 16),
    *(_QWORD *)(a2 + 24));
  ZNKR3fixIZ4mainEUlT_St7variantIJjNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESt10shared_ptrI4ConsEEESB_E0_EclIJSB_EEEDcDpOT_(
    v7,
    v4,
    v6);
  ZNKR3fixIZ4mainEUlT_St7variantIJjNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEESt10shared_ptrI4ConsEEESB_SB_E3_EclIJSB_RSB_EEEDcDpOT_(
    a1,
    v2,
    (__int64)v7,
    v3);
  std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::~variant((__int64)v7);
  std::variant<unsigned int,std::string,std::shared_ptr<Cons>>::~variant((__int64)v6);
  return a1
```

一层层跟进这个调用，函数调用递归一层接一层把我绕晕了，而且每一层代码还不少，人工分析工程量很大，而且递归调用的地方不止一处，对人的记忆力也有很高的要求。总之，人工分析的话，工程量大，难度大，并且有的地方不用真的逆。所以我们思路，让工具辅助我们，找到主逻辑，然后我们再打开ida逆向。

#

```
二

pyda trace
```

##

使用pyda trace来跟踪程序的主逻辑

首先搭建环境：

```
FROM ubuntu:24.04 as target

FROM ghcr.io/ndrewh/pyda

COPY --from=target /usr/lib/x86_64-linux-gnu/ /target_libs/

RUN apt update && apt install -y patchelf

COPY F /F
RUN patchelf --set-interpreter /target_libs/ld-linux-x86-64.so.2 --set-rpath /target_libs/ /F
RUN apt install -y binutils
```

###

### trace cmp - 确定密文长度

首先trace cmp，使用仓库中的example/cmplog.py trace cmp

```
from pyda import *
from pwnlib.elf.elf import ELF
from pwnlib.util.packing import u64, u32
import string
import sys
import subprocess
from collections import defaultdict

p = process()

e = ELF(p.exe_path)
e.address = p.maps[p.exe_path].base

plt_map = { e.plt[x]: x for x in e.plt }

def get_cmp(proc):
    p = subprocess.run(f"objdump -M intel -d {proc.exe_path} | grep cmp", shell=True, capture_output=True)

    output = p.stdout.decode()
    cmp_locs = {}
    for l in output.split("\n"):
        if len(l) <= 1:
            continue

        # TODO: memory cmp
        if "QWORD PTR" in l:
            continue

        if ":\t" not in l:
            continue

        cmp_locs[int(l.split(":")[0].strip(), 16)] = l.split()[-1]

    return cmp_locs

cmp_locs_unfiltered = get_cmp(p)
cmp_locs = {}
for (a, v) in cmp_locs_unfiltered.items():
    info = v.split(",")
    if len(info) != 2:
        continue
    if "[" in info[0] or "[" in info[1]:
        continue

    if "0x" in info[0] or "0x" in info[1]:
        continue

    cmp_locs[a] = info

print(f"cmp_locs: {len(cmp_locs)}")

eq_count = 0
neq_count = 0
reg_map = {
    "eax": "rax",
    "ebx": "rbx",
    "ecx": "rcx",
    "edx": "rdx",
    "esi": "rsi",
    "edi": "rdi",
    "ebp": "rbp",
    "esp": "rsp",
    "r8d": "r8",
}

counts_by_pc = defaultdict(int)
good_cmps = defaultdict(int)
def cmp_hook(p):
    global eq_count, neq_count
    info = cmp_locs[p.regs.pc - e.address]

    counts_by_pc[p.regs.pc - e.address] += 1

    reg1 = reg_map.get(info[0], info[0])
    reg2 = reg_map.get(info[1], info[1])
    r1 = p.regs[reg1]
    r2 = p.regs[reg2]
    eq = r1 == r2

    if eq:
        eq_count += 1
    else:
        neq_count += 1

    print(f"cmp @ {hex(p.regs.rip - e.address)} {reg1}={hex(r1)} {reg2}={hex(r2)} {eq}")

for x in cmp_locs:
    p.hook(e.address + x, cmp_hook)

p.run()
```

开始trace：

```
pyda cmplog.py -- /F
cmp_locs: 46
FLAG: AAAAAAAAAAAAAAAA
//.. TOO LONG NOT TO SHOW
cmp @ 0x182a7 rcx=0x10 rdx=0x40 False
"Wrong"
```

可以看到程序输入“Wrong”之前的最后一个cmp，rcx=0x10 正好是我们输入的长度，所以猜测rdx=0x40是flag的真正长度。

输入正确长度的字符串，再次trace：

```
pyda cmplog.py -- /F
cmp_locs: 46
FLAG: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
//.. TOO LONG NOT TO SHOW
cmp @ 0x1891b rcx=0xc3df45f3 rdx=0x11793013 False
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000001 rax=0x100000001 True
cmp @ 0x15787 rdx=0x100000002 rax=0x100000001 False
"Wrong"
`...