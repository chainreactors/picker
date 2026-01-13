---
title: 擦除与重生：Windows 系统下删除文件如何实现 LPE（持久化文件执行）
url: https://mp.weixin.qq.com/s/xXJWd1ICsS-sSH6elVKjlw
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:27:42.769651
---

# 擦除与重生：Windows 系统下删除文件如何实现 LPE（持久化文件执行）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz10IsBNc0fVgvictCE7gpVbITplllnHbu6lrJWqAVLWQ17KLHs0UgFgbw/0?wx_fmt=jpeg)

# 擦除与重生：Windows 系统下删除文件如何实现 LPE（持久化文件执行）

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

介绍

检查时间到使用时间 (TOCTOU) 竞争条件已经困扰 Windows 软件数十年，但即使在现代代码中仍然屡见不鲜。在最近对 TestedAPP 的一次审计中，我们发现了一个典型的例子：应用程序的后台服务首先检查缓存目录是否存在，然后在几毫秒后将其删除，而没有重新验证路径。由于每个非特权用户都可以在应用程序目录树中创建文件和文件夹，攻击者可以赢得竞争，将合法目录替换为 NTFS 挂载点，并将删除操作重定向到系统驱动器上的任何位置。最容易且最具破坏性的目标是隐藏的 C:\Config.Msi 暂存文件夹，Windows Installer 在安装回滚操作期间将其视为完全信任的文件夹 [1, 2]。

利用这一漏洞非常简单。通过将 SetOpLock（在服务发出删除请求后立即冻结该服务）与 Google Project Zero 符号链接工具包中的 CreateMountPoint 和 CreateSymlink 函数结合使用，低权限用户可以将看似无害的文件夹清除操作转化为任意文件夹删除操作。

一旦 C:\Config.Msi 被删除，攻击者会将其重新创建为指向其他位置的连接点，并投放一个恶意回滚脚本和一个 DLL 有效载荷。当 Windows Installer 恢复运行并执行回滚脚本时，该 DLL 将以 NT AUTHORITY\SYSTEM 身份调用，从而启动 SYSTEM 级别的命令提示符，并将计算机的完全控制权交给攻击者。

除了直接的权限提升影响之外，该发现还凸显了两个问题：Windows 仍然授予普通用户对许多应用程序目录的广泛写入权限，并且开发人员仍然依赖于非原子文件系统操作，而这些操作可以通过对象管理器技巧进行规避。因此，这项研究既可以作为漏洞利用案例研究，也可以作为强化安装程序风格代码路径以抵御现代竞态条件攻击的实用检查清单。

概念验证

模块行为和攻击向量

经测试的应用程序模块包含一个名为 downloader.exe 的命令行实用程序，任何本地（非特权）用户都可以通过提供 URL 来调用它，从而预取或“缓存”软件包。由于该工具不会验证或限制 URL 参数，攻击者可以执行例如以下命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1qiaDFVZfXYfAwH1ibSkfV6YqEIIo1iaRpzrZe4S7ELGt8bOHTpOyg8pOA/640?wx_fmt=jpeg&from=appmsg)

经测试的应用程序模块包含一个名为 downloader.exe 的命令行实用程序，任何本地（非特权）用户都可以通过提供 URL 来调用它，从而预取或“缓存”软件包。由于该工具不会验证或限制 URL 参数，攻击者可以执行例如以下命令：

执行缓存命令后，程序会发送 .MANI 清单的请求来启动软件包下载过程，该清单用作软件包描述符。发出两个 HTTP GET 请求：

1. 第一个请求发送到清单生成端点，生成指定软件包的 .MANI 描述符；

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1j1sbmpPkeg47guqI6uaXUX2iaOFQAbDkYZicJ9ic3fZb3klNIxvNibWRaw/640?wx_fmt=jpeg&from=appmsg)

2. 然后发送第二个请求，检索该 .MANI 文件的内容，并将清单下载到本地缓存文件夹，以便进行解析和后续的文件下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1fxHicWDPT5ZuKjv9UzA3RwFDgqujzR9SRX5bAmWsMuJia38EErbgou2w/640?wx_fmt=jpeg&from=appmsg)

下面提供了一个 .MANI 清单示例，其中列出了文件名、大小和校验和。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1icf5tKKvM2J8lWmHcicib6GQ8zU4qxWL8GUs6myOZtJRXv2XYL5lYtWzQ/640?wx_fmt=jpeg&from=appmsg)

清单保存在中央缓存目录中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1WvGqiaCL0dnzed9mbIIO50jYOucHqicGh4ZmCnFKncojUtAkRW37pibZg/640?wx_fmt=jpeg&from=appmsg)

然后在该路径下创建一个以 CONTENTID（例如 ABC123）命名的子目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1fOgAOZiaRXsOvPbDgpye473b5N2oXzJRXUmvvjvWXJicNQhcxH0lYG8A/640?wx_fmt=jpeg&from=appmsg)

在这个暂存文件夹中，清单中声明的每个文件都会被下载，并在最终放置之前根据提供的校验和验证其完整性。随后，通过 HTTP GET 请求获取 .MANI 清单中列出的文件。对于上面显示的 Windows 条目，请求采用以下形式：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1BNYVibM42A54BCnmVj2Vrhk1uwrYhwicGBUQWuquKIUgmzm9jwsRDWWQ/640?wx_fmt=jpeg&from=appmsg)

如果服务器未能返回请求的文件，或者下载文件的校验和与声明的值不匹配，则与该软件包关联的所有文件都将被清除。此漏洞的关键在于 TestedApp.exe 服务尝试访问一个不存在的 CachePKG\[CONTENTID]\_0\_1 目录。如下面的 Procmon64.exe 工具（来自 SysInternals 套件）截图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz14WJnAZBas2sJQMPIXFeBKVmhoOtSob1Yvg8Sd2lqjqegZ0tK8ZQDog/640?wx_fmt=jpeg&from=appmsg)

否则，如果该目录存在，则会被服务删除：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1pWiaz73fniaUVP9zttIoK6ZAbRVPSSbBAJKOicsQOUHbXJkBzgYcDEbgw/640?wx_fmt=jpeg&from=appmsg)

此外，在文件删除序列的初始阶段，服务会引用一个不存在的文件，这种行为可被利用：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1LBdLca6amd2f1xdDiaCXibjAXzCNDA2ZFyKmXI0Hx0KWV6MkwdVsE9ew/640?wx_fmt=jpeg&from=appmsg)

另一个不太重要但值得注意的行为是，应用程序会反复循环执行整个 HTTP 请求序列，生成 .MANI 清单文件，获取 .MANI 文件，尝试下载其中声明的每个文件，并清除软件包数据。

剥削——前提条件

Windows 将 NTFS 连接点的创建限制为特权帐户，这使得传统的符号链接攻击对普通用户来说不可行。然而，Google Project Zero 的研究表明，可以在 \RPC Control 对象目录（一个非特权进程通常具有写入权限的对象管理器命名空间）上创建一个挂载点，从而有效地模拟符号链接，而无需使用 SeCreateSymbolicLinkPrivilege 函数。

为了实现这项技术，我们使用了 symboliclink-testing-tools 套件，该套件可在 GitHub 上的此 URL 地址 [4] 找到。我们从该仓库中使用了以下实用程序：

• 使用 SetOpLock.exe 对文件（或目录）建立机会性锁定，防止在释放锁定之前将其删除。

• 使用 CreateMountPoint.exe 将一个原本为空的文件系统目录绑定到 \RPC Control 命名空间（或任何其他可写对象目录），从而将后续的文件系统操作重定向到对象管理器路径。

• CreateSymlink.exe 用于在对象管理器命名空间内生成文件级符号链接，从而允许在没有管理员权限的情况下将打开、读取、写入或删除操作重定向到任意目标。

通过结合使用这些工具，例如使用 oplock 暂停删除例程、将空文件夹挂载到 \RPC Control 目录，然后创建对象管理器符号链接，非特权用户即可获得针对受保护系统路径的任意文件删除原语。

此外，在此过程中必须提供 .MANI 清单文件，TestedApp 服务将尝试缓存该软件包，从而触发允许删除文件夹的应用程序行为。以下基于 Flask 框架构建的 Python 脚本用于提供所请求的 .MANI 清单文件的内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1hTKa9uJYhVuAjUNORGxRAO8Zicx17pwbFcrrIKrXZnJvnkIrtV6d29A/640?wx_fmt=jpeg&from=appmsg)

包含 Flask 应用程序的目录还必须包含一个 mani\_file 文件，其内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1icf5tKKvM2J8lWmHcicib6GQ8zU4qxWL8GUs6myOZtJRXv2XYL5lYtWzQ/640?wx_fmt=jpeg&from=appmsg)

该脚本可以在本地执行，也可以在远程攻击者控制的计算机上执行。

利用步骤——删除文件夹

要成功利用此漏洞，必须执行以下步骤：

1. 首先，必须通过执行以下命令启动 .MANI 服务端点：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz15psGAy5vZP38NRU0u93lLytDMdV9vhVNWkNWqPW4y9OMuvjcKkXMQg/640?wx_fmt=jpeg&from=appmsg)

此命令会启动基于 Flask 的服务器，该服务器将监听传入的请求并在查询时返回 .MANI 清单。

2. 创建文件 EXPLOIT\_1.SPARSEMAP，然后设置机会锁以暂停文件删除操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1gCxUHpkLibTPDq22PlWFrKm2bmcFeXMor4Br8aZtiabhZSXc6az6NWAQ/640?wx_fmt=jpeg&from=appmsg)

3. 使用 Downloader.exe 启动软件包下载过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1ZugYyx8J2g3Byu5ZT3uzZAzY8BIicOZiaP0dMbBvOicibQ9Yv0JLSZhFWA/640?wx_fmt=jpeg&from=appmsg)

4. 在不存在的 CachePKG 文件夹路径处建立挂载点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1KMbmtuZxeEB6XH7MrZhcpx3Pu3mthuufZ0m3oW5gv5xQ3Mqic5XEiauw/640?wx_fmt=jpeg&from=appmsg)

5. 从 CachePKG\EXPLOIT\_0\_1 创建指向目标删除目录的符号链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1nQ3KPkjbMAEtM0WR3G48ln9aGFw5YO1PSBlQxG3ZFVN3ByQu9hiczSQ/640?wx_fmt=jpeg&from=appmsg)

6. 按 Enter 键释放机会锁。

完成这些步骤后，TestedApp.exe 服务将删除指定的文件夹，如下面的 Procmon64.exe 屏幕截图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1l9YuuNO8H6KuPIMV3wNVkzvMKEpPichFB6ybyjdvQia74TiauK8NGZOibg/640?wx_fmt=jpeg&from=appmsg)

利用步骤——权限提升

Windows Installer (MSI) 在系统驱动器上的一个隐藏文件夹 C:\Config.Msi 中执行所有文件暂存和回滚脚本生成操作，在提交任何更改之前，会将该文件夹中的所有内容视为完全可信的安装程序数据。在正常安装过程中，新文件或替换文件首先会被复制到 Config.Msi 文件夹中，并在其中生成相应的回滚脚本（.rbs/.rbf）。只有当所有暂存步骤成功完成后，文件才会被移动到最终位置；如果暂存失败或显式调用了回滚/卸载操作，则存储在 Config.Msi 中的回滚脚本将以 SYSTEM 帐户身份执行，以撤销或最终确定所有更改。

攻击者可以利用 Config.Msi 创建后立即出现的任意文件夹删除漏洞，删除该文件夹并将其替换为 NTFS 连接点。当 Windows Installer 随后对 C:\Config.Msi 执行清理或回滚删除操作时，该连接点会导致删除受保护的目标目录，而不是原始的暂存区域。删除系统文件后，攻击者可以重新创建一个恶意的 Config.Msi 目录（或连接点），其中包含攻击者控制的 .rbs/.rbf 回滚脚本。下次调用回滚机制时，这些脚本将以 SYSTEM 权限运行，从而实现任意代码执行和本地权限完全提升。零日漏洞利用计划 (Zero Day Initiative) 已在 GitHub 上发布了一个完整的概念验证漏洞利用程序 [3]。

该程序实现了一个两阶段攻击，利用了 Windows Installer 的回滚机制以及任意文件夹删除原语。在第二阶段，攻击者启动一个 MSI 安装程序，然后在回滚过程中中止该安装程序。在删除并使用宽松的 DACL（自主访问控制列表）重新创建 C:\Config.Msi 文件后，安装程序生成的回滚脚本 (.rbs) 和回滚文件 (.rbf) 会被替换：.rbf 有效载荷是一个精心构造的 DLL，用于启动命令行；而恶意 .rbs 脚本则指示 Windows Installer 将该 DLL 文件复制到：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1TrctNiaksp6Qrlicia3fE8YWpB6iaJc2u4FB2b7nCofPf113PseNXDQrUA/640?wx_fmt=jpeg&from=appmsg)

当回滚过程恢复时，这些文件将以 SYSTEM 帐户执行，导致 DLL 文件被放入 ink 目录。此后，每次在安全桌面上调用屏幕键盘 (osk.exe)（例如，通过 Ctrl + Alt + Delete）都会导致加载被劫持的 HID.dll，从而通过 DLL 劫持生成一个具有 SYSTEM 权限的命令提示符窗口。

要成功利用此漏洞，必须执行以下步骤：

1. 首先必须通过执行以下命令启动 .MANI-serving 端点：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1F38cF2ZmDLuAasT3sGp6kjFL46fLdCx181tJtceqv26aQo3w9qhvBA/640?wx_fmt=jpeg&from=appmsg)

此命令启动基于 Flask 的服务器，该服务器将监听传入的请求并在查询时返回 .MANI 清单。

2. 必须按如下方式执行之前从 GitHub 仓库编译的 FolderOrFileDeleteToSystem.exe 二进制文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz101ic6zib65J5DSfTVmRZe5A8BvjHAMWVcibV2T6icNNibRjsBib34EHCC7Fw/640?wx_fmt=jpeg&from=appmsg)

3. 创建文件 EXPLOIT\_1.SPARSEMAP，然后设置机会锁以暂停文件删除例程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5GMs8KkT4MYxmz1hBiacKntAakdWkjXGhjwibib9TZDwwGLxoou7vmzRMYT4rWN0sShquL9g/640?wx_fmt=jpeg&from=appmsg)

4. 使用 downloader.exe 启动软件包下载过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tadkIM5sU5...