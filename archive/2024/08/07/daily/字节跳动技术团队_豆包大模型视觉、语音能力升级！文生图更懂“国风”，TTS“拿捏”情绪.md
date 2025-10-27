---
title: 豆包大模型视觉、语音能力升级！文生图更懂“国风”，TTS“拿捏”情绪
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508620&idx=1&sn=fb8b3695721a8aa8ab315d5e2fec4388&chksm=e9d3696edea4e078f0f8f6edce18bad2fb7b38042c726ba91d225f20618af460f7bab68f6d11&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-07
fetch_date: 2025-10-06T18:04:29.347538
---

# 豆包大模型视觉、语音能力升级！文生图更懂“国风”，TTS“拿捏”情绪

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjTBIR8PvBUMuXp0U8XbswPLNvrAu0CV2QP4HdsQLFTVkQTRXq2BsDcjGia3S0ia1icLHlLTqib3l2Cgg/0?wx_fmt=jpeg)

# 豆包大模型视觉、语音能力升级！文生图更懂“国风”，TTS“拿捏”情绪

豆包大模型团队

字节跳动技术团队

2024 火山引擎 AI 创新巡展・成都站于近日正式举办。活动现场发布了豆包・图生图模型，以及升级版的豆包・文生图模型、豆包・语音合成模型、豆包・声音复刻模型。

本文介绍了升级版文生图、语音合成、声音复刻模型特征，包括图像生成方面更深刻理解主客体关系、空间构造等特点，语音合成方面准确表达情绪、保留吞音、口音等能力。来自豆包大模型团队视觉、语音方向的同学还展望了未来文生图及语音合成方面的发展趋势。

日均 tokens 使用量突破 5000 亿——近日，2024 火山引擎 AI 创新巡展・成都站上，豆包大模型最新进展对外公布。一同发布的，还有豆包・图生图模型，以及升级版豆包・文生图模型、豆包・语音合成模型、豆包・声音复刻模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0Ahj3ECSBqotWrDjeU0uhmA8hniaC0dYdtQmZNryjibp1VrlebkHSYnug/640?wx_fmt=jpeg)

今年 5 月，字节跳动发布豆包大模型家族。据后续第三方 FlagEval 大模型评测平台发布的榜单显示，豆包大模型（Doubao-Pro-4k）在闭源大模型的“客观评测”中，以综合评分 75.96 分排名第二，仅次于 GPT-4 ，是得分最高的国产大模型。在“主观评测”中，豆包大模型同样排名第二。

2 个多月过去，平均每家企业客户日均大模型 tokens 使用量较发布时增长了 22 倍。爆发式增长的背后，也是豆包大模型模型能力和应用效果受到认可的体现。

**豆包大模型团队为本次发布的主要能力提供了技术支持，本文将介绍这些主要能力细节，解读背后涉及的技术内核。**

## **1.更懂“国风”的文生图模型**

本次文生图模型升级能力体现在三个方面：

**其一，****新一代模型能够深度理解复杂 prompt ，包括多主体、反现实、主客体关系等内容，图文匹配更精准。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0UECo31ag0fTWDTXiaosmTKDHOic6wr4q6oibURZUg1Uva5qYAgX68nMPg/640?wx_fmt=jpeg&from=appmsg)

> prompt：摄影作品，超现实主义，电影质感，一只超级巨大的猫咪，陆家嘴，超级可爱，躺在上海的街头，小汽车，猫咪和大楼一样高，和马路一样宽，堵住了马路，马路上很多车辆来来往往，汽车和猫爪一样大

**其二，模型也更善于从光影明暗、氛围色彩和人物美感三个方向提升画面质感。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiab5slKmn8za5jRgFbzL2H02I15wkOmBIZHV9bQt181ThZbibnmlmUWwLibpH0AyDPyPEN5O0p2vlFQ/640?wx_fmt=png&from=appmsg)

> prompt：大卫雕像，站在草地上，扔铅球的姿势，石膏材质，在现代奥运会场馆内，史诗般的构图，超精细，完美的光照

**其三，强化中国特色内容，能够对中国元素，包括中国人物、物品、朝代、地理、美食、节日等精准理解。**

团队认为，此次发布模型的“中国风”生成能力是最大亮点。我们使用了原生双语 LLM + 数据，实现了精准的中国元素生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0HYE25JpxicyhOQMTZu6wJEia3y58UiaJvTyhATQnH1eRWO4eEuuV8LVbQ/640?wx_fmt=png&from=appmsg)

> prompt：一个国风女孩穿着清朝的服装，眼神灵动，鼻子自然且好看，头上戴着黄金头饰，复杂的纹理，皇后，红色的袍子上面是龙和凤凰的刺绣，复杂的图案，珍珠项链，下雪，金色的指套，红色的大门和城墙

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0cj6E97GfL2kxFNclYU4xaEx4Xv9SlquRNstT2O1jPRaqKnHm4XA0iag/640?wx_fmt=png&from=appmsg)

> prompt：一个中国古代女侠，指向前方，侧身侧脸，表情凝重，中景镜头，风沙，（背后许多剑都朝手指的方向飞去：1.4 ），史诗般的构图，中式玄幻，细腻的皮肤，写实风格，景深，摄影艺术，极致的细节，阴影，电影海报，胶片噪点，低饱和度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0bw7c0PK7cCHM76LzUyNiagKCqIRRZXQNyTKn848icx98yw6OTRTyP4BQ/640?wx_fmt=png&from=appmsg)

> prompt：电影质感，摄影作品，哈苏，极简主义，意境构图，大面积留白，雾凇，一座苏州园林里，树梢挂满了雾凇，超高质量，超精细，最佳质量，禅意，东方意境

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0LnacNPqpSaiammJqogtcR0ziaodTewnHQsAmsZoscEneMDpjOcELH8Nw/640?wx_fmt=jpeg&from=appmsg)

> prompt：classic red and white，细线条，水墨写意，含苞待放的梅花上有落雪，天气极寒，一个穿着清朝斗篷的女人，在巨大的梅花树下斜倚着，吹笛子，忧伤的思绪，担心笛声会惊扰梅花

为使模型实现能力提升，团队进行了多方面准备。

在数据上，团队持续加强数据 Re-caption 能力，对数据进行精确打标以实现对数据质量更高把控。面向大批量数据进行管理和处理，团队还对训练集群稳定性也进行了优化。

文本理解模块，团队采用原生双语大语言模型作为文本编码器，显著提升对中文的理解能力。它能拥有更广泛的世界知识并对不同语言已经形成基础认知，换而言之，无论面对中文特色用语，还是英语俚语，语言模型都能提供更准确的 Text Embedding ，让模型能够精准的学习原始的文化元素。

部署推理方面，团队使用蒸馏方式，解决模型推理耗时问题，以实现在更低部署环境下，完成高质量的图片生成。从数据上看，他们将原有模型生成图像步数简化，消耗时长压缩到原有 40%。

最后，团队还规划了更全面、准确的维度以评价图片生成质量，其中包括：结构准确度、画质、图像美感、图文一致性、内容创造、复杂度适应性等。即便是同维度中，团队还会通过主体准确性、多主体准确性、动作数量等维度对生成效果进行评价。

除却文生图模型，本次发布还包含图生图模型，不仅能高度保留原图的人物轮廓、表情、空间结构等多维特征，还支持 50 余种不同风格，支持图片扩展、局部重绘和涂抹玩法，让图片进行创意延展。现已应用于抖音、剪映、豆包、星绘等应用，并已服务于三星、努比亚等企业，涵盖了手机相册、工具助手、电商营销、广告投放等多个领域。

## **2.让数据自己“说话”的语音基座模型**

**语音同样是本次发布重点，包括升级版豆包・语音合成模型和豆包・声音复刻模型。**

其中，语音合成模型能深度理解故事情节和人物角色，正确表达情绪，还能保留吞音、口音等发音习惯，媲美真人音色，让发声更自然。团队针对 26 个精品音色进行了更精细的把控，以支持各种细分场景下专业主播需求，落地方向包括现场主持、播音、直播等场景。

与之相对，豆包・声音复刻模型则支持 5 秒复制高保真音色，高度还原说话人声音特征和口音，支持跨 6 大语种迁移，发音更接近于当地人表达。这一模型面向于“学习任一角色声音”，复刻能力更好，甚至连说话人的口癖好也能学习到。

*注：声音复刻“太白金星”效果展示*

上述两个模型的底层技术，都关联[Seed-TTS](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247484723&idx=1&sn=37fe8f93d0f4bcd6df27411f9c85fe2f&chksm=c2772dacf500a4ba24b5fe6e84150136044644cc2147ed1e9cf20826d6e153eea2449cc32d44&scene=21#wechat_redirect)。

这是一个语音生成基座模型。与传统 TTS 面向单一任务不同，Seed-TTS 能够建模各种声音，且允许同时从很多个维度进行操控，比如方言，真人口癖，甚至吞字这类语音上的瑕疵。

至于大模型如何学习“吞音”、“口音”、“口癖”的原理，团队认为，传统的 TTS 使用特定建模，针对模型框架、模型时长、能量分布、音调分布进行设计，注入了人类的先验性，没能很好反映数据特征。但大模型能“让数据自己说话”。

本身大模型就拥有建模并提取大数据特征的能力，使得语音特征得以保留，再加上 RL 、数据增强、更好的文本标注、文本表征，强化了特定层面的表现。

比如“哈哈”二字，在不同语境有截然不同的意思和表达方式，Seed-TTS 可以通过上下文理解不同场景的意思，以学习到不同场景的对应表达方式。同理，TTS 模型也能实现深度理解故事情节和人物角色，正确表达情绪。

*注：语**音合成中更多情绪表达展示*

，时

具体实现方面，Seed-TTS 针对语言模型系统，主要解决了语音的 tokenize 和稳定性问题。

目前市面上，连续和离散的 tokenizer 都有，团队通过研究探索发现，token 包含信息的设计，对整个模型各方面表现及稳定性有非常关键的影响，这既包括 token 的信息、帧率等，也包括如何 tokenize ，以及如何将其再变回声音。

语言模型稳定性方面，团队在 token ，模型设计，解码策略，数据准备上进行了多方面的探索，真正做到了工业及应用的要求。

对于纯 Diffusion 系统，由于去掉了额外的时长模型，其难点同样集中在稳定性上。经过多方的尝试，团队在该链路也实现了很好指标。

研究工作外，为支持本次升级发布，豆包大模型语音团队还在算法层面进行迭代，包括增加可控性、表现力和稳定性。在工程上，团队参与降低了运算量，还与工程同学一起 Debug ，确保实际效果和 Demo 一致。

## **3.团队持续关注并致力于解决大模型底层问题**

回顾语音大模型领域发展，团队认为，传统 TTS 、ASR 等任务研究彼此分隔，落地到不同领域和场景中也相应要做适配和调整，随着大模型浪潮来临，各种任务从底层融合，才是大势所趋。

过去的研究显示，人脑学习语言和发音是通过经验和不断模仿，这一过程中，“听”与“说”两者同等重要，对机器也一样。

如果说 TTS 模型是机器的“嘴巴”，那 ASR 模型则对应“耳朵”，一个掌管发声，一个负责听见及理解，但两者的内核都依赖于对声音和文本信息的特征提取。

与之对应，豆包大模型团队在语音方向已经先后公布了 Seed-TTS、Seed-ASR 两个模型。其中，Seed-ASR 技术报告近期才对外披露，它能利用 LLM 丰富的知识，整体提升 ASR 识别结果的准确性，在多个领域、多种语言、方言、口音综合评估集上，Seed-ASR 比其他端到端模型表现出显著改进。目前，相关技术也已集成到豆包・语音识别模型中。

关于 TTS 模型和 ASR 模型的融合探索工作，团队已在进行中。

至于文生图方面的展望，豆包大模型视觉团队认为，Stable Diffusion 发布至今已过去 2 年，业内有很多新技术和插件涌现，比如 LoRA 、ControlNet 、Adapter ，也有 DiT 架构和更为强大的语言模型。团队透露，基于 DiT 架构的文生图 2.0 版本即将上线，新版本将比当前模型生成效果高 40% ，图文一致性和美感也有大幅提升。

同时，文生图领域目前仍有一些底层问题没有很好地被解决，也将是团队未来努力的方向。

一方面，模型对事件的理解能力需要进一步提升，具体来说，图文匹配能力，是文生图技术发展的核心。

另一方面，文生图需要更好的可控编辑生成能力，即便 ControlNet、Adapter，目前仍有缺陷，该问题的解决能为应用落地带来更广阔可能性。

最后是社会责任问题，文生图模型需要从公平性、安全性、消除偏见等方面进一步提升，以对社会公众更负责。

从文生图的 DiT 架构升级，到语音模型的“ All-in-One ”，我们希望持续吸引目标远大、有志于“用科技改变世界”的优秀人才加入团队，贡献创新性想法，并一同参与这些底层问题的解决与突破中。

**豆包大模型团队持续热招中，欢迎点击阅读原文，了解团队招聘相关信息。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugP4pgV3m4sm7iaL5YQKnwzVgzXsgicVupQ16FZVjotMEEWqjAnxM635ibmJrVpYDJMWT8H2KUQ1612w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiab5slKmn8za5jRgFbzL2H0ftghBFR6TrTqib86JVuUC6IHDe9jUNia0UuKjBMypyIvuFVibDlPYnPPg/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNeDAia52bianoHXZSqQ4APYI7dWibv3BLgy8uUrQicmhQH5FrGIvbQ6MBgg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247484993&idx=1&sn=10b3b6e1261b957de9391c72e7c401bc&chksm=c2772edef500a7c8c42314050204d2bbe2a45f2d22a37f8eaabdc65f9090f8a696610ce89e14&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESugoPxyC3kKz6FBQyu4XRwibNrBG9ibZePwWAia6l8ZkdbNpiaubKCPk0x1HahF0orWKOZJANicTnZ5SjFQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkzMDY5MzYxNg==&mid=2247484723&idx=1&sn=37fe8f93d0f4bcd6df27411f9c85fe2f&chksm=c2772dacf500a4ba24b5fe6e84150136044644cc2147ed1e9cf20826d6e153eea2449cc32d44&scene=21#wechat_redirect)

**点击“阅读原文”，了解团队招聘信息 ！**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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