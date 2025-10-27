---
title: 手把手教你如何用 ROP 绕过数据执行保护
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557648&idx=2&sn=edf38daa0b18f33de334991dcf333400&chksm=e914322ade63bb3c31f0b887f6ed1f2ccddf962d53e42006aaa93a78d45ee0e1c5beb80037b5&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-18
fetch_date: 2025-10-04T07:25:48.653559
---

# 手把手教你如何用 ROP 绕过数据执行保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtkCibmK0cqjDEXbib4EbADXMvSDgWPIyibOA3Nd2psjk3vBxZ9Z8HzSd4w/0?wx_fmt=jpeg)

# 手把手教你如何用 ROP 绕过数据执行保护

xiaohui

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

DEP（数据执行保护）是一种内存保护功能，允许系统将内存页标记为不可执行。ROP（面向返回的编程）是一种利用技术，允许攻击者在启用DEP等保护的情况下执行shellcode。在这篇文章中，我们将介绍应用程序的逆向过程，以发现缓冲区溢出漏洞，并开发用于绕过DEP的ROP小工具链(Gadget Chain)。

我们将在开发过程中使用以下工具：QuoteDB、TCPView（一个查看端口和线程的小工具，只要木马在内存中运行，一定会打开某个端口，只要黑客进入你的电脑，就有新的线程）、IDA Freeware、WinDbg（在windows平台下，强大的用户态和内核态调试工具）和rp++。

QuoteDB是一个设计上易受攻击的应用程序，创建它是为了实践逆向工程并利用它进行开发。如下图所示，该应用程序正在侦听端口3700上的网络连接：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYticqkYmxrEoVBTLjE29vl9j5ZFFFfBU7esIFO1ZVGvhPqNqKtuZhoHXg/640?wx_fmt=jpeg)

我们已经使用TCPView确认程序确实在监听端口3700。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYticWb3MTW3LF7ibRD6cM72PoJcNicaFHSxCfkXgK1n0uic3PNzribaeCT9xw/640?wx_fmt=jpeg)

现在我们需要对应用程序进行逆向工程，看看它是如何处理网络连接的。accept函数用于允许指定端口上的传入连接，然后进程创建一个运行“handle\_connection”例程的新线程，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtcEKEXSuzwgH7HJFGwarOpDqVcnfAhiaXHZ7OgIj1m6oTPVAq2xTiarPQ/640?wx_fmt=jpeg)

recv函数用于从连接的套接字接收数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtnf5F3DUrc5YUexXqyRxTSIEm27nicXBf5VgXTWUqmnoBS1ASI1DBEKQ/640?wx_fmt=jpeg)

我们已经开发了一个基本的Python脚本，它创建一个TCP套接字，并在端口3700上向远程服务器发送1000个“a”字符：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtNH9a8D87Aw0dUHMEKDHZPB3icCqr1ticFv8Ow91hj542eB9IJPibKEM7g/640?wx_fmt=jpeg)

我们已将WinDbg附加到QuoteDB.exe进程，并列出了加载的模块，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtXe6fprFyANPF1iaRyDfeLYftTTjBiaiaG6uWs7dNvmfUmCkHFL0Br3Eyg/640?wx_fmt=jpeg)

我们可以使用“bp”命令在recv函数调用后放置断点，使用“bl”命令确认断点已成功设置：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYt8sicqzucvS6sQClYicu0PfLUDUUmPD8E3e7hoGgXtfXIqlSRUDydp51g/640?wx_fmt=jpeg)

recv函数返回后，EAX寄存器包含以十六进制接收的字节数：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtl3TwNJgWdVOYiaQlmssuWDSFu7WmSRk1q25fpCR4BzJqGeTmEibBfJGw/640?wx_fmt=jpeg)

缓冲区的前4个字节表示一个操作码，该操作码被移到EAX寄存器中，然后打印在命令行中：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtLjCibhVl0vxZQMgLfQ1EldRf0dz7RQGtiae0tIFYr9PeDyZtHJfgyHcg/640?wx_fmt=jpeg)

下图显示了WinDbg中的printf调用，我们可以观察到第三个参数（=Opcode）由4个“A”字符组成：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtqc8T3X7u1QS7brMWDZcF9mpV5AcFKj5TsNF60iaDJyxytZ5WymUC6UQ/640?wx_fmt=jpeg)

该进程显示源IP地址、源端口、缓冲区长度和十进制的操作码：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtGuqOG0mNc8NIkVra0ticyib4uBEsdFQaiabicNwib7OuJPDXFtnxjL2s9wg/640?wx_fmt=jpeg)

应用程序从Opcode中减去0x384（十进制900），并将结果与4进行比较。这是一个带有5个示例的开关，也显示在下图中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtyh88xbhXwXkibEZqlMbrZZ3EhdzEKDvW5HbAXia1o0l6o2icr5AcT7KIg/640?wx_fmt=jpeg)

EAX寄存器大于4，执行流被重定向到默认情况，该情况调用“log\_bad\_request”函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtgyUlHpIibq61hPeHWvPy3dvsTTmV0eZTwOpQFCYB8cHxhrRWWTZ3ysw/640?wx_fmt=jpeg)

上述函数包含缓冲区溢出漏洞，如下图所示，可执行文件在堆栈上分配0x818（2072）字节，用0初始化缓冲区，并在不检查边界的情况下将有效负载复制到此缓冲区：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYt8jmgunzuT6ZPmn8lqoKU32A8G0jgB8HoHpmXZg9O492Fm2VialJaRibg/640?wx_fmt=jpeg)

发生溢出是因为要复制的字符数（0x4000）大于缓冲区的大小，并且可能会重写返回地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtSXvBibdsldCZRsgMG1GliaQ8OVQCqcZhYyHSsD1OpTzHIYVOSYWbj32A/640?wx_fmt=jpeg)

我们选择发送3000个“A”字符以利用该漏洞。如下所示，返回地址在堆栈上被重写，程序因此崩溃：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYttKic2U3KNZWkywV6dufwTQ5An71Uy4O3NN7siaEw84RhOz63C83znJaQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtVaBpeJiaZcGyIbAnDTh3nhT3v44BBTtW711ia2viaYvKcRtOH40s3ZJKQ/640?wx_fmt=jpeg)

我们使用了“msf-pattern\_create”命令来生成一个唯一的模式，该模式将为我们提供偏移量。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtgZ44jmEWwsToeryk6qiaao8icVNWTGjcXaQWcC8JjQbYOh31KUcS0tww/640?wx_fmt=jpeg)

应用程序在不同的地址崩溃，该地址用于使用“msf-pattern\_offset”命令确定精确的偏移量：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtEkyAvq8rQ97w9AL1tt2DiaFgcVeo6UicE3jjkAcjF2L43K5TicvVBacWg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtqPpkia83CCpCgNGGicwo8jlhJu8DoNhVYG1vk9VeZGHevPELln4EAsgQ/640?wx_fmt=jpeg)

我们修改了概念证明，以包括上述偏移量。在正确的地址崩溃后，ESP寄存器指向我们控制的缓冲区的最后一部分：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtA1YUcA7Q2rQ0B2b8XhSXU5QqicV5FwZDhOYRu0tJgQtbFTqhAFqOVPA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtDZeRhJLbTSiaOLNz1mBLKyIw4BYJdrhVbFqRdjdkGibI3oDmmmAvRUNw/640?wx_fmt=jpeg)

我们使用了narly WinDbg扩展来显示加载的模块及其内存保护，下图显示了该可执行文件是在启用ASLR和DEP保护的情况下编译的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtwxv5eDFI5E2PQfJshtV3yicPs16U6DWNv86AnC9ftv3t3jx40Em8YjQ/640?wx_fmt=jpeg)

Windows Defender Exploit Guard可以用来启用/禁用ASLR。我们需要进入“Exploit protection settings”，选择“Program settings”页签，点击“Add Program to custom”，选择“Choose exact file path”选项：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtxjw6maARMnUp52Sr6GicaKJ2cWHaUibvdWyl0jffl8Pm2E5RFALGIaZg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtSv6hIt0KPa3LzMBXwwzTu0r0mupYBw53vPI2qcWzrwVG9nBjOic2zsw/640?wx_fmt=jpeg)

我们想通过发送从“\x00”到“\xFF”的所有字节并确定它们如何写入堆栈来找出哪些字符被认为是“不适合”的：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtO5PXnOgnICXVZ71sde47nP1iaCicsOhHibeuAbia3HXUH1W4Za6qHofiblg/640?wx_fmt=jpeg)

如下图所示，没有不适合的字符，不过为了研究，我们将“\x00”视为不适合字符，因为它通常是不适合字符。正因为如此，漏洞开发过程稍微复杂一些，但它可能更容易适应其他应用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtNmYcBLT2LSb8leAxw3tkT1LheTDJdy407zwtrOjHLXeHYEb4wLUfpA/640?wx_fmt=jpeg)

我们使用rp++工具从“SysWOW64\kernel32.dll”模块中提取ROP小工具，因为ASLR是禁用的，所以我们可以选择任何提供必要ROP小工具的DLL，但是，我们将在以后的文章中看到应用程序泄漏特定DLL中的地址。我们已将小工具中的最大指令数设置为5：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtJ6B8MiaNJoSYibZ7z9OYVldWJjAzCWKCTBoQPTDqfquOAhMfXTaThEpQ/640?wx_fmt=jpeg)

由于DEP保护，堆栈不再是可执行的，我们需要找到执行shellcode的方法。我们可以使用VirtualAlloc、VirtualProtect和WriteProcessMemory等API来绕过DEP。VirtualAlloc函数用于保留、提交或更改进程地址空间中页面的状态。该函数有4个参数：

lpAddressdwSizeflAllocationTypeflProtect

我们的目的是将flAllocationType参数设置为0x1000（MEM\_COMMIT），将flProtect设置为0x40（PAGE\_EXECUTE\_READWRITE）。我们需要在堆栈上创建以下框架：

VirtualAlloc addressReturn address (Shellcode address)lpAddress (Shellcode address)dwSize (0x1)flAllocationType (0x1000)flProtect (0x40)

我们为每个元素分配了一个特定的值，需要在运行时使用正确的值对其进行修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtWmyF8GTXVAeFlg0icDPLYVOgpRcwibLrJTjlD4Dm8H7BL00PfIsRgR2Q/640?wx_fmt=jpeg)

如下图所示，可以在ESP寄存器的固定偏移处找到框架：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtpagw2YNBjoA2MzWEvd5jOtt4Mxib5pFBeOkKiaRiakcwhCichyc7jBGfHQ/640?wx_fmt=jpeg)

kernel32.dll模块的起始地址可以使用WinDbg来标识。所有ROP小工具的地址必须使用该值而不是“ROP.txt”文件中的加载地址来计算：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtHQJRplYE8Md4TstOlpOoCbKMt8e8nG417lbaEhwbNKruaQbaYFpsQA/640?wx_fmt=jpeg)

首先，我们需要找到一个保存ESP寄存器值的ROP小工具。我们确定了一个将ESP寄存器复制到ESI寄存器的寄存器：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtOBb9FwdKGrSHeMMWKk5PicOSxRWVAZrE8nBQzlAVHGFtyurmXOnvWyA/640?wx_fmt=jpeg)

我们修改了Python脚本，以包含kernel32地址和上述ROP小工具偏移量，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYt6ekGh7qFymRhVryFBOibicZ2hsdT6TXF4ibEwr8Iqj0PoOQ2ibwuWj8DYQ/640?wx_fmt=jpeg)

我们已经成功地将执行流程重定向到我们的第一个ROP小工具，接着将其他ROP小工具链接在一起，因为ESP仍然指向我们的缓冲区：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZaKhYtpfy6wGGMmvXicrkEqh3NkKxrwSNL9Pic3BYYt3RURiceK9UicrAW6ahucw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibQQbqDfjRXtn9RUWZ...