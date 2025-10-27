---
title: 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（三）
url: https://buaq.net/go-141329.html
source: unSafe.sh - 不安全
date: 2022-12-26
fetch_date: 2025-10-04T02:30:46.784640
---

# 以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（三）

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

![](https://8aqnet.cdn.bcebos.com/24ea1f6d1eddd8ff1d8139323b0f9d0e.jpg)

以 Roshtyak 后门为例介绍恶意软件的自保护、逃逸等技巧（三）

导语：本文就以 Roshtyak 后门为例介绍恶意软件的自保护、杀软逃逸技巧。Raspberry Robin于2021年9月首次被发现，通过受感染的USB设备传播。
*2022-12-25 12:0:0
Author: [www.4hou.com(查看原文)](/jump-141329.htm)
阅读量:33
收藏*

---

导语：本文就以 Roshtyak 后门为例介绍恶意软件的自保护、杀软逃逸技巧。Raspberry Robin于2021年9月首次被发现，通过受感染的USB设备传播。

**变量隐藏**

一些变量不是以明文形式存储的，而是使用一个或多个算术指令隐藏起来的。这意味着如果 Roshtyak 没有主动使用变量，它将以混淆的形式保留该变量的值。每当Roshtyak需要使用该变量时，它必须在使用它之前先解开它的掩码。相反，在Roshtyak使用该变量后，它会将其转换回掩码形式。这种隐藏方法使调试期间跟踪变量的工作变得复杂，并使搜索内存中已知变量值变得更加困难。

**循环变换**

Roshtyak 在一些循环条件下很有创意。它没有像 for (int i = 0; i < 1690; i++) 那样编写循环，而是将循环转换为for (int32\_t i = 0x06AB91EE;我! = 0 x70826068;i = i \* -0x509FFFF + 0xEC891BB1)。虽然两个循环都将执行 1690 次，但第二个循环要难得多。乍一看，不清楚第二个循环执行了多少次迭代，甚至不知道它是否会终止。在第二种情况下，在调试期间跟踪循环迭代的次数也要困难得多。

**包装**

如上所述，Roshtyak 的核心隐藏在多层包装之后。虽然所有的层看起来都像是最初编译到PE文件中，但除了严格必要的数据（入口点、节、导入和重定位）之外的所有数据都被剥离了。此外，Roshtyak 支持两种自定义格式来存储剥离的 PE 文件信息，各层轮流使用对应的格式。此外，段自定义格式是加密的，有时使用基于各种反分析检查结果生成的密钥。

这使得将 Roshtyak 的层静态解压到一个独立的 PE 文件中变得很困难。首先，必须对自定义格式进行逆向工程，并弄清楚如何解密加密段。然后，必须重构 PE 标头、段、段标题和导入表（重定位表不需要重构，因为重定位可以被关闭）。虽然这一切都是完全可行的，并且可以使用像 LIEF 这样的库来简化，但这可能需要大量的时间。除此之外，这些层有时是相互依赖的，在内存中动态分析 Roshtyak 可能更容易。

![15.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666163807100937.png "1666163807100937.png")

其中一个自定义 PE 类文件格式的段标题：raw\_size 对应于 SizeOfRawData，raw\_size + virtual\_padding\_size 实际上是 VirtualSize。没有 VirtualAddress 或 PointerToRawData 等效项，因为这些段是按顺序加载的。

**其他混淆技巧**

除了上述技巧之外，Roshtyak 还使用其他混淆技巧，包括：

垃圾指令插入；

导入哈希；

频繁清除内存；

混合布尔算术混淆；

冗余线程；

重多态性；

**核心功能**

既然我们已经描述了 Roshtyak 如何保护自己，那么看看它的实际作用可能会很有趣。 Roshtyak 的 DLL 相对较大，超过 1 兆字节，但是一旦消除了所有的混淆，它的功能就非常简单。它的主要目的是下载更多的有效载荷来执行。此外，它还执行通常的恶意软件操作，即建立持久性、提升权限、横向移动和泄露有关受害者的信息。

**持久性攻击**

Roshtyak 首先在 %SystemRoot%\Temp 中生成一个随机文件名，并将其 DLL 映像移动到那里。生成的文件名由2到8个随机小写字符与从硬编码列表中选择的随机扩展名组成。用于生成此文件名的PRNG的卷序列号为C:\。我们分析的示例是硬编码的7个扩展名（.log、.tmp、.loc、.dmp、.out、.ttf 和 .etl）。我们观察到其他示例中使用了其他扩展，这表明这个列表是动态的。 Roshtyak 也很有可能会使用随机生成的扩展。一旦完全构建，到Roshtyak DLL的完整路径可能看起来如C:\Windows\Temp\wcdp.etl这样。

将 DLL 映像移动到新的文件系统路径后，Roshtyak 将其修改后的时间戳记到当前系统时间。然后它继续设置 RunOnce(Ex) 注册表项，以实际建立持久性。注册表项是使用前面描述的间接注册表写入技巧创建的。插入密钥的命令可能如下所示：

RUNDLL32.EXE SHELL32.DLL,ShellExec\_RunDLL REGSVR32.EXE -U /s "C:\Windows\Temp\wcdp.etl."

这里有几点需要注意。首先，regsvr32 不关心它加载的 DLL 的扩展名，从而允许 Roshtyak 隐藏在 .log 等看似无害的扩展名下。其次，/s 参数将 regsvr32 置于静默模式。如果没有它，regsvr32将抱怨找不到名为DllUnregisterServer的导出。最后，请注意路径末尾的句号字符。该句号在路径规范化期间被释放，因此它实际上对命令没有影响。所以，我们不确定开发者的初衷是什么。它看起来像是被设计用来欺骗一些反恶意软件，使其无法将持久性条目与文件系统上的有效负载连接起来。

默认情况下，Roshtyak 使用 HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce 项进行持久化。但是，在某些情况下（例如，当它通过检查名为 avp.exe 的进程检测到 Kaspersky 正在运行时）将使用密钥 HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx。 RunOnceEx 项能够加载 DLL，因此在使用该项时，Roshtyak 直接指定 shell32.dll，省略了 rundll32的使用。

![16.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666163818202795.png "1666163818202795.png")

Roshtyak 建立的 RunOnceEx 持久性条目

**权限提升**

Roshtyak 使用 UAC 绕过和常规 EoP 漏洞来尝试提升其权限，与许多其他恶意软件只是盲目地执行开发者可以找到的任何 UAC 绕过/利用的恶意软件不同，Roshtyak 努力确定权限提升方法是否有可能成功。由于不必要地使用了不兼容的绕过/漏洞，这可能是为了降低检测的机会。对于 UAC 绕过，这涉及检查 ConsentPromptBehaviorAdmin 和 ConsentPromptBehaviorUser 注册表项。对于 EoP 漏洞利用，这是关于检查 Windows 内部版本号和补丁级别。

除了检查 ConsentPromptBehavior(Admin|User) 项之外，Roshtyak 还执行其他健全性检查以确保它应该继续绕过 UAC。即，它使用 SID S-1-5-32-544 (DOMAIN\_ALIAS\_RID\_ADMINS) 的 CheckTokenMembership 检查管理员权限。它还检查 KUSER\_SHARED\_DATA.SharedDataFlags 中 DbgElevationEnabled 标志的值。这是一个未记录的标志，在启用 UAC 时设置。最后，还有针对 BitDefender（由模块 atcuf32.dll 检测）、卡巴斯基（进程 avp.exe）和我们自己的 Avast/AVG（模块 aswhook.dll）的杀毒软件检查。如果检测到这些杀毒软件，Roshtyak 会避开选定的 UAC 绕过技巧，大概是那些可能导致被检测到。

至于实际的UAC旁路，主要有两种实现方法。第一个是 UACMe 中恰当命名的 ucmDccwCOM 方法的实现。有趣的是，当执行此方法时，Roshtyak 通过覆盖对应于主可执行模块的\_LDR\_MODULE 结构中的FullDllName 和BaseDllName 临时将其进程伪装成explorer.exe。此方法启动的有效负载是一个随机命名的 LNK 文件，使用 IShellLink COM 接口放入 %TEMP%。此 LNK 文件旨在通过 LOLBins（例如 advpack 或 register-cimprovider）重新启动 Roshtyak DLL。

第二种方法更像是一个 UAC 绕过框架而不是特定的绕过方法，因为多个 UAC 绕过方法遵循相同的简单模式：首先注册一些特定的 shell 打开命令，然后执行自动提升的 Windows 二进制文件（内部触发 shell 打开命令）。例如，可以通过向 HKCU\Software\Classes\ms-settings\shell\open\command 写入有效负载命令，然后从 %windir%\system32 执行 fodhelper.exe 来完成 UAC 绕过。基本上，同样的绕过可以通过用其他对替换ms-settings/fodhelper.exe来实现，例如mscfile/eventvwr.exe。Roshtyak使用以下6对来绕过UAC：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666163828142504.png "1666163828142504.png")

现在让我们看看 Roshtyak 用于提升权限的内核漏洞（CVE-2020-1054 和 CVE-2021-1732）。与 Roshtyak 中的常见情况一样，这些漏洞被加密存储，并且仅在需要时才解密。有趣的是，一旦解密，漏洞利用结果是具有完全有效标头的常规 PE 文件，与 Roshtyak 中的其他层不同，它们要么以 shellcode 形式存在，要么以自定义剥离的 PE 格式存储。此外，这些漏洞不像Roshtyak的其他漏洞那样容易混淆，所以它们的代码可以立即反编译，而且只使用了一些基本的字符串加密。我们不知道为什么攻击者让这些漏洞如此暴露，但这可能是由于位数的不同。虽然 Roshtyak 本身是 x86 代码（大段时间在 WoW64 下运行），但漏洞利用是 x64，考虑到它们利用 64 位代码中的漏洞，这是有道理的。可能 Roshtyak 的开发者使用的混淆工具是为 x86 设计的，不能移植到 x64。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666163837437092.png "1666163837437092.png")

Roshtyak利用CVE-2020-1054的代码片段，扫描IsMenu找到HMValidateHandle的偏移量

为了执行漏洞，Roshtyak 生成（AMD64 版本）winver.exe 并使用 KernelCallbackTable 注入方法获取漏洞代码以在其中运行。Roshtyak的这种注入方法的实现基本上与公共PoC相匹配，最大的区别是由于需要跨子系统注入而使用了略微不同的API函数(例如NtWow64QueryInformationProcess64而不是NtQueryInformationProcess或NtWow64ReadVirtualMemory64而不是ReadProcessMemory)。注入winver.exe的代码不是利用PE本身，而是稍微混淆的 shellcode，旨在将漏洞利用 PE 加载到内存中。

内核漏洞针对某些未打补丁的 Windows 版本。具体来说，CVE-2020-1054 仅用于版本号不高于 24552 的 Windows 7 系统。另一方面，CVE-2021-1732 的漏洞利用在 Windows 10 上运行，目标内部版本号范围为16353 到 19042。在利用CVE-2021-1732之前，Roshtyak还会扫描已安装的更新包，以查看是否安装了针对该漏洞的补丁。它通过枚举HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based services \Packages下面的注册表项，并检查KB4601319(或更高)的包是否存在。

**横向运动**

在横向移动方面，Roshtyak 只使用久经考验的 PsExec 工具。在执行 PsExec 之前，Roshtyak 通过检查与“众所周知的”WinAccountDomainAdminsSid 组匹配的 SID 来确保运行它是有意义的。如果未检测到域管理员权限，Roshtyak 将完全跳过其横向移动阶段。

Roshtyak 试图通过设置 Defender 排除项来绕过检测，因为 PsExec 通常被标记为黑客工具（有充分的理由）。它为 %TEMP% 设置一个路径排除（它将释放 PsExec 和其他用于横向移动的文件）。稍后，它会为执行 PsExec 的确切路径设置一个进程排除。

虽然我们希望PsExec被捆绑到Roshtyak中，但结果是Roshtyak从https://download.sysinternals[.]com/files/PSTools.zip按需下载PsExec。下载的zip归档文件被放入%TEMP%中，后缀名为.zip。然后使用Windows Shell COM接口(IShellDispatch)将PsExec从这个归档文件解压缩到%TEMP%中随机命名的.exe文件中。

PsExec 执行的有效负载是一个自解压包，由名为 IExpress 的工具创建。这是一个古老的安装程序，它是 Windows 的一部分，这可能就是使用它的原因，因为 Roshtyak 可以依赖它已经在受害者设备上。安装程序生成由使用自解压指令 (SED) 语法的文本文件配置。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221019/1666163846103339.png "1666163846103339.png")

Roshtyak 的 IExpress 配置模板

Roshtyak 使用具有三个占位符（%1、%2 和 %3）的 SED 配置模板，它在运行时将其替换为实际值。如上所示，配置模板是混合大小写编写的，通常在 Raspberry Robin 中经常使用。准备好SED配置后，它就会被写入 %TEMP% 中随机命名的 .txt 文件。然后，调用 iexpress 以使用 C:\Windows\iexpress.exe /n /q

生成有效负载后，Roshtyak就开始实际运行PsExec。 Roshtyak 可以通过两种方式执行 PsExec。第一个使用命令

**分析受害者**

USB 蠕虫往往有自己的活动。由于它们的蠕虫行为通常是完全自动化的，因此最初部署蠕虫的攻击者不一定完全控制它的传播位置。这就是为什么攻击者将蠕虫信标返回到他们的 C&C 服务器很重要的原因。有了信标机制，攻击者就可以获知他们控制的所有机器的信息，并可以利用这些信息对蠕虫进行管理。

发出的信标邮件通常包含有关受感染计算机的一些信息。这有助于有经济动机的攻击者决定如何利用攻击获利。Roshtyak 也不例外，它收集了有关每个受感染受害者的大量信息。 Roshtyak 将所有收集到的信息连接成一个大字符串，使用分号作为分隔符。这个大字符串然后被转移到Roshtyak的C&C服务器上。下面按顺序列出了过滤出来的信息。

外部 IP 地址（在 Tor 连接检查期间获得）;

一个硬编码到 Roshtyak 代码中的字符串，例如AFF123（我们无法确定这背后的含义，但它看起来像一个附属 ID）;

DLL 的 PE 标头的 16 位哈希（一些字段清零）与其 TimeDateStamp 的低 16 位异或。 TimeDateStamp 似乎是经过特殊设计的，因此异或会产生一个已知值。这可以作为篡改检查或水印的功能；

系统驱动器上 System Volume Information 文件夹的创建时间戳；

系统驱动器的卷序列号；

处理器计数 (GetActiveProcessorCount)；

IsWow64Process (\_PROCESS\_EXTENDED\_BASIC\_INFORMATION.Flags & 2)；

Windows 版本 (KUSER\_SHARED\_DATA.Nt(Major|Minor)Version)；

Windows 产品类型 (KUSER\_SHARED\_DATA.NtProductType)；

Windows 构建号 (PEB.OSBuildNumber)；

**本地管理权限**（ZwQueryInformationToken(TokenGroups)/CheckTokenMembership，检查 DOMAIN\_ALIAS\_RID\_ADMINS）；

域管理权限（检查 WinAccountDomainAdminsSid/WinAccountDomainUsersSid）；

系统时间 (KUSER\_SHARED\_DATA.SystemTime)；...