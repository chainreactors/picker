---
title: 是谁解决了AI大模型的关键技术，让其具备了推理能力？
url: https://mp.weixin.qq.com/s/-UFsY2fZMw4JLW2tESUthA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:59:31.783625
---

# 是谁解决了AI大模型的关键技术，让其具备了推理能力？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LZlV7oU8yGNgGsc9YR2ibm8sPic5WwWtF0gsic6RbdlHicRkvbiaMftwjkjjKPt61mpWFhiapUdxxDAPlBHyxh36As675Fvmb0jAjKDeNtsDVnXGs/0?wx_fmt=jpeg)

# 是谁解决了AI大模型的关键技术，让其具备了推理能力？

原创

JUN哥
JUN哥

君说安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3WYWmfDLDTqrW5PNAwrdyF8hD8H2dtYcaejKFPHJicJaxoAv7NXpDDcoz3AIg3S187nIib9khvj34dg/640?wx_fmt=jpeg)

****分享网络安全知识，提升网络安全认知！****

****让你看到达摩克利斯之剑的另一面！****

---

**“** 是谁解决了AI大模型的关键技术，让其具备了推理能力？**”**

![](https://mmbiz.qpic.cn/mmbiz_png/LZlV7oU8yGNOnSV2gBaic1bAV4yk51REE52H6Rms8VCm23topVXRS0utZxLajREYiaYlJwzKDxGjRa37uTa7lJlWbqhhesrC3aUS3en0LjAn0/640?wx_fmt=png&from=appmsg)

**备注：图片来源于网络**

---

大家好，我是Jun哥。

今天咱们介绍个冷知识，那就是AI大模型为什么能够呈现“思考力”关键能力。

今天，当我们用AI赋能各行各业，例如解决复杂的数学计算问题，规划旅游的出行路线，或者在某场CTF比赛中使用AI轻松挖取flag时......AI变得越来越聪明，已经到了可以取代部分人类的工作。

有时候，我一直在想，AI的这份“思考力”是否并非天生，那么又是谁破解了AI大模型的关键技术，让它从“鹦鹉学舌”的语言模仿者，蜕变为能逻辑推演、分析判断的“思考者”？

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  01 AI推理能力的诞生

要理解这个问题，咱们得先回到AI的“懵懂时代”。

Jun哥查阅了相关资料，早期的AI模型，本质上是“模式匹配的高手”。

比如，它能记住海量文本、图片数据中的关联，却无法理解背后的逻辑，或者它能背诵勾股定理，却不会用定理计算一个直角三角形的边长；疑惑它可以能生成看似连贯的代码，却无法排查代码中的逻辑漏洞。

这可以说是当时大模型缺乏“推理能力”的核心困境，即不能基于已知信息，通过逻辑推导得出未知结论的能力。

打破这一困境的，是2017年一篇里程碑式的论文《Attention is All You Need》，这篇论文提出的Transformer架构，彻底改变了AI处理语言和信息的方式，为推理能力的实现搭建了核心“骨架”。

而在这一架构的发明中，波兰计算机科学家Łukasz Kaiser功不可没，他既是这篇论文的核心合著者之一，也是Transformer架构的关键设计者。

在Transformer出现之前，AI处理序列信息（如语言、时间序列）依赖循环神经网络（RNN），但这种架构存在“记忆短板”，无法高效捕捉长文本中的逻辑关联，更难以进行复杂的多步骤推理。

而Transformer架构的核心创新机制即自注意力机制（Self-Attention），让模型能同时关注输入信息的所有部分，理清不同内容之间的依赖关系。

举个简单的例子，比如处理“因为下雨，所以地面湿了”这句话时，大模型能清晰识别“下雨”与“地面湿”的因果逻辑，而非简单记住这两个短语的搭配。

Łukasz Kaiser长期深耕深度学习基础研究，在谷歌大脑任职期间，他主导了注意力机制的核心研发，最终与团队共同提出Transformer架构。

这一架构不仅解决了长文本处理的难题，更重要的是，它为模型提供了“整合信息、梳理逻辑”的能力，成为后续所有具备推理能力的大模型（从GPT系列到Gemini系列）的基础。

因此，可以说：没有Transformer，就没有AI推理能力的后续突破，而Łukasz Kaiser的贡献，正是为这场革命奠定了第一块基石。

Transformer架构是大模型的“骨架”，当然仅有骨架还不行，还得有肌肉，即让大模型学会如何运用逻辑进行推理。

实现这一突破的，正是以OpenAI“波兰军团”为核心的科研团队。

其中Jakub Pachocki、Szymon Sidor等波兰裔研究者，成为推动AI推理能力落地的关键力量，功不可没。

Jakub Pachocki是OpenAI首席科学家，是GPT-4等核心模型的领军人物，也是强化学习（RL）与大模型结合的关键推动者。

他从2017年加入OpenAI后，主导了大规模强化学习与复杂博弈系统的研究，通过OpenAI Five（Dota 2）等项目，验证了“规模化训练引发能力跃迁”的这一核心认知。

此后，他带领团队将强化学习与大语言模型结合，提出了“基于人类反馈的强化学习（RLHF）”技术。

> RLHF技术，简单来说就是让模型先生成答案，再通过人类专家的反馈修正错误，不断优化推理逻辑，让模型逐渐学会“正确的思考方式”。

与Jakub Pachocki并肩作战的，还有Szymon Sidor，他也是OpenAI早期核心研究者，也是将强化学习引入大语言模型的关键人物。

他与Ilya Sutskever、Łukasz Kaiser共同合作，将强化学习技术融入模型训练，直接催生了后来具备强大推理能力的OpenAI o1模型。

而Szymon Sidor的核心贡献，就是让强化学习从理论走向实践，让模型的推理能力从“潜在”变为“可见”，当时OpenAI创始人奥特曼曾盛赞他：“不知疲倦，能解决看似不可能的问题”。

此外，OpenAI联合创始人Wojciech Zaremba、前研究副总裁Jerry Tworek等波兰裔研究者，也在推理模型的研发中发挥了重要作用。

Jerry Tworek领导了o1、GPT-4等早期推理相关工作，被业界誉为“大语言模型推理能力发展”的关键人物；

而Wojciech Zaremba则在模型训练体系搭建、代码推理能力优化上做出了重要贡献，推动模型从“理解语言”向“解决问题”跨越。

因此，这几个人组成的团队也被称为AI界的“波兰黑手党”，他们用工程化的思维，将基础研究与实际应用结合，让AI的推理能力真正落地。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  02 AI推理能力的进化

如果说Transformer架构和强化学习让AI具备了“基础推理能力”，那么谷歌DeepMind团队推出的Gemini 3 Deep Think，則让AI的推理能力实现了“质的飞跃”。

让AI学会“慢思考”机制，让推理能力达到人类专家级，对推理机制的颠覆性创新，这正是DeepMind团队致力的工作。

2026年2月谷歌DeepMind发布的Gemini 3 Deep Think版本，引入了“慢思考”（Slow Thinking）模式，彻底改变了AI大模型的推理方式。

Gemini不再追求“快问快答和快速生成答案”，而是像人类专家一样，进行多路径并行搜索、深度节点分析和自我修正，从而实现复杂任务的精准推理。

在Codeforces编程竞赛中，它达到全球第8名；在数学证明中，它能发现人类同行评审遗漏的漏洞；在ARC-AGI-2抽象推理测试中，正确率高达84.6%，远超此前的最佳水平。

这一突破的核心，是DeepMind团队设计的三大技术支柱。

一是慢思考模式、自我修正机制和成本效率优化。慢思考模式让模型同时探索3-5条解题路径，在关键决策点深入分析；

二是自我修正机制让模型在推理过程中实时检查逻辑一致性，发现矛盾时自动回溯调整；

三是成本效率优化则通过智能路径剪枝，将高质量推理的成本降低200倍以上，让深度推理从“实验室奢侈品”变为“可大规模商用的技术”。

Gemini 3 Deep Think的研发团队，汇聚了全球顶尖的AI研究者，他们借鉴认知科学中的双系统理论，将人类的思考模式融入模型设计，让AI从“概率生成器”重塑为“逻辑处理器”。

而后续推出的Gemini 3.1 Pro，更是在这一基础上迭代升级，推理性能达到上一代的两倍以上，进一步拓展了AI推理的应用边界。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  03 总结

除了上述AI研发核心团队和个人，AI大模型推理能力的突破，还离不开全球科研者的协同努力和技术的持续迭代。

从2015年到2025年的十年间，模型推理技术经历了从CPU手工优化到量子混合精度的革命性跃迁，加速倍数从10-50倍飙升至10万倍以上，功耗大幅降低，精度损失控制在0.1%以内，为推理能力的提升提供了强大的技术支撑。

在技术优化层面主要有三个突破。

首先是量化技术（QAT/PTQ）的突破，让AI大模型在降低精度的同时保留推理能力，让大模型能运行在手机等端侧设备；

其次是PagedAttention技术，它解决了内存碎片问题，提升了模型的并发推理能力；

再次是是推测解码技术，它用小模型辅助大模型推理，实现了速度与精度的平衡，是当前最为核心的突破。

这些技术的突破，来自全球多个科研团队的努力，华为昇腾、阿里MNN、腾讯NCNN等中国团队，也在端侧推理、量子加速等领域做出了重要贡献，推动中国从AI推理的跟随者跃升为领跑者。

回望AI大模型推理能力的发展历程，我们很难说“某一个人”解决了所有关键技术。

整个AI技术的发钻，从Łukasz Kaiser等研究者搭建的基础架构，到OpenAI“波兰军团”推动的强化学习落地，再到DeepMind团队创新的“慢思考”机制，也是全球无数科研者的技术迭代与协同攻坚。

没有哪一个突破是孤立的，没有哪一个贡献是微不足道的，正是这些力量的汇聚，才让AI从“模仿”走向“思考”，从“工具”走向“伙伴”。

如今，AI的推理能力还在持续进化，量子加速、自进化推理等技术的突破，正在让AI的思考变得更精准、更高效。

而那些幕后的科研者，依然在深耕细作、不断探索，他们或许不被大众熟知，但正是他们的智慧与坚持，一步步解锁了AI的“思考密码”，推动着人类文明向更智能的未来迈进。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  04 关于网络安全

当前AI智能体应用已经遍地开花，取代普通人类的工作只是时间问题，一项最新的统计数据显示，AI在未来能够取代60%以上的工作。

在网络安全行业，当前AI已经取代了30%的基础安全工作者，这也是各大网络安全企业降本增效裁员的基础线，即至少砍掉30%的基础性员工。

未来，网络安全行业的裁员比例还会更多，基础类员工至少消失50%以上，管理类员工至少会消失80%.

这绝不是危言耸听，这会让安全企业全面进入扁平化管理时代，甚至会出现一人公司，只有老板是真人，其他的可能都是AI。

当人类都被AI取代后，那么我们还能干什么？这是一个值得深度思考的问题，欢迎大家思索和探讨。

---

全文完，喜欢**请三连**，这对我**很重要！**

---

备注：

本文参考资料均来自公开科研文献、权威科技媒体报道及企业官方发布。

---

**-End-**

****免责声明：****本文相关素材均来自互联网，仅为传递信息之用。****

****如有侵权，请联系作者删除。****

---

**★****点赞，转发，设为星标**★

**与你一起分享网络安全职场故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

君说安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

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