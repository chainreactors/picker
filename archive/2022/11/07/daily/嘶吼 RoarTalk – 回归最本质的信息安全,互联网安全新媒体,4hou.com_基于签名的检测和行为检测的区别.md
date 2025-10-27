---
title: 基于签名的检测和行为检测的区别
url: https://www.4hou.com/posts/nJjD
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-07
fetch_date: 2025-10-03T21:52:02.890897
---

# 基于签名的检测和行为检测的区别

基于签名的检测和行为检测的区别 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 基于签名的检测和行为检测的区别

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-11-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)143108

收藏

导语：我们会在本文中介绍基于签名的检测和基于行为的检测之间的主要区别。此外，还会举例说明了绕过各个检测的示例。

我们会在本文中介绍基于签名的检测和基于行为的检测之间的主要区别。此外，还会举例说明了绕过各个检测的示例。

经常会有人有疑问，为什么在有关Packer（封隔器）被发布后，MSF- 或CobaltStrike- (CS)有效负载仍然会被检测到。答案无非有两种：

1.基于签名的检测被绕过了；2.基于行为的检测被触发并终止进程。

使用我们的自定义封隔器将导致反扫描。被封隔的MSF有效负载如下：

![1.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470636103506.jpeg "1665470636103506.jpeg")

但这并不意味着，在运行时执行时，这些杀毒程序不会检测到有效负载。为什么会出现这种情况？

**基于签名的检测**

基于签名的检测非常简单。最早的杀毒程序有一个带有File-Hashes的签名数据库，他们只是将磁盘上任何可执行文件的哈希与已知的恶意可执行程序哈希进行比较。例如，该数据库包含Mimikatz发布二进制文件的SHA1/MD5哈希。改变一个可执行文件的哈希值就像操纵其中的一个字节一样简单，所以这种检测并不可靠。

基于这一事实，安全供应商转而检测特定的字节模式(Byte Pattern)签名。因此，为了继续使用Mimikatz的示例，具体的字节模式/十六进制值被标记如下：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470643230804.png "1665470643230804.png")

可以看到，不仅要为每个已知的恶意二进制文件/有效负载标记一个模式，而且要使用多个常见模式。Mimikatz始终是基于签名的检测的一个很好的示例，因为通常供应商有几十种Mimikatz二进制检测的模式。通过这种方式，稍微修改过的版本也能被检测到。

甚至可以使用yara规则构建更高级的检测。这些规则可以扫描文件或内存内容，并允许更复杂的条件和不同模式的组合。Mimikatz yara规则的一个示例如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470652138819.png "1665470652138819.png")

在本示例中，如果在文件或内存中找到上述三个字符串，则会触发此规则，AV/EDR程序可以执行警报或终止进程等操作。例如，我们在构建自定义Mimikatz二进制代码的文章中描述的技术就可以绕过这样的检测。

**封隔器的内部工作原理**

首先要了解封隔器的基本工作原理，了解它能做什么，不可能做什么。最后利用一个程序将一个有效负载封装到另一个程序中，以避免对其进行基于签名的检测。因此，如果像Mimikatz这样的负载包含特定的字符串，那么这些字符串将在生成的二进制文件中不再可见。包装过程可以通过某种编码/混淆或加密来完成。我个人更喜欢加密有效负载，因为这将产生最好的随机性，因此基于签名的检测最少。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470661116538.png "1665470661116538.png")

这种经过编码或加密的负载必须在生成的加载器程序中解码/解密，以便可以从内存中执行明文负载。

根据有效负载的不同，封隔器也可以在当前进程或远程进程中删除更多检测：

如果你的封隔器正在打补丁/绕过AMSI，你可以安全地从内存执行不同的已知恶意脚本(PS1,VBA,JS等)或c#程序集。

为了绕过基于ETW的检测，封隔器还可以通过不同的发布技术修补/绕过ETW。

基于挂钩的Win32 API检测可以通过取消挂钩或直接/间接使用Syscall来绕过。

基于熵的检测将检测到许多封隔器，因为有效负载的加密将由于随机性而导致非常高的熵。这可以通过在生成的二进制中添加数千个单词来绕过，因为这再次降低了熵。

但是，即使所有这些技术都得到了应用，仍然存在更多潜在的“问题”:

1.内存扫描；

2.行为检测；

3.攻击者。

一般来说，使用封隔器也可以绕过内存扫描，但这非常有限。

**内存扫描和常用的绕过技术**

由于基于签名的检测很容易被封隔器技术绕过，越来越多的AV/EDR供应商倾向于使用扫描进行内存分析。这些扫描通常不会在所有进程中一直进行，因为这会消耗太多资源，但可能会由特定条件触发。

例如，内存扫描通常在以下情况下出现：

生成一个新进程，例如运行一个可执行文件；

进程的行为触发内存扫描；

第一个很容易绕过。例如，即使是封隔器也可以在解码/解密真正的有效负载之前休眠一段时间。在这种情况下，将进行内存扫描，但不会发现任何东西，因为负载仍然是加密的。仍然有方法检测Win32基于睡眠的内存扫描绕过，例如这里演示的。作为使用Sleep的替代方案，你也可以在特定的时间内执行伪代码或进行计算。除了使用Sleep，还有许多其他替代方法。

但一般来说，绕过内存扫描有以下三种方法：

更改/修改有效负载的源代码，以避免基于签名的检测；

更改有效负载的行为，以便永远不会触发内存扫描；

内存加密。

我个人更喜欢第一种选择，它在每个程序中都是一次性的，只要新的代码库不公开，它也不应该在未来被检测到。

绕过基于行为的内存扫描是比较困难的，这取决于你的有效负载的行为。试想一下Mimikatz的行为（例如，用OpenProcess打开LSASS的句柄）会触发一次扫描，此时，无法从内存中隐藏Mimikat，因为它需要进行加密才能工作。因此，Mimikatz不会选择内存加密。

对于像Cobalt Strike这样著名的C2框架，最常见的选择是内存加密。但是如果你没有访问源代码的权限，就不可能修改它以避免内存检测。一般来说，C2框架是这项技术的优先选择，因为它们大部分时间都处于休眠状态。如果一个程序什么也不做，它的内存内容可以在这个时间段内被加密，而不会出现任何问题。

**基于行为检测的一些示例和绕过**

但是，哪些行为会在运行时触发AV/EDR操作或内存扫描呢？基本上全都可以。将内容写入内存，以特定的顺序或时间框架加载特定的库，创建注册表项，执行初始HTTP请求或任何其他操作。

我将在这里举几个例子，介绍相应绕过技术。

根据我的个人经验，AV/EDR在检测到特定行为后极少立即终止进程。这是因为AV/EDR供应商不希望有太多的误报结果。由于误报结果与终止进程的行为会导致生产环境的中断，这是非常糟糕的。所以他们需要几乎100%的确定，一个行为肯定是恶意程序终止相应的进程。这也是为什么许多供应商将行为检测与内存扫描结合起来，以验证他们发现了恶意内容。

**Fodhelper UAC绕过示例**

基于行为的检测的一个很好的示例是带有Windows Defender的Fodhelper UAC绕过。这个方法非常流行，但也很容易被利用，因为它只需要创建一个注册表项，然后调用fodhelper.exe：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470671201403.png "1665470671201403.png")

在启用杀毒软件的情况下执行此操作将导致以下检测：

![6.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470681772547.jpeg "1665470681772547.jpeg")

此警报既不会终止正在执行的进程，也不会终止新生成的进程，但仍会导致任何攻击中的检测。检测本身不能绕过AMSI，修补ETW也无济于事。因为这是触发此警报的特定行为。

我对此处标记的内容进行了一些简单的试错分析，发现杀毒软件不喜欢HKCU:\Software\Classes\ms-settings\Shell\Open\command(Default) 条目以及目录\*C:\windows\system32\*和\*C:\windows \syswow64\*中的任何.exe。

因此，触发警报的行为是使用其中一个字符串在上述目录中创建注册表项。

幸运的是，我们不需要指定.exe来执行二进制文件，也不需要两个目录来进行攻击。因此，作为一种替代方案，我们可以直接将e.G. a C2-Stager复制到任何可写目录中，并使用UAC-Bypass执行它，而无需调用扩展名。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470690151570.png "1665470690151570.png")

但到2022年，许多OffSec用户将意识到，在安装了AV/EDR的系统上运行任何未签名的可执行文件可能不是一个好主意。因此，作为一种替代方案，我们还可以执行任何经过签名的可信可执行文件，并将相应的Sideloading-DLL放到相同的目录中。还有第三种选择，就是我们可以将rundll32.exe复制到我们的可写目录中并在那里执行它。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470700112873.png "1665470700112873.png")

**基于Meterpreter行为的检测**

切记，不要使用分段有效负载，它们会被杀毒软件捕获。因此，在我们的示例中，我们将生成用于执行的不分段的反向HTTPS Shellcode。这可以通过以下命令来实现：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470709876379.png "1665470709876379.png")

我不会在本文介绍执行Shellcode的方式，因为我只想展示行为检测，但通常您需要以下内容：

对Shellcode进行加密并在运行时解密，以避免在磁盘上签名，或者在运行时从远程Web服务器加载它；

使用直接或间接的系统调用执行，否则Shellcode将在执行前被标记；

在这种情况下，无需修补AMSI/ETW即可使Meterpreter运行。

但是，即使你使用系统调用绕过了基于签名的磁盘检测和Shellcode检测，你也应该能够看到一个新的 Meterpreter Session传入：

![10.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470721605374.jpeg "1665470721605374.jpeg")

但这只是意味着，我们的初始有效负载成功地执行了。一秒钟后，进程被终止并出现以下检测：

![11.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470729128645.jpeg "1665470729128645.jpeg")

同样，这是一个基于行为的检测，由附加的DLL文件触发，通过普通Win32 API和反射DLL注入技术加载。在本例中，stdapi-DLL的注入触发了一个警报。

在msfconsole提示符中，你可以通过以下命令禁用stdapi DLL的加载：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470738122249.png "1665470738122249.png")

这样，你就应该可以很好地接收Meterpreter Session：

![13.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470747979039.jpeg "1665470747979039.jpeg")

然而，禁用stdapi加载将导致你的Meterpreter-Session中几乎没有命令/模块，只有“内核命令”可用。

等待几分钟后，你可以使用以下命令手动加载stdapi，但仍应没有检测：

![14.JPG](https://img.4hou.com/uploads/ueditor/php/upload/image/20221011/1665470757565904.jpeg "1665470757565904.jpeg")

这种基于行为的检测是关于什么的？我不能百分之百地肯定，但很可能是以下因素的组合：

1.新生成的进程；

2.在调用用于反射加载DLL的特定Windows API之前，新进程的时间框架x；

3.内存扫描，用于验证恶意内容；

4.内存中Meterpreter的检测和终止进程的操作。

注意：这是绕过Meterpeter防御行为检测的唯一可能方法。

如上所述，绕过内存扫描的一个通用方法是修改源代码以避免内存中的签名。绕过内存扫描的一个通用方法是修改源代码以避免内存中的签名，因此修改源代码是另一种选择，Meterpreter源代码混淆的自动化方法可以点击这里。这样做之后，就能够在启用autostdapi-Loading的情况下避免这种检测。

第三种方法是内存加密，这对于Meterpreter来说并不容易实现，因为在请求命令之前，HTTP/HTTPS源代码不像许多其他c2框架那样在时间框架x上休眠。它只是抛出许多HTTP(S)请求，其间有一些小延迟。所以内存加密会中断这个过程。如果你使用这个方法，那么你需要在源代码中自己集成一个带有内存加密的自定义Sleep-function。

**Cobalt Strike检测**

Cobalt Strike很可能是最复杂、分析最深入的C2框架。这很可能是因为在过去几年里，它被许多不同的攻击组织在野外使用。不更改默认设置在大多数环境中是不可用的，因为这会立即被检测到。

即使使用自定义的打包器/加载器和系统调用来执行Shellcode，在许多环境中仍然会失败。因此，我会解释作为操作员在使用此框架时需要做的最低要求和修改。

C2服务器/基础设施最低要求：

1.禁用Malleable配置文件中的分段，如果启用了该功能，你的植入程序几乎会立即被终止，因为有许多Internet范围内的自动扫描器下载第二阶段来分析和共享它。

2.你必须使用带有许多不同重要绕过设置的自定义Malleable C2-Profile来绕过一些检测。

3.必须在C2服务器前面使用重定向器。此重定向程序应释放/阻止已知的沙盒分析IP范围，并且仅允许和重定向那些符合Malleable C2配置文件的请求。RedWarden或...