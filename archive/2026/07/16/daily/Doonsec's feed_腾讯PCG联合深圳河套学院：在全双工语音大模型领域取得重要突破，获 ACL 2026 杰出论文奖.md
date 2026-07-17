---
title: 腾讯PCG联合深圳河套学院：在全双工语音大模型领域取得重要突破，获 ACL 2026 杰出论文奖
url: https://mp.weixin.qq.com/s/d7TgHluCVmGM90Rjjny0Mw
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:57:12.840448
---

# 腾讯PCG联合深圳河套学院：在全双工语音大模型领域取得重要突破，获 ACL 2026 杰出论文奖

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz9059MYgAUGpApViaLF9GRQMJNIPRibicfdgsQa90psgvfz49Tb1ITkZyuQZ08vX8RicWxZKruicejg0OvEmPskF8oLiaq1F6ytlmYoqsg/0?wx_fmt=jpeg)

# 腾讯PCG联合深圳河套学院：在全双工语音大模型领域取得重要突破，获 ACL 2026 杰出论文奖

腾讯技术工程
腾讯技术工程

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](http://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

近日，自然语言处理领域顶级国际学术会议 ACL 2026 公布获奖结果，腾讯PCG技术线-AI创新应用中心联合深圳河套学院AI训练平台张民教授团队凭借全双工语音大模型研究成果 《Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs》 斩获大会杰出论文奖。ACL(国际计算语言学协会年会)迄今 64 届，是 NLP 领域历史最悠久、学术地位最高的国际顶会，被中国计算机学会(CCF)列为 A 类推荐会议、国际 CORE 评级体系列为 A 等级。本届ACL共收到投稿逾 1.2 万篇，杰出论文仅18篇。![image](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz907lPtoTTd9Rx8jtO8kxbVt4VibTOrZSSV108iaYDEuYESX5ECK4BmUicQgcibiaIm5Y6VzgeoC1dj4iao4W86Kt5ibgSfrBmbIpia0AU1c/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

---

🔗 **论文地址**：https://www.researchgate.net/publication/408700315\_Hierarchical\_Acoustic-Semantic\_Modeling\_Modality\_Separation\_and\_Semantic\_Coherence\_for\_Full-Duplex\_SLMs

### 01 问题：为什么过去的语音交互总是不自然？

在大模型快速走向真实应用的过程中，语音交互正在成为 AI 与人连接的关键入口。相比文本输入，语音天然更接近人的交流方式，但现有语音 AI 常常停留在"一问一答、听完再说"的轮次式交互范式。

近期，OpenAI 发布的 GPT-Live 又一次将实时语音交互推至聚光灯下，也进一步印证了一个趋势：语音交互正在从轮次式问答，走向连续、双向、实时的自然交流。

但要真正实现这一目标，真正的难点，不只是让系统"看起来可以被打断"，而是让持续倾听、语义理解、语音生成和节奏控制成为模型内部原生具备的能力。如何在保持语义理解能力与推理效率的同时，实现响应迅速、回答准确、对话自然的原生全双工语音交互，正是语音大模型走向类人交互的核心挑战。

在此背景下，腾讯 PCG 技术线-AI 创新应用中心，联合深圳河套学院AI训练平台张民教授与户保田教授立知大模型团队、香港中文大学（深圳）李海洲教授团队，研发了原生端到端全双工语音大模型 Lychee-FD。Lychee-FD 不仅在多个全双工语音交互基准上达到业内领先水平，也首次揭示了原生全双工语音大模型长期难以兼顾交互流畅度、语义理解能力与推理效率的根本原因。这意味着，全双工语音交互不再是靠外部模块拼凑出的产品体验，而是模型在连续语音流中同步倾听、理解与回应的交互本能——它标志着语音交互真正走向了原生类人交互智能。

![a09080d4-6959-40c2-8ead-1a68293f794b](http://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz906vlCuCNQgTGPgiaFKD4c8GqxKSmtv8icQcpcmciaqb1FzRicP4Eic819gjSIWib93k1a9dFxic8NibNjbwettmiareynzO7Zs8nVINlN2g/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

为达到全双工交互的体验，行业中有一些系统级全双工方案：在传统语音链路外部增加打断检测、状态判断和调度模块，让 AI 看起来可以边听边说。但这种系统级全双工，本质上仍然是多个模块在外部协作——一个模块负责听，一个模块负责想，一个模块负责说，另一个模块负责判断什么时候该停、什么时候该接话。

然而，这种级联的架构不仅带来了延迟、生硬的轮次切换，并且还有更致命的问题：听、想、说、控节奏被拆散了，AI 的语音理解与表达就很难真正统一。

Lychee-FD 走了一条完全不同的路：原生端到端全双工。它不是在旧系统外面叠加全双工模块，而是把持续倾听、语义理解、语音生成和对话节奏控制，统一注入到大模型内部。模型不只是更快地回答，而是开始学会如何像人一样参与一段对话。

---

### 02 Demo：全双工能力，看四段真实对话

> **📹 视频 Demo 1：**同时听说的能力：

——演示 用户争吵

---

> **📹 视频 Demo 2：**单向倾听同时实时反馈的能力

——演示 AI 助手倾听用户的烦恼并整理信息

---

> **📹 视频 Demo 3：**单向诉说同时智能停止的能力

——AI助手自助讲故事哄用户睡觉，确认睡着后自我关闭

三段 Demo 分别对应全双工交互的三种典型模式：听说并行、边听边应、边说边判。它们共同指向同一个目标——让 AI 像人一样参与对话，而不只是快速应答。

全双工闲聊部分能力体现在QQ 测试bot：

> **📹 实机体验**

尔尔录屏实机.mp4

QQ 扫码体验

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz9060LZ2ZBOZozC45XibPicDtoYekT2cHNlGMShGqYFngadVONR83SRnqbibDicV4iaXLia7MTvKPhOxI5eoKg23lNLmZrsAP0rLeuV5wc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz906HUDSj3jJUBicvcFtBmXRIxXibn5ibImFhEUHAFMnLrnOJmmPVPUOLxyZpZLcREIzyPBOibs4reLth2l6h787Bwcqibmf0hOqzReWg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

---

### 03 Lychee-FD：原生端到端全双工语音大模型

为了实现流畅自然的类人交互，原生全双工遇到的挑战不只是边听边说。真正困难的是：模型既要保持大语言模型的理解和推理能力，又要实时生成自然语音，还要在连续对话中判断何时倾听、何时回应、何时停止输出。

过去很多方法往往只能在两端取舍：要么保留智能，但引入复杂模块和更高延迟；要么追求端到端低时延，却牺牲语义理解和知识保持能力。

> **Lychee-FD 的核心价值，在于它不是绕开这个问题，而是首次从模型优化机制上揭示了原生全双工语音大模型难以做好的根本原因，并围绕这一原因完成了架构设计与工程实现。**

#### 1. 科学洞察：揭示原生全双工降智的根本原因

在原生端到端全双工模型中，语音和语义并不是简单“合在一起”就能协同工作。

**病因一：深层梯度冲突。** 论文通过细粒度的优化动态分析发现，当声学建模和语义建模被迫共享同一套深层参数空间时，二者会出现内生的**梯度冲突**：浅层网络中，语音和文本目标仍然可以相互协同；但进入深层之后，它们的优化方向开始分化，甚至互相牵制。就像让同一个人同时背诵诗词和解数学题——刚开始还好，越到深层逻辑，两件事开始“打架”。

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz907Q063gcANn1VGjcqicdInTovibicbd5Kiaiblj6pnqNIwvsIRHwIhK1qOvfocvM0TuACF16sibSS0Scic0a7J5A5ZL624ZV0xO4TU7jM/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

**病因二：语义稀释。** 由于语音信号频率远高于文本语义信号（语音约 25Hz，文本约 3Hz），传统对齐方式要用大量填充 token（padding）补位，导致文本序列中 80% 以上都是无意义的 padding。稀疏的文本监督被高频声学信号淹没，模型在训练中逐渐偏向“复现声音”，而削弱了对语义逻辑的保持。

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz905bVuJy9pzlyOnVehQIys2T6f8cjt2pLLwDXUtRL9XTzP4wlPDTlFib2ssBzBk6Vlq1j7tTd9FjRiaHK8J3d745EspYyWicslJm2o/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

**这一发现解释了为什么原生全双工语音大模型长期难以同时做到“聪明、自然、低时延”。问题不只是工程不够快，而是模型内部的语音生成和语义推理本身存在深层冲突。**

#### 2. 架构创新：用层次化解耦解决层次化冲突

找到问题之后，Lychee-FD 的方法并不是简单增加模块，而是在模型架构上做了对应设计。

团队提出了**层次化语义-声学建模框架**：在浅层，模型保留共享主干，让语音和语义共同学习底层表示；在深层，则将语义、声学和对话控制拆分为不同的专门通道，让它们各自完成最适合自己的建模任务。

简单来说，浅层负责“共同理解输入”，深层负责“各司其职”：语义通道保持语言理解和知识能力，声学通道生成自然语音，对话控制通道判断开始、停止和交互节奏。同时引入密集语义对齐通道（内部独白），让模型在生成语音的同时保留清晰、连续的“内部语义线索”。

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz904KRufPZ1MDq17LmHOWuj3hc927W7BvJrcaOXffjuIufSvJNeHthbD0kUE4Hoe3KNs0oSS3au9WYNf0fEDOkBMU9TK3hNPoJkI/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

因此，Lychee-FD 的全双工能力不是外挂的打断模块，也不是级联系统里的流程调度，而是被内化到模型架构中的原生交互能力。实验结果也验证了这一点：Lychee-FD 在 Spoken QA 任务上平均提升7.4%，在 FullDuplexBench 1.5 上平均提升28.5%，在 3 个全双工语音交互基准的 10 个指标上达到当前领先水平。

#### 3. 工程实现：从论文模型到可在线交互系统

真正的全双工交互，最终必须落到实时系统里。Lychee-FD 的架构同时生成语义、声学和控制信号，这对推理引擎提出了新的挑战。

为此，团队以 vLLM 为高性能推理底座，围绕层次化多通道架构进行了定制化改造，**开发了实时并行多流推理框架**：在共享主干完成计算后，系统会将中间表示分发到语义、声学和控制通道，使多个专门通道并行执行，并分别管理多流 KV cache。相比基础推理框架，该并行多流推理框架实现了 **2.96 倍**的提速，同时将 GPU 显存占用降低23%。

![图片](http://mmbiz.qpic.cn/mmbiz_png/KVER9adz904uPgWqn7f8HdjEwSvhttribF0S0yibN72jpdQcibgAibE8NYKJEr2J1lQzvEZSTPgUKUnNeNOwEYkN4SbsFYE1CmiaVssGlbyJ5mFQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

同时，团队进一步提出**控制头早退策略**。由于打断、停说、转入倾听等行为首先依赖控制信号，系统不必等待完整语音和文本生成结束，而是让控制 Token 更早产出，为打断响应提供一条“快速通道”。

> **从科学洞察，到架构创新，再到在线推理引擎优化，Lychee-FD 完成了理论突破、算法创新和工程实现的全栈闭环。**

### 04 ACL 情况

#### 4.1 ACL 是什么

ACL（Association for Computational Linguistics，计算语言学协会年会）是自然语言处理（NLP）领域最顶级的国际学术会议，与 NeurIPS、ICML 并列为 AI 领域最高荣誉平台。

* **录取率极低**：ACL 2026 共收到投稿 12148 篇，主会录用率约 19%
* **获奖更难**：Outstanding Paper 获奖率  0.15%
* **工业价值高**：ACL 获奖论文通常直接代表产业落地能力，历届获奖均在翻译、语音、大模型等方向留下重要印记

####

![图片](http://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYjZ7Hx6Udjjk2BGLzC9ahJq7ibxDd1RGA0c9NYZc1husEsvb3tY4FcWPQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

![图片](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj5q5PQEOc5ibURPb03vnRibrxC3UR8xzdyATfiawTYRV2vJvBnAIcE1FeQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

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