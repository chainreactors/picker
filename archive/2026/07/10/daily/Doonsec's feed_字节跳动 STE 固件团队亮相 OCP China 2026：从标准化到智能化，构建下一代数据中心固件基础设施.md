---
title: 字节跳动 STE 固件团队亮相 OCP China 2026：从标准化到智能化，构建下一代数据中心固件基础设施
url: https://mp.weixin.qq.com/s/0ziaihKvu9yMPYHKMdyCyQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:59:50.155982
---

# 字节跳动 STE 固件团队亮相 OCP China 2026：从标准化到智能化，构建下一代数据中心固件基础设施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FedqyzemfRSTwbZHoIPiaAibN7BkpOZ4oNtIR7n49lO5AuMqFibposbQ8ic8frEz2HhMlCEb0ic1saLTSDGJyvKY4mk81U1zksUOUKSA/0?wx_fmt=jpeg)

# 字节跳动 STE 固件团队亮相 OCP China 2026：从标准化到智能化，构建下一代数据中心固件基础设施

原创

STE 固件团队
STE 固件团队

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在 AI 算力规模爆发式增长的今天，服务器固件——这个曾经隐藏在操作系统底层的"隐形基础设施"——正成为决定数据中心可靠性、安全性和运维效率的关键变量。

2026 年开放计算中国峰会（OCP China 2026）上，字节跳动 STE 固件团队带来了三场技术分享，覆盖了 XPU 模组标准化接口设计、OpenBMC 平台移植的 Agent 框架、以及 RAS API 标准化三大方向。

如果把万卡级智算集群比作一座城市，那么这三项工作恰好回答了三个递进的问题：**如何统一管理城中形形色色的算力设施？如何高效构建承载这些管理能力的固件平台？当规模带来不可避免的故障时，如何快速发现、定位和恢复？**——从**管理接口标准化**到**研发效率智能化**再到**运行可靠性体系化**，三者构成了一条完整的技术闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FefwRF9PgsshHQdmibHibLulcrFuiannJBQwfdCmA50U9BsVDfTvTRpEonhcJaU5GZDCLLlA45Cw9XANtAoSJ6NBL0hDuIebR56ZSA/640?wx_fmt=jpeg&from=appmsg)

图 1：三项工作技术闭环——"管理—构建—运行"

本文将深度解读这三项工作的技术内核，分享字节跳动在服务器固件领域的工程实践与思考。

**一、XPU 模组标准化接口设计：让万卡集群的管理不再是"适配地狱"**

**分享人：郁雷、孙国新 | 字节跳动 STE 固件团队**

**1.1 问题背景：智算时代的 XPU 管理之痛**

随着大模型训练和推理需求的爆发，数据中心中 XPU（GPU/NPU/加速卡）的部署规模急剧增长。单机 XPU 数量已从 4-8 卡增长到 16-32 卡，万卡级集群成为常态。然而，XPU 规模的爆发只是挑战的一个维度——更深层的问题在于**管理的碎片化。**

字节跳动固件团队在实际业务中发现了三大核心痛点：

* **场景复杂：**训练、推理、微调等不同业务场景对 XPU 的监控需求各异，难以用一套方案覆盖。
* **生态分散：**不同厂商的 GPU/NPU/XPU 管理接口差异巨大，运维工具需要为每个厂商单独适配。
* **运维压力：**万卡集群需要自动化、标准化的管理手段，但现有接口能力参差不齐，难以支撑规模化运维。

**1.2 现状分析：监控能力"百家争鸣"背后的适配成本**

团队对主流 XPU 厂商的带外管理能力做了一次系统性的横向对比，结果不容乐观：

|  |  |  |  |
| --- | --- | --- | --- |
| **监控能力** | **厂商 A** | **厂商 B** | **厂商 C** |
| **基础信息（温度/功耗）** | 支持 | 支持 | 支持 |
| **网卡监控** | 支持 | 支持 | 支持 |
| **光链路监控** | 支持 | 不支持 | 不支持 |
| **端口状态（Switch）** | 支持 | 不支持 | 支持 |
| **一键日志收集** | 不支持 | 支持 | 支持 |
| **固件升级接口** | 支持 | 部分支持 | 不支持 |

虽然各厂商基本都遵循 Redfish 标准并提供 IPMI 接口，但在**具体监控能力和功能完整性**上存在显著差异。这意味着，运维工具必须为不同厂商编写不同的解析逻辑，适配成本随厂商数量线性增长。

**1.3 解决方案：统一 Redfish 接口层**

面对这一挑战，字节跳动提出了**"接口与实现解耦"**的核心设计理念：机头 BMC 不区分 XPU 型号，统一使用标准化的 Redfish 接口进行管理。

整体架构采用**分层设计：**

* **管理通道：**Redfish over LAN，作为主通道提供完整的带外管理能力。
* **Sideband 备用通道：**I2C，作为底层控制和应急机制，在主通道不可用时提供基础管理能力。

![](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FecpWxYbZSgZ6jqNLTWNBWlY1CAloV3iape0Sdy0DGgduf6eTogTBYS6XfT4acJYyNNkbsQnJnojel4S4iaZMRnMjWL8ickgbKAdPs/640?wx_fmt=jpeg&from=appmsg)

图 2：XPU 统一 Redfish 管理架构

**1.4 为什么不是 RDE？**

DMTF 提出的 Redfish Device Enablement（RDE）是带外设备管理的行业标准之一，团队在设计方案时对其进行了深入评估：

|  |  |  |
| --- | --- | --- |
| **维度** | **DMTF RDE 规范** | **本方案：Redfish XPU 标准** |
| **协议** | PLDM (MCTP over SMBus/I3C) | Redfish |
| **数据格式** | BEJ 二进制编码 | JSON 明文 |
| **优势** | 标准化程度高，适合通用设备 | 实现简单、易于调试，针对 XPU 场景优化 |
| **劣势** | Schema 不一致，调试困难，带宽受限 | 需定义 XPU 专用 Schema，社区需共同维护 |
| **扩展性** | 扩展需修改 BEJ 映射，成本高 | 扩展只需新增 Schema 文件，成本低 |
| **运维体验** | 不同部件内容不一，运维困难 | 接口统一，运维简单 |
| **适用场景** | 通用 PCIe 设备 | 专注 XPU 管理 |

RDE 在 XPU 场景面临如下关键挑战：

1. **Schema 不一致：**不同 XPU 厂商实现的 RDE Schema 仍有差异，上层仍需差异化适配。
2. **调试困难：**BEJ 二进制编码导致问题排查效率低下。
3. **带宽受限：**MCTP/SMBus 链路带宽有限，难以满足 XPU 场景下高频采集大量传感器数据的需求。
4. **Schema 缺失：**缺乏面向 XPU 特有资源（如 Scale Up Switch、Retimer）的标准 Schema 定义。

RDE 为通用 PCIe 设备管理提供了良好基础，但 XPU 场景需要更聚焦的接口设计。字节跳动的方案选择直接使用 Redfish JSON 明文通信，在可调试性和扩展性上取得明显优势。

**1.5 核心接口规范**

方案定义了一套覆盖 XPU 全生命周期管理的核心 API：

|  |  |  |
| --- | --- | --- |
| **功能分类** | **Redfish URI** | **关键字段** |
| **模组 BMC 状态** | /redfish/v1 | /redfish/v1 |
| **StartupState** | /redfish/v1/Chassis/{id}/Processors/{xpu\_id} | ReadingCelsius, PowerWatts |
| **Switch 端口信息** | /redfish/v1/Fabrics/{id}/Switches/{id}/Ports/{id}/Metrics | BadTLPCount |
| **RNIC 信息** | /redfish/v1/Chassis/{id}/NetworkAdapters/{id} | LinkStatus |
| **Retimer 信息** | /redfish/v1/Chassis/{id}/Retimer/{id} | LinkWidth, LinkSpeed |
| **固件版本** | /redfish/v1/UpdateService/FirmwareInventory/{component} | Version |
| **Bundle 升级** | /redfish/v1/UpdateService/FirmwareFile | UpdateStatus |
| **一键日志收集** | /redfish/v1/Managers/LogService/CollectAllLog | Status |
| **功耗封顶** | /redfish/v1/Chassis/{id}/Power | LimitInWatts |
| **多卡互联** | /redfish/v1/Systems/{id}/Processors/{xpu\_id} | PartitionID |

这套接口设计具有**良好的可扩展性：**新模组只需实现接口集加 OEM 扩展，即可被机头 BMC 统一管理，无需修改上层运维逻辑。

**1.6 开放生态与社区路线**

字节跳动明确表示，XPU 模组标准化接口设计将走**开放、开源社区联合开发**的路线，目标是构建开放共赢的 XPU 管理生态。这不仅有利于行业标准化推进，也为 XPU 厂商提供了清晰的接口规范参考。

**二、超越代码生成：用 Agent 框架破解 OpenBMC 平台移植难题**

**分享人：郏春辉 | 字节跳动 STE 固件团队**

**从管理接口到固件构建：标准化落地的效率瓶颈**

第一节介绍的统一 Redfish 接口层，最终要运行在 BMC 固件之上。然而，每一款新的 XPU 模组、每一代新的服务器平台，都意味着 OpenBMC 固件需要重新移植适配。如果平台移植的速度跟不上硬件迭代节奏，再好的标准化接口设计也无法快速落地。字节跳动固件团队面对的下一个挑战，正是**如何把 BMC 固件的开发效率提升到与万卡集群部署规模相匹配的水平。**

**2.1 OpenBMC 平台移植的痛点**

OpenBMC 作为开源 BMC 固件项目，已被越来越多的数据中心采用。然而，将 OpenBMC 移植到新硬件平台是一项复杂且重复性高的工程——涉及传感器配置、GPIO 映射、FRU 信息、IPMI 命令、Web UI 适配等大量平台特定代码的编写。

传统的移植流程高度依赖资深工程师的经验积累，存在三个突出问题：

* **知识传承困难：**平台移植知识散落在不同工程师的脑中、代码注释里、历史 commit 中，新人上手周期长。
* **重复劳动多：**每个新平台都要从头配置相似的传感器、GPIO、FRU 等信息，已有的经验难以复用。
* **质量不可控：**依赖人工编写配置，容易出错且难以系统性验证。

**2.2 从"代码生成"到"Agent 框架"**

字节跳动固件团队没有止步于简单的"AI 辅助代码生成"，而是构建了一套面向 **OpenBMC 平台移植的 Agent 框架。**这个框架的核心思想是：**将工程师的经验转化为可执行的知识库，让 AI Agent 基于工具链完成平台移植的全流程。**

框架的关键设计包括：

**可执行知识库（Executable Knowledge Base）**

不同于静态文档，可执行知识库将平台移植知识结构化为 Agent 可直接调用的规则和工具。知识库中的每一条知识都关联了具体的执行逻辑——比如 "NVMe sensor 依赖对应的 I2C 通道，DTS 配置中需要添加 mctp 相关属性" 这样的规则，会被转化为 Agent + CLI 工具链生成的配置。

**CLI + Agent 协同**

框架采用 CLI 工具与 AI Agent 协同的工作模式：CLI 工具负责确定性的数据读取和配置生成，AI Agent 负责理解需求、决策流程、调用工具和处理异常。这种"工具+Agent"的组合有效降低了 AI 幻觉风险——Agent 的每一步操作都有工具验证，而非纯粹依赖模型推理。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9Feda53iaiaafeDPzPX5mwF9UcekyLRib5dycQbc7RHr3AbC0YmsHwPEYVNe2dsRibgadB2oZgbhccQkEpSuM9fPcmJQicvGooh9BxF8Y/640?wx_fmt=jpeg&from=appmsg)

图 3：OpenBMC Agent 框架协同架构

**2.3 效果与价值**

这套 Agent 框架在实际使用中取得了显著成效：

* **配置生成速度：**完成一个新平台的配置生成仅需不到 1 分钟。
* **人力成本降低：**累计工作量从过去的人月级降低到不到 2 人周。
* **质量提升：**通过工具链的系统性验证，配置一致性显著提高，减少了人为错误。

更重要的是，这个框架展示了 AI 在基础设施工程中的正确用法：不是用 AI 替代工程师，而是**将工程师的经验沉淀为可执行的知识资产，通过 Agent 框架实现经验的规模化和自动化复用。**

**三、构建开放的 RAS API 标准：为高可用数据中心打地基**

**分享人：龚发强 | 字节跳动 STE 固件团队**

**从构建到运行：规模化带来的可靠性挑战**

当 XPU 管理接口实现了标准化、BMC 固件开发效率大幅提升之后，万卡集群的部署和运维便有了基础保障。但规模本身就是新的风险源——万台设备的集群中，硬件故障不再是"小概率事件"而是"常态"。**问题从"如何建设和部署"转向了"当故障不可避免时，如何快速发现、精准定位、高效恢复"。**这正是 RAS（可靠性、可用性、可服务性）要回答的问题。

**3.1 RAS 标准化的行业迫切性**

在传统 CPU 为主的数据中心时代，RAS 能力已相对成熟。但随着异构计算（CPU + GPU + NPU）成为主流，RAS 面临着全新的挑战。

字节跳动固件团队在业务实践中发现，当前行业 RAS 领域存在一个结构性问题：**不同厂商使用不同的故障上报方案。**

这意味着，当数据中心部署了来自多个厂商的服务器时，运维团队需要对接多套不同的 RAS 接口，故障定位和根因分析的效率严重受限。在万卡级集群中，一个 GPU 故障可能引发训练任务中断，如果不能快速定位和恢复，损失以小时甚至天计。

值得注意的是，这里的"多厂商接口不一致"与第一节中 XPU 管理接口碎片化的问题如出一辙——**标准化缺失是贯穿固件生态的结构性痛点**，无论管理接口还是故障上报接口都未能幸免。

**3.2 推动 RAS API 标准化**

为解决这一问题，字节跳动固件团队在 OCP 社区中牵头推动 RAS API 的标准化工作，从需求定义到接口规范设计均发挥了核心驱动作用，引领异构计算故障管理体系的标准化建设。

RAS API 标准化的目标不是重新发明轮子，而是在**现有厂商方案之上定义统一的接口层**，让上层运维平台可以通过标准化的 API 获取故障信息、触发诊断流程、执行恢复操作，而不必关心底层厂商差异。

**3.3 异构计算时代的 RAS 新挑战**

异构计算的兴起给 RAS 带来了几个全新命题：

**从单节点到跨数据中心**

传统 RAS 关注单台服务器的故障检测和恢复。但在 AI 训练场景中，一个训练任务横跨数百甚至数千台服务器，RAS 需要从**单节点视角升级到集群甚至数据中心视角**——不仅要知道"哪台机器出了什么故障"，还要评估"这个故障对正在运行的任务有什么影响，最优的恢复策略是什么"。

**从 CPU 中心到异构协同**

过去 RAS 以 CPU 为中心，GPU/NPU 等加速卡是"外围设备"。如今 XPU 成为算力主力，RAS 必须覆盖 XPU 的故障检测、错误隔离和恢复，而 XPU 的故障模式与 CPU 有显著差异。

**AI 驱动的故障预测**

基于历史故障数据和运行时遥测信息，利用 AI 技术进行故障预测，是 RAS 演进的重要方向。标准化的 RAS API 为构建统一的数据采集层提供了基础，使得 AI 故障预测模型可以获取到一致、高质量的训练数据。这与第二节中 Agent 框架的理念遥相呼应——**AI 的价值不在于替代人工，而在于将数据转化为可行动的智能决策。**

**3.4 云系统 RAS 演进路线**

字节跳动提出了云系统 RAS 的演进路线，从单节点 RAS 到集群级 RAS，再到跨数据中心的智能 RAS 体系。这条路线的核心思路是：

1. **标准化先行：**协同 OCP 社区推动 RAS API 标准化，统一数据采集和上报接口。
2. **平台化支撑：**构建统一的 RAS 数据平台，汇聚全量故障数据。
3. **智能化闭环：**基于 AI 实现故障预测、自动诊断和智能恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FeeewqNslmcuJj9sV1VUIdEbeBl0CEeuUo0XCgANXjp5sMttXK8EBp9SiaibE2tWQFJG0M62xQJaibmeDYvhXI6IGFu78ian7ibRDGuA/640?wx_fmt=jpeg&from=appmsg)

图 4：RAS 演进路线

**四、总结与展望**

字节跳动 STE 固件团队在 OCP China 2026 上的三场分享，勾勒出了一条清晰的技术路线：

|  |  |  |
| --- | --- | --- |
| **方向** | **核心命题** | **关键成果** |
| **XPU 标准化接口** | 解决多厂商 XPU 管理碎片化 | 统一 Redfish 接口层，社区开放共建 |
| **OpenBMC Agent 框架** | 提升平台移植效率 | 配置生成 < 1 分钟，工作量降至 < 2 人周 |
| **RAS API 标准** | 统一异构计算故障管理 | 定义 RAS API 标准，统一异构故障上报接口 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/FGB4hYw9FecFreKjNXiaNNic0PZsN0O01YdA8Fyjk5dsZyXYPROKjdPrMTpVbbSOcsNRfCHib2dlpUckq7Eh6r6pwYVfYNUiaIQ34bVQIZmYdOU/640?wx_fmt=jpeg&from=appmsg)

图 ...