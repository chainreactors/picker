---
title: 第152期 | GPTSecurity周报
url: https://mp.weixin.qq.com/s/oSGSM5EDjBxhwCo5lku1eQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:45:50.174225
---

# 第152期 | GPTSecurity周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PwkEAAy3OPXiciappoiakIaGS748UDd0ZqiaHDWTRTLEXLctgiciaBKaqaVgwclgUDIEDNRzV3H7x4PSicGTAMk4D9AtDgI1iaAKstKPRhicvcR3FvAI/0?wx_fmt=jpeg)

# 第152期 | GPTSecurity周报

原创

知识分享者
知识分享者

安全极客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/vWuBpewLia8QmTLhv0jB8GS6Wtic69pG44V8Gib7ccD3FZolnOVkdOPafA3YULibw9S5AEkdO8sstRLGNFVDj7SgRg/640?wx_fmt=jpeg&from=appmsg)

GPTSecurity是一个涵盖了前沿学术研究和实践经验分享的社区，集成了生成预训练Transformer（GPT）、人工智能生成内容（AIGC）以及大语言模型（LLM）等安全领域应用的知识。在这里，您可以找到关于GPT/AIGC/LLM最新的研究论文、博客文章、实用的工具和预设指令（Prompts）。现为了更好地知悉近一周的贡献内容，现总结如下。

**Security Papers**

1. VEXAIoT：利用人工智能智能体进行自主物联网漏洞利用

摘要：IoT 系统由于硬件受限、固件老旧和不安全默认配置而普遍存在安全弱点，这促使人们寻求可扩展、自适应的安全测试方法。作者指出，尽管近期 LLM 智能体在渗透测试和 CTF 场景中展现出潜力，但针对 IoT 的应用尚未被探索。他们提出 VEXAIoT——一个自主多智能体框架，将漏洞检测智能体与攻击执行智能体结合，用于对 IoT 服务进行侦察、规划与漏洞利用。在 IoTGoat 和 Metasploitable 环境下、覆盖 OWASP 映射的十种场景进行了评估，攻击成功率高达 100%，Token 开销较低，平均每次攻击不到 2 分钟完成。260 次执行中总体成功率为 95.0%（IoTGoat 94.5%，Metasploitable2 96.7%），显示 LLM 驱动的进攻性 IoT 安全工作流具有自动化潜力。

链接：

https://arxiv.org/abs/2607.09653

2. 利用安全感知工具描述缓解 MCP 服务器中的污点式漏洞

摘要：LLM 越来越多地作为智能体通过 MCP 与工具交互，虽简化集成但也扩大了攻击面。作者分析 MCP 服务器漏洞，发现污点式（taint-style）漏洞占相当比例、修复需大幅改动代码、且社区响应缓慢。他们提出 SPELLSMITH——一种基于文本的方法，用于屏蔽污点式漏洞。它分析 MCP 服务器公开的高风险能力，结合工具描述与参数语义构建工具级风险画像，然后利用协议的 Description 属性和 LLM 自我反思迭代优化输出。实验显示对多种漏洞具有有效缓解与良好泛化性。

链接：

https://arxiv.org/abs/2607.07461

3. SeedSmith：基于LLM的定向模糊测试种子合成

摘要：定向模糊测试瞄准用户定义的 sink 函数，但常无法触发崩溃。存在两大挑战：不完整的间接调用静态分析（隐藏可达路径，使基于距离的引导失效）与缺乏针对崩溃前置条件的语义引导（盲变异难以快速满足）。关键的干预点是初始种子语料——具备正确控制流路径且满足前置条件的种子可将盲目探索转为局部细化。现有方法要么缺乏 sink 感知，要么受一次性提示的静态分析局限。SeedSmith 是一个模拟安全分析师工作流的智能体式 LLM 流水线：从 sink 出发，迭代探索代码、解析间接调用、识别前置条件并合成具体输入。在 Magma 上，几何平均崩溃时间加速比从 11.51× (AFL++) 到 14.66× (AFLGo)；在 ARVO 上，跨 10 个项目触发 16 个先前不可达的漏洞。

链接：

https://arxiv.org/abs/2607.08949

4. SynapseFlow：状态机引导的驱动自动生成

摘要：高质量的 fuzz 驱动是灰盒模糊测试的关键。LLM 显示出自动化驱动生成的潜力，但现有单轮方法因粗粒度函数定位和错位工作流而受幻觉与覆盖缺口困扰。作者提出 SynapseFlow——自动驱动生成器，引入两项创新：数据流感知的函数聚合与分阶段、可回滚的工作流分解。SynapseFlow 分析源码构建结构流图并提取一致的 Function Triplet，再通过分阶段回滚保证正确性的四阶段流程生成驱动。在 25 个真实开源项目上，SynapseFlow 超越 OSS-Fuzz-Gen、CKGFuzzer 和 PromeFuzz，分支覆盖率分别提高 3.07×、1.71× 和 4.26×，漏洞检出率分别提高 1.77×、1.51× 和 1.36×。发现 7 个先前未报告的漏洞（5 个已分配 CVE）。

链接：

https://arxiv.org/abs/2607.07007

5. 思考更多，驾驭更好：基于状态机引导的资源自动生成，结合项目消化和工作流分解

摘要：高质量的模糊测试框架对于有效的灰盒模糊测试至关重要。虽然大型语言模型（LLM）有望实现该任务的自动化，但现有的单轮生成方法由于粗粒度的功能目标和不匹配的生成工作流程，存在着生成结果不理想和覆盖率不足的问题。研究者提出了 SynapseFlow，一种自动框架生成器，它通过两项关键创新解决了这些局限性：数据流感知的功能聚合和分阶段、支持回滚的生成工作流程分解。SynapseFlow 首先分析源代码以构建结构流图并提取连贯的功能三元组。然后，它通过一个由分阶段回滚算法控制的四阶段分解过程来合成框架，以确保其正确性。研究者在 25 个真实的开源软件项目上评估了 SynapseFlow。实验结果表明，SynapseFlow 的性能优于目前最先进的工具（OSS-Fuzz-Gen、CKGFuzzer、PromeFuzz），达到了 3.07 的准确率。×，1.71×，以及 4.26×更高的分支机构覆盖率，以及 1.77×，1.51×，以及 1.36×更高的漏洞检测率。更重要的是，SynapseFlow 发现了 7 个此前未报告的漏洞（其中 5 个已分配 CVE 编号），证明了其在实际漏洞发现中的有效性。

链接：

https://arxiv.org/abs/2607.07007

6. 用于保护与语言模型交互中敏感数据隐私的多智能体防火墙架构

摘要：LLM 是重要的生产力工具，但将其集成到工作流中而无安全保护会带来风险。本文提出一个开源、面向隐私、面向用户的防火墙，同时保护基于 Web 与程序化 LLM 交互。设计结合了浏览器扩展与智能体，拦截 HTTP(S) 和 WebSockets 上所有流量。其核心是一个灵活的多智能体流水线，通过确定性检测器与 LLM 驱动语义分析的混合提供数据泄漏防护、专有代码泄漏防护，以及未来增强（如提示注入回避防御）的可扩展组件。分层架构使得可在多种环境部署，组织可在成本、检测深度和延迟之间平衡。评估显示"在最优配置下 F1 分数高达 94.93%"。

  链接：

https://arxiv.org/abs/2607.08282

7. 事件突发触发：一种针对基于事件的SNN目标检测的可用性后门攻击

摘要：基于事件的视觉和脉冲神经网络在延迟/能耗约束下越来越多用于边缘智能，但 SNN 目标检测的可用性后门漏洞尚未充分研究。作者提出 Event Burst Trigger (EBT)，针对 SNN 检测器的可用性后门攻击。EBT 向训练数据注入触发器，在推理时产生时间集中的事件流。这些爆发膨胀了虚假目标候选并推高后处理成本，尤其是 Non-Maximum Suppression。在 SpikeYOLO 上以纯投毒威胁模型（不修改架构、损失或流水线）评估，准确率基本保持（mAP@0.5 下降 <0.099），但 NMS 延迟上升高达 38%。边缘平台测试显示基线资源使用抬升而无明显尖峰，STRIP 类防御无法可靠检测该攻击。（DSN 2026）

链接：

https://arxiv.org/abs/2607.09115

-End-

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8R7Rm0KL55HCcIiasO8JJ7IibXzYxx3losWVb2eddxdClACzWxWtQLwl0wkAl1ZLibcESVWvx5dCeibtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=2)

*![图片](https://mmbiz.qpic.cn/mmbiz_gif/D9wGKNiaQYpx7bvaHqVZibq0ogu5pckjQMepnZgmhgM01uFQsoFz5QDDE0iapRkuUumSGfk8Dz7mjnbvibwPk7jISg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)*

![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8QRqLMRicZIN6VJg0ue41W1HVSmDpDqkj86j5SNicNE3X5KkPgcdv1ZmxM7FXrFUdkBes8dpos7d27w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=4)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8SDzMyjUl8Lr0J0V4feAVeZ5eMLYibJKzJyVxRuoHpXEDLpGkGm6hQcBm7OyEu3EiclN8sNdPvWIWiaw/0?wx_fmt=png)

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