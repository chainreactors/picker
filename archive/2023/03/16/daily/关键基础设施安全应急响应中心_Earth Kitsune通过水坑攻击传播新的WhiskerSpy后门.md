---
title: Earth Kitsune通过水坑攻击传播新的WhiskerSpy后门
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535394&idx=2&sn=a7bb1470b76f404b9c92e1d2eb5c9fb1&chksm=c1e9c773f69e4e65081ef587419b9ce0319c3d063ff328017e72a4b5f8f972734df442f9ca68&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-16
fetch_date: 2025-10-04T09:45:45.286218
---

# Earth Kitsune通过水坑攻击传播新的WhiskerSpy后门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibIBRrFwoKr6bib9sHnSV5sE0ROqT4TOsX2rCrP7PD2lXYq9Cn0x25ZibA/0?wx_fmt=jpeg)

# Earth Kitsune通过水坑攻击传播新的WhiskerSpy后门

关键基础设施安全应急响应中心

趋势科技研究人员最近发现了一个新的后门，他们将其归因于之前报道过的被称为Earth Kitsune的攻击者。自2019年以来，“Earth Kitsune”一直在向主要对朝鲜感兴趣的个人传播自主开发的后门变体。在我们过去调查的许多示例中，攻击者通过使用了水坑攻击策略，攻击与朝鲜有关的网站，并将浏览器漏洞注入其中。在分析的最新活动中，Earth Kitsune使用了类似的策略，但没有使用浏览器漏洞，而是使用了社会工程。

在2022年底，研究人员发现一个亲朝组织的网站被入侵和修改，以传播恶意软件。当目标访问者试图在网站上观看视频时，攻击者注入的恶意脚本会显示一条消息提示，通知受害者视频编解码器错误，以诱使他们下载并安装木马编解码器安装程序。安装程序经过修复，加载了一个以前看不见的后门，我们称之为“WhiskerSpy”。此外，我们还发现攻击者采用了一种有趣的持久性技术，滥用了Google Chrome的本地消息主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuOd7oK9YFPEBTGSukKgo0pmFGVIuz3xAzJFbMA1IoVic0wINuQqqfz9Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

WhiskerSpy感染链

在这篇文章中，我们将揭示Earth Kitsune所使用的WhiskerSpy后门的感染链和技术细节。

在2022年底，我们注意到一个亲朝网站在他们的视频页面中注入了恶意脚本。该脚本显示了一个带有虚假错误消息的弹出窗口，旨在诱使受害者安装伪装成高级视频编解码器AVC1的恶意包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGutdxRjBTN5tp5wwA01nq57ZzOelrpJh12PwbZKcnbO74c9aiaRIhLFJg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

一个被攻破的亲朝网站的社会工程示例

这些网页被配置为只向目标IP地址列表中的访问者发送恶意脚本（没有这些IP地址的访问者不会收到恶意负载）。这种配置使得攻击难以被发现。幸运的是，我们设法在攻击者的服务器上找到了一个文本文件，其中包含与目标IP地址匹配的正则表达式。其中包括：

位于中国沈阳的IP地址子网；

一个位于日本名古屋的特定IP地址；

位于巴西的IP地址子网；

沈阳和名古屋的IP地址很可能是他们的真正目标。然而，我们发现巴西的目标IP地址大多属于一个商业VPN服务。我们认为，攻击者使用此VPN服务来测试其水坑攻击的部署。它还为我们提供了一个验证水坑攻击的机会，通过使用相同的VPN服务来成功接收恶意脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuNB0ADPzJ6TZuNsHwDcZn94nTOibjbTAkfqYiaqaDoGjhUBw62vukUS6g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

原始页面（左侧）和带有注入脚本的页面（右侧）之间的网页内容比较

该网站加载带有以下重定向代码的恶意JavaScript（popup.js）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGu4zGy97iaQibLhxSicVQLmiaDiatK5uYMXXMr074iczZJPJqCoOg7tQbH7icqQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

嵌入式JavaScript重定向到恶意安装程序下载

# **修复安装程序**

安装程序文件是一个MSI安装程序，它封装了另一个NSIS安装程序。攻击者滥用了合法的安装程序(windows.10.codec.pack.v2.1.8.setup.exe - e82e1fb775a0181686ad0d345455451c87033cafde3bd84512b6e617ace3338e)，并将其修复为包含恶意shellcode。该补丁包括增加的部分数量，从5个增加到6个(图5中的红色括号)，并增加图像大小，为恶意shellcode创建额外的空间(图5中的绿色括号)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGucLMUQDicTxhCoHxUFD4Yicev8vttkiaf4pg3nJ51BFvLNXasZxs86LFFw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

原始（上）和修复（下）安装程序，在修复版本中某些参数的大小会增加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGugQgicPsNKmurVFlNMmYZfBy4sb44184XvKsM76s050GYQVwlDyic6ebg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

在修复的安装程序中新添加了.odata部分

修复后的安装程序的入口点被更改为立即跳转到shellcode。shellcode使用简单密钥(XOR 0x01)加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibpkB92TDFlOPRFKM7dEKDj7Fr8Qm3p2gWxiciazju7BJAjmTuFwXaic3wg/640?wx_fmt=jpeg)

修复后的安装程序的入口点跳转到.odata部分的代码中

解密后，shellcode运行几个PowerShell命令来下载恶意软件的其他阶段。这些文件都是可执行文件，从一开始就有几百个字节，使用单字节密钥进行异或。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuW5GRF2l3zmwS3oWHOb2sjOrnZicv5icUibFbEic9keiaBmSmsBhcRFkl3eA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

.odata部分中的Shellcode调用几个PowerShell命令来下载其他加载器

然后，它恢复原始入口点(总共15个字节)，以确保原始安装程序按预期运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibmNEkutdZ8Leu2RkNvkYlltsEjEU5Dp4vyx4licib5WSjVRujLicosrYEw/640?wx_fmt=jpeg)

.odata部分中的Shellcode恢复安装程序的原始入口点

# **下载的二进制文件：加载器**

通过OneDrive持久化的路径（Icon.jpg）

这包含路径\microsoft\onedrive\vcruntime140.dll，这是另一个下载文件（bg.jpg）以vcruntime140.dll的名称释放的位置。

# **持久性和加载器滥用OneDrive侧加载漏洞(Bg.jpg)**

这是vcruntime140.dll (Microsoft C Runtime库)的修复版本。在本例中，函数memset被修复。从函数（retn）返回的值被一个跳转到覆盖（在新添加的.onda部分中）所取代，其中注入的代码从覆盖中读取字节，用一个单字节的密钥对它们进行异或处理，并将嵌入的有效负载注入到werfautl.exe进程中。覆盖层中的shellcode是主后门的加载器。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibFY8XElHkxbqNZJ0YdtT7Yfq5hYia4UZ5N2XDaqfa80gRjvMicJLLETkw/640?wx_fmt=jpeg)

原始memset函数，注意地址0x18000C7D1处的指令返回（retn）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuHicUJIb5icqVo1u7mPBFWicbITbFic8LoXA7GLyLPvMiaMEL1vkOHtjuH4w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

修复的memset函数，注意，地址0x18000C7D1的指令是跳转(jmp)，以覆盖shellcode

该文件被放置在%LOCALAPPDATA%\microsoft\onedrive\目录中，这是onedrive应用程序的默认用户安装位置。此前有报道称，攻击者利用OneDrive侧加载漏洞，将虚假dll放置到该OneDrive目录中，以实现在受攻击计算机中的持久性。

# **持久性和加载程序使用恶意Google Chrome扩展(Favicon.jpg)**

这是一个安装包，包含installer.exe（一个Google Chrome扩展安装程序）、NativeApp.exe（一个本地消息主机）和Chrome扩展文件（background.js、manifest.json和icon.png）。

NativeApp.exe是一个本地消息主机，使用标准输入(stdin)和标准输出(stdout)与Chrome扩展通信。注意扩展清单中的type = " stdio "。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibyRZjHCBde60OEgy25713L7f9U4OicibYM7UDlXJ7klcyhVMwaEBKsNrw/640?wx_fmt=jpeg)

扩展清单，请注意扩展ID (allowed\_origins)路径导致被释放的可执行文件和type =标准输入/输出

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibjBRGjQibYV4EtIYm6WnOc0PEaUfBZJKxBVPG3ohJIzicsOD9wPxcmGWg/640?wx_fmt=jpeg)

在Google Chrome扩展选项卡中查看的恶意扩展

Background.js扩展脚本向onStartup消息添加一个监听器。该侦听器将“inject”命令发送到本机消息传递主机，有效地充当某种独特的持久性方法，因为恶意有效负载在每次Chrome浏览器启动时都会执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuceQ9TL2tTt5EgBOHaEicftNXeWHiaZia8Z9b6icGIC6F7m8LTO22eDFd6A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

onStartup事件的处理程序（Chrome浏览器的启动）

NativeApp使用JSON格式的消息与Chrome扩展交换数据，并实现三个命令：execute、load和inject。

消息的格式如下：xx xx xx xx {“cmd”:””,”data”:””}，其中 xx xx xx xx是以字节为单位的消息长度。“cmd”项必须包含一个已实现的命令值（execute、load和inject），而“data”项可能包含其他参数，如路径和要执行的程序。

以下是有效JSON消息的示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibwCvPrx1K9NH0PVzl8OGOCkgEHicFvccJbU7Rb2TIGn33FsN5Ysltbwg/640?wx_fmt=jpeg)

注意，每个消息的前面必须有一个4字节的小端序长度值。传递不可打印字符(0x00，如下图所示)可以通过使用PowerShell及其Get-Content cmdlet和-raw参数实现，然后通过管道“|”将该内容重定向到NativeApp。如果cmd.bin文件包含如下图所示的相同内容，NativeApp.exe将运行notepad.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icP4v3hMwmb4NlEx1gqGRGuodRpV50szibCI7Pz6WNjibS0p5OwpRnB3tdQOoKiaagK12NIoKgLElX7w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

指示执行notepad.exe的消息，第一个DWORD 0x0000003f是以下JSON消息的长度

在当前实现中，inject命令没有参数。相反，它连接到硬编码的URL地址http://

主后门加载器（Help.jpg）

这是一个shellcode，加载另一个嵌入式可执行文件——我们命名为WhiskerSpy的主后门负载。

主有效载荷：WhiskerSpy

WhiskerSpy使用椭圆曲线密码（ECC）在客户端和服务器之间交换加密密钥。以下是已实现的后门命令：

交互式shell；

下载文件；

上传文件；

删除文件；

列表文件；

截图；

加载可执行文件并调用其导出；

向进程中注入shellcode；

设备ID被计算为位于系统管理生物系统（SMBIOS）的系统信息表中的16字节UUID的32位Fowler-Noll-Vo 哈希（FNV-1）。有关UUID值的更多详细信息，请参阅SMBIOS规范第33页。使用参数“RSMB”调用函数GetSystemFirmwareTable以检索原始SMBIOS表，然后对其进行解析以定位16字节UUID，该UUID已计算其FNV-1哈希。

对于与命令和控制（C&C）服务器的通信，后门生成一个随机的16字节AES密钥。它根据该密钥计算会话ID，作为32位Murmur3哈希。

如上所述，后门使用椭圆曲线密码（ECC）。我们可以从“.data”部分中存储的硬编码值确定椭圆曲线域参数。在下图中，你可以看到素数（p，黄色）、第一个系数a（红色）、第二个系数b（绿色）、生成器（基点，蓝色）和辅因子（h，橙色）。了解这些参数有助于我们确定“secp256r1”是所使用的曲线，因为我们可以看到列出的大多数常用椭圆曲线的所有重要常数，例如在tinyec项目中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibPOSYInK6dHUWibNMPATwW52MDIYObabpZIsvy3h0dMPa7yibEYTVniaAw/640?wx_fmt=jpeg)

“secp256r1”曲线的硬编码参数

上图还显示了一个值（棕色），它表示硬编码服务器的公钥。

然后进行一系列计算（椭圆曲线Diffie–Hellman或ECDH密钥交换）：

生成随机32字节客户端私钥（clientPrivKey）；

通过将客户端私钥乘以曲线生成器来计算客户端公钥(clientPubKey = clientPrivKey \* curve.g)；

通过将客户端私钥乘以服务器公钥来计算sharedKey(sharedKey = clientPrivKey \* serverPubKey)；

这些计算的结果作为一个64字节二进制blob上传到C&C服务器，其中前32个字节是客户端公钥的x坐标，因为常用的共享函数f(P)是取点P的x坐标。后32个字节来自一个随机的16字节AES密钥。

C&C通信首先注册设备ID(函数号= 3;POST请求“l

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibymia71N2Vfn8wOcwd6VGvcfCrmMTrAXiblmPUIgNJWnShDuK4iaqhzSWw/640?wx_fmt=jpeg)

注册新计算机

随后上传带有客户端公钥的x坐标和加密的AES密钥的64字节文件(函数号= 1;POST请求:l

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibicP1z67AB3DImLRItkYTSibtH6tNEjJRW2mQQuftIzdH2wmaqxHmUCcw/640?wx_fmt=jpeg)

注册一个新的会话密钥并上传

然后，WhiskerSpy定期向C&C服务器请求其应执行的任何任务（函数号= 2;POST请求“h

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibJSFN48XSFPPQvb2zaavVpOicNvM4Ybx9WQ2UzgytBc4BR3m0PymicEwg/640?wx_fmt=jpeg)

WhiskerSpy请求执行任务

接收的数据包（文件h

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvp1kb8csp4dzCrpVPOgZRibMuqPjicoHB9Qd8TCiacTeHJE4gicuSGAKYqtqFOhDGml9PTgC33g1x9HQ/640?wx_fmt=jpeg)

特殊类型的消息

Whiske...