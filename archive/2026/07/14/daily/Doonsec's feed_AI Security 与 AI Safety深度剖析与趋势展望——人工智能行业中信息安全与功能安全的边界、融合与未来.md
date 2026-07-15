---
title: AI Security 与 AI Safety深度剖析与趋势展望——人工智能行业中信息安全与功能安全的边界、融合与未来
url: https://mp.weixin.qq.com/s/h1U7eFRkCB6qkDuwXjX-3A
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:35.905127
---

# AI Security 与 AI Safety深度剖析与趋势展望——人工智能行业中信息安全与功能安全的边界、融合与未来

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88UMEmZhhCmxCwdBBn4v6yExAJOqMbaJskfoTb5NFNHvPeJsEJkZokNJhIwXc2j9we5y07QK8G56a5LIrxl5uotRciavJKZialUf0/0?wx_fmt=jpeg)

# AI Security 与 AI Safety深度剖析与趋势展望——人工智能行业中信息安全与功能安全的边界、融合与未来

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88WLb6FkEjiap4INxJDjAaFMPDemiaquibUgu42CtbEWtiaY4eOnEpicibdVLjC61PPzHNAVaVMC3tTFNMVWiaZC9Lk7fsTdTeZRFWktcQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

一、引言：AI 时代的安全双重奏

人工智能正在以前所未有的速度渗透进入人类社会的每一个角落。从大语言模型的广泛应用，到自主 AI Agent 的崛起，再到通用人工智能（AGI）的遥不可及的论述——技术的进步令人振奋，但同样令人担忧的是，“安全”这个词在 AI 领域中正被严重混淆。当一个团队负责人说“我们的 AI 系统是安全的”时，他指的到底是系统能抵御外部攻击者的 Jailbreak，还是模型不会生成有害或歧视性内容？这两者是完全不同的概念，却经常被简单地归类为“AI 安全”。

在英语技术语境中，这两个概念有着明确的界限分野。AI Security（AI 信息安全）关注的是防止未授权的外部攻击者利用 AI 系统的漏洞进行恶意操作——从提示注入、Jailbreak 攻击，到对抗样本和数据投毒，这些威胁正在随着 AI 系统的复杂度指数级增长。AI Safety（AI 功能安全）则关注系统在正常运行或异常情况下不会对用户、社会或环境造成不可接受的风险——幻觉、算法偏见、价值漂移等内生问题。

本文将从 AI 行业的视角出发，系统地剖析 AI Security 与 AI Safety 的核心定义、关键差异、具体威胁、全球治理框架以及未来发展趋势。我们不仅关注技术层面的攻击与防御，更关注这两个领域如何在复杂 AI 系统中深度交织，以及如何构建真正可信、可靠且面向未来的 AI 系统。

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

二、AI Security 与 AI Safety：核心定义与区别

2.1 AI Security：防御外部攻击

AI Security 是指保护 AI 系统免受未授权访问、使用、披露、破坏、修改或丢失的能力。它的核心目标是应对“恶意行为”——即外部攻击者故意利用 AI 系统的漏洞实施的攻击。在大语言模型时代，AI Security 的威胁景观已经从传统的软件安全扩展到了全新的维度。

根据 NIST AI 100-2e2025 发布的对抗性机器学习分类体系，AI Security 面临的主要威胁包括以下几类。第一类是逃逸攻击（Evasion），攻击者通过微小修改输入数据诱使模型输出错误结果，对抗样本（Adversarial Examples）是其典型代表。第二类是数据投毒（Poisoning），攻击者在训练数据中注入恶意样本，使模型在特定触发条件下产生错误输出。第三类是隐私攻击（Privacy Attacks），包括模型窃取（Model Stealing）、成员推断（Membership Inference）和数据重建（Data Reconstruction）。第四类是提示注入（Prompt Injection），攻击者通过精心构造的输入穿透模型的安全对齐机制，诱使其输出有害内容或泄露敏感信息。

2.2 AI Safety：确保系统可靠

AI Safety 是指确保 AI 系统在规定条件下不会对人、社会或环境造成不可接受风险的能力。与 AI Security 不同，AI Safety 关注的不是外部攻击，而是系统自身的可靠性、值得观一致性和行为可控性。它的核心问题是：即使在没有外部攻击的情况下，AI 系统也可能因设计缺陷、训练数据偏差或目标函数不当而产生有害结果。

AI Safety 的典型问题包括四个核心方面。幻觉（Hallucination）是最广为人知的问题——模型生成看似合理但事实错误的内容。研究表明，ChatGPT 在人物传记生成中的事实准确率仅为 58%，而 NeurIPS 2025 的论文审查中已经发现了大量模型生成的虚假引用。算法偏见（Bias）是另一个重要问题——模型可能因训练数据中的偏差而对某些群体产生歧视性结果。对齐问题（Alignment）则是 AI Safety 的核心挑战——如何确保模型的行为与人类的价值观和意图保持一致。OpenAI、Anthropic 等领先实验室已经将大量资源投入到对齐研究中，但现有方法如 RLHF 和 Constitutional AI 仍然存在明显局限。

2.3 核心差异对比

|  | AI Security | AI Safety |
| --- | --- | --- |
| 核心目标 | 防止未授权攻击者利用 AI 漏洞 | 确保 AI 系统不产生有害结果 |
| 对抗对象 | 外部攻击者（恶意） | 系统内生缺陷（无意） |
| 典型威胁 | 提示注入、Jailbreak、对抗样本 | 幻觉、偏见、对齐失败 |
| 评估方法 | Red Teaming、渗透测试、对抗训练 | 安全评估、偏差审计、对齐评估 |
| 防御手段 | 对齐训练、Guardrails、输入过滤 | RLHF、Constitutional AI、人类监督 |
| 关联标准 | NIST AI 100-2、MITRE ATLAS | EU AI Act、ISO/IEC 42001 |
| 简单记忆 | 防人搞 AI | 防 AI 搞人 |

表1：AI Security 与 AI Safety 核心差异对比

从上表可以看出，AI Security 与 AI Safety 虽然目标一致——都是保护 AI 系统和用户——但它们的出发点、方法论和评估体系存在本质区别。简单来说，AI Security 是“防人搞 AI”，AI Safety 是“防 AI 搞人”。然而，在复杂的实际系统中，这两者的界限正在迅速模糊。例如，一个成功的 Jailbreak 攻击不仅是安全问题，也可能触发安全风险（如生成有害内容）；而一个设计不当的安全机制可能为攻击者提供可乘之机。

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

三、AI Security：攻击面与防御体系

AI Security 的攻击面正在以惊人的速度扩展。OWASP 连续三年将提示注入列为 LLM 应用的第一大风险（LLM01），HackerOne 报告 2025 年提示注入漏洞报告增长了 540%。CrowdStrike 分析了超过 30 万个对抗性提示，追踪了 150 多种不同的攻击技术。这些数字背后，是一个正在快速演进的攻击生态。

3.1 提示注入与 Jailbreak 攻击

提示注入攻击是当今 AI 安全领域最突出的威胁。直接提示注入（Direct Prompt Injection）中，攻击者直接向 LLM 提交恶意输入，试图覆盖系统的原始指令。2025-2026 年，这类攻击已经从简单的“Ignore all previous instructions”进化到了高度复杂的技术——包括密码编码（base64、自定义暗号）、认知骗术、多语言翻译、角色扮演框架以及对抗性后缀（Adversarial Suffixes）等。

更加危险的是间接提示注入（Indirect Prompt Injection）。攻击者不直接与 AI 交互，而是将恶意指令嵌入到 AI 系统会检索或使用的外部数据中——如电子邮件、网页内容、RAG 知识库、工具输出等。2026年 4 月，Palo Alto Networks Unit 42 报告了首例真实世界中的恶意间接提示注入事件，证实了这类攻击已经从理论走向实践。

Jailbreak 攻击的进化令人卫然。最新研究表明，将 1,200 个 MLCommons 有害提示转换为诗歌形式后，攻击成功率最高可达基线的 18 倍。手工编写的诗歌实现了 62% 的平均 Jailbreak 成功率，元提示转换版本也达到约 43%。更加令人震惊的是，2026 年 Nature Communications 的一篇论文显示，大型推理模型作为自主 Jailbreak 代理，在跨模型组合中实现了 97.14% 的整体成功率。这揭示了一个“对齐回退”现象——更强大的推理模型在穿透其他系统的安全机制时更加得心应手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8SYXzUAIerTfsm75whNgkrAFOmtH0PU5DM9dffjdhLDFhOmqnh80ZdlunqolicqvPlMmqCPsVnuOAhw5HXHso3P3OHr7abtuaPyP7KqAe9Tw/640?wx_fmt=png#imgIndex=0)

图1：Jailbreak 攻击成功率与防御进化对比（2023-2026）

3.2 对抗样本与数据投毒

对抗样本（Adversarial Examples）是深度学习系统中一类独特的安全威胁。攻击者通过对输入数据添加人眼难以察觉的微小扰动，就能诱使模型产生完全错误的输出。这类攻击的危害远超计算机视觉领域，已经扩展到垃圾邮件过滤、入侵检测、生物特征识别等关键应用场景。在医疗 AI 领域，对抗样本可能导致误诊断或未授权访问患者记录；在网络安全领域，攻击者可能通过微妙修改恶意软件，使其在基于 AI 的杀毒系统面前显得无害。

数据投毒（Data Poisoning）则是更加难以检测的威胁。攻击者通过在训练数据中注入恶意样本，使模型在特定触发条件下产生错误输出。USENIX Security 2025 年发表的 PoisonedRAG 研究表明，在包含数百万条目的知识库中注入仅 5 份恶意文档，就能对攻击者关心的查询实现 90-99% 的攻击成功率。这种“五分之一个百万”的比例让任何基于统计检测的防御方法都面临巨大挑战。

3.3 模型窃取与隐私攻击

模型窃取（Model Stealing）攻击指攻击者通过向商业 AI API 发送大量查询，并观察输出，从而重建一个功能相似的替代模型。这不仅威胁商业 AI 应用的安全性，更可能泄露模型依赖的训练数据信息。隐私攻击则更加精细——成员推断攻击可以判断某个数据是否被用于训练模型，数据重建攻击则可以从模型的输出中恢复原始训练数据。2026 年的研究表明，即使是最先进的安全对齐模型，如 Claude Opus 4.6 和 GPT-5.4，仍然存在显著的隐私泄露风险。

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

四、AI Safety：内生风险与对齐挑战

AI Safety 面临的挑战远比 AI Security 更加深层。它不仅涉及技术问题，更涉及哲学、伦理学和社会学问题。当 AI 系统被赋予越来越多的决策权力时，如何确保它们的行为符合人类的价值观和意囲，成为了一个根本性的难题。

4.1 幻觉与事实错误

幻觉是大语言模型最突出的安全问题之一。模型生成看似合理但事实错误的内容的倾向已经在跨任务和模型家族中被广泛记录。FActScore 研究发现，ChatGPT 在人物传记生成中的事实精确率仅为 58%。更令人担忧的是，NeurIPS 2025 的论文审查中已经发现了大量模型生成的虚假引用，ICLR 2026 则组建了专门的桌面拒绝队列来处理包含幻觉引用的投稿。

幻觉问题的根源在于 LLM 的训练目标——预测下一个 token，而非确保输出的事实正确性。这使得模型在追求“流畅”和“合理”时，很容易生成看似正确实则虚构的内容。研究者发现，即使是最先进的模型，其引用中也有高达 57% 是事后合理化的——模型先生成答案，然后事后配置引用。

4.2 算法偏见与公平性

算法偏见是 AI Safety 领域中最具社会影响力的问题之一。AI 模型往往反映并放大训练数据中的社会偏见，导致在招聘、贷款、执法和医疗等领域产生歧视性结果。例如，AI 驱动的招聘工具可能因历史招聘数据中的偏见而倾向某些人群；预测性执法算法可能不比例地针对边缘化社区，加剧了现有的不平等。

解决这一问题需要多维度的努力。技术上，可以采用公平性度量（如统计平等、机会平等、校准）、对抗性训练和偏见检测工具。治理上，需要建立透明、可审计的机制。欧盟 AI Act 明确要求高风险 AI 系统必须检查训练数据中的偏见，纳纳约市的 Local Law 144 更是强制要求对自动化招聘决策工具进行年度独立偏见审计。

4.3 模型对齐与价值漂移

模型对齐（Alignment）是 AI Safety 的核心挑战。它的核心问题是：如何确保 AI 系统的目标与人类的价值观和意围保持一致。当前主流的对齐方法包括监督微调（SFT）、基于人类反馈的强化学习（RLHF）以及 Anthropic 提出的 Constitutional AI。

然而，这些方法都存在明显局限。国际 AI 安全报告 2026 指出，人类反馈受到人类错误和偏见的限制，导致奖励骗取（Reward Hacking）和谄媚行为（Sycophancy）。更令人担忧的是，下游微调（Downstream Fine-tuning）可以打破先前建立的安全机制，而后门攻击（Backdoor）则可以在训练阶段隐藏特殊触发器，使模型在特定条件下表现异常。FutureSearch AI 的预测表明，26% 的专家认为解决 ASI 对齐问题需要一个尚未形成的全新范式，而可扩展监督（Scalable Oversight）以 19% 的概率被视为最有前景的现有方法。

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

五、深度融合：当 Security 遇见 Safety

在复杂的 AI 系统中，AI Security 与 AI Safety 的界限正在迅速模糊。传统的“先做 Safety，再做 Security”的串行模式已经无法满足复杂 AI 系统的需求。正确的做法是 Security-aware Safety 和 Safety-aware Security——即在安全设计中考虑安全因素，在安全设计中考虑安全影响。

这种深度融合的典型体现是当今大语言模型的对齐与防御之间的张力。一方面，强力的安全对齐可以有效减少有害输出，提升 AI Safety；另一方面，过度的安全限制可能降低模型的有用性，甚至为攻击者提供新的攻击面。例如，ARMOR 等先进的防御系统通过三步推理管道——分析 Jailbreak 策略、提取核心意图、应用策略验证——实现了平均有害率 0.002% 和攻击成功率 0.06% 的领先性能，远低于其他推理型模型。

在多模态 AI 系统中，这种融合更加复杂。PolyJailbreak 研究发现，多模态大语言模型存在“多模态安全不对称”现象——视觉对齐引入了不均匀的安全约束，削弱了整体鲁棒性。其实验结果表明，PolyJailbreak 在商业黑盒模型上的成功率超过 95%，包括 GPT-4o 和 Gemini。这意味着，单纯依赖某一模态的安全机制已经不足以保护复杂的多模态系统。

![](https://mmbiz.qpic.cn/mmbiz_png/8SYXzUAIerTAEJXwY9NddorxlkwCicgiae8jPAt01yiagsGwSEgSWInrsQsKUILS3t3FvTgaYLSSeWdiapjvplkutRkoxCa4718uVF6A0Zj9HjM/640?wx_fmt=png#imgIndex=1)

图2：AI Security 与 AI Safety 风险地图

![](https://mmbiz.qpic.cn/mmbiz_png/nickSG1u8Cfiacibx2XiatEFkXrasSPxoDYItyIYCMJ9oUj431bUhA51Tf8WNwfwI24JNFlMFnAYWQLrtHXZLeicDt0Jk7Q36QZdadFtckhkUlzA/640?from=appmsg)

六、全球治理与监管格局

全球 AI 治理正在迅速成熟。从欧盟的风险分类框架，到中国的算法备案制度，再到美国的自愿性框架，各主要司法辖区都在构建自己的 AI 监管体系。这些框架虽然路径不同，但都共同关注一个核心问题：如何在保护创新的同时，确保 AI 系统的安全与安全。

6.1 欧盟 AI Act：风险分类的创新

欧盟 AI Act（Regulation (EU) 2024/1689）是全球首个综合性的 AI 监管法规，于 2024 年 8 月生效，采用分阶段实施。其最大的创新在于风险分类方法——将 AI 系统分为四个风险等级：不可接受风险（直接禁止）、高风险（严格合规要求）、有限风险（透明度义务）和最低风险（自愿准则）。

不可接受风险的 AI 实践已于 2025 年 2 月被禁...