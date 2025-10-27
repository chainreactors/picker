---
title: OT环境勒索软件分析与防范
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534528&idx=1&sn=52d5c7673f8d4f37a8c71297cd3d6e9b&chksm=c1e9cb91f69e42878dac570fbbc406f8da86531bd2db073ff51a1375db647631bdf8a442f113&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-18
fetch_date: 2025-10-04T07:23:12.903473
---

# OT环境勒索软件分析与防范

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs8icFDywQkWfTIhxVChZX9vAVInW2AJbKdR1MJQMpzXTICibjlz2vQbztM2Y6XgF3uVnqf9NeX9ic6w/0?wx_fmt=jpeg)

# OT环境勒索软件分析与防范

关键基础设施安全应急响应中心

2023年1月，匿名者旗下的GhostSec黑客组织声称对RTU（远程终端单元）进行了“有史以来第一次”勒索软件攻击，RTU是一种通常部署在工业控制系统 (ICS)环境中的小型设备，是周边监控和数据采集(SCADA)设备，用于测量和控制实际物理设备。从图片中可以看出，黑客进入了RTU设备的嵌入操作系统内部，并对文件进行了加密：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3NW1FFZLqhRxMN5vEZMOPjFlBdCFcgxL38CHF3ibPJqgmVINp1r3H7UQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3fxfgvjWJuiakVXPz4WvvVctmcweuJPEBeexZoDfl8oDhXgxmicImXSIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

近期SynSaber公司的报告，回顾统计分析了CISA在2020年至2022年期间发布的ICS系统报告数量，工业控制系统(ICS)中漏洞报告数量持续增加，2021、2022年的增加数量大致相同为350份，但2022年新增的漏洞数量达到1342个，2021年为1191个。

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3STM3xQaQt0ctBk1icbShrLhfWQ3CZricYCX10Nrb3qrdl7tyrsKrTh7A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

“严重”等级的漏洞数量增长更为显着，从2021年的186个增加到2022年的近300 个。根据CVSS评分，总共有近1,000个漏洞为“严重”或“高严重性”。报告特别指出，在过去三年中，已发布的工业控制系统(ICS)漏洞数量增长了近70%，关键是其中超过21%仍未被修补。

0x01 勒索的潜在影响

勒索软件是病毒的一种形式，或者更常称为恶意软件。从本质上讲，攻击者会找到一种方法（网络钓鱼、社会工程等）首先入侵目标网络。然后，他们的“软件”在网络中运行（遍历网络共享、本地驱动器等），使用只有攻击者才知道的密钥对其发现的所有内容进行加密。如果你想解锁你的文件，你必须付钱给坏人给你钥匙。根据攻击者和受害者的具体情况，获取密钥和解密文件的成本可能从数百美元到数千美元甚至数百万美元不等。

勒索软件植根于诈骗和勒索犯罪世界，从本质上讲，它也可以用来针对较大的资产所有者和组织，或掩盖其他可能更不正当的活动。勒索软件对企业的攻击，包括OT企业，各类新闻早已屡见不鲜。为什么勒索软件正在成为当今工业组织面临的挑战：

1、勒索软件利用“可用性”风险，在工业组织中利润丰厚。网络窃取个人信息的业务曾经相当有利可图，但随着供应的增加，这些信息的价格已大幅下降。因此，网络罪犯找到了新的商业模式。它们已经从机密性-完整性-可用性三要素中的“C”转变为“A”。而工业组织需要可用性来运作，因此付款通常是快速和大量的。

2、在大多数情况下，保险支付赎金和追索费用是的很大一部分。因此，在目前的政策下，保险的存在使支付过程变得更加顺利。然而，随着保险公司开始改变未来的政策，这种情况正在发生变化，正如安盛（AXA）最近宣布停止对勒索软件支付的覆盖。

3、通过IT系统攻击可以关闭OT操作。为什么会这样？首先，OT系统通常非常容易受到勒索软件的攻击，如果勒索软件进入这些系统的话。因此，任何事件响应处置的第一步都是通过断开与OT系统连接来阻止传播。虽然IT系统的恢复成本很高，但OT系统的成本可能是IT系统的3-4倍，并且可能需要更长的时间。

4、勒索软件通常利用基于网络的不安全性来获取访问权限（例如，通过RDP），但会从一个端点传播到另一个端点。补偿控制、系统加固、漏洞管理和其他技术（如网络隔离）都在减少病毒攻击的影响和传播方面发挥着关键作用。

下图显示了勒索软件攻击设施的典型路径和杀伤链（Kill Chain）：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3za8SRRZ9rjDib8TDM2H8VnWYAyaJcaicHguJ7MFp2nJsGXvgBh6ibMKwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3OgWLcm8aJJZicfc0AiaHddqB3T68cAWnqD6NSfNpjX0NYJG26WrIZtDw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2021年底和2022年初的预测都认为，发达经济体的重大勒索软件攻击将持续爆发。然而，实际情况是，预测的爆炸从未发生。根据来源，围绕2022年期间勒索软件是略有增加还是实际减少存在一些争议。但无论从哪个数据集来看，人们担心的勒索软件大流行从未发生。使用与去年相同的数据源， 2022年第三季度的事故略有减少（约10%）。在此之前，第二季度略有增长，第一季度基本持平。全年来看基本轻微增加和减少，而不是另一个巨大的峰值。

2022年没有快速增长并不意味着勒索软件仍然不是工业环境的最大威胁。同样，根据分析师的不同，勒索软件在2022年至少同比持平——与历史数据相比，持平在一个非常高的水平。

攻击格局在2022年确实发生了重大变化。到目前为止，LockBit2.0仍然是“市场份额”领先集团，并在年中关闭了最臭名昭著的集团之一Conti–意味着LockBit的份额日益集中,以及众多新的竞争团体的崛起——Basta、Hive和其他几个团体。有一些人认为，这些不同的团体中有许多是Conti的重组团体。一个基本的勒索软件市场占比如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3tRWzuSYVm93iaHNbzvL7u6WAUxTrSszdiaIiaZ48ltZrthhpyWX4EresQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Dragos的报告总结了2022年全年的工业控制系统勒索事件

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3UTHvmnmQrIiaicgHh2VcOBsibAuiaSRiaAmlXjUZAflAVmlaTTpsXbWzOsA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/ibQxG9cezyUahwDNtlEwibxXpMvgfuBGx3MhX2ia8f5W1jZOKxhnb84xPUZ0uCIT61ttK47OIjsyX8RbPsMlCk4bA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

0x02 减少与防范OT环境中的勒索

考虑到当前ICS系统攻击事件和漏洞呈上升趋势，因此ICS系统风险状态以及工业环境中勒索软件事件存在再次加速的可能性，OT企业应如何组织响应呢？

**了解勒索软件攻击给您带来的实际操作和安全风险**

要了解这一情况，组织需要掌握三条关键信息：

1、理解不同资产在运营环境中的关键程度。例如，你可能有某些工厂、制造、设施等，这对企业的财务业绩至关重要。其他人可能在财务上不那么重要，但他们是这些关键站点的关键供应商。因此，对站点/设施重要性的业务理解是基础。

2、全面了解这些设施中的资产面临的勒索软件风险。通常通过“技术驱动漏洞评估”来实现这一点。在OT环境中，对软件和硬件漏洞、网络保护和资产的保护、补丁程序状态等的详细把握。这种360度的风险视图提供了对现场/设施/工厂等的潜在威胁的可视化。

3、恢复和响应能力的现状。准备充分的组织可以减少任何勒索软件事件的范围。强大且更新的备份、快速事件响应计划、Canary文件警报(Canary共享文件类型为检测勒索软件感染的诱饵，但其数据对企业并无价值。该共享文件类型仅用于快速的感染检测)以在早期阶段捕获勒索软件等。所有这些都可以提供限制因素。通过评估这些响应和恢复能力，组织可以确定攻击的潜在影响范围。

**创建站点级别的补救和保护路线图**

我们经常看到组织采取某种措施来降低勒索软件（和其他潜在的OT攻击）的风险。例如，一个常见的做法是全面的网络划分，以减少连通性IT和OT之间以及OT环境内的隔离，这当然是稳健做法的一部分。然而，这可能不是整个计划中最有影响力的第一步。了解风险和一系列举措是取得快速但可持续进展的关键。如果不清楚网络上的资产以及它们如何相互通信，通常很难进行适当的网络分段。因此，全面的环境清单加快了最终的细分工作。类似地，一些计划可能会迅速产生影响，例如，利用可能已经到位的备份工具，但要确保它们得到使用和更新。站点和企业级别的这一系列计划提供了一个路线图，可在构建保护和检测的长期基础的同时实现近期保护和恢复功能。

**基于第一点中的站点和资产优先级加快OT安全建设**

接着是补救的时候了，“技术驱动评估”的优势之一是上面提到的技术已经准备到位，能够立即修复已识别的风险。从修补到配置强化，再到管理有风险的软件、用户和帐户等。

除了加速这些终端的检测之外，还需要一系列额外的保护和响应能力。最大的挑战之一是确定适当的执行计划来保护最核心的站点和资产，同时不会在这些大型/复杂的站点上陷入困境，并且永远不会对评级为“中等”关键程度资产进行过度保护。

一种称之为“双焦点”的执行方法：一方面，我们肯定会在最关键的站点上进行稳健的计划部署。然而，与此同时，我们将鼓励一种广泛而浅显的方法，在企业级别对所有站点应用有限的保护，同时在关键站点上进行更深入的工作。

0x03 OT安全计划中的关键要素

**资产盘点**

有效的终端管理始于稳健的资产库存。正如一句谚语所说：如果你不知道你拥有什么，你就无法管理风险。每个终端资产360度资产画像将为合理的端点管理提供支撑。OT挑战：整合自动化资产清单，其中包括从基于操作系统到网络的所有资产类型，还嵌入了深入的资产配置文件，包括设置关键程度、用户和帐户、补偿控制的存在等。

**补丁管理**

大多数威胁都是通过商用系统（如Windows计算机）进入的。您无法在OT中修补所有内容，但由于多个环境因素，端到端修补程序管理计划（即修补程序的自动化和智能应用）非常重要例如合规性、法规和风险管理（例如，具有连接到互联网的RDP或防火墙的主机上的补丁应优先于由多个层保护的PLC）。当今勒索软件的实际情况是，它主要针对基于操作系统的设备（服务器、工作站、HMI）。在管理补丁程序以解决勒索软件时，这些是主要的关注点。在不可行的情况下，应用程序白名单和策略强制执行会增加攻击的成本和难度，以提高您防御或拒绝对您的OT组织进行勒索软件攻击的机会。OT挑战：需要有一个排定了优先级的修补流程并转移到补偿控制必要的时候/地方。

**应用程序白名单**

这始于可能尝试在HMI、工作站等上运行的新软件的应用程序控制。在IT中，考虑到所需的新应用程序的广度，维护此解决方案相当具有挑战性。然而，在OT中，大多数系统应该被“锁定”，新的应用程序是不必要的。因此，国土安全部强烈建议将白名单作为2-3项首要举措之一。白名单还可以扩展到USB、可移动介质和临时设备，尤其是在您的网络存在“物理隔离”或受到严格控制的情况下。用户将通过可移动介质绕过您的控制。作为最佳实践，系统策略易于部署，使用白名单软件，注册安全驱动器和其他技术（如802.X）可确保网段上允许授权系统。OT挑战：列举、应用、监控和执行可移动介质策略以及扩展到临时网络资产。

**强大且更新的备份**

任何安全计划都不足以阻止每一次攻击。因此，全面的备份程序对于确保快速恢复至关重要。这包括确定要备份的系统的优先级，确保及时备份，监控失败的备份（在许多OT环境中似乎经常发生），以及确保在离线存储库中进行复制，以便恶意软件不会限制其有效性。OT挑战：创建与供应商无关的备份解决方案，因为许多OEM都有首选的备份解决方案。成功的关键是创建单一的备份平台，以便能够提高效率，同时确保跨各种站点的法规遵从性。

**实施网络分离或分段**

减缓勒索软件传播的一个关键方法是在IT和OT网络之间（甚至在IT和/或OT的网段内）设置网络屏障。这种方法是一个基本要素，但由于其技术挑战，往往没有得到充分利用。OT挑战：对IT或OT进行分段并不容易，但在OT中，由于传统设备、物理布线需求、将系统移至新防火墙所需的停机时间等原因，出现了特殊的挑战。OT细分需要一个对网络和OT系统有深入了解的团队。

# **参考资料：**

https://industrialcyber.co/industrial-cyber-attacks/hacker-group-discloses-ability-to-encrypt-an-rtu-device-using-ransomware-industry-reacts/https://synsaber.com/resources/industrial-cve-retrospective-2020-2021-2022

https://verveindustrial.com/resources/blog/how-to-prevent-ransomware-in-2023/

https://hub.dragos.com/ics-cybersecurity-year-in-review-2022

原文来源：博智非攻研究院

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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