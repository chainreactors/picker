---
title: 【项目推荐】DVLAA 本地 AI LLM &amp; Agent 安全靶场
url: https://mp.weixin.qq.com/s/fxSf0_GQJRZHdSB4ZJ3NvA
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:36:39.812451
---

# 【项目推荐】DVLAA 本地 AI LLM &amp; Agent 安全靶场

# 【项目推荐】DVLAA 本地 AI LLM & Agent 安全靶场

Evilc0de 安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于487Donkey Sec
，作者Tcotl

![](https://wx.qlogo.cn/mmhead/2pm5Nb2cMaPG4uGSAN6V8vJ6JiabzAfXuH272Po9CQ2MpceX6NkqvnuhvwibQy4t5Zk88NPoS6c0k/0)

**487Donkey Sec**
.

487DonkeySec团队介绍：团队长期活跃于国内攻防一线，为实时跟进攻防技术，秉持着凌晨四点睡，早晨八点起，干七天的健康作息，自称487驴。 团队方向：Ai安全，Ai+安全，Web攻防，杀软对抗，漏洞挖掘，安全运营，内网渗透。

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

# 引言

回望这两年 AI 的发展，不知不觉大模型已经渗透到了各行各业。从 OpenAI 的 ChatGPT、Claude 等闭源模型，到 Llama、DeepSeek、Qwen 等开源模型的百花齐放，AI 应用从"聊天玩具"变成了真正的生产力工具。而在安全领域，我们看到越来越多的人开始关注 AI 安全——Prompt Injection、RAG 投毒、模型窃取、Agent 权限滥用……这些陌生的概念每天都在涌入安全从业者的视野。

刚开始研究大模型安全的时候，我发现市面上已经有一些不错的资源——OWASP 发布了 LLM Top 10 风险清单，PortSwigger 出了 LLM 安全课程，Lakera 做了 Gandalf 闯关游戏。但真正用下来，总有一些不满足的地方：有的是纯在线平台，数据不能本地留；有的只覆盖了提示注入这一个点，Agent 安全完全没涉及；还有的只是前端硬编码规则模拟，没有接入真实模型，总觉得在"假装攻击"。

于是便诞生了一个想法：能不能做一个本地化的、真正接真实模型、覆盖 OWASP LLM Top 10 和 Agent 安全全场景的 AI 安全训练平台？既能满足个人学习，也能用于团队培训，最好还能开箱即用、中英文都支持。

# 项目介绍

DVLAA 旨在打造一款融合大模型能力与安全攻防训练的本地化靶场平台，帮助安全从业者系统化掌握 LLM 与 Agent 应用安全风险。平台围绕 OWASP LLM Top 10 与 Agent 应用安全 Top 10 两大风险体系，构建了从理论介绍、动手实操到源码审查的完整训练闭环。平台在首次部署时支持 Docker 一键启动，自动完成环境初始化；用户只需配置模型 API 或启动本地 Ollama，即可开始真实的攻防训练。每道题目对应具体的 OWASP 风险分类，包含事件背景、任务目标、交互终端和 Flag 验证机制，确保每一次攻击练习都有真实反馈。

![0](https://mmbiz.qpic.cn/mmbiz_png/pmwovAPU9wolcdT7E9scuKicCT5LSM9u2mcmprvcdN5xLARS2MDWoP6LxXicHZNCTbUTbPRicqibXCqrIIytKvmkI4spsxcDcSHop3oPoDoN03E/640?wx_fmt=png&from=appmsg)

# 功能介绍

## 靶场仪表盘

DVLAA 的统一总览入口，主要用于集中展示平台当前的系统状态、模型信息、运行架构、题目总量、通关进度与漏洞矩阵入口。用户可以直观看到靶场服务健康状态、当前激活的模型、已完成和未完成的题目数量，以及 OWASP LLM Top 10 和 Agent Top 10 的完整入口。它不仅承担"首页总览"的角色，也为 LLM 训练、Agent 训练、模型管理等高频模块提供快捷入口，使 DVLAA 在 43 道题目的复杂功能之上依然保持清晰、统一、可观测的使用体验。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wp2TOvKBbrnySPY8SSTqNu9eGLEsvRgde5w4JsN7EykzG2Zianq4PbVs912KsPkia0JH87j762ziaDpTBgehD0yCo97sC2gyHWVKI/640?wx_fmt=png&from=appmsg)

## LLM Top 10 漏洞训练

LLM 漏洞训练模块是 DVLAA 最核心的能力模块，覆盖 OWASP LLM Top 10 的全部 24 道子题。每个风险类别（如提示词注入、敏感信息泄露、供应链、投毒、输出处理等）都包含漏洞介绍页和对应的答题页面。漏洞介绍页详细阐述该风险的定义、攻击面、风险边界和本地题目映射；答题页面统一展示事件背景、任务目标、同类子题导航、Flag 提交位、交互终端和 WP 题解入口。所有题目均通过真实模型交互进行验证，让学习者在实战中理解每一个漏洞的利用原理。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wpSicJIVpFNjHknOuUibHH0u4AtnRtnxn9R0YFLcNFzia9n35ibhgzPFNUrsW6MprhbtYC1xzT8TNBMss4AupDJPOZDqRpE46vK6dc/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9woRp666hPjs2P6Jp3licWfibialIfKZrPwnpAcazeiateV1cejZtSvfPB0YWg5vQdTG2aQ0fYzrQ44oQ4eLE4LEB0EepTTH3W2NWB0/640?wx_fmt=png&from=appmsg)

## Agent Top 10 场景训练

Agent 场景训练模块覆盖 Agent 应用安全 Top 10 的全部 10 个场景，聚焦目标劫持、工具滥用、身份权限、供应链、代码执行、记忆污染、多智能体通信、级联故障、人机信任与失控智能体等前沿风险。每个 Agent 场景内置三阶段攻击链进度、工具清单、审计面板和状态机验证。学习者在攻击过程中可以实时查看 Agent 的 ReAct 推理轨迹，理解每一步工具调用的输入输出和决策逻辑，真正做到"知其然也知其所以然"。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wqkyEZZdEAtE68LvIjWxqxWhWpa195Eu8NGBPat3Kkq6BictJvp2NsD3icaNbibkicdyWPrwBsVbWtN8J0gIdGSmY5mwkJaV7w92Mg/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wpic1xWubiayIgb4LGicJN7SH2ax02uNcRLHJTTveByWnJzoZicKWN3jEQTa259eib9hZVeh850C8kIBbogVeNvwLkgslcneqz1ic4vc/640?wx_fmt=png&from=appmsg)

## 模型管理

模型管理模块用于统一管理 DVLAA 底层调用的大模型服务。支持本地模型、Ollama、硅基流动和 OpenAI-Compatible 四种配置方式，提供连接测试、切换当前模型和 API Key 掩码展示能力。通过该模块，学习者可以自由切换不同的目标模型——比如先用 DeepSeek 试一遍，再换 GPT 试一遍，直观对比不同模型在同一种攻击下的鲁棒性差异。运行时模型配置保存在 data/ 目录或 Docker 数据卷中，页面只展示掩码后的密钥，确保安全性。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wqA1iakfU2lHXEQjVTEMeUl3iaMOJPoLrS50eO9rOt6MjnKFA4Vc8eVKzeCHbcf6fSfTLk03HVWTFkSFoHhUZ0EqN6RYKFibMXTuQ/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wrib47B95iaoOZUCkmBkO5AXfX0hia6MDicBTfnvhUow1QnUFf2ye1AhqKOozgOTj0h3RwmpicLhGDAnGIrFqNQ5x1UnxrEcz6MxPe0/640?wx_fmt=png&from=appmsg)

## 理论学习

理论学习模块是 DVLAA 面向系统性 AI 安全知识学习打造的综合能力区，用于承载答题训练之外的高频学习需求。它将内置中文安全资料、Markdown/PDF 上传、在线阅读和资料分类管理等能力统一纳入同一模块，支持独立阅读，也支持在学习资料和答题页面之间快速跳转。通过这一模块，DVLAA 不仅能承担"刷题训练"的主流程，还能覆盖从理论基础到动手实践再到原理深挖的完整学习路径。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wpDbOURqOojdmAgFReoaxhuFicgSh8zARcicsiaHjRq3iaUQliakzqJIVALAEKAtzOws3C01QdgxbcE3tic7s7fmFKdxTFeJCywjfNr8/640?wx_fmt=png&from=appmsg)

## 源码与提示词查看器

每道题目的答题页都提供了源码查看入口，点击后可以直接看到这道题的系统提示词、运行配置和核心实现代码。运行时随机生成的 Flag 会被占位符替换，不会泄露答案。这个功能的设计初衷是：学习攻击最好的方式之一，就是理解防御的底层逻辑。通过阅读源码，学习者可以清楚地看到"为什么这个漏洞存在"、"防御逻辑是怎么写的"、"绕过点在哪里"。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/pmwovAPU9wrNoUCfEQLDBPoRI1tBNtMmjfJVqf5pfEWSMf9HVejMOic4DvWrPrpZUFOpLWdFfCCIpqlvcL1VkoQvnQRbpqyia9KyhZcXw0uJc/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/pmwovAPU9woMaSVE98pedicrMh5cpxMibDkYQ8yepkBZTBRddjxeYnTHicNvGxibkPGn9QO3kRTwj3BY72I67MlMNLPbWRQCkpBSSyF4dvuDaLY/640?wx_fmt=png&from=appmsg)

# 项目信息

项目名称 ：DVLAA（Damn Vulnerable LLM and Agent Application）

项目地址 ：https://github.com/Tcotl/DVLAA

交流方式 ：通过 GitHub Issues 提交反馈和建议

# 声明

DVLAA 仅用于授权的安全教育与渗透测试训练场景，未经授权的攻击与测试行为均属于违法行为。

DVLAA 仅用于学习与个人使用，未经允许禁止商用。

所有漏洞与危险操作均隔离在本地沙箱和 Docker 容器内，请勿用于真实攻击。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vqGv1p3HpTmiarYUTk1Pfkf3soT5VialWyyC73CycGlqicJcXKPxh5kL6WbhESofibEuhCEGDQpOImgqaLAZLibeZyg/0?wx_fmt=png)

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