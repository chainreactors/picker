---
title: 以SentinelOne的产品为例，说说eBPF在CWPP应用中的优势
url: https://www.4hou.com/posts/KEgY
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-26
fetch_date: 2025-10-04T08:07:56.888357
---

# 以SentinelOne的产品为例，说说eBPF在CWPP应用中的优势

以SentinelOne的产品为例，说说eBPF在CWPP应用中的优势 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 以SentinelOne的产品为例，说说eBPF在CWPP应用中的优势

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-02-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)132096

收藏

导语：我们会在本文详细介绍eBPF的工作原理，以及它对于云工作负载保护平台(CWPP)的重要性。

eBPF（extended Berkeley Packet Filter） 可谓 Linux 社区的新宠，很多大公司都开始投身于 eBPF 技术，如 Goole、Facebook、Twitter 等。eBPF 是从 BPF（也称为 cBPF：classic Berkeley Packet Filter）发展而来的，BPF 是专门为过滤网络数据包而创造的。但随着 eBPF 不断完善和加强，现在的 eBPF 已经不再限于过滤网络数据包了。

eBPF用于在Linux OS内核中加载和运行用户定义的程序，以观察、更改和响应内核行为，而不会影响内核模块的不稳定。eBPF直接从用户空间提供内核级可见性。可见性和稳定性的结合使得eBPF框架对安全应用程序特别有吸引力。

我们会在本文详细介绍eBPF的工作原理，以及它对于云工作负载保护平台(CWPP)的重要性。

**eBPF架构概述**

eBPF程序允许我们观察和响应内核中的应用程序负载行为，而无需修改应用程序代码本身。这对于许多应用程序都很有用，尤其是云工作负载保护等安全应用程序。

为了讲解方便，我们对ebpf.io中的原始图进行了修改。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222829955291.jpeg "1676222829955291.jpeg")

架构简述

以一个在用户空间中运行的应用程序——CWPP代理为例，它包括一个用于Linux内核中进程级可见性的eBPF程序。eBPF程序本身是字节码，尽管开发人员通常使用更高级别的编程语言，其编译器支持eBPF字节码。该eBPF程序被加载到Linux内核中，该程序立即由eBPF验证引擎进行验证。然后，程序被编译并附加到设计目标内核事件，这就是所谓的eBPF程序是“事件驱动的”的真实意思。无论何时发生此事件，程序都会附加到此事件，运行其观察和分析任务直至完成，并将结果返回给应用程序。

在eBPF程序和用户空间应用程序/工作负载之间传递信息的机制被称为“eBPFmap”或简称为“map”。

**eBPF安全**

eBPF验证引擎和即时编译器是eBPF框架首先确保在内核中加载和运行的eBPF程序不会破坏内核稳定的方法。这便是第一条规则：无攻击性。

考虑eBPF的替代方案：编写内核模块。内核模块引起了对操作稳定性和复杂性的关注。虽然编写内核模块确实允许开发人员更改内核行为，但这是一项高度专业化的技能，因此人员配备和保留便成为一个问题。更明确地说，使用内核模块会引发两个关键风险问题：1.内核模块会使设备崩溃吗？2、它是否会引入安全漏洞？

除了稳定性和安全性之外，还有操作时的功耗问题：内核模块只适用于特定的Linux内核版本和发行版。维护内核模块会消耗宝贵的开发周期，不必要使操作管理复杂化。eBPF框架解决了这些痛点，

在将任何eBPF程序加载到内核之前，它都要经过验证引擎和JIT编译器。验证程序确保程序运行安全，不会使系统崩溃，也不会破坏数据。它验证满足以下几个条件：

加载eBPF程序的进程具有执行此操作所需的权限；

eBPF程序不会使系统崩溃；

eBPF程序运行至完成，也就是说，它不会无限循环。

一旦经过验证，JIT编译器就会将程序从字节码转换为设备指令，从而优化执行速度。

现在eBPF程序已经验证和编译，它被附加到内核级事件，这样当事件发生时，程序就会被触发，直至运行完成，并将信息呈现给用户空间应用程序。这就引出了eBPFmap，或者简单的“map”。

**eBPFmap**

eBPFmap是在eBPF程序和用户空间应用程序之间传递信息的机制。支持双向信息流。map是eBPF程序和用户空间应用程序可以读取或写入的数据结构。

例如，程序可能会在文件的gzip等事件上被触发。eBPF程序将向map中写入有关该事件的一些信息，例如文件名、文件大小和gzip时间戳。它还可以增加给定时间段内gzip操作发生的次数。如果该数字超过某个阈值，eBPF程序可以将“恶意”判断写入数据结构。简单地说，eBPF程序观察到表明勒索软件攻击的行为，并将此行为标记为恶意行为。用户空间程序（在我们的示例中是云工作负载保护（CWPP）代理）可以读取该map，查看恶意判断，并采取适当的操作。基本信息处理发生在eBPF程序中，最大限度地减少了传递给用户空间应用程序的信息量，从而优化了性能。

**CWPP中eBPF的优势**

云工作负载保护平台代理执行其他安全控制所没有的操作，实时检测并响应运行时威胁，如勒索软件或零日威胁。这使得CWPP成为云防御深度战略的重要组成部分。一个组织可以而且经常应该有其他云安全措施，如AppSec、CSPM等。每一项都在稳健的云安全策略中发挥作用。CWPP代理与这些其他控件一起工作，以提供运行时保护和记录工作负载追踪分析。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222846522520.jpeg "1676222846522520.jpeg")

SentinelOne控制台中显示的Linux勒索软件攻击

如下图所示，对云计算实例（VM）的勒索软件攻击可以在几毫秒内锁定云工作负载。请注意，在这段1分钟的视频中，CWPP代理在勒索软件启动后几分钟（不到一秒钟）就检测到并阻止了勒索软件攻击。

尝试从侧面扫描解决方案获取实时响应是无法实现的。侧面扫描通常每天只运行一次，因为对云计算实例的存储卷进行快照检查的成本非常高。此外，侧面扫描架构在内核中缺乏进程级可见性。这些是SOC需要调查的法医细节，并将事件适当标记并发送给适当的DevOps所有者。只有使用eBPF框架的行为、实时CWPP代理才能提供实时过程级可见性和稳定性的组合，使其成为首选。

工作负载追踪分析的历史记录不仅有助于在发生安全事件时进行调查，还可以进行主动威胁搜索。通过这种方式，攻击者甚至可以在发动攻击之前被阻止。

eBPF框架在CWPP计划中的应用提供了几个优点，包括但不限于：

运行稳定性；

系统性能；

业务灵活性；

运行稳定性；

虽然内核模块可以提供CWPP应用程序所需的内核可见性，但在内核中运行代码可能是危险的。错误的操作会破坏系统的稳定（例如内核被攻击），或在内核中引入安全漏洞。这两种结果都是不可接受的，特别是在涉及CWPP代理的情况下。使用内核模块的CWPP代理可能会导致内核被攻击，从而导致VM崩溃并阻碍你的工作负载。这些威胁会直接影响到财务绩效、订单履行、客户忠诚度。

与内核模块形成鲜明对比的是，eBPF框架包括诸如验证引擎、JIT编译器等安全控件。因此，eBPF程序不会使内核崩溃，它们也不能进入内核中的任意内存空间，这使得它们更不容易出现安全漏洞。eBPF程序提供了所有内核级的可见性，并且没有来自内核模块的任何风险。基于这些原因，从运行稳定性的角度来看，eBPF是CWPP的首选。

**系统性能/资源效率**

将信息从内核内部传输到用户空间的速度缓慢，并且会带来CPU、内存性能损耗。相反，eBPF框架使我们能够观察内核行为，并在将结果的子集传输回用户空间之前在内核内执行分析。这为在用户空间中运行并使用eBPF程序的CWPP代理创造了基本的性能优势。eBPF与具有内核模块的CWPP代理相比，用最低的消耗提供了较高的可观测性。

**业务敏捷性**

开发人员应该专注于创新，而不是解决内核模块引入的内核依赖问题。通过从用户空间进行操作，DevOps可以更灵活地更新主机操作系统映像，而不必担心更新与CWPP代理发生冲突。eBPF使这成为可能。因此，更多的DevOps可以用于创新，而不必花精力去维护。

此外，由于CWPP代理本身使用eBPF框架并避免内核模块，因此供应商也更加注重创新。当然，客户也从业务敏捷性中获益。

以SentinelOne的产品为例，说说CWPP的一些出色性能

**高性能**

独立测试结果证明了这一点。2021年4月，MITRE Engenuity发布了Carbanak和FIN7的MITRE ATT&CK基准测试结果，这是一项专注于模拟金融威胁群体的评估。MITRE ATT&CK首次在其测试中包含Linux服务器。SentinelOne是唯一一个在Windows设备和Linux服务器之间具有100%可见性的供应商。我们拥有最丰富的检测(MITRE的术语是“分析检测”)，如下图所示。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222878482136.jpeg "1676222878482136.jpeg")

Visibility, MITRE Engenuity, Carbanak + FIN7

![5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222913147294.jpeg "1676222913147294.jpeg")

Analytic Detections, MITRE Engenuity, Carbanak+FIN7

如果CWPP要保护云工作负载免受运行时攻击并确保业务连续性，那么它必须是实时的如果是延迟检测，哪怕是几秒钟的时间，攻击者都可以使云工作负载停止。如果不是勒索软件，那就是恶意软件在你的云足迹中悄悄传播。从广义上讲，传播范围越广，补救力度就越大。损失也就越大。正如MITRE定义的那样，SentinelOne提供了100%的实时检测，零延迟。这就意味着，延迟越少越好。

![6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222963449942.jpeg "1676222963449942.jpeg")

Delayed Detections, MITRE, Carbanak + FIN 7

同样，2022年MITRE Engenuity ATT&CK测试显示SentinelOne具有极高的性能。Wizard Spider+Sandworm模拟还包括Linux服务器。此时，SentinelOne再次以99%的分析覆盖率领先于CrowdStrike、Microsoft或TrendMicro。可以在MITRE Engenuity网站上进行直接比较。

![7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230213/1676222939107295.jpeg "1676222939107295.jpeg")

2022年MITRE信息图

**资源效率**

任何应用程序，无论是CWPP代理还是其他应用程序，都需要计算和内存资源才能运行，这些资源都是有成本的。对于在固定和沉没成本基础设施（如数据中心）内的部署，此类应用程序会占用原本可用于主要业务工作负载的资源，虽然这不是一项增加的运营费用，但存在资源的机会成本。然而，对于云IaaS，所使用的资源是按需计量和付费的。部署CWPP代理可能必然会增加云计算实例的大小（例如，从 t4g.medium到 t4g.large），从而逐渐增加其运营费用。当然，这是一项必要的支出，但也是一项增量支出。

因此，SentinelOne的产品更关注CPU和内存利用率，就像关注性能一样。2022年7月，SentinelOne宣布支持AWS Graviton3，这是最新一代AWS ARM处理器，在计算、功率等方面提供了进一步的优势。

本文翻译自：https://www.sentinelone.com/blog/the-advantages-of-ebpf-for-cwpp-applications/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1n6XJ67U)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/pos...