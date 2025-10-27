---
title: 64位下使用回调函数实现监控
url: https://buaq.net/go-130936.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:54:56.749744
---

# 64位下使用回调函数实现监控

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ff87de50843abb90bad7a201ecdd375f.jpg)

64位下使用回调函数实现监控

在32位的系统下，我们想要实现某些监控十分简单，只需要找到对应的API实现挂钩操作即可检测进程。但在64位系统下随着Patch Guard的引入，导致我们如果继续使用挂钩API的方式进行监控会出现不可
*2022-10-14 21:59:26
Author: [mp.weixin.qq.com(查看原文)](/jump-130936.htm)
阅读量:26
收藏*

---

在32位的系统下，我们想要实现某些监控十分简单，只需要找到对应的API实现挂钩操作即可检测进程。但在64位系统下随着`Patch Guard`的引入，导致我们如果继续使用挂钩API的方式进行监控会出现不可控的情况发生。微软也考虑到了用户程序的开发，所以开放了方便用户调用的系统回调API函数，在64位系统下的监控，使用系统回调相对于直接hook的方式往往是更值得青睐的一方。

## PsSetCreateProcessNotifyRoutineEx

这个函数主要是设置进程回调监控进程创建与退出

```
NTSTATUS PsSetCreateProcessNotifyRoutineEx(
;
```

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0gVhYYXWWX7ucuSrrsR3SibvhzKRFYrKWiapXwzXO04mDpvgvv1r7cIeg/640?wx_fmt=png)

`PsSetCreateProcessNotifyRoutineEx`这个函数并不是随便就能够使用的，微软为了确保安全性要求拥有数字签名的驱动才能够使用此函数。这里微软如何检测是否有数字签名呢？这里就使用到了强制完整性检查

强制完整性检查是一种确保正在加载的二进制文件在加载前需要使用签名的策略，`IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY`标志在链接时通过使用`/integritycheck`链接器标志在PE头中进行设置，让正在加载的二进制文件必须签名，这个标志使windows内存管理器在加载时对二进制文件进行签名检查

那么微软就是通过加载二进制文件时是否存在标志来确认驱动的发布者身份是否为已知状态，这就是强制完整性检查

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0GbDjVt64CxlRtlb3wQpnJWozQRDb9cSLHE0TlPIhMEEhv3BbJvbg0w/640?wx_fmt=png)

这里在内核里面，windows使用到`MmVerifyCallbackFunction` 这个内核函数来判断

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0ich2Cs3MniaKR3Z0ibaJ2Q2gd3HdXWh1syBkw7RJRBFNhkff4p4VCibf8w/640?wx_fmt=png)

到IDA里面继续跟`MmVerifyCallbackFunction`这个函数，发现其逻辑就是通过比较`[rax+68h]`是否包含了0x20来判断是否拥有正确的数字签名

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0fL6libBqibbWPhkfq0cxGPtMYbacLIY26VGMxzCbBuUia0od5ibxeFCfrA/640?wx_fmt=png)

这里的`rax`表示`DriverSection`，而`DriverSection`指向的是`_LDR_DATA_TABLE_ENTRY`结构，那么`[rax + 0x68]`指向的就是`ProcessStaticImport`

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0CHzgS89MCrmVYVZtI51GFOCFVnMmf5AaSrSkPCCK34nm2VKrcIzxVA/640?wx_fmt=png)

那么如果我们要使用`PsSetCreateProcessNotifyRoutineEx`这个函数就需要拥有数字签名，这里我们就可以将`DriverObject->DriverSection->Flags`的值与`0x20`按位或即可

这里我们就可以编写一个绕过强制完整性检查的函数，注意一下在32位和64位结构体的定义不同，需要分开定义

```
BOOLEAN bypass_signcheck(PDRIVER_OBJECT pDriverObject)
{
#ifdef _WIN64
 typedef struct _KLDR_DATA_TABLE_ENTRY
 {
  LIST_ENTRY listEntry;
  ULONG64 __Undefined1;
  ULONG64 __Undefined2;
  ULONG64 __Undefined3;
  ULONG64 NonPagedDebugInfo;
  ULONG64 DllBase;
  ULONG64 EntryPoint;
  ULONG SizeOfImage;
  UNICODE_STRING path;
  UNICODE_STRING name;
  ULONG   Flags;
  USHORT  LoadCount;
  USHORT  __Undefined5;
  ULONG64 __Undefined6;
  ULONG   CheckSum;
  ULONG   __padding1;
  ULONG   TimeDateStamp;
  ULONG   __padding2;
 } KLDR_DATA_TABLE_ENTRY, *PKLDR_DATA_TABLE_ENTRY;
#else
 typedef struct _KLDR_DATA_TABLE_ENTRY
 {
  LIST_ENTRY listEntry;
  ULONG unknown1;
  ULONG unknown2;
  ULONG unknown3;
  ULONG unknown4;
  ULONG unknown5;
  ULONG unknown6;
  ULONG unknown7;
  UNICODE_STRING path;
  UNICODE_STRING name;
  ULONG   Flags;
 } KLDR_DATA_TABLE_ENTRY, *PKLDR_DATA_TABLE_ENTRY;
#endif
 PKLDR_DATA_TABLE_ENTRY pLdrData = (PKLDR_DATA_TABLE_ENTRY)pDriverObject->DriverSection;
 pLdrData->Flags = pLdrData->Flags | 0x20;

return TRUE;

}
```

到这里我们就已经绕过了微软的强制完整性检查，能够调用`PsSetCreateProcessNotifyRoutineEx`函数，可以看到`PsSetCreateProcessNotifyRoutineEx`的第一个参数指向`CREATE_PROCESS_NOTIFY_ROUTINE_EX`，来执行我们需要执行的回调函数，这里我们继续看`PCREATE_PROCESS_NOTIFY_ROUTINE_EX`这个结构

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0srRdetibJYVmQtjqiacW1L4UAXqrdZAf5kib2PC4yneydL5EXAvolVxNA/640?wx_fmt=png)

## PCREATE\_PROCESS\_NOTIFY\_ROUTINE\_EX

第一个参数是`Process`，指向`EPROCESS`结构，第二个参数`ProcessId`就是PID，第三个参数`CreateInfo`是一个指向`PS_CREATE_NOTIFY_INFO`的指针，当它为`NULL`时表明进程退出，不为`NULL`时表明进程创建，里面存储着要创建的进程信息

```
PCREATE_PROCESS_NOTIFY_ROUTINE_EX PcreateProcessNotifyRoutineEx;

void PcreateProcessNotifyRoutineEx(
  [_Inout_]           PEPROCESS Process,
  [in]                HANDLE ProcessId,
  [in, out, optional] PPS_CREATE_NOTIFY_INFO CreateInfo
)
{...}
```

msdn的定义如下

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0lgMHmGOXSwpj7P6YAMibxOibgicvqLY7fQsL2s6jx63QSxib0FicoAXOKdw/640?wx_fmt=png)

然后我们再去看一下`PS_CREATE_NOTIFY_INFO`

## PS\_CREATE\_NOTIFY\_INFO

```
typedef struct _PS_CREATE_NOTIFY_INFO {
  SIZE_T              Size;
  union {
    ULONG Flags;
    struct {
      ULONG FileOpenNameAvailable : 1;
      ULONG IsSubsystemProcess : 1;
      ULONG Reserved : 30;
    };
  };
  HANDLE              ParentProcessId;
  CLIENT_ID           CreatingThreadId;
  struct _FILE_OBJECT *FileObject;
  PCUNICODE_STRING    ImageFileName;
  PCUNICODE_STRING    CommandLine;
  NTSTATUS            CreationStatus;
} PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO;
```

msdn定义如下

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0n3m84jIsQx9MdOSTbSOGv1URwYgo0ISGm8PrwnbHkNCh2zn6OHT4rg/640?wx_fmt=png)

这里的话我们要注意两个值，一个是`ImageFileName`即要创建的进程名，一个是`CreationStatus`，我们可以看到msdn里面说驱动程序可以将此值修改为错误代码以防止创建进程，这里我们如果想阻止进程创建就可以把这个值设置为`STATUS_UNSUCCESSFUL`

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY00YLaxjUgUicph1q8998Ls7sEMTaCPVkyMgYICHAeRicRDbl1lQEsofJg/640?wx_fmt=png)

我们去WRK里面看一下实现，这个API是64位才有的，所以在WRK里面是没有`PsSetCreateProcessNotifyRoutineEx`这个函数的，但是在32位下有一个`PsSetCreateProcessNotifyRoutine`，我们看一下

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0Svx067SlxcXwIicWiaiajTjiauoGbeyn756IlWua05ib8XwZibfPzXic1Kd7A/640?wx_fmt=png)

通过源码可以发现是操作数组，这个数组里面存放的是我们填写的回调，而操作系统会依次调用回调，那我们跟随数组查看发现是个定长数组，里面只有8项，在64位系统下，这个数组的长度变为了64项

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0JI4tsNaUXHiaBx2umF5L3JExqH4oamCBVEMtKIsqat4Zv20AZZYB0Ag/640?wx_fmt=png)

根据`PCREATE_PROCESS_NOTIFY_ROUTINE_EX`的结构定义回调函数

```
VOID CreateProcessNotifyEx(
    __inout PEPROCESS  Process,
    __in HANDLE  ProcessId,
    __in_opt PPS_CREATE_NOTIFY_INFO  CreateInfo
    );
```

那么我们这里通过`PsSetCreateProcessNotifyRoutineEx`设置回调函数，通过判断`status`的返回值判断回调函数是否设置成功

```
NTSTATUS SetReFunction()
{
 NTSTATUS status = PsSetCreateProcessNotifyRoutineEx((PCREATE_PROCESS_NOTIFY_ROUTINE_EX)CreateProcessNotifyEx, FALSE);
    if (!NT_SUCCESS(status))
    {
        DbgPrint("回调函数设置失败, status=%X", status);
    }
    else
    {
        DbgPrint("进程监控已开启\r\n");
    }
}
```

然后进行回调函数的实现

```
VOID CreateProcessNotifyEx(PEPROCESS Process, HANDLE ProcessId, PPS_CREATE_NOTIFY_INFO CreateInfo)
```

首先判断`CreateInfo`的值，如果为`NULL`则表示进程退出，如果不为`NULL`才为进程的创建

```
if (CreateInfo == NULL)
{
    DbgPrint("进程退出\n");
    return;
}
```

那么这里通过`PsGetProcessImageFileName`获取进程名之后进行判断，如果是我们想要拦截的进程就通过设置`CreationStatus`的值为`STATUS_UNSUCCESSFUL`来阻止进程的创建

```
else
{
    pszImageFileName = PsGetProcessImageFileName(Process);

if (pszImageFileName)
        DbgPrint("新创建的进程是:%s\r\n", pszImageFileName);
    if (strcmp(pszImageFileName, "test.exe") == 0)
    {
        CreateInfo->CreationStatus = STATUS_UNSUCCESSFUL;
        DbgPrint("拦截进程:%s成功\r\n", pszImageFileName);
    }
}
```

这里我们的回调函数就已经完成，这里需要注意，在卸载驱动的时候就需要将回调函数摘除，否则新创建或者退出的进程会因为找不到回调函数而导致蓝屏

```
VOID DriverUnload(IN PDEVICE_OBJECT driverObject)
{
    NTSTATUS status = PsSetCreateProcessNotifyRoutineEx((PCREATE_PROCESS_NOTIFY_ROUTINE_EX)CreateProcessNotifyEx, TRUE);

    if (!NT_SUCCESS(status))
    {
        DbgPrint("回调函数删除失败\r\n status=%X", status);
    }
    else
    {
        DbgPrint("回调函数成功删除\r\n");
    }
    DbgPrint("驱动卸载完成\r\n");
}
```

## 实现效果

首先注册一下驱动

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY0HjSEyDyn9LzhYiaygR1OQDNkuXIVwbJu7xEicmgAMqUo2HYiaG7VPszaw/640?wx_fmt=png)

然后这里首先执行一下我们的exe

![](https://mmbiz.qpic.cn/mmbiz_png/ibZ6uZjjH3v7dU0M5IG5w7txkGOuviaGY06RhF3b8LU4BuCzb0FCYMKb1NEAyyhZq5L1XME2hzwLyr577o9YeRAg/640?wx_fmt=png)

然后加载我们的驱动可以看到这里`test...