---
title: 手把手教你如何用 ROP 绕过数据执行保护
url: https://www.4hou.com/posts/50OK
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-18
fetch_date: 2025-10-04T07:21:36.336432
---

# 手把手教你如何用 ROP 绕过数据执行保护

手把手教你如何用 ROP 绕过数据执行保护 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 手把手教你如何用 ROP 绕过数据执行保护

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-02-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161127

收藏

导语：在这篇文章中，我们将介绍应用程序的逆向过程，以发现缓冲区溢出漏洞，并开发用于绕过DEP的ROP小工具链(Gadget Chain)。

DEP（数据执行保护）是一种内存保护功能，允许系统将内存页标记为不可执行。ROP（面向返回的编程）是一种利用技术，允许攻击者在启用DEP等保护的情况下执行shellcode。在这篇文章中，我们将介绍应用程序的逆向过程，以发现缓冲区溢出漏洞，并开发用于绕过DEP的ROP小工具链(Gadget Chain)。

我们将在开发过程中使用以下工具：QuoteDB、TCPView（一个查看端口和线程的小工具，只要木马在内存中运行，一定会打开某个端口，只要黑客进入你的电脑，就有新的线程）、IDA Freeware、WinDbg（在windows平台下，强大的用户态和内核态调试工具）和rp++。

QuoteDB是一个设计上易受攻击的应用程序，创建它是为了实践逆向工程并利用它进行开发。如下图所示，该应用程序正在侦听端口3700上的网络连接：

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572223881227.jpeg "1674572223881227.jpeg")

我们已经使用TCPView确认程序确实在监听端口3700。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572239684302.jpeg "1674572239684302.jpeg")

现在我们需要对应用程序进行逆向工程，看看它是如何处理网络连接的。accept函数用于允许指定端口上的传入连接，然后进程创建一个运行“handle\_connection”例程的新线程，如下所示：

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572247156133.jpeg "1674572247156133.jpeg")

recv函数用于从连接的套接字接收数据：

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572257110760.jpeg "1674572257110760.jpeg")

我们已经开发了一个基本的Python脚本，它创建一个TCP套接字，并在端口3700上向远程服务器发送1000个“a”字符：

![5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572268696252.jpeg "1674572268696252.jpeg")

我们已将WinDbg附加到QuoteDB.exe进程，并列出了加载的模块，如下图所示。

![6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572276201560.jpeg "1674572276201560.jpeg")

我们可以使用“bp”命令在recv函数调用后放置断点，使用“bl”命令确认断点已成功设置：

![7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572285144118.jpeg "1674572285144118.jpeg")

recv函数返回后，EAX寄存器包含以十六进制接收的字节数：

![8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572294460651.jpeg "1674572294460651.jpeg")

缓冲区的前4个字节表示一个操作码，该操作码被移到EAX寄存器中，然后打印在命令行中：

![9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572303857767.jpeg "1674572303857767.jpeg")

下图显示了WinDbg中的printf调用，我们可以观察到第三个参数（=Opcode）由4个“A”字符组成：

![10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572313104708.jpeg "1674572313104708.jpeg")

该进程显示源IP地址、源端口、缓冲区长度和十进制的操作码：

![11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572323176777.jpeg "1674572323176777.jpeg")

应用程序从Opcode中减去0x384（十进制900），并将结果与4进行比较。这是一个带有5个示例的开关，也显示在下图中。

![12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572333300138.jpeg "1674572333300138.jpeg")

EAX寄存器大于4，执行流被重定向到默认情况，该情况调用“log\_bad\_request”函数：

![13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572344158988.jpeg "1674572344158988.jpeg")

上述函数包含缓冲区溢出漏洞，如下图所示，可执行文件在堆栈上分配0x818（2072）字节，用0初始化缓冲区，并在不检查边界的情况下将有效负载复制到此缓冲区：

![14.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572356141041.jpeg "1674572356141041.jpeg")

发生溢出是因为要复制的字符数（0x4000）大于缓冲区的大小，并且可能会重写返回地址：

![15.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572367754864.jpeg "1674572367754864.jpeg")

我们选择发送3000个“A”字符以利用该漏洞。如下所示，返回地址在堆栈上被重写，程序因此崩溃：

![16.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572379132395.jpeg "1674572379132395.jpeg")

![17.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572389122804.jpeg "1674572389122804.jpeg")

我们使用了“msf-pattern\_create”命令来生成一个唯一的模式，该模式将为我们提供偏移量。

![18-1536x180.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572404191133.jpeg "1674572404191133.jpeg")

应用程序在不同的地址崩溃，该地址用于使用“msf-pattern\_offset”命令确定精确的偏移量：

![19.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572422216862.jpeg "1674572422216862.jpeg")

![20.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572433190876.jpeg "1674572433190876.jpeg")

我们修改了概念证明，以包括上述偏移量。在正确的地址崩溃后，ESP寄存器指向我们控制的缓冲区的最后一部分：

![21.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572446192263.jpeg "1674572446192263.jpeg")

![22.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572456170023.jpeg "1674572456170023.jpeg")

我们使用了narly WinDbg扩展来显示加载的模块及其内存保护，下图显示了该可执行文件是在启用ASLR和DEP保护的情况下编译的。

![23.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572478169558.jpeg "1674572478169558.jpeg")

Windows Defender Exploit Guard可以用来启用/禁用ASLR。我们需要进入“Exploit protection settings”，选择“Program settings”页签，点击“Add Program to custom”，选择“Choose exact file path”选项：

![24.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572492317768.jpeg "1674572492317768.jpeg")

![25.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572502679379.jpeg "1674572502679379.jpeg")

我们想通过发送从“\x00”到“\xFF”的所有字节并确定它们如何写入堆栈来找出哪些字符被认为是“不适合”的：

![26-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572514954027.jpeg "1674572514954027.jpeg")

如下图所示，没有不适合的字符，不过为了研究，我们将“\x00”视为不适合字符，因为它通常是不适合字符。正因为如此，漏洞开发过程稍微复杂一些，但它可能更容易适应其他应用程序。

![27.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572527651784.jpeg "1674572527651784.jpeg")

我们使用rp++工具从“SysWOW64\kernel32.dll”模块中提取ROP小工具，因为ASLR是禁用的，所以我们可以选择任何提供必要ROP小工具的DLL，但是，我们将在以后的文章中看到应用程序泄漏特定DLL中的地址。我们已将小工具中的最大指令数设置为5：

![28.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572539151397.jpeg "1674572539151397.jpeg")

![29.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572549124749.jpeg "1674572549124749.jpeg")

由于DEP保护，堆栈不再是可执行的，我们需要找到执行shellcode的方法。我们可以使用VirtualAlloc、VirtualProtect和WriteProcessMemory等API来绕过DEP。VirtualAlloc函数用于保留、提交或更改进程地址空间中页面的状态。该函数有4个参数：

```
lpAddress
dwSize
flAllocationType
flProtect
```

我们的目的是将flAllocationType参数设置为0x1000（MEM\_COMMIT），将flProtect设置为0x40（PAGE\_EXECUTE\_READWRITE）。我们需要在堆栈上创建以下框架：

```
VirtualAlloc address
Return address (Shellcode address)
lpAddress (Shellcode address)
dwSize (0x1)
flAllocationType (0x1000)
flProtect (0x40)
```

我们为每个元素分配了一个特定的值，需要在运行时使用正确的值对其进行修改。

![30-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572563138559.jpeg "1674572563138559.jpeg")

如下图所示，可以在ESP寄存器的固定偏移处找到框架：

![31.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572602132672.jpeg "1674572602132672.jpeg")

kernel32.dll模块的起始地址可以使用WinDbg来标识。所有ROP小工具的地址必须使用该值而不是“ROP.txt”文件中的加载地址来计算：

![32.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230124/1674572612340768.jpeg "1674572612340768.jpeg")

首先，我们需要找到一个保存ESP寄存器值的ROP小工具。我们确定了一个将ESP寄存器复制到ESI寄存器的寄存器：

![33.jpg](https://img.4hou.com/uploads/ueditor/php/upload/imag...