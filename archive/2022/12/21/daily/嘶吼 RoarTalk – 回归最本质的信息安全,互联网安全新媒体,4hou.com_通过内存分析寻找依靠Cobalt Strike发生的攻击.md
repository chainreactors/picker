---
title: 通过内存分析寻找依靠Cobalt Strike发生的攻击
url: https://www.4hou.com/posts/4KZJ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-21
fetch_date: 2025-10-04T02:04:00.439529
---

# 通过内存分析寻找依靠Cobalt Strike发生的攻击

通过内存分析寻找依靠Cobalt Strike发生的攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 通过内存分析寻找依靠Cobalt Strike发生的攻击

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115384

收藏

导语：本文介绍了三种新的加载程序，并展示了如何使用各种技术检测它们，这些检测技术在新的基于管理程序的沙盒中可用。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301223159566.png "1670301223159566.png")

Unit 42研究人员检查了几个包含Cobalt Strike组件的恶意软件样本，并发现通过分析进程中关键执行工件可以捕获这些样本。

 cobalt strike(简称CS)是一款团队作战渗透测试神器,分为客户端及服务端，一个服务端可以对应多个客户端，一个客户端可以连接多个服务端。它不仅在红队中流行，而且也被用于恶意目的。

尽管该工具包只出售给受信任的组织进行安全测试，但由于源代码泄露，它的各种组件不可避免地进入了攻击者的武器库，从勒索软件组织到国家支持的攻击组织。滥用Cobalt Strike的恶意软件甚至在2020年臭名昭著的SolarWinds供应链攻击事件发挥了作用。

**为什么是Cobalt Strike？**

Cobalt Strike之所以被如此广泛的利用，主要是因为Cobalt Strike集成了端口转发、扫描多模式端口Listener、Windows exe程序生成、Windows dll动态链接库生成、java程序生成、office宏代码生成，包括站点复制获取浏览器的相关信息等。由于它的设计是从底层开始的，所以攻击者会定期使用它引入新的规避技术。

Cobalt Strike的主要优点之一是，一旦初始加载程序被执行，它主要在内存中运行。当有效负载是静态防护的、仅存在于内存中并且拒绝执行时，这种情况会给检测带来问题。这对许多安全软件产品来说都是一个挑战，因为扫描内存绝非易事。

在许多情况下，Cobalt Strike是在目标网络中获得初始足迹的自然选择。攻击者可以使用具有大量部署和混淆选项的构建器，根据可定制的模板创建最终有效负载。

该有效负载通常以加密或编码的形式嵌入到文件加载程序中。当受害者执行文件加载程序时，它将有效负载解密/解码到内存中并运行它。由于有效负载以其原始形式存在于内存中，因此由于某些特定功能，可以很容易地检测到它。

作为恶意软件研究人员，我们经常看到潜在的有趣的恶意样本，结果只是Cobalt Strike的加载程序。通常也不清楚加载程序是由红队创建的还是真正的攻击者创建的，因此使归因更具挑战性。

接下来我们将深入研究三种不同的Cobalt Strike加载程序，它们是由我们设计的一个新的基于管理程序的沙箱检测到的，该沙箱允许我们分析内存中的工件。每个示例加载不同的植入类型，即SMB、HTTPS和stager信标。我们将这些Cobalt Strike装载程序称为KoboldLoader, MagnetLoader和LithiumLoader。我们还将讨论可以用来检测这些有效负载的一些方法。

**KoboldLoader SMB信标**

以以下样本为例

SHA256: 7ccf0bbd0350e7dbe91706279d1a7704fe72dcec74257d4dc35852fcc65ba292

这个64位KoboldLoader可执行文件使用各种已知的技巧来绕过沙盒，并使分析过程更加耗时。

为了绕过只挂钩高级用户模式函数的沙盒，它只调用内置API函数。为了使分析人员的工作更加困难，它通过哈希而不是使用纯文本字符串来动态解析函数。恶意软件包含调用以下函数的代码：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301234502169.png "1670301234502169.png")

该恶意软件创建了两个单独的函数哈希/地址对表。一个表包含所有内置函数的一对，而第二个表只包含Nt\*个函数对。

对于所使用的Rtl\*函数，它循环遍历第一个表并搜索函数哈希以获得函数地址。对于使用的Nt\*函数，它遍历第二个表并同时增加一个计数器变量。

当找到哈希时，它将获取计数器值，即相应内置函数的系统调用号，并输入自定义系统调用存根。这有效地绕过了许多沙盒，即使挂接了较低级别的内置函数而不是高级函数。

加载程序的整体功能相对简单，并使用映射注入来运行负载。它生成Windows工具sethc.exe的子进程，创建一个新部分，并将解密的Cobalt Strike信标加载程序映射到其中。Cobalt Strike加载程序的最终执行是通过调用RtlCreateUserThread来加载SMB信标的。

**内存中的规避功能**

通过新的基于管理程序的沙盒，我们能够在内存中检测到解密的Cobalt Strike SMB信标。这个信标加载程序甚至使用了一些内存中的规避功能，创建了一种奇怪的嵌合体文件。虽然它实际上是一个DLL，但“MZ”神奇的PE字节和随后的DOS标头被一个小的加载程序shellcode覆盖，如下图所示。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301243182914.png "1670301243182914.png")

解密的Cobalt Strike SMB信标shellcode

shellcode加载程序跳转到导出的函数DllCanUnloadNow，该函数在内存中准备SMB信标模块。为此，它首先加载Windows pla.dll库，并清空代码段(.text)中的一大块字节。然后，它将信标文件写入该blob并修复导入地址表，从而创建一个可执行内存模块。

在分析该文件的过程中，我们可以找出所使用的一些内存内规避功能，如下表所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301251147087.png "1670301251147087.png")

内存内规避功能

总之，信标加载程序和信标本身是同一个文件。PE标头的部分用于跳转到导出函数的shellcode，该函数反过来在Windows DLL中创建自己的模块。最后，shellcode跳转到信标模块的入口点，在内存中执行它。

如上所述，我们没有办法成功检测我们的KoboldLoader示例的信标，除非我们可以在执行过程中查看内存内部。

**MagnetLoader**

我们将研究的第二个加载程序是一个模仿合法库的64位DLL。

SHA256:6c328aa7e903702358de31a388026652e82920109e7d34bb25acdc88f07a5e0

这个MagnetLoader示例试图在一些方面看起来像Windows文件mscms.dll，通过使用以下类似的功能：

相同的文件描述；

一个具有许多相同函数名的导出表；

几乎相同的资源；

一个非常相似的互斥锁；

这些功能也显示在下图中，其中恶意软件文件与有效的mscml.dll进行了对比。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301260735439.png "1670301260735439.png")

MagnetLoader(左)和mscml.dll(右)的文件描述、导出表和资源的比较

MagnetLoader不仅尝试静态地模拟合法的Windows库，而且在运行时也如此。

MagnetLoader的所有导出函数内部调用相同的主要恶意软件例程。当调用其中一个时，首先运行DLL入口点。在入口点，恶意软件加载原始的mscms.dll，并解析它所伪造的所有函数。

这些原始函数的地址在执行伪方法后被存储和调用。因此，每当调用MagnetLoader的导出函数时，它都会运行主恶意软件例程，然后调用mscms.dll中的原始函数。

主要的恶意软件例程相对简单。它首先创建了一个名为SM0:220:304:WilStaging\_02\_p1h的互斥体，看起来与mscms.dll创建的原始互斥体非常相似。

Cobalt Strike信标加载程序被解密到内存缓冲区中，并在一个已知的技巧的帮助下执行。加载程序没有直接调用信标加载程序，而是使用Windows API函数EnumChildWindows来运行它。

该函数包含三个参数，其中一个是回调函数。恶意软件可能滥用此参数，通过回调函数间接调用地址，从而隐藏执行流程。

**LithiumLoader**

最后一个Cobalt Strike示例是DLL侧加载链的一部分，其中使用了一种安全软件的自定义安装程序。DLL侧加载是一种劫持合法应用程序以运行独立的恶意DLL的技术。

SHA256: 8129 bd45466c2676b248c08bb0efcd9ccc8b684abf3435e290fcf4739c0a439f

这个32位的LithiumLoader DLL是由攻击者自定义创建的Fortinet VPN安装包的一部分，该安装包以FortiClientVPN\_windows.exe (SHA256: a1239c93d43d657056e60f6694a73d9ae0fb304cb6c1b47ee2b38376ec21c786)的形式提交给VirusTotal。

FortiClientVPN\_windows.exe文件不是恶意的或被破坏的。由于该文件是签名的，攻击者利用它来逃避反病毒检测。

安装程序是一个自解压缩RAR存档，包含以下文件：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301268197346.png "1670301268197346.png")

FortiClientVPN\_windows.exe文件内容

自解压脚本命令如下：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301277121018.png "1670301277121018.png")

自解压脚本命令列表

当安装程序运行时，所有文件都会被无声地放到本地%AppData%文件夹中，两个可执行文件都会启动。当FortiClient VPN安装程序执行时，WinGup工具侧加载libcurl.dll LithiumLoader恶意软件。恶意软件之所以这样做，是因为它从libcurl库的合法副本中导入了以下函数，如下图所示：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301286969872.png "1670301286969872.png")

导入WinGup.exe的地址表

此威胁还试图通过PowerShell将%AppData%文件夹路径添加到Windows防御器中的排除列表中。

在启动GUP.exe时，恶意的libcurl.dll文件被加载到进程空间中，因为它静态地导入上图所示的函数。虽然所有四个libcurl函数都在运行，但只有curl\_easy\_cleanup包含在编译库的新版本时注入的恶意例程。因此，我们不是在处理合法DLL的打了补丁的版本。这是一种更干净的解决方案，不会像在其他恶意软件中经常看到的那样，在插入恶意程序后破坏代码。

这个curl\_easy\_cleanup函数通常只包含一个子例程(Curl\_close)，并且没有返回值(如其在GitHub上的源代码所示)。修改后的函数如下图所示。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301294102551.png "1670301294102551.png")

修改了libcurl.dll的curl\_easy\_cleanup导出函数

load\_shellcode函数通过XOR和密钥0xA解密shellcode，如下图所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301303179885.png "1670301303179885.png")

Shellcode加载程序函数load\_shellcode()

这个函数通过EnumSystemGeoID间接运行Cobalt Strike阶段shellcode，而不是直接跳转到它。这个Windows API函数有三个参数，最后一个参数是一个被LithiumLoader滥用的回调函数。

Cobalt Strike stager shellcode是从Metasploit借来的，是反向的HTTP外壳负载，它使用以下API函数：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301312155239.png "1670301312155239.png")

shellcode连接到以下URL，其中包含泰国一所大学的IP地址

**LithiumLoader检测问题**

在本文发布时，Cobalt Strike信标的有效负载已不再可用。如果API调用的执行报告中没有有效负载或任何可操作的信息，沙盒通常很难确定样本是否恶意。这个示例本身没有任何可以被归类为恶意的功能。

**通过内存分析寻找Cobalt Strike**

在这三个例子中都存在一些常见的检测挑战。这些示例不能在正常的沙盒环境中执行。但是正如我们所讨论的，如果我们在执行期间查看内存内部，就可以使用大量的信息进行检测，比如函数指针、已解码的加载程序阶段和其他工件。

为了准确地检测，研究人员发现解决高度规避恶意软件的一个关键功能是，除了使用系统API更好地理解所发生的事情外，还需要在执行样本时查看内存。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221206/1670301322127780.png "1670301322127780.png")

研究人员发现，在恶意软件检测中，查看执行关键点的内存增量，以提取有意义的信息和工件是很有用的。当我们的系统处理大量的样本时，要实现大规模的工作有很多挑战。接下来，我们将详细介绍目前从内存中收集的一些主要类型的数据，以帮助检测。尽管我们在本文介绍的是通过内存方法，但我们绝不是说检测和记录API调用对检测没有用。

**自动有效负载提取**

如上所述，恶意软件开发者混淆其有效负载越来越普遍。虽然使用可执行打包器可以压缩和模糊文件来实现这一点并不新鲜，但当它与逃避策略结合使用时就会出现问题，因为没有对准确检测有用的静态或动...