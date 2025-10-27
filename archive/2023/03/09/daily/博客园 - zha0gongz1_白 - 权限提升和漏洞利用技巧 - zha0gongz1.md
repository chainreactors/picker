---
title: 白 - 权限提升和漏洞利用技巧 - zha0gongz1
url: https://www.cnblogs.com/H4ck3R-XiX/p/17192109.html
source: 博客园 - zha0gongz1
date: 2023-03-09
fetch_date: 2025-10-04T09:00:35.541442
---

# 白 - 权限提升和漏洞利用技巧 - zha0gongz1

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/zha0gongz1/)

# [zha0gongz1](https://www.cnblogs.com/zha0gongz1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/zha0gongz1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/zha0gongz1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [白 - 权限提升和漏洞利用技巧](https://www.cnblogs.com/zha0gongz1/p/17192109.html "发布于 2023-03-08 16:34")

总结梳理Windows提权的一些常见的技术或攻击手法

## Windows服务

### 1.不安全的服务文件权限或路径

#### 基本原理

Windows服务是一种在后台运行的计算机程序，它在概念上类似于Unix守护进程。

每个Windows服务都将其可执行文件的路径存储在称为`BINARY_PATH_NAME`的变量中。当启动服务时，会检查此变量并执行其下设置的`.exe`文件。

#### 步骤

**前提条件：Windows服务必须启用第3点权限，并且当前用户有启动或停止服务权限，否则必须等待系统重启才能执行恶意payload。**

1. 检查目标系统中的所有服务
2. 枚举服务的所有权限集
3. 查找`SERVICE_ALL_ACCESS`或`SERVICE_CHANGE_CONFIG`是否已启用（这些权限允许用户修改服务配置和 bin 路径）
4. 查询该服务以检查该服务是否以更高的权限运行
5. 可使用命令或恶意文件更改服务的 BINARY\_PATH\_NAME (binpath)
6. 重启或启动服务并获得更高权限shell

#### 实操

使用 [PowerUp](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1)脚本查找错误配置，枚举机器服务寻找打开了 binpath 的服务。

```
<#返回当前用户可以写入服务的路径或其配置的服务#>
powershell -ep bypass

.\powerup.ps

Get-ModifiableServiceFile
```

找到了一个名为“daclsvc”的服务，为避免工具误报，可使用[Accesschk工具](https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk)再次检查此服务以确认它确实设置了`SERVICE_ALL_ACCESS`或`SERVICE_CHANGE_CONFIG`权限。

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163043152-1172723745.png)

有启动 (service\_start)权限 、停止权限，也有权更改服务“daclsvc”的可执行文件路径的权限

进一步查看一下该服务以何种权限运行

**注意：大多数情况下，Windows会以 SYSTEM 或管理员权限运行所有服务**

以本地系统权限运行

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163058453-1889028233.png)

利用这个错误配置，可以使用`sc`或`service control`（默认安装）来更改此服务的可执行文件路径

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163109062-913747262.png)

可将其设置为反弹shell的可执行文件路径。再次使用`sc`查询以检查设置的新路径是否正确

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163125680-1837197817.png)

配置无误后，使用`net`（默认安装）启动此服务即可获得 SYSTEM 权限的shell

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163133918-1684014738.png)

服务已运行

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163235760-1341863589.png)

### 2.不安全的服务文件

#### 基本原理

可执行文件是包含可以由操作系统执行的机器码指令构成的文件，可以是特定于平台的，也可以是跨平台

#### 步骤

**前提条件：服务的 .exe（二进制文件）权限是可写的或启用`FILE_ALL_ACCESS`权限以及启动/停止服务的权限**

* 1.枚举所有服务以检查全部原始`.exe`（二进制文件）是否可写
* 2.使用恶意文件替换或更改原始二进制文件
* 3.刷新或启动该服务，该服务将执行其 `.exe` 并以 SYSTEM 权限运行上面写入的任何内容

#### 实操

使用 [winPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS/winPEASexe) 来枚举所有可执行文件权限配置错误的服务。

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163248155-739545463.png)

在 winpeas 探测结果中，我们可以看到`filepermsvc`服务的原始 `.exe` 为任意用户设置了`AllAccess`权限。简单来说就是“系统上的所有用户都可以对该文件进行任何操作（r、w、x）”，再次使用`accesschk`工具确认，这些自动化工具在加固的系统运行时可能触发告警

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163257333-79753420.png)

利用错误配置，只需修改脚本，或者在这里用恶意文件覆盖原始的 `.exe`

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163304805-86631316.png)

最后只需启动服务即可

![](https://img2023.cnblogs.com/blog/1449167/202303/1449167-20230308163315106-714835573.png)

**注意：即使服务以`localSystem`权限运行，我们也有启动和停止服务的权限**

### 3. 注册表 (.msi利用)

#### 基本原理

.msi 文件专为 Windows 软件而设计的，其中包含了以标准化方式（由 Windows Installer 服务管理）安装应用程序所需的信息和文件。此利用手法体现在 Windows installer数据包 (.msi) 中，数据包默认是以管理员权限运行。这意味着任何执行 .msi 数据包的用户或应用程序都会自动获得管理员权限，而无需任何用户输入或身份验证。

#### 步骤

**前提条件：下面两个注册表项值的权限都设置为 TRUE ，才能允许通过管理员工权限安装 .msi**

1. 检查注册表，当前用户是否允许下载 .msi

```
# 必须设置为 1 (0×1) 表示启用
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

2. 创建一个 .msi payload 传到目标机器上，执行该 .msi 即可获得 ADMIN/SYSTEM 权限

#### 实操

检查注册表项

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509120317764-960833470.png)

两者都设置为0×1，目标机器可以尝试使用该方法提权

创建一个恶意的 .msi payload(stageless)

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509120740882-676367427.png)

至于如何传到目标机上，是格局打开五花八门的，例如在 HTTP、SMB 服务器托管此恶意文件，在目标端使用 certutil、PowerShell 或 SMB 从VPS或其他服务器下载 .msi payload

目标机运行 .msi

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509121225181-983683926.png)

攻击端

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509121250625-89246488.png)

### 4.未加引号的服务程序路径

Windows服务是一种在后台运行的计算机程序，在概念上类似于 Unix 守护进程

Windows每个服务都将其可执行文件的路径写在 `BINARY_PATH_NAME`的变量中。当系统启动服务时，会检查此变量并执行其下设置的 .exe文件

注意：这与上面在[不安全的服务文件权限和路径](https://www.cnblogs.com/H4ck3R-XiX/p/17192109.html#tid-ssSzcC)所讲述的是同一回事，但是第一节中 binpath 变量是可写的，所以可以劫持。此节讲述的利用场景完全不同：**在服务的 BINPATH 是安全的/不允许操作的情况下**

#### 基本原理

未加引号的服务程序路径（Unquoted Service Path）利用发生在安装了 包含空格但未包含引号的可执行程序路径的Windows服务中。

当 Windows启动服务时，系统会在服务配置中指定的路径中查找可执行文件。**如果服务路径不包含引号且其中有空格，Windows 将尝试将路径的第一个单词作为可执行文件执行，并将其余单词用作命令行参数。**

例如，对于服务程序的路径`C:\Program Files\Script dir\service.exe`
Windows系统将尝试执行:

```
C:\Program.exe
C:\Program Files\Script.exe (Here \Program Files dir is writable so the attacker can create a payload with the service’s extension to get it executed by OS during traversing)
C:\Program Files\Script dir\service.exe
```

#### 步骤

**前提条件：1.必须有服务的路径，不包含引号和空格；2.与原二进制目录相比，在更高优先级的目录中拥有可写权限**

1.枚举所有服务，检查是否有某个服务的 BinPath 未被引用并且包含空格或其他分隔符
2.然后在列出的未加引号的二进制路径中找到至少一个可写目录，并且与原始目录相比，它的优先级必须更高
3.使用 sc 查询服务以检查该服务是否以 (SYSTEM/Admin) 权限运行
4.在该可写目录中创建一个恶意文件
5.重启或启动服务以使用 SYSTEM 权限执行 .exe

#### 实操

```
wmic service get name,displayname,pathname,startmode | findstr /i /v “C:\Windows\system32\” |findstr /i /v """
```

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150015685-884013079.png)

最后，服务路径有空格或未包含在引号中

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150045614-963608740.png)

进一步检查文件目录，与原始服务程序路径相比要具有更高优先级的可写路径

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150157879-71564143.png)

没有权限写入当前目录，继续查看其他目录

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150220825-1330643859.png)

获取到可以创建恶意文件的地方，在未加引号的服务程序路径上的目录中拥有完全访问 (rwx) 权限，并且此处目录的执行优先级也更高。

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150233775-807614048.png)

将恶意文件复制到可写目录并将其名称更改为 Common.exe（因为操作系统将在遍历查找期间执行此目录）

现在只需使用`net start <service-name>`启动此服务，即可获得目标机器的管理员权限shell

![](https://img2023.cnblogs.com/blog/1449167/202305/1449167-20230509150239308-212920702.png)

简单总结下，原始目录是`C:\Program Files\Unquoted Path Service\Common Files\UnquotedPathService.exe`, 因为 BinPath 有空格但没有用引号括起来所以可被利用提权

因此正常情况下，每当此服务启动时，Windows系统都会通过以下方式读取此BinPath

```
C:\Program.exe (Program Not Found)
C:\Program Files\Unquoted.exe (Program Not Found)
C:\Program Files\Unquoted Path.exe (Program Not Found)
C:\Program Files\Unquoted Pa...