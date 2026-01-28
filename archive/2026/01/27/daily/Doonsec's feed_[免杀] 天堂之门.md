---
title: [免杀] 天堂之门
url: https://mp.weixin.qq.com/s/DljrsqfemEZcblCyVYNDsQ
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:11.820419
---

# [免杀] 天堂之门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9whbh13xlAnuH6uWogHqWgjCPWNEeLWgHWia9Eus7cEoZIjUu0Db26JA/0?wx_fmt=jpeg)

# [免杀] 天堂之门

原创

joe1sn
joe1sn

不止Sec

![]()

在小说阅读器中沉浸阅读

这里是两段汇编代码

```
section .data    msg db "Hello, World!", 10    len equ $ - msg
section .text    global _start
_start:    ; ssize_t write(int fd, const void *buf, size_t count)    mov eax, 4          ; sys_write    mov ebx, 1          ; stdout    mov ecx, msg    mov edx, len    int 0x80
    ; void exit(int status)    mov eax, 1          ; sys_exit    xor ebx, ebx    int 0x80
```

使用`int 0x80`系统调用完成输出

```
section .data    msg db "Hello, World!", 10    len equ $ - msg
section .text    global _start
_start:    ; ssize_t write(int fd, const void *buf, size_t count)    mov rax, 1          ; sys_write    mov rdi, 1          ; stdout    lea rsi, [rel msg]    mov rdx, len    syscall
    ; void exit(int status)    mov rax, 60         ; sys_exit    xor rdi, rdi    syscall
```

这里使用的是`syscall`完成输出

或许在之前你已经了解过DLL注入的相关篇章

[https://mp.weixin.qq.com/s/qYO0Cf5MRT4vKCT5WYz1KQ](https://mp.weixin.qq.com/s?__biz=Mzk0MTY5NDg3Mw==&mid=2247483780&idx=1&sn=efe49b87489187beda54ed372fd7895a&scene=21#wechat_redirect)

不禁让人产生疑问：32位和64位程序使用的指令集不同，那么64位系统如何兼容运行32位软件呢？本篇文章在windows上作为探索。

## Wow64分析

32位程序在64位windows上的运行时通过`wow64`模拟器实现的

![image-20260127133658568](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic96IicWkNGib2srjjBiaBzaSHz1FxwiawPpXnPQzGuTQpblNb7Pic0hfxyZjA/640?wx_fmt=png&from=appmsg)

顺带提一嘴，这里根据《深入解析windows操作系统》`3.6 CreateProcess` 的创建进程中相关步骤

1. 首先是转换并验证参数：主要调度优先级，是否调试，分析参数
2. 打开要执行的映像：主要是创建对应的windows映像

   ![image-20260127132913114](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9O7Q5RA5wk6zrxlYT9WyRHpjPiarmgP7IiaewQEHoCw6OH1pon8fiaAicSQ/640?wx_fmt=png&from=appmsg)
3. 创建Windows进程执行体对象：主要是设置`EPROCESS`对象，其中

* 如果处于`Wow64`下检查是否使用大页面
* `Wow64`下则随后分配辅助结构`EWOW64PROCESS`
* 在映射`Ntdll.dll`到进程中，对于`Wow64`进程还需要映射32位的`Ntdll.dll`

## 操作系统相关知识

在OS混沌未开之际，便有几位老祖

* CS (Code Segment Register)：代码段的段基址
* DS(Data Segment Register)：数据段的段基址
* ES(Extra Segment Register)：其值为附加数据段的段基值，称为“附加”是因为此段寄存器用途不像其他 `sreg` 那样固定，可以额外做他用。
* FS(Extra Segment Register)：其值为附加数据段的段基值
* GS：同上
* SS(Stack Segment Register)：堆栈段寄存器

其存储着os的本源灵气（物理地址）

再后来一生二、二生三，老祖集天地之造化，创结界（保护模式），著天书（全局描述符GDT（Global Descriptor Table）），生韵韵众生于虚幻。老祖（段寄存器）在虚幻中的像，幻化众生心中便为**段选择子**。

---

说人话：

段寄存器（CS / DS / SS …）里放的 **不是地址**，而是：一个 `索引 + 权限声明`的小结构。

在windows中

| CS | 含义 |
| --- | --- |
| `0x23` | 32 位用户代码段 |
| `0x33` | 64 位用户代码段 |
| `0x10` | 内核代码段 |

* 怎么做权限隔离？
* 怎么防止用户程序乱访问内核？
* 怎么同时跑不同“模式”的代码？

Intel 的答案：把“段的定义”集中放在一张表里，让 CPU 强制检查

![img](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9WvJuFJnCRITCjuzm4bNF69pqia7fZlJIUBMkhNmnZPz3ovibKqVLrraQ/640?wx_fmt=jpeg&from=appmsg)

段选择子一般长这样（冒号后面可以理解为二进制的长度(bit长度)，注意是小端序）

```
typedef struct selector{    unsigned char RPL :2;    unsigned char TI :1;	//local descriptor table    unsigned short index :13;} __attribute__((packed)) selector;
//15           3 2  1 0//+--------------+--+--+//|   Index      |TI|RPL|//+--------------+--+--+
```

那么当`CS=0x33=0b110011时，按照段选择子的结构体解析：`

* RPL = 11 b = 2
* TI = 0 = 0
* index = 110 = 6

那么CPU就回去`GDT[6]`看这是一个 64 位 ring3 代码段

## 天堂之门 Heaven’s Gate

利用`Wow64`机制，就可以在32位程序中运行64位代码，这样EDR 常 hook 32 位 `ntdll.dll`的时候就可以绕过检测。同时分析32位的程序发现了64位的指令一般是反汇编不出的，例如使用32位的ida分析64位的程序。

这种方式的特征就是使用长跳，类似如下代码：

```
; 32-bit contextfar_jump CS=0x33, RIP=entry64
; ===== 64-bit context =====entry64:    ; 64-bit instructions    ; e.g. call 64-bit ntdll stub    far_return CS=0x23
```

现在结合`Minhook`编写一段`hook ntdll.dll`中 测试代码

关于minhook的使用可以参考：[https://mp.weixin.qq.com/s/Po\_t-JGj0e3dMBKDd9i8cw](https://mp.weixin.qq.com/s?__biz=Mzk0MTY5NDg3Mw==&mid=2247483708&idx=1&sn=bce5798c93813b51cd552186d1341b67&scene=21#wechat_redirect)

为了省去LDR这种通用过程的代码，我使用了 https://github.com/JustasMasiulis/wow64pp

这个框架的长跳部分实现如下：

![image-20260127200245626](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9dkqGnOC6I64MQSag46zOwEJyia1NZuG29Zibq3V8wshWccRibHkQJ1Jkg/640?wx_fmt=png&from=appmsg)

![image-20260127200001817](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9RY3Bhak09L6yVdulYAUBic7rDZdXBak1N1Kiayu3Pt2AMbcib6bRiaoJKg/640?wx_fmt=png&from=appmsg)

**其中的`push 0x33`只是为“远返回 / 远跳转”准备一个新的段选择子**

框架是header-only的，只有一个`.h`文件，非常轻松的就能使用，但是这个框架目前存在两个问题：

* 只能使用ntdll.dll中的函数。怎么说呢，根据一些看雪老哥的说法是

  > 另外无法加载kerner32.dll，和user32.dll是操作系统设计限制，就算你加载成功并调用了里面的函数，之后程序也会问题，因为程序已经进入一个混乱的状态了（同时拥有了32位和64位的窗口态等），会让系统分不清楚你这个进程到底是64位的还是32位的
* 多参数传参问题。最开始我使用的是`NtCreateFile`，但是返回的结果是传参错误，换了`NtQuerySystemTime`就可了。这种保持堆栈平衡之类的感觉很难做到十全十美。

```
#define NOMINMAX#include "extern/minhook/minhook.h"#include "extern/wow64pp/wow64pp.hpp"#include <iostream>#include <Windows.h>#include <winternl.h>typedef NTSTATUS(NTAPI* NtQuerySystemTime_t)(    PLARGE_INTEGER SystemTime    );NtQuerySystemTime_t fpNtQuerySystemTime = nullptr;NTSTATUS NTAPI HookedNtQuerySystemTime(    PLARGE_INTEGER SystemTime){    std::cout << "[hook] NtQuerySystemTime called (x86 stub), ";    NTSTATUS status = fpNtQuerySystemTime(SystemTime);    if (NT_SUCCESS(status))    {        std::cout << "[hook] SystemTime = "            << SystemTime->QuadPart << std::endl;    }    return status;}int main() {    LARGE_INTEGER systemTime = { 0 };    NtQuerySystemTime(&systemTime);    if (MH_Initialize() != MH_OK)    {        std::cerr << "[x] init hook failed\n";        return 1;    }    LPVOID pTarget = GetProcAddress(GetModuleHandleW(L"ntdll.dll"), "NtQuerySystemTime");    std::cout << "[*] now hook NtQuerySystemTime: 0x" << std::hex << pTarget << std::endl;    if (MH_CreateHook(pTarget, &HookedNtQuerySystemTime, reinterpret_cast<LPVOID*>(&fpNtQuerySystemTime)) != MH_OK)    {        std::cerr << "[x] create hook failed\n";        return 1;    }    MH_EnableHook(pTarget);    NtQuerySystemTime(&systemTime);    auto ntdllHandle = wow64pp::module_handle("ntdll.dll");    std::cout << "[*] found ntdll (x64): 0x" << std::hex << ntdllHandle << "\n";    auto NtQuerySystemTime64 = wow64pp::import(ntdllHandle, "NtQuerySystemTime");    std::cout << "[*] found NtQuerySystemTime (x64): 0x" << std::hex << NtQuerySystemTime64 << "\n";    auto status = wow64pp::call_function(        NtQuerySystemTime64,        &systemTime        // PLARGE_INTEGER    );    std::cout << "[wow64] NtQuerySystemTime status: 0x" << std::hex << status << "\n";    std::cout << "[wow64] SystemTime (100ns since 1601): " << systemTime.QuadPart << "\n";    MH_DisableHook(pTarget);    return 0;}
```

1. 正常调用`NtQuerySystemTime`
2. Hook `NtQuerySystemTime`并调用
3. 使用Wow64进行64位的`NtQuerySystemTime`调用

![image-20260127195411794](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9wdVIb6kjwygKy1Xnou8Pvs9dOfe7UVEiamibbicyibjJ6FElRPFYFf80UA/640?wx_fmt=png&from=appmsg)

## 后记

看似很nb但是现在这种技巧已经不怎么行了

比如上面的绕过hook，这种应用层的很明显是无法绕过内核/etw hook的，同时有明显的shellcode特征。不过可以恶心一手逆向的人，因为这样可以向32位的程序狠狠塞64位的shellcode，造成反汇编指令识别的错误，但也只能恶心了。

关于项目结构这里给出来便于复现。

![image-20260127201247825](https://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVSvaiazkcQnexLM438MuyAic9YwGnWbY5QnOV0MgO0X3o7Uhymn94MVGiaxrJIsL5cMbbRBsnAZTec7Q/640?wx_fmt=png&from=appmsg)

`extern\minhook\CMakeLists.txt`

```
cmake_minimum_required(VERSION 3.11)project(minhook)
set(MINHOOK_SOURCES    buffer.c    hook.c    trampoline.c    hde/hde32.c    hde/hde64.c    )
set(MINHOOK_INCLUDE    buffer.h    trampoline.h    hde/hde32.h    hde/hde64.h    hde/pstdint.h    hde/table32.h    hde/table64.h    )
add_library(${PROJECT_NAME}  STATIC    ${MINHOOK_SOURCES}    ${MINHOOK_INCLUDE})
target_include_directories(${PROJECT_NAME}  PUBLIC    ${CMAKE_CURRENT_SOURCE_DIR})
```

`extern\wow64pp\CMakeLists.txt`

```
cmake_minimum_required(VERSION 3.11)project(wow64pp LANGUAGES CXX)
# 创建一个 interface 库add_library(${PROJECT_NAME} INTERFACE)
# 添加 include 目录target_include_directories(${PROJECT_NAME} INTERFACE    ${CMAKE_CURRENT_SOURCE_DIR})
```

`CMakeLists.txt`

```
cmake_minimum_required(VERSION 3.11)project(gat...