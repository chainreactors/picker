---
title: [系统安全] 四十七.恶意软件分析 (4)Cape沙箱批量提取动态API特征
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247498025&idx=1&sn=5d97c115b4ab670be999638da5915adc&chksm=cfcf49e4f8b8c0f24e5a37e375302748665292dfa7411618102dafc82f8c9c4c8c2f921fe5cb&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2023-03-27
fetch_date: 2025-10-04T10:46:58.693628
---

# [系统安全] 四十七.恶意软件分析 (4)Cape沙箱批量提取动态API特征

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKQo8pVYpP5sFaTFeEsy6fUW06icIUjB3pjFNZaOcIj5eDLHOdbgdqmUg/0?wx_fmt=jpeg)

# [系统安全] 四十七.恶意软件分析 (4)Cape沙箱批量提取动态API特征

原创

eastmount

娜璋AI安全之家

最近真的太忙了，天天打仗一样，感谢大家的支持和关注，稍微松口气分享几篇博客，继续加油！该系列文章将系统整理和深入学习系统安全、逆向分析和恶意代码检测，文章会更加聚焦，更加系统，更加深入，也是作者的慢慢成长史。漫漫长征路，偏向虎山行。享受过程，一起奋斗~

**前文详细介绍恶意代码静态分析经典工具Capa的基础用法，以及批量提取静态特征和ATT&CK技战术，主要是从提取的静态特征Json文件中提取关键特征。这篇文章将详细讲解动态分析沙箱Cape，其是一个开源的自动恶意软件分析系统，通过自动运行和分析恶意软件，全面分析和提取恶意软件的关键特征。本文先介绍Cape沙箱的安装和基础用法，后续随着深入再分享。基础性文章，希望对您有帮助，如果存在错误或不足之处，还请海涵。且看且珍惜！**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMA9s1oJIEgJ8QTOwtVkLHOPE8CfKwSiaScua0dGx0c0TpWcZRVHbyBh8SG4x1cd3M4lvFyoicu5mwA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

文章目录：

* **一.恶意软件分析**

+ 1.静态特征
+ 2.动态特征

* ****二.Cuckoo和Cape沙箱简介****

+ 1.Cuckoo沙箱简介
+ 2.Cape沙箱简介
+ 3.Cape原理

* ******三.Cape沙箱识别单样本特征******

+ 1.启动沙箱关键步骤
+ 2.样本分析

* ****四.Cape沙箱批量分析恶意软件****

+ 1.Python脚本批量分析样本
+ 2.运行结果
+ 3.Submit an Analysis
+ 4.Python Functions

* ****五.**总结******

作者的github资源：

* 逆向分析：

+ https://github.com/eastmountyxz/

  SystemSecurity-ReverseAnalysis

* 网络安全：

+ https://github.com/eastmountyxz/
+ NetworkSecuritySelf-study

作者作为网络安全的小白，分享一些自学基础教程给大家，主要是关于安全工具和实践操作的在线笔记，希望您们喜欢。同时，更希望您能与我一起操作和进步，后续将深入学习网络安全和系统安全知识并分享相关实验。总之，希望该系列文章对博友有所帮助，写文不易，大神们不喜勿喷，谢谢！如果文章对您有帮助，将是我创作的最大动力，点赞、评论、私聊均可，一起加油喔！

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROZ0FiaQhr7u82U6dJibrM3VO0dUcD3EMLylohBICfH8ibt9D8T7r2jcvDCAFuf4VR5IhcypN5mvCSVg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

> 声明：本人坚决反对利用教学方法进行犯罪的行为，一切犯罪行为必将受到严惩，绿色网络需要我们共同维护，更推荐大家了解它们背后的原理，更好地进行防护。（参考文献见后）

# 一.恶意软件分析

恶意软件或恶意代码分析通常包括静态分析和动态分析。特征种类如果按照恶意代码是否在用户环境或仿真环境中运行，可以划分为静态特征和动态特征。

那么，如何提取恶意软件的静态特征或动态特征呢？ 因此，第一部分将简要介绍静态特征和动态特征。

## 1.静态特征

没有真实运行的特征，通常包括：

* 字节码

  二进制代码转换成了字节码，比较原始的一种特征，没有进行任何处理
* IAT表

  PE结构中比较重要的部分，声明了一些函数及所在位置，便于程序执行时导入，表和功能比较相关
* Android权限表

  如果你的APP声明了一些功能用不到的权限，可能存在恶意目的，如手机信息
* 可打印字符

  将二进制代码转换为ASCII码，进行相关统计
* IDA反汇编跳转块

  IDA工具调试时的跳转块，对其进行处理作为序列数据或图数据
* 常用API函数
* 恶意软件图像化

静态特征提取方式：

* CAPA
  – https://github.com/mandiant/capa
* IDA Pro
* 安全厂商沙箱

---

## 2.动态特征

相当于静态特征更耗时，它要真正去执行代码。通常包括：
– API调用关系：比较明显的特征，调用了哪些API，表述对应的功能
– 控制流图：软件工程中比较常用，机器学习将其表示成向量，从而进行分类
– 数据流图：软件工程中比较常用，机器学习将其表示成向量，从而进行分类

动态特征提取方式：

* Cuckoo
  – https://github.com/cuckoosandbox/cuckoo
* CAPE
  – https://github.com/kevoreilly/CAPEv2
  – https://capev2.readthedocs.io/en/latest/
* 安全厂商沙箱

---

# 二.Cuckoo和Cape沙箱简介

## 1.Cuckoo沙箱简介

Cuckoo Sandbox 是一个开源的自动恶意软件分析系统，并且是经典的沙箱分析工具。Cuckoo沙箱将在几秒钟内为您提供一些详细的分析结果，概述该文件在隔离环境中执行时的情况。不像在线VirusTotal、VirusShare、微步、AnyRun、Hybrid等在线沙箱，Cuckoo可以实现本地安装和离地分析，其定制化和可控程度更高。

* https://github.com/cuckoosandbox/cuckoo

Cuckoo Sandbox始于2010年蜜网计划中的谷歌Summer of Code项目，它最初是由Claudio“nex”Guarnieri设计和开发的。在2010年夏天开启该工作之后，第一个测试版于2011年2月5日发布，这是Cuckoo第一次公开发布。2011年3月，在谷歌Code Summer of 2011期间，Cuckoo再次被选为蜜网项目的支持项目，在此期间Dario Fernandes加入了该项目并扩展了其功能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKvCnccErQeZd15yz06eqzia53lg2EUAnHQakfTjm4Rxxoic724iaR2ibzyw/640?wx_fmt=jpeg)

> Cuckoo Sandbox started as a Google Summer of Code project in 2010 within The Honeynet Project. It was originally designed and developed by Claudio “nex” Guarnieri, who is still the main developer and coordinates all efforts from joined developers and contributors.

---

## 2.Cape沙箱简介

CAPE Sandbox 是一款用于自动分析可疑文件或恶意软件的开源系统，它使用自定义组件来监视在隔离环境中运行的恶意进程的行为。CAPE来源于Cuckoo Sandbox，目的是添加自动恶意软件解包和配置提取——因此它的名字是一个缩写“配置和有效载荷提取（`Config And Payload Extraction`）”。自动解包允许基于Yara签名的分类，以补充网络(Suricata)和行为(API)签名。于2016年诞生。

* https://github.com/kevoreilly/CAPEv2
* https://capesandbox.com

> CAPE Sandbox is an Open Source software for automating analysis of suspicious files. To do so it makes use of custom components that monitor the behavior of the malicious processes while running in an isolated environment.

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKDDzzgUChHKSUUyXHcICrXjfUoawtpL47ItwfCRns72IB5X7IWcUz6Q/640?wx_fmt=jpeg)

CAPE被用来自动运行和分析文件，并收集全面的分析结果，概述恶意软件在孤立的Windows操作系统中运行时的行为。它可以检测以下类型的结果:

* 由恶意软件生成的所有进程执行的win32 API调用的痕迹。
* 恶意软件在执行过程中创建、删除和下载的文件。
* 恶意软件进程的内存转储。
* PCAP格式的网络流量跟踪。
* 在执行恶意软件期间截取的Windows桌面截图。
* 机器的全内存转储。

由于CAPE的模块化设计，它既可以作为独立的应用程序使用，也可以集成到更大的框架中。它可以用来分析:

* Generic Windows executables
* DLL files
* PDF documents
* Microsoft Office documents
* URLs and HTML files
* PHP scripts
* CPL files
* Visual Basic (VB) scripts
* ZIP files
* Java JAR
* Python files
* Almost anything else

虽然CAPE沙箱的配置和有效载荷提取是最初声明的目标，但CAPE调试器的首要目标是：为了从任意恶意软件家族中提取配置文件或解压缩有效负载，而不依赖进程转储（迟早会被坏人破坏），指令级别的监视和控制是必要的。CAPE中的新调试器遵循最大化使用处理器硬件和最小化使用Windows调试接口的原则，允许通过Yara签名或API调用在引爆期间以编程方式设置硬件断点，从入口点偷偷地检测和操纵恶意软件。这允许捕获指令跟踪，或执行操作，如控制流操作或转储内存区域。

调试器允许CAPE在其原始功能之外继续发展，这些功能现在包括了动态反规避绕过。由于现代恶意软件通常试图在沙箱中逃避分析，例如通过使用定时陷阱来进行虚拟化或API钩子检测，CAPE允许开发动态对策，结合调试器在Yara签名中的动作，来检测隐藏的恶意软件，并执行控制流程操作，迫使样品完全引爆或跳过规避动作。CAPE的动态旁路越来越多，其中包括:

* Guloader
* Ursnif
* Dridex
* Zloader
* Formbook
* BuerLoader
* Pafish

CAPE利用了许多恶意软件技术或行为，允许未打包的有效载荷捕获，这些行为将导致捕获注入、提取或解压缩的有效载荷，以便进一步分析。此外，CAPE自动为每个进程创建一个进程转储，或者在DLL的情况下，为内存中的DLL模块映像创建一个进程转储。

推荐读者学习官方文档：

* https://capev2.readthedocs.io/en/latest/
* https://capev2.readthedocs.io/en/latest/usage/submit.html

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKovT3HdaujtjZRI6y9C1zHgYa5MdGAETt8ujcIIvSOxI2tg4xelGQog/640?wx_fmt=png)

---

## 3.Cape原理

CAPE Sandbox由处理样本执行和分析的中央管理软件组成。每个分析都在一个全新的、孤立的虚拟机中启动。CAPE的基础结构由一台主机（管理软件）和一些Guest机器（用于分析的虚拟机）组成。主机Host运行管理整个分析过程的沙盒核心组件，而Guest是安全执行和分析恶意软件样本的隔离环境。

CAPE的主要架构如下图所示：

* 推荐的设置是GNU/Linux (Ubuntu LTS最好)作为主机，Windows 7作为客户。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKgdAPqgnYj4CibIvgdVmxTvSzNwibITablh4mr5a82l49XTJFiayZIFWNw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKcXS3dzWEuc5gaNFlPOCjHPtbFt3rRjPShiaeBXv8ibQaN2AYj0t678UA/640?wx_fmt=png)

---

# 三.Cape沙箱识别单样本特征

## 1.启动沙箱关键步骤

第一步，安装VMware虚拟机并载入Cape环境镜像。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BK0RevHFgTVde7WEBibibSCWw8B0jZjjvic8J5TFxtTdpt4FO3ZKCkkloRg/640?wx_fmt=png)

第二步，按照四个关键步骤启动Cape沙箱。

* （1）在任意文件夹中运行"sudo virtualbox"，现在已经安装了一个Win7 X64专业版虚拟机。
* （2）进入/opt/CAPEv2/文件夹，运行"sudo python3 cuckoo.py"。
* （3） 在/opt/CAPEv2/文件夹下运行"sudo python3 utils/process.py -p7 auto"，参数代表优先级划分，输入多个样本时，沙箱会优先运行高优先级样本。
* （4）在/opt/CAPEv2/web目录下(由于环境依赖的问题，必须由指向该文件夹的shell运行该命令)，运行"sudo python3 manage.py runserver 127.0.0.1:8088"(该虚拟机的8080端口已被占用，端口可自己指定)。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKbG0hiaFwpwE0vat0icSbc9ialxGEXcPhP6rKJn78j1hQgEMS4u95UIkNA/640?wx_fmt=png)

---

## 2.样本分析

在虚拟机的火狐中打开127.0.0.1:8088，在submit页面提交样本即可。

> 再次强调
> 在恶意软件分析中，一定要做好本机保护，包括在虚拟机隔离环境中进行分析，甚至需要断网防止沙箱逃逸。同时，本人坚决反对渗透和破坏行为，一切犯罪行为必将受到严惩，绿色网络需要我们共同维护。这里仅是分享恶意软件分析背后的原理，更好地进行防护。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BK3T1dDR3yxWMDrcvHw6MRor8ich2Qkc2DoOX9tia02Y8YECmUibxfic5NWQ/640?wx_fmt=png)

运行结如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKibHAz0siaKMATRxAYXp7yZ7FykzABZibdcRR0JRUjoPWWhRaT7afZTAtg/640?wx_fmt=png)

点击控制面板的“Recent”查看分析结果。由图可知，本文分析的结果已产生，同时有之前提交的两个样本。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BK7bG7BjSyENquFA0St9opzoUoTQphdMzmtMaKOEXowvoswkXb3s4ibxw/640?wx_fmt=png)

对应的分析结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKM00wPbB4vJicqAwxP8wtsxvoQO31icfMiccB5lp9Dic6y6Txic64Z3z96iaA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKiajMCO0WpIUApEPQjkLEw0boVzhDNjXVvZJZqTRsyDhprlkhicKt5aFg/640?wx_fmt=png)

此时会遇到一个问题：在做恶意软件分析过程中，通常会遇到大量的恶意软件。如果手动添加其过程极其繁琐并且耗时，如何解决该问题呢？

---

# 四.Cape沙箱批量分析恶意软件

在Cape沙箱中，已经集成对应的批量分析的Python脚本，通过调用脚本来指定要分析的恶意软件既可以实现批量分析。具体分析过程如下：

## 1.Python脚本批量分析样本

该方法通过提供的submit.py命令实现，该文件位置为：

* /opt/CAPEv2/utils/submit.py

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BK3QlcAVW6dicUw6wPzfOlxiaysiahsOnqEXaP0TqVNicKC2gibdbe7IO0r7A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPgNXPC1GBUhKic0AGH6s6BKwbYZmkb...