---
title: 【工具推荐】35 + 大模型安全相关仓库
url: https://mp.weixin.qq.com/s/_2uycaNxpEd8tU5FpOlSRQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:23.829612
---

# 【工具推荐】35 + 大模型安全相关仓库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqVC8QjhvtCLUuGskxcHbA3bMvyeVic8ENguicCXr5TfMDDABSUl3iaDPN05nDI5NNvfEvSWrZbl5fwUJelCSuJZTNsbT5qQW1jMyE/0?wx_fmt=jpeg)

# 【工具推荐】35 + 大模型安全相关仓库

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 知识库 / Awesome Lists

* • **corca-ai/awesome-llm-security[1] ⭐️ 1564 / 2025-08-20**
  目前最全面的 LLM 安全资源索引，红队、防御、基准全覆盖。
* • **beyefendi/awesome-llm-security[2] ⭐️ 9 / 2026-04-05**
  侧重防御/guardrail 和 red teaming 工具，agent 安全扫描器收录很全。
* • **ydyjya/Awesome-LLM-Safety[3] ⭐️ 1818 / 2026-04-03**
  安全论文、文章、资源精选，适合学术研究者快速定位文献。
* • **user1342/Awesome-LLM-Red-Teaming[4] ⭐️ 95 / 2025-09-04**
  专攻 red teaming 训练、资源、工具，含 playground 和实战靶场。
* • **yueliu1999/Awesome-Jailbreak-on-LLMs[5] ⭐️ 1299 / 2026-03-30**
  jailbreak 方法、数据集、防御全集，持续追踪最新攻击手段。
* • **WhileBug/AwesomeLLMJailBreakPapers[6] ⭐️ 134 / 2023-11-03**
  LLM jailbreak 学术论文合集，附代码实现链接，读论文必备。

---

## Red Teaming / Jailbreak / 对抗攻击工具

### 综合性框架

* • **General-Analysis/GA[7] ⭐️ 591 / 2025-05-26** — 集成 TAP、GCG、AutoDAN、Crescendo 等多种 jailbreak 方法的最大开源框架之一。
* • **Azure/PyRIT[8] ⭐️ 6 / 2026-03-25** — Microsoft 官方出品的企业级 Python Risk Identification Tool，适合有合规要求的组织。
* • **confident-ai/deepteam[9] ⭐️ 1522 / 2026-04-06** — 对新手极其友好的 red teaming 框架，支持模拟攻击和 guardrail 测试。
* • **promptfoo/promptfoo[10] ⭐️ 19911 / 2026-04-11** — Dev-first 的 red teaming & eval 框架，支持 PAIR、tree-of-attacks 等策略，可无缝接入 CI/CD。
* • **AI45Lab/OpenRT[11] ⭐️ 241 / 2026-03-25** — 多模态 LLM red teaming 框架，内置 42+ 攻击方法。

### 高效自动化攻击

* • **amazon-science/TurboFuzzLLM[12] ⭐️ 24 / 2025-11-24** — 基于强化学习的 mutation fuzzing，论文报告攻击成功率 >98%。
* • **LLM-QC/AdversariaLLM[13] ⭐️ 21 / 2026-04-04** — 统一 adversarial attack 工具箱，集成 GCG、PAIR、AutoDAN、BEAST 等经典方法。
* • **patrickrchao/JailbreakingLLMs[14] ⭐️ 716 / 2025-07-02** — 黑盒 PAIR 算法经典实现，可在 20 queries 内完成 jailbreak。
* • **llm-attacks/llm-attacks[15] ⭐️ 4603 / 2024-08-02** — GCG 论文官方实现，通用可迁移的对抗后缀生成。
* • **sherdencooper/GPTFuzz[16] ⭐️ 576 / 2026-02-27** — 自动生成 jailbreak prompt 的 fuzzing 工具。
* • **BishopFox/BrokenHill[17] ⭐️ 158 / 2024-12-18** — BishopFox 出品的自动化 GCG 攻击工具，渗透测试团队常用。

### 小众但极具创造力的工具

* • **cyberark/FuzzyAI[18] ⭐️ 1312 / 2026-02-06** — 提供 GUI + CLI 的 LLM 自动 fuzzing/jailbreak 测试框架，可视化做得很好。
* • **xunhuang123/CC-BOS[19] ⭐️ 166 / 2026-03-30** — 古典中文对抗 prompt 自动生成工具，对中文大模型有独特的攻击效果。
* • **elder-plinius/P4RS3LT0NGV3[20] ⭐️ 605 / 2026-04-05** — 专注于文本转换、编码混淆和 mutation，配合 PromptCraft 使用非常灵活。
* • **elder-plinius/L1B3RT45[21] ⭐️ 18236 / 2026-02-17** — 与 P4RS3LT0NGV3 同作者，AI jailbreaking 工具集的另一个分支。
* • **EasyJailbreak/EasyJailbreak[22] ⭐️ 832 / 2026-03-30** — 极其轻量的 Python 框架，适合批量生成 adversarial jailbreak prompt。
* • **CHATS-lab/persuasive\_jailbreaker[23] ⭐️ 353 / 2025-10-17** — Persuasive Adversarial Prompt（PAP）说服式 jailbreak，用 persuasion 而非 brute-force 突破模型防线。

### 基准与数据集

* • **JailbreakBench/jailbreakbench[24] ⭐️ 571 / 2025-04-04** — 标准化 jailbreak 基准 + artifacts 数据集，做研究必须引用。

---

## Fuzzing / Scanning / 漏洞检测工具

* • **NVIDIA/garak[25] ⭐️ 7511 / 2026-04-10** — LLM 漏洞扫描器里最知名的一个，内置 100+ attack modules，NVIDIA 官方背书。
* • **mnns/LLMFuzzer[26] ⭐️ 346 / 2024-02-12** — LLM 专用 fuzzing 框架，主打 prompt 生成与变异策略。
* • **utkusen/promptmap[27] ⭐️ 1175 / 2025-12-01** — 针对自定义 LLM 应用的 prompt injection 自动化扫描器。
* • **Tencent/AI-Infra-Guard[28] ⭐️ 3433 / 2026-04-10** — 腾讯开源的全栈 AI red teaming 平台，带 Web UI，支持多类型扫描。
* • **kortex-labs/plexiglass[29] ⭐️ 154 / 2026-02-04** — LLM 安全工具箱，兼顾测试与防护。
* • **facebookresearch/PurpleLlama[30] ⭐️ 4118 / 2026-04-10** — Meta 官方 LLM 安全评估工具集，含 CyberSecEval 等子项目。
* • **praetorian-inc/augustus[31] ⭐️ 178 / 2026-04-10** — 生产级漏洞扫描器，210+ probes，支持 28 个主流 LLM 提供商 API。

---

## Guardrails / 防御与 Prompt Injection 防护

* • **protectai/llm-guard[32] ⭐️ 2804 / 2025-12-15**（原 rebuff） — 多层 prompt injection 检测与防护，支持输入过滤、输出扫描和敏感信息去识别。
* • **deadbits/vigil-llm[33] ⭐️ 468 / 2024-01-31** — prompt injection 检测 toolkit + REST API，可快速接入现有服务。
* • **prompt-security/ps-fuzz[34] ⭐️ 671 / 2026-02-16** — GenAI 应用 fuzzing 硬化工具，通过主动 fuzz 来暴露并修复防御盲区。
* • **greshake/llm-security[35] ⭐️ 2065 / 2025-07-17** — 间接 prompt injection 攻击演示与防御研究，适合理解「RAG 场景下的注入风险」。

---

## Benchmarks / 数据集

* • **thu-coai/SafetyBench[36] ⭐️ 282 / 2025-07-28** — 11k+ 安全多选题基准，覆盖 7 大安全类别，中文模型也能测。
* • **Libr-AI/do-not-answer[37] ⭐️ 322 / 2024-06-07** — 有害请求防护评估数据集，经典且被广泛引用。
* • **SORRY-Bench[38] ⭐️ 79 / 2025-03-01** — 精细化安全拒绝行为基准，关注模型「拒绝的边界和一致性」。
* • **SafeDialBench[39] [被删除]⭐️ ? / ?** — 多轮对话安全基准，专门测试对话上下文中的 jailbreak 风险。

---

*更新于 2026 年 4 月 11 日*

#### 引用链接

`[1]` corca-ai/awesome-llm-security: *https://github.com/corca-ai/awesome-llm-security*
`[2]` beyefendi/awesome-llm-security: *https://github.com/beyefendi/awesome-llm-security*
`[3]` ydyjya/Awesome-LLM-Safety: *https://github.com/ydyjya/Awesome-LLM-Safety*
`[4]` user1342/Awesome-LLM-Red-Teaming: *https://github.com/user1342/Awesome-LLM-Red-Teaming*
`[5]` yueliu1999/Awesome-Jailbreak-on-LLMs: *https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs*
`[6]` WhileBug/AwesomeLLMJailBreakPapers: *https://github.com/WhileBug/AwesomeLLMJailBreakPapers*
`[7]` General-Analysis/GA: *https://github.com/General-Analysis/GA*
`[8]` Azure/PyRIT: *https://github.com/Azure/PyRIT*
`[9]` confident-ai/deepteam: *https://github.com/confident-ai/deepteam*
`[10]` promptfoo/promptfoo: *https://github.com/promptfoo/promptfoo*
`[11]` AI45Lab/OpenRT: *https://github.com/AI45Lab/OpenRT*
`[12]` amazon-science/TurboFuzzLLM: *https://github.com/amazon-science/TurboFuzzLLM*
`[13]` LLM-QC/AdversariaLLM: *https://github.com/LLM-QC/AdversariaLLM*
`[14]` patrickrchao/JailbreakingLLMs: *https://github.com/patrickrchao/JailbreakingLLMs*
`[15]` llm-attacks/llm-attacks: *https://github.com/llm-attacks/llm-attacks*
`[16]` sherdencooper/GPTFuzz: *https://github.com/sherdencooper/GPTFuzz*
`[17]` BishopFox/BrokenHill: *https://github.com/BishopFox/BrokenHill*
`[18]` cyberark/FuzzyAI: *https://github.com/cyberark/FuzzyAI*
`[19]` xunhuang123/CC-BOS: *https://github.com/xunhuang123/CC-BOS*
`[20]` elder-plinius/P4RS3LT0NGV3: *https://github.com/elder-plinius/P4RS3LT0NGV3*
`[21]` elder-plinius/L1B3RT45: *https://github.com/elder-plinius/L1B3RT45*
`[22]` EasyJailbreak/EasyJailbreak: *https://github.com/EasyJailbreak/EasyJailbreak*
`[23]` CHATS-lab/persuasive\_jailbreaker: *https://github.com/CHATS-lab/persuasive\_jailbreaker*
`[24]` JailbreakBench/jailbreakbench: *https://github.com/JailbreakBench/jailbreakbench*
`[25]` NVIDIA/garak: *https://github.com/NVIDIA/garak*
`[26]` mnns/LLMFuzzer: *https://github.com/mnns/LLMFuzzer*
`[27]` utkusen/promptmap: *https://github.com/utkusen/promptmap*
`[28]` Tencent/AI-Infra-Guard: *https://github.com/Tencent/AI-Infra-Guard*
`[29]` kortex-labs/plexiglass: *https://github.com/kortex-labs/plexiglass*
`[30]` facebookresearch/PurpleLlama: *https://github.com/facebookresearch/PurpleLlama*
`[31]` praetorian-inc/augustus: *https://github.com/praetorian-inc/augustus*
`[32]` protectai/llm-guard: *https://github.com/protectai/llm-guard*
`[33]` deadbits/vigil-llm: *https://github.com/deadbits/vigil-llm*
`[34]` prompt-security/ps-fuzz: *https://github.com/prompt-security/ps-fuzz*
`[35]` greshake/llm-security: *https://github.com/greshake/llm-security*
`[36]` thu-coai/SafetyBench: *https://github.com/thu-coai/SafetyBench*
`[37]` Libr-AI/do-not-answer: *https://github.com/Libr-AI/do-not-answer*
`[38]` SORRY-Bench: *https://github.com/sorry-bench/sorry-bench*
`[39]` SafeDialBench: *https://github.com/thu-coai/SafeDialBench*

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

赛博生存指南

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

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