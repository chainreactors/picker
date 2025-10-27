---
title: DynamoRIO 9无法捕捉UWP数据的终级原因
url: http://blog.nsfocus.net/dynamorio-9/
source: 绿盟科技技术博客
date: 2022-11-16
fetch_date: 2025-10-03T22:53:13.201345
---

# DynamoRIO 9无法捕捉UWP数据的终级原因

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# DynamoRIO 9无法捕捉UWP数据的终级原因

### DynamoRIO 9无法捕捉UWP数据的终级原因

[2022-11-15](https://blog.nsfocus.net/dynamorio-9/ "DynamoRIO 9无法捕捉UWP数据的终级原因")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,002

只说这个版本，DynamoRIO-Windows-9.0.19181。

calc
tasklist | findstr Calculator
DynamoRIO-Windows-9.0.19181\bin64\drrun.exe -verbose -64 -attach <pid> -t drcov
DynamoRIO-Windows-9.0.19181\bin64\drrun.exe -verbose -64 -t drcov — calc

一种attach，一种直接run，这两种方式均无法捕捉Win10计算器的数据，在Ring3用Process Monitor发现dynamorio.dll加载失败，已经处理过”ALL APPLICATION PACKAGES (S-1-15-2-1)”的读取和执行权限。

云海用内核调试器跟了一下为何dynamorio.dll加载失败，找到终极原因。加载dynamorio.dll时，LdrpMapViewOfSection返回0xC0000269，其值含义如下

STATUS\_ILLEGAL\_DLL\_RELOCATION

{Illegal System DLL Relocation} The system DLL %hs was relocated in memory.
The application will not run properly. The relocation occurred because the
DLL %hs occupied an address range that is reserved for Windows system DLLs.
The vendor supplying the DLL should be contacted for a new DLL.

Calculator开了这个

[+0x000 ( 4: 4)] ForceRelocateImages : 0x1 [Type: unsigned long]

在内核调试器中直接改\_EPROCESS的MitigationFlags，去掉Calculator的ForceRelocateImages，就可以加载dynamorio.dll；后者设置了IMAGE\_FILE\_RELOCS\_STRIPPED，过不了ForceRelocateImages的检查。

用ProcessHacker查看Calculator的”Mitigation Policies”，第一行是

ASLR (high entropy, force relocate, disallow stripped)

下面有解释

Address Space Layout Randomization is enabled for this process. High entropy randomization is enabled. All images are being forcibly relocated(regardless of whether they support ASLR). Images with stripped relocation data are disallowed.

参看

————————————————————————–
IMAGE\_FILE\_HEADER structure (winnt.h)
https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image\_file\_header

#define IMAGE\_FILE\_RELOCS\_STRIPPED 0x0001 // Relocation info stripped from file.
————————————————————————–

IMAGE\_FILE\_RELOCS\_STRIPPED置位时，解释如下

Relocation information was stripped from the file. The file must be loaded at its preferred base address. If the base address is not available, the loader reports an error.

用CFF Explorer查看dynamorio.dll

————————————————————————–
File Header
Characateristics
Relocation info stripped from file
On
Data Directories
Relocation Directory RVA 0
Relocation Directory Size 0
————————————————————————–

dynamorio.dll不只是设置了IMAGE\_FILE\_RELOCS\_STRIPPED，也实际抹除了重定位信息。

用livekd查看ForceRelocateImages

“X:\Windows Kits\10\x64\Debuggers\x64\livekd.exe” -k “X:\Windows Kits\10\x64\Debuggers\x64\kd.exe”

kd> !process 0 0 Calculator.exe
PROCESS ffff8c040d4f5340

kd> .process /p /r ffff8c040d4f5340

kd> dt nt!\_EPROCESS ImageFileName MitigationFlags MitigationFlagsValues. ffff8c040d4f5340
+0x5a8 ImageFileName : [15] “Calculator.exe”
+0x9d0 MitigationFlags : 0x38
+0x9d0 MitigationFlagsValues :
…
+0x000 ForceRelocateImages : 0y1
…

kd> dt nt!\_EPROCESS MitigationFlagsValues.ForceRelocateImages ffff8c040d4f5340
+0x9d0 MitigationFlagsValues :
+0x000 ForceRelocateImages : 0y1

kd> dx ((nt!\_EPROCESS \*)0xffff8c040d4f5340)->MitigationFlags
: 0x38 [Type: unsigned long]

kd> dx ((nt!\_EPROCESS \*)0xffff8c040d4f5340)->MitigationFlagsValues
…
[+0x000 ( 4: 4)] ForceRelocateImages : 0x1 [Type: unsigned long]
…

kd> dx ((nt!\_EPROCESS \*)0xffff8c040d4f5340)->MitigationFlagsValues.ForceRelocateImages
: 0x1 [Type: unsigned long]

查看系统中所有ForceRelocateImages置位的进程

kd> dx @$ForceRelocateImages = 0x10
kd> dx -r1 @$cursession.Processes.Where(p=>(p.KernelObject.MitigationFlags & @$ForceRelocateImages) != 0)

[0x424] : fontdrvhost.exe
[0x1560] : dllhost.exe
[0x1cac] : StartMenuExperienceHost.exe
…
[0x39bc] : Microsoft.Photos.exe
…
[0x3de8] : SearchApp.exe
[0x424c] : ShellExperienceHost.exe
…
[0x375c] : Calculator.exe
[0x1dbc] : RuntimeBroker.exe

或者

kd> dx -r1 @$cursession.Processes.Where(p=>(p.KernelObject.MitigationFlagsValues.ForceRelocateImages == 1))

尝试禁用Calculator的ForceRelocateImages，无果。

> Get-Item -Path “C:\Program Files\WindowsApps\Microsoft.WindowsCalculator\_10.2103.8.0\_x64\_\_8wekyb3d8bbwe\Calculator.exe” | %{ Get-ProcessMitigation -Name $\_.Name } | findstr ForceRelocateImages
ForceRelocateImages : NOTSET

ForceRelocateImages缺省是NOTSET，尝试禁用

> Get-Item -Path “C:\Program Files\WindowsApps\Microsoft.WindowsCalculator\_10.2103.8.0\_x64\_\_8wekyb3d8bbwe\Calculator.exe” | %{ Set-ProcessMitigation -Name $\_.Name -Disable ForceRelocateImages }
ForceRelocateImages : OFF

$ reg.exe query “HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Calculator.exe”

HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Calculator.exe
MitigationOptions REG\_BINARY 000200000000000000000000000000000000000000000000
MitigationAuditOptions REG\_BINARY 000000000000000000000000000000000000000000000000
EAFModules REG\_SZ

MitigationOptions缺省全零，禁用ForceRelocateImages后出现02，启用后出现01。

也可以GUI

————————————————————————–
设置
更新和安全
Windows安全中心
应用和浏览器控制
Exploit Protection设置
程序设置
————————————————————————–

禁用ForceRelocateImages后，不知是否要重启生效，反正不重启时，用ProcessHacker、livekd确认仍然启用ForceRelocateImages。或许对UWP无法真正禁用ForceRelocateImages，内核调试器那种不算。

若从源码自编译DynamoRIO，改用反射式DLL加载，应该可以加载dynamorio.dll；另一种可能的选择是，编译时允许dynamorio.dll重定位，不清楚DynamoRIO是否要求该DLL不得重定位。这些都停留在探讨阶段，无测试动力。

未实测加载dynamorio.dll之后是否就能捕捉UWP的数据，不排除有其他幺蛾子等着，也未测试最新版DynamoRIO是否有变化，本文只是记录云海关于ForceRelocateImages的调试结论。

参看

————————————————————————–
MitigationFlags in the EPROCESS
https://www.geoffchappell.com/studies/windows/km/ntoskrnl/inc/ntos/ps/eprocess/mitigationflags.htm

Customize exploit protection
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/customize-exploit-protection

Exploit Protection Reference
https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference

Understanding a New Mitigation: Module Tampering Protection – Yarden Shafir [2022-08-16]

> [Understanding a New Mitigation: Module Tampering Protection](https://windows-internals.com/understanding-a-new-mitigation-module-tampering-protection/)

Security Features You’ve Never Heard of (but should) – Yarden Shafir [2022-02]
https://github.com/yardenshafir/conference\_talks/blob/main/Paranoia\_2022\_security\_mitigations.pdf

Software defense: mitigating common exploitation techniques – [2013-12-11]

> [Software defense: mitigating common exploitation techniques](https://msrc-blog.microsoft.com/2013/12/11/software-defense-mitigating-common-exploitation-techniques/)

(The Force ASLR feature has been enabled by default for UWP)

Clarifying the behavior of mandatory ASLR – Matt Miller [2017-11-21]

> [Clarifying the behavior of mandatory ASLR](https://msrc-blog.microsoft.com/2017/11/21/clarifying-the-behavior-of-mandatory-aslr/)

————————————————————————–

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文...