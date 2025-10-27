---
title: Mimikatz与Bypass Credential Guard的记录
url: https://buaq.net/go-147559.html
source: unSafe.sh - 不安全
date: 2023-02-02
fetch_date: 2025-10-04T05:28:03.989744
---

# Mimikatz与Bypass Credential Guard的记录

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

![](https://8aqnet.cdn.bcebos.com/043d5eb6a004627ef56721345c85dbea.jpg)

Mimikatz与Bypass Credential Guard的记录

本文内容主要参考Bypass Credential Guard项目，通过对这个项目代码的学习和理解，来更好的学习分析Mimikatz和Credential Guard
*2023-2-1 20:30:0
Author: [xz.aliyun.com(查看原文)](/jump-147559.htm)
阅读量:48
收藏*

---

本文内容主要参考Bypass Credential Guard项目，通过对这个项目代码的学习和理解，来更好的学习分析Mimikatz和Credential Guard这两个在转储凭证时必不可少的因素。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201201651-4ee0e4a8-a22a-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201201715-5d0fa870-a22a-1.png)

**Mimikatz和sekurlsa::wdigest分析**
了解这两个首先我们需要针对lsass进程进行调试学习，其主要用于本地安全和登陆策略
调试一下lsass进程 来深入了解一下 wdigest.dll 和 Credential Guard是怎样保护lsass进程的，以及我们该用怎样的方法去进行bypass.
测试调试环境 Win1909-18363.592
调试lsass.exe 得从内核调试才行，因为直接windbg附加的话会被告警然后重新启动停止运行。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201201904-9df43c3e-a22a-1.png)

!process 0 0 lsass.exe 获取进程地址 通过EPROCESS 确定地址 然后调试会话切换到 lsass进程
.process /i /p /r address lm 即可显示我们现在可以访问wdigest.dll的内存空间

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201201916-a5909b72-a22a-1.png)

查看Mimikate 源代码，可以发现其针对于不同的架构是在内存中识别凭证，其过程是通过扫描签名完成的。

```
#elif defined(_M_X64)
BYTE PTRN_WIN5_PasswdSet[]  = {0x48, 0x3b, 0xda, 0x74};
BYTE PTRN_WIN6_PasswdSet[]  = {0x48, 0x3b, 0xd9, 0x74};
KULL_M_PATCH_GENERIC WDigestReferences[] = {
    {KULL_M_WIN_BUILD_XP,       {sizeof(PTRN_WIN5_PasswdSet),   PTRN_WIN5_PasswdSet},   {0, NULL}, {-4, 36}},
    {KULL_M_WIN_BUILD_2K3,      {sizeof(PTRN_WIN5_PasswdSet),   PTRN_WIN5_PasswdSet},   {0, NULL}, {-4, 48}},
    {KULL_M_WIN_BUILD_VISTA,    {sizeof(PTRN_WIN6_PasswdSet),   PTRN_WIN6_PasswdSet},   {0, NULL}, {-4, 48}},
};
#elif defined(_M_IX86)
BYTE PTRN_WIN5_PasswdSet[]  = {0x74, 0x18, 0x8b, 0x4d, 0x08, 0x8b, 0x11};
BYTE PTRN_WIN6_PasswdSet[]  = {0x74, 0x11, 0x8b, 0x0b, 0x39, 0x4e, 0x10};
BYTE PTRN_WIN63_PasswdSet[] = {0x74, 0x15, 0x8b, 0x0a, 0x39, 0x4e, 0x10};
BYTE PTRN_WIN64_PasswdSet[] = {0x74, 0x15, 0x8b, 0x0f, 0x39, 0x4e, 0x10};
BYTE PTRN_WIN1809_PasswdSet[] = {0x74, 0x15, 0x8b, 0x17, 0x39, 0x56, 0x10};
KULL_M_PATCH_GENERIC WDigestReferences[] = {
    {KULL_M_WIN_BUILD_XP,       {sizeof(PTRN_WIN5_PasswdSet),   PTRN_WIN5_PasswdSet},   {0, NULL}, {-6, 36}},
    {KULL_M_WIN_BUILD_2K3,      {sizeof(PTRN_WIN5_PasswdSet),   PTRN_WIN5_PasswdSet},   {0, NULL}, {-6, 28}},
    {KULL_M_WIN_BUILD_VISTA,    {sizeof(PTRN_WIN6_PasswdSet),   PTRN_WIN6_PasswdSet},   {0, NULL}, {-6, 32}},
    {KULL_M_WIN_MIN_BUILD_BLUE, {sizeof(PTRN_WIN63_PasswdSet),  PTRN_WIN63_PasswdSet},  {0, NULL}, {-4, 32}},
    {KULL_M_WIN_MIN_BUILD_10,   {sizeof(PTRN_WIN64_PasswdSet),  PTRN_WIN64_PasswdSet},  {0, NULL}, {-6, 32}},
    {KULL_M_WIN_BUILD_10_1809,  {sizeof(PTRN_WIN1809_PasswdSet),    PTRN_WIN1809_PasswdSet},    {0, NULL}, {-6, 32}},
};
```

我们这里着重关注 PTRN\_WIN6\_PasswdSet 所示的签名 可以看到有针对于不同架构的定义
我们可以通过其扫描机制确定 解密过程中参与的函数 也是提权凭据的关键 通过值我们可以定位到
wdigest.dll 如下的函数
LogSessHandlerPasswdSet 从名字可以大概理解到这是一个有关乎缓存中密码设置的，

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202011-c65b7a5c-a22a-1.png)
继续分析查看交叉引用的话可以发现在其被调用存在这么一个函数 SpAcceptCredentials
SpAcceptCredentials 是一个从Wdigest.dll 导出的函数 ，msdn对其有着一定的解释

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202054-dfdc79d6-a22a-1.png)

```
NTSTATUS Spacceptcredentialsfn(
  [in] SECURITY_LOGON_TYPE LogonType,
  [in] PUNICODE_STRING AccountName,
  [in] PSECPKG_PRIMARY_CRED PrimaryCredentials,
  [in] PSECPKG_SUPPLEMENTAL_CRED SupplementalCredentials
)
```

根据msdn的描述，可以确定我们的方向没错，可以看到凭据是通过此回调函数传递.
然后下个断点继续查看 验证一下

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202124-f1c4e16a-a22a-1.png)
触发断点 runas /USER:renyimen /netonly cmd.exe 查看调用的参数，传入的凭据

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202134-f76dbce0-a22a-1.png)
查看寄存器的值发现，我们传入的用户名 主机名和输入的密码都是明文的发送传进来的。
从调用栈其实可以发现wdigest.dll 还有关于lsasrv.dll的参与
分析lsasrv! 调用的系列函数加上分反编译lsasrv.dll 可以明白主要是lsasrv做的凭证的加解密处理

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202144-fd7081cc-a22a-1.png)
分析lsasrv!LsapUpdateNamesAndCredentials 断点调用发现函数LsaProtectMemory，于是断点发现确实经过.

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202155-041f5142-a22b-1.png)
而在其中真正实现的函数是LsaEncryptMemory

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202203-08b9b1ca-a22b-1.png)
而LsaEncryptMemory 实际上也是通过BCryptEncrypt去实现具体功能

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202211-0d9b6b34-a22b-1.png)
BCryptEncrypt 又是由bcrypt.dll导出的，通过断点已经确定加密的流程就是如此

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202220-12db57c6-a22b-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202224-155d0a62-a22b-1.png)

经过分析总结调用过程 BCryptEncrypt -->ApplyEncryptionPadding -->BCryptGenRandom

```
NTSTATUS __stdcall BCryptEncrypt(
        BCRYPT_KEY_HANDLE hKey,
        PUCHAR pbInput,
        ULONG cbInput,
        void *pPaddingInfo,
        PUCHAR pbIV,
        ULONG cbIV,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG *pcbResult,
        ULONG dwFlags)
```

通过msdn对此函数的介绍 可以明白 hkey是秘钥是句柄，pbinput 包含明文存放的地址，cbinput是加密的字节数，padding就是填充信息，pbiv为偏移
具体的算法我们先不用管，大致就是lsasrv是实现对明文凭证的加密，而具体算法实现的是通过bcrypt，然后通过msdn对于算法函数参数的介绍，我们已经明白关键是秘钥的生成。所以如果要解密Wdigest的凭据的话，就肯定需要获取到秘钥的信息。
然后这一步我们就可以看看mimikatz是如何做的，因为既然mimikatz是可以获取到没有被保护的凭证，那么肯定有其获取的办法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202255-27d7e3a6-a22b-1.png)
如图我们可以在其中获取到Windows 版本和结构的完整签名列表，mimikatz这一步跟上边的签名搜索异曲同工也是在内存中搜索加密的秘钥。然后再通过计算其偏移提取出来。这样就完成了一个WDigest 缓存凭证被抓取和解密的过程。
下一步就是 绕过 保护的过程了。
**UseLogonCredential与绕过Credential Guard**
首先因为转储明文凭据这个机制在微软看来已经并不安全，于是微软决定默认禁用对这一遗留的机制问题。当然微软也会有考虑一些用户可能正在使用 WDigest，所以讲这个启动和关闭的决定权也留给了用户，因此提供重新启用和关闭它的选项。也就是注册表
HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential
UseLogonCredential 在这种情况下催生出来。默认情况下是不存在这一项的

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202333-3e6f3ccc-a22b-1.png)

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 0 /f
将其从“0”切换为“1”会强制 WDigest 再次开始缓存凭据
```

在 wdigest.dll 内部，直接搜索一下关键词UseLogonCredential，并且该变量是在注册表内可控的 再加上关于注册表操作的API，最后发现 wdigest!SpInitialize

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202352-49dca6bc-a22b-1.png)
从上述代码我们可以明白了 ，其通过 g\_fParameter\_UseLogonCredential 变量来确定系统是否设置了 UseLogonCredential 注册表键值。RegQueryValueExW也是用来检索当前注册表UseLogonCredential的键值。
通过了解 WDigest.dll 中的哪些变量控制凭据缓存，那么我们是否可以在不更新注册表的情况下修改它？在内核调试下这可以轻松做到。
首先当前系统禁用了 Wdigest，并且 Credential Guard 没有启用

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202409-53da9264-a22b-1.png)
然后进行测试 ed wdigest!g\_fParameter\_UserLogonCredential 1

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202417-58dd371c-a22b-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202421-5af97b28-a22b-1.png)
成功修改。 此时然后还有一个变量g\_IsCredGuardEnabled
这个变量就是重点了，它主要是保存模块内 Credential Guard 的状态，也就是我们主要绕过的目标。
而且它还决定了Wdigest是否使用 Credential Guard 兼容的功能。根据老办法搜索可以看到如下代码分析，g\_fParameter\_UserLogonCredential 和 g\_IsCredGuardEnabled 都跟我们是否开启Credential Guard 的状态有关系。 那么我们就可以在修改g\_fParameter\_UserLogonCredential同时将这个值也修改为0或者1，来进行尝试看是否可以成功bypass。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230201202437-64929aac-a22b-1.png)
关键代码分析
具体实现来结合一下github BypassCredGuard项目代码分析一下
首先最主要的肯定要通过RtlGetNtVersionNumbers 获取操作系统的版本，这样才能保证后续的正常运行。

```
int wmain(int argc, wchar_t* argv[])
{
    HANDLE hToken = NULL;

    RtlGetNtVersionNumbers(&NT_MAJOR_VERSION, &NT_MINOR_VERSION, &NT_BUILD_NUMBER);
    // Open a process token and get a process ...