---
title: 反调试常见技法
url: https://mp.weixin.qq.com/s/GfTaHNd5O0Rpzwuwjap9EA
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:43:02.749890
---

# 反调试常见技法

# 反调试常见技法

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 反调试常见技法

# 反调试API

IsDebuggerPresent：

读取进程环境块 (PEB) 中的 BeingDebugged 标志。函数返回 BOOL 类型；返回 0（FALSE）代表未被调试，返回非 0（TRUE）代表进程正在被用户态调试器附加。

CheckRemoteDebuggerPresent:

与IsDebuggerPresent函数效果几乎一致。用于检测本地机器中的一个进程是否运行在调试器中，而不是检测远程主机的调试器。同时可以探测系统其他进程是否被调试。函数用法将一个进程句柄作为参数，检查这个句柄对应的进程是否被调试器附加。同时，CheckRemoteDebuggerPresent也可以通过传递自身进程句柄探测自己是否被调试

# NtQueryInformationProcess

该函数是Ntdll.dll中的一个原生态API，它用来提取一个给定进程的信息。它的第一个参数是进程句柄，第二个参数告诉我们它需要提取进程信息的类型，例如将该参数置为ProcessDebugPort(值为7)，将会告诉你这个句柄标识的进程是否正在被调试。如果进程正在被调试，则返回调试端口，否则返回0

# 手动检测

检测BeingDebugged属性，BeingDebugged为0则代表没有调试器附加

```
mov     eax, large fs:30hmov     bl, [eax+2]
```

# 系统痕迹检测

查找调试器引用的注册表项如

```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
```

该表项指定当应用程序发生错误时，触发哪一个调试器。默认情况下，它被设置为Dr.Watson如果该注册表的键值被修改了，则恶意代码就可能确定它正在被调试

找调试器窗口的类名或标题

```
if(FindWindow(”OLLYDBG”,0)==NULL)
```

# 调试器行为

# INT扫描

```
call            $+5pop             edisub		edi,5mov		ecx,400hmov		eax,0CChrepne	scasbjz		DebuggerDetected
```

这段代码首先执行一个函数调用，随后用pop指令将EIP寄存器的值存入EDI。然后将EDI设置为代码的开始。接下来，扫描这段代码的0xCC字节。如果发现了0xCC字节，证明存在调试器。

# 时钟检测

使用rdtsc指令（操作码0x0F31）

rdtsc指令返回至系统重新启动以来的时钟数，并且将其作为一个64位的值存入edx:eax中。恶意代码运行两次rdtsc指令，然后比较两次读取之间的差值

```
rdtscxor ecx,ecxadd ecx,eaxrdtscsub eax,ecxcmp eax,0xFFFjb NoDebugger
```

# 使用QueryPerformanceCounter和GetTickCount

GetTickCount

```
a = GetTickCount();MaliciousActivityFunction();b = GetTickCount(); delta = b - a;if ((delta) > 0x1A){    //Debugger Detected}
```

QueryPerformanceCounter

```
QueryPerformanceCounter(&PerformanceCount);QueryPerformanceCounter(&v4);if((v4.LowPart - PerformanceCount.LowPart) > 1200){//Debugger Detected}
```

# 干扰调试器

使用tls回调

```
void __stdcall TlsCallback_0(int a1, int a2, int a3){  if ( a2 == 1 && FindWindowA(ClassName, 0) )    exit(0);  if ( a2 == 2 )    sub_401020();}
```

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
推荐
，轻点两下取消推荐
分享
留言
收藏
听过