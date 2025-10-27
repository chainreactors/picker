---
title: DangerousSavanna：为期两年的针对非洲法语区的金融机构的攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552524&idx=2&sn=ae2bc9e1ebe87ce3c01831b916cccd64&chksm=e915de36de625720bc6e6d0dce784b75f7effbc14a6a7a3dcfe2f6935ff49fcbbbc9ef4ccf41&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-22
fetch_date: 2025-10-03T20:36:29.599221
---

# DangerousSavanna：为期两年的针对非洲法语区的金融机构的攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyCRN8pIN2rib12OwlQ5Ysiafb7TYaAmqXp00YptiaYIYJj29E8ofQBYIhw/0?wx_fmt=jpeg)

# DangerousSavanna：为期两年的针对非洲法语区的金融机构的攻击

lucywang

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyYXyX6hcQQiajaeu4mb66vibPGLR3gkWibE19btOrRf4ZovJQnQfTpMvqQ/640?wx_fmt=png)

最近的研究表明，中非和西非超过 85% 的金融机构多次遭受包括盗取信息、盗窃用户身份、转账欺诈和用虚假支票取款等多重网络攻击。

本文会介绍研究人员发现的一个名为 DangerousSavanna（危险草原）的恶意活动，该活动在过去两年中一直针对非洲法语区的多个主要金融服务机构。该活动背后的攻击者使用鱼叉式网络钓鱼作为初始感染手段，向至少五个不同法语国家的金融机构员工发送带有恶意附件的电子邮件：科特迪瓦、摩洛哥、喀麦隆、塞内加尔和多哥。在过去的几个月里，该活动主要集中在科特迪瓦。根据受害者的特征、策略、技术和程序 (TTP) ，研究人员认为 DangerousSavanna 背后的动机可能出于经济上的考虑。

DangerousSavanna 倾向于在受感染的环境中安装相对简单的软件工具。这些工具都是自行编写的，并且基于 Metasploit、PoshC2、DWservice 和 AsyncRAT 等开源项目。攻击者的创造力在初始感染阶段就展现出来，他们不断地监控目标公司的员工，不断改变利用各种恶意文件类型的感染链，从自写的可执行加载程序和恶意文档，到各种组合的 ISO、LNK、JAR 和 VBE 文件。攻击者不断演变的感染链反映了过去几年我们所看到的威胁格局的变化，因为感染载体变得越来越复杂和多样化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9Uly6DwYb6RVwLu8VOvULVGFMsZ737WLQkc5HlzTPSN3EwkNDe9jQpcvVg/640?wx_fmt=jpeg)

攻击目标均位于讲法语的非洲国家

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)感染链

感染始于用法语编写的鱼叉式网络钓鱼电子邮件，通常发送给目标公司的几名员工，这些公司都是非洲法语区的中大型金融机构。在活动的早期阶段，网络钓鱼电子邮件是使用 Gmail 和 Hotmail 服务发送的。为了提高可信度，攻击者开始使用相似域名，冒充非洲的其他金融机构，如突尼斯外国银行、南非莱利银行等。去年，攻击者还使用了当地一家保险咨询公司伪造的电子邮件地址，该公司的域名没有SPF记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyzRPs6PKo8xXdb4UG5ImIz2ryyQ1d4SC0XupSiasoFsXjib5s59ec6c4g/640?wx_fmt=jpeg)

一个网络钓鱼电子邮件示例，其中攻击者使用了受害企业现有员工的姓名

网络钓鱼电子邮件附件的类型以及随后的感染链也在整个活动时间范围内发生了变化，从 2020 年伪装成 PDF 的自行编写的可执行加载程序到 2022 年的各种文件类型。DangerousSavanna 迅速加入了恶意攻击的趋势。在 Microsoft 决定默认阻止从 Internet 获取的宏之后，攻击者从“经典”启用宏的文档转向尝试其他文件类型。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyYMnsuguECxqQYD0l6S5lUFqcfL1sL5RPRYrDQgJZ73Mgw9XiccNN2DQ/640?wx_fmt=jpeg)

DangerousSavanna 感染链、基础设施和有效负载的变化情况

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)恶意文件

自 2021 年以来，攻击者就开始将恶意文档附加到其网络钓鱼电子邮件中。这些文档要么是带有宏的 Word 文档，要么是带有远程模板（在某些情况下是几层外部模板）的文档，或者是诱使受害者下载然后手动执行下一阶段的 PDF 文档。所有这些文档，无论是 MS Office 还是 PDF，都是用法语编写的，并且共享类似的元数据，例如用户名 digger、hooper davis 和 HooperDEV。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlygV1KANxGRC7icw3BIpJnobxJ2aRic8hR6AwqpS8BicDSDJgRv2OrWhn4w/640?wx_fmt=jpeg)

活动中使用的诱饵文件概览

基本流程使用带有宏的 Word 文档，在 Startup 文件夹中放置一个 LNK 文件。执行 LNK 文件时，它会从服务器下载并执行 PowerShell 命令，这些命令会绕过 AMSI 并最终安装 PoshC2 植入程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyPoyuZlIkwfAS1ibmjc3rAbvG0Ot8bOwnpbIzHRm9v2pYWtI9mtf5zBw/640?wx_fmt=jpeg)

带有宏感染流的网络钓鱼文档

宏包含许多未使用的代码，使其分析复杂化。主要功能的代码很简单，只包含反向字符串混淆和插入符号混淆来创建用于检索 PoshC2 植入的 LNK 文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyHMzQhx01Oia12mPM4pepbZe5Aoepv5lewVtXOah2dqjGoicPUUzBvWAQ/640?wx_fmt=png)

在此活动中，我们观察到此流程的多种变化：

1.在某些情况下，类似的宏会将 LNK 文件放到桌面而不是启动文件夹，LNK 文件通常称为 IMPORTANT\_2022.lnk，需要用户执行操作才能运行。桌面和启动 LNK 方法都依赖于受感染设备上的额外操作，因此可以避免在沙盒环境中自动执行可疑的 PowerShell。

2.初始附件可能是下载执行类似宏的外部模板的 DOCX 文档。在某些情况下，我们已经看到在传播带有实际宏的最终文档之前检索了一系列远程模板。

3.一些早期版本的宏直接运行 PoshC2 PowerShell 释放器并跳过带有 LNK 文件的步骤。

4.包含宏的文档通常以容器文件的形式提供，例如 ZIP 和 ISO 文件。

此外，攻击者积极使用PDF文件引诱用户下载并手动执行下一阶段。这些VBE或JAR文件执行非常类似的操作，直接加载 PoshC2 植入程序或释放LNK 文件以加载 PoshC2。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)PoshC2

最近，攻击者主要依靠 PoshC2 植入程序来控制受感染的设备。通常，在初始感染启动 PowerShell 以从名为 paste.c-net.org 的类似 Pastebin 的服务或专用 C&C 服务器下载代码后，它会使用 PowerShell PoshC2 植入程序进行回应，通常包含三个字节编码块（所有标准来自 PoshC2 的模块）。执行的前两个 PowerShell 代码块包含两种非常相似的 AMSI 绕过技术：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlynmSm7slicu4H3wmrNGRMWloibyV6PHgCe4upKjlPFe0icrPEmf9RN8YDA/640?wx_fmt=png)

第三个块包含一个后门，负责与 C&C 服务器进行通信。它使用一个名为 SessionID 的 cookie 循环向服务器发送请求，该 cookie 带有一个 base64 编码的 AES 加密字符串，其中包含有关受害者的信息：

"$env:userdomain;$u;$env:computername;$env:PROCESSOR\_ARCHITECTURE;$pid;$procname;1"

该脚本预计 C&C 的响应也是 PowerShell 脚本，因为它将结果传递给 Invoke-Expression cmdlet。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)AsyncRAT

早在 2021 年 10 月，研究人员就观察到一个案例，该活动的恶意文档访问了 paste.c-net.org，但取而代之的是检索了一个在内存中加载 AsyncRAT 程序集的 PowerShell 脚本。然而，这个 AsyncRAT 构建完全没有混淆，实际上包含一个带有 CN “AsyncRAT Server”的服务器证书，表明攻击者几乎没有考虑对开源工具进行任何迭代。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9Uly5BsKttUeqoTcMZ4MWiaWFNp18p5fNGxGCFRfrHp2l3JEyvSkVKGh4Yg/640?wx_fmt=png)

GitHub 上的 AsyncRAT 源代码与反编译的 AsyncRAT（右侧）

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)旧文档版本

最早版本的文档日期为 2021 年上半年，具有不同的宏，这些宏的混淆程度明显更高，并且包含超过 1MB 的垃圾代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyLIWtCYqEicuH1c4PyKT3WKUKJmlT057Bz11bmj8QTDUliaoIZL9Dia6XQ/640?wx_fmt=jpeg)

2021 年 5 月文档 (md5:a09b19b6975e090fb4eda6ced1847b1) 的 1.7MB 宏的 Vba2graph 可视化的一部分，唯一的功能流程从 Document\_Open 开始。

其中一个名为 Nouvelles\_Dispositions\_Sanitaires.doc (New Sanitary Provisions.doc) 的文档使用宏从 4sync.com 下载 PowerShell 脚本，在不同设备之间的云存储同步文件，然后从https://3.8.126[.]182/minom.txt加载并在内存中执行一个程序集。在2021年5月的一篇InQuest博客文章中，有一份非常类似的文件详细地描述了该文件，它也使用4sync安装了一个名为Billang的自定义后门。它是一个具有以下 PDB 路径的 .NET 可执行文件：C:\Users\wallstreet\source\repos\Billang\Billang\obj\Release\Billang.pdb。它收集有关它运行的设备的一些信息，将其发送到远程服务器，并检索另一个名为 liko 的 .NET 可执行文件或者，基于 PDB 路径的WindowsFormsApp3。除其他功能外，该程序将字节反转的 Meterpreter HTTPS shellcode 注入 mspaint.exe 进程。这个二进制文件的另一个有趣的特性是，shellcode 仅在检测到鼠标点击后才会启动，这可能是作为一种反沙盒特性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9Uly5rBFvTibdhqicJTqV8wQBW948jM60121Yo1BkAZia9vgWVgOb6jWjudicA/640?wx_fmt=jpeg)

从WindowsFormsApp3.exe (0b1d7c043be8c696d53d63fc0c834195) 到 mspaint.exe 的 Shellcode 注入

在搜索更多相关文件时，我们发现了用 C# 编写的其他可执行文件，它们以类似的方式启动诸如 notepad.exe 或 mspaint.exe 之类的进程，并将 shellcode 注入它们（注意不是嵌入），而是从 C&C 服务器下载到良性进程中。这些简单的注入器可执行文件在功能上几乎没有什么不同。它们之间的区别在于混淆方法：有些是用 SmartAssembly 打包的，有些包含混淆的变量名。但是，迄今为止观察到的所有 shellcode 有效负载都是 Meterpreter shellcode，并且在那些包含其调试信息的可执行文件中，都引用了以 C:\Users\wallstreet\ 开头的 PDB 路径。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)可执行滴管

在活动早期，从 2020 年底到 2021 年初，攻击者们依靠 .NET 中的小型自写工具而不是文档。附加到网络钓鱼电子邮件的第一阶段可执行投放器伪装成文档，并带有 PDF 图标，有时名称中有双扩展名（例如，Nouvelles Reformes 2021.pdf.exe，英文为“New Reforms 2021.pdf.exe” ）。事实上，这些简单的下载器使用批处理脚本（或 cmd 命令）和 PowerShell 从 4sync.com 或 filesend.jp 等文件共享平台检索第二阶段加载器并执行它们。在此特定示例中，下载器创建并运行一个 bat 文件，该文件通过 COM 劫持执行 AMSI 绕过，然后使用 PowerShell 下载下一阶段加载程序并将其作为 WinTray.exe 保存在磁盘上：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib6pOE5ekElKPDLNE7J9Ulyk21u7sqA4dJu9HMOia2gn528ibF15SG8sjhVKFLZmeJbd5fUfQyWCJBg/640?wx_fmt=jpeg)

“Nouvelles Reformes 2021.pdf.exe” (7b8d0b4e718bc543de4a049e23672d79) 的简化感染链

第二阶段可执行文件的目的是将最终的有效载荷（通常从硬编码地址下载的 Meterpreter shellcode）注入到不同的良性 Windows 进程中。这些工具与 InQuest 讨论的工具类似，除非它们的调试信息被删除，否则它们还包含具有唯一用户名wallstreet 的 PDB 路径。

2021 年末，一些感染链开始使用 C# 可执行文件来执行更简单的操作，只需启动 PowerShell 从服务器拉下一个阶段。当时，该活动已经在使用 PoshC2 植入程序而不是 Metasploit 有效负载，但这些工具仍然具有引用wallstreet 的 PDB 路径。例如，C:\Users\wallstreet\source\repos\PDF Document\PDF Document\obj\Release\PDF Document.pdb。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)感染后的活动

当初始 PowerShell 后门连接到 C&C 时，攻击者自动发送 AMSI 绕过命令和 PoshC2 植入，然后检索第二阶段植入以在 PowerShell 会话中添加额外功能。接下来，攻击者建立持久性并执行监测，同时还运行一些命令来尝试逃避检测。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib6pOE5ekElKPDLNE7J9UlyY63ibzn4dNlywu0Um5tFNqqMyrj0diatjaJpAPrYxX5PJb1bjkNc5XPA/640?wx_fmt=png)逃避...