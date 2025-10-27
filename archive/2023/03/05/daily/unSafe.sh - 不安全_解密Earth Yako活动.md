---
title: 解密Earth Yako活动
url: https://buaq.net/go-151938.html
source: unSafe.sh - 不安全
date: 2023-03-05
fetch_date: 2025-10-04T08:43:16.103783
---

# 解密Earth Yako活动

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

![](https://8aqnet.cdn.bcebos.com/8c92e95867f72cc4435b2de1cb739ffa.jpg)

解密Earth Yako活动

导语：2021年，趋势科技的研究人员观察到日本发生了几起针对学术组织和智库研究人员的攻击事件。此后，他们一直在追踪这一系列攻击，并将攻击命名为“Earth Yako”，研究人员将其归因于已知的活动“O
*2023-3-4 12:0:0
Author: [www.4hou.com(查看原文)](/jump-151938.htm)
阅读量:29
收藏*

---

导语：2021年，趋势科技的研究人员观察到日本发生了几起针对学术组织和智库研究人员的攻击事件。此后，他们一直在追踪这一系列攻击，并将攻击命名为“Earth Yako”，研究人员将其归因于已知的活动“Operation RestyLink”或“Enelink”。

2021年，趋势科技的研究人员观察到日本发生了几起针对学术组织和智库研究人员的攻击事件。此后，他们一直在追踪这一系列攻击，并将攻击命名为“Earth Yako”，研究人员将其归因于已知的活动“Operation RestyLink”或“Enelink”。

在调查了几起事件后，研究人员发现了之前未知的恶意软件、战术、技术和程序（TTP）以及Earth Yako用于网络间谍活动的基础设施。攻击者在短时间内引入了新的工具和恶意软件，频繁地改变和扩大其攻击目标。由于研究人员在2023年1月就观察到了相关的攻击，他们认为Earth Yako仍然活跃，并将很快继续针对更多组织。

**活动介绍**

自2022年1月以来，研究人员一直在观察Earth Yako，因为它瞄准了日本学术界和研究智库的研究人员。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423161204587.png "1677423161204587.png")

Earth Yako活动时间线

尽管攻击者一直以研究人员为目标，但随着时间的推移，Earth Yako的部署和目标确定的兴趣领域也有所不同。2022年早些时候，他们的主要目标是与经济安全相关的人员，但后来扩大到能源或经济行业等其他部门。

在本次活动中，Earth Yako使用鱼叉钓鱼链接进行初始访问。钓鱼邮件中的URL下载包含恶意快捷方式文件（.lnk）的压缩（.zip）或光盘映像（.iso）文件，以下载另一个有效负载。研究人员观察到了几封伪装成私人或公开会议等事件邀请的钓鱼邮件，这导致在目标系统中下载恶意软件。

**恶意软件和工具**

以下是研究人员从不同事件中观察到的新恶意软件和工具的摘要：

MirrorKey：内存动态链接库(DLL)加载程序；

TransBox：一个滥用Dropbox API的后门；

PlugBox：基于Dropbox API的后门，具有多种功能；

Dulload：通用加载程序名称；

PULink：一个用c++ /CLR编写的ShellBox的滴管，能够实现持久性；

ShellBox：另一个用C # 编写的基于Dropbox API的stager。

**示例分析**

研究人员观察到Earth Yako使用鱼叉钓鱼作为攻击起点，电子邮件正文中的URL引导目标在点击时下载.zip或.iso文件。压缩文件中包含的.lnk文件诱使目标下载恶意Word模板。在打开URL后，该例程通过Cobalt Strike感染目标，并侧加载一个.dll文件。接下来，我们将介绍2022年Earth Yako部署新恶意软件时研究人员观察到的一些示例。

**示例1**

第一个示例于2022年3月观察到，目标是日本学术机构的研究人员。攻击目标系统后，攻击者在以下流程中部署了MirrorKey和TransBox。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423179362592.png "1677423179362592.png")

事件1中MirrorKey和TransBox的执行流程

**MirrorKey**

研究人员在受感染的系统中发现文件名为OCLEAN.DLL的MirrorKey。此DLL由OFFCLN.EXE加载，这是一个合法的Microsoft应用程序，但用于DLL侧加载，以便在执行时将OCLEAN.DLL加载到同一目录中。加载后，MirrorKey在同一目录中查找DWINTL.DLL，这是一个由Microsoft签名的DLL，其代码部分中没有恶意代码，因此看起来无害。但是，数字签名被滥用以嵌入针对漏洞MS13-098或CVE-2013-3900的加密有效负载。CVE-2013-3900是一个在Authenticode签名验证过程中无法正确验证可执行文件（PE）摘要的漏洞，攻击者可以滥用该漏洞在合法数字签名的末尾嵌入任意数据。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423199119291.png "1677423199119291.png")

Microsoft发布的DWINTL.DLL的合法数字签名

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423214212196.png "1677423214212196.png")

滥用CVE-2013-3900的嵌入式数据

在本例中，嵌入了两种类型的数据：加密有效负载和解密数据。MirrorKey处理嵌入在文件末尾的数据，以生成有效负载的解密密钥。一旦成功生成，密钥将用于使用AES128-ECB解密嵌入的有效负载。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423230883838.png "1677423230883838.png")

用于有效负载解密的密钥生成逻辑

**TransBox**

解密的有效负载是一个内部名为FILETRANDLL.DLL的DLL。此DLL由MirrorKey动态加载到内存中，并在调用导出函数Start\_时开始其恶意活动。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423246969751.png "1677423246969751.png")

DLL中嵌入的原始文件名

研究人员的分析显示，这个DLL是一个使用Dropbox API的后门，主要用于文件和数据窃取。过去没有发现过类似的恶意软件。

**攻击起始点**

在执行时，TransBox为受感染的用户生成一个唯一的ID（受害者ID），这是由以下四个元素的乘积计算的：

被感染终端域名的CRC32；

用户名的CRC32；

主机名的CRC32；

卷序列号的前4个字节(DWORD)。

接下来，收集来自受感染机器的系统信息，例如驱动器相关信息、主机名、操作系统（OS）版本和IP地址。然后使用zlib压缩系统信息，并使用1字节XOR密码进行编码，然后上传到攻击者的Dropbox帐户。上传时，在将信息上传到URL hxxps://content[.]dropboxapi[.]com/2/files/upload时指定了Dropbox /

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423264288243.png "1677423264288243.png")

签入时的HTTP请求

**上传文件**

TransBox可以通过特定目录下的特定扩展名将文件上传到Dropbox。目标目录和文件扩展名如下：

**目标目录**

所有驱动器（A驱动器和CD-ROM除外）；

```
%USERPROFILE%\Desktop；%USERPROFILE%\Documents；
```

目标扩展：

```
7z.doc.docx.jsd.jst.jtd.odt.pdf.ppt.pptx.rar.rtf.xls.xlsx.zip
```

但以下目录被排除在外，这可能是为了提高示例的效率。考虑到TransBox的目的是扫描“有趣”的文档，该示例可能被设计为忽略以下这些文件夹：

```
C:\Program FilesC:\Program Files (x86)C:\PerfLogsC:\WindowsD:\Program FilesD:\Program Files (x86)E:\Program FilesE:\Program Files (x86)%APPDATA%
```

TransBox实现了另一个功能，以.ini格式文件记录文件修改日期，以便在更新目标文件时再次上传该文件。.ini文件是在文件路径中创建的，其中包含的信息格式为%LOCALAPPDATA%\sxda

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423282167381.png "1677423282167381.png")

用作数据库的.ini文件

**接收命令**

TransBox还可以通过Dropbox API接收后门命令。为了接收命令，在向URL hxxps://content.dropboxapi[.]com/2/files/download发送GET请求时指定Dropbox /

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423298553578.png "1677423298553578.png")

命令和控制（C&C）服务器的响应格式

TransBox可以根据攻击者的后门命令执行以下功能：

更改文件上载大小限制和块大小；

下载DLL并在内存中执行；

上传与浏览器(如Chrome或Firefox)凭据相关的文件；

添加扩展以收集；

上传指定文件或在指定目录下上传指定扩展名的文件；

显示指定目录下的文件和目录列表。

**示例2**

该示例发生在2022年6月左右，同样是针对日本一家学术机构的研究人员。在该示例中，研究人员观察到使用了上一个示例研究中介绍的MirrorKey变体，以及同样滥用Dropbox API的PlugBox恶意软件。与前面的示例研究一样，攻击者攻击目标系统并安装了这些恶意软件。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423314106033.png "1677423314106033.png")

示例2中MirrorKey和PlugBox的执行流程

**MirrorKey（使用微型加密算法的变体）**

在本例中观察到的MirrorKey变体是在文件名为GTN.dll的受感染系统中发现的。此dll的加载方式与前一例中使用的dll侧加载过程类似。这一次，存在于同一目录中的合法谷歌应用程序GoogleToolbarNotifier.exe被滥用。与先前的MirrorKey变体类似，它搜索同一目录中存在的espui.dll，这会滥用CVE-2013-3900来嵌入加密的有效负载。然而，该变体使用微型加密算法（TEA）而不是AES来解密有效负载。此外，代码与三月观察到的MirrorKey变体完全不同。虽然它最初可以被认为是一个不同的加载程序，但它与第一个观察到的变体部分共享通用TTP和代码。

**PlugBox**

解密的负载是一个内部名为LoadPlgFromRemote.DLL的DLL。此DLL由MirrorKey动态加载到内存中，并在调用导出函数Run时开始执行。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423328188246.png "1677423328188246.png")

嵌入DLL中的原始名称

分析表明，这个DLL和TransBox一样，是基于Dropbox API的后门。

**安装**

在执行时，它通过复制以下文件开始安装过程：

```
%windir%\SysWOW64\cttune.exe -> %localappdata%\NVIDIA\cctune.exe；\GTN.dll -> %localappdata%\NVIDIA\DWrite.dll；\espui.dll -> %localappdata%\NVIDIA\espui.dll；
```

此外，它将合法的DLL复制到当前工作目录并加载DLL。这个过程对于恶意活动来说毫无意义，并使PlugBox看起来无害。复制的合法DLL如下：

```
%windir%\SysWOW64\migration\TableTextServiceMig.dll；%windir%\SysWOW64\migration\msctfmig.dll；%windir%\SysWOW64\migration\WMIMigrationPlugin.dll；%windir%\SysWOW64\migration\imjpmig.dll；%windir%\SysWOW64\migration\imkmig.dll；%windir%\SysWOW64\migration\tssysprep.dll；%windir%\SysWOW64\migration\cosetup.dll；
```

**攻击起始点**

接下来，攻击者使用硬编码的API密钥登录Dropbox帐户。虽然TransBox嵌入了访问令牌，但PlugBox没有。相反，它嵌入了Refresh和Auth令牌，并使用这些值获取访问令牌，这是访问Dropbox over API所必需的。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423346368796.png "1677423346368796.png")

使用Refresh和Auth令牌获取访问令牌

然后，它会为每个受感染的用户生成一个受害者ID，以便在用户数据上传到Dropbox时按照以下步骤识别他们:

获取%temp%的文件路径，并将“\”替换为“+”；

获取受感染设备的ProcessorId；

获取受感染设备主板的序列号；

用“\r\n”连接上面的字符串并计算SHA256哈希值；

提取SHA256哈希值的前32个字节作为受害者ID；

然后，它向URL hxxps://content[.]dropboxapi[.]com/2/files/upload 发送一个HTTP POST请求，并将特定的详细信息details /

然后PlugBox将用户信息以纯文本形式上传：

%temp%的文件路径(将“\”替换为“+”)；

受感染设备的ProcessorId；

受感染设备主板的序列号；

**接收命令**

为了接收后门命令，PlugBox发送一个HTTP GET请求到hxxps://content.dropboxapi[.]com/2/files/download ，并将 /

PlugBox支持的功能如下：

更改接收命令的间隔；

下载加密的DLL，用TEA解密它们，并在内存中执行；

执行任意命令；

**示例3**

该示例发生在2022年6月和7月左右，同样是针对日本一家学术机构的研究人员。在这种情况下，滴管PULink和研究人员称为ShellBox的新恶意软件被使用。在研究人员的调查过程中，研究人员发现了一个包含目标用户名称的ISO文件，这表明攻击者可能试图通过让他们下载电子邮件中的ISO文件来入侵系统。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423364950609.png "1677423364950609.png")

.iso中的文件列表

ISO文件包含一个带有双扩展名的EXE文件、三个DLL（MSVCR100.DLL无害）和一个诱饵文档。EXE文件是一个合法的Word应用程序，但被自定义为在同一目录中加载wwlib.DLL的DLL。一旦执行，EXE文件就会启动恶意示例。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423381179071.png "1677423381179071.png")

事件3中PULink和ShellBox的执行流程

**Dulload (Loader)**

加载的第一个DLL文件是wwlib.DLL，这是一个用C++/CLR编写的简单加载程序，旨在加载同一目录中存在的Wordcnv.DLL，并调用导出的方法MS\_word.release\_file。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230226/1677423405247713.png "1677423405247713.png")

调用“Wordcnv.dll”的导出方法

**PULink（Loader）**

Wordcnv.dll中的导出方法旨在安装有效负载和组件（之后详细介绍）。在这种方法中，PULink使用AES1...