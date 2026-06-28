---
title: GPT-5.6正式亮相，但被白宫装上了“安全门禁”
url: https://mp.weixin.qq.com/s/gwADc_x2wVRAzqLpIZYUAQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:57.492094
---

# GPT-5.6正式亮相，但被白宫装上了“安全门禁”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3VAbGdShjQ9ks3mqCCn9Zr7SyScicZ5XPLyVHibelSenQG5ibGtaAYd2D5VicraiabZOqEvwHLhFdVDbibb2GMstToWvbn5YYZW7qCA/0?wx_fmt=jpeg)

# GPT-5.6正式亮相，但被白宫装上了“安全门禁”

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX046oF8l9uotoBx1h1BLicEDPqrtTADyFOYQhulvfiatOmJANh67ZicZoRoavA8IYhvicqiaAB9gibJm0PYwAfDtKrfbb2VoyGXvteYA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1RicxYXtusxVdAx4tMrIriaARPMSk92a3iaS0MZUdFlM27agKIVzCKcA95q9KXMSDKibdR05rx49GAxf6JyWpYicDgqiauRDuvJdXso/640?wx_fmt=png&from=appmsg)

OpenAI正式发布GPT-5.6系列模型有限预览版。该系列包含GPT-5.6 Sol、GPT-5.6 Terra和GPT-5.6 Luna三款模型，分别对应高难度推理、大规模生产和日常高频任务等不同场景。

与以往单纯强调性能提升的模型更新不同，GPT-5.6的发布同时围绕能力边界、安全审查和分阶段开放展开。OpenAI表示，模型初期仅面向少量受信任合作伙伴开放，后续再逐步扩展至ChatGPT、Codex和API等更广泛场景。

Part01

三款模型上线，覆盖不同使用场景

GPT-5.6系列采用Sol、Terra、Luna三档命名，核心逻辑是让用户在智能、速度和成本之间做更清晰的选择，而不是简单区分"大模型"和"小模型"。

* GPT-5.6 Sol：旗舰模型，面向复杂推理、长期任务、多工具协同、网络安全和科研等高难度场景。
* GPT-5.6 Terra：低成本模型，适合客户支持、内部工具、文档分析和大规模生产环境。
* GPT-5.6 Luna：轻量模型，面向摘要、起草、常规自动化和日常内容处理等高频任务。

![三款模型对比](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Jj9TLLaLEfz0iaWvDySLBVw47kepLjzpy1GYQibbmNLg5A9CVBU6sGjc3fTFS8YYcPlO1wfZ5wzRLB7J0R6l7hR8wsIS6gEXJI/640?wx_fmt=png)

Part02

Sol能力提升，长链任务表现突出

GPT-5.6 Sol是此次发布中最受关注的模型。OpenAI为其提供更强的推理配置，其中max模式更适合需要深度思考的任务，ultra模式则可调度多个子智能体，把复杂任务拆分后并行推进，再汇总输出结果。

这种设计使Sol在长链任务、命令行工作流和多工具协同中表现更稳。在Terminal-Bench 2.1测试中，Sol取得领先成绩，说明其在规划、迭代和工具调用方面较前代模型进一步提升。

![GPT-5.6 Sol在Terminal-Bench 2.1测试中的表现](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2TbOb3y77YcJrKYnBJickK0Aib5vNdHR7G761niafic6Nj7c0VjVibJsK8wFibyv4NibOfRS76UPbznY69B2WMy5trcyYpNMWG5dYGwg/640?wx_fmt=png)

GPT-5.6 Sol在Terminal-Bench 2.1测试中的表现

除软件工程场景外，Sol在生物信息学任务中的表现也有所提升。OpenAI披露，Sol在GeneBench v1等基准上优于前代，并在部分任务中以更少输出token完成更高质量的分析。

Part03

网络安全能力增强，边界仍需控制

网络安全方向是GPT-5.6 Sol此次升级中最敏感、也最具讨论度的一部分。OpenAI称，Sol在漏洞研究、漏洞识别和长期安全任务处理方面均有进展，尤其适用于帮助防御者发现和修复问题。

在ExploitBench等安全评测中，Sol以较少输出token接近顶级安全模型表现；在推理时间延长后，其处理复杂网络安全任务的能力也会随之增强。这意味着模型不只是"答题更准"，也更适合处理持续推理和多步骤分析任务。

![GPT-5.6 Sol在ExploitBench测试中的表现](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX26y6E43Eib3SpCWCX1DdicWF4iczQFMeiaYicSPvdV4oFrPxjCQa03BdSguOicCxQfhVLMWh10lAe0huytibC4pergsqSh9uQlLRxahM/640?wx_fmt=png)

GPT-5.6 Sol在ExploitBench测试中的表现

不过，OpenAI也明确划出了边界：Sol在受控测试条件下可以识别Chromium和Firefox中的漏洞及利用原语，但尚不能在无人类指导的情况下自主拼接出完整漏洞利用链。因此，OpenAI认为其尚未触及"网络安全关键"评估阈值。

![GPT-5.6系列在内部CTF任务中的表现](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2lia0rAFLz4ebJ1QL0jjH6PIqtJmcRRAVxIyZXycyxDUjesDwicrnEGItv3yx4fZicNlmQqdiaaOPQwCYkM3YfFgSIuBlMwBLxfnY/640?wx_fmt=png)

GPT-5.6系列在内部CTF任务中的表现

Part04

降低高能力模型滥用风险

正因为模型在网络安全、生物信息学等敏感领域能力进一步提升，OpenAI在此次发布中把安全体系放在了更重要的位置。GPT-5.6并不是简单"放开能力"，而是在更强能力外层叠加更严格的约束机制。

具体来看，GPT-5.6的防护体系包含三层：模型层面训练其拒绝违禁网络攻击请求，并识别伪装意图和越狱尝试；生成过程中部署实时分类器，发现潜在违规后暂停生成，并由更大规模的推理模型复核；账户层面则监测跨会话风险信号，识别持续性恶意行为模式。

为验证这些防护是否可靠，OpenAI投入超过70万个A100等效GPU小时开展自动化红队测试，重点覆盖通用越狱、恶意提示注入和可跨场景泛化的攻击路径。同时，第三方人工专家红队测试也会贯穿整个预览期。

Part05

前沿模型进入受控上线阶段

GPT-5.6并未在发布当天面向所有用户开放。OpenAI表示，公司已提前向美国政府通报模型能力和发布计划，并按照要求先向小范围受信任合作伙伴开放API及Codex访问权限。

这一安排说明，前沿AI模型的发布逻辑正在变化。过去，模型上线主要围绕性能、成本和产品体验展开；现在，网络安全、生物安全、政府审查、合作伙伴准入和双重用途风险，正在共同影响模型发布节奏。

OpenAI也指出，政府接入和审查流程不应成为长期默认模式，否则可能延误开发者、企业、网络安全防御者及全球合作伙伴获取先进工具。此次有限预览，更像是OpenAI在能力快速演进与安全治理仍在成形之间做出的阶段性平衡。

Part06

结语

整体来看，GPT-5.6并不是一次单纯的模型参数或性能升级。Sol、Terra、Luna分别覆盖高难度推理、低成本生产和日常轻量任务；与此同时，更强网络安全能力、更严格安全体系和更谨慎的开放策略，共同构成了这次发布的核心变化。

对于开发者和安全从业者而言，GPT-5.6的意义不只在于"模型更强"，更在于前沿模型正在进入一个更受控、更审慎、也更强调责任边界的部署阶段。

参考来源：

Previewing GPT‑5.6 Sol: a next-generation model

https://openai.com/index/previewing-gpt-5-6-sol/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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