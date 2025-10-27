---
title: [译文] 恶意代码分析：4.ViperSoftX机制-利用AutoIt和CLR隐蔽执行PowerShell
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500611&idx=1&sn=e768fa776263aa04707d27b8acbdc0e9&chksm=cfcf738ef8b8fa988fbed5fa8141868bab951a52077393a05a816727c62edac0b214cc11b7c8&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-07-19
fetch_date: 2025-10-06T17:43:37.282279
---

# [译文] 恶意代码分析：4.ViperSoftX机制-利用AutoIt和CLR隐蔽执行PowerShell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEDlLz73Za9NHqtduNT6Tjlyqo97ISRVpqd5eicVGcKwW1riblfibe8XzQg/0?wx_fmt=jpeg)

# [译文] 恶意代码分析：4.ViperSoftX机制-利用AutoIt和CLR隐蔽执行PowerShell

原创

eastmount

娜璋AI安全之家

> “
>
> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROZTxtlMEIJicPa3Fkxv0hsq6bPQFn74FAq7r23ziahWkGy74BLcYnTBM5QXk2GRXAPBVmsXwaxdheQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

这是作者新开的一个专栏，主要翻译国外知名安全厂商的技术报告和安全技术，了解它们的前沿技术，学习它们威胁溯源和恶意代码分析的方法，希望对您有所帮助。当然，由于作者英语有限，会借助LLM进行校验和润色，最终结合自己的安全经验完成，还请包涵！

前文介绍了DNS隧道的两个新技术——跟踪和扫描。这篇文章将详细讲解ViperSoftX机制，利用AutoIt和CLR隐蔽执行PowerShell代码，通过运用CLR，ViperSoftX能够无缝集成PowerShell功能，使其能够在执行恶意功能的同时，规避可能标记独立PowerShell活动的检测机制。基础性技术文章，希望您喜欢！

**文章目录：**

* **一.威胁总结**
* **二.感染流程**
* **三.Torrent陷阱：ViperSoftX的恶意电子书与隐藏威胁**
* **四.从防御到进攻：ViperSoftX的战略代码重用**

+ 1.在AutoIt脚本中执行PowerShell命令
+ 2.绕过AMSI检测

* **五.揭露隐藏的PowerShell载荷**
* **六.结论**
* **七.TTPs和IOCs**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEkYzNswXtTxk6tvctooS4IwUW0s0BFscEwIe1S5LIzBfcWVhN8mK50Q/640?wx_fmt=png&from=appmsg)

* 原文标题：《The Mechanics of ViperSoftX: Exploiting AutoIt and CLR for Stealthy PowerShell Execution》
* 原文链接：https://www.trellix.com/blogs/research/the-mechanics-of-vipersofts-exploiting-autoit-and-clr-for-stealthy-powershell-execution/
* 文章作者：Mathanraj Thangaraju and Sijo Jacob
* 发布时间：2024年7月9日
* 文章来源：https://www.trellix.com/

---

# 一.威胁总结

在网络威胁（cyber threats）不断演变的动态环境中，ViperSoftX作为一种高度复杂的恶意软件（highly sophisticated malware）已崭露头角，其擅长渗透系统并窃取敏感信息。自2020年首次被发现以来，ViperSoftX经历了数次迭代，每个版本都展现出更高的复杂性和更先进的功能。起初，它主要通过破解软件传播，利用盗版应用程序诱导用户安装恶意软件。ViperSoftX早期还通过种子（torrent）网站分发，但现在我们观察到它专门以电子书的形式在种子文件中传播。

当前ViperSoftX变种的一个显著特点是利用公共语言运行时（Common Language Runtime，CLR）动态加载和运行PowerShell命令，从而在AutoIt内部创建PowerShell环境以执行操作。通过运用CLR，ViperSoftX能够无缝集成PowerShell功能，使其能够在执行恶意功能的同时，规避可能标记独立PowerShell活动的检测机制。

此外，ViperSoftX还采用了一种策略，即攻击者有选择地从攻击性安全脚本中调整组件，仅修改必要的元素以符合他们的恶意目标，而非从头开始编写新代码。通过利用这些现有脚本，恶意软件开发者不仅可以加速了开发过程，还可以专注于提升逃避检测的技术，使ViperSoftX在网络安全领域成为一股不可忽视的威胁。

深入了解这些方法对于开发有效防御此类高级威胁至关重要。在本博文中，我们将深入探讨ViperSoftX的工作原理，包括其感染链、有效载荷执行以及采用的多种逃避检测技术。

> 公共语言运行时 (Common Language Runtime，CLR) 是 .NET 提供的运行时环境，它运行托管代码并提供跨语言集成、安全性、版本控制等服务。

---

# 二.感染流程

图1展示了恶意软件的感染流程，包括初始化、恶意组件、CLR、Payload执行、命令与控制等。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEPfcYahibqzwfQ1svPhndTv3icCndHTYXQiamVUCcvnFSUzw0M686mVpXQ/640?wx_fmt=png&from=appmsg)

---

# 三.Torrent陷阱：ViperSoftX的恶意电子书与隐藏威胁

图2展示了电子书Torrent链接。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEqXnEz5ctuic28czxIq4zuibBXmMbohibGrxemheruDBRMznq8ibic2VK41A/640?wx_fmt=png&from=appmsg)

当用户从恶意Torrent链接下载电子书时，攻击就开始了，他们误以为正在获取合法文件。然而，下载的RAR文件中隐藏着多重威胁，包括一个隐藏文件夹、一个伪装成无害PDF文件的狡猾快捷方式文件、PowerShell脚本、AutoIt.exe以及AutoIt脚本，这些文件均巧妙地伪装成JPG文件。隐藏文件夹内包含一组与当前文件夹中相同的文件，但除了一份作为诱饵的PDF或电子书文档外，该文档旨在掩盖其真实目的。

下图分别展示了RAR文件夹内容以及LNK文件命令。注意，图片格式其实是伪装的恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEcwrnY44HC0bOm3aDfUPDK6BU5py4yksaRfgjtxOXgwTmJjibiaBLYGvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEmjskJKT9cdAe5F5AdsMPjuSE3KH5SVHsk6tVslEXBn0Uoic6R3YTofA/640?wx_fmt=png&from=appmsg)

当用户执行快捷方式文件时，它会启动一个命令序列，该序列首先列出“zz1Cover4.jpg”的内容。随后，它从该文件中逐行读取内容，并在命令提示符中将它们作为命令执行，从而有效地自动化执行多个命令。这种策略允许在无需用户直接交互的情况下，流畅且自动地执行潜在恶意命令。图5展示了隐藏的PowerShell代码。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEwTtc52v3IMZECsLooxO2zfpVDBVRCVc7GZmmtUicLvAOI38kr6JCOSw/640?wx_fmt=png&from=appmsg)

如上所述，LNK文件执行“zz1Cover4.jpg”，该文件巧妙地在多个进程日志的空白处隐藏了PowerShell代码。

这段PowerShell代码执行了以下几个操作：

1. 取消隐藏文件夹的隐藏状态。
2. 该脚本计算所有磁盘驱动器的总大小，并将该大小用作AutoIT脚本的文件名和任务名。该脚本配置Windows任务计划程序（Task Scheduler），设置两个触发器：一个在登录时触发，每5分钟重复一次；另一个每天触发，每10分钟重复一次。
3. 它将两个文件（zz1Cover2.jpg和zz1Cover3.jpg）复制到%APPDATA%\Microsoft\Windows目录下，并将zz1Cover2.jpg重命名为<磁盘驱动器大小总和>.au3，将zz1Cover3.jpg重命名为AutoIt3.exe。
4. 删除当前目录中的所有.lnk文件。

图6显示了隐藏文件夹内容突出显示诱饵电子书（eBook）。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEobGxpE4HTsD1PPSsuicbQtU9keMLPfnBUR93MC8tLHZJ3BU7tjTdpjA/640?wx_fmt=png&from=appmsg)

图7显示了以计划任务运行AutoIT脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEtYGzvntdeiaCM6SSQBkl7zEV9rWOD1VMapQN3ftGLhvddKvg5AsPWibA/640?wx_fmt=png&from=appmsg)

---

# 四.从防御到进攻：ViperSoftX的战略代码重用

在研究ViperSoftX时，我们发现了一个清晰的模式：攻击者利用AutoIt脚本来隐藏其恶意行为。攻击者使用各种技术精心混淆这些脚本，增加了复杂性，这对研究人员和分析工具试图解密其功能构成了挑战。

此外，我们的分析揭示了ViperSoftX广泛使用了大量代码，这表明了其操作的复杂性和深度。通过对源代码的反编译，我们能够进行彻底的分析，更深入地了解ViperSoftX的操作，并揭示其功能和工作方法。

图8展示了混淆AutoIT脚本的片段。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEt8X1nDkuv7u2zoOzg1KZibNZCVibRgf7pXWyArW50ibw5oziaAMl3FMRlA/640?wx_fmt=png&from=appmsg)

## 1.在AutoIt脚本中执行PowerShell命令

AutoIt脚本超越了其原本良性的起源，成为秘密执行PowerShell命令的强大工具。AutoIt有害用途的关键在于它能够与.NET公共语言运行时（CLR）框架进行交互。尽管AutoIt默认不支持.NET公共语言运行时（CLR），但该语言的用户定义函数（user-defined functions，UDF）为CLR库提供了一个接口，从而使恶意行为者能够访问PowerShell的强大功能。

借助.NET CLR的支持，AutoIt获得了利用PowerShell自动化类“System.Management.Automation.PowerShell”的能力。这些类促进了在非托管运行空间中与PowerShell模块、cmdlet和脚本的交互。利用这些类，攻击者可以轻易地执行各种有害活动而不被察觉。

更多详情，可参阅AutoIT论坛和微软官方文档。

* https://learn.microsoft.com/en-us/powershell/scripting/developer/hosting/adding-and-invoking-commands?view=powershell-7.4

图9展示了使用.NET CLR在AutoIt中嵌入PowerShell脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEQncZ2sT7oHWxSoEl440jj02jiaN5l3MXcXXqs9LV9HtbicS2FMMje0KA/640?wx_fmt=png&from=appmsg)

下面详细解释这段Powershell代码：

（1）加载程序集

* 脚本首先通过 \_CLR\_LoadLibrary 加载 System.Management.Automation 程序集。
* 此步骤初始化一个局部变量 $oAssembly，用于存储加载的程序集对象。

（2）获取类型信息

* 脚本利用 $ oAssembly.GetType\_2 方法检索 Management.Automation.PowerShell 类的类型信息。
* 初始化一个局部变量 $pAssemblyType 来存储此类型信息。

（3）动态创建对象

* 基于之前获取的类型信息，使用 ObjCreateInterface 创建一个激活器（activator）对象 $oActivatorType。
* 该激活器对象的目的是动态地创建PowerShell对象的实例。

（4）初始化PowerShell对象

* 脚本使用激活器（activator）对象和 InvokeMember\_3 方法初始化一个PowerShell对象 $pObjectPS。
* 此步骤在AutoIt内有效创建了一个PowerShell环境，用于执行PowerShell命令。

（5）添加和执行PowerShell脚本

* 将存储在 $ PSScript 中的PowerShell脚本添加到PowerShell对象 $ pObjectPS 中，使用 $ pObjectPS.AddScript方法。
* 然后，通过 $ pObjectPS.BeginInvoke 方法异步执行脚本，该方法返回一个异步操作句柄 $objAsync。

（6）处理异步执行

* 脚本进入一个循环，等待异步操作完成（即 $ objAsync.IsCompleted = False）。
* 在循环内部，ContinueLoop确保脚本保持在循环中，直到操作完成。
* 一旦操作完成，脚本使用 $ pObjectPS.EndInvoke 检索结果，并将其存储在 $objPsCollection中。

---

## 2.绕过AMSI检测

在执行前，AMSI（Antimalware Scan Interface）赋予安全产品审查脚本内容的能力，包括PowerShell脚本。这种主动防御策略增加了一层宝贵的防护层，能够在恶意活动对系统和网络造成破坏之前进行阻止。ViperSoftX中的 \_PatchAMSI() 函数具有单一目的：在执行PowerShell脚本之前，消除AMSI的警惕注视。通过给AMSI打补丁，ViperSoftX能够绕过依赖于AMSI进行恶意脚本扫描和阻止的安全解决方案的检测，从而在被入侵的系统中进行未被发现的操作。

图10展示了尝试绕过AMSI检测。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEBr1lfBrfaxyiaZnN03odIwnms1SkAtQk91tWwXcv7n3xTDeW5g2ssfw/640?wx_fmt=png&from=appmsg)

下面逐行解析 \_PatchAMSI 函数的功能：

（1）定义补丁字节（Patch Bytes）

* 此行代码将补丁字节定义为十六进制字符串。这些字节包含将被写入AmsiScanBuffer内存位置的操作码，这些操作码有效地改变了函数的行为，使其返回 E\_INVALIDARG 错误。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHHI56vlg9KJRn9qEq5daEsiblFgl9gfp3oLiaPHnrArpEKjIR2PqalxnTPpicuzFY3icKEtWhA/640?wx_fmt=png&from=appmsg)

（2）加载DLL

* \_HexToString 函数将十六进制字符串转换为DLL名称（此处为dll）的可读字符串。
* \_WinAPI\_LoadLibrary 函数将指定的DLL加载到内存中。

（3）获取ASB地址

* 另一个十六进制字符串被转换为可读字符串（“AmsiScanBuffer”）。
* \_WinAPI\_GetProcAddress 函数检索已加载DLL中指定函数（AmsiScanBuffer）的内存地址。

（4）修补内存

* BinaryLen计算补丁字节的大小。
* DllCall 调用Windows API函数 VirtualProtect 以修改内存保护属性。
* 该函数修改指定内存地址（$asbLoc）的保护属性，以允许写入（0x40代表PAGE\_EXECUTE\_READWRITE）。
* 原始保护状态被存储在变量中以便后续恢复。

（5）应用补丁

* 创建一个动态结构（$patchBuffer）以存储补丁字节。
* 通过 DllStructSetData 函数将补丁字节写入分配的内存中。
* 最终，在应用补丁后，将内存保护恢复到其原始状态。

---

# 五.揭露隐藏的PowerShell载荷

如前文所述，“PS有效载荷”指的是在感染过程中执行的一个恶意PowerShell脚本。它存储在变量 $PSScript 中，并通过Base64加密进行隐藏。AutoIt函数 \_RUN\_PSHOST\_SCRIPT() 负责加载并执行此PowerShell脚本。

图11展示了Base64编码的PS有效载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPWYkWJHH...