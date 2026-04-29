---
title: 受邀国内头部技术峰会 | 网易智企专家带来内容风控垂直领域大小模型研发实践分享
url: https://mp.weixin.qq.com/s/BhYkYYsYaPkRidWzONbu9A
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:08:04.900167
---

# 受邀国内头部技术峰会 | 网易智企专家带来内容风控垂直领域大小模型研发实践分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ0joGelwLZibPUCTbibaiaN1p9dGPbCia5YicMOCzE6bXnBiabIaes912OoHjYYvqcg6qib2vfOh3diapHibcQkLYqbLfVkSCXysjMaLCeQMiap3wS7w/0?wx_fmt=jpeg)

# 受邀国内头部技术峰会 | 网易智企专家带来内容风控垂直领域大小模型研发实践分享

原创

AI驱动的
AI驱动的

网易智企-易盾

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，由极客邦科技旗下InfoQ中国主办的QCon全球软件开发大会·2026北京站圆满落地。本届大会以 “Agentic AI时代的软件工程重塑” 为主题，聚焦100+重磅议题，汇聚来自阿里、腾讯、网易、字节跳动、小米、百度等一线科技企业技术专家，围绕AI工程化、系统架构与研发模式演进展开深入探讨。

本次大会共吸引超2000位开发者，现场交流热烈、思想碰撞不断。网易智企·易盾业务算法专家胡宜峰受邀亮相「小模型与领域适配模型」专场，带来《面向内容风控垂直领域的大小模型研发实践》分享，与行业从业者共话前沿技术趋势与产业落地实践。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLa7lWyR6gZL0LTWibEQcY5GFry4p2mXG94D85x9MorR1bXzvBkeIg6QPsZ1MU506RaIdiaTp9sIFftQp0OQmcz7A5pUS23YuVUlg/640?wx_fmt=png&from=appmsg)

大模型代表了AI能力的上限，通过更大的尺寸、更多的数据追求更通用的能力。但在场景落地中，业内往往面临着精度不够、响应太慢、成本太高、隐私受限等问题。从业者们迫切希望，有经过领域适配后（Domain-Specific Model）的小尺寸模型（Small Language Model）在业务场景下做到“更快、更精、更专业”。

本次演讲结合了内容风控场景的实践，聚焦“精度、效率、成本、性能”核心问题，从“解决方案、模型、数据、部署”角度出发，充分结合大模型复杂场景理解能力强、泛化能力强、创造能力强的优势，同时结合小模型低成本低时延、定制敏捷、可控性高的特点，打造效果精准、实时响应、迭代敏捷、成本优化、稳定可靠的新一代数字内容风控系统。

以下为演讲全文整理：

---

大模型技术飞速发展，其在通用能力与泛化性上表现优异。然而在垂直领域落地时，小模型凭借低成本、低时延、高并发的优势，依然发挥着不可替代的作用。大小模型优势互补，协同发展是必然趋势。此外，随着Agent智能体的兴起，其核心在于实现大模型与局部工具之间的规划与联动，而小模型本身就是优秀的局部专家工具，恰好契合Agent时代对工具多样性的要求。因此，基于大小模型协同的技术架构，在垂直领域中正扮演着越来越重要的角色。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLY9Hs18MCI5bwt3QhayndQicibRnfg6874Vl9udbTlMOgN4Do4OqTUy6G3zE2QuxGvXfQ3DicKiaFbKuQ9v9KKGOX0vhNzO7nia3ED8/640?wx_fmt=png&from=appmsg)

大小模型协同的核心目标是取长补短、整合优势，构建覆盖解决方案、数据、知识、特征的全维度协同架构。在解决方案层面，小模型可作为大模型的前置节点，承接流量负载，实现高效引流；大模型也可通过Agent以MCP方式调用小模型，拓展能力边界与粒度。在数据、知识与特征层面，大模型利用其通用能力为小模型的领域拓展提供敏捷支撑，小模型则凭借深耕领域的专业能力反哺大模型，优化其领域适配效果。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLaLGF4R4m4pcrxHxa0iayZynXBXl3ycFCvlj8UPiahF1M8IVlnLSujVc5klTjQNagibfU68B21UBrsCwUg8FENeSMU2nvoLbY81dQ/640?wx_fmt=png&from=appmsg)

垂直领域模型研发的核心诉求，是实现精度效果、迭代效率、部署成本、运行性能的协同提升。具体而言：效果上需兼顾泛化性与局部最优，效率上支持敏捷迭代与增量更新，成本上控制数据与部署开销，性能上满足高并发与低时延要求。这些诉求正是大小模型协同架构的核心设计导向。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLY8xAAMxfZc6D3MJI4MiasX4v85jvPOUv2bAibKWBRLMzViaXwlZJhSCb56bXUTNTbicWIcbTMzn9oyGAOuP1dDwbrmEJIferuYXEQ/640?wx_fmt=png&from=appmsg)

在解决方案与效果层面，我们构建了“大模型赋能—小模型精进—双向反哺—协同落地”的阶梯式技术路径。第一阶段为大模型赋能，依托大模型的通用认知与泛化能力，快速补齐小模型的初始短板。通过多阶段蒸馏技术，将大模型的知识、特征与判断逻辑迁移至小模型，使其从泛化能力较弱的起点，快速具备扎实的基础能力。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLbVZRQyg8uylPQ0WwtjCWzbJ2SOYtoVXh3z98g8jyWkIDnCn6gqchDb2gak6KtKEzrFMBaPtYAjuuiaxzWEQHX2QnBwv9ficLpTA/640?wx_fmt=png&from=appmsg)

第二阶段为小模型精进，充分发挥小模型在垂直领域的深耕优势，基于半监督学习、对抗训练、难例挖掘等技术积累，进行定向优化与局部场景的极致打磨，将小模型提升至局部优秀水平。

第三阶段为双向反哺，借助PEFT高效微调技术，将小模型沉淀的领域专属知识与精准判别逻辑反向传递回大模型，修正大模型的领域偏差，使其同步达到优秀的垂直领域能力，实现大小模型的能力对齐。

第四阶段为协同落地，通过三级动态推理架构实现大小模型的深度融合，最终达成垂直领域的极致效果与极致性能。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLZqM2XrHbYcECbOZ0KCk3icDp4M13icIVRWQvMatDCiaFkdAXJnKCgVjUibkakvQ0kh7AOWqLCZfEu6EpkTqG5icHT2eo6ZF2LsjxFY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLaeK0ueQicqQ0qgX9bkHlBYPqNy4fficz1Kx38MAaicSy8MtiaHBaPBLuvCkaksLFVZicT8oz8nZVQPqk6m9B25WUI3Fpt7GFtiaMHYU/640?wx_fmt=png&from=appmsg)

数据层面的大小模型协同，是领域适配效果的重要支撑，也是数据成本的重要环节。覆盖数据生成、模型标注、人工标注完整数据周期。

基于AIGC的训练数据生成，核心是平衡多样性与准确率，即文本可控性与保真度的矛盾，需在保留核心属性的前提下实现样本多样化，我们基于Stable Diffusion构建三路生成范式，通过双路特征注入、CFG Scale平衡调节、能量噪声约束等创新，实现属性保真与样本多样的平衡，满足领域训练数据需求；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLajicZP4syYMRgrWbN4qHK8niaB1ANYkS9drO1OHg8SqTP43icf6ibmx2kBFo6Jn45OeibMDvmiaqfBviaHy5pUB6tSnIQy0jjIfA6pqY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLaEO5RjcA1nMiaEuF3SJ3My4gk05rlbrZqM0OBxcyyQKic7uIOGWJJPa1PL71yicnvYSj7KSibT4dicgOPARsvg1aXJZbQ6uaR8T8LQ/640?wx_fmt=png&from=appmsg)

模型标注层面，采用多模态半监督学习技术，充分挖掘无标签数据价值，降低标注依赖；人工标注层面，通过大小模型融合过滤，筛选高价值样本送入人工环节，提升标注效率与精准度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLZrQ29ZUFdpfYZLYwqo9duYSJ4HUbIicI4HSqZB09XCQ25psBLUjGUibhhAiazr3QW8iciaD4m6biaZWltWxYsb9iabollFBrv62WTSnI/640?wx_fmt=png&from=appmsg)

敏捷响应方面，内容风控领域对响应效率有极致要求，风险类型层出不穷，AIGC 生成与黑产对抗风险持续涌现，对敏捷响应能力有极高的要求，因此我们构建了轻量化敏捷迭代体系。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLa6qRzyJ29W8niacjo1ZzeTWjP6pjxicaBXkToNOzSNpz3hUY6ITvibJK2o37AtK9WsIKJCKDHGHO4J5ribUZJCw2uxXx8JzVltxvw/640?wx_fmt=png&from=appmsg)

核心思路包含三大技术点：一是属性感知特征描述，针对领域小众概念，通过CoT设计提炼精准描述特征让模型快速理解；二是多模态原型构建，基于小样本学习思想，构建视觉与文本原型的最优匹配路径，实现小样本快速适配；三是Attention机制优化，针对大模型幻觉的核心诱因（多模态特征未对齐、统计偏差），通过注意力机制改造强化特征对齐，从实操层面缓解幻觉问题，进一步提升领域适配稳定性。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLZTibv3YYg5gkaT5woMoXOibUV7UO2fweHvYnIJ0YicibcG2icIaCDafSicbADw2ia8xewM2sr8JVO5q8WNdKp7ZY3fw2xj6icRf1zT4icg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLYhE47ib717qDH3hglzBa6Hm7LfNf1MFt2lKUDbz4lm0w0V4bYJib4AlkhkoGdkhiaQaSMOZuXErlQsz3gzHgcDC1cQson3aUFGnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ0joGelwLb6f63pFR6kdy3cdsBx2zvj7W7nZ0HxgJ7eznmKPbcR5haJIfCqBAyQIGdx9YPr8oRwiaouUNjMub3ZUR1N9t79NG4ZG5Crricxs/640?wx_fmt=png&from=appmsg)

服务性能优化方面，基于内容风控场景数据分布极端不平衡的特点，我们进一步优化多级动态推理的大小模型协同框架，从模型、网络深度、尺度、token等维度，实现正常内容、简单违规内容、复杂违规内容的多级动态过滤。实现小模型承载规模、大模型提升上限的目标，从而实现效果与性能的同步优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLbjiaTBUib9z7ad5ugHP0OibKdibhCszo3qjzpNMjn4qMyvbvqGziawLCqzUBLtfqfZBicuScj3xgj37mbm7O3YHyS4of6qkqOiaFpauE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ0joGelwLah7XunWByNrvibJFyia5JkgoGxojmCcZ7acxCibF3NEEXeUrGg2AczbIXT7zcLOegWyFOAPDc60D4Y2libFdYd9q5IdoYcqgjVnfY/640?wx_fmt=png&from=appmsg)

综上，大模型时代，大小模型以全新的协同姿态成为垂直领域落地的核心支撑。大小模型协同架构，既发挥了大模型的泛化与通用优势，又保留了小模型的高效、低成本、领域精准特性，完美匹配内容风控等场景的效果、效率、成本、性能诉求。

未来，随着 Agent 技术与多模态技术的深化发展，大小模型的协同维度将持续拓展，从模型、数据、推理向部署、迭代、运维全流程延伸，成为垂直领域 AI 落地的重要范式，为产业智能化提供更高效、更灵活、更经济的技术方案。

---

🔻

AI 正在从「能用」走向「好用」，但技术落地从来不是单点突破，而是一场产业协同的远征。 如果你也在寻找 AI 与业务深度融合的真实路径，期待与千位企业决策者面对面碰撞，5月29日杭州，网易创新企业大会诚邀你现场见证、共创答案。

👇 扫码立即报名，锁定席位

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/0qAcsxd1gKuYoG3SI9HUHk5eCfNMIpzxVAWwlN0oicj0yHticOxkiaiaMcEBrbO3k0Liafo8VESsaoqNU23g499mfpazBHMmlaVuVbFcdhfJEPh0/640?wx_fmt=jpeg&from=appmsg&wxfrom=10005&wx_lazy=1&tp=wxpic#imgIndex=3)

**关于我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ehYgAEz05867UZvA9BFyUd2Q5lhRsLhMthibV04KzJj75WfFQLdTryeA722Va46ea0icm4NophAGm8KshrAicST3w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

**免费下载干货资料**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPISRj2RdNL4q9lHiaANKo7sDLgKDKycf3OuPtBXqFRwLINvrHoskRic69A/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&randomid=tmwg91d7&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPIuwlP0DOX5yqLP5USV9R8VU8v6REteETJ7PI9Y4AFlbPhQ44ibdlG6sA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&randomid=sirmeop4&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587IAXGp2Pc7rr0ZAJRlaxPIV6tLwsaX5QLEH6WCBqoQSHxm6gQo9DzWQyEibl0tCQX1eoDaTSZ9rUA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&randomid=5fx3ksfs&tp=webp#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zQ0joGelwLaDxwqX6u6fVmMiauya1icqNxt80lzRT1vribZjZRHvSAtBxF2228WEKpa95s3buDU2HibWaYUn94dsNecYPktZzDptoGGbZdnzVDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587KLs4PyHJbujWQ4n9h71kjWBeJbVBYGAY32CvtzFia8uejH1HIhSKSH7g1vLPMHgw12A7GI0xaDvQ/0?wx_fmt=png)

网易智企-易盾

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ehYgAEz0587KLs4PyHJbujWQ4n9h71kjWBeJbVBYGAY32CvtzFia8uejH1HIhSKSH7g1vLPMHgw12A7GI0xaDvQ/0?wx_fmt=png)

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