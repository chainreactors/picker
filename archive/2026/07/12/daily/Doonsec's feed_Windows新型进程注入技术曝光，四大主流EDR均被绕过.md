---
title: Windows新型进程注入技术曝光，四大主流EDR均被绕过
url: https://mp.weixin.qq.com/s/Tc9QY115rhAUaL_GnOm3Ow
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:28:12.553879
---

# Windows新型进程注入技术曝光，四大主流EDR均被绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5yYXmGfnscQiaszcicYvD7Izjzo1cMxoDiaveWCjNP3cIbxHn4sZuSDWolLiavSLN3f4icrgmNia1U0NDFudiaLpwjpgEPtibQUibuF5iaCzyl5dib7UEI/0?wx_fmt=jpeg)

# Windows新型进程注入技术曝光，四大主流EDR均被绕过

乌雲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一项新发布的Windows概念验证（PoC）展示了攻击者如何在规避端点安全工具常用的多项告警指标的同时，将恶意代码植入合法进程内部。

该方法被称为“进程参数投毒”（Process Parameter Poisoning），它利用Windows启动程序时通常传入的信息，而非直接将载荷写入其他进程。该研究并不关联任何活跃的恶意软件家族或已确认的攻击活动。但其重要性在于，恶意软件广泛使用进程注入技术来混入受信任程序并隐藏自身行为。

攻击者只需已具备在Windows机器上执行代码的能力，即可改造并运用这一技术。GitHub项目的分析人员指出，该加载器在针对四款主流端点检测与响应（EDR）产品的测试中，成功绕过了其检测机制。这项发现揭示了一个盲区：当防御措施主要聚焦于常见的内存写入和进程创建行为时，便存在漏洞。

Orange Cyberdefense在与Cyber Security News（CSN）分享的一份报告中表示，该方法将shellcode暂存于新进程的启动数据中，随后修改该进程的主线程，使其开始运行该代码。公开项目P-Shellcode Loader被定位为安全研究工具，而非武器化的恶意程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0CNlfRJVK6CH8DaE4c4LgOmx0zT2xtczcXYPXm9rnN0xibCRtibNWglPmgLP7dibyNaC42ziceDMH2I4cXKWDk8lGfdmKFdWicmKl0/640?wx_fmt=png&from=appmsg#imgIndex=2)

Part01

新型Windows进程注入技术

传统的进程注入通常遵循一条可识别的路径：程序打开或启动目标进程，在其内部分配内存、写入代码、将内存标记为可执行，然后启动或重定向一个线程。安全产品通常会标记与这些步骤相关的API调用，包括VirtualAllocEx、WriteProcessMemory和CreateRemoteThread等。

新方法另辟蹊径。当Windows通过CreateProcessW创建进程时，它会将命令行数据、环境变量和启动设置复制到称为进程环境块（PEB）的内部结构中。加载器将载荷放入其中一个复制值中，研究人员将这一操作称为“投毒进程参数”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3dYkAAnRK5nIc19xrMdQZibDtDT1fPfLEGotXicwEzLy51gAJaKx9bRKP04oAZxCIZ9wHmJzkvwugH0oKTQ0CBJzWJfkBWoJAV0/640?wx_fmt=jpeg#imgIndex=3)

它可以利用命令行、环境块或lpReserved启动字段（Windows将其映射为ShellInfo）来隐藏载荷。程序启动后，加载器读取目标进程的PEB，并通过内存读取函数找到存储的数据。它避开了许多EDR检测优先关注的常规远程内存分配和写入调用。

随后，该技术修改已存储内存的权限，使载荷能够运行。它不创建远程线程，而是通过NtSetContextThread更改新进程主线程的指令指针，将正常程序执行流导向注入代码，从而规避与经典注入相关的多个常规检测指标。

测试还发现，该加载器无需将目标进程以挂起状态创建，也无需后续挂起其线程——这些操作通常与进程空洞（Process Hollowing）及类似技术相关联。较少的高调操作可以缩减基于行为的防御所能追踪的痕迹，尽管这并不能使活动完全隐形。

Part02

检测需要更广泛的上下文

该研究表明，防御者不应仅依赖内存分配、远程写入或远程线程创建的告警。监控还应检查异常的CreateProcessW输入，尤其是异常长的命令行、不寻常的环境数据以及通过STARTUPINFO结构提供的异常值。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1AvZjuXI55V9KZfAnaTqKyphhLardweVHV2b2tgakbGS0pqt7UWP1XsRhs58JG4fYm25q9zsaw0RC65OCAx9GTXgDTZictuxaI/640?wx_fmt=jpeg#imgIndex=4)

关联进程创建与快速的线程上下文变更，可以揭示更完整的攻击序列。安全团队可以查找启动参数包含与其预期角色不符的数据的进程，随后出现NtQueryInformationProcess以及PEB读取操作。之后内存保护从可读可写更改为可读可执行，再结合NtSetContextThread，这一系列操作值得重点关注。这些事件单独来看可能属于正常行为，但其发生时序和组合则意义重大。

该概念验证存在局限性。进程参数是以null结尾的字符串，因此含有空字节的原始shellcode无法通过简单方法完整复制。研究人员通过生成不含空字节的代码，并采用分阶段（staged）例程来重建任意载荷（包括DLL加载或从HTTPS位置获取的内容）来解决这一问题。

对于防御者而言，实际应对措施包括：针对此模式验证检测规则；扩展围绕进程启动数据和线程上下文操纵的遥测采集；调查异常的父子进程关系。应用程序白名单、最小权限控制和及时补丁无法根除此技术，但可以降低攻击者获得执行代码能力并利用该技术的可能性。

参考来源：

New Windows Process Injection Technique Bypasses Four Leading EDR Solutions

https://cybersecuritynews.com/new-windows-process-injection-technique/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

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