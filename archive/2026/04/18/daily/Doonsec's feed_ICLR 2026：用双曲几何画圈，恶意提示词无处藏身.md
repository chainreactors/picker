---
title: ICLR 2026：用双曲几何画圈，恶意提示词无处藏身
url: https://mp.weixin.qq.com/s/cuzx3sQHd5OQgDhNl-y6oQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:25.253885
---

# ICLR 2026：用双曲几何画圈，恶意提示词无处藏身

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kEIzVCZlD8xtrqRcmnWpuklW8PNd6dFMocOzBtYsVuBduEDgadnYKGnsltDvQSnUTuwn1fZ0kP3iaFpic3NR2dxLC3KcQibAbgEXX9ibZrm0vCk/0?wx_fmt=jpeg)

# ICLR 2026：用双曲几何画圈，恶意提示词无处藏身

原创

AI安全观察
AI安全观察

鉴模

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

ICLR 2026接收的HyPE论文提出了一种新颖的恶意提示词检测方法——用双曲几何在语义空间中"画圈"，F1分数达0.98，且只需训练一个参数。这篇解读帮你看懂论文的核心内容。

**一、解决什么问题？**

当你让ChatGPT或Midjourney生成内容时，有些人会故意输入恶意提示词，比如让AI生成暴力、违法内容。如何自动识别并拦截这些恶意提示词？

现有方案有两个主流做法：

**1. 黑名单过滤**：维护一个"违禁词表"，输入包含这些词就拦截。问题：攻击者换个说法就能绕过，比如"暴力"改成"强力的"。

**2. 训练分类器**：用大量恶意样本训练一个AI来判断。问题：需要大量恶意数据，计算成本高，而且攻击者在embedding层面做手脚就能骗过分类器。

HyPE提供了第三条路：不需要恶意样本，只用良性数据训练，就能精准识别恶意提示词。

**二、核心原理：用双曲几何"画圈"**

**什么是双曲几何？**

想象一个漏斗形状的空间——越往边缘走，空间越"宽敞"。这种几何结构天然适合表达层级关系：比如"动物→哺乳动物→猫→橘猫"这样的分类，在双曲空间里可以非常紧凑地表示。

**HyPE的技术原理：**

论文的核心思想非常直观：

1. 把所有"正常提示词"映射到双曲空间
2. 在双曲空间里画一个"圈"（其实是超球体）
3. 新来的提示词，如果在圈里就是正常的，在圈外就是恶意的

这个"圈"的大小由一个参数决定——半径R。HyPE只需要学习这一个参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEIzVCZlD8xDedicXjgbXWibibbnQ5sSAicBst2X0z4w944pzCaCEsibm2XyC4jR8ElDVLacGTVETm1pLzWQNtsdQnibksX2UbSqDFb3rc1jul2qE/640?wx_fmt=png)

**上图解读：**这是论文的方法框架图。左边是输入的提示词，经过一个编码器转换成双曲空间中的点，然后计算这个点到中心的距离。如果距离大于半径R，就判定为恶意。整个系统只需要学习半径R这一个参数。

**为什么有效？**

关键洞察：正常提示词在语义空间里有很强的"聚合性"——它们围绕某些中心概念分布。恶意提示词则像"叛徒"，试图混进去但本质上属于"另一个世界"。双曲几何能清晰地刻画这种边界。

**三、实验验证：六个数据集全面测试**

论文在六个数据集上做了测试，涵盖不同类型的恶意提示词：

• **ViSU**：视觉安全相关提示词
• **MMA**：多模态攻击提示词
• **SneakyPrompt**：隐蔽的恶意提示词
• **COCO**：通用图像描述
• **I2P**：图像到提示词
• **NSFW56k**：不安全内容数据集

对比了五种现有方法：NSFW-Classifier、DiffGuard、Detoxify、Latent Guard、GuardT2I。

关键实验设置：**HyPE只用了ViSU数据集的良性样本训练**，然后直接在所有数据集上测试。

![](https://mmbiz.qpic.cn/mmbiz_png/kEIzVCZlD8zpibiaKaPhVcvx7FIcgRyXySjIQxr7jaSntS0mSjYicxSbLV47oDyJkMgbdUoGGzgT2qKc2xqVkD7ZWrxDFj5q1IkbNiaGs6F1aSg/640?wx_fmt=png)

**上图解读：**这是实验结果对比表。看最后一行HyPE的数据：ViSU数据集F1=0.98（接近完美），MMA数据集F1=0.95，即使是对抗攻击场景(adv-MMA)也达到F1=0.96。每一列都是最高分，显著超越其他方法。

**四、关键发现**

**发现一：单参数模型效果惊人**

对比其他方法动辄数百万参数，HyPE只学习一个参数（半径R），却达到了最优效果。这证明了方法设计的精妙——选对了几何空间，复杂度可以大幅降低。

**发现二：攻击绕过的代价极高**

论文设计了"自适应攻击"实验——攻击者知道HyPE的存在，专门针对性地调整提示词。结果发现一个有趣现象：

**攻击者要想成功绕过检测，必须把提示词改成"不再恶意"的内容。**

换句话说，攻击成功的代价是放弃攻击意图。这揭示了一个根本性的安全优势。

**发现三：跨语言泛化能力强**

在西班牙语、法语、意大利语数据上，HyPE的F1分数全部超过0.80。说明这个方法不依赖特定语言的特征，抓住了恶意提示词的本质。

**五、配套方案：如何净化恶意提示词？**

检测出恶意提示词后怎么办？论文提出了HyPS（Hyperbolic Prompt Sanitization）净化系统。

**技术原理：**

用一种叫"层级积分梯度"的技术，定位提示词中哪个词对"恶意判定"贡献最大。然后针对这个词进行处理。

**三种净化策略：**

**策略一：直接删除**
把有害词删掉。净化率最高（85%），但语句可能不通顺。

**策略二：同义词典替换**
查字典找反义词替换。比如"暴力"换成"温和"。净化率约75%。

**策略三：LLM智能替换**
用大语言模型(Qwen3-14B)生成语义相近但无害的替换。净化率65%，但语义保留最好（相似度0.82）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kEIzVCZlD8x4dutWXfxEfavHWnMf55ObFctw3iaGguiaWbWbfMoUotC5LicMGEbRthVSr96SExL7sSb1iaQLtvHToz8vGkxEuPy3UauD6KYIxHo/640?wx_fmt=png)

**上图解读：**可视化展示了双曲空间中正常提示词和恶意提示词的分布。可以看到，正常样本聚集成一个紧密的簇（在"圈"内），而恶意样本被清晰地分离在外面。边界清晰，这正是HyPE高效检测的原因。

**六、研究意义与局限**

**核心优势：**

• **轻量**：单参数模型，部署成本极低
• **数据高效**：只用良性数据训练，无需收集恶意样本
• **泛化强**：跨语言、跨攻击类型都表现优秀
• **安全性高**：攻击绕过的代价是放弃恶意意图

**存在局限：**

• 依赖预训练的双曲嵌入编码器(HySAC)，编码器质量影响最终效果
• 面对高强度、针对性的自适应攻击，性能会有所下降
• 净化后的提示词语义保留还有提升空间

**七、实践启示**

对于AI产品团队，这篇论文提供了几个有价值的思路：

1. **几何视角**：选择合适的数学空间（双曲 vs 欧氏）可以显著简化问题
2. **单类学习**：只用正常数据就能做异常检测，降低数据收集成本
3. **对抗设计**：让攻击成本高于收益，是更深层的安全思路

**论文信息**

论文：HyPE: Harnessing Hyperbolic Geometry for Harmful Prompt Detection and Sanitization
会议：ICLR 2026
arXiv：https://arxiv.org/abs/2604.06285
代码：https://github.com/HyPE-VLM/Hyperbolic-Prompt-Detection-and-Sanitization
项目：https://hype-vlm.github.io/

如果觉得有收获，欢迎**点赞**、**转发**支持，你的鼓励是我持续输出的动力。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kEIzVCZlD8yA1PJQqa6mjMLEcevtnmOBvzFkyf6zID5fibv3vdPGR63A90e6tNn82gBiaHXHWWGd3eIwEWkWbCahrcH2Gt0Vt2am4eeTTibFV8/0?wx_fmt=png)

鉴模

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kEIzVCZlD8yA1PJQqa6mjMLEcevtnmOBvzFkyf6zID5fibv3vdPGR63A90e6tNn82gBiaHXHWWGd3eIwEWkWbCahrcH2Gt0Vt2am4eeTTibFV8/0?wx_fmt=png)

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