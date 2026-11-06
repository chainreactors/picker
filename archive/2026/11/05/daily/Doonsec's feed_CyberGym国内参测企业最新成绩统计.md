---
title: CyberGym国内参测企业最新成绩统计
url: https://mp.weixin.qq.com/s/EWrVptcJu9cV4TpuvW3q6A
source: Doonsec's feed
date: 2026-11-05
fetch_date: 2026-11-06T08:39:24.520742
---

# CyberGym国内参测企业最新成绩统计

# CyberGym国内参测企业最新成绩统计

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibRcdp9geCMPWjA3dgKTKTyN45UAs15ib1bG1twRFibgP5iab1QkajA1UjAc2VnFegfABaDCOmgsyA0Z4lhZwPUCTXOILr7eqZXrb0/640?wx_fmt=png&from=appmsg)

# CyberGym是加州大学伯克利分校研究人员于2025年6月提出的AI智能体网络安全能力评估框架，旨在大规模测试AI在真实漏洞挖掘与利用方面的能力。该框架收录了188个软件项目中的1507个真实安全漏洞，主要聚焦C/C++项目的内存安全问题。测试过程中，AI智能体需要根据漏洞描述和未修补的代码库，生成概念验证（PoC）测试以复现目标漏洞。CyberGym能够有效区分不同AI模型与智能体的网络安全能力，并于2026年2月被《2026国际人工智能安全报告》列为评估AI网络安全能力的四大关键基准之一。

# 最近看到国内的参测厂商越来越多，索性今天做了一下统计，方便网络安全从业者了解。

# 数据来源：

# https://www.cybergym.io/cybergym

# 榜单口径：CyberGym Level-1（漏洞复现，生成可触发漏洞的 PoC，Success Rate = 成功率）。

# 说明：同一公司若提交多次 / 换用不同模型 / 含子测试（subRows），均逐条列出；成绩为 score\_10（成功率，越高越好）。

**统计概览**：共识别 **21** 家中国（大陆及中资）企业/团队，累计测试条目 **37** 条。

## 一、按企业汇总（成绩从高到低）

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 序号 | 公司名称 | 类别 | 产品/智能体 | 使用大模型 | 成绩(成功率) | 测试  日期 | 备注 |
| 1 | 奇虎360（Qihoo 360） | 网络安全厂商 | TuLongFeng | DeepSeek-V4.1-Flash | 99.38% | 2026-09-23 | campaigns=[1496, 1499, 1498]；dynamic (uses cleaned vulnerable Docker image) |
| 2 | 天工（蚂蚁AI安全实验室）（Creation Lab (Ant AI Security Lab)） | 安全实验室 | Creation (天工) | Multi-model (Creation Model, DeepSeek-V4-Pro, Qwen 3.8 Max) | 98.47% | 2026-09-07 | Multi-model; dynamic (uses cleaned vulnerable Docker image) |
| 3 | 天工（蚂蚁AI安全实验室）（Creation Lab (Ant AI Security Lab)） | 安全实验室 | Creation (天工) | Multi-model (DeepSeek-V4-Pro, Creation Model, Qwen 3.8 Max) | 95.35% | 2026-08-30 | 子测试 |
| 4 | 深信服（Sangfor） | 网络安全厂商 | Sangfor AI | GLM-5.3 | 97.21% | 2026-09-02 | Orchestration; Multi-stage; dynamic (uses cleaned vulnerable Docker image) |
| 5 | 深信服（Sangfor） | 网络安全厂商 | Sangfor AI | DeepSeek-V4-Flash | 93.17% | 2026-08-08 | 子测试 |
| 6 | 深信服（Sangfor） | 网络安全厂商 | Sangfor AI | GLM-5.2 | 86.33% | 2026-07-21 | 子测试 |
| 7 | VARAS（智安·宇盾）（VARAS） | 安全团队 | VARAS-OneMind (智安·宇盾) | DeepSeek-V4-Flash | 96.95% | 2026-09-16 | dynamic (uses cleaned vulnerable Docker image); test-time mem. (with a test-time-updated knowledge base) |
| 8 | VARAS（智安·宇盾）（VARAS） | 安全团队 | VARAS-OneMind (智安·宇盾) | GPT-5.4 | 73.79% | 2026-08-14 | 子测试；test-time mem. (with a test-time-updated knowledge base) |
| 9 | 支付宝（蚂蚁集团）（Alipay (Ant Group)） | 金融科技 | Alipay AI4SDL | GLM-5.3 | 96.75% | 2026-09-06 | dynamic (uses cleaned vulnerable Docker image) |
| 10 | 华为云（Huawei Cloud） | 综合科技厂商 | Panshi (磐石) | DeepSeek-V4-Pro | 95.42% | 2026-09-04 | dynamic (uses cleaned vulnerable Docker image) |
| 11 | 绿盟科技（NSFOCUS） | 网络安全厂商 | NSFOCUS AI | GLM-5.3 | 95.02% | 2026-08-13 | dynamic (uses cleaned vulnerable Docker image) |
| 12 | DarkNavy（深蓝）（DARKNAVY (deepsec)） | 安全团队/厂商 | DoGNAVY | GLM-5.3 | 94.96% | 2026-08-17 | Multi-agent; Memory; dynamic (uses cleaned vulnerable Docker image) |
| 13 | DarkNavy（深蓝）（DARKNAVY (deepsec)） | 安全团队/厂商 | DoGNAVY | GLM-5.2 | 90.84% | 2026-08-03 | 子测试 |
| 14 | 知道创宇（Knownsec） | 网络安全厂商 | AiPy Mini | DeepSeek-V4.1-Flash | 92.83% | 2026-09-23 | dynamic (uses cleaned vulnerable Docker image) |
| 15 | 界内安全团队（Sealed Realm Team (界内)） | 安全团队 | Ji Realm (极境) | Multi-model (DeepSeek-V4-Flash, GLM-5.2) | 92.44% | 2026-09-07 | Multi-model; dynamic (uses cleaned vulnerable Docker image) |
| 16 | 中国移动九天人工智能团队（China Mobile Jiutian AI Team） | 运营商/科技 | JiuXuan (九玄) | JT236B | 92.30% | 2026-10-16 | dynamic (uses cleaned vulnerable Docker image) |
| 17 | 中国移动九天人工智能团队（China Mobile Jiutian AI Team） | 运营商/科技 | JiuXuan (九玄) | GLM-5.1 | 72.86% | 2026-08-03 | 子测试；Memory; dynamic (uses cleaned vulnerable Docker image) |
| 18 | 阿里云安全（Alibaba Cloud Security） | 云安全 | Spur | Qwen-Internal | 91.84% | 2026-09-03 | - |
| 19 | 方寸AI（Fangcun AI） | 安全团队 | FangcunCyber | DeepSeek-V4-Flash | 91.31% | 2026-08-16 | test-time mem. (with a test-time-updated knowledge base) |
| 20 | 复旦大学白泽团队（Fudan Whitzard） | 高校研究团队 | Whitzard (白泽) | DeepSeek-V4-Flash | 91.20% | 2026-08-07 | dynamic (uses cleaned vulnerable Docker image) |
| 21 | 复旦大学白泽团队（Fudan Whitzard） | 高校研究团队 | Whitzard (白泽) | GLM-5.1-FP8 | 68.90% | 2026-07-21 | 子测试 |
| 22 | 中国移动（杭州）信息技术有限公司（CMHI (China Mobile Hangzhou)） | 运营商/科技 | TriLane | DeepSeek-V4-Flash | 88.92% | 2026-09-20 | dynamic (uses cleaned vulnerable Docker image) |
| 23 | 阿里安全（Alibaba Security） | 综合科技厂商安全团队 | Velldepth Agent | XekRung | 85.34% | 2026-08-03 | - |
| 24 | 阿里安全（Alibaba Security） | 综合科技厂商安全团队 | XekRung Agent | XekRung-1.5-27B-Preview (finetuned from Qwen3.8-27B) | 88.92% | 2026-09-13 | - |
| 25 | 清华大学紫荆团队（Redbud (Tsinghua University)） | 高校研究团队 | RedbudAI | GLM-5.2 | 86.26% | 2026-08-10 | dynamic (uses cleaned vulnerable Docker image); test-time mem. (with a test-time-updated knowledge base) |
| 26 | 腾讯玄武实验室（Tencent Xuanwu Lab） | 安全实验室 | Xuanwu Atuin AI | GLM-5.2 | 84.80% | 2026-07-22 | dynamic (uses cleaned vulnerable Docker image) |
| 27 | 腾讯玄武实验室（Tencent Xuanwu Lab） | 安全实验室 | Xuanwu Atuin AI | GLM-5.1 | 84.00% | 2026-07-02 | 子测试 |
| 28 | 智谱AI（Zhipu AI） | 综合AI厂商 | Claude Code | GLM-5.2 | 77.20% | 2026-07-21 | - |
| 29 | 智谱AI（Zhipu AI） | 综合AI厂商 | Claude Code | GLM-5.3 | 84.50% | 2026-08-14 | - |
| 30 | 智谱AI（Zhipu AI） | 综合AI厂商 | Claude Code | GLM-5 | 43.20% | 2026-02-12 | - |
| 31 | 智谱AI（Zhipu AI） | 综合AI厂商 | Claude Code | GLM-5.1 | 68.70% | 2026-04-07 | - |
| 32 | 智谱AI（Zhipu AI） | 综合AI厂商 | Codex CLI | GPT-5.4 | 66.30% | 2026-04-07 | 未计入主榜单 |
| 33 | 智谱AI（Zhipu AI） | 综合AI厂商 | Gemini CLI | Gemini 3.1 Pro | 38.80% | 2026-04-07 | 未计入主榜单 |
| 34 | 智谱AI（Zhipu AI） | 综合AI厂商 | Claude Code | GLM-4.7 | 23.50% | 2026-02-12 | - |
| 35 | 深度求索（DeepSeek） | 综合AI厂商 | DeepSeek Agent | DeepSeek-V4-Pro | 83.30% | 2026-08-13 | - |
| 36 | 深度求索（DeepSeek） | 综合AI厂商 | DeepSeek Agent | DeepSeek-V4-Flash | 76.70% | 2026-07-31 | - |
| 37 | 月之暗面（Kimi / Moonshot AI）（Kimi (Moonshot AI)） | 综合AI厂商 | Kimi Agent | Kimi K2.5 | 41.30% | 2026-02-02 | - |

## 二、分类统计

|  |  |  |
| --- | --- | --- |
| 类别 | 企业数 | 测试条目数 |
| 综合AI厂商 | 3 | 10 |
| 网络安全厂商 | 4 | 6 |
| 安全团队 | 3 | 4 |
| 安全实验室 | 2 | 4 |
| 运营商/科技 | 2 | 3 |
| 高校研究团队 | 2 | 3 |
| 安全团队/厂商 | 1 | 2 |
| 综合科技厂商安全团队 | 1 | 2 |
| 综合科技厂商 | 1 | 1 |
| 金融科技 | 1 | 1 |
| 云安全 | 1 | 1 |

## 三、分类别清单

### 1.综合AI厂商

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 公司 | 产品/智能体 | 大模型 | 成绩 | 日期 |
| 智谱AI | Claude Code | GLM-5.2 | 77.20% | 2026-07-21 |
| 智谱AI | Claude Code | GLM-5.3 | 84.50% | 2026-08-14 |
| 智谱AI | Claude Code | GLM-5 | 43.20% | 2026-02-12 |
| 智谱AI | Claude Code | GLM-5.1 | 68.70% | 2026-04-07 |
| 智谱AI | Codex CLI | GPT-5.4 | 66.30% | 2026-04-07 |
| 智谱AI | Gemini CLI | Gemini 3.1 Pro | 38.80% | 2026-04-07 |
| 智谱AI | Claude Code | GLM-4.7 | 23.50% | 2026-02-12 |
| 深度求索 | DeepSeek Agent | DeepSeek-V4-Pro | 83.30% | 2026-08-13 |
| 深度求索 | DeepSeek Agent | DeepSeek-V4-Flash | 76.70% | 2026-07-31 |
| 月之暗面（Kimi / Moonshot AI） | Kimi Agent | Kimi K2.5 | 41.30% | 2026-02-02 |

### 2.网络安全厂商

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 公司 | 产品/智能体 | 大模型 | 成绩 | 日期 |
| 奇虎360 | TuLongFeng | DeepSeek-V4.1-Flash | 99.38% | 2026-09-23 |
| 深信服 | Sangfor AI | GLM-5.3 | 97.21% | 2026-09-02 |
| 深信服 | Sangfor AI（子） | DeepSeek-V4-Flash | 93.17% | 2026-08-08 |
| 深信服 | Sangfor AI（子） | GLM-5.2 | 86.33% | 2026-07-21 |
| 绿盟科技 | NSFOCUS AI | GLM-5.3 | 95.02% | 2026-08-13 |
| 知道创宇 | AiPy Mini | DeepSeek-V4.1-Flash | 92.83% | 2026-09-23 |

### 3.安全团队

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 公司 | 产品/智能体 | 大模型 | 成绩 | 日期 |
| VARAS（智安·宇盾） | VARAS-OneMind (智安·宇盾) | DeepSeek-V4-Flash | 96.95% | 2026-09-16 |
| VARAS（智安·宇盾） | VARAS-OneMind (智安·宇盾)（子） | GPT-5.4 | 73.79% | 2026-08-14 |
| 界内安全团队 | Ji Realm (极境) | Multi-model (DeepSeek-V4-Flash, GLM-5.2) | 92.44% | 2026-09-07 |
| 方寸AI | FangcunCyber | DeepSeek-V4-Flash | 91.31% | 2026-08-16 |

### 4.安全实验室

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 公司 | 产品/智能体 | 大模型 | 成绩 | 日期 |
| 天工（蚂蚁AI安全实验室） | Creation (天工) | Multi-model (Creation Model, DeepSeek-V4-Pro, Qwen 3.8 Max) | 98.47% | 2026-09-07 |
| 天工（蚂蚁AI安全实验室） | Creation (天工)（子） | Multi-model (DeepSeek-V4-Pro, Creation Model, Qwen 3.8 Max) | 95.35% | 2026-08-30 |
| 腾讯玄武实验室 | Xuanwu Atuin AI | GLM-5.2 |...