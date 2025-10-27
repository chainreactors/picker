---
title: ESET发现了BlackLotus恶意软件：首个可在 Win11上绕过Secure Boot的UEFI bootkit（三）
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559413&idx=2&sn=2d834bd9eecb9881544fe7607434d9d7&chksm=e91438cfde63b1d9c260b1aafa167db92883af8ab6659736775efccfca48cda6c4d188ab168c&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-04-01
fetch_date: 2025-10-04T11:24:31.100108
---

# ESET发现了BlackLotus恶意软件：首个可在 Win11上绕过Secure Boot的UEFI bootkit（三）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPWsZeibHyjld1q7s2rxBFaJvh3xqVImQDFYuWp7S898ysDVJOMs8uPbA/0?wx_fmt=jpeg)

# ESET发现了BlackLotus恶意软件：首个可在 Win11上绕过Secure Boot的UEFI bootkit（三）

luochicun

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)与HTTP下载器的通信

内核驱动程序能够通过使用命名的Event和Section与HTTP下载器通信。所使用的命名对象的名称是根据受害者的网络适配器MAC地址（以太网）生成的。如果一个八位字节的值小于16，那么将向其添加16。生成的对象名称的格式可能在不同的示例中有所不同。例如，在我们分析的一个示例中，对于MAC地址00-1c-0b-cd-ef-34，生成的名称为：

\BaseNamedObjects\101c1b：用于命名部分（仅使用MAC的前三个八位字节）；

\BaseNamedObjects\Z01c1b：用于命名事件，与Section相同，但MAC地址的第一个数字被替换为Z；

如果HTTP下载器想要将一些命令传递给内核驱动程序，它只需要创建一个命名的节，在其中写入一个包含相关数据的命令，并通过创建一个指定事件等待驱动程序处理该命令，直到驱动程序触发（或发出信号）该命令。

驱动程序支持以下一目了然的命令：

安装内核驱动程序；

卸载BlackLotus；

细心的读者可能会注意到这里的BlackLotus弱点，即使bootkit保护其组件不被删除，内核驱动程序也可以通过创建上述命名对象并向其发送卸载命令来完全卸载bootkit。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)HTTP下载器

最后一个组件负责与C&C服务器通信，并执行从其接收的任何C&C命令。我们能够发现的所有有效载荷都包含三个命令。这些命令非常简单，正如部分名称所示，主要是使用各种技术下载和执行额外的有效载荷。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)C&C通信

为了与其C&C通信，HTTP加载器使用HTTPS协议。通信所需的所有信息都直接嵌入到下载器二进制文件中，包括使用的C&C域和HTTP资源路径。与C&C服务器通信的默认间隔设置为一分钟，但可以根据C&C的数据进行更改。与C&C的每个通信会话都从向其发送信标HTTP POST消息开始。在我们分析的示例中，可以在HTTP POST标头中指定以下HTTP资源路径：

/network/API/hpb\_gate[.]php/API/hpb\_gate[.]php/gate[.]php/hpb\_gate[.]php

信标消息数据以checkin=字符串开头，包含有关受攻击机器的基本信息，包括自定义设备标识符（称为HWID）、UEFI Secure Boot状态、各种硬件信息以及一个看起来是BlackLotus内部版本号的值。HWID由设备MAC地址（以太网）和系统卷序列号生成。加密前的消息格式如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPBqCDEPhMmmwPxnxDha1CFg8rJTicejaL3XjPAVpMia9zG46u4zOGricFA/640?wx_fmt=png)

在向C&C发送消息之前，首先使用嵌入的RSA密钥对数据进行加密，然后使用URL安全的base64编码。在分析过程中，我们发现样本中使用了两个不同的RSA密钥。这种HTTP信标请求的示例如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9YfPJZ8tT1QWY99LWiaDBclqmOWiaHXkCicD1SIFBjaO0N0w3UtVz8WlQ/640?wx_fmt=png)

信标HTTP POST消息示例（由VirusTotal中的示例生成——具有本地IP而非真实C&C地址的示例）

作为对信标消息的响应，从C&C接收的数据应以两字节魔法值HP开头；否则，不进一步处理响应。如果魔法值正确，则在CBC模式下使用256位AES对魔法值之后的数据进行解密，并使用上述HWID字符串作为密钥。

解密后，该消息类似于信标，一个JSON格式的字符串，并指定命令标识符（称为Type）和各种附加参数，例如：

C&C通信间隔；

执行方法；

有效负载文件名；

基于文件扩展名的负载类型（支持.sys、.exe或.dll）；

应该用于请求下载有效负载数据的身份验证令牌；

用于解密有效负载数据的AES密钥；

下表列出了所有支持的命令及其说明。

表2：C&C命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPD8pmPIAVb7I8elddEmQh4M9BStPpSWcaE6mVkIZzIRYBwsRSXrS1zQ/640?wx_fmt=png)

在这些命令中，C&C可以指定是在执行负载之前先将其放到磁盘上，还是直接在内存中执行。在将文件放到磁盘的情况下，操作系统卷上的ProgramData文件夹将用作目标文件夹，文件名和扩展名由C&C服务器指定。在直接在内存中执行文件的情况下，svchost.exe用作注入目标。当C&C发送需要内核驱动程序协作的命令时，或者操作员希望以内核模式执行代码时，将使用与HTTP下载器通信部分中描述的机制。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)反分析技巧

为了更难检测和分析这一恶意软件，其开发者试图将标准文件工件（如文本字符串、导入或其他未加密的嵌入数据）的可见性限制在最低限度。以下是所用技术的摘要。

**字符串和数据加密：**

示例中使用的所有字符串都使用简单的密码进行加密；

所有嵌入的文件都在CBC模式下使用256位AES加密；

各文件的加密密钥可能因样本而异；

除AES加密之外，一些文件还使用LZMS进行压缩。

**Runtime-only API解析：**

在所有示例中（如果适用），Windows API总是在运行时进行排他解析，并且使用函数哈希而不是函数名来查找内存中所需的API函数地址；

在某些情况下，直接syscall 指令调用用于调用所需的系统函数；

**网络通信：**

使用HTTPS通信；

HTTP下载器发送到C&C的所有消息都使用嵌入的RSA公钥进行加密；

从C&C发送到HTTP下载器的所有消息都使用来自受害者设备环境的密钥或C&C提供的AES密钥进行加密；

**反调试和反VM技巧：**

如果使用该方法，通常放在入口点的开头，仅使用临时沙盒或调试器检测技巧。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)缓解措施和补救措施

首先，必须保持所使用的系统及其安全产品是最新的；

然后，要防止使用已知的易受攻击UEFI二进制文件绕过UEFI Secure Boot，需要采取的关键步骤是在UEFI取消数据库（dbx）中取消这些二进制文件，在Windows系统上，应使用Windows Update传播dbx更新。

问题是，广泛使用的Windows UEFI二进制文件的取消可能会导致数千个过时的系统、恢复映像或备份无法启动，因此，取消通常需要很长时间。

请注意，BlackLotus使用的Windows应用程序的取消将阻止启动工具包的安装，但由于安装程序将用已取消的启动加载器替换受害者的启动加载器，这可能会使系统无法启动。要在这种情况下进行恢复，重新安装操作系统或仅进行ESP恢复即可解决问题。

如果在设置BlackLotus持久性之后发生取消，则bootkit将保持正常运行，因为它使用具有自定义MOK密钥的合法填充程序进行持久性。在这种情况下，最安全的缓解方案是重新安装Windows，并使用mokutil实用程序删除攻击者注册的MOK密钥（由于在启动过程中需要用户与MOK管理器进行必要的交互，因此执行此操作需要实体存在）。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMP9dQJ1bia6nyNUpoib23icKjbbqIluNuwjFttv3ibiaRgatqrtzz557PF6icw/640?wx_fmt=png)总结

在过去几年中，已经发现了许多影响UEFI系统安全的关键漏洞。不幸的是，由于整个UEFI生态系统的复杂性和相关的供应链问题，即使在漏洞修复后很长一段时间，或者至少在用户被告知它们已修复后，这些漏洞中的许多漏洞仍会使许多系统处于易受攻击状态。下面是一些去年允许UEFI Secure Boot绕过的修复或取消失败的示例：

首先，当然是CVE-2022-21894，这是一个被BlackLotus利用的漏洞。在修复该漏洞一年后，易受攻击的UEFI二进制文件仍然没有被取消，这使得BlackLotus等攻击可以在启用了UEFI Secure Boot的系统上秘密运行。

早在2022年，研究人员就披露了几个允许禁用UEFI Secure Boot的UEFI漏洞。许多受影响的设备不再受到OEM的支持，但在联想消费级笔记本电脑中发现高影响的UEFI漏洞。

在2022年晚些时候，研究人员发现了其他一些UEFI漏洞，这些漏洞也允许攻击者很容易地禁用UEFI Secure Boot。正如Binarly的研究人员指出的那样，在警告发布几个月后，警告中列出的几个设备都没有被修复，或者没有正确地被修复，这使得这些设备容易受到攻击。与前面的情况类似，一些设备将永远处于易受攻击状态，因为它们已经无法更新。在不远的将来，有攻击者会滥用这些漏洞，创建一个能够在启用UEFI Secure Boot的系统上运行的UEFI bootkit。

参考及来源：https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/

相关阅读：

[ESET发现了BlackLotus恶意软件：首个可在Win11上绕过 Secure Boot 的 UEFI bootkit（一）](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247558872&idx=2&sn=f788d2812dd2ccb1a11500a5bffcd86f&chksm=e91436e2de63bff4be5f09d1c43dcc035ee60d5a451ba9aba30851f1f5eacb641675d8ce0f99&scene=21#wechat_redirect)

[ESET发现了BlackLotus恶意软件：首个可在Win11上绕过Secure Boot的UEFI bootkit（二）](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559250&idx=3&sn=191a244c909a64cd8ea4bf9983faef8d&chksm=e9143868de63b17eef77cec8225fedf0b7e29a9ba4c29f1c0c7a5a6e396bf1f5ee39f67b65fb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPnU2MhrhCF0mrypTJPLNYMSZBreJa6rEU1wFAh2pxrFl23L1B7AiaR4A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icgBxPHicPYibnnJcKrJnEHMPZjibEQkItGhIjkhwkiabRqwfSFLibfdJOKloneXgJ4NBUEFnRicoSruxXg/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过