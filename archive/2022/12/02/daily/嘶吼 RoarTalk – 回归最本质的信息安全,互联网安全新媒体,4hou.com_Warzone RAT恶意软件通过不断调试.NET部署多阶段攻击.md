---
title: Warzone RAT恶意软件通过不断调试.NET部署多阶段攻击
url: https://www.4hou.com/posts/2JBA
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-02
fetch_date: 2025-10-04T00:16:27.718290
---

# Warzone RAT恶意软件通过不断调试.NET部署多阶段攻击

Warzone RAT恶意软件通过不断调试.NET部署多阶段攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Warzone RAT恶意软件通过不断调试.NET部署多阶段攻击

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)158896

收藏

导语：本文介绍了如何创建自定义.NET程序来帮助调试直接在内存中加载和调用的DLL。

FortiGuard实验室最近发现了一封假装来自匈牙利政府的电子邮件。它通知用户，他们的政府门户的新凭证已经附加。然而，附件是一个压缩的可执行文件，在执行时，它将把Warzone RAT提取到内存中并运行它。在我们最初发现的几天后，匈牙利国家网络安全中心也发布了关于这次攻击的警告。

受影响的平台：Microsoft Windows；

受影响方：Microsoft Windows用户；

影响：为攻击者提供远程访问；

严重级别：高；

**感染载体**

最初的感染是通过模仿匈牙利政府门户网站的仿冒电子邮件（图1）发生的。该门户用于在线开展公务，如提交文件、订购ID等。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610112348879.png "1669609547113251.png")

含有Warzone RAT恶意软件附件的恶意邮件

电子邮件告诉受害者，他们的凭据已更改，并附上了新的凭据。完整的翻译是：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610113542794.png "1669609559789345.png")

从语言上看，这封邮件是由母语为英语的人写的，然而这封邮件并没有使用官方通信应有的语法。

附件是一个zip文件，其中包含一个伪装为PDF的可执行文件。如上图所示，该文件包含一个模仿Adobe PDF Reader图标的图。文件名以pdf结尾，但扩展名为.exe。然而，在默认的Windows安装中，文件扩展名是隐藏的，它看起来像一个实际的PDF文件。用户唯一的警告是文件资源管理器将文件类型显示为“应用程序”，这意味着它是可执行文件而不是文档。但这对普通用户来说可能并不明显。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610114186676.png "1669609568102187.png")

伪装成PDF的可执行文件

**俄罗斯套娃式的混淆**

当我们开始分析“Uj bejelentkezEsi adatai·pdf.exe”时，我们很快意识到它就像一个俄罗斯套娃混淆，但不是每次打开一个娃娃都会得到一个更小的娃娃，而是得到越来越多的混淆的.NET二进制文件，这就是我们将在本节中看到的。

“Uj bejelentkezEsi adatai·pdf.exe”是一个32位的.NET可执行文件。一旦在dnspy（一个著名的.NET反编译程序）中进行了反编译，我们就会发现源代码很简单，同时也很容易混淆。代码的一般结构如下图所示。原始二进制文件可能在重命名为“Uj bejelentkezEsi adatai·pdf.exe”之前被称为iANO。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610115107291.png "1669609588187097.png")

“Uj bejelentkezEsi adatai·pdf.exe”的程序结构

代码显示了BattleShipLiteLibrary和一个计算器的混合体，这看起来像是桌面游戏Battleship的实现。下图显示了实现计算器的实际代码。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610115168657.png "1669609598141990.png")

计算器的实现

有时它看起来像一个计算器，行为也像一个计算器，但它仍然不是一个真正计算器。在本例中，为计算器设置用户界面的InitializeComponent()函数也会在最后调用PerformLayout()函数。然后该函数继续调用ResourceTemplateDefine()函数。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610116770317.png "1669609610280300.png")

从资源加载代码

ResourceTemplateDefine()函数加载名为“Web”的资源。起初，它似乎将其解释为位图，但最后，它将其转换为程序集。如果我们在十六进制编辑器中查看这个资源，我们会看到它有一个位图标头。但是当我们进一步观察时，它还包括MZ字符，这是可移植可执行文件(PE)的神奇值。在底部，我们甚至可以看到臭名昭著的“此程序不能在DOS模式下运行”字符串，这是PE文件的另一个标志。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610117204152.png "1669609620164526.png")

检查“Web”资源发现它隐藏了一个PE文件

该PE文件从资源中加载。下图显示了使用GetMethod()加载它的方法，并调用其中一个方法。另一个图显示了在调试器中调用的方法是' sk41Ua2AFu5PANMKit.abiJPmfBfTL6iLfmaW.Y5tFvU8EY() '。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610118137992.png "1669609631486660.png")

从PE文件加载并调用特定的方法

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610119951843.png "1669609643164178.png")

显示被调用方法名称的调试器

**KeyNormalize.dll**

“Web”资源中的PE文件的原始名称是KeyNormalize.dll。从被调用函数的名称中，我们已经可以预期它是混淆的。由于它是另一个.NET可执行文件，我们可以在dnspy中打开它并轻松检测，并使用SmartAssembly确认它已被混淆。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610120592771.png "1669609654753637.png")

使用SmartAssembly混淆器

De4Dot是一个去混淆器工具，在消除二进制文件的混淆方面很有效率。但是，它不能解析混淆的字符串。为此，我们编写了一个可以解析字符串的定制程序。

在静态分析KeyNormalize.dll之后，我们看到它从资源加载另一个二进制文件并执行函数调用，如前面所示。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610121179102.png "1669609665204149.png")

从资源加载程序集并调用它的一个函数

我们可以恢复二进制文件，并再次使用调试器调用哪个函数。下图显示了变量'text6 '中的base64编码数据，在解码之后，我们看到它是另一个PE文件。这个PE文件也是一个.NET可执行文件，最初称为Metall.dll。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610121659189.png "1669609676140840.png")

变量' text6 '中的Base64编码数据

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610122176178.png "1669609688201305.png")

' text6 '中的数据是另一个PE文件

在调试器中，我们还可以看到在这个新恢复的PE文件中调用了' OwbdG5aNVQQYu6X20i.o9pVsMvoTr75y5TrkE.V4j9c6YCwC() '函数。

**Metall.dll**

在开始分析这个二进制文件之后，我的第一反应如下图所示。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610123171484.png "1669609700809403.png")

metal .dll为游戏添加了另一层混淆

不用说，metal .dll通过向二进制文件添加控制流扁平化等特性，增加了混淆的程度。当我们谈到混淆器时，我们说他们的目标是减缓逆向进程。这在某种程度上是有效的。然而，在本例中，我们可以简单地采取一个快捷方式，让二进制文件运行并将其最终有效载荷加载到内存中。这样，我们可以将其转储到一个文件中，以便进一步分析。

**Warzone RAT**

最终由metal .dll加载到内存中的有效负载是Warzone远程访问木马(RAT)的一个版本。这是一个众所周知的恶意软件操作作为恶意软件服务(MaaS)。它在互联网上是公开的，任何人都可以通过订阅模式访问它。当前的定价如下图所示。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610124828828.png "1669609710762436.png")

Warzone RAT的当前定价

它为其订户提供以下功能：

```
Native, independent stub
Cookies Recovery
Remote Desktop
Hidden Remote Desktop - HRDP
Privilege Escalation - UAC Bypass
Remote WebCam
Password Recovery
File Manager
Download & Execute
Live Keylogger
Offline Keylogger
Remote Shell
Process Manager
Reverse Proxy
Automatic Tasks
Mass Execute
Smart Updater
HRDP WAN Direct Connection
Persistence
Windows Defender Bypass
```

WarzoneRAT通常也被称为“Ave\_Maria Stealer”，因为下图所示的字符串出现在二进制文件中。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610125709906.png "1669609721110290.png")

Ave\_Maria Stealer名称来自于二进制文件中的这个误导性字符串

嵌入到GitHub的链接没有提供任何有用的东西，这可能只是误导逆向的另一种方式。

Warzone根据Windows版本提供多种升级权限的方法。其中一个是在同一个二进制文件中实现的，另一个作为WM\_DSP资源添加到二进制文件中。如果需要，这将在运行时加载并执行。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610126123300.png "1669609731159516.png")

可以在资源中找到一个特权升级漏洞

为了躲避防病毒软件，Warzone试图将自己添加到Windows Defender的排除列表中，如下图所示。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610126214227.png "1669609742214221.png")

Warzone将自己添加到防病毒排除列表中

为了建立持久性，它还将自身复制到以下路径：

C:\Users\Admin\Documents\ Adobe5151.exe

Warzone还使用与其指挥控制服务器的加密通信。过去，加密的密码/密钥是字符串' warzone160\x00 '。在此示例中，它已更改为字符串“nevergonnagiveyouup”。所以，受害者在不知不觉的情况下被人用人力推倒。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610127180444.png "1669609752111970.png")

使用新密码进行加密

通过动态分析，C2服务器的地址为171.22.30.72:5151。在我们的内部系统中查找这个IP和端口号，如下图所示。从这张图中我们可以看到，这场特别的攻击活动早在2022年6月20日就开始了。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221128/1669610128110289.png "1669609762867204.png")

访问地址171.22.30.72:5151

可以看出，攻击者用一封写得很好的虚假政府邮件作为诱饵，执行所附的恶意软件。这种诱惑是经过深思熟虑的，因为它与匈牙利所有使用在线管理门户的人都相关。

嵌入式.NET二进制文件的russian yoshka doll具有越来越复杂的混淆功能，支持攻击者越来越依赖现代混淆技术的趋势。这将导致逆向工程师不得不投入更多的时间来清除和分析恶意软件。使用Warzone RAT作为最终有效载荷也支持了攻击者对MaaS服务日益增长的依赖。我们在勒索软件样本中看到了类似的趋势，勒索软件即服务提供商越来越受欢迎。

如上所述，该活动的最后一个有效载荷Warzone RAT是通过一系列混淆的.NET二进制文件部署的。每个阶段都从二进制文件中的某个位置加载下一个阶段，对其进行解码，将其加载到内存中，并调用一个函数将控制流传递给下一个阶段。这样的多阶段加载程序可能会使动态分析变得困难，因为每次重新启动恶意软件样本时，在不同的阶段进行导航都会很困难。为了避免这个问题，我们从各个阶段创建了独立的可执行文件，以实现更高效的调试。这就是我们将在下面讨论的。

下图显示了Warzone ...