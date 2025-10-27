---
title: Windows App 运行控制机制 Smart App Control 的内部安全架构分析（上）
url: https://www.4hou.com/posts/EQpK
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-28
fetch_date: 2025-10-03T23:54:42.395415
---

# Windows App 运行控制机制 Smart App Control 的内部安全架构分析（上）

Windows App 运行控制机制 Smart App Control 的内部安全架构分析（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows App 运行控制机制 Smart App Control 的内部安全架构分析（上）

luochicun
[技术](https://www.4hou.com/category/technology)
2022-11-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)131914

收藏

导语：本文会详细分析Windows即将推出的最大安全功能——智能应用控制（Smart App Control，SAC）。

本文会详细分析Windows即将推出的最大安全功能——智能应用控制（Smart App Control，SAC）。“智能应用控制”功能是什么，为什么我认为它是 Windows 中最牛的安全功能之一。首先，SAC 会嵌入在操作系统中，启用后将阻止恶意或不受信任的应用程序。这与 AppLocker 非常相似。

在之前一篇文章中，我们看到了SAC是如何启用和初始化的。在本文中，我们将讨论SAC如何执行这些操作。即使SAC是一个新功能，该功能使用的大部分代码也已经在操作系统中了。我的意思是，在22H2之前的版本中，通过使用适当的策略规范，可以获得类似的行为。总之，SAC的最大变化是MS将激活特定的WDAC策略，类似于启用HVCI时，操作系统如何启用Driver Block Rule策略。

需要注意的是，因为我们在这篇文章中看到的很多内容在操作系统中已经存在了很长时间。AppLocker或AppID等功能利用了它。当然，有几个方面只适用于SAC，我一定会注意到这些。从好的方面来看，这篇文章的绝大多数可以推断出其他WDAC策略是如何评估的。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653363171462.png "1665653363171462.png")

**SAC运行**

在本节中，我们将重点关注CI处理来自内核的验证请求所采取的步骤。我们将深入探讨此过程中涉及的主要例程，还将讨论CI使用的一些主要结构。正如我刚才提到的，这些步骤中的大多数并不是SAC独有的，无论启用哪种策略，都将采取这些步骤。如上图所示，我们看到有三个主要的评估来源。据我所知，这些要点与以下功能/策略规范有关，至于是选择使用一个或多个评估取决于策略规范。

OriginClaim (EAs or Token): 托管安装程序、AppLocker、SmartScreen和SAC；

Query 防御措施: Intelligent Security Graph (ISG) & SAC；

Policy FileRules: 通用于所有具有FileRule的策略。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653372634983.png "1665653372634983.png")

在上一篇文章中，我们已经说过全局g\_CiPolicyState具有位NW\_ENABLED，这意味着SAC已启用，SAC策略（强制或评估）处于活动状态，并存储在g\_SiPolicyCtx中。现在，让我们看看CI向内核提供的回调，看看内核的验证方式。以下函数建议执行某种类型的验证：

```
CiValidateImageHeader；
CiValidateImageData；
CiValidateFileAsImageType；
CiRevalidateImage；
```

在本文中，我将只关注CiValidateImageHeader。

**CiValidateImageHeader**

可以说，此函数是大多数CI验证的主要入口点。内核将从MiValidateSectionCreate中引用的SeValidateImageHeader调用此函数。CiValidateImageHeader将处理CI初始化的第2阶段，主要初始化minCrypt、ETW、Lookaside缓冲区等。一旦完成(只有一次)，第一步是获取指定映像（CiGetActionsForImage）行为。此函数将根据诸如Requested SigningLevel之类的内容，或者如果对象来自受保护进程或系统进程，来确定将要进行的验证操作，这些操作是位字段枚举，但我不知道大多数值的含义.

操作进行后，函数就可以开始验证映像了。如果操作变量设置了位0（action\_FILE\_In\_CACHE（0x1）），则CI将尝试获取之前为此FO设置的任何验证数据，并重新验证。

在本文中，我们不会涉及CI缓存及其验证原理。本质上，它将尝试获取内核EA:$Kernel.Purge.CIpCache或$Kernell.Purge.ESBCache（请参阅函数CipGetFileCache）。然后，它会将策略应用于CiApplyPolicyToSyntheticEa内的这些属性。这个例程最终将调用CipApplySiPolicyEx，我们稍后将详细讨论。

如果未设置“file in cache”属性，则会分配用于处理验证的主结构(CipAllocateValidationContext)。此结构用于所有类型的验证，例如，此上下文也用于HVCI验证（请参阅CiHvciSetValidationContextForHvci）。一旦分配了这个上下文，我看到UMCI验证会发生两个操作。

如果设置了位2（ACTION\_PAGE\_HASH（0x4）），验证函数为->CipValidatePageHash；

如果设置了位8（ACTION\_FILE\_HASH（0x100）），验证函数为->CipValidateFileHash。

CipValidateImageHash将接收发生操作的Validation函数作为函数指针。无论传递的是什么函数指针，PageHash还是FileHash，CipValidateImageHash最终都会调用它。在这两个验证函数中，CI都会使用被验证对象的信息更新验证上下文。诸如FileInfo（CipUpdateValidationContextWithFileInfo）、文件版本（CiGetFileResourceInformation）、嵌入签名（CipImageGetCertInfo）或对象哈希（Page CipCalculateHeaderHash或File CipCalpulateImageHash）。有了所有这些信息，代码将通过函数CipApplySiPolicyEx方法继续应用策略。

对于未签名映像的验证，验证函数将返回STATUS\_INVALID\_IMAGE\_HASH，代码将进入CipApplySIPolicyUMCI，最终调用前面提到的CipApply SiPolicyEx。相反，对于签名文件，将从CiVerifyPageHashSignedFile或CiVerify FileHashSingedFile访问此函数。简单说明一下，这两个函数有它们的HVCI对应函数CiHvciXxx。

**CipApplySiPolicyEx**

顾名思义，此函数将把策略应用于正在验证的对象。该函数将首先设置两个结构，然后将其传递给验证引擎。一个结构将保存正在验证的ImageFile的信息，而另一个结构则包含“外部”授权过程所需的信息，我说“外部”授权是因为MS在验证对象的回调函数名中使用了“外部”授权这个词。

这两个结构将存储在Validation Context中，并且实际上都将被来自Validation Context的数据填充。其中一个包含映像数据，我命名为CI\_VALIDATE\_IMAGE\_DATA，其中包含以下内容：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653383197768.png "1665653383197768.png")

另一方面，外部授权结构(我将其命名为CI\_EXTERNAL\_AUTH)具有以下有趣的值：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653391969573.png "1665653391969573.png")

在调用验证引擎例程之前，CipApplySiPolicyEx将设置一个结构数组，其中包含每个策略的验证结果，该数组的大小将等于活动策略的数量。我将此结构命名为CI\_VALIDATION\_RESULT，它具有以下字段：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653400116071.png "1665653400116071.png")

最后，我们准备调用SIPolicyObjectValidationEngine，它具有以下原型：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653409136275.png "1665653409136275.png")

这个例程将简单地遍历策略和补充策略，为每个策略调用内部例程SIPolicyValidateImageInternal。

内部验证例程的任务是调用外部授权回调，以从“外部源”获取验证分数。它将根据此分数，选择继续或不继续根据策略中的规范评估映像。我们将首先关注外部回调，设置为函数CipExternalAuthorizationCallback，然后我们将讨论如何评估策略规范。

从代码中我可以看到，这与MS在文件规范优先顺序一节中声明的有些不同。他们说“它将首先处理它找到的所有显式拒绝规范。然后，它将处理所有显式允许规范。如果不存在拒绝或允许规范，WDAC将检查托管安装程序EA。最后，如果这些集合都不存在，WDAC会回到ISG”。相反，在代码中，似乎在处理FileRule之前检查了托管安装程序和ISG（外部授权）。

**CipExternalAuthorizationCallback**

这个函数包含了SAC的核心功能，即使它从21H2到22H2没有太大的变化，当启用SAC时，有一些细节会造成很大的不同。尽管如此，我们将要讨论的大部分内容都将被AppLocker和ISG使用(并且已经被使用了)，所以从好的方面来看，我们也将从中学习一些东西。为了概述我们是如何做到这一点的，下面是我们到达外部授权回调时的堆栈，用于验证未签名映像时的堆栈。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653418186460.png "1665653418186460.png")

该函数将通过检查策略选项Intelligent Security Graph Authorization（智能安全图授权）或Managed Installer（托管安装程序）启动，如果这些选项都没有设置，则该函数将退出，SIPolicyValidateImageInternal将继续处理策略FileRule，我们将在稍后的章节中看到这一点。

如果设置了任何选项，下一步是根据签名级别确定映像是否可信。这是通过使用为映像获取的ValidatedSigningLevel，并将此值与全局变量g\_CipWhichLevelComparisons内索引为0xC的位掩码进行比较来实现的。

请注意：全局变量g\_CipWhichLevelComparisons存储了一个指向ulong数组的指针。每个值表示适用于此签名级别的比较级别。通常与已验证的签名级别一起使用，以确定映像的不同操作/选项。例如，对于等于“File Unsigned”（即数组中的索引1）的已验证签名级别，位掩码为0xFFFFFFFE，因此大多数情况下测试此位掩码时，结果都为正值。在其他情况下，如上所述，索引在代码中被硬编码为仅作用于与该索引的位掩码匹配的已验证签名级别。下表有望帮助理解g\_CipWhichLevelComparisons和ValidatedSigningLevel之间的关系。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653427948692.png "1665653427948692.png")

如上表所示，索引0xC表示位掩码0x5000，表示“Windows签名”和“Windows TCB签名”。此外，接下来的两个级别“仅用于.NET NGEN编译器的签名”和由使用AMPPL的产品的反病毒签名”也将包含在可信映像列表中。此时，函数将继续调用CipCheckSmartlockerEAandProcessToken以获得第一个验证分数。

我觉得这是一个讨论命名的好时机，希望微软的人能联系到我，并澄清命名。有人称之为Smart App Control和Nights Watch，也有人称之为AppLocker，内部名称似乎是SmartLocker。相同或非常相似的事物有4个不同的名称。这确实有点令人困惑。

该函数具有以下原型：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653436117114.png "1665653436117114.png")

这个函数有两条路径，其中一条总是被执行，另一条基于boolean IsTrustedSigning。如果不受信任，那么下面的EA将被查询为正在验证的文件对象，它也试图从当前流程文件对象中获得相同的EA，但除了存储在验证上下文中，我没有看到它们在其他地方被使用。

$ Kernel.Smartlocker.Hash: 包含映像的哈希；

$ Kernel.Purge.Smartlocker.Valid: 布尔值是否有效；

$Kernel.Smartlocker.OriginClaim: 包含我命名为EA\_ORIGIN\_CLAIM的结构。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653446116758.png "1665653446116758.png")

如果获得了有效的EA，那么将检查OriginClaim结构以确定图像的分数。Origin值将决定第一个分数，如果Origin == 0，则score |= 1，如果Origin == 1，则score |= 0x1002。

不过我对这方面了解不多。这很可能与WDAC在策略中设置托管安装程序选项时在AppLocker中使用的特殊规范集合有关。这很可能与在策略中设置托管安装程序选项时WDAC使用的AppLocker中的特殊规范集合有关。从我所看到的，我知道appid.sys确实设置了此EA，另一种设置此EA的方法是通过CI回调cisetcachedorigin声明。这个函数在发出带有标志0x2000的syscall NtSetCachedSigningLevel时被内核调用，当然不像调用这个syscall来设置EA origi...