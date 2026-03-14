---
title: Windows x64汇编
url: https://mp.weixin.qq.com/s/EGIXQ7L0Np_yOR6jEsG8Lw
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:10.889164
---

# Windows x64汇编

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5FtPcWDnic0eGK544LdRqDMZqsZPW4oJ6nCibAXgib05IYPRYf8XGKs4MoBgJjiaVTwKy3LVZthmrEUwBz2aQhKrIDV6yNqRhkHwMxlx5JwiaSLo/0?wx_fmt=jpeg)

# Windows x64汇编

原创

ybdt
ybdt

卡卡罗特取西经

![]()

在小说阅读器中沉浸阅读

学完王爽老师的Windows 16位汇编、罗云彬老师的Windows 32位汇编，最后就是Windows x64汇编，下面这个系列是我觉得不错的学习资源

```
【x64汇编与shellcode入门教程 01】https://mp.weixin.qq.com/s/HzEWKEpYpeBNJyk4IEll2g?scene=1【x64汇编与shellcode入门教程 02】https://mp.weixin.qq.com/s/vEfsmgBpEOJSzvXcvnEtUA?scene=1【x64汇编与shellcode入门教程 03】https://mp.weixin.qq.com/s/bJnqwt0_9rQCmaYZFrcFKg?scene=1【x64汇编与shellcode入门教程 04】https://mp.weixin.qq.com/s/-SEK85Fflt-Gr_Km9YcD3w?scene=1【x64汇编与shellcode入门教程 05】https://mp.weixin.qq.com/s/xC02bij37DTr_j4arJi_ag?scene=1【x64汇编与shellcode入门教程 06】https://mp.weixin.qq.com/s/db2pQXBx44IF4Dst0hw9sQ?scene=1【x64汇编与shellcode入门教程 07】https://mp.weixin.qq.com/s/AmjTv9wzFqzV1GKZYUecNQ
```

原文在这里：https://g3tsyst3m.com/shellcoding/assembly/debugging/x64-Assembly-and-Shellcoding-101/

翻译的质量不错，都很准确，当然你想看原文也可以

直接上代码，Windows x64汇编实现动态获取kernel32.dll地址，解析kernel32.dll导出表后定位WinExec，最后通过WinExec执行calc.exe

![](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0e4Gzlhkr1QgfLdicYBXcnoR8a8JWy3d6UWRXngYOKIojUCY67OAghjvThfKFIvzpshtw1waLeHsM1ibYrLU28j0BmZuVuJHat7k/640?wx_fmt=png&from=appmsg)

代码中包含了详细注释，我就不再赘述解释了

```
; nasm -fwin64 x64findkernel32.asm; ld -m i386pep -o x64findkernel32.exe x64findkernel32.obj
BITS 64SECTION .textglobal mainmain:

; get the base address of kernel32.dll by gs segment registersub rsp, 0x28and rsp, 0xfffffffffffffff0xor rcx, rcx                      ; rcx = 0   mov rax, [gs:rcx + 0x60]          ; gs contain the base address of TEB, and offset 0x60 is the base address of PEBmov rax, [rax + 0x18]             ; offset 0x18 is the base address of PEB->Ldrmov rsi, [rax + 0x10]             ; offset 0x10 is the base address of PEB->Ldr->InLoadOrderModuleListmov rsi, [rsi]                    ; jump to next node of linked list PEB->Ldr->InLoadOrderModuleList, ntdll.dllmov rsi, [rsi]                    ; jump to next node of linked list  PEB->Ldr->InLoadOrderModuleList, kernel32.dllmov rbx, [rsi + 0x30]             ; offset 0x30 is the base address of kernel32.dllmov r8, rbx                       ; the value of rbx assign to r8
; parse pe file header and export table to locate WinExec addressmov ebx, [rbx+0x3C]               ; pe file offset 0x3c contains nt headers addressadd rbx, r8                       ; relative address + base addressmov edx, [rbx+0x88]               ; nt headers offset 0x88 contains export directory addressadd rdx, r8                       ; relative address + base addressmov r10d, [rdx+0x14]              ; Total count for number of functionsxor r11, r11                      ; clear R11 mov r11d, [rdx+0x20]              ; AddressOfNames = RVAadd r11, r8                       ; AddressOfNames = VMAmov rcx, r10                      ; setup loop countermov rax, 0x00636578456E6957       ; "WinExec" string NULL terminated with a '0' push rax                          ; push to the stackmov rax, rsp                      ; move stack pointer to our WinExec string into RAXadd rsp, 8                        ; keep with 16 byte stack alignment
kernel32findfunction:    jecxz FunctionNameNotFound    ; If ecx is zero (function not found), set breakpoint    xor ebx, ebx                  ; Zero EBX    mov ebx, [r11+rcx*4]          ; EBX = RVA for first AddressOfName    add rbx, r8                   ; RBX = Function name VMA / add kernel32 base address to RVA to get WinApi name    dec rcx                       ; Decrement our loop by one, this goes from Z to A    mov r9, qword [rax]           ; R9 = "WinExec"    cmp [rbx], r9                 ; Compare all bytes    jz FunctionNameFound          ; jump if zero flag is set (found function name!)    jnz kernel32findfunction      ; didn't find the name, so keep loopin til we do!
FunctionNameFound:    push rcx    jmp OrdinalLookupSetup
FunctionNameNotFound:    int3
OrdinalLookupSetup:    pop r15    js OrdinalLookup
OrdinalLookup:    mov rcx, r15                  ; move our function's place into RCX    xor r11, r11                  ; clear R11 for use    mov r11d, [rdx+0x24]          ; AddressOfNameOrdinals = RVA    add r11, r8                   ; AddressOfNameOrdinals = VMA    inc rcx    mov r13w, [r11+rcx*2]         ; AddressOfNameOrdinals + Counter. RCX = counter    xor r11, r11    mov r11d, [rdx+0x1c]          ; AddressOfFunctions = RVA    add r11, r8                   ; AddressOfFunctions VMA in R11. Kernel32+RVA for function addresses    mov eax, [r11+r13*4]          ; function RVA.    add rax, r8                   ; Found the WinExec Api address!!!    push rax                      ; Store function addresses by pushing it temporarily    js executeit
; call WinExecexecuteit:pop r15                           ; address for WinExecmov rax, 0x00                     ; push null string terminator '0'push rax                          ; push it onto the stackmov rax, 0x6578652E636C6163       ; move string 'calc.exe' into RAX push rax                          ; push string + null terminator to stackmov rcx, rsp                      ; RDX points to stack pointer "WinExec" (1st parameter))mov rdx, 1                        ; move 1 (show window parameter) into RDX (2nd parameter)sub rsp, 0x30                     ; align stack 16 bytes and allow for proper setup for shadow space demandscall r15                          ; Call WinExec!!
```

说一点感悟，常说的汇编难，其实难在它背后藏了很多知识，比如Windows PE中的导出表、再比如通过TEB、PEB的结构体，这些不懂的话，肯定看不懂汇编，不过路虽远，行则将至，再难的知识只要去学也能学会

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

卡卡罗特取西经

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过