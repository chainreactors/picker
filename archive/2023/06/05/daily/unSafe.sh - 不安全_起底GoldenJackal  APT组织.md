---
title: 起底GoldenJackal  APT组织
url: https://buaq.net/go-167124.html
source: unSafe.sh - 不安全
date: 2023-06-05
fetch_date: 2025-10-04T11:44:37.963762
---

# 起底GoldenJackal  APT组织

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

![](https://8aqnet.cdn.bcebos.com/7bdc7ce81c074544544043ba88b8130f.jpg)

起底GoldenJackal APT组织

GoldenJackal是一家APT组织，自2019年开始活跃，通常针对中东和南亚的政府和外交机构。尽管他们早在几年前就开始了活动，
*2023-6-4 11:10:0
Author: [www.4hou.com(查看原文)](/jump-167124.htm)
阅读量:38
收藏*

---

GoldenJackal是一家APT组织，自2019年开始活跃，通常针对中东和南亚的政府和外交机构。尽管他们早在几年前就开始了活动，但该组织似乎没有被详细介绍过。

卡巴斯基实验室的研究人员早在2020年中开始监测该组织，观察到这是一个极其专业的组织。该组织的主要开发.NET恶意软件、JackalControl、JackalWorm、JackalSteal、JackalPerInfo和JackalScreenWatcher等特定工具集，目的是：

**·**控制受害者计算机；

**·**在使用可移动驱动器的系统中传播；

**·**从受感染的系统中窃取某些文件；

**·**窃取凭据；

**·**收集有关本地系统的信息；

**·**收集有关用户网络活动的信息；

**·** 截取桌面的屏幕截图；

根据工具集和攻击者的行为，研究人员认为GoldenJackal APT组织的主要动机是间谍活动。

**攻击途径**

研究人员发现攻击者假冒Skype安装程序，使用恶意Word文档。

另一个已知的攻击途径是一个恶意文档，它使用远程模板注入技术下载恶意HTML页面，该页面利用了Follina漏洞。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675273111680.png "1685285199995044.png")

这份文件被命名为 “Gallery of Officers Who Have Received National And Foreign Awards.docx”的文件似乎是合法的，旨在收集巴基斯坦政府授予勋章的官员的信息。值得注意的是，Follina漏洞是在2022年5月29日首次被公布，该文档似乎在发布两天后的6月1日进行了修改，并于6月2日首次被检测到。

该文档被配置为从合法且已被攻击的网站加载外部对象：

hxxps://www.pak-developers[.]net/internal\_data/templates/template.html！

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675273837617.png "1685285467518449.png")

用于加载远程资源的代码段

远程网页是公共“概念证明”的修改版本，用于利用Follina漏洞。原始PoC可在[GitHub](https://github.com/thalysonsousa/follina/blob/main/teste.html)上获得。攻击者将IT\_BrowseForFile变量值替换为以下值：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675274139706.png "1685285482173779.png")

利用Follina漏洞的代码段

解码后的字符串为：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675274210563.png "1685285623204938.png")

**解码脚本**

该漏洞会下载并执行托管在合法受攻击网站上的可执行文件，并将其存储在以下路径中：“%Temp%\GoogleUpdateSetup.exe”。下载的文件是JackalControl恶意软件。

在其他情况下，研究人员没有发现真正的攻击途径，他们还观察到在横向活动进程中系统受到攻击。具体来说，研究人员观察到攻击者使用psexec实用程序启动恶意批处理脚本。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675274208922.png "1685285650378447.png")

批处理脚本执行各种操作，例如安装 Microsoft .Net Framework 4、用JackalControl木马感染系统并收集有关系统的信息。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675275159200.png "1685285706142781.png")

**JackalControl**

这是一种木马，允许攻击者通过一组预定义和支持的命令远程控制目标计算机。信息是通过HTTPS通信信道在恶意软件和C2服务器之间进行接收的，并且可以指示植入进行以下任何操作：

**·**使用提供的参数执行任意程序；

**·**下载任意文件到本地文件系统；

**·**从本地文件系统上传任意文件；

在过去几年中，攻击者多次更新该工具，已出现了多种变体。接下来，我们将描述2023年1月观察到的最新版本（8C1070F188AE87FBA1148A3D791F2523）。

该木马是一个可执行文件，可以作为标准程序或Windows服务启动。

它需要一个参数，该参数可以等于以下一个值：

**·**/0：作为标准程序运行，只与C2服务器联系一次；

**·**/1：作为标准程序运行，并定期联系C2服务器；

**·**/2：作为Windows服务运行；

恶意软件参数和相关的恶意软件行为根据变体而变化。一些变体只提供两个参数：

**·**/0作为标准程序运行；

**·**/1作为Windows服务运行；

其他变体可以自我安装不同的持久性机制。恶意软件的执行流程由运行该恶意软件的命令行中提供的参数决定。

**·**/h0：将通过创建Windows计划任务使恶意软件获得持久性；

**·**/h1：将通过创建相应的注册表运行项使恶意软件获得持久性；

**·**/h2：将通过创建Windows服务使恶意软件获得持久性；

**·**/r0：作为标准进程运行（此参数由Windows计划任务指定）；

**·**/r1：作为标准进程运行（此参数由生成的注册表运行项值指定）。

**·**/r2：作为服务运行（此参数由创建的Windows服务指定）。

攻击者已经将不同的变体进行了传播：有些包括用于维护持久性的代码，另一些则被配置为在不感染系统的情况下运行；并且感染进程通常由诸如上述批处理脚本之类的其他组件执行。

恶意软件通过生成BOT\_ID开始其活动，这是用于识别受攻击系统的唯一值。此值源自其他几个基于主机的值：

从以下WMI查询中获得的UUID值：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675275761557.png "1685285785419298.png")

从以下注册表项获取的计算机GUID:

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675275126690.png "1685285800497228.png")

从另一个WMI查询中获得的额外驱动器的列表，这反过来允许他们确定' PHYSICALDRIVE0 '的' SerialNumber '：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675275123527.png "1685285826212545.png")

收集到的信息被连接在一个字节数组中，然后用MD5哈希，MD5被用作创建BOT\_ID的种子。用于生成后者的算法只是对结果MD5哈希中每两个连续字节求和，并将所得字节（模数256）作为最终BOT\_ID的单个字节。下面的代码片段描述了这种逻辑，它取自恶意软件。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675275314674.png "1685285852120865.png")

用于生成BOT\_ID的代码段

生成的BOT\_ID还用于初始化DES密钥和IV，然后用于加密与C2的通信。

恶意软件使用HTTP POST请求进行通信，其中数据参数将以编码形式作为请求主体的一部分进行传播。然后，整个请求结构将显示如下：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675276103986.png "1685285957207415.png")

一个有效的响应应该以以下方式形成：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675276189818.png "1685286062158215.png")

响应使用base64进行解码：生成的有效负载是一个字符串数组，其中使用的分隔符是标准的Windows新行序列-“\r\n”。每一行都用base64再次解码，用DES解密，并用GZIP算法解压缩。

每个命令都具有以下结构：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675276153474.png "1685286081112121.png")

命令结构

00：执行——使用指定的参数执行任意程序。如果攻击者将NoWait标志设置为False，则恶意软件会重定向进程输出，读取数据并将其转发给C2；

01：下载——从本地系统读取文件并将其上传到服务器；

02：上传——使用攻击者指定的文件路径将接收到的数据保存到本地系统。

命令数据字段旨在携带有关命令参数的信息，并且对于每种操作类型具有不同的结构，如下所述：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675276180606.png "1685286099509415.png")

命令结果通常被组成一条消息，该消息还包括底层命令类型和命令ID的值，该值唯一地标识向恶意软件发出的命令的示例。这三个值用GZIP压缩，用DES加密，并用base64编码。

生成的有效负载使用“|”字符与BOT\_ID连接，再次使用base64编码，然后使用上述POST请求格式将其上传到远程服务器。

**安装程序模式**

一些变体可以感染系统，在特定位置创建恶意软件的副本，并保证其持久性。

恶意软件位置是通过特定进程选择的，它枚举CommonApplicationData中的所有子目录，并随机选择一个子目录保存其副本。生成的文件名将以子目录的名称作为后缀，并附加另一个静态值Launcher.exe，如下所示：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675277202737.png "1685286123151460.png")

如果操作成功，它还会更改新的文件时间戳，并使其与所选子目录的时间戳相同。

如果操作失败，它会随机选择另一个目录，并再次尝试复制恶意软件。

如果对所有子目录的操作都失败，它将尝试使用硬编码目录名列表：

**·**Google

**·**Viber

**·**AdGuard

**·**WinZip

**·**WinRAR

**·**Adobe

**·**CyberLink

**·**Intel

如果所有尝试都失败了，它将尝试在以下位置使用相同的进程：

**·**ApplicationData

**·**LocalApplicationData

**·**Temp

**持久性能力**

恶意软件的持久性通常通过以下机制来保证：

**·**服务安装；

**·**创建新的Windows注册表项值；

**·**创建新的计划任务；

该服务通常由恶意软件在执行Windows sc.exe实用程序时安装。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675277148978.png "1685286146975497.png")

注册表值等于复制的恶意软件文件名，不带扩展名，并存储在以下各项中：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675277158949.png "1685286163149004.png")

计划任务是使用硬编码的XML模板创建的，该模板在运行时被修改，并使用相同的恶意软件文件路径在文件系统释放，但扩展名不同，为.XML而不是.exe。

然后将生成的XML文件与Windows schtasks.exe实用程序一起使用来创建任务。

例如：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675277650974.png "1685286180973048.png")

任务和服务描述会根据变体而变化。

**JackalSteal**

JackalSteal是另一种植入程序，通常部署在一些受感染的计算机上，用于在目标系统中查找感兴趣的文件，并将其窃取至C2服务器。

此工具可用于监控目标系统中的可移动USB驱动器、远程共享和所有逻辑驱动器。恶意软件可以作为标准流程或服务来工作。它无法维护持久性，因此必须由另一个组件安装。

JackalSteal通过解析参数开始执行。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675277124361.png "1685286198148347.png")

选项说明

**·**-n：配置文件的唯一标识符值；

**·**-p：要检查的目录路径；

**·**-s：请求文件的最大大小；

**·**-d：自上次写入请求文件以来的天数；

**·**-m：使用正则表达式在配置的目录中查找以逗号分隔的字符串掩码列表；

**·**-w：配置Profile的连续目录扫描之间的时间间隔（以秒为单位）；

**·**-e：从扫描活动中排除路径；

**·**/0：作为标准进程运行；

**·**/1：作为服务运行；

这些选项允许攻击者指定“概要文件”，该文件定义了攻击者感兴趣的文件。该配置文件由一个ID和一个模式列表组成。每个模式都包含一个具有以下属性的选项列表：

**·**Path：目标路径；

**·**Credentials：用于访问远程共享的凭据用户和密码；

**·**Masks：包含通配符和掩码字符的掩码字符串，可用于使用正则表达式匹配任何一组文件；

**·**MaxSize：文件的最大大小；

**·**Days：自上次写入文件以来的天数；

**·**Interval：两次连续路径扫描之间的时间间隔

**·**Exclude：扫描活动期间必须排除的路径；

用于配置JackalSteal组件的命令如下：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685675278196494.png "1685286221186062.png")

唯一标识符“-n”通常与JackalControl木马程序生成的BOT\_ID相同。

在参数处理之后，恶意软件将数据序列化为XML，使用由带有“-n”选项传递的ID生成的密钥用DES加密它们，并将生成的有效负载存储在以下位置：“%ApplicationData%\SNMP\cache\%Filename]”，其中%Filename%是由攻击者指定的唯一标识符的MD5生成的GUID。

恶意软件通常使用“/0”或“/1”选项和“-n”选项执行，该选项用于加载获得的配置文件ID。在第二种情况下，它从前面提到的位置加载配置文件，并启动 ‘Watchers’。

Watcher是在具有相同名称的类中定义的对象，该对象在不同的线程中运行，并根据指定的选项扫描位置。该模式可以表示：

**·**本地文件系统中的简单路径；

**·**远程共享上的路径；

**·**常量字符串all；

**·**常量字符串usb。

当模式等于“all”时，恶意软件会枚举所有逻辑驱动器，并为每个驱动器创建一个新的Watcher对象。当模式为“usb”时，它会侦听与在系统上创建新的可移动驱动器的操作相对应的系统事件。当检测到新的驱动器时，它会创建一个新的Watcher对象。

每次添加新的Watcher时，恶意软件都会通知日志该事件，并使...