---
title: 整理Windows 全架构 Hook 技术图谱：从 Ring3 到固件层 34 种实现
url: https://mp.weixin.qq.com/s/edRWQu4cFuXa-UZsZ92-8g
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:50.535611
---

# 整理Windows 全架构 Hook 技术图谱：从 Ring3 到固件层 34 种实现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2ribYMmNxvfUmpLicvkY01vJFQwXll3Y4HicO8rNgDFpyVJxfS6iahy0tMPLqiafjKGL9soabxEMfseIfpRrPytYNdjTa2ianxx7icXU/0?wx_fmt=jpeg)

# 整理Windows 全架构 Hook 技术图谱：从 Ring3 到固件层 34 种实现

kyx\_san
kyx\_san

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 从最容易被检测的用户态 Hook，到理论上无法被静态发现的 Hypervisor 级 Hook，按隐蔽性从低到高排列。每种技术均提供完整可编译的实现代码。

#

**第一层：用户态 Hook（Ring 3）**

用户态 Hook 是最基础的拦截手段，所有代码运行在应用层，任何反作弊/安全软件只要扫描进程内存就能发现。隐蔽性最低，但开发成本也最低。

## 1.1 IAT Hook（导入地址表 Hook）

### 原理

PE 文件加载时，Loader 会填充 IAT（Import Address Table），记录每个导入函数的实际地址。IAT Hook 直接修改这张表里的函数指针，让程序调用时跳到你的函数。

### 完整实现

```
#include <windows.h>
#include <winternl.h>

typedef HANDLE(WINAPI* fnOpenProcess)(DWORD, BOOL, DWORD);
fnOpenProcess OriginalOpenProcess = NULL;

// Hook 函数
HANDLE WINAPI HookedOpenProcess(DWORD dwDesiredAccess, BOOL bInheritHandle, DWORD dwProcessId) {
// 过滤掉对保护进程的访问
if (dwProcessId == GetProtectedPid()) {
        SetLastError(ERROR_ACCESS_DENIED);
return NULL;
    }
return OriginalOpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId);
}

// IAT Hook 核心逻辑
BOOL IatHook(HMODULE hModule, const char* dllName, const char* funcName, PVOID hookFunc, PVOID* originalFunc) {
// 获取 DOS Header
    PIMAGE_DOS_HEADER pDos = (PIMAGE_DOS_HEADER)hModule;
if (pDos->e_magic != IMAGE_DOS_SIGNATURE) return FALSE;

// 获取 NT Header
    PIMAGE_NT_HEADERS pNt = (PIMAGE_NT_HEADERS)((BYTE*)hModule + pDos->e_lfanew);
if (pNt->Signature != IMAGE_NT_SIGNATURE) return FALSE;

// 获取导入表 RVA
    DWORD importRva = pNt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress;
if (importRva == 0) return FALSE;

    PIMAGE_IMPORT_DESCRIPTOR pImport = (PIMAGE_IMPORT_DESCRIPTOR)((BYTE*)hModule + importRva);

// 遍历每个导入的 DLL
while (pImport->Name) {
char* modName = (char*)((BYTE*)hModule + pImport->Name);
if (_stricmp(modName, dllName) == 0) {
// 找到目标 DLL，遍历其 IAT
            PIMAGE_THUNK_DATA pOrigThunk = (PIMAGE_THUNK_DATA)((BYTE*)hModule + pImport->OriginalFirstThunk);
            PIMAGE_THUNK_DATA pThunk = (PIMAGE_THUNK_DATA)((BYTE*)hModule + pImport->FirstThunk);

while (pOrigThunk->u1.AddressOfData) {
// 通过名字匹配
if (!(pOrigThunk->u1.Ordinal & IMAGE_ORDINAL_FLAG)) {
                    PIMAGE_IMPORT_BY_NAME pName = (PIMAGE_IMPORT_BY_NAME)((BYTE*)hModule + pOrigThunk->u1.AddressOfData);
if (strcmp(pName->Name, funcName) == 0) {
// 找到目标函数，保存原始地址
                        *originalFunc = (PVOID)pThunk->u1.Function;

// 修改内存保护
                        DWORD oldProtect;
                        VirtualProtect(&pThunk->u1.Function, sizeof(ULONG_PTR), PAGE_READWRITE, &oldProtect);
                        pThunk->u1.Function = (ULONG_PTR)hookFunc;
                        VirtualProtect(&pThunk->u1.Function, sizeof(ULONG_PTR), oldProtect, &oldProtect);
return TRUE;
                    }
                }
                pOrigThunk++;
                pThunk++;
            }
        }
        pImport++;
    }
return FALSE;
}

// 使用
void InstallIatHook() {
    IatHook(GetModuleHandle(NULL), "kernel32.dll", "OpenProcess",
            HookedOpenProcess, (PVOID*)&OriginalOpenProcess);
}
```

### 检测难度：★☆☆☆☆

遍历 IAT，对比每个条目是否指向对应 DLL 的地址范围内即可发现。CRC 校验 IAT 区域也能立即暴露。

### 局限

* 只能 Hook 通过 IAT 调用的函数，GetProcAddress 动态获取的地址不经过 IAT
* 每个模块有独立的 IAT，需要逐一修改
* 任何内存扫描工具一眼就能看到

## 1.2 EAT Hook（导出地址表 Hook）

### 原理

修改 DLL 的 EAT（Export Address Table），让后续模块通过 GetProcAddress 获取到的地址是 Hook 函数。

### 完整实现

```
BOOL EatHook(HMODULE hDll, const char* funcName, PVOID hookFunc, PVOID* originalFunc) {
PIMAGE_DOS_HEADERpDos = (PIMAGE_DOS_HEADER)hDll;
PIMAGE_NT_HEADERSpNt = (PIMAGE_NT_HEADERS)((BYTE*)hDll + pDos->e_lfanew);

DWORDexportRva = pNt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress;
if (exportRva == 0) return FALSE;

PIMAGE_EXPORT_DIRECTORYpExport = (PIMAGE_EXPORT_DIRECTORY)((BYTE*)hDll + exportRva);
    DWORD* pFunctions = (DWORD*)((BYTE*)hDll + pExport->AddressOfFunctions);
    DWORD* pNames = (DWORD*)((BYTE*)hDll + pExport->AddressOfNames);
    WORD* pOrdinals = (WORD*)((BYTE*)hDll + pExport->AddressOfNameOrdinals);

for (DWORDi =0; i < pExport->NumberOfNames; i++) {
char* name = (char*)((BYTE*)hDll + pNames[i]);
if (strcmp(name, funcName) == 0) {
// 保存原始函数地址
            *originalFunc = (PVOID)((BYTE*)hDll + pFunctions[pOrdinals[i]]);

// 计算 Hook 函数相对于 DLL 基址的 RVA
DWORDhookRva = (DWORD)((BYTE*)hookFunc - (BYTE*)hDll);

            DWORD oldProtect;
            VirtualProtect(&pFunctions[pOrdinals[i]], sizeof(DWORD), PAGE_READWRITE, &oldProtect);
            pFunctions[pOrdinals[i]] = hookRva;
            VirtualProtect(&pFunctions[pOrdinals[i]], sizeof(DWORD), oldProtect, &oldProtect);
return TRUE;
        }
    }
return FALSE;
}

// 注意：EAT Hook 的 hookFunc 地址必须在目标 DLL 的地址空间内
// 否则 RVA 会溢出。解决方案：在目标 DLL 附近分配内存作为跳板
PVOID AllocateNearby(HMODULE hDll, SIZE_T size) {
    MEMORY_BASIC_INFORMATION mbi;
    BYTE* addr = (BYTE*)hDll;

// 在 DLL 前后 2GB 范围内找可用空间（RVA 是 32 位有符号偏移）
for (BYTE* p = addr - 0x70000000; p < addr + 0x70000000; p += mbi.RegionSize) {
if (VirtualQuery(p, &mbi, sizeof(mbi)) == 0) continue;
if (mbi.State == MEM_FREE && mbi.RegionSize >= size) {
PVOIDalloc = VirtualAlloc(p, size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
if (alloc) return alloc;
        }
    }
return NULL;
}
```

### 检测难度：★☆☆☆☆

和 IAT Hook 一样，对比 EAT 条目与磁盘原始文件即可发现。

### 局限

* 只对后续调用 GetProcAddress 的模块有效
* 已经缓存了函数地址的模块不受影响
* 同样是从内存修改，扫描即暴露

## 1.3 Inline Hook（内联 Hook / Detour）

### 原理

直接修改目标函数的头部字节，写入一条 jmp 指令跳转到你的 Hook 函数。执行完自定义逻辑后，跳回被覆盖的原始指令继续执行（Trampoline）。

### 完整实现（含指令重定位引擎）

```
#include <windows.h>
#include <stdint.h>

// x64 指令长度解析器（简化版，覆盖常见指令）
// 完整版应使用 Zydis/distorm 等反汇编库
typedef struct _INSTRUCTION {
uint8_t length;
    BOOL isRipRelative;      // 是否包含 RIP 相对寻址
int32_t ripOffset;       // RIP 偏移在指令中的位置
int32_t ripDisplacement; // 原始 displacement 值
} INSTRUCTION;

// 解析单条指令长度（简化版核心逻辑）
INSTRUCTION ParseInstruction(constuint8_t* code) {
    INSTRUCTION inst = {0};
constuint8_t* p = code;

// 跳过前缀 (REX, LOCK, REP, segment override 等)
while (*p == 0xF0 || *p == 0xF2 || *p == 0xF3 ||
           *p == 0x26 || *p == 0x2E || *p == 0x36 || *p == 0x3E ||
           *p == 0x64 || *p == 0x65 || *p == 0x66 || *p == 0x67 ||
           (*p >= 0x40 && *p <= 0x4F)) { // REX prefix
        p++;
    }

uint8_t opcode = *p++;

// 处理双字节操作码 (0F xx)
if (opcode == 0x0F) {
uint8_t op2 = *p++;
// ModRM
if (op2 >= 0x80 && op2 <= 0x8F) {
// Jcc rel32 (条件跳转)
            inst.length = (int)(p - code) + 4;
            inst.isRipRelative = TRUE;
            inst.ripOffset = (int)(p - code);
            inst.ripDisplacement = *(int32_t*)p;
return inst;
        }
// 其他 0F xx 指令处理...
if ((op2 & 0xC0) != 0xC0) { // 有 ModRM
uint8_t modrm = *p++;
uint8_t mod = (modrm >> 6) & 3;
uint8_t rm = modrm & 7;
if (mod == 0 && rm == 5) { // RIP-relative
                inst.isRipRelative = TRUE;
                inst.ripOffset = (int)(p - code);
                inst.ripDisplacement = *(int32_t*)p;
                p += 4;
            } else if (mod == 0 && rm == 4) { p++; } // SIB
else if (mod == 1) { if (rm == 4) p++; p++; }
else if (mod == 2) { if (rm == 4) p++; p += 4; }
        }
        inst.length = (int)(p - code);
return inst;
    }

// 单字节操作码处理
switch (opcode) {
case 0xE8: // CALL rel32
case 0xE9: // JMP rel32
            inst.length = (int)(p - code) + 4;
            inst.isRipRelative = TRUE;
            inst.ripOffset = (int)(p - code);
            inst.ripDisplacement = *(int32_t*)p;
return inst;
case 0xEB: // JMP rel8
            inst.length = (int)(p - code) + 1;
            inst.isRipRelative = TRUE;
            inst.ripOffset = (int)(p - code);
            inst.ripDisplacement = (int8_t)*p;
return inst;
// ... 其他操作码
    }

// 通用 ModRM 解析
// (这里省略完整的操作码表映射，实际项目应使用 Zydis)
    inst.length = (int)(p - code);
if (inst.length == 0) inst.length = 1; // 兜底
return inst;
}

// Trampoline 构建器：将被覆盖的原始指令复制到 trampoline，并修正 RIP 相对引用
#define HOOK_STUB_SIZE 14  // x64 绝对跳转: FF 25 00 00 00 00 [8字节地址]
#define TRAMPOLINE_MA...