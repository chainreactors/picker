---
title: 跨层残差绕过LLM内生安全
url: https://mp.weixin.qq.com/s/xPTz3Id-e5mgpCGKjB-btg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:09:20.973177
---

# 跨层残差绕过LLM内生安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7libzb7or0pAhZJ4Af7LaTia80n22DrdOXqwpQcp0tcMWDcuZQPx8ZjAKMbcZKnFfxaZoicwDHbD5gibJEksdCe3Bcef6qwoa5NMA0/0?wx_fmt=jpeg)

# 跨层残差绕过LLM内生安全

原创

Holiday
Holiday

联想全球安全实验室

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

**一、传统白盒越狱**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dYyA3er8jiaibnSsyZwic136Um7ic8ribwg45Eu1zLaHyEOjbticTjufgh7YibZrZnSVJdqA7OYpfe1yCmvL3mkz2fzvw/640?wx_fmt=png)

**贪婪坐标梯度法（GCG）**：将越狱建模为离散优化问题，利用模型梯度搜索一段对抗性后缀。做法是评估 字符/Token 替换对损失或目标输出概率的影响，采用贪婪式坐标更新不断提升越狱成功率；但生成结果常是无意义“乱码/乱序 Token”，容易被基于困惑度等简单过滤策略拦截**。**

**AutoDAN：**引入遗传算法与结构化变异，在尽量保持语义连贯的前提下做对抗优化（词级变异、句级交叉等），生成更像“正常文本”的攻击指令；同时出现混合式思路（如结合 GCG 与自动迭代模板的策略），但 AutoDAN 仍常依赖初始模板、计算开销较大，并且在无法访问概率分布/梯度信息的黑盒场景中适用性受限。

![](https://mmbiz.qpic.cn/mmbiz_gif/z7JJtd2SEucqpJMgAz6yyn0VVfJ2USz82QqmP91hibhyicdLmLUu4HLurUSTBI1abkoD7os8AH8AUzWUqxF8jkwg/640?wx_fmt=gif)

**二、LLM机制可解释性研究**

在白盒攻击中，精确定位模型内部负责安全过滤的关键层，是实施高效干预的前提。但在标准的 Transformer 实现里，研究者通常更容易拿到输入和输出；要稳定获取中间激活、精确定位到“某一层/某一处张量”，并在前向过程中进行可控干预，工程成本往往较高。为了解决这类“可观测、可干预性不足”的问题，可以借助 TransformerLens 这类面向大模型机制可解释性研究的工具。

TransformerLens 的核心是 HookedTransformer：它基于 PyTorch 的 hook 能力，在模型关键计算位置插入可命名的 HookPoint，从而在前向传播中捕获并缓存关键中间激活（如注意力模式、MLP 输出、残差流等）。

以 "The capital of France is" -> "Paris" 为例，TransformerLens 以词嵌入与位置嵌入作为残差流起点，并在每层分别提取注意力与 MLP 对残差流的写入（attn\_out、mlp\_out），将其堆叠为形如 [组件数, 批次, 位置, d\_model] 的张量。随后将目标 token "Paris" 映射为残差空间的方向向量，并用缓存的归一化缩放因子做尺度校正；最后对每个组件与该方向做点积，得到其对 "Paris" 对应 logit 的贡献度，数值越大表示该层（或该组件）对预测 "Paris" 的推动越强。

下图是一个demo实验结果，观测Qwen3:8B模型，得出27层对于"Paris"结果的贡献度可能最大：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7lgEqVSnia9zSM1wCbjtGyWnWjkHHhkJ3EGzlwIFXtxed5S0gL4ekWZKAibuCQFGPCzsXAFOBoEy4jPjkj3Nriaqzg8scVqTJm6x4/640?wx_fmt=png)

**三、SABER攻击方法：**

**跨层残差绕过安全对齐**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dYyA3er8jiaibnSsyZwic136Um7ic8ribwg45Eu1zLaHyEOjbticTjufgh7YibZrZnSVJdqA7OYpfe1yCmvL3mkz2fzvw/640?wx_fmt=png)

**SABER**（Safety Alignment Bypass via Extra Residuals）是来自印度理工学院德里分校的研究团队在2025年提出的一种新型白盒越狱方法，该方法通过跨层残差连接绕过了LLM的内生安全，提高了攻击成功率。

目前全网还没有人复现，感觉挺有意思的，结合TransformerLens 尝试能不能复现。

【原理】

 1、 加载模型并包装 Hook 机制，利用 PyTorch 的 register\_forward\_hook在前向传播时抓取该层输出Transformer 每层的隐藏表示（残差流输出）。

2、用 Activation Patching 找到防御层，是把“良性prompt”和“有害prompt”看作两条不同的内部计算轨迹：先记录良性提示在各层产生的中间表示，然后在评估有害提示时，逐层把某一层的中间表示替换为良性对应层的表示，并观察模型输出的行为指标（例如，更偏向拒答还是更偏向继续回答）发生了多大变化；如果某一层的替换会引起最大的行为转向，说明该层对安全相关行为最敏感，可作为后续分析与加固的重点对象。

然后提取源层激活作为对照信号，在模型处理同一输入时读取该源层的中间表示（激活向量）。

3、注入攻击：提前配置好不同组的干预幅度、源层与防御层的相对距离、后缀注入提示词。选定一组“源层/目标层”作为实验配置；随后对同一输入运行一次前向计算以获取源层的中间表示，并构造一个干预函数用于在目标层对激活进行受控修改；接着把该干预函数注册到目标层对应的激活位置，再运行一次生成过程并记录输出变化；最后统一清理所有 hooks 与缓存，确保每次实验相互独立、可重复对比。

【实验结论】

这里的测试对象分别选用了： Qwen-1\_8B-Chat（弱逻辑模型）、DeepSeek-R1-Distill-Qwen-32B（思考能力强逻辑模型）、Qwen3-30B-A3B-Instruct（MoE架构模型）。

下图是程序运行的结果，可以发现安全对齐权重大的层都是在最后的几层，这和SABER论文中在中间位置的结论是有区别的，因为当时的模型都是2024年发布的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0UKPAuBeu7m1fNQN7iaUtef97LutXibupGMoc6YEAWxCUl3XQchTUeWVn4iaejGONuFZVn9xShUaT3BKlfxJs1emZ1WCTFQjOqpUM3GicMyGicBM/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mJes8riag1jpXnvCOicNZAsng1k7BPs0PM3r41Anb6oicLf4YAXwpJ7ro4CLA4s1JKonC9FiaP80e5yHOOxvNYOuBwY4KyLXodC2s/640?wx_fmt=png)

【风险】

**1、绕过内生安全机制：**诱导模型生成本应拒绝的有害/毒性内容。

**2、推理包装器滥用：**在私有化部署中无需改模型文件，仅通过外层脚本劫持推理流程即可输出不合规内容。

**3、定向投毒/微调：**定位关键层后冻结其余层、仅微调目标层以降低拒答，但易产生过拟合与行为漂移风险。

![](https://mmbiz.qpic.cn/mmbiz_gif/z7JJtd2SEucqpJMgAz6yyn0VVfJ2USz82QqmP91hibhyicdLmLUu4HLurUSTBI1abkoD7os8AH8AUzWUqxF8jkwg/640?wx_fmt=gif)

**四、防御方案**

**1、模型来源与完整性校验**：只使用可信来源模型，做完整性校验。

**2、防推理过程被 Hook 劫持/滥用**

**•** 激活异常检测：在推理服务中监控关键层激活的范数/方差变化，出现非自然突增则告警或中断。

**•** 代码/运行时完整性：在受控环境禁用或审计动态 hook 行为（如阻止注册 forward hook、限制运行时反射），并对推理进程与依赖做权限隔离与可观测审计。

**3、模型层级加密（联想全球安全实验室专利）**

对模型结构进行分析，定位安全相关或关键贡献的目标层，并按加密策略对这些目标层进行加密保护，从模型文件分发与部署环节提升关键层参数/结构的安全性，降低被篡改或被恶意利用的风险。

**（专利：CN120541862A《模型加密方法、数据处理方法和电子设备》，公开日 2025-08-26；发明人 Conna He）**。

**参考文献**

reference

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dYyA3er8jiaibnSsyZwic136Um7ic8ribwg45Eu1zLaHyEOjbticTjufgh7YibZrZnSVJdqA7OYpfe1yCmvL3mkz2fzvw/640?wx_fmt=png)

【1】TransformerLens. TransformerLens 文档（v2.16.1）：生成式语言模型的机械可解释性库 [Web Page]. 检索于

https://transformerlensorg.github.io/TransformerLens/

【2】Joshi, M., Nandi, P., & Chakraborty, T. （2025 年 9 月 19 日）. SABER：基于跨层残差连接的安全对齐漏洞挖掘. arXiv. https://doi.org/10.48550/arXiv.2509.16060

![](https://mmbiz.qpic.cn/mmbiz_gif/z7JJtd2SEucqpJMgAz6yyn0VVfJ2USz82QqmP91hibhyicdLmLUu4HLurUSTBI1abkoD7os8AH8AUzWUqxF8jkwg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7JGQtVQ4Ilu1djlUIqz0NlpKO3BgxPAZEcYHKShQu4nNtVUwUyVfUCNFXurUBhRiaPYnFptpFTbiaZmp4s7SUvibA/640?wx_fmt=gif)

**往期精彩合集**

●[模块化机房建设踩坑纪实](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493543&idx=1&sn=444f0e8922c8968fc3447dc38f154215&scene=21#wechat_redirect)

●[App 接口安全：被低估的系统安全边界](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493510&idx=1&sn=5cac29cd413f33b84d74e7e0946ff37d&scene=21#wechat_redirect)

●[从 XSS 到 RCE：Electron 应用中的真实攻击链](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493436&idx=1&sn=06457e0fc73b9a16493921008063c84d&scene=21#wechat_redirect)

●[小心你的路由器 —— UPnP 协议分析](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493424&idx=1&sn=199b5933ea6cd2bd29dde05e3419f7ca&scene=21#wechat_redirect)

●[从开发视角看：Android App代码混淆进阶方法](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493314&idx=1&sn=3978f2e63baea1cd474534c5c167303b&scene=21#wechat_redirect)

**长**

**按**

**关**

**注**

联想GIC全球安全实验室（中国）

chinaseclab@lenovo.com

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0UKPAuBeu7lEfROXH717MiaCjUKOtXCSWd4RFcLGIKWzJHoGv5KwuoUejmLaHh6Uza2H4vJCHUg437KLVTicud6JfwHFaaoOB8sGDc9E6ULnw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

联想全球安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

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