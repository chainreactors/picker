---
title: Earth Preta的最新隐蔽攻击策略（上）
url: https://www.4hou.com/posts/PJXn
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-26
fetch_date: 2025-10-04T11:32:59.924435
---

# Earth Preta的最新隐蔽攻击策略（上）

Earth Preta的最新隐蔽攻击策略（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Earth Preta的最新隐蔽攻击策略（上）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-04-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105973

收藏

导语：研究人员还观察到攻击者正在积极地改变研究人员的工具、战术和程序（TTP）以绕过安全解决方案。在这篇文章中，研究人员还将介绍和分析攻击者使用的其他工具和恶意软件。

经过几个月的调查，趋势科技的研究人员发现Earth Preta正在使用一些从未被公开的恶意软件和用于泄露目的的有趣工具。研究人员还观察到攻击者正在积极地改变研究人员的工具、战术和程序（TTP）以绕过安全解决方案。在这篇文章中，研究人员还将介绍和分析攻击者使用的其他工具和恶意软件。

在之前的研究中，研究人员披露并分析了Earth Preta(又名Mustang Panda)组织发起的一项新型攻击活动。在最近的一次活动中，研究人员通过监测发现Earth Preta通过鱼叉式网络钓鱼邮件和谷歌驱动器链接发送诱饵文件。经过几个月的调查，研究人员发现攻击者在这次活动中使用了一些从未公开的恶意软件和用于泄露目的的有趣工具。

**感染链**

经调查，整个攻击始于鱼叉式网络钓鱼电子邮件。经过对攻击程序的长期调查，研究人员确定了完整的感染链如下所示。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983741348972.png "1679983741348972.png")

完整的感染链

研究人员将不同的TTP分为六个阶段：攻击载体、发现、权限升级、横向移动、命令与控制(C&C)和泄露。在之前的研究中，研究人员在第一阶段(攻击载体)涵盖了大多数新的TTP和恶意软件。但是，研究人员观察到一些TTP已经发生了变化。在接下来的部分中，我们将重点关注更新后的攻击载体及其后续阶段。

**攻击载体**

之前Earth Preta使用的攻击载体，研究人员将它们分为三种类型（DLL侧加载、快捷链接和伪文件扩展名）。从2022年10月和11月开始，研究人员观察到攻击者开始改变研究人员的TTP，以部署TONEINS、TONESHELL和PUBLOAD恶意软件和QMAGENT恶意软件。研究人员认为，攻击者正在使用这些新技术逃避。

**Trojan.Win32.TONEINS**

根据研究人员之前的观察，TONEINS和TONESHELL恶意软件是从嵌入电子邮件正文的谷歌驱动器链接下载的。为了绕过电子邮件扫描服务和电子邮件网关解决方案，谷歌驱动器链接现在已经嵌入到诱饵文件中。该文件诱使用户下载带有嵌入式链接的受密码保护的恶意文件。然后可以通过文件中提供的密码在内部提取文件。通过使用此技术，攻击背后的恶意攻击者可以成功绕过扫描服务。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983749938011.png "1679983749938011.png")

一份诱饵文件，其中嵌入了谷歌驱动器链接和密码

在新的攻击载体中，整个感染流程已更改为下图所示的程序。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983845968821.png "1679983845968821.png")

攻击载体的感染流

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983853980748.png "1679983853980748.png")

新攻击载体中的文件

在分析下载的文件后，研究人员发现这是一个恶意RAR文件，包含TONEINS恶意软件libcef.dll和 border.docx中的TONESHELL malware ~List of terrorist personnel 。它们的感染流程类似于之前报告中的攻击载体类型C，唯一的区别是伪造的.docx文件具有XOR加密内容，以防止被检测到。例如，~$Evidence information.docx是一个伪装成Office Open XML文件的文件。因此，它似乎是无害的，甚至可以通过使用7-Zip等解压软件打开。

攻击者在一个文件的ZIPFILERECORD结构中隐藏了一个PE文件。TONEINS恶意软件libcef.dll将在XOR操作中用一个字节解密该文件，找到PE头，并将有效负载放置到指定的路径。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983862842329.png "1679983862842329.png")

在对最后一个ZIPFILECECORD结构中的frData成员进行解密后，将显示PE文件

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983871184474.png "1679983871184474.png")

TONEINS的解密函数

感染流的后续行为通常与之前的分析相同，更多的细节我们之前已经介绍过。

**Trojan.Win32.PUBLOAD**

在最近的案例中，恶意软件PUBLOAD也是通过嵌入在诱饵文件中的谷歌驱动器链接传播的。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983880515401.png "1679983880515401.png")

美国大使馆的诱饵邀请函

自2022年10月以来，研究人员一直在观察PUBLOAD的一种新变体，该变体使用伪造的HTTP标头来传输数据，LAC的报告也讨论了这一点。与之前的PUBLOAD变体不同，它在数据包中预先准备了一个具有合法主机名的HTTP标头。研究人员认为，攻击者试图在正常流量中隐藏恶意数据。HTTP正文中的数据与过去的变体相同，后者具有相同的魔法字节17 03 03和加密的受害者信息。研究人员能够成功地从实时C&C服务器中检索到有效负载，这使得我们能够继续分析。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983889124866.png "1679983889124866.png")

PUBLOAD HTTP变体的C&C流量

一旦接收到有效负载，它将检查前三个魔术字节是否为17 03 03，以及接下来的两个字节是否为有效载荷的大小。然后，它将使用预定义的RC4密钥78 5A 12 4D 75 14 14 11 6C 02 71 15 5A 73 05 08 70 14 65 3B 64 42 22 23 2000 00 00 00 00 00 00 00 00解密加密的有效负载，该密钥与PUBLOAD加载程序中使用的密钥相同。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983898553092.png "1679983898553092.png")

从PUBLOAD HTTP变体检索到的第一个有效负载

解密之后，它检查解密有效负载的第一个字节是否为0x06。解密的有效负载包含用字节23 BE 84 E1 6C D6 AE 52 90进行XOR加密的另一个有效负载。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679983908878735.png "1679983908878735.png")

从PUBLOAD HTTP变体检索到的第二个有效负载

解密后，还有另一个支持数据上传和命令执行的最终后门负载。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679984960572222.png "1679984960572222.png")

PUBLOAD HTTP变体的最终有效负载

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985011113693.png "1679985011113693.png")

PUBLOAD HTTP变体中的命令代码

此外，研究人员还在PUBLOAD示例中发现了一些有趣的调试字符串和事件名称。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985035161043.png "1679985035161043.png")

PUBLOAD中的事件名称

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985046140103.png "1679985046140103.png")

PUBLOAD中的调试字符串

总之，研究人员认为新的TONESHELL和PUBLOAD文件一直在迭代，且有了一些共同之处。例如，为了绕过防病毒扫描，它们现在都被放置在诱饵文件中（如谷歌硬盘链接）。

**攻击过程**

一旦攻击者获得了对受害者环境的访问权限，研究人员就可以通过以下命令开始检查环境：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985055181248.png "1679985055181248.png")

**权限提升**

在这次活动中，研究人员发现了Windows 10中用于UAC绕过的几个工具。接下来我们将一一介绍。

**HackTool.Win 32.ABPASS**

HackTool.Win32.ABPASS是一个用于绕过Windows 10中的UAC的工具。根据我们的分析，它重用了ucmShellRegModMethod3函数中的代码，该函数来自一个著名的开源项目UACME。Sophos的一份报告介绍了这一工具。

该工具接受一个参数，并将以下数据写入注册表：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985082182707.png "1679985082182707.png")

ABPASS更改了注册表项

它还改变了Windows处理ms-settings协议的方式，在本例中，字符串ms-settings是一个编程标识符(ProgID)。如果CurVer项设置在ProgID下，它将用于版本控制并将当前ProgID (ms-settings)映射到CurVer默认值中指定的ProgID。反过来，ms-settings的行为被重定向到自定义的ProgID aaabbb32。它还设置了一个新的ProgID aaabbb32及其shell打开命令。最后，执行fodhelper.exe或computerDefaults.exe来触发ms-settings协议。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985093131403.png "1679985093131403.png")

新增的ProgID aaabbb32

**HackTool.Win 32.CCPASS**

HackTool.Win 32.CCPASS是另一个用于Windows 10 UAC绕过的工具，并类似地重用项目UACME中函数ucmMsStoreProtocolMethod中的代码。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985108154202.png "1679985108154202.png")

CCPASS和ucmMsStoreProtocolMethod中的代码相似性

它的工作方式与ABPASS类似。然而，与ABPASS不同的是，它劫持了ms-windows存储协议。黑客工具CCPASS的工作原理如下：

1.它禁用了协议ms-windows存储的应用程序关联toast。

2.它在注册表中创建一个新的Shell；

3.它调用未记录的API UserAssocSet来更新文件关联；

4.它执行WSReset.exe来触发此协议。

在Windows 10及以上版本中，系统会显示一个新的toast对话框，用于为选定的文件类型选择打开的应用程序。要隐藏此窗口，该工具会明显地将新条目添加到HKCU\Software\Microsoft\Windows\CurrentVersion\ApplicationAssociationToast，以禁用与协议ms-Windows存储相关的所有Toast。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985118603663.png "1679985118603663.png")

应用程序关联toast的示例

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985129951698.png "1679985129951698.png")

通过注册表隐藏应用程序关联toast

完成此操作后，该工具开始更改ms-windows-store的shell命令，并最终使用WSReset.exe触发它。

**SilentCleanup**

在Windows 10中，有一个名为“SilentCleanup”的本地Windows服务。该服务具有最高权限，可以用于Windows 10 UAC绕过。通常，此服务用于运行%windir%\system32\cleanmgr.exe。但是，可以劫持环境变量%windir%并将其更改为任何路径以实现权限升级。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1679985139161421.png "1679985139161421.png")

滥用SilentCleanup服务的恶意命令

研究人员观察到攻击者使用这种技术来执行c:\users\public\1.exe。

**横向运动**

在这个阶段，研究人员观察到某些恶意软件，如HIUPAN和ACNSHELL（最初由Mandiant和S...