---
title: 游戏安全入门-扫雷分析&远程线程注入
url: https://mp.weixin.qq.com/s/2Zd0rTXFMl0bPaWhxjkCvA
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:28:21.745767
---

# 游戏安全入门-扫雷分析&远程线程注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdiaicFcUXnCjnnEF4h6H4kUBozjeHJTibc9NANCHNIhapgVkGp3TiaK3xIg/0?wx_fmt=jpeg)

# 游戏安全入门-扫雷分析&远程线程注入

IX221
IX221

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/TL4Y9UAcgrv4ib11v7vDSBJYcwqpJYQAEhc55bHr0HwZTvddqsoibgBc0kanr5JGUpZ0KkxNp1z0XL1VFeFux9mQ/640?wx_fmt=gif&from=appmsg)

**声明：本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。**

# 前言

无论学习什么，首先，我们应该有个目标，那么入门windows游戏安全，脑海中浮现出来的一个游戏 -- 扫雷，一款家喻户晓的游戏，虽然已经被大家分析的不能再透了，但是我觉得自己去分析一下还是极好的，把它作为一个小目标再好不过了。 我们编写一个妙妙小工具，工具要求实现以下功能：时间暂停、修改表情、透视、一键扫雷等等。 本文所用工具： Cheat Engine、x32dbg(ollydbg)、Visual Studio 2019

# 扫雷游戏分析

游戏数据在内存中是地址，那么第一个任务，找内存地址 打开CE修改器

## 修改时间->时间暂停

计数器的时间是一个精确的值，所以我们通过精确数值扫描出来，游戏开始之前计数器上的数是0，所以我们扫描0。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPd5wzlTcTPD1mINECz6z2SkV3U4lhNJWAmGlaPVeSkJiaGrLVHarDF2VQ/640?wx_fmt=other&from=appmsg "null")

时间在变化，选择介于什么数值之间再次扫描![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdYSJPDibUbBvM7XmoEh0ln5jPAQXYTQy0iaC7vxMKQ22N1ejROca9YpYg/640?wx_fmt=other&from=appmsg "null")

可得 0x100579c --- winmine.exe+579C![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdNQmw0rXpm2SAlNxKJ2iacqeicdGAaeEUEnhFAm5CRPvV5btsm47koKDg/640?wx_fmt=other&from=appmsg "null")

我们发现这个数据都是直接通过基址 + 固定偏移能直接得到的。 然后我们对数据去找 **是什么改写了这个地址**，得到一个指令和指针：![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPd6cCU0ZOA5B1TmDMZbqicEJnqVAGoibiajdb9q7WR5u1w8WUYgFhD0bYUw/640?wx_fmt=other&from=appmsg "null")

时间：0x100579c

## 修改表情 - 没啥用

修改表情这个功能怎么搞我觉得还是很容易想到的，这个按钮的作用是重新开始游戏，开始游戏，游戏胜利，游戏失败。 （表情的状态被分成了两个变量（4byte）来控制） 所以它是一种状态，所以我们通过0和1进行扫描，游戏进行状态输入1进行扫描，还原游戏之后输入0进行扫描。 首先是游戏进行状态，输入1进行扫描![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdksgEHTz4ObB7kVK9GjexPLtWJicnjDdx93Kib6vtbyD4tJj22n97nKVQ/640?wx_fmt=other&from=appmsg "null")

再点击表情，将游戏还原，输入0开始扫描![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdkMJeDjhjGvPy9nTlufRgYCibAyJS4km0CSiaiaJuZbA6n3O4m11mPmWqA/640?wx_fmt=other&from=appmsg "null")

如此反复进行扫描，得到表情的内存地址 0x1005164 -- winmine.exe+5164![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdwCWIFTrb1tPqm0CukATVAibwQA9vZOxsNewBeQ9oicBvYDId37GZaEaQ/640?wx_fmt=other&from=appmsg "null")但是嘞，修改成2或者3，表情没有心得反应，所以控制游戏胜利和游戏失败的是其他的地址，我们知道，一般来说，一个功能的代码在内存中基本上都是连续的，(就像你修改一个游戏的血量，浏览血量内存块，你可以发现怒气，蓝量等内存地址) 所以，我们浏览内存![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdx4Sdia9FgShGZ8VH8P5ERibELS8MnNANWHJiazHtQ8iabgVeN5PL00MMDQ/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdUcmlicF635VPKDWtrQTTWBtR21sibqZicSTeHclZeKlHy5ZRQ4E9PZ9ZQ/640?wx_fmt=other&from=appmsg "null")

0x1005164-4 = 0x1005160 修改为3，发现出现了戴墨镜的表情（游戏胜利）**但是这个胜利知识一个状态，并不能说明扫雷完成**.![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdkud1cUfMBYwAwRdPxTGxiagr7dpNV44ZMVHXw8bwdWoiaCyfMVy3tZkA/640?wx_fmt=other&from=appmsg "null")

表情：0x1005160与0x1005164

## 透视 - 显示雷区

思考游戏结束的时候会自动显示所有的雷，因此我们动态调试，看看在哪个函数调用之后会显示所有的雷![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdcKic1POAD3PI1lNbJFIzWj31ibo0p4UR2qGOg8iabq0KnHOXp1dlm0ia7Q/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdKsw7kic0SeLoHXYhN3yfF00D07n1IkZ5f0PVYB8NP0cvoBrsragbg7A/640?wx_fmt=other&from=appmsg "null")

经过几次的动态调试之后发现：0x2F80函数是我们要找的结果。![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdRq7fJvLgM2icR55Hyqm4giaEcHOndNiahDLQ0egQkgs4uia3M1gMQo88NA/640?wx_fmt=other&from=appmsg "null")

## 一键扫雷

通过透视，我们玩一把游戏，使得游戏胜利(点完最后一个)![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdcia936Zpa4n1vvR0wu8HhD7HMJSVSDGsy9mY9KqkC9PbGAKZXjXqIxA/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdv4al2xz1XvS0R2NO0nMrPz0Xd63dSQWJXR1kZ6iaABFJtk3cGuUfBAw/640?wx_fmt=other&from=appmsg "null")

然后后两个函数，是破纪录跟英雄榜的函数![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdSO618Q7MIN82spOvpWMW6fjPstdlrUH1TygicCmHI5oaiakDZKNsFT2g/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdk3kKMImPoVDYElcia5O1QAsEiaXd2GtEYbVmXALSYFOv2wZpPyic8F7fw/640?wx_fmt=other&from=appmsg "null")

ret来到了这儿，游戏通关了，来到了这儿，可以知道，这个0x347c就是判断输赢的函数 并且通过调试发现由一个参数 0 1 来控制，所以跟透视差不多，带个参数线程回调就完了![](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrusqoMzwmKn4G9ichs9qOtPdXEg2wQ00oLHNG1v0ZJmLIAtU3qDibwtt2IZtGzicbR7PLRfeSzgMkGVA/640?wx_fmt=other&from=appmsg "null")

# 编写妙妙小工具

怎么实现这个工具呢，当然是选择DLL注入 那么dll 怎么注入进去呢，这里选择远程线程注入 这里先简单介绍下什么是远程线程注入

## 前置知识-动态调用dll

主要就是这几个个 API：

### LoadLibraryA

加载指定 DLL 并返回模块句柄，参数为字符串，就是 dll 的路径。

### GetProcAddress

获取指定 dll 的导出函数的地址。 第一个参数是模块句柄，第二个参数是模块函数，返回值为函数的地址。 通过这两个函数，我们可以拿到所有函数的地址，然后就能进行调用。

### CreateThread - 远程线程注入

里面几乎只有一个参数，那就是线程回调函数，然后当然还有返回地址，返回线程 id 啥的，这里我们都可以不用管，几乎是与 Linux 的创建线程函数一致。 还有一个远程版本的叫 CreateRemoteThread，它可以给别的进程创建一个线程并可以在本进程创建那个进程调用的回调函数。我们可以在回调函数中加载指定的 dll，在 dllmain 的入口当中，有一个 switch 的四个选项。

```
// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"

BOOL APIENTRY DllMain( HMODULE hModule,//指向自身的句柄
                       DWORD  ul_reason_for_call,//调用原因
                       LPVOID lpReserved//隐式加载or显式加载
                     )
{
switch(ul_reason_for_call)
{
case DLL_PROCESS_ATTACH://附加到进程上时执行
case DLL_THREAD_ATTACH://附加到线程上时执行
case DLL_THREAD_DETACH://从线程上剥离时执行
case DLL_PROCESS_DETACH://从进程上剥离时执行
break;
}
return TRUE;
}
```

我们可以在 DLL\_PROCESS\_ATTACH 的选项中加入代码，让它在加载的时候调用执行。 那么我们的步骤是：

1. 1. 打开指定进程获得句柄
2. 2. 开辟远程进程的空间，分配可读可写段。
3. 3. 调用 WriteProcessMemory 将 dll 路径写入该内存区域。
4. 4. 创建远程线程，回调函数使用 LoadLibrary 加载指定 dll。
5. 5. 等待返回（loadLibrary返回）
6. 6. 释放空间
7. 7. 释放句柄
8. 8. 返回结果

   #### demo：

   `void Inject(DWORD ProcessId, const char* szPath)
   {
   //1.打开目标进程获取句柄
    HANDLE hProcess =OpenProcess(PROCESS_ALL_ACCESS, FALSE,ProcessId);
   printf("进程句柄:%p\n", hProcess);
   //2.在目标进程体内申请空间
    LPVOID lpAddress =VirtualAllocEx(hProcess,NULL,0x100, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
   //3.写入DLL路径
    SIZE_T dwWriteLength =0;
   WriteProcessMemory(hProcess, lpAddress, szPath,strlen(szPath),&dwWriteLength);
   //4.创建远程线程，回调函数使用 LoadLibrary 加载指定 dll
    HANDLE hThread =CreateRemoteThread(hProcess,NULL,NULL,(LPTHREAD_START_ROUTINE)LoadLibraryA, lpAddress,NULL,NULL);
   //5.等待返回（loadLibrary返回）
   WaitForSingleObject(hThread,-1);
   //6.释放空间
   VirtualFreeEx(hProcess, lpAddress,0, MEM_RELEASE);
   //7.释放句柄
   CloseHandle(hProcess);
   CloseHandle(hThread);
   //返回结果
   AfxMessageBox(L"完成");
   }`

   ## 编写DLL注入器

   ```cpp #include<windows.h> #include

   #include<time.h> #include<stdlib.h> #include<TlHelp32.h> DWORD FindProcess() {  HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS\_SNAPPROCESS, 0);  PROCESSENTRY32 pe32;  pe32 = { sizeof(pe32) };  BOOL ret = Process32First(hSnap, &pe32);  while (ret)  {  if (!wcsncmp(pe32.szExeFile, L"mine.exe", 11)) {      printf("Find winmine.exe Process %d\n", pe32.th32ProcessID);      return pe32.th32ProcessID;  }  ret = Process32Next(hSnap, &pe32);  }  return 0; } void Inject(DWORD ProcessId, const char\* szPath) {  //1.打开目标进程获取句柄  HANDLE hProcess = OpenProcess(PROCESS\_ALL\_ACCESS, FALSE, ProcessId);  printf("进程句柄:%p\n", hProcess);  //2.在目标进程体内申请空间  LPVOID lpAddress = VirtualAllocEx(hProcess, NULL, 0x100, MEM\_COMMIT | MEM\_RESERVE, PAGE\_READWRITE);  //3.写入DLL路径  SIZE\_T dwWriteLength = 0;  WriteProcessMemory(hProcess, lpAddress, szPath, strlen(szPath), &dwWriteLength);  //4.创建远程线程，回调函数使用 LoadLibrary 加载指定 dll  HANDLE hThread = CreateRemoteThread(hProcess, NULL, NULL, (LPTHREAD\_START\_ROUTINE)LoadLibraryA, lpAddress, NULL, NULL);  //5.等待返回（loadLibrary返回）  WaitForSingleObject(hThread, -1);  //6.释放空间  VirtualFreeEx(hProcess, lpAddress, 0, MEM\_RELEASE);  //7.释放句柄  CloseHandle(hProcess);  CloseHandle(hThread); }

int main() {     DWORD ProcessId = FindProcess();     while (!ProcessId) {         printf("未找到扫雷程序，等待两秒中再试\n");         Sleep(2000);         ProcessId = FindProcess();  ...