---
title: 朝韩网络攻击一角：APT37改用LNK文件大肆传播RokRAT
url: https://www.4hou.com/posts/QKnq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-10
fetch_date: 2025-10-04T11:38:49.601195
---

# 朝韩网络攻击一角：APT37改用LNK文件大肆传播RokRAT

朝韩网络攻击一角：APT37改用LNK文件大肆传播RokRAT - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 朝韩网络攻击一角：APT37改用LNK文件大肆传播RokRAT

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-05-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)318842

收藏

导语：本文是Check Point根据其2022年7月首次发现的一个RokRAT样本来做的深入分析。

![微信截图_20230507224157.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472580149147.png "1683472580149147.png")

本文是Check Point根据其2022年7月首次发现的一个RokRAT样本来做的深入分析。

早在 2022 年 7 月，APT37（Inky Squid、RedEyes、Reaper或ScarCruft）就开始试验使用超大 LNK 文件传播 RokRAT 活动，企图利用不受信任来源的宏发起攻击，巧的是，同月微软开始默认阻止跨 Office 文档的宏。与以前一样，攻击的目标还是韩国的目标。

研究结果表明，用于最终加载ROKRAT的各种多阶段感染链被用于其他攻击，导致传播与同一攻击者相关的其他工具。这些工具包括另一个自定义后门，GOLDBACKDOOR和Amadey。

在前几年，ROKRAT感染链通常涉及带有漏洞的恶意朝鲜文字处理器（HWP，韩国流行的文档格式）文档或带有宏的Microsoft Word文档。虽然一些ROKRAT样本仍然使用这些技术，但传播方式上还是进行了改进，即使用伪装成合法文档的LNK文件传播ROKRAT。这种转变并不是ROKRAT独有的，而是代表了2022年非常流行的更大趋势。

**ROKRAT的背景介绍**

Talos于2017年4月首次报道了APT37开发的ROKRAT（也称为DOGCALL），这个工具被用来针对韩国的政府部门，记者、活动人士和脱北者。根据最初的报告，其中一个ROKRAT样本使用Twitter作为其命令和控制（C&C）基础设施，而另一个则依赖于Yandex和Mediafire。后一个更接近于如今ROKRAT的活动方式，依赖云文件存储服务作为一种C&C机制。

最初只支持Windows，多年来ROKRAT已经适应了其他平台，在野外发现了macOS和Android版本。macOS版本，也称为CloudMensis，于2022年7月由ESET首次描述。虽然Android版本的ROKRAT已经存在了很长时间，但InterLab和S2W都在Android上推出了一个更新版本的ROKRAT，称为RambleOn（Cumulus）。所有这些都表明，这种恶意软件仍在迭代中。

APT37的许多工具都是自定义编写的工具，如ROKRAT，包括（但不限于）最近报道的M2RAT、Konni RAT、Chinotto和GOLDBACKDOOR。然而，攻击者也会使用Amadey等普通恶意软件。使用普通恶意软件使得将攻击归因于特定组织变得更加困难，因为它广泛可用，任何人都可以获得它。

今年2月，AhnLab报告了一种名为Map2RAT（简称M2RAT）的新RAT。这种RAT利用隐写术技巧，将可执行文件隐藏在JPEG文件中以逃避检测。今年3月，Sekoia和ZScaler都发布了APT37使用钓鱼网站和PowerShell后门的报告，ZScaler导致了另一个名为Chinotto的植入程序的传播。

**诱饵和感染链**

在过去的四个月里，我们观察到多个感染链导致了ROKRAT的传播。在大多数情况下，LNK文件会启动攻击，尽管在少数情况下，DOC文件被用于相同的目的（以前的ROKRAT攻击中的方法）。在分析ROKRAT感染链的过程中，研究人员发现了导致Amadey传播的攻击链，Amadey是一种在地下论坛上出售的商业RAT。尽管攻击的性质不同，但研究人员认为所有这些攻击都是由相同的攻击者策划的。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472629758807.png "1683472629758807.png")

诱饵和感染链的时间线

**诱饵LNK感染链**

2022年4月，Stairwell发表了对GOLDBACKDOOR的详细分析，这是一种针对韩国记者的有针对性攻击中使用的恶意软件。Stairwell对利用运行PowerShell的大型LNK文件的感染链进行了彻底分析，导致在释放诱饵文档的同时执行新发现的恶意软件。这项技术是一个名为EmbeddExeLnk的公共工具的独特实现。

虽然最初与GOLDBACKDOOR有关，但对最近与APT37相关的诱饵的分析表明，这种技术已经成为一种重要的方法，用于传播与同一攻击者相关的另一种工具，即ROKRAT。ROKRAT和GOLDBACKDOOR加载机制的实现非常相似，只有在检索有效负载时才能区分。

在过去的几个月里，研究人员能够利用ZIP和ISO档案中提供的这种独特实现来识别多个诱饵。只有其中一些诱饵被证实会导致ROKRAT的传播。所有的诱饵都以韩国国内外事务为主题。

**LNK感染链分析**

目前已知的所有LNK都会导致几乎相同的感染链。下面以“利比亚项目”中描述的一个感染为例进行说明：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472660191105.png "1683472660191105.png")

“利比亚项目”诱饵的感染链

点击恶意LNK文件会触发PowerShell的执行，并启动以下感染链：

1.PowerShell从LNK中提取文档文件，将其放入磁盘，然后打开它。这个文件是一个诱饵，欺骗用户以为他们只是打开了一个普通的PDF或HWP文件。

2.PowerShell从LNK中提取BAT脚本，将其放入磁盘并执行。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472677159692.png "1683472677159692.png")

3.BAT脚本执行一个新的PowerShell实例，该实例从OneDrive下载有效负载，通过将有效负载的第一个字节作为密钥对其进行解码，并将其与有效负载的其余部分进行异或。

4.生成的有效负载以反射方式注入PowerShell，使其作为新线程运行。

5.shellcode使用四字节异或密钥对有效负载的ROKRAT部分进行解码并执行它。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472695134265.png "1683472695134265.png")

**典型的ROKRAT感染链**

ROKRAT运营商在采取新的行为同时，仍夹杂了一些旧习惯，比如，ROKRAT仍然使用恶意Word文档进行部署。

2022年12月，有人向VirusTotal提交了一份恶意的Word文档，命名为“.doc”（Case fee\_Payment request.doc）。该文件本身包含一个输入个人和银行信息的简短表格。然而，对该文件的仔细检查显示，其中提到了韩国的统一部。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472714172744.png "1683472714172744.png")

“利比亚项目”诱饵的感染链

一旦用户打开恶意文档并允许宏执行，就会触发以下感染链：

1.宏通过设置AccessVBOM注册表项以加载其他代码来检查并确保它可以访问Visual Basic项目。

2.宏解码一个新的VBA脚本，将其写入宏中的一个新模块，然后执行它。这是在不将任何代码释放到磁盘的情况下完成的。

3.第二个VBA脚本运行notepad.exe并将shellcode注入其中。

4.shellcode在notepad.exe中运行，并进入OneDrive下载ROKRAT有效负载并在内存中执行它。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472730162556.png "1683472730162556.png")

这里描述的感染链与MalwareBytes在2021年1月报告的非常相似，MalwareBytes也通过将shellcode注入notepad.exe并将RAT加载到内存中来传播ROKRAT。然而，MalwareBytes研究中描述的样本的编译日期是从2019年开始的，而checkpoint发现的新ROKRAT样本似乎是在2022年12月21日编译的，距离文件提交给VirusTotal只有六天时间。

此外，在2023年4月发现的另一个文件似乎是同一感染链的一部分，只是这次注入的目标进程是mspaint.exe，该文件以朝鲜的核武器为主题。不幸的是，在我们进行分析时，URL不再响应下载负载的请求。但是，这份文件很有可能也是为了传播ROKRAT。

**与Amadey的关联**

2022年11月初，一个名为securityMail.zip的文件被提交给了VirusTotal。这个ZIP包含两个LNK，它们的大小都不到5MB，令人怀疑。PowerShell命令在两个LNK中的实现是唯一的，并且仅与ROKRAT和GOLDBACKDOOR LNK感染重叠。然而，这个特定的感染链最终传播了Amadey，这是一种可在网络犯罪论坛上出售的恶意软件。Amadey过去曾被认为是Konni开发的，Konni组织与APT37的背景类似。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472747185352.png "1683472747185352.png")

“安全邮件”诱饵的感染链，打开这些LNK中的任何一个都会产生恶意流程：

1.PowerShell命令从LNK中提取一个诱饵HTML文件，并将其放入磁盘，其方式与ROKRAT感染链类似：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472765217169.png "1683472765217169.png")

2.这个PowerShell还从包含DLL的LNK中提取一个ZIP文件。然后将DLL作为mfc100.dll放入磁盘。

3.PowerShell最终也从LNK中提取了一个BAT脚本，将其放到磁盘上并执行。

4.BAT脚本运行带有rundll32.exe的DLL并删除自身。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472779189613.png "1683472779189613.png")

对DLL文件的初步分析显示，它包含了商业代码保护解决方案Themida。在分析了它执行的内存转储后，我们能够确认这实际上是Amadey。诱饵HTML文件中包含一个伪造的Kakao银行的登录页面，Kakao是韩国一家受欢迎的银行。对HTML的进一步分析表明，它不是用于密码钓鱼，而是用来隐藏攻击者的意图。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472798138309.png "1683472798138309.png")

伪造Kakao银行登录页面

**ROKRAT技术分析**

ROKRAT只是APT37使用的许多自定义工具之一，但它绝对是通用且强大的。ROKRAT主要侧重于运行额外的有效负载和大量的数据窃取。它的C&C功能依赖于云基础设施，包括DropBox、pCloud、Yandex cloud和OneDrive。ROKRAT还收集有关计算机的信息，以防止被其他竞争者再次感染。

虽然在过去几年中，ROKRAT并没有发生重大变化，但其破坏力依然不容小觑，这可以归因于它巧妙地使用内存执行，将C&C通信伪装成潜在的合法云通信，以及额外的加密层，以阻碍网络分析和逃避网络签名。因此，最近发表的关于ROKRAT的文章并不多。

**通用恶意软件结构**

ROKRAT的大多数样本都有一个非常简单的WinMain函数。到目前为止分析的所有样本都包含一个数据收集功能（CollectMachineData，如下图所示），该功能在主RAT线程（MainRATThread）执行之前执行。这个线程初始化RAT并运行一个循环，以尝试从C&C获取命令，然后解析并执行它们。

WinMain函数中嵌入了两个额外的功能，我们只在样本的一个子集中观察到了这两个功能。第一个检查RAT是否能够写入TEMP目录（CheckTemp，如下图所示）。第二个创建了一个线程（KillCertainProcessesThread），用于停止与以前利用Hancom Office漏洞的感染载体相关的某些进程。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472815207319.png "1683472815207319.png")

ROKRAT中WinMain函数的示例

**受害目标分析**

ROKRAT在执行时调用的第一个函数旨在收集有关受感染计算机的数据。在初始攻击阶段，这可能有助于攻击者区分这是否是一个期望的目标，然后采取相应的行动。

在这个函数（以及许多其他函数）中，ROKRAT使用加密字符串来防止静态分析看不到使用的一些技术。此处收集的信息包括程序是否在WOW64上运行（表示32位应用程序在64位窗口上运行）、vmtoolsd.exe的版本（VMWare Tools Daemon，如果已安装）、注册表中的SMBIOS数据以及注册表中的系统BIOS版本。

RAT还收集用户名、计算机名和RAT正在执行的可执行文件的完整路径。后者很重要，因为感染链通常涉及将ROKRAT PE文件注入现有进程的内存。换言之，这使攻击者能够查看ROKRAT是否在预期的进程中执行，如powershell.exe或notepad.exe。最后，该函数检查可执行文件是否有权在C:\Windows下创建用于写入的文件。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230507/1683472833210849.png "1683472833210849.png")

CollectMachineData收集有关受感染计算机的各种信息

虽然在上述函数中收集了大量目标的数据，但在ROKRAT开始接受命令之前，还有另一个数据收集函数在主RAT线程的上下文中运行。第二个函数检查调用IsDebuggerPresent API，将结果存储...