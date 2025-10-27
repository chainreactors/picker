---
title: 黑客攻击揭秘：探究APT37如何借助LNK文件大肆传播RokRAT
url: https://www.secpulse.com/archives/200175.html
source: 安全脉搏
date: 2023-05-11
fetch_date: 2025-10-04T11:36:56.886716
---

# 黑客攻击揭秘：探究APT37如何借助LNK文件大肆传播RokRAT

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 黑客攻击揭秘：探究APT37如何借助LNK文件大肆传播RokRAT

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-10

24,493

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686689.jpeg)

********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：https://mp.weixin.qq.com/s/I0\_MkneXT9wqLz37xe9I9A********

转载来源：http://www.myzaker.com/article/6459c5c6b15ec03db53bcd88

翻译原文：https://research.checkpoint.com/2023/chain-reaction-rokrats-missing-link/

本文是 Check Point 根据其 2022 年 7 月首次发现的一个 RokRAT 样本来做的深入分析。

早在 2022 年 7 月，APT37（Inky Squid、RedEyes、Reaper 或 ScarCruft）就开始试验使用超大 LNK 文件传播 RokRAT 活动，企图利用不受信任来源的宏发起攻击，巧的是，同月微软开始默认阻止跨 Office 文档的宏。与以前一样，攻击的目标还是韩国的目标。

研究结果表明，用于最终加载 ROKRAT 的各种多阶段感染链被用于其他攻击，导致传播与同一攻击者相关的其他工具。这些工具包括另一个自定义后门，GOLDBACKDOOR 和 Amadey。

在前几年，ROKRAT 感染链通常涉及带有漏洞的恶意朝鲜文字处理器（HWP，韩国流行的文档格式）文档或带有宏的 Microsoft Word 文档。虽然一些 ROKRAT 样本仍然使用这些技术，但传播方式上还是进行了改进，即使用伪装成合法文档的 LNK 文件传播 ROKRAT。这种转变并不是 ROKRAT 独有的，而是代表了 2022 年非常流行的更大趋势。

**ROKRAT 的背景介绍**

Talos 于 2017 年 4 月首次报道了 APT37 开发的 ROKRAT（也称为 DOGCALL），这个工具被用来针对韩国的政府部门，记者、活动人士和脱北者。根据最初的报告，其中一个 ROKRAT 样本使用 Twitter 作为其命令和控制（C&C）基础设施，而另一个则依赖于 Yandex 和 Mediafire。后一个更接近于如今 ROKRAT 的活动方式，依赖云文件存储服务作为一种 C&C 机制。

最初只支持 Windows，多年来 ROKRAT 已经适应了其他平台，在野外发现了 macOS 和 Android 版本。macOS 版本，也称为 CloudMensis，于 2022 年 7 月由 ESET 首次描述。虽然 Android 版本的 ROKRAT 已经存在了很长时间，但 InterLab 和 S2W 都在 Android 上推出了一个更新版本的 ROKRAT，称为 RambleOn（Cumulus）。所有这些都表明，这种恶意软件仍在迭代中。

APT37 的许多工具都是自定义编写的工具，如 ROKRAT，包括（但不限于）最近报道的 M2RAT、Konni RAT、Chinotto 和 GOLDBACKDOOR。然而，攻击者也会使用 Amadey 等普通恶意软件。使用普通恶意软件使得将攻击归因于特定组织变得更加困难，因为它广泛可用，任何人都可以获得它。

今年 2 月，AhnLab 报告了一种名为 Map2RAT（简称 M2RAT）的新 RAT。这种 RAT 利用隐写术技巧，将可执行文件隐藏在 JPEG 文件中以逃避检测。今年 3 月，Sekoia 和 ZScaler 都发布了 APT37 使用钓鱼网站和 PowerShell 后门的报告，ZScaler 导致了另一个名为 Chinotto 的植入程序的传播。

**诱饵和感染链**

在过去的四个月里，我们观察到多个感染链导致了 ROKRAT 的传播。在大多数情况下，LNK 文件会启动攻击，尽管在少数情况下，DOC 文件被用于相同的目的（以前的 ROKRAT 攻击中的方法）。在分析 ROKRAT 感染链的过程中，研究人员发现了导致 Amadey 传播的攻击链，Amadey 是一种在地下论坛上出售的商业 RAT。尽管攻击的性质不同，但研究人员认为所有这些攻击都是由相同的攻击者策划的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686691.jpeg)

诱饵和感染链的时间线

**诱饵 LNK 感染链**

2022 年 4 月，Stairwell 发表了对 GOLDBACKDOOR 的详细分析，这是一种针对韩国记者的有针对性攻击中使用的恶意软件。Stairwell 对利用运行 PowerShell 的大型 LNK 文件的感染链进行了彻底分析，导致在释放诱饵文档的同时执行新发现的恶意软件。这项技术是一个名为 EmbeddExeLnk 的公共工具的独特实现。

虽然最初与 GOLDBACKDOOR 有关，但对最近与 APT37 相关的诱饵的分析表明，这种技术已经成为一种重要的方法，用于传播与同一攻击者相关的另一种工具，即 ROKRAT。ROKRAT 和 GOLDBACKDOOR 加载机制的实现非常相似，只有在检索有效负载时才能区分。

在过去的几个月里，研究人员能够利用 ZIP 和 ISO 档案中提供的这种独特实现来识别多个诱饵。只有其中一些诱饵被证实会导致 ROKRAT 的传播。所有的诱饵都以韩国国内外事务为主题。

**LNK 感染链分析**

目前已知的所有 LNK 都会导致几乎相同的感染链。下面以 " 利比亚项目 " 中描述的一个感染为例进行说明：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-16836866911.jpeg)

" 利比亚项目 " 诱饵的感染链

点击恶意 LNK 文件会触发 PowerShell 的执行，并启动以下感染链：

1.PowerShell 从 LNK 中提取文档文件，将其放入磁盘，然后打开它。这个文件是一个诱饵，欺骗用户以为他们只是打开了一个普通的 PDF 或 HWP 文件。

2.PowerShell 从 LNK 中提取 BAT 脚本，将其放入磁盘并执行。

3.BAT 脚本执行一个新的 PowerShell 实例，该实例从 OneDrive 下载有效负载，通过将有效负载的第一个字节作为密钥对其进行解码，并将其与有效负载的其余部分进行异或。

4. 生成的有效负载以反射方式注入 PowerShell，使其作为新线程运行。

5.shellcode 使用四字节异或密钥对有效负载的 ROKRAT 部分进行解码并执行它。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686693.jpeg)

**典型的 ROKRAT 感染链**

ROKRAT 运营商在采取新的行为同时，仍夹杂了一些旧习惯，比如，ROKRAT 仍然使用恶意 Word 文档进行部署。

2022 年 12 月，有人向 VirusTotal 提交了一份恶意的 Word 文档，命名为 ".doc"（Case fee\_Payment request.doc）。该文件本身包含一个输入个人和银行信息的简短表格。然而，对该文件的仔细检查显示，其中提到了韩国的统一部。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686694.jpeg)

一旦用户打开恶意文档并允许宏执行，就会触发以下感染链：

1. 宏通过设置 AccessVBOM 注册表项以加载其他代码来检查并确保它可以访问 Visual Basic 项目。

2. 宏解码一个新的 VBA 脚本，将其写入宏中的一个新模块，然后执行它。这是在不将任何代码释放到磁盘的情况下完成的。

3. 第二个 VBA 脚本运行 notepad.exe 并将 shellcode 注入其中。

4.shellcode 在 notepad.exe 中运行，并进入 OneDrive 下载 ROKRAT 有效负载并在内存中执行它。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-16836866941.jpeg)

这里描述的感染链与 MalwareBytes 在 2021 年 1 月报告的非常相似，MalwareBytes 也通过将 shellcode 注入 notepad.exe 并将 RAT 加载到内存中来传播 ROKRAT。然而，MalwareBytes 研究中描述的样本的编译日期是从 2019 年开始的，而 checkpoint 发现的新 ROKRAT 样本似乎是在 2022 年 12 月 21 日编译的，距离文件提交给 VirusTotal 只有六天时间。

此外，在 2023 年 4 月发现的另一个文件似乎是同一感染链的一部分，只是这次注入的目标进程是 mspaint.exe，该文件以朝鲜的核武器为主题。不幸的是，在我们进行分析时，URL 不再响应下载负载的请求。但是，这份文件很有可能也是为了传播 ROKRAT。

**与 Amadey 的关联**

2022 年 11 月初，一个名为 securityMail.zip 的文件被提交给了 VirusTotal。这个 ZIP 包含两个 LNK，它们的大小都不到 5MB，令人怀疑。PowerShell 命令在两个 LNK 中的实现是唯一的，并且仅与 ROKRAT 和 GOLDBACKDOOR LNK 感染重叠。然而，这个特定的感染链最终传播了 Amadey，这是一种可在网络犯罪论坛上出售的恶意软件。Amadey 过去曾被认为是 Konni 开发的，Konni 组织与 APT37 的背景类似。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686695.jpeg)

" 安全邮件 " 诱饵的感染链，打开这些 LNK 中的任何一个都会产生恶意流程：

1.PowerShell 命令从 LNK 中提取一个诱饵 HTML 文件，并将其放入磁盘，其方式与 ROKRAT 感染链类似：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686696.jpeg)

2. 这个 PowerShell 还从包含 DLL 的 LNK 中提取一个 ZIP 文件。然后将 DLL 作为 mfc100.dll 放入磁盘。

3.PowerShell 最终也从 LNK 中提取了一个 BAT 脚本，将其放到磁盘上并执行。

4.BAT 脚本运行带有 rundll32.exe 的 DLL 并删除自身。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686699.jpeg)

对 DLL 文件的初步分析显示，它包含了商业代码保护解决方案 Themida。在分析了它执行的内存转储后，我们能够确认这实际上是 Amadey。诱饵 HTML 文件中包含一个伪造的 Kakao 银行的登录页面，Kakao 是韩国一家受欢迎的银行。对 HTML 的进一步分析表明，它不是用于密码钓鱼，而是用来隐藏攻击者的意图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200175-1683686700.jpeg)

伪造 Kakao 银行登录页面

**ROKRAT 技术分析**

ROKRAT 只是 APT37 使用的许多自定义工具之一，但它绝对是通用且强大的。ROKRAT 主要侧重于运行额外的有效负载和大量的数据窃取。它的 C&C 功能依赖于云基础设施，包括 DropBox、pCloud、Yandex cloud 和 OneDrive。ROKRAT 还收集有关计算机的信息，以防止被其他竞争者再次感染。

虽然在过去几年中，ROKRAT 并没有发生重大变化，但其破坏力依然不容小觑，这可以归因于它巧妙地使用...