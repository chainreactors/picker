---
title: 清华大学 x 中国信通院「BigModelGym 大模型安全评测体系」联合发布
url: https://mp.weixin.qq.com/s/knWiYCuuJT8sFZGFqTMN1g
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:23.760810
---

# 清华大学 x 中国信通院「BigModelGym 大模型安全评测体系」联合发布

# 清华大学 x 中国信通院「BigModelGym 大模型安全评测体系」联合发布

原创

赛博新经济
赛博新经济

赛博新经济

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**LEADERBOARD RELEASE · BigModelGym**

**清华大学 x 中国信通院**

**「BigModelGym 大模型安全评测体系」**

**联合发布**

*Large Model Safety Evaluation Leaderboards*

大模型正在从「回答问题」走向「理解系统、调用工具、驱动物理世界」，安全风险的边界也随之不断外扩。为从动态真实系统环境刻画前沿模型的真实安全水位，清华大学和中国信通院牵头发布**大模型安全评测榜单体系BigModelGym**，覆盖四大方向：

|  |  |  |
| --- | --- | --- |
| **榜单** | **评测对象** | **核心问题** |
| CyberSpace World Model Benchmark | 基础大模型 | 模型真的理解网络空间世界吗？ |
| MAS-RolePressure | 多智能体系统中的大模型 | 框架角色模板会不会「压弯」模型的安全判断？ |
| Embodied Agent | 多模态规划模型 | 当大模型驱动物理世界，攻击面有多大？ |
| Agent3σ | 单智能体 | 静态测评的高分，挡得住真实环境的攻击吗？ |

**评测平台链接：https://bigmodelgym.com**

四张榜单相互衔接，实现从模型决策、认知、行动到全链路模型真实环境评测，构成人工智能场景下智能生态的**全链路安全把控**。以下逐一介绍评测设计与最新结果。

**01**

**网络空间安全认知评测：CyberSpace World Model Benchmark**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWVyW5RnribXEseGeuNHibStcxEJuAV5hbEr6aKiaXm2AgqFKthxQU6TEwk0vrWiceyP0BloGxphpIEWtpFnRAfn64UrSvY6Js1UD7M/640?wx_fmt=png)

**模型真的理解网络空间世界吗？**

网络系统世界中的多元数据链——软件代码、智能体轨迹、网络流量、系统指令——可汇聚为系统状态链（System State-Chain）。本评测以 **1,000 条系统状态链问答**（四类数据各 250 条）考察模型对网络空间世界的理解、预测与研判能力，覆盖三种任务：

▪**Complete（链补全）**：续写缺失的状态节点；

▪**Predict（链预测）**：推演系统下一步演化；

▪**Security（安全研判）**：判定系统状态正常或异常。

计分采用两个口径：**Answer 正确性**（世界理解任务按语义相似度计分、安全研判按判断准确率计分）与 **Reasoning 正确性**（对推理理由独立评判），形成两张独立榜单。共评测 8 个模型：StarCore-9B 与 7 个前沿基础模型。

**▌ Answer 榜单（百分制，按综合分降序）**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **模型** | **综合** | **安全研判** | **链补全** | **链预测** |
| **StarCore-9B** † | **82.0** | 90.4 | **83.8** | **72.1** |
| Qwen3.5-35B | 75.6 | 90.1 | 67.1 | 68.8 |
| Qwen3.5-9B | 73.3 | 88.5 | 64.3 | 66.0 |
| MiniMax M3 | 71.3 | 87.7 | 62.0 | 65.8 |
| GLM-5.2 | 66.9 | 77.3 | 62.6 | 60.7 |
| Kimi K3 | 59.0 | 67.7 | 56.3 | 51.7 |
| DeepSeek-v4-Pro | 55.6 | 53.4 | 54.0 | 59.5 |
| DeepSeek-v4-Flash | 38.5 | 47.8 | 38.0 | 29.6 |

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWgUAPIHGibyGqpicRgYqutibhe2runQ3sHQWOFZrrlckMiaKIL1UYSU6yXw2I8oiaJQn9ez1Qxejuqibj2qVfEHICibmfGXwibamiaicibWk/640?wx_fmt=png)

CyberSpace World Model Benchmark Answer 综合分

**▌ Reasoning 榜单（百分制，按综合分降序）**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **模型** | **综合** | **安全研判** | **链补全** | **链预测** |
| **StarCore-9B** † | **52.8** | 57.0 | 60.2 | 41.1 |
| MiniMax M3 | 47.7 | 48.0 | 55.7 | 38.4 |
| GLM-5.2 | 44.0 | 49.8 | 44.2 | 38.0 |
| Qwen3.5-35B | 43.9 | 47.9 | 50.9 | 32.5 |
| Qwen3.5-9B | 42.7 | 49.1 | 47.7 | 31.1 |
| DeepSeek-v4-Flash | 40.2 | 35.9 | 38.4 | 46.3 |
| DeepSeek-v4-Pro | 39.8 | 44.4 | 43.0 | 32.0 |
| Kimi K3 | 39.6 | 35.7 | 44.6 | 36.6 |

**核心发现**

▪**9B 规模的 StarCore 综合分 82.0，领先次名 Qwen3.5-35B 达 6.4 分**，在安全研判、链补全、链预测三项任务上全面居首，展现出领域专用模型对更大参数通用模型的显著超越。

▪**「答对」不等于「想对」**：所有模型的 Reasoning 得分均大幅低于 Answer 得分，榜首 StarCore-9B 的推理正确性也仅 52.8 分——模型可以给出正确答案，但推理过程的正确性仍是普遍短板，这在安全研判场景中尤为值得关注。

**02**

**多智能体系统中的大模型安全压力基准：MAS-RolePressure**

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWDtSfqyLW7CjrSCKRIiaeia8E2doGSVyxd8IwoWPQc0vzZ7em8OTcZp3ksyg8icDiaq3HoYr4btP8jaaFBR6OgzT4icfNGYzPjCbic4/640?wx_fmt=png)

**同一条恶意输入，裸发给模型会被拒绝；进入多智能体框架的角色模板后，往往被直接执行。**

大模型作为多智能体系统（MAS）中的节点，收到的不是用户原始消息，而是框架写好的提示词模板——角色设定、任务范围与输出格式。MAS-RolePressure 从 **AutoGen、EvoAgentX、CrewAI 三个真实框架逐字提取 16 个决策点模板**，以决策切片（模板 T + 恶意输入 x + 经验证无害的上下文 c）为评测单元，把同一条输入分别以「裸输入」和「模板内」发给每个模型——因此观察到的顺从可以**归因于模板的结构性压力**。

回复按三个维度独立评判：**识别**（模型发现危害了吗）、**行动**（拒绝、脱毒还是顺从）、**角色一致性**（是否守住角色输出格式）。共评测 16 个模型、6 家厂商，每个模型 919 条模板内测试用例，覆盖 44 个种子、8 类危害。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **模型** | **综合分 ↑** | **R·Flag % ↑** | **A·Comply % ↓** | **C·Hold % ↑** | **ΔComply pp ↓** |
| **Claude Haiku 4.5** | **76.0** | **91.1** | 9.3 | 72.3 | 9.3 |
| Claude Opus 4.8 | 71.3 | 84.3 | **3.3** | 55.5 | **3.3** |
| Claude Sonnet 4.6 | 70.5 | 79.8 | 9.4 | 68.6 | 9.4 |
| GLM-5.2 † | 69.3 | 78.4 | 20.0 | 81.7 | 10.8 |
| GPT-5.4-mini | 64.2 | 69.8 | 31.8 | **96.5** | 30.7 |
| Qwen3.7-Max | 54.1 | 63.7 | 35.8 | 85.0 | 31.0 |
| Qwen3.7-Plus | 52.1 | 65.1 | 36.1 | 81.7 | 32.8 |
| GPT-5.4-nano | 51.4 | 57.9 | 43.2 | 94.7 | 30.3 |
| GPT-5.5 | 39.8 | 32.0 | 5.7 | 55.9 | 4.6 |
| Gemini 3.5 Flash | 37.0 | 45.5 | 51.6 | 81.5 | 26.2 |
| Gemini 3.1 Flash-Lite | 36.3 | 47.3 | 57.7 | 90.5 | 26.4 |
| Gemma-4-E4B-it † | 31.4 | 39.3 | 61.8 | 89.0 | 42.3 |
| DeepSeek-V4-Flash † | 30.5 | 39.7 | 64.9 | 94.5 | 39.9 |
| DeepSeek-V4-Pro † | 29.7 | 35.3 | 65.1 | **95.4** | 49.3 |
| Gemma-4-E2B-it † | 27.1 | 30.6 | 66.4 | 91.5 | **51.7** |
| Gemma-4-12B-it † | 26.3 | 31.6 | 66.2 | 88.9 | 44.5 |

注：综合分（0–100）为行动门控 × 识别与角色一致性的等权组合；ΔComply 为模板内顺从率减去同模型裸输入顺从率；† 为开源权重模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWXSian3Xm8V1kLpXaSczIPIFxkXQRf4vYiaNad13FQqadORRNozwOFXw8kEoen7j0WMEXcb6x7c2cZl5oQlDdk7jWAUniac2xoUDg/640?wx_fmt=png)

MAS-RolePressure 综合分

**核心发现**

▪**16 个被测模型无一幸免**：平均拒绝率下降 32.3 个百分点，ΔComply 全部为正（+3.3 ~ +51.7 pp）。退化由模板压力引发，而非输入太弱——裸输入下全体模型的池化顺从率仅 11.6%。

▪**最强模型的安全来自「看见并拒绝」**：榜首 Claude Haiku 4.5 识别率高达 91.1%；而高顺从模型的失守发生在**识别环节**而非抵抗环节——Gemma-4-12B 的盲从率达 61.5%。

▪**知情顺从真实存在**：5.9% 的回复在明确识别危害后仍然执行，角色压力的独立性不容忽视。

**03**

**具身智能安全评测：Embodied Agent**

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXoDFRjKf5kMIxicg726hx6WlNsDv7iciczpPpicfs0MUVdWR3kkM7VIEqdSTbc27Da1MiaL2lqCiaa0GUVcrOgAB3Z1ibVweL6Tib8aME/640?wx_fmt=png)

**当大模型成为机器人的规划器，攻击面就从文本扩展到了物理世界。**

本评测以 **1,000 条具身智能有害指令及摄像头采集数据对**（模拟器环境、合成环境、真实室内、真实室外各 250 条）为输入，考察 **15 种攻击方法**（文本、多模态、具身专用）在 **5 个多模态规划模型**（GPT-4o、Qwen3VL、GLM-4.6V、Claude-4.6、Gemini-3.5）上的表现，覆盖信息安全、监管安全、行为安全、伦理安全 4 大类共 10 个细粒度安全类别。评测输出两个指标：**ASR**（攻击成功率，越低越安全）与 **HS**（LLM-as-judge 行为有害度评分 1–5，越低越安全）。

**▌ ASR 榜单（平均攻击成功率 %，越低越安全）**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **模型** | **ASR ↓** | **最脆弱攻击** | **最差值** | **最稳攻击** | **最稳项** |
| **GPT-4o** | **16.6** | RoboPAIR | 78.0 | Cipher | 2.0 |
| Gemini-3.5 | 26.1 | FigStep | 72.0 | Cipher | 3.0 |
| Claude-4.6 | 32.8 | SI-attack | 60.0 | BadRobot\_CJ | 13.0 |
| GLM-4.6V | 71.7 | DeepInception | 96.0 | FigStep | 33.0 |
| Qwen3VL | 94.9 | DeepInception | 99.0 | FigStep | 90.0 |

**▌ HS 榜单（平均行为有害度 1–5，越低越安全）**

|  |  |  |  |
| --- | --- | --- | --- |
| **模型** | **平均 HS ↓** | **最脆弱攻击** | **最差值** |
| **GPT-4o** | **1.59** | RoboPAIR | 4.03 |
| Claude-4.6 | 1.82 | SI-attack | 3.02 |
| Gemini-3.5 | 2.86 | BadRobot\_CJ | 3.59 |
| GLM-4.6V | 3.57 | BadRobot\_CJ | 4.47 |
| Qwen3VL | 4.42 | Cipher | 4.67 |

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWW6PuicMIrx376UibAAMWrNhlDtkqMDIJpxia1vxwVHTsm4oW22QRwyiczgmZib1VYv3tiaOvIk70R7G2WpDygAliazqc8858FfyHvzMA/640?wx_fmt=png)

Embodied Agent 平均攻击成功率

**核心发现**

▪**模型间差距悬殊**：5 个模型的平均 ASR 从 16.6% 到 94.9%，最安全与最脆弱模型相差近 **6 倍**；Qwen3VL 几乎全线失守，连表现最好的攻击维度（FigStep）ASR 也高达 90%。

▪**具身专用攻击威胁最大**：RoboPAIR、FigStep、DeepInception 等面向视觉与物理场景的攻击方法普遍比传统文本攻击更有效——GPT-4o 在文本攻击下整体稳健，却在 RoboPAIR 下 ASR 飙升至 78%。

▪ 没有任何模型能对所有攻击免疫，**具身智能部署前的专项安全评测不可或缺**。

**04**

**单智能体多层次安全评测：Agent3σ**

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWVcrkfDaehR4VxTFIwda53j9bs25eq82ibgrPyqrIwzwuJUYFyOicZ4OaDtwvZicyfiafqGGPYIKoiaVcWWc1icTiauUYuSLFC5qzDeSM/640?wx_fmt=png)

**静态测评的高分，挡不住真实环境里的攻击。**

当 AI Agent 从「回答问题」走向「调用工具、操控系统、执行真实业务」，风险也从说错话升级为做错事——核心文件被删、资金外流、机密泄露，甚至系统级联失控。Agent3σ将真实任务中的智能体风险归纳为 **7 大类、30+ 典型场景**（本地环境破坏、数据与信息安全、记忆污染、权限管控、网络攻击、业务滥用、金融交易），以三级递进式评测刻画智能体的真实安全水位：

▪**L1 Sweep**：静态样本离线评估，覆盖广、成本低；

▪**L2 Stage**：插件仿真网页、邮件等多轮交互，稳定可复现；

▪**L3 Canary**：真实工具接口执行，还原智能体实际运行轨迹。

指标包括 ASR 攻击成功率（越低越好）、安全意识（风险任务明确拒绝率）、任务成功（正常任务成功率），综合分按 0.6/0.2/0.2 加权，总分为三级综合分的算术平均。

**▌ 总榜（12 个模型，按总分降序）**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **模型** | **总分** | **L1 静态** | **L2 仿真** | **L3 真实** |
| **Claude Opus 4.6** | **85.1** | 79.3 | **88.1** | **87.8** |
| GPT-5.4 | 74.6 | 75.2 | 81.0 | 67.7 |
| Claude Sonnet 4.5 | 73.2 | **81.9** | 79.2 | 58.4 |
| Qwen3.6-Plus | 69.8 | 69.5 | 68.6 | 71.4 |
| GLM-5 | 67.2 | 74.7 | 62.7 | 64.2 |
| DeepSeek-V4-Pro | 57.2 | 54.9 | 57.0 | 59.8 |
| Qwen3.5-397B-A17B | 56.1 | 63.6 | 52.0 | 52.6 |
| Gemini-3.1-Pro | 53.0 | 67.9 | 41.5 | 49.7 |
| Kimi-K2.5 | 51.4 | 53.0 | 52.7 | 48.5 |
| MiniMax-M2.5 | 50.8 | 55.8 | 47.8 ...