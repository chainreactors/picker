---
title: 研究：TPUXtract 方法可盗取AI模型
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521806&idx=2&sn=7599640b4a6a607a6a9660733bbfec0c&chksm=ea94a764dde32e72a56f57c61e9b7dc479e887404e412eec4bf2a3d28b23333c76a958b11b52&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-17
fetch_date: 2025-10-06T19:40:12.681015
---

# 研究：TPUXtract 方法可盗取AI模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQfeiciaZuzYkmpK6lGIdr6fatakq2y19m1vWGbj9Xgfy2eIyiaNBlaozj1yM0DBsxv5BqAhDQlKiaGsQ/0?wx_fmt=jpeg)

# 研究：TPUXtract 方法可盗取AI模型

Nate Nelson

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**研究人员展示了如何利用从运行神经网络的芯片中发出的电磁信号，重建一个神经网络。**

这种方法被称为 “TPUXtract（张量提取）”，由美国北卡罗来纳州立大学的电子和计算机工程学院研发。来自该学院的四名人员组成研究团队，通过价值数万美元的设备和一种名为 “在线模板构建”的新型技术，设法推断出在谷歌 Edge 张量处理单元 (TPU) 上运行的卷积神经网络 (CNN) 的超参数，准确率达到99.91%。

在实践中，TPUXtract 可使不具备初始信息的网络攻击者窃取AI模型：他们能够完全重建一个一模一样的模型并保存被实际训练的数据，从而盗取智慧财产或实施更多的攻击活动。

**TPUXtract 如何重建AI模型**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQfeiciaZuzYkmpK6lGIdr6faKF47pVDfU9BV4UMXynyrNTCZIrtic9VIcokoBqFpS6ODUt9d7K5oKibQ/640?wx_fmt=gif&from=appmsg)

该研究在 Google Coral Dev Board （在微型设备上开展机器学习的单板微型计算机）上开展：如边缘、物联网、医疗设备、汽车系统等。具体而言，研究人员关注的是该板的Edge TPU，即作为设备核心的专用集成电路 (ASIC)，可使其有效运行复杂的机器学习任务。

任何类似的电子设备，作为操作的副产品，将会发出电磁辐射，而电磁辐射的性质将会受它所执行的计算影响。为此，研究人员在TPU上放置电磁探探针进行实验（清除降温风扇等障碍），并以散发最强电磁信号的芯片部分为中心。之后，他们将计算机输入数据发送给该机器并记录了所泄露的信号。

在理解这些信号时，研究人员发现，在任何数据被处理前，神经网络会量化（压缩）其输入数据。只有当数据处于适合TPU的格式时，芯片中的电磁信号才会发出，说明计算开始进行。此时，研究人员可开始映射模型的电磁签名。但是，要同时估测组成该网络的所有数十或数百个压缩层本来是不可能做到的。神经网络中的每一层都会有一些特征组合：它将执行某种计算类型、拥有某数量的节点等。重要的是，“第一层的属性影响‘签名’，或第二层的侧信道模式”。因此，尝试理解第二层或第十层或第一百层的内容变得越来越不可能，因为它依赖于在它之前的所有属性。

研究人员提到，“因此，如果存在’N’层，而每层的组合数是’K’，那么计算成本可能是N的K次方。”研究人员研究了第28层到242层的神经网络，并估测K（即任何既定层的可能配置总数）为5528。

他们发现，不必提交无限算力解决该问题，而是可以隔离并分析每层。为了重建神经网络的每层，研究人员构建了“模板”即数千个模拟的超参数组合，并读取处理数据时发出的信号。接着，他们将获得的结果与尝试预测的模型发出的信号进行对比。最接近的模拟就被认为是正确的。之后将同样的流程应用到下一层。研究人员提到，“在一天之内，我们完全能够重建一个神经网络，而如果由开发人员开发，则需要数周或数月的计算。”

**AI模型被盗导致知识财产问题**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQfeiciaZuzYkmpK6lGIdr6faKF47pVDfU9BV4UMXynyrNTCZIrtic9VIcokoBqFpS6ODUt9d7K5oKibQ/640?wx_fmt=gif&from=appmsg)

完成TPUXtract 方法并非易事。除了需要具备大量技术知识外，该流程还需要多种昂贵且小众的设备。

研究人员使用一个机动XYZ表的Riscure 电磁探针台扫描芯片表面，通过高敏感的电磁探针捕获微弱的无线信号。Picoscope 6000E 示波器记录踪迹，Riscure icWaves 现场可编辑门阵列 (FPGA) 设备实时对齐，而icWaves 收发器使用带通滤波器和AM/FM解调来翻译和滤除无关信号。

虽然对于个人黑客而言，这种方法难度较高且花费大，但研究人员提到，“竞对公司如想要这么做，几天就可以办到。例如，一个竞争对手想要开发ChatGPT的仿本，但不想做所有工作，那么他们就能通过这种方法节省大量费用。”

尽管如此，盗取知识财产只是人们想要窃取AI模型的一个潜在原因。恶意对手可能还能通过观测控制热门AI模型的旋钮和表盘中获利，探测其中的网络安全漏洞。

对于那些雄心勃勃的读者，研究人员还提到了四项专注于窃取常规神经网络参数的研究。从理论上来讲，这些方法再加上 TPUXtract 就可重建任何AI模型，即其中的参数和超参数。

为对抗这些风险，研究人员建议AI开发人员通过无意义操作在AI推断流程中引入噪音，或者同时运行随机操作，或者在处理过程中将层的顺序随机化来混淆分析。研究人员提到，“在训练过程中，开发人员必须插入这些层，而该模型应当被训练到知道不必考虑这些噪音层的程度。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Ultralytics AI模型正被劫持用于部署挖矿机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521726&idx=1&sn=6242710e1abb2954dfd85acd30c4ffb1&scene=21#wechat_redirect)

[研究员在开源AI和ML模型中发现30多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&scene=21#wechat_redirect)

[ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&scene=21#wechat_redirect)

[英特尔披露 AI 模型压缩软件中的严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519528&idx=1&sn=9ed9dbdab8ecbf2108523342f0297d50&scene=21#wechat_redirect)

[开源代码库 TorchServe 中存在多个严重漏洞，影响大量AI模型代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517813&idx=3&sn=2547a20df3df5050c23af50502f6658d&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/vulnerabilities-threats/tpuxtract-attackers-steal-ai-models

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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