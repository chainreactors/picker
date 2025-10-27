---
title: 漩涡：EDR内核回调、钩子和调用堆栈
url: https://www.cnxct.com/maelstrom-edr-kernel-callbacks-hooks-and-callstacks/
source: CFC4N的博客
date: 2023-03-26
fetch_date: 2025-10-04T10:43:02.141758
---

# 漩涡：EDR内核回调、钩子和调用堆栈

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
不要对没做过的事情说没意义。

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# 漩涡：EDR内核回调、钩子和调用堆栈

[2023/03/262023/03/26](https://www.cnxct.com/maelstrom-edr-kernel-callbacks-hooks-and-callstacks/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [译者序](#ftoc-heading-1)
2. [介绍](#ftoc-heading-2)
3. [目的](#ftoc-heading-3)
4. [重要概念](#ftoc-heading-4)
   1. [我们所说的端点检测和响应是什么意思](#ftoc-heading-5)
   2. [常见的EDR架构](#ftoc-heading-6)
   3. [简要回顾和比较高级别的EDR行为](#ftoc-heading-7)
   4. [用户空间和内核空间](#ftoc-heading-8)
   5. [驱动程序](#ftoc-heading-9)
   6. [Hooking](#ftoc-heading-10)
5. [狩猎ELK](#ftoc-heading-11)
6. [内核回调](#ftoc-heading-12)
   1. [触发回调](#ftoc-heading-13)
   2. [欺骗payload](#ftoc-heading-14)
   3. [绕过回调](#ftoc-heading-15)
   4. [内核回调结论](#ftoc-heading-16)
7. [Hooking 和 进程仪表化](#ftoc-heading-17)
   1. [Hooking 示例](#ftoc-heading-18)
      1. [手动 Hooks (x86)](#ftoc-heading-19)
      2. [NtSetProcessInformation 回调函数](#ftoc-heading-20)
   2. [绕过用户空间钩子](#ftoc-heading-21)
      1. [DLL](#ftoc-heading-22)
      2. [加载器](#ftoc-heading-23)
      3. [检测功能](#ftoc-heading-24)
      4. [绕过用户空间钩子](#ftoc-heading-25)
   3. [钩子和进程仪器结论](#ftoc-heading-26)
8. [线程调用堆栈](#ftoc-heading-27)
9. [结论](#ftoc-heading-28)

## 译者序

本文来自：[Maelstrom: EDR Kernel Callbacks, Hooks, and Call Stack](https://pre.empt.dev/posts/maelstrom-edr-kernel-callbacks-hooks-and-callstacks/)，版权归原作者所有。

译者从事HIDS/HIPS等领域，与EDR安全产品场景类似。从本篇文章中，也学到了Windows系统上的HOOK知识，了解了攻击手法，故翻译整理出来，分享给大家。感谢翻译工具OpenAI Translator。

## 介绍

为了回顾一下这个系列，我们从总体上看了一个命令和控制服务器（C2）的高级目的和意图，到设计和实现我们第一个植入物和服务器。如果你一直在跟随着做，你可能会认为自己已经写出了一个 C2
这是一种常见的心态。根据我们的经验，在达到这个点上并不需要太多复杂性。我们之前所有的工作都可以很容易地通过使用 C#、Python、Go 等语言在疯狂喝咖啡打字的晚上轻松完成（而且已经完成过！）。C2 的主要特点通常可以与软件工程中相当古老且解决方案明确的概念和模式联系起来，例如线程管理、处理空闲进程以及确保正确执行程序流。

但正如我们编写各种 C2 时发现的那样，并且许多其他攻击性开发人员编写他们自己的植入物和服务器时也发现了同样问题：一旦代码运行良好并能获得 pingback 后，您就停止在开发计算机上运行您的植入物并尝试在第二台计算机上运行它。这就是问题开始浮现之处。比如“为什么我无法访问远程文件？”，“为什么我可以通过这个协议进行出站请求，但不能通过那个协议？”，“为什么这个命令只是失败了而没有解释”，以及对于有足够的冒名顶替综合症的愤世嫉俗者，“为什么 Defender 没有阻止我做这件事？”。

就我们个人而言，这篇文章是我们期待写作的。它将是一个讨论，并附带一些示例，介绍在具有主动端点保护环境中越来越常见的行为。在 2022 年，植入物面临着更多审查——植入物和 C2 运营商必须准备好面对或规避此类审查，而防御者必须了解其工作原理，以便最大限度地利用它。

在撰写本文时，我们还想澄清关于“它避开了<插入公司名称> EDR”的推文。虽然该植入物能够执行操作并不意味着端点保护程序看不到它——可能会如此，但我们想演示一些这些解决方案用于识别恶意行为并引起对植入物怀疑的技术。

简而言之，执行的证明并不等于逃避的证明。

## 目的

这篇文章将涵盖以下内容：

* 设置 [The Hunting ELK](https://github.com/Cyb3rWard0g/HELK)
* 审查三种EDR可以检测或阻止恶意执行的方式：
  + Kernel Callbacks
  + Hooking
  + Thread Call Stacks

通过本篇文章的阅读，我们将了解到现代EDR如何保护免受恶意植入物的攻击以及这些保护措施如何被绕过。我们将从一个技术上可行但实际无法达成操作目标的植入物转变为对如何编写能够实际工作并能够达成操作者目标的植入物有所认识。

正如我们多次强调的那样，我们不会创建一个可用于操作的C2。本系列输出内容质量较差且存在缺陷 – 它只足以作为一种破碎证明特定主题中讨论内容正确性的概念验证代码，以避免该代码被恶意使用。出于同样原因，我们试图避免在本系列中讨论红队操作策略。然而随着文章深入，很明显与已经受到妥协用户典型行为相融合是有效的。这是 [xpn](https://twitter.com/_xpn_)在Twitter上曾经谈论过的话题：

> Find Confluence, read Confluence.. become the employee!
>
> — Adam Chester (@*xpn*) [January 22, 2022](https://twitter.com/_xpn_/status/1484970081046126594?ref_src=twsrc%5Etfw)

如果您的植入物已被EDR标记，查询每个AD加入计算机上的[NetSessionEnum](https://blog.compass-security.com/2022/05/bloodhound-inner-workings-part-2/)以查找活动会话可能不是典型用户行为。直到它停止响应，您可能不知道自己的植入物已被标记。从这里开始，就要竞赛了，直到您的植入物上传到[VirusTotal](https://virustotal.com)，然后您必须重新开始规划。

在本博客中我们将经常提到以下程序：

* [The Hunting ELK](https://github.com/Cyb3rWard0g/HELK) (HELK)：HELK是[Elastic](https://www.elastic.co/)堆栈最好由他们自己总结的开源狩猎平台之一:> The Hunting ELK或简称HELK是第一个具有高级分析功能（如SQL声明性语言、图形、结构化流和甚至通过Jupyter笔记本和Apache Spark进行机器学习）ELK堆栈上的开源狩猎平台之一。

> 该项目主要用于研究，但由于其灵活设计和核心组件，可以在正确配置和可扩展基础设施下部署在更大环境中。

* [PreEmpt](https://mez0.cc/projects/preempt/)：伪EDR，具有消化EtwTi、内存扫描器、钩子等功能。虽然这不是公开的，但在必要时将共享代码。

这两个工具将允许我们在需要时生成概念验证数据。

## 重要概念

与[Maelstrom: Writing a C2 Implant](https://pre.empt.dev/posts/maelstrom-the-implant/)类似，我们希望有一个专门的部分来澄清一些在继续之前需要一些背景知识的主题。

### 我们所说的端点检测和响应是什么意思

端点检测和响应（EDR）软件有许多不同的缩写，不同公司的程序及其功能可能存在区别。为简单起见，我们称所有仅限于静态扫描磁盘文件的程序为“反病毒”，而将所有进一步扫描设备内存、查看程序运行时行为并在发生威胁时进行响应的程序称为“EDR”。这些可能被称为各种名称，包括XDR、MDR或普通AV。

在本系列中，正如我们迄今所做的那样，我们将坚持使用“EDR”。

关于此问题一个很好的概述是[CrowdStrike发布了“What is Endpoint Detection and Response (EDR)”](https://www.crowdstrike.com/cybersecurity-101/endpoint-security/endpoint-detection-and-response-edr/)。

> 端点检测和响应（EDR），也称为端点检测和威胁响应（EDTR），是一种端点安全解决方案，可持续监视最终用户设备以侦测和应对勒索软件和恶意软件等网络威胁。
>
> EDR由Gartner的Anton Chuvakin创造，被定义为“记录并存储端点系统级行为，使用各种数据分析技术来检测可疑的系统行为，提供上下文信息、阻止恶意活动，并提供修复建议以恢复受影响的系统。”

因为这与本帖子相关，下一节将介绍EDR架构并比较不同厂商之间的EDR行为。我们不会大量偏离主题地涉及其他相关领域，例如反病毒软件如何工作、基于磁盘保护如何防止植入执行（如果您仍在运行磁盘）、AntiVirus和EDR实际上是如何扫描文件及其行为的。结果证明，那就像一个完整的学科领域。

### 常见的EDR架构

在讨论端点保护时，了解其架构可能会有所帮助。[Symantec EDR Architecture](https://pre.empt.dev/posts/maelstrom-edr-kernel-callbacks-hooks-and-callstacks/Symantec%20EDR%20architecture) 的架构大致如下：![](https://image.cnxct.com/2023/03/symantec-arch.png)

类似的方法也可以看到 [Defender for Endpoint](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/onboarding-endpoint-manager?view=o365-worldwide) 中。基本上，安装该产品的设备将具有代理程序，其中包括几个驱动程序和进程，这些驱动程序和进程从机器的各个方面收集遥测数据。通过本文和下一篇文章，我们将介绍其中一些。

> 顺便说一句，在Windows环境中，Microsoft天生就占据优势。虽然这目前针对“大型企业”客户（或者至少我们认为是这样，考虑到他们在Azure上的价格！），但Microsoft Defender和新版Defender MDE都可以访问Microsoft对…自己操作系统的知识，并影响新操作系统功能的开发。长期来看，不难想象微软Defender MDE会以类似于微软Defender影响反病毒市场的方式影响EDR市场。

所有EDR通常都是从代理发送遥测数据到云端，在那里通过各种沙盒和其他测试设备运行，并且可以由机器和人员操作员进一步分析其行为。

对于过度好奇的读者，以下链接详细介绍了特定供应商的EDR架构方法：

* [EDR Architecture (Bitdefender)](https://www.bitdefender.com/business/support/en/77209-87486-edr-architecture.html)
* [EDR Security | Move Beyond Traditional Endpoint Detection and Response (paloalto Networks)](https://www.paloaltonetworks.com/blog/security-operations/edr-security-move-beyond-traditional-endpoint-detection-and-response/)
* [Symantec EDR architecture (Symantec)](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-detection-and-response/4-4/introduction-v119804561-d38e3280/architecture-v125228003-d38e2709.html)
* [Onboarding using Microsoft Endpoint Manager (Microsoft)](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/onboarding-endpoint-manager?view=o365-worldwide)

### 简要回顾和比较高级别的EDR行为

不想离题太远，就像并非每个红队评估都是红队一样，并非每个EDR都是真正的EDR。以下[Gartner Magic Quadrant](https://www.gartner.com/en/research/methodologies/magic-quadrants-research)来自[Gartner 2021年5月报告](https://www.gartner.com/reviews/market/endpoint-detection-and-response-solutions)，大致勾画了EDR领域的格局。值得注意的是，[CrowdStrike雇佣](https://www.crowdstrike.com/blog/author/alex-ionescu/) [Alex Ionescu](https://twitter.com/aionescu)(ReactOS内核维护者)表明目前最佳实践的EDR在很大程度上利用了对Windows内部功能知识以提高其性能：

![](https://image.cnxct.com/2023/03/gartner-edr-landscape.png)

由于许多EDR功能依赖于我们将在此处讨论的方法（例如定制编写直接行为、如内核回调和挂钩），因此能够快速实现新Microsoft Windows特性并开发自己可靠地与恶意进程交互和中断方式似乎是现代EDR与同行区分开来的显著特点。

另一个EDR供应商倾向使用且尤其因报告公开而使用的度量标准是[Mitre Enginuity](https://mitre-engenuity.org/)。[攻击评估](https://mitre-engenuity.org/attackevaluations/)描述如下：

> MITRE Engenuity ATT&CK® 评估（Evals）计划将产品和服务提供商与MITRE专家合作，共同评估安全解决方案。Evals过程采用基于威胁的紫队方法应用系统化方法，以捕获关于解决方案能力的关键上下文，该能力可以检测或保护免受ATT&CK知识库定义的已知对手行为。每次评估的结果都会得到彻底记录并公开发布。

例如，在[SentinelOne](https://sentinelone.com)中，其结果可在以下链接中查看：[SentinelOne概述](https://attackevals.mitre-engenuity.org/enterprise/participants/sentinelone?view=overview&adversary=wizard-spider-sandworm)。概述介绍了APT场景，并标记了是否检测到该技术，并可用作其“有效性”的跟踪器。然而，一些人在线上表达了这不是确定产品效果的全面方式。

从购买角度来看EDR时，有几种确定有效性的方法值得考虑，并在此简要介绍它们。主要考虑因素是某些供应商未必比杀毒软件提供更多功能。与任何产品一样，请确保为您的业务需求购买正确的解决方案。

### 用户空间和内核空间

在讨论内核和用户空间模型时，将使用以下架构图像，这对任何计算机科学毕业生来说都很熟悉：

![](https://image.cnxct.com/2023/03/win-rings.png)

绝大多数用户活动将发生在第3环（User Mode），令人惊讶的是内核在Kernel Mode中运行。

有关...