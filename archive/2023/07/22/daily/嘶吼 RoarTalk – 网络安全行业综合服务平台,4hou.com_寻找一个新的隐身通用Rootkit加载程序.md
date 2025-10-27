---
title: 寻找一个新的隐身通用Rootkit加载程序
url: https://www.4hou.com/posts/jgLy
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-22
fetch_date: 2025-10-04T11:53:21.183507
---

# 寻找一个新的隐身通用Rootkit加载程序

寻找一个新的隐身通用Rootkit加载程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 寻找一个新的隐身通用Rootkit加载程序

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-07-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113978

收藏

导语：我们会在本文对一个带签名的rootkit进行分析，它的主要二进制函数是一个通用加载程序，使攻击者能够直接加载第二阶段的未签名内核模块。

我们会在本文对一个带签名的rootkit进行分析，它的主要二进制函数是一个通用加载程序，使攻击者能够直接加载第二阶段的未签名内核模块。

在趋势科技最近的一次调查中，研究人员发现了一个有趣的攻击活动，他们最初认为这是检测微软签名文件时的误报。然而，追踪发现，这是一个新出现的签名rootkit，它与一个大型命令和控制(C&C)基础设施通信，用于我们目前正在跟踪的未知攻击者，我们认为这与rootkit FiveSys背后的攻击者相同。其攻击目标是中国的游戏行业。恶意软件似乎已经通过了Windows硬件质量实验室(WHQL)获得了有效签名。WHQL签章要求确保所有驱动程序是获得OS厂商验证及签章，但这类签章无法保证出于真正App开发商之手。这显示恶意程序作者想利用微软签章制度，让用户误以为它是合法驱动程序而安装。研究人员已在2023年6月向微软安全响应中心(MSRC)报告了他们的发现。

主二进制文件充当通用加载程序，允许攻击者直接加载第二阶段未签名内核模块。每个第二阶段插件都是针对部署它的受害设备自定义的，有些甚至包含针对每台设备的自定义编译驱动程序。每个插件都有一组要从内核空间执行的特定操作。

发现的变体由八个主要集群组成，这些集群基于从签名(Authenticode)中的SPC\_SP\_OPUS\_INFO字段中提取的特定于供应商的元数据，揭示了这些变体代表其签名的各种发布者。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689307982190188.png "1689307982190188.png")

每个集群中的示例数量

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308191196117.png "1689308191196117.png")

2022年和2023年使用微软门户网站签署的驱动程序数量

攻击者目前使用不同的方法对其恶意内核驱动程序进行签名，通常包括：

滥用微软签名门户；

使用泄露和被盗的证书；

使用黑市服务；

接下来，我们将介绍一种明显遵循第一种方法的攻击：滥用WHQL在恶意驱动程序上获得有效签名，该恶意驱动程序可以在最新的Windows版本上成功加载。我们还将提供这种新发现的恶意软件的技术细节，该恶意软件是由微软直接签名的独立内核驱动程序，这是一种不断发展的攻击技术，现在出现的非常频繁。尽管构建这样的能力非常复杂，但当前的攻击者似乎很热衷于这些工具、策略和程序(TTP)。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308206387706.png "1689308206387706.png")

作为独立内核驱动程序由Microsoft直接签名的恶意软件

**WHCP滥用史**

下图显示了Windows硬件兼容性程序(WHCP)滥用史，这些报告导致了Windows内核信任模型的妥协。2021年6月，Netfilter rootkit被报道，之后微软发布了一份报告，详细说明它被用作游戏社区中地理定位作弊的手段。Bitdefender随后在2021年10月披露了FiveSys，这是一个主要用于在线游戏玩家的rootkit，主要目的是窃取凭证和在游戏中购买劫持。最后，Mandiant报告了已知的最后一次滥用，揭露了Poortry恶意软件，该恶意软件已被用于许多网络攻击，包括基于勒索软件的事件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308219113628.png "1689308219113628.png")

WHCP发生时间表

**现代rootkit的检测方法**

在引入内核模式代码签名(KMCS)策略机制的时代，随着64位签名驱动程序的数量增加，现在寻找64位签名的rootkit并不那么容易，如下图所示。由于现代内核rootkit的开发成本更高，而且将内核rootkit纳入其恶意软件库的技术能力不足，或者可以访问绕过新Windows版本中添加的安全防御所需的技术，这使得检测这类攻击变得更加困难。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308233107573.png "1689308233107573.png")

2015年前后检测到的一次以上已签名驱动程序总数

如下图所示，研究人员根据以下内容评估了Windows内核驱动程序示例：

他们签署的驱动程序签名被吊销；

它们有一个或多个基于恶意软件搜索引擎的误报检测，包括VirusTotal恶意软件存储库：

Set 1：未被吊销且无误报检测的已签名驱动程序；

Set 2：未被吊销且有一个或多个来自不同引擎的误报检测的已签名驱动程序；

Set 3：已被吊销且无误报的签名驱动程序；

Set 4：已被吊销的签名驱动程序，其中包含来自不同引擎的一个或多个误报。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308260642557.png "1689308260642557.png")

Windows内核驱动程序基于其签名驱动程序被吊销或以其他方式进行采样，并且它们具有一个或多个误报检测。

从Set 1和Set 2中寻找新的示例提交以查找攻击这样就可以研究这个新出现的示例集群和服务于第二阶段插件的底层C&C基础设施。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308296206252.png "1689308296206252.png")

从2020年到2022年5月，属于示例Set 2的内核驱动程序提交数量增加

**第一阶段分析**

根据从这次活动中收集的示例，我们确定了两个不同的集群，它们的示例之间有多个相似之处。研究人员观察到一种模式，即使用VMProtect对一些示例进行模糊处理，然后在没有任何模糊处理的情况下对具有更多功能的较新示例进行签名，这表明这些示例背后的攻击者仍处于测试和开发阶段。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308329401718.png "1689308329401718.png")

有很多相似之处的两个不同集群

大多数示例都是“Microsoft Windows Hardware Compatibility Publisher”签名的驱动程序。下面我们将对第一个集群中的一个示例进行分析。

驱动程序首先检查加载到内存中的驱动程序上是否有另一个实例，方法是尝试打开由驱动程序在初始化期间创建的符号名称“\？？\ea971b87”。如果成功打开，DriverEntry返回的错误代码“0FFFFCFC7”将停止加载驱动程序。然后，如果驱动程序尚未加载，它将创建一个符号名称“\？？\ea971b87”，并初始化其处理程序的函数。基于我们观察到的当前变体，它仅使用“IRP\_MJ\_DEVICE\_CONTROL”和“IRP\_J\_SHUTDOWN”。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308343499506.png "1689308343499506.png")

检查驱动程序是否已经加载

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308363691579.png "1689308363691579.png")

初始化IO处理程序

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308379193542.png "1689308379193542.png")

注册关闭通知处理程序

然后，驱动程序检查二进制编译是调试构建还是发布，如下图所示。在调试构建的情况下，它在整个执行过程中打印一些调试消息，这表明目前的产品仍在开发和测试中。然后，驱动程序通过编辑注册表禁用用户帐户控制(UAC)和安全桌面模式，并初始化Winsock内核(WSK)对象，以启动C&C服务器的网络活动。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308397506672.png "1689308397506672.png")

检查编译是否是调试构建的

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308448168196.png "1689308448168196.png")

禁用UAC然后初始化WSK对象

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689308484947074.png "1689308484947074.png")

从“IRP\_J\_DEVICE\_CONTROL”设备控制处理程序挂接文件系统堆栈

**第一阶段网络初始化**

第一阶段驱动程序负责与C&C服务器之间的所有网络通信。它使用WSK（一种内核模式的网络编程接口）从内核空间启动所有通信。使用WSK，内核模式软件模块可以使用用户模式Winsock2支持的相同套接字编程概念执行网络I/O操作。

它使用域生成算法（DGA）生成不同的域。如果它无法解析地址，它会直接连接到硬编码在驱动程序内部的辐射ip，它连接到端口80上的驱动程序，并创建一个TCP套接字用于通信。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309454156805.png "1689309454156805.png")

wsk创建的套接字类型

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309467799136.png "1689309467799136.png")

解析DNS

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309479292712.png "1689309479292712.png")

解析DNS

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309494899640.png "1689309494899640.png")

来自第一阶段驱动程序的DNS请求

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309507635056.png "1689309507635056.png")

连接C&C服务器

然后，它定期连接到C&C服务器以获取配置。它可以选择作为内核驱动程序加载程序：

它逐字节地接收来自C&C服务器的数据；

它对接收到的数据进行解码和解密；

它将接收到的内核驱动程序直接加载到内存中，而不将其写入磁盘；

它解析接收到的可移植可执行文件（PE）并执行所有重新定位；

它调用驱动程序入口点；

这样，内核插件就永远不会接触磁盘，只会在内存中，这使得它更隐蔽，并使其能够绕过检测。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309523149134.png "1689309523149134.png")

解码从C&C服务器接收到的数据

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309536697167.png "1689309536697167.png")

接收第一阶段的配置

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309548464474.png "1689309548464474.png")

解析用于加载新接收到的驱动程序的函数地址

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309563206868.png "1689309563206868.png")

获取驱动程序入口地址

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309577129619.png "1689309577129619.png")

调用驱动程序入口函数

**第二阶段插件**

下载的第二阶段驱动程序是自签名的，因为它完全由第一阶段加载程序加载，绕过Windows本机驱动程序加载程序。因此，不需要对这些第二阶段的变体进行签名。它打开文件“C:\WINDOWS\System32\drivers\687ae09e.sys”，然后读取数据并对其进行编码。然后，它将数据划分为内存块并将其写入注册表路径“\ registry \Machine\Software\PtMyMem”及其大小和MD5。之后，它从磁盘中删除文件“C:\WINDOWS\System32\drivers\687ae09e.sys”。

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230714/1689309625877394.png "1689309625877394.png")

第二阶段的自签名驱动程序

![26.png](https://img.4hou.com/up...