---
title: 揭开Earth Preta最新的工作原理
url: https://www.4hou.com/posts/4vYJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-07
fetch_date: 2025-10-04T11:52:41.570022
---

# 揭开Earth Preta最新的工作原理

揭开Earth Preta最新的工作原理 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 揭开Earth Preta最新的工作原理

luochicun
[技术](https://www.4hou.com/category/technology)
2023-07-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117773

收藏

导语：本文将介绍Earth Preta APT组织利用的最新工具、技术和程序（TTP）的更多技术细节。

本文将介绍Earth Preta APT组织利用的最新工具、技术和程序（TTP）的更多技术细节。介绍在2022年11月，趋势科技的研究人员就披露了由高级持续性威胁（APT）组织Earth Preta（也称为Mustang Panda）发起的大规模网络钓鱼活动。该活动通过鱼叉式网络钓鱼电子邮件针对亚太地区的多个国家。自2023年初以来，该组织正在使用新的方法，例如MIROGO和QMAGENT。

此外，研究人员还新发现了一个名为TONEDROP的释放程序，它可以释放TONEINS和TONESHELL恶意软件，根据观察，该组织正在将其目标扩展到不同的地区，如东欧和西亚，再加上亚太地区的几个国家，如缅甸和日本。

通过追踪分析恶意软件和下载网站，研究人员试图找到攻击者用来绕过不同安全解决方案的工具和技术。例如，研究人员收集了部署在恶意下载网站上的脚本，这使他们能够弄清楚它们的工作原理。研究人员还观察到，Earth Preta向不同的受害者提供不同的有效负载。

**受害者研究**

从2023年1月开始，研究人员就观察到几波针对不同地区个人的鱼叉式网络钓鱼电子邮件。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544324690668.jpg "1688544324690668.jpg")

鱼叉式网络钓鱼邮件收件人的国家分布

研究人员还能根据目标行业对受害者进行细分。如下图所示，大多数目标自电信行业。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544888222825.png "1688544888222825.png")

鱼叉式网络钓鱼邮件收件人的行业分布

2023年，研究人员使用了新的攻击指标监测了Earth Preta，包括MIROGO、QMAGENT和名为TONEDROP的新TONESHELL释放程序。

同样，这些攻击链也发生了变化。例如，除了部署合法的Google Drive下载链接外，攻击者还使用其他类似但实际上不是Google Drive页面的下载网站。

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544906116162.jpg "1688544906116162.jpg")

2023年的事件时间线

**Backdoor.Win32.QMAGENT**

2023年1月左右，研究人员发现QMAGENT恶意软件通过鱼叉式网络钓鱼电子邮件传播，目标是与政府组织有关的个人。QMAGENT（也称为MQsTTang）最初是在ESET的一份报告中披露，值得注意的是，它利用了物联网（IoT）设备中常用的MQTT协议来传输数据和命令。由于上述报告详细描述了恶意软件的技术细节，我们在此不再赘述。然而，研究人员认为所使用的协议值得进一步调查。

**Backdoor.Win32.MIROGO**

2023年2月，研究人员发现了另一个用Golang编写的名为MIROGO的后门，Check Point Research首次将其报告为TinyNote恶意软件。研究人员注意到，它是通过一封嵌入Google Drive链接的钓鱼电子邮件发送的，然后下载了一个名为Note-2.7z的压缩文件。该压缩文件受密码保护，密码在电子邮件正文中提供。提取后，研究人员发现了一个伪装成发给政府的可执行文件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544931111227.png "1688544931111227.png")

MIROGO攻击流程

**Trojan.Win32.TONEDROP**

2023年3月，研究人员发现了一个名为TONEDROP的新释放程序，它可以释放TONEINS和TONESHELL恶意软件。它的攻击链与之前报告中介绍的相似，涉及隐藏被异或的恶意二进制文件的虚假文件。

在接下来的几个月里，研究人员发现该组织还在使用这个释放程序。在研究人员的调查过程中，他们发现了TONESHELL后门的一个新变体。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544949196436.png "1688544949196436.png")

释放程序流程

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544971294313.png "1688544971294313.png")

TONEDROP中的文件

在释放和安装文件之前，TONEDROP将检查文件夹C:\ProgramData\LuaJIT是否存在，以确定环境是否已经被破坏。它还将检查正在运行的进程和窗口是否与恶意软件分析工具有关。如果是这样，它将不会继续其例行程序。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688544989196440.png "1688544989196440.png")

检查正在运行的进程和窗口

如果所有条件都满足了，它将开始安装过程并释放几个文件。这些文件嵌入到释放程序中，并使用异或密钥解密。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545012158134.png "1688545012158134.png")

释放的文件和用于解密它们的异或密钥

被释放后，WaveeditNero.exe将侧载waveedit.dll并解密其他两个伪造的PDF文件：

它用XOR密钥0x36解密C:\users\public\last.pdf，并将其写入C:\users\public \documents\WinDbg（X64）.exe。

它用XOR密钥0x2D解密C:\users\public\update.pdf，并将其写入C:\users\public\documents\ libvcl .dll。

TONEDROP将为进程C:\users\public\documents\WinDbg（X64）.exe设置一个计划任务，它将绕过加载C:\users\public\documents\ libvcl .dll。接下来，它将通过调用具有回调函数的API EnumDisplayMonitors来构造恶意负载并在内存中运行它。

**TONESHELL变体D的C&C协议**

研究人员发现了TONESHELL的一个新变体，它具有如下命令和控制（C&C）协议请求数据包格式：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545028167768.png "1688545028167768.png")

加密后发送数据的内容

C&C协议类似于PUBLOAD和其他TONESHELL变体所使用的协议。研究人员将其归类为TONESHELL变体D，因为它还使用CoCreateGuid来生成唯一的受害者ID，这与旧的变体类似。

在第一次握手中，有效负载应该是一个0x221字节长的缓冲区，其中包含加密密钥和唯一受害者ID。表4显示了有效负载的结构。请注意，字段type、victim\_id和xor\_key\_seed在发送缓冲区之前使用xor\_key进行加密。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545044604759.png "1688545044604759.png")

发送数据的内容

研究人员发现该恶意软件将victim\_id的值保存到文件%USERPROFILE%\AppData\Roaming\Microsoft\Web.Facebook.config中。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545061214309.png "1688545061214309.png")

第一次握手中的有效负载

C&C通信协议的工作原理如下：

1.将包含xor\_key和victim\_id的握手发送到C&C服务器；

2.接收由魔术组成并且具有0x02大小的5字节大小的数据包；

3.接收到一个用xor\_key解密的2字节大小的数据包，该数据包的第一个字节必须为0x08；

4.接收到由魔术和下一个有效负载大小组成的数据。

5.使用xor\_key接收并解密数据。第一个字节是命令代码，下面的数据是额外的信息。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545080941805.png "1688545080941805.png")

C&C通信

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545095964162.png "1688545095964162.png")

命令代码

**虚假Google Drive网站**

2023年4月，研究人员发现了一个传播QMAGENT和TONEDROP等恶意软件类型的下载网站。当研究人员请求URL时，它下载了一个名为Documents.rar的下载文件，其中包含一个原来是QMAGENT示例的文件。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545111950387.png "1688545111950387.png")

下载网站的截图

虽然这个页面看起来像Google Drive下载页面，但它实际上是一个试图伪装成普通网站的图片文件（gdrive.jpg）。在源代码中，它运行脚本文件，它将下载文件Document.rar。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545127134045.png "1688545127134045.png")

嵌入下载网站的恶意脚本

2023年5月，Earth  Preta连续传播了具有不同路径的同一下载网站来部署TONESHELL，例如https://rewards[.]roshan[.]af/aspnet\_client/acv[.]htm。在这个版本中，攻击者用另一段JavaScript混淆了恶意URL脚本，如下图所示。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545152688550.png "1688545152688550.png")

该页面的源代码

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545169155697.png "1688545169155697.png")

解码后的恶意脚本URL

最后，脚本jQuery.min.js将从https://rewards.roshan[.]af/aspnet\_client/Note-1[.]rar下载归档文件。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545190128539.png "1688545190128539.png")

jQuery.min.js脚本

**技术分析**

在调查过程中，研究人员尝试了几种方法来追踪事件，并将所有指标联系在一起。研究人员的发现可以概括为三个方面：代码相似性、C&C连接和糟糕的操作安全性。

**代码相似性**

研究人员观察到MIROGO和QMAGENT恶意软件之间有一些相似之处。由于检测次数有限，研究人员认为这两种工具都是Earth Preta开发的，且它们都是用两种不同的编程语言实现了类似的C&C协议。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545273601863.png "1688545273601863.png")

MIROGO和QMAGENT恶意软件的异同

**C&C 通信**

恶意软件QMAGENT使用MQTT协议传输数据。经过分析，研究人员意识到所使用的MQTT协议没有加密，也不需要任何授权。由于MQTT协议中的独特“特性”（一个人发布消息，其他所有人接收消息），研究人员决定监控所有消息。他们制作了一个QMAGENT客户端，看看有多少受害者被盯上了。经过长期监测，研究人员制作了如下统计表：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545300113580.png "1688545300113580.png")

QMAGENT通信

主题名称iot/server0用于检测分析或调试环境，因此受害者数量最少。3月份的峰值最高，因为ESET报告是在3月2日发布的，这个峰值涉及自动化系统（沙箱和其他分析系统）的激活。因此，研究人员决定将峰值分解成更小的范围。

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545326115735.png "1688545326115735.png")

QMAGENT受害者

来自QMAGENT恶意软件的C&C请求JSON体包含一个Alive密钥，该密钥是恶意软件的正常运行时间（以分钟为单位）。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230705/1688545340296811.png "1688545340296811.png")

QMAGENT受害者活动时间

研究人员将前10个的运行时间分为三类：473秒、200秒和17...