---
title: 华中科技大学开源俱乐部师生论文获CCF-A类安全顶会 NDSS 录用
url: https://mp.weixin.qq.com/s/qVuJRTrR_pwjzEZLbakGlg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:53:25.961271
---

# 华中科技大学开源俱乐部师生论文获CCF-A类安全顶会 NDSS 录用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsNickAI6APc3lV2z7c1skjfUvRW584icaSpBLX6iabwyHLr4rO4Us8fcjVRiahkibyNJhmnYencYMqHNwLw/0?wx_fmt=jpeg)

# 华中科技大学开源俱乐部师生论文获CCF-A类安全顶会 NDSS 录用

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

以下文章来源于开源内核安全修炼
，作者胡崟昊

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7U23dhib9UH4pvdTYPu8icSXZnGDXDgnIkHIEwvlUQDL6Q/0)

**开源内核安全修炼**
.

华中科技大学开放原子开源俱乐部（https://hust.openatom.club/）官方公众号，主要用于俱乐部活动宣传，HCTT译文推广，安全漏洞或事件分析等。

## 会议介绍

Network and Distributed System Security Symposium（NDSS） 是由国际互联网协会（ISOC）主办的网络与分布式系统安全领域的顶级学术会议。作为安全领域“四大顶会”之一，同时也是中国计算机学会推荐的 A 类国际学术会议（CCF-A），NDSS 长期代表着全球网络与系统安全研究的前沿方向，汇聚了来自学术界与工业界的众多顶尖研究人员和实践专家，以其高水平的学术质量和严格的录用标准备受国际社会关注。NDSS 2026 Cycle 2 共收到950篇投稿，最终录用152篇，录用率仅为16%。

本期，由华中科技大学网络空间安全学院联合中关村实验室、美国西北大学、武汉金银湖实验室等单位合作完成的学术论文《SoK: Take a Deep Step into Linux Kernel Hardening Effectiveness from the Offensive-Defensive Perspective》已被 NDSS 2026 正式录用。论文由华科大开源俱乐部指导老师****慕冬亮****老师指导，俱乐部****胡崟昊****同学为第一作者，****丁鹏宇****同学为第二作者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K8s1Ua2qgL9sPhG1iaqA1FRMdrm9y1jzzpffnzKRYsOD38wbGWR81qMvHmicsO8BOibicSZ93cHDVmGUkGCzmjiaYFA/640?wx_fmt=png&from=appmsg)

## 论文简介

Linux 内核作为支撑全球绝大多数服务器、超级计算机以及众多发行版（如 Ubuntu、Debian、Fedora）的核心基石，其安全性至关重要。然而，尽管内核社区（如 KSPP 项目）和安全厂商投入了大量精力部署各种缓解机制，Linux 内核依然面临着持久且复杂的内存安全漏洞威胁。现有研究的局限性在于，缺乏从攻防视角对这些缓解措施有效性的系统性评估：研究人员往往难以确切知晓现有的防御究竟覆盖了哪些攻击路径，以及它们在面对不断演进的利用技术时是否依然可靠。

因此，本工作从****攻击者、防御者与发行版厂商****三方视角出发，对 ****Linux 内核加固的有效性进行了深度剖析****。为了实现这一目标，本文首先提出了****首个 Linux 内核利用系统化分解框架****，将复杂的内核利用过程拆解为多个通用步骤。基于该框架，我们详尽分析了 2015 年以来的 ****121 个公开漏洞利用****，识别并归纳了 ****64 种常见攻击向量****。在此基础上，本研究深度评估了 ****51 种主线内核防御机制****的防御边界与局限性（例如，发现 23 种攻击向量完全未受保护，31 种防御机制可被绕过）。此外，为了评估防御机制在真实生产环境中的有效性，本文还进一步调研了 ****10 个主流 Linux 发行版****的实际部署策略，揭示了理论安全设计与实际落地之间的巨大差距。

具体来说，本文的主要贡献可以归纳为以下三项工作：

1. ****系统化攻击分解框架****：提出了一种从攻击者视角出发的可扩展框架，将内核利用过程划分为“从内部错误到内存破坏”、“从内存破坏到利用原语”、“从原语到利用目标”三个关键阶段，为理解和评估内核漏洞利用提供了统一的基准。
2. ****多层次内核加固分析****：基于上述框架，对 51 种主线内核缓解机制进行了全面评估，通过将防御措施精确映射到具体的攻击向量，揭示了每种机制的防御覆盖面、局限性及防御间的相互作用（如冗余或互补关系）。
3. ****主流发行版内核防御策略的现实部署调研****：通过评估 Ubuntu、Fedora、Arch 等 10 个主流 Linux 发行版的默认内核配置，揭示了理论防御设计与实际部署之间的显著差距，指出了部分发行版存在的配置缺陷，并为开发者和安全从业者提供了改进建议。

---

### **攻击分解框架**

****研究范围****: 聚焦于由****软件内部错误****（如竞争条件、溢出等）引发的内存破坏漏洞，这类漏洞占据了内核 CVE 的 70%.****威胁模型****: 假定攻击者为****本地非特权用户****，旨在利用内核漏洞提升权限，不包含侧信道或物理攻击。****数据集收集****: 收集并整理了自 2015 年以来的 ****121 个公开利用****（涵盖 102 个漏洞），基于真实攻防数据提出了一个系统化的****三阶段攻击分解框架****。

#### **框架概览与攻击向量图谱**

首先，本研究从****攻击者视角****切入，构建了一个通用的内核利用分解框架。通过将复杂的利用过程抽象为三个连续阶段，我们细化出了 ****64 种具体的攻击向量 (Attack Vectors)******。该框架以图论的形式，清晰地展示了攻击步骤之间的******前置错误条件（pre-exploit errors）**** 与 ****后置利用结果（post-exploit consequences）****，即前一阶段的输出如何成为下一阶段的输入，从而描绘出完整的攻击链条。

通过对后续缓解机制的细致分析，我们根据这些攻击向量分为三类：：1）****完全阻断（Fully Blocked）****：现有防御机制可完全阻断的向量；2）****部分阻断（Partially Blocked）****：可部分绕过现有防御机制的向量；3）****无法缓解（Unmitigated）****，即我们评估的任何主线内核缓解机制都无法应对的向量。此外，我们还量化了每类向量的数量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K8s1Ua2qgL9sPhG1iaqA1FRMdrm9y1jzzSnv8BzFj7DvtF2QBzpGXbP1gYmwoK0hQFaMIwaFLyJRG5jCYUyyOhw/640?wx_fmt=png&from=appmsg)

#### **攻击阶段详解**

* ****阶段 I：从内部错误到内存破坏 (Internal Error To Corruption)****

+ 前置条件：攻击者触发内核逻辑中的内部错误（Internal Error），如引用计数不平衡错误等 。
+ 后置结果：造成初始的****内存破坏 (Memory Corruption)**** ，具体表现为栈破坏、堆破坏或全局/静态区破坏 。
+ 实例：以 ****Error 8: Reference Miscounting (CWE-911)**** 为例，攻击者利用引用计数管理不当（如遗漏增加或错误减少计数），导致对象被过早释放。这一错误直接导致了 ****Use-After-Free (UAF)****   ，从而造成堆内存破坏（Heap Corruption）。

* ****阶段 II：从内存破坏到利用原语 (Corruption To Primitive)****

+ 前置条件：初始的内存破坏能力（通常是不稳定的或受限的）。
+ 过程：攻击者通过 ****堆风水/堆布局操控**** 等手段，将初始受限的内存破坏转化为原语操作，提升其漏洞破坏能力。
+ 后置结果： 获得稳定的****利用原语 (Exploitation Primitives)******。主要分为两类：******指令指针控制 (IP Control)**** 和 ****可控内存读写 (Controllable R/W)**** 。

* ****阶段 III：从原语到利用目标 (Primitive To Exploitation Goal)****

+ 前置条件：掌握了稳定的 IP 控制或读写原语 。
+ 过程：利用原语执行 ROP 链、修改进程凭证（如 `struct cred`）或读取敏感数据。
+ 后置结果：达成最终攻击目标，即****权限提升 (Privilege Escalation)**** 或 ****信息泄露 (Information Disclosure)**** 。

#### **关键观察 (Observations)**

基于上述框架对 121 个内核利用的量化分析，本文得出了两项重要观察：

* ****Observation 1：大量未受缓解的向量 (Unmitigated Vectors)****在识别出的 64 种攻击向量中，有 ****23 种****（约占 36%）在主线内核防御体系下****完全缺乏对应的缓解措施****。这意味着一旦攻击者进入相关路径，内核将处于“裸奔”状态 。
* ****Observation 2：高频攻击向量 (High-Frequency Vectors)****攻击向量的分布呈现出明显的集中趋势。研究发现有 ****8 种**** 攻击向量出现在了超过 20 个内核利用中。这其中，****cache内堆布局操控 (Heap manipulation within cache)**** 是最常见的手段之一。此外，针对通用对象（如弹性对象（elastic objects）、页表、凭证结构）的攻击也非常频繁，因为这些目标往往缺乏专门的保护机制。

---

### **内核缓解机制的多维度分析**

其次，本研究转换至****防御者视角****，对内核加固的有效性展开多维度剖析。为了避免将防御视为孤立的技术点，我们将从 KSPP、PaX/Grsecurity 等权威来源收集的 51 种主线内核缓解机制，精确映射到前述的****攻击分解框架****中。这一过程清晰地揭示了防御机制在攻击的三个阶段（从内部错误到最终目标）中阻断特定攻击向量时的覆盖范围与潜在局限。

为了理清防御的设计逻辑，本研究根据防御目标将 51 种内核缓解机制划分为五大类 ：

* ****隔离类保护 (Isolation-based Protections)：**** 旨在隔离特权与非特权空间的数据传输及敏感操作，限制非特权用户的行为。
* ****控制流完整性 (Control Flow Integrity, CFI)：**** 防止非预期的内核代码修改，保障执行控制流的完整性。
* ****数据流完整性 (Data Flow Integrity, DFI)：**** 保护关键变量免受恶意篡改，并确保其使用在预期边界内。
* ****基于熵的保护 (Entropy-based Protections)：**** 增加代码布局、栈/堆布局及敏感结构体的不可预测性（如 KASLR）。
* ****杂项保护 (Miscellaneous Protections)：**** 涵盖防止敏感信息泄露及针对特定漏洞的防御措施。

在此基础上，为了评估这些机制的实际防御能力，本文分析了收集的 121 个内核利用是否能够绕过相应的防御。根据绕过情况，防御有效性被划分为三个等级 ：

* ****有效 (Effective)：**** 在本研究收集的所有内核利用中，没有任何一个能够绕过该机制。
* ****中等 (Moderate)：**** 能够提高利用门槛，但已被部分内核利用绕过。
* ****不安全 (Unsafe)：**** 在本研究中被完全绕过，无法提供可靠防护。

为了直观地展示这 51 种防御机制在攻击分解框架中的****防御覆盖面****（即针对哪些攻击向量）以及具体的****防御有效性****（即是否可被绕过），我们绘制了如下的全景图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K8s1Ua2qgL9sPhG1iaqA1FRMdrm9y1jzzUWgOMsCTDUwOQJA6WYbfQOmHvibkysCJFOx1n8otxKCHkDeeU0obALw/640?wx_fmt=other&from=appmsg)

基于上述多维度的映射分析，本研究得出了几项具有深远影响的观察：

* ****Observation 3：有效的防御 (Effective Hardening)**** ：尽管挑战重重，研究仍识别出了 ****20 种有效防御****。这些机制主要集中在****隔离****和****权限强制****方面（而非随机化）。值得注意的是，部分强大的防御（如 `PAX_RANDSTACK`）虽然有效，但因尚未合入上游主线，导致其在大多数发行版中不可用 。
* ****Observation 4：不完整的缓解机制 (Incomplete Hardening)**** ：在 51 种防御机制中，高达 ****31 种**** 被判定为“中等”或“不安全”。这意味着它们至少可以被一种已知的公开内核利用绕过。研究进一步总结了三种绕过模式：违反防御依赖的不变量（Invariant violations）、破坏防御自身的完整性（Breaking integrity）、以及滥用防御的设计原理（Abusing rationale）。这表明仅依赖现有的单一防御往往不足以应对复杂的攻击。
* ****Observation 6：通用型加固 (Versatile Hardening)**** ：研究发现有 ****12 种**** 防御机制能够同时阻断多个不同的攻击向量。典型的例子是 `SMAP`，它通过广泛地限制内核对用户空间的访问，能够切断多种依赖用户态数据的攻击路径。这类“一石多鸟”的防御机制在提升系统整体安全性方面具有极高的性价比。

---

### **现实环境部署现状**

最后，为了探究理论防御与实际部署之间的差距，本研究转向****发行版厂商视角****。本文深入分析了 ****10 个主流 Linux 发行版****（基于 DistroWatch 排行）在 2023-2025 年间的内核配置快照，旨在考察这些在理论上有效的防御设计，是否真正落地到了真实的生产环境中。

由于现代 Linux 发行版的基础内核配置存在大量重叠，为了直观地揭示不同厂商安全策略的****分歧****，我们引入了下表（Table V）。该表****仅展示了各发行版存在启用差异的关键加固选项****，而非罗列所有配置 。透过这张表，我们可以清晰地看到一个分裂的现状：尽管都是广受使用的“主流”发行版，它们在防御机制的部署上却存在巨大差异，直接揭示了防御机制从****理论安全****到****现实安全****之间的巨大鸿沟 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K8s1Ua2qgL9sPhG1iaqA1FRMdrm9y1jzzCnQ6H6UNPL3PPuAfyf27qic8hj1k612RrTBzAVNbYWiaQZworaWb6kTg/640?wx_fmt=png&from=appmsg)

****基于该表的关键发现：****

1. ****安全分层显著：********Arch Linux Hardened**** 开启的保护最为全面（包括 `init_on_free` 等性能开销较大的选项），稳居第一梯队；****RHEL****、****Fedora**** 和 ****Gentoo**** 紧随其后，在平衡性能与安全方面表现出色 。
2. ****关键配置缺失：**** 令人担忧的是，部分流行发行版存在严重的安全短板。例如，****MX Linux AHS**** 竟然默认关闭了 `KASLR`（地址空间随机化）和 `FORTIFY_SOURCE` 等基础防御，极大地降低了攻击门槛；****openSUSE**** 则禁用了 `HARDENED_USERCOPY`，使其面临更高的越界读写风险 。
3. ****上游与下游的断层：**** 对比发现，仅依赖上游内核的默认配置（`defconfig`）并不足以构建安全的系统。许多关键防御（如 `init_on_alloc`）在上游默认配置中并未开启，完全依赖下游发行版维护者的手动配置。这种依赖关系的脆弱性，是导致不同发行版安全性参差不齐的重要原因 。

## 论文信息

> Y. Hu, P. Ding, Z. Lin, D. Mu, and Y. Li. SoK: Take a Deep Step into Linux Kernel Hardening Effectiveness from the Offensive-Defensive Perspective. In Proceedings of the 2026 Network and Distributed System Security Symposium (NDSS), 2026.

更多有关论文的具体细节，欢迎关注原文。

数据集及论文: https://github.com/OS3Lab/sok-kernel-hardening/

来源：开源内核安全修炼

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcN...