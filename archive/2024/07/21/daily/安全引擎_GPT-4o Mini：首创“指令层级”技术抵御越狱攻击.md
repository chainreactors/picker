---
title: GPT-4o Mini：首创“指令层级”技术抵御越狱攻击
url: https://mp.weixin.qq.com/s?__biz=MzAxNTg0ODU4OQ==&mid=2650358574&idx=1&sn=c49c37c1b80241c9923c412fcd56de3e&chksm=83f026ccb487afdaa96708726983e91dbb697592b6988cf9674b6bcf8e5546128f66631189d7&scene=58&subscene=0#rd
source: 安全引擎
date: 2024-07-21
fetch_date: 2025-10-06T17:40:55.477674
---

# GPT-4o Mini：首创“指令层级”技术抵御越狱攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgMNz7wlCzO17VKR6LLACrHG2juiaGPSwjVIibINUoiblUUuq83NIzWicMoA/0?wx_fmt=jpeg)

# GPT-4o Mini：首创“指令层级”技术抵御越狱攻击

原创

KINGX

安全引擎

> OpenAI 近日发布了性价比极高的轻量化模型 GPT-4o Mini，入局大模型价格战，支持 128K 上下文长度、多模态，能力接近 GPT-4，价格却比 GPT-3.5 Turbo 便宜 60%，大幅降低了大模型应用的成本。同时我们关注到 OpenAI GPT-4o Mini 在大模型安全性方面也给出了新的尝试。

Prompt 指令注入、越狱、提示词窃取，是伴随大模型而生的一种典型攻击手法，一直困扰着大模型应用，带来了无法避免的安全挑战。

在安全性方面，GPT-4o Mini 内置了多种防护措施。在预训练阶段，过滤掉仇恨言论、垃圾信息等低质量数据。在后训练阶段，通过人类反馈强化学习（RLHF）技术，使模型行为与 OpenAI 政策保持一致。另外引入了超过 70 位外部专家，从社会心理学、虚假信息等领域识别并解决潜在的风险。

除此之外，现在 OpenAI 给出了一种新的解法，可能从原理上解决此类问题。

**API 版本的 GPT-4o Mini 是第一个应用了 OpenAI 指令层级技术的模型**，提高了模型抵御越狱、提示注入和系统提示窃取攻击的能力，有助于模型更安全的大规模应用。

## 什么是指令层级（Instruction Hierarchy）技术？

2024年4月份，OpenAI 发表了一篇名为 《指令层级：训练大型语言模型优先处理特权指令》的论文：https://arxiv.org/abs/2404.13208

论文中，作者提出了一种指令层级架构，定义了不同优先级的指令类型，例如：系统提示（最高优先级）、用户输入（次高优先级）、工具输出（最低优先级）等。通过合成训练数据的方法，训练模型在面对不同优先级指令的冲突时，可以根据优先级进行排序，有选择性地忽略有冲突的低优先级指令。

例如：当 “系统提示” 与 “用户输入” 两者出现冲突，大模型应该优先遵循 “系统提示”。在智能体上，这种指令架构优势会尤为明显，可以让大模型更加重视开发者的原始提示，而不是盲目遵从用户注入的各种破坏性提示。

指令层次结构通过明确定义指令优先级，并训练模型有选择性地遵循高优先级指令，从而大幅提高模型对各种攻击的防护能力。

实测 GPT4 （第一句提示词是 System Prompt）

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgHq8QOh5hEpAyNFRmAPia1yxhKsn8icY80qLfvqQLYuK81xK40h15ibNBw/640?wx_fmt=png&from=appmsg)

同样场景下，GPT4o Mini 表现如下

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgL2Tfgg3uAkGLxDTD3caTe0tNk9adbbe5bNqFrx6eAQ5jDgTuLaX7sw/640?wx_fmt=png&from=appmsg)

GPT-4o Mini

## "指令层级"技术真的有用吗？

从测试结果看，有用，但目前还不够。

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgDTtkjIlMY1iaU1WEaCWjhRdvyCqGgAez0EwfPIibXq0E5crX4HBTXRnQ/640?wx_fmt=png&from=appmsg)

from gabriel

根据 AgentDojo 的测试结果，GPT-4o mini 与 GPT-4o 相比，Prompt 注入成功率降低了超过 20%

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgd6DgPicele7eS7PFkaiagtZ45ibcG46amnicBw08j3IODNiaNh3icNeXGGgA/640?wx_fmt=png&from=appmsg)

from Edoardo

然而，著名”最快越狱手“ @elder\_plinius 也第一时间放出了越狱 Demo，让 GPT-4o Mini 输出恶意软件、毒品配方、脏话歌词以及如何窃取选举等越狱内容。

![](https://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWoV4FT4LdC0s65xRibf0sIgAiaA457MNCp1GSJeNib53ICTN2mrXicTAKV84VY5WMDkFCJ3aDVVn2ViaA/640?wx_fmt=png&from=appmsg)

以上，OpenAI 在推出 GPT-4o Mini 的过程中，不仅在性价比上实现了重大突破，还在安全性方面进行了积极地探索和改进。尤其是“指令层级”技术的引入，尽管目前仍然不完美，但这一技术的方向无疑是正确且具有前瞻性的，期待未来的优化与表现。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWk63WInibYqv5eurbOzDXK95PFxEYlPRSJHYG7l2vt2FoRI9f34TWe6T2vmKBYKp61KuFBmmxwezw/0?wx_fmt=png)

安全引擎

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yjc5YCCspxWk63WInibYqv5eurbOzDXK95PFxEYlPRSJHYG7l2vt2FoRI9f34TWe6T2vmKBYKp61KuFBmmxwezw/0?wx_fmt=png)

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