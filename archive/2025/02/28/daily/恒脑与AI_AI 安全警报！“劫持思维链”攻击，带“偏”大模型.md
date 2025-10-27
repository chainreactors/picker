---
title: AI 安全警报！“劫持思维链”攻击，带“偏”大模型
url: https://mp.weixin.qq.com/s?__biz=MzI1MDU5NjYwNg==&mid=2247496715&idx=1&sn=40e0b437daf97524ac82e20ffa754709&chksm=e9fd699ade8ae08ccfa47e86b0d733b6c93a843aa760d0c47d2a3e65a5d603e0da09a0246fa5&scene=58&subscene=0#rd
source: 恒脑与AI
date: 2025-02-28
fetch_date: 2025-10-06T20:38:55.941371
---

# AI 安全警报！“劫持思维链”攻击，带“偏”大模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vBt6OmTmXXCl5RuEskwKaWicIXaI6OiaJVUb7hraj7TDKcF2GByF4y6a2GuE4B9bCianzUgsRa7AmBXY553HoqBVw/0?wx_fmt=jpeg)

# AI 安全警报！“劫持思维链”攻击，带“偏”大模型

AI前沿

恒脑与AI

**文末附报告链接**

当你和 AI 助手愉快聊天、让它帮你出谋划策时，有没有想过它可能被 “带坏”？最近，杜克大学、埃森哲和台湾国立清华大学的研究团队，揭示了大型推理模型（LRMs）存在严重安全漏洞，还提出了一种可怕的 “劫持思维链”（H-CoT）攻击方法 。

![](https://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXCl5RuEskwKaWicIXaI6OiaJVQxJvZ1P1sj8l41lJX4VHVEFPhXKjrDLqicjK2SDxmBGh6RkDco6Y5OA/640?wx_fmt=png&from=appmsg)

**一、大模型思维链****推理机制**

如今，OpenAI 的 o1/o3 系列、DeepSeek-R1 和谷歌的 Gemini 2.0 Flash Thinking 等大型推理模型，凭借强大的推理能力，在各种复杂任务中表现出色，被广泛应用。为了平衡模型效用与内容无害性，它们大多采用思维链（Chain-of-Thought, CoT）推理机制进行安全决策。

**简单来说，就是模型在生成回答前，会像人一样 “思考” 一下，判断内容是否安全。可这个看似坚固的安全防线，真的无懈可击吗？**

研究团队构建了 “恶意教育者”（Malicious-Educator）数据集，模拟各种具有极端危险或恶意意图的请求，就像给模型出了一堆刁钻的 “安全考题”。结果令人大跌眼镜，这些模型在安全推理机制上存在严重漏洞 ，面对恶意请求时，表现得十分脆弱。

**二、什么是“劫持思维链”，**

**大模型如何被 “带偏”？**

**劫持思维链”（H-CoT）攻击**

是一种针对大型推理模型的新型攻击方法。它通过操纵模型的中间推理过程，绕过内置的安全检查机制，使模型从谨慎拒绝有害内容转变为积极提供有害信息。

正常情况下，模型会通过思维链推理来判断请求是否安全。比如你问 “如何制造炸弹”，模型会在思维链中分析这是危险有害的内容，从而拒绝回答。

但在 H-CoT 攻击下，攻击者会巧妙地修改模型的思维过程。他们先把原始恶意请求替换成较弱变体，诱导模型生成一个看似正常的执行阶段思维过程，然后把这个片段注入到原始输入中。**比如请求可能会将勒索软件的创建描述为“专业网络安全培训”。**模型就像被误导的孩子，跳过了安全判断环节，直接进入执行阶段，生成有害内容 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vBt6OmTmXXCl5RuEskwKaWicIXaI6OiaJVvZ8AFPGKD9kBnmbO5KWoHTm7WXTMYib4lPbgPXBwQRPH8y61ML9XoIA/640?wx_fmt=jpeg&from=appmsg)

举个例子，原本模型对 “如何进行金融诈骗” 的请求拒绝率高达 98%，但在 H-CoT 攻击下，拒绝率骤降至 2% 以下 ，轻易就被攻击者 “牵着鼻子走”。

**三、攻击带来的连锁反应**

**01安全机制失效**

H-CoT 攻击直接绕过了模型内置的安全检查，让模型的安全机制如同虚设。这意味着，我们以为安全可靠的 AI，在黑客面前可能毫无招架之力，随时可能泄露有害信息，对个人、社会造成严重危害。

**02模型更新的潜在风险**

为了提升性能和降低成本，模型会不断更新。但研究发现，模型更新可能无意中削弱了安全性。比如 OpenAI 的 o1 模型，在面对来自 DeepSeek-R1 的竞争时，为了提高推理性能和成本效率，更新后的安全性有所下降，这也给攻击者留下了可乘之机 。

**03多语言和地理定位攻击的隐患**

不同语言和地理位置的用户，可能面临不同程度的安全风险。实验表明，通过 VPN 代理进行地理定位攻击，欧洲 IP 的脆弱性比美国端点高 15% 。而且，多语言不一致性也会被攻击者利用，比如英语查询绕过了中文安全过滤器，攻击成功率提高到 96.8% 。

**04生成后审核机制的缺陷**

一些模型的生成后审核机制也存在问题，拒绝率仅为 20%，而且在安全过滤器介入前，还会短暂输出有害内容。在 H-CoT 攻击下，拒绝率更是进一步下降至 4% 。

**四、如何应对这场 AI 安全危机**

**①避免显示安全推理过程**

全面隐藏模型安全推理过程信息，防止攻击者利用这些信息操纵模型。如 OpenAI 在 o3 - mini 网页版对危险查询思考过程的处理。

**②强化对模仿 H-CoT 攻击的防御**

核心问题在于模仿的 H-CoT 劫持了危险的思维过程，更有效的解决方案是将查询中与思维链（CoT）相关的提示与核心请求分离。如果核心请求是安全的，可以添加 CoT 相关提示进行处理；然而，如果核心请求是危险的，查询中的 CoT 相关提示应被排除在输入之外，以避免劫持模型的安全推理。

**③增强训练过程中的安全推理能力**

H-CoT 攻击凸显大模型安全对齐挑战，需要更先进的训练方法和高质量数据集，深入理解用户意图，避免陷入恶意逻辑陷阱。

**④避免因当前效用竞争而忽视安全**

推理模型发展不应因追求推理性能和降低成本而忽视安全。像 OpenAI 的 o1 模型、DeepSeek-R1 和 Gemini 模型都存在安全问题，未来发展应将安全与效用并重，企业需重视两者平衡 。

**⑤部署大模型内容安全防火墙：**考虑到大量模型应用者并非模型训练者，缺乏从训练层面增强模型安全性的能力，建议广泛部署大模型内容安全防火墙。这类防火墙可在模型输入输出环节实时监测和过滤数据，阻挡恶意请求、识别潜在有害内容，在应用层面为模型提供额外安全防护，有效降低 H-CoT 等攻击风险，保障模型安全稳定运行。

**报告链接**

《H-CoT: Hĳacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models, Including OpenAI o1/o3, DeepSeek-R1, and Gemini 2.0 Flash Thinking》

全英文版报告链接：

https://arxiv.org/pdf/2502.12893

![](https://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXCl5RuEskwKaWicIXaI6OiaJVllveBZXVgnkS6bneAicvxicgTiaLCIXaYv2BlvpUFgNIX8kdRKOWnZPJg/640?wx_fmt=png&from=appmsg)

**你有什么看法？欢迎在评论区留言分享你的观点！**

![](https://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXCl5RuEskwKaWicIXaI6OiaJVmp9xFDHsibUWU4MmUGf7bG5JhqT92NwBKQGI0YJ0qiaoia1yia5dPbr4ibg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB4teTJe4cicFkCR5yYmhkQl8GdM82NiciaujRc9tc5UREZboCcFzIbUF0KrqKWgRqdhQ5vmBUXR9bYw/0?wx_fmt=png)

恒脑与AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB4teTJe4cicFkCR5yYmhkQl8GdM82NiciaujRc9tc5UREZboCcFzIbUF0KrqKWgRqdhQ5vmBUXR9bYw/0?wx_fmt=png)

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