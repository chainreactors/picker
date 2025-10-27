---
title: 攻击者通过Freeze.rs和SYK Crypter传播恶意软件
url: https://www.4hou.com/posts/XXP5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-25
fetch_date: 2025-10-04T11:59:35.076484
---

# 攻击者通过Freeze.rs和SYK Crypter传播恶意软件

攻击者通过Freeze.rs和SYK Crypter传播恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 攻击者通过Freeze.rs和SYK Crypter传播恶意软件

lucywang
[技术](https://www.4hou.com/category/technology)
2023-08-24 11:22:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)108818

收藏

导语：FortiGuard实验室最近检测到一种用Rust编写的新注入器，它可以注入shellcode并将XWorm引入受害者的环境。

受影响平台：Windows

受影响方：任何组织

影响：控制受害者的设备，收集敏感信息

严重性级别：紧急

FortiGuard实验室最近检测到一种用Rust编写的新注入器，它可以注入shellcode并将XWorm引入受害者的环境。虽然Rust在恶意软件开发中相对不常见，但自2019年以来，已经有几个活动采用了这种语言，包括Buer loader、Hive和RansomExx。FortiGuard实验室的分析还显示，2023年5月期间注入器活动显著增加，其中shellcode可以使用Base64编码，并可以从AES、RC4或LZMA等加密算法中进行选择，以逃避防病毒检测。

通过检查编码算法和API名称，研究人员在攻击者工具“Freeze.rs”中确定了这种新型注射器的来源，该工具旨在创建能够绕过EDR安全控制的有效负载。此外，在分析过程中，研究人员发现SYK Crypter通常用于通过社区聊天Discord传播恶意软件家族的工具，该工具涉及加载Remcos，这是一种复杂的远程访问木马（RAT），可用于控制和监控运行Windows的设备。SYK Crypter出现于2022年，已被各种恶意软件家族使用，包括AsyncRAT、jnrat、QuasarRAT、WarzoneRAT和NanoCore RAT。

FortiGuard实验室在7月13日观察到网络钓鱼电子邮件活动，该活动使用恶意PDF文件启动了攻击链。此文件重定向到HTML文件，并利用“search-ms”协议访问远程服务器上的LNK文件。点击LNK文件后，PowerShell脚本执行Freeze.rs和SYK Crypter准备进一步进攻。最后，加载XWorm和Remcos，并与C2服务器建立通信。

在本文中，我们将深入研究用于传播Rust-lang注入器SYK Crypter的初始攻击方法，并进一步探讨攻击的后续阶段。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720483198666.png "1691720483198666.png")

初始访问

如下图所示，钓鱼电子邮件伪装成发送给多家公司的紧急订单补充请求，以欺骗收件人。它还在PDF文件中使用模糊图像来引诱受害者点击隐藏的按钮。所附的PDF文件如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720492226276.png "1691720492226276.png")

网络钓鱼邮件

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720502166430.png "1691720502166430.png")

PDF文件

恶意URL隐藏在流对象(/ObjStm)中，使其难以被检测到。然而，通过pdf解析器提取URL显示它位于流对象1中的对象14中，如下图所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720512125434.png "1691720512125434.png")

流对象中的URL

点击该文件后，受害者连接到URL https：//www[.]cttuae[.]com/ems/page[.]html，这是一个伪装成提供旅游服务的网站。攻击者在7月12日上传了一个恶意HTML文件到“ems”路径，源代码如下图所示。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720521144719.png "1691720521144719.png")

HTML页面“page. HTML”

攻击者不是直接下载恶意软件，而是采用更复杂的方法，利用“search-ms”协议触发搜索结果。具体来说，他们在由DriveHQ提供的远程云存储服务器上搜索“ORDER\_SPEC0723”。值得注意的是，文件“ORDER\_PSEC0723”伪装成PDF文件图标，但仔细检查后发现，它是在同一文件夹中执行PowerShell脚本的LNK文件，如下图所示。这种策略允许攻击者谨慎地启动他们的恶意活动。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720530823008.png "1691720530823008.png")

搜索结果和LNK文件“ORDER\_PSEC01723”

然后执行PowerShell脚本“pf.ps1”，首先使用“regsvr32”启动用Rust编写的注入器“doc.dll”。它打开诱饵PDF文件“T.PDF”并执行“AA.exe”。最后，使用“Stop-Process”关闭所有文件资源管理器窗口。下图中的PDF文件“T.PDF”看起来很干净，包含清晰的文本，旨在分散受害者对其他恶意行为的注意力。以下部分将详细介绍“doc.dll”和“AA.exe”。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720539140902.png "1691720539140902.png")

PowerShell脚本“pf.ps1”

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720548644586.png "1691720548644586.png")

诱饵文件“T.pdf”

**Rust注入器：doc.dll**

下图显示了基于字符串部分分析，注入器是用Rust编程语言编写的。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720557111601.png "1691720557111601.png")

字符串部分

注入过程首先使用CreateProcessA创建一个“notepad.exe”进程。shellcode随后通过Base64解码和LZMA解压缩获得。然后，注入器直接使用NTAPI库的函数注入shellcode。以上便是“Freeze.rs”的整个攻击过程。该网站于今年5月发布，显示出人们非常喜欢这一新工具，源代码和注入器的汇编代码如下图所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720568677472.png "1691720568677472.png")

Shellcode注入

在过去的一个月里，研究人员编译了一系列不同的Rust注入器，包括带有lzma压缩的shellcode的DLL文件，带有rc4加密的shellcode的DLL文件，以及包含rc4加密的shellcode的EXE文件。这些注入器中的shellcode数据都使用Base64编码，有趣的是，文件类型和加密算法似乎是程序中可选择的选项。这个观察结果与“Freeze.rs”存储库中的选项一致，这表明它们之间存在某种关系。选择加密方法和文件类型的灵活性增加了这些注入器的复杂性，进一步复杂化了安全研究人员的检测和分析。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720578493797.png "1691720578493797.png")

“Freeze.rs”选项

当使用RC4算法变体时，密钥被扩展到256字节，并用于伪随机生成算法（PRGA）。该注入器变体的相应源代码和组件如下图所示。经过比较，很明显，此攻击者使用“Freeze.rs”绕过EDR并利用挂起的进程。解密后的shellcode可以在地址0x650000找到，如下图所示。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720589106580.png "1691720589106580.png")

RC4解密

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720600106920.png "1691720600106920.png")

解密后的shellcode

解密的shellcode应用AMSI绕过和WDLP绕过技术，随后执行.NET有效负载。一旦执行，.NET程序集就可以从内存地址0x1AAB6E70转储，如下图所示，从而可以作为独立的.NET可执行文件进行分析。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720609106119.png "1691720609106119.png")

解密的.Net有效负载

在此过程中发现的.NET有效负载被称为XWorm，根据分析，这是一种在地下论坛交易的RAT工具。XWorm配备了典型的RAT功能，包括收集设备信息、捕捉屏幕截图、记录击键以及建立对受攻击设备的控制。在该示例中，XWorm有效负载版本是v3.1，C2服务器信息仍然隐藏在“pastebin.com”网站上，如下图所示。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720619124174.png "1691720619124174.png")

XWorm V3.1和pastebin.com上的C2服务器IP地址

**MSIL下载程序：AA.exe**

执行文件“AA.exe”作为MSIL下载程序运行，并嵌入了两个链接：

“95[.]214[.]27[.]17/storage/NAR”和“plunder[.]ddnsguru[.]com/storage/NAR”。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720629617620.png "1691720629617620.png")

MSIL下载程序的链接

下载完成后，“AA.exe”使用文件名“760”作为解码密钥，并对下载数据中的每个字节执行减法运算。解码的数据是一个名为“SYKSBIKO”的资源的SYK Crypter，其中包含加密的有效负载。DLL文件进行检查以确保环境未处于调试模式，然后通过使用密钥“gOhgyzyDebuggerDisplayAttributei”的RC4解密来继续处理资源数据。它调用一个小的.NET代码“Zlas1”以进行进一步的压缩。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720639555901.png "1691720639555901.png")

调用.Net代码进行解压缩

为了逃避检测，SYK Crypter对其执行流中使用的字符串进行编码，解码函数如下图所示。此外，它还使用了“GetProcessesByName”“Directory.Exists”和“File.Exists”等函数来评估安全设备在受攻击环境中是否存在。用于检查的列表如下图所示。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720648181156.png "1691720648181156.png")

字符串转换器函数

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720658149972.png "1691720658149972.png")

安全设备检查列表

为了持久性攻击，恶意软件将“.exe”扩展名附加到文件“AA”，并将MSIL下载程序复制到“Startup”文件夹。它还在“HCKU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows”中添加了一个注册表项“Run”，相应的代码如下图所示。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720667697291.png "1691720667697291.png")

自我复制到“Startup”

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720677176969.png "1691720677176969.png")

添加注册表

在对资源数据“SYKSBIKO.Properties.Resources.resources‎‎.a,”进行RC4解密和压缩之后，将获得执行文件，如下图所示。然后，SYK-Crypter加载一个Base64.NET代码并调用其“GetDelegateForFunctionPointer”函数，在同一方法中从kernel32或ntdll创建对所有API的委托。下图显示了一个加载“kernel32！WriteProcessMemory”的片段，随后解密的有效负载被注入到进程中。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720686442345.png "1691720686442345.png")

从SYK Crypter解密资源数据

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230811/1691720695822128.png "1691720695822128.png")

调用“GetDelegateForFunctionPointer”来获取API

注入的有效负载是Remcos RAT，最初是作为远程计算机控制的合法工具设计的。然而，自2...