---
title: 深入分析BundleBot新型恶意软件
url: https://buaq.net/go-173782.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:58:57.655153
---

# 深入分析BundleBot新型恶意软件

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

![](https://8aqnet.cdn.bcebos.com/56777e28979fc77fc964cffd7a44ddfb.jpg)

深入分析BundleBot新型恶意软件

Check Point Research (CPR)对被称为BundleBot的新型恶意软件进行了深入分析发现，BundleBot滥
*2023-8-6 12:0:0
Author: [www.4hou.com(查看原文)](/jump-173782.htm)
阅读量:26
收藏*

---

Check Point Research (CPR)对被称为BundleBot的新型恶意软件进行了深入分析发现，BundleBot滥用dotnet bundle（单文件），这是一种自包含的格式，可以很好绕过静态检测。它会伪装成常规实用程序，人工智能工具和游戏。通常通过Facebook广告和受攻击帐户传播。

**详细分析**

在过去的几个月里，BYOS公司一直在监控一个新的未知的窃取程序，研究人员称之为BundleBot，他们发现其传播并滥用dotnet bundle(单文件)，自包含格式。从.net core 3.0+到dotnet8+，这种形式的dotnet编译已经支持了大约四年，并且已经有一些已知的恶意软件家族滥用它，例如Ducktail。

使用这种特定dotnet格式的BundleBot主要是滥用Facebook广告和受攻击帐户，利用dotnet bundle(单文件)、自包含格式、多阶段攻击和自定义混淆。

dotnet bundle（单文件）、自包含的格式通常会导致整个dotnet运行时出现非常大的二进制文件。此外，分析和调试这样的文件可能会导致一些问题，特别是如果这样的文件受到一些混淆的影响。

本文主要深入分析BundleBot的攻击方式，重点对dotnet bundle（单文件）、自包含格式进行分析。

**发现过程**

自.NET Core 3.0（2019）发布以来，可以将.NET程序集部署为单个二进制文件。这些文件是不包含传统.NET元数据标头的可执行文件，并通过特定于平台的应用程序主机引导程序在底层操作系统上本地运行。

dotnet bundle（单文件），自包含格式是一种编译形式，可以生成一个不需要在操作系统上预装特定Dotnet运行时版本的可执行二进制文件。可执行文件实际上是一个本地托管二进制文件，在其覆盖中包含整个dotnet运行时、程序集和其他依赖项，因此它很大，约几十MB。本机托管二进制文件负责从覆盖中提取（在执行时）所有内容，加载dotnet运行时和程序集，准备所有内容，并将执行转移到.NET模块的入口点。

当涉及到从覆盖中提取程序集时（在执行时），我们可以根据用于编译特定应用程序的目标dotnet版本来处理不同的例程。dotnet版本之间的区别在于，在dotnet5+（.NET Core 3.0+）之前，默认情况下，所有程序集都被提取到磁盘（临时目录）并加载到进程内存中。

另一方面，在dotnet5+版本中，覆盖层中的所有程序集都被提取并直接加载到进程内存中（没有文件被释放在磁盘上，则只有本地库）。在dotnet5+中，可以在编译期间指定提取，但默认设置是直接被提取到内存中的。

尽管研究人员仍在处理与dotnet相关的应用程序，但上述对这种特定文件格式的描述清楚地表明，需要使用不同的工具集和技术来正确分析它。

研究人员检测到BundleBot滥用dotnet bundle(单文件)，将其作为攻击的最后阶段，它与已经被公布的几个恶意活动有关，很可能是由同一个组织发起的。

**攻击载体**

在发现的示例中，最初的攻击载体都是通过Facebook广告或被攻击的账户传播的，攻击程序伪装成常规程序、人工智能工具和游戏。例如，Google AI、PDF Reader、Canva、Chaturbate、Smart Miner、超级马里奥3D世界。由于BundleBot的功能之一是窃取Facebook账户信息，这些被盗的信息进一步用于通过新受攻击的账户传播恶意软件。

尽管如此，我们不能完全排除其他可能的传播方式，因为我们无法通过相关的跟踪信息获得所有检测到的样本源链接。

一旦受害者被诱骗从钓鱼网站下载假程序实用程序，第一阶段下载程序以“RAR”形式发送。这些下载阶段通常是在Dropbox或Google Drive等托管服务上。

下载的“RAR”文件包含一个独立的dotnet bundle(单文件)格式的第一阶段下载程序。在执行第一阶段后，第二阶段以密码保护的“ZIP”文件的形式下载，通常来自Google Drive等托管服务。第二阶段的密码在下载程序中进行硬编码，通常是以编码的形式。

被提取和执行的受密码保护的“ZIP”文件的主要部分是BundleBot，它是dotnet bundle(单文件)、自包含格式和自定义混淆的组合。

下面是一个与虚假的实用程序“Google AI”有关的详细攻击链示例，它伪装成使用Google AI Bard的营销工具：

1.来自受攻击账户的Facebook广告或Facebook帖子的钓鱼网站https://marketingaigg[.]com/。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691026956103047.png "1691026956103047.png")

受攻击账户的Facebook上的钓鱼网站

2.钓鱼网站https://marketingaigg[.]com/伪装成营销工具，使用Google Bard AI引导下载页面https://googlebardai[.]wiki/Googleai。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691026973869388.png "1691026973869388.png")

导致下载阶段的钓鱼网站

3.URL https://googlebardai[.]wiki/Googleai正在从Dropbox托管服务。

下载“RAR”文件Google\_AI.rar (SHA-256:

“dfa9f39ab29405475e3d110d9ac0cc21885760d07716595104db5e9e055c92a6”)；4.Google\_AI.rar包含GoogleAI.exe (SHA-256: " 5ac212ca8a5516e376e0af83788e2197690ba73c6b6bda3b646a22f0af94bf59 ")， dotnet bundle(单个文件)和自包含的应用程序；

5.GoogleAI.exe包含用作下载程序的GoogleAI.dll dotnet模块(从https://drive.google[.]com/uc?id=1-mC5c7o\_B1VuS6dbQeDAAqLuPbfAV58O&export=download&confirm=t, password=alex14206985alexjyjyjj下载受密码保护的“ZIP”文件adsnew - 1.0.0.0 . ZIP)；

6.解压后的ADSNEW-1.0.0.3.zip (SHA-256: " 303c6d0cea77ae6343dda76ceabaefdd03cc80bd6e041d2b931e7f6d59ca3ef6 ")包含RiotClientServices.exe, dotnet bundle (单文件)以及自包含应用程序。

7.RiotClientServices.exe作为最后阶段服务和执行，包含两个恶意dotnet模块RiotClientServices.dll，BundleBot,和libarysharing .dll ，他们是C2数据序列化程序。

**自包含Dotnet Bundle 的分析**

当我们需要分析一个自包含的dotnet bundle(单文件)二进制文件时，我们会遇到几个问题。

第一个问题是，我们需要以某种方式提取所有二进制文件，这些二进制文件是上述包bundle覆盖的一部分。这种提取将帮助我们静态地调查每个文件，就像我们在处理普通的dotnet程序集时所做的那样。尽管目前该做法还不太成熟，但是已经有一些解决方案能够充分分析dotnet bundle格式了，从而帮助我们进行提取。我们基于GUI的工具和库，以编程的方式实现这一点。值得注意的是，目前dnSpy/dnSpyEx不支持提取dotnet bundle文件。

可以帮助提取的最可靠的基于GUI的工具包括：

ILSpy：开源.NET程序集浏览器和反编译器；

dotPeek：免费的.NET反编译器和程序集浏览器；

ILSpy中dotnet bundle的提取：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027006617752.png "1691027006617752.png")

ILSpy中的dotnet bundle提取

dotPeek中dotnet bundle的提取：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027024486755.png "1691027024486755.png")

dotPeek中dotnet bundle的提取

如上所述，dotnet bundle文件的提取也可以通过编程的方式完成。当我们处理较大的文件集时，这种方法非常方便。

为此，最合适的解决方案是使用AsmResolver。AsmResolver是一个便携式可执行(PE)检查库，能够读取，修改和写入可执行文件，这包括.NET模块以及本机映像。该库仍然允许用户访问低级结构。更重要的是，AsmResolver理解bundle文件格式，因此我们可以使用它来自动提取。

下面是使用AsmResolver和PowerShell提取bundle文件内容的代码示例。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027065111874.png "1691027065111874.png")

现在，当我们成功地提取了dotnet bundle文件的全部内容时，就可以使用通常用来检查普通dotnet程序集的任何工具，比如dnSpyEx。这将允许我们静态地调查每个.net程序集。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027081202282.png "1691027081202282.png")

dnSpyEx中dotnet程序集的静态分析

由于dotnet程序集，特别是恶意程序集，通常非常复杂，并且经常受到一些混淆或保护的影响，大多数研究人员倾向于将静态和动态分析方法结合起来。关于动态方法，我们使用一个自包含的dotnet bundle(单文件)二进制调试来接近第二个问题。

在托管调试器(如dnSpyEx)中调试dotnet程序集是常用的一种方法。dnSpyEx中的调试不完全支持自包含的dotnet bundle二进制文件，如果试图调试此类文件，可能会导致如下所示的类似异常。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027097116812.png "1691027097116812.png")

调试自包含dotnet bundle时抛出的DnSpyEx异常

幸运的是，最近发布的dnSpyEx版本(v6.4.0)改进了对这类文件的调试，因此我们应该不会再遇到这种异常，调试可以顺利进行。

尽管我们可以在最新版本的dnSpyEx (v6.4.0)中调试自包含的dotnet bundle文件，但它无法解决作为dotnet bundle混淆的dotnet程序集的处理问题。

当dotnet二进制文件被编译为一个自包含的包时，这仅仅意味着整个依赖项(尤其是dotnet运行时)是生成的应用程序的一部分，并且这样的应用程序通过其配置文件被配置为使用它们。这些配置文件是在提取包和去混淆每个受保护程序集之后影响调试的主要问题。

为了解决这个问题，我们实际上可以将自包含的dotnet bundle文件转换为非自包含的、非单文件的.NET程序。通过这种方式转换的程序将被诱骗使用dotnet运行时，这是操作系统的一部分，所以我们必须确保安装了它。

转换步骤如下：

1.如上所示，提取dotnet bundle文件的内容；

2.查找要在操作系统中安装的dotnet运行时版本并进行安装。为了快速查找我们的.NET应用程序所依赖和需要安装的具体dotnet运行时的版本信息，我们可以定位并检查配置文件\*[appname].runtimeconfig.json\*和\*[appname].deps.json\*，它们应该在之前提取的内容中。

在下面的示例中，我们可以清楚地看到，需要安装 .NET Runtime 5.0.17, x86。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027114186096.png "1691027114186096.png")

配置文件

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027137114096.png "1691027137114096.png")

需要安装的dotnet运行时版本(Microsoft)

3.修改配置文件\*[appname].runtimeconfig.json\*和\*[appname].deps.json\*的内容。通过修改这些文件，我们将应用程序转换为非自包含的、非单文件的.NET程序，并强制它使用已安装的dotnet运行时版本。

修改\*[appname]. runtimeeconfig .json\*，将" includedFrameworks "字符串改为" frameworks "。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027160392630.png "1691027160392630.png")

修改“[appname].runtimeconfig.json”

通过删除来自“libraries”的“runtimepack”条目来修改\*[appname].deps.json\*。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027178336610.png "1691027178336610.png")

修改“[appname]. depth .json”

4.运行和调试。自包含的dotnet bundle应用程序可以依赖于本机库，这些库可能是bundle的一部分，所以我们已经从内容中提取了它们，或者它们可以与bundle可执行文件一起单独提供。通过检查配置文件或运行配置文件，我们可以快速发现应用程序是否有这样的依赖关系（在\*[appname].deps.json\*中定义），如下所示。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027195285858.png "1691027195285858.png")

运行提取的bundle应用程序时出现依赖关系相关错误要解决这个问题，只需将bundle应用程序旁边的所有依赖项复制到先前提取内容的位置。现在，调试应该像使用安装在操作系统中的dotnet运行时的普通.NET应用程序一样运行了。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691027215698326.png "1691027215698326.png")

在dnSpyEx中调试转换的非自包含、非单文件的.NET应用程序

如果我们不处理作为dotnet bundle一部分的混淆的dotnet程序集，则不需要像上面那样，因为使用最新版本的dnSpyEx (v6.4.0)可以直接调试它们。尽管如此，当我们处理混淆的程序集并倾向于以去混淆的形式调试它们时，仍然需要上面的操作方法。

如上所述，我们介绍了一种将自包含的dotnet bundle文件转换为普通的dotnet程序集的通用方法，这取决于目标操作系统上预安装的适当版本的dotnet运行时。这种方法应该适用于不同的操作系统平台（Windows、Linux、macOS）。

了解了如何提取自包含的dotnet bundle文件的内容以及如何对其进行调试后，我们就可以继续进行分析了。

**技术分析**

自带的dotnet bundle格式，可加强分析和静态检测；

受简单但有效的自定义模糊处理的影响；

滥用密码保护的文件来进行最后阶段的传播；

最后阶段是一个新的窃取程序BundleBot；

用于C2通信的自定义homebrew分组数据序列化。

**下载程序技术分析**

下载阶段的分析，请使用GoogleAI.exe示例SHA-256：“5ac212ca8a5516e376e0af83788e2197690ba...