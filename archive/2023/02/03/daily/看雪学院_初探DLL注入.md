---
title: 初探DLL注入
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493266&idx=1&sn=1105289534522f736c8ecb0ed7f47d2a&chksm=b18e91d886f918ce7bf0b33861b347cd93680c68d96e5043f6373fa35839a24b10e8df75cdd1&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-02-03
fetch_date: 2025-10-04T05:35:10.147226
---

# 初探DLL注入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FacY5173sn2mR9ticoVp7wwOeqXf9XGr9NCeEsTrcq20VQXTwe50aPX99WWR8cTCLM874r3tc63kg/0?wx_fmt=jpeg)

# 初探DLL注入

顾忧

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EYaibg8K5vn9b1ABb77ofz89KswU54BMToIYj2w8cK1W7UocEExG28WOxLWVgZ47tOiaU98jphrM2g/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：顾忧

DLL注入是指向运行中的其它进程强制插入特定的DLL文件。从技术细节来说，DLL注入命令其它进程自行调用LoadLibrary()API，加载用户指定的DLL文件。DLL注入与一般DLL加载的区别在于，加载的目标进程是其自身或其他进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8T3wjVdc94x6uvARJHsEP0E9EVgbeZUsiaXrVPtibN8o26PfPI49sibhylw/640?wx_fmt=jpeg)

从上图可以看到，test.dll已被强制插入进程(本来notepad并不会加载test.dll)。加载到某一进程中的test.dll与已经加载到某一进程中的dll一样，拥有访问notepad.exe进程内存的权限。

```
DLL被加载到进程后会自动运行DLLMain()函数，用户可以把想执行的代码放到DLLMain()函数，每当加载DLL时，添加的代码就会得到执行。利用这种特性可以修复程序Bug以及添加新功能
```

###

```
DllMain 函数是DLL模块的默认 入口点。当Windows加载DLL模块时调用这一函数。系统首先调用全局对象的 构造函数，然后调用 全局函数DLLMain。DLLMain 函数不仅在将DLL链接加载到进程时被调用，在DLL模块与进程分离时（以及其它时候）也被调用。 BOOL APIENTRY DllMain( HANDLE hModule, DWORD ul_reason_for_call, LPVOID lpReserved){　switch (ul_reason_for_call)　{　　case DLL_PROCESS_ATTACH:      //添加想要执行的代码      //当dll被进程加载时DLLMain被调用　　　//printf(" process attach of dll");　　　break;　　case DLL_THREAD_ATTACH:      //添加想要执行的代码      //当有线程被创建时，DLLMain被调用　　　printf(" thread attach of dll");　　　break;　　case DLL_THREAD_DETACH:      //添加想要执行的代码      //当有线程结束时，DLLMain被调用　　　printf(" thread detach of dll");　　　break;　　case DLL_PROCESS_DETACH:      //添加想要执行的代码      //当dll被进程卸载时，DLLMain被调用　　　printf(" process detach of dll");　　　break;　}　return TRUE;}
```

###

###

###

```
一

DLL注入示例
```

使用LoadLibrary()API加载某个DLL时，该DLL中的DLLMain()函数会被调用执行。DLL注入的工作原理就是从外部促使目标进程调用LoadLibrary()API,所以会强制调用执行DLL的DLLMain函数。并且被注入的DLL拥有目标进程内存的访问权限，用户可以随意操作。

###

###

```
二

实现DLL注入的方法
```

####

#### 1、创建远程线程(CreatRemoteThread)

####

#### 2、使用注册表(AppInit\_DLLs值)

####

#### 3、消息钩取（SetWindowsHookEx()API）

###

###

```
三

创建远程线程(CreatRemoteThread)
```

####

#### **3.1、效果示例**

运行process explorer（或者火绒剑，任务管理器）获取notepad.exe进程的pid。

可以看见process explorer.exe的pid为2788。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8TuzN3sCDqu0ByfGjXAQ6selK4p4MEeYxdR2mL8h9GMEX1KTALdVJdFw/640?wx_fmt=png)

运行InjectDll.exe将myhack.dll注入到notepad.exe进程当中。可以看到dll文件已经被注入到里面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8TVYI4S7KlGe44DqaIGnVh77N9nbH0H3NRhElaOL9L3bx4YgnDia1DXVA/640?wx_fmt=png)

要想在process explorer中看见注入的dll文件，需要依次选择view->Lower Pane view->DLLS选项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8TkAiaFHa55VbXBlckuWsnDX1bT8102xldZSNVFKqwtbvUjhic2fBMhicgw/640?wx_fmt=png)

进行注入时需要注意：

```
1.LoadLibraryA 和 LoadLibraryW 不同字符表示之前一直没有成功，没有使用L,但是使用了LoadLibraryW，导致加载dll失败，如果不使用L，请用LoadLibraryA 2.注册的时候注意DLL完整路径，除非被注入程序和dll在同一个文件夹InjectDll.exe 3480 D:\test\myhack.dll
```

同时可以看见文件内已经多了一个html文件，此文件是dll中所指定的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fz4lU5jRTibIbrXKXTr0s8TIjNuQAWH25DMkb5Yvp9gGLhcLUBRTyTe8A41Sl6eNePqOmAU8rFaag/640?wx_fmt=png)

#### **3.2、分析示例源码**

在DLLMmain()函数中可以看到，这个dll被加载(DLL\_PROCESS\_ATTACH)时,先输出一个字符串（"<myhack.dll> Injection!!!"），然后再创建线程调用函数（ThreadProc）。在ThreadProc函数中通过调用URLDownloadToFile来下载指定网站的index.html文件。前面提到过，向进程注入dll后会调用dll的DLLMain函数。所以当dll文件注入到exe进程后，会调用URLDownloadToFile下载文件。

```
//myhack.cpp#include "windows.h"#include "tchar.h" #pragma comment(lib, "urlmon.lib") #define DEF_URL       (L"http://www.naver.com/index.html")#define DEF_FILE_NAME   (L"index.html") HMODULE g_hMod = NULL; DWORD WINAPI ThreadProc(LPVOID lParam){    TCHAR szPath[_MAX_PATH] = {0,};     if( !GetModuleFileName( g_hMod, szPath, MAX_PATH ) )        return FALSE;         TCHAR *p = _tcsrchr( szPath, '\\' );    if( !p )        return FALSE;    //下载指定网站的index.html文件    _tcscpy_s(p+1, _MAX_PATH, DEF_FILE_NAME);     URLDownloadToFile(NULL, DEF_URL, szPath, 0, NULL);      return 0;} BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved){    HANDLE hThread = NULL;     g_hMod = (HMODULE)hinstDLL;     switch( fdwReason )    {    case DLL_PROCESS_ATTACH :  //加载时        OutputDebugString(L"<myhack.dll> Injection!!!"); //输出调试字符串        hThread = CreateThread(NULL, 0, ThreadProc, NULL, 0, NULL); //创建线程        CloseHandle(hThread);        break;    }     return TRUE;}
```

main函数的主要功能时检查输入程序的参数，然后调用InjectDLL函数。InjectDLL函数是用来进行dll注入的核心，其作用是使目标进程自行调用LoadLibrary这个api。

```
//InjectDLL.cpp#include "windows.h"#include "tchar.h" BOOL SetPrivilege(LPCTSTR lpszPrivilege, BOOL bEnablePrivilege) {    TOKEN_PRIVILEGES tp;    HANDLE hToken;    LUID luid;     if( !OpenProcessToken(GetCurrentProcess(),                          TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY,                           &hToken) )    {        _tprintf(L"OpenProcessToken error: %u\n", GetLastError());        return FALSE;    }     if( !LookupPrivilegeValue(NULL,           // lookup privilege on local system                              lpszPrivilege,  // privilege to lookup                               &luid) )        // receives LUID of privilege    {        _tprintf(L"LookupPrivilegeValue error: %u\n", GetLastError() );         return FALSE;     }     tp.PrivilegeCount = 1;    tp.Privileges[0].Luid = luid;    if( bEnablePrivilege )        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;    else        tp.Privileges[0].Attributes = 0;     // Enable the privilege or disable all privileges.    if( !AdjustTokenPrivileges(hToken,                                FALSE,                                &tp,                                sizeof(TOKEN_PRIVILEGES),                                (PTOKEN_PRIVILEGES) NULL,                                (PDWORD) NULL) )    {         _tprintf(L"AdjustTokenPrivileges error: %u\n", GetLastError() );         return FALSE;     }      if( GetLastError() == ERROR_NOT_ALL_ASSIGNED )    {        _tprintf(L"The token does not have the specified privilege. \n");        return FALSE;    }      return TRUE;} BOOL InjectDll(DWORD dwPID, LPCTSTR szDllPath){    HANDLE hProcess = NULL, hThread = NULL;    HMODULE hMod = NULL;    LPVOID pRemoteBuf = NULL;    DWORD dwBufSize = (DWORD)(_tcslen(szDllPath) + 1) * sizeof(TCHAR);    LPTHREAD_START_ROUTINE pThreadProc;     // #1. 使用 dwPID 获取目标进程(notepad.exe)句柄（PROCESS_ALL_ACCESS权限），然后就可以用 hProcess 控制进程.    if ( !(hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID)) )    {        _tprintf(L"OpenProcess(%d) failed!!! [%d]\n", dwPID, GetLastError());        return FALSE;    }     // #2. 在目标进程(notepad.exe) 内存中分配 szDllName 大小的内存，返回 pRemoteBuf 作为该缓冲区的地址.    pRemoteBuf = VirtualAllocEx(hProcess, NULL, dwBufSize, MEM_COMMIT, PAGE_READWRITE);     // #3. 将 myhack.dll 路径写入刚刚分配的缓冲区.    WriteProcessMemory(hProcess, pRemoteBuf, (LPVOID)szDllPath, dwBufSize, NULL);     // #4. 获取 LoadLibraryW() API 地址，kernel32.dll在每个进程中的加载地址相同（这个特性就是我们要利用的）.    hMod = GetModuleHandle(L"kernel32.dll");    pThreadProc = (LPTHREAD_START_ROUTINE)GetProcAddress(hMod, "LoadLibraryW");         // #5. 在 notepad.exe 中运行线程    hThread = CreateRemoteThread(hProcess, NULL, 0, pThreadProc, pRemoteBuf, 0, NULL); //CreateRemoteThread()驱使进程调用LoadLibrary()，进而加载指定的DLL文件    WaitForSingleObject(hThread, INFINITE);        CloseHandle(hThread);    CloseHandle(hProcess);     return TRUE;} int _tmain(int argc, TCHAR *argv[]){    if( argc != 3)    {        _tprintf(L"USAGE : %s <pid> <dll_path>\n", argv[0]);        return 1;    }     // change privilege    if( !SetPrivilege(SE_DEBUG_NAME, TRUE) )        return 1;     // inject dll    if( InjectDll((DWORD)_tstol(argv[1]), argv[2]) )        _tprintf(L"InjectDll(\"%s\") success!!!\n", argv[2]);    else        _tprintf(L"InjectDll(\"%s\") failed!!!\n", argv[2]);     return 0;}
```

下面来详细分析一下injectDll函数。

调用 OpenProcess这个API，借助程序运行时以参数形势传递过来的dwPID值，获取exe进程的句柄（PROCESS\_ALL\_ACCESS）。得到PROCESS\_ALL\_ACCESS之后，就可以用获取的句柄控制对应进程。

```
//获取目标的进程句柄hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID)
```

需要把即将加载的dll文件的路径通知目标进程。因为任何内存空间都无法进行写入操作，所以先使用VirtualAllocEx() API在目标进程的内存空间中分配一块缓冲区，且指定的缓冲区大小为dll文件路径字符串的长度。

``...