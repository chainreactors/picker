---
title: 国防科技大学 | 通过知识注入保护检索增强代码生成
url: https://mp.weixin.qq.com/s/pJQWd_lRKu063aw15w9NlQ
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:01:17.469282
---

# 国防科技大学 | 通过知识注入保护检索增强代码生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQ88S3agrIibG3aUQDscxafVriboD8qib9ytU0U8kw1mUr6kbhHk6LtMhgw/0?wx_fmt=jpeg)

# 国防科技大学 | 通过知识注入保护检索增强代码生成

原创

龙函城
龙函城

安全学术圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQkBFtNr1YXgG8QaScOK2icGeTxcQK5wuXEufT2pVqDtpibibfNvQrOKjXg/640?wx_fmt=png&from=appmsg)

> *原文标题：Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection*
> *原文作者：Bo Lin, Shangwen Wang, Yihao Qin, Liqian Chen, Xiaoguang Mao*
> *发表会议：ACM Conference on Computer and Communications Security*
> *笔记作者：龙函城*
> *主编：黄诚@安全学术圈*

## 研究概述

检索增强代码生成（Retrieval-Augmented Code Generation, RACG）通过从外部知识库中检索相关代码示例，并将其作为上下文提供给大语言模型（LLMs），从而显著提升代码生成任务中的功能正确性与覆盖能力。然而，现有 RACG 研究大多将关注重点放在功能增强层面，而对生成代码的安全性问题缺乏系统性考虑。在现实软件开发场景中，RACG 所依赖的外部知识库通常来源于开源代码仓库或社区贡献内容，其质量和安全性难以得到完全保障。一旦攻击者向知识库中注入包含漏洞或恶意实现的代码样本，模型在检索阶段便可能将这些不安全示例作为“参考答案”，从而在生成过程中复现甚至放大安全缺陷。已有研究表明，即使仅向知识库中注入极少量投毒样本，也可能显著降低生成代码的整体安全水平，这使得 RACG 成为潜在的攻击放大器。

为应对上述挑战，本文提出 CodeGuarder，其整体框架如图1所示，核心思想并非简单地过滤不安全示例，而是从根本上改变 RACG 的增强方式：将真实漏洞中的安全知识显式引入生成过程，对模型进行“安全课程式”的知识注入（Knowledge Injection）。通过将漏洞根因与修复模式结构化为可检索的安全知识，CodeGuarder 在生成阶段对模型施加安全约束，使其在满足功能需求的同时，更倾向于生成安全实现，从而实现功能正确性与安全性的协同优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WEkpibswMXJXnqApQUUIpYSQ9jDIR0qlyUbCf61vM5HsnCTwuDFeufUR7Fv6F4t4FKFic7tmDKNYu5g/640?wx_fmt=png&from=appmsg)

*图 1 CodeGuarder 整体框架*

### （1）离线阶段：安全知识库构建

在离线阶段，CodeGuarder 基于 ReposVul 数据集中真实世界漏洞样本，自动构建安全知识库。ReposVul 提供了函数级别的“漏洞代码—补丁代码”配对数据，能够准确反映漏洞产生原因及其对应的修复方式。针对每一组漏洞样本，作者设计了一种结构化安全知识表示形式，将其组织为以下三部分：

* **功能描述**
  通过大语言模型对漏洞代码进行语义理解，提取其功能层面的描述信息，用于缩小用户生成需求与漏洞知识之间的语义差距。
* **漏洞根因**
  包含漏洞产生的原因说明及对应的不安全代码示例，用于帮助模型识别高风险实现模式，如不安全 API 调用、边界检查缺失或资源管 理错误。
* **修复模式**
  提供修复思路说明与安全代码实现示例，为模型提供明确的安全替代方案，从而在生成阶段直接引导其输出更安全的实现。

### （2）在线阶段：代码安全强化

在在线生成阶段，CodeGuarder 针对每个用户生成请求执行代码安全强化流程，具体流程包括：

1. **Query细粒度分解**
   将原始生成请求拆分为多个子任务，以识别程序中潜在的多个安全风险点，例如内存管理、字符串处理或输入校验等。
2. **安全知识检索**
   针对每个子任务，从安全知识库中分别检索语义相关的安全知识条目，确保不同风险点均获得对应的安全指导。
3. **安全知识的重排与过滤**
   考虑到大模型上下文长度有限，作者引入基于漏洞易感度的重排策略，利用不同漏洞类型在 LLM 生成中出现频率的统计信息，对安全知识进行风险加权，优先保留高风险、高价值的安全信息。
4. **安全增强代码生成**
   将筛选后的子任务与对应安全知识拼接至最终 prompt 中，引导模型在生成过程中主动规避不安全实现，并采用推荐的修复模式。

## 贡献分析

* **贡献点1**
  论文提出了CodeGuarder，一种面向 RACG 系统的先进安全加固框架。该框架通过在生成阶段显式注入安全知识，有效缓解了由不安全检索示例或投毒知识引发的安全风险。同时，CodeGuarder 在显著提升生成代码安全性的同时，能够较好地保持代码的功能正确性，实现了安全性与可用性的平衡。
* **贡献点2**
  作者在多种复杂场景下对 CodeGuarder 进行了系统而全面的实验评估，包括标准 RACG 场景、两种不同的 RACG 知识库投毒设置，以及直接代码生成任务。实验结果表明，CodeGuarder 在不同模型、不同任务形式下均表现出显著的安全提升效果和良好的泛化能力，验证了该方法在多种实际应用场景中的稳健性与有效性。

## 代码分析

代码链接：https://zenodo.org/records/16957113

1. **使用类库分析**：CodeGuarder 的代码实现主要基于Python 生态的开源类库与工具链，整体属于“开源安全工具集成 + LLM 调用 + 脚本化复现”的工程形态，不依赖闭源核心组件。从复现实验工件可以看出，其主要依赖包括：

* **Python 标准库**：用于脚本调度、配置管理与实验流程控制；
* **静态安全分析工具链**：集成正则规则与 Semgrep 规则，用于对生成代码中的不安全模式进行检测；
* **大语言模型接口**：通过统一配置方式调用在线或本地部署的代码大模型（如 DeepSeek-Coder、CodeLlama 等）；
* **评测工具**：用于统计 Security Rate（SR）与 CodeBLEU 等指标。

整体依赖体系以成熟开源工具为主，工程实现具备良好的可复现性与可扩展性。

2. **代码实现难度与工作量评估**：从实现复杂度来看，该项目的实现难度处于中等偏上水平，工作量较大。其难点不在于单一模型或算法实现，而在于需要支撑一个完整的 RACG 安全加固与评测框架，具体体现在：

* 需要同时支持标准 RACG、知识库投毒等多种实验场景；
* 需要适配不同代码生成模型与调用方式；
* 需要将安全检测、指标统计与实验复现流程进行工程化封装。

总体而言，该代码并非简单的实验脚本，而是面向论文评测设计的系统性工程实现。

3. **代码关键实现功能**：结合代码结构与复现实验说明，其核心功能可概括为以下4个模块：

* 实验调度与复现模块：通过脚本统一组织不同模型、不同实验场景下的生成与评测流程，保证论文结果的可复现性。
* 模型调用与配置管理模块：负责管理大语言模型的调用接口与参数配置，支持在线 API 调用与本地模型部署两种方式。
* CodeGuarder模块：实现论文提出的安全知识注入机制，在代码生成阶段将安全相关信息显式注入 prompt，以降低不安全代码生成风险。
* 生成代码安全检测与评估模块：基于正则规则与 Semgrep 规则，对生成代码中的不安全模式进行扫描，并据此统计 Security Rate 等安全性指标。

从代码层面来看，CodeGuarder 更强调安全加固框架的工程落地与评测复现，而非复杂模型结构设计。其实现思路清晰，模块划分明确，具有较高的工程参考价值。

## 论文点评

总体来看，本文围绕RACG场景下的安全问题，提出了一个具有明确工程背景和现实意义的研究方向，并通过 CodeGuarder 框架给出了较为系统的解决思路。

优点方面。论文选题具有较强的前沿性与实用价值。随着 RACG 在实际软件开发中的广泛应用，其对外部知识库的依赖使得安全风险被显著放大，而现有工作大多关注功能正确性，对安全威胁缺乏系统建模。本文将“知识库投毒”作为核心威胁模型进行研究，问题定义清晰，贴合真实应用场景，具有较高的研究与工程参考价值。同时，作者提出通过显式安全知识注入的方式对生成过程进行约束，而非单纯依赖事后检测或过滤，在方法设计上具有一定创新性和启发意义。

在方法实现上。CodeGuarder 并未引入复杂的模型结构修改，而是以 prompt 级安全加固为核心，结合真实漏洞知识进行引导，具有较好的通用性和可扩展性。从实验与代码实现来看，该框架能够适配不同模型与不同 RACG 设置，体现了方法在实际落地层面的可行性。

不足之处。主要体现在安全知识来源与泛化能力方面。CodeGuarder 所依赖的安全知识库主要来自已有漏洞数据集，其覆盖范围和时效性在一定程度上受限，对于新型漏洞模式或特定领域代码的适应能力仍有待进一步验证。此外，安全知识注入的效果在一定程度上依赖于检索与排序质量，当查询理解或安全知识匹配不准确时，防护效果可能受到影响。

总体而言，本文在 RACG 安全方向上迈出了具有代表性的一步，为后续研究提供了清晰的问题建模思路和工程化参考方案。其核心思想对于从事代码生成安全、RAG 系统安全以及 LLM 应用安全研究的工作具有较强的借鉴价值。

## 论文文献

Lin B, Wang S, Qin Y, et al. Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection[C]//Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security. 2025: 3356-3370.

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

---

**专题最新征文**

* [期刊征文 | 暗网抑制前沿进展](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491610&idx=1&sn=8b6c9caf92435cbd9b76b77686619972&scene=21#wechat_redirect) (中文核心)
* [期刊征文 | 网络攻击分析与研判](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491661&idx=1&sn=ab0a97741cdf854757ef3024b03f1d44&scene=21#wechat_redirect) (CCF T2)
* [期刊征文 | 域名安全评估与风险预警](https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491703&idx=1&sn=7f351031fc81e1b63d5215ddb8dc91b5&scene=21#wechat_redirect) (CCF T2)

  ---

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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