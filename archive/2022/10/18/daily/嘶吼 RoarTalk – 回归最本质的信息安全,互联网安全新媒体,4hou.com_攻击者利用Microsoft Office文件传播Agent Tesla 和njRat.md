---
title: 攻击者利用Microsoft Office文件传播Agent Tesla 和njRat
url: https://www.4hou.com/posts/KEvz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-18
fetch_date: 2025-10-03T20:06:12.119351
---

# 攻击者利用Microsoft Office文件传播Agent Tesla 和njRat

攻击者利用Microsoft Office文件传播Agent Tesla 和njRat - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者利用Microsoft Office文件传播Agent Tesla 和njRat

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-10-17 11:44:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113042

收藏

导语：Agent Tesla和njRat多年来都是高度活跃的恶意软件。

研究人员最近发现了一些恶意的Microsoft Office文件，这些文件试图利用合法网站MediaFire和Blogger执行shell脚本，然后释放Agent Tesla和njRat的两个恶意变体。Agent Tesla是一款著名的监视软件，首次发现于2014年，它可以从web浏览器、邮件客户端和FTP服务器中窃取个人数据，收集屏幕截图和视频，并收集剪贴板数据。njRat（也称为Bladabindi）是2013年首次发现的远程代理木马，能够远程控制受害者的设备，记录击键、访问摄像头、窃取浏览器中存储的凭据、上传/下载文件、操作注册表等。

**·**受影响的平台：Microsoft Windows

**·**受影响方：Windows用户

**·**影响：控制和收集受害者设备中的敏感信息

**·** 严重级别：严重

在本文中，我们将详细介绍我们发现的文件、它们用于传播有效负载的嵌入脚本，以及这些恶意软件变体的行为。

**第1阶段**

在2022年9月，研究人员发现了两种文件。一个是PowerPoint加载项，另一个是包含诱饵图片和嵌入Excel表单的Word文件。这两个文件都包含类似的VBA脚本，在打开文件后立即执行宏。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214466134039.png "1665214466134039.png")

根据PPT插件中的VBA脚本（如上图所示），代码会自动触发，因为它使用了“Auto\_Open()”函数。其“ControlTipText”和“Tag”字段包含完整的命令 “mshta” 和MediaFire URL。我们可以在 “vbaProject.bin”中看到完整的URL。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214473101627.png "1665214473101627.png")

PPT加载项中的VBA宏

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214482239897.png "1665214482239897.png")

vbaProject.bin文件中完整的恶意URL

**第2阶段**

从下图所示的Process Explorer中可以看到，“mshta”进程在点击文件中的“Enable Macros”后立即启动。这导致了MediaFire网站，这是一个合法的文件和图片共享平台。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214490118920.png "1665214490118920.png")

点击“Enable Macros”后的Process Explorer

以下是第一阶段VBA宏中“1.htm”的内容：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214498256416.png "1665214498256416.png")

从MediaFire下载的“1.htm”

下图显示了将一些十六进制字符串转换为ascii字符串后的更清晰的图片。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214507117019.png "1665214507117019.png")

转换后的“1.htm”

这个HTML文件有三个主要任务：

1.从MediaFire网站传送第三阶段脚本文件；

2.终止任务WINWORD.EXE；

3.通过创建计划任务添加持久性。它使用“mshta”连接到“http[:]//www.webclientservices.co[.]uk/p/1[.]html”网站，该网站每73分钟包含一个类似的脚本。以下是2022年9月的博客截图：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214516158034.png "1665214516158034.png")

9月中旬www[.webclientservices[.co[.uk/p/1[.html]网页

研究人员还发现，“www[.]webclientservices[.]co[.]uk”中的1.html文件已更新并重命名为“real all BACK SEP 2022”。嵌入式JavaScript也被修改了，现在可以发布其他恶意软件。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214527163777.png "1665214527163777.png")

9月底发现的www[.]webclientservices[.]co[.]uk/p/1[.]html更新页面

**第3阶段**

 “1.txt”中的PowerShell脚本是从MediaFire下载的，它通过进程空心化技术提供最终有效负载。它首先终止所有相关进程，并对加载程序和有效负载进行解码。然后它调用最终有效载荷并部署它，绕过AMSI。主要恶意软件和部分代码被编码并替换为字符串，以增加分析的难度。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214536130974.png "1665214536130974.png")

用于加载代理特斯拉的PowerShell的全图

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214544195990.png "1665214544195990.png")

执行PowerShell后的Process Explorer

在“Load Agent Tesla Payload”过程的第二部分中，变量$CLE11和$RNBX1是更换一些字符串后的最终有效负载和加载器。基于.NET的不同版本，它自定义了继续进行进程空心化活动的路径：

$Path = 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\jsc.exe'

$Path2 = 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\caspol.exe'

$Path3 = 'C:\Windows\Microsoft.NET\Framework\v3.5\Msbuild.exe

 [Ref]/Assembly::Load((HexaToByte($RNBX1))).GetType('CALC'.PAYSIAS'.'GetMethod'(Execute).Invoke($null,[object[]] ($Path, HexaToByte($CLE11)));

研究人员将$RNBX1保存为可执行文件，并用dnSpy打开它。目标类和方法如下图所示。此.Net加载器利用一些模糊处理来隐藏主要API（CreateProcess、VirtualAllocEx…等）。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214565102727.png "1665214565102727.png")

Net Loader

研究人员找到了目标进程“jsc.ex”、“caspol.exe”和“Msbuild.exe”，它们在受害者的设备中安静运行。详细信息如下图所示。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214575184743.png "1665214575184743.png")

流程空心化时的Process Explorer

在PowerShell部分的末尾，它禁用了日志记录，并通过打补丁绕过AMSI。详细步骤如下所示。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214585137843.png "1665214585137843.png")

绕过PowerShell中的AMSI

**最后阶段（第一部分）**

第一个恶意软件负载是Agent Tesla。这种变体在9月中旬开始传播。它包括合法的文件信息，“NirSoft”公司的“Web浏览器密码查看器”，并使用FTP发送被盗数据。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665214595171001.png "1665214595171001.png")

Agent Tesla的基本信息

下图是用于传输提取数据的攻击者FTP服务器信息的屏幕截图，包括用户名和密码。此变体还将自身复制到%appdata%目录中，文件名为“NGCwje.exe”以进行持久化。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215529217934.png "1665215529217934.png")

攻击者的服务器信息

然后，它开始提取受害者设备的信息，例如基板的序列号、处理器ID和MAC地址。然后，它为该数据生成一个MD5哈希。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215540270341.png "1665215540270341.png")

为受害设备的信息生成Md5哈希

Agent Tesla使用一个典型的应用程序列表来窃取登录凭据、Cookie、邮件信息和VPN数据。这些项目的一部分如下图所示：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215551124693.png "1665215551124693.png")

目标浏览器应用程序列表

一旦恶意软件从受害者的设备检索到凭证和其他信息，它通过使用硬编码IP的FTP协议发送这些数据。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215560213545.png "1665215560213545.png")

使用FTP协议

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215571127046.png "1665215571127046.png")

从受害者设备捕获的流量

根据遇到的不同类型的文件，它使用四种打开字符串：“CO”表示cookie数据，“KL”表示键盘记录，“PW”表示受害者的密码信息，“SC”表示屏幕截图文件。恶意软件使用下划线将数据类型、用户名、设备名称和时间戳连接在一起，作为数据ZIP文件的文件名。被盗zip文件列表如下所示：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215583134368.png "1665215583134368.png")

FTP服务器上Zip文件的部分列表

**最后阶段（第二部分）**

第二个有效载荷是njRat，也称为Bladabindi。它是一个.NET特洛伊木马，用于控制和监控受害者的设备。此变体对其字符串生成和代码流使用模糊处理。从方法ko()的IDA图形概览中，你可以看到这个变体更复杂，但你仍然可以识别类似的函数。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215594189148.png "1665215594189148.png")

IDA图概述

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215604158310.png "1665215604158310.png")

njRat的入口点

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215616206875.png "1665215616206875.png")

字符串解码功能

首先，它在“Startup”和“Templates”文件夹中创建lnk和exe文件，文件名为“Windows”。这个名字用来欺骗用户和分析师，让他们认为它是合法的Windows文件。

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215627392878.png "1665215627392878.png")

创建持久性

然后，它以相反的顺序获取命令和控制服务器主机名和端口号。

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215637708843.png "1665215637708843.png")

命令和控制服务器信息

为了确保此恶意软件只在此受害者上运行一次，它添加了名为“di” 、数据为 “!”的“HKEY\_CURRENT\_USER”。

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221008/1665215650741080.png "1665215650741080.png")

添加到“HKEY\_CURRENT\_USER”中的...