---
title: 前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day
url: https://www.4hou.com/posts/6MAV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-24
fetch_date: 2025-10-06T22:27:36.393916
---

# 前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day

前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day

企业资讯
[技术](https://www.4hou.com/category/technology)
2025-05-23 15:40:42

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)145534

收藏

导语：本篇为《深蓝洞察》系列最新技术专栏「前瞻对抗」的首篇。

正如 DARKNAVY 在深蓝洞察 | 2024年度最具想象空间的新应用所展望的：

新一代的 AI Agent 将具备优秀的推理能力和泛化能力，并能熟练地运用多种安全研究工具，继承大量的人类专家经验，如同顶尖的安全专家一般，发现现实世界中更多的 0day 漏洞。

不出所料，随着大语言模型 (LLM) 对复杂任务处理能力的日益增强，智能体技术 (Agent) 正在成为漏洞挖掘领域的新型范式。随着去年 Google Project Zero 团队推出了 Naptime[1]，越来越多的 Agent 审计工具正在涌现，通过为 LLM 提供必要的工具集和待测源码，模拟安全研究员的行为进行代码审计与漏洞确认。

然而，DARKNAVY 观察到单个 Agent 在审计中大型项目时，常因 LLM 推理能力的局限性（如逻辑不完整、幻觉现象）导致误报与漏报。DARKNAVY 基于多年实际漏洞挖掘经验，提出了 multi-agent 系统架构，通过模拟安全团队内部的分工与协作机制，实现了全自动漏洞挖掘工具 Argusee。

在对 Linux USB 协议栈源码的测试中，Argusee 在短时间内便发现了一个自 Linux 6.5 版本引入的高危漏洞，该漏洞已获编号 CVE-2025-37891 并得到修复，影响了包括 Ubuntu 和 Arch Linux 在内的多个主流发行版。DARKNAVY 对该漏洞进行利用开发后得到了一个在 Arch Linux 上稳定提升至 root 权限的利用脚本。

本篇为《深蓝洞察》系列最新技术专栏「前瞻对抗」的首篇。

**Argusee：多智能体协同架构**

Argus had a hundred eyes round his head, that took their rest two at a time in succession while the others kept watch and stayed on guard.

— Ovid: The Metamorphoses

尽管 Naptime 等单 Agent 工具为 LLM 驱动的代码审计提供了可用范式，但在面对中大型项目时，往往因模型推理逻辑不够严谨、上下文感知有限而产生较多误报与漏报，且难以灵活调整审计流程，难以满足对精准定位和深度验证的需求。

对此，**Argusee 并非旨在完全取代人工审计，进行从零开始的漏洞挖掘**，而是作为安全审计人员强大的辅助工具，依赖于审计人员提供精确的分析入口（如特定的函数或代码模块）及必要的上下文信息，在此基础上进行深度分析与潜在风险识别，从而大幅提升专业审计人员的工作效率。

与现有工作不同，Argusee 的核心创新在于其多智能体协同机制，其借鉴了人类安全团队的协作模式，将复杂的审计任务分解给不同角色的智能体。更重要的是，相较于一些早期多智能体探索[2]中各智能体功能相对独立、交互固化的方式，Argusee 赋予了 LLM 更大的自主权，使其能够动态地进行任务理解与分派，从而实现更灵活和高效的协同审计。这正对应了强化学习之父 Richard Sutton 在 The Bitter Lesson 一文中所写到的：「我们希望人工智能 Agent 能够像我们人类一样去发现，而不是在系统里集成我们已经发现的东西。建立在我们已知发现之上只会让我们更难看到如何完成发现过程。」

作为一个实现原型，Argusee 的架构如下图所示，主要包含以下核心智能体：

![微信图片_2025-05-23_152638_001.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747985478214703.png "1747985259143122.png")

Argusee 原型框架图

**1.管理者 Manager Agent**

Manager 是用户的交互点，用户向其提供分析入口（如目标文件或函数）。Manager 负责从宏观层面理解任务，例如，判断函数核心功能，识别潜在的关键代码段，并进行任务分解与分派，将不同的代码片段连同必要的上下文信息分发给多个 Auditor。

**2.审计员 Auditor Agent**

Auditor 专注于分析来自 Manager 分配的、通常较为短小的代码片段。它们结合上下文信息，深入挖掘代码细节中可能存在的漏洞，如 Buffer Overflow，Use After Free 等漏洞。

**3.校验者 Checker Agent**

为了降低误报和漏报，Manager 在汇总审计结果并输出最终结论前，会请求 Checker 对整个逻辑链条进行复核与验证，查漏补缺。最终，由 Manager 整合信息并输出审计报告。

各 Agent 在执行任务过程中，均可按需调用预设的工具集，工具的使用时机和方式皆由 Agent 自主决策。另一方面，后端工具集的有效运行依赖于对目标项目和环境的适配，例如，源码阅读器 (Code Reader) 的变量定位功能依赖于后端语言服务协议 (LSP) 所建立的源码索引功能。

为了更好的理解 Argusee 的工作流程，下图展示了 Argusee 在实际运行过程中的思维链条：

![微信图片_2025-05-23_152753_409.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747985480142952.png "1747985348161757.png")

Argusee 在某次实际运行时的简化工作流程

用户在指定目标文件和入口函数的情况下，Manager 通过分析将任务分派给了两个 Auditor，其中一个 Auditor 发现了一处疑似缓冲区溢出风险并报告给了 Manager。随后，Manager 请求 Checker 对该漏洞进行了复核，最终确认这是一处真实存在的堆缓冲区溢出漏洞，并产出了漏洞审计报告。

**实战测试与效果评估**

为验证 Argusee 的有效性，我们分别在基准测试数据、中小规模开源项目和超大规模开源项目（如 Linux 内核）上对其进行了测试评估。

**基准数据集测试**

在来自 META CyberSecEval 2[3] 的单文件标准测试用例中，Argusee 展现出接近完美的漏洞识别能力，在 Buffer Overflow 等类别的测试用例上达到了 100% 的准确率。

**中小规模开源项目实战审计**

针对中等规模的真实世界开源项目，Argusee 同样取得了显著成果，在多个经过充分测试的项目中累计发现了 15 个先前未知的安全缺陷，测试项目涉及到 GPAC、GIFLIB 等多个解析复杂文件格式的开源软件库。

以开源多媒体框架 GPAC[4] 为例，该项目长期经受 Fuzz 测试，近年来被发现的新漏洞相对较少。然而，Argusee 在短时间内便识别出数个较难通过传统方式发现的新漏洞。DARKNAVY 观察到，对于 GPAC 这类输入格式明确、以内容解析为核心功能的目标，Argusee 的表现尤为突出。

例如，下图代码是 Augusee 发现的一处整数溢出造成的内存破坏漏洞。对于 Fuzzer 而言，要构造出能够触发此漏洞（需满足 zlib 压缩格式且原始数据足够大以引发溢出）的输入样本难度极高。而 Argusee 通过模拟人工审计的逻辑推理过程，成功定位了这一深藏的缺陷。

![微信图片_2025-05-23_152925_491.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747985482706678.png "1747985417664528.png")

Argusee 在 GPAC 中发现的内存破坏漏洞代码

**Linux Kernel 实战审计**

除此之外，Argusee 也针对体量庞大的代码项目进行了尝试，例如 Linux Kernel USB 协议栈这类庞大且复杂的项目。在使用过程中，尽管需要为 Agent 提供更丰富的上下文信息，Argusee 在代码的辅助理解、高风险区域定位等方面依然表现出强大的潜力，能够显著提升研究人员的审计效率。

下图为 Argusee 在 Linux Kernel USB 协议栈中找到的漏洞 CVE-2025-37891[5]：

![微信图片_2025-05-23_153044_899.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747985482263219.png "1747985482263219.png")

CVE-2025-37891 的修复补丁

该漏洞发生在 Linux 内核 USB 的主机侧，恶意用户可以通过插入支持 USB MIDI2 协议的模拟设备来进行攻击。对于支持 MIDI2 的 USB 设备，Linux 内部会将 MIDI1 包转换成 UMP 包，由于长度检测不当，转换时用来存储 MIDI 字节流的缓冲区可以发生溢出，使得攻击者获得内核堆上任意溢出的原语。Augusee 被指定 USB MIDI2 入口点相关函数与文件后，迅速找到了此漏洞并提供了清晰的漏洞原理分析与复现。

当然，Argusee 的能力不止于此。鉴于构建全面的漏洞挖掘能力评估数据集及衡量标准本身是一项复杂工作，更细致的量化评估以及实战测试结果将在后续的研究中呈现。

展望未来，为了进一步释放 Argusee 的潜力，基于当前原型，Argusee 还可以围绕以下三个维度进行增强补充：

**Agent 系统**：引入更多专业角色，如负责构造 PoC 以验证漏洞的复现者 (Reproducer Agent)，以及评估漏洞可利用性并尝试编写 Exploit 的利用者 (Exploit Agent)。

**工具集**：集成更丰富的分析工具，如调试器，帮助 Agent 理解程序执行流和漏洞触发过程，以及其他高级静态、动态分析工具等，构建强大的武器库。

**目标项目与环境**：整合更多辅助代码审计的信息源，如利用 RAG 技术检索相关源码知识、分析编译后的二进制文件等。

**结语**

智能体技术正深刻变革漏洞挖掘的既有范式，而 Argusee 的实践证明，多智能体协同是提升代码审计效率的有效途径。赋予 LLM 合适的结构与工具，结合人类研究员的经验，更高效地自动化发现漏洞，其潜力远超单体智能的局限。

此趋势下的探索，Argusee 仅是起点。DARKNAVY 致力于深化智能体协同安全研究，让 AI 智能体与安全专家无缝协作、各展所长，共同构筑稳固的数字防线。

或许某一天，在这场智能体引领的变革中，安全人员将从繁重的低级审计工作中解放，更多聚焦策略设计与风险评估；当经验与创见得以释放时，又能推动安全研究达到怎样的新高度？

**参考：**

[1] <https://googleprojectzero.blogspot.com/2024/06/project-naptime.html>

[2] <https://arxiv.org/html/2409.00899v2>

[3] <https://arxiv.org/abs/2404.13161>

[4] <https://github.com/gpac/gpac>

[5] https://git.kernel.org/stable/c/ce4f77bef276e7d2eb7ab03a5d08bcbaa40710ec

**预告**

AI会有一天取代白帽黑客吗？6月16日，专注纯粹技术交流的全新网络安全闭门沙龙 deepsec.cc (Deep Security Closed-door Conference)，DARKNAVY 将在现场继续深入探讨 Argusee。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4qoFIR22)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

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

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典...