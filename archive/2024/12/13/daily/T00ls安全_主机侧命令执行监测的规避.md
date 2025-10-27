---
title: 主机侧命令执行监测的规避
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzYzODU5NQ==&mid=2247484894&idx=1&sn=513ddea2f76c9a5bc7e6b7e6986b9c25&chksm=cf1ea372f8692a649a82ba31296a0367a3ed3cbe91863b71f8d217351f73503a214f6d1fe09e&scene=58&subscene=0#rd
source: T00ls安全
date: 2024-12-13
fetch_date: 2025-10-06T19:39:44.590442
---

# 主机侧命令执行监测的规避

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkB4mPD62nMlPF5DEmzMoeLiaw6rUAAPnD8LBdO9sribsgAibFEBaSyBkwr1NyRFokDmwYNWBWZk5HQhq2NNFVQ7g/0?wx_fmt=jpeg)

# 主机侧命令执行监测的规避

原创

QWETVG

T00ls安全

# 使用场景

像一些0day防御系统，当我们打出来whoami等等极具`特征`的命令时，会有一个基于主机侧`命令执行检测`，会出现`告警`，那我们就需要进行一些`规避`，用来像权限查询，判断主站上有什么东西，我们该如何进行`信息收集`。

**场景为当我们的C2上线后，或WebShell直接上线之后,我们可以用一些Windows的api进行信息收集**

# GetUserNameW

**GetUserNameW：检索与当前线程关联的用户的名称**

```
#include <Windows.h>
#include <stdio.h>
#include <Psapi.h>
#include <LM.h>

int main{
        WCHAR userName[UNLEN +1];// 定义了一个宽字符数组用于存储用户名
        DWORD userNameLength = UNLEN +1;// UNLEN是一个预定义的宏，表示Windows用户名的最大长度，加1是为了存储字符串的终止符

if(GetUserNameW(userName,&userNameLength)){
// userNane是用来接收用户名的缓冲区指针
// &userNameLength，是指向DWORD类型的指针，表示缓冲区的大小，并在成功后返回实际的用户名长度
            wprintf(L"User: %ls\\n", userName);// 如果为True则会获取当前用户的用户名，并输出
}
else{
            wprintf(L"[-] E: %d",GetLastError());// 如果为False则会打印错误信息
}
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nMlPF5DEmzMoeLiaw6rUAAPnQajMbrG5OzicBaS6X55CriaEWmXd2WSHRXIjoQpQ9FyB0m5ZqCDElOKQ/640?wx_fmt=png&from=appmsg)

### 输出结果

这里我们用到了`GetUserNameW`这个Windows api（GetUserNameW是GetUserName的宽字符版本),宽字符版本使用 UTF-16 编码，适用于处理 Unicode 字符串。

这是函数定义

```
BOOL GetUserNameW(
  LPWSTR  lpBuffer,
  LPDWORD pcbBuffer
);
```

`lpBuffer`是一个`LPWSTR`类型的指向一个缓冲区的指针，用于接收当前用户的登录名。缓冲区的大小由`pcbBuffer`指定。

`pcbBuffe`r是一个`LPDWORD`类型指向一个变量，该变量指定`lpBuffer`缓冲区的大小（以字符为单位）。

在函数返回时，该变量包含复制到缓冲区中的字符数，包括终止的空字符。如果缓冲区大小不够，函数会失败，并在此变量中返回所需的缓冲区大小。

### 返回值为:

True，lpBuffer包含当前用户的`登录名`

False，GetLastError函数获取更多的`错误信息`

这里我们可以深入,会涉及两个东西，关于beacon：

一个是cs-bof加载

一个是inline-execute

**像我们一些高强的对抗的环境下，后续的信息收集一定是基于这种的情况下去进行，而不是打开cmd执行whoami这种**

# GetComputerNameExW

**GetComputerNameExW：检索与本地计算机关联的 NetBIOS 或 DNS 名称。这些名称是在系统启动时建立的，即系统从注册表中读取它们**

### 函数定义:

```
BOOL GetComputerNameExW(
  COMPUTER_NAME_FORMAT NameType,
  LPWSTR lpBuffer,
  LPDWORD nSize
);
```

`NameType`: 指定要获取的计算机名的格式，这个参数是一个COMPUTER\_NAME\_FORMAT枚举值 常用的枚举值包括：

* • ComputerNameNetBIOS: 获取 NetBIOS 名称。
* • ComputerNameDnsHostname: 获取 DNS 主机名。
* • ComputerNameDnsDomain: 获取 DNS 域名。
* • ComputerNameDnsFullyQualified: 获取 DNS 完全限定域名 (FQDN)。
* • ComputerNamePhysicalNetBIOS: 获取物理 NetBIOS 名称。
* • ComputerNamePhysicalDnsHostname: 获取物理 DNS 主机名。
* • ComputerNamePhysicalDnsDomain: 获取物理 DNS 域名。
* • ComputerNamePhysicalDnsFullyQualified: 获取物理 DNS 完全限定域名 (FQDN)。

`lpBuffer`: 指向一个缓冲区，用于接收计算机名称。

`nSize`: 指向缓冲区大小的指针。输入时为缓冲区的大小，以字符为单位；输出时为存储在缓冲区中的计算机名的字符数，包括终止的 null 字符。

### 返回值：

函数执行成功，返回 TRUE。

如果失败，返回 FALSE，可以使用 GetLastError 获取详细的错误信息

```
WCHAR hostName[UNLEN +1];
// 定义一个 WCHAR 数组 hostName 用于存储计算机的完全限定域名（FQDN）。
// UNLEN 是用户名的最大长度常量（256 字符），加上 1 是为了容纳终止的 null 字符。

DWORD hostNameLength = UNLEN +1;
// 定义一个 DWORD 类型的变量 hostNameLength，并将其初始化为 UNLEN + 1。
// 这个变量表示 hostName 数组的大小，以字符为单位。

if(GetComputerNameExW(ComputerNameDnsFullyQualified, hostName,&hostNameLength)){
    wprintf(L"Hostname: %ls\n", hostName);
}
// 调用 GetComputerNameExW 函数获取计算机的完全限定域名（FQDN）。
// 如果调用成功，输出计算机的主机名。

else{
    wprintf(L"[-] E: %d",GetLastError());
}
// 如果 GetComputerNameExW 调用失败，输出错误代码。

WCHAR dnshostName[UNLEN +1];
// 定义一个 WCHAR 数组 dnshostName 用于存储计算机的 DNS 域名。

DWORD DNShostNameLength= UNLEN +1;
// 定义一个 DWORD 类型的变量 DNShostNameLength，并将其初始化为 UNLEN + 1。
// 这个变量表示 dnshostName 数组的大小，以字符为单位。

if(GetComputerNameExW(ComputerNameDnsDomain, dnshostName,&DNShostNameLength)){
    wprintf(L"ComputerNameDnsDomain: %ls\n", dnshostName);
}
// 调用 GetComputerNameExW 函数获取计算机的 DNS 域名。
// 如果调用成功，输出 DNS 域名。

else{
    wprintf(L"[-] E: %d",GetLastError());
}
// 如果 GetComputerNameExW 调用失败，输出错误代码。

WCHAR CdnshostName[UNLEN +1];
// 定义一个 WCHAR 数组 CdnshostName 用于存储计算机的物理 DNS 域名。

DWORD CDNShostNameLength= UNLEN +1;
// 定义一个 DWORD 类型的变量 CDNShostNameLength，并将其初始化为 UNLEN + 1。
// 这个变量表示 CdnshostName 数组的大小，以字符为单位。

if(GetComputerNameExW(ComputerNamePhysicalDnsDomain,CdnshostName,&CDNShostNameLength)){
    wprintf(L"ComputerNamePhysicalDnsDomain: %ls\n",CdnshostName);
}
// 调用 GetComputerNameExW 函数获取计算机的物理 DNS 域名。
// 如果调用成功，输出物理 DNS 域名。

else{
    wprintf(L"[-] E: %d",GetLastError());
}
// 如果 GetComputerNameExW 调用失败，输出错误代码。
```

### 输出结果:

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nMlPF5DEmzMoeLiaw6rUAAPnDJ5rwiaoNWuY8OPKLiaXAOyESBP9A9ricgvvQT4JER5tr4Ypt3csel5xg/640?wx_fmt=png&from=appmsg)

# RtlGetVersion

**RtlGetVersion：返回有关当前正在运行的操作系统的版本信息**

### 函数定义

```
NTSTATUS RtlGetVersion(
  PRTL_OSVERSIONINFOW lpVersionInformation
);
```

`lpVersionInformation`: 指向 RTL\_OSVERSIONINFOW 结构的指针，该结构用于接收操作系统的版本信息

### 返回值

返回一个 NTSTATUS 类型的值，表示函数调用的结果。如果函数成功，返回的状态值通常为 STATUS\_SUCCESS（即 0）。

### 结构

```
typedef struct _OSVERSIONINFOW {
  ULONG dwOSVersionInfoSize; // 结构的大小（以字节为单位）
  ULONG dwMajorVersion;      // 操作系统的主版本号
  ULONG dwMinorVersion;      // 操作系统的次版本号
  ULONG dwBuildNumber;       // 操作系统的构建编号
  ULONG dwPlatformId;        // 操作系统平台标识
  WCHAR szCSDVersion[128];   // 服务包信息
} RTL_OSVERSIONINFOW, *PRTL_OSVERSIONINFOW;
```

```
#include <Windows.h>
#include <stdio.h>
#include <Psapi.h>
#include <LM.h>

// 定义函数指针类型
typedef NTSYSAPI NTSTATUS(WINAPI* procRtlGetVersion)(PRTL_OSVERSIONINFOW lpVersionInformation);

// 是将STATUS_SUCCESS作为0x00000000的一个替代符号，这样你可以在代码中使用STATUS_SUCCESS来表示操作成功
#define STATUS_SUCCESS 0x00000000

intmain(){
// 初始化一个 RTL_OSVERSIONINFOW 结构体，并将其所有成员设置为零
RTL_OSVERSIONINFOW osversioninfow ={0};

// 获取 ntdll.dll 模块的句柄，该模块包含了 Windows 的低级函数
HMODULE hntdll =GetModuleHandleA("ntdll.dll");

// 从 ntdll.dll 模块中获取 RtlGetVersion 函数的地址
procRtlGetVersion myRtlGetVersion =(procRtlGetVersion)GetProcAddress(hntdll,"RtlGetVersion");

// 如果成功检索并调用了 RtlGetVersion 函数
if(myRtlGetVersion(&osversioninfow)== STATUS_SUCCESS){
// 打印 Windows 操作系统的主版本号和次版本号
    wprintf(L"Windows Version: %lu.%lu\\n", osversioninfow.dwMajorVersion, osversioninfow.dwMinorVersion);

// 打印 Windows 操作系统的内部版本号
    wprintf(L"Windows Build: %lu\\n", osversioninfow.dwBuildNumber);
}
}
```

### 输出结果

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nMlPF5DEmzMoeLiaw6rUAAPnWI0e08LnWOKNxeT5syB47mSqWFM895l4GX8ALSqgqyibKx8UT4KFlzg/640?wx_fmt=png&from=appmsg)

像我们上升到xdr的对抗，走beacon内存加载，在beacon中就要完成`脱钩`的操作，如果没有做脱钩的话，我们就到更深一层的维度，更底层的调用。

`virtualprotect`为主，首先调用user32dll里面 转到kernel32dll 转到ntdll 最后通过syscall在内核中完成修改一块内存的保护属性。

# GetCurrentDirectory

**GetCurrentDirectory ：检索当前进程的当前目录**

### 函数定义

```
DWORD GetCurrentDirectory(
  DWORD  nBufferLength,  // 指定缓冲区的大小，单位为字符
  LPTSTR lpBuffer        // 指向存储当前目录路径的缓冲区
);
```

`nBufferLength:`指定缓冲区 lpBuffer 的大小，单位是字符数。这个大小应该足够大以容纳当前目录的路径，包括终止符 '\0'。

`lpBuffer:` 指向一个字符数组（缓冲区），用于接收当前目录的绝对路径。

### 返回值：

如果函数成功，返回值是存储在缓冲区中的字符串的长度。

如果缓冲区大小不足以存储路径，函数将返回所需的缓冲区大小（包括终止符），并且不会将路径存入lpBuffer中。

如果函数调用失败，返回值为0。在这种情况下，可以调用 GetLastError 函数来获取详细的错误信息。

```
WCHAR currentDir[MAX_PATH +1];
// 定义一个 WCHAR 数组 currentDir 用于存储当前目录路径。
// MAX_PATH 是 Windows 系统中定义的最大路径长度（通常为 260 字符），加上 1 是为了容纳结尾的 null 字符。

DWORD currentDirLength = MAX_PATH +1;
// 定义一个 DWORD 类型的变量 currentDirLength，并将其初始化为 MAX_PATH + 1。
// 这个变量表示 currentDir 数组的大小，以字符为单位。

if(GetCurrentDirectoryW(currentDirLength, currentDir)!=0){
    wprintf(L"Pwd: %ls\\n", currentDir);
}
// 调用 GetCurrentDirectoryW 函数获取当前工作目录。
// 如果调用成功，输出当前目录路径。

else{
    wprintf(L"[-] E: %d",GetLastError());
}
// 如果 GetCurrentDirectoryW 调用失败，输出错误代码。
```

### 输出结果

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nMlPF5DEmzMoeLiaw6rUAAPnnvhXL440aSru6GjvsgaS2O0YKm2EZOj2WCSPE4Uia4AgtZ0uiboQCzhg/640?wx_fmt=png&from=appmsg)

# GetTickCount64

**GetTickCount64：检索自系统启动以来经过的毫秒数**

来判断他到底会不会经常关机，如果动静不大，webshell独家 那就不需要维权

白加黑+测加载 白是在计划任务（很少的情况） --> 成本性问题 edr或xdr

常规的exe不要在有edr或xdr的服务器中进行启动

常规的exe进行维权 加启动项 计划任务 com劫持，但是我们不会有签名

侧重到webshell 隐匿性 打不打内存马

### 函数定义

```
ULONGLONG GetTickCount64(void);
这个函数不接受任何参数
```

### 返回值

返回一个 ULONGLONG 类型的值，该值表示自系统启动以来经过的时间（以毫秒为单位）

```
DWORD tickCount = (DWORD)GetTickCount64();
// 调用 GetTickCount64 函数获取系统启动后的运行时间（以毫秒为单位），并将其转换为 DWORD 类型。
// 注意：这里将 64 位的时间值强制转换为 32 位的 DWORD 类型，这在系统运行时间超过大约 49.7 天（即 32 位的最大值 4294967295 毫秒）后可能导致数据丢失。

DWORD dcuptime = ((tickCount / 1000) / 60);
// 将获取到的毫秒数除以 1000 转换为秒，再除以 60 转换为分钟。
// 结果是系统启动后的运行时...