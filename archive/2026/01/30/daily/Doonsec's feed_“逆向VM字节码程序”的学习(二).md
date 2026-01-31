---
title: “逆向VM字节码程序”的学习(二)
url: https://mp.weixin.qq.com/s/5R05yfX6Xya0UKZ5eMNqug
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:00:50.101273
---

# “逆向VM字节码程序”的学习(二)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCl5wYd8Tt7R4YMx4mvFOJgOmaY2l3L4N5chKmY0qUrMYzJlzrh7PrNw/0?wx_fmt=jpeg)

# “逆向VM字节码程序”的学习(二)

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器中沉浸阅读

把关键点藏进VM字节码，这是个非常有创意的想法，如果用在病毒上则是非常地隐蔽。分析者必须先逆解释器，再逆字节码，无形中加大了隐蔽性和破解的难度。

就这个问题，我们这篇再继续细细研究下。

1、字节码结构和内容（位于0x40A140）：

{`regions`:[{`addr`:`0x40A140`,`size`:64}]}

[{"addr":"0x40A140","data":"0x0 0x0 0x21 0x0 0x2 0x0 0x0 0x0 0x91 0x0 0x8 0x0 0x0 0x0 0x16 0x0 0x0 0x0 0xc 0x0 0x9 0x0 0xa 0x0 0xb 0x0 0x0 0x0 0x0 0x0 0xc 0x0 0x2 0x0 0xc 0x0 0x0 0x0 0x0 0x0 0x1d 0x0 0xa 0x0 0xb 0x0 0x0 0x0 0x0 0x0 0x63 0x0 0x2 0x0 0xc 0x0 0x0 0x0 0x0 0x0 0x18 0x0 0x6 0x0"}]

2、VM执行函数VMFetchAndExecuteNextOpcode：

这段汇编代码实现了一个典型的 **虚拟机（VM）指令分派器（Dispatcher）**，也就是解释器的核心取指-执行循环。它的功能可以分解为以下几个步骤：

.text:00401540 VMFetchAndExecuteNextOpcode proc near

.text:00401540 var\_4 = word ptr -4

.text:00401540     push    ebp

.text:00401541     mov     ebp, esp

.text:00401543     push    ecx

；标准的函数入口，创建一个栈帧，并在栈上分配一个 16 位（word）的局部变量 `var_4` 用来暂存当前操作码。

.text:00401544     movzx   eax, vm\_instruction\_pointer

.text:0040154B     mov     cx, ds:word\_40A140[eax\*2]

.text:00401553     mov     [ebp+var\_4], cx

；取指Fetch

* 从 `vm_instruction_pointer` 读取当前指令位置
* **`word_40A140`** 是 **字节码/操作码数组**（Opcode Array）
* 由于索引乘以 2（`eax*2`），说明每个操作码是 **16 位（2 字节）**
* 读取的操作码存入 `CX`（并保存到栈上变量）

.text:00401557     movzx   edx, [ebp+var\_4]

.text:0040155B     mov     eax, vm\_opcode\_handlers[edx\*4]

.text:00401562     call    eax ; vm\_opcode\_handlers

; 译码与分派

* **`vm_opcode_handlers`** 是 **跳转表/函数指针表**（Jump Table）
* 由于索引乘以 4（`edx*4`），说明是 32 位指针数组（x86 架构）
* 根据操作码值查表得到对应的处理函数地址，然后间接调用

.text:00401564     mov     esp, ebp

.text:00401566     pop     ebp

.text:00401567     retn

.text:00401567 VMFetchAndExecuteNextOpcode endp

这是一个 **基于跳转表（Jump Table）的 VM 解释器核心循环**，实现了：

1. **取指**：从 `vm_instruction_pointer` 指向的位置读取 16 位操作码
2. **译码**：将操作码作为索引查询 `vm_opcode_handlers` 表
3. **执行**：跳转到对应的操作码处理函数执行具体逻辑

**典型应用场景**：

* 软件保护壳（如 VMProtect、 Themida 等）的虚拟化保护
* 脚本语言解释器（如早期的 Lua、Python 字节码解释器）
* 模拟器/仿真器核心

3、VM的主循环和入口点函数sub\_401610：

.text:00401610 sub\_401610      proc near

.text:00401610     push    ebp

.text:00401611     mov     ebp, esp

.text:00401613     call    InitializeVMOpcodeHandlers

.text:00401618     xor     eax, eax

.text:0040161A     mov     word\_40DF18, ax

.text:00401620     xor     ecx, ecx

.text:00401622     mov     word\_40DF1A, cx

.text:00401629     mov     edx, 9

.text:0040162E     mov     word\_40DF1C, dx

.text:00401635     xor     eax, eax

.text:00401637     mov     vm\_instruction\_pointer, ax

.text:0040163D \_\_vm\_execution\_loop:

.text:0040163D     movzx   ecx, vm\_instruction\_pointer

.text:00401644     movzx   edx, vm\_code\_size

.text:0040164B     cmp     ecx, edx

.text:0040164D    jge     short \_\_last\_vm\_instruction\_reached

.text:0040164F     call    VMFetchAndExecuteNextOpcode

.text:00401654     jmp     short \_\_vm\_execution\_loop

.text:00401656 \_\_last\_vm\_instruction\_reached:

.text:00401656      mov     ax, word\_40DF18

.text:0040165C      pop     ebp

.text:0040165D      retn

.text:0040165D sub\_401610      endp

4、opcode处理器的初始化函数和处理器表：

.text:00401570 InitializeVMOpcodeHandlers proc near

.text:00401570     push    ebp

.text:00401571     mov     ebp, esp

.text:00401573     mov     dword\_40DEE0, offset VMOpcodeHandler\_push

.text:0040157D     mov     dword\_40DEE4, offset VMOpcodeHandler\_pop

.text:00401587     mov     dword\_40DEE8, offset VMOpcodeHandler\_add

.text:00401591     mov     dword\_40DEEC, offset VMOpcodeHandler\_sub

.text:0040159B     mov     dword\_40DEF0, offset VMOpcodeHandler\_RotateRight

.text:004015A5     mov     dword\_40DEF4, offset VMOpcodeHandler\_RotateLeft

.text:004015AF     mov     dword\_40DEF8, offset VMOpcodeHandler\_xor

.text:004015B9     mov     dword\_40DEFC, offset VMOpcodeHandler\_not

.text:004015C3     mov     dword\_40DF00, offset VMOpcodeHandler\_eq

.text:004015CD    mov     dword\_40DF04, offset VMOpcodeHandler\_sel

.text:004015D7    mov     dword\_40DF08, offset VMOpcodeHandler\_jmp

.text:004015E1     mov     dword\_40DF0C, offset VMOpcodeHandler\_load

.text:004015EB     mov     dword\_40DF10, offset VMOpcodeHandler\_store

.text:004015F5     mov     dword\_40DF14, offset VMOpcodeHandler\_nop

.text:004015FF     pop     ebp

.text:00401600     retn

.text:00401600 InitializeVMOpcodeHandlers endp

5、opcode处理字节码（举例）：

.text:00401030 VMOpcodeHandler\_push proc near

.text:00401030 immediate = word ptr -4

.text:00401030     push    ebp

.text:00401031     mov     ebp, esp

.text:00401033     push    ecx

.text:00401034     mov     ax, vm\_instruction\_pointer

.text:0040103A     add     ax, 1

.text:0040103E     mov     vm\_instruction\_pointer, ax

.text:00401044     movzx   ecx, vm\_instruction\_pointer

.text:0040104B     mov     dx, ds:word\_40A140[ecx\*2]

.text:00401053     mov     [ebp+immediate], dx

.text:00401057     movzx   eax, [ebp+immediate]

.text:0040105B     push    eax

.text:0040105C     call    VMStack\_push

.text:00401061     add     esp, 4

.text:00401064     mov     cx, vm\_instruction\_pointer

.text:0040106B     add     cx, 1

.text:0040106F     mov     vm\_instruction\_pointer, cx

.text:00401076     mov     esp, ebp

.text:00401078     pop     ebp

.text:00401079     retn

.text:00401079 VMOpcodeHandler\_push endp

这段汇编就是“虚拟机里  push imm16  指令”的执行过程——把字节码流里的 16 位常数取出来，压到 VM 自己的小栈上，再把指令指针往前挪 2 字节。逐句翻译如下：

|  |  |  |
| --- | --- | --- |
| 汇编 | 伪代码 | 说明 |
| mov ax, vm\_instruction\_pointer | ax = ip | 取当前字节码偏移 |
| add ax, 1 | ax++ | 跳过 opcode 字节 |
| mov vm\_instruction\_pointer, ax | ip = ax | 更新 ip |
| movzx ecx, vm\_instruction\_pointer | ecx = ip | 零扩展成 32 位索引 |
| mov dx, word\_40A140[ecx\*2] | dx = bytecode[ip] | 读下一个 16 位立即数 |
| push eax / call VMStack\_push | stack\_push(dx) | 把常数压进 VM 栈 |
| 再次 ip++ | ip += 1 | 跳过刚才读完的 2 字节立即数 |

一句话：“取 2 字节常数 → 压栈 → 指令指针 +2，继续取下一条指令”——这就是 VM 世界里  push imm16  的全部工作。

6、VM字节码执行可视化追踪

完整执行时间线

假设输入：smokestack.exe SECRET1234

时间轴：程序执行的每个关键步骤

══════════════════════════════════════

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCLmjBtOiaHkjfTR5T9wVpB0LTr0G5VeUsKkX62GuDKraQU78Dx5ibYGtg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCNfdNVw5dNACpWQfUqXemPUVRmMZaa7ZJIo6fnWamNd0zTK0tqTFGvA/640?wx_fmt=png&from=appmsg)

；具体代码如下：

; 循环变量 i 在 [ebp+var\_4]

; argv[1] 指针在 [ebp+argv]

loc\_402FA5:

    mov     edx, [ebp+var\_4]        ; edx = i

    add     edx, 1                  ; i++

    mov     [ebp+var\_4], edx        ; 保存i

loc\_402FAE:

    cmp     [ebp+var\_4], 0Ah        ; 比较 i < 10

    jge     short loc\_402FCF        ; 如果 i >= 10，跳出循环

    mov     eax, [ebp+argv]         ; eax = argv

    mov     ecx, [eax+4]            ; ecx = argv[1]（第一个参数字符串）

    mov     edx, [ebp+var\_4]        ; edx = i

    movsx   ax, byte ptr [ecx+edx]  ; ax = argv[1][i]（字符，符号扩展）

    mov     ecx, [ebp+var\_4]        ; ecx = i

    mov     word\_40DF20[ecx\*2], ax  ; VM栈[i] = argv[1][i]

    jmp     short loc\_402FA5        ; 继续循环

loc\_402FCF:

    call    sub\_401610              ; 调用VM主函数

    mov     word ptr [ebp+var\_1C], ax  ; 保存VM返回值（ax寄存器）

========================

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxC3j5icrfQGGKfQBwicpM7CUCBtys8icld3HyyY59ArsMjNkv8wbNBuicibiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCdlzM6MllcbGHUQqLtib0yd9qVxMzG3qK5TvX5FWaribKljKkxpY8SjAA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCKMVD5DudOOsnrY6hmbN5LJKFI4qWbLxN9NYUdcliaPfX7lEAup82QOQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCrKDAIQkkIN7Cpds0wO3uzr6AsJNuFw0XzicavEW7RFBsCPXhxiaGPdag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpKG5LpmG6wBpQoT5kjxhwxCJ...