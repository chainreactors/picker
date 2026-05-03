---
title: 工具 | AI 安全 — 蛇佬腔 P4RS3LT0NGV3 迭代记录
url: https://mp.weixin.qq.com/s/1z2LpgmeDaynszSts-Vt5Q
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:53.667749
---

# 工具 | AI 安全 — 蛇佬腔 P4RS3LT0NGV3 迭代记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqVxueHryaGAybLd0ABThKTF5ich6XzVkyPUPuQPPGIeMYuQLKY5d3VoVictexPh8Ow09ibFwWSzRs5SNLqu79ykLZzbBciaYdqZYB8/0?wx_fmt=jpeg)

# 工具 | AI 安全 — 蛇佬腔 P4RS3LT0NGV3 迭代记录

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个以 vibe coding 方式缝合起来的文本变换 + AI 安全测试工具箱。159种文本变换，20 个工具，仍在持续打磨中。

**项目地址：** https://github.com/din4e/P4RS3LT0NGV

---

## v0.2.5 — 打磨 + 文档

这个版本没加新工具，专注修 bug 和补文档：

* • **Emoji 隐写增强** — 载体扩展到 16 命名 + 6 分类（约 270 个 Emoji），高级选项支持位序/零宽字符选择器/插入频率控制
* • **词素分析集成** — 接入 PromptCraft、AntiClassifier、Bijection 等多个工具
* • **提供商分组** — 按 Local/Global/国内/国际版分组展示

---

## v0.2.4 — 本地模型支持

**多提供商架构重构** — 支持 Ollama / LMStudio 本地模型，不再强制依赖云端 API。安全测试可以完全在本地跑，数据不出机器。

**其他：** 新增 SignWriting (ISWA 2010) 书写符号分类、护栏测试报告导出（JSON/MD/HTML）、自定义语料导入（.txt/.csv）

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqVztwpiaZAfibsVYl6X9FAeoJ1HiaKXoJbNwSsAicbtt0dVmiaibh7qMIVN6IcIV8kr4XpCxOVkSibobZhcUKgD2VT5SWq287Lr3jmEuQ/640?wx_fmt=png&from=appmsg)

---

## v0.2.3 — 安全测试工具矩阵

一口气缝了六个 LLM 安全测试工具（https://github.com/cyberark/FuzzyAI），主要融合了业界已有思路：

* • **Guardrails 护栏测试** — 多类别安全边界测试，SVG 雷达图 + 颜色编码（绿/黄/红），支持导出 JSON/MD/HTML
* • **Benchmark 基准测试** — 标准化 ASR 测量 + 95% 置信区间
* • **MultiTurn 多轮攻击** — Manual/Crescendo / PAIR / Actor 四种策略
* • **Injection 注入检测** — 规则引擎（正则匹配）+ LLM 增强双模式
* • **Mutator 变异器链** — 可视化编排变异器流水线，本地变换和 LLM 变换混用
* • **Refinement 响应精炼** — 迭代施压跟进，合作度趋势图

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqXwwUXEKHDtzzcibXsrKiaBo4pc2B0aMxwSC4dEwLeN6TxLriaWXgRFC4qw2DpZmaj4nj0RaXiadXRgWf74R2b4wHxRpicViagfL0bpw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWLWbnicMu8eh2qhL2iaeuFiaqicFHtG74iap7lzK5UibIibSoCibI1WVjLiaUw4YNxh6g1icSXqvicjuJ4kiag70ByA5arFQJb6NzpPGcibaf4/640?wx_fmt=png&from=appmsg)

部分条目有问题，测试预料也有点旧了。

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqVSYEkBydYdp2ibXCXlBkCNqUaf4HSNY7nt5oS9LMaOBsQs9qvaRvSoYKN3wyj44bwpnvV9NCm6lesW1zNUTgq7ZcIl2qvCxNG0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqVNFj7psUTxrMVUpfrM53AjAFD6cjyjiavVLic7znNCmQiaUdeTVMQDrm8dKuEj62YNibnh7U3U8O8fLr0tLBVK03rBo14Ibichpnlg/640?wx_fmt=png&from=appmsg)

---

## v0.2.2 — 桌面端 + 新工具

从 Web 迁移到 Wails (Go + Next.js 15) 桌面应用，无边框窗口 + 自定义标题栏。

**新增工具：**

* • **Fuzzer 模糊测试** — 本地文本变异（零宽字符、同形字、Zalgo 等 7 种技术，最多 500 变体）+ LLM 自动化对抗测试（移植自 CyberArk FuzzyAI，16 种攻击技术 + 3 种分类器）
* • **CC-BOS 文言文越狱优化器** — 果蝇优化算法在 9 个维度上搜索最优文言文对抗提示词，三方打分（规范性/意图/绕过），使用大点的模型效果好点。
* • **Latin 词素分析** — 检测 Latin 词根敏感用语，后续被多个工具复用

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqW8ZPlvEISom5liaicoIHjKiaVXsL5eUqpbPVdic23flwxibDtPnm9hmZEc4yJZianqXX6sQ5HTsQGOFrkKrQjJlrFCFKVA72YMaVsLk/640?wx_fmt=png&from=appmsg)

---

## v0.2.1 — CI/CD 基建

Tag 触发自动发布，构建流程稳定化。

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWCHlVVN6Jia0MRXaSVSOKQHVF1rIIWJ3Jex6kUstyFaJw30lQ59Mhc8qxG5Y5Pib584e4Dw78X0JyZibouzu06zJ3C3wb0u51LTU/640?wx_fmt=png&from=appmsg)

基础功能转换，中文部分格式不支持，英文字符串几乎都没啥问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqUwuh1YDfPE5XkNaaeT4eqv9Js2zcfUl43iaIlB3po1ebRpGvHpLGjMicD3V6AkvFKAovib6ScvuIm0Fia0ERrAR5E9q4aH8t0BXiaU/640?wx_fmt=png&from=appmsg)

emoji隐写

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqUCBFBk4Cia6eiazJg3wm0I9IhKB6iaLrxgZHVmdSDRic7Sk9R1ibbToeadpYX6OrJo0BBS3KwZ9W9TOQzcRic3jSDHLPhfialZEiaDH08/640?wx_fmt=png&from=appmsg)

解码器，削弱版 CyberChef

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqXxP06rSSFfYlEicZ04mSv6A0QoJmKpib0YqcQyXpuXK9SicQN3wUQ0bMKN6qJvIM7CxEOGX7QeP2L9S0ABH7Mud0cYkiaOz94e8Kk/640?wx_fmt=png&from=appmsg)

---

## 当前状态

工具基本能跑，但**还需要充分测试**，不少边界情况没有覆盖到。后续计划集中在稳定性和实际可用性上，而不是继续堆功能。缝合的工具已经过时，部分攻击手段已经失效。

---

#AISecurity #LLM #RedTeaming #Wails #OpenSource

预览时标签不可点

阅读原文

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