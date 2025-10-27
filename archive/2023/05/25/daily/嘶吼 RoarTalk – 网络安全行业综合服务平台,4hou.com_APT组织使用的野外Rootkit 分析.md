---
title: APT组织使用的野外Rootkit 分析
url: https://www.4hou.com/posts/XXQ8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-25
fetch_date: 2025-10-04T11:38:58.562748
---

# APT组织使用的野外Rootkit 分析

APT组织使用的野外Rootkit 分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# APT组织使用的野外Rootkit 分析

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-05-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121015

收藏

导语：本文会分析野外发现的两个rootkit示例：Husky rootkit和Mingloa/CopperStealer rootkit。

本文会分析野外发现的两个rootkit示例：Husky rootkit和Mingloa/CopperStealer rootkit。

**驱动入口函数DriverEntry**

让我们从二进制的驱动入口函数DriverEntry开始，在Windows内核驱动程序中，它是DriverEntry。

DriverEntry通常包括以下代码块：

调用IoCreateDevice和IoCreateSymbolicLink；

初始化主要函数数组，其中包含指向各种处理函数的函数指针；

为DriverUnload例程分配一个指向处理程序函数的函数指针。

以下片段（代码段1）展示了如何用C语言实现简单Windows内核驱动程序的DriverEntry。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390806182898.png "1684388478138769.png")

C语言中DriverEntry实现的一个示例

下一个代码段(代码段2)展示了同一个DriverEntry的反汇编过程。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390807206226.png "1684388487605897.png")

代码段2：DriverEntry的反汇编

**DriverUnload函数**

DriverUnload是一个在卸载驱动程序时调用的函数。

此处理程序函数的目的是清除驱动程序在初始化和执行过程中创建的任何资源，例如，删除在DriverEntry中创建的设备和符号链接。

调用ExFreePoolWithTag来取消分配在DriverEntry函数中分配的任何池内存也是一个很好的策略函数。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390808863095.png "1684388497163286.png")

代码段3：C语言中DriverUnload实现的一个示例

**Windows内核结构**

为了充分理解Windows内核驱动程序的反汇编，我们还应该熟悉对象管理器和内核中其他组件使用的一些内核结构。

例如，以下结构是DRIVER\_OBECT（代码段4）。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390808688031.png "1684388513153241.png")

代码段4：分解DRIVER\_OBECT结构

当对IRP进行逆向工程时，绘制出驱动程序使用的IRP主要函数是很有用的。例如，通过查看结构偏移（代码段4）和反汇编（代码段2），我们可以确定sub\_1400014B0是DriverUnload。

我们还可以使用wdm.h/ntddk.h中描述的IRP主要函数代码值，通过检查代码的主要函数，得出sub\_140001280（在Snippet 2中）是IRP\_MJ\_CREATE的函数处理程序的结论，该代码将从DRIVER\_OBECT结构中的MajorFunction（0x70）的偏移量得出0x70的结果。这显然是0x00\*PointerSize（x64体系结构中为8）；因此，正在处理的是IRP\_MJ\_CREATE。

可以用同样的方式，确定IRP\_J\_CLOSE、IRP\_J\_READ、IRP\_MJ\_WRITE和IRP\_J\_DEVICE\_CONTROL的函数处理程序是什么。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390809135327.png "1684388526160856.png")

代码段5：摘自wdm.h，它定义了所有IRP主要函数的常数值

在进行分析时，我们熟悉的其他一些内核结构是IRP和IO\_STACK\_LOCATION结构。

IRP，也称为I/O请求包，是一种在创建I/O请求期间，在设备堆栈中的不同驱动程序之间移动，直到请求完成的结构。

当在用户获取的设备对象的句柄上从用户模式调用具有特定IOCTL操作的DeviceIoControl时，会创建IRP。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390810423899.png "1684388537157502.png")

代码段6：IRP结构的分解

此外，IO\_STACK\_LOCATION表示IRP在设备堆栈中的当前位置（因此IRP结构中的CurrentLocation字段是指向IO\_STACK-LOCATION的指针）。

IO\_STACK\_LOCATION结构包含一个联合类型的参数字段，该字段指定驱动程序中不同主函数要使用的不同参数。

例如，如果当前操作是IRP\_MJ\_DEVICE\_CONTROL，则将使用DeviceIoControl类型的参数，包括OutputBufferLength、InputBufferLength、IoControlCode和Type3InputBuffer。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390810102965.png "1684388552921017.png")

代码段7：IO\_STACK\_LOCATION结构的分解

有了我们对Windows内核驱动程序的新理解，以及如何在Windows驱动程序中找到关键函数，让我们看看一些真实的示例。

**示例1：Brute Ratel C4(BRC4)攻击释放 “Husky” Rootkit**

这项研究来源于Palo Alto Networks Unit 42在一篇关于Brute Ratel C4的博客https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/中提到的与活动相关的示例。不过，他们没有提供这个示例的技术分析。

**示例详细信息**

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390811114548.png "1684388580180487.png")

**示例概述**

该示例是一个内核驱动程序，使用LAP$US组织窃取的NVIDIA证书进行签名。它使用zerosum0x0（图1）找到的Heresy's Gate方法https://zerosum0x0.blogspot.com/2020/06/heresys-gate-kernel-zwntdll-scraping.html，这是一种用于从内核模式驱动程序绕过SMEP向用户模式注入代码的技术。

![微信截图_20230518134625.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390812836064.png "1684388798171111.png")

通过zerosum0x0使用Heresy‘s Gate方法对签名驱动程序进行分解

注入的shellcode使用经典技术，如遍历InLoadOrderModuleList以查找库句柄，以及解析API函数（如LoadLibraryA和GetProcAddress），这些函数可用于解析任何其他API。

注入的shellcode分析起来也很长（图2），看起来与前面提到的Unit 42博客中描述的shellcode非常相似，因为它使用多个推送指令在堆栈上存储数据。存储在堆栈中的数据包括：

Brute Ratel C4的Base64编码配置数据；

Brute Ratel C4有效负载；

可移植可执行文件（PE）64二进制文件，是VMProtect打包的内核驱动程序，稍后加载。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390812611139.png "1684388988120432.png")

图2：摘自shellcode，将许多值推送到堆栈并形成Base64 blob

Brute Ratel C4配置可以使用以下短脚本（代码段8）进行解密：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390813125633.png "1684388997118193.png")

代码段8：用于解码和解密从堆栈中提取的Base64 blob的配置的代码段

解密配置后，我们得到以下输出：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390813210774.png "1684389004197315.png")

代码段9：解密配置的示例

解密的配置数据（Snippet 9）包括Brute Ratel C4有效负载的一些基本配置，包括C2服务器地址和开始通信的端口，对C2的请求应该是什么样子的Base64编码模板，以及C2上用于各种功能和选项的不同路径。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390814190565.png "1684389011926816.png")

攻击场景

我们发现x64 rootkit与Brute Ratel C4示例一起安装在受攻击的设备上更有趣，因为它被覆盖相同示例的其他供应商完全忽略了。

**Husky Rootkit**

x64 rootkit，我们称之为Husky Rootkit，与Brute Ratel有效负载一起被释放。

内核驱动程序由VMProtect打包，并使用颁发给“SHANGMAO CHEN”的证书进行签名(图4)。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390815184015.png "1684389033177278.png")

rootkit使用的证书

**驱动入口函数DriverEntry**

由于这个DriverEntry(图5)函数被打包并混淆了，因此很难从中收集任何信息。它从一系列无条件分支指令(jmp)开始，基本上指向VMProtect解包存根。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390815747405.png "1684389047768244.png")

VMProtected DriverEntry显示了一个无条件分支指令作为它的第一条指令

但是在解包之后，我们发现像GsDriverEntry这样的函数包含了更多的信息，以及我们可以在分析中使用的重要字符串（图6）。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390816165105.png "1684389060417635.png")

从GsDriverEntry中反汇编一个分支，该分支包含以thpt（HTTP的混合版本）作为其URL协议的URL字符串

**C2通信**

rootkit直接与\\Device\Tcp进行交互以进行通信。因此，在受攻击的设备上运行的用户模式工具(如netstat和tcpview)会隐藏连接。

另一种方法是在VM主机上使用Wireshark进入客户机的共享网络接口，以监控受攻击虚拟机的所有通信流量（图7和图8）。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390817382938.png "1684389074200596.png")

Wireshark网络捕获的由rootkit启动的流量

该恶意软件与多个域以及每个域的相对路径进行通信。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390817140588.png "1684389091985145.png")

从服务器到URL中的/xccdd路径的Web请求和响应显示了响应有效负载

**隐写术**

引起我们注意的特定HTTP流量是从以下URL下载的一些图像（JPEG–JFIF标头）：http://pic.rmb.bdstatic.com//bjh/.jpeg.

JPEG文件(图9)是一张看起来很无辜的狗的图片，因此研究人员将这些图片命名rootkit为“Husky”。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390818151935.png "1684389101183588.png")

该图片含有有效负载

每个JPEG也有一个隐写有效负载，其形式是在多个0的分隔符之后，将数据连接到偏移量为0x1769的图片末尾(图10)。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390819908520.png "1684389131302393.png")

jpg文件中带有狗的图片末尾和负载的开始之间的分隔符的Hexview

通过查看数据，我们可以看到前32个字节与前一个请求对hxxp://rxeva6w.com:10100/xccdd的十六进制格式的服务器响应相同(代码段10)。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230518/1684390820162157.png "1684389148188217.png")

代码段10：有效负载的前32个字节在不同的有效负载中相似

讽刺是，域rxeva6w.com在88次检测中一次...