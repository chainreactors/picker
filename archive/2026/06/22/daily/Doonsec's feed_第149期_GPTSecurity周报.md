---
title: 第149期|GPTSecurity周报
url: https://mp.weixin.qq.com/s/jZalVcBvusVPq6Tj4nov0A
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:05:03.767048
---

# 第149期|GPTSecurity周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PwkEAAy3OPVdGVrnBQZGf56q2KhQVF09vnZvsYOb1hajWUzjFrFTo61N4q220NIYVg1ZgBuEJPQ0mmMjPqBnVHQpuhG2rGTJek5URhdPZDo/0?wx_fmt=jpeg)

# 第149期|GPTSecurity周报

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

1. 针对基于RAG的聊天机器人中提示注入的分层安全框架

简介：针对 OWASP 排名首位的 LLM 漏洞——提示注入，本文提出了一种面向 RAG 聊天机器人的三层中间件框架。第一层使用规则与微调分类器对用户输入进行筛查；第二层在上下文组装阶段强制执行基于来源溯源的指令层级；第三层使用策略引擎与漂移检测器对输出进行审计。在 GPT-4o、Llama 3 与 Mistral 7B 上的 5,080 个样本评测中，该框架将攻击成功率从 71.4% 降至 11.3%，优于单层基线，假阳性率约 4.8%，中位延迟开销约 61.2 毫秒。

链接：

https://arxiv.org/abs/2606.19660

2. CodeSentinel：代码上下文中针对间接提示注入的三层防御

简介：代码 LLM 摄入外部上下文（仓库、文档、issues），由此通过注释、字符串或标识符产生注入路径。CodeSentinel 是一个推理时的清洗器，利用 Tree-sitter 抽取高风险的具体语法树（CST）节点，然后依次应用语法引导的预过滤、CST 引导的动态 Min-K% 评分以及节点扰动分析，以识别对抗性或拟自然语言的触发。被标记的节点会被移除或中和。在六类攻击家族上，平均节点级 F1 达 0.80，优于 CodeGarrison、DePA 与 KillBadCode。

链接：

https://arxiv.org/abs/2606.19235

3. SafeClawBench：在工具调用LLM智能体中区分语义、审计证据与沙箱危害

简介：SafeClawBench 是一个分阶段的工具调用智能体对抗基准，包含 600 个任务，覆盖六类攻击家族，包括直接/间接提示注入、工具返回注入、记忆投毒、记忆提取与歧义性诱发的不安全推理。它分别对语义接受、审计可见的危害证据以及沙箱观察到的工具/状态危害进行评分。在没有提示防护时，语义层失败率介于 9.0% 与 44.2%。一项 12,000 行的配对分析发现，347 个沙箱危害样本中有 291 个通过了语义检查，说明各评估端点暴露的失败模式互不相同。

链接：

https://arxiv.org/abs/2606.18356

4. Anthropic Fable 5 与 Opus 4.8 模型的红队研究

简介：作者使用 HackAgent 对 Anthropic 的 Fable 5 与 Opus 4.8 运行了 4 类自动化越狱攻击，覆盖 10 个类别、共 7,826 条有害意图，并由三个评判模型多数投票判定成功与否。两个模型阻止了大多数攻击，但 tree-of-attacks 在 Opus 4.8 上对 11.5% 的意图越狱成功，在 Fable 5 上则达到 6.1%。研究共记录了 Opus 4.8 上 1,620 条、Fable 5 上 702 条已确认的有害补全，结论是前沿模型在持续的自动化压力下仍可被攻破。

链接：

https://arxiv.org/abs/2606.18193

5. OpenAnt：通过代码分解、对抗性验证与动态测试的LLM漏洞发现

简介：OpenAnt 是一个开源流水线，结合静态分析与 LLM 推理用于仓库级漏洞发现。它使用三项技术：将代码分解为可达性过滤的单元、通过攻击者模拟进行对抗性验证、在沙箱中进行动态漏洞利用验证。在 OpenSSL、WordPress 与 Flowise 上的评测中发现了新颖漏洞，并降低了假阳性率。

链接：

https://arxiv.org/abs/2606.19149

6. ARVO：开源软件可复现漏洞图谱

简介：ARVO 基于 OSS-Fuzz 构建了一个可复现漏洞数据集，包含 311 个项目中的 6,100 多个真实漏洞。每个漏洞均可在不同版本上稳定地重建、触发与分析，从而支持自动化补丁定位。系统成功复现了 81% 的漏洞，补丁定位准确率达 89.4%。论文被 EuroS&P 2026 接收。

链接：

https://arxiv.org/abs/2606.17283

7. PhantomSkill：智能体技能生态系统中的恶意代码注入

简介：本文提出了一种攻击框架，将恶意行为隐藏在 LLM 智能体技能的辅助资源中，而非其文本描述中。其 VulMask 技术将明显的恶意脚本改写为形似漏洞的代码，仅在攻击者触发器存在时才会被激活。评测显示该攻击能保持效用同时降低被检测率，表明技能生态系统需要资源级别的审查与运行时容器化隔离。

链接：

https://arxiv.org/abs/2606.19191

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