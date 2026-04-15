---
title: 从\"鲁迅为什么暴打周树人\"看AI\"真相\"
url: https://mp.weixin.qq.com/s/rpyW4Zr0h1oU3nyNabsQhA
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:56.950904
---

# 从\"鲁迅为什么暴打周树人\"看AI\"真相\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PIWj1VguNotAMJPDwZJYMKXoHfb7QQwAv8j9DaYR4kCOiaWShzxP0icHySphpB00VvWN8EIeRpuK4VZxyldjBicSMrNtXa2blESFibicrcn1wU9g/0?wx_fmt=jpeg)

# 从"鲁迅为什么暴打周树人"看AI"真相"

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **[ 🔍 智库导读 ]** 当前企业的现状就是：**无AI = 无KPI**，哪些整天特吹AI无所不能的人真的 **懂AI**吗？
>
> 很多人问，为什么 AI 发展到 2026 年，还是改不了撒谎的毛病？
>
> 事实是，**AI 从未打算告诉你真相。** 当你问它 **‘鲁迅为什么暴打周树人’** 时，它并不是在翻阅历史书，而是在玩一场名为‘概率接龙’的高级拼图。它排列出的每一个字，都只为了满足下一个字出现的数学概率，而非现实世界的客观事实。”

---

### 一、 什么是幻觉？一场华丽的“概率拼图”

正如权威论文 *《Survey on Hallucination in Large Language Models》* 所界定的：**幻觉是指模型生成的内容与现实事实或给定上下文不符。**

要理解它的由来，我们需要回溯到计算机科学中一个经典的技术——**马尔可夫生成器（Markov Generator）**。

* **逻辑拆解**：马尔可夫生成器会统计单词出现的频率。它发现“the”后面接“whale”的概率是 10%，接“harpoon”是 5%。
* **本质**：当你运行它时，它根据概率盲目选择下一个词。它完全不了解单词背后的意义，它只知道哪些词经常“凑在一起”。

**今天的 LLM（大语言模型）本质上并没有摆脱这种机制。** 虽然它更庞大、更复杂，但底层依然是在 **“预测单词”**，而非 **“理解事实”**。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosSgIe11YMJFL9glmU99laPicpLmebjAxo2NgeHfzJ6jRSdujZuGMLSvUH6flhwhYUmeQYOI9VSVbQZuNLek5tY216NcwOIOW0c/640?wx_fmt=png&from=appmsg)

---

### 二、 幻觉的三大“导火索”

为什么 AI 会在关键时刻掉链子？主要源于以下三个不可规避的痛点：

#### 1. 概率预测的代价

当 AI 生成一段逻辑通顺、语法优美的回答时，它只是完成了一次完美的“概率接龙”。至于这块拼图在现实中是否真实？**对不起，这不在它的算法考虑范围内。**

#### 2. 训练数据的局限

模型学到了互联网上过时的、甚至虚构的信息。对于冷门知识，它会基于模糊的记忆片段进行 **“二次创作”**，导致张冠李戴。

#### 3. “过度讨好”的倾向

为了完成用户指令，模型有时会表现出 **“讨好型人格”**。在用户的诱导下，它会编造理由来顺应错误的假设，甚至强行给不存在的事物寻找解释。

---

### 三、 既然无法根除，如何有效“缓解”？

幻觉是概率接龙的副作用。既然无法彻底消灭，我们就需要给这套机制戴上“镣铐”。以下是目前行业公认的**四剂“特效药”**：

#### 药方 1：RAG（检索增强生成）——给 AI 一本参考书

这是目前最实用的方案。不要让模型完全凭记忆“闭卷考试”，而是在回答前，先在可靠的私有库中检索事实，**强迫模型“照着书说”**。

#### 药方 2：设置“逃生口”

在 Prompt（提示词）中明确规定：**“如果你不知道答案，请直接回答‘不知道’”**。这能有效抑制模型的编造欲。

#### 药方 3：思维链（CoT）——让 AI 想清楚再说

引导模型写出推理过程。当模型被迫展开逻辑细节时，更容易触发内部的 **“语义对齐”**，从而实现自我纠错。

#### 药方 4：降低 Temperature（温度系数）

在技术参数层面调低“温度”，减少随机性，让模型生成更稳定、更确定性的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNovaibVx6oT8aMmkjTJeuEcqO2NZVGJSpqH59Wz63MLvLJMicPJy83NGpPEGDNfFDiaJLuTtlQgPvPIOpD5eFdFRLc6mUm6noZgenc/640?wx_fmt=png&from=appmsg)

---

### 四、 结语：创造力与谎言的“双面性”

**幻觉是大模型的本质属性，它与模型的创造力其实是同一枚硬币的两面。**

正如人类的想象力偶尔会滑向谎言，AI 的幻觉也预示着它模拟世界的巨大潜力。理解了马尔可夫式的“单词预测”本质，我们就不必神话 AI，也不必因噎废食。

在通往 AGI（通用人工智能）的路上，**“去伪存真”将是每一个 AI 从业者的必修课。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

APT-101

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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