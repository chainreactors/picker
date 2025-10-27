---
title: 出于经济利益，Void Rabisu使用RomCom后门在地缘冲突中获利
url: https://www.4hou.com/posts/5wlA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-19
fetch_date: 2025-10-04T11:45:06.052720
---

# 出于经济利益，Void Rabisu使用RomCom后门在地缘冲突中获利

出于经济利益，Void Rabisu使用RomCom后门在地缘冲突中获利 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 出于经济利益，Void Rabisu使用RomCom后门在地缘冲突中获利

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-06-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)130507

收藏

导语：由经济利益驱动，恶意组织在地缘冲突区域发起APT攻击的趋势越来越明显。

由经济利益驱动，恶意组织在地缘冲突区域发起APT攻击的趋势越来越明显。

Void Rabisu，也被称为Tropical Scorpius，研究人员认为它使用RomCom后门发起攻击。分析发现，Void Rabisu的攻击是出于经济动机。自2022年10月以来，Void Rabisu的动机似乎发生了变化，当时RomCom后门被报道出现在俄乌冲突中。

研究发现，至少自2022年10月以来，RomCom后门一直出现在地缘政治区域，接下来，研究人员将讨论RomCom是如何随着时间的推移而演变的，以及后门是如何通过类似APT的方法传播的，以及目前正在发生的著名网络犯罪活动所使用的方法，以表明RomCom正在使用更多的逃避技术。

RomCom使用的第三方服务也被其他攻击者使用，如恶意软件签名和二进制加密。RomCom已经通过许多诱饵网站传播。Void Rabisu是出于经济动机的，他们的目标和动机在特殊的地缘政治环境下看起来更像是出于政治目的。

**RomCom活动**

自2022年夏天以来，研究人员一直在跟踪RomCom的活动，自那以后，它的逃避方法有所升级，恶意软件不仅经常使用VMProtect来增加手动和自动沙盒分析的难度，而且还在有效负载文件上使用二进制填充技术。这为文件添加了大量的覆盖字节，增加了恶意负载的大小（研究人员看到一个文件的大小为1.7G）。此外，最近添加了一个新的例程，该例程涉及有效负载文件的加密，只有在下载特定密钥以激活有效负载的情况下，才能对有效负载文件进行解密。

除了这些逃避技术外，RomCom还使用诱饵网站进行传播，这些网站通常看起来是合法的，并被用于目标定位。这使得通过网络信誉系统自动屏蔽这些诱惑网站变得更加困难。Void Rabisu一直在使用谷歌广告诱导他们的目标访问诱饵网站，类似于2022年12月传播IcedID僵尸网络的活动。一个关键的区别是，虽然IcedID的目标范围更广，但Void Rabisu可能选择了谷歌广告向其广告商提供的更有针对性的目标。

RomCom的活动还利用了具有高度针对性的鱼叉式网络钓鱼电子邮件。

在RomCom诱饵网站上，目标被提供合法应用程序的木马版本，如聊天应用程序(如AstraChat和Signal)、PDF阅读器、远程桌面应用程序、密码管理器和其他通常由系统管理员使用的工具。

![1.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869895347346.png "1686869895347346.png")

![1.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869903441656.png "1686869903441656.png")

![1.3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869916863956.png "1686869916863956.png")

![1.4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869928124347.png "1686869928124347.png")

![1.5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869939142285.png "1686869939142285.png")

![1.6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869954135362.png "1686869954135362.png")

研究人员统计了自2022年7月以来建立的几十个诱饵网站。例如，RomCom在2022年3月对一名欧洲议会议员使用了鱼叉式网络钓鱼，但在2022年10月通过谷歌广告定位了一家欧洲国防公司，该广告导致一个中介登陆网站重定向到RomCom诱饵网站。该中介登陆网站使用了域名“kagomadb[.]com”，该域名后来于2022年12月用于Qakbot和Gozi有效负载。

追踪发现，RomCom后门的目标是乌克兰及其盟友。

**RomCom 3.0：AstraChat活动**

接下来，我们将分析2023年2月针对东欧目标使用的RomCom后门样本。Palo Alto的Unit 42分析了以前的RomCom版本，使用模块化架构，支持多达20种不同的命令。从那时起，恶意软件在支持的命令数量方面发生了显著变化，但其模块化架构几乎没有改变。RomCom 3.0背后的攻击者还使用不同的技术来释放和执行恶意软件。该分析基于一项将RomCom 3.0嵌入AstraChat即时消息软件安装包的活动。

**Dropper**

astrachat.msi 文件是一个Microsoft安装程序（msi）文档。尽管安装了与合法的AstraChat软件相关的文件，但它还是打开了一个恶意的InstallA.dll文件，并调用其Main()函数。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686869975941617.png "1686869975941617.png")

InstallA.dll文件提取%PUBLIC%\Libraries文件夹下的三个动态链接库（DLL）文件：

prxyms

winipfile

netid

这些DLL文件中的数字是基于从HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid的Windows注册表中读取的计算机GUID的整数。

**持久性**

为了持久性，RomCom使用COM劫持，因此得名。InstallA.dll在Windows注册表中写入以下注册表值：

[HKEY\_CURRENT\_USER\SOFTWARE\Classes\CLSID\{C90250F3-4D7D-4991-9B69-A5C5BC1C2AE6}\InProcServer32]

@="%PUBLIC%\\Libraries\\prxyms

这会覆盖HKEY\_LOCAL\_MACHINE hive中的相同项，导致请求该类ID（CLSID）的进程加载位于%PUBLIC%\Libraries\prxyms.DLL的RomCom加载程序DLL。其中一个进程是explorer.exe，它由RomCom dropper重新启动，因此调用加载程序DLL。

RomCom加载程序还通过使用转发的导出将对其导出函数的调用重定向到合法的actxprxy.dll。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686870031690046.png "1686870031690046.png")

RomCom 3.0加载程序(prxyms

但是，在调用被转发之前，RomCom加载程序的DLL入口点上的恶意代码会运行。这段代码使用 rundll32.exe来执行从winipfile

**基础架构**

RomCom 3.0分为三个组件：一个加载器，一个与命令和控制(C&C)服务器交互的网络组件，以及一个在受害者计算机上执行操作的工作组件。网络组件由netid

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686870129197207.png "1686870129197207.png")

RomCom 3.0总体架构

**Bot命令**

RomCom 3.0命令是恶意网络组件对HTTP POST请求的响应。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230616/1686870155119511.png "1686870155119511.png")

RomCom 3.0命令结构

上图显示了接收到命令5的示例，该命令是将文件下载到受害者的计算机上的命令。用于通信的ID是0x950，并且接收到带有附加数据的命令0x05。在这种情况下，附加数据告诉受感染计算机上运行的恶意软件，下载的文件应占用939 (0x3ac – 1) 4KB 块。文件本身是在单独的响应中下载的，因此在这种情况下，受害者端的最终文件大小将为3,846,144字节。作为一种逃避技术，将空字节附加到文件中以实现此结果，附加数据字段的内容可能因命令而异。

在RomCom 3.0中，研究人员列举了42个有效命令，以下是用于常规后门的大量命令，但是其中一些命令只是其他命令的变体。

1—发送连接的驱动器信息；

2—发送指定目录下的文件名列表；

3—启动cmd.exe以运行现有程序；

4—将指定的文件上载到C&C服务器；

5—将文件下载到受害者的计算机上；

6—删除受害者计算机上的指定文件；

7—删除受害者计算机上的指定目录；

8—生成一个带有PID欺骗的给定进程(PID也作为命令数据的一部分)；

12—从%PUBLIC%\Libraries\PhotoDirector.dll中调用startWorker()，然后将%PUBLIC%\Libraries\PhotoDirector.zip发送到C&C服务器并将其删除；

13—从%PUBLIC%\Libraries\PhotoDirector.dll中调用startWorker()，将屏幕信息写入%PUBLIC%\Libraries\update.conf；

14—将%PUBLIC%\Libraries\PhotoDirector.zip上传到C&C服务器并将其删除；

15—发送正在运行的进程及其PID的列表；

16—发送已安装软件列表；

17—删除worker组件(winipfile

18—下载文件并将其保存到%PUBLIC%\Libraries\PhotoDirector.dll；

19—下载一个文件，保存到“%PUBLIC%\Libraries\BrowserData\procsys.dll”中，调用其导出的stub()函数；

20—下载一个可能包含3proxy和plink的ZIP文件；

21—使用3proxy和plink，通过SSH协议建立代理，接收IP地址、密码、本地和远程端口作为命令参数，SSH服务器用户名固定为“john”；

22—终止3proxy.exe和plink.exe进程；

23—下载一个文件并将其保存到%PUBLIC%\Libraries\upd-fil

24—发送%PUBLIC%\Libraries\BrowserData\Result的内容；

25—复制工作线程；

26—发送Windows版本；

29—从C&C服务器下载freeSSHd；

30—运行freeSSHd并使用plink创建51.195.49.215的反向连接，用户名为“john”，密码为“eK6czNHWCT569L1xK9ZH”

31—关闭freeSSHd进程；

32—在%USERPROFILE%中的“下载”、“文档”和“桌面”文件夹中发送.txt、.rtf、.xls、.xlsx、.ods、.cmd、.pdf、.vbs、.ps1、.one、.kdb、/kdb、.doc、.doc，.odt、.eml、.msg和.email文件；

34—在受害者计算机的隐藏窗口运行AnyDesk，将AnyDesk ID发送给C&C服务器；

35—终止AnyDesk进程，并删除其可执行文件；

36—下载AnyDesk可执行文件并将其保存到%PUBLIC%\Libraries\dsk.exe；

38—下载文件并将其保存到%PUBLIC%\Libraries\wallet.exe；

39—下载文件并将其保存到%PUBLIC%\Libraries\7z.dll；

40—下载文件并将其保存到%PUBLIC%\Libraries\7z.exe；

41—发送用7-Zip压缩的%PUBLIC%\Libraries\tempFolder的内容；

42—下载文件并将其保存到%PUBLIC%\Libraries\7za.exe；

43—使用%PUBLIC%\Libraries\7za.exe将给定文件夹压缩为fold.zip文档，并将压缩后的文档发送到C&C服务器；

44—终止PhotoDirector.dll进程；

45—下载文件并将其保存到%PUBLIC%\Libraries\msg.dll；

46—调用%PUBLIC%\Libraries\msg.dll导出的stW()函数；

47—下载文件并将其保存到%PUBLIC%\Libraries\FileInfo.dll；

48—调用%PUBLIC%\Libraries\FileInfo.dll导出的fSt()函数；

49—更新网络组件；

**其他恶意软件**

根据发送回C&C服务器的消息以及命令如何使用这些文件，研究人员可以推断出几个附加组件的用途：

PhotoDirector.dll—用于获取一个或多个屏幕截图，并将它们压缩到%PUBLIC%\Libraries\PhotoDirector.zip中的程序；

procsys.dll—一个被称为STEALDEAL的窃取程序，用于检索浏览器cookie并将其写入%PUBLIC%\Libraries\BrowserData\Result；

wallet.exe—一个加密钱包抓取器，将被盗信息写入%PUBLIC%\Libraries\tempFolder；

msg.dll—用于窃取聊天信息的即时消息抓取器；

FileInfo.dll—FTP凭据的窃取器，或使受害者的计算机将文件上传到FTP服务器的组件；

除了这些额外的恶意软件，RomCom 3.0似乎也有下载和运行合法软件的命令：

dsk.exe–AnyDesk软件的便携式版本；

7z.dll、7z.exe和7za.exe–与7-Zip程序相关的文件；

**STEALDEAL**

通过RomCom的C&C服务器下载的窃取程序是一个相对简单的程序，它可以从以下浏览器中窃取存储的凭据和浏览历史：

```
Google Chrome
Microsoft Edge
Mozilla Firefox
Chromium
Chrome Beta
Yandex Browser
```

窃取器还收集了有关已安装邮件客户端的信息。被盗数据本地存储在受害者计算机上的%PUBLIC%\Libraries\BrowserData\Result，通过C&C命令24，这些数据通过RomCo...