---
title: 新型Remcos RAT变种通过Excel文件攻击Windows用户
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492404&idx=1&sn=cc3ea2b75d8c9a39d4d5f2c4089bc81b&chksm=e90dc91ede7a400863918af2ac712b1ecca14e5827cba19ac6b647772d0420d7b2b74c7223c6&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-11
fetch_date: 2025-10-06T19:16:18.295023
---

# 新型Remcos RAT变种通过Excel文件攻击Windows用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型Remcos RAT变种通过Excel文件攻击Windows用户

BaizeSec

白泽安全实验室

**一、事件概述**

近期，Fortinet的研究人员揭露了一个针对Windows用户的新型网络攻击钓鱼活动，该活动通过恶意Excel文件传播Remcos RAT（远程访问木马）的新变种。Remcos是一种在线销售的商业RAT（远程管理工具），它为购买者提供广泛的高级功能，以远程控制属于买家的计算机，对用户的数据安全和隐私构成严重威胁。Remcos RAT因其高级功能而被网络犯罪分子所青睐，包括数据窃取、远程执行、键盘记录、屏幕截图、音频记录等。

此次网络攻击钓鱼活动特别值得关注，因为它不仅展示了攻击者如何利用社会工程学技巧和已知漏洞（如CVE-2017-0199）来诱骗受害者，还体现了他们如何利用复杂的技术手段来规避安全检测和分析。攻击者通过精心设计的网络攻击钓鱼邮件，伪装成订单通知，诱使受害者打开附件中的恶意Excel文档。一旦文档被打开，攻击链就会触发，利用CVE-2017-0199漏洞下载并执行一个HTML应用程序（HTA）文件，该文件进一步下载并部署Remcos RAT。

Remcos RAT的传播和执行过程涉及多个阶段，包括利用多个脚本语言和编码方法来混淆恶意代码，以及采用高级的反分析技术来对抗安全研究人员的分析。这些技术包括向量异常处理、API哈希值匹配、调试器检测和进程挖空等。这些复杂的技术手段使得Remcos RAT能够在受害者的计算机上悄无声息地运行，同时难以被传统的安全解决方案检测到。

此外，Remcos RAT还能够与远程的C&C服务器通信，接收来自攻击者的命令，执行各种恶意行为，如信息收集、文件操作、远程执行等。这种远程控制能力使得攻击者能够对受害者的计算机进行完全的控制，从而可能导致敏感数据的泄露、网络资源的滥用，甚至可能被用作进一步网络攻击的跳板。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINFiagehEmjExic6pHFnzQcCp8ZTbJRhIcXjDkfQFE5AEMdDsaWtic5tf3NYgfZdHzmAMGzGE7maAvWw/640?wx_fmt=png&from=appmsg)图 1 网络攻击钓鱼活动的整个工作流程

**二、网络攻击技术分析过程**

**1. 初始感染：网络钓鱼邮件**

攻击活动以伪装成订单通知的网络钓鱼邮件开始，邮件中包含一个OLE Excel文档。受害者一旦打开附件中的恶意Excel文档，就会触发CVE-2017-0199漏洞，下载并执行一个HTML应用程序（HTA）文件。

**2. 漏洞利用与HTA文件执行**

CVE-2017-0199漏洞存在于Microsoft Office处理OLE对象的方式中。OLE（对象链接和嵌入）是一种技术，允许在文档中嵌入或链接到其他类型的文件，如图像、视频或程序。这个漏洞特别与OLE对象的自动链接功能有关，该功能允许文档中的OLE对象链接到外部文件。攻击者可以利用这个漏洞，通过在RTF（富文本格式）或OLE文件中插入恶意代码来执行远程代码。当受害者打开或预览这些特制文件时，恶意代码会被触发，允许攻击者在受害者的计算机上执行任意代码。本攻击活动中的这个HTA文件包含多层混淆代码，使用JavaScript、VBScript、Base64编码、URL编码和PowerShell等多种脚本编写，负责传递主要的有效载荷。

**3. 下载与执行恶意程序**

恶意HTA文件随后下载一个恶意可执行文件（dllhost.exe），并通过32位PowerShell进程执行，以提取和部署Remcos RAT。恶意软件会修改系统注册表，以便在系统启动时自动启动，确保其持续性。

**4. C&C服务器通信**

Remcos连接到C&C服务器，并发送包含受感染系统关于系统、用户、网络和版本信息的注册包，接收信息收集、文件操作、远程执行、键盘记录、屏幕录制和网络摄像头捕获等命令。

**5. 持久性机制与反分析技术**

这个新变种采用了多种持久性机制，包括高级反分析技术，如向量异常处理。它创建自定义异常处理程序来拦截/处理执行异常，阻止单步执行等调试技术。Remcos不直接存储API名称，而是使用哈希值来识别API，通过匹配哈希值从进程环境块（PEB）中提取地址，这使得静态分析更具挑战性。它还通过检查调试寄存器（DR0至DR7）、监控调试器常用的API调用，并使用ZwSetInformationThread() API隐藏当前线程以检测调试器的存在。此外，它使用ZwQueryInformationProcess() API检测是否有调试器附加到进程，并采取规避行动。

**6. 进程挖空技术**

进程挖空是它用来逃避检测的另一种技术。研究人员发现，恶意软件会暂停了一个新创建的合法进程（Vaccinerende.exe），将其代码注入到内存中，然后恢复它，使其成为一个持久的威胁。

参考链接：

https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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