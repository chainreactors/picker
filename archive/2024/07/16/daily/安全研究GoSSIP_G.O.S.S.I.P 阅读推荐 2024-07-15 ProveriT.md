---
title: G.O.S.S.I.P 阅读推荐 2024-07-15 ProveriT
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498451&idx=1&sn=22b459a36638233834a21d9ec51631ea&chksm=c063d40af7145d1cd4826dbe3e6d2a85c76971fcda40a819e5df18448acf4a47b5ad000e4636&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-16
fetch_date: 2025-10-06T17:44:49.709706
---

# G.O.S.S.I.P 阅读推荐 2024-07-15 ProveriT

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILYmicDejiaBEkKSbn1FBmGYy1Ge4wxToxlIZJSSSdwrP4x0h2yUGdRicbQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-15 ProveriT

Jilin@ZJU

安全研究GoSSIP

今天为大家推荐的论文来自浙江大学网络空间安全学院赵永望研究组投稿并发表在IEEE TDSC期刊上的最新工作**ProveriT: A Parameterized, Composable, and Verified Model of TEE Protection Profile**。该工作提出了组合验证框架并对可信执行环境的安全规范文档进行了形式化建模。通过形式化验证确保其正确性并且发现了漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSIL3swsgZG1AogPcVstbvIhTNnuw4MOPCh0gYCNc3icofOy1AZiaiaSUdr8Q/640?wx_fmt=png&from=appmsg)

在现代计算机系统中，可信执行环境（TEE）扮演着至关重要的角色。TEE通过提供隔离执行环境，确保电子设备中敏感数据的安全。然而，一旦TEE被攻破，可能会导致巨大的损失。尽管已经有许多TEE产品，但大多数缺乏强有力的安全保障。为了解决这一问题，GlobalPlatform（GP）定义了TEE的保护轮廓标准GPTEE PP: GlobalPlatform Technology TEE Protection Profile。其中，GlobalPlatform(GP)是一个致力于确保数字设备安全的国际性组织。该组织制定了许多安全标准和规范，以保障数字设备和服务的安全性和互操作性。GP的工作覆盖了从移动支付到数字身份认证等多个领域，广泛应用于全球范围内的数字设备和服务。而GPTEE PP被广泛用于TEE开发和Common Criteria（CC）安全认证。通过遵循GPTEE PP的要求，TEE开发人员可以确保他们的产品达到高安全级别的要求，保障包括移动支付、数字身份和安全通信在内的关键应用的安全性。然而，尽管GPTEE PP非常重要，它却从未被形式化规约和验证，可能存在错误。该工作介绍了ProveriT，一种GPTEE PP的参数化、可组合和经过形式化验证的模型，旨在填补这一空白。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILDEy5ib2s9KbeE7NfWSjzibECYicwa2FZzuOYlYqwJJ9SkrRYClAWMm5fw/640?wx_fmt=png&from=appmsg)

图1 ProveriT框架图

首先，该工作首个提出了GPTEE PP的形式化规范，以参数化方式涵盖了安全问题、安全目标和安全功能要求的定义。其次，研究人员提供了一个组合框架，利用横向计算算子和纵向计算算子，使TEE开发人员能够灵活地组合特定的安全功能要求，并减少验证过程中的证明工作量。ProveriT在特定TEE产品的验证和CC认证中具有可扩展性和可重用性。第三，研究团队对模型中的依赖关系进行了全面的形式化验证，以确保GPTEE PP的正确性。在验证过程中，发现了8个问题，并提供了解决建议。最后，通过将ProveriT应用于一个商业TEE 的验证，研究人员展示了其模型的可扩展性和有效性。

该论文主要的贡献如下：

1. 在深入分析GPTEE PP后，该工作提出了首个完整的形式化规范，涵盖了GPTEE PP核心的全部内容。该规范可重用且可扩展，适用于TEE验证和CC认证，为TEE的安全验证提供了坚实的理论基础。
2. 该工作提出了一个组合框架，利用横向计算和纵向计算来选择和组合GPTEE PP中的独立安全元素，并描述它们之间的关系。该框架满足了认证TEE产品部分功能的需求，同时降低了验证GPTEE PP的证明负担。
3. 该工作使用组合框架形式化验证了GPTEE PP的依赖关系。经过验证的GPTEEPP有更高的可靠性和安全性，为未来的TEE开发和验证提供了宝贵的经验和指导。
4. ProveriT被应用于验证小米公司开发的商业TEE产品MiTEE，展示了其方法的可扩展性和有效性。

**背景介绍**

可信执行环境（TEE）为敏感数据和代码提供了一个安全且隔离的环境。TEE将操作环境分为两个独立的域：普通域和安全域。从普通域到安全域的通信和访问由监控器严格控制。图2展示了典型的TEE架构。客户端应用程序（CA）和可信应用程序（TA）分别运行在普通域和安全域中，安全域中的TEE操作系统包括受信任的内核、驱动程序以及负责与常规执行环境（REE）侧的通信代理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILzzQvqoSV5kn88pfTkMncP7LuyGRPYjHh5GeQhZn5MeibibwkXvYOUq6Q/640?wx_fmt=png&from=appmsg)

图2 TEE架构示例

Common Criteria（CC）是一个国际公认的信息技术（IT）产品安全评估和认证标准（ISO/IEC 15408）。它建立了从EAL1到EAL7的七个安全保证级别，其中级别5到7需要半形式化或全形式化的方法。最高保证级别要求全形式化的安全模型、产品的功能规范及其对应的证明。此外，CC描述了一条证据支持链，确保产品的安全性，包括安全威胁、目标、要求和功能。

GPTEE PP是由GlobalPlatform TEE安全工作组开发的TEE安全标准，并且符合CC认证要求。它涵盖了支持链中的前三种安全元素，而功能定义涉及具体的系统实现，由开发人员负责。GPTEE PP定义了核心的TEE保护文档，包括TEE的最低安全要求，如安全初始化、固件完整性、安全存储、与REE的隔离以及应用空间之间的隔离。此外，它还建立了两个补充的PP模块：TEE时间和回滚，确保完全的回滚保护和持续的单调时间，以及TEE调试，允许对调试功能进行受控访问。GPTEE PP被广泛认为是TEE的关键安全标准，并被众多设备制造商、安全评估人员和认证机构所采用。

**方法概述**

ProveriT提出了一个组合框架，以满足现实世界产品的需求，即灵活组合安全功能需求（SFRs），并且能简化依赖关系正确性的验证。ProveriT的组合框架提供了两种模块计算方法，即横向计算和纵向计算。横向计算有助于灵活组合同一层的模块，纵向计算则描述了不同安全元素模块之间的精化关系。这些计算方法方便了依赖关系正确性的证明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILibeDCupDHszgiaTZyjwnytNSWhw0DibfejcicgScR8A6jkNTbKoqT2L1NQ/640?wx_fmt=png&from=appmsg)

图3 GPTEE PP安全元素与依赖关系图

ProveriT采用参数化建模方式，高度抽象，能在不同底层硬件架构（如TrustZone、Intel SGX等）上的TEE中得到应用。TEE开发人员可以直接扩展和实例化该模型，以确保其TEE的安全性或辅助CC认证。在ProveriT中，整个GPTEE PP被分解为数据模型、四个安全层及其依赖关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILENgDXxh4G94VZJcicwutnBLZl0DMrSOuZHwK9EibwYicZTkTWul7af0rw/640?wx_fmt=png&from=appmsg)

图4 威胁层状态机模型

SPD中的安全资产被形式化为数据模型。不同抽象层次的TEE系统被形式化为三个状态机，即威胁层状态机TSM、安全目标层状态机OSM和需求层状态机RSM。数据模型和状态机作为四个安全层的基础（即威胁层、安全目标层、高级组合层和需求层）。GPTEE PP中的威胁被形式化为模块，并与TSM一起构成威胁层。一个模块包括声明操作或数据类型的局部参数和限制系统行为的约束。SOs被指定为独立模块，与OSM一起构成安全目标层。SFRs引入了具体概念，例如主体和对象，并包含访问控制和信息流政策，从而更加复杂。ProveriT将每个SFR建模为独立模块，这些模块与RSM一起构成需求层。直接验证SOs和SFRs之间的依赖关系既复杂又容易出错。因此，高级组合层（HCL）旨在减轻证明负担。HCL将相同目的的SFRs组合成HCL SFRs，这些SFRs也依赖于RSM。

在形式化规范中建模每个安全元素后，该工作利用ProveriT的组合框架展示了它们的依赖关系。需求层的特定SFRs通过横向计算组合成HCL SFRs，其关系通过纵向计算表示。使用相同的方法，HCL中的模块被组合以满足安全目标层中的模块，安全目标层中的模块被组合以防止威胁。一个SFR或SO可以多次组合以覆盖其上层中的不同模块。此外，还存在状态机之间的精化关系，即RSM精化OSM，OSM精化TSM。通过逐步验证，ProveriT确保了GPTEE PP的正确性。

**实验评估**

通过对MiTEE的验证，研究人员不仅验证了ProveriT模型的可行性，还展示了如何利用该模型进行实际TEE产品的安全验证。这一过程包括定制安全模型、实例化模型以及验证模型与实际实现之间的一致性，为TEE产品的开发和验证提供了一个明确的流程和方法。研究人员在Isabelle/HOL中指定并验证了GPTEE PP。所有推导都通过了Isabelle的证明内核。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HUlosUWK3AicmcFHo0iavSILeuUL1maNExUY3dLAJ1EgaUjPicd19fTtPWe9QKrCdkple1a9y885A3Q/640?wx_fmt=png&from=appmsg)

图5 规约与证明代码统计

在验证安全元素之间依赖关系正确性的过程中，研究人员发现了GPTEE PP中的8个问题。这些问题被归为两类：(1)单一推导规则的不满足，即某个SFR中的描述不满足某个SO依赖关系中的特定推导规则，或者某个SO中的描述不满足某个威胁依赖关系中的特定推导规则；(2)依赖关系推导规则的不完整，即SO或威胁依赖关系中的推导规则不完整，SO依赖关系中的SFR或威胁依赖关系中的SO不完整。

在反馈给GlobalPlatform官方后，GP确认了这些漏洞并且将在下一个PP版本中解决这些问题。未来，ProveriT有望在更多类型的TEE产品中得到应用，而不仅限于MiTEE。研究团队计划进一步扩展和完善ProveriT模型，使其能够应对更加复杂和多样化的安全需求。此外，研究人员还将探索如何利用机器学习和人工智能技术，提升ProveriT模型的自动化验证能力和效率，为TEE安全保障提供更为强大的技术支持。

论文下载：

https://ieeexplore.ieee.org/abstract/document/10465667/authors#authors

投稿作者简介：

胡霁林，2021级浙江大学计算机科学与技术学院直博生，本科毕业于西安交通大学物理试验班，导师为赵永望老师。研究方向为形式化验证和操作系统安全。

赵永望，浙江大学计算机科学与技术学院/网络空间安全学院教授,研究兴趣包括形式化方法、操作系统、安全认证等。

个人主页：https://lvpgroup.github.io/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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