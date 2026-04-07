---
title: 周一| 论文/资料精选：大语言模型安全框架
url: https://mp.weixin.qq.com/s/V2d-omfoYzHi21jKqCVcuA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:29:16.639678
---

# 周一| 论文/资料精选：大语言模型安全框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z0u4bSRUopMIaSIaV9OQFkGVYGricMCBicdd579cniaHkyD197P0CSjpdzy3H32LC0l1vviaiacJMTfpicc3VrGXB8d6Z8BPIYyAUkfjsSxGwXH2w/0?wx_fmt=jpeg)

# 周一| 论文/资料精选：大语言模型安全框架

原创

t0data铁马
t0data铁马

AI安全圈

![]()

在小说阅读器中沉浸阅读

美国国家标准与技术研究院（NIST）在其发布的《大语言模型网络安全》专章中，系统性地阐述了构建 LLM 安全、可靠与可信层的现有及新兴标准。

此举为全球 AI安全治理，提供了首个由政府权威机构背书的顶层设计蓝图，旨在解决大模型在透明性、可解释性及抗攻击性方面的核心挑战，为大模型的安全对齐与部署设立了明确的“技术基线”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z0u4bSRUopOlgKEH2Hib2MNxObFblEicVfwmiaJ6qibH1oTFrGxjtlSpqK9HO10Ipf6syYdsVOdnO2ia3NC8AFYm8RJeQIzZ4EQJpRVNjwEBGcxI/640?wx_fmt=png&from=appmsg)

*(图像源：NIST AI RMF)*

## ● 大模型的安全防御严重滞后于AI能力的增长

当前，大模型的安全防御严重滞后于其能力的指数级增长。

攻击者利用提示注入、越狱、数据投毒等新兴攻击面，能够轻易绕过基于规则和静态过滤的传统安全护栏。

行业普遍面临“攻易守难”的困境，缺乏统一的漏洞定义、评估标准和缓解措施指导。

**第一大核心痛点是“漏洞定义的缺失”**。与传统软件拥有 CVE（通用漏洞披露）体系不同，大模型的“漏洞”形态多样（如越狱提示、对抗性样本），其严重性、影响范围和修复方式尚无公认标准，导致安全响应碎片化。

**第二大核心痛点是“风险管理框架的空白”**。尽管各方都意识到 AI 风险，但如何将“治理”转化为开发生命周期中可“测量”和“管理”的具体动作，缺乏可操作的技术标准。这导致安全建设要么流于形式，要么因严重影响性能而被搁置。

![AI 风险管理成熟度对比](https://mmbiz.qpic.cn/sz_mmbiz_jpg/z0u4bSRUopOicmUXNKZcKVbDkRnYSjDFNHtjtBMza0jjGHVtic5ibRFBYuzLIy5I93KNTcqtWts7KRkP9OWlBA0UsnJW8Yl3xF39g92LRoqP8A/640?wx_fmt=jpeg&from=appmsg)*(图表源：示意图，传统 IT 安全与 AI 安全治理成熟度差距)*

## ● 全新的大模型架构与防御机制

NIST 标准框架的核心在于将传统网络安全领域的成熟方法论，适配并引入大模型安全治理体系，构建从威胁建模到持续监控的闭环。

**第一步：借鉴 ATT&CK 框架，构建 LLM 专属攻击技战术库**。 标准建议将 MITRE ATT&CK 和网络杀伤链模型进行扩展，用于系统化描述针对 LLM 的提权、数据泄露、模型窃取等攻击链，为红蓝对抗和威胁狩猎提供统一语言。

**第二步：建立贯穿生命周期的 AI 风险管理框架（AI RMF）**。该框架围绕“治理、映射、测量、管理”四大功能，要求组织在模型设计之初就明确风险容忍度，在开发中持续映射和测量风险，并在部署后建立动态管理机制。其配套的“行动手册”提供了从战略到落地的具体步骤。

## ● 如何使用

为了将这套标准框架落地，企业不能仅将其视为合规文档，而需将其核心思想工程化。

1）**必须建立 LLM 应用资产与威胁的映射图谱**。利用扩展的 ATT&CK 矩阵，对自有 Agent、插件、API 调用链进行攻击面分析，明确每一环节可能对应的战术和技术。

2）**将“测量”环节工具化**。 开发或采购能够对提示注入、越狱攻击、输出一致性等进行自动化测试和评分的平台，将风险量化。

3）**将加密标准（如 NIST 后量子密码标准）前置**，保护训练数据、模型权重及推理交互的机密性与完整性。

对于一线安全团队和厂商而言，这是将安全能力产品化、标准化的历史性机遇。

* **建议具有底层算力的安全厂商提前布局“标准符合性”检测平台**，提供对标 NIST AI RMF 和未来 LLM CVE 的自动化评估与证明服务，成为企业采购的“必选项”。
* **建议中小企业利用其“安全左移”思想进行流程重塑**。在 Prompt 工程、微调、RAG 系统构建的每个环节，嵌入标准要求的检查点，用最小成本构建可信 AI 的合规基线。

**本文参考资料直达：**

---

👉 加入AI安全圈，前沿资料尽享

👉 订阅AI安全日报，获取每日推送

![](https://mmbiz.qpic.cn/mmbiz_png/z0u4bSRUopPxn0mmJhiayU4kCOVF8XgmDic7lDfzleHuKgbS1PxANSVAHSPxG5T4AcX3jQTRH40Jsrundw0DBYIc8L6ebmNhZhtEylN8L8ahM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

AI安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0R80na6wzXdZWBKECSwo8H5S6LNZvXaLNemfgTALpBNqL3VpUlA3mQtwfrEoIh2LHb1zJuv8A5z0Jo60tH7pgw/0?wx_fmt=png)

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