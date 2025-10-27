---
title: DeathStalker使用Janicab新变种发起攻击
url: https://buaq.net/go-140450.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:18.502608
---

# DeathStalker使用Janicab新变种发起攻击

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

![](https://8aqnet.cdn.bcebos.com/9bac1f1bd3a6656c6438d761e878d1c4.jpg)

DeathStalker使用Janicab新变种发起攻击

Janicab于2013年作为能够在macOS和Windows操作系统上运行的恶意软件首次出现。Windows版本将基于VBscri
*2022-12-18 11:33:0
Author: [www.4hou.com(查看原文)](/jump-140450.htm)
阅读量:19
收藏*

---

![Janicab_malware_law_SL-featured-1200x600.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914804130518.png "1670914804130518.png")

Janicab于2013年作为能够在macOS和Windows操作系统上运行的恶意软件首次出现。Windows版本将基于VBscript的植入作为最后阶段，而不是之前在Powersing示例中观察到的C#/PowerShell组合。到目前为止，我们确定的基于VBS的植入程序样本具有一家族版本号，这意味着它仍在开发中。总的来说，Janicob显示了与其对应的恶意软件家族相同的功能，但不像EVILNUM和Powersing攻击那样在攻击生命周期的后期下载多个工具，分析的样本将大部分工具嵌入并混淆在滴管中。

有趣的是，攻击者继续使用YouTube、Google+和WordPress web服务作为DDR。然而，观察到的一些YouTube链接未列出，可以追溯到2015年，这表明可能会重复使用基础设施。

**初始攻击点**

在ZIP文件中使用基于LNK的滴管的初始感染方法与以前使用EVILNUM、Powersing和PowerPepper的活动类似，但每个活动似乎都侧重于不同的钓鱼主题，好像每个恶意软件家族都由不同的团队操作或针对不同类型的受害者。在Janicab的一个例子中，诱饵是一个工业企业概况，与先前PowerPepper攻击中使用的诱饵主题相匹配。根据我们的分析，传送机制仍然是鱼叉式网络钓鱼。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914816889549.png "1670914816889549.png")

LNK文件中的诱饵文件

LNK滴管的元数据类似于我们报道或公开分析的许多Powersing和Janicab植入程序。也就是说，SID、字体家族、字体大小、屏幕缓冲区和窗口大小、运行窗口和MAC地址是相似的。

尽管Janicab和Powersing在执行流程以及VBE和VBS的使用方面非常相似，但它们的LNK结构有些不同。此外，较新的Janicab变体在结构上与2015年的旧Janicab Windows变体相比发生了显著变化。新的Janica变体还嵌入了一个CAB文件，其中包含一些Python文件和其他在攻击生命周期后期使用的工件。以下是Powersing与新旧Janicab车型之间的高级比较。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914858977826.png "1670914858977826.png")

LNK文件结构比较

**执行流程**

一旦受害者被诱骗打开恶意LNK文件，链接中的恶意软件文件就会被释放。LNK文件有一个嵌入的“命令行参数”字段，用于提取和执行编码的VBScript加载器（1.VBE）。后者将释放并执行另一个嵌入和编码的VBScript（2.VBE），该VBScript将提取包含额外资源和Python库/工具的CAB文件（CAB.CAB），并通过提取最后一个阶段（基于VBScript的植入程序，称为Janicab）来结束感染。最后阶段将通过在Startup目录中部署一个新的LNK文件来启动持久性，并开始与DDR web服务通信，以收集实际的C2 IP地址。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914879176610.png "1670914879176610.png")

Janicab是一种基于VBS的恶意软件植入程序，其功能与对应的恶意软件家族Powersing和EVILNUM基本相似。所有这些都具有基本功能，如命令执行、导入注册表文件，以及下载其他工具的能力，同时保持高反VM和防御规避的持久性。

由于这三个恶意软件家族都有很强的相似性，所以在本节中我们只讨论Janicab版本之间的有趣差异。

Janicab可以被认为是一种模块化的、解释语言的恶意软件。这意味着攻击者能够添加/删除功能或嵌入文件；解释语言恶意软件以相当低的工作量提供了这种灵活性。例如，在旧版本中，SnapIT.exe(一种已知的用于捕捉屏幕截图的工具)每隔一段时间就会嵌入、删除和执行。该工具在后来的版本中被其他定制的工具所取代，这些工具可以完成相同的工作。我们还在较老的版本中看到了音频录制功能，但在后来的版本中没有。

在较新的变体中，我们开始看到攻击者嵌入了一个基于DLL的键盘记录器或屏幕捕获实用程序，该实用程序使用“run\_DLL\_or\_py”函数调用。有趣的是，根据卡巴斯基威胁归因引擎（KTAE）分析，该键盘记录器与我们之前报告的Powersing攻击中使用的另一个键盘记录器非常相似，其名称为“AdobeUpdater.dll”。在Powersing攻击中，DLL在攻击周期的后期从辅助C2服务器获取。然而，在Janicab攻击中，它大多被嵌入为HEX字节数组，或作为额外资源嵌入CAB文件中。我们知道有八个不同的Janicab版本：1.0.8、1.1.2、1.1.4、1.2.5、1.2.7、1.2.8、1.2.9a、1.3.2。

**Janicab恶意软件演变**

对不同Janicab版本的进一步比较表明，在整个恶意软件开发周期中添加了附加功能，同时保留了特定功能。下表显示了一些有趣的新功能，这些功能是根据参与者的要求或为了逃避安全控制而在几个变体的开发过程中引入的：

**函数名称简介**

1.函数checkRunningProcess（）——检查指示恶意软件分析或进程调试的进程列表；

2.函数delFFcookies（），函数delGCcookies（），函数delIEcookies（）——指向相应的浏览器位置并删除其cookie；

3.函数downFile（args）——用于从C2下载文件并将其保存到磁盘；

4.函数GetKl（kl）——获取键盘记录器数据，base64对其进行编码，然后将其发送到C2；

5.函数runCmd（cmd，cmdType）——使用cmd .exe或PowerShell.exe执行命令的函数；

6.函数run\_dll\_or\_py（arg1，arg2）——用于在使用两个参数时执行Python或dll文件；arg1是DLL路径，arg2是DLL导出的函数名（MyDllEntryPoint）；

7.函数add\_to\_startup\_manager(server, installedAV)，函数add\_to\_startup\_reg\_import（startupFile，starterFile），函数add\_to\_startup\_shortcut（startupFile，starterFile）——用于在C2上首次注册受害者；执行持久化操作并在系统启动文件夹和注册表HKEY\_CURRENT\_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon中安装Microsoft Sync Services.lnk；

8.函数isMalwb（）——用于检查是否安装了MalwareBytes。在检查其他AV产品的其他变体中也看到了类似的函数；

9.函数HandleCCleaner（）——通过检查系统注册表检查是否安装了CCleaner，并相应地删除注册表项；

10.函数RunIeScript（）——使用CScript.exe运行 ie.vbe脚本，以确保C2通信使用IE隐藏浏览器后不存在剩余的Internet Explorer实例；

11.函数getAV（）——获取已安装的AV产品列表；

从1.0.8版本开始，Janicab VBS植入程序以字节数组的形式嵌入了几个文件。这些文件通常是注册表、VBE、PE EXE或DLL文件。在最近的示例中，虽然我们仍然可以看到此类资源的嵌入式字节数组，但大部分额外资源都放在CAB文件文件中，该文件在第一阶段的进程中被释放。

以下是值得注意的释放文件及其说明：

K.dll——以其创建的目录命名为Stormwind，这是一个基于dll的键盘记录器，它枚举系统区域设置、时区信息，并设置全局挂钩以捕获击键。它将带有时间戳的击键写入\AppData\Roaming\Stormwind目录下名为log.log的日志文件中。它监视键盘记录器kill switch命令的\AppData\Local\Temp\ReplaceData\下的killKL.txt。

PythonProxy.py——一个支持IPv4/IPv6的基于Python的代理，能够在本地目标系统和远程C2服务器之间中继web流量。支持HTTP方法CONNECT、OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE。

Ftp.py——本地Ftp基于Python的服务器，服务于具有creds test:test端口2121。使用Junction.exe（一个sysinternals工具）创建除软盘驱动器之外的所有现有驱动器的目录别名。添加regkey以接受EULA，因为它是一个系统内部工具，如果是首次运行，则需要EULA。然后将“连接”的本地目录提供给FTP服务器。

Runner.py——一个Python脚本，使用四个参数：远程SSH服务器、远程SSH端口、远程绑定端口和“ftp”或“代理”作为应用程序选项。

根据为应用程序选项接收的参数，它将运行ftp.py(如果参数为ftp)或pythonproxy.py(如果参数为proxy)。

在这两个选项中，脚本将启动一个SSH反向隧道，连接到由攻击者控制的远程服务器，并将该隧道用作socks代理，或作为一种方法来浏览先前使用本地FTP服务器初始化的本地驱动器。

如果在%temp%\ReplaceData\中找到killrunner.txt文件，runner.py将退出。

Junction.exe——是一个[sysinternals工具](https://docs.microsoft.com/en-us/sysinternals/downloads/junction)，它创建NTFS连接点（别名）；创建“\\Drives”目录，并将其映射到使用FTP.py创建的本地FTP服务器并提供其内容。

Plink.exe——已知的基于Windows的CLI SSH客户端，用于透视和隧道，由Runner.py引用以进行反向隧道/文件复制。

**基础设施**

Deathstalker的一个显著特点是它使用DDR/web服务来托管一个编码字符串，该字符串随后被恶意软件植入程序解密。我们一直认为YouTube被用作DDR，尽管恶意软件设置中存在其他网络服务链接，但未被使用，例如2019年4月停用的Google+链接。

我们最近注意到的一个有趣的方面是使用了2021攻击中使用的未列出的旧YouTube链接。从历史上看，分析师可以使用搜索引擎和YouTube搜索功能来查找各自web服务中使用的模式。然而，由于攻击者使用未列出的YouTube旧链接，在YouTube上找到相关链接的可能性几乎为零。这也有效地允许攻击者重用C2基础设施。

有趣的是，旧的和新的Janicab变体仍然使用相同的web服务功能声明——YouTubeLinks，并在将十进制数转换为后端C2 IP地址的过程中继续使用常数除法。最近使用的除法是1337和5362。

至于实际的C2 IP地址，我们发现两个IP地址（87.120.254[.]100、87.120.37[.]68）与PowerPepper攻击中使用的C2（例如PowerPepper C2 87.120.37[.]192）位于同一ASN中。C2通信使用的协议是带有GET/POST方法的HTTP，后端C2软件是PHP。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914958155540.png "1670914958155540.png")

Janicab 2021 DDR清单

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914977699426.png "1670914977699426.png")

Janicab 2015 DDR列表

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670914989188623.png "1670914989188623.png")

最近攻击中使用的未列出YouTube DDR示例

在评估其中一个C2服务器时，我们发现攻击者正在托管并调用来自受害设备的ICMP shell可执行文件。名为icmpxa.exe的ICMP shell工具基于一个旧的Github项目。攻击者编译了icmpsh-s.c (MD5 5F1A9913AEC43A61F0B3AD7B529B397E)，同时更改了其中的一些内容。这个可执行文件（哈希和文件名）的独特性，使我们能够透视和收集攻击者使用的其他以前未知的C2服务器。有趣的是，我们还发现以前在PowerPepper攻击中使用了相同的ICMPshell可执行文件，这表明两个恶意软件家族之间存在潜在的基础设施重叠。

由于Janicab是一个基于VBS的恶意软件，C2命令可以很容易地从嵌入的函数中派生出来。该恶意软件利用VBS函数通过HTTPGET/POST请求连接到C2服务器，并连接到特定的PHP页面。每个PHP页面都提供某些功能。自从Janicab的早期版本以来，PHP页面的文件名基本保持不变，并表示后端/预期功能。然而，从1.1.x版本开始，攻击者开始缩短PHP页面的文件名，而不改变预期的功能。下表总结了PHP页面、它们的旧命名及其潜在用途：

**PHP页面及其原有名称的介绍**

Status2.php（原名Status.php）——检查服务器状态；

a.php（Alive.php）——从受害者接收信标数据；

/gid.php?action=add（GenerateID.php?action=add）——如果这是一个新的受害者，则生成一个用户ID并在C2后端注册系统配置文件信息；将受害者添加到数据库；

rit.php（ReportIT.php）——在评估设备是否有任何反分析检查后，记录用户设备是否与IT人员相关。在旧的Janicab版本中，消息也以(“it guy”)的形式发送。

受影响的对象属于传统的Deathstalker目标范围；主要是法律和金融投资管理（FSI）机构。然而，我们还记录了一个潜在的新受影响行业——旅行社。中东地区和欧洲也是 Deathstalker的重灾区。

**归因**

本报告中讨论的攻击与Deathstalker攻击组织有关。归因基于新Janicab变体的使用、独特的TTP、受害者学和攻击者运营商使用的基础设施。Janicab和Powersing的比较攻击分析突出了几个阶段的相似之处。

1.与之前的Deathstalker攻击中使用的LNK滴管相同的SID和元数据；

2.Janicob和Powersing之间使用启动文件夹中的LNK的类似持久机制；

3.Janicab具有类似的感染执行流程，并使用解释语言工具集，如VBS、VBE和Python；

4.Janicab macOS和Windows版本的Python文件命名类似于EVILNUM恶意软件（例如runner.py、serial.txt等）；

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670915064700180.png "1670915064700180.png")

EVILNUM runner.py用于文件传输

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670915077176960.png "1670915077176960.png")

Janicab 2021 runner.py文件传输片段

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221213/1670915092458063.png "1670915092458063.png")

MacOS runner.py的旧Janicab，用于启动具有文件传输功能的后台服务

基于Python的工具集和库的使用在使用Janicab、Powersing、EVILNUM和PowerPepper的所有Deathstalker攻击中是常见的；

YouTube以及其他网络服务/DDR的使用在Janicob和Powersing攻击中很常见；在Janicab、Powers...