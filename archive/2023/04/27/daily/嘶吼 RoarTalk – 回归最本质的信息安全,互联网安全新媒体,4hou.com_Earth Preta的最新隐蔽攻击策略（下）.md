---
title: Earth Preta的最新隐蔽攻击策略（下）
url: https://www.4hou.com/posts/VZg1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-27
fetch_date: 2025-10-04T11:32:01.100656
---

# Earth Preta的最新隐蔽攻击策略（下）

Earth Preta的最新隐蔽攻击策略（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Earth Preta的最新隐蔽攻击策略（下）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-04-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110718

收藏

导语：研究人员还观察到攻击者正在积极地改变研究人员的工具、战术和程序（TTP）以绕过安全解决方案。在这篇文章中，研究人员还将介绍和分析攻击者使用的其他工具和恶意软件。

**WinRAR和curl**

根据研究人员的一些监控日志，攻击者滥用安装的WinRAR二进制文件和上传的curl可执行文件来窃取文件(下图显示了执行的命令)。注意，可执行文件log.log是一个合法的curl二进制文件。所有泄露的数据都被收集并发送回攻击者控制的FTP(文件传输协议)服务器。

![35.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985909321421.png "1679985909321421.png")

使用WinRAR和curl泄露数据

在某些示例中，研究人员偶然发现了FTP服务器的帐户和密码。在检查FTP服务器后，研究人员了解到攻击者主要专注于敏感和机密文件，其中大部分都经过压缩并使用密码保护。根据观察，这些文件是通过对受害者的主机名和磁盘驱动器进行分类来组织的。

![36.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985923153107.png "1679985923153107.png")

有被盗文件的FTP服务器

**HackTool.Win32.NUPAKAGE**

除了众所周知的合法工具外，攻击者还制作了高度定制的用于泄露的工具。研究人员将这个恶意软件命名为“NUPAKAGE”，该名称源自其唯一的PDB字符串D:\Project\NEW\_PACKAGE\_FILE\Release \NEW\_PACKAGE\_FILE.PDB。

NUPAKAGE恶意软件需要一个唯一的密码才能执行，被窃取的数据被封装在自定义文件格式中。攻击者似乎在不断更新该工具，以提供更大的灵活性并降低检测的可能性，包括添加更多的命令行参数和混淆机制。默认情况下，它只收集文件，包括具有以下扩展名的文件：

doc

.docx

.xls

.xlsx

.ppt

.pptx

.pdf

它避免收集文件名以“$”或“~”开头的文件，因为这些类型的文件通常要么是系统生成的临时文件，要么是伪装成诱饵文件的PE文件。

此工具的用法如下：

![37.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985933219892.png "1679985933219892.png")

NUPAKAGE恶意软件的参数

每一个NUPAKAGE恶意软件都需要一个唯一的密码作为它继续执行的首个参数。如下图所示，它首先检查密码是否存在。否则，恶意软件执行过程将终止。在检测过程中，研究人员观察到每个恶意软件中都有不同的密码。

![38.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985943856196.png "1679985943856196.png")

NUPAKAGE中的密码检查例程

![39.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985952214376.png "1679985952214376.png")

NUPAKAGE中的密码

执行后，NUPAKAGE将释放xxx.zip和xxx.z两个文件。xxx.zip文件是一个日志文件，其虚假zip标头以0x0偏移量为前缀，占用了前0x100个字节。从偏移量0x100开始，在XOR操作中使用单个字节对日志记录字符串进行加密，如下图所示。

![40.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985964237327.png "1679985964237327.png")

原始日志文件（顶部），解密后的日志文件（底部）中显示纯文本

以其中一个执行结果为例，保存了被泄露数据的大部分信息，包括原始文件路径、原始文件大小和压缩文件大小。研究人员认为攻击者利用它来进一步追踪哪些文件被处理过。对于安全研究人员来说，这个日志文件还有助于揭示有多少数据被泄露，并提供有关影响范围的信息。

![41.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986329142713.png "1679986329142713.png")

扩展名为.z的文件是一个自定义文件格式的泄露数据blob。NUPAKAGE恶意软件首先随机生成一个密钥blob，密钥在自定义算法中加密。之后，它将加密的密钥blob存储到扩展名为.z的文件的前0x80字节中。从偏移量0x80开始，存在一个包含所有已过滤数据的长数组。

泄露文件中的大部分信息都会被保存，例如MD5哈希、文件名长度、压缩文件大小、原始文件大小、文件名和文件内容。为了分离文件blob，它在每个blob的末尾放置一个唯一的字节序列，55 55 55 55 AA AA AA AA FF FF FF 99 99 99 99。

![42.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986342169614.png "1679986342169614.png")

NUPAKAGE生成的扩展名为.z的文件中的自定义格式

![43.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986554161534.png "1679986554161534.png")

NUPAKAGE生成的扩展名为.z的文件中的自定义格式描述

值得一提的是，在NUPAKAGE的最新版本中，越来越多的混淆被用来阻止静态分析。

![44.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986567151813.png "1679986567151813.png")

NUPAKAGE最新版本的垃圾代码

**HackTool.Win32.ZPAKAGE**

ZPAKAGE是另一个用于封装文件的自定义恶意软件的示例；它的工作原理也与NUPAKAGE类似。它还需要一个密码来确保它按预期使用。在下图所示的示例中，密码是“start”。

![45.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986582118316.png "1679986582118316.png")

一个ZPAKAGE密码的示例

ZPAKAGE也支持命令行参数，但它拥有的函数比NUPAKAGE少。该工具的使用方法如下:

![46.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986594214426.png "1679986594214426.png")

ZPAKAGE支持的参数

ZPAKAGE也表现出与NUPAKAGE相似的行为。例如，它还避免使用名称以“$”或“~”开头的文件。此外，它还生成两个文件，一个扩展名为.z，另一个扩展名称为.zip。扩展名为.z的文件是已过滤的数据blob，扩展名为.zip的文件是日志文件。

在生成的扩展名为.z的文件中，被泄露的文件将通过zlib算法进行压缩，以最小化文件大小。它还定义了用于存储的布尔字段“type”，无论文件是否被压缩。如果压缩后的文件大小小于原文件，则类型为1。否则，类型将被设置为0，并将选择原始文件内容，而不是压缩文件内容。无论文件内容是否被压缩，它都将在异或操作中使用特定字符串qwerasdf对其进行加密。

![47.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986603708088.png "1679986603708088.png")

ZPAKAGE生成的扩展名为.z的文件中的自定义格式

![48.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986613977958.png "1679986613977958.png")

ZPAKAGE生成的扩展名为.z的文件中的自定义格式描述

**检测恶意攻击**

自2022年10月以来，攻击者已经更改了TTP，并开始使用受密码保护的文件。例如，研究人员在VirusTotal上发现了一个TONEINS示例(SHA256: 8b98e8669d1ba49b66c07199638ae6012adf7d5d93c1ca3bf31d6329506da58a)，该示例不能链接到“关系”选项卡中的任何其他文件。但是，研究人员发现在“行为”选项卡中打开了两个文件，文件名分别为~$Evidence information.docx和~$List of terrorist personnel at the border.docx，下一阶段的有效负载通常嵌入在虚假文件文件中。

![49.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986625169235.png "1679986625169235.png")

打开的TONEINS示例文件

下图显示了在VirusTotal上查询“边境恐怖分子人员名单”的搜索结果。第一个文件是研究人员在本节前面提到的TONEINS DLL示例，而第二个文件是一个正常的可执行文件，最初名为adobe\_licensing\_wf\_helper.exe，显然是上传到VirusTotal的，文件名为 List of terrorist personnel at the border.exe。

![50.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986636150462.png "1679986636150462.png")

在VirusTotal上搜索字符串边境恐怖分子名单的结果

![51.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986650409929.png "1679986650409929.png")

提交adobe\_licensing\_wf\_helper.exe

第三个文件是受密码保护的文件，它有完全相同的文件名List of terrorist personnel at the border[1].rar。但由于没有密码，研究人员无法解压它。但它在“Relations”选项卡中有一个有趣的父项执行，这是一个名为Letter Head.docx的文件。

![52.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986660212665.png "1679986660212665.png")

terrorist personnel at the border[1].rar的父项执行

在Letter Head.docx文件中，有一个谷歌驱动器链接和一个密码。内容本身与缅甸联邦共和国政府有关，并用缅甸语书写。

![53.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986671795576.png "1679986671795576.png")

Letter Head.docx

检查下载链接后，研究人员发现它与之前在VirusTotal上发现的受密码保护的文件相同。

![54.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986682171703.png "1679986682171703.png")

谷歌驱动器链接截图

新的攻击载体流与之前介绍的类似，受害者将收到一个包含谷歌驱动器链接和相应密码的诱饵文件，而不是嵌入在电子邮件中的文件下载链接，并与之交互。

至于为什么密码保护的文件有父项执行，通过在VirusTotal上检查Letter Head.docx的沙箱执行行为，研究人员发现VirusTotal沙箱会选择文件中嵌入的任何链接。这将导致打开带有文件下载提示的Internet Explorer窗口。

![55.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986692219151.png "1679986692219151.png")

VirusTotal上Letter Head.docx文件的沙盒截图

当显示下载提示时，甚至在用户选择“保存”按钮之前，Internet Explorer将在后台静默地下载该文件。

结果，该文件将被保存到名为“INetCache”的缓存文件夹中，之后会看到一个被释放的RAR文件：

C:\Users\user\AppData\Local\Microsoft\Windows\INetCache\IE\R0IAZP7Z\List%20of%20terrorist%20personnel%20at%20the%20border[1].rar.

由于RAR文件是由Internet Explorer自动下载的，因此Letter Head.docx将被视为它的执行父文件。

![56.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986932139620.png "1679986932139620.png")

在VirusTotal上被释放的Letter Head.docx文件

为了找到嵌入谷歌驱动器链接的其他受密码保护的文件，研究人员尝试使用以下查询：

![57.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679986943773513.png "1679986943773513.png")

该查询可以查找任何加密的RAR文...